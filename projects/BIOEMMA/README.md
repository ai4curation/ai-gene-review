---
title: "BioEMMA evaluation: supporting material"
---

# BioEMMA evaluation: supporting material

Supporting files for the [BioEMMA Evaluation](../BIOEMMA.md) project page.

| file | what it is |
|---|---|
| `bioemma_eval.py` | Fetches KEGG KGML maps and a BiGG model, runs BioEMMA with FBA, writes per-map / per-reaction tables and joins GPR genes to `genes/<SPECIES>` reviews. PEP 723 inline dependencies (`uv run`). |
| `subsystem_recall.py` | Recall of BioEMMA-retained reactions against the BiGG JSON model's own `subsystem` field, with a reason class for every dropped reaction. |
| `results/<model>_map_summary.tsv` | One row per KEGG map: reactions on the map, mapped to BiGG/SEED, retained, match route, non-zero FBA flux. |
| `results/<model>_retained_reactions.tsv` | One row per retained reaction: KEGG id, model id, flux, GPR, genes. |
| `results/<model>_gpr_review_coverage.tsv` | One row per (reaction, gene): whether the gene has a review directory. |
| `results/<model>_subsystem_recall.tsv`, `_subsystem_dropped.tsv` | Recall per (map, subsystem) and the classified drops. |
| `results/iJN1463_rn00220_escher_map.json` | Example BioEMMA output (arginine biosynthesis map for *P. putida* iJN1463); open it in [Escher](https://escher.github.io). |

Regenerate everything from the repo root (network needed on the first run):

```bash
uv run projects/BIOEMMA/bioemma_eval.py --model iJN1463 \
  --maps rn00010 rn00020 rn00030 rn00220 rn00250 rn00260 rn00270 rn00290 rn00300 \
         rn00340 rn00361 rn00362 rn00620 rn00630 rn00670 rn00770 rn00780 \
  --reviews-dir genes/PSEPK --workdir /tmp/bioemma-work --out projects/BIOEMMA/results

uv run projects/BIOEMMA/bioemma_eval.py --model e_coli_core --maps rn00010 rn00020 rn00030 \
  --workdir /tmp/bioemma-work --out projects/BIOEMMA/results

curl -sSL -o /tmp/bioemma-work/models/iJN1463.json http://bigg.ucsd.edu/static/models/iJN1463.json
uv run projects/BIOEMMA/subsystem_recall.py --model-json /tmp/bioemma-work/models/iJN1463.json \
  --retained projects/BIOEMMA/results/iJN1463_retained_reactions.tsv \
  --kgml-dir /tmp/bioemma-work/kgml --out projects/BIOEMMA/results \
  --pair rn00010="S_Glycolysis|S_Gluconeogenesis" --pair rn00020=S_TCA_Cycle \
  --pair rn00220=S_Arginine_and_Proline_Metabolism  # ... see the project page for the full list
```
