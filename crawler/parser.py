from bs4 import BeautifulSoup


def parse_html(html):
    """
    Parse HTML using BeautifulSoup.
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup