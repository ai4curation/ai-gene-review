# AICDA review notes

## 2026-09-27 substantive review

The approved human symbol is **AICDA** (HGNC:13203; UniProt Q9GZX7); aliases are HIGM2, CDA2, ARP2 and AID. The authoritative HGNC snapshot has no previous symbol. Source3 supplied the normal, machine-generated seed. All three seed-file hashes matched `/tmp/AICDA-root-baseline.json`. A read-only GitHub query at main `509f4a01609d48870601d32f0ad7ae8a64e80cf7` found no canonical or alias directory, no open title-matching PR for any of the five names, and no matching AICDA branch. The original source3 import base remains `ba3ff58d7d2de76dbe3c24b16e05e12369f463fc` for publication of new files. Root owns publication and project tracking.

All 47 seeded annotations, qualifiers, supporting entities, 22 original reference identities and two alternative products are preserved. This review adds six primary references, one integrated catalytic core and no NEW annotations. The 47 decisions are 24 ACCEPT, 14 REMOVE of uninformative generic protein binding, four KEEP_AS_NON_CORE, two UNDECIDED, two MODIFY and one MARK_AS_OVER_ANNOTATED. Broad nuclear/cytoplasmic assertions are retained where independent positive target evidence supports them; experimental absence is not inferred from an abstract or a protein's predominant compartment.

### Research execution and availability

The required genuine Falcon attempt used `just deep-research-falcon human AICDA --fallback perplexity-lite --timeout 1200` with writable task-specific UV tool/cache paths. Falcon and fallback both failed while resolving the deep-research-client dependency from PyPI (DNS), before provider contact. The wrapper exited 1; neither provider created a report. `/tmp/AICDA-provider.log` preserves the actual errors. These notes are manual curation, not provider output.

The normal GOA publication-cache command completed with 16/16 records already cached (`/tmp/AICDA-fetch-goa.log`). A normal request for six additional primary sources completed with 0/6 recovered and DNS failures (`/tmp/AICDA-fetch-new-primary.log`). No publication, UniProt, GOA, InterPro or provider file was manually rewritten. The six required cache gates are PMID:10373455, PMID:12651944, PMID:25957684, PMID:28757211, PMID:19188259 and PMID:23341589. They are reserved for a future recovery batch; frozen source9 is unchanged. No other cited source gap or provider-only source exists in this gene directory.

Local `full_text_unavailable` flags follow the machine cache metadata. External primary reading is recorded separately. In particular, PMID:19734146 and PMID:21496894 have locally abstract-only records despite external Results access. PMID:21722948 contains full-text sections with a true metadata flag, but its local extraction omits Results; indexed original Figure 6 supplied the missing interaction context. Neither a flag nor a title is treated as proof that every assay was inspected.

### Substrate chemistry and the central function

The core is zinc-dependent deamination of cytosine in exposed single-stranded DNA, creating uracil lesions that initiate antibody hypermutation and class switching. AID performs the deamination; repair enzymes perform subsequent excision and recombination. Human immunodeficiency and biochemical evidence are complementary, rather than interpreting knockout necessity alone as a process mechanism [PMID:11007475; PMID:18722174; PMID:12651944].

The live [GO:0004126 record](https://amigo.geneontology.org/amigo/term/GO%3A0004126) formally describes free cytidine/deoxycytidine conversion (EC 3.5.4.5). This is not identical to DNA-cytosine deamination (EC 3.5.4.38, RHEA:50948 in the immutable UniProt record). Nevertheless, free-substrate activity must not be rejected: the original mouse study measures GST-AID activity [PMID:10373455], and the human Ramos-derived preparation in [PMID:12651944](https://pmc.ncbi.nlm.nih.gov/articles/PMC153055/) directly measures both free nucleosides in Figure 4b. Its Methods specify Ramos cDNA, GST fusion and Sf9 expression. It also measures DNA deamination and inhibitory RNA association. One exact Results excerpt is: “AID is most active when deaminating the free deoxynucleoside, CdR → deoxyuridine”. This is an assay comparison, not a physiological flux claim.

Accordingly, the four existing cytidine-deaminase assertions are retained. The core uses verified [GO:0019239 deaminase activity](https://amigo.geneontology.org/amigo/term/GO%3A0019239), with the DNA substrate specified in prose, and the two very broad hydrolase assertions are refined to it. No DNA-specific MF identifier was invented. The remaining ontology question distinguishes the known chemistry from the absence of an adequately specific term found in this search. [PMID:28757211](https://pmc.ncbi.nlm.nih.gov/articles/PMC5771415/) and the [author PDF](https://wulab.tch.harvard.edu/_files/ugd/feeaaa_f8d5b1054d45494f9494cfd5c7918e44.pdf) support engineered human AID recognition of structured DNA, catalytic zinc and substrate-dependent oligomerization. Bound cytidine derivatives in a structure are not used as a turnover assay, nor is an obligatory native homodimer claimed.

### RNA and viral contexts

RNA binding is independently positive: the human biochemical preparation binds inhibitory RNA, and mouse switch-RNA experiments provide a targeting mechanism [PMID:12651944; [PMID:25957684](https://pmc.ncbi.nlm.nih.gov/articles/PMC4426339/)]. Mouse experiments are not relabeled as direct human experiments, and RNA binding alone is not RNA editing.

The [original HBV paper, PMID:23341589](https://pmc.ncbi.nlm.nih.gov/articles/PMC3568302/) reports C-to-U changes in nucleocapsid RNA, with RNase-H-defective polymerase, lamivudine and core immunoprecipitation controls. Human and mouse AID-ER are explicitly compared in separate DNA-hypermutation experiments; endogenous human BL2 AID also reduces viral nucleocapsid DNA. The first Results section explicitly introduces the unfused construct as human AID; subsequent RNA panels continue that AID/GFP comparison without identifying a species change. This resolves the earlier construct-scope concern sufficiently to retain the IBA as non-core with positive human experimental corroboration. The ancestral IBD chain remains uninspected. This is distinct from proving an endogenous immunoglobulin RNA-editing mechanism. Root independently highlighted the first Results sentence, which was then re-read alongside the RNA panels.

Broad antiviral defense is retained as non-core using the endogenous human BL2 result and the AID/UNG-dependent HBV cccDNA study [PMID:23341589; PMID:26867650]. The [GO:0045869 definition](https://amigo.geneontology.org/amigo/term/GO%3A0045869) specifically concerns single-stranded viral RNA replication through DNA. HBV is a DNA virus. The [full PMID:19188259 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC2665220/) explicitly tests human AID among eight vertebrate proteins and supports L1/MusD retrotransposition restriction; this does not automatically establish infectious retroviral restriction. The specific IBA remains UNDECIDED pending its IBD evidence and a properly matched assay.

### Localization, partners and process scope

Human AID-GFP shuttling was measured in a mouse NIH3T3 host [PMID:14769937]; human patient and engineered Ramos cells independently confirm a nuclear pool [PMID:32484799]. PMID:21385873 contains AID experiments despite its spliceosomal title: human-cell localization/interaction work and a separate chicken DT40 CTNNBL1-loss assay. The P-body IBA remains unresolved; cytoplasmic signal does not establish a specific granule, and failure to recover that experiment does not establish an erroneous annotation.

The 14 generic binding assertions retain their source records but are removed as functionally uninformative. Reported interactions are not denied. AID is a PKA substrate, karyopherin cargo and chaperone client; those relationships do not make it a kinase, transport receptor or chaperone [PMID:16387847; PMID:19412186; PMID:21385873; PMID:22085931]. Specific RNF126 ligase binding is retained as contextual regulation of AID [PMID:23277564]. The AID–RNA-exosome association is real in human Ramos/transfection experiments, but the paper explicitly leaves direct versus indirect interaction open [PMID:21255825]. Broad protein-complex membership is retained without claiming AID is a constitutive exoribonuclease subunit.

The [full SLIP-GC study, PMID:19734146](https://pmc.ncbi.nlm.nih.gov/articles/PMC2781619/), assigns replication-factory localization to SLIP-GC. AID knockdown rescues DNA damage/apoptosis after SLIP-GC depletion. The full Results do not demonstrate a defined AID replication-regulatory step; the [GO:0033262 definition](https://amigo.geneontology.org/amigo/term/GO%3A0033262) concerns alteration of nuclear cell-cycle replication. The existing process assertion is marked over-annotated, while preserving the actual positive AID-dependent damage finding.

The demethylation annotation remains non-core. [PMID:21496894](https://pmc.ncbi.nlm.nih.gov/articles/PMC3088758/) uses human ORF constructs in HEK293 cells and demonstrates AID-dependent changes to hydroxymethylated reporters. Its endogenous adult mouse brain loss-of-function data center on Tet1/Apobec1; ectopic AID results are separate. The paper does not establish direct purified AID removal of a methyl group and explicitly allows other intermediates. [PMID:21722948](https://pmc.ncbi.nlm.nih.gov/articles/PMC3230223/) Figure 6 supports AID/TDG/GADD45A associations across tagged human-cell, mouse P19 and purified-protein assays; TDG performs the measured glycosylase reaction. The precise physiological human targeting and reacting intermediate remain questions. Aars1 independently inspected these two sources and verified the human-ORF versus mouse-brain distinction.

### Propagation and annotation completeness

Every IBA is traced to its actual PTN ancestral node, not the extant member list. Full PAINT IBD/tree evidence was not recovered. Independent positive target evidence supports some annotations despite this provenance limit; uncertain node-specific claims remain UNDECIDED. Target-in-WITH is legitimate descendant evidence and is not called circular. ARBA predicates and the Ensembl donor record remain explicitly uninspected, while the mouse Aicda enzymology is grounded in the original experiment. InterPro signatures support the deaminase fold, but their LLM-generated unchecked descriptions are not used as scientific evidence.

The cached GO-CAM index contains no AICDA/Q9GZX7 entry. No process NEW is proposed: antibody diversification and DNA deamination are already seeded, and class switching is within the existing diversification coverage. The review does not manufacture a redundant descendant merely to populate the core. The core has one catalytic function; oligomerization and recruitment are supporting mechanisms, not extra redundant function blocks.

### Verification checkpoint

The authored draft preserves all original source objects and alternative products by parsed equality, and original reference IDs/titles by ordered equality. UniProt and GOA remain byte-identical to source3. Cached supporting snippets are checked case-sensitively after whitespace normalization. Schema, ontology, references, strict GOA coverage, best practices, history and HTML rendering are checked before the final manifest. Status is DRAFT while the six genuine publication-cache gates remain. No remote action is part of this authored handoff.

Root independently reviewed all 47 decisions, 28 reference assessments, the integrated core and questions, and inspected the human free-nucleoside and HBV RNA primary experiments. The resolved human-vector evidence supports contextual RNA editing. No further biological change was requested. The final exact checks and immutable-byte receipts are recorded in `/tmp/AICDA-local-manifest.json`.

## 2026-09-27 PR #3290 evidence and ontology follow-up

Read the complete comment 5854585122 and formal review 5329725143. All five
canonical files matched published head `ac32f2e1c60c33487462716d84391df22e2ea74b`
before edits. The six source10 requests were fixed and pending at the initial
follow-up checkpoint; their subsequent verified import is recorded below.
No unchanged local retry was performed. Status remains DRAFT.

Live primary AmiGO records establish that GO:0019239 and GO:0016814 are siblings
under GO:0016810, and both parent GO:0004126. The two broad InterPro rows remain
MODIFY but now propose GO:0004126, using the measured free-nucleoside capacity.
The existing four cytidine-deaminase assertions remain unchanged. The review's
count of five was not reproduced. These are refinements of existing assertions,
not NEW rows; the NEW ancestor/descendant prohibition does not require deleting
valid source assertions. The previous sibling-to-sibling specificity explanation
was incorrect and is replaced.

The core deliberately retains GO:0019239 with explicit ssDNA chemistry. The
formal GO:0004126 reaction is free cytidine/deoxycytidine, so substituting it in
the DNA-substrate core would introduce a different substrate scope. The existing
GO:0070383 process already makes DNA cytosine deamination machine-readable.
Primary GO/EBI searches did not establish an appropriate DNA-specific MF; the
QuickGO API search was inaccessible. This is a bounded search result, not proof
that no term can exist. The ontology question now names the existing BP coverage.

The original PMID:12651944 Results were recovered again through indexed
[PMC153055](https://pmc.ncbi.nlm.nih.gov/articles/PMC153055/). Its free-deoxycytidine
assay is quoted briefly in the six relevant annotation reasons with the public
URL and external access scope. The normal abstract cache supplies an exact
ordinary supporting snippet. Public browser text is not placed in
`supporting_text_fulltext`, which is reserved for non-shareable full text. The
same correction places the PMID:23341589 human-vector excerpt in its reason
and attaches the cached abstract's positive HBV RNA-editing result.
VERIFIED records independently checked primary identity and relevant content;
local full-text availability is assessed separately.

Three contextual assertions change from ACCEPT to KEEP_AS_NON_CORE:

- B-cell differentiation retains positive terminal antibody-diversification
  context. AID performs Ig-DNA deamination, but the broad developmental category
  is not an additional core function. Giant germinal centers do not show that
  every stage of B-cell differentiation is normal.
- Protein-containing complex retains the actual PMID:21255825 multistep
  purification (DNA affinity, size chromatography and affinity purification),
  RNA-exosome association and functional stimulation. Live GO:0032991 requires
  more than a simple co-IP; this source supplies additional purification and
  functional evidence. Indirect contact does not itself disprove assembly
  membership. Neither a fixed stoichiometry nor a constitutive RNA-exosome
  core-subunit assignment is asserted.
- Identical-protein binding retains independent positive human AID evidence in
  [PMID:28757211](https://pmc.ncbi.nlm.nih.gov/articles/PMC5771415/). Original
  Results and Methods distinguish engineered soluble proteins, G4-dependent
  oligomers, and full-length untagged internal mutants assayed in mouse splenic
  B cells. An exact positive oligomerization quote is attached. The original
  PMID:19412186 panel remains unrecovered, and no obligatory native homodimer is
  inferred. Independent positive evidence supports retention rather than an
  absence-based removal.

The KPNA1 row now quotes its own karyopherin-specific Figure 5 binding result;
the PMID:21518874 hypermutation row now attaches its BL2 reporter mutation
result. Both are exact cached snippets and both actions are unchanged. Repeated
reference-review prose is shortened while retaining the full source-specific
findings and access limits. No source fields, qualifiers, isoforms, reference
identities or core objects are changed; no NEW annotation is proposed. Final
counts are 21 ACCEPT, seven KEEP_AS_NON_CORE, 14 REMOVE, two MODIFY, two
UNDECIDED and one MARK_AS_OVER_ANNOTATED.

### Verified source10 recovery and final access scope

All six required records were imported by the parent from the pinned normal
fetch artifact, without alteration or overwrite. Each canonical byte sequence
was independently compared with the staged file and import receipt
`tmp/source10-canonical-import-receipt.json` (SHA256
`18d517caec871b4306b21283bb89204639ecc0b25f6f495802bd664d072c8359`).

PMID:10373455, PMID:12651944 and PMID:23341589 are abstract-only local records.
PMID:19188259, PMID:25957684 and PMID:28757211 contain substantial extracted
main text. Their Methods/Results were read; repeated XML-derived sections and
supplement labels are not treated as proof of complete supplementary coverage.
The mouse discovery/biochemistry in PMID:10373455 and mouse switch-RNA assays
in PMID:25957684 remain distinct from human AID experiments. The latter record's
machine title capitalization is now reproduced exactly. The retrotransposition
paper identifies human AID among eight vertebrate constructs and does not by
itself establish infectious-retrovirus restriction. The structured-DNA paper's
engineered biochemical constructs remain distinct from untagged full-length
internal mutants used for mouse B-cell rescue.

The cache census covers all authored YAML/notes references and links: 22 PMIDs,
all present, with no provider artifact, unresolved DOI-only citation or Reactome
gate. No annotation action changes were needed for the recovered evidence.
All 47 immutable source assertions, two alternative products and the integrated
core are preserved. Status remains DRAFT because the deliberately generic
GO:0019239 core has a validator coverage advisory after the two broad rows are
refined to free-cytidine activity. A redundant NEW annotation is not introduced
solely to suppress that advisory. The final validation and exact-file manifest
record the remaining advisory separately from the now-closed source gates.
