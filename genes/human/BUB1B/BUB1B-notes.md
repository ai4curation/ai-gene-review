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


## 2026-10-03 — source-specific reassessment of the complete review

This reassessment supersedes the earlier action rationales where they conflict with the decisions below. The earlier notes remain intact as a historical record. The normal UniProt, GOA, publication, Reactome and genuine Falcon source files were preserved. All 119 machine-sourced annotation objects, all three alternative products and their source identifiers are unchanged; the 120 raw GOA rows include a repeated CENP-E source assertion. No annotation was manufactured to compensate for that representation difference.

All 119 decisions have been assessed: 50 ACCEPT, 21 KEEP_AS_NON_CORE, 7 MODIFY and 41 UNDECIDED. There are no REMOVE, MARK_AS_OVER_ANNOTATED, NEW or PENDING actions. The uncertainty is substantive: seven catalytic assertions remain disputed; 32 protein-binding source records remain unverified at the relevant target-assay level; the centrosomal and meiotic-cohesion assertions need additional original evidence. Completion of this review does not resolve those questions.

### Two supported core functions and the catalytic conflict

The first core is inhibition of APC/C through the BUBR1-containing mitotic checkpoint complex. Human MCC purification, recombinant complex assays and structures establish that BUBR1 itself supplies CDC20-binding degron-like contacts and obstructs E2 engagement; this is direct inhibitory work, not simply a checkpoint-arrest phenotype ([PMID:11535616](https://pubmed.ncbi.nlm.nih.gov/11535616/), [PMID:25383541](https://pubmed.ncbi.nlm.nih.gov/25383541/), [PMID:27509861](https://pubmed.ncbi.nlm.nih.gov/27509861/)). The core retains GO:1990948 ubiquitin ligase inhibitor activity and the mitotic checkpoint process. The original APC/C-component annotation is refined to the inhibitory MCC, while acknowledging that the two complexes physically associate.

The second core is kinetochore recruitment of PP2A-B56. Human-cell replacement and MVA-fibroblast rescue experiments connect BUBR1's B56-binding region with attachment stabilization; artificial kinetochore targeting provides a mechanistic rescue. Human recombinant fragments and structural/ITC assays identify the KARD LxxIxE interface with B56. This supports GO:0140483 kinetochore adaptor activity, not intrinsic phosphatase catalysis or a demonstrated allosteric activation of PP2A ([PMID:23789096](https://pubmed.ncbi.nlm.nih.gov/23789096/), [PMID:27350047](https://pubmed.ncbi.nlm.nih.gov/27350047/)). The 2016 binding experiments use human BUBR1 and B56 fragments; they do not establish whole-protein stoichiometry. Actual phosphoserine effects are distinguished from aspartate substitutions, which did not reproduce the same affinity effects in vitro. The normally fetched abstracts of PMID:23079597 and PMID:33207204 provide additional KARD-regulation and noncatalytic-domain context. Core support now rests on primary papers instead of the generated literature summary alone.

Intrinsic kinase activity remains a real experimental disagreement. PMID:31201382 reports activity with human full-length BUBR1 purified from insect cells and a CENP-E substrate; its structural work uses Drosophila protein and is not a human crystal structure. PMID:22698286 reports negative tests with human kinase-domain constructs expressed in bacteria, positive BUB1 controls and cellular immunoprecipitate controls. Constructs, expression systems and tested substrates differ. The original PMID:9660858 authors explicitly did not exclude a copurifying kinase. Conversely, kinase dispensability for checkpoint function is not a demonstration that no BUBR1 molecule can catalyse phosphotransfer. All seven inherited catalytic annotations therefore remain UNDECIDED. PMID:33207204 is the peer-reviewed form of the previously discussed Braga work; preprint and thesis versions are not independent replications. The prior categorical pseudokinase/ancestral misplacement arguments are not carried forward as settled facts.

### Protein binding and source identity

The standing project instruction takes precedence over the general skill/validator preference to remove uninformative protein-binding annotations: a supported interaction is retained as non-core when no defensible finer MF is established; an unverified source remains UNDECIDED. All 55 binding rows were joined to their exact GOA partner identifiers, reference and evidence code. The result is six MODIFY to ubiquitin ligase inhibitor activity, 17 KEEP_AS_NON_CORE and 32 UNDECIDED. Of the 36 previously removed generic-binding rows, nine are now supported non-core interactions and 27 remain unresolved. No row is removed simply because it is a screen result, a substrate interaction or a broad MF.

The six CDC20 refinements use direct human MCC inhibitory evidence as well as each source's actual association context. The other retained interactions include BUB3/MAD2 complex association, KNL1 contacts, PLK1 association, PCAF/KAT2B and CBP/SIRT2 regulatory interactions, and CENP-E association. A cellular-component term is not substituted for a molecular-function binding term. Coassociation is not automatically called a purified binary interaction: in particular, the original CENP-E paper explicitly left direct binding unresolved. The CBP interaction preserves the source's mouse Crebbp partner accession; the precise heterologous construct provenance was not resolved from the accessed excerpt. Source isoform suffixes remain unchanged and do not imply that a binding activity is unique to that isoform.

PMID:19407811 demonstrates covalent ubiquitination of BUBR1, but that alone does not establish the selective noncovalent interaction meant by GO binding. Its UBC row remains UNDECIDED because a separate supporting assay was not inspected. The exact BUB3 experiment in PMID:22000412 and PCAF binding experiment in PMID:24825348 also remain unresolved despite independent evidence for those interactions in other papers. Most systematic-screen rows need the individual supplementary record. Failure to find a target name in an abstract or cached excerpt is an access limitation, not evidence that the experiment did not occur. The BUB1-centered PMID:15525512 and RIPK3-centered PMID:29883609 are consequently not called wrong-gene citations.

### Locations, processes and phylogenetic assertions

Human HeLa imaging in PMID:9763420 supports the interphase cytoplasmic pool, mitotic kinetochore recruitment and later spindle redistribution. PMID:19468067 supplies explicit BUBR1/CREST outer-kinetochore context. Nuclear/perinuclear staining in PMID:20531406 is from Ramos lymphoma cells; it is not direct localization evidence from normal germinal-centre tissue. These contextual nuclear and spindle locations remain non-core. The separate centrosome assertion is UNDECIDED because the original localization experiment was not recovered; a centrosome-number phenotype alone does not establish a centrosomal pool.

The 24 Reactome rows assert cytosol. Their complete cached summaries were read, but no complete participant graph was reconstructed. Acceptance of a supported BUBR1 cytosolic pool does not assign the enzyme activity of every reaction named in those entries to BUBR1. Direct human checkpoint perturbation, purification and reconstitution support the existing chromosome-segregation and checkpoint assertions.

Exact PAINT ancestral-node/IBD source sets were checked for the four noncatalytic IBA rows. Kinetochore and mitotic checkpoint assertions remain ACCEPT; nucleus remains non-core with independent human support. The meiotic centromeric-cohesion assertion has actual fly BubR1 and fission-yeast bub1 donor provenance, but its complete donor experiments and full ancestral placement were not inspected. It is UNDECIDED, rather than labelled a demonstrated wrong-paralog transfer. The kinase IBA likewise remains unresolved on the contested target evidence. A short donor list or inclusion of BUB1B itself is not a propagation error. No unverified topology or evolutionary loss is invented to fill structured failure metadata.

No NEW annotation is proposed. The local GO-CAM index had no matching BUB1B/O60566 entry in the inspected snapshot; that is not proof of a curation gap. The two existing core summaries retain mechanistically supported terms, including three terms absent from the source annotation block. The warning about that difference is disclosed; it is not a reason to manufacture NEW assertions without the required comparator, ontology and participation review.

### Actual source access and corrections

All 44 original PMID abstracts and all five newly recovered normal-cache abstracts were read completely. The five additional papers are PMID:23079597, PMID:23789096, PMID:27350047, PMID:33207204 and PMID:22698286. Selected complete source-relevant Results, Methods, Discussion passages and captions were read from the following original caches: PMID:10477750, 11535616, 12925705, 17227893, 19407811, 19468067, 20220147, 20531406, 21407176, 22000412, 22331848, 25383541, 25502805, 27509861, 9660858 and 9763420. The newly recovered 23789096 and 27350047 caches were read at the relevant human rescue, recombinant binding and structural sections. This is not a claim to have read every paper in full or every supplement. Figure images were not separately inspected.

Indexed primary Results supplied the BUBR1–PLK1 passage in PMID:16760428 and CBP/SIRT2 passages in PMID:24825348; direct full-paper access and the relevant supplementary images were not completed. The independent catalytic consultation read the positive 2019 assays and the institutional primary PDF Results/Methods for the negative 2012 study. The normal 22698286 cache itself remains abstract-only, as do 23079597 and 33207204. Full-text cache flags do not imply that every experimental section or partner-level data entry was available or inspected. Reference-level assessments and individual review reasons record these distinctions.

The inspected official corrections for PMID:17227893 concern author order; for PMID:21988832 an author name; and for PMID:22000412 an affiliation and omitted Figure 3B comparison legend. None of these notices identifies a reversal of the assay conclusion used here ([JCB correction](https://doi.org/10.1083/jcb.20061009920070116c), [MSB correction](https://doi.org/10.15252/msb.20178107), [Structure correction](https://doi.org/10.1016/j.str.2011.11.011)).

### Evidence anchors and validation

The prior YAML contained 164 supporting-text fields, including long and repeated excerpts. They have been replaced with 17 short exact instances representing 11 distinct source anchors, with at most 18 quoted words from any one publication across all uses in the revised YAML (including repeated uses). Both cores and selected mechanistic/localization rows retain direct anchors; other support is reference-only with explicit reasons. The original notes and immutable publication text are preserved. The pruning does not mean the original source annotations were deleted or the papers were all rejected.

Normal candidate validation, including terms, references and GOA checks, passed with no errors and 22 warnings. Seventeen warnings reflect the deliberate project rule retaining supported generic binding. Two reflect unfilled structured failure metadata for unresolved IBA assertions; no failure mechanism was invented. Three reflect core-synthesis terms absent from existing source annotations. DRAFT is the schema-consistent status while warnings remain, although no decision is PENDING. This is a completed scientific candidate awaiting independent whole-gene peer review and authorized canonical application; publication and history have not been changed by this candidate preparation.

## 2026-10-03 — Canonical application

The independently reviewed candidate was applied after ROOT whole-science approval. Normal canonical validation passed with 23 warnings: the 22 documented candidate warnings plus one canonical-context advisory that the existing Falcon file is not cited by an annotation, and the standard EDIT history passed validation. All 119 source assertions, three alternative products, existing source caches, generated provider files and previous history were preserved. The 50 ACCEPT, 21 KEEP_AS_NON_CORE, seven MODIFY and 41 UNDECIDED decisions remain; DRAFT correctly records the remaining warnings. Remote publication is a separate step.


## 2026-10-03 — First published-review follow-up

This entry supersedes the earlier overly strict source-record judgments while preserving the earlier notes as historical provenance. All 119 machine assertions, three named alternative products, 85 reference identities, both core functions and source/cache bytes are preserved. The revised decisions are 50 ACCEPT, 39 KEEP_AS_NON_CORE, 19 MODIFY and 11 UNDECIDED, with no new annotations. DRAFT continues to record the remaining advisories and uncertainty.

### Standing instruction and established interactions

The [immutable published project instruction](https://github.com/ai4curation/ai-gene-review/blob/3eb5f8979787f246e82ecaadcb5fc6e49507ff4c/projects/CLINGEN_MENDELIAN.md#curation-instructions) explicitly records the user's standing direction to retain supported generic binding as non-core when no evidence-backed finer MF is established. It also expressly identifies the task-specific departure from the skill's informational-exclusion recommendation. That published instruction supplies the authority; this follow-up changes no repository-wide skill or validator and claims no maintainer sign-off.

The broad binding claim can be supported by independent target experiments while the original screen/table remains uninspected. Twenty-nine former UNDECIDED rows are resolved on that basis: twelve CDC20 rows refine to GO:1990948, consistently with the six earlier CDC20 refinements; seventeen BUB1, BUB3, MAD2 and PCAF rows retain supported association as non-core. The BioPlex rows contain four partners, including BUB1. Human BUBR1–BUB1 two-hybrid Results distinguish heterodimerization from homodimerization; human BUB3 constructs show deletion-sensitive copurification in BHK cells; human HeLa MCC purification/reciprocal IP supports MAD2 coassociation; human HeLa IP supports PCAF association. This does not claim that every screen edge, image or purified binary interaction was independently verified. Original identifiers and partner fields remain unchanged.

The UBC row remains unresolved because covalent ubiquitin conjugation does not itself establish noncovalent binding. RIPK3 and YWHAE rows retain their source-access uncertainty; no rejection is inferred from the paper title.

### Separate localization and evolutionary judgments

The centrosome assertion is retained as non-core using the preserved UniProt location and curator deference. The [official original primary abstract](https://pubmed.ncbi.nlm.nih.gov/19503101/) was independently read and explicitly reports centrosomal localization separately from amplification phenotypes. Its normal cache is absent, so it is supplementary notes-only corroboration; no YAML publication quote, full-paper or localization-image inspection is claimed. The specific meiotic centromeric-cohesion IBA remains UNDECIDED: actual fly BubR1/fission-yeast Bub1 donor identities are established, but complete donor experiments and ancestral placement remain uninspected. That limitation is not a claim of a wrong node, inadequate donor count or a requirement for human-specific experiments.

### Catalytic evidence and access

All seven catalytic assertions remain UNDECIDED after separate reassessment. The positive [2019 study](https://pubmed.ncbi.nlm.nih.gov/31201382/) uses human Sf9-derived preparations, active-site mutants, a CENP-E Ser2639 substrate test and BRT-1-binding-site rescue controls. D882N explicitly addresses protein stability. Those controls are substantive evidence; a hypothetical contaminant is not treated as a demonstrated explanation. The crystal structure is Drosophila, whereas the human structural representation is a model. The negative [2012 primary PDF](https://www.hubrecht.eu/app/uploads/2017/11/Kops_Research_2012_Suijkerbuijk_The-vertebrate-mitotic-checkpoint-protein-BUBR1-is-an-unusual-psuedokinase.pdf) was inspected as text at PDF Results pages 4–5 and Methods page 8: bacterial human-domain assays with active BUB1 controls and cellular IP activity persisting after catalytic changes/domain removal challenge intrinsic attribution under different conditions. Neither negative preparation results nor catalytic dispensability prove absence under every condition. The conflict remains unresolved, and no catalytic core is added.

The normal 2012 cache remains abstract-only. The [2020 published Braga paper](https://www.sciencedirect.com/science/article/pii/S2211124720313863) was read through its cached abstract plus indexed publisher passages; direct full-page access failed. No complete institutional PDF is claimed for that paper or for [the KARD study](https://pubmed.ncbi.nlm.nih.gov/23079597/), whose complete normal abstract was read. Preprint/thesis versions are not independent experiments. The existing core's detailed PP2A evidence remains grounded in the separately inspected normal 2013 and 2016 sources.

The five spindle-checkpoint rows retain source-specific explanations: human perturbation for the IDA, direct MCC purification for the NAS, family mapping corroborated by direct target evidence for the IEA, the inspected IBD plus target evidence for the IBA, and curator deference with independent checkpoint evidence for the IMP whose exact source assay remains uninspected.

### Evidence anchors and validation

Annotation-level anchors now include positive catalytic/substrate observations, partner coassociation, checkpoint interference and cytoplasmic localization. Two existing finding quotes were moved to the corresponding annotation to avoid duplication. The revised YAML contains 25 exact quote instances; aggregate repeated words never exceed 22 for one source. The earlier 18-word maximum described that earlier file and was not a repository convention or a reason to discard biologically useful evidence. Unchanged legacy notes remain historical; this appendix adds no publication quotations.

Normal full candidate validation is recorded in the accompanying check result before independent peer review. This candidate has not yet been applied to canonical gene files.

### First follow-up application

The independently approved correction was applied and the targeted review page rendered. Full normal candidate and canonical validation passed with 40 warnings: 34 standing-policy binding advisories, two unresolved-propagation metadata advisories, one unused generated-research advisory and three core-coverage advisories. DRAFT remains appropriate. A new standard codex/gpt-6 EDIT history for PR3908 was scaffolded and validated; previous history, all source/cache bytes, 119 machine assertions, three products, 85 reference identities and both cores were preserved. The interphase-cytoplasm anchor is attached to the matching cytoplasm assertion.
