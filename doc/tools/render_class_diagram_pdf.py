#!/usr/bin/env python3
"""Gera PDF do diagrama Mermaid em doc/diagrams/class-diagram-top-down.mmd."""
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
MMD = ROOT / "doc" / "diagrams" / "class-diagram-top-down.mmd"
PDF_OUT = ROOT / "doc" / "class-diagram-top-down.pdf"


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip("\n")
    return text


def main() -> None:
    diagram = strip_frontmatter(MMD.read_text(encoding="utf-8"))
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<title>Diagrama de classes</title>
<style>
body {{ margin: 0; padding: 12px; background: #fff; }}
h1 {{ font-family: system-ui, sans-serif; font-size: 13px; font-weight: 600; margin: 0 0 12px 0; }}
.mermaid svg {{ max-width: none !important; }}
</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
</head>
<body>
<h1>python.poo.biblioteca — diagrama de classes (top-down: main.py no topo)</h1>
<div class="mermaid">
{diagram}
</div>
<script>
  mermaid.initialize({{ startOnLoad: true, theme: "neutral", securityLevel: "loose" }});
</script>
</body>
</html>"""
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=".html",
        delete=False,
    ) as tmp:
        tmp.write(html)
        tmp_path = Path(tmp.name)

    uri = tmp_path.resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 3000, "height": 4200})
        page.goto(uri, wait_until="networkidle", timeout=180000)
        page.wait_for_selector(".mermaid svg", timeout=120000)
        page.pdf(
            path=str(PDF_OUT),
            format="A2",
            landscape=True,
            print_background=True,
            margin={"top": "8mm", "right": "8mm", "bottom": "8mm", "left": "8mm"},
            scale=0.58,
        )
        browser.close()
    tmp_path.unlink(missing_ok=True)
    print(f"PDF gerado: {PDF_OUT}")


if __name__ == "__main__":
    main()
