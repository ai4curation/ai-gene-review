# ADTRP (Q96IZ2) — review notes

Human ADTRP, androgen-dependent TFPI-regulating protein. HGNC:21214, chromosome 6, 230 aa,
`PE 1: Evidence at protein level`.

## Accession verified independently of the worklist

`projects/paint/human-no-IBA-simple.csv:409` reads `human,Q96IZ2,ADTRP`. Confirmed against
UniProt: `Q96IZ2` is `ADTRP_HUMAN`, reviewed (Swiss-Prot), 230 aa, gene name `ADTRP`
(synonym `C6orf105`), recommended name "Androgen-dependent TFPI-regulating protein".

**The worklist's "no-IBA" name is stale for this gene.** GOA carries **three IBA rows** —
`GO:0016787`, `GO:0042758` and `GO:0005901`, all `GO_REF:0000033`, assigned by GO_Central. Two
were placed 2025-11-27 and one 2026-05-28, i.e. after the list was drawn. Never read IBA status
off the filename.

## Row-count reconciliation, done before reviewing

```
GOA TSV data lines            27   (28 including header)
GOA TSV distinct lines        27
fetch-gene stub entries       26   <-- under-seeded by one
final review entries          27
```

The stub collapsed the **two `GO:0005515` rows** into one. They differ only in the WITH/FROM
partner (`Q6PL24` TMED8 and `Q96FZ5` CMTM7), which is exactly the documented
`GOAValidator.seed_missing_annotations` behaviour — its key is
`(GO id, evidence, reference, negated, qualifier)` and omits WITH/FROM. Both were restored so
each partner has its own verdict. The review is built from the TSV, not from the stub, with an
assertion that the counts match.

## The contested enzymatic identity, resolved

The two descriptions in the literature are **both correct and are annotated in different GO
aspects**, so the "conflation" this review was asked to look for is not present in GOA:

| claim | aspect in GOA | terms |
|---|---|---|
| hydrolyses FAHFAs | molecular function | `GO:0120573`, `GO:0016787` |
| regulates TFPI expression | biological process | `GO:0010628`, `GO:0030195` |

**"Regulates the expression of TFPI" is not annotated as a molecular function anywhere**, and
the vascular/thrombosis phenotypes are likewise confined to BP rows. That check comes back
negative and is worth recording as such.

### Which activity is measured, and at what granularity

Measured, in `PMID:27018888` (cached with `full_text_available: true`, read in full):

- ADTRP-transfected HEK293T membrane lysates hydrolyse FAHFAs and *not* other lipid classes —
  [PMID:27018888 "The membrane lysates of hAIG1- and hADTRP-transfected HEK293T cells showed
  negligible hydrolytic activity above a mock-transfected control proteome with the majority of
  tested lipid substrates, including common classes of (lyso)-phospholipids and neutral lipids"]
- both catalytic residues are required — [PMID:27018888 "The FAHFA hydrolase activities of AIG1
  and ADTRP were abolished by mutating their putative catalytic nucleophilic residues Thr-43 and
  Thr-47, respectively"] and [PMID:27018888 "We also tested the H134A mutant of AIG1 and H131A
  mutant of ADTRP and found that these proteins showed no detectable FAHFA hydrolase activity
  above a mock-transfected control"]
- substrate preference — [PMID:27018888 "AIG1 and ADTRP displayed a preference for FAHFAs with
  branching distal from the carboxylate head group of the lipids"]

The residues are in the UniProt feature table with experimental evidence, so the mechanism can be
cited from UniProt rather than from a provider narrative:
`FT SITE 47 /note="Important for catalytic activity" /evidence="ECO:0000269|PubMed:27018888"` and
the same at position 131. Sequence positions confirm Thr47 and His131. Both lie inside
`FT TRANSMEM` helices (47..67 and 120..140) — a hydrolase working inside the bilayer.

**Granularity is already optimal and RHEA-anchored.** `GO:0120573 FAHFA hydrolase activity` was
created **2026-03-14** and carries 12 RHEA cross-references; UniProt curates 12 catalytic-activity
lines for ADTRP (RHEA:52048 … RHEA:52101), each `ECO:0000269|PubMed:27018888`. The GOA IEA row
lists 11 of them. So this is the ADPRH/RHEA:14885 situation: an exact reaction-level anchor
exists and is in use. Nothing to sharpen.

### Reaction direction and substrate identity — checked, not assumed

The hint that a removing hydrolase gets annotated as if it added a group **does not apply here**:

- `GO:0120573`'s definition states the direction: "…yielding a free fatty acid and a hydroxy fatty
  acid".
- UniProt gives `PhysiologicalDirection=left-to-right` on all 12 reactions, i.e. hydrolysis.
- ChEBI settles the substrate question for `GO:0042758 long-chain fatty acid catabolic process`:
  the substrate **9-PAHSA(1-) `CHEBI:83670` is itself classified as a long-chain fatty acid
  anion** ("A long-chain fatty acid anion that is the conjugate base of 9-PAHSA"). So cleaving a
  FAHFA genuinely is the breakdown of a long-chain fatty acid, and `GO:0042758` names the right
  chemistry rather than being an inversion.

## The finding: a mechanism/substrate category error at one PAINT node

From the repo's own cached PAINT table, `interpro/panther/PTHR10989/PTHR10989-paint.tsv`:

| node | GO | aspect | IBD seeds | taxon | date |
|---|---|---|---|---|---|
| PTN000862533 | GO:0005783 | C | SGD:S000001182 | taxon:451864 Dikarya | 20251127 |
| PTN001659973 | GO:0016787 | F | Q9NVV5, Q96IZ2 | taxon:2759 Eukaryota | 20260528 |
| PTN001659973 | GO:0042758 | P | Q96IZ2, Q9NVV5 | taxon:2759 Eukaryota | 20251127 |
| PTN002591065 | GO:0005901 | C | Q96IZ2 | taxon:117571 Euteleostomi | 20251127 |

`PTN001659973` is **pan-eukaryotic** and seeded by exactly two human proteins, yet carries the
*root* of the hydrolase branch as its molecular function and a *four-step-deep* biological process.
It reaches 86 gene products: 40 Vertebrata, 25 invertebrate Metazoa, 14 Fungi, 5 Viridiplantae,
2 other Eukaryota.

### I got the explanation wrong on the first pass, and measurement corrected it

My first reading was that clade **heterogeneity** justified the general MF and therefore made the
specific BP unwarranted. That reasoning does not survive measurement.

Prompted by a sentence in the very paper I was citing — [PMID:27018888 "The HHpred search results,
however, uncovered a distinct set of uncharacterized AIG1/ADTRP-like proteins that possess the
conserved Thr and His residues and are found in non-mammalian eukaryotic organisms"] — I aligned
all 85 other recipients to ADTRP, requiring the aligned column to land on ADTRP's own annotated
SITE positions:

| clade | dyad Thr/His intact | of which ≥25% identity |
|---|---|---|
| Vertebrata | 39/39 | 39/39 |
| Metazoa (invertebrate) | 17/25 | 14/17 |
| Fungi | 11/14 | **0/0** |
| Viridiplantae | 4/5 | 1/1 |
| other Eukaryota | 2/2 | 2/2 |

Positive control: AIG1, whose catalytic residues are independently annotated as Thr43/His134,
scores dyad-intact at 36.5% identity, so the aligner recovers a known case.

### PTHR12242 vs PTHR10989 — the paper points at a *different* family, and it still exists

The sentence above continues "…(Panther family **PTHR12242**; members in insects, plants, protozoa,
and other non-vertebrates)", whereas this whole analysis works from **PTHR10989**. That is not a
discrepancy to explain away and **it is not a PANTHER renumbering** — I checked both, and both are
live and distinct:

| family | name | proteins | InterPro integration |
|---|---|---|---|
| `PTHR10989` | ANDROGEN-INDUCED PROTEIN 1-RELATED | 5163 | `IPR006838` |
| `PTHR12242` | OS02G0130600 PROTEIN-RELATED | 6117 | none |

ADTRP is in `PTHR10989`, subfamily `PTHR10989:SF17` (`ADTRP-uniprot.txt` `DR PANTHER` lines), and
`PTN001659973` is a node of that family. So the paper's remark describes a **sister set of
AIG1/ADTRP-like proteins in a separate family**, not the recipients of the node under review —
which is exactly why it was treated as a *lead* to go and measure rather than as an answer. Anyone
comparing the 2016 paper against `RESULTS.md` should not expect the two family ids to match.

**The dyad is broadly conserved — 73/85.** So heterogeneity is the wrong basis for the objection.
Note also that **all 14 fungal members fall below 25% identity**, where pairwise alignment
manufactures residue matches from noise: their dyad status is **undetermined, not negative**. An
absence of evidence, which is not evidence of absence.

**The corrected finding is sharper and is a category distinction, not a sloppiness claim:**

> A conserved catalytic dyad licenses an inference about catalytic **mechanism**, not about
> **substrate**. `GO:0016787 hydrolase activity` states mechanism only, so it is exactly scoped to
> what the residues support family-wide — the general MF is *well founded*.
> `GO:0042758 long-chain fatty acid catabolic process` is a **substrate-level** claim, and the
> substrate is established only for the four characterised animal members (human and mouse ADTRP
> and AIG1). The node propagates a substrate claim on evidence that can only support a mechanism
> claim.

The fix is asymmetric and cheap: move the process term to the vertebrate/mammalian subclade where
the seeds sit — PANTHER already has `PTN002591065` at Euteleostomi for exactly that purpose — and
leave the mechanism-level MF at Eukaryota. Filed as a `suggested_question` to PAINT.

This also matters for how the MF row was judged: because the MF is well founded at the node, it is
`KEEP_AS_NON_CORE` (true, but redundant on this gene against `GO:0120573`) rather than `MODIFY`.

### Reciprocal node question — benign answer, reported as a negative

"Which node's reach is exactly my gene set, and what did it give them?" `PTN002591065` covers 25
gene products which resolve to ADTRP orthologues in 25 **vertebrate** species and nothing else;
the paralog AIG1 is correctly excluded. Caveolae are a vertebrate structure requiring caveolins,
so the node's taxon scope (Euteleostomi) and the term agree. No defect. The one reservation is the
**relation**: the seeding evidence is a `located_in` IDA, and the propagation asserts
`is_active_in`, i.e. that catalysis happens in caveolae — which no assay has shown.

## The three non-PAINT routes — all three non-confirmations, with the reasons

1. **InterPro2GO.** The signature supplying `GO:0016020` is `IPR006838`, named **"ADTRP/AIG1"** —
   a *family-specific* signature, not a bare fold. Its interpro2go mapping is `GO:0016020` **and
   nothing else**: a cellular component, no molecular function, even though the family is now a
   characterised hydrolase family. Counting how its own reviewed members are curated: of 5788
   family proteins, **8 are reviewed (Swiss-Prot)** — 4 ADTRP, 2 AIG1, and **2 uncharacterised
   UPF0641 proteins** (`P38842` YHR140W, `Q96WV4` SPBPJ4664.05). So a quarter of its curated
   members are uncharacterised and the entry still declines to assert an activity. **This entry
   shows restraint** — the opposite of the `IPR012108` case where a majority of reviewed members
   are curated as catalytically dead while the entry still maps the activity.
2. **Bulk classification imports carrying TAS.** ADTRP has **no TAS row at all**. Reference
   projection test, fully paginated: `PMID:27018888` 8 annotations / 2 entities;
   `PMID:21868574` 10 / 2 (ADTRP and TFPI `P10646`); `PMID:28341552` 22 / 4 (ADTRP, AKT1, MIA3,
   PIK3R3). `PMID:32296183` has **85343** annotations across GOA, so its entity count is recorded
   as **UNAVAILABLE** rather than approximated from one page.
   `PMID:27018888` does give its 2 entities identical term sets — the projection signature — but
   the paper individually mutated and individually assayed **both** proteins, so this is parallel
   per-protein curation, not one finding projected across a set. No ACTR8-style phenotype spread:
   the two multi-entity references give each entity a *different* term set.
3. **ARBA rules.** No WITH/FROM on any ADTRP row names an `ARBA…` rule. The two automatic routes
   present are `GO_REF:0000044` (Swiss-Prot subcellular-location mapping, naming
   `UniProtKB-SubCell:SL-0039`) and `GO_REF:0000116` (Rhea mapping, naming 11 reaction ids). Both
   name their source explicitly and neither grants an activity on a family's *name*.

## Measured-and-absent vs unmeasured, kept apart

Nothing on this gene earns a `REMOVE`. To be explicit about which category each doubt falls in:

- **Measured and absent:** ADTRP is inactive against phospholipids, lysophospholipids and mono-,
  di- and triglycerides — measured, and correctly *not* annotated. No action needed.
- **Unmeasured:** whether the hydrolase activity occurs in caveolae; whether any non-animal family
  member hydrolyses anything; whether the TFPI effect requires catalysis. These attract
  `KEEP_AS_NON_CORE` and `suggested_experiments`, never `REMOVE`.

## `GO:2000402` is the wrong leukocyte lineage — sibling, not ancestor

`PMID:28341552` is annotated `GO:2000402 negative regulation of lymphocyte migration` (IMP,
BHF-UCL). Cell-type words in the cached abstract: **monocyte 4, lymphocyte 0, leukocyte 0**. The
phenotype is [PMID:28341552 "Knockdown of ADTRP expression by siRNA promoted oxidized-LDL-mediated
monocyte adhesion to ECs and transendothelial migration of monocytes, inhibited EC proliferation
and migration, and increased apoptosis"].

Both closures were fetched before calling this a granularity problem:

- `GO:2000402` (lymphocyte) is **not** an ancestor of `GO:2000438` (monocyte extravasation)
- `GO:2000438` is **not** an ancestor of `GO:2000402`
- verified common ancestors: `GO:0071676` (mononuclear cell), `GO:0002686` (leukocyte)

**Neither contains the other, so the term is wrong, not imprecise.** Monocytes are myeloid
mononuclear phagocytes; lymphocytes are lymphoid. `MODIFY` → `GO:2000438 negative regulation of
monocyte extravasation`, which matches "transendothelial migration of monocytes" precisely. The
full text is **not** cached, so if it does contain a lymphocyte migration assay the conservative
resolution is `GO:0071676`, a verified ancestor of both that asserts strictly less. Either way
nothing is lost: the leukocyte-level claim is separately annotated from the same paper as
`GO:0002686`. Raised as a question to BHF-UCL rather than asserted as curator error.

## `GO:0005886` from `PMID:27018888` — a reference-attribution problem, not a GO error

The cached full text of `PMID:27018888` (`full_text_available: true`) contains **no localisation
experiment**. Occurrence counts, with positive controls from the same file and the same call
pattern so a zero cannot be a broken scan:

| probe | count | | control | count |
|---|---|---|---|---|
| `plasma membrane` | 0 | | `membrane lysates` | 9 |
| `cell surface` | 0 | | `membrane fraction` | 3 |
| `immunofluoresc` | 0 | | `transmembrane` | 29 |
| `confocal` | 0 | | `hek293t` | 36 |
| `localization` | 0 | | `fahfa` | 67 |

What that paper shows is recovery in the membrane fraction plus six topology predictors —
[PMID:27018888 "and found that these programs consistently predicted that both the conserved Thr
and His residues of AIG1 and ADTRP were located within transmembrane domains of these proteins"].
That supports `GO:0016020 membrane`, which the same paper is separately and correctly cited for by
IDA — not `GO:0005886`.

UniProt's `SUBCELLULAR LOCATION` line cites **both** `PubMed:21868574` and `PubMed:27018888` for
"Cell membrane", and GOA has split that into two EXP rows. So the row is a faithful reflection of
UniProt; the question belongs upstream. Filed as a UniProt correction request. **No GO action**:
the term is correct for ADTRP on `PMID:21868574`'s own evidence, and inventing a GO action to
express a reference-attribution concern would be an over-annotation of the opposite sign.
Supplementary figures are not in the cache, so the scan is scoped to the cached full text.

## `GO:0005515` — one screen counted three ways (third instance in this campaign)

IntAct returns 10 interactions for `Q96IZ2`. Both GOA rows come from `PMID:32296183` (HuRI), and
each partner is logged under three *sub-methods of one screen*:

| partner | methods | distinct methods | distinct experiments |
|---|---|---|---|
| TMED8 | two hybrid array, two hybrid prey pooling approach, validated two hybrid | 3 | 1 |
| CMTM7 | two hybrid array, two hybrid prey pooling approach, validated two hybrid | 3 | 1 |

All yeast two-hybrid, MI-score 0.56, host *S. cerevisiae*. **This is what UniProt's `NbExp=3` is
counting** — not three independent experiments. No orthogonal assay, no follow-up anywhere in the
ADTRP literature. ADTRP is a six-pass membrane protein whose loops are 13–22 residues, a poor Y2H
substrate.

Partner-accession discipline, reported including the negative: **both partners resolve to reviewed
canonical Swiss-Prot entries with matching lengths** — `Q6PL24` TMED8_HUMAN 325 aa and `Q96FZ5`
CKLF7_HUMAN 175 aa, each identical to the canonical entry for its symbol. No TrEMBL/ORFeome
substitution here, unlike the ACRV1 case. `MARK_AS_OVER_ANNOTATED`, not `REMOVE`: nothing refutes
the interactions, they are simply unreplicated.

IntAct also holds S100B and CREB3 (Y2H, MI 0.37) and VTN. S100B is interesting because a mouse
study reports Adtrp–S100b binding driving thermogenesis, but that is mouse and not in human GOA,
so it is left out of the review body.

## Logical-opposite cross-product — negative

Computed from the GOA TSV alone: 8 positive/negative regulation terms, **0 opposed pairs on the
same base process**, so no reference-set intersection to inspect. No `GO:0120162`/`GO:0120163`-style
defect here.

## affinage record — recall checked rather than assumed, and it did well

`gates_passed: True`, 12 citations, `faith_pct: 100.0`. Verified independently:

- all 12 ids are **numeric PMIDs** — no `PMID:bio_10.1101_…` bioRxiv ids in a PMID-shaped field;
- all 12 resolve to papers **genuinely about ADTRP** — no gene-symbol collision of the ADPRH kind;
- **none** carries a retraction, erratum or expression of concern (checked `PublicationType` and
  `CommentsCorrections/RefType` on each record);
- it **surfaced two papers absent from GOA** that this review uses: `PMID:32152231` (the in vivo
  Adtrp-knockout FAHFA demonstration) and `PMID:32445923` (POU1F1).

So on this gene the provider's recall was genuinely useful — worth recording, since the campaign
has mostly measured its misses.

One defect to note: its own **GO grounding block is wrong** — it lists
`GO:0140098 catalytic activity, acting on RNA` for a lipid hydrolase. Not used. Consistent with
the standing rule, no affinage sentence carries a mechanistic claim in the review; the POU1F1 lead
it provided is cited alongside the primary `PMID:32445923` quotes, which carry the claim.

## What TFPI regulation is, mechanistically — so no MF is inferred from it

`PMID:32445923` resolves it: the DNA-binding protein is **POU1F1**, not ADTRP —
[PMID:32445923 "Deletion of POU1F1-binding site or knockdown of POU1F1 expression abolished
ADTRP-mediated transcription of TFPI."] and [PMID:32445923 "ChIP and EMSA demonstrated that POU1F1
binds to the ADTRP response element."]. ADTRP sits upstream of a transcription factor. That is why
`GO:0010628` is retained as a process and **no DNA-binding or transcription-factor molecular
function is proposed**.

## Ontology gap

GO can express FAHFA hydrolysis as a molecular function (`GO:0120573`) but has **no
biological-process counterpart** — a QuickGO text search for "FAHFA" returns exactly one term.
That absence is why a pan-eukaryotic node has to reach for `GO:0042758`. Proposed
"fatty acid ester of hydroxy fatty acid catabolic process" under `GO:0042758`, with the
counter-argument recorded rather than suppressed: GO may reasonably decline it on the grounds that
a single-step hydrolysis is adequately covered by the molecular function.

## Sibling/paralog cross-check — reported as a null

`genes/human/AIG1/` does **not** exist on `main`, so no merged sibling review was available to
check for divergent verdicts on identical rows. This matters, because **AIG1 (`Q9NVV5`) carries the
byte-identical `GO:0016787` and `GO:0042758` IBA rows from the same node `PTN001659973` with the
same WITH/FROM**, plus its own `GO:0120573` IMP and `GO:0016020` IEA from `IPR006838`. AIG1 is the
obvious next gene, and whoever takes it should reach the same verdicts on those two IBA rows or
explain the divergence.

## Reproducibility

Every computed number above is produced by
`ADTRP-bioinformatics/analyze_adtrp_propagation.py` → `results.json` + `RESULTS.md`. A fresh run
reproduces the committed `RESULTS.md` apart from the timestamp line (verified by diff). The review
YAML is generated by `ADTRP-bioinformatics/build_review.py`, which asserts every quote is a
whitespace-normalised substring of its cited source, asserts one entry per distinct GOA row,
asserts each row's quotes actually mention the row's subject, and dumps with aliases disabled so
no two rows can share a quote object. All five of its guards were break-tested; the mutation for
each was asserted non-no-op first.

## Review round 1 (PR #2338) — what changed

Two blocking items, both real and both mechanical; no verdict changed.

1. **`PMID:32152231` appeared four times in `references:`.** Root cause found and fixed at the
   generator, not the output: `build_review.py` loads **its own previous output** as the starting
   document and then appended the extra references, so every re-run appended again — I had run it
   four times. Replaced the appends with a **merge keyed on reference id**, which makes the step
   idempotent (three consecutive runs are now byte-identical; they were not before). References
   went 14 → **11**, matching the reviewer's count.

   Note the guard I wrote first was **vacuous**: I asserted uniqueness *after* building the list
   from a dict, where duplicates are impossible by construction, so the assertion could never
   fire. A break-test caught that — the mutation that re-introduced the bug shape passed cleanly.
   Restructured into two checks that can actually fail: a **detector on the loaded input** (run it
   against the pushed commit and it reports exactly `['PMID:32152231']`) and a **post-condition in
   its own function** so an append-shaped regression is caught (break-tested: fires, rc=1).
   This is the "unreachable check that reads as coverage" mode — worse than no check.

2. **`source_status: SUPPORTS_SOURCE_BUT_NOT_TARGET` on the `GO:0042758` IBA row** contradicted its
   own `action: ACCEPT`, `root_cause: NO_FAILURE_CORE` and comment. The schema reads that value as
   "propagation to the target is unsafe", but the target here is human ADTRP, which has its own
   IMP. Changed to `SUPPORTS_TRANSFER`; the over-reach-to-other-recipients concern stays in the
   `comment` and in `suggested_questions`, which is where a nuance belongs when the enum has no
   value for it.

Non-blocking suggestions, all adopted except two:

- **Truncated quote** in `knowledge_gaps` provenance (ended mid-word at "…protei") replaced with the
  full sentence, which is also more probative for the gap.
- **`PTHR12242`** written up above — but *not* as "PANTHER renumbered", which I checked and it did
  not: both families are live and distinct with different names and protein counts.
- **`GO:0016020` dropped from `core_functions.locations`** as a verified ancestor of `GO:0005886`
  that adds nothing there. Its `existing_annotations` rows keep the claim.
- **Declined `MODIFY` on `GO:0005886` EXP / `PMID:27018888`**, for a mechanical reason as well as a
  judgement one: the repo validator requires all rows on one term to share an action, and the other
  two `GO:0005886` rows are correctly `ACCEPT`, so a lone `MODIFY` would trip
  same-term-same-action while asserting the gene is not at the plasma membrane. Instead the
  **summary was reworded to lead with the acceptance** and carry the attribution caveat second, so
  the row no longer reads like a `MODIFY`. The concern stays where it is actionable: a UniProt
  correction request.
- **Declined adding `GO:0071676` as a second `proposed_replacement_terms` entry** on `GO:2000402`.
  The abstract directly supports the monocyte reading, and two replacement terms would make the
  machine-readable intent ambiguous rather than conservative. The fallback stays in the `reason`
  and in the `suggested_question` addressed to BHF-UCL, which is who would apply it.

**One further item I found by running the standing "does a structured field state what the prose
refuses" check across the whole file:** `GO:0009986 cell surface` was `ACCEPT`, and `ACCEPT` is
defined in the schema as retaining the annotation *as representing the core function* — while its
reason hedges ("retained on curator authority… the cached abstract does not state it") and the term
is deliberately absent from `core_functions.locations`. Changed to `KEEP_AS_NON_CORE`. Unlike
`GO:0016020`, cell surface is **not** an ancestor of plasma membrane (verified, separate branch), so
it is an independent claim, and the catalytic residues sit inside the bilayer rather than on the
external face. After the change the only `ACCEPT` term absent from `core_functions` is `GO:0016020`,
which is a verified ancestor of a core location — coherent by construction.

## Review round 2 (PR #2338) — a regression introduced by the round-1 fix

The round-1 de-duplication was correct on the thing it deduped and **silently dropped payload
attached to two *other* references**: `PMID:32445923` and the affinage record came back with no
`reference_review`. What was lost was exactly the reviewer judgement that field exists to hold and
that no format validation can catch — the **POU1F1-is-the-DNA-binding-protein** note, and the
**affinage caveat that its own GO grounding block is wrong (`GO:0140098` catalytic activity acting
on RNA, for a lipid hydrolase)**. Restored verbatim from the round-1 commit.

**Why every gate missed it:** the ids were all still correct. `references` was 11/11 distinct, the
duplicate detector was clean, `checkquotes` was clean, `just validate` was clean. An id-level check
cannot see payload loss, and that is the general shape: *a de-duplication that rewrites the carrier
drops whatever was attached to the duplicates.*

**And the first two attempts at a guard for it did not work, which is the part worth recording.**

1. Attempt 1 asserted every non-`GO_REF` reference has a `reference_review`. It passed — and was
   **unreachable**, because the builder loads its own previous output, so the payload was being
   silently carried over from disk. A guard that cannot fail is not protection.
2. Attempt 2's break-test *also* failed to fire, for the same reason, and an earlier mutation had
   failed for the wrong reason entirely (a `NameError` before the check was reached — a mutation
   coarser than the claim).
3. So the **shape** changed rather than the predicate: the builder now **strips any inherited
   `reference_review` when loading**, so reviewer judgement can only come from one place, the
   `reviews` dict. That makes the loss impossible by construction *and* makes the assertion
   load-bearing.

Break-tested both directions after the restructure: dropping one `reviews` entry (ids intact, code
valid) fires with `non-GO_REF references lacking reference_review: ['PMID:32445923']`, and the
control run on the corrected file stays clean. Run against the shipped defect (commit `ec41395a1`)
the check reports exactly the two affected references.

Three rounds have now produced three forms of one predicate, which is the signal to stop iterating
on it — hence the structural fix rather than a fourth assertion.
