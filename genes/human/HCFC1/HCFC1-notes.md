# HCFC1 curation notes

## 2026-11-15: identity and evidence scope

Human HCFC1 (HGNC:4839; UniProt P51610; 2035 amino acids) encodes host cell factor 1. The native seed contains 114 GO annotation contexts and four alternative splice products. Preserve the seeded identifiers, evidence codes, partners, qualifiers and alternative-product mappings. The six N-terminal and six C-terminal CHAIN features describe proteolytic products, a different distinction from alternative splicing.

This is manual primary-literature research. The known Falcon authentication and Perplexity quota failures remain unresolved; no provider-generated deep-research report is claimed. Some publications remain abstract-only. Specific conclusions below distinguish accessible experimental evidence from unresolved source contexts.

## Transcriptional scaffold and context-dependent regulation

HCFC1 links transcription factors to chromatin-regulatory complexes. Human HeLa purification and interaction studies support tethering of SIN3 and SET1/Ash2 machinery; some domain-mapping assays use mouse constructs in yeast. Associated deacetylase or methyltransferase activity belongs to the partner complexes, not an intrinsic HCFC1 catalytic domain. [PMID:12670868, *Human Sin3 deacetylase and trithorax-related Set1/Ash2 histone H3-K4 methyltransferase are tethered together selectively by the cell-proliferation factor HCF-1.*: “HCF-1 tethers the Sin3 and Set1/Ash2 transcriptional regulatory complexes together”.]

The direction of regulation depends on the recruited factors. The E2F study reports activation with E2F1 and repression with E2F4; its cached abstract supports that distinction but does not justify inventing assay details. [PMID:17612494, *E2F activation of S phase promoters via association with HCF-1 and the MLL family of histone H3K4 methyltransferases.*: “coactivator properties when bound to the E2F1 activator and corepressor properties when bound to the E2F4 repressor”.]

THAP11/ZNF143 promoter recruitment experiments support the bridging mechanism. Chromatin occupancy does not establish intrinsic sequence-specific DNA recognition by HCFC1. [PMID:26416877, *Genomic Determinants of THAP11/ZNF143/HCFC1 Complex Recruitment to Chromatin.*: “HCFC1 serves as a scaffold protein, bridging interactions between transcription factors”.] Full-text access was incomplete for this source; the abstract and accessible figure descriptions were reviewed.

Human SET1/MLL complex studies support HCFC1 as an accessory interactor, not necessarily a stoichiometric catalytic subunit. The quantitative complex survey explicitly supports SET1A/B and MLL1/2 associations and does not establish MLL3/4 membership. The WDR82 study identifies HCF1 in repeated SET1 affinity purifications. [PMID:23508102, *Quantitative dissection and stoichiometry determination of the human SET1/MLL histone methyltransferase complexes.*; PMID:18838538, *Molecular regulation of H3K4 trimethylation by Wdr82, a component of human Set1/COMPASS.*.] Both sources were refreshed with full text through the native publication fetcher.

## Processing and fragment-specific experiments

OGT initiates HCF-repeat cleavage through glycosylation of a glutamate side chain and formation of an internal pyroglutamate; subsequent backbone hydrolysis is proposed to occur after enzyme dissociation. The later chemical study includes repeat-derived model peptides and modified constructs. It does not establish autonomous HCFC1 protease activity. [PMID:24311690, *HCF-1 is cleaved in the active site of O-GlcNAc transferase.*; PMID:27618188, *How the glycosyltransferase OGT catalyzes amide bond cleavage.*: “Glycosylation on glutamate is followed by conversion to an internal pyroglutamate”; “Hydrolysis likely occurs after dissociation from the enzyme.”]

Native UniProt SITE descriptions retain legacy “autolysis” wording. Preserve the source record and describe the experimentally established OGT-dependent mechanism in the review. No NEW proteolysis or maturation annotation is inferred simply because HCFC1 is processed.

Human HeLa depletion/rescue experiments distinguish N-fragment functions in G1 progression from C-fragment functions in mitotic exit and cytokinesis. The study also includes hamster cells and mouse fibroblasts; the primary-cell experiment is not human. Engineered HCF-1N1011 and HCF-1C600 constructs do not independently validate every native cleavage product. Grouped functional classes can retain all twelve chain IDs while explicitly limiting the functional inference. [PMID:12743030, *Proteolytic processing is necessary to separate and ensure proper cell growth and cytokinesis functions of HCF-1.*; PMID:21295698, *O-GlcNAc transferase catalyzes site-specific proteolysis of HCF-1.*.]

HCFC1 also stabilizes nuclear OGT in human-cell experiments. Uncleaved HCFC1 can remain chromatin-associated after OGT depletion, so cleavage is not treated as a universal prerequisite for chromatin binding. [PMID:21285374, *Crosstalk between O-GlcNAcylation and proteolytic cleavage regulates the host cell factor-1 maturation pathway.*: “HCF-1 is, in turn, required for stabilizing OGT in the nucleus.”]

## MLL5 recruitment versus disputed catalytic interpretation

HCFC1-dependent recruitment of MLL5/KMT2E to E2F-responsive promoters is experimentally separable from claims that MLL5 itself methylates histones. Retain assessable interaction/recruitment results without transferring catalytic claims to HCFC1. [PMID:23629655, *Mixed lineage leukemia 5 (MLL5) protein regulates cell cycle progression and E2F1-responsive gene expression via association with host cell factor-1 (HCF-1).*.]

The earlier MLL5 GlcNAcylation paper (PMID:19377461) was retracted, with notice PMID:24336203. That notice does not retract PMID:23629655. Independent structural and biochemical work on human MLL5 SET constructs supports lack of intrinsic methyltransferase activity. [PMID:24336203, *Retraction: GlcNAcylation of a histone methyltransferase in retinoic-acid-induced granulopoiesis.*; PMID:27812132, *The Human Mixed Lineage Leukemia 5 (MLL5), a Sequentially and Structurally Divergent SET Domain-Containing Protein with No Intrinsic Catalytic Activity.*.]

## Source-specific limitations

PMID:20091349 resolves on PubMed to an osteoarthritis/chondrocyte study whose abstract describes an animal model. It is the native source for three localization contexts. The accessible abstract does not establish the HCFC1 experiments; full text and annotation provenance remain to be reconciled. Preserve the original identifier and leave these contexts unresolved. Do not infer a replacement PMID or declare curator misattribution merely from the title/abstract.

HSV immediate-early transcription and release from latency are infection contexts. Later conditional mouse Hcf1 deletion experiments support a causal role in reactivation, but they are not new human experimental annotations. [PMID:10675337; PMID:36692302, *Deletion of the Transcriptional Coactivator HCF-1 In Vivo Impairs the Removal of Repressive Heterochromatin from Latent HSV Genomes and Suppresses the Initiation of Viral Reactivation.*.]

Specific protein interactions require source-by-source review. In particular, CREBZF and the GABP beta coactivator must not automatically be described as DNA-binding transcription factors. High-throughput interaction or localization evidence alone does not establish a new core function.

## Retained native evidence and provenance

Native fetched sources and the 114-row seed are retained in commit `63575f1ec17aaa2d2eb10fa0fc120345e7b76fce`. The fetch downgraded PMID:23629655 to an abstract; commit `ce561d2ead51d432fbc215b0d668c369e7cfa89c` restores the exact 39,051-byte full-text record from base `a0fef8e0aa0b75e1842f20a7795c1d413e0ff1ba`. The fetched abstract remains recoverable in Git. Canonical full-text SHA256: `47e0938ae3a988ac2d4bafa0f5167dee894d8ed5c175b0187c8b4795e046e860`.

The native PTHR46003 PAINT slice was produced from retained source files without downloading or modifying the global cache. It contains four positive IBD assertions at PTN000582135: GO:0003713, GO:0006338, GO:0006355 and GO:0035097. No loss assertions occur in this slice. This checks the recorded node assertions, not the entire tree topology or alignment. A target appearing among its own descendant evidence is expected, not circular.

Retained PAINT source SHA256 values:

- Leaf GAF: `8ccffa658f6cb8a925a66353a236091a14130ffa7457e1fbf3681d737102b199`
- IBD GAF: `0c672914e10c1f79d3fb365077d843a92e518eb6eee2aac00c67150274adf569`
- TreeGrafter annotations: `03ad195b42a48ff2fb0caadd337bf2c98464382855618c1f14fe2869b3d6bf3f`
