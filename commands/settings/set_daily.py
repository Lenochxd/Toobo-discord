import re
import json
import nextcord
from nextcord.abc import GuildChannel
from utils.languages import text

from utils.settings import daily
from utils.config import config
bot_owner = config.get('owner-id')


async def format_time(lang, new_time, interaction: nextcord.Interaction=None, message: nextcord.Message=None):
    # Format new_time
    formatted_time = ""
    if "h" in new_time:
        parts = new_time.split("h")
        hours = parts[0].zfill(2)
        minutes = parts[1].zfill(2) if len(parts) > 1 else "00"
        formatted_time = f"{hours}:{minutes}"
    elif ":" in new_time:
        parts = new_time.split(":")
        hours = parts[0].zfill(2)
        minutes = parts[1].zfill(2)
        formatted_time = f"{hours}:{minutes}"
    else:
        formatted_time = f"{new_time.zfill(2)}:00"

    # Validate the formatted time
    try:
        hours, minutes = map(int, formatted_time.split(":"))
        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            raise ValueError
    except ValueError:
        return None
    
    return formatted_time

def handle_text(message: nextcord.Message):
    # Extract channel or channel ID from the message using regex
    
    channel_mention = re.search(r'<#(\d+)>', message.content)
    if channel_mention:
        channel_id = int(channel_mention.group(1))
    else:
        channel_id = message.channel.id

    # Extract time from the message
    time_parts = [part for part in message.content.split() if ':' in part or 'h' in part]
    new_time = time_parts[0] if time_parts else None
    
    if new_time is None:
        new_time = message.content.replace(f'<#{channel_id}>', '').strip()
        if new_time == '':
            return channel_id, None
    
    return channel_id, new_time


async def set_daily(lang: str, prefix: str, message: nextcord.Message):
    if message.author.guild_permissions.manage_guild == False and message.author.id != bot_owner:
        await message.reply(text('manage_guild_error', lang), mention_author=False)
        return
    
    channel_id, new_time = handle_text(message)
    if new_time is None:
        await message.reply(
            text('setup_invalid_syntax', lang).replace('%prefix%', prefix),
            mention_author=False
        )
        return

    new_time = await format_time(lang, new_time, None, message)

    daily.set_time(message.guild.id, new_time)
    daily.set_channel(message.guild.id, channel_id)
    
    if new_time:
        await message.reply(
            text('setup_success', lang).replace('%channel%', f'<#{channel_id}>').replace('%time%', new_time),
            mention_author=False
        )
    else:
        await message.reply(
            text('setup_invalid_time_format', lang),
            mention_author=False
        )

async def set_daily_slash(lang: str, interaction: nextcord.Interaction, new_time: str, channel: GuildChannel):
    new_time = await format_time(lang, new_time, interaction)

    daily.set_time(interaction.guild_id, new_time)
    daily.set_channel(interaction.guild_id, channel.id)
    
    if new_time:
        await interaction.response.send_message(
            text('setup_success', lang).replace('%channel%', f'<#{channel.id}>').replace('%time%', new_time)
        )
    else:
        await interaction.response.send_message(
            text('setup_invalid_time_format', lang),
            ephemeral=True
        )