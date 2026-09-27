# BUB1B (BubR1, UniProt O60566) - curation notes

## Session 2026-09-25 - full review of GOA annotations

### Identity and architecture

- Human BUB1B encodes BubR1 (hBUBR1, MAD3L, SSK1), the Mad3-related paralog of BUB1. Taylor et al. noted
  at the outset that it is "perhaps not an additional member of the Bub1 family, but more likely a Mad3-related
  protein" and that its kinase domain "lacks several of the residues that are usually highly conserved among
  most protein kinases" [PMID:9660858 "hBubR1 lacks several of the residues that are usually highly conserved among most protein kinases"].
- Domain map (UniProt + literature): N-terminal TPR domain (KNL1/Blinkin binding, KEN1 box at residue 26,
  ABBA motifs, D-box), GLEBS/Bub3-binding motif, KEN2, KARD (LxxIxE PP2A-B56 motif; S670 CDK1, S676 PLK1
  sites), C-terminal kinase-like domain (766-1050).
  [PMID:22331848 "Bub3-BD, Bub3-binding domain, also known as GLEBS motif; KEN, KEN box; PP1-BD, protein phosphatase 1–binding domain; KI1, Bub1-binding domain 1; KI2, BubR1-binding domain 2"]

### Core function 1 - MCC subunit / APC/C-CDC20 inhibitor (GO:1990948, GO:0033597, GO:0007094)

- hBUBR1 is essential for the mitotic checkpoint: antibody microinjection abrogates nocodazole arrest
  [PMID:10477750 "Furthermore, microinjection of hBUBR1 antibodies abrogated the mitotic arrest and caused cells to exit mitosis."].
- The MCC was purified from HeLa cells as hBUBR1/hBUB3/CDC20/MAD2 in near-equal stoichiometry and inhibits
  APC/C ubiquitin ligase activity; the inhibitor co-fractionates with hBUBR1 at every step
  [PMID:11535616 "At each of the three successive chromatographic steps, the peaks of APC/C inhibitory activity and hBUBR1 coincided."].
  A preformed MCC exists in interphase
  [PMID:11535616 "Surprisingly, hBUBR1 complex isolated from interphase HeLa cells (synchronized in the G1/S boundary) inhibited APC/C activity and contained the same subunits found in mitotic MCC (unpublished data)."].
- BubR1 inhibits APC/C-Cdc20 independently of Mad2 and of its kinase activity
  [PMID:11702782 "Surprisingly, the kinase activity of BubR1 is not required for the inhibition of APCCdc20."].
- Mechanism (cryo-EM, APC/C-MCC): BubR1 degron-like motifs block Cdc20 degron-recognition sites and the
  BubR1 TPR obstructs UbcH10
  [PMID:27509861 "BubR1TPR interacts directly with the UbcH10 interface of Apc2WHB that repositions to contact BubR1TPR"];
  MCC forms when C-Mad2-Cdc20 binds the BubR1-Bub3 dimer
  [PMID:27509861 "Soluble C-Mad2 engages the N-terminus of Cdc20 (refs 10,11), the mitotic activating subunit of the APC/C, which then binds the BubR1-Bub3 dimer to form the MCC 12."].
- KEN1 (K26EN) is essential for the core MCC; D-box/KEN2 let the MCC inhibit a second, APC/C-bound CDC20
  [PMID:25383541 "Here, we show that the MCC can inhibit a second CDC20 that has already bound and activated the APC/C."].
- Acetylation at K250 by PCAF switches BubR1 from APC/C inhibitor (pseudosubstrate) to APC/C-Cdc20 substrate
  [PMID:19407811 "Instead, BubR1 functions as a pseudosubstrate of the APC/C complex by competing with genuine substrates of the APC/C complex for the same Cdc20-binding sites (D-box and KEN box) (Burton and Solomon, 2007)."].
- Checkpoint silencing: p31comet drives ATP-dependent MCC disassembly, dissociating Cdc20 from BubR1
  [PMID:21300909 "Although p31(comet) binds to Mad2, it promotes the dissociation of Cdc20 from BubR1 in MCC."].

### Core function 2 - kinetochore recruitment and KARD-dependent PP2A-B56 recruitment

- Kinetochore localization requires Bub3 binding through the GLEBS segment
  [PMID:9660858 "In addition, hBubR1 can localize to kinetochores during prometaphase and the ability to bind Bub3 is required for this localization."];
  BubR1 assembles onto kinetochores in prophase, after CENP-F and before CENP-E
  [PMID:9763420 "The combined data show that hBUBR1 assembled onto kinetochores sometime in prophase, after CENP-F but before CENP-E."].
- Recruitment is Bub1- and Bub3-dependent and needed both for SAC arrest and stable K-MT attachment
  [PMID:20220147 "BubR1 kinetochore enrichment is dependent on Bub1 and Bub3 (28, 29) and is required to sustain a SAC arrest, as well as for stable kinetochore-microtubule interactions (23)."].
  TPR-KI2 (Knl1) contacts are dispensable for recruitment
  [PMID:22331848 "deletion of the TPR domain of BubR1 (BubR1(Δ204) or BubR1(Δ328)) did not evidently affect kinetochore recruitment"].
- BubR1 sits in the outer kinetochore (Spindly colocalizes with BubR1 adjacent to CREST)
  [PMID:19468067 "Colocalization with BubR1, adjacent to the CREST signal, indicated that hSpindly is an outer KT protein"].
- PP2A-B56 recruitment via the KARD (not in the local publication cache; from deep research):
  [file:human/BUB1B/BUB1B-deep-research-falcon.md "BUBR1 therefore acts as a targeting platform that positions PP2A-B56 where kinetochore phosphosignalling must be reversed."]
  [file:human/BUB1B/BUB1B-deep-research-falcon.md "Mutation of BUBR1 residues required for B56 binding disrupts chromosome congression; Aurora B inhibition can partially reverse this phenotype, supporting the proposed kinase–phosphatase balance."]
  Primary papers to cache for a future pass: Suijkerbuijk et al. 2012 Dev Cell; Kruse et al. 2013 J Cell Sci;
  Xu et al. 2013 Biol Open; Wang et al. 2016 Protein Cell; Braga et al. 2020 Cell Rep.
  GOA carries no annotation for this function; captured in core_functions with GO:0140483 (kinetochore adaptor
  activity) and flagged in suggested_questions rather than asserted as NEW.

### The kinase question (GO:0004672 / GO:0004674 / GO:0106310 / EC 2.7.11.1)

- Historical evidence: autophosphorylation in GST pull-downs, with the caveat of co-purifying kinases
  [PMID:9660858 "Although we cannot rule out the possibility that the observed activities are due to another copurifying protein kinase, these data are consistent with the notion that, like ScBub1 (Roberts et al., 1994), mBub1 and hBubR1 exhibit autophosphorylation activity in vitro."];
  immunoprecipitate kinase activity stimulated by nocodazole
  [PMID:10477750 "Comparison of hBUBR1 kinase activity between metaphase cells and those that were exposed to nocodazole showed that kinase activity was rapidly stimulated within 15 min of nocodazole treatment"];
  CENP-E stimulates the activity
  [PMID:12925705 "CENP-E binding selectively stimulated the GSTHis-BubR1 kinase inasmuch as addition of another BubR1-binding partner, hCdc20, did not affect GSTHis-BubR1 kinase activity"].
- Pseudokinase consensus (deep research; Suijkerbuijk 2012, Braga 2020):
  [file:human/BUB1B/BUB1B-deep-research-falcon.md "Phylogenomic, structural and direct biochemical analyses found no convincing intrinsic phosphotransfer activity."]
  [file:human/BUB1B/BUB1B-deep-research-falcon.md "Deleting or mutating the region reduced kinetochore PP2A-B56, delayed checkpoint silencing and caused chromosome-alignment defects."]
- Contrary report: Huang et al. 2019 claim human BubR1 is an active kinase phosphorylating CENP-E S2639
  [PMID:31201382 "Indeed, human BubR1 WT was found to have catalytic activity and our enzymatic assays confirmed that Lys795 and Asp911 are critical for that activity (Fig. 1e )."],
  while conceding the active-kinase signature is not conserved
  [PMID:31201382 "However, this type of signature of an active kinase is not apparently conserved in human BubR1."]
  and acknowledging the controversy
  [PMID:31201382 "Despite prior experimental evidence that BubR1 has kinase activity, this has been highly controversial, as a widely held view is that BubR1 is an unusual pseudokinase containing modules to interact with Bub1, Bub3, PP2A-B56 and KNL."].
- Decision: all seven kinase rows (IBA, IDA x2, NAS, TAS, EC-IEA, Rhea-IEA) graded MARK_AS_OVER_ANNOTATED, consistently.
  Not REMOVE because a direct experimental claim exists and has not been formally refuted; not ACCEPT because
  the activity is disputed, dispensable for the core function, and the field consensus is pseudokinase.
  PMID:31201382 flagged DISPUTED in reference_review. The IBA is annotated with a propagation_review
  (PROPAGATION_BAD / PSEUDO_OR_SUBACTIVITY_LOSS + WRONG_ORTHOLOG_OR_PARALOG): node PTN000361607 predates the
  Bub1/BubR1 split and kinase activity is genuine on the BUB1 branch.

### Localization rows

- Cytoplasm (interphase) is the dominant pool
  [PMID:9763420 "Examination of the subcellular distribution of hBUBR1 by immunofluorescence staining showed that it was concentrated in the cytoplasm of all interphase cells"];
  spindle/midzone in late anaphase
  [PMID:9763420 "By late anaphase, hBUBR1 was prominently distributed in two patches in the spindle midzone that flanked a narrow stripe of CENP-E"].
- Nucleus (IBA, UniProt keyword): KEEP_AS_NON_CORE - phylogenetic (closed-mitosis yeasts) and inferred for human.
- Centrosome (UniProt keyword from PubMed:19503101, not cached): KEEP_AS_NON_CORE.
- Perinuclear (PMID:20531406, B-cell interactome co-localization with MCM3): KEEP_AS_NON_CORE
  [PMID:20531406 "High-resolution confocal imaging showed that these proteins are co-localized either in the nucleus or perinuclearly (Figure 6C)."].
- Cytosol: HPA IDA and 24 Reactome TAS rows all ACCEPT (same location claim); the 11 rows derived from
  cohesin/separase/astral-MT-capture/EML4-NUDC reactions are noted as peripheral pathway-membership rows.
- Anaphase-promoting complex (TAS, PMID:10477750): MODIFY -> GO:0033597. BubR1 binds APC/C-CDC20 as an
  inhibitor within the MCC; it is not an APC/C subunit
  [PMID:10477750 "As hBUBR1 appears to form a fairly stable complex with the cyclosome/APC in cells arrested in mitosis, its kinase activity may be labile."].

### Protein binding (GO:0005515) - 55 IPI rows

Policy: MODIFY where the cited paper supports an informative MF or complex; REMOVE (uninformative, interaction
not disputed) for high-throughput datasets, PTM-enzyme partners (BubR1 as substrate) and recruitment partners
without an MF; UNDECIDED where the cached abstract gives no handle.

- CDC20 (19 rows): mechanistic papers (PMID:11030144, 15525512, 19407811, 20212161, 21300909, 21407176,
  22000412, 24581499, 25383541) -> MODIFY to GO:1990948; HT/pharmacology (PMID:20360068, 25241761, 25502805,
  25852190, 31515488, 32707033, 33961781, 35271311, 37926298, 40205054) -> REMOVE.
- MAD2L1 (8) and BUB3 (11): MCC-context papers -> MODIFY to GO:0033597 mitotic checkpoint complex; HT -> REMOVE.
- BUB1 (4, all HT) -> REMOVE. KNL1 (4) -> REMOVE (recruitment interaction; CC rows carry it).
- CENPE (PMID:9763420), PLK1 (PMID:16760428) -> REMOVE (no settled MF for BubR1).
- KAT2B, UBC, CREBBP, SIRT2 -> REMOVE (BubR1 is the substrate). YWHAE (14-3-3 interactome) -> REMOVE.
- RIPK3 (PMID:29883609, abstract-only, no BubR1 mention) -> UNDECIDED.
- PMID:15525512 and PMID:16760428 abstracts foreground Bub1/Plk1-Bub1; no mis-attribution asserted (curator had
  the full text); reference_review notes this.

### Meiotic centromeric cohesion (GO:0051754, IBA)

- Sources: fly BubR1 and pombe bub1 at PTN000361607. KEEP_AS_NON_CORE with propagation_review
  (NO_FAILURE_NON_CORE / CONTEXT_OR_TISSUE_MISMATCH): the shugoshin-recruiting kinase function is BUB1's in
  human; BubR1-PP2A-B56 does participate in cohesion protection, and mouse oocyte studies (Touati et al. 2015,
  not cached) support a BubR1 requirement in meiosis. Raised in suggested_questions.

### Disease

- MVA1: biallelic BUB1B variants; R727C/L844F destabilise the protein and abolish its interactions
  [PMID:25502805 "we find that the mutations R727C and L844F on the spindle checkpoint kinase Bub1b both cause the protein to become unstable and lose all its interactors"].
- Ageing: BubR1 levels decline with age via K668 acetylation balance (CBP vs SIRT2), mouse
  [PMID:24825348 "the loss of BubR1 levels with age is due to a decline in NAD(+) and the ability of SIRT2 to maintain lysine-668 of BubR1 in a deacetylated state, which is counteracted by the acetyltransferase CBP"].
  Not annotated as a GO process for BUB1B; treated as regulation of BubR1 abundance, not a BubR1 function.

### Repository context

- modules/metaphase_anaphase_transition_and_mitotic_exit.yaml models BubR1/Mad3 as the "pseudokinase/KEN-box
  subunit that blocks Cdc20 substrate-binding sites" in the MCC - consistent with this review.
- gocams/67369e7600002505 (pombe) types the mad3-containing MCC activity as GO:0140678 molecular function
  inhibitor activity, occurring in the kinetochore, part of GO:0007094; the human review uses the more specific
  GO:1990948 ubiquitin ligase inhibitor activity, consistent with the MAD2L1 review.

### Validation

- `just validate human BUB1B`: valid, 3 warnings (core-function terms GO:0140483, GO:0007080, GO:0051315 not
  present in existing_annotations - deliberate, see above). All supporting_text snippets checked verbatim.
