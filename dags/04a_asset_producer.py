"""DAG 4a: produces an Asset (a data product). Airflow 3 feature."""
from datetime import datetime

from airflow.sdk import DAG, Asset, task

daily_revenue = Asset("file:///tmp/daily_revenue")

with DAG(
    dag_id="04a_asset_producer",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["lab"],
):
    @task(outlets=[daily_revenue])
    def produce():
        print("Daily revenue data updated")

    produce()
