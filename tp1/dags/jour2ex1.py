"""
Jour 2 - Exercice 1 : Branchements, capteurs et communication inter-tâches
"""
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta
import random
import logging


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


def generer_nombre():
    """Génère un nombre aléatoire et retourne la branche à exécuter."""
    nombre = random.randint(1, 100)
    logging.info(f"Nombre généré : {nombre}")
    if nombre % 2 == 0:
        return "tache_pair"
    return "tache_impair"


def tache_pair():
    logging.info("Exécution tâche PAIR")


def tache_impair():
    logging.info("Exécution tâche IMPAIR")


def tache_finale():
    logging.info("Tâche finale exécutée")


with DAG(
    dag_id="jour2ex1",
    default_args=default_args,
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["jour2"],
) as dag:

    t1 = BranchPythonOperator(
        task_id="generer_nombre",
        python_callable=generer_nombre,
    )

    t2a = PythonOperator(task_id="tache_pair", python_callable=tache_pair)
    t2b = PythonOperator(task_id="tache_impair", python_callable=tache_impair)

    t3 = PythonOperator(
        task_id="tache_finale",
        python_callable=tache_finale,
        trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS,
    )

    t1 >> [t2a, t2b] >> t3
