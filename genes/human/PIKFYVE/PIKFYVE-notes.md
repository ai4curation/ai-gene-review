# PIKFYVE (human, Q9Y2I7) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human PIKFYVE is the closest experimentally characterised relative of HORSE/PIKFYVE
(A0A3Q2HE51). Both are in PANTHER PTHR46715:SF1, the single PIKfyve/Fab1 subfamily, and human
Q9Y2I7 is an experimental donor for PAINT nodes PTN002928511 and PTN002928512. No ProtNLM2 output
was consulted.

### Process / provenance
- `just fetch-gene human PIKFYVE` gave 88 GOA rows. `just fetch-gene-pmids` cached 22 papers.
- Deep research failed twice. Falcon: Edison API `403 Forbidden` on `/auth/login`. The automatic
  perplexity-lite fallback and a manual `just deep-research human PIKFYVE --provider perplexity-lite`
  both hit the 600 s timeout. No deep-research file exists, so the review rests on the cached
  primary literature and the curated UniProt entry.
- Abstract-only caches: PMID:11706043, 15046600, 16448788, 17556371, 28779020.

### What is experimentally established for the HUMAN protein (use as the reference for transfer)
- PI3P 5-kinase activity (PI3P -> PI(3,5)P2). The reconstituted human PIKfyve-VAC14-FIG4 complex
  was assayed directly [PMID:33098764 "We find the PIKfyve complex comprises five copies of the
  scaffolding protein Vac14 and one copy each of the lipid kinase PIKfyve, generating PI(3,5)P2 from
  PI3P and the lipid phosphatase Fig4, reversing the reaction."]. Kinase-dead PIKfyve does not rescue
  in human cells [PMID:41639454].
- PI 5-kinase activity (PI -> PI5P) in vitro, and PIKfyve is the main cellular PI5P source
  [PMID:22621786]. Part of the PI5P may come indirectly through myotubularin action on PI(3,5)P2
  [PMID:25578879].
- Protein serine kinase activity, as autophosphorylation (S23, S48, S1522, S1669, S1969, S2053).
  This represses lipid kinase activity and stimulates FIG4 [PMID:33098764]. No trans substrate is
  known. PAINT did not propagate a protein kinase term.
- PAS complex membership (1 PIKfyve : 1 FIG4 : 5 VAC14) [PMID:33098764, PMID:18950639].
- Locations: early endosome membrane [PMID:16448788, PMID:16954148], phagosome membrane
  [PMID:30612035], late endocytic membranes, which depend on the FYVE finger [PMID:11706043; the
  construct was probably mouse PIKfyve].
- Endosome-to-TGN retrograde transport, by siRNA in HeLa cells [PMID:16954148]. The protein is NOT
  needed for receptor-mediated endocytosis (transferrin, EGFR) [PMID:14551253, PMID:16954148].
- Downstream, cell-type-specific requirements, all kept as non-core: neutrophil chemotaxis and ROS,
  phagosome-lysosome fusion, phagosome maturation, melanosome biogenesis, MHC-II presentation,
  autophagosome assembly via PI5P, EGFR nuclear transit, and STING activation (PI(3,5)P2 is a STING
  ligand). Most of these rest on inhibitor data only (apilimod, YM201636).

### Key decisions
- Removed GO:0043813 (PI(3,5)P2 5-phosphatase). This is FIG4's activity, transferred to PIKfyve
  through the Reactome complex reaction. Also removed the GO:0036092 (PI3P biosynthesis) inference
  that follows from it.
- Removed GO:0015485 (cholesterol binding) and GO:0080025 (PI(3,5)P2 binding). Both are ISS rows from
  STING1 (Q86WV6), which is not a homolog. Recorded as UniProt source_defects.
- Removed GO:0016308 (PI4P 5-kinase). PIKfyve is a type III PIPK. The TAS comes from a review on
  Btk and type I PIP5Ks (PMID:15046600), probably attached through the legacy symbol PIP5K3 (suspected
  source defect). The IDA membrane-raft row from the same review is UNDECIDED.
- Changed GO:1903100 and GO:1904562 (metabolic process) to the biosynthetic children GO:1903102 and
  GO:1904563 (ancestry checked in OLS). Changed GO:0006661 (PI biosynthesis; GO:1903102 is not under
  it) to GO:1903102.
- Refined endosome membrane to early plus late endosome membrane, and S/T kinase to serine kinase.
- Marked receptor-mediated endocytosis of virus (GO:0019065) as over-annotated. It is consistent with
  the accepted NOT receptor-mediated endocytosis row: the requirement is in post-internalisation
  maturation.
- Golgi membrane (ARBA, Reactome) marked over-annotated. No direct localisation data support it.
- NEW: GO:0032266 PI3P binding (FYVE finger) [PMID:11706043].
- IBA rows are all retained. The single-subfamily node placement is sound, and neutrophil chemotaxis
  sits on the separate node PTN002928512.

### Validation
- `just validate human PIKFYVE` passes.
