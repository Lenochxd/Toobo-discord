import json
import nextcord
from nextcord.ext import commands, application_checks
from nextcord.abc import GuildChannel
from utils.get_commands_locales import get_commands_locales

from commands.meteo import send_meteo_slash
from commands.settings.enable import enable_auto_message, disable_auto_message
from commands.settings.set_daily import set_daily_slash
from commands.settings.set_prefix import set_prefix_slash

from utils.settings import prefix
from utils.config import config

default_locale = config.get('default-slash-locale', 'fr')
lang = config.get('default-language', 'fr')


def register_slash_commands(bot: commands.Bot):
    locales = get_commands_locales()
    
    command = 'prefix'
    @bot.slash_command(
        name=locales[command]['name'][default_locale],
        description=locales[command]['desc'][default_locale],
        name_localizations=locales[command]['name'],
        description_localizations=locales[command]['desc'],
        default_member_permissions=(nextcord.Permissions(manage_guild=True))
    )
    @application_checks.has_permissions(manage_guild=True)
    async def prefix_command(interaction: nextcord.Interaction,
        new_prefix: str = nextcord.SlashOption(
            name=locales[command]['args'][0]['name'][default_locale],
            name_localizations=locales[command]['args'][0]['name'],
            description=locales[command]['args'][0]['desc'][default_locale],
            description_localizations=locales[command]['args'][0]['desc']
        )
    ):
        await set_prefix_slash(lang, interaction, new_prefix)
    
    
    command = 'setup'
    @bot.slash_command(
        name=locales[command]['name'][default_locale],
        description=locales[command]['desc'][default_locale],
        name_localizations=locales[command]['name'],
        description_localizations=locales[command]['desc'],
        default_member_permissions=(nextcord.Permissions(manage_guild=True))
    )
    @application_checks.has_permissions(manage_guild=True)
    async def set_daily_command(interaction: nextcord.Interaction,
        channel: GuildChannel = nextcord.SlashOption(
            name=locales[command]['args'][0]['name'][default_locale],
            name_localizations=locales[command]['args'][0]['name'],
            description=locales[command]['args'][0]['desc'][default_locale],
            description_localizations=locales[command]['args'][0]['desc'],
            channel_types=[nextcord.ChannelType.text]
        ),
        new_time: str = nextcord.SlashOption(
            name=locales[command]['args'][1]['name'][default_locale],
            name_localizations=locales[command]['args'][1]['name'],
            description=locales[command]['args'][1]['desc'][default_locale],
            description_localizations=locales[command]['args'][1]['desc'],
            default=config.get('default-time', '19:50'),
            min_length=1, # 9
            max_length=6  # 19:50h
        )
    ):
        await set_daily_slash(lang, interaction, new_time, channel)
    
    
    command = 'activer-toobo'
    @bot.slash_command(
        name=locales[command]['name'][default_locale],
        description=locales[command]['desc'][default_locale],
        name_localizations=locales[command]['name'],
        description_localizations=locales[command]['desc']
    )
    async def enable_auto_message_command(interaction: nextcord.Interaction):
        await enable_auto_message(lang, interaction)
    
    
    command = 'desactiver-toobo'
    @bot.slash_command(
        name=locales[command]['name'][default_locale],
        description=locales[command]['desc'][default_locale],
        name_localizations=locales[command]['name'],
        description_localizations=locales[command]['desc']
    )
    async def disable_auto_message_command(interaction: nextcord.Interaction):
        await disable_auto_message(lang, interaction)
    
    
    command = 'meteo'
    @bot.slash_command(
        name=locales[command]['name'][default_locale],
        description=locales[command]['desc'][default_locale],
        name_localizations=locales[command]['name'],
        description_localizations=locales[command]['desc']
    )
    async def meteo_command(interaction: nextcord.Interaction,
        meteo_date: str = nextcord.SlashOption(
            name=locales[command]['args'][0]['name'][default_locale],
            name_localizations=locales[command]['args'][0]['name'],
            description=locales[command]['args'][0]['desc'][default_locale],
            description_localizations=locales[command]['args'][0]['desc'],
            required=False,
            min_length=6, # 1/2/24
            max_length=10 # 10/21/2024
        )
    ):
        await send_meteo_slash(lang, prefix.get(interaction.guild_id), interaction, meteo_date)

# Testing
if __name__ == '__main__':
    print(get_commands_locales())