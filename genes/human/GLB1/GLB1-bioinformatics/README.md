# GLB1 PAINT replay

Run from this directory with Python 3.9 or newer; only the standard library is used:

```sh
python3 replay.py --family PTHR23421 --book inputs \
  --mapping inputs/family-an-ptn.tsv.gz --ibd inputs/family-IBD.gaf \
  --raw inputs/raw-contexts.json --fasta inputs/canonical.fasta \
  --accession P16278 --paint inputs/paint.tsv --entries inputs/entries.csv \
  --agi-crosswalk inputs/agi-crosswalk.json --zfin-crosswalk inputs/zfin-crosswalk.json \
  --domain-start 30 --domain-end 360 --output results.json
```

The script parses the saved PANTHER19.0 book, resolves its literal AN/PTN mapping, joins incoming IBA contexts to IBD rows, maps experimental donors to leaves, and projects selected alignment columns. It checks exact target sequence identity across canonical FASTA, tree alignment and cluster sequence. The outputs are computed from inputs; no expected node counts, selected-node identities or residue results are hardcoded.

The full book alignment and cluster FASTA are losslessly compressed. Mapping and IBD inputs contain exact family rows from retained complete downloads; original download hashes and line numbers are in `input-provenance.json`. The family-slice replay reproduced every calculated result of the complete-input replay. Input paths, line numbers and Python version are provenance fields, not identical across those two executions.

Repeated leaf labels and cluster-only sequences remain represented. Selected donor and ancestral windows were manually examined; the entire alignment was not. This analysis does not establish experimental function, a loss-of-function event, or the activity of an alternate human product by itself.
