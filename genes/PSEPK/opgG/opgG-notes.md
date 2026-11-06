# OpgG review notes

## 2026-11-06 comparative audit

Reviewed all eight historical rows (seven machine annotations plus one inherited NEW from before this audit). The original NEW GO0033913 payload and action remain intact. No new rows were added. The review is COMPLETE because all curation decisions are explicit, not because every native reaction is known.

PMID37735577 directly assayed BL21(DE3) CAQ31569.1 signal-deleted, C-terminal His6 OpgG; its native precursor is identical to K-12 P33136. Exact sequence and residue mapping are in opgG-source-analysis/. KT2440 D268/R327/D356 and S410/L412 match the homolog's catalytic-pocket/OpgG-like Loop A residues; Y56F differs. The direct assay is not on KT2440. Relative activity is 0.79% at 8 mg/mL substrate and OpgG specific activity 0.11 U/mg; no inferred 1000-fold ratio, failed rescue assay, or Michaelis–Menten constants are claimed.

The historical intrinsic hydrolase proposal is retained as a specific homology-based chemical-capability inference. The original description/core incorrectly treated hydrolysis as established physiological OPG processing. The revised core records conserved OPG participation and inferred periplasmic action with the exact glycan reaction unresolved; it does not substitute carbohydrate binding or invent a new MF merely to fill a slot. Primary authors explicitly leave transglycosylation/cofactor alternatives open. The broad carbohydrate-binding row is refined to polysaccharide binding based on the homolog's bound Sop16 and target pocket/family evidence; this ancillary recognition is not a replacement core.

Current QuickGO confirms the GO0033913 hydrolysis definition, polysaccharide-binding child relation, and OPG-biosynthesis descendants of the broad carbohydrate/glucan process terms. GO1900727 is not a descendant of GO0051274 in the retrieved closure; that refinement explicitly describes a pathway-specific lateral interpretation. All location statements are curated homology/prediction rather than a KT2440 assay. PMID17906125 is PA14 (not KT2440) and abstract-only; PMID15313617 is abstract-only structural/branching hypothesis, not proven catalysis.

Genuine OpenScientist research and its PDF/HTML artifacts were available and preserved byte-for-byte. No provider rerun was needed. Its asserted native hydrolytic processing is qualified against the primary evidence; no fake provider output was created. No source publication was refreshed or hand-edited. Scoped computational analysis is reproducible with `uv run python genes/PSEPK/opgG/opgG-source-analysis/map_opgg.py`.
