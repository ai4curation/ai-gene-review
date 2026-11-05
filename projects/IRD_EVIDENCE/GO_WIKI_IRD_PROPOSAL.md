# Proposed update to the GO wiki IRD page: draft

Draft text for [Inferred from Rapid Divergence (IRD)](https://wiki.geneontology.org/index.php/Inferred_from_Rapid_Divergence(IRD)),
last reviewed January 30, 2018. It has not been posted. The behaviour it describes was
measured on PAINT's current `IBD.gaf` and leaf GAF (see [../IRD_EVIDENCE.md](../IRD_EVIDENCE.md));
the PAINT team should confirm it before the page changes.

## Questions for the PAINT team first

1. Are gene-level IRD rows, like the page's TAIR CPuORF7 example, still produced anywhere?
   None appear in the current PAINT exports: the leaf GAF has no IRD evidence and no
   IRD-only NOT|IBA rows.
2. Is "an IRD stops the ancestral IBD from reaching the genes below, and exports nothing
   for them" the intended behaviour, or should an IRD also emit NOT|IBA rows as IKR does?
3. Should an IRD whose ancestral node no longer carries the IBD (14 such rows today) be
   removed when the IBD is withdrawn?

## Proposed text

### Overview

IRD (Inferred from Rapid Divergence, ECO:0000321) is a PAINT evidence code. A PAINT curator
uses it to record that a function annotated by IBD at an ancestral node has been lost, or
diverged beyond recognition, in one clade of the family tree. The IRD is a NOT annotation
on the internal node where the change occurred.

An IRD blocks propagation: the IBD's term is not inherited as IBA by the genes below the
IRD node. It does not create NOT annotations on those genes, so a gene below an IRD simply
receives no IBA for the term. This differs from IKR (Inferred from Key Residues), which
records a loss inferred from missing key residues and does propagate, as NOT|IBA rows on
the genes below.

### Use of the With/From field for IRD

With/From holds the PANTHER node (`PANTHER:PTN...`) of the ancestral IBD whose term the IRD
stops. The reference is `GO_REF:0000033`.

### Example

The ancestral node `PTN002538135` (PTHR21646) carries an IBD for cysteine-type deubiquitinase
activity, seeded by experimentally characterised USPs:

| Node | Qualifier | GO ID | Reference | Evidence | With/From (abridged) | Date |
|---|---|---|---|---|---|---|
| PTN002538135 | | GO:0004843 | GO_REF:0000033 | IBD | UniProtKB:Q8NFA0, SGD:S000002476, ... | 20260529 |
| PTN001922764 | NOT | GO:0004843 | GO_REF:0000033 | IRD | PANTHER:PTN002538135 | 20260529 |

`PTN001922764` is the eukaryote-wide USP39/Sad1 clade (121 members). USP39 lacks the
conserved catalytic Cys and His of USP-type deubiquitinases and is a tri-snRNP component,
so the IRD stops the deubiquitinase IBA from reaching human USP39 and its orthologs. In
the PAINT leaf GAF, human USP39 (Q53GS9) has no row for the term: no IBA and no NOT.

For contrast, an IKR on the vertebrate PGM5 clade (`PTN002731341`, NOT phosphoglucomutase
activity) does reach the genes, for example:

| DB Object ID | Symbol | Qualifier | GO ID | Evidence | With/From |
|---|---|---|---|---|---|
| UniProtKB:Q15124 | PGM5 | NOT\|enables | GO:0004614 | IBA | PANTHER:PTN002731341\|PANTHER:PTN000501426 |

### When IRD should NOT be used

- When residues required for the function are lost: use IKR, which records the evidence
  and propagates NOT|IBA to the genes.
- When only some members of the clade have diverged: place the IRD on the smallest node
  that contains them, or annotate the divergent genes directly with experimental evidence.
- When an experimentally characterised member of the clade still has the function: such a
  gene is often a seed of the IBD being blocked. This was a recurring pattern among the
  contested IRDs in our survey (for example S. cerevisiae SSA1 under the fungal
  protein-refolding IRD in PTHR19375).

### Quality control checks

- The node in With/From carries an IBD for the same term (otherwise the IRD blocks nothing).
- No gene below the IRD node has a positive experimental annotation for the term, unless
  PAINT re-annotates the term on a lower node that contains it.
- The IRD node lies below the IBD node in the family tree.

## Remove

The TAIR CPuORF7 example (`TAIR:AT2G31280`, NOT GO:0004674, With/From
`PANTHER:PTN000357291`). `PTN000357291` is absent from the current `IBD.gaf`, AT2G31280 now
maps to bHLH155 (Q58G01, PTHR46196), and no current PAINT output contains a gene-level IRD
row.
