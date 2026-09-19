# ARHGAP11B — review notes

UniProt `Q3KRB8` (`RHGBB_HUMAN`), 267 aa, `PE 1: Evidence at protein level`.
GOA TSV: 17 rows. Seeded `existing_annotations`: 17. Counts reconcile exactly, so no
`GO:0005515` partner rows and no same-term/different-assigner rows were collapsed by the
stub on this gene. (Checked because the stub is known to under-seed on other genes.)

## What the gene is

ARHGAP11B arose on the human lineage by **partial duplication of ARHGAP11A**
(`Q6P4F7`, 1023 aa), then acquired a single C→G substitution that creates a novel splice
donor site. 55 nt are spliced out, the reading frame shifts, and the protein ends at 267
residues with a C-terminus found in no other protein.

> "The first 220 amino acids of ARHGAP11B are 98% identical to those of ARHGAP11A (216 of
> 220 residues; for a discussion of the four amino acid changes, see below and the
> Supplementary Materials) and encompass most of its GAP domain (amino acids 46 to 246)"
> [PMID:27957544]

> "Thus, the single C→G base change in the ARHGAP11B gene is ultimately the reason for the
> reading frame shift that leads to the truncation of the GAP domain of ARHGAP11B and its
> novel C-terminal sequence (amino acids 221 to 267; Fig. 1 and fig. S2), which is unique
> to ARHGAP11B and not found in any other protein thus far described in the animal
> kingdom" [PMID:27957544]

The substitution predates the split from Neanderthals and Denisovans and is fixed in
present-day humans [PMID:27957544, "The crucial C→G base substitution was also found in
Neanderthal and Denisova ARHGAP11B (fig. S3). Moreover, all present-day humans analyzed
(31) carry the C→G substitution."].

## The central curation problem: GOA asserts GAP activity and its negation simultaneously

The GOA TSV carries **both** of these for the same gene:

| row | qualifier | term | evidence | reference |
|---|---|---|---|---|
| 5 | `NOT\|enables` | GO:0005096 GTPase activator activity | IDA | PMID:27957544 |
| 15 | `NOT\|enables` | GO:0005096 GTPase activator activity | IDA | PMID:25721503 |
| 14 | `enables` | GO:0005096 GTPase activator activity | **TAS** | Reactome:R-HSA-8981637 |
| 13 | `NOT\|involved_in` | GO:0043547 positive regulation of GTPase activity | IDA | PMID:27957544 |
| 3 | `involved_in` | GO:0051056 regulation of small GTPase mediated signal transduction | **TAS** | Reactome:R-HSA-9012999 |

Two independent experimental papers say the protein has no GAP activity; Reactome says it
does. This is not a subtle over-annotation — it is a **flat contradiction inside a single
gene's GOA record**, and the positive side is the one with the weaker evidence code.

### Where the wrong positive comes from, measured

Querying QuickGO **by reference** rather than by gene settles it (`numberOfHits` compared
against `len(results)` each time, and paged until they matched):

| reference | annotations | distinct entities | terms |
|---|---|---|---|
| `Reactome:R-HSA-8981637` | 43 (all read, 1 page) | 22 | `GO:0005096` to 21 entities, `GO:0005829` to 21, `GO:0005886` to 1 — all TAS |
| `Reactome:R-HSA-9012999` | 103 (all read, 2 pages) | 103 | `GO:0051056` to all 103 — all TAS |

R-HSA-8981637 is a `Reaction` in the cytosol/plasma-membrane compartments whose **single
`catalystActivity` is a set-level entity, `"GTPase activator activity of RHOA GAPs
[cytosol]"`**. So both the activity term and the cytosol term are handed to every member of
a defined catalyst set at once. ARHGAP11B is in that set because it looks like ARHGAP11A.
For ARHGAP11A the same projection is correct and should stay.

### The paralog comparison, which is the cleanest evidence in the whole review

QuickGO for the two genes side by side:

| term | ARHGAP11A (`Q6P4F7`) | ARHGAP11B (`Q3KRB8`) |
|---|---|---|
| `GO:0005096` GTPase activator activity | **IBA** (node `PTN001038329`) + **IDA `enables`** (PMID:27957544) + Reactome TAS | **IDA `NOT|enables` x2** + Reactome TAS **`enables`** |
| `GO:0043547` positive regulation of GTPase activity | **IDA `involved_in`** (PMID:27957544) | **IDA `NOT|involved_in`** (PMID:27957544) |
| localisation (IDA) | `GO:0005634` nucleus (PMID:31883789) | `GO:0005759` mitochondrial matrix (PMID:31883789) |
| `GO:0005829` cytosol | Reactome TAS | Reactome TAS |

**The same paper produced the positive annotation on ARHGAP11A and the negated one on
ARHGAP11B**, and the same study that put ARHGAP11B in mitochondria put ARHGAP11A in the
nucleus. The UniProt-sourced curation is internally consistent and correct for both
paralogs. Every wrong row on ARHGAP11B is non-experimental, and the shared Reactome cytosol
call describes neither paralog's measured location.

UniProt has already adjudicated it, twice over. The recommended *name* is a verdict:

> "RecName: Full=Inactive Rho GTPase-activating protein 11B"
> [`file:human/ARHGAP11B/ARHGAP11B-uniprot.txt`]

and the entry carries a `CAUTION` block (lines 154-159 of the cached record) stating that
although the protein contains a Rho-GAP domain it does not have GTPase activator activity,
citing PubMed:25721503 and PubMed:27957544, and that restoring the activity abolishes the
ability to promote basal-progenitor amplification. That block is paraphrased rather than
quoted because it wraps across `CC` continuation lines and so cannot be reproduced
verbatim on one line.

### The experimental evidence, quoted to the end of the interpreting clause

> "However, contrary to ARHGAP11A (27, 28), ARHGAP11B does not exhibit RhoGAP activity when
> expressed in monkey fibroblast-like cells (23)." [PMID:27957544]

`(23)` is Florio et al. 2015 = PMID:25721503, which is abstract-only in our cache. So the
2016 full text independently confirms what the 2015 IDA records, which matters because I
cannot read the 2015 paper directly.

The important qualification, which must not be dropped:

> "Modern ARHGAP11B lacks RhoGAP activity in intact cells (23) and exhibits only very low
> RhoGAP activity in a cell-free assay." [PMID:27957544]

So the honest statement is **no activity in cells, very low activity in a cell-free
assay** — not "zero under all conditions". `NOT|enables` is still the right call for an
`is_active_in`-style claim about the protein in a cell, and it is the curators' call on a
full text I have read, but the review should not overstate it as an absolute.

The decisive genetic experiment is the resurrected ancestral protein:

> "In contrast to modern ARHGAP11B, but similar to ARHGAP11A-250, ancestral ARHGAP11B was
> found to exhibit RhoGAP activity, as compared to a negative control (empty vector)
> (Fig. 2)." [PMID:27957544]

> "However, similar to ARHGAP11A (23), ancestral ARHGAP11B did not exert any effect on
> mitotic BP abundance (Fig. 3)." [PMID:27957544]

i.e. GAP activity and progenitor amplification are **anti-correlated** across the three
proteins tested. Loss of the catalytic function is not incidental damage; it is what makes
the modern protein do its job.

## Why the standard pseudo-enzyme check fails here — and what actually broke

Committed analysis: `ARHGAP11B-bioinformatics/` (`RESULTS.md`, `results.json`,
regenerated by `analyze_arhgap11b.py`; `--self-test` exercises six guards).

**The arginine finger is RETAINED.** UniProt annotates `SITE 87 Arginine finger` on
ARHGAP11B and, at the identical position, on ARHGAP11A. The analysis confirms it
reciprocally: both ARHGAP11A's own finger (87) and ARHGAP1/p50RhoGAP's structurally
resolved finger (282) align onto ARHGAP11B residue 87, which is an arginine **and** is one
of ARHGAP11B's own annotated Site features.

This is worth stating plainly because the campaign's reflex would get it backwards: the
usual "a catalytic term with no catalytic residues is `PSEUDOENZYME_OVERANNOTATION`"
argument **does not apply to this gene**, and reaching for it would have produced a
correct action supported by a false reason.

The test is not vacuous — of 66 reviewed (Swiss-Prot) human proteins carrying the PROSITE
RhoGAP profile PS50238, **6 do have a non-arginine at their annotated finger position**
(OCRL and INPP5B/I5P2 and ARAP2 and FAM13B with Q, ARHGAP36 with T, DEPDC1B with I). The
test works; ARHGAP11B is simply a **false negative** of it. A pipeline that gated a GAP
term on arginine-finger presence would keep the term here.

**What the truncation removes instead.** Projecting the GAP:GTPase interface from PDB 1TX4
(p50RhoGAP:RhoA:GDP:AlF4, 1.65 Å) onto ARHGAP11A, **2 of 24 mapped interface positions**
(ARHGAP11A L221 and A225, both inside its Rho-GAP domain) fall past the divergence point
at residue 220. The catalytic arginine survives; a small part of the surface that has to
present it to the GTPase does not. That is corroboration, not proof — 8% of an interface
is not on its own an argument for inactivity, and the review rests the `NOT` rows on the
experiments, with the structure as support.

Two measurement bugs were caught by guards and are documented in the analysis README,
because both produced confident wrong numbers first:
- a global alignment put ARHGAP1's arginine finger on ARHGAP11A residue **684** (the two
  proteins carry their Rho-GAP domain at opposite ends);
- once fixed, a *local* alignment reported **0 of 25** contacts lost — because it stopped
  at ARHGAP11A residue 204, sixteen residues short of the divergence point. Six contacts
  were past its end: not absent, **not measured**.

**Independent reproduction:** the divergence point (220) and the prefix identity
(216/220 = 98.2%) are derived from a changepoint fit with no chosen cutoff, and reproduce
the published figures exactly. That is a check on the pipeline, not a new finding.

### A UniProt feature defect worth reporting

| | Rho-GAP DOMAIN (UniProt) | length |
|---|---|---|
| ARHGAP11B (truncated, GAP-dead) | 49..250 | 202 aa |
| ARHGAP11A (intact, active) | 49..239 | 191 aa |

ARHGAP11B's annotated Rho-GAP domain runs **30 residues past residue 220**, i.e. into the
human-specific frameshift C-terminus that is homologous to nothing. The consequence is
perverse: **the annotated domain on the inactive truncated paralog is 11 residues longer
than the annotated domain on the catalytically active parent.** Any automated step reading
domain extent as evidence of an intact RhoGAP reads this protein as *more* intact than the
active one. This plausibly contributes to the `GO:0007165` IEA from `InterPro:IPR000198`.

## The actual molecular function: mitochondrial, not cytoskeletal

PMID:31883789 is **abstract-only** in our cache (`full_text_available: false`), so the IDA
rows sourced from it are accepted on the curators' reading of a full text I have not seen,
which is the correct default. The abstract does state each claim:

> "Here, we show that ARHGAP11B is imported into mitochondria, where it interacts with the
> adenine nucleotide translocase (ANT) and inhibits the mitochondrial permeability
> transition pore (mPTP)." [PMID:31883789]

> "BP expansion by ARHGAP11B requires its presence in mitochondria, and pharmacological
> inhibition of ANT function or mPTP opening mimic BP expansion by ARHGAP11B."
> [PMID:31883789]

> "Searching for the underlying metabolic basis, we find that BP expansion by ARHGAP11B
> requires glutaminolysis, the conversion of glutamine to glutamate for the tricarboxylic
> acid (TCA) cycle." [PMID:31883789]

The two `GO:0005515 protein binding` IPI rows resolve to `UniProtKB:P12235` (SLC25A4 /
ANT1) and `UniProtKB:P05141` (SLC25A5 / ANT2) — the ADP/ATP translocases named in that
sentence. These are not screen noise: they are the mechanism, they are corroborated by
UniProt's SUBUNIT line, and they are topologically coherent with a mitochondrial-matrix
protein. Each therefore gets a MODIFY to an informative term rather than the bare
`protein binding`.

Note the direction of the ANT relationship: ARHGAP11B **inhibits** mPTP opening via ANT.
`GO:0035795 negative regulation of mitochondrial membrane permeability` captures exactly
that, and is one of the better-fitted terms in this record.

## The neocortex phenotype — attribute it to the system it was measured in

Five of the seven primary papers assay **ectopic or transgenic expression of the human
protein in a non-human system**. That does not make the annotations wrong (the gene
product assayed *is* the human protein), but the review should not state mouse or ferret
results as measurements of the human protein in human tissue.

| PMID | system | what was done |
|---|---|---|
| 25721503 | mouse (in utero electroporation) + human fetal tissue expression | BP amplification; human radial-glia-specific expression |
| 27957544 | mouse (in utero electroporation), COS-7 for the GAP assay | ancestral vs modern ARHGAP11B |
| 30484771 | **ferret** | bRG increase, neocortex expansion |
| 32554627 | **marmoset** | neocortex enlargement and folding (not cached — fetch failed) |
| 33938018 | **transgenic mouse** | persistence into adulthood, memory flexibility |
| 31883789 | mouse + human fetal neocortex ex vivo | mitochondria, ANT, mPTP, glutaminolysis |
| 36098218 | **human and chimpanzee cerebral organoids** | loss- and gain-of-function |

The human-side expression evidence is real and is in UniProt's DEVELOPMENTAL STAGE block,
which records radial-glia-specific expression in human fetal neocortical progenitors:

> "Preferentially expressed in apical and basal radial glia"
> [`file:human/ARHGAP11B/ARHGAP11B-uniprot.txt`]

(The same block adds that ARHGAP11B is not detected in cortical neurons or cortical plate.)

## Recall gap: the decisive human loss-of-function paper is absent from GOA

The affinage record's trust gates passed, which certifies only that the citations it gave
are real — it says nothing about what it missed. In this case affinage actually *supplied*
the paper that GOA lacks:

**PMID:36098218** is the only study that perturbs ARHGAP11B **in a human system**, and it
does so in both directions:

> "dominant‐negative inhibition of ARHGAP11B's function by ARHGAP11A220 reduces cycling BP
> abundance in human cerebral organoids to the chimpanzee level." [PMID:36098218]

> "by subjecting ARHGAP11A plus ARHGAP11B double‐knockout human forebrain organoids to
> either ARHGAP11A or ARHGAP11B rescue, we find that ARHGAP11B is essential to maintain the
> level of basal (or outer) radial glia (bRG), the BP type of particular relevance for
> neocortex expansion." [PMID:36098218]

Every `GO:0021987` row in GOA is a **gain-of-function** experiment. The necessity evidence
— and the only human-cell perturbation of this gene anywhere — produces no GO annotation
at all. That is a **coverage** defect, not an over-annotation defect, and it is the single
most useful thing a curator could act on from this review after the Reactome contradiction.

## Checks run, including the ones that came back negative

- **Row reconciliation:** 17 GOA rows, 17 seeded entries. No collapse. (Negative result.)
- **Retraction / erratum / expression-of-concern:** checked per-PMID against each cited
  article's own PubMed `CommentsCorrections`/`RefType`, not by a publication-type search
  (which cannot see Publisher Corrections). Result recorded per reference below.
- **IBA:** ARHGAP11B has **no IBA row at all**, and UniProt records
  `PAN-GO; Q3KRB8; 0 GO annotations based on evolutionary models`. PAINT deliberately gave
  this gene nothing. Given that PANTHER places ARHGAP11B in `PTHR15670:SF4`, a subfamily
  **named for its paralog** ("RHO GTPASE-ACTIVATING PROTEIN 11A"), that restraint is the
  correct outcome and deserves to be recorded as such — the predicted IBA-sweep failure
  mode **did not occur here**. The paralog leak arrived through Reactome instead.
- **Arginine-finger loss:** hypothesis **not confirmed**; the residue is retained (above).
- **Partner accession resolution:** both `GO:0005515` partners resolve to reviewed
  canonical Swiss-Prot entries of the expected length, with no TrEMBL/ORFeome substitution.

## Final actions

| action | n | rows |
|---|---|---|
| ACCEPT | 11 | both `NOT GO:0005096` IDA rows, `NOT GO:0043547`, `GO:0005759` x2, `GO:0006543`, `GO:0021987` x4, `GO:0035795` |
| MODIFY | 2 | the two `GO:0005515` rows → `GO:0044325` transmembrane transporter binding |
| REMOVE | 4 | `GO:0005096` TAS, `GO:0005829` TAS, `GO:0051056` TAS, `GO:0007165` IEA |
| NEW | 1 | `GO:2000179` positive regulation of neural precursor cell proliferation, IMP, PMID:36098218 |

11 + 2 + 4 + 1 = 18 = 17 GOA rows + 1 NEW row.

These counts come from `ARHGAP11B-bioinformatics/check_review_counts.py`, not from counting
by eye, and writing it immediately earned its keep. My hand tally said **ACCEPT 12** and
wrote the arithmetic as `12 + 2 + 4 = 18`, which *also* came to 18 — because it had dropped
the NEW row from the sum at the same time as inflating ACCEPT by one. Two errors cancelling
into a total that looked reconciled. The row list beside the number was correct all along
(2 + 1 + 2 + 1 + 4 + 1 = 11); only the number was wrong. The wrong figure had already
reached the commit message and the PR body before the script was run.

Every REMOVE is non-experimental (three TAS, one IEA). **No experimental annotation was
removed, modified or demoted anywhere in this review** — the two `GO:0005515` MODIFYs
replace an uninformative term with a more specific one and do not weaken any claim.

## A tooling limitation that shaped this file: no `file:` references

This review carries **no `file:` references at all**, which is unusual for a gene with a
committed bioinformatics analysis. The reason is environmental, not editorial.

The pre-write hook `.claude/hooks/validate_ai_review_pretool_hook.py` computes
`project_root = Path(__file__).parent.parent.parent` and runs the validator with that as
`cwd`. For an agent working in `.claude/worktrees/<id>/`, that resolves to the **main
checkout**, where `genes/human/ARHGAP11B/` does not exist — so every `file:` reference is
rejected as pointing at a non-existent file and the write is blocked.

I measured that this is a false positive rather than assuming it: a copy of this review with
`file:human/ARHGAP11B/ARHGAP11B-bioinformatics/RESULTS.md` added validates `✓ Valid` when
`ai-gene-review validate` is run from this worktree, and CI runs from a checkout root where
the gene folder exists. So the references would have been fine on the PR; only the local
hook could not see them.

Consequence: the bioinformatics numbers are cited **in `review.reason` prose**, naming the
analysis directory, rather than as `supported_by` entries. Since CI does not check `file:`
supporting_text at all, nothing verifiable was lost — but the `⚠ No annotations reference
available deep research files` warning that `just validate` emits is a direct result of this
and should not be read as the affinage record having been ignored.

## Open items I could not resolve

- **PMID:32554627** (marmoset, Science 2020) would not fetch (`Failed to fetch PMID
  32554627`). It is cited by UniProt and by affinage but is not in GOA, so nothing in the
  review depends on it; it is named in the notes only as part of the systems table.
- **PMID:31883789 and PMID:25721503 are abstract-only.** Their IDA rows are accepted on the
  curators' authority. I did not attempt to overrule any of them.
