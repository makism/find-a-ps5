from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from helpers import fetch_page
from operators import BaseCheck

from bs4 import BeautifulSoup


class CheckCoolblue(BaseCheck):
    """Check the Coolblue stock."""

    @apply_defaults
    def __init__(self, link: str, description: str, *args, **kwargs) -> None:
        super().__init__(
            name="Coolblue", link=link, description=description, *args, **kwargs
        )

    def execute(self, context):
        page = self.init_execute()

        if page is not None:
            pass1 = self.pass1Text(page, target="Tijdelijk uitverkocht")
            pass2 = self.pass2Parse(page)

            self.check_pass([pass1, pass2])

    def pass2Parse(self, page: str) -> bool:
        """Parses the HTML code, and tries to access the specific HTML elements."""
        soup = BeautifulSoup(page, "html.parser")

        strong_all = soup.find_all(
            "strong",
            attrs={"class": "text-color--unavailable"},
            text="Tijdelijk uitverkocht",
            limit=1,
        )

        if len(strong_all) == 1:
            return False

        return True
