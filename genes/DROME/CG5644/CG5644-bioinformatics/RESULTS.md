# CG5644 versus AgEcK2: subfamily placement and catalytic-loop motif

Script: `compare_eck2.py` (run with `uv run compare_eck2.py > results-eck2.txt`).
It fetches live UniProt records for CG5644 (Q9VSS3), the biochemically
characterised Anopheles gambiae ecdysteroid 22-kinase AgEcK2 (AGAP002181,
UniProt F5HIV2) and the SF6 fly paralog CG6830 (Q9VGJ8), reports their PANTHER
and eggNOG cross-references, scans for the HxDxxxxN catalytic-loop motif of the
APH/CHK kinase fold, and computes global BLOSUM62 pairwise identities.

## Output (2026-10-21)

```
CG5644_DROME	Q9VSS3	length=459	PANTHER=PTHR11012:SF47,PTHR11012	eggNOG=ENOG502SGND	HxDxxxxN=[(289, 'HGDLWVNN')]
AgEcK2_ANOGA	F5HIV2	length=460	PANTHER=PTHR11012:SF47,PTHR11012	eggNOG=ENOG502SGND	HxDxxxxN=[(283, 'HGDTWVNN')]
CG6830_DROME	Q9VGJ8	length=891	PANTHER=PTHR11012:SF6,PTHR11012	eggNOG=ENOG502RZD1	HxDxxxxN=[(297, 'HGDCWMNN'), (548, 'HSDNDAIN'), (725, 'HGDAWINN')]
CG5644_DROME vs AgEcK2_ANOGA: 38.8% identity over 436 aligned residues
CG5644_DROME vs CG6830_DROME: 28.6% identity over 416 aligned residues
AgEcK2_ANOGA vs CG6830_DROME: 25.7% identity over 439 aligned residues
```

## Interpretation

- CG5644 and AgEcK2 are in the same PANTHER subfamily (PTHR11012:SF47) and the
  same eggNOG orthologous group (ENOG502SGND), and are nearly identical in length.
  This agrees with the published EcKL phylogeny, which places both in subfamily D,
  Diptera orthologous clade Dip14, as 1:1 orthologs (PMID:38291829, PMID:39208453).
  So CG5644 and AgEcK2 are subfamily-level orthologs, not merely best BLAST hits.
- Both proteins keep the HGDxWVNN catalytic loop (CG5644 residues 289-296), so the
  catalytic machinery of the kinase fold appears intact in CG5644.
- CG6830 is in a different PANTHER subfamily (SF6) and a different eggNOG group,
  and is less similar to either SF47 protein. Subfamily-D/SF47-specific properties
  (ecdysteroid 22-regiospecificity) are therefore not transferable to CG6830 on
  this basis.
- QuickGO returned no GO annotations for F5HIV2 (queried 2026-10-21), and no PAINT
  IBA annotation exists for CG5644. Any ecdysteroid 22-kinase claim for CG5644 is
  therefore based on orthology to AgEcK2, whose activity was shown by an in vitro
  assay (PMID:35794471). It has not been assayed biochemically in Drosophila.
