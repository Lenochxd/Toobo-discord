import json
import nextcord
from datetime import datetime
from nextcord.ext import commands, tasks

from handlers.message_handler import handle_message
from handlers.slash_commands import register_slash_commands

from commands.meteo import get_meteo
from utils.settings import daily
from utils.languages import init as langs_init
import utils.sql as db

langs_init()
db.init()

intents = nextcord.Intents.default()
intents.message_content = True

def load_config():
    with open("config/config.json", "r") as f:
        return json.load(f)

config = load_config()


bot = commands.Bot(command_prefix=config['default-prefix'], intents=intents)


@bot.event
async def on_message(message):
    
    await handle_message(bot, message)

register_slash_commands(bot)


@tasks.loop(minutes=1)
async def minute_loop():
    for guild in bot.guilds:
        time = daily.get_time(guild.id)
        
        if time and time == datetime.now().strftime("%H:%M"):
            channel_id = daily.get_channel(guild.id)
            channel = bot.get_channel(channel_id)
            if channel:
                await channel.send(
                    await get_meteo(
                        config.get('default-language', 'fr')
                    )
                )

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    minute_loop.start()


if config.get('production', False) == True:
    bot.run(config['tokens']['main'])
else:
    bot.run(config['tokens']['test'])