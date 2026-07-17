import json
import os


def save_json_report(data, filename="report.json"):
    """
    Save crawler results into a JSON report.
    """

    os.makedirs("reports", exist_ok=True)

    filepath = os.path.join("reports", filename)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"\n[+] Report saved to: {filepath}")