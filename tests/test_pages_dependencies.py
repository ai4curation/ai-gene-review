"""Static dependency resolution, including missing and unsafe targets."""

from pathlib import Path

from ai_gene_review.tools.pages_dependencies import DependencyResolver


def test_missing_and_unsafe_links(tmp_path: Path, tmp_path_factory):
    outside = tmp_path_factory.mktemp("outside-pages") / "outside-pages-test.txt"
    outside.write_text("outside")
    (tmp_path / "escape.txt").symlink_to(outside)
    result = DependencyResolver(tmp_path).scan(
        Path("index.html"),
        """
        <a href="missing.pdf">missing</a><a href="missing.pdf#again">duplicate</a>
        <a href="absent/">directory</a><a href="escape.txt">symlink</a>
        <a href="../outside-pages-test.txt">outside</a><a href=".private/key">hidden</a>
    """,
    )
    assert result.missing == {Path("missing.pdf"), Path("absent/index.html")}
    assert result.existing == set()


def test_inline_import_preload_and_shared_script_document_context(tmp_path: Path):
    (tmp_path / "module.js").write_text('fetch("data.json"); import("child.js")')
    (tmp_path / "child.js").write_text('fetch("child.json")')
    for directory in ("one", "two"):
        (tmp_path / directory).mkdir()
        for name in ("data.json", "child.json"):
            (tmp_path / directory / name).write_text("{}")
    resolver = DependencyResolver(tmp_path)
    for directory, html in (
        ("one", '<script>import("../module.js")</script>'),
        ("two", '<link rel="modulepreload" href="../module.js">'),
    ):
        result = resolver.scan(Path(directory) / "index.html", html)
        assert result.missing == set()
        assert result.existing == {
            Path("module.js"),
            Path("child.js"),
            Path(directory) / "data.json",
            Path(directory) / "child.json",
        }
    assert len(resolver.script_cache) == 2
    # Caches are scoped to a build; a new build must observe changed scripts.
    (tmp_path / "module.js").write_text('fetch("new.json")')
    assert DependencyResolver(tmp_path).scan(
        Path("index.html"), '<script src="module.js"></script>'
    ).missing == {Path("new.json")}


def test_javascript_identifier_boundaries(tmp_path: Path):
    result = DependencyResolver(tmp_path).scan(
        Path("index.html"),
        """<script>
        prefetch("no1"); obj.fetch("no2"); $fetch("no3");
        fetch("real.json"); import("real.js");
    </script>""",
    )
    assert result.missing == {Path("real.json"), Path("real.js")}


def test_base_srcset_and_css_urls(tmp_path: Path):
    resolver = DependencyResolver(tmp_path)
    html = resolver.scan(
        Path("docs/index.html"),
        """
        <base href="../assets/"><base href="ignored/">
        <img srcset="small.png 1x, large%20image.png 2x">
        <style>@import "theme.css"; /* url(ignored.png) */
        body { background: url(bg.png) }</style>
    """,
    )
    assert html.missing == {
        Path("assets") / name
        for name in ("small.png", "large image.png", "theme.css", "bg.png")
    }
    css = resolver.scan(
        Path("assets/theme.css"), '@import "other.css"; src: url(font.woff2)'
    )
    assert css.missing == {Path("assets/other.css"), Path("assets/font.woff2")}


def test_off_base_links_only_flag_safe_repository_matches(tmp_path: Path):
    (tmp_path / "research").mkdir()
    (tmp_path / "research/report.md").write_text("report")
    (tmp_path / "image.png").write_text("image")
    (tmp_path / ".secret").write_text("private")
    result = DependencyResolver(tmp_path).scan(
        Path("index.html"),
        """
        <a href="/research/report.html">Report</a>
        <img src="/image.png">
        <a href="/other-project/">Other project</a>
        <a href="/.secret">Hidden</a>
        <a href="https://example.org/image.png">External</a>
    """,
    )
    assert result.off_base == {
        "https://ai4curation.io/research/report.html",
        "https://ai4curation.io/image.png",
    }
    assert result.existing == set()
    assert result.missing == set()


def test_published_markdown_url_survives_project_renderer(tmp_path: Path):
    from ai_gene_review.render_projects import process_markdown_content

    target = tmp_path / "research/report.md"
    target.parent.mkdir()
    target.write_text("research")
    url = "https://ai4curation.io/ai-gene-review/research/report.md"
    html = process_markdown_content(f"[Full details]({url})")
    result = DependencyResolver(tmp_path).scan(Path("pages/projects/report.html"), html)
    assert f'href="{url}"' in html
    assert result.existing == {Path("research/report.md")}
    assert result.off_base == set()
    assert result.missing == set()
