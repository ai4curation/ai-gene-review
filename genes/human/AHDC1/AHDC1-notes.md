# AHDC1 (Q5TGY3) — review notes

Working journal for the GO annotation review of human AHDC1 / Gibbin.

## 1. Row reconciliation (do this first)

| source | count |
|---|---|
| `AHDC1-goa.tsv` data rows (16 lines − 1 header) | 15 |
| `fetch-gene` stub `- term:` entries | 15 |
| QuickGO `geneProductId=UniProtKB:Q5TGY3` (`numberOfHits`) | 15 |

The three agree, so the stub did **not** collapse any rows on this gene (contrast
ADAMTSL5 and ACTR5, where it did). The three `GO:0005515` rows are already split
one-per-partner-per-publication.

## 2. The brief's headline hypothesis did NOT confirm — and the reason is checkable

The task brief predicted "an InterPro2GO mapping from the AT-hook is almost certainly
present, granting a DNA-binding MF with `GO_REF:0000002`". **There is no such row, and
there cannot be one.**

InterPro API (`/api/entry/InterPro/protein/UniProt/Q5TGY3/`, `count=2`, unpaginated):

| entry | type | name | interpro2go |
|---|---|---|---|
| `IPR032757` | domain | Domain of unknown function DUF4683 | *(empty)* |
| `IPR039225` | family | Transcription factor Gibbin | *(empty)* |

and `/api/entry/all/protein/UniProt/Q5TGY3/` returns exactly four signatures:
`IPR032757`, `IPR039225`, `pfam PF15735` (DUF4683), `panther PTHR15617`.

Two consequences:

1. **No AT-hook signature matches AHDC1 at all.** Neither Pfam `PF02178` nor the
   PROSITE AT-hook profile nor `IPR017956` appears. UniProt's two `DNA_BIND` "A.T hook"
   features are manual and carry **no `/evidence` line**, so nothing in the sequence
   databases independently detects them.
2. **Neither matching InterPro entry carries any GO term**, so the InterPro2GO pipeline
   has nothing to emit. `PTHR15617`'s cached metadata also has `go_terms: null`, and
   UniProt records `DR   PAN-GO; Q5TGY3; 0 GO annotations based on evolutionary models.`
   — so there is no IBA/PAINT row either.

So AHDC1 has **no family-level or domain-level GO inference from any source**. Every
row on the gene traces to one of four publications plus four automatic pipelines. This
is worth stating as a non-confirmation rather than quietly dropping (ADAMTSL5 lesson).

### But hazard #2 in the brief *did* confirm, by a different route

The over-claim is present — it just entered as a **manual `IDA` from UniProt** off the
Nature paper, not as a domain-derived IEA. `GO:0003700 DNA-binding transcription factor
activity` requires (QuickGO definition, fetched):

> "A transcription regulator activity that modulates transcription of gene sets via
> selective and non-covalent binding to a **specific double-stranded genomic DNA
> sequence (sometimes referred to as a motif)** within a cis-regulatory region."

Nothing in `PMID:35585237` measures sequence-specific binding. See §4.

## 3. What the AT-hooks actually look like

Computed from the cached UniProt sequence (`athook.py`, asserts length 1603):

| feature | residues | sequence | canonical `R-G-R-P` core? |
|---|---|---|---|
| A.T hook 1 | 396–408 | `RRKAGRGRKADAG` | **no** — `GRGRK`, the invariant proline is absent |
| A.T hook 2 | 544–556 | `KRKRGRPPKNLLL` | **yes** — `KRK`·`RGRP`·`PKN`, textbook |

`RGRP` occurs exactly once in the 1,603-residue sequence, at 547–550. So AHDC1 has one
canonical AT-hook and one degenerate one. An AT-hook binds the **minor groove of AT-rich
DNA**; even at full strength it confers no sequence specificity in the `GO:0003700`
sense.

The genetics does support the motif mattering: `PMID:34950897` finds four of ten XGS
missense variants inside 71 residues (537–607) around AT-hook 2, **two of them inside
the 12-residue core** — matching UniProt's `VAR_086664` (G548S) and `VAR_086665` (R549H),
which lie inside 544–556. That is evidence the region is functionally important; it is
not a DNA-binding measurement. The same paper says only that "AHDC1 **likely** has a
function in the nucleus mediated by its AT-hook binding motifs", and the Nature paper's
Discussion says "We **speculate** that this regulation occurs through Gibbin DNA
binding".

## 4. What `PMID:35585237` (Collier et al., Nature 2022) actually did

This single paper supplies five of the fifteen GOA rows. Full text is cached.

| claim | assay | what it licenses |
|---|---|---|
| binds promoters/enhancers | ChIP-seq of a **stably introduced, inducible, tagged** Gibbin transgene in hESC | chromatin association; no motif, no sequence specificity reported |
| regulates ~1,100 transcripts | RNA-seq of two **CRISPR KO** hESC clones | regulation of Pol II transcription |
| works with GATA3 | RNA-seq epistasis; GATA3 over-expression effect abolished in GKO | coregulator, not the DNA-recognition module |
| interactome | **BASU proximity labelling** + MS | zinc-finger TFs incl. the entire GATA family; methyl-CpG readers |
| loop maintenance | cohesin **HiChIP**, WT vs GKO | requirement for contacts; not a bridging measurement |
| hypermethylation | 850k arrays, WT vs GKO; DNMT activity assay | restrains cytosine methylation at cis-regulatory DNA |
| mesoderm / skin | scRNA-seq, organoids, mosaic CRISPR mouse | mesoderm formation, skin morphogenesis |

The decisive sentences against a sequence-specific TF reading are the authors' own:

> "Interestingly, Gibbin DNA binding itself does not appear to be sufficient to drive
> gene expression, as ChIP-seq signal was not restricted to the mesoderm lineage or to
> Gibbin-regulated loci"

> "Day 0 ChIP-seq indicated Gibbin does not bind to DNA in the absence of RA/BMP4"

and the abstract's framing that "enhancer- or promoter-bound Gibbin interacts with
dozens of sequence-specific zinc-finger transcription factors" — i.e. the sequence
specificity in the system is supplied by the partners.

**No purified AHDC1 protein appears anywhere in the paper.** No EMSA, no SELEX, no motif
call, no fluorescence anisotropy. The whole DNA-side of the story is crosslinked
chromatin from cells.

Conclusion: `GO:0003700` → **MODIFY to `GO:0003712 transcription coregulator activity`**,
whose definition ("modulates the transcription of specific gene sets via binding to a
DNA-binding transcription factor at a specific genomic locus, either on its own or as
part of a complex") is what the paper actually demonstrates. `GO:0003682 chromatin
binding` is added separately for the ChIP-seq itself.

**And the shape of the correction matters as much as its direction.** Ancestor closure
over `is_a,part_of` was fetched for both terms: `GO:0003712`'s only ancestors are
`GO:0140110` and the molecular-function root, and `GO:0003700` sits under `GO:0140110`
too. So `GO:0003712` is a **sibling of `GO:0003700` under `GO:0140110`**, not an ancestor
of it. This is a *lateral* correction inside the transcription-regulator branch — the
review is not retreating to a vaguer parent, it is naming a different activity in the same
class. That distinction is the difference between "we could not tell how specific to be"
and "the specific claim on record is the wrong one", and only the second is true here.

The same closure query is what showed that `GO:0006355` is an ancestor of `GO:0003700`
but **not** of `GO:0003712` — i.e. correcting the MF silently voids the `GO_REF:0000108`
BP row, which is why that row is handled explicitly rather than left alone.

### Reading the whole paragraph, not the quotable sentence (ACTR10 lesson)

Two places where the neighbouring sentence changes the reading:

- The keratinocyte stratification defect looks like a cell-autonomous AHDC1 phenotype
  until you read that WT mesoderm recombined with GKO ectoderm **rescues** it and that
  "This effect was not seen in primary keratinocyte mutants (NHKs)". So I did **not**
  propose `GO:0030216 keratinocyte differentiation`: the defect is non-cell-autonomous
  and annotating it to AHDC1 would misattribute a dermal phenotype to an epidermal
  process.
- The interactome is enriched for heterochromatin factors, which invites a
  heterochromatin term — but the same paragraph reports that "loss of Gibbin did not
  alter H3K9me3 deposition or heterochromatin (HP1α positive) nuclear bodies". So
  `GO:0090310 negative regulation of DNA methylation-dependent heterochromatin
  formation`, the one surviving GO term in that area, is excluded by the paper's own
  negative result.

## 5. The `GO:0140585` call

`GO:0140585 promoter-enhancer loop anchoring activity` is defined as "**Bridging
together** two cis-regulatory elements … holding two loop anchors together to maintain a
chromatin loop." That is a direct molecular claim about AHDC1 being the bridge.

What the paper has: (a) AHDC1 ChIP peaks at promoters and enhancers; (b) AHDC1 and GATA3
separated by typical promoter–enhancer distances, which the authors say only
"suggest**ing** that promoter/enhancer-bound Gibbin interacts with enhancer-bound GATA3
through long-range chromatin contacts"; (c) a knockout that loses contacts. And their own
mechanistic model routes the loop effect **through DNA methylation and CTCF**, with
decreased CTCF binding at over 2,700 sites in the GKO.

So the loop loss is established; AHDC1 being the physical bridge is not.
→ `MARK_AS_OVER_ANNOTATED`, with `GO:1902275 regulation of chromatin organization`
proposed as the claim the knockout does support.

`GO:0140588 chromatin looping` was considered and **rejected on its definition**: it
describes "loading of an extrusion motor (by an SMC family complex) … chromatin
extrusion that stops at loop anchoring sites". AHDC1 is not an extrusion motor. Reading
the label rather than the definition would have shipped a wrong term here.

## 6. Ensembl Compara round-trip: the two `GO_REF:0000107` rows are circular

WITH/FROM on both is `UniProtKB:Q6PAL7|ensembl:ENSMUSP00000101535`. Resolved:
`Q6PAL7` = `AHDC1_MOUSE`, **reviewed (Swiss-Prot)**, 1,594 aa vs human 1,603 — a genuine
1:1 ortholog, not a paralog.

QuickGO on the donor shows where its two projected terms come from:

```
GO:0001707  IMP  PMID:35585237  UniProt
GO:0043589  IMP  PMID:35585237  UniProt
```

**The same paper** that gives human AHDC1 its own `IDA` rows for those two terms. So
Compara projects mouse annotations of `PMID:35585237` onto a human gene that already
carries direct annotations of `PMID:35585237`. `EVIDENCE_CIRCULAR_OR_REDUNDANT` /
`CIRCULAR_PROPAGATION`, with the term itself correct. Compara runs it in both directions:
mouse Ahdc1 carries `GO:0003700` and `GO:0140585` as `GO_REF:0000107` IEAs projected
*from* the human IDAs.

**Same paper, same experiment class, two different evidence codes.** Human hESC
`GKO` clones and mosaic CRISPR mouse embryos are both loss-of-function perturbations.
UniProt coded the mouse rows `IMP` and the human rows `IDA`. The human rows should be
`IMP` too. This affects `GO:0001707`, `GO:0043589` and, arguably, `GO:0140585` and
`GO:0003700`. Noted per row; it changes no term.

Asymmetry worth recording: mouse Ahdc1 additionally carries **seven** `IMP` rows from
`PMID:37819197` (`GO:0001889`, `GO:0006112`, `GO:0006664`, `GO:0009060`, `GO:0032868`,
`GO:0042445`, `GO:0060612` — liver development, energy reserve metabolism, glycolipid
metabolism, aerobic respiration, response to insulin, hormone metabolism, adipose tissue
development). **None** of these was projected to human. I deliberately did not propose
them: they are whole-animal physiological consequences of a nuclear regulator in one
species, the correct human code would be `ISO`/`ISS` not `IMP` (AHNAK lesson), and the
mechanism linking AHDC1 to energy expenditure is unknown. Recorded as a question instead.

## 7. Projection check on `PMID:35585237` — negative, and that is a finding

QuickGO by reference: `PMID:35585237` → **7 annotations over exactly 2 entities**
(`UniProtKB:Q5TGY3` ×5, `UniProtKB:Q6PAL7` ×2). Not paginated; `numberOfHits == len(results)`.

This is the ACTR8 check, and it comes back clean: no complex-level projection, no
spreading of one phenotype across a subunit set. Contrast ACTR8, where
`PMID:23979016` annotated 16 entities with identical evidence.

## 8. `GO:0005515` — what `NbExp` actually decomposes into

**This section was rewritten after I got it wrong the first time.** My first pass wrote
that "all twelve HTT records are the same single experiment logged twelve times", inferred
from the records sharing one publication accession. Dumping the full records instead of
the summary fields refuted it: the twelve rows carry **twelve distinct interaction ACs**
and four distinct `aliasesA` construct sets. The campaign rule is *verify the number, don't
find a story that makes it acceptable* — I nearly shipped the story.

UniProt's `CC   -!- INTERACTION:` block reads `ATXN1; NbExp=5` and `HTT; NbExp=12`.
Expanding every IntAct record (73 records, 45 distinct partners; `totalElements` asserted
against rows read; **2** of the 73 are RNA-level records where AHDC1 appears as
`ENST00000374011` and are reported rather than silently dropped):

| partner | records | publications | what the records actually differ by | MI |
|---|---|---|---|---|
| ATXN1 `P54253` | 5 | 2 | PMID:16713569 → **2** records, one method (`2 hybrid`), differing by **ATXN1 fragment**: 528-815 "c terminal" and 557-699 "axh region", both `sufficient to bind`. PMID:32814053 → **3** records differing **only by sub-method label**, all one construct `p.Gln225[50]` | 0.67 |
| HTT `P42858` | 12 | **1** | **4 HTT constructs × 3 sub-method labels**. Constructs: 1932-2642; 1-511 `Gln18[49]`; exon-1 with `Gln18` at 17/20/23/49/51/79; 1-504 with `Gln18[23]`/`Gln18[80]` | 0.56 |

So the honest decomposition is:

- **The sub-method triplication is real and is a threefold inflation.** `validated two
  hybrid` (MI:1356) + `two hybrid array` (MI:0397) + `two hybrid pooling` (MI:0398) are
  three logs of one assay. This is the third occurrence in the campaign (ACRV1, ADAMTSL5).
- **The remaining fourfold variation on HTT is the screen's standard huntingtin bait
  panel**, not a mapping performed on this pair — exon-1 and 506-residue polyQ series plus
  a C-terminal fragment, applied to every prey in a ~500-protein neurodegeneration screen.
- **But the records are not contentless.** IntAct curates HTT 1932-2642 as `sufficient to
  bind`, and curates some polyQ lengths as `mutation disrupting strength` and others as
  `mutation with no effect`, so the Y2H readout is graded. And on ATXN1, PMID:16713569
  genuinely maps the binding region to the **AXH domain** (557-699).
- **No region is mapped on the AHDC1 side of any ATXN1 or HTT record.** (Other partners do
  have AHDC1-side `sufficient to bind` features, on `EBI-10697753` and `EBI-9090956`; the
  tag features elsewhere are construct tags, not mapping.)

Promiscuity check: HTT has **1,216** distinct IntAct partners and ATXN1 **634**, against
AHDC1's 45. Both are polyQ neurodegeneration baits, and both screens were designed around
neurodegeneration panels rather than around AHDC1's biology. AHDC1 is also heavily
disordered (ten MobiDB-lite disordered regions in UniProt), the classic sticky-prey
profile.

Partner-accession discipline (ACRV1 lesson): both partners resolve to **reviewed
Swiss-Prot canonical** entries at full length (ATXN1 815 aa, HTT 3,142 aa). No TrEMBL or
ORFeome substitution here — a negative result, reported.

**Verdict, per partner, and it splits:**

- **ATXN1 (both rows) → `KEEP_AS_NON_CORE`.** Two independent laboratories, region mapping
  onto the AXH domain, and a topologically plausible pair (ATXN1 is itself a
  chromatin-binding transcriptional corepressor; both proteins are nuclear). Calling that
  an over-annotation would be wrong. It is simply not a core function, and the term
  conveys nothing.
- **HTT → `MARK_AS_OVER_ANNOTATED`.** One laboratory, bait-panel design, a 1,216-partner
  hub, nothing tested functionally.

Neither is `REMOVE`: both are experimental IPI rows. The informative replacement is not a
refinement of either — it is `GO:0140297 DNA-binding transcription factor binding`, from
the functional paper's own proximity interactome.

## 9. Retraction / erratum check — clean

`CommentsCorrections` read from each cited article's own PubMed record (a Publisher
Correction is **not** findable by a publication-type query — ACTR8 lesson):

| PMID | pubtypes | CommentsCorrections |
|---|---|---|
| 35585237 | Journal Article | none |
| 33644933 | Journal Article + support | none |
| 32814053 | Journal Article + support | none |
| 16713569 | Journal Article + support | `CommentIn` → PMID:16713557 (a Cell Preview, not a correction) |
| 34950897 | Journal Article | none |
| 37819197 | Journal Article + support | none |
| 24791903 | Case Reports + Journal Article | none |

No retractions, errata or expressions of concern.

## 10. affinage: `faith_pct: 100.0` and it missed the only functional paper

The record has no `gates_passed` field; its frontmatter carries
`self_evaluation_pairwise: tie`, `faith_pct: 100.0`, `n_discoveries: 6`,
`citation_count: 6`. All six citations are real numeric PMIDs (no `PMID:bio_*`
preprint ids); each was fetched from PubMed and resolves to a record whose title matches
the claim attached to it, and none carries a retraction, erratum or expression of
concern. Precision is not the problem here.

But its narrative states:

> "The direct molecular mechanism by which nuclear AHDC1 influences gene regulation,
> development, or metabolism has not been characterized in the available corpus."

and its citation list does **not include `PMID:35585237`** — a 2022 *Nature* paper that
is the source of five of the gene's fifteen GO annotations and the sole basis of UniProt's
entire `FUNCTION` block. This is the precision/recall split the campaign has measured:
the gate certifies what it returned, not what it missed. Here the miss is total for
molecular function.

It did surface one thing GO does not have on the human gene: `PMID:37819197`, the mouse
metabolic phenotype (see §6).

## 11. Coverage census — derived, not hand-counted

`ahdc1_refcensus.py` parses the `RN`/`RP`/`RX` blocks of the cached UniProt file and
joins against the GOA TSV:

- **28** UniProt reference blocks, all with a PubMed id, contiguous `RN [1]`–`RN [28]`.
- Classified by the `RP` line: **13 clinical genetics**, **10 proteomics/PTM**,
  **4 sequencing**, **1 function** (`RN [28]` = `PMID:35585237`).
- **2 of 28** UniProt-listed references produced any GO annotation (`35585237`,
  `33644933`).
- The two GOA PMIDs absent from UniProt's list are the two Y2H screens.

So AHDC1's shape is the AFF4 shape: a large literature that is almost entirely human
genetics and mass spectrometry, one functional paper, and a GO record that is thin
because the experiments were thin — a **coverage** situation, not an over-annotation
situation. The exception is the single MF row, which over-reaches.

## 12. Terms considered and rejected

| term | why not |
|---|---|
| `GO:0003680 minor groove of adenine-thymine-rich DNA binding` | This is the motif-derived MF the brief warned about. Nothing has ever measured AHDC1 binding AT-rich DNA. Proposing it would be exactly the defect being reported. |
| `GO:0000987 cis-regulatory region sequence-specific DNA binding` | "sequence-specific" is the claim under challenge. |
| `GO:0140588 chromatin looping` | Definition is SMC-driven loop extrusion. |
| `GO:0090310 negative regulation of DNA methylation-dependent heterochromatin formation` | Excluded by the paper's own H3K9me3/HP1α negative result. |
| `GO:0030216 keratinocyte differentiation` | Non-cell-autonomous; rescued by WT mesoderm; absent in primary keratinocyte mutants. |
| mouse metabolic terms from `PMID:37819197` | Mouse only; would need `ISO`/`ISS`; mechanism unknown. |
| `GO:0044030 regulation of DNA methylation` | **Obsolete**, `term_replaced_by: None`, `consider` → `GO:0030234` (an MF) and `GO:0040029`. `GO:0006306 DNA methylation` is obsolete too. `GO:0040029 epigenetic regulation of gene expression` is the live term whose definition explicitly includes "cytosine methylation of DNA", and is what I used. |

## 13. Sibling / paralog cross-check

`PTHR15617` has **682** proteins in InterPro's cached metadata, of which the
reviewed-member CSV holds **2** (0.3%) — human `Q5TGY3` and mouse `Q6PAL7`, both in
subfamily `PTHR15617:SF1`. There is no human paralog of AHDC1, so there is no sibling
review to cross-check against (the AADACL2/3/4 check is not applicable here). The
`eggNOG` group is `ENOG502QSFA`, and the only other protein named in the literature as
sharing a domain is REV3L via DUF4683 (`PMID:34950897` calls it "a conserved REV3L
domain"), which is a domain-level resemblance with no functional claim attached.

## 14. Review round: what the reviewer caught, and what I checked before conceding

`ai4c-reviewer` approved with five non-blocking items. Each premise was verified first.

**The off-by-one was real.** The PR body and the first history event said "5 NEW / 20
entries"; the file had **4 NEW / 19**. Cause: `GO:0006357` was planned as a NEW row and
implemented as the `proposed_replacement_terms` of a MODIFY, and the narrative count was
never re-derived. This is the campaign's most-confirmed lesson landing on me — a number
that does not add up is the bug report — and the tell was that I *wrote* the count from a
plan rather than deriving it with `grep -c '^- term:'` and `grep -o 'action: NEW'`.

Note the trap in the fix: acting on item 3 below **added** a fifth NEW row, so the file is
now 20 = 15 + 5 and the original claim reads as correct again. It was not correct when
made. Said explicitly in the reply and in the history record, because a number that quietly
becomes true is the easiest kind of correction to lose.

**The off-target quote was real.** The `GO:0001707` `GO_REF:0000107` row was supported by
*"Heterozygous or homozygous Gibbin mutants ... failed to survive past birth"*. Perinatal
lethality speaks to neither mesoderm formation nor to the circularity the row argues.
Replaced with the human scRNA-seq mesoderm result and the day-3 onset — which is the right
choice for this row specifically, because what needs evidencing is that the *target already
holds the term from this publication*. The `GO:0043589` Compara row carried the identical
quote and got a different fix: the mouse skin data (KRT14/KRT10 loss, reduced differentiated
layers), because on that row the donor's evidence genuinely is a distinct experiment. One
bad quote, two different right answers — worth noting, since the reflex is to apply one
replacement to both.

**`GO:0000785 chromatin`.** Checked before adding: enum-valid, and its ancestor closure
over `is_a,part_of` **does** contain `GO:0005694`, so it specialises the existing row rather
than competing with it. Added as a NEW `located_in` row on the same reference rather than
re-graining the `EXP` row, which reflects UniProt's curated Chromosome location and is not
wrong. Also added to both `core_functions` `locations`. The validator then cleared the two
"location term not reflected in existing_annotations" warnings that the core_functions-only
version had produced — i.e. the additive route was also the one the repo's own rules wanted.

**`core_functions` restructure.** The reviewer's objection was that entry 2 re-stated entry
1's activity and hung downstream developmental terms off it. Fixed by dividing the two
entries **by activity and by experiment**: entry 1 is the partner-facing arm (`GO:0003712`,
`GO:0006357`; proximity proteomics and epistasis), entry 2 the DNA-facing arm (`GO:0003682`,
`GO:0040029` moved here from entry 1, `GO:1902275`, plus the developmental outcomes;
ChIP-seq, methylation arrays, HiChIP). Entry 2 now states the causal distance explicitly:
mesoderm formation is the direct readout, skin morphogenesis is reached
non-cell-autonomously — the same argument used to decline `GO:0030216`.

**The `IPI` query was not an objection, and I did not concede it.** Coding `GO:0140297` off
the GATA3 epistasis instead was considered and rejected: the epistasis is a genetic result
about GATA3's *dependence on* AHDC1, which is IMP-shaped and would support a regulation
term, not a binding term. `IPI` on the proximity data with the labelling-radius caveat is
what matches the measurement. Recorded in the row rather than only in the PR reply.

**A sixth item, from the second (later dismissed) review, and the sharpest of them:** the
tagged-transgene caveat was *weighted one way for `GO:0003700` and another for
`GO:0003682`* and got only a trailing clause. That is a real inconsistency to answer,
because it is the **same experimental limitation** reaching two opposite conclusions — the
shape the campaign flags as "same author, same gene, two verdicts".

The asymmetry survives being made explicit, which is why it is now stated on both rows
rather than removed. Over-expression of a tagged chromatin protein distorts **which** sites
are occupied far more than **whether** the protein reaches chromatin at all: an
over-expressed protein samples weak and off-target sites that the endogenous one would not.
`GO:0003700` claims site specificity, so the limitation is load-bearing there.
`GO:0003682` claims only association, so it is secondary there. Two further facts limit it
on the `GO:0003682` side and are cited only there: the occupancy is **conditional** —
absent at day 0 and present at day 7 in the same cells with the same construct, which
over-expression alone would not reproduce — and an **independently generated** ENCODE
dataset in a different cell type recovers the same chromatin-state distribution, peak
number and target gene set. Neither rescues a specificity claim, which is why neither
appears on the `GO:0003700` row.

And the `GO:0003700` objection never rested on the construct anyway: all four arguments
there hold if the transgene were endogenous. The audit script now enforces that the
weighting is justified in **both** places, via an occurrence-count check, because a
file-presence check cannot express "stated on both sides of a comparison".

One factual note about the review itself: it ran with neither `uv` nor `just` available, so
its term-id and quote checks were manual against `cache/go/terms.csv` and the cached
publications. Its conclusions matched the local `just validate` result, but the `Build and
test` workflow is the authoritative signal.

## 15. Process

- Branch `paint/AHDC1` from `origin/main`; own worktree.
- Every supporting_text pre-verified with a normalising substring check before writing
  the YAML (34/34 candidates matched), then re-verified with the repo's
  `checkquotes` script including the duplicate-YAML-key and raw-vs-parsed reconciliation.
- `cache_lint` gated on its real exit status (`cmd >/dev/null 2>&1; echo $?`), run after
  merging `origin/main` as well as after my own edits.
