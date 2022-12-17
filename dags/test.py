import psycopg2
import uuid
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

try:
    host = os.getenv("POSTGRES_HOST", 'postgres')
    connection = psycopg2.connect(user="airflow",
                                  password="airflow",
                                  host=host,
                                  port="5432",
                                  database="search")
    cursor = connection.cursor()

    uuidv4 = uuid.uuid4()
    postgres_insert_query = """ INSERT INTO search.search_listings (listing_id, url, title, price, size, created_at) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (str(uuidv4), 'test_url',
                        'test_title', 'test_price', 'test_size', datetime.now())
    cursor.execute(postgres_insert_query,
                   record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into search table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into search table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
