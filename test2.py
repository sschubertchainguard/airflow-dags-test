from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import logging

# Try importlib.metadata (Python 3.8+)
try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from pkg_resources import get_distribution, DistributionNotFound
    version = lambda name: get_distribution(name).version
    PackageNotFoundError = DistributionNotFound

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='celery_provider_version_check',
    default_args=default_args,
    description='Check version of apache-airflow-providers-celery',
    schedule_interval=None,
    catchup=False,
    tags=['debug', 'celery'],
) as dag:

    def print_airflow_celery_provider_version():
        try:
            pkg_name = 'apache-airflow-providers-celery'
            celery_provider_version = version(pkg_name)
            logging.info(f"{pkg_name} version: {celery_provider_version}")
            print(f"{pkg_name} version: {celery_provider_version}")
        except PackageNotFoundError:
            logging.error("Package apache-airflow-providers-celery not found.")
            print("Package apache-airflow-providers-celery not found.")

    check_provider_version = PythonOperator(
        task_id='print_airflow_celery_provider_version',
        python_callable=print_airflow_celery_provider_version
    )
