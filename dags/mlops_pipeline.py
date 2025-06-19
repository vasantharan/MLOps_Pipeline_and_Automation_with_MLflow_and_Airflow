from data_ingestion import create_data
from create_model import train_model

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args ={
    'owner': 'techkalvi',
    'start_date': datetime(2024, 10, 27),
}

dag = DAG('mlops_pipeline', default_args= default_args, schedule_interval=None)

data_op = PythonOperator(
    task_id ="data",
    python_callable=create_data,
    dag=dag
)

train_op = PythonOperator(
    task_id ="model",
    python_callable=train_model,
    dag=dag
)

data_op >> train_op