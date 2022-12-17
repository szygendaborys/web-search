cat init.sql | docker exec -i otodom-search-postgres-1 psql -U airflow -d airflow
