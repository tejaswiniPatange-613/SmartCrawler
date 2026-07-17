from urllib.parse import urlparse


def normalize_url(url):
    """
    Ensure the URL has a valid scheme.
    """

    url = url.strip()

    parsed = urlparse(url)

    if not parsed.scheme:
        url = "https://" + url

    return url