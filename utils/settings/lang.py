import mysql.connector
from utils.sql import get_db_connection
from utils.sql.create_guild import guild_db
from utils.sql.create_user import user_db

import json

with open('config/config.json') as config_file:
    config = json.load(config_file)
    default_language = config['default-language']


@guild_db
def set_guild(guild_id: int, new_language: str):
    """
    Sets a new language for a given guild ID in the database.

    Args:
        guild_id (int): The ID of the guild.
        new_language (str): The new language to be set for the guild.

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
        query = 'UPDATE guilds SET bot_language = %s WHERE id = %s'
        cursor.execute(query, (new_language, guild_id))
        conn.commit()
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

@user_db
def set_user(user_id: int, new_language: str):
    """
    Sets a new language for a given user ID in the database.

    Args:
        user_id (int): The ID of the user.
        new_language (str): The new language to be set for the user.

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
        query = 'UPDATE users SET bot_language = %s WHERE id = %s'
        cursor.execute(query, (new_language, user_id))
        conn.commit()
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


@user_db
@guild_db
def get(guild_id: int, user_id: int) -> str:
    """
    Retrieves the language for a given user and guild ID from the database.

    Args:
        guild_id (int): The ID of the guild.
        user_id (int): The ID of the user.

    Returns:
        str: The language for the user or guild. If no language is found, it returns the default language.

    Raises:
        mysql.connector.Error: If there's an error while querying the database.
    """
    
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check user language
        query = 'SELECT bot_language FROM users WHERE id = %s'
        cursor.execute(query, (user_id,))
        user_result = cursor.fetchone()
        
        if user_result and user_result[0]:
            return user_result[0]
        
        # Check guild language
        query = 'SELECT bot_language FROM guilds WHERE id = %s'
        cursor.execute(query, (guild_id,))
        guild_result = cursor.fetchone()
        
        if guild_result and guild_result[0]:
            return guild_result[0]
        
        # If no language is set, return default
        return default_language
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return default_language
    finally:
        cursor.close()
        conn.close()
