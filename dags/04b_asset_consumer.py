"""DAG 4b: scheduled by the Asset, not by the clock.
Teaching point: run when the data is ready, instead of guessing a time."""
from datetime import datetime

from airflow.sdk import DAG, Asset, task

daily_revenue = Asset("file:///tmp/daily_revenue")

with DAG(
    dag_id="04b_asset_consumer",
    start_date=datetime(2025, 1, 1),
    schedule=[daily_revenue],   # triggered when 04a updates the asset
    catchup=False,
    tags=["lab"],
):
    @task
    def consume():
        print("Triggered because the asset was updated")

    consume()
