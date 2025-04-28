from airflow.api.client.local_client import Client

client = Client()
dag_id = "test_manual_trigger_dag" 
execution_date = None  

client.trigger_dag(dag_id=dag_id, execution_date=execution_date)
print(f"🫡 Successfully triggered DAG: {dag_id}")
