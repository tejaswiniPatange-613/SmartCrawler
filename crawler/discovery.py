import requests
from urllib.parse import urljoin


def check_common_files(base_url):

    files = [
        "robots.txt",
        "sitemap.xml",
        ".well-known/security.txt",
        "favicon.ico"
    ]

    results = []

    for file in files:

        url = urljoin(base_url, file)

        try:
            response = requests.get(url, timeout=5)

            results.append({
                "file": file,
                "url": url,
                "status": response.status_code
            })

        except requests.RequestException:

            results.append({
                "file": file,
                "url": url,
                "status": "Error"
            })

    return results