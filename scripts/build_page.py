"""Build index.html from page/template.html and data/viz_data.json."""
import pathlib
root = pathlib.Path(__file__).resolve().parents[1]
body = (root / "page" / "template.html").read_text().replace("__DATA__", (root / "data" / "viz_data.json").read_text())
head, rest = body.split("<style>", 1)
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="description" content="What digital and data-first support does for micro and small businesses: results from 30 impact evaluations, by type of support, delivery model and effect size.">\n'
        + head + "<style>" + rest.replace('<div class="wrap">', '</head>\n<body>\n<div class="wrap">', 1) + "\n</body>\n</html>\n")
(root / "index.html").write_text(html)
print("wrote index.html")
