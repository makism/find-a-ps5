import requests
from bs4 import BeautifulSoup


def fetch_page(url: str) -> str:
    """Fetch the page from the given URL."""

    try:
        r = requests.get(url)
        return r.text

    except Exception as err:
        print(err)
        return None
