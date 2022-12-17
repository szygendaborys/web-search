import pendulum
import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from archive_listings_db import archive_listings
from listing import Listing
from fetch_listings import fetch_listings
from save_listings_db import save_listings_db

with DAG(
    "otodom_scrapper",
    default_args={"retries": 2},
    description="Scraps the data from the otodom page",
    schedule_interval='*/15 * * * *',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["otodom"],
) as dag:
    def archive_previous_listings(**kwargs):
        print('Archiving listings...')

        archive_listings()

        print('Archiving listings succeded!')

    def load_from_website(**kwargs):
        ti = kwargs["ti"]

        print('Fetching listings...')

        data = fetch_listings()

        data_str_list = []

        for listing in data:
            data_str_list.append(str(listing))

        ti.xcom_push("listings_data", str(data_str_list))

        print('Fetching listings succeded!')

    def save_listings(**kwargs):
        ti = kwargs["ti"]

        listings_data_string = ti.xcom_pull(
            task_ids="load_from_website", key="listings_data")

        listings_data = eval(listings_data_string)
        listings = []

        for listing_raw in listings_data:
            print(listing_raw)
            listings.append(Listing(json.loads(listing_raw)))

        print('Saving listings...')

        save_listings_db(listings)

        print('Saving listings succeeded!')

    archive_previous_listings_task = PythonOperator(
        task_id="archive_previous_listings",
        python_callable=archive_previous_listings,
    )

    load_from_website_task = PythonOperator(
        task_id="load_from_website",
        python_callable=load_from_website,
    )

    save_listings_task = PythonOperator(
        task_id="save_listings",
        python_callable=save_listings,
    )

    archive_previous_listings_task >> load_from_website_task >> save_listings_task
