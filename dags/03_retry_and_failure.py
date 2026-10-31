"""DAG 3: retries.
Teaching point: failures are normal. Retries recover from temporary problems;
downstream tasks run only after the failing task finally succeeds."""
from datetime import datetime, timedelta

from airflow.sdk import DAG, task

with DAG(
    dag_id="03_retry_and_failure",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["lab"],
    default_args={"retries": 2, "retry_delay": timedelta(seconds=10)},
) as dag:

    @task
    def flaky(**context):
        attempt = context["ti"].try_number
        print(f"Attempt {attempt}")
        if attempt < 3:
            raise RuntimeError("Simulated temporary failure")
        print(f"Succeeded on attempt {attempt}")

    @task
    def after():
        print("Runs only after flaky() succeeds")

    flaky() >> after()
