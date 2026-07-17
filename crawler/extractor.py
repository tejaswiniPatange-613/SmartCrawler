from urllib.parse import urljoin, urlparse


def extract_links(soup, base_url):
    """
    Extract all unique and valid links from a webpage.
    """

    links = set()

    for tag in soup.find_all("a"):

        href = tag.get("href")

        if not href:
            continue

        if href.startswith(("mailto:", "javascript:", "tel:", "#")):
            continue

        absolute_url = urljoin(base_url, href)

        links.add(absolute_url)

    return sorted(links)


def classify_links(links, base_url):
    """
    Separate links into internal and external.
    """

    internal_links = []
    external_links = []

    base_domain = urlparse(base_url).netloc

    for link in links:

        link_domain = urlparse(link).netloc

        if link_domain == base_domain:
            internal_links.append(link)
        else:
            external_links.append(link)

    return internal_links, external_links


def extract_images(soup, base_url):
    """
    Extract image URLs.
    """

    images = set()

    for img in soup.find_all("img"):

        src = img.get("src")

        if src:
            images.add(urljoin(base_url, src))

    return sorted(images)


def extract_js_files(soup, base_url):
    """
    Extract JavaScript files.
    """

    js_files = set()

    for script in soup.find_all("script"):

        src = script.get("src")

        if src:
            js_files.add(urljoin(base_url, src))

    return sorted(js_files)


def extract_css_files(soup, base_url):
    """
    Extract CSS files.
    """

    css_files = set()

    for css in soup.find_all("link"):

        rel = css.get("rel")

        if rel and "stylesheet" in rel:

            href = css.get("href")

            if href:
                css_files.add(urljoin(base_url, href))

    return sorted(css_files)


def extract_forms(soup):
    """
    Extract all forms from the webpage.
    """

    return soup.find_all("form")