from airflow import DAG
from airflow.providers.celery.operators.celery import CeleryOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'test_celery_operator',
    default_args=default_args,
    description='A DAG to test CeleryOperator',
    schedule_interval=None,
    catchup=False,
) as dag:
    celery_task = CeleryOperator(
        task_id='run_celery_task',
        celery_app='my_celery_app',
        task_name='my_celery_app.tasks.add',
        op_args=[2, 3],
    )
