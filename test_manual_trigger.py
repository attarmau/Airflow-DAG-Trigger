from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def test_trigger_function(**kwargs):
    execution_time = kwargs['execution_date']
    print(f"🫡 DAG manually triggered at {execution_time}")

with DAG(
    dag_id="test_manual_trigger_dag",
    description="A DAG to test manual trigger and execution time",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["test"],
) as dag:

    trigger_test_task = PythonOperator(
        task_id="print_trigger_time",
        python_callable=test_trigger_function,
        provide_context=True,
    )
