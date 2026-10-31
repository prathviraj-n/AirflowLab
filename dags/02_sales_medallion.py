"""DAG 2: bronze -> silver -> gold, written to be idempotent.
Teaching point: each task writes only its own partition (the run date) and OVERWRITES it,
so re-running the same date never changes the answer."""
import csv
from datetime import datetime
from pathlib import Path

from airflow.sdk import DAG, task

BASE = Path(__file__).resolve().parent.parent / "data"   # <repo>/data

with DAG(
    dag_id="02_sales_medallion",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["lab"],
) as dag:

    @task
    def bronze(**context):
        ds = context["ds"]                       # logical date, e.g. 2025-01-01
        out = BASE / "bronze" / f"orders_{ds}.csv"
        out.parent.mkdir(parents=True, exist_ok=True)
        rows = [("o1", "Pune", "100"), ("o2", "Goa", "250"), ("o2", "Goa", "250")]  # duplicate on purpose
        with open(out, "w", newline="") as f:     # "w" overwrites: safe to re-run
            csv.writer(f).writerows([("order_id", "city", "amount")] + rows)
        return str(out)

    @task
    def silver(path, **context):
        ds = context["ds"]
        with open(path) as f:
            rows = list(csv.DictReader(f))
        clean = list({r["order_id"]: r for r in rows}.values())   # remove duplicates
        out = BASE / "silver" / f"orders_{ds}.csv"
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["order_id", "city", "amount"])
            w.writeheader()
            w.writerows(clean)
        return str(out)

    @task
    def gold(path, **context):
        ds = context["ds"]
        with open(path) as f:
            total = sum(float(r["amount"]) for r in csv.DictReader(f))
        out = BASE / "gold" / f"revenue_{ds}.txt"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"{ds},{total}\n")          # overwrite, not append
        print(f"Revenue for {ds} = {total}")

    gold(silver(bronze()))
