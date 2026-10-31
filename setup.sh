#!/usr/bin/env bash
# One-time setup: creates a virtual environment and installs Airflow.
set -e
AIRFLOW_VERSION="${AIRFLOW_VERSION:-3.3.2}"
python3 -m venv venv
source venv/bin/activate
PYTHON_VERSION="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install --upgrade pip
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
echo "Setup done. Next: source env.sh && airflow standalone"
