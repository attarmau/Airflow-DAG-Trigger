# Airflow-DAG-Trigger

## Objective

The goal is to add manual triggering functionality in Airflow, where the trigger prints the time when the DAG is manually triggered. To achieve this, I have designed the test_manual_trigger_dag, which is a simple sample DAG created to test the manual triggering functionality in Airflow.

In your case, you need to replace the test_manual_trigger.py file with your own DAG file to test manual triggering in your specific DAG.

Important: When you’re testing your own DAG file, the 'dag_id' in Step 3 needs to be updated accordingly to reflect the name of your original DAG.

For further details, follow the specific steps outlined below.

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
Note: Make sure to replace 'test_manual_trigger_dag' with the correct 'dag_id' if it's different from ur original setting

<img width="423" alt="Screenshot 2025-04-28 at 10 28 19 PM" src="https://github.com/user-attachments/assets/35841f7e-b6fc-41b1-9a9c-2996939d3185" />

## Verify: Check the DAG Run
```
airflow dags show test_manual_trigger_dag
```
This will display the execution history and status of the DAG runs. You can check if there are any failures or if the DAG completed successfully.

## Expected Output 

If the time the DAG was triggered is printed to the logs, which would look something like this:
```
🫡 DAG manually triggered at 2025-04-28 10:35:00
```
➡️ In the Airflow web interface, you will see the DAG execution has been triggered, and you can check the logs for the task to confirm the printed time.
