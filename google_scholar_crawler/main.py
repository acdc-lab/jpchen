from datetime import datetime
import json
import os
import re

import requests
from bs4 import BeautifulSoup


scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
fallback_citedby = os.environ.get("FALLBACK_CITEDBY", "0")
scholar_url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"

try:
    response = requests.get(
        scholar_url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        },
        timeout=30,
    )
    response.raise_for_status()
    lowered_html = response.text.lower()
    if "unusual traffic" in lowered_html or "not a robot" in lowered_html:
        raise RuntimeError("Google Scholar returned an anti-bot page.")

    soup = BeautifulSoup(response.text, "html.parser")
    text_parts = []
    for selector in [
        ("meta", {"name": "description"}),
        ("meta", {"property": "og:description"}),
    ]:
        node = soup.find(*selector)
        if node and node.get("content"):
            text_parts.append(node["content"])
    text_parts.append(soup.get_text(" ", strip=True))

    match = re.search(r"Cited by\s+([\d,]+)", " ".join(text_parts))
    if not match:
        raise RuntimeError("Could not locate citation count in Google Scholar page.")

    author = {
        "scholar_id": scholar_id,
        "citedby": int(match.group(1).replace(",", "")),
        "publications": [],
    }
except Exception as exc:
    print(f"Failed to fetch Google Scholar data: {exc}")
    author = {
        "scholar_id": scholar_id,
        "citedby": int(fallback_citedby),
        "publications": [],
        "fetch_error": str(exc),
    }

author["updated"] = str(datetime.now())
author["publications"] = {
    v["author_pub_id"]: v for v in author.get("publications", []) if "author_pub_id" in v
}

os.makedirs("results", exist_ok=True)

with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldsio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
    json.dump(shieldsio_data, outfile, ensure_ascii=False)
