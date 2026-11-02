# CTNNB1 (human, P35222) - curation notes

**Automated deep research was unavailable** (no deep-research provider keys in this
environment). These notes were written by hand from the cached publications in
`publications/` (many are abstract-only; see `full_text_available:`), the UniProt
record, the sister reviews of human VCL, sponge VIN1 and human CDH1, and a small
UniProt/PANTHER census in `CTNNB1-bioinformatics/`. No `-deep-research-*.md` file
exists for this gene.

## Core molecular functions

### 1. Wnt/TCF transcriptional coactivator (nuclear pool)

- Coactivator of LEF/TCF [PMID:11751639 "beta-catenin, a dedicated coactivator of LEF/TCF enhancer-binding proteins"];
  [PMID:11751639 "recombinant beta-catenin strongly enhances binding and transactivation by LEF-1 on chromatin templates in vitro"].
- TCF4 activity depends on beta-catenin [PMID:9065401 "hTcf-4 transactivates transcription only when associated with beta-catenin"];
  constitutive complexes in APC-/- cells [PMID:9065401 "Nuclei of APC-/- colon carcinoma cells were found to contain a stable beta-catenin-hTcf-4 complex that was constitutively active"].
- Structure of the TCF4-beta-catenin complex [PMID:11713476 "it interacts with the Adenomatous polyposis coli (APC) protein and TCF/Lef family transcription factors"].
- BCL9-Pygopus recruitment [PMID:17052462 "Stimulation of the Wnt pathway leads to the association of beta-catenin with Tcf and BCL9 in the nucleus"];
  [PMID:11955446 "Wnt transduction is mediated by the association of beta-catenin with nuclear TCF DNA binding factors"].
- CBP/p300 [PMID:21751375 "p300/CBP (CREB-binding protein) is recruited by nuclear β-catenin to regulate a wide array of T-cell factor (TCF)-dependent gene expression"].
- Other DNA-binding partners: FOXO [PMID:15905404 "beta-Catenin binds directly to FOXO and enhances FOXO transcriptional activity in mammalian cells"];
  nuclear receptors [PMID:22187462 "The LRH-1 binding site in β-catenin is also required for association with androgen receptor"].
- ICAT blocks TCF binding but not cadherin binding [PMID:12408824 "We show that ICAT selectively inhibits beta-catenin/Tcf binding in vivo, without disrupting beta-catenin/cadherin interactions"].

### 2. Cadherin and alpha-catenin binding (junctional pool)

- Binds cadherins [PMID:11713476 "The multifunctional protein beta-catenin is important for cell adhesion, because it binds cadherins"];
  links VE-cadherin to the cytoskeleton [PMID:18287330 "linking the VE-cadherin junction complex to the cytoskeleton"].
- Stabilizes the E-cadherin complex [PMID:18593713 "Smad7 increases the stabilized beta-catenin to form a complex with E-cadherin and stabilizes the E-cadherin-beta-catenin complex"];
  surface E-cadherin via vinculin [PMID:20086044 "an interaction between beta-catenin and vinculin is crucial for stabilizing E-cadherin at the cell surface"].
- Alpha-catenin binding through the N-terminal half [PMID:7890674 "although the amino-terminal half independently binds alpha-catenin"];
  reciprocal site on alpha-catenin [PMID:9264463 "Here we have now identified the reciprocal complementary binding site in alpha-catenin which mediates its interaction with beta-catenin and plakoglobin"].

### Regulation (destruction complex)

- APC binding [PMID:8638126 "The APC protein binds to the cellular adhesion molecule beta-catenin"];
  GSK3/Axin [PMID:17318191 "Axin/GSK3beta binding to beta-catenin and its subsequent S/T phosphorylation"].
- SCF(beta-TrCP) recognition [PMID:12820959 "The F box protein beta-TrCP1 recognizes the doubly phosphorylated DpSGphiXpS destruction motif, present in beta-catenin and IkappaB"].
- Oncogenic stabilizing mutations [PMID:9065402 "colorectal tumors with intact APC genes were found to contain activating mutations of beta-catenin that altered functionally significant phosphorylation sites"].

### Peripheral functions

- PDZ-binding motif [PMID:17242191 "such as the one between the β-catenin PDZ motif and the PDZ2 domain"];
  proteome-scale PDZ affinity map [PMID:36115835 "both containing PBMs that detectably bound to PDZs in our quantified interactome"].
- Centrosome [PMID:18086858 "We show that beta-catenin binds to and is phosphorylated by Nek2"];
  [PMID:20300119 "Wnt/β-catenin signalling and conductin regulate centrosomal cohesion by altering the phosphorylation status of β-catenin at the centrosomes"].
- PML SUMOylation [PMID:22155184 "β-catenin inhibited Ran-binding protein 2-mediated SUMOylation of PML-IV"].

## GO-CAM

`gocams/index.tsv` lists one CTNNB1 activity: model 62900b6400001630 "PTEN in excitatory
hippocampal synapse long-term depression (Human)", activity
gomodel:62900b6400001630/62900b6400001715, enabled by CTNNB1 (ISS from rat RGD:70487):
GO:0003713 transcription coactivator activity, part of GO:0045944 positive regulation of
transcription by RNA polymerase II, occurring in GO:0000785 chromatin. This model is the source of the
ISS rows for chromatin, transcription coactivator activity (RGD:70487) and long-term
synaptic depression. The MF typing agrees with core function 1.

## Annotation review summary (723 rows)

- **Protein binding (335 IPI rows).** Following repository policy:
  - MODIFY where the partner defines a specific binding function: cadherins to cadherin
    binding, alpha-catenins to alpha-catenin binding, TCF/LEF/SOX/FOXM1/RUNX3/NF-kappaB
    and other DNA-binding factors to DNA-binding transcription factor binding, nuclear
    receptors to nuclear receptor binding, protein kinases (GSK3B, SRC, ABL1, NEK2, TNIK,
    RTKs) to protein kinase binding, PTPs to protein phosphatase binding, beta-TrCP and
    other E3s to ubiquitin protein ligase binding, PDZ proteins to PDZ domain binding,
    CBP/p300 to histone acetyltransferase binding, HDAC6 to histone deacetylase binding,
    and BCL9/BCL9L, TBL1/TBLR1, parafibromin, MLLT10, CITED1, YAP/TAZ to transcription
    coregulator binding.
  - REMOVE otherwise. This includes the destruction-complex scaffolds APC, Axin and AMER1
    (captured by the destruction complex CC rows), ICAT (captured by the beta-catenin-ICAT
    complex row) and the neurodegeneration Y2H screen PMID:32814053.
  - Two specific REMOVE cases:
    - PMID:12370829 PTPRC: the abstract reports that CD45 did *not* bind catenins
      [PMID:12370829 "Catalytic domains of the tyrosine phosphatases PTP-PEST, CD45, and PTPbeta did not interact with proteins of the catenin family to detectable levels"].
    - PMID:19433865 HDAC1/2/APPL: the association goes through Reptin
      [PMID:19433865 "The ability of Reptin to bind both β-catenin and HDAC1 further suggested the formation of a β-catenin-Reptin-HDAC1 complex at the promoter"].
- **Substrate-type process rows removed** (participation test): protein polyubiquitination
  and proteasome-mediated catabolism (PMID:29374064), and regulation of protein
  ubiquitination (PMID:15829978). Beta-catenin is the substrate in all three
  [PMID:29374064 "IRF2BPL in turn interacted with β-catenin, increasing its ubiquitination and degradation"].
- **MODIFY of non-binding rows:**
  - Obsolete GO:0030331 nuclear estrogen receptor binding to GO:0016922. QuickGO
    confirms the obsolescence and gives GO:0016922 as the consider term.
  - GO:0070602 regulation of centromeric sister chromatid cohesion to GO:0030997
    regulation of centriole-centriole cohesion. The cited paper (PMID:20300119) is
    about centrosome cohesion.
  - GO:0019900 kinase binding with GSK3B to protein kinase binding.
  - Enzyme binding with HDAC6 to histone deacetylase binding.
- **UNDECIDED:** GO:0045892 negative regulation of DNA-templated transcription (IMP,
  PMID:19653274). The abstract says the LEF-1 isoform effect is beta-catenin-independent
  [PMID:19653274 "Forced expression of Lef-1 Deltaexon VI inhibited E-cadherin expression in a beta-catenin-independent way"],
  and the full text is not cached.
- **Over-annotated:**
  - Chromatin binding (beta-catenin has no DNA-binding domain).
  - Detection of mechanical stimulus and detection of muscle stretch.
  - Wnt signalosome.
  - Negative regulation of canonical Wnt signaling.
  - Response to xenobiotic stimulus (sulindac) and response to indole-3-methanol (both
    expression-change evidence).
  - Bicellular tight junction, focal adhesion (HDA) and extracellular exosome (HDA).
- **Non-core:** the many mouse-derived developmental, neural and synaptic terms. These
  are downstream outputs of Wnt/TCF target genes or tissue-specific instances of
  junctional localization.
- **IBA rows** (PAINT node PTN001153077): cadherin binding, alpha-catenin binding, catenin
  complex, adherens junction, cell-cell adhesion, transcription coactivator activity,
  canonical Wnt signaling, nucleus/cytoplasm, nuclear receptor binding, protein
  phosphatase binding and positive regulation of Pol II transcription. All accepted.
  Human CTNNB1 among the donors is expected, not circular. The donors are bilaterian
  (fly arm, worm hmp-2/bar-1/sys-1, mouse, zebrafish, human JUP).

## Premetazoan evidence: ancestral vs animal-specific

**Bioinformatics** (`CTNNB1-bioinformatics/RESULTS.md`):
- PANTHER PTHR45976, the beta-catenin/Armadillo family containing CTNNB1 as SF4, has 4921
  metazoan UniProt members.
- It has 0 members in choanoflagellates, Filasterea, Ichthyosporea or Dictyostelium. The
  only 2 non-metazoan hits are isolated plant entries, probably contamination.
- Dictyostelium Aardvark (Q54I71) is classified in PTHR22895 "ARMADILLO REPEAT-CONTAINING
  PROTEIN 6", not in the beta-catenin family.

**Literature (all read in the cache):**
- *Beta-catenin as an animal-specific family:* catenin beta is a core animal-specific
  family [PMID:29848444 "this set of genes includes seven from the Wnt pathway (including Frizzled, Dishevelled, TCF/LEF and β-catenin)"].
  Wnt-pathway genes are largely absent outside animals
  [PMID:20883218 "Most of these genes are not detected in the choanoflagellate and other nonmetazoan eukaryotic genomes"].
- *The armadillo fold is older* [PMID:23481191 "the cadherin repeat domain and the armadillo repeat domain, predate metazoans"].
- *Dictyostelium (Amoebozoa, an independent origin of multicellularity):*
  - Aardvark acts at actin-associated junctions and separately in signalling
    [PMID:11130075 "We have isolated a gene encoding a beta-catenin homologue, aardvark, which is a component of the junctional complex, and, independently, is required for cell signalling"].
  - The authors concluded [PMID:11130075 "the dual role of beta-catenin in cell-cell adhesion and cell signalling evolved before the origins of metazoa"].
  - The later study showed that an alpha-catenin ortholog binds Aardvark to build a
    polarized epithelium without cadherins
    [PMID:21393547 "Although D. discoideum lacks a cadherin homolog, we identify an α-catenin ortholog that binds a β-catenin-related protein"];
    [PMID:21393547 "the role of the catenins in cell polarity predates the evolution of Wnt signaling and classical cadherins"].
  - Aardvark's signalling role does not go through GSK-3, i.e. it is not Wnt-like
    destruction-complex signalling
    [PMID:12128211 "This process does not involve the kinase GSK-3"].
- *Classical cadherins are an animal innovation*
  [PMID:22837400 "the later appearance of classical cadherins coincides with metazoan origins"].
  - The sponge beta-catenin keeps the residues that bind cadherin
    [PMID:22837400 "Oc_bcat has two lysine residues (homologous to positions K312 and K435 in mouse) required for the interaction of mouse β-catenin with E-cadherin"].
  - A Y2H screen with the sponge beta-catenin recovered the sponge classical cadherin (same paper).
- *Nuclear signalling is ancient within animals:* cnidarian nuclear beta-catenin
  specifies endoderm
  [PMID:14647383 "translocated into nuclei in cells at the site of gastrulation and used to specify entoderm"].
- *Sponge vinculin* did not bind a beta-catenin peptide
  [PMID:29880641 "Moreover, Op vinculin bound talin but not β-catenin"].
  The VCL review notes that this peptide was the alpha-catenin-binding region, so the
  result does not test the human vinculin-beta-catenin N-terminal interface.

**Synthesis:**
- Ancestral (pre-animal), in the broad sense: an armadillo-repeat catenin working with
  alpha-catenin to organize cell polarity and junctions. The evidence comes from
  Dictyostelium. Whether Aardvark shares descent with beta-catenin or converged on this
  role is unresolved: PANTHER does not place it in the beta-catenin family, and no
  beta-catenin-family protein is classified in unicellular holozoans.
- Animal-specific:
  - The beta-catenin family itself (by current classification).
  - Binding of classical cadherins (the partners arise with animals, though present in
    sponges).
  - TCF/LEF-dependent transcriptional coactivation in Wnt signalling (TCF/LEF and Wnt are
    animal-specific).
  - All of the developmental, tissue and synaptic process terms.
- Both the junctional and the Wnt/TCF roles were present in the last common ancestor of
  animals (sponge cadherin-binding residues; sponge Wnt-pathway components; cnidarian
  nuclear beta-catenin).
- Unverified background, not cited: whether ctenophores have a TCF-coupled beta-catenin.
  I did not read primary data on this.


## 2026-10-13: complete source-specific augmentation

This entry supplements the preserved journal above. It supersedes its older generic-binding removal policy and the source interpretations identified below. All 723 historical annotation source objects remain exact, including qualifiers, partner accessions, evidence codes and multiplicity. The current 737 API records and 736 literal TSV rows reconcile to those same 723 source keys; date-only and other literal multiplicities remain in the audit rather than being rewritten into the historical cache. No NEW annotation is proposed.

The full review now distinguishes 255 ACCEPT, 233 KEEP_AS_NON_CORE, 185 MODIFY, 44 UNDECIDED, three REMOVE and three MARK_AS_OVER_ANNOTATED decisions. Of 335 generic protein-binding assertions, 180 receive source-supported refinements, 120 remain positive non-core interactions, 34 are unresolved and one is contradicted by its original experiment. This follows the standing project instruction in `projects/CLINGEN_MENDELIAN.md` under the generic-binding policy: retain supported correct interactions when no justified specific replacement is available. A partner class describes what beta-catenin binds; it does not assign that partner's catalytic activity to beta-catenin.

### Molecular functions and products

The two compact core units are nuclear transcriptional coactivation and cadherin-tail binding at adherens junctions. The latter explicitly includes alpha-catenin recruitment without assigning alpha-catenin's actin-binding function to beta-catenin. Human LEF/TCF chromatin-template experiments establish cooperative beta-catenin association and transcriptional activity; absence of an intrinsic sequence-specific DNA-binding domain does not exclude partner-mediated chromatin association. ICAT can suppress transcription while the LEF–beta-catenin complex remains chromatin-bound at the tested doses, so its action is not universally simple displacement (PMID:11751639). The source's positive binding does not by itself establish the narrower current transcription-corepressor class for ICAT.

The official P35222 record supplies one displayed 781-residue product and no ALTERNATIVE PRODUCTS listing. This limited official scope is not a claim that all transcripts or experimental deletions are equivalent. Human TCF7L2 residues 8–54 and beta-catenin 134–668 were coexpressed in bacteria for the structural study, with 293-cell reporter tests (PMID:11713476). Other studies use truncations, phosphosite mutants, species-specific constructs and tagged domains; curated whole-reference ROGIDs do not establish the actual fragment sequence. The prior taxonomic census is preserved as a historical classification analysis, not a new origin-date inference. Its own limitations leave the relationship of Dictyostelium Aardvark unresolved; the actual current PAINT node placement is assessed separately.

### Interaction identity, catalytic classes and quantitative screens

Historical TCF4 is an important accession ambiguity. Official P15884 is TCF4/E2-2; Q9NQB0 is TCF7L2, historically also called TCF4. Recovered original Methods and fragments frequently describe HMG TCF/LEF reagents. Eight exact P15884 pair assertions therefore remain UNDECIDED without replacing their source accessions. The PMID:25402006 experimental GST/radiolabel pair is retained with curator deference and a specific RNA polymerase II transcription-factor-binding refinement: its canonical P15884 assignment has no observed contradictory insert in the material available. Its supplementary image/insert remains unread. The biologically supported TCF/LEF complex remains ACCEPT, with the accession ambiguity explicit. A TCF7L2 quotation is not reused as proof of a distinct P15884 pair.

PMID:12370829 Figure 3B is a genuine source contradiction for the CD45 pair: the target-height beta-catenin band occurs for DEP1 D/A with pervanadate, not CD45 D/A. The original experiment uses bacterial GST catalytic-domain trapping constructs and HUVEC lysates. The positive MINT source field remains untouched; the specific assignment is REMOVE without a new NOT assertion or a universal claim that CD45 never associates with beta-catenin. A separate phosphopeptide/CD45 interaction in PMID:19167335 remains distinct.

PTPRU binding is retained while its older active-phosphatase interpretation is qualified by the later pseudophosphatase original (PMID:32591542). The historical dephosphorylation excerpt is preserved at that row as a disputed claim. It is removed as generic corroboration for unrelated phosphatase partners. PTPN23 is assessed independently: PMID:19340315 reports negative wild-type synthetic-substrate activity, whereas PMID:21724833 reports peptide turnover and E1357A lysate trapping, and PMID:29066500 reports wild-type-domain dephosphorylation of immunoprecipitated FYN relative to C1392S. These support a qualified phosphatase partner class; none proves that beta-catenin itself was dephosphorylated in the trapping assay. PTPRU's class is not transferred to PTPN23 by analogy.

The actual fragmentomics workbook contains 266 beta-catenin entries: 133 measured DAPF rows and 133 entries with blank assay fields. The tested beta-catenin tail is residues 772–781, NQLAWFDTDL, paired with isolated PDZ domains (PMID:36115835). Seventy literal records reconcile with the 27 imported generic assertions. Twelve receive PDZ-domain-binding refinement; fifteen remain UNDECIDED where the recorded domain is below quantification. Positive alternate domains are explicitly separated from a censored original-domain record. The LNX1 PDZ1 result lies only 0.00004825 above the BI 0.05 threshold, with n=2 and no reported SD; it is not robust affinity evidence for every LNX1 product. The correction concerns figure labels, not replacement of the workbook. The public index supplies compact domain/assay limits, not a raw workbook dump.

### Processes, localization and performed roles

The original centrosome experiments measure gamma-tubulin-marked centrosome separation and beta-catenin phosphorylation/localization. They support regulation of centriole cohesion, not centromeric sister-chromatid cohesion (PMIDs:18086858 and 20300119). The latter cache is partial despite its true full-text flag; its missing Results/Discussion were genuinely recovered independently. The mouse source record is now traced directly, rather than described as an unavailable donor lookup. NEK2 binding has recombinant evidence; rootletin co-IP is retained without claiming personally inspected supplemental Far-Western data.

The three source-specific removals concern the CD45 assay above and two assignments treating beta-catenin's own IRF2BPL-dependent ubiquitination/turnover as work it performs (PMID:29374064). By contrast, the complete PMID:23245942 abstract explicitly describes beta-catenin bridging TAZ to beta-TrCP. That different-substrate regulatory role supports non-core regulation of ubiquitination; its full original remains inaccessible. The old own-substrate excerpt is retained alongside the new abstract anchor so that this distinction is visible. The ICAT-derived negative-Wnt assertion is over-annotated because ICAT performs inhibition and beta-catenin is its inhibited target (PMID:10898789).

Mechanical participation is not rejected merely for lacking an autonomous sensor. The molecular interface measured in fly experiments and mouse-structure simulations can support a conserved human inference, with human Y654 verified, and is retained as non-core detection of mechanical stimulus (PMID:30024850). This is not a human or muscle experiment. The specific muscle-stretch assertion from PMID:30568254 remains unresolved because expression/localization and accessible cited abstracts do not settle that endpoint.

The indole-3-carbinol study reports catenin abundance changes after 24 hours in human MCF-7 and MDA-MB-468 cells, with a proposed joint cadherin–catenin anti-invasion mechanism (PMID:10868478). The response definition permits expression changes and does not require direct sensing. GO expression guidance nevertheless permits declining an expression-only association where participation is not established (GO Consortium guide, PMC3706743, expression-study paragraph). The indole rows remain source-specific overannotations of beta-catenin's performed contribution, preserving the positive observation. Sulindac also changes beta-catenin/TCF activity and target expression, but operative Methods/Results are absent from the selected cache; that response assertion remains UNDECIDED (PMID:18291362).

Other contextual positives retain actual source scope: TRPC4 association, targeting and calcium entry depend on cell-contact state, with mouse channel constructs and human hosts distinguished (PMID:19996314); the M8P/vinculin experiments support cadherin-surface stabilization without loss of every beta-catenin partner (PMID:20086044); the antibody-specificity paper preserves controlled beta-catenin redistribution while identifying a cross-reacting nuclear antigen (PMID:19187541). The SATB1 source remains accompanied by its editorial notices, not treated as retracted or free of concerns. Corrections to PMID:22056988 and PMID:33428810 have narrower reporting scopes and do not reverse the inspected target findings.

### Phylogeny, transfers and curated models

The actual 137-node PTHR45976 tree and MSA contain the exact 781-residue target PTN002511128. All 12 scoped IBDs are at on-path PTN001153077, with their recorded taxon placement preserved. Short donor lists and legitimate human self donors are not failures. The full donor and orthology records retain extensions and assay contexts; not every underlying donor paper was personally read. Missing current exact records are distinguished from functional loss, with descendant terms checked where appropriate. The seven ARBA rules were reconstructed across 1,295 condition branches; matching a branch does not settle the biological scope of its output.

All 77 cited Reactome event summations and 160 literal target paths were inspected. Beta-catenin can appear in a complex, as a phosphorylated substrate or as an input to a reaction; membership does not give it the catalyst's activity. HPA XML supports its stated plasma-membrane, junction and conditional ciliary/basal-body contexts; image-pixel inspection is not claimed.

GO-CAM 62900b6400001630 retains activity 62900b6400001715: transcription coactivator activity in chromatin, placed within positive transcription regulation and hippocampal LTD through rat RGD:70487 transfer. This corroborates the coactivator role but is not an independent human LTD experiment. The exact current rat LTD source was not reconstructed, and the inspected mouse PTEN promoter-occupancy work does not independently settle beta-catenin-specific LTD performance. The LTD row remains UNDECIDED. Likewise, cytosolic LRRK2/destruction-complex co-IP and a recruitment model do not settle direct receptor-associated Wnt-signalosome membership (PMIDs:22899650 and 24115276).

### Access and preservation

The 265 historical PMID abstracts were personally read, together with the explicitly recorded selected original Methods/Results and independently attributed bounded consultations. A cache's full-text flag does not establish complete experimental access. References distinguish source identity, target support, original recovery and unread supplementary data. The immutable audit contains raw receipts, exact source joins and personal read windows; the compact public index provides reproducible public/repository locators and conclusions without copying those responses or every annotation decision.

The normal isolated fetch completed. Genuine default Falcon and bounded fallback attempts ended in timeouts without a provider report; no manual text is labeled as provider output. Historical notes, source caches, provider artifacts, bioinformatics and six history records remain preserved. Relevant supplied excerpts are retained; narrow removals correct a misleading partner/role linkage, not a blanket quotation budget. The sole newly selected external quote is the short PMID:23245942 bridge statement, used once in the annotation support.


### Independent whole-review refinements

The receptor-binding comparison refines two further positive interactions to GO:0005102. PMID:21132015 reports human PTK7 intracellular-domain mapping, full-length co-immunoprecipitation in COS7 cells and endogenous Caco2 association. PMID:24960609 reports mouse Ryk full-length and uncleavable receptor association with endogenous beta-catenin in 293T cells, separately from its released intracellular domain. Neither refinement assigns kinase activity to the pseudokinase partner or agonist activity to beta-catenin. COS7 is not a human cell line; the paper's wording is not repeated as a species claim.

The final counts after these two refinements are 255 ACCEPT, 231 KEEP_AS_NON_CORE, 187 MODIFY, 44 UNDECIDED, three REMOVE and three MARK_AS_OVER_ANNOTATED. Among the 335 generic-binding sources, 182 are refined, 118 retained as non-core, 34 unresolved and one removed. Four additional reason corrections preserve actions: B6V8E6 is the dog ortholog, and NAS/TAS neurogenesis rows and the human IMP mesenchymal-stem-cell row do not inherit the mouse-transfer wording from other annotations. All original source objects, references, products, quotations and both core functions remain unchanged.


## 2026-10-14: explicit alpha-catenin core and finite review follow-up

The molecular-function schema has one MF slot per core unit. Alpha-catenin binding (GO:0045294) is therefore restored as an explicit third core alongside transcriptional coactivation and cadherin binding. Its N-terminal interaction recruits the alpha subunit into junctional machinery, while alpha-catenin supplies the regulated actin-associated interface. Five existing alpha-catenin-binding annotations and eleven binding refinements already retain this function. Two existing source-exact anchors from PMID:7890674 and PMID:9264463 move from the cadherin core to the new alpha-catenin core, without duplication. Their cached abstracts explicitly report the interaction/domain mapping, but do not authenticate all assay constructs. The comparative Dictyostelium source PMID:21393547 remains relevant comparative evidence in the preserved findings and journal, not a direct human experimental anchor or a resolved origin-date claim.

The preceding statement that “both core functions remain unchanged” described only the final twelve-leaf owner refinement relative to its already two-core first draft. It did not describe the change from the historical three-core review. That earlier consolidation is now reversed at the machine-readable MF level. All prior journal text and history records remain intact; this paragraph supersedes the earlier two-core synthesis.

The optional FLYWCH1/ICAT generalization was reconsidered against both current definitions. GO:0001221 retains the non-DNA-binding coregulator/basal-machinery role; moving to that parent does not resolve the source-specific classification uncertainty. Positive FLYWCH1 binding/repression and ICAT inhibition remain explicit under their existing UNDECIDED and KEEP_AS_NON_CORE decisions. No domain-absence exclusion or negative binding assertion is introduced.

LNX1 PDZ1 remains a narrow biochemical positive under the original study’s BI threshold: 0.05004825 exceeds 0.05, but with only two measurements and no standard deviation. The source-specific precision caveat is now explicit in its reason. This differs from the fifteen below-quantification rows; no new threshold or statistical confidence is invented. The conserved mechanosensing inference remains explicitly based on fly experiments and mouse-structure simulations, not direct human or muscle assays. One duplicate bare PMID:15829978 support pointer is removed; its inherited quoted evidence and the independent PMID:23245942 TAZ-bridging support are retained.

The other nonblocking suggestions do not require broad scientific churn: source-specific HIGH relevance records remain tied to the actual asserted functions; detailed reasons carry the assay/partner distinctions behind repeated concise summaries. Earlier history is append-only; the new history can name only applicable YAML sections and mention the separate notes/evidence files in its details. Genuine provider failures remain documented, with no fabricated report or repeated provider request in this finite follow-up. All 723 source objects, actions/replacements, 360 references, official product, machine caches and prior notes are preserved.
