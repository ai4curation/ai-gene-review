# DYNC2H1 saved-input results

The actual Python replay completed successfully on 2026-10-18, and a separate read-only `--check` reproduced all four outputs from 26 pinned inputs.

| Analysis | Computed result | Interpretation boundary |
|---|---|---|
| PANTHER/PAINT | 787 tree nodes and 787 aligned sequences; target PTN002472916 reproduces the 4,307-residue Q8NCM8-1 sequence. Ten selected literal IBD records join the queried ancestral nodes; dynein-1 sibling IRDs are separately retained in the output. | Target descent and real IBD identity are verified. Biological placement remains a manual judgment; donor count and target self-grounding are not errors. |
| Reactome | Eighteen saved records produce twelve Q8NCM8 target paths from six imported reaction roots. The target spans residues 1–4307 in cilium or ciliary-tip compartments. | These are linked pathway model assertions, not twelve independent experiments. |
| IntAct and products | Forty-six returned interaction records. Two PMID:21525035 PEX14–DYNC2H1 records have target ROGIDs matching Q8NCM8-1. The query returns no PMID:29742051 record. | Absence from this interaction query does not negate the separately read 2018 tail-coimmunoprecipitation experiment. Literal accession/sequence matches do not identify a native transport mechanism. |
| Urinary exosome table | One DYNC2H1 record: NP_001073932, two peptides, reference number 2, which the table bibliography maps to PMID:19056867. | Positive protein-group detection is preserved. Peptide sequences, product specificity, secretion route and exosome function are not inferred. |

All outputs are recomputed from the archived input bytes. Source counts and target values are not hardcoded into the calculation. `outputs/paint.json` contains the selected IBD/IRD rows and target lineage; `reactome.json` contains target paths; `interactions.json` preserves the literal pair fields and ROGID matches; `exosome.json` preserves the target row and reference-number join.

The larger original-publication target survey for the male-germ-cell-nucleus assertion is deliberately separate. Its decisive evidence is positive DYNC1H1 reagent identity and the Supplementary Figure 4 target labels, with whole-text/workbook name searches as corroboration. Nuclear-envelope topology alone is not used to reject a nuclear localization term.
