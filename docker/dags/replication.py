from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="SCD2_snapshots",
    default_args=default_args,
    description="Run dbt snapshot for SCD2 tables",
    schedule_interval="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["dbt", "snapshots"]
) as dag:
    dbt_run_staging = BashOperator(
        task_id="dbt_run_staging",
        bash_command="cd /opt/airflow/banking_dbt && dbt run --profiles-dir /home/airflow/.dbt --select models/staging",
    )

    dbt_snapshot = BashOperator(
        task_id="dbt_snapshot",
        bash_command="cd /opt/airflow/banking_dbt && dbt snapshot --profiles-dir /home/airflow/.dbt",
    )

    dbt_run_marts = BashOperator(
        task_id="dbt_run_marts",
        bash_command="cd /opt/airflow/banking_dbt && dbt run --profiles-dir /home/airflow/.dbt --select marts",
    )

    dbt_run_staging >> dbt_snapshot >> dbt_run_marts
