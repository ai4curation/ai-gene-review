# RTT109 curation notes

## 2026-09-02 Update: added missing R-loop-suppression citation and proposed new term

While auditing the existing review, found that both the top-level `description`
and the `core_functions` entry for `GO:0010484` (histone H3 acetyltransferase
activity) already asserted that RTT109 "prevents DNA-RNA hybrid accumulation" /
contributes to "R-loop suppression" through H3K14/H3K23 acetylation, but no
reference anywhere in the file actually cited or quoted the paper establishing
this. The gene's own working file `RTT109-CURATION-REVIEW.md` (an untracked
scratch document in this folder) explicitly flagged this: "R-loop/DNA-RNA
hybrid prevention not explicitly annotated but supported (NEW annotation
should be added)" -- but that follow-up was never done in the actual
`RTT109-ai-review.yaml`.

Identified and fetched the source paper: PMID:35866610, Cañas et al. 2022,
Genetics, "A role for the Saccharomyces cerevisiae Rtt109 histone
acetyltransferase in R-loop homeostasis and associated genome instability"
[PMID:35866610 "Rtt109 prevents DNA-RNA hybridization by the acetylation of
histone H3 lysines 14 and 23"]. Full text now cached at
`publications/PMID_35866610.md` via `ai-gene-review fetch-pmid`.

Checked whether an existing GO term could be used for a direct `NEW`
`existing_annotations` entry (as done for e.g. ROF1's filamentous-growth
annotation). Searched QuickGO for "R-loop" and "DNA-RNA hybrid": the only
R-loop *process* term is `GO:0062176` (R-loop processing), whose definition is
explicitly R-loop *disassembly* -- the opposite direction from what RTT109
does (RTT109 loss increases R-loop levels; RTT109 activity prevents their
formation). No term for "negative regulation of R-loop formation" exists in
GO. Per project convention (never force a mismatched id onto a real finding),
recorded this as a `proposed_new_terms` entry instead, with `PMID:35866610` as
support and `GO:0006325` (chromatin organization, already used elsewhere in
this review) as a defensible `proposed_parent`.

Also added `PMID:35866610` to `references:` with a `reference_review` (HIGH
relevance, VERIFIED -- PubMed/PMC-verified, full text cached) and attached
`supported_by` provenance to the `GO:0010484` core-function block that was
making the previously-uncited claim.

No other issues found in this review during this audit pass. The bulk of the
70 `existing_annotations` entries (H3K56/K9/K27/K14/K23 acetyltransferase
activity, chromatin assembly, DNA damage response, etc.) are well-supported
by the cited literature and internally consistent.

## 2026-09-29 IBA propagation re-review and recent-literature check

Rechecked the three RTT109 IBA rows against the cached PAINT export for
PTHR31571. All three propagate from the same fungal RTT109 ancestor,
`PANTHER:PTN001586545`: `GO:0032931` is seeded by budding yeast RTT109, fission
yeast SPBC342.06c, and Candida CAL0000176178; `GO:0006974` is seeded by budding
and fission yeast; `GO:0005634` is seeded by budding yeast. The target appearing
among the descendant seeds is expected for PAINT and is positive support, not a
circular donor. The H3K56 acetyltransferase activity, nuclear localization, and
DNA damage response annotations are therefore all retained with
`NO_FAILURE_CORE`.

Updated the legacy generic `GO:0005515 protein binding` calls during the same
pass. The cited Vps75 and Asf1 interactions are real and mechanistically
important, but `protein binding` is not an informative molecular-function
annotation for the Rtt109 histone-chaperone acetyltransferase system. Those
rows now use `REMOVE`, while the catalytic and H3 histone acetyltransferase
complex rows continue to capture the relevant biology.

Searched PubMed and the web for 2023-2026 RTT109/Rtt109 papers in budding
yeast. Three new PMIDs were worth caching:

- PMID:37937370: full-text Mol Cell Biol study showing H4K16 deacetylation
  promotes Rtt109 recruitment and H3K56 acetylation at constitutively
  transcribed loci.
- PMID:38382924: abstract-only Genes Genet Syst study that places Rtt109 among
  histone acetyltransferase-related factors contributing to IMD2 right
  subtelomeric boundary regulation.
- PMID:39631395: full-text Mol Cell study showing the RCNA pathway, including
  RTT109 and H3K56 acetylation, is specifically required for efficient repair
  of leading-strand replication-dependent double-strand breaks.

These newer papers extend the transcription and replication-associated repair
contexts but do not require new GO actions beyond the existing accepted
chromatin organization, DNA damage response, and H3 acetyltransferase activity
annotations.

## 2026-10-01 current GOA refresh

Rebased the RTT109 review onto current GOA/UniProt with `just fetch-gene yeast RTT109
--force`; current GOA has 79 rows and the fetch seeded 15 new source assertions.
The additions were broad experimental `GO:0004402 histone acetyltransferase
activity` parents for the older Rtt109 HAT literature, one current RHEA/EC IEA
for the same broad activity, two generic Vps75 `GO:0005515 protein binding`
rows, two broad `GO:0061733 protein-lysine-acetyltransferase activity` rows, and
one Vps75-sourced `GO:0070775 H3 histone acetyltransferase complex` row. The
catalytic parents and complex row were accepted; the Vps75 protein-binding rows
were removed as generic duplicates of the specific Rtt109-Vps75 H3
acetyltransferase complex mechanism.

No PAINT topology changed in the refreshed PTHR31571 export: `GO:0005634`,
`GO:0032931`, and `GO:0006974` still all propagate from the fungal node
`PANTHER:PTN001586545`. The prior PTN-only `propagation_review` entries remain
valid; SGD RTT109 appearing among the node seeds is target-supported PAINT
evidence, not circular evidence.

Checked PubMed for 2025-2026 `Rtt109`/`RTT109`/`KAT11` hits. The direct budding
yeast replication-repair paper PMID:39631395 was already cached in the prior
pass; newer PubMed hits were either non-Saccharomyces, human EP300, model
systems that only mention yeast RTT109, or a 2026 bioRxiv Candida albicans
Rtt109 preprint, and did not require new RTT109 curation.
