# Airflow-DAG-Trigger

## Step1: Ensure Airflow is running

First, make sure that the Airflow services are up and running. This can be done using the following commands:

```
airflow webserver --port 8080
```

Start the Airflow scheduler
```
airflow scheduler
```

## Step 2: Check if the DAG is listed
```
airflow dags list
```
This command will show all the available DAGs in Airflow. Look for the dag_id of your DAG, which should match the ID you have defined in your DAG file. In this demo, the DAG file is named 'test_manual_trigger_dag'. !Ignore this file if u r using ur own DAG file!
