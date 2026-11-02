# CG31099 (Q8IMT2) re-review bioinformatics (2026-10-20)

## Catalytic motif scan

Script: `motif_scan_rereview.py` (reads `../CG31099-uniprot.txt`).

Output:

```
length=400
Brenner HxDxxxxN at 248-255: HSDCWVNN
D residues within 30 aa after N255: [261, 262, 268, 273, 285]; window=VMFKFDDSGHVEDTALLDYQLVKYGSPAID
```

Interpretation: the 400-residue product retains a single HxDxxxxN catalytic-loop
motif (H248-S-D250-C-W-V-N-N255) inside the SMART CHK domain (130-320), as expected
for an APH/CHK-type small-molecule kinase fold. Retention of the motif is consistent
with, but does not prove, catalytic competence; no substrate can be inferred from it.

## PANTHER subfamily placement of characterised EcKLs (UniProt REST, 2026-10-20)

| Protein | Accession | Organism | PANTHER subfamily |
|---|---|---|---|
| CG31099 (Dro14-0) | Q8IMT2 | D. melanogaster | PTHR11012:SF6 |
| CG6830 (Dro24-1) | Q9VGJ8 | D. melanogaster | PTHR11012:SF6 |
| BmEc22K (eck) ecdysteroid 22-kinase | Q0PCR8 | Bombyx mori | PTHR11012:SF54 |
| CG5644 (Dro42-0), ortholog of AgEcK2 | Q9VSS3 | D. melanogaster | PTHR11012:SF47 |
| CG13813 / wall (Dro38-1), subfamily A | Q9VW98 | D. melanogaster | PTHR11012:SF48 |

Query used: `https://rest.uniprot.org/uniprotkb/search?query=organism_id:7227 AND (gene:CG5644 OR gene:CG13813 OR gene:CG6830)` and
`query=organism_id:7091 AND ecdysteroid`, fields accession, gene_names, xref_panther.

Interpretation: neither biochemically characterised ecdysteroid 22-kinase
(BmEc22K, SF54; AgEcK2 via its fly ortholog CG5644, SF47) shares PANTHER subfamily
SF6 with CG31099. The only other D. melanogaster SF6 member, CG6830, is itself
uncharacterised. No experimentally characterised SF6 member was found.
