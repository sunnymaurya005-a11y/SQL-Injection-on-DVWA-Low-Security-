"""
Secure SQL Query Example
Project: DVWA SQL Injection Lab

Demonstrates parameterized SQL queries
using MySQL Connector/Python.
"""

def get_user_by_id(connection, raw_user_id):

    # Validate user input
    try:
        user_id = int(raw_user_id)
    except (TypeError, ValueError):
        raise ValueError("Invalid user ID")

    if user_id < 1:
        raise ValueError("User ID must be positive")

    cursor = connection.cursor(dictionary=True)

    try:
        # Parameterized SQL query
        query = """
            SELECT user_id, first_name, last_name
            FROM users
            WHERE user_id = %s
        """

        cursor.execute(query, (user_id,))

        return cursor.fetchone()

    finally:
        cursor.close()


# Security best practices:
# 1. Use parameterized queries.
# 2. Validate user input.
# 3. Never concatenate user input into SQL.
# 4. Use least-privilege database accounts.
# 5. Handle errors securely.
