# tse5 (PA2684, Q9I0F4) — review notes

Tier-3 PseudoCAP review. `tse5` was added to batch 5 because it carries `GO:0097351`, the term
on which the merged `tse6`/`tsi6` pair holds a recorded wrong-gene divergence. It turns out to
be a third instance of the same inversion, from a different paper.

## The gene

Swiss-Prot **reviewed** (TSE5_PSEAE, 1317 aa), and named from one of the two papers cited here:

`[file:PSEAE/tse5/tse5-uniprot.txt "Toxin secreted by the H1 type VI (H1-T6SS) secretion system that acts on bacterial target cells."]`
`[file:PSEAE/tse5/tse5-uniprot.txt "The producing bacterium is protected by a cognate immunity protein."]`

Both carry `ECO:0000269` tied to PubMed:24589350 and PubMed:24794869 — curated text anchored to
the very publications the annotations cite, which is the strongest support available. The
immunity partner is named on the record:
`[file:PSEAE/tse5/tse5-uniprot.txt "Deletion mutant together with deletion of its cognate immunity protein Tsi5 leads to a significant loss of fitness advantage"]`

Architecture: `DUF6531`, `RHS`, `Rhs_assc_core`, six `RHS_repeat`s, `YD`, and the family
assignment `[file:PSEAE/tse5/tse5-uniprot.txt "DR   InterPro; IPR050708; T6SS_VgrG/RHS."]`. So
Tse5 is the Rhs-type polymorphic toxin PMID:24794869 calls RhsP1:
`[PMID:24794869 "VgrG1c is involved in the delivery of an Rhs protein, RhsP1."]`

## `GO:0097351` is the immunity protein's function, annotated to the toxin

`GO:0097351 toxin sequestering activity` is defined as binding a toxin to prevent it acting —
what an immunity protein does. Tse5 is the toxin, so the relationship is inverted, exactly as
the merged `tse6` review found for its own gene, where the same term from the same
effector-immunity experiment had been entered on both halves of the bicistron.

Three statements establish the direction without reading beyond what is quoted here: the
curated `FUNCTION` (Tse5 is the toxin; something *else* protects the producer), the curated
`DISRUPTION PHENOTYPE` (that something is **Tsi5**), and the paper
(`[PMID:24794869 "The RhsP1 C terminus carries a toxic activity, from which the producing bacterium is protected by a cognate immunity."]`).

`REMOVE`, with `WRONG_GENE_PRODUCT` / `REPOINT` at `CONFIRMED` to **P0DTB6** (TSI5_PSEAE,
Immune protein Tsi5, gene `tsi5` / PA2683.1). That accession was resolved through the UniProt
API, not guessed — `tsi5` has no folder in this corpus to read it from.

This is the **third** instance: `tse6` (confirmed, merged), `tsi6` (the correct half of that
pair), and now `tse5` from a different paper and a different effector family. Worth recording
as a pattern rather than three isolated slips — a pair-level toxin/immunity experiment tends to
be entered against both genes, and the immunity-side term lands on the toxin. A
reference-level sweep of `GO:0097351` across the T6SS effector genes would likely find more.

## `GO:0033103` — accepted on the same structural basis as tse6, after a correction

Both rows (IDA, IMP) are `ACCEPT`ed. Recording how I got here, because my first reading was
wrong.

The merged `tse6` review is explicit that cargo status alone does **not** earn this term —
being carried by a secretion system is being its substrate, and a substrate is not a
participant. It accepts the term on *structural* grounds: Tse6 is an evolved PAAR protein, and
PAAR repeats cap the VgrG spike, so it supplies a component the apparatus depends on.

My first pass concluded that this basis did **not** transfer to tse5, because tse5's InterPro
list contains no PAAR signature while tse6's carries `IPR008727 PAAR_motif`, and because
PMID:24794869 describes VgrG1c as *delivering* RhsP1, which is cargo language. On that reading
I was going to accept the rows on a visibly weaker footing.

That was an error, and PMID:24589350 — full text, in the cache, cited on the IDA row — says so
directly:

`[PMID:24589350 "our screen failed to identify two predicted H1-T6SS effectors, Tse5 and Tse6, which differ from Hcp-stabilized substrates by the presence of toxin-associated PAAR-repeat motifs"]`
`[PMID:24589350 "our data suggest that the PAAR domain-containing effectors, Tse5 and Tse6, do not require Hcp for stability and display a strict functional requirement for their cognate VgrG proteins"]`

The paper groups Tse5 *with* Tse6 as PAAR domain-containing effectors, and explains what the
domain does:
`[PMID:24589350 "it also likely functions as a protein-protein interaction module that tethers effectors to VgrGs"]`
— alongside a structural role at the spike tip. It also notes that PAAR repeats occur in
`[PMID:24589350 "PAAR repeats are found in many putative toxins including rearrangement hot-spot/tyr-asp (RHS/YD)-repeat containing proteins"]`,
which is precisely tse5's RHS/YD architecture.

So the structural basis applies to tse5 on the same footing as tse6, and the rows are accepted
on the same grounds rather than on a weaker inference.

**The lesson is the one CLAUDE.md states about negative results.** I treated "no PAAR in the
InterPro list" as evidence of absence, when it was absent-signature rather than absent-domain:
InterPro coverage of divergent PAAR regions is incomplete. The check that caught it was reading
the paper already sitting in the cache with `full_text_available: true`, which I had skipped on
the assumption that the record told me enough. A negative drawn from a database listing needs
the same scrutiny as a negative drawn from a query.

That signature gap is itself worth noting as an observation: InterPro annotates no PAAR motif on
Q9I0F4, although the primary literature describes the protein as PAAR-containing. Recorded here
rather than filed as a source defect, since it is a signature-coverage limitation rather than a
wrong assertion.

## Curation gap

`tsi5` (P0DTB6, PA2683.1) has no folder in this corpus, so the `GO:0097351` repoint cannot be
checked against a sibling review the way the `tse6`/`tsi6` pair could be. Reviewing `tsi5`
would complete the pair and confirm from the other side, as `femI` did for `femA`. A curation
gap, not a knowledge gap.
