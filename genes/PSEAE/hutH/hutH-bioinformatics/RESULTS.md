# hutH (PA5098) MIO motif check

Script: `mio_motif_check.py` (run with `uv run python mio_motif_check.py` from the repository
environment; sequences are fetched live from UniProt REST; Biopython global alignment,
BLOSUM62, gap open -10, extend -0.5; identity = identical aligned positions / shorter length).

## Output (2026-10-28)

```
PA5098_hutH (Q9HU85): length 509; first 'ASG' at 142
PA5093_HutH-like (Q9HU90): length 510; first 'ASG' at absent
Pputida_hutH (P21310): length 510; first 'ASG' at 143
P. putida MIO motif positions: 143-145
PA5098_hutH residues aligned to P. putida MIO motif: A142 S143 G144
PA5093_HutH-like residues aligned to P. putida MIO motif: Y146
identity PA5098_hutH vs PA5093_HutH-like: 0.409
identity PA5098_hutH vs Pputida_hutH: 0.821
identity PA5093_HutH-like vs Pputida_hutH: 0.400
```

## Interpretation

- PA5098 (Q9HU85) carries the MIO-forming Ala-Ser-Gly tripeptide at 142-144, aligned with
  the motif of the structurally characterised P. putida histidase (UniProt numbering 143-145,
  Ala-Ser-Gly 142-144 in the mature-protein numbering of the crystal-structure paper), and is
  82% identical to it. It is the functional histidase of PAO1.
- PA5093 (Q9HU90), the second HutH-like gene in the PAO1 hut locus, has no Ala-Ser-Gly
  tripeptide anywhere, and only one residue aligns with the P. putida motif (the other two
  positions are gapped). It is about 40% identical to both histidases. This matches the
  P. fluorescens SBW25 HutH1 paralog, which lacks the active-site residues and is genetically
  non-functional as a histidase (PMID:17717196). PA5093 is therefore unlikely to be a
  histidase, although it still receives histidase IBAs from PANTHER node PTN000796665.
