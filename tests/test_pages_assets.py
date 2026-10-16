"""Staged template assets preserve content and load order."""

from pathlib import Path

from ai_gene_review.tools.pages_assets import share_template_assets


def test_share_exact_template_blocks_and_keep_sources(tmp_path: Path):
    templates = tmp_path / "templates"
    templates.mkdir()
    css = "<style>body { color: black; }" + " " * 1100 + "</style>"
    script = "<script>window.example = 1;" + " " * 1100 + "</script>"
    (templates / "gene_review.html.j2").write_text(css + script)
    output = tmp_path / "_site"
    pages = [
        output / "genes/human/A/A-ai-review.html",
        output / "pages/projects/B.html",
    ]
    original = (
        "<html><head>" + css + "</head><body>unchanged" + script + "</body></html>"
    )
    for page in pages:
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(original)
    saved = share_template_assets(output, pages, templates)
    total_after = sum(p.stat().st_size for p in output.rglob("*") if p.is_file())
    assert saved == 2 * len(original.encode()) - total_after
    assert saved > 0
    assets = list((output / "_pages-assets").iterdir())
    assert len(assets) == 2
    assert {p.read_text() for p in assets} == {
        css.removeprefix("<style>").removesuffix("</style>"),
        script.removeprefix("<script>").removesuffix("</script>"),
    }
    for page in pages:
        html = page.read_text()
        assert "unchanged" in html
        assert html.index('rel="stylesheet"') < html.index("</head>")
        assert html.index('src="') > html.index("unchanged")
        assert "defer" not in html and "async" not in html
        import re

        for url in re.findall(r'(?:href|src)="([^"]+)"', html):
            assert (page.parent / url).resolve().is_file()
    assert (templates / "gene_review.html.j2").read_text() == css + script
    assert share_template_assets(output, pages, templates) == 0


def test_leave_dynamic_relative_and_unrecognized_blocks_inline(tmp_path: Path):
    templates = tmp_path / "templates"
    templates.mkdir()
    blocks = [
        "<style>body { background: url(image.png); }" + " " * 1100 + "</style>",
        "<script>const gene = '{{ gene.id }}';" + " " * 1100 + "</script>",
        "<script>document.currentScript.dataset;" + " " * 1100 + "</script>",
    ]
    (templates / "gene_review.html.j2").write_text("".join(blocks))
    output = tmp_path / "_site"
    output.mkdir()
    page = output / "index.html"
    original = "".join(blocks) + "<style>unknown</style>"
    page.write_text(original)
    assert share_template_assets(output, [page], templates) == 0
    assert page.read_text() == original


def test_base_document_is_left_unchanged(tmp_path: Path):
    templates = tmp_path / "templates"
    templates.mkdir()
    block = "<style>body { color: black; }" + " " * 1100 + "</style>"
    (templates / "gene_review.html.j2").write_text(block)
    output = tmp_path / "_site"
    output.mkdir()
    page = output / "index.html"
    original = '<base href="/elsewhere/">' + block
    page.write_text(original)
    assert share_template_assets(output, [page], templates) == 0
    assert page.read_text() == original
