import nextcord
from utils.languages import text, get_languages_info

from utils.settings import lang as language

async def set_guild_lang(lang: str, message: nextcord.Message):
    if message.author.guild_permissions.manage_guild == False:
        await message.reply(text('manage_guild_error', lang), mention_author=False)
        return
    
    new_lang = message.content
    
    lang_codes = [lang["code"] for lang in get_languages_info()]
    
    if new_lang not in lang_codes:
        await message.reply(
            text('set_guild_lang_error', lang).replace('%new_lang%', new_lang).replace(
                '%available_langs%', '`'+f'` {text("or", lang).strip()} `'.join(lang_codes)+'`'
            ),
            mention_author=False
        )
        return
    
    language.set_guild(message.guild.id, new_lang.lower())
    
    await message.reply(
        text('set_guild_lang_success', new_lang).replace('%new_lang%', new_lang),
        mention_author=False
    )


async def set_guild_lang_slash(lang: str, interaction: nextcord.Interaction, new_lang: str):
    lang_codes = [lang["code"] for lang in get_languages_info()]
    
    if new_lang not in lang_codes:
        await interaction.response.send_message(
            text('set_guild_lang_error', lang).replace('%new_lang%', new_lang).replace(
                '%available_langs%', '`'+f'` {text("or", lang).strip()} `'.join(lang_codes)+'`'
            )
        )
        return
    
    language.set_guild(interaction.guild_id, new_lang.lower())
    
    await interaction.response.send_message(
        text('set_guild_lang_success', new_lang).replace('%new_lang%', new_lang)
    )