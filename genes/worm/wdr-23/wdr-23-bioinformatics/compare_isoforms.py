"""Compare frozen WDR-23 isoform B sequence and the benchmark product."""
from pathlib import Path
import json
p=Path(__file__).resolve().parent.parent
seq=''.join((p/'wdr-23-reference-isoform-b.fasta').read_text().splitlines()[1:])
target=json.loads((p/'wdr-23-protnlm-source.json').read_text())['uniprot']['sequence']['value']
r={'reference':'P90794-2','reference_length':len(seq),'target':'S6FN32','target_length':len(target),'exact_substring_start':seq.find(target)+1 if target in seq else None}
(p/'wdr-23-bioinformatics/isoform-b-comparison.json').write_text(json.dumps(r,indent=2)+'\n')
