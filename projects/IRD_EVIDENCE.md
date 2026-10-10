---
title: "IRD Evidence: How PAINT Uses Inferred from Rapid Divergence"
maturity: IN_PROGRESS
tags: [EVALUATION, PIPELINE]
species: [human, mouse, rat, yeast, SCHPO, DROME, NEUCR, ARATH]
genes: [SSA1, SSA2, SSA3, SSA4, SSB1, SSB2, SSZ1, SLC52A1, CFLAR, HDAC6, PIP4K2A, FZD9, ATG16L2, pmp20, cia30]
---
# IRD Evidence: How PAINT Uses Inferred from Rapid Divergence

**Bottom line:** IRD (Inferred from Rapid Divergence, ECO:0000321) is a negative
evidence code that never reaches a gene. All 2,538 IRD calls sit on internal PANTHER
tree nodes in PAINT's `IBD.gaf`, every one as a NOT. None of them produces a NOT
annotation on any protein: GOA has zero IRD rows, and none of the 2,881 NOT|IBA rows in
PAINT's leaf file comes from an IRD alone (all come from IKR, key-residue, losses). An
IRD only stops the ancestral IBD from descending, so the genes below it get *no*
annotation rather than a negative one. That makes IRD the most invisible curation
decision in GO. It records that a PAINT curator looked at a clade and judged the family
function gone, yet a reviewer looking at GOA for one of the 33,633 proteins under an IRD
node cannot see that. The calls mostly hold up: inside the effective block, experimental
annotations contradict 170 of the 2,538 IRD rows (6.7%), and 165 rows are supported by
experimental NOTs. The contradicted ones form a short, checkable worklist (Hsp70 protein
refolding in fungi, the riboflavin transporter SLC52A1, Frizzled-9/10 Wnt receptor
activity). For our reviews, IRD is direct evidence for the rule *do not add what
curators deliberately declined to add*, and it explains 24 IBAs in 15 of our reviews
that PAINT has since withdrawn but our cached GOA files still carry.

## Question

How is IRD used, what does it actually do downstream, and how should a gene reviewer
treat it? This complements the [NOT Annotation Usage Audit](NOT_ANNOTATION_USAGE.md),
which found no IRD among GOA's 10,622 NOT annotations. This project finds out why: IRD
lives one level up, in PAINT.

The GO Handbook describes IRD as an evidence code for negative annotations: "negative
annotations can be assigned to highly divergent sequences using the code IRD
(Inferred from Rapid Divergence)"
([handbook](../docs/paper/literature/Gene_Ontology_Handbook_Full.md)). In practice PAINT
records IRD as a NOT on a node, but that NOT is not propagated to the genes below the node.

The GO wiki page on IRD
([Inferred from Rapid Divergence (IRD)](https://wiki.geneontology.org/index.php/Inferred_from_Rapid_Divergence(IRD)),
last reviewed January 30, 2018) is short. Its overview says: "IRD is a type of
phylogenetic evidence characterized by rapid divergence from ancestral sequence.
Annotating with this evidence code implies a NOT annotation." It maps IRD to
ECO:0000321 and points to Gaudet et al., 2011, "Phylogenetic-based propagation of
functional annotations within the Gene Ontology consortium". The sections "Use of the
With/From Field for IRD", "When IRD Should NOT be Used" and "Quality Control Checks" are
empty. Its one example is a gene-level TAIR GAF row:

| DB Object ID | DB Object Symbol | Qualifier | GO ID | DB:Reference | Evidence Code | With/From |
|---|---|---|---|---|---|---|
| TAIR:AT2G31280 | CPUORF7 | NOT | GO:0004674 | TAIR:Communication:501741973 | IRD | PANTHER:PTN000357291 |

The row puts the NOT on a named gene. It cites a TAIR communication rather than PAINT's
`GO_REF:0000033`, and it puts the PTN node in with/from.

The example no longer matches the data (checked 2026-10-05):

- `PTN000357291` is absent from the current `IBD.gaf`. The only IRD on GO:0004674 in
  the WNK-related family PTHR13902 sits on a Drosophila node (`PTN000357107`), and no
  Arabidopsis protein is under it.
- AT2G31280 now maps to UniProt Q58G01, bHLH155 (PTHR46196), a transcription factor.
  CPuORF7 is a conserved upstream-ORF peptide named after that locus. Q58G01 has no
  NOT annotation in GOA, and nothing for GO:0004674.
- No current PAINT output contains a gene-level IRD row of this kind. The leaf file has
  no IRD evidence at all, and no IRD-only NOT|IBA rows.

So the wiki documents IRD as it was once submitted: a NOT on a named gene, with the
divergent node as with/from. Current PAINT keeps IRD on internal nodes and exports
nothing for the genes below. The statement "implies a NOT annotation" is therefore true
of the node in `IBD.gaf`, but not of any gene annotation a user can see. The wiki page
should be updated: a current example, the with/from convention (the ancestral IBD node),
and a note that IRD blocks propagation instead of creating NOT|IBA rows. Its three empty
sections could be filled from this project. The change in practice should be confirmed
with the PAINT team first.

## Methods

The scripts are in [IRD_EVIDENCE/](IRD_EVIDENCE/). Run them in order with
`uv run python projects/IRD_EVIDENCE/<script>`. The large PAINT and PANTHER downloads
are cached in the git-ignored `.cache/`. The TSV outputs named below are written next to
the scripts but are not committed (they are git-ignored), so regenerate them to work with
the rows. [RESULTS.md](IRD_EVIDENCE/RESULTS.md) is committed and is regenerated each time.

1. `fetch_paint_ird.py` reads PAINT's current release (`IBD.gaf`, the leaf IBA GAF
   `gene_association.paint_uniprot.gaf.gz`, and the TreeGrafter node-to-family table).
   It writes every IRD row to `ird_nodes.tsv`, with its family, the ancestral IBD node it
   overrides, and whether an IKR loss shares that ancestor and term. It also tallies every
   leaf IBA by the losses sitting on the ancestor+term it was projected from
   (`leaf_iba_loss_sources.tsv`).
2. `fetch_ird_clades.py` fetches the tree of each of the 894 families from the PANTHER
   `treeinfo` API and lists the leaf proteins under every IRD node
   (`ird_clade_members.tsv.gz`, 52,660 rows).
3. `fetch_clade_experimental.py` downloads from QuickGO every experimental annotation
   (ECO:0000269 and descendants) on those proteins (`clade_experimental_annotations.tsv.gz`).
4. `analyze_ird.py` matches experimental annotations to the blocked term or any GO
   is_a/part_of descendant, excluding proteins PAINT re-annotates below the IRD node.
   It writes `ird_experimental_conflicts.tsv` and joins clade members to our gene
   reviews (`ird_review_overlaps.tsv`). Summary tables are in
   [RESULTS.md](IRD_EVIDENCE/RESULTS.md).

## Findings

Full tables are in [RESULTS.md](IRD_EVIDENCE/RESULTS.md).

- **What IRD blocks.** There are 2,538 IRD rows on 1,539 nodes in 894 families: 968 BP,
  850 MF and 720 CC.
  - **MF:** GTPase activity (74 rows), metalloendopeptidase activity (43) and protein
    serine/threonine kinase activity (19) lead.
  - **CC:** mitochondrion (72), plasma membrane (71), nucleus (57) and cytosol (52) lead.
    Many IRDs are therefore localization blocks, not activity blocks.
  - **Dates:** IRD use has grown sharply. 1,036 rows are dated 2026 and 577 are dated
    2025, against 46 in 2017.
- **IRD never becomes a gene annotation.**

  | Leaf IBA polarity | Losses on the source ancestor+term | Leaf rows |
  |---|---|---|
  | NOT | IKR | 2,170 |
  | NOT | IKR and IRD | 459 |
  | NOT | none (NOT\|IBD nodes) | 252 |
  | NOT | IRD only | **0** |
  | positive | IRD (sister clades retaining the function) | 333,738 |

  The contrast with IKR is the core result. A key-residue loss produces a NOT|IBA on
  every descendant, which is visible in GOA, in our reviews and in the NOT projects. A
  divergence call produces nothing at all.
- **Most IRD clades are not tiny.** 789 IRD rows sit on a single leaf, 599 cover 2–10
  leaves, 1,048 cover 11–100 and 102 cover more than 100.
  - PAINT re-annotates below the IRD node in 51 rows (31 partly, 20 fully, where the IRD
    then blocks nothing). DROSHA is an example: it sits under the PTHR11207 IRD for
    primary miRNA processing, but PAINT annotates it again from a lower node.
  - 14 IRD rows point at an ancestral node that no longer carries the IBD they override.
    These are stale overrides left behind when the parent annotation was removed.
- **Experimental support and conflict.** Experimental annotations were downloaded for
  the 2,909 clade proteins that have any.
  - **Conflicts:** within the effective block, 345 positive experimental rows on 237
    (IRD, protein) pairs contradict 170 IRD rows (6.7%). The share by aspect is MF 7.4%,
    BP 4.6% and CC 8.6%. 157 of these IRD rows have at least one low-throughput conflict.
  - **Support:** experimental NOT annotations agree with 165 IRD rows.
  - **Mostly IRD right, positive questionable:**
    - PIP4K2A/B/C carry IDA "1-phosphatidylinositol-4-phosphate 5-kinase activity", but
      they are PI5P 4-kinases.
    - HDAC6 and HDAC10 carry histone deacetylase activity (IDA, in vitro), but their
      main physiological substrates are tubulin and polyamines. This one is contested
      rather than clear.
    - Gamma-tubulin carries "located_in microtubule" and "polar microtubule". It
      nucleates microtubules from the gamma-TuRC rather than being built into the
      lattice, so this is partly a term-scope question.
  - **IRD probably wrong:**
    - Fungal Hsp70 protein refolding (PTHR19375, dated 2026-06-16), against SSA1 IDA.
    - SLC52A1 riboflavin transporter activity, against IDA.
    - FZD9/FZD10 Wnt receptor activity.
    - The PTHR10210 ribose-phosphate diphosphokinase complex, which blocks yeast PRS2–5.
  - The ranked worklist is in RESULTS.md section 4.
- **Our reviews.**
  - 191 reviews cover a protein under an IRD node; 79 (review, blocked term) pairs
    inside the effective block annotate the blocked term or a descendant.
  - **Agreement:** many of these agree with PAINT. Several reviews ACCEPT a NOT on the
    blocked term (CRY1/CRY2 photolyase, ILK kinase, CALR3 calcium binding, UPF3A NMD,
    CPT1C, AGO1 endonuclease). Others REMOVE it (ACTL7A/B, KL, CFLAR peptidase,
    IDH3B).
  - **Stale IBAs:** 24 IBAs in 15 reviews are for terms that PAINT has since blocked
    with an IRD. The current PAINT leaf file no longer emits them, but the cached
    `*-goa.tsv` still carries them, for example yeast SSA1–4, SSB1/2 and SSZ1
    protein refolding, SCHPO pmp20 (6 terms), CFLAR (4) and SLC52A1. Reviewers had
    already REMOVEd or MARK_AS_OVER_ANNOTATED 7 of the 24 on their own, and ACCEPTed 8
    (the rest are MODIFY, UNDECIDED or KEEP_AS_NON_CORE).
  - **Possible NEW-term conflicts:** some core functions or NEW annotations fall on IRD
    terms, for example ACTR1A/ACTR1B "structural constituent of cytoskeleton"
    (IDA, NEW), ANO10/ANO5 scramblase activity (IDA, NEW) and ADAMTSL1 extracellular
    matrix (IDA, NEW). These have direct experimental support, so they are not invalid.
    However, each one now argues against a deliberate PAINT decision and should say so.

### Adjudicated IRD rows (family reviews)

Family reviews can now record a PAINT loss directly: a node assessment carries
`evidence: IRD` (or IKR) and `negated: true`, and takes one of the loss verdicts
LOSS_SUPPORTED, LOSS_CONTRADICTED, LOSS_TOO_BROAD or LOSS_STALE. The validator checks
these against the family's `paint.tsv`. [ird_seed_assessments.yaml](IRD_EVIDENCE/ird_seed_assessments.yaml)
pre-fills an entry for each of the 170 contested IRD rows, leaving only the verdict to
decide. The 18 rows that fall in families with a review have been adjudicated (one more,
TYK2, was already done), each with verbatim supporting quotes:

| Family | IRD node | Blocked term | Verdict | Why, in short |
|---|---|---|---|---|
| PTHR45807 | PTN002910252 | JAK-STAT signalling (TYK2) | LOSS_CONTRADICTED | TYK2 is required for type I IFN, IL-12 and IL-23 signalling |
| PTHR11588 | PTN000172659 | microtubule (gamma-tubulin) | LOSS_CONTRADICTED | gamma-TuRC caps minus ends and is recruited along microtubules; the location stays |
| PTHR11588 | PTN000172659 | structural constituent of cytoskeleton | LOSS_SUPPORTED | gamma-tubulin nucleates, it is not built into the lattice |
| PTHR11588 | PTN000172725 | cytoplasm (plant gamma-tubulin) | LOSS_CONTRADICTED | plant gamma-tubulin works at cytoplasmic sites |
| PTHR24056 | PTN000756102 | protein Ser/Thr kinase activity (CDKL5) | LOSS_CONTRADICTED | CDKL5 phosphorylates serines lost in the kinase-dead mutant |
| PTHR24056 | PTN000623095 | mediator complex (CDK8/19) | LOSS_CONTRADICTED | term-scope change to CKM complex, not divergence; yeast Ssn3 keeps the term |
| PTHR10638 | PTN000067358 | primary methylamine oxidase (AOC3) | LOSS_CONTRADICTED | direct assays in human, mouse and rat; topaquinone mutant is dead |
| PTHR45618 | PTN000642212 | oxidative phosphorylation uncoupler (UCP3) | LOSS_CONTRADICTED | knockouts and overexpression change proton leak; contested, moderate confidence |
| PTHR12210 | PTN002639282 | phosphoprotein phosphatase (TIMM50 clade) | LOSS_SUPPORTED | clade lacks the DxDx(T/V) motif; the outside T. brucei Tim50 keeps it |
| PTHR24068 | PTN000629507 | ubiquitin conjugating enzyme (UEV clade) | LOSS_SUPPORTED | UBE2V1/2 and Mms2 lack the active-site cysteine |
| PTHR21646 | PTN001922764 | cysteine-type deubiquitinase (USP39) | LOSS_SUPPORTED | USP39 lacks the catalytic Cys/His and is inactive in vitro |
| PTHR19375 | PTN001065099 | protein refolding (fungal Hsp70) | LOSS_TOO_BROAD | right for SSB/SSZ1, wrong for SSA (SSA1 seeds the blocked IBD) |
| PTHR11972 | PTN001379754 | ferric-chelate reductase (FRO6) | LOSS_CONTRADICTED | FRO6 has reductase activity in yeast; it differs from FRO7 in location only |
| PTHR11972 | PTN002279285 | superoxide-generating NADPH oxidase | LOSS_TOO_BROAD | blocks the only seed, yeast Yno1/AIM14; plausible for the FRE branches |
| PTHR10196 | PTN000023394 | cytosol (glycerol kinase) | LOSS_CONTRADICTED | the IRD clade contains the human and mouse seeds of the blocked IBD |
| PTHR10648 | PTN000068762 | cytosol (Arabidopsis PP2AA3) | LOSS_CONTRADICTED | PP2AA3 is itself a seed of the blocked IBD |
| PTHR11610 | PTN000176957 | extracellular region (PNLIPRP1) | LOSS_CONTRADICTED | PLRP1 is secreted; the activity IRDs on the same node stand |
| PTHR42884 | PTN001647685 | trans-Golgi network (PCSK1) | LOSS_CONTRADICTED | PC1/3 is seen in the TGN; rat Pcsk1 seeds the blocked IBD; partly term scope |
| PTHR11706 | PTN007528568 | plasma membrane (yeast SMF3) | LOSS_SUPPORTED | Smf3p is vacuolar; the conflicting row is a high-throughput membrane proteome |

So 12 of the 19 contested IRDs look wrong, 5 right, and 2 placed too deep. That is a
sample biased towards conflicts, not an error rate for IRD. Two patterns recur:

- **The IRD clade contains a seed of the IBD it blocks.** This happens for glycerol
  kinase, PP2AA3, PNLIPRP1, PCSK1, Yno1/AIM14 and fungal SSA1. A seed was used as
  evidence that the ancestor had the function, and the IRD then denies it to that same
  protein. This is a mechanical check that could run over all 2,538 IRD rows.
- **A localization IRD that followed an activity change.** PNLIPRP1 lost lipase activity,
  not secretion. CDK8 moved to a more specific complex term rather than leaving Mediator.

### Case study: yeast Hsp70s and "protein refolding"

This one case shows most of what this project found about IRD.

**What PAINT did.** In 2022 PAINT placed an IBD for GO:0042026 protein refolding on
PTN000452648, the ancestor of the cytosolic and mitochondrial Hsp70s (PTHR19375). Its
seeds were yeast SSA1 (`SGD:S000000004`), yeast mitochondrial SSC1 (`SGD:S000003806`)
and six human HSPA proteins. On 2026-06-16 an IRD (PTN001065099, Fungi) stopped that
term descending into all fungal cytosolic Hsp70s. In *S. cerevisiae* the IRD clade holds
four groups:

| Group | Subfamily | Role | Our gene reviews |
|---|---|---|---|
| SSA1, SSA2 | SF395 | general cytosolic chaperones, stress refolding and disaggregation | ACCEPT the refolding IBA; core function |
| SSA3, SSA4 | SF385 | stress-induced SSA paralogs | ACCEPT the refolding IBA; core function |
| SSB1, SSB2 | SF467 | ribosome-associated, fold nascent chains | MODIFY the IBA to protein folding, citing this IRD |
| SSZ1 | SF539 | ribosome-associated complex (RAC) partner of Zuo1 | MODIFY the IBA to protein folding, citing this IRD |

**Verdict: LOSS_TOO_BROAD.** The loss fits SSB and SSZ1, whose job is cotranslational
folding rather than rescuing denatured proteins. It does not fit SSA:

- SSA1 is itself one of the seeds of the IBD the IRD blocks, and SGD has two IDA
  refolding annotations for it: reactivation of denatured luciferase (PMID:18706386) and
  Hsp104/Hsp70/Hsp40 rescue of aggregated proteins (PMID:9674429).
- The fix is to move the IRD down onto the SSB/SSZ1 branch, or remove it, so the SSA
  subfamilies inherit the term again.

**Why the gene reviews look fine but are not settled.**

- **Our cached GOA files predate the IRD.** All seven proteins still carry the refolding
  IBA in their `*-goa.tsv`. In the current PAINT leaf file none of them do.
- **The reviews split the right way, by different routes.** The SSB/SSZ1 reviews were
  written after the IRD existed, saw it, and MODIFYed. The SSA reviews ACCEPTed an
  annotation that has since been withdrawn upstream by a block we judge to be wrong.
- **SSA3 and SSA4 rest on the IBA alone.** SSA1 has its own IDA rows for refolding. SSA2's
  review cites a refolding paper. SSA3 and SSA4 have no experimental refolding annotation
  in GOA; their nearest experimental rows are IGI for the broader GO:0006457 protein
  folding (PMID:9789005).
- **What happens on the next GOA refresh.** Unless PAINT moves the IRD, SSA3 and SSA4
  lose their only refolding annotation. Their reviews would then name a core function
  with no annotation behind it.

**What to do.**

- **PAINT feedback (main action).** Ask for the IRD to be moved to the SSB/SSZ1 branch.
  The evidence: SSA1 is a seed of the blocked IBD, and the SSA paralogs are the canonical
  yeast refolding chaperones.
- **Gene reviews (no change now).**
  - SSA2–4 could add a note that the refolding IBA they accept has been withdrawn
    upstream by an IRD judged too broad (PTHR19375 family review).
  - SSA3 and SSA4 should get literature support for refolding if the IRD stays.

### PAINT slices were missing most IRD rows

While adjudicating these rows we found that `interpro/panther/*/*-paint.tsv`, the
per-family PAINT slices the validator checks against, were missing 1,005 of 1,448 IRD
rows. The slicer found a family's nodes only through leaf IBA rows, and an IRD node
never has any. It now also adds loss nodes whose with/from names a family node, and
uses PANTHER's own node-to-family table (`PAINT_TreeGrafter_Annotations_TOTAL`). The
second source catches a gain whose whole clade is blocked, such as the Yno1 oxidase
IBD. Refreshing the 545 affected slices added 1,340 IRD, 410 IKR and 829 IBD rows and
removed 3 IBD rows.

## Proposed guidance (draft, for discussion)

1. **An IRD is a curator's decision not to annotate. It is not a missing annotation.**
   Before proposing a NEW term from family membership, check whether the gene sits under
   an IRD node for that term (`ird_clade_members.tsv.gz`, regenerated by `fetch_ird_clades.py`). If it does, the
   "comparator check" in CLAUDE.md has already been run by a PAINT curator, and the
   answer was no.
2. **An IRD is not a NOT.** It must not be cited as evidence that the gene lacks the
   function, and it must not be converted into a NOT annotation without gene-level
   evidence (assay or key residues, i.e. IKR).
3. **A reviewed IBA under a fresh IRD should be reconsidered.** Where our cached GOA
   predates the IRD, the IBA is already withdrawn upstream. Prefer REMOVE when the
   biology agrees, or record the disagreement when it does not (SSA1).
4. **Experimental conflicts go to PAINT as feedback.** Where several orthologues under
   one IRD node carry low-throughput experimental positives, the IRD should be
   re-examined.

## Related projects

- [NOT Annotation Usage Audit](NOT_ANNOTATION_USAGE.md): the GOA-level NOT audit; IKR
  NOTs are counted there, IRD cannot be.
- [Top-Nots](TOP_NOTS.md): candidate NOTs mined from our REMOVE decisions. IRD clades
  are a source of candidates that need gene-level evidence first.
- [PAINT](PAINT.md), [IBA Annotation Review](IBA_REVIEW.md) and
  [PANTHER IBA Family Review](PANTHER_IBA_REVIEW.md): these already recommend new IRDs
  in places (NAALADL2, gei-17 JAK-STAT, CIRBP/RBM3 splicing).
- [UniProt CAUTION Note](UNIPROT_CAUTION_NOTE.md).

---
# STATUS

Updated 2026-10-06.

- [x] Extract all IRD rows from PAINT `IBD.gaf` (2,538 rows, 894 families)
- [x] Show that IRD produces no leaf IBA (0 IRD-only NOT|IBA rows)
- [x] Resolve IRD clades from PANTHER trees (52,660 protein rows)
- [x] Cross-check against experimental GOA annotations and our reviews
- [x] Correct the IRD description in `src/ai_gene_review/etl/panther_paint.py`
- [x] Family-review schema and validator support for IRD/IKR loss assessments
- [x] Pre-filled seed assessments for the 170 contested IRD rows (`ird_seed_assessments.yaml`)
- [x] Adjudicate the 18 contested IRD rows in families that already have a review
- [x] Fix the PAINT slicer so IRD nodes are not dropped; refresh the 545 affected slices
- [ ] Adjudicate the remaining 151 seeded IRD rows (their families have no review yet)
- [ ] Run the "IRD clade contains a seed of the blocked IBD" check over all IRD rows
- [ ] Report the fungal Hsp70 refolding IRD (PTHR19375) to PAINT as too broad
- [ ] SSA2–4 gene reviews: note that the accepted refolding IBA was withdrawn upstream;
      find literature support for SSA3/SSA4 refolding if the IRD stays
- [ ] Revisit the 24 stale IBAs in 15 reviews (SSA/SSB/SSZ1, pmp20, CFLAR, SLC52A1, cia30,
      CACNA1G, CASP14, Drd1, Acot1)
- [ ] Add an IRD check to the annotation-reviewer skill, so that IRD clade membership is
      reported when a gene is reviewed
- [ ] Inspect the 14 stale overrides and the 20 fully re-annotated IRD rows
- [ ] Report probable IRD errors to PAINT
- [ ] Confirm with PAINT that gene-level IRD rows (the TAIR CPuORF7 wiki example) are
      no longer exported, and propose an update to the IRD wiki page (current example,
      with/from convention, propagation behaviour, the empty "When IRD should NOT be used"
      and QC sections)

# NOTES

## 2026-10-05

Project started from the NOT annotation audit, which found no IRD among GOA's NOT
annotations. Tracing it showed that IRD exists only in PAINT's node file and is never
propagated as a leaf annotation. Experimental matching uses GO is_a/part_of
descendants of the blocked term, so gamma-tubulin "located_in polar microtubule"
counts as a conflict with a blocked "microtubule". Some conflicts are
therefore term-scope rather than real disagreement, and the worklist needs reading
before anything is sent upstream.

## 2026-10-06

Added loss verdicts to family reviews and adjudicated the 18 contested IRD rows that
fall in reviewed families; the results are above. The adjudication exposed the slicer
bug. The reference validator's "Total checks: 0" on family reviews is not a gap: the
count covers only reported problems, and a fabricated quote is caught.
