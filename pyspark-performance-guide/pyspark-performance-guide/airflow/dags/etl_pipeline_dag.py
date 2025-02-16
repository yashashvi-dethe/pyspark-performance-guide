from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.etl_pipeline import run_etl

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

dag = DAG(
    'etl_pipeline_dag',
    default_args=default_args,
    schedule_interval='@daily'
)

etl_task = PythonOperator(
    task_id='run_etl_pipeline',
    python_callable=run_etl,
    dag=dag
)
