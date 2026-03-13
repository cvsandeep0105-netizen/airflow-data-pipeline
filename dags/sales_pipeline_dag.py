from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append("./scripts")

from etl_process import run_etl

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1)
}

with DAG(
    dag_id="sales_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_pipeline = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_etl
    )

    run_etl_task