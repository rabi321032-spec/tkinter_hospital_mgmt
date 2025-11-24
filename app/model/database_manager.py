import pymssql as mysql


class DatabaseManager:
    def __init__(self, host, database, user, password):
        self.config = {
            'host': host,
            'database': database,
            'user': user,
            'password': password
        }
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            print("Connected to database successfully")
            return True
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return False

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())

            if query.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
                return result
            else:
                self.connection.commit()
                return cursor.rowcount

        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")


# # Method 1: Try importing pymssql
# try:
#     import pymssql
#     print("✓ pymssql imported successfully")
#     print(f"✓ pymssql version: {pymssql.__version__}")
# except ImportError as e:
#     print("✗ pymssql not installed")
#     print(f"Error: {e}")
# Usage
db = DatabaseManager('localhost', 'mydb', 'user', 'password')
if db.connect():
    # Create table
    db.execute_query('''
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    ''')

    # Insert data
    db.execute_query(
        "INSERT INTO customers (name, email) VALUES (%s, %s)",
        ('John Doe', 'john@example.com')
    )

    # Query data
    results = db.execute_query("SELECT * FROM customers")
    print(results)

    db.close()