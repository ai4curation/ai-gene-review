# RAD27 / RTH1 (S. cerevisiae, UniProt P26793) — curation notes

## Data provenance for this review

- `RAD27-uniprot.txt`, `RAD27-goa.tsv`: fetched via `just fetch-gene yeast RAD27`; 41 GOA rows seeded.
- Publications: all 15 PMIDs cited by GOA are cached under `publications/`. Abstract-only entries include
  PMID:15342630, PMID:16837458, PMID:7673186, PMID:9121462, PMID:9166764, PMID:11825897, PMID:10025407.
  Full text is available for PMID:41140146, PMID:36672839, PMID:20967232 and PMID:16079237.
- **Deep research: no usable output.** `just deep-research-falcon yeast RAD27 --fallback perplexity-lite`
  failed: falcon returned HTTP 402 (no credits on the Edison Scientific platform) and the perplexity
  provider is not configured here. The asta provider ran and produced `RAD27-deep-research-asta.md`, but
  all 19 retrieved papers are unrelated to RAD27 or FEN1 (M. tuberculosis annotation, avian immunome DB,
  bovine sperm proteome, etc.). The file is retained as the genuine provider artifact but contributed
  nothing to this review. A re-run with a working provider is worthwhile.
- `UV_PYTHON=3.12` must be exported before any `just deep-research-*` recipe: `uvx` otherwise resolves
  Python 3.11 and `deep-research-client` requires >=3.12.

## Function summary as used for the review

Rad27 is the budding-yeast FEN1 orthologue: a Mg2+-dependent, structure-specific XPG/RAD2-family nuclease.

**Substrate specificity is the most precisely characterized aspect.** Rad27p prefers a *double*-flap
substrate and the 3' tail of the upstream primer, not the 5' flap, sets the cut site:
[PMID:11825897 "Cleavage was most efficient when the upstream primer contained a 1-nucleotide 3'-tail as
compared with the fully annealed upstream primer traditionally tested."]
[PMID:11825897 "The site of cleavage was exclusively at a position one nucleotide into the annealed
region, allowing human DNA ligase I to seal all resulting nicks."]
It discriminates among branch-migration isomers of the same substrate:
[PMID:11825897 "FEN1 only cleaved those containing a 1-nucleotide 3'-tail."]
This is why every Rad27 product is directly ligatable and why Rad27 and Cdc9 must act in an ordered way.

**Exonuclease activity.** Purified as the pol alpha-associated 5'→3' exonuclease before it was recognized
as the RAD27 product:
[PMID:9166764 "Peptide sequence analysis of the purified 47 kDa exonuclease was carried out, and the
peptide sequence was found to be identical to the S. cerevisiae gene YKL510 encoded polypeptide, which is
also known as yeast RAD2 homolog 1 or RTH1 nuclease."]

**Two primer-removal routes.** Reconstitution shows the short-flap/Rad27-only route dominates, with a
minor Dna2-dependent long-flap route:
[PMID:16837458 "One proposed pathway for flap removal involves pol delta displacement of long flaps,
coating of those flaps by replication protein A (RPA), and sequential cleavage of the flap by Dna2
nuclease followed by flap endonuclease 1 (FEN1)."]
[PMID:16837458 "Results showed that in the presence of PCNA and FEN1, pol delta displacement synthesis
favors formation and cleavage of primarily short flaps, up to eight nucleotides in length"]
Genetically, DNA2 and RAD27 are synthetically lethal and their products co-purify:
[PMID:9121462 "dna2-1 rad27/rth1 delta double mutants are inviable, indicating that the mutations are
synthetically lethal."]

**PCNA ordering.** PIP-box alleles establish that PCNA sequences Rad27 and Cdc9 entry into fragment joining:
[PMID:16079237 "These results suggest that PCNA mediates the entry of the flap endonuclease and DNA ligase
I into the process of Okazaki fragment joining, and this ordered entry is necessary to prevent CAG repeat
tract expansions."]

**Repeat instability — the strongest in vivo phenotypes.**
CAG tracts: [PMID:16079237 "Among replication mutations that destabilize CAG repeat tracts, mutations of
RAD27, encoding the flap endonuclease, and CDC9, encoding DNA ligase I, increase the incidence of repeat
tract expansions to the greatest extent."]
rDNA (2025, full text available): [PMID:41140146 "Here, we demonstrate that Rad27/FEN1, a
structure-specific nuclease in budding yeast, plays a crucial role in maintaining the stability of the
ribosomal DNA (rDNA) repeats."] — and importantly the mechanism is *not* break-mediated:
[PMID:41140146 "The rad27Δ mutant accumulates Okazaki fragments in the rDNA region, without inducing the
formation of detectable DSBs."] with partial redundancy:
[PMID:41140146 "Furthermore, Exonuclease 1 and PCNA partially compensate for the loss of Rad27 in rDNA
stabilization."]

**Mitochondrial pool.**
[PMID:19699691 "Our findings demonstrate that Rad27p/FEN1 is localized in the mitochondrial compartment of
both yeast and mice and that Rad27p has a significant role in maintaining mtDNA integrity."]

## Decisions that needed judgement

**GO:0005737 cytoplasm, IBA `is_active_in` — MODIFY to GO:0005739 mitochondrion.** This is the one IBA
localization call I changed. "Active in cytoplasm" implies a cytosolic site of action, but Rad27's
substrate is DNA; the only extranuclear compartment where it has a demonstrated substrate is the
mitochondrion (which is part_of cytoplasm, so the parent is not *false*, just uninformative and
misleading about site of action). The PANTHER seed set (PTN000871783, EXO1, RAD27 itself) does not
support cytosolic activity for any member. Recorded with `propagation_review`
(root_cause TERM_SCOPING_PROBLEM; failure modes COMPARTMENT_OR_COMPLEX_MISMATCH, GRANULARITY_MISMATCH).

**GO:0005829 cytosol (IDA, PMID:22932476) — KEEP_AS_NON_CORE, not REMOVE.** The source is a hypoxia
relocalization screen whose stated focus is SWI/SNF
[PMID:22932476 "we have found that over 120 nuclear proteins with important functions ranging from
transcriptional regulation to RNA processing exhibit altered cellular locations under hypoxia."].
Rad27 is one of the surveyed nuclear proteins. I did not overrule the SGD curator — the observation is
plausible as a condition-dependent redistribution — but it is peripheral, since there is no cytosolic
substrate. The same paper's nucleus IDA was accepted outright.

**GO:0007534 gene conversion at mating-type locus (IMP, PMID:10025407) — KEEP_AS_NON_CORE.** Real and
specific assay, but mechanistically it reports the *same* lagging-strand requirement as the core Okazaki
role; the authors interpret strand invasion as creating a modified replication fork
[PMID:10025407 "Surprisingly, mutants of lagging strand replication, DNA polymerase alpha (pol1-17), DNA
primase (pri2-1), and Rad27p (rad27 delta) also greatly inhibit completion of DSB repair, even in
G1-arrested cells."]. Not a mating-type-specific function of Rad27.

**GO:0006303 NHEJ (IDA, PMID:15342630) — KEEP_AS_NON_CORE.** Well supported biochemically
[PMID:15342630 "we demonstrated that FEN-1(Rad27) physically and functionally interacted with both Pol4
and Dnl4/Lif1 and that together these proteins coordinately processed and joined DNA molecules with
incompatible 5' ends."], but Rad27's contribution is 5'-end trimming, not a core identity. Parallels the
MMEJ flap-trimming role Reactome assigns to human FEN1.

**PMID:9166764 title names DNA polymerase alpha, not RAD27 — annotation NOT second-guessed.** The
abstract explicitly identifies the purified protein as the RTH1/RAD27 gene product by peptide sequencing,
so the 5'-3' exonuclease IDA is correctly attributed. Flagged as VERIFIED in `reference_review`.

**No REMOVEs.** Nothing in the RAD27 set is contradicted by evidence; the weakest entries (cytosol,
`protein binding` IPIs) are downgraded rather than deleted.

## Proposed new annotations

Two, both from PMID:36672839 (full text cached), which assayed yeast and human FEN1 side by side:

- **GO:0004523 RNA-DNA hybrid ribonuclease activity** (IDA) — RAD27 currently lacks any RNase H-type
  annotation although human FEN1 has one.
  [PMID:36672839 "We found that both human and yeast FEN1 efficiently cleaved an RNA flap in the
  intermediates using its endonuclease activity."]
- **GO:0062176 R-loop processing** (IDA) — gives a process context to that activity.
  [PMID:36672839 "Our study provides the first evidence that FEN1 endonucleolytic cleavage can result in
  the resolution of R-loops via the BER pathway, thereby maintaining genome integrity."]

The matching GO:0062176 annotation was also proposed for human FEN1.

## Action tally

43 annotations (41 from GOA + 2 proposed NEW):
ACCEPT 29 · MODIFY 4 · KEEP_AS_NON_CORE 4 · MARK_AS_OVER_ANNOTATED 4 · NEW 2 · REMOVE 0.
