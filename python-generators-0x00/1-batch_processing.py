import mysql.connector
from decimal import Decimal

def stream_users_in_batches(batch_size):
    """
    Generator that yields users in batches from the user_data table.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Update this if your MySQL has a password
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)

        offset = 0
        while True:
            cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
            rows = cursor.fetchall()
            if not rows:
                break
            yield rows
            offset += batch_size

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print("Database error:", err)
        return

def batch_processing(batch_size):
    """
    Process and print users in batches who are over age 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            # Convert Decimal to int for age if needed
            age = user['age']
            if isinstance(age, Decimal):
                age = int(age)
            if age > 25:
                print(user)
