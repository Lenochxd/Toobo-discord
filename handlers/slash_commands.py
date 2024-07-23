import json
import nextcord
from nextcord.ext import commands, application_checks
from utils.get_commands_locales import get_commands_locales

from commands.meteo import send_meteo_slash
from commands.settings.set_prefix import set_prefix_slash

from utils.settings import prefix
from utils.languages import get_languages_info

# Load JSON localization data
with open('config/config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)
    default_locale = config['default-slash-locale']
    lang = config['default-language']


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