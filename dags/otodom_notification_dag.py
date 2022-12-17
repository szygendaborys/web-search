import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from mark_notifications_as_sent_db import mark_notifications_as_sent_db
from notify_about_new_listings import notify_about_new_listings

with DAG(
    "otodom_notification_dag",
    default_args={"retries": 2},
    description="Sends notifications about new offers",
    schedule_interval='*/30 * * * *',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["otodom"],
) as dag:
    def send_notifications():
        print('Sending notifications...')

        notify_about_new_listings()

        print('Sending notifications succeeded!')

    def mark_notifications_as_sent():
        print('Marking notifications as send...')

        mark_notifications_as_sent_db()

        print('Marking notifications as send succeeded!')

    send_notifications_task = PythonOperator(
        task_id="send_notifications",
        python_callable=send_notifications,
    )

    mark_notifications_as_sent_task = PythonOperator(
        task_id="mark_notifications_as_sent",
        python_callable=mark_notifications_as_sent,
    )

    send_notifications_task >> mark_notifications_as_sent_task
