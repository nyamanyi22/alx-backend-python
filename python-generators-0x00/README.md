# 📘 Python Generators - 0x00

This project explores **Python generators** by working with **MySQL databases** and streaming data row-by-row or in batches. It emphasizes **memory-efficient** data processing techniques for large datasets.

---

## 📁 Files

| Filename             | Description                                      |
|----------------------|--------------------------------------------------|
| `seed.py`            | Initializes database and table, inserts CSV data |
| `0-main.py`          | Script to seed DB and print sample data          |
| `0-stream_users.py`  | Generator to stream one user at a time           |
| `1-batch_processing.py` | Streams and processes data in batches         |
| `2-lazy_paginate.py` | Lazy-loads data in paginated format              |
| `3-main.py`          | Script to test lazy pagination                   |
| `4-stream_ages.py`   | Memory-efficient average calculation             |
| `user_data.csv`      | Sample user data file                            |

---

## 📦 Task 0: Getting started with Python generators

**Objective:**  
Set up a MySQL database `ALX_prodev` with a `user_data` table and populate it using a CSV file.

### Requirements:

- Table fields:
  - `user_id` (UUID, Primary Key, Indexed)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)

### Prototypes:

```python
def connect_db()
def create_database(connection)
def connect_to_prodev()
def create_table(connection)
def insert_data(connection, data_file)
