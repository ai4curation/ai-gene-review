# ARHGAP23 (Q9P227) — curation notes

Working journal for the PAINT-campaign review. Provenance is recorded inline as
`[PMID:NNNN "verbatim quote"]`. Quotes marked as coming from a cached publication were
checked as verbatim substrings of `publications/PMID_NNNN.md`; quotes from publisher
supplementary files are reproduced by the committed script
`ARHGAP23-bioinformatics/analyze_arhgap23.py`, which parses them rather than transcribing.

## 1. What the automated provider returned, and what it missed

The affinage record (`ARHGAP23-deep-research-affinage.md`) passed its trust gates
(accession Q9P227 matches, human, `self_evaluation_pairwise: win`) and is accurate as far
as it goes, but it returned only **three** citations: PMID:15254754 (the 2004 in-silico
identification), PMID:38970683 (PKP4 at adherens junctions) and PMID:42006337 (the
VE-cadherin interactome). Its closing sentence is the problem:

> "Beyond these junction-associated roles, the enzymatic GAP activity and domain functions
> of ARHGAP23 have not been experimentally characterized in the available corpus."

That is wrong, and an independent sweep (Europe PMC full enumeration of 205 `ARHGAP23`
hits, NCBI gene2pubmed for GeneID 57636, plus partner/paralog-targeted searches) found
**three tier-1 papers that do characterize its GAP activity**, none of which names the gene
in its title — the exact failure mode this campaign has seen before:

| PMID | Title | Why the provider missed it |
|---|---|---|
| 27226243 | *A lateral signalling pathway coordinates shape volatility during cell migration.* | Title names a phenotype |
| 28114311 | *RhoGTPase Regulators Orchestrate Distinct Stages of Synaptic Development.* | Title names the family |
| 32203420 | *Systems analysis of RhoGEF and RhoGAP regulatory proteins reveals spatially organized RAC1 signalling from integrin adhesions.* | Title names the family; paywalled, not in PMC |

PMID:27226243 is in NCBI's curated gene2pubmed set for GeneID 57636, so it was reachable
from the gene identifier alone.

## 2. The substrate question: three experiments, three partly-conflicting answers

**RhoA — PMID:27226243 (Nat Commun 2016), full text cached.** Loss and gain of function in
MDA-MB-231 cells:

- [PMID:27226243 "Following siRNA-mediated knockdown of either Pk1 or Arhgap21/23, the level of GTP-bound, active RhoA was significantly enhanced (Fig. 4a), and active Rac1 was either unchanged or decreased, respectively"]
- [PMID:27226243 "Moreover, overexpressing Arhgap23 in MDA/shPk1 cells suppressed the elevation of active RhoA to a similar level as treatment with the active RhoA inhibitor, C3 transferase (Supplementary Fig. 3d)."]

Note the second clause of the first quote carefully: in these cells Arhgap21/23 knockdown
*decreased* active Rac1. That is the opposite of what a Rac1 GAP knockdown should do, and
it is the first half of the tension below.

**Rac1 — PMID:28114311 (PLoS One 2017), full text cached.** A Rac FRET biosensor in CHO.K1
cells:

- [PMID:28114311 "A Rac FRET biosensor [39] confirmed that shRNA against ARHGAP23 increased Rac1 activity to levels indistinguishable from constitutively active Raichu Rac V12 (Fig 5D and 5E), demonstrating that ARHGAP23 functions as a novel Rac1 GAP in adhesion maturation of migratory CHO.K1 cells as well as synapse maturation in neurons."]
- Same paper, neurons: two independent shRNAs against rat *Arhgap23* increase spine density
  and produce immature, filopodial spine morphology.

**Both, in a head-to-head screen — PMID:32203420 (Nat Cell Biol 2020).** Main text is
paywalled and absent from PMC, but the publisher's Source Data for Fig. 1b is open and is
parsed by the committed script. ARHGAP23's row (cellular FRET biosensor, normalised ΔR/R0,
authors' own significance flags):

| GTPase | norm ΔR/R0 AVG | p | authors' significance flag |
|---|---|---|---|
| RhoA | −0.364 | 2.93 × 10⁻⁵ | 1 |
| Rac1 | −0.372 | 2.92 × 10⁻⁶ | 1 |
| Cdc42 | +0.197 | — | 0 |

The same paper's Supplementary Table 2 records the resulting call for ARHGAP23 as the
dual-specificity class `RhoA+Rac1`, and its literature-review columns cite only
PMID:27226243 and list nothing under "in vitro".

**Synthesis.** RhoA activity is supported by two independent systems (pulldown in
MDA-MB-231, biosensor in the screen). Rac1 activity is supported by two independent
systems (biosensor in CHO.K1, biosensor in the screen) but is *contradicted* by
PMID:27226243's Rac1 measurement in MDA-MB-231. Cdc42 is scored negative in the only
experiment that tested it. The honest reading is: RhoA well supported, Rac1 supported but
cell-type dependent, Cdc42 not supported. All of it is cellular; **no assay on purified
protein exists** — the one systematic in-vitro study of the family (PMID:27481945) lists
ARHGAP23 in its table of all 66 human RhoGAPs but did not select it for purification.

## 3. The catalytic residue — and the published mutant that does not hit it

Committed analysis: `ARHGAP23-bioinformatics/` (`analyze_arhgap23.py`, `RESULTS.md`,
`results.json`; `--self-test` plus `mutation_test.py` for the guards).

- **The arginine finger is retained.** ARHGAP1/p50RhoGAP's own annotated finger (R282,
  resolved in PDB 1TX4, the RhoA:GDP:AlF4 transition-state complex) maps onto ARHGAP23
  **R942**, which is ARHGAP23's own annotated Site, and the projection is reciprocal. The
  same holds against the closest paralog ARHGAP21 (R1184).
- **Retention proves nothing on its own**, and the controls say so quantitatively: of two
  proteins known to be GAP-dead, the residue test calls one of them "retained" (ARHGAP11B,
  which has two curated `NOT|enables GO:0005096` IDA rows yet keeps its arginine); it
  correctly calls OCRL "not retained" — UniProt: *"the Rho-GAP domain lacks the catalytic
  arginine and is catalytically inactive"* (ECO:0000269). Family-wide, 60 of 66 human
  RhoGAP-profile proteins have an arginine at their annotated finger.
- **Interface conservation does not discriminate either**: ranked by identity at the 25
  1TX4 GAP:GTPase contact positions, the GAP-dead ARHGAP11B (64%) scores *above* the
  experimentally active ARHGAP21 (52%). That number tracks distance from ARHGAP1, not
  catalysis, and is reported as context only.
- **What does carry information**: at those same 25 interface positions, ARHGAP23 and the
  experimentally active ARHGAP21 carry the **same residue at 22**.
- **The mutant discrepancy.** PMID:32203420's Supplementary Table 4 describes its ARHGAP23
  imaging construct as a "GAP-deficient arginine finger mutant", and the SI figure names it
  **ARHGAP23-R986K**. Supplementary Table 1 gives the screened cDNA as NP_001186346.1,
  1491 aa — the same length as Q9P227, so the numbering is directly comparable. But 986 is
  **not** the UniProt/PROSITE arginine finger (942): it aligns to ARHGAP1 R323, which is in
  the 1TX4 interface but does **not** contact the nucleotide/AlF4/Mg transition state,
  whereas R282 does. That mutant was used only for TIRF localization; the arginine-finger
  controls that validated the activity screen were other proteins — [supplementary,
  machine-extracted: "mutation of critical arginine residues ('arginine fingers') abrogated
  the activity of the RhoGAPs ARHGAP11A, ARHGAP40, ARHGAP4, FAM13A, and SYDE2 (Extended
  Data Fig. 2h)."]. So **no experiment has tested whether R942 is required for ARHGAP23's
  measured activity**, and one of the two residue assignments is wrong.

This is reported as a discrepancy, not a correction: the structural argument favours 942,
but only an experiment settles it.

## 4. Localization and partners

- **Lateral, non-protrusive cortex**, Prickle1-dependent
  [PMID:27226243 "In migrating cells, we find that Pk1 and Arhgap21/23 are located at non-protrusive membranes that are lateral to active protrusions."] and
  [PMID:27226243 "Moreover, on Pk1 knockdown, Arhgap23 was absent from the periphery following ACM treatment (Fig. 2g)"].
- **Focal adhesions.** PMID:32203420's TIRF screen places ARHGAP23 among the FA-enriched
  regulators with a pericentric distribution (Supplementary Table 4, parsed by the script:
  *"Focal adhesion localization found by TIRF imaging (GAP-deficient arginine finger
  mutant), pericentric."*). Independently, ARHGAP23 knockdown in CHO.K1 gives nascent
  adhesions and its overexpression gives adhesion maturation [PMID:28114311 "Conversely, cells expressing GFP-tagged ARHGAP23 exhibited increased adhesion maturation"].
- **Adherens junctions / PKP4.** PKP4-GFP affinity purification pulls down ARHGAP23 and,
  notably, *not* ARHGAP21 [PMID:38970683 "ARHGAP21 did not co-purify with PKP4. In contrast, the GAPs ARHGAP23, ARHGAP24, and RACGAP1 co-precipitated."]. Functionally,
  [PMID:38970683 "In PKP4-KO cells, ARHGAP23 depletion correlated with a loss of stress fibers, suggesting that ARHGAP23 is active in the PKP4-KO cell cytoplasm to reduce cortical RhoA activity and suppress cortical ring formation."].
- **VE-cadherin interactome** [PMID:42006337 "In this study, we used a proteomics approach through which four core VE-cadherin interactors were identified: ARVCF, ARHGAP23, KEAP1, and NGLY1."] — an interaction, not a localization result for ARHGAP23; the paper's
  co-IP/co-localization follow-up was on ARVCF.
- **α-catenin (CTNNA1)** appears as a "GOLD"-tier ARHGAP23 AP-MS interactor in
  PMID:32203420's Supplementary Table 3. This matters because a secondary source
  (PMID:33646271) states that ARHGAP21 *and ARHGAP23* "have been shown to bind directly to
  α-catenin", citing two papers that on inspection assay ARHGAP21 (PMID:15793564) and an
  E-cadherin BioID list (PMID:24338363) respectively. The claim is family-level
  generalisation in that source, but the Müller AP-MS table is independent primary support
  for the ARHGAP23–CTNNA1 association.
- **PDZ domain unprofiled**: [PMID:23722234 "Note that the PDZ domains of AHNAK2, ARHGAP23, LIMK1, SHANK3, SHROOM2, SHROOM3, SIPA1, SNTB2, SYNPO2L, and TJP1-PDZ1 are missing from the resource as a result of unsuccessful amplification."] so the only PDZ-ligand
  claim for this protein (PTEN C-terminus, PMID:37305272) is pure docking.

## 5. Where the existing GOA rows come from

Eight rows, and they collapse to three distinct assertions:

- `GO:0005096` × 3 — one IBA (PANTHER node PTN008592632, donor UniProtKB:Q5T5U3 = ARHGAP21)
  and two Reactome TAS. The IBA node is well grounded: ARHGAP21 carries its own `enables
  GO:0005096` **IDA** from PMID:15793564. The two Reactome reactions are the RhoA set
  (R-HSA-8981637) and the Rac1 set (R-HSA-9013144), and — unlike the ARHGAP11B case in this
  batch — ARHGAP23's membership in both is explicitly sourced in Reactome's own summaries:
  "ARHGAP23 (Müller et al. 2020)" for RhoA and "ARHGAP23 (Martin Vilchez et al. 2017; Müller
  et al. 2020)" for Rac1. Martin-Vilchez et al. 2017 is PMID:28114311. So the set membership
  is correct here; what is lost is that all three rows flatten to the same substrate-blind
  term.
- `GO:0005829` cytosol × 2 — the compartment attached to those same two Reactome reactions.
- `GO:0007165` (InterPro IEA from the RhoGAP domain) and `GO:0051056` (Reactome pathway
  membership) — both true and both strictly less informative than what the direct evidence
  supports.
- `GO:0070062` extracellular exosome — HDA from a parotid-gland exosome MudPIT
  (PMID:19199708), a bulk proteomics inventory.

## 6. The ontology gap

Checked across **three independent services**, because this is load-bearing:

- `GO:0005100` "Rho GTPase activator activity" is **obsolete/merged**: OLS4 reports
  `is_obsolete: true`; `api.geneontology.org` returns an empty record for it; QuickGO
  silently resolves the id and returns **GO:0005096** instead.
- `GO:0005096` "GTPase activator activity" now carries `Rho GAP activity`, `Rho GTPase
  activator activity`, `Rac GAP activity`, `Rac GTPase activator activity` (and the ARF,
  Rab, Ral, Ran, Rap, Ras, Sar equivalents) as **narrow synonyms**.
- `GO:0005096` has **no `is_a` children**: OLS4 hierarchicalChildren = 0,
  `api.geneontology.org` subgraph descendents = 0, QuickGO returns one child, `GO:1902773`,
  via `capable_of` — not `is_a`.

So the molecular-function branch cannot express *which* GTPase a GAP acts on. The
biological-process branch still can: `GO:0035024` negative regulation of Rho protein signal transduction
and `GO:0035021` negative regulation of Rac protein signal transduction both exist. The
specificity that three papers measured is therefore recordable as process and not as
activity — which is the single most useful thing this review has to say to a curator.

## 7. Disease and other associations (background, not curated)

- 17q12 eosinophilic-esophagitis risk locus, ARHGAP23 the named gene (PMID:33446330,
  rs7211886, meta P = 5.4 × 10⁻⁷). No functional follow-up.
- 5′ partner in an ARHGAP23–FER fusion in a myofibroblastic neoplasm (PMID:34545945); the
  gene donates its promoter, which says nothing about the protein.
- PMID:38022849 is the only other ARHGAP23-titled paper; it is database mining and its
  opening sentence ("ARHGAP23 is known to activate RHO-GTPase") inverts what a GAP does.
  Not usable as functional evidence.
- No knockout phenotype exists in any organism. The nearest in-vivo handle is indirect:
  *Arhgap23* is downregulated in LEC-*Foxc1;Foxc2* double-knockout mouse embryos and FOXC1/2
  bind conserved regions of the locus (PMID:32510325).
