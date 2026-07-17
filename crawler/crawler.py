import requests


def fetch_page(url):
    """
    Downloads the HTML content of a webpage.
    Returns the Response object if successful.
    """

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        return response

    except requests.exceptions.Timeout:
        print("[-] Error: The request timed out.")

    except requests.exceptions.ConnectionError:
        print("[-] Error: Could not connect to the website.")

    except requests.exceptions.HTTPError as err:
        print(f"[-] HTTP Error: {err}")

    except requests.exceptions.RequestException as err:
        print(f"[-] Request Error: {err}")

    return None