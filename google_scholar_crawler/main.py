from datetime import datetime
import json
import os

from scholarly import ProxyGenerator, scholarly


scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

author = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
author["updated"] = str(datetime.now())
author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}

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
