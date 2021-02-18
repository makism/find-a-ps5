 

             ¡
             █████▄ç
             ███ ▐███          ▀▀▀▀▀▀▀▀▀▀▀██⌐      ▄█▀▀▀▀▀▀  ██▀▀▀▀▀▀▀▀▀▀▀▀
             ███ ▐███                     ▄█▌     ▐█▌        ██
             ███ ╘██▀          ▄█▀▀▀▀▀▀▀▀▀▀╘      ▐█▌        └▀▀▀▀▀▀▀▀▀▀▀█▄
      ▄▄▄██▀ ███ ███▀▀██▄,     ██                 ██▌                   ╓██
     ╙▀██▄▄█ ███ ▄▄▄███▀▀      ▀▀           ▀▀▀▀▀▀▀¬         ▀▀▀▀▀▀▀▀▀▀▀▀╙   `
             ▀▀█▐▀▀┘   '£

<i>Some simple Airflow pipelines to check and notify for PS5 availability.</i>

- - -

## Stores

Currently the pipelines probe the following stores:

- Coolblue
- Bol
- BCC
- Nedgame
- Gamemania

## Installation 

Place the contents of the directory `airflow/` into your local Airflow installation directory.

## Setup Airflow

### Notifications

1. Telegram

You have to create a group, and your own bot. Then fill in the following variables in airflow:

| variable            | description  |
|---------------------|--------------|
| TELEGRAM_BOT_TOKEN  | 'xxx:xxx'    |
| TELEGRAM_CHAT_ID    | '-xxxx'      |

2. E-mail

You have to configure properly the `smtp` section in the file `airflow.cfg`.

| variable                 | description                                     |
|--------------------------|-------------------------------------------------|
| PS5_notification_to      | the e-mail address to receive the notifications |
| PS5_notification_subject | a one line subject of the e-mail                |


