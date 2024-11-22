import psycopg2
from config.settings import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def initialize_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    with open("database/schema.sql", "r") as f:
        schema = f.read()

    cursor.execute(schema)
    conn.commit()
    cursor.close()
    conn.close()

    print("Database initialized successfully.")
