from airflow.models import BaseOperator
from airflow.models import Variable
from airflow.configuration import AIRFLOW_HOME
from airflow.utils.decorators import apply_defaults
from airflow.utils.email import send_email_smtp

from helpers import fetch_page

import os
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader


class BaseCheck(BaseOperator):
    @apply_defaults
    def __init__(self, name: str, link: str, description: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.link = link
        self.description = description
        self.log_str_base = f"[{self.name} - {self.description}] "

    def init_execute(self):
        self.log.info(self.log_str_base + "Checking...")

        page = fetch_page(self.link)
        return page

    def check_pass(self, checks):
        pass_check = True if True in checks else False
        result = "Probably available" if pass_check else "Not available..."
        self.log.info(self.log_str_base + result)

        notfication_email_to = None
        notfication_email_subject = None
        try:
            notification_email_to = Variable.get("PS5_notification_to")
        except Exception as err:
            pass

        try:
            notfication_email_subject = Variable.get("PS5_notification_subject")
        except Exception as err:
            pass

        if pass_check:
            base_path = AIRFLOW_HOME + "/dags/"
            env = Environment(loader=FileSystemLoader(base_path))
            tpl = None
            content = ""

            try:
                tpl = env.get_template("email.tpl")
            except Exception as err:
                self.log.error("Couldn't find template file: ", err)
                return

            try:
                content = tpl.render(
                    store=self.name, link=self.link, description=self.description
                )
            except Exception as err:
                self.log.error("Failed rendering: ", err)
                return

            send_email_smtp(
                to=notification_email_to,
                subject=notification_email_subject,
                html_content=content,
                dryrun=False,
            )

    def pass1Text(self, page: str, target: str) -> bool:
        """Checks for the given string in the page."""
        if target in page:
            return False

        return True

    def pass2Parse(self, page: str) -> bool:
        """Parses the HTML code, and tries to access the specific HTML elements."""
        ...
