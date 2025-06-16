import psycopg2

def check_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="online_voting_system",
            user="postgres",
            password="root",
            port=5432
        )
        print("Database connection successful!")
    except Exception as e:
        print("Failed to connect to the database:", e)
    finally:
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    check_connection()
