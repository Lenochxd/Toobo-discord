import mysql.connector
from utils.sql import get_db_connection
from utils.sql.create_guild import guild_db

import json

with open('config/config.json') as config_file:
    config = json.load(config_file)
    default_prefix = config['default-prefix']
    

@guild_db
def set(guild_id: int, new_prefix: str):
    """
    Sets a new prefix for a given guild ID in the database.

    Args:
        guild_id (int): The ID of the guild.
        new_prefix (str): The new prefix to be set for the guild.

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
        query = 'UPDATE guilds SET prefix = %s WHERE id = %s'
        cursor.execute(query, (new_prefix, guild_id))
        conn.commit()
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

@guild_db
def get(guild_id: int) -> str:
    """
    Retrieves the prefix for a given guild ID from the database.

    Args:
        guild_id (int): The ID of the guild.

    Returns:
        str: The prefix for the guild. If no prefix is found, it sets and returns the default prefix.

    Raises:
        mysql.connector.Error: If there's an error while querying the database.
    """
    
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = 'SELECT prefix FROM guilds WHERE id = %s'
        cursor.execute(query, (guild_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            set(guild_id, default_prefix)
            return default_prefix
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        set(guild_id, default_prefix)
        return default_prefix
    finally:
        cursor.close()
        conn.close()