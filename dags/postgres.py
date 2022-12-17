from dotenv import load_dotenv
import os
import psycopg2


def get_db_connection():
    try:
        load_dotenv()

        host = os.getenv("POSTGRES_HOST", 'postgres')
        connection = psycopg2.connect(user="airflow",
                                      password="airflow",
                                      host=host,
                                      port="5432",
                                      database="airflow")

        return connection

    except (Exception, psycopg2.Error) as error:
        print("Failed to create a connection", error)
