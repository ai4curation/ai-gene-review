# dnajc6 isoform and motif comparison (re-review, 2026-10-21)

Script: `compare_isoforms_rereview.py` (stdlib + MAFFT). Sequences fetched from the
UniProt REST API: A0A8M9QG43 (benchmark entry, RefSeq XP_021332835.1), A0A8M9Q6X2
(UniProt gene-centric canonical dnajc6 product, RefSeq XP_021332834.1) and O75061
(human auxilin, DNAJC6). The canonical was identified with the UniProt gene-centric
endpoint (`/genecentric/search?query=accession:A0A8M9QG43`), which lists A0A8M9Q6X2
as canonical and A0A8M9QG43 among 25 related dnajc6 entries.

## Summary

- A0A8M9QG43 (974 aa) differs from the canonical A0A8M9Q6X2 (979 aa) only by a
  5-residue deletion (GPPSP) after residue 66, N-terminal to the tensin-type
  phosphatase domain (109-276). It is an alternative-splice isoform of dnajc6 with
  all domains intact; the J domain HPD motif is retained.
- Both zebrafish entries are 65.5% identical to human auxilin over aligned columns.
- Neither zebrafish entry nor human auxilin has a PTEN-class CX5R P-loop in the first
  400 residues. All three instead carry a shortened CX3R window at the predicted
  catalytic cysteine (zebrafish CSDGR at 218 in A0A8M9QG43, 223 in A0A8M9Q6X2; human
  CLDGR at 164). The P-loop therefore departs from the PTEN-class signature in the
  same way in zebrafish and human auxilin; the bovine auxilin 1 crystal structure
  attributes the lack of phosphatase activity to a change in P-loop structure
  (PMID:20826345). This motif scan does not itself test activity.

## Raw output

```
A0A8M9QG43	length=974
A0A8M9Q6X2	length=979
O75061	length=913

# Differences A0A8M9QG43 vs A0A8M9Q6X2 (QG43 residue coordinates)
aln 67-71	near QG43 residue 66	QG43=-----	Q6X2=GPPSP
total difference blocks: 1
A0A8M9QG43 vs O75061: identity 568/867 = 0.655
A0A8M9Q6X2 vs O75061: identity 571/872 = 0.655

# Motifs (ungapped sequence coordinates)
A0A8M9QG43	HPD at [938]	last 120 aa contains HPD: True
A0A8M9QG43	CX5R windows (first 400 aa): []
A0A8M9QG43	CX3R windows (first 400 aa, shortened auxilin-type P-loop): [(218, 'CSDGR')]
A0A8M9Q6X2	HPD at [943]	last 120 aa contains HPD: True
A0A8M9Q6X2	CX5R windows (first 400 aa): []
A0A8M9Q6X2	CX3R windows (first 400 aa, shortened auxilin-type P-loop): [(223, 'CSDGR')]
O75061	HPD at [877]	last 120 aa contains HPD: True
O75061	CX5R windows (first 400 aa): []
O75061	CX3R windows (first 400 aa, shortened auxilin-type P-loop): [(164, 'CLDGR')]
```
