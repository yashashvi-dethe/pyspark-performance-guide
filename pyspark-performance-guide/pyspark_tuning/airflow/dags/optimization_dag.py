from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.optimization import optimize_queries

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

dag = DAG(
    'optimization_dag',
    default_args=default_args,
    schedule_interval='@daily'
)

optimization_task = PythonOperator(
    task_id='optimize_queries',
    python_callable=optimize_queries,
    dag=dag
)
