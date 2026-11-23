# eck (BmEc22K, Q0PCR8) bioinformatics notes

## Motif scan (`motif_scan.py`, reads `../eck-uniprot.txt`)

Output of `python3 motif_scan.py` (2026-10-21):

```
length: 386
Brenner motif HxDhxxxN: HADYRTCN at 236-243 (H236, D238, N243)
Loose HxDxxxxN: HADYRTCN at 236-243
candidate Mg-binding D in VDW near 143
candidate Mg-binding D in VVDY near 258
candidate Mg-binding D in VDY near 259
```

Interpretation: the single Brenner phosphotransferase motif (HxDhxxxN, the
catalytic-loop signature shared by aminoglycoside phosphotransferases, choline
kinases and protein kinases) lies at 236-243, inside the SMART CHK kinase-like
domain (124-307) annotated in the UniProt record. The catalytic-loop residues are
therefore retained, consistent with this protein being an active kinase (which
was shown biochemically by Sonobe et al. 2006, PMID:16899460). The Mg-binding
candidates are pattern hits only and have not been mapped to a structure; they
are not used as evidence.

## Family placement (from the UniProt record)

- PANTHER PTHR11012 (PROTEIN KINASE-LIKE DOMAIN-CONTAINING), subfamily
  PTHR11012:SF54.
- Pfam PF02958 (EcKL), InterPro IPR004119 (EcKL), IPR015897 (CHK kinase-like).
- Scanlan and Robin 2024 (PMID:38291829) place BmEc22K in EcKL subfamily A,
  Lepidoptera clade Lep1; the other characterized ecdysteroid 22-kinase,
  Anopheles AgEcK2, is in subfamily D.

No PAINT/IBA annotation exists for this protein.
