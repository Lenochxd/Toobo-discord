import mysql.connector
from utils.sql import get_db_connection
from utils.sql.create_guild import guild_db

from utils.config import config
default_time = config.get('default-time', '19:50')


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
    except Exception as err:
        print(f'Error: {err}')
        set(guild_id, default_time)
        return None
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
        query = 'UPDATE guilds SET auto_channelid = %s, auto_message_enabled = TRUE WHERE id = %s'
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


@guild_db
def set_enabled(guild_id: int, enable: bool) -> bool:
    """
    Enables or disables the auto message feature for a given guild ID.

    Args:
        guild_id (int): The ID of the guild.
        enable (bool): True to enable, False to disable the feature.

    Returns:
        bool: True if the operation was successful, False otherwise.

    Raises:
        mysql.connector.Error: If there's an error while updating the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = 'UPDATE guilds SET auto_message_enabled = %s WHERE id = %s'
        cursor.execute(query, (enable, guild_id))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return False
    finally:
        cursor.close()
        conn.close()

@guild_db
def is_enabled(guild_id: int) -> bool:
    """
    Checks if the auto message feature is enabled for a given guild ID.

    Args:
        guild_id (int): The ID of the guild.

    Returns:
        bool: True if the auto message feature is enabled, False otherwise.

    Raises:
        mysql.connector.Error: If there's an error while querying the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = 'SELECT auto_message_enabled FROM guilds WHERE id = %s'
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        return bool(result[0]) if result else False
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return False
    finally:
        cursor.close()
        conn.close()
