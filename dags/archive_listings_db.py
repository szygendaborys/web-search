import psycopg2
from postgres import get_db_connection


def archive_listings():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        postgres_insert_query = """ UPDATE search.search_listings SET deleted_at = now() WHERE deleted_at IS NULL; """

        cursor.execute(postgres_insert_query)

        connection.commit()
        count = cursor.rowcount

        print(count, "Records archived in the search table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to archive records in the search table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
