# Airflow-DAG-Trigger

## Objective

The goal is to add manual triggering functionality in Airflow, where the trigger prints the time when the DAG is manually triggered. To achieve this, I have designed the ’test_manual_trigger_dag.py', which is a simple sample DAG created to test the manual triggering functionality in Airflow. 

For further details, follow the specific steps outlined below.

## Needed File 1: test_manual_trigger.py (The DAG)
This is the DAG definition file that defines how the DAG behaves when triggered. 

This DAG will not run on its own; it only runs when manually triggered. The task in the DAG prints the time when it was manually triggered.

## Needed file 2: trigger.py (Manually Trigger the DAG)
This is the script that triggers the DAG. When you run trigger.py, it will use Airflow's API to manually trigger the test_manual_trigger_dag

## How to Use the Trigger in Your Own DAG
### Step 1: Keep the trigger.py file as it is to manually trigger any DAG
Change the dag_id in trigger.py to match the dag_id of the ur own DAG (e.g., "my_custom_dag")

### Step 2: Add this function in the ur own DAG file (for example, my_custom_dag.py):
- Define the DAG with tasks that u want
- The dag_id in their DAG file must match the dag_id used in trigger.py

## ➡️ How You Can Trigger Your Own DAG
- Place the DAG file (e.g., my_custom_dag.py) in the dags/ folder
- Use the existing trigger.py script to manually trigger it
```
dag_id = "my_custom_dag"  # Replace with your own DAG id
```
After that, running `trigger.py` will manually trigger their DAG.

### Step 3: Run the Manual Trigger

To manually trigger the DAG:

1. Navigate to the directory containing `trigger.py`.
2. Run the command:

   ```bash
   python trigger.py
   ```

This will trigger the `test_manual_trigger_dag` (or their custom DAG) and print the time when it was triggered.

---

### Summary

1. **Place the DAG file** in the `dags/` folder.
2. **Update `trigger.py`** to reference the correct `dag_id`.
3. **Run `trigger.py`** to manually trigger the DAG and check the printed message in the logs.





# Please ignore the Testing from my Side Below

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
