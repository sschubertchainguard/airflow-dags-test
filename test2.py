from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import logging
import celery
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

# Define the DAG
with DAG(
    dag_id='celery_version_check',
    default_args=default_args,
    description='A DAG to print the Celery version used by Airflow',
    schedule_interval=None,  # Run manually
    catchup=False,
    tags=['debug', 'celery'],
) as dag:

    def print_celery_version():
        version = celery.__version__
        logging.info(f"Celery version: {version}")
        print(f"Celery version: {version}")

    # Task: Print Celery version
    check_celery = PythonOperator(
        task_id='print_celery_version',
        python_callable=print_celery_version
    )
