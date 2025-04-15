from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 15),
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

with DAG(
    'test_celery_executor',
    default_args=default_args,
    description='A simple DAG to test CeleryExecutor',
    schedule_interval=None,
    catchup=False,
) as dag:
    test_task = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello from CeleryExecutor!"',
    )
