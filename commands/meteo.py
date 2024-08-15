
import aiohttp
import nextcord
from datetime import datetime, timedelta
from utils.languages import text

def get_tomorrow_date():
    tomorrow = datetime.now() + timedelta(1)
    return tomorrow.strftime('%d-%m-%Y')

meteo_cache = {}

def format_date(date_str):
    # Replace possible separators with '-'
    date_str = date_str.replace('/', '-').replace('.', '-').replace(' ', '-')

    # Split the date string by the separator
    parts = date_str.split('-')

    if len(parts) != 3:
        raise ValueError("Date format not recognized")

    day, month, year = parts

    # Pad day and month with leading zeros if necessary
    day = day.zfill(2)
    month = month.zfill(2)

    # Handle year formats (assumes current century for 2-digit years)
    if len(year) == 2:
        year = f"20{year}"
    elif len(year) != 4:
        raise ValueError("Date format not recognized")

    return f"{year}-{month}-{day}"
    
async def get_meteo(lang, date=None):
    global meteo_cache
    
    if date is None or date.strip() == '':
        date = get_tomorrow_date()

    date = format_date(date)

    if date in meteo_cache:
        return meteo_cache[date]

    date = get_tomorrow_date() if date is None else date
    url = f"http://toobo.bishokus.fr:8000/API/toobo?date={date}"
    print(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                meteo_cache[date] = data.get('data',{}).get('text', text('meteo_404_error', lang))
                return meteo_cache[date]
            else:
                return None


async def send_meteo(lang: str, prefix, message: nextcord.Message):
    try:
        meteo_date = message.content

        await message.reply(
            await get_meteo(lang, meteo_date),
            mention_author=False
        )
    
    except Exception:
        await message.reply(
            text('meteo_format_error', lang).replace('%prefix%', prefix),
            mention_author=False
        )


async def send_meteo_slash(lang: str, prefix, interaction: nextcord.Interaction, meteo_date: str=get_tomorrow_date()):
    if meteo_date is None:
        meteo_date = get_tomorrow_date()
        
    try:
        meteo = await get_meteo(lang, meteo_date)
    except Exception:
        await interaction.response.send_message(
            text('meteo_format_error', lang).replace('%prefix%', prefix),
            ephemeral=True
        )
        return
        
    try:
        await interaction.response.send_message(meteo)
    except Exception:
        print("The API took too long to respond.")
    