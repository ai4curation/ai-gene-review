"""Extract exact localization evidence from the normally cached PMC full text."""
from pathlib import Path
import hashlib
source=Path('publications/url_https___pmc.ncbi.nlm.nih.gov_articles_PMC2492630_.md')
s=source.read_text()
assert '18567826' in s and '10.1104/pp.108.121459' in s
start=s.index('As shown in Figure 2, immunofluorescence')
end=s.index('\nFigure 2.',start)
quote=s[start:end]
out=Path(__file__).with_name('README.md')
out.write_text('''# ARGAH1 and ARGAH2 matrix-localization evidence

Canonical paper: PMID:18567826, Flores et al. (2008),
[Arginase-negative mutants of Arabidopsis exhibit increased nitric oxide signaling
in root development](https://doi.org/10.1104/pp.108.121459).

The original paper tests the two Arabidopsis proteins as myc-tagged constructs
in tobacco BY-2 cells. These are heterologous localization experiments with the
target proteins, not native Arabidopsis fractionation. E1β marker colocalization
and selective digitonin permeabilization resolve the internal mitochondrial pool.
They do not exclude a distinct chloroplast pool under other conditions.

Normal PMID refresh and full-text warming did not recover the body into the PMID
cache. This script extracts the exact inspected passage from the normally cached
PMC source; it never edits a source cache. Reproduce from the repository root:
`uv run python genes/ARATH/ARGAH1/ARGAH1-source-analysis/extract_localization.py`.

Source SHA256: `'''+hashlib.sha256(source.read_bytes()).hexdigest()+'''`.

## Verbatim Results passage accompanying Figure 2

> '''+quote+'''

## Curation consequence

Retain the informative mitochondrial organelle assertions. Add the experimentally
resolved matrix location alongside them for both paralogs; do not substitute the
subcompartment for the organelle or convert a paper title into localization evidence.
''')
print(out)

# Preserve other already-cited Results passages under the same canonical paper.
import yaml, re
extra = []
def walk(x):
    if isinstance(x, dict):
        if x.get('reference_id') in ['file:publications/url_https___pmc.ncbi.nlm.nih.gov_articles_PMC2492630_.md', 'file:ARATH/ARGAH1/ARGAH1-source-analysis/README.md'] and x.get('supporting_text'):
            q=x['supporting_text']
            if q not in extra and q not in quote:
                assert re.sub(r'\s+', ' ', q).strip() in re.sub(r'\s+', ' ', s).strip(), q
                extra.append(q)
        for v in x.values(): walk(v)
    elif isinstance(x, list):
        for v in x: walk(v)
for g in ['ARGAH1', 'ARGAH2']:
    walk(yaml.safe_load(Path('genes/ARATH',g,g+'-ai-review.yaml').read_text()))
if extra:
    with out.open('a') as fh:
        fh.write('\n## Additional cited Results passages\n\n'+'\n\n'.join('> '+q for q in extra)+'\n')
