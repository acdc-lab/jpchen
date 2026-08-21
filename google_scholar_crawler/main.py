from datetime import datetime
import json
import os
import signal

from scholarly import scholarly


scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
fallback_citedby = os.environ.get("FALLBACK_CITEDBY", "0")
fetch_timeout = int(os.environ.get("SCHOLAR_FETCH_TIMEOUT", "45"))


def timeout_handler(signum, frame):
    raise TimeoutError(f"Google Scholar fetch exceeded {fetch_timeout} seconds")

try:
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(fetch_timeout)
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
except Exception as exc:
    print(f"Failed to fetch Google Scholar data: {exc}")
    author = {
        "scholar_id": scholar_id,
        "citedby": int(fallback_citedby),
        "publications": [],
        "fetch_error": str(exc),
    }
finally:
    signal.alarm(0)

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
