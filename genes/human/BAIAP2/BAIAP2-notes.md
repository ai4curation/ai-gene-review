# BAIAP2 (IRSp53) — curation notes

UniProt Q9UQB8. Human. GOA snapshot refreshed during this pass (see "Stale snapshot"
below); all claims cross-checked live against QuickGO.

## What the protein does

IRSp53 is a curvature-sensitive membrane–actin adaptor. Three modules, three jobs:

- **N-terminal I-BAR/IMD** — binds PI(4,5)P2 directly and reads *negative* membrane
  curvature. Mattila et al. mapped the PI(4,5)P2-binding site and showed its geometry is
  inverted relative to classical BAR domains, so the domain binds the *interior* of a
  tubule
  [PMID:17371834 "because of a difference in the geometry of the PI(4,5)P(2)-binding site, IMDs"].
  That single structural fact explains why I-BAR proteins make protrusions where BAR
  proteins make invaginations. The same domain binds and bundles F-actin
  [PMID:14752106 "The IMD alone, derived from either IRSp53 or MIM, induced filopodia in HeLa cells and the formation of tightly packed parallel F-actin bundles in vitro"].
- **Central partial-CRIB / proline-rich region** — receives activated Cdc42 and Rac1
  [PMID:11130076 "Activated Rac binds to the amino terminus of IRSp53"]. It also carries
  the phosphorylation sites through which 14-3-3 holds the protein autoinhibited.
- **C-terminal SH3** — recruits the effectors that actually polymerize and bundle actin:
  WAVE2, N-WASP, Eps8, Mena/VASP
  [PMID:11696321 "Cdc42 induces filopodia by promoting the formation of an IRSp53:Mena complex."].

In neurons the same adaptor logic operates postsynaptically, via PSD-95/PSD-93 and the
Shank family
[PMID:15673667 "(IRSp53), which is highly expressed in the postsynaptic density (PSD), is known"].

A point worth carrying forward, because it cuts against the obvious reading of the
bundling annotations: Mattila et al. found the filopodia-forming activity of the IMD to
depend on membrane deformation *rather than* on F-actin bundling or GTPase binding
[PMID:17371834 "that the membrane-deforming activity of IMDs, instead of the previously proposed"].
Actin binding is a real property of the domain but not the mechanism by which protrusions
are built, and `core_functions` orders the four entries accordingly.

## Audit of the prior review (this pass)

The review was already `status: COMPLETE` from the PAINT no-IBA batch (PR #2956) and
passed validation. Four defect classes were found. All are fixed; the file went from 118
to 131 annotations and from 2 to 4 core functions.

### 1. Fabricated citations that passed validation via an escape hatch

Seven `supported_by` entries cited bare DOIs (`DOI:10.7554/eLife.72316`,
`DOI:10.1242/jcs.262064`) that appear nowhere in the `references` list. **Six of the seven
quotes are verbatim text from `BAIAP2-deep-research-falcon.md`, attributed to primary
papers they were never taken from**; one ("IRSp53 recognizes ~100 nm PM evaginations…") is
a paraphrase occurring in no source at all. One still carried its bullet label,
`"Sites of action: …"`.

**Why they passed is worth recording precisely, because the obvious explanation is wrong.**
It is not that a DOI citation is unverifiable. `publications/` holds 232 DOI-keyed records,
`validation/supporting_text.py` resolves `DOI:x/y` to `publications/DOI_x_y.md`, and *both*
DOIs here were already cached — `DOI_10.7554_eLife.72316.md` is 83 KB of full text,
committed in the same PR (#2956) that wrote these quotes. The verbatim check also does
cover annotation-level `supported_by`, not just `references[].findings[]`.

The actual reason is that each of those entries carried `full_text_unavailable: true`, and
that flag suppresses the substring check outright — irrespective of reference type, and
irrespective of whether the publication is cached with full text. Verified by injecting
`"PURPLE ELEPHANTS CATALYSE THE RIBOSOME ON TUESDAYS."` as the `supporting_text` on
`PMID:37747150` (83 KB of cached full text): caught as `Text part not found as substring`
without the flag, `✓ Valid` with it. Five of the six original quotes are likewise genuinely
absent from the cached DOI files, so the fabrication finding stands; the flag is what let
them through.

The flag therefore does double duty — a legitimate signal on abstract-only records, and a
blanket verification opt-out — and the two uses are indistinguishable in the file. Anyone
auditing a review here should treat `full_text_unavailable: true` on a `supported_by` entry
as "this quote was never checked", not as a property of the cited paper, and should confirm
the flag against the cached record rather than trusting it.

Three of the seven sat on rows GOA has since retired and went away with them. The remaining
four were re-grounded on primary literature with quotes verified verbatim against the
cache: GO:0030838 and GO:0007009 → PMID:37747150, GO:0043197 → PMID:24639075, GO:0061003 →
PMID:15673667.

The `DOI:10.1242/jcs.262064` citation was doubly wrong: it resolves to PMID:39404604,
*"HIV-1 assembly — when virology meets biophysics"*, cited in support of adaptor activity.

Where this pass sets `full_text_unavailable: true` itself (on the PMID:19366662 reference,
whose cached record really is abstract-only and about the paralog), it is set on the
*reference* entry and the unverifiable quotes were deleted rather than left flagged — so no
`supporting_text` in this file is exempted from checking.

### 2. Six IEA calls dismissed on rationales that misstate their provenance

Every `MARK_AS_OVER_ANNOTATED` row was justified with some version of "not supported" or
"may be transferred from ortholog data". Tracing each `GO_REF:0000107` Ensembl transfer
back to its source shows all six rest on a rodent **experimental** annotation by RGD or
SynGO — curators who read the full text. Per the CLAUDE.md rule against overruling
curators from incomplete evidence, all six were re-decided, and the review now contains
no `MARK_AS_OVER_ANNOTATED` calls at all.

| Term | Real source | Was | Now |
|---|---|---|---|
| GO:0001221 transcription coregulator binding | rat Baiap2 IPI, PMID:10332026 (RGD) | OVER_ANNOTATED | KEEP_AS_NON_CORE |
| GO:0005874 microtubule | rat Baiap2 IDA, PMID:24639075 (RGD) | OVER_ANNOTATED | KEEP_AS_NON_CORE |
| GO:0030141 secretory granule | rat Baiap2 IDA, PMID:17120053 (RGD) | OVER_ANNOTATED | KEEP_AS_NON_CORE |
| GO:0098685 Schaffer collateral - CA1 synapse | mouse Baiap2 IDA+IMP, PMID:19193906 (SynGO) | OVER_ANNOTATED | ACCEPT, then dropped — GOA retired the row |
| GO:0099523 presynaptic cytosol | rat Baiap2 IDA, PMID:15673667 (SynGO) | OVER_ANNOTATED | KEEP_AS_NON_CORE |
| GO:0099524 postsynaptic cytosol | rat Baiap2 IDA, PMID:15673667 (SynGO) | OVER_ANNOTATED | ACCEPT |

Three deserve comment.

`GO:0001221` was called unsupported, but its source is PMID:10332026, the DRPLA paper
showing atrophin-1 binding the IRSp53 SH3 domain. Atrophin-1 is a transcriptional
corepressor, so `GO:0001221` is the correctly-typed molecular function — and since human
GOA has now retired its own generic `GO:0005515` row citing that paper, this transferred
term is the only remaining record of the interaction.

`GO:0099523`/`GO:0099524` were dismissed as "overly specific; cytosol annotation is
sufficient". Specificity at that granularity is the purpose of the SynGO term set, and
both are SynGO IDAs.

`GO:0005874 microtubule` is the one where the verdict survives in spirit but the reasoning
did not: it is a genuine rat immunogold EM observation
[PMID:24639075 "and large dendritic shafts, where it was typically associated with microtubules"],
not an ortholog artefact — but proximity is not function, so it is non-core rather than
dismissed.

### 3. Two NEW annotations cited a generated summary as IDA evidence

`GO:0140090` and `GO:0005546` were proposed with
`original_reference_id: file:human/BAIAP2/BAIAP2-deep-research-falcon.md`, and the first
rationale referred only to "eLife 2023" with no identifier. A generated summary is not
admissible evidence for an IDA. Re-grounded:

- `GO:0140090` → **PMID:37747150** (Quiroga et al., eLife 2023, doi 10.7554/eLife.72316 —
  the "eLife 2023" the draft meant). The falcon file is retained as a secondary
  corroborating source, which is what it actually is.
- `GO:0005546` → **PMID:17371834** (Mattila et al., J Cell Biol 2007), with PMID:38724689
  (Picas et al., Commun Biol 2024) as independent corroboration.

Comparator check on `GO:0140090`: the term is already carried in human by the
BAR-superfamily proteins **ARFIP2, ICA1 and PICK1**, each IDA from PMID:29768204, so
annotating curvature sensing to a BAR-domain protein is established practice and IRSp53's
absence is a gap. The activity is executed by IRSp53's own I-BAR domain, so it clears the
"which entity performs the step" test.

### 4. `proposed_replacement_terms` invented from bulk interaction data

Thirteen `REMOVE` rows sourced from high-throughput interactome screens proposed a
specific molecular function (`GO:0030674` or `GO:0097110`) inferred from the fact of a
binding alone. Naming a function from an interaction list is exactly what the skill
forbids; the replacements were withdrawn and each row now says why. Nothing is lost —
both terms are independently annotated and accepted elsewhere in the review.

The mirror error was also present: `GO:0003779 actin binding` was proposed as a
replacement on a row whose evidence is an **ACTB co-immunoprecipitation** (PMID:19171758).
An adaptor pulls down whatever its partners are attached to; that is not actin-binding
evidence. Withdrawn there and asserted once on its real in vitro source (below).

### 5. A missing molecular function

`GO:0003779 actin binding` was added as `NEW` and as a fourth core function. BAIAP2
carries `GO:0051017` and `GO:0051764` as processes but had **no actin-binding molecular
function anywhere in GOA**, so the activity producing those processes was unrepresented.
The evidence is in vitro on purified IMD and purified actin (PMID:14752106), with the
residues mapped
[PMID:15635447 "Mutagenesis of conserved basic residues at the extreme ends of the dimer abrogated actin bundling in vitro and filopodia formation in vivo"].
Comparator: MTSS1 carries GO:0003779 by IDA (PMID:12570871) and IBA, MTSS2 by IEA and
IBA, so there is no convention against the family. Their IBA sits on node PTN004481656,
not BAIAP2's PTN001022094, which is why it has not propagated — the argument here is
target-specific direct evidence, not a propagation claim.

`GO:0180020 membrane bending activity` was considered for the deformation half of the
I-BAR activity and **rejected**: in human it is carried only by CHMP2A, CHMP3 and OPA1,
by no BAR-superfamily protein at all. `GO:0097753 membrane bending` (a process, not a
function) is similarly sparse. That systematic absence reads as a convention not yet
identified rather than a gap to fill, so the point is raised in `suggested_questions`
rather than asserted.

### 6. Stale GOA snapshot

The cached tsv predated a GOA release. After `just fetch-gene --force`, 30 rows were newly
seeded and reviewed, and 18 rows retired by GOA were dropped (the validator treats
carrying them as an error). Among the additions are three experimental annotations the
review had no row for at all:

- `GO:0009898 cytoplasmic side of plasma membrane`, **IDA, PMID:38149472** — de novo
  BAIAP2 p.Arg29Trp in lissencephaly; the variant blocks membrane localization, and Arg29
  is in the I-BAR domain, so the defect is the expected consequence of the mechanism.
- `GO:0046847 filopodium assembly` and `GO:0048812 neuron projection morphogenesis`,
  **IMP, PMID:41133935** — de novo missense variants causing developmental and epileptic
  encephalopathy, clustered in the phosphorylation region mediating 14-3-3 autoinhibition.
  These are *gain*-of-function: the mutants escape autoinhibition and drive constitutive
  hybrid filopodia-lamellipodia protrusions, which is the cleanest evidence that IRSp53
  activity drives protrusion rather than merely permitting it.

Most of the other 27 are additional per-interactor `GO:0005515` rows, removed per
convention.

### Other changes

- Ten `supporting_text` values were article titles carrying scraped journal-date prefixes
  ("2006 Sep 25. …"); prefixes stripped and the highest-value ones replaced with real
  result sentences.
- The four rows citing PMID:19366662 quoted text about **IRTKS (BAIAP2L1)**, the paralog —
  the cached record is abstract-only and its abstract is about IRTKS. Per CLAUDE.md the
  annotations are kept (curators read the full text; UniProt independently cites this
  paper for BAIAP2), but the paralog quotes were removed rather than left looking like
  support, and the reference is flagged `full_text_unavailable` with a `reference_review`.
- Eight references now carry a `reference_review`; seven references were added.
- A section comment had been left inside a `review:` mapping, splitting an annotation's
  `supported_by` from its `action`. Valid YAML, misleading to read; moved.
- `description` extended to cover the postsynaptic role, 14-3-3 autoinhibition, and the
  disease genetics, none of which it mentioned.

## Open questions

Recorded in `suggested_questions`. Two flagged here:

- The presynaptic pool implied by `GO:0099523` sits oddly against everything else known
  about IRSp53, which is postsynaptic. SynGO curated it IDA, so it stands, but a targeted
  presynaptic localization study would settle it.
- `GO:0098685 Schaffer collateral - CA1 synapse` was re-decided to ACCEPT on strong SynGO
  evidence (PMID:19193906) and then dropped because GOA retired the Ensembl transfer it
  rode in on. The underlying mouse annotation is unaffected. If a future GOA release
  restores it, the analysis above is why it should be accepted rather than dismissed.
