from typing import List
import psycopg2
from sendgrid_sender import send_email
from listing import Listing
from postgres import get_db_connection


def notify_about_new_listings():
    listings = get_active_listings()

    if len(listings) > 0:
        send_notification_emails(listings)
    else:
        print("No new listings")


def get_active_listings() -> List[Listing]:
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        postgres_insert_query = """ select distinct title, url, price, size from "search".search_listings sl where url not in (select distinct url from "search".search_listings where notification_sent_at is not null) group by url, title, price, "size" having count(url) = 1; """

        cursor.execute(postgres_insert_query)

        records_found = cursor.fetchall()
        listings = []

        print(records_found)

        for record in records_found:
            listing = Listing({
                'title': record[0],
                'href': record[1],
                'price': record[2],
                'size': record[3],
                'price_per_square': -1,  # might add it later
            })

            listings.append(listing)

        return listings

    except (Exception, psycopg2.Error) as error:
        print("Failed to query record into search table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def send_notification_emails(listings: List[Listing]):
    # Create the container (outer) email message.
    message_str = 'Znaleziono nowe dzialki! Wszystkie zostaly wylistowane ponizej \/ \n \n \n'

    for listing in listings:
        message_str = message_str + listing.get_message()

    send_email(message_str)

    print('A message has been sent! :-)')
