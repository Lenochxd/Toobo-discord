import nextcord
from utils.languages import text

from utils.settings import daily

from utils.config import config
bot_owner = config.get('owner-id')


async def enable_auto_message(lang: str, message: nextcord.Message):
    if not message.author.guild_permissions.manage_guild and message.author.id != bot_owner:
        await message.reply(text('manage_guild_error', lang), mention_author=False)
        return

    success = daily.set_enabled(message.guild.id, True)
    
    if success:
        await message.reply(text('enable_daily_success', lang), mention_author=False)
    else:
        await message.reply(text('enable_daily_error', lang), mention_author=False)

async def disable_auto_message(lang: str, message: nextcord.Message):
    if not message.author.guild_permissions.manage_guild and message.author.id != bot_owner:
        await message.reply(text('manage_guild_error', lang), mention_author=False)
        return

    success = daily.set_enabled(message.guild.id, False)
    
    if success:
        await message.reply(text('disable_daily_success', lang), mention_author=False)
    else:
        await message.reply(text('disable_daily_error', lang), mention_author=False)


async def enable_auto_message_slash(lang: str, interaction: nextcord.Interaction):
    if not interaction.user.guild_permissions.manage_guild and interaction.user.id != bot_owner:
        await interaction.response.send_message(text('manage_guild_error', lang))
        return

    success = daily.set_enabled(interaction.guild_id, True)
    
    if success:
        await interaction.response.send_message(text('enable_daily_success', lang))
    else:
        await interaction.response.send_message(text('enable_daily_error', lang))

async def disable_auto_message_slash(lang: str, interaction: nextcord.Interaction):
    if not interaction.user.guild_permissions.manage_guild and interaction.user.id != bot_owner:
        await interaction.response.send_message(text('manage_guild_error', lang))
        return

    success = daily.set_enabled(interaction.guild_id, False)
    
    if success:
        await interaction.response.send_message(text('disable_daily_success', lang))
    else:
        await interaction.response.send_message(text('disable_daily_error', lang))
