from functools import wraps
from utils.sql import get_db_connection, execute_sql_file


def ensure_user_exists(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Check if the user already exists
    cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()

    if result is None:
        # User doesn't exist, so we add it
        execute_sql_file(cursor, 'utils/sql/init_user.sql', (user_id,))

        connection.commit()

    cursor.close()
    connection.close()


def user_db(func):
    """
    A decorator that ensures the user exists in the database before executing the wrapped function.

    This decorator checks if the user with the given ID exists in the database.
    If it doesn't exist, it creates the user using the `ensure_user_exists` function.

    Args:
        func (callable): The function to be wrapped.

    Returns:
        callable: The wrapped function.

    Usage:
        @user_db
        def some_function(user_id):
            # Function implementation
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = args[0] if args else kwargs.get('user_id')
        if user_id:
            ensure_user_exists(user_id)
        return func(*args, **kwargs)
    return wrapper
