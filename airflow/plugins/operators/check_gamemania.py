from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.utils.email import send_email_smtp

from operators import BaseCheck
from helpers import fetch_page

from bs4 import BeautifulSoup


class CheckGamemania(BaseCheck):
    """Check the Gamemania stock."""

    @apply_defaults
    def __init__(self, link: str, description: str, **kwargs) -> None:
        super().__init__(name="Gamemania", link=link, description=description, **kwargs)

    def execute(self, context):
        page = self.init_execute()

        if page is not None:
            pass1 = self.pass1Text(page, target="Niet beschikbaar")
            pass2 = self.pass2Parse(page)

            self.check_pass([pass1, pass2])

            return True

        return False

    def pass2Parse(self, page: str) -> bool:
        """Parses the HTML code, and tries to access the specific HTML elements."""
        soup = BeautifulSoup(page, "html.parser")

        strong_all = soup.find_all(
            "span", attrs={"class": "other"}, text="(Niet beschikbaar)", limit=1
        )

        if len(strong_all) == 1:
            return False

        return True
