import mysql.connector
from mysql.connector import Error

def create_database():
    """Connects to MySQL and creates the alx_book_store database."""
    connection = None  # Initialize connection to None
    try:
        # --- IMPORTANT ---
        # Replace "YOUR_PASSWORD" with your actual MySQL root password.
        # If you have no password, keep it as "".
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully! ✅")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # This check is now more robust. It ensures 'connection' was successfully assigned.
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()