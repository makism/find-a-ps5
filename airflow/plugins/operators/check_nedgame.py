from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from helpers import fetch_page
from operators import BaseCheck

from bs4 import BeautifulSoup


class CheckNedgame(BaseCheck):
    """Check the Coolblue stock."""

    @apply_defaults
    def __init__(self, link: str, description: str, *args, **kwargs) -> None:
        super().__init__(
            name="Nedgame", link=link, description=description, *args, **kwargs
        )

    def execute(self, context):
        page = self.init_execute()

        if page is not None:
            pass1 = self.pass1Text(page, target="Uitverkocht")
            pass2 = self.pass2Parse(page)

            self.check_pass([pass1, pass2])

            return True

        return False

    def pass2Parse(self, page: str) -> bool:
        """Parses the HTML code, and tries to access the specific HTML elements."""
        soup = BeautifulSoup(page, "html.parser")

        div_main = soup.find("div", attrs={"class": "koopdiv"})
        div_result = div_main.find_all(
            "div", attrs={"class": "title"}, text="Uitverkocht", limit=1
        )

        if len(div_result) == 1:
            return False

        return True
