# TRMT6 review notes

Reviewed as a pair with **TRMT61A** (`genes/human/TRMT61A/TRMT61A-notes.md`), which carries the
full write-up of the mRNA-m1A substrate dispute. This file covers what is specific to TRMT6: it is
the **non-catalytic** subunit, and its GOA molecular-function coverage is essentially a single
uninformative `RNA binding` row.

## The problem with TRMT6's MF annotations

`TRMT6-goa.tsv` contains exactly two distinct MF terms:

- `GO:0005515` protein binding — IPI ×6 (three of them the TRMT61A interaction, the rest
  high-throughput interactome hits: KAT5, LMO3, PPIA, SETDB1, YWHAG)
- `GO:0003723` RNA binding — HDA, from a proteome-wide mRNA interactome capture
  [PMID:22658674 "We identify 860 proteins that qualify as RBPs by biochemical and statistical
  criteria"]

Neither says anything about what TRMT6 does. Its actual molecular role has been known at atomic
resolution since 2015 and is simply not represented.

## What TRMT6 actually does

The human complex is a dimer of heterodimers, two TRMT6 + two TRMT61A. TRMT6 is a catalytically dead
paralogue of TRMT61A that has been repurposed as the substrate-binding half of the enzyme:

[PMID:26470919 "a homologous but noncatalytic chain, Trm6, repurposed as a tRNA-binding subunit that
acts in trans"]

Crucially, it does not merely hold the tRNA — it delivers the target base into the partner subunit's
active site, in trans across the dimer interface:

[PMID:26470919 "tRNAs bind across the dimer interface such that Trm6 from the opposing heterodimer
brings A58 into the active site of Trm61."]

and it does so by remodelling the tRNA so that a normally buried base becomes reachable:

[PMID:26470919 "T-loop and D-loop are splayed apart showing how A58, normally buried in tRNA,
becomes accessible for modification."]

The complex is obligate: activity requires both chains
[PMID:16043508 "Stable hTrm6p/hTrm61p complexes purified from yeast maintained tRNA m(1)A Mtase
activity in vitro."], and the two genes are separately essential in yeast
[PMID:16043508 "the tRNA 1-methyladenosine 58 (m(1)A58) methyltransferase (Mtase) is a two-subunit
enzyme encoded by the essential genes TRM6 (GCD10) and TRM61 (GCD14)"].
Site specificity resides in the complex, not in TRMT61A alone
[PMID:16043508 "The human m(1)A Mtase complex also exhibited substrate specificity--modifying
wild-type yeast tRNA(i) (Met) but not an A58U mutant."].

## How that is expressed in GO

Three pieces, all of which already exist in the ontology:

1. **`GO:0000049` tRNA binding** (MF) — a direct, structure-supported specialisation of the HDA
   `GO:0003723` row. Verified against QuickGO to be a descendant of `GO:0003723`.
2. **`GO:0140767` enzyme-substrate adaptor activity** (MF) — definition: *"An adaptor that brings
   together an enzyme and its substrate. Adaptors recruit the substrate to its enzyme, thus
   contributing to substrate selection and specificity."* This is a near-verbatim description of
   the trans-delivery of A58 into the TRMT61A active site. It is the best available MF for what
   TRMT6 itself does, as distinct from what the complex does.
3. **`contributes_to` `GO:0160107`** tRNA (adenine(58)-N1)-methyltransferase activity — the
   complex-level catalytic activity that TRMT6 enables but does not independently possess. The
   schema's `contributes_to_molecular_function` slot exists for exactly this case.

Plus `GO:0031515` tRNA (m1A) methyltransferase complex in `in_complex` (already annotated, IBA/IEA/IPI).

So "subunit of the tRNA m1A58 methyltransferase complex" **is** expressible — the combination above
says it precisely. What is *not* expressible is the specific mechanism (bind tRNA, splay the loops,
present a buried nucleotide to a partner active site), which is why a narrower child of `GO:0140767`
is proposed in `proposed_new_terms` rather than a term for complex membership, which would be
redundant with `GO:0031515`.

`GO:0008047` enzyme activator activity was considered and rejected: TRMT6 is not a regulator that
modulates an otherwise-functional enzyme, it is an obligate structural half of it.

## The mRNA m1A dispute (shared with TRMT61A)

Summary only; see `TRMT61A-notes.md` for the full argument and quotes.

- The mRNA substrate assignment for the complex comes from two 2017 base-resolution studies
  [PMID:29072297 "Within the cytosol, m1A is present in a low number of mRNAs, typically at low
  stoichiometries, and almost invariably in tRNA T-loop-like structures, where it is introduced by
  the TRMT6/TRMT61A complex."] and
  [PMID:29107537 "A different, small subset of m1A exhibit a GUUCRA tRNA-like motif, are evenly
  distributed in the transcriptome, and are dependent on the methyltransferase TRMT6/61A."]
- It is challenged by [PMID:42337368 "Using SCARPET, we show that newly mapped internal m1A sites
  are not m1A, but instead contain inosine from A-to-I editing."], whose conclusion is
  [PMID:42337368 "These results strongly support the conclusion that m1A is not widespread in
  mammalian mRNAs but is instead largely restricted to the previously validated sites in PRUNE1, ND5
  and MALAT1 RNA."]
- That paper is a discriminating assay, not a blanket debunk — it confirmed the equally contested
  internal m7G: [PMID:42337368 "m7G is indeed present as an internal modification at specific mRNA
  sites, with unexpectedly high stoichiometries"].

TRMT6-specific note: GOA gives TRMT6 `GO:0006397` mRNA processing (IDA ×2, the same two 2017 papers)
but **no** `GO:0061953` MF row — the MF sits only on TRMT61A. That asymmetry is correct: the
catalytic activity belongs to the catalytic subunit. TRMT6's contribution to any mRNA methylation is
the same adaptor role, and is not separately annotated here.

The cancer literature asserting abundant TRMT6-deposited mRNA m1A
([PMID:42003777 "Mechanistically, TRMT6-mediated m1A modification enhanced the stability and
translation efficiency of cyclin-dependent kinase 9 (CDK9) mRNA."];
[PMID:40897821 "Mechanistically, TRMT6 reduces SST mRNA levels by inhibiting its stability in an
m1A-YTHDF2-dependent manner, thereby promoting the development of neuroblastoma."]) depends on the
mapping methods under challenge, and reports opposite directions of effect on target stability.
PMID:40897821's title is additionally self-contradictory — it calls TRMT6 an "m1A methylase" that
acts "by demethylating" its target
([PMID:40897821 "m1A methylase TRMT6 promotes neuroblastoma development by demethylating SST mRNA in
an m1A/YTHDF2-dependent manner."]) — while its abstract describes deposition, not removal. No
annotation in this review is supported by it.

## Curation position taken

- `GO:0140767` enzyme-substrate adaptor activity → added as **NEW** (IDA, PMID:26470919). Not in GOA;
  proposed, not asserted as existing curation. It is the MF used by `core_functions`.
- `GO:0003723` RNA binding (HDA) → **MODIFY** to `GO:0000049` tRNA binding. True but uninformative;
  the replacement is supported by the crystal structure rather than by the poly(A)-capture experiment
  itself, and that is stated in the `reason`.
- `GO:0005515` protein binding (IPI ×6) → **MARK_AS_OVER_ANNOTATED**, per project guidance. The one
  interaction that matters (TRMT61A) is already stated properly by `GO:0031515`.
- `GO:0031515` tRNA (m1A) methyltransferase complex (IBA/IEA/IPI) → **ACCEPT**, core.
- `GO:0030488` tRNA methylation (IEA) → **ACCEPT**, core BP.
- `GO:0006397` mRNA processing (IDA ×2) → **KEEP_AS_NON_CORE**, dispute recorded, kept consistent
  with the parallel decision on TRMT61A. Not removed: experimental annotations, full text unseen.
- Nucleus / nucleoplasm → **ACCEPT**.

## Terms verified

All GO ids checked against QuickGO before use: `GO:0000049` MF, `GO:0140767` MF (definition quoted
above), `GO:0160107` MF, `GO:0031515` CC, `GO:0030488` BP, `GO:0006397` BP, `GO:0003723` MF,
`GO:0005634` CC, `GO:0005654` CC, `GO:0060090` MF (parent chain of `GO:0140767`). All cited PMIDs
re-verified against PubMed metadata.
