import mysql.connector
import json
import os

from utils.config import config
db_config = config['mysql']


def get_db_connection():
    """
    Establishes and returns a connection to the MySQL database.

    This function attempts to connect to the database using the configuration
    specified in the 'db_config' dictionary. If the initial connection fails
    due to a ProgrammingError (which might occur if the database doesn't exist),
    it will create the database and then attempt to connect again.

    Returns:
        mysql.connector.connection.MySQLConnection: A connection object to the MySQL database.

    Raises:
        mysql.connector.Error: If there's an error connecting to the database
        that isn't resolved by creating the database.

    Note:
        This function relies on the 'db_config' dictionary being properly
        populated with the necessary connection parameters.
    """
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.errors.ProgrammingError:
        
        database = db_config['database']
        del db_config['database']
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        create_database(cursor, database)
        
        db_config['database'] = database
        return mysql.connector.connect(**db_config)


def create_database(cursor, db_name):
    """
    Creates a database if it does not exist.

    :param cursor: MySQL cursor object
    :param db_name: Name of the database to create
    """
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET 'utf8'")
        print(f"Database {db_name} created or already exists.")
    except mysql.connector.Error as err:
        print(f"Failed to create database {db_name}: {err}")
        exit(1)

def execute_sql_file(cursor, sql_file_path, replacements=None):
    """
    Executes a SQL file with caching.

    :param cursor: MySQL cursor object
    :param sql_file_path: Path to the SQL file
    :param replacements: Dictionary of replacements for %s placeholders
    """
    cache = {}

    def read_file(path):
        if path not in cache:
            with open(path, 'r') as file:
                cache[path] = file.read()
        return cache[path]

    def clear_cache():
        cache.clear()

    sql_commands = read_file(sql_file_path).split(';')
    for command in sql_commands:
        command = command.strip()
        if command:
            if replacements:
                cursor.execute(command, replacements)
            else:
                cursor.execute(command)

    # Clear cache if file has been modified
    if os.path.getmtime(sql_file_path) > cache.get(sql_file_path + '_mtime', 0):
        clear_cache()
        cache[sql_file_path + '_mtime'] = os.path.getmtime(sql_file_path)

def init():
    """
    Initializes the database connection, executes SQL file, and performs initial setup.
    """

    conn = get_db_connection()
    cursor = conn.cursor()
    
    execute_sql_file(cursor, 'utils/sql/init_db.sql')
    
    #   CONFESS BAN JSON STRUCTURE:
    #
    # {
    #     "admin_id": message.author.id,
    #     "type": "confess_id",
    #     "reason": ban_reason,
    #     "message_banned": confess_message_banned,
    #     "confess_id": 000
    # }
    
    cursor.execute("SELECT COUNT(*) FROM guilds")
    guilds_count = cursor.fetchone()[0]
    print('Database | guilds_count:', guilds_count)
    if guilds_count < 1:
        print('The database is new.')
    
    conn.commit()
    conn.close()