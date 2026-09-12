"""Extract the Ptk7 row, headers and caption from PMID:27002738 Table 1.
Input is the unmodified Europe PMC full-text XML snapshot, PMID:27002738.
Run with UV_NO_SYNC=1 uv run python extract_kidney_table.py.
"""
from pathlib import Path
from lxml import etree
here=Path(__file__).resolve().parent
root=etree.parse(str(here.parent/'Ptk7-PMC4804176-fulltext.xml'))
lines=['# Primary kidney-phenotype table: PMID:27002738','','Source: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4804176/fullTextXML','']
for table in root.xpath('//table-wrap'):
 rows=[row for row in table.xpath('.//tr') if any('Ptk7' in ''.join(c.itertext()) for c in row)]
 if not rows:continue
 lines+=[' '.join(table.xpath('./label//text()')+table.xpath('./caption//text()')),'']
 headers=table.xpath('.//thead/tr')
 for row in headers+rows:
  lines.append(' | '.join(' '.join(''.join(c.itertext()).split()) for c in row))
 lines+=['']
(here/'kidney-table.md').write_text('\n'.join(lines)+'\n')
