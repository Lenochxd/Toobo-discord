import nextcord
from utils.languages import text

from utils.settings import daily

from utils.config import config
bot_owner = config.get('owner-id')

async def enable_auto_message(lang: str, interaction: nextcord.Interaction):
    if not interaction.user.guild_permissions.manage_guild and interaction.user.id != bot_owner:
        await interaction.response.send_message(text('manage_guild_error', lang))
        return

    success = daily.set_enabled(interaction.guild_id, True)
    
    if success:
        await interaction.response.send_message(text('auto_message_enable_success', lang))
    else:
        await interaction.response.send_message(text('auto_message_enable_error', lang))

async def disable_auto_message(lang: str, interaction: nextcord.Interaction):
    if not interaction.user.guild_permissions.manage_guild and interaction.user.id != bot_owner:
        await interaction.response.send_message(text('manage_guild_error', lang))
        return

    success = daily.set_enabled(interaction.guild_id, False)
    
    if success:
        await interaction.response.send_message(text('auto_message_disable_success', lang))
    else:
        await interaction.response.send_message(text('auto_message_disable_error', lang))
