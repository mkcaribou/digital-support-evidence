"""Attach delivery groups and paper details to the coded results; write data/viz_data.json and data/evidence_results.csv."""
import csv, json, pathlib
from collections import Counter
from delivery_map import delivery, ORDER
root = pathlib.Path(__file__).resolve().parents[1]
rows = list(csv.DictReader(open(root / "data" / "evidence_results_coded.csv")))
titles = list(csv.DictReader(open(root / "data" / "paper_titles.csv")))
def title_for(paper):
    best = None
    for t in titles:
        if paper.startswith(t["key"]) or (", " in t["key"] and paper.replace(".", "").startswith(t["key"].replace(".", ""))):
            if best is None or len(t["key"]) > len(best["key"]): best = t
    if best is None: raise SystemExit("no title for " + paper)
    return best
for r in rows:
    r["delivery"] = delivery(r["paper"])
    t = title_for(r["paper"]); r.update(authors=t["authors"], year=t["year"], country=t["country"], title=t["title"], url=t["url"])
cols = ["pillar","delivery","type","paper","authors","year","country","title","url","arm","outcome","estimate","direction","unit","stars","result","sample","share_women"]
with open(root / "data" / "evidence_results.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
num = lambda x: float(x) if x not in ("", None) else None
slim = [dict(k=r["paper"], au=r["authors"], y=r["year"], c=r["country"], t=r["title"], url=r["url"], a=(r["arm"] or "").strip(),
             o=r["outcome"], r=r["result"], e=num(r["estimate"]), dir=r["direction"], u=r["unit"], s=r["stars"],
             pl=r["pillar"], d=r["delivery"], ty=r["type"], n=r["sample"]) for r in rows]
(root / "data" / "viz_data.json").write_text(json.dumps(slim, ensure_ascii=False))
print(len(slim), "results from", len({r["k"] for r in slim}), "studies")
