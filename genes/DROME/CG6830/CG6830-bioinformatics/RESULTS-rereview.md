# CG6830 (Q9VGJ8) re-review bioinformatics (2026-10-21)

## Catalytic motif scan

Script: `motif_scan_rereview.py` (reads `../CG6830-uniprot.txt`).

Output:

```
length=891
HxDxxxxN at 297-304: HGDCWMNN in ['CHK domain 1']
HxDxxxxN at 548-555: HSDNDAIN in no CHK domain
HxDxxxxN at 725-732: HGDAWINN in ['CHK domain 2']
```

Interpretation: both SMART CHK kinase-like domains (174-369 and 605-797) retain
an HxDxxxxN catalytic-loop motif (H297-G-D299-C-W-M-N-N304; H725-G-D727-A-W-I-N-N732),
as expected for APH/CHK-type small-molecule kinases. The hit at 548-555 lies in the
inter-domain linker and is a chance match. Motif retention is consistent with, but
does not prove, catalytic competence of either domain; no substrate can be inferred.

## Gene model

FlyBase reports one annotated transcript and one unique polypeptide for CG6830, and
UniProt Q9VGJ8 (891 aa, sequence version 1) is that product. The benchmark accession
is therefore the canonical, full-length product, not an isoform or fragment.

## PANTHER placement

UniProt places Q9VGJ8 in PTHR11012:SF6 (CHK DOMAIN OV1-RELATED). The CG31099
re-review (genes/DROME/CG31099/CG31099-bioinformatics/RESULTS-rereview.md) found that
the biochemically characterised ecdysteroid 22-kinase BmEc22K (Q0PCR8) is in SF54 and
CG5644, the fly ortholog of AgEcK2, is in SF47; CG31099 is the only other fly SF6
member, and it is also uncharacterised. No experimentally characterised SF6 member
is known.
