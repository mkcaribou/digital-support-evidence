# Digital support for small businesses

An interactive page that charts what digital and data-first support does for micro and small businesses. It draws on Caribou's evidence map of 30 impact evaluations (125 results), updated in October 2026.

**Page:** https://mkcaribou.github.io/digital-support-evidence/

## What the page shows

The page presents the evidence in three charts:

1. Results for business practices, sales and profits, by type of support.
2. Sales and profit results, by how support reached the business, from remote training to human mentoring, bundled programs, and tools or finance on their own.
3. Each result placed on its estimated effect size.

Each circle is one result: one outcome for one program variant. Hovering over or tapping a circle shows the study, its effect size and its significance level. A table at the end of the page lists every result.

## How results are coded

- **Positive impact:** the estimate is above zero and statistically significant at the 10 percent level or better.
- **Negative impact:** the estimate is below zero and significant.
- **No impact:** the estimate is not statistically significant.

Practices are measured in standard deviations; sales and profits as a percent difference to the control group. Where a paper does not report an estimate, the data record the direction and significance only.

## Repository contents

- `index.html`: the published page, self-contained apart from Google Fonts.
- `page/template.html`: the page source, with a placeholder for the data.
- `data/evidence_results_coded.csv`: one row per study arm and outcome, as coded from the evidence map.
- `data/paper_titles.csv`: authors, year, country, title and link for each study.
- `data/evidence_results.csv` and `data/viz_data.json`: the coded results joined with study details and delivery groups.
- `scripts/`: the build scripts.

## Rebuild the page

```
python3 scripts/build_data.py
python3 scripts/build_page.py
```

`scripts/code_evidence.py` recodes the results from the source workbook, which is not included in this repository:

```
python3 scripts/code_evidence.py "<path to evidence map .xlsx>"
```

Python 3.9 or later is needed, plus `openpyxl` for the recoding step.
