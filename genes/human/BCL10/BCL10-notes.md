# BCL10 evidence review, 2026-09-30

Research before canonical import used the authenticated Seed46 archive (`8fa1efcff2c9694bbdd924c9b33898993adeafbdae3ebefd11a38bd77f34c7d7`). This is a reviewer log, not a generated provider report. No source cache was edited.

All 58 normally fetched PMID records were inspected at the abstract/metadata level (1040062 has no abstract): initial batches cf5830/d12b10, then e369db, b00e0b, 1ac036, dee841, bc5f01. The full 178 source assertion tuples were read as 876e14. Source assertions include two contributes_to kinase-activator entries; preserve those qualifiers. Source products and alternative_products are null, not an invented isoform list.

PMID:24074955, *Structural architecture of the CARMA1/Bcl10/MALT1 signalosome: nucleation-induced filamentous assembly*: selected complete Results and Methods paragraphs 11–13,20–22,43–44,47,50,64 read as 43e9ee. Human recombinant CARD11/BCL10 forms CARD filaments; the reconstituted ternary complex incorporates MALT1, enhances MALT1 activity, and filament-interface mutations impair NF-kappaB signaling. Endogenous HBL-1 immunoprecipitates also contain CBM components with filamentous morphology. This supports BCL10 as a signaling adaptor, not an enzyme. The initial overly broad display 8548d6 was truncated and is not a full-text read claim.

PMID:28628108, *Germline hypomorphic CARD11 mutations in severe atopic disease*: selected complete Results and Methods paragraphs 15,71 read as 43e9ee. BCL10 co-immunoprecipitation directly assays mutant-dependent impairment of CARD11/MALT1 assembly in human T-cell lines. The CARD11-focused title is not a reason to reject BCL10 complex membership.

PMID:25365219, *Inherited BCL10 deficiency impairs hematopoietic and nonhematopoietic immunity*: primary JCI Results/captions previously read at lines331–394. The BCL10-deficient patient has strong lymphocyte and fibroblast defects, while tested myeloid cytokine responses are preserved. Human innate dependence is cell-type specific; do not describe universal dependence of all human innate responses on BCL10.

PMID:15125833, *The TRAF6 ubiquitin ligase and TAK1 kinase mediate IKK activation by BCL10 and MALT1 in T lymphocytes*: abstract explicitly describes purified biochemical reconstitution. Oligomeric BCL10/MALT1 promotes TRAF6/TAK1/IKK activation. Retain contributes_to kinase activator and use signaling adaptor as the principal molecular function.

PMID:15207693, *Characterization of Bcl10 as a potential transcriptional activator that interacts with general transcription factor TFIIB*: normally fetched abstract and independently indexed PubMed source (turn7061search1) describe mammalian Gal4-DBD fusion assays and TFIIB interaction, with activity mapped to the N-terminal13 residues. This supports contextual non-core coactivation/TFIIB binding; it does not establish constitutive sequence-specific DNA binding. No full-paper read claimed.

PMID:16280327, *A pathway for tumor necrosis factor-alpha-induced Bcl10 nuclear translocation*: normal abstract and indexed PubMed identity read. MCF7 TNFalpha induces Akt phosphorylation and BCL3-associated nuclear translocation. The abstract's NF-kappaB-binding site is in BCL10 regulatory DNA; the existing protein-binding annotation needs full-paper verification. DOI full-text open failed; keep uncertainty, do not claim wrong-gene or misattribution from abstract alone.

PMID:22267217, *Dectin-1 is an extracellular pathogen sensor for the induction and processing of IL-1beta via a noncanonical caspase-8 inflammasome*: normal abstract/publisher abstract+figure captions establish CARD9/BCL10/MALT1/caspase8/ASC assembly and IL1B induction/processing. Do not equate caspase8 inflammasome activity with apoptosis without reading the relevant experiment. Publisher full body is restricted. Existing IMP apoptosis should remain unresolved pending evidence, rather than being removed from its title.

PMID:1040062 resolves to *[Nurses replies to expectations of the nursing profession]*, an unrelated nursing article. GOA generic interaction partner Q15628 was independently verified as TRADD. PMID:10400625, *c-E10 is a caspase-recruiting domain-containing protein that interacts with components of death receptors signaling pathway and activates nuclear factor-kappaB*, has independently verified PubMed identity and an abstract explicitly describing TRADD co-precipitation (turn7060search0). Preserve original_reference_id1040062, record a formal reference replacement10400625, and use that paper under its own identifier as support. This correction follows content, not simply a guessed missing digit.

PMID:19593445, *Expression of the Bcl-2 protein BAD promotes prostate cancer growth*: full unique narrative Introduction, Methods, Results, figure captions and Discussion read as9a19eb; raw text search79ddfe found no BCL10, Bcl-10, mechanical or stress mentions. Experiments manipulate BAD in prostate cancer cells and mouse xenografts. This paper does not substantiate BCL10's mechanical-stimulus IEP; no intended replacement established. Flag the citation as MISCITED and the process as UNDECIDED rather than claiming the biological process is disproven.

PMID:23264731 has a MTR120-focused abstract and normally cached full text unavailable. PMC open returned a browser challenge. Cytoplasmic microtubule localization therefore requires target-specific evidence inspection; do not infer wrong-gene annotation from the title. Similar caution applies to CARD8-focused PMID11821383.

The IPI screen papers25416956,25910212,27107012,32296183,33961781,40205054 were read at abstract level. Preserve curated partner assertions as non-core when supported by the source record; do not claim supplementary pairs, constructs or isoforms were independently reproduced. PMID27071417 provides explicit BCL10/MALT1-dependent CARD14 signaling; CARD14-1 and CARD14-2 are partner isoforms, not BCL10 isoforms.

GO:0035591 current official definition and parentage verified at AmiGO (turn7061search0): signaling adaptor is a child of protein-macromolecule adaptor. Refine the existing broad adaptor assertion to this specific existing term; no NEW term is needed. GO:0038061 current definition explicitly requires NIK/IKKalpha/p100→p52 processing (turn7062view3), which is not interchangeable with general CBM-driven canonical signaling. GO:0071260 definition checked (turn7062view1). NF-kappaB-binding and apoptotic-signaling official opens failed in that batch; no substituted unofficial term definition used.

No new quotations have yet been committed for this gene. No full PAINT tree/node placement review has been performed; target in WITH/FROM is valid descendant evidence, not circularity. Existing GO-CAM65d7e4ac00000022 models BCL10 as adaptor, consistent with the central molecular role. No new process proposal is justified by absence alone.


## Retained cache comparison and focused consultation

The canonical source import is complete. All 58 PMID titles and 30 Reactome records agree with the draft's declared identities. Five publication availability flags differ from the archived candidates and were corrected to the retained normal caches: PMID21157432, PMID22528498, PMID23264731, PMID27071417 and PMID28628108. Full-text availability is not a claim that a complete paper was supplied or read: the retained 22528498 and 23264731 bodies contain Introduction and Discussion after the abstract. The BCL10-specific microtubule image/list in 23264731 remains uninspected.

The independent 13-assertion consultation was integrated without changing actions. It identifies actual BCL10 comparator experiments in the CARD8 paper, the ORFeome screen in the MTR120 paper, and the distinction between NF-kappaB binding to regulatory DNA and an unresolved BCL10/protein interaction. The original incorrectly indexed nursing citation remains preserved with its independently verified reference replacement. The BAD/prostate-cancer mechanical-stimulus mismatch remains MISCITED and the biological assertion UNDECIDED.

The 13-word PMID15125833 quote now preserves the canonical cache's literal space before its line break. No new quoted words or annotations were added. The remaining new primary citation PMID19897484 is awaiting the one normal recovery job; no canonical review application or final validation is claimed here.


## Independent whole-review correction

The high-throughput reporter qualification is now limited to the PMID12761501 assertion; it has been removed from six adjacent mechanistic or orthology rows. Actions and all original source objects are unchanged. PMID17287217 is added as source-only support for the membrane-raft core location: its complete normal abstract reports recruitment of the CD26/CARMA1/BCL10/IKK complex to lipid rafts after CD26 ligation. No new quote or annotation is introduced. Final PMID19897484 normal-cache integration remains pending.


## Normal PMID19897484 source reassessment

The authenticated normal source contains HTML-derived full text (PMCID PMC2804200; DOI 10.1074/jbc.M109.050815). The complete cached abstract, Introduction, Experimental Procedures, Results and Discussion were read; this does not include visual inspection of the figures or supplements. BCL10 siRNA reduced carrageenan-induced nuclear p52/RelB responses in human NCM460 cells and mouse embryonic fibroblasts. Reduced NIK phosphorylation supports an upstream requirement in that stimulus context and does not establish BCL10 as the phosphorylating enzyme. Row135 remains non-core, now with a formal supplemental reference and source link. No source object, action, core, product or supporting quotation changed. Canonical application remains conditional on exclusive import of the exact normal cache bytes.


## Final integration and validation, 2026-10-01 UTC

The exact normal PMID19897484 record is now imported and verified; the source-import condition above is closed. All 178 distinct source assertions from 180 raw GOA rows remain intact, including qualifiers and supporting entities. The complete review passes focused validation, rendering and history validation. Fifty-one advisories concern supported generic protein interactions retained as non-core under the supplied action definitions. One advisory concerns missing structured propagation metadata for an unresolved IBA; the donor/node evidence was not reconstructed and no failure cause is invented. The seven explicit UNDECIDED decisions remain visible. No new global validation pass or whole-paper coverage beyond the recorded reading scopes is claimed.
