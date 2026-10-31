"""DAG 1: tasks, order and parallel fan-out.
Teaching point: a DAG is tasks plus dependencies. Independent tasks run in parallel."""
from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="01_hello_parallel",
    start_date=datetime(2025, 1, 1),
    schedule=None,          # run manually
    catchup=False,
    tags=["lab"],
) as dag:
    start = BashOperator(task_id="start", bash_command="echo 'Hello from Airflow'")

    loads = [
        BashOperator(task_id=f"load_{city}", bash_command=f"echo loading {city}; sleep 5")
        for city in ["pune", "goa", "delhi"]
    ]

    combine = BashOperator(task_id="combine", bash_command="echo 'All cities loaded'")

    start >> loads >> combine
