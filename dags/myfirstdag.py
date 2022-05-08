from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor

from datetime import datetime, timedelta

def download_data():
    print('Inside download_data python function')
    with open('/tmp/tmpfile.txt', 'w') as f:
        f.write('my_file sample data')

with DAG(dag_id='my_first_dag', start_date=datetime(2021, 1, 1)) as dag:
    download_data = PythonOperator(
                        task_id='download_data',
                        python_callable=download_data
    )

    # fs_default is name of connection needed by FileSensor (created in the UI)
    waiting_for_file = FileSensor(
        task_id='sensor_operator',
        fs_conn_id = 'fs_default',
        filepath='tmpfile.txt'
    )


