# vps-15 (Q23669) notes

Deep research failed on 2026-10-08 (falcon exit 137; perplexity provider unavailable). No
deep-research file. PubMed searches ("vps-15 elegans", "ZK930.1 OR VPS-15 OR Vps15 OR PIK3R4 AND
elegans") found no paper that studies worm VPS-15 directly. GOA has no PMID-backed rows.

## Accession choice
ZK930.1 (WBGene00014151) has two TrEMBL entries: Q23669 (ZK930.1a, 1354 aa, full length with
pseudokinase, HEAT and WD40 regions, 16 GOA rows) and E9P864 (ZK930.1b, 445 aa, a C-terminal
WD40-only fragment, 3 IEA rows). Q23669 is the full-length protein and is used here.

## Key findings
- Worm literature names VPS-15 as a subunit of the class III PI3K [PMID:26783301 "the class III PI3K complex, which is composed of VPS-34, BEC-1, and VPS-15/p150"].
- Human VPS15 is a GTP-binding pseudokinase [PMID:39913640 "Finally, we found that VPS15PKD is an unusual pseudokinase that binds GTP instead of ATP"].
- Gatekeeper arginine conserved in worm (R101, aligned to human R103):
  `vps-15-bioinformatics/RESULTS.md`, script `gatekeeper_check.py`.

## Curation decisions
- All protein kinase / kinase / transferase activity rows (IBA, IEA) -> REMOVE, matching the
  human PIK3R4 review (genes/human/PIK3R4).
- ATP binding IEA -> MARK_AS_OVER_ANNOTATED (likely GTP).
- Nucleus-vacuole junction IBA -> MARK_AS_OVER_ANNOTATED (fungal-specific contact site).
- Complexes I and II, macroautophagy, late endosome to vacuole transport -> ACCEPT.
- Core functions: contributes_to GO:0016303 in PI3KC3-C1 (autophagy) and PI3KC3-C2 (endosomal).
