# PPH21 (YDL134C, UniProt P23594) — curation notes

## Identity and redundancy

- PPH21 and PPH22 were cloned as the two yeast PP2A catalytic-subunit genes; they are
  linked on chromosome IV, <10% divergent from each other, and 74% identical to rabbit
  PP2Ac [PMID:2176150 "The two PPH genes show less than 10% amino acid sequence
  divergence from each other and while disruption of either PPH gene alone is without any
  major effect, the double disruption is lethal."].
- The two genes account for essentially all measurable PP2A activity
  [PMID:2176150 "Measurement of type 2A protein phosphatase activity in yeast strains
  lacking one or other of the genes indicates that they account for most, if not all,
  protein phosphatase 2A activity in the cell."]. In other backgrounds the double mutant
  is viable but very sick (G2 accumulation, aberrant buds, disorganised actin); the
  pph21-102 ts allele fails to enter mitosis with short spindles
  [file:yeast/PPH21/PPH21-deep-research-falcon.md "The clearest phenotype of reduced
  canonical PP2A function is defective G2/M progression and polarized growth."].
- UniProt: 5620 molecules/cell (PMID:14562106); Leu-369 methyl ester by Ppm1, removed by
  Ppe1 (PMID:11060018, PMID:11697862); Leu-99/Glu-102/Glu-103 needed for Tap42 binding
  (PMID:14551259); Mn2+-dependent (by similarity).
- Every process-level phenotype in the GOA set is a pph21 pph22 double-mutant or
  B-subunit-mutant result. Redundancy with Pph22 is therefore treated explicitly in each
  review block; nothing in the literature distinguishes the two catalytic subunits
  functionally (deep research: "Most pathway phenotypes ... were measured after combined
  perturbation of PPH21 and PPH22").

## Biogenesis and complexes (PMID:17550305, full text)

- HA-Pph21 activity toward phosphorylase a drops to ~25% in tpd3Δ and is also low in
  rrd1Δ rrd2Δ; free C subunit is a low-activity conformer that Rrd2 + Tpd3 switch on
  [PMID:17550305 "Here we show that the generation of the catalytically active C subunit
  depends on the physical and functional interaction between RRD2 and the structural
  subunit, TPD3."].
- ~5-10% of Pph21 is Rrd2-bound in wild-type cells; sequential IP proves an
  Rrd2-Tpd3-Pph21 trimer [PMID:17550305 "Analysis of the HA-PPH21 immunoprecipitates
  with antibodies to the A subunit, TPD3, revealed that these proteins indeed are in the
  same multimeric complex."].
- Ppe1 binding to Pph21 rises in tpd3Δ and rrd1Δ rrd2Δ (demethylation, inactivation);
  Ppe1 overexpression strips Rrd2/Tpd3 and kills activity. Tap42 bound to Pph21 rises
  several-fold in tpd3Δ (Tap42/Tpd3 competition).
- Complex Portal: CPX-1856/1857 (PP2A variants with Cdc55 or Rts1), CPX-1380
  (Tap42-Rrd2-Pph21). Note that GO:0000159 is defined as containing a scaffold subunit;
  the Tap42 trimer lacks Tpd3, so the IPI row from PMID:15689491 is accepted with that
  caveat.

## TOR/TORC1 branch

- Tor phosphorylates Tap42; phospho-Tap42 competes with Cdc55/Tpd3 for the C subunit,
  and Cdc55/Tpd3 promote Tap42 dephosphorylation [PMID:10329624 "phosphorylated Tap42
  effectively competes with Cdc55/Tpd3 for binding to the phosphatase 2A catalytic
  subunit."].
- Rrd2 is specifically in the Tap42-PP2Ac complex; rapamycin releases the
  PTPA-phosphatase dimer as a functional unit [PMID:15689491 "We demonstrate a specific
  interaction of Rrd1 with the Tap42-Sit4 complex and that of Rrd2 with the Tap42-PP2Ac
  complex."].
- Tap42-phosphatase complexes sit on TORC1-containing membranes and are released into
  the cytosol by rapamycin or nutrient deprivation; ~5-10% of Pph21 is Tap42-bound in
  growing cells [PMID:16874307 "Rapamycin abrogates this association and releases the
  Tap42-phosphatase complexes into the cytosol."].
- Pph21/22 inactivation blocks rapamycin induction of NDP genes [PMID:12820961 "In
  contrast, Tap42 inactivation, as does inactivation of the protein phosphatases Sit4
  and Pph21/22, blocks rapamycin induction of nitrogen discrimination pathway genes."].
  This places PP2A *downstream* of TORC1 as an effector, which is why the
  "regulation of TORC1 signaling" rows are MODIFY -> GO:0038202 TORC1 signaling.
- Autophagy: pph21Δ pph22Δ (not singles) impairs Atg13 dephosphorylation, Atg1
  activation, PAS formation and autophagy after rapamycin; PP2A-Cdc55 and PP2A-Rts1 are
  redundant; Atg13-8SA bypasses [PMID:27973551 "After rapamycin treatment,
  dephosphorylation of Atg13, activation of Atg1 kinase, pre-autophagosomal structure
  (PAS) formation and autophagy induction are all impaired in PP2A-deleted cells."].
  GO:2000786 accepted.

## Localisation

- Immunofluorescence/GFP (Gentry & Hallberg 2002, PMID:12388751, not in this gene's
  cache but cached for CDC55): cytoplasmic with nuclear enrichment at all stages; rarer
  bud-tip, perinuclear and bud-neck signal (GFP-Pph21 did not fully complement)
  [file:yeast/PPH21/PPH21-deep-research-falcon.md "Pph21 is broadly cytoplasmic and
  enriched in the nucleus throughout the mitotic cycle."].
- Genome-wide GFP screen: Pph21 forms Apj1-dependent subnuclear foci with Cmr1 and Hos2
  after replication stress [PMID:22842922 "Thus, Cmr1, Hos2, Apj1, and Pph21 define a
  distinct subnuclear DNA damage response focus."].
- Stress-granule cores (PMID:26777405, supplementary proteomics only) — kept non-core.

## G1/S rows (PMID:12518319)

- Abstract-only. Multicopy suppressors of the sit4 hal3 G1-S arrest included PP2A-family
  genes; the abstract does not name PPH21 [PMID:12518319 "Several of these gene products
  are involved in phospho-dephosphorylation processes, including members of the protein
  phosphatase 2A and protein phosphatases 2C families, as well as components of the
  Hal5 protein kinase family."]. Interpretation: extra PP2A substitutes for the related
  Sit4 phosphatase; not evidence that Pph21 normally executes a G1/S step. All four
  G1/S rows (IGI x2, IBA at the Saccharomycetales node PTN000911598 seeded only by these
  IGIs, ARBA IEA) marked MARK_AS_OVER_ANNOTATED, not removed (curators had full text).

## Decisions summary

- ACCEPT: complex (x4), phosphatase activity (x3), mitotic cell cycle IBA, nucleus (x2),
  cytoplasm, cytosol, TOR signaling NAS, autophagosome assembly (x2).
- MODIFY: hydrolase activity IEA -> GO:0004722; regulation of TORC1 signaling (IEA, IGI)
  -> GO:0038202.
- MARK_AS_OVER_ANNOTATED: G1/S (x4), regulation of translation (IEA, IPI).
- KEEP_AS_NON_CORE: cytoplasmic stress granule HDA.
- REMOVE: ten bare protein-binding IPI rows (Tap42 x7, Ppe1 x2, Rrd2 x1 — all are
  regulators acting on Pph21; the interactions stay in IntAct/UniProt).
- No NEW rows: the mitotic-entry/exit terms used in core_functions (GO:0010971,
  GO:0001100) rest on cdc55-mutant work and are carried on CDC55; adding them to the
  catalytic subunit would duplicate holoenzyme-level evidence without an isoform-resolved
  experiment.

## Uncached sources referred to by the deep-research report (not quoted as evidence)

- Zabrocki et al. 2002 Mol Microbiol 43:835 (review; <2% of Pph21 Tap42-bound in log
  phase).
- Castermans et al. 2012 Cell Res 22:1058 (glucose-induced PP2A activation via
  methylation; pph21 pph22 enhances SUC2 derepression).
- Lin & Arndt 1995 (pph21-102), Evans & Stark 1997 (pph21 alleles: cell wall, actin,
  mitosis), Gentry & Hallberg 2002 (localisation; cached as PMID:12388751 under CDC55).
