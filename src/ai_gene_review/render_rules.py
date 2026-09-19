"""Render cached rule reviews and their complete index without fetching data."""

import argparse
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


def render_rules_index(cache_dir: Path) -> Path:
    """Index every review YAML, including incomplete reviews and absent metrics."""
    reviews = []
    for path in sorted(cache_dir.glob('*/*-review.yaml')):
        data = yaml.safe_load(path.read_text())
        reviews.append({
            'data': data,
            'href': path.with_suffix('.html').relative_to(cache_dir).as_posix(),
            'yaml_href': path.relative_to(cache_dir).as_posix(),
        })
    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent / 'templates'),
        autoescape=select_autoescape(['html', 'j2']),
    )
    output = cache_dir / 'index.html'
    html = env.get_template('rules_index.html.j2').render(reviews=reviews)
    output.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n')
    return output


def main() -> None:
    """Build the index, optionally rendering each cached review first."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cache_dir', type=Path, nargs='?', default=Path('rules/arba'))
    parser.add_argument('--render-reviews', action='store_true')
    args = parser.parse_args()
    if args.render_reviews:
        from ai_gene_review.etl.rule_analysis import render_rule_review_html

        for path in sorted(args.cache_dir.glob('*/*-review.yaml')):
            render_rule_review_html(path.parent.name, args.cache_dir)
    print(f'Generated {render_rules_index(args.cache_dir)}')


if __name__ == '__main__':
    main()
