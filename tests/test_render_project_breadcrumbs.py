"""Project breadcrumbs must resolve to the site and project indexes at any depth."""
from pathlib import Path

from bs4 import BeautifulSoup
import pytest

from ai_gene_review.render_projects import render_project


@pytest.mark.parametrize('subfolder', ['', 'GROUP', 'GROUP/support'])
def test_breadcrumb_destinations(tmp_path: Path, subfolder: str) -> None:
    """Nested reports retain the same Home and Projects destinations."""
    projects = tmp_path / 'projects'
    source = projects / subfolder / 'report.md'
    source.parent.mkdir(parents=True)
    source.write_text('# Report\n\nBiological findings.\n')
    genes = tmp_path / 'genes'
    genes.mkdir()
    output = tmp_path / 'pages' / 'projects'
    output.mkdir(parents=True)
    project_index = output / 'index.html'
    home = tmp_path / 'index.html'
    project_index.write_text('Projects')
    home.write_text('Home')

    rendered, _ = render_project(source, output_dir=output, genes_dir=genes, projects_dir=projects)
    soup = BeautifulSoup(rendered.read_text(), 'html.parser')
    links = soup.select('nav.breadcrumb a')
    assert len(links) == 2
    destinations = []
    for link in links:
        href = link.get('href')
        assert isinstance(href, str)
        destinations.append((rendered.parent / href).resolve())
    assert destinations == [home.resolve(), project_index.resolve()]
