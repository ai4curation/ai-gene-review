"""Cache the curated reaction/catalyst localization omitted by the summary ETL."""
from pathlib import Path
import json
import requests

url = 'https://reactome.org/ContentService/data/query/R-MTU-936703'
r = requests.get(url, timeout=60)
r.raise_for_status()
data = r.json()
out = Path(__file__).parent
(out/'R-MTU-936703.json').write_text(json.dumps(data, indent=2)+'\n')
compartments = [c['displayName'] for c in data['compartment']]
catalysts = [c['displayName'] for c in data['catalystActivity']]
assert 'cytosol' in compartments
assert 'sulfite reductase (ferredoxin) activity of Sir holoenzyme [cytosol]' in catalysts
(out/'README.md').write_text('''# Sir reaction localization in Reactome

Source: [Reactome R-MTU-936703](https://reactome.org/content/detail/R-MTU-936703).
Reproduce: `uv run python genes/MYCTU/sir/sir-source-analysis/fetch_reactome_location.py`.
The adjacent JSON is the unmodified ContentService response, retrieved on
2026-10-26. The repository's ordinary Reactome summary cache omits these fields.

The reaction compartment displayName is:

> cytosol

Its catalystActivity displayName is:

> sulfite reductase (ferredoxin) activity of Sir holoenzyme [cytosol]

This is a curated pathway location, not a direct localization experiment.
It supports retention of the TAS cytosol annotation without treating a soluble
crystal structure as evidence of cellular localization.
''')
print(out/'README.md')
