"""Extract target-specific passages from the normally cached publisher article.

Run from the repository root. This never modifies the publication cache.
"""
from pathlib import Path
import hashlib

source = Path('publications/url_https___oup.silverchair-cdn.com_article-minimal_1018655.md')
text = source.read_text()
doi = '10.1093/oxfordjournals.molbev.a003853'
assert doi in text
starts = [
    'Regions homologous to PFO domain III',
    'PuSR encodes a translational fusion',
    'F, Conservation between PNO',
]
ends = [' Furthermore,', ' Sequence similarity between']
quotes = [text[text.index(start):text.index(end, text.index(start))] for start, end in zip(starts[:2], ends)]
# The legend contains abbreviated species names; extract to its next panel marker.
start = text.index(starts[2]); end = text.index(' H, NADPH sulfite reductase', start)
quotes.append(text[start:end])
output = Path(__file__).with_name('README.md')
output.write_text('''# Yeast sulfite-reductase domain evidence

Source: Rotte et al. (2001), PMID:11319255,
[original article](https://doi.org/10.1093/oxfordjournals.molbev.a003853).
The publication title concerns protist pyruvate metabolism, but its Results and
Figure 3 explicitly compare the yeast sulfite-reductase subunits. These are
sequence/domain comparisons, not isolated-subunit FMN-binding measurements.
The standard PMID refresh and full-text warming did not retrieve the publisher
body into the PMID cache. This extraction preserves the inspected, normally
cached publisher text without rewriting that cache or inventing a quotation.

Source cache SHA256: `'''+hashlib.sha256(source.read_bytes()).hexdigest()+'''`.
Reproduce with `uv run python genes/yeast/MET5/MET5-source-analysis/extract_domain_evidence.py`.

## Verbatim target passages

'''+ '\n\n'.join('> '+q for q in quotes)+'''

## Interpretation

The Results identify Met10/SR-alpha with FAD and NADP domains. The Figure 3F
legend identifies PuSR as S. cerevisiae P47169 (Met5); its architecture includes
the FMN domain fused to a hemoprotein domain. This supports the domain-based
placement of FMN on Met5 rather than Met10, together with the independent
Met10 sequence study and measured FMN content of the complete holoenzyme.
It does not show direct cofactor binding by purified isolated Met5.
''')
print(output)
