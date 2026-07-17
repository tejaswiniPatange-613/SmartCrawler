from crawler.crawler import fetch_page
from crawler.parser import parse_html
from crawler.extractor import (
    extract_links,
    classify_links,
    extract_images,
    extract_js_files,
    extract_css_files,
    extract_forms,
)
from crawler.utils import normalize_url
from crawler.reporter import save_json_report
from crawler.discovery import check_common_files


def main():

    print("=" * 50)
    print("        SmartCrawler v1.0")
    print("=" * 50)

    # Get URL from user
    url = input("Enter Website URL: ")
    url = normalize_url(url)

    # Fetch webpage
    response = fetch_page(url)

    if response is None:
        print("\nCrawler stopped.")
        return

    # Response Information
    print("\n========== RESPONSE INFORMATION ==========\n")

    print(f"Status Code : {response.status_code}")
    print(f"Final URL   : {response.url}")
    print(f"Encoding    : {response.encoding}")
    print(f"Content Type: {response.headers.get('Content-Type')}")
    print(f"Server      : {response.headers.get('Server')}")
    print(f"Content Size: {len(response.text)} characters")

    # First 500 Characters
    print("\n========== FIRST 500 CHARACTERS ==========\n")
    print(response.text[:500])

    # Parse HTML
    soup = parse_html(response.text)

    # Page Title
    print("\n========== PAGE TITLE ==========\n")

    if soup.title:
        print(soup.title.text.strip())
    else:
        print("No title found.")

    # Extract Links
    links = extract_links(soup, response.url)

    # Classify Links
    internal_links, external_links = classify_links(
        links,
        response.url
    )


    images = extract_images(soup, response.url)

    js_files = extract_js_files(soup, response.url)

    css_files = extract_css_files(soup, response.url)

    forms = extract_forms(soup)
    common_files = check_common_files(response.url)

    # Display Links
    print("\n========== LINKS FOUND ==========\n")

    for link in links:
        print(link)

    print("\n========== SUMMARY ==========\n")
    print(f"Total Links     : {len(links)}")
    print(f"Internal Links  : {len(internal_links)}")
    print(f"External Links  : {len(external_links)}")

    print("\n========== ASSETS ==========\n")

    print(f"Images Found      : {len(images)}")
    print(f"JavaScript Files  : {len(js_files)}")
    print(f"CSS Files         : {len(css_files)}")
    print(f"Forms Found       : {len(forms)}")

    print("\n========== COMMON FILES ==========\n")

    for item in common_files:
        print(f"{item['file']:30} {item['status']}")

    # Create Report
    report = {
    "url": response.url,
    "status_code": response.status_code,
    "title": soup.title.text.strip() if soup.title else "No Title",
    "total_links": len(links),
    "internal_links": internal_links,
    "external_links": external_links,
    "images": images,
    "javascript_files": js_files,
    "css_files": css_files,
    "forms_found": len(forms),
    "common_files": common_files
}
    # Save JSON Report
    save_json_report(report)


if __name__ == "__main__":
    main()