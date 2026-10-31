# Run this in every new terminal:  source env.sh
source "$(dirname "${BASH_SOURCE[0]}")/venv/bin/activate"
export AIRFLOW_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/airflow_home"
export AIRFLOW__CORE__DAGS_FOLDER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/dags"
export AIRFLOW__CORE__LOAD_EXAMPLES=False
