"""

"""

import sys

import json
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

from operators import CheckBol, CheckCoolblue, CheckGamemania, CheckNedgame, CheckBcc

#
# Define the DAG and its settings.
#
default_args = {
    "owner": "Avraam Marimpis",
    "depends_on_past": False,
    "start_date": datetime(2021, 2, 1),
    # "end_date": datetime(2021, 2, 14),
    "retries": 10,
    "retry_delay": timedelta(minutes=5),
    "catchup": False,
    "email_on_retry": False,
}

with DAG(
    dag_id="check_ps5",
    default_args=default_args,
    description="Check for PS5 stock changes.",
    #schedule_interval="@once",
    schedule_interval="*/1 * * * *",
) as dag:

    op_start = DummyOperator(task_id="begin_execution")

    t_coolblue_digital = CheckCoolblue(
        task_id="Coolblue_PS5_Digital",
        link="https://www.coolblue.nl/product/865867/playstation-5-digital-edition.html",
        description="PlayStation 5 Digital",
    )

    t_coolblue_disk = CheckCoolblue(
        task_id="Coolblue_PS5_Disk",
        link="https://www.coolblue.nl/product/865866/playstation-5.html",
        description="PlayStation 5 Disk Edition",
    )

    t_bol_digital = CheckBol(
        task_id="Bol_PS5_Digital",
        link="https://www.bol.com/nl/p/sony-playstation-5-digital-edition-console/9300000004162392/",
        description="PlayStation 5 Digital",
    )

    t_bol_disk = CheckBol(
        task_id="Bol_PS5_Disk",
        link="https://www.bol.com/nl/p/sony-playstation-5-console/9300000004162282",
        description="PlayStation 5 Disk Edition",
    )

    t_nedgame_digital = CheckNedgame(
        task_id="Nedgame_PS5_Digital",
        link="https://www.nedgame.nl/playstation-5/playstation-5-digital-edition-bundel/6481373393/",
        description="PlayStation 5 Digital",
    )

    t_nedgame_disk = CheckNedgame(
        task_id="Nedgame_PS5_Disk",
        link="https://www.nedgame.nl/playstation-5/playstation-5-disc-version-bundel/9820628451/",
        description="PlayStation 5 Disk",
    )

    t_bcc_bundle = CheckBcc(
        task_id="BCC_PS5_Bundle",
        link="https://www.bcc.nl/gaming/playstation/playstation-5-console/playstation-5-bundel-met-extra-controller/302239",
        description="PlayStation 5 Bundle with Extra Controller",
    )

    t_gm_digital = CheckGamemania(
        task_id="Gamemania_PS5_Digital",
        link="https://www.gamemania.nl/Consoles/playstation-5/144093_playstation-5-disc-edition",
        description="PlayStation 5 Digital Edition",
    )

    op_end = DummyOperator(task_id="finish_execution")


op_start >> [
    t_coolblue_digital,
    t_coolblue_disk,
    t_bol_digital,
    t_bol_disk,
    t_nedgame_disk,
    t_nedgame_digital,
    t_bcc_bundle,
    t_gm_digital,
] >> op_end
