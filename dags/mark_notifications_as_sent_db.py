import psycopg2

from postgres import get_db_connection


def mark_notifications_as_sent_db():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        postgres_update_query = """ UPDATE search.search_listings SET notification_sent_at = now() WHERE notification_sent_at is null; """

        cursor.execute(postgres_update_query)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully in the search table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to update record in the search table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
