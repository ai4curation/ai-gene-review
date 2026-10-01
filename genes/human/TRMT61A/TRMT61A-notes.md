# TRMT61A review notes

Reviewed as a pair with **TRMT6** (`genes/human/TRMT6/TRMT6-notes.md`). The two proteins form
one obligate heterotetrameric enzyme, so the two review files are kept consistent: TRMT61A is
the catalytic subunit, TRMT6 the non-catalytic substrate-binding subunit.

## Why this gene was selected

Contested **substrate class**. GOA carries two molecular functions for TRMT61A:

- `GO:0160107` tRNA (adenine(58)-N1)-methyltransferase activity — EXP (PMID:16043508), IBA, IEA
- `GO:0061953` mRNA (adenine-N1-)-methyltransferase activity — **IDA** ×2
  (PMID:29072297, PMID:29107537)

The enzyme itself is not in doubt. What is contested is whether mRNA is a real substrate class,
because the transcriptome-wide m1A mapping methods that produced the mRNA assignments have
disputed specificity, and a 2026 biochemical validation paper concludes that most mapped internal
mRNA "m1A" is in fact inosine.

## The tRNA m1A58 activity (not contested)

The two-subunit architecture and the activity were established in yeast and then shown to be
conserved in humans:
[PMID:16043508 "the tRNA 1-methyladenosine 58 (m(1)A58) methyltransferase (Mtase) is a two-subunit
enzyme encoded by the essential genes TRM6 (GCD10) and TRM61 (GCD14)"] and
[PMID:16043508 "Stable hTrm6p/hTrm61p complexes purified from yeast maintained tRNA m(1)A Mtase
activity in vitro."]

Site specificity was demonstrated directly by the A58U substrate mutant:
[PMID:16043508 "The human m(1)A Mtase complex also exhibited substrate specificity--modifying
wild-type yeast tRNA(i) (Met) but not an A58U mutant."]

The crystal structure of the human complex bound to tRNA3(Lys) confirms the stoichiometry and the
division of labour:
[PMID:26470919 "a homologous but noncatalytic chain, Trm6, repurposed as a tRNA-binding subunit
that acts in trans"] and
[PMID:26470919 "tRNAs bind across the dimer interface such that Trm6 from the opposing heterodimer
brings A58 into the active site of Trm61."]

The mechanism of access to a buried base is also resolved:
[PMID:26470919 "T-loop and D-loop are splayed apart showing how A58, normally buried in tRNA,
becomes accessible for modification."]

This is the core function, and nothing in the 2025-2026 literature challenges it.

## The mRNA m1A activity (contested)

### What the two IDA papers actually say

Importantly, the two papers GOA cites for `GO:0061953` are themselves the **sceptical**,
base-resolution papers that cut the earlier antibody-based m1A maps down from thousands of sites
to a handful. They are not maximalist claims:

[PMID:29072297 "Within the cytosol, m1A is present in a low number of mRNAs, typically at low
stoichiometries, and almost invariably in tRNA T-loop-like structures, where it is introduced by
the TRMT6/TRMT61A complex."]

and the same paper's overall conclusion is that mRNA m1A is something cells avoid:
[PMID:29072297 "m1A on mRNA, probably because of its disruptive impact on base pairing, leads to
translational repression, and is generally avoided by cells"]

The independent base-resolution study agrees on the same narrow, structure-driven substrate class:
[PMID:29107537 "A different, small subset of m1A exhibit a GUUCRA tRNA-like motif, are evenly
distributed in the transcriptome, and are dependent on the methyltransferase TRMT6/61A."]

This is mechanistically coherent rather than surprising: the complex recognises its substrate by
**structure** (the T-loop, splayed open by TRMT6 as above), so an mRNA that folds into a T-loop-like
element is a legitimate, if adventitious, substrate. UniProt's own annotation records exactly this
qualified reading ("N(1) methylation takes place in tRNA T-loop-like structures of mRNAs and is
only present at low stoichiometries").

### The 2026 challenge

[PMID:42337368 "Using SCARPET, we show that newly mapped internal m1A sites are not m1A, but
instead contain inosine from A-to-I editing."]

and the paper's bottom line:
[PMID:42337368 "These results strongly support the conclusion that m1A is not widespread in
mammalian mRNAs but is instead largely restricted to the previously validated sites in PRUNE1, ND5
and MALAT1 RNA."]

SCARPET is a **discriminating** method rather than a blanket debunk of epitranscriptomics — applied
to the equally controversial internal m7G, it confirmed the modification:
[PMID:42337368 "m7G is indeed present as an internal modification at specific mRNA sites, with
unexpectedly high stoichiometries"]

Two things follow that matter for how far the challenge reaches:

1. The target of the SCARPET refutation is the **newly mapped** sites from the evolved reverse
   transcriptase (Zhou et al. 2019), not the Safra/Li 2017 sites. The 2017 base-resolution studies
   are cited approvingly.
2. SCARPET **positively confirms** nuclear-encoded mRNA m1A at PRUNE1 (A58) and at the MALAT1
   lncRNA: [PMID:42337368 "SCARPET unambiguously identified m1A in ND5 and PRUNE1 mRNA, and in
   MALAT1 lncRNA, in agreement with previous studies"] and
   [PMID:42337368 "Overall, our data suggest that m1A is not a widespread modification but instead
   is limited to just the PRUNE1 mRNA, ND5 mRNA and MALAT1 lncRNA in mammalian cells."]

   Caveat (recorded honestly): PMID:42337368 **never mentions TRMT6 or TRMT61A**. It does not itself
   attribute the confirmed PRUNE1/MALAT1 sites to this complex. The attribution would have to come
   from the 2017 papers, which state that the cytosolic sites are TRMT6/TRMT61A-dependent and lie in
   tRNA T-loop-like contexts. Connecting the two is an inference, not something either paper asserts,
   and it is flagged as such in `suggested_questions`. (ND5 is mitochondrial and is TRMT10C's, not
   this complex's — PMID:29072297 is explicit about that.)

So the net effect of the 2026 work is to **narrow** the mRNA substrate class to a handful of
T-loop-like sites, not to abolish it.

### The opposing stream: cancer mRNA-m1A papers

A separate literature continues to report abundant, functionally consequential TRMT6/TRMT61A-deposited
mRNA m1A driving tumour phenotypes:

- [PMID:41103012 "TRMT61A boosted the mRNA stability of one cut homeobox 2 (ONECUT2), which in turn
  triggered son of sevenless homolog 1 (SOS1) transcription"], concluding
  [PMID:41103012 "we established that TRMT61A promoted CRC tumorigenesis and progression by
  enhancing the mRNA stability of critical targets in an m1A-dependent manner"].
- [PMID:42003777 "Mechanistically, TRMT6-mediated m1A modification enhanced the stability and
  translation efficiency of cyclin-dependent kinase 9 (CDK9) mRNA."]

These rest on m1A-seq / MeRIP-type mapping, i.e. precisely the class of method PMID:42337368 argues
is unreliable for internal mRNA m1A. Note also that the direction of effect is inconsistent across
this literature — CRC and HCC papers report m1A **stabilising** target mRNAs, while the
neuroblastoma paper reports m1A **destabilising** its target via YTHDF2
([PMID:40897821 "Mechanistically, TRMT6 reduces SST mRNA levels by inhibiting its stability in an
m1A-YTHDF2-dependent manner, thereby promoting the development of neuroblastoma."]).
Opposite directions are not fatal on their own (reader context can differ), but combined with a
shared methodological dependency they lower the weight of this stream considerably.

**A sceptical line on PMID:40897821 specifically.** Its title is internally incoherent: it calls
TRMT6 an m1A *methylase* and simultaneously says it acts *by demethylating* its target —
[PMID:40897821 "m1A methylase TRMT6 promotes neuroblastoma development by demethylating SST mRNA in
an m1A/YTHDF2-dependent manner."] — while the abstract describes the opposite, deposition:
"TRMT6 mediates m1A modification of SST". A writer cannot demethylate. This is at best sloppy
wording that survived peer review; it is not a reason to dismiss the data outright, but it is a
reason not to lean on this paper for any mechanistic claim, and no annotation in this review is
supported by it.

## Curation position taken

- `GO:0160107` tRNA (adenine(58)-N1)-methyltransferase activity (EXP, IBA, IEA) → **ACCEPT**, core.
  Direct biochemistry, structure, and a sound phylogenetic assertion all converge.
- `GO:0061953` mRNA (adenine-N1-)-methyltransferase activity (IDA ×2) → **KEEP_AS_NON_CORE**,
  with the methodological dispute recorded in `reason`. Explicitly **not REMOVE**: these are
  experimental annotations whose full texts are not in the cache (`full_text_available: false` for
  both), CLAUDE.md forbids overruling an IDA from an abstract, and the cited papers are the
  conservative ones, not the discredited antibody maps. Non-core because even on their own account
  the sites are few and sub-stoichiometric, the substrate recognition is a structural spillover from
  tRNA recognition rather than a separate evolved function, and the 2026 biochemistry narrows the
  set further.
- `GO:0006397` mRNA processing (IDA ×2, same two papers) → **KEEP_AS_NON_CORE** for the same reason
  and to keep the action consistent with the MF it derives from.
- `GO:0006396` RNA processing (IEA/ARBA) → **MODIFY** to `GO:0030488` tRNA methylation. Correct but
  a distant ancestor: `GO:0030488` is a descendant of `GO:0006396` (verified against QuickGO), and
  the gene already carries the specific term.
- `GO:0005515` protein binding (IPI ×4) → **MARK_AS_OVER_ANNOTATED** per project guidance. The
  biologically meaningful interaction (TRMT6, UniProtKB:Q9UJA5, three of the four rows) is already
  captured far better by `GO:0031515`.
- Nucleus/nucleoplasm and complex terms → **ACCEPT**.

## Terms verified

All GO ids used were checked against QuickGO (id, label, aspect, obsolescence) rather than recalled:
`GO:0160107` MF, `GO:0061953` MF, `GO:0031515` CC, `GO:0030488` BP, `GO:0006396` BP, `GO:0006397` BP,
`GO:0005634` CC, `GO:0005654` CC. Ancestry check confirming `GO:0006396` ⊃ `GO:0030488` was run
against the QuickGO ancestors endpoint.

All cited PMIDs were re-verified against PubMed metadata (title, journal, year) before use.
