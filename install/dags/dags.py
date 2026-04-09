from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


default_args = {

    'owner' : 'airflow',
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5),

}


def print_hello():
    print('hello from airflow')

def print_hello2():
    print('hello from 2')

with DAG(
    dag_id = 'salut',
    default_args = default_args,
    start_date=datetime(2021,1,1),
    schedule='@daily',
) as dag:


    t1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "hello world"',
        retries=3
    )


    t2 = BashOperator(
        task_id='print_hello2',
        bash_command='echo "hello from task 2"',
        retries=3
    )

    t1 >> t2