import psycopg2
import uuid
from datetime import datetime
from typing import List
from postgres import get_db_connection

from listing import Listing


def save_listings_db(listings: List[Listing]):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        for listing in listings:
            uuidv4 = uuid.uuid4()
            kwargs = {
                "cursor": cursor,
                "uuid": str(uuidv4),
                "listing": listing
            }

            save_single_listing(**kwargs)

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


def save_single_listing(cursor, uuid, listing: Listing):
    postgres_insert_query = """ INSERT INTO search.search_listings (listing_id, url, title, price, size, created_at) VALUES (%s,%s,%s,%s,%s,%s)"""

    record_to_insert = (uuid, listing.href,
                        listing.title, listing.price, listing.size, datetime.now())

    cursor.execute(postgres_insert_query,
                   record_to_insert)
