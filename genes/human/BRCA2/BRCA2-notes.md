# BRCA2 (P51587) notes

## 2026-07-22 — QA re-review (no changes to YAML)

Performed a quality-assurance pass over `BRCA2-ai-review.yaml` (~151 annotations).
The file was already the product of a careful A→Z manual review. Conclusion: it is
in good shape and **no edits were warranted** under a conservative bar (only change
what is a confident improvement).

Checks performed and results:

- **Structural validation** (`uv run ai-gene-review validate`): ✓ Valid, no warnings.
- **Supporting-text verbatim check** (`linkml-reference-validator validate data`): all
  PMID-quoted `supporting_text` values pass as verbatim substrings of the cached
  publications. The only reported errors were "Could not fetch reference" for Reactome
  and `file:` references — these are offline-fetch failures in this environment, not
  quote mismatches.
- **Action consistency across evidence types**: consistent. GO:0000724 (HR repair) is
  ACCEPT across IBA/IEA/IDA/IMP; GO:0005515 (protein binding) is uniformly REMOVE;
  GO:0005654 (nucleoplasm) uniformly ACCEPT; GO:0005813 (centrosome) and GO:0070200
  uniformly KEEP_AS_NON_CORE; GO:0010484/GO:0010485 (HAT) both UNDECIDED. No same-term
  action conflicts.
- **"protein binding" guideline**: no GO:0005515 annotation is marked ACCEPT — all are
  REMOVE (with the specific interactor recorded in the summary). REMOVE is an
  established repo-wide action for this uninformative term, so these were left as-is
  rather than flipped wholesale.
- **core_functions branch placement** (strictly validated): correct. `molecular_function`
  = GO:0003697 (MF); `directly_involved_in` = GO:0000724/0000730/0042148/0031297/1990426
  (all BP); `locations` = GO:0005634/0005654 (CC); `in_complex` = GO:1990391 (CC/complex).
- **Core function capture**: RAD51 loading / presynaptic filament (ssDNA binding + HR +
  DNA recombinase assembly + DNA strand invasion) and stalled-fork protection are both
  captured as core; D-loop formation is represented via the GO:0042148 NEW term. Not
  over-generalized.
- **Description field**: clean standalone biology, no project/workflow framing.

Issues considered but deliberately left alone (all guideline-compliant as written):

- **HAT activity tension**: the positive H3/H4 HAT IDAs (GO:0010484/GO:0010485,
  PMID:9619837) are UNDECIDED while the negated GO:0004402 (NOT HAT, PMID:9824164) is
  ACCEPT. Mild internal tension, but UNDECIDED is the correct conservative choice for a
  contested experimental IDA, and REMOVE of an experimental annotation is disallowed.
- **GO:0006289 nucleotide-excision repair** (IMP, PMID:16845393) sits on an
  interstrand-cross-link-repair paper; KEEP_AS_NON_CORE with an honest caveat is a
  defensible conservative call (a MODIFY to GO:0036297 would be reinterpreting a GOA
  term id, out of scope for QA).
- **GO:0030141 secretory granule** (IDA, PMID:8589722, a BRCA1-titled paper) is
  UNDECIDED with a hedged "possible annotation error" note — compliant because the
  cached abstract explicitly foregrounds BRCA1, and the reviewer used UNDECIDED (not
  REMOVE) per the guideline for experimental annotations whose full text is unseen.


## 2026-10-03 — BRCA2 completed annotation audit

The annotation audit is complete: every machine-seeded annotation has a reviewed decision. Thirty-four decisions remain UNDECIDED because the available sources do not resolve the specific assertion. The schema status is DRAFT because 38 supported generic-binding rows produce validation policy warnings; there are no PENDING decisions. The full normal validation passed. Existing notes are preserved above, and provider outputs, publication/Reactome caches and prior consultation reports were preserved. ROOT retains responsibility for canonical application and fresh ownership/source reconciliation before publication.

All 149 machine-seeded annotations were reviewed; their complete non-review field projections, including the negated HAT assertion, are unchanged. The row ledger accounts for all 163 raw GOA observations and preserves every WITH/FROM partner in the evidence join. The two older NEW rows are author proposals and were assessed separately. No new quotations were added. The 92-reference collection was retained, with all 61 PMID titles matching the protected caches.

The review has 49 ACCEPT, 65 KEEP_AS_NON_CORE, 34 UNDECIDED and one MODIFY. Of 48 generic binding rows, 38 retain supported interactions as non-core, nine remain unresolved because the target assay or primary provenance is unavailable, and one is refined to an experimentally supported activity. This applies the explicit ClinGen campaign policy; the repository's generic-binding validator therefore produces 38 expected policy warnings.

The primary activity is GO:0140619 DNA strand exchange activator activity. Purified full-length human BRCA2 binds RAD51 and stimulates its strand-exchange reaction by promoting productive RAD51 assembly on ssDNA, including overcoming RPA occupancy. RAD51 performs strand exchange; BRCA2 is its mediator/activator. The actual Results distinguish BRCA2 alone from the RAD51 reaction. Generic row 22, PMID:20729832, is MODIFY to this specific MF; DMC1 binding in the same paper is not converted into an unsupported DMC1 activation claim. Direct DNA/ssDNA-binding annotations remain accepted. PMID:20729859 and PMID:36976771 independently support RAD51 loading/nucleation. The current QuickGO response obtained by ROOT confirms the term's name, MF aspect and non-obsolete status; the existing molecular-activity enum contains it. GO:0120230 recombinase activator activity was considered, but GO:0140619 specifically describes the assayed strand-exchange activation.

One narrow activity core replaces the previous two ssDNA-binding cores. BRCA2-dependent protection of reversed replication forks remains prominent in the description and the process reviews. PMID:29038466 distinguishes this protection from fork reversal itself. A second MF was not invented to explain protection, and strand-exchange stimulation is not assumed to be the chemistry of fork protection. GO:1990391 DNA repair complex remains a broad, supported complex description for the PALB2-linked BRCA1-BRCA2 assembly; no narrower complex identifier was guessed (PMID:19369211).

The BRCC paper explicitly includes BRCA2 in an isolated complex but reconstructs an E3 complex from BRCA1, BARD1, BRCC45 and BRCC36, without BRCA2. Row 94 is therefore retained as non-core complex membership, with no intrinsic BRCA2 ligase inference. The same abstract does not expose a BRCA2-specific perturbation behind its radiation/checkpoint observations, so rows 96 and 97 are unresolved (PMID:14636569). USP11 complex association remains supported, while the former claim that USP11 physiologically controls BRCA2 stability is removed; the paper distinguishes its survival role from BRCA2 deubiquitination (PMID:15314155). MAGE-D1 stabilization and mammary-cell growth suppression remain supported context-specific observations without attributing an enzyme activity to BRCA2 (PMID:15930293).

The HAT conflict is preserved explicitly. PMID:9619837 claims intrinsic H3/H4 acetylation by BRCA2 amino-terminal material, whereas PMID:9824164 reports no intrinsic HAT activity and associates the observed activity with P/CAF. Both are abstract-only caches. Positive rows 72/73 remain UNDECIDED, negative row 86 remains ACCEPT with negated:true, and the GO:0010484-derived chromatin-remodeling inference remains UNDECIDED. Complete purification/control experiments were not reassessed.

Several source limitations materially change the older decisions. PMID:9126734 contains metadata under an Abstract heading but no scientific abstract, so its transcriptional activation assay is unresolved. PMID:8589722 explicitly mentions a BRCA2 granin-like motif, but the abstract does not expose a BRCA2 secretory-granule localization assay; the older suggestion of a wrong-gene error is removed. PMID:16845393 explicitly supports BRCA2-dependent repair of replication-associated DSBs but discusses nucleotide excision separately, so its NER row is unresolved while DSBR remains accepted. PMID:21601571 supports BRCA2-RAD51 binding but not an accessible self-binding assay; a distinct self-association row is supported by the actual dimer Results in PMID:25282148. The precise gamma-tubulin binding assay is unavailable in PMID:17286961, although its nuclear/centrosome localization and centrosome-duplication observations are explicit.

Fifteen precise mouse/Ensembl-derived developmental, proliferation or signaling assertions are unresolved pending their donor experiments. Their shared sources are UniProtKB:P97929 and ensembl:ENSMUSP00000038576. The older blanket reasoning that phenotypes must be indirect is not retained. Established repair, telomere and meiotic contexts have independent supporting evidence and were assessed separately; no phylogenetic claim was rejected because of donor count or the target's appearance in WITH/FROM.

The two previous NEW process proposals are omitted. BRCA2 directly contributes to RAD51 assembly; the work-performing entity is the BRCA2 mediator positioning RAD51 on DNA. Local GO-CAM models 69a0c46f00002570 and 69a0c46f00002668 already represent BRCA2 adaptor activity in GO:0000730 DNA recombinase assembly, and 69a0c46f00002608 represents an adaptor activity in HR plus a separate inhibitory activity. Complete target activity blocks were read; the newer cited primary papers were not independently reassessed, so their other activities are not newly asserted here. The official assembly hierarchy is part_of synthesis-dependent strand annealing, which is under the existing HR process. The campaign's redundancy constraint supports keeping the assembly mechanism in prose instead of adding another process assertion. For strand invasion, RAD51 performs the invasion step, while the old rationale mixes preceding loading with subsequent POLH-dependent D-loop synthesis. No extra invasion proposal is needed. ROOT's comparator check was incomplete: PALB2's local GOA lacked these proposed terms, but equivalent human RAD52/yeast Rad52 records and a complete remote comparison were unavailable. This is not evidence of systematic absence.

The protected UniProt entry has canonical chain 1–3418 (PRO_0000064984), but no ALTERNATIVE PRODUCTS block, IsoId records or VAR_SEQ features. No structured alternative products were invented. The delta105 splice product studied in PMID:21719596, experimental fragments and peptides, drug-resistance reversion alleles, and serum BRCA2 fragments are distinct contexts and are not assigned made-up UniProt isoform identifiers.

Source access is documented paper by paper in the TMP ledger. Sixty cached records contain scientific abstracts; PMID:9126734 does not. Metadata flags mark 35 caches as full text and 26 as abstract-only, but several nominal full-text records contain only Introduction/Discussion or a duplicated abstract. Actual Results were inspected for the critical purified-protein, telomere, structural dimer, target HR/SSA, interaction and peptide-binding evidence identified in the ledger. No complete figure/supplement inspection is claimed. All 23 Reactome event summaries were inspected for their localization/mechanistic context; large mutant enumerations were not exhaustively adjudicated, and the underlying physical-entity records were not fetched.

Full normal validation of the final V5 review passed with ontology-term validation enabled and no disabled reference, GOA or other checks. The only 38 findings are the expected generic protein-binding policy warnings. Separate read-only checks confirmed all source fields, 163 GOA observations, reference identifiers, cached PMID titles, core branch membership and the current specific MF label. Independent scientific review of all 149 decisions passed on preserved V3; the narrow supplemental review covers the later evidence and workflow deltas.

Final staging: row 53 now includes direct human gamma-irradiation evidence from the rechecked cached abstract of PMID:10551859; no source fields or annotation actions changed. The normal update-status command computed DRAFT on the explicit V5 temporary review path. This supersedes V4's incorrect COMPLETE status, since COMPLETE requires no validation warnings. The complete initial ownership/source baseline is recorded separately at fixed main 4b945bf9ef3b2bbce2a75790581d91b609db39a7 and does not authorize publication without a fresh preflight. Full normal validation and the independent full and supplemental scientific review records accompany the final handoff.


## 2026-10-03 — Follow-up to PR #3893 review

This follow-up supersedes the preceding audit's treatment of the fifteen Ensembl process transfers and its decision to represent fork protection only in prose. All 149 machine-sourced annotation objects remain unchanged outside their review fields, including the negated HAT assertion. The final decisions are 50 ACCEPT, 69 KEEP_AS_NON_CORE, 27 UNDECIDED, two MARK_AS_OVER_ANNOTATED and one MODIFY. There are no PENDING decisions. The description remains a project-independent biological summary.

The earlier revision deleted all 101 pre-existing `supporting_text` values, including useful core-function evidence. Its statement that no new quotations were added did not adequately disclose that deletion. No general project rule required deleting every evidence excerpt. This follow-up restores selected, verified experimental anchors: eleven supporting-text entries drawn from six short source excerpts, covering RAD51 strand-exchange stimulation, RPA-coated ssDNA loading, fork protection and both sides of the HAT dispute. Each is an exact substring of its protected publication cache. The remaining reference-only supports retain the source-specific assessments and access limits; they do not imply that an inaccessible assay was read.

The homologous-recombination core retains GO:0140619 DNA strand exchange activator activity. Its immediate process is now GO:0000730 DNA recombinase assembly: purified full-length human BRCA2 stimulates RAD51 assembly and strand exchange, and promotes RAD51 binding to RPA-coated ssDNA ([PMID:20729832](https://pubmed.ncbi.nlm.nih.gov/20729832/), [PMID:20729859](https://pubmed.ncbi.nlm.nih.gov/20729859/)). RAD51 performs the strand-exchange reaction. Cached GO-CAM model 69a0c46f00002570 explicitly places its BRCA2-enabled activity 69a0c46f00002580 in DNA recombinase assembly, within homologous recombination; its enabling molecular function is the broader adaptor activity. The independently supported, more specific activator term is retained here. Earlier notes acknowledged this model but applied the restriction on redundant NEW annotations too broadly when excluding assembly from the core. No extra NEW process row is added, and the older strand-invasion proposal remains omitted. The incomplete comparator check is not converted into evidence that curators systematically exclude BRCA2.

A separate core now records protection of regressed fork arms from nuclease degradation through stabilization of protective RAD51 filaments, under the existing GO:0031297 replication fork processing process. Its molecular-function slot is deliberately omitted: the schema permits this, and a precise separate MF has not been established. This avoids equating fork protection with strand-exchange activation. The actual source distinguishes BRCA2-dependent protection from fork reversal, and distinguishes the human S3291A construct's protective defect from its homologous-recombination competence. The S3291A complementation uses human BRCA2 in hamster V-C8 cells; human RPE-1 experiments provide a separate cellular context. No intrinsic BRCA2 fork-reversal or fork-restart activity is inferred. Relevant Results, captions and Discussion were read, but no figure or supplementary images were inspected ([PMID:29038466](https://pubmed.ncbi.nlm.nih.gov/29038466/)).

The current GOA identifies the same authentic mouse sources for all fifteen questioned transfers: UniProtKB:P97929 and ensembl:ENSMUSP00000038576, assigned by Ensembl on 2025-05-27. The [MGI Brca2 comparative GO table](https://www.informatics.jax.org/homology/GOGraph/Brca2) supplies historical experimental term-to-paper mappings. That graph was generated on 2023-03-10; the site's later footer date does not make it a reconstruction of the 2025 transfer run. It shows that these assertions have specific donor evidence, contrary to a claim that no publications underlie them. The actions below combine that limited provenance with independently inspected evidence, rather than treating every tissue phenotype as either direct or indirect.

| Existing process | Decision and evidence boundary |
| --- | --- |
| Oocyte maturation | UNDECIDED. The donor abstract describes abnormal meiotic progression, with some oocytes completing prophase I, fertilizing and producing embryos in a human-BRCA2 BAC rescue model. The precise maturation experiment remains unread; infertility alone is not the basis for dismissal ([PMID:14660434](https://pubmed.ncbi.nlm.nih.gov/14660434/)). |
| Inner cell mass proliferation | UNDECIDED. The donor abstract reports defective embryonic proliferation and normal apoptosis, but does not expose the specific inner-cell-mass assay ([PMID:9171369](https://pubmed.ncbi.nlm.nih.gov/9171369/)). |
| Brain development | KEEP_AS_NON_CORE. Neural Brca2 deletion causes genotoxic stress and p53-dependent loss during neurogenesis. This supports a bounded developmental genome-maintenance role, not an independent patterning function. The cache has Abstract, Introduction and Discussion, without complete Results or Methods ([PMID:17476307](https://pubmed.ncbi.nlm.nih.gov/17476307/)). |
| Cell population proliferation and positive regulation of mitotic cell cycle | KEEP_AS_NON_CORE. Human BRC5 perturbation disrupts the BRCA2-HMG20b interaction and delays cytokinesis without the RAD51-focus defect caused by BRC4. These actual Results support a contextual division role beyond a generic repair-loss phenotype; peptide perturbation is not equated with universal mitogenic activity ([PMID:21399666](https://pubmed.ncbi.nlm.nih.gov/21399666/)). |
| Female gonad development | UNDECIDED. A truncating mouse allele produces germ-cell loss, but the accessible abstract does not resolve ovarian development versus secondary germ-cell depletion ([PMID:9398843](https://pubmed.ncbi.nlm.nih.gov/9398843/)). |
| DNA-damage intrinsic apoptotic signaling, including its p53-mediated child | MARK_AS_OVER_ANNOTATED. The inspected neural study links repair loss to damage-associated, p53-dependent death; it does not identify BRCA2 as the factor transmitting that death signal. Atm loss did **not** markedly attenuate apoptosis and is not described as required for it. Separate human BRCA2-p53 binding and suppression of p53 activity are explicitly acknowledged ([PMID:17476307](https://pubmed.ncbi.nlm.nih.gov/17476307/), [PMID:20421506](https://pubmed.ncbi.nlm.nih.gov/20421506/)). |
| Hemopoiesis and hematopoietic stem cell proliferation | UNDECIDED. The donor abstract reports colony formation, marrow repopulation and physiological stem-cell proliferation defects. Full assays separating survival, self-renewal, proliferation and lineage development remain unavailable ([PMID:16859999](https://pubmed.ncbi.nlm.nih.gov/16859999/)). |
| p53 DNA-damage signal transduction | UNDECIDED. The historical mapping used obsolete GO:0006978, locally verified as replaced by GO:0030330, but its donor paper was inaccessible. The direct human p53 interaction is relevant without establishing BRCA2 as a signal-transducing component ([PMID:8738145](https://pubmed.ncbi.nlm.nih.gov/8738145/), [PMID:20421506](https://pubmed.ncbi.nlm.nih.gov/20421506/)). |
| Chordate embryonic development | KEEP_AS_NON_CORE. The cached mouse-null abstract establishes early developmental failure, partly alleviated by p53 loss. The role is bounded to genome maintenance and embryonic viability, without claiming body-pattern specification ([PMID:9171368](https://pubmed.ncbi.nlm.nih.gov/9171368/)). |
| Chromosome organization | ACCEPT. Direct human BRCA2-mediated RAD51 assembly and repair support this broad chromosome-maintenance process without implying chromosome coating or BRCA2-catalyzed strand exchange ([PMID:20729832](https://pubmed.ncbi.nlm.nih.gov/20729832/)). |
| Stem cell proliferation | UNDECIDED. Relevant donor experiments remain incompletely assessed; repair/survival rescue is not automatically a measurement of proliferation rate ([PMID:9398843](https://pubmed.ncbi.nlm.nih.gov/9398843/), [PMID:9660919](https://pubmed.ncbi.nlm.nih.gov/9660919/)). |
| Cellular senescence | UNDECIDED. A donor C-terminal deletion accelerates senescence with preserved irradiation checkpoints; preventing repair-loss senescence differs from executing its program, and the complete assay remains unread ([PMID:9699678](https://pubmed.ncbi.nlm.nih.gov/9699678/)). |

No new publication cache was manufactured or fetched for those donor studies. The uncached abstracts and historical mappings are linked here with their access limits. The only added YAML references, PMID:17476307 and PMID:9171368, already existed in the protected local cache; their exact cached titles are retained. These bring the collection to 94 references, including 63 PMIDs. Donor consultation and the independent core consultation were bounded contributions; they are not substitutes for the separate final scientific review.

Positive H3/H4 acetyltransferase rows remain UNDECIDED, with short anchors from both the positive claim and the opposing P/CAF-associated activity report. The accepted NOT annotation is unchanged. Both caches are abstract-only; the purification and contamination-control experiments were not inspected. No claim is made about an exhaustive replication history. Specific questions and a proposed controlled reconstitution experiment now record this remaining conflict and the fork-MF/donor-provenance gaps ([PMID:9619837](https://pubmed.ncbi.nlm.nih.gov/9619837/), [PMID:9824164](https://pubmed.ncbi.nlm.nih.gov/9824164/)).

The previous append-only history record listed suggested_questions and suggested_experiments among its default section names even though those fields were absent from that revision. That old record is preserved. This follow-up actually adds both sections; the next history entry should explicitly correct the earlier section-list imprecision and identify the sections changed here.

Normal validation of candidate V4 passed with ontology, reference, GOA and all usual checks enabled. It reports 39 warnings: 38 supported generic-binding policy warnings and one warning that GO:0000730 in the core lacks a matching annotation row. The latter is retained deliberately rather than adding a redundant NEW assertion. The fork core's omitted molecular-function slot causes no validation error. Status remains DRAFT because warnings remain; all annotation decisions have been completed, including the 27 explicitly unresolved ones. The first V1 validation attempt failed because its default uv cache was unwritable; the preserved rerun and V2 used the existing writable temporary-cache configuration. No source caches or Git metadata were changed.


## 2026-10-03 — HR core process coverage follow-up

PR #3893 review 5399761458 accepted the donor-evidence, evidence-anchor and fork-protection corrections, and identified a remaining gap in the core summary. Restored GO:0000724 (double-strand break repair via homologous recombination) alongside GO:0000730 (DNA recombinase assembly) in the RAD51-activation core. The former is already supported by five ACCEPT annotations, including purified-protein evidence; the latter records the immediate assembly step represented in GO-CAM. This is a core-summary refinement, not a NEW annotation. Existing annotation decisions, source fields, references, quotes, the separate fork-protection core and DRAFT status are unchanged. Targeted validation and rendering are rerun for this revision.
