import nextcord

from utils.languages import text
from utils.settings import prefix
from utils.settings import lang as language

from commands.roll import roll_dice
from commands.settings.set_prefix import set_prefix
from commands.settings.set_guild_lang import set_guild_lang


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
            text('bot_mention', language.get(message.guild.id, message.author.id)).replace('%prefix%', p),
            mention_author=False
        )
    
    
    if message.content.startswith(p) or message.content.lstrip('!').startswith(f'<@{bot.application_id}>'):
        message.content = message.content.removeprefix(p).removeprefix(f'<@{bot.application_id}>').removeprefix(f'<@!{bot.application_id}>').strip()        
        if not len(message.content) > 0:
            return
        command = message.content.split()[0].lower()
        
        lang = language.get(message.guild.id, message.author.id)
        
        match command:
            case 'prefix' | 'setprefix' | 'set_prefix':
                message.content = remove_command(message.content, ('prefix', 'setprefix', 'set_prefix'))
                await set_prefix(lang, message)
                
            case 'setlang' | 'setlanguage' | 'lang' | 'language' | 'setserverlang' | 'serverlang' | 'set_serverlang' | 'set_server_lang' | 'setguildlang' | 'set_guildlang' | 'set_guild_lang' | 'guild_lang' | 'guildlang':
                message.content = remove_command(
                    message.content, ('setlang', 'setlanguage', 'lang', 'language', 'setserverlang', 'serverlang', 'set_serverlang', 'set_server_lang', 'setguildlang', 'set_guildlang', 'set_guild_lang', 'guild_lang', 'guildlang')
                )
                await set_guild_lang(lang, message)
                
            case 'roll' | 'dice' | 'diceroll' | 'rolldice' | 'dice_roll' | 'roll_dice':
                message.content = message.content.removeprefix('roll').strip()
                await roll_dice(lang, p, message)
                
            case _:
                print(f"Unknown command: {command}")
                