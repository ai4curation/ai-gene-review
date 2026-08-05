# ADAMTSL1 (Q8N6G6, punctin-1) — review notes

Human ADAMTSL1, PAINT + affinage campaign. GOA record is unusually small: **4 rows**
(1 IEA + 3 TAS), no IBA, no IPI, no MF annotation of any kind.

## 1. Domain content: the "-like" really does mean non-catalytic

Established from the UniProt feature table before reading any narrative source, because the
campaign has twice shipped an inverted premise about catalysis.

The FT block of `ADAMTSL1-uniprot.txt` lists, over the 1762-aa precursor: a signal peptide
(1–28), nine annotated TSP type-1 repeats, four Ig-like C2-type domains, and a C-terminal
PLAC domain. There is **no metalloprotease domain, no disintegrin-like domain, no
prodomain, and no zinc-binding site feature**. There is no `CATALYTIC ACTIVITY` comment and
no EC number. UniProt states it outright
[file:human/ADAMTSL1/ADAMTSL1-uniprot.txt "lacks the metalloprotease and disintegrin-like domains which are"],
and the primary literature says the same in two places
[PMID:11805097 "Punctin lacks the pro-metalloprotease and the disintegrin-like domain typical of this family but contains other ADAMTS domains in precise order including four thrombospondin type I repeats."]
and
[PMID:28722276 "it also contains a family of seven ADAMTS-like proteins (ADAMTSL family) comprising an ADAMTS ancillary domain but lacking the protease domain and thus, enzymatic activity"].

So the lead in the task brief holds for this gene, and it is established from the entry's own
feature table rather than from the family name.

The **ADAMTS spacer region** named in the review `description` is *not* an FT DOMAIN feature;
it comes from `DR   Pfam; PF05986; ADAMTS_spacer1; 1.` and `DR   InterPro; IPR010294;
ADAMTS_spacer1.`. Sourced in the review's UniProt reference rather than left as an unattributed
claim.

Pfam/PROSITE counts differ from the FT list (PROSITE `TSP1` 9, SMART `TSP1` 13, Pfam
`TSP1_ADAMTS` 11) — the field's usual count for the full-length protein is **thirteen** TSRs
[PMID:28722276 "which contains thirteen thrombospondin type 1 repeats (TSRs), four Immunoglobulin-like C2-type domains and a single PLAC (protease and lacunin) domain in its full-length form (1762 amino acids) and four TSRs in a short splice variant named punctin-1 (525 amino acids)"].
Nothing in the review depends on the exact repeat count.

## 2. The peptidase error IS present — but in UniProt's keywords, not in GOA

`Q8N6G6` carries **`KW-0378 Hydrolase`** (Molecular function category), which generates
[file:human/ADAMTSL1/ADAMTSL1-uniprot.txt "GO:0016787; F:hydrolase activity; IEA:UniProtKB-KW."]
in the entry's own GO cross-reference list
[file:human/ADAMTSL1/ADAMTSL1-uniprot.txt "Extracellular matrix; Glycoprotein; Hydrolase; Immunoglobulin domain;"].

This is contradicted **inside the same entry** by the CAUTION comment quoted above, and there
is no reaction anywhere in the record to support it.

It is also anomalous within the family. Of the six human ADAMTS-like proteins, only ADAMTSL1
and THSD4 carry the Hydrolase keyword; ADAMTSL2, ADAMTSL3, ADAMTSL4 and ADAMTSL5 carry the
identical CAUTION about the missing metalloprotease domain and **no** MF keyword. None of the
six has a CATALYTIC ACTIVITY comment. Computed in
[file:human/ADAMTSL1/ADAMTSL1-bioinformatics/RESULTS.md "Entries with a CATALYTIC ACTIVITY comment: none."].

**The important curation fact: this never reached GOA.** `GO:0016787` is absent from
`ADAMTSL1-goa.tsv` and from QuickGO, because keyword-derived annotations (`GO_REF:0000043`)
were withdrawn for cellular organisms. So the defect is live in UniProt and invisible in GO.
It is reported in `suggested_questions` as a UniProt correction to file, not as an
`existing_annotations` row, because reviewing rows that GOA does not carry would break the
row-count reconciliation.

Two other places the same conflation shows up, worth separating because they have different
standing:

- **PANTHER's family GO-slim.** `geneinfo` for Q8N6G6 returns `GO_SLIM_MF: GO:0004222`,
  `GO_SLIM_BP: GO:0006508`, and protein class `PC00153 metalloprotease`. This is *not* a
  per-gene judgement — the identical slim block is returned for every member queried,
  including ADAMTS5 (a real protease) and ADAMTSL2 (which carries an explicit
  `NOT|enables GO:0004222` in GOA). It is the family summary and it is not negation-aware.
  Do not cite it as PANTHER calling ADAMTSL1 a protease.
- **The primary literature.** PMID:30714143 proposes
  [PMID:30714143 "We hypothesize that mutations in ADAMTSL1 cause failure to cleave aggrecan in the condylar cartilage, and that leads to overgrowth of the mandible."]
  — a mechanism that requires a proteolytic activity ADAMTSL1 does not have. It is labelled a
  hypothesis by its authors. The affinage record softens it to "aggrecan cleavage regulation",
  which is a different and weaker claim than the paper makes; neither is annotatable.

**InterPro2GO got this right.** `IPR013273 ADAMTS/ADAMTS-like` is the only one of ADAMTSL1's
fourteen InterPro entries with a GO mapping, and it maps to `GO:0030198` alone — no peptidase
term — even though the signature spans the catalytic ADAMTS proteases. That is the correct
treatment of a signature covering a mechanistically heterogeneous family.

## 3. PAINT knows catalysis was lost on this branch, and says so on one gene out of six

The cached PAINT table for the family contains two *negated* rows:

```
PTHR13723 PTN002673039 GO:0004222 F IKR true PANTHER:PTN000347317
PTHR13723 PTN002673039 GO:0006508 P IRD true PANTHER:PTN000347317
```

`IKR` (inferred from key residues) and `IRD` (inferred from rapid divergence) at node
`PTN002673039` block metalloendopeptidase activity and proteolysis from propagating below it.
In GOA that loss surfaces as exactly one annotation — ADAMTSL2's `NOT|enables GO:0004222`
IBA — and on no other ADAMTS-like member. ADAMTSL1 gets neither the positive term (good) nor
the explicit negation (a missed opportunity: the NOT is the machine-readable form of the
CAUTION comment UniProt already writes).

## 4. The headline finding: ADAMTSL1 is the only human family member with no `GO:0031012`

PAINT holds `GO:0031012 extracellular matrix` as an IBD at node `PTN000347317`. Census over
all 26 human members of PTHR13723:

- **24 of 26** receive it by IBA from that node.
- PAPLN is the other member without the IBA. I first wrote this off as PAINT declining to
  overlay an existing direct annotation, which is wrong: PAPLN's only `GO:0031012` rows are
  **IEA and TAS**, neither experimental, so redundancy suppression cannot be the reason. The
  concurrent ADAMTSL5 review (PR #2305) sharpens it further — three PAPLN orthologs (fly
  `Ppn`, mouse `Papln`, worm `mig-6/ppn-1`) are themselves seeds at that node. PAPLN is a
  second coverage gap, not an explained omission. The script now derives this rather than
  asserting it.
- **ADAMTSL1 has no `GO:0031012` annotation of any kind, from any evidence code.**

And the gap is species-specific, not subfamily-specific: **mouse Adamtsl1 (Q8BLI0), same
PANTHER subfamily SF157, does receive the IBA from `PTN000347317`**, plus three HDA rows from
matrisome proteomics. Full table in
[file:human/ADAMTSL1/ADAMTSL1-bioinformatics/RESULTS.md "Members with no `GO:0031012` annotation of any kind: ADAMTSL1."].

UniProt records the human localisation as experimentally supported by three papers
(`ECO:0000269|PubMed:11805097`, `PubMed:17395588`, `PubMed:19671700`), and independent human
evidence exists:

- [PMID:11805097 "In transfected COS-1 cells, punctin is deposited in the cell substratum in a punctate fashion and is excluded from focal contacts."]
  — the observation the protein is named for. Caveat: recombinant epitope-tagged protein in a
  heterologous cell line.
- [PMID:24281761 "we identified the extracellular matrix protein ADAMTS-like protein 1 (ADAMTSL1) as a direct MMP10 substrate"]
  — endogenous ADAMTSL1 detected in human **fibroblast secretomes** by TAILS degradomics. This
  is the stronger localisation evidence of the two: native protein, native compartment.

So the one gene in the family whose ECM residence is *directly* shown in human cells is the
one gene in the family with no ECM annotation. Proposed as a `NEW` row (`located_in
GO:0031012`, IDA, PMID:11805097) rather than left for PAINT, because the human primary
evidence stands on its own.

## 5. `GO:0030198` extracellular matrix organization (the one IEA)

**KEEP_AS_NON_CORE**, not ACCEPT. The first draft accepted it and rested the acceptance partly
on the annotation being "well-constructed and unrefuted", which the PR reviewer correctly
identified as absence of contradiction rather than positive support. There *is* positive
support, but all of it is family-level:

- The mapping is well-constructed (§2): `IPR013273` → `GO:0030198` only.
- `GO:0030198` is the term the heterogeneous family agrees on. Catalytic ADAMTS members reach
  it by proteolysis; ADAMTSL2/ADAMTSL4/THSD4 reach it non-catalytically through fibrillin
  microfibril assembly. So the term does **not** depend on the domain ADAMTSL1 lacks, and it
  is the correct level of generality rather than a granularity failure.
- PAINT reached the same term independently: `GO:0030198` is an IBD at `PTN000347317` seeded
  by **14 gene sources** (11 mouse, 2 fly, 1 worm), and it propagated by IBA to 22 human
  members of the family, three of them ADAMTS-like (ADAMTSL2, ADAMTSL4, THSD4). Note the
  seed count is 14, not the 15 you get by counting WITH/FROM tokens on the derived IBA rows:
  GOA appends the PANTHER node itself to that field. Both figures are now **computed** by
  `check_family_propagation.py` rather than counted by eye: the 14 in RESULTS.md section 4
  (IBD seed composition) and the 22 in section 1 (a second census pass over `GO:0030198`,
  added after the PR reviewer pointed out the script censused only `GO:0031012`).
- But there is **no ADAMTSL1-specific evidence for it**, and the group that discovered the
  protein says so:
  [PMID:28722276 "The function of punctin-1 in tissues is currently unknown, however, by analogy with other family members (Apte 2009; Dubail and Apte 2015; Hubmacher and Apte 2015), there is a strong possibility that it mediates the assembly and turnover of extracellular matrix at the affected sites."]

Kept on those three grounds, with the gap recorded in `knowledge_gaps`. Being present in the
ECM and being an MMP10 substrate places ADAMTSL1 in ECM remodelling; neither demonstrates
that it organises the matrix. So the term stays, but it is not asserted as this gene's core
function, and `core_functions` deliberately carries only `locations: GO:0031012` — the one
claim the gene's own data establishes.

### Divergence from the concurrent ADAMTSL5 review, and a premise that turned out false

PR #2305 (ADAMTSL5) marks the **identical** InterPro `GO:0030198` IEA
`MARK_AS_OVER_ANNOTATED`. I was told the two positions could both stand because ADAMTSL1 has
the `GO:0030198` IBA and ADAMTSL5 does not. **That premise is false**, and #2305's own table
says so: ADAMTSL1 is `–` in its `GO:0030198` column. My census agrees — the IBA from
`PTN000347317` reaches only ADAMTSL2, ADAMTSL4 and THSD4 within the ADAMTS-like branch.
ADAMTSL1 and ADAMTSL5 hold the InterPro IEA and nothing else, i.e. **identical evidentiary
positions**, and if anything ADAMTSL5 has *more* gene-specific matrix evidence (its own IDA
to `GO:0031012`, plus microfibril and heparin binding). The divergence therefore cannot be
justified per gene; it is about where the family draws the KEEP_AS_NON_CORE /
MARK_AS_OVER_ANNOTATED line, and it is filed once in `suggested_questions`. The script now
asserts the parity so the comparison cannot go stale.

One asymmetry worth recording, raised by the PR reviewer: for `GO:0030198` the IBA misses
4 of 26 human members (ADAMTSL1, ADAMTSL3, ADAMTSL5, PAPLN), against 2 of 26 for
`GO:0031012`. So "coverage gap" is a weaker reading for `GO:0030198` than it is for the
headline `GO:0031012` finding, and this review does not lean on it — the claim made about
`GO:0030198` is only that the IBD node sits above ADAMTSL1, with the propagation pattern
itself filed as a question rather than argued as a defect.

Where the two reviews *agree*: ADAMTSL1 has no IBA at all (#2305 flagged this as worth
checking against my branch — no discrepancy, my review reports the absence, never IBA
support), and absence of an IBA at an incoherently-propagating node is a coverage gap rather
than a curatorial judgement. My headline uses the absence exactly that way.

## 6. The `GO:0005788` ER lumen rows (three of them)

All three are true and all three say the same thing. ADAMTSL1's TSRs are O-fucosylated by
POFUT2 and extended by B3GLCT in the ER lumen, and this is required for export
[PMID:17395588 "Mutation of the putative modified Ser/Thr residues in TSR2, TSR3, and TSR4 led to significantly decreased levels of secreted punctin-1."],
with C-mannosylation acting in the same quality-control step
[PMID:19671700 "Together, these modifications appear to provide a quality control mechanism for punctin-1 secretion."].

Reasons for `KEEP_AS_NON_CORE` rather than `ACCEPT`:

- The ER lumen is a biosynthetic transit compartment; ADAMTSL1 acts in the ECM.
- The three rows are one statement from three reactions of one Reactome pathway, and
  `R-HSA-6785565` is a **FailedReaction** ("Defective B3GALTL does not transfer glucose to
  O-fucosyl-proteins") modelling the Peters-plus disease state — so the third copy is derived
  from a reaction that by construction does not occur.
- Projection check: each of the three Reactome references annotates ~9 gene products with the
  same three terms (`GO:0005788`, `GO:0005789`, plus the enzyme's activity). That is
  set-membership projection from a pathway participant list, not nine independent findings.

**Sibling divergence, declared.** The merged ADAMTSL4 review resolved the *identical* three
rows as `ACCEPT`, but its own reason reads "This localization reflects its secretory pathway
transit, not a functional localization" — substantively the same judgement, encoded with a
different action. Flagged in `suggested_questions` for harmonisation rather than silently
diverging.

## 7. Isoforms — the short form is punctin-1, not the long one

The task brief had this the wrong way round, so stating it plainly: **punctin-1 is the SHORT
splice variant** (525 aa, UniProt `Q8N6G6-1`), and the canonical displayed sequence is the
long isoform 3 (1762 aa, `Q8N6G6-3`)
[PMID:28722276 "four TSRs in a short splice variant named punctin-1 (525 amino acids)"].
UniProt applies the AltName "Punctin-1" at entry level, which is where the confusion comes
from; the literature uses it for the short form.

This matters because **essentially every ADAMTSL1 experiment was done on isoform 1**:

- the 2002 purification, rotary shadowing, Edman sequencing, glycosylation analysis and
  punctate substratum deposition (mass spectrometry range 28–525);
- all O-fucosylation and C-mannosylation site mapping and every secretion mutant
  (Trp36/39/42, Trp385, Trp445, Thr312, Ser391, Thr451 — all within residues 1–525);
- the Trp42Arg disease-variant secretion assay, explicitly:
  [PMID:28722276 "A plasmid construct for full-length ADAMTSL1 is presently unavailable."]

`isoform: Q8N6G6-1` is therefore set on the proposed `GO:0031012` row to record *what was
tested*, per CLAUDE.md's isoform-tracking convention — not to assert the localisation is
isoform-restricted. It almost certainly is not: isoforms 1–4 all retain the signal peptide.
Isoforms 5 and 6 delete residues 1–1299 including the signal peptide (`VSP_039322`) and so
would not enter the secretory pathway at all, and isoform 5 is flagged as NMD-prone; that
distinction is recorded in `functional_isoforms`.

**Minor tooling bug found:** `fetch-gene` seeded `alternative_products` with isoform 5's
`sequence_note` as `VSP_039322, VSP_039329, VSP_039330,` — the trailing `VSP_039331` was
dropped because the UniProt `CC` block wraps mid-list. Corrected by hand in the review YAML.

## 8. Checks run, including the ones that came back negative

- **Retractions / errata / expressions of concern** — all twelve PMIDs relied on were checked
  via each article's own `CommentsCorrections` record (a publication-type search does not see
  Publisher Corrections). **None flagged.**
- **IntAct / partner resolution** — 16 interaction records for Q8N6G6, but they reduce to
  **seven distinct protein partners** (ACOX1, B3GLCT, WDCP, FBN2, RSPRY1, FHL2, GRN), each
  reported twice because BioPlex 2.0 (PMID:28514442) and BioPlex 3.0 (PMID:33961781) are the
  same anti-tag co-IP pipeline; every record is MI-score 0.35 in over-expressing HEK293T, with
  no orthogonal assay. One further AP-MS hit (LPAR1, PMID:40205054, U2OS). Several partners are
  cytosol- or peroxisome-facing (FHL2, ACOX1) and so compartment-implausible for a
  signal-peptide protein. **GOA carries zero `GO:0005515` rows for ADAMTSL1, and none of this
  should be imported.** Two hits are worth keeping as hypotheses only: B3GLCT is the enzyme
  that glucosylates ADAMTSL1's O-fucosylated TSRs (so the "interaction" is an expected
  enzyme–substrate encounter in the ER), and FBN2 would be the first fibrillin link for this
  family member.
- **Complex/reference projection check** — applied to the Reactome references (§6). Positive:
  they are projections. Not applicable to a literature reference here, since no experimental
  GOA row exists.
- **Sibling-paralog consistency** — ADAMTSL4's merged review checked; divergence on the ER
  lumen action declared (§6).
- **Downward-MODIFY check (the ACRV1 pattern)** — no IBA rows exist on ADAMTSL1, so there is
  no propagation landing above its donor. Negative, by absence of the row class.
- **Marker-vs-function check** — PMID:35115729 and PMID:39880678 use *Adamtsl1* purely as a
  transcriptional marker of a mouse Pmp2+/Cldn14+ myelinating Schwann cell subtype
  [PMID:35115729 "including a subtype characterized by expression of Pmp2, Adamtsl1 and Cldn14 that preferentially myelinates motor axons"].
  PMID:39880678 ablates the **cell population**, not the gene, so its large-caliber-axon
  phenotype is a property of the cell type. Nothing annotatable to ADAMTSL1; deliberately not
  proposed.
- **Worm orthologue** — MADD-4 is a secreted midline guidance cue acting through UNC-40/DCC
  (PMID:22014523), but that paper itself declines to extend it:
  [PMID:22014523 "The biological role of MADD-4 orthologs, including ADAMTSL1 and 3 in mammals, is unknown."]
  Not carried into any human annotation.
- **Chondrosarcoma** — PMID:24634412 reports ADAMTSL1 as a Hedgehog-responsive gene that
  "regulates chondrosarcoma cell proliferation". This is the only gene-specific functional
  perturbation in the ADAMTSL1 literature, so it is now adjudicated **in the review file**
  with a `reference_review`, not only here. Declined on three grounds: the cached record is
  abstract-only and gives no direction, so neither `GO:0008284` nor `GO:0008285` can be
  chosen; the assay is a cancer cell line with no normal-physiology counterpart; and a
  proliferation phenotype narrows neither recorded gap, since it identifies no molecular
  function and says nothing about matrix organisation. It does mean the review's "nothing is
  known" claim must be stated precisely — no molecular function and no matrix-organisation
  evidence, rather than no functional observation of any kind. `PMID:39880678` is likewise
  now a `references` entry rather than a notes-only mention.

## 8b. The one molecular-function experiment ever done on ADAMTSL1, and it is negative

Found late, and not by me: the concurrent ADAMTSL3 review surfaced it. `PMID:22242013` is
titled *"Microenvironmental regulation by fibrillin-1"*, so no ADAMTSL1-keyed search reaches
it; it is absent from ADAMTSL1's GOA and from the affinage record. It is the campaign's
"a paper titled for something else holds your gene's answer" lesson in its partner-named form.

Two direct SPR negatives for human ADAMTSL1, in a panel where its relatives were positive:

- [PMID:22242013 "ADAMTSL-2, -3, and papilin polypeptides interacted with the N-terminal half of fibrillin-1, while ADAMTSL-1 did not."]
- [PMID:22242013 "However, neither ADAMTSL-2 nor -1 bound to ADAMTS-10, indicating that ADAMTS enzymes may partner only with specific ADAMTSL proteins."]

This is a **measured negative, not an absence**, which makes it much stronger than the silence
this review was otherwise working against.

**Only the fibrillin-1 half is discriminating**, and the PR reviewer was right that my first
write-up read as two independent exclusions. ADAMTSL-2 is *equally* negative against ADAMTS-10
and still reaches `GO:0030198`; ADAMTS-10 binding was shown only for ADAMTSL-3; THSD4 was never
tested against it. So the ADAMTS-10 result does not separate ADAMTSL1 from its relatives and
must not be double-counted. The fibrillin-1 negative alone carries the argument, and it is
enough.

**The caveat is the isoform question again.** The methods say
*"Recombinant full length ADAMTSL-1, -2, LTBP-1, -4 ... were covalently coupled to CM5 sensor
chips"* but never give a length, and the Apte lab stated five years later that no construct
for the 1762-residue form existed. Both RefSeqs were available in 2012 (`NP_443098` = isoform 1,
525 aa; `NP_001035362` = isoform 3, 1762 aa), so the paper alone does not settle it, and the
balance of evidence favours punctin-1. Recorded as a **bounded** negative: firm for whatever
was assayed, and probably untested for the nine extra TSRs, four Ig-like domains and PLAC
domain of the long form.

**What it changed in this review.** Ground two of the `GO:0030198` reason — "a non-catalytic
route to the term is available to this architecture" — is now explicitly qualified, because
the specific route the relatives use is excluded for this protein. It does not flip the verdict
to `MARK_AS_OVER_ANNOTATED`: `GO:0030198` is far broader than fibrillin-1 binding, and
excluding one mechanism is not refuting the process. But it removes the strongest mechanistic
analogy, and it is a further reason the term cannot be called core. The MF `knowledge_gap` is
now bounded on both sides — what is established, *and* what has been measured and excluded —
and the proposed binding experiment became an unbiased partner search rather than the
candidate SPR I had originally proposed, which would have repeated a published negative.

One more correction from the same round, and it is the lesson of this section applied to
itself: I wrote that "the LTBPs remain untested". Unsafe. LTBP-1 and LTBP-4 were coupled to
CM5 chips in these very experiments, and the LTBP results sit in a supplementary table that is
not in the cached record. "Not reported in the main text" is what the evidence supports. This
whole section exists because a candidate that looked untested turned out to have been tested,
so asserting a second one untested on the same paper would have been the same error twice.

**And the parity claim needed narrowing.** I had written that ADAMTSL1 and ADAMTSL5 are "in
exactly the same evidentiary position" for `GO:0030198`. That was true when I wrote it and this
paper made it false: the two remain in the same *IBA* position, but ADAMTSL5 has its own IDA to
`GO:0031012` plus microfibril and heparin binding, while ADAMTSL1 now carries a measured
negative against the route by which the family reaches `GO:0030198`. **The difference runs
against this review**, not for it — the better-supported gene is the one taking the harsher
action. That does not change the verdict here, but it converts the family-wide line-drawing
question from a tie into an argument, and it is carried into `suggested_questions` as such.

## 8c. A gap in `checkquotes.py` worth knowing about

Reconciling a count that did not add up (I added three quotes and the checker's total rose by
one) turned up a real scope gap rather than an arithmetic slip. `checkquotes.py` walks
`supported_by` and `findings` only; **`provenance` lists inside `knowledge_gaps` are invisible
to it**, as is any other `reference_id` + `supporting_text` pair under a differently-named key.
For this file: 17 `supported_by` + 32 `findings` = 49, exactly what the checker reports, and
**6 `provenance` quotes are unchecked**. They were verified here with a walker that matches on
the *shape* of the entry rather than on its parent key, and all 6 pass. Anyone relying on
`checkquotes.py` alone for a review that uses `knowledge_gaps` provenance is not checking those
quotes.

**But it is a local-script gap, not a project-gate gap** — I initially implied the wider risk and
that was wrong. The gate that actually runs in CI is `linkml-reference-validator` via
`just validate`, and it *does* walk provenance. Established by breaking it rather than by reading
code: injecting `THIS SENTENCE APPEARS IN NO PUBLICATION ANYWHERE ZZQQXX.` as a provenance
`supporting_text` turns `just validate` from `✓ Valid` into
`✗ Invalid ... Text part not found as substring`. The probe asserted its anchor was present before
mutating, and the file was restored to a clean `git diff` afterwards. So provenance quotes in this
repo are gated; it is only the scratch checker that misses them.

## 8d. The recurring defect in this review, and what finally caught it

Five of the review rounds on this gene found the **same** defect shape: a claim corrected in the
field I was thinking about and left standing in a parallel field saying the same thing elsewhere.
The instances were the `GO:0030198` reason vs `core_functions`; the top-level MF gap boundary vs
the nested BP gap boundary; the `suggested_questions` tail vs its own narrowed opening; the
`knowledge_gaps` resolution vs `suggested_experiments`; and the reference `findings` statement vs
the row reason. The reviewer caught four. **The fifth I found only by giving up on per-field
fixes and sweeping the whole parsed document for every phrasing I had ever retracted** — it was
in the top-level MF boundary, which had already been rewritten twice without anyone noticing the
old double-count framing still sitting in it.

The sweep is seven regexes run over every string value in the parsed YAML:

```
two partners that place | both been tested for ADAMTSL1 and both were negative |
exactly the same evidentiary position | well-constructed and unrefuted |
LTBPs remain untested | no positive binding result of any kind |
divergence is not attributable to a difference between the genes
```

It is the ACBD3 lesson (a claim asserted at N sites with no generation relationship between
them) in a review that had read that lesson and still reproduced it five times. The transferable
part is not "be careful": it is that **the unit of correction has to be the document, not the
field**, and a retraction list scanned over all prose is cheap enough to run on every round.

**And the sweep is only half the control.** The commit that fixed instances 1-5 produced a
sixth of the same shape: a `(data not shown)` caveat added to the reference `findings` and to
the row reason but not to the nested BP boundary. A retraction list structurally cannot catch
that — it looks for **old** phrasing left standing, whereas this is **new** phrasing propagated
to some siblings and not others. The complementary check has to run at write time and enumerate
the siblings: for the C-terminal widening the sibling set is `references.findings[1]`,
`existing_annotations[0].review.reason` and
`existing_annotations[0].review.knowledge_gaps[0].boundary`, and the edit now asserts that both
the claim *and* its caveat appear in all three before it is accepted. Two directions, two
checks: sweep for what should be gone, assert co-occurrence for what should be everywhere.

**And the co-occurrence check failed too, for the reason the reviewer named: it is only as good
as the hand-authored sibling list, and enumerating siblings is the same judgement that produced
the six instances.** My list had three members; the widened claim was load-bearing in a fourth —
the top-level MF boundary, which concluded "what is excluded is fibrillin-1 binding" while
stating the evidence as the N-terminal half only, so the field used the widened scope without
carrying what licenses it. Three of four beats the sweep alone, but the residual failure mode
survived the new control.

The fix is to stop hand-listing. **Derive the sibling set from the document**: collect every
string field, select those that draw the widened conclusion (`excluded is fibrillin-1 binding`
or `covers fibrillin-1 entire`), and require each to state the basis (`C-terminal half`). That
found the missing field immediately and now passes on three. Two further guards make the check
non-vacuous: it asserts the selector matched something at all, and the selector keys on the
*conclusion* rather than on a list of field paths, so a claim copied into a new field is caught
automatically. Generalisable form: **select the fields by what they assert, not by where they
live.**

**And that control leaked too, in a smaller way — which turns out to be the real finding.** The
selector matched two fixed English phrasings, so it missed the reference `findings` statement,
which draws the same conclusion as *"covers fibrillin-1 in its entirety, not only the N-terminal
half"*. Nothing was wrong in the file — that field carried the basis and the caveat and passed on
merit — but had the caveat later been dropped from it, the check would still have reported all
green, because the field asserting the conclusion in different words was never selected. Matching
on fixed phrasings is still selecting by *how* a field asserts something; it is one abstraction
level up from a path list, not a different kind of thing. Broadened to four patterns, and the
selected set went 3 → 4.

**The pattern across the whole review is the point.** Each control caught one more instance than
its predecessor and left a smaller version of the same gap:

| control | caught | residual gap |
|---|---|---|
| fix the field in front of me | 1 at a time | 5 parallel fields left stale |
| retraction sweep over all prose | the 5th instance | cannot see *new* phrasing propagated unevenly |
| hand-listed sibling co-occurrence | 3 of 4 siblings | list is the same judgement that caused the defect |
| conclusion-derived selector | the 4th sibling | selector is phrase-literal, misses paraphrase |
| broadened phrase set | the paraphrase | still phrase-literal in principle |

No text-matching control closes this completely, because the thing being checked is whether two
sentences *mean* the same. The honest summary is that each round bought a real reduction and none
of them bought closure, and that a reviewer reading the parsed fields end to end caught what
every mechanical control missed.
Note the notes file legitimately still contains three of those strings, because explaining why a
phrasing was retracted requires quoting it — so the sweep belongs on the review YAML, not on
prose that discusses it.

## 9. What ADAMTSL1 is, in one paragraph

A large secreted ADAMTS-like glycoprotein of the extracellular matrix, built from
thrombospondin type-1 repeats, Ig-like C2-type domains and a PLAC domain, with none of the
catalytic machinery of the ADAMTS proteases. Its biosynthesis is unusually
glycosylation-dependent: O-fucosylation of the TSRs by POFUT2 with B3GLCT extension, and
C-mannosylation of TSR1 tryptophans, together gate export from the ER, and a natural
Trp42Arg substitution at a C-mannosylation site blocks secretion and acts dominant-negatively
in a family with congenital glaucoma, craniofacial, dental, auditory, renal and limb
anomalies. Once secreted it is deposited punctately into the matrix and is a substrate of
MMP10 in fibroblast secretomes. Its molecular function is undetermined.
