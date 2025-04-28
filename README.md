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

## Step 3: Trigger the DAG
```
airflow dags trigger test_manual_trigger_dag
```
Note: Make sure to replace 'test_manual_trigger_dag' with the correct 'dag_id' if it's different from urs 

<img width="423" alt="Screenshot 2025-04-28 at 10 28 19 PM" src="https://github.com/user-attachments/assets/35841f7e-b6fc-41b1-9a9c-2996939d3185" />
