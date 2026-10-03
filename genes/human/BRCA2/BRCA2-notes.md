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
