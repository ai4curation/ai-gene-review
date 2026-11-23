# Human ACO2 review notes

Current decisions after the second PR review: 24 ACCEPT, one UNDECIDED (cytosol),
one TOO_GENERAL, and one NEW nucleus annotation. The final journal entry below
supersedes the earlier KEEP_AS_NON_CORE cytosol assessment; original-source access
limitations remain explicit.

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
consultation. The initial assessment was DRAFT with 18 ACCEPT, seven UNDECIDED,
one TOO_GENERAL, plus one NEW nucleus CC. The later PR-review entry supersedes
six of those source-specific UNDECIDED actions while preserving the access gaps.

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

### Nuclear evidence and the initial cytosolic assessment

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
does not resolve human cytosolic ACO2. The follow-up below uses a distinct human
cytosolic fractionation result.

PTHR43160 native members place Q99798 in mitochondrial SF3. PAINT assigns
activity/cluster/TCA at PTN000186533 and mitochondrial location at PTN000186534.
Q99798 appearing among descendant evidence for TCA is expected, not circular.
The historical cytosolic PTN001705783 gain boundary, seeded by yeast ACO1 and
bacterial AcnB, was not recovered; the follow-up evaluates independent human
localization evidence rather than claiming to have verified that boundary.
Its short donor list is not itself a reason to reject the IBA. Family curation
is outside this PR; another active PR owns that family review. Human ACO1/IRP1,
budding-yeast ACO2, and fission-yeast Aco2 are not interchangeable with human ACO2.

### Original-source access limits

PMID:9630632 is abstract-only. It directly identifies an iron-dependent
mitochondrial enzyme, supporting the TAS iron-binding and mitochondrial rows.
The IDA iron-binding/TCA/citrate assays and the citrate-metabolism TAS statement
cannot be checked from this abstract; their initial UNDECIDED actions were
subsequently revised to ACCEPT for the independently established biological claims.
An inaccessible full text is not evidence that the original curator was wrong.
[PubMed record](https://pubmed.ncbi.nlm.nih.gov/9630632/).

PMID:20833797's retained cache contains Abstract and Discussion despite its
`full_text_available: true` flag. The ACO2-specific phosphoproteomic result is
not exposed. PMID:34800366's article body is available, but the ACO2-specific
Table S1 row was not recovered. Both experimental localization contexts remain
unverified as individual experiments. Their initial UNDECIDED actions were later
revised to ACCEPT with curator deference; neither missing prose mention nor a
failed supplement fetch is used as evidence against mitochondria.
[PMID:20833797](https://pubmed.ncbi.nlm.nih.gov/20833797/),
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

The initial review passed schema, ontology-term, best-practice, and history
validation. Three warnings flagged differing ACCEPT/UNDECIDED actions for shared
iron-binding, mitochondrion, and TCA terms; the differences deliberately retain
original-source uncertainty rather than contradict the biological functions.
The literature validator checked 16 snippets and eight titles without issues;
its 39 skipped database snippets were not counted as literature-verified.
The canonical all-quote check separately verified all 79 supporting-text
occurrences against retained sources, with zero unchecked or failing quotes.
Canonical HTML rendering succeeded in memory. Native GOA/UniProt bytes and all
26 native annotation identities remained unchanged. No local environment or
lockfile was created or modified by the guarded checks.

## 2026-11-15 — PR review follow-up

External review [5910686575](https://github.com/ai4curation/ai-gene-review/pull/6400#pullrequestreview-5910686575)
correctly identified that six actions treated source-access gaps as uncertainty
about biological claims that accessible independent evidence already establishes.
The original curation instructions explicitly permit ACCEPT with curator
deference when the function is clearly correct. Iron binding, mitochondrial
localization, the aconitase TCA step, and citrate metabolism therefore become
ACCEPT consistently across their native evidence contexts. This does not certify
inspection of the original PMID:9630632 assays or the unrecovered ACO2 proteomics
table rows. PMID:20833797 and PMID:34800366 retain UNVERIFIED assessments of those
source-specific observations. All native evidence codes and references remain.

The separate request to mark the cytosol IBA as over-annotated is not supported
by the cited precedents. The [PTHR43160 node assessment](https://github.com/ai4curation/ai-gene-review/blob/8bcaac48a09c9b5c08ad5b6328b5ca1b0e8f1583/interpro/panther/PTHR43160/PTHR43160-review.yaml#L228)
is itself UNRESOLVED and discusses a **homocitrate dehydratase named ACO2 in
budding yeast**, not human Q99798. The [SPAC24C9.06c review](https://github.com/ai4curation/ai-gene-review/blob/8bcaac48a09c9b5c08ad5b6328b5ca1b0e8f1583/genes/SCHPO/SPAC24C9.06c/SPAC24C9.06c-ai-review.yaml#L170)
concerns a fission-yeast protein. These are useful comparisons, but neither
demonstrates a human compartment-specific loss or settles the human PAINT node
boundary. The number of descendant seeds is not used as a quality score.

The human record's TRANSIT 1..27 feature supports mitochondrial targeting, with
by-similarity evidence from P16276; it is not an independently verified human
processing assay or proof of mitochondrial exclusivity. The known human nuclear
pool demonstrates why targeting alone cannot exclude additional compartments.
The two nuclear quotations were removed from the cytosol row. Its final positive
support instead comes from the distinct human cytosolic fractionation panel and
its legend, as described below. Targeting remains a positive mitochondrial
observation, not negative evidence about other compartments.

Primary Fig. 1a of PMID:42386731 provides positive human evidence: a discrete ACO2
band is visible in the cytosolic (C) fraction of **22Rv1** cells, alongside
cytosolic beta-tubulin and without an obvious C-lane Tom20 or Lamin A/C band.
The caption reports these fraction-purity markers and at least three independent
experiments per cell line. This qualitative observation supports the existing
cytosol annotation as KEEP_AS_NON_CORE in the demonstrated context. Lower signal
than the mitochondrial band is not grounds to reject a location annotation;
other TCA enzymes in the same fraction do not by themselves establish contamination.

The [original Fig. 1 image](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7ce1/13462710/ac2033c906aa/41467_2026_74786_Fig1_HTML.jpg)
was independently inspected by ROOT and the consultant in memory, without
retaining a source snapshot. Its 705-by-993-pixel JPEG has SHA256
`e89b7304f965d830c7b8f8b7008b3be156d7d61f11ca78377732bb21be3ce3df`.
This is a qualitative band-presence assessment, not densitometry, a cytosolic
catalytic assay, or evidence for a complete cytosolic TCA cycle. The native
relationship qualifier is preserved and does not impose an extra assay criterion.

Fig. 2b concerns a different human cell line, MDA-MB-468; its C-lane signal is
less resolved and cannot negate the 22Rv1 observation. The redistribution after
KPNA2 depletion in Fig. 2h is mouse GL261 and is not used as positive human
cytosol evidence. An initial follow-up inclination to retain UNDECIDED was
superseded after closer inspection of Fig. 1a and its compartment controls.
The unresolved historical PAINT gain boundary remains explicit in the source
metadata without overriding independently supported localization. Final counts
are 24 ACCEPT, one KEEP_AS_NON_CORE, one TOO_GENERAL and one NEW. No new process
annotation is introduced; the sole core unit remains the mitochondrial TCA step.

Follow-up schema, term and best-practice validation passes with no curation
warnings, so the review status is COMPLETE under the schema's definition.
Reference validation checks 16 snippets and eight titles without issues; its
41 skipped database snippets are covered by the separate canonical check of all
82 quote occurrences, with zero unchecked or failed quotes. In-memory HTML
rendering succeeds. All 26 native identities and native source bytes, the NEW
nucleus identity, and the initial CREATE history record remain unchanged. The
new EDIT history record captures this follow-up. These checks do not claim that
unavailable original assays have been recovered or grant campaign delivery credit.


## 2026-11-15 — second PR review: cytosolic residency remains unresolved

[Review 5910848709](https://github.com/ai4curation/ai-gene-review/pull/6400#pullrequestreview-5910848709)
accepts the six earlier claim-level corrections and acknowledges that the cited
budding-yeast ACO2 precedent is not human ACO2. Those corrections remain intact.
The carryover concern warrants a narrower interpretation of the human fractionation.
ROOT and an independent consultant re-inspected the original Fig. 1 image linked
above in memory; its bytes and SHA256 match the previously recorded image.

In the displayed 22Rv1 fractions, ACO2, FH and OGDH have visible C-lane signal; SDHA is predominantly mitochondrial with no confidently resolved discrete C band, and MDH2 C-lane signal is faint or ambiguous relative to its clear M band.

The image and reported markers do not by themselves distinguish a resident cytosolic ACO2 pool from soluble mitochondrial carryover; neither contamination nor true cytosolic residency is established by this qualitative inspection.

Beta-tubulin is present in the C lane, Lamin A/C is predominantly N, and Tom20 is
predominantly M without an obvious C band. These qualitative marker observations
have no calibrated detection limit or cross-antibody abundance comparison. A
negative membrane marker does not exclude leakage of a soluble matrix protein;
we do not infer either quantitative contamination or an ACO2-to-Tom20 abundance
ratio. Lower intensity than M alone is not a reason to reject a location claim.

The controls must also be described accurately. The Results place OGDH with CS,
ACO2 and IDH2 among enzymes seen in nuclear fractions. The subsequent
predominantly-mitochondrial list is SUCLG1, SDHA, FH and MDH2, specifically contrasted
with little signal in the nucleus. It is not a categorical claim that all of these
proteins are absent from cytosol. Thus FH/OGDH C signal is not, by itself, proof of
carryover. Conversely, the displayed panel does not supply an independently
validated quantitative test excluding soluble mitochondrial carryover. The Methods
state that the Dignam modifications optimized nuclear and mitochondrial purity.
The paper's orthogonal ACO2 localization and flux experiments establish nuclear
biology; they do not independently resolve endogenous cytosolic residency in 22Rv1.

The native cytosol IBA is therefore UNDECIDED. This reverses the earlier
KEEP_AS_NON_CORE conclusion because the location itself remains uncertain, not
because a cytosolic catalytic assay is demanded and not because the cytosolic pool
has been disproved. The human PAINT gain/loss placement remains UNRESOLVED;
mitochondrial targeting and other-species precedents still do not prove a human
loss. The positive mitochondrial and human nuclear conclusions are unchanged.

The separate qualifier objection does not control this assessment. The
[annotation-reviewer skill](https://github.com/ai4curation/ai-gene-review/blob/c5137909dd32dd7d635f26cde65a7f2db6cfe2c6/.codex/skills/annotation-reviewer/SKILL.md#L156)
explicitly treats relationship values as inert for adjudication except NOT and
contributes_to. The native is_active_in value is preserved unchanged; it is not
used to impose an additional catalytic-activity criterion. The nucleus annotation
and all other native identities likewise remain unchanged.

The confident cytosol sentence is removed from the biological description. The
figure-reading inference is recorded here and cited as reviewer analysis, rather
than presented as the authors' cytosolic conclusion. This notes citation makes the
interpretation traceable; it is not independent biological corroboration. No
NEW process or cytosolic activity is proposed. All 26 native contexts and the one
NEW nucleus context remain: 24 ACCEPT, one UNDECIDED, one TOO_GENERAL and one NEW.
The single core function remains mitochondrial citrate/isocitrate isomerization.

Round-two schema, term and best-practice validation passes with zero curation
warnings. Reference validation checks 17 snippets and eight titles with no issues;
its 42 skipped snippets are covered by the canonical audit of all 84 quote
occurrences against 17 input files. Rendering succeeds in memory. COMPLETE is
retained under the schema definition (no PENDING and no validation warnings); it
does not mean the one explicitly UNDECIDED localization has become certain.
The third, append-only EDIT history record documents this reassessment. Neither
local validation nor record status grants delivery or campaign completion credit.
