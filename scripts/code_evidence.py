"""Code the MSEs tab of the evidence map into one row per study arm x outcome.

Source: Caribou evidence map workbook (not included), sheet "MSEs" (rows 3 to the last filled row).
Rule: positive = estimate above zero and significant (any star, p<0.10); negative = below zero and significant;
none = estimate reported without significance ("no impact" on the page). Blank or N/A = not tested (dropped).
Some rows use "positive"/"negative" where no estimate was extracted, "n.s." for not significant,
and "sig." for significant at an unextracted level.
Fuchs et al. (Kenya, preliminary results without estimates) is left out.
"""
import csv, pathlib, openpyxl
import sys
# The source workbook is not part of this repository. Pass its path as the first argument.
if len(sys.argv) < 2: raise SystemExit("usage: python scripts/code_evidence.py <path to evidence map .xlsx>")
src = pathlib.Path(sys.argv[1])
ws = openpyxl.load_workbook(src, data_only=True)["MSEs"]
OUT = {"Knowledge and capabilities": (4, 5, "SD"), "Business practices": (7, 8, "SD"),
       "Sales or revenue": (10, 11, "%"), "Profits": (13, 14, "%"), "Other outcomes": (17, 18, "var")}
PILLAR = {"DIGITAL UPSKILLING": "Digital training and mentoring", "BUNDLED INTERVENTIONS": "Bundled support",
          "DBO": "Data, platforms and business tools", "DFS": "Digital finance"}
EXCLUDE = ("Fuchs et al.",)
rows, pillar, typ, paper, sample, women, other_var = [], None, None, None, None, None, None
for i, r in enumerate(ws.iter_rows(min_row=3, values_only=True), 3):
    if not any(r[:22]): break
    if r[0]: pillar = PILLAR[r[0].strip()]
    if r[2]: paper, typ, sample, women, other_var = r[2], r[1], r[20], r[21], None
    if r[16]: other_var = r[16]
    if paper.startswith(EXCLUDE): continue
    for outcome, (vi, si, unit) in OUT.items():
        v, s = r[vi], (r[si] or "")
        s = s.strip() if isinstance(s, str) else s
        if isinstance(v, str) and v.strip().upper() == "N/A": v = None
        if v is None and not s: continue
        sign = None
        if isinstance(v, str): sign, v = v.strip().lower(), None
        if s and s != "n.s.":
            pos = (v > 0) if v is not None else (sign != "negative")
            cls = "positive" if pos else "negative"
        else:
            cls = "none"
        rows.append(dict(pillar=pillar, type=typ, paper=paper, arm=r[3], outcome=outcome, estimate=v,
                         direction=sign or "", unit=unit if outcome != "Other outcomes" else other_var,
                         stars="" if s == "n.s." else s, result=cls, sample=sample, share_women=women))
out = pathlib.Path(__file__).resolve().parents[1] / "data" / "evidence_results_coded.csv"
with out.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
