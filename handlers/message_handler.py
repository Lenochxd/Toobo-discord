import nextcord

from utils.languages import text
from utils.settings import prefix
from utils.config import config

from commands.meteo import send_meteo
from commands.settings.set_prefix import set_prefix
from commands.settings.set_daily import set_daily
from commands.settings.enable import enable_auto_message, disable_auto_message

lang = config.get('default-language', 'fr')


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
            text('bot_mention', lang).replace('%prefix%', p),
            mention_author=False
        )
    
    
    if message.content.startswith(p) or message.content.lstrip('!').startswith(f'<@{bot.application_id}>'):
        message.content = message.content.removeprefix(p).removeprefix(f'<@{bot.application_id}>').removeprefix(f'<@!{bot.application_id}>').strip()        
        if not len(message.content) > 0:
            return
        command = message.content.split()[0].lower().replace('é','e')
        
        match command:
            case 'setup' | 'config' | 'configure' | 'heure' | 'daily' | 'time' | 'settime' | 'set_time' | 'set_daily':
                message.content = remove_command(message.content, ('setup', 'config', 'configure', 'heure', 'daily', 'time', 'settime', 'set_time', 'set_daily'))
                await set_daily(lang, p, message)
                
            case 'activer-toobo' | 'activer' | 'enable' | 'enable-toobo' | 'enabledaily' | 'enable-daily' | 'activertoobo' | 'enabletoobo':
                message.content = remove_command(message.content, ('activer-toobo', 'activer', 'enable', 'enable-toobo', 'activertoobo', 'enabletoobo'))
                await enable_auto_message(lang, message)
                
            case 'desactiver-toobo' | 'desactiver' | 'disable' | 'disable-toobo' 'disabledaily' | 'disable-daily' | 'desactivertoobo' | 'disabletoobo':
                message.content = remove_command(message.content, ('desactiver-toobo', 'desactiver', 'disable', 'disable-toobo', 'desactivertoobo', 'disabletoobo'))
                await disable_auto_message(lang, message)
                
            case 'prefix' | 'setprefix' | 'set_prefix':
                message.content = remove_command(message.content, ('prefix', 'setprefix', 'set_prefix'))
                await set_prefix(lang, message)
                
            case 'meteo' | 'get_meteo' | 'getmeteo' | 'show_meteo' | 'showmeteo':
                message.content = remove_command(message.content, ('meteo', 'get_meteo', 'getmeteo', 'show_meteo', 'showmeteo'))
                await send_meteo(lang, p, message)
                
            case _:
                print(f'Unknown command: {command}')