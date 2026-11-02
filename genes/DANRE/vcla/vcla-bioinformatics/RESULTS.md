# vcla / vclb protein comparison with human VCL

Script: `compare_vinculins.py` (run with `uv run python genes/DANRE/vcla/vcla-bioinformatics/compare_vinculins.py`).
Raw output: `output.txt`. Global alignments, Biopython PairwiseAligner, BLOSUM62, gap open -10 / extend -0.5.
Zebrafish sequences are read from the cached UniProt records (B3DI32 = vcla, A0A0S2I7K2 = vclb); human
P18206 isoforms are fetched from the UniProt REST API.

## Results (from output.txt, 2026-09-28)

| Comparison | Identity | Columns |
|---|---|---|
| vcla (1131 aa) vs human metavinculin P18206 (1134 aa) | 85.4% | 1140 |
| vcla vs human vinculin P18206-2 (1066 aa) | 82.0% | 1131 |
| vclb (1066 aa) vs human vinculin P18206-2 | 86.0% | 1066 |
| vclb vs human metavinculin P18206 | 80.9% | 1134 |
| vcla vs vclb | 81.4% | 1131 |

- **Metavinculin insert.** Human metavinculin has a 68-aa insert (positions 911-978) that the 1066-aa
  vinculin isoform lacks. The vcla UniProt entry B3DI32 aligns 59/68 of those positions (46 identical):
  **B3DI32 is the metavinculin-type isoform of vcla**. The vclb entry A0A0S2I7K2 aligns 0/68: it is the
  vinculin-type isoform. The lower vcla-vclb identity (81.4%) is therefore partly an isoform artefact
  (about 65 insert columns are gaps). Whether the vclb gene can encode a metavinculin exon is not tested here.
- **Key residues** (numbering of human 1066-aa vinculin): A50, Y100, S1033, S1045 and Y1065 are
  conserved in both copies. **Y822 is Y in vcla and F in vclb**, confirming the Y822F substitution
  reported by Han et al. 2017 (PMID:28767718).

## Interpretation

Both copies keep the residues known to matter for talin/alpha-catenin/alpha-actinin binding (A50) and the
regulatory phosphosites tested in mammals, except Y822 in vclb. The difference between the two cached
UniProt entries in length reflects which splice isoform each entry represents, not a protein-level
divergence between the genes.
