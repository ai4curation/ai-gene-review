# RGLG4 (At1g79380, Q9SAL0) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: RGLG4 is the experimentally characterised Arabidopsis member of PANTHER
subfamily PTHR45751:SF16, used as the reference relative for rice Q6YYC5. This review
treats RGLG4 in its own right; no ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon ARATH RGLG4 --fallback perplexity-lite` failed: falcon
returned `Failed to authenticate` (403) and the perplexity-lite fallback returned
`insufficient_quota` (401). No deep-research file exists; this review is built from the
cached literature below, a PubMed search for RGLG3/RGLG4/RGLG1/RGLG2/RGLG5, the UniProt
record and the PANTHER/PAINT family files.

### Literature directly on RGLG4

- PMID:22898498 (Zhang et al. 2012, abstract only in cache). In vitro E3 activity for
  both RGLG3 and RGLG4 ["Both RGLG3 and RGLG4 possessed ubiquitin ligase activities"];
  rglg3 rglg4 double mutant attenuates MeJA/coronatine root inhibition, JA-responsive
  gene expression, wound responses and wound-induced JA biosynthesis; the double mutant
  is resistant to coronatine-producing Pst DC3000 ["rglg3 rglg4 was resistant to the
  coronatine-secreting pathogen Pseudomonas syringae pv tomato DC3000"]. Authors'
  conclusion: "essential upstream modulators of JA signaling". Single mutants have no
  phenotype (UniProt), so the genetic evidence is redundant RGLG3/RGLG4 function.
- PMID:23073017 (addendum, full text). RGLG3/4 do not interact in Y2H with COI1, AXR1,
  MYC2/3/4 or CYP94B3; "RGLG3 and RGLG4 likely catalyze only Lys 48-type
  ubiquitination", unlike RGLG2 (K48 + K63). SA represses RGLG3/4 promoters
  NPR1-independently; rglg3 rglg4 moderates SA suppression of PDF1.2.
- PMID:25788731 (full text). GFP-RGLG4 in cytoplasm and nucleus (DAPI), resembling free
  GFP; FLAG-RGLG4 found in both nuclear and cytoplasmic fractions with H3/GDPase markers.
  RGLG3/4 positively and redundantly promote FB1-induced PCD; RING-domain mutants do not
  promote PCD, i.e. E3 activity is required. FB1 suppresses RGLG4 (induces RGLG3)
  expression.
- PMID:27497447 (abstract only). Substrate trapping with RING-dead RGLG3/RGLG4 identified
  GRXS17 (Q9ZPH2) as substrate; UBC30 (Q9FKT3) is a cognate E2 that interacts with RGLG3
  and RGLG4; GRXS17 is ubiquitinated and degraded in an RGLG3-/RGLG4-dependent manner
  in planta; GLB3 (Q67XG0) binds RGLG3/4 and appears to inhibit RGLG3 activity. The in
  vitro E2-dependent reconstitution named in the abstract is for RGLG3
  (auto-ubiquitination) and GRXS17 ubiquitination; the abstract does not say whether RGLG4
  itself was tested in vitro with UBC30.
- PMID:28887381 (HDA, membrane-protein correlation profiling). RGLG4 not named in the
  main text; the mitochondrion call presumably comes from supplementary data. No focused
  study places RGLG4 in mitochondria.

### Evolutionary grounding

- UniProt: PANTHER PTHR45751:SF16 "E3 UBIQUITIN-PROTEIN LIGASE RGLG4"; VWFA (79-299)
  + C-terminal RING (357-390). In the family entries file, the reviewed Arabidopsis
  paralogs sit in different subfamilies: RGLG1 SF15, RGLG2 SF29, RGLG3 SF11, RGLG5 SF30.
  RGLG4 is the only reviewed Arabidopsis protein in SF16.
- PAINT node PTN002247669 (seeds RGLG1-4 + rice Q69V56) carries IBD only for
  GO:0004842 ubiquitin-protein transferase activity, GO:0005634 nucleus and GO:0016567
  protein ubiquitination. PAINT did NOT propagate RGLG1's IDA protein K63-linked
  ubiquitination (GO:0070534, PMID:17586653) or the RGLG1/RGLG2 plasma-membrane IDA. I
  treat those omissions as deliberate, consistent with RGLG3/RGLG4 being a separate
  subclade (PMID:35743207, "representing a subclade different from the RGLG1 and RGLG2
  clade") that forms K48 rather than K63 chains.
- RGLG1/RGLG2 begin MG(G/T)GNSKE (canonical N-myristoylation, documented for RGLG2,
  PMID:17586653); RGLG4 begins MTMGNFLKRF, lacking Gly2, consistent with its
  soluble nucleo-cytoplasmic distribution. Membrane association should therefore not be
  transferred from RGLG1/2 to RGLG4.

### Decisions summary

- MF: ligase activity is experimental (IDA, PMID:22898498) and RING-dependent in vivo
  (PMID:25788731). GO:0004842 rows -> MODIFY to GO:0061630 ubiquitin protein ligase
  activity (more specific, RING E3); GO:0061630 IEA ACCEPT.
- IPI protein binding: UBC30 row -> MODIFY to GO:0031624 ubiquitin conjugating enzyme
  binding; GRXS17 and GLB3 rows REMOVE (uninformative; interactions real).
- CC: nucleus and cytoplasm ACCEPT (IDA + IBA/IEA); mitochondrion HDA
  MARK_AS_OVER_ANNOTATED.
- BP: protein ubiquitination IBA ACCEPT; JA-mediated signaling IMP -> MODIFY to
  GO:2000022 regulation of JA mediated signaling pathway (RGLG3/4 are modulators upstream
  of COI1, targets unknown; no "positive regulation" child term exists in GO); response to
  wounding KEEP_AS_NON_CORE; defense response to bacterium MARK_AS_OVER_ANNOTATED (the
  double mutant is more resistant; the effect is an indirect consequence of
  JA signaling/coronatine hijacking, not RGLG4 executing defense).
- No NEW terms. Proteasome-mediated degradation of GRXS17 is plausible (UniProt curated
  text) but rests on an abstract-only paper and no RGLG paralog carries
  GO:0043161 despite PP2CA degradation evidence for RGLG1/5; raised as a question.
