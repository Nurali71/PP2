import psycopg2
from config import params

def get_connection():
    try:
        # 
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f" Error while connecting to PostgreSQL: {error}")
        return None

if __name__ == "__main__":
    # Test the connection
    connection = get_connection()
    if connection:
        print("Connection successful!")
        connection.close()