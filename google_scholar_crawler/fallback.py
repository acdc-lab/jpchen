from datetime import datetime
import json
import os


scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
fallback_citedby = int(os.environ.get("FALLBACK_CITEDBY", "0"))

os.makedirs("results", exist_ok=True)

author = {
    "scholar_id": scholar_id,
    "citedby": fallback_citedby,
    "publications": {},
    "fetch_error": "Google Scholar fetch timed out; fallback citation count used.",
    "updated": str(datetime.now()),
}

with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldsio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{fallback_citedby}",
}
with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
    json.dump(shieldsio_data, outfile, ensure_ascii=False)
