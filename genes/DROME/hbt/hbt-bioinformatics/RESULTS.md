# hbt isoform and family-relationship analysis

Script: `compare_isoforms.py` (run with `uv run python compare_isoforms.py`; sequences are fetched live
from UniProt REST). Raw output: `compare_isoforms_output.txt`.

## Isoform structure

UniProt holds four unreviewed hbt (FBgn0264308) products: A0A6H2EJZ8 (isoform E, 1003 aa; the UniProt
gene-centric canonical), M9PFU0 (isoform A, 963 aa), Q9VK01 (isoform C, 663 aa) and Q9VK03 (isoform D,
451 aa; the benchmark accession).

- Isoform D residues 1-451 align to isoform E residues 513-963 with 451/451 identity, and likewise to
  isoform A 513-963. Isoform D is therefore an N-terminally truncated product (alternative start) that
  lacks the first 512 residues of isoform E (a region that in isoform E carries predicted coiled coils at
  30-59 and 94-121 and a disordered, low-complexity segment at 377-482) and, relative to isoform E, the
  40 C-terminal residues after position 963.
- Isoform D retains the entire Rost (PF21534) region and all six predicted transmembrane helices
  (D 40-250 = E 552-762), and the disordered Gly-rich C-terminal tail.
- Isoform C shares only D residues 1-149 (E 513-661): it carries only three of the six helices.

## Family relationship

- Isoform D vs Drosophila Rolling stone (O44252; PTHR12242:SF46): local alignment over D 22-252 /
  Rost 28-251, 67/218 identical (30.7%). This is consistent with common membership of PTHR12242 and the
  Rost Pfam domain, but they sit in different PANTHER subfamilies (SF49 vs SF46).
- Isoform D vs human AIG1 (Q9NVV5; FAHFA hydrolase whose catalytic Thr43/His134 were defined in
  PMID:27018888): 40/182 identical (22.0%), raw SW score 43. This pairwise alignment is not significant
  and does not establish homology; the coincidental mapping of AIG1 T43 onto D T80 and H134 onto D N165
  is uninterpretable. The PMID:27018888 statement that PTHR12242 members are AIG1/ADTRP-like proteins
  retaining the Thr and His came from HHpred profile comparison, which this script does not reproduce.
  Result: inconclusive; no hydrolase activity is inferred for hbt.
