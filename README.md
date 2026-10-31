# Airflow Hands-on Lab (Data Engineering for Managers, TAPMI)

Five DAGs that teach the main ideas of the orchestration module. Tested with Apache Airflow 3.3.2.

| File | DAG(s) | What it teaches |
|---|---|---|
| `dags/01_hello_parallel.py` | `01_hello_parallel` | Tasks, order, parallel fan-out |
| `dags/02_sales_medallion.py` | `02_sales_medallion` | Bronze, silver, gold; idempotent re-runs |
| `dags/03_retry_and_failure.py` | `03_retry_and_failure` | Retries and failure handling |
| `dags/04a_asset_producer.py` | `04a_asset_producer` | Producing an Asset (Airflow 3) |
| `dags/04b_asset_consumer.py` | `04b_asset_consumer` | Scheduling on data, not on the clock |

## Run it in GitHub Codespaces (no install, no PowerShell)

1. Upload these files to a GitHub repository (keep the folder layout, including `.devcontainer`).
2. On the repository page: **Code > Codespaces > Create codespace on main**.
3. Wait for setup to finish (about 2 to 5 minutes; it runs `setup.sh`).
4. In the terminal:
   ```bash
   source env.sh
   airflow standalone
   ```
5. Open the **Ports** tab, click the globe next to port **8080**, and log in with the password printed in the terminal.
6. Unpause a DAG and click **Trigger**.

Stop the codespace when you are done (**Codespaces menu > Stop**) to save your free hours.

## Run it on Linux, macOS or WSL

```bash
bash setup.sh
source env.sh
airflow standalone
```
Then open http://localhost:8080.

## Check the idempotency lesson (DAG 2)

After triggering `02_sales_medallion` twice for the same date:
```bash
cat data/gold/revenue_*.txt     # the total stays 350.0, it never doubles
```

## Quick test without the UI

```bash
source env.sh
airflow db migrate
airflow dags test 02_sales_medallion 2025-01-02
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `airflow: command not found` | Run `source env.sh` in that terminal |
| A DAG is missing | Check the import errors banner; confirm the file is in `dags/` |
| Password unknown | Stop `airflow standalone`, start it again, read the printed password |
| Port 8080 not shown | Add port 8080 manually in the Ports tab |
