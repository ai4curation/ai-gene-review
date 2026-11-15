# Human ACO2 review notes

## 2026-11-15 — initial evidence review

Native intake: human ACO2, HGNC:118, UniProt Q99798, NCBITaxon:9606.
`just fetch-gene human ACO2` produced 26 GOA rows and 26 annotation contexts.
Their terms, references, evidence codes, qualifiers, and supporting entities are
preserved. No alternative-product identifiers were supplied by the native seed.
The older report of multiple electrophoretic protein forms is not used to invent
splice-product identifiers.

Falcon deep research failed authentication; its perplexity-lite fallback failed
for insufficient quota. Neither produced a research report. These notes document
manual primary-source research, with independent annotation and core-function
consultation. The review remains DRAFT because seven native source contexts are
unresolved: 18 ACCEPT, seven UNDECIDED, one TOO_GENERAL, plus one NEW nucleus CC.

### Catalytic mechanism and mitochondrial function

The core activity is reversible citrate/isocitrate interconversion through
cis-aconitate, GO:0003994, in the mitochondrial matrix, GO:0005759, as part of the
TCA cycle, GO:0006099. The native UniProt record specifies one catalytic
[4Fe-4S] cluster per subunit. Its catalytic/cofactor evidence is transferred from
bovine P20004, and its matrix location from mouse Q99KI0; these are not relabeled
as direct human assays. The human Reactome reaction corroborates the chemistry
and modeled matrix compartment. [UniProt Q99798](https://www.uniprot.org/uniprotkb/Q99798/entry),
[Reactome R-HSA-70971](https://reactome.org/content/detail/R-HSA-70971).

PMID:22405087 measured cis-aconitate consumption in patient lymphoblasts and
tested human ACO2 in yeast complementation. This supports catalytic impairment,
but yeast growth requiring the glyoxylate shunt does not establish that pathway
in humans. The article's background wording suggesting four separate clusters
and an 805-residue product is not propagated onto the current 780-residue Q99798
record. [Primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3309186/).

PMID:41763199 provides a physiological refinement: ACO2-deficient human A549 and
Calu1 cells accumulated excess citrate and acquired growth defects when pyruvate
increased citrate production. Baseline proliferation was not uniformly
ACO2-dependent. Citrate clearance is therefore described with its metabolic
context; the conditional mouse kidney phenotype is not presented as a human
experiment. Knockout-induced stress does not justify a new stress-signaling
annotation. [Primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC13045649/).

Iron binding remains informative alongside [4Fe-4S] cluster binding. Likewise,
mitochondrion is retained alongside mitochondrial matrix under the repository's
root-organelle rule. GO:0006091 is TOO_GENERAL because its broad energy-metabolism
meaning is imprecise alone and the accepted TCA term supplies the specific
process. QuickGO ancestry confirms the relevant is_a/part_of relationship.

### Nuclear evidence and the unresolved cytosolic IBA

PMID:42386731 supports a NEW nucleus annotation in the demonstrated human
MDA-MB-468 context. Human evidence includes imaging-flow localization in
Fig. 1b,c, nuclear fractionation in Fig. 2b, and nuclear immunoprecipitation in
Fig. 2f. Fig. 4e measures labeled citrate formation in isolated human nuclei
after ACO2 or IDH2 depletion. In contrast, Fig. 1e,f,h microscopy and Fig. 2h
KPNA2 perturbation use mouse GL261. These species distinctions are retained.

ACO2 performs isomerization; IDH2 performs reductive carboxylation, and KAT2A
performs acetyl transfer. ACO2 is not assigned either partner's activity. Keep
the primary core unit in the matrix: the nuclear experiment supports local
citrate metabolism, not a complete nuclear TCA cycle or universal nuclear
localization. [Primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC13462710/).

QuickGO verifies GO:0005634 nucleus and no is_a/part_of redundancy with the
existing ACO2 CC terms. No Q99798 entry was found in the inspected GO-CAM index.
No NEW process term is proposed. The cytosolic IBA is separate: nuclear evidence
does not resolve human cytosolic ACO2, and a mitochondrial import precursor is
not evidence of an active cytosolic enzyme pool.

PTHR43160 native members place Q99798 in mitochondrial SF3. PAINT assigns
activity/cluster/TCA at PTN000186533 and mitochondrial location at PTN000186534.
Q99798 appearing among descendant evidence for TCA is expected, not circular.
The cytosolic PTN001705783 node, seeded by yeast ACO1 and bacterial AcnB, remains
unresolved for human ACO2 because the complete gain boundary was not recovered.
Its short donor list is not itself a reason to reject the IBA. Family curation
is outside this PR; another active PR owns that family review. Human ACO1/IRP1,
budding-yeast ACO2, and fission-yeast Aco2 are not interchangeable with human ACO2.

### Original-source access limits

PMID:9630632 is abstract-only. It directly identifies an iron-dependent
mitochondrial enzyme, supporting the TAS iron-binding and mitochondrial rows.
The IDA iron-binding/TCA/citrate assays and the citrate-metabolism TAS statement
cannot be checked from this abstract; those four contexts remain UNDECIDED.
An inaccessible full text is not evidence that the original curator was wrong.
[PubMed record](https://pubmed.ncbi.nlm.nih.gov/9630632/).

PMID:20833797's retained cache contains Abstract and Discussion despite its
`full_text_available: true` flag. The ACO2-specific phosphoproteomic result is
not exposed. PMID:34800366's article body is available, but the ACO2-specific
Table S1 row was not recovered. Both experimental localization contexts remain
UNDECIDED; neither missing prose mention nor a failed supplement fetch is used
as evidence against mitochondria. [PMID:20833797](https://pubmed.ncbi.nlm.nih.gov/20833797/),
[PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/).

PMID:1946331 and PMID:25351951 are abstract-only corroboration of purified human
protein and functional impairment, respectively. The reported secondary ACO1
activity defect in patient fibroblasts is not a cytosolic ACO2 localization assay.
PMID:25944712 is an N-terminomics lead; no ACO2-specific peptide was verified in
the accessible abstract, so no cleavage-coordinate assertion is made.

Reactome matrix rows are retained as curated reaction contexts. Some CLPXP
summaries are generic, whereas LONP1 explicitly names oxidized ACO2. ACO2 being
a protease substrate, an oxidation target, or a recipient of frataxin-supplied
iron does not assign it proteolysis, antioxidant catalysis, or Fe–S assembly.

### Source preservation and validation

The native PMID fetch shortened the existing PMID:20833797 cache and removed
discussion text supporting an unrelated gene's quotation. The exact richer
committed cache was restored before curation. Metadata-only refreshes of
PMID:34800366 and PTHR43160 entries/metadata were also restored, preserving the
existing source context and avoiding unrelated family changes. Retained hashes
and source-impact findings are recorded in the campaign's compact audit receipts.
All newly fetched ACO2-specific sources remain native downloader output.

The completed review passes schema, ontology-term, best-practice, and history
validation. Three warnings flag differing ACCEPT/UNDECIDED actions for shared
iron-binding, mitochondrion, and TCA terms; the differences deliberately retain
original-source uncertainty rather than contradict the biological functions.
The literature validator checked 16 snippets and eight titles without issues;
its 39 skipped database snippets were not counted as literature-verified.
The canonical all-quote check separately verified all 79 supporting-text
occurrences against retained sources, with zero unchecked or failing quotes.
Canonical HTML rendering succeeded in memory. Native GOA/UniProt bytes and all
26 native annotation identities remained unchanged. No local environment or
lockfile was created or modified by the guarded checks.
