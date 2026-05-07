# Ang2 ISO Source Trace Results

Command used:

```bash
python3 genes/mouse/Ang2/Ang2-bioinformatics/trace_iso_sources.py
```

## Summary

- The local `Ang2-goa.tsv` file contains 46 `ISO` annotations for mouse `Ang2`.
- Every one of those 46 ISO rows is transferred through `GO_REF:0000119` from the same source entity, `UniProtKB:P03950` (human angiogenin/ANG).
- The current QuickGO trace divides those source terms into three buckets:
  - `34` with current direct experimental support on human ANG.
  - `4` with only inferred support on human ANG (`GO:0019731`, `GO:0045087`, `GO:0050830`, `GO:0061844`).
  - `8` with no current matching human ANG source term (`GO:0001878`, `GO:0002181`, `GO:0006898`, `GO:0005694`, `GO:0015629`, `GO:0019732`, `GO:0033554`, `GO:0036416`).
- `9` ISO terms overlap a non-ISO mouse Ang2 annotation for the same GO term in the local GOA export, so those transfers are redundant even before biological review.

## Biological Interpretation

- Mouse Ang2 is `Angrp` / angiogenin-related protein, a paralog of canonical mouse/human angiogenin rather than a simple one-to-one functional equivalent. The original biochemical characterization found that mouse Ang is angiogenic but `Angrp is not`, while Angrp still has appreciable ribonucleolytic activity toward tRNA and related substrates [PMID:8633065 "mouse Ang is potently angiogenic, but Angrp is not... Angrp has somewhat greater ribonucleolytic activity toward tRNA and dinucleotide substrates than does Ang"].
- The later structural study reinforced paralog divergence and showed that `mAng-2 is almost 80% active compared to the human form` in comparative tRNA cleavage assays, while also noting that `mAng-2 is not angiogenic` among the murine paralogues [PMID:23170778 "mAng-2 is almost 80% active compared to the human form" ; "Experiments have shown that mAng, mAng-3 and mAng-4 have angiogenic activities comparable to that of hAng, whereas mAng-2 is not angiogenic"].
- Because of that divergence, even ISO terms with real experimental support on human ANG are unsafe to accept automatically for mouse Ang2 when they concern angiogenesis, receptor binding, signaling, stress-granule biology, nuclear trafficking, or immune effector roles.

## Review Implications

- `GO:0004540` and `GO:0004549` are the main ISO terms that remain biologically plausible for Ang2, because mouse Ang2 has direct biochemical evidence for RNase/tRNA cleavage activity [PMID:8633065 "Angrp has somewhat greater ribonucleolytic activity toward tRNA and dinucleotide substrates than does Ang"] [PMID:23170778 "mAng-2 is almost 80% active compared to the human form"].
- Immune/antimicrobial ISO terms are particularly weak because their current human ANG source is itself inferred rather than experimental.
- ISO terms with no current human source term are best treated as stale transfers.
- The non-ISO experimental block in the local GOA file also contains clear homonym errors:
  - `PMID:17670746` is about angiopoietin-2, not angiogenin-2 [PMID:17670746 "High glucose increases angiopoietin-2 transcription in microvascular endothelial cells..."].
  - `PMID:25313067` and `PMID:28096417` are about angiotensin II (`AngII`) signaling and WNK4, not Ang2/angiogenin-related protein [PMID:25313067 "Angiotensin II signaling via protein kinase C phosphorylates Kelch-like 3, preventing WNK4 degradation"] [PMID:28096417 "Phosphorylation by PKC and PKA regulate the kinase activity and downstream signaling of WNK4"].
  - `PMID:29065170` is a ZNF418 cardiac hypertrophy paper that uses `Ang II` as a stimulus, not an Ang2 gene study [PMID:29065170 "effect and mechanism of zinc-finger protein 418 (ZNF418) on cardiac hypertrophy caused by ... angiotensin II (Ang II)"].
