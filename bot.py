import nextcord
from datetime import datetime
from nextcord.ext import commands, tasks

from handlers.message_handler import handle_message
from handlers.slash_commands import register_slash_commands

from commands.meteo import get_meteo
from utils.settings import daily
from utils.languages import init as langs_init
from utils.languages import text
from utils.config import config
import utils.sql as db

langs_init()
db.init()

intents = nextcord.Intents.default()
intents.message_content = True


bot = commands.Bot(
    command_prefix=config.get('default-prefix', ';'),
    owner_id=config.get('owner-id'),
    intents=intents
)


@bot.event
async def on_message(message):
    await handle_message(bot, message)

register_slash_commands(bot)


@tasks.loop(minutes=1)
async def minute_loop():
    default_language = config.get('default-language', 'fr')
    for guild in bot.guilds:
        time = daily.get_time(guild.id)
        
        if time and time == datetime.now().strftime("%H:%M"):
            channel_id = daily.get_channel(guild.id)
            channel = bot.get_channel(channel_id)
            if channel and daily.is_enabled(guild.id) == True:
                try:
                    await channel.send(
                        await get_meteo(default_language)
                    )
                    
                except nextcord.errors.Forbidden:
                    # If sending to the channel fails, try to DM the guild owner
                    try:
                        guild_owner = guild.owner
                        if guild_owner:
                            await guild_owner.send(
                                text('meteo_daily_403_error', default_language).replace('%channel_mention%', channel.mention)
                            )
                    except nextcord.errors.HTTPException:
                        # If DMing also fails, we can't do much more
                        pass
                    
                except nextcord.errors.NotFound:
                    # If the channel doesn't exist, try to DM the guild owner
                    try:
                        guild_owner = guild.owner
                        if guild_owner:
                            await guild_owner.send(
                                text('meteo_daily_404_error', default_language)
                            )
                    except nextcord.errors.HTTPException:
                        # If DMing also fails, we can't do much more
                        pass



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    minute_loop.start()


if config.get('production', False) == True:
    bot.run(config['tokens']['main'])
else:
    bot.run(config['tokens']['test'])