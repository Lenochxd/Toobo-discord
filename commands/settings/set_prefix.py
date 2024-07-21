import nextcord
from utils.languages import text

from utils.settings import prefix


async def set_prefix(lang: str, message: nextcord.Message):
    if message.author.guild_permissions.manage_guild == False:
        await message.reply(text('manage_guild_error', lang),mention_author=False)
        return
    
    if '`' in message.content:
        await message.reply(
            text('prefix_wrong_char_error', lang).replace('%prefix%', message.content),
            mention_author=False
        )
        return
    
    if len(message.content) > 20:
        await message.reply(text('prefix_length_error', lang))
        return
    
    if len(message.content) == 0:
        await message.reply(text('prefix_empty_error', lang), mention_author=False)
        return
    
    
    prefix.set(message.guild.id, message.content)
    
    await message.reply(
        text('prefix_success', lang).replace('%prefix%', message.content),
        mention_author=False
    )


async def set_prefix_slash(lang: str, interaction: nextcord.Interaction, new_prefix: str):
    
    if '`' in new_prefix:
        await interaction.response.send_message(
            text('prefix_wrong_char_error', lang).replace('%prefix%', new_prefix)
        )
        return
    
    if len(new_prefix) > 20:
        await interaction.response.send_message(text('prefix_length_error', lang))
        return
    
    if len(new_prefix) == 0:
        await interaction.response.send_message(text('prefix_empty_error', lang))
        return
    
    
    prefix.set(interaction.guild_id, new_prefix)
    
    await interaction.response.send_message(
        text('prefix_success', lang).replace('%prefix%', new_prefix)
    )