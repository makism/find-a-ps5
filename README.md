#### find-a-ps5
<i>Some simple Airflow pipelines to check and notify for PS5 availability.</i>

- - -

# Installation 

Place the contents of the directory `airflow/` into your local Airflow installation directory.

# Setup Airflow

## E-mail

You have to configure properly the `smtp` section in the file `airflow.cfg`.

## Variables

| variable                 | description                                     |
|--------------------------|-------------------------------------------------|
| PS5_notification_to      | the e-mail address to receive the notifications | 
| PS5_notification_subject | a one line subject of the e-mail                |


