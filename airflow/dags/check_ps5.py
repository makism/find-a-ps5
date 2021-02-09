"""

"""

import sys

import json
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

from operators import CheckBol, CheckCoolblue, CheckGamemania

#
# Define the DAG and its settings.
#
default_args = {
    "owner": "Avraam Marimpis",
    "depends_on_past": False,
    "start_date": datetime(2021, 2, 1),
    "end_date": datetime(2021, 2, 14),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "catchup": False,
    "email_on_retry": False,
}

with DAG(
    dag_id="check_ps5",
    default_args=default_args,
    description="Check for PS5 stock changes.",
    # schedule_interval="@once",
    schedule_interval="*/1 * * * *",
) as dag:

    op_start = DummyOperator(task_id="begin_execution")

    t0 = CheckCoolblue(
        task_id="Coolblue_PS5_Digital",
        provide_context=True,
        link="https://www.coolblue.nl/product/865867/playstation-5-digital-edition.html",
        description="PlayStation 5 Digital Edition",
    )

    t1 = CheckBol(
        task_id="Bol_PS5_Digital",
        provide_context=True,
        link="https://www.bol.com/nl/p/sony-playstation-5-digital-edition-console/9300000004162392/",
        description="PlayStation 5 Digital Edition",
    )

    t2 = CheckGamemania(
        task_id="Gamemania_PS5_Digital",
        provide_context=True,
        link="https://www.gamemania.nl/Consoles/playstation-5/144093_playstation-5-disc-edition",
        description="PlayStation 5 Digital Edition",
    )

    op_end = DummyOperator(task_id="finish_execution")


op_start >> [t0, t1, t2] >> op_end
