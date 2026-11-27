# PA5422 (Q9HTE2) review notes

## Two annotations belong to a different gene

GOA carries two PseudoCAP IMP rows on PA5422 — `GO:0008976` polyphosphate kinase activity and
`GO:0006798` polyphosphate catabolic process — both citing PMID:9734809. The paper is about a
different locus, and the record settles it without needing the full text:

- **The paper names the neighbour, and the neighbour is not this gene.**
  [PMID:9734809 "The gene immediately follows the hemB gene encoding porphobilinogen synthase
  responsible for heme synthesis."] *hemB* in PAO1 is **PA5243** (UniProt Q59643), and the gene
  immediately preceding it is **PA5242**, whose UniProt entry is **P0DP44, `PPK1_PSEAE`, gene
  name `ppk`, "Polyphosphate kinase", 690 residues**. The locus the paper describes is therefore
  PA5242, not PA5422 — the two differ by a transposition of the middle digits.
- **The sizes are incompatible.** The paper describes a PPK "similar to those of PPKs previously
  characterized except that it possesses an extra stretch of 46 amino acids at its N-terminus",
  i.e. *longer* than a typical ~690-residue PPK. Q9HTE2 is **318 residues** — less than half —
  and its only domain is an aldose-1-epimerase β-sandwich (`PF01263`, `IPR008183`).
- **The identical row is already on the right gene.** QuickGO returns `GO:0008976` on P0DP44
  with evidence code **EXP**, citing the same PMID:9734809. The claim is not lost by removing it
  here; it is already recorded where it belongs.
- **The process row is wrong in a second, independent way.** The paper reports
  [PMID:9734809 "ATP-dependent polyphosphate-synthesizing activity was drastically enhanced,
  confirming that the protein is a PPK."] — synthesis. P0DP44 is annotated `GO:0006799`
  polyphosphate *biosynthetic* process. PA5422's row is `GO:0006798` polyphosphate *catabolic*
  process, the opposite direction, which nothing in the paper supports for any gene.

This meets the bar for a confident wrong-gene claim under the repository's rule: the abstract
defines the entity by a neighbouring gene and a size, both of which exclude this protein, and the
intended locus was identified from the genome rather than guessed. Filed as `WRONG_GENE_PRODUCT`
at `CONFIRMED` with `requested_change: DELETE_ROW` against PseudoCAP, the assigning resource for
both rows.

## What the gene actually is

Once the two misattributed rows are gone there is **no experimental evidence on PA5422 at all**;
everything left is computational. The computational case is nevertheless specific rather than
generic:

- `DR InterPro; IPR025532; G6P_1-epimerase.` — a signature for the glucose-6-phosphate
  1-epimerase subfamily, not for the aldose-epimerase fold in general (that is IPR008183, which
  the entry also matches).
- Two active-site residues are placed by a curated PIR site rule:
  `FT ACT_SITE 184 /note="Proton donor" /evidence="ECO:0000256|PIRSR:PIRSR016020-1"`, and the
  same at 287.
- The family assignment itself comes from `PIRNR016020`, a curated UniRule system.

The reaction (α-D-glucose 6-phosphate ⇌ β-D-glucose 6-phosphate, EC 5.1.3.15, RHEA:16249)
interconverts the anomers of glucose 6-phosphate, accelerating a mutarotation that also happens
spontaneously. That is why the enzyme is easy to overlook and why the UniProt name keeps
"Putative": no one has assayed this protein.

The `CC CATALYTIC ACTIVITY` and `CC SIMILARITY` lines carry `ECO:0000256|ARBA:` evidence
alongside the PIRNR evidence, and `PE 3: Inferred from homology` states that the entry rests on
prediction. Neither is used as support here; the subfamily signature and the site rule are.

## Carbohydrate binding

`GO:0030246` comes from `IPR011013` (galactose mutarotase-like domain) and `IPR014718` (GH-type
carbohydrate-binding), both fold-level descriptors of the β-sandwich that *is* the catalytic
domain. The protein does bind a carbohydrate — its own substrate, in its own active site — so
the term is not false, but it describes the substrate-binding half of the epimerase activity
rather than a separate binding function, and neither signature identifies a discrete
carbohydrate-binding module. Marked over-annotated rather than removed.
