from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def print_start():
    print("début du dag")

def print_end():
    print("fin du dag")

def print_date():
    print(datetime.now())

default_args = {
    'owner' : 'airflow',
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5),

}
with DAG(
    dag_id='exercice1',
    default_args=default_args,
    start_date=datetime(2021, 1, 1),
    schedule='@daily',
) as dag:

    t1 = BashOperator(
        task_id='print_start',
        bash_command='echo start',
    )


    t2 = PythonOperator(
        task_id='print_date',
        python_callable=print_date,
    )

    t3 = BashOperator(
        task_id='print_end',
        bash_command='echo end',
    )

    t1 >> t2 >> t3
