# AUTS2 review journal

Started 2026-09-30 UTC. Earlier working notes below retain their historical scope; the final integration entry will record completed source imports and validation.

# AUTS2 preliminary primary reading

2026-09-29. Read-only preparation for the next project gene after AURKC.
No seed, fetch, recovery reservation, canonical edit or complete ownership
preflight has occurred. The canonical AUTS2 directory is absent locally.

[NCBI Gene 26053](https://www.ncbi.nlm.nih.gov/gene/26053/) identifies human
AUTS2 as HGNC:14262 / ENSG00000158321, with aliases MRD26 and FBRSL2.
[UniProt's reviewed entry](https://www.uniprot.org/uniprotkb/Q8WXX7/publications)
identifies Q8WXX7 / AUTS2_HUMAN and a 1,259-residue sequence. Exact alternative
products and construct mapping must come from the normal seed; the multiple
RefSeq isoforms cannot be mapped by numbering alone.

The existing immutable cache for
[PMID:25519132](https://pubmed.ncbi.nlm.nih.gov/25519132/) contains full text.
Read its complete abstract and selected visible Results/Methods passages; the
initial broad extraction was truncated, so this is not a complete-paper read.
The human 293 T-REx reporter and reconstitution experiments distinguish the
recruiting role of AUTS2 from the enzymes it recruits. PCGF5 bridges AUTS2 and
RING1B, whereas AUTS2 interacts with CK2 and P300. CK2 phosphorylates RING1B and
inhibits its H2A ubiquitination; P300 supplies acetyltransferase activity.
AUTS2-mediated transcriptional activation therefore does not establish an
intrinsic AUTS2 kinase, ubiquitin-ligase or acetyltransferase activity.
GAL4 tethering also does not establish autonomous sequence-specific DNA binding.
Mouse CNS perturbations are distinct from the human reporter measurements.
Figure pixels and supplemental tables have not been inspected.

[PMID:34637754](https://pubmed.ncbi.nlm.nih.gov/34637754/) is absent from the
normal cache. Its official abstract links AUTS2 HX-repeat variants to impaired
P300 interaction and identifies NRF1-mediated recruitment of ncPRC1.3 to
chromatin. The differentiation experiment described there uses mouse embryonic
stem cells. Full Methods, construct species and residue mapping remain unread.

[PMID:25533347](https://pubmed.ncbi.nlm.nih.gov/25533347/) is a second mechanistic
priority. The official abstract reports nuclear and cytoplasmic localization,
including growth cones, and Rac1/Cdc42-dependent cytoskeletal phenotypes.
This abstract does not establish AUTS2 as a catalytic guanine-nucleotide exchange
factor. Read the original Methods and interaction assays before choosing a
specific molecular-function refinement. No annotation decision is made here.

Next: establish current alias/PR ownership, perform the single normal gene seed,
then assess the machine-sourced annotations with an annotation-reviewer agent.

## Bounded continuation after independent identity check

Read the unique, nonduplicated Results paragraphs at cache lines 80, 82,
88–100 and selected Methods at 134, 140, 152, 154, 160, 166, 178, 190 and
196 of PMID:25519132. The broad preliminary text search duplicated long
sections and was truncated; the subsequent bounded display was complete.
The Methods explicitly identify a human AUTS2 cDNA for the tagged constructs.
The reconstitution host was Sf9; the cell-based reporter host was 293 T-REx.
Thus, human construct identity is established separately from host species.
PCGF5 is required for the tested RING1B–AUTS2 association, whereas the reported
AUTS2–CK2 and AUTS2–P300 interactions have recombinant assay support.
The tested AUTS2 404–913 fragment retained reporter activation and P300
recruitment. This fragment is not automatically a natural alternative product.
The kinase experiment assigns phosphorylation to CK2 and the ubiquitination
experiment assigns catalysis to RING1B; neither establishes AUTS2 catalysis.

The indexed original [PMID:34637754 Results and Figure 3 caption](https://pmc.ncbi.nlm.nih.gov/articles/PMC8604784/)
identify human AUTS2 variants
expressed in 293 T-REx cells and reciprocal P300 co-immunoprecipitation. HX-repeat
variants disrupted P300 association while retaining RING1B association.
This adds construct-specific evidence beyond the abstract, but the complete
Methods and exact isoform mapping remain unread. Direct PMC access returned
a browser challenge. The official record links an
[erratum, PMID:34798045](https://pubmed.ncbi.nlm.nih.gov/34798045/);
its correction text has not yet been inspected, so its scientific impact is
not inferred from the metadata.

The official search also identified
[PMID:30953002](https://pubmed.ncbi.nlm.nih.gov/30953002/), reporting different
PCGF3/PCGF5 interactions for long and short AUTS2 forms. This is a lead only:
the full abstract, constructs and Methods have not been read. It is a reason
to preserve product-specific uncertainty, not to map the paper's form names
onto unseeded UniProt isoform identifiers.

# AUTS2 primary reading continuation

The initial source seed is now imported, with 28 original GO objects and four
normal alternative products. The all-row consultation is complete. PMID34637754
remains staged pending separate cache eligibility; the other three additional
references are reserved in Source76 after a single failed normal batch.

Read all six normal source abstracts and bibliographic sections in c799ab.
Independent official PMID34637754 identity, full abstract, DOI and PMCID matched
in the [PubMed record](https://pubmed.ncbi.nlm.nih.gov/34637754/). The linked
[erratum](https://pubmed.ncbi.nlm.nih.gov/34798045/) is a separate publication.

Selected unique original PMID34637754 Results and Methods were read in 497776
and 137662. Human HX-repeat mutants in 293 T-REx cells lose P300 association
while retaining RING1B association. Reciprocal endogenous P300 co-IP supports
the specificity of that result. GAL4-tethered reporters demonstrate activation
without establishing autonomous sequence-specific DNA binding. The Methods
place the stable reporter in HEK293T 5XGal4 TK-Luc cells; the broader Results
description uses the 293 T-REx label, so retain this experimental distinction.

Mouse postnatal brain co-IP and chromatin measurements favor PCGF3-containing
assemblies in that tissue. NRF1 depletion in mouse-derived motor neurons
decreases AUTS2 occupancy, whereas NRF1 occupancy largely persists after AUTS2
loss. This is a targeting mechanism in the tested system, not proof of universal
NRF1 dependence in every tissue. The authors explicitly distinguish homozygous
mouse cellular perturbations from heterozygous human variants and note that
additional factors may recruit complexes in NRF1-poor brain regions.

The proposed core records P300 binding/recruitment and transcriptional
activation. It does not assign the enzymes' chemistry to AUTS2. Natural human
products retain their machine identifiers, including the missing ordinal 4;
the mouse long/short names and engineered constructs are not remapped by name.
No figure pixels, full supplement or complete-paper reading is claimed.

One prescribed provider invocation finished b87a32 with authentication/DNS
failure and no report. Existing gene files were unchanged. This manual note is
not labeled as provider-generated deep research.



## Integrated draft and source closure (2026-09-30T01:26:42.947124+00:00)

The normal seed preserves 28 annotation source objects and four natural products
(Q8WXX7-1, -2, -3 and -5). Independent annotation assessment and separate
core/reference assessment are complete. The draft has seven ACCEPT, twelve
KEEP_AS_NON_CORE, four MODIFY, four UNDECIDED and one MARK_AS_OVER_ANNOTATED.
There are no NEW assertions. Three experimentally supported generic complex
associations remain non-core; the four uninspected source-specific interactome
pairs remain undecided. The two P300 interaction rows are refined to histone
acetyltransferase binding, without assigning acetyltransferase catalysis to AUTS2.

The core describes P300 recruitment in nuclear noncanonical PRC1. The original
PRC1-family compaction experiments concern PRC1.4 and do not establish a general
heterochromatin-forming role for AUTS2-containing PCGF3/5 assemblies. Mouse
cytoplasmic localization, Rac signaling and neuronal phenotypes remain
contextual functions, not evidence that human AUTS2 catalyzes nucleotide exchange.

The staged PMID:34637754 record has now been imported byte-identically into the
normal publication cache. All five pre-existing publication records and both
family files were preserved. The separate six-reference recovery has been
dispatched once; AUTS2 references PMID:25533347, PMID:30953002 and correction
PMID:34798045 still await verified normal-cache recovery. Final reference
integration, canonical review application, focused validation and rendering
will follow that closure. The integrated candidate remains under tmp.

The required Falcon/perplexity-lite research command was attempted once and
failed after 5.68 seconds with authentication/DNS errors, producing no report.
The manual literature work above is the research record. No provider-labelled
research report was fabricated, and no source cache was hand-written.

History was scaffolded as
`history/genes/human/AUTS2/2026-09-30T011542Z-codex-e19374.yaml`; its validation
and final session details remain pending until the review is applied.


## Completed review integration (2026-09-30T02:02:17.636573+00:00)

Source76 normal caches PMID:25533347, PMID:30953002 and correction
PMID:34798045 are now imported and byte-verified. The correction is a
bibliographic erratum, with no cached abstract or body; it is not treated
as independent experimental support. The original primary article
PMID:34637754 remains a separate source. PMID:30953002 supports long/short
AUTS2 context in neuronal differentiation, including human transcript rescue
in mouse embryonic stem cells; it does not map the four natural human products
to independently demonstrated functions.

The reviewed draft is now canonical: 28 source annotations, four natural
products, one nonenzymatic nuclear recruitment core, and no NEW assertions.
Actions are 7 ACCEPT, 12 KEEP_AS_NON_CORE, 4 MODIFY, 4 UNDECIDED and
1 MARK_AS_OVER_ANNOTATED. All original annotation source objects and product
records are preserved. The four unresolved high-throughput interactions remain
UNDECIDED. All selected source excerpts match the normal caches, with at most
24 quoted words per source across the YAML. Focused validation, rendering and
history validation follow this application.

Focused schema, ontology-term and best-practice validation passed; rendering
also passed. Three advisories flag generic interactions retained as non-core
under the curation action definitions. They are not evidence that those
interactions are false. All four uninspected interactome pairs remain
UNDECIDED. The scaffolded history records these results.


## First review follow-up — 2026-09-30

The independent biological consultation confirms that the core should explicitly
include a contribution to transcription coactivator activity (GO:0003713),
alongside direct histone acetyltransferase binding (GO:0035035). Human AUTS2
GAL4 reporter experiments establish active P300 recruitment and dependence on
P300 and PRC1 components. Mouse NRF1 co-association and chromatin-occupancy
experiments supply the native targeting mechanism in the studied neural
contexts. The description distinguishes these systems and assigns the enzymatic
steps to P300 and CK2. It does not assert autonomous DNA recognition or a direct
human neuronal NRF1 experiment.

Selected complete Results/Methods paragraphs in PMID:25519132 and
PMID:34637754 were independently rechecked; whole papers and supplements were
not newly read. The broad cytoskeletal location is retained as non-core and
positive transcription regulation as core, without duplicating narrower terms
already represented in the source annotations. Counts are now eight ACCEPT,
13 KEEP_AS_NON_CORE, two MODIFY, four UNDECIDED and one MARK_AS_OVER_ANNOTATED.
All 28 original source objects and four products remain unchanged, with no NEW
assertion. Supported generic interactions are preserved under the user action
definitions; the review's blanket-removal policy objection remains unresolved.


## 2026-10-01 UTC — Binding-policy clarification

The [review of PR #3569](https://github.com/ai4curation/ai-gene-review/pull/3569) at `04712c385` correctly distinguishes exclusion of an uninformative term from rejection of a reported interaction. The repository default can exclude GO:0005515 even when the interaction is real. The earlier notes should not be read as claiming that the default requires biological falsity or that a touched annotation falls within a legacy exception.

For this task, the explicit instruction is not to remove generic binding solely for informativeness and to preserve UNDECIDED when the relevant experiment cannot be adjudicated. The existing decisions are a scoped application of those instructions. This is a documented departure from the default binding policy, not a global policy change or a claim that its advisory warnings have disappeared.

The three retained rows distinguish PCGF5 association, PCGF5-dependent RNF2 association, and the RNF2 association retained by the tested human variants. They do not assign purified autonomous AUTS2–RNF2 binding or ubiquitin-ligase catalysis to AUTS2. PRC1 membership and the qualified transcription-coactivator contribution remain represented separately from the source-specific interactions. The P300-specific refinements are preserved; their mechanism is not transferred indiscriminately to the RNF2 rows. Four unadjudicated interaction rows remain UNDECIDED.

This addendum adds no primary-source reading, assay verification or quotation. All existing actions, source assertions, products, reference findings and core claims remain unchanged.
