import mysql.connector
import csv

# 1. Connect to MySQL server only
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # Use your XAMPP password if set
    )

# 2. Create the database ALX_prodev if it doesn't exist
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

# 3. Connect to the ALX_prodev database
def connect_to_prodev():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ALX_prodev'
    )

# 4. Create the user_data table with proper columns
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        )
    """)
    connection.commit()
    print("Table user_data created successfully")
    cursor.close()

# 5. Insert data from CSV into user_data table
def insert_data(connection, data_file):
    cursor = connection.cursor()
    with open(data_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (row['user_id'], row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()
