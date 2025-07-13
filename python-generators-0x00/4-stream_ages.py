#!/usr/bin/python3
import seed

def stream_user_ages():
    """Generator that yields user ages one by one from the database"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield float(row[0])
    cursor.close()
    connection.close()

def compute_average_age():
    """Computes and prints average age using the generator"""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    if count == 0:
        print("No users found.")
    else:
        average = total / count
        print(f"Average age of users: {average:.2f}")
