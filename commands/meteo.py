import nextcord
import random
from utils.languages import text


async def send_meteo(lang: str, prefix, message: nextcord.Message):
    try:
        rolls, limit = map(int, message.content.split('d'))
    except ValueError:
        await message.channel.send(
            text('roll_format_error', lang).replace('%prefix%', prefix)
        )
        return

    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await message.reply(result, mention_author=False)

async def send_meteo_slash(lang: str, prefix, interaction: nextcord.Interaction, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except ValueError:
        await interaction.response.send_message(
            text('roll_format_error', lang).replace('%prefix%', prefix),
            ephemeral=True
        )
        return

    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await interaction.response.send_message(result)