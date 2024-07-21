import json
import nextcord

from utils.languages import text
from utils.settings import prefix

from commands.meteo import send_meteo
from commands.settings.set_prefix import set_prefix

with open('config/config.json') as config_file:
    config = json.load(config_file)
    lang = config['default-language']
    

def remove_command(content: str, prefixes: tuple) -> str:
    for prefix in prefixes:
        if content.startswith(prefix):
            return content[len(prefix):].strip()
    return content.strip()


async def handle_message(bot, message: nextcord.Message):
    p = prefix.get(message.guild.id)
    
    if message.author == bot.user:
        return
    
    # Check if the message mentions the bot
    bot_mention = f'<@{bot.user.id}>'
    if message.content == bot_mention or (bot_mention in message.content.lstrip('!') and not message.content.startswith(bot_mention)):
        await message.reply(
            text('bot_mention', lang),
            mention_author=False
        ).replace('%prefix%', p)
    
    
    if message.content.startswith(p) or message.content.lstrip('!').startswith(f'<@{bot.application_id}>'):
        message.content = message.content.removeprefix(p).removeprefix(f'<@{bot.application_id}>').removeprefix(f'<@!{bot.application_id}>').strip()        
        if not len(message.content) > 0:
            return
        command = message.content.split()[0].lower().replace('é','e')
        
        match command:
            case 'prefix' | 'setprefix' | 'set_prefix':
                message.content = remove_command(message.content, ('prefix', 'setprefix', 'set_prefix'))
                await set_prefix(lang, message)
                
            case 'meteo' | 'get_meteo' | 'getmeteo' | 'show_meteo' | 'showmeteo':
                message.content = remove_command(message.content, ('meteo', 'get_meteo', 'getmeteo', 'show_meteo', 'showmeteo'))
                await send_meteo(lang, p, message)
                
            case _:
                print(f"Unknown command: {command}")
                