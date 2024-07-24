import mysql.connector
from utils.sql import get_db_connection
from utils.sql.create_guild import guild_db

import json

with open('config/config.json') as config_file:
    config = json.load(config_file)
    default_time = config['default-time']
    

@guild_db
def set_time(guild_id: int, new_time: str):
    """
    Sets a new time for a given guild ID in the database.

    Args:
        guild_id (int): The ID of the guild.
        new_time (str): The new time to be set for the guild.

    Raises:
        mysql.connector.Error: If there's an error while updating the database.

    Note:
        This function handles the database connection, commits the changes,
        and ensures proper closure of the cursor and connection.
        If an error occurs during the update, it will be printed and the transaction will be rolled back.
    """
    
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = 'UPDATE guilds SET auto_message_hour = %s WHERE id = %s'
        cursor.execute(query, (new_time, guild_id))
        conn.commit()
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

@guild_db
def get_time(guild_id: int) -> str:
    """
    Retrieves the time for a given guild ID from the database.

    Args:
        guild_id (int): The ID of the guild.

    Returns:
        str: The time for the guild. If no time is found, it sets and returns the default time.

    Raises:
        mysql.connector.Error: If there's an error while querying the database.
    """
    
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = 'SELECT auto_message_hour FROM guilds WHERE id = %s'
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            set(guild_id, default_time)
            return default_time
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        set(guild_id, default_time)
        return default_time
    finally:
        cursor.close()
        conn.close()


@guild_db
def set_channel(guild_id: int, channel_id: int) -> None:
    """
    Sets the auto channel ID for a given guild ID in the database.

    Args:
        guild_id (int): The ID of the guild.
        channel_id (int): The ID of the channel to set.

    Raises:
        mysql.connector.Error: If there's an error while updating the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = 'UPDATE guilds SET auto_channelid = %s WHERE id = %s'
        cursor.execute(query, (channel_id, guild_id))
        conn.commit()
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

@guild_db
def get_channel(guild_id: int) -> int:
    """
    Retrieves the auto channel ID for a given guild ID from the database.

    Args:
        guild_id (int): The ID of the guild.

    Returns:
        int: The auto channel ID for the guild. If no channel is found, it returns None.

    Raises:
        mysql.connector.Error: If there's an error while querying the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = 'SELECT auto_channelid FROM guilds WHERE id = %s'
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return None
    finally:
        cursor.close()
        conn.close()
