import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=None):
        self.query = query
        self.params = params or []
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')  # Open DB connection
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)  # Execute query
        return self.cursor.fetchall()  # Return results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()  # Ensure connection is closed
