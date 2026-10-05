---
title: "IRD Evidence: How PAINT Uses Inferred from Rapid Divergence"
maturity: IN_PROGRESS
tags: [EVALUATION, PIPELINE]
species: [human, mouse, rat, yeast, SCHPO, DROME, NEUCR, ARATH]
genes: [SSA1, SSA2, SLC52A1, CFLAR, HDAC6, PIP4K2A, FZD9, ATG16L2, pmp20, cia30]
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

All code and data are in [IRD_EVIDENCE/](IRD_EVIDENCE/). Run the scripts in order
with `uv run python projects/IRD_EVIDENCE/<script>`; RESULTS.md is regenerated each
time. The large PAINT and PANTHER downloads are cached in the git-ignored `.cache/`.

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

## Proposed guidance (draft, for discussion)

1. **An IRD is a curator's decision not to annotate. It is not a missing annotation.**
   Before proposing a NEW term from family membership, check whether the gene sits under
   an IRD node for that term (`ird_clade_members.tsv.gz`). If it does, the
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

Updated 2026-10-05.

- [x] Extract all IRD rows from PAINT `IBD.gaf` (2,538 rows, 894 families)
- [x] Show that IRD produces no leaf IBA (0 IRD-only NOT|IBA rows)
- [x] Resolve IRD clades from PANTHER trees (52,660 protein rows)
- [x] Cross-check against experimental GOA annotations and our reviews
- [x] Correct the IRD description in `src/ai_gene_review/etl/panther_paint.py`
- [ ] Read the top of the experimental-conflict worklist and classify each case as IRD
      wrong, experimental annotation wrong, or term-scope mismatch
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
