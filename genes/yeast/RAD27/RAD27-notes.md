# RAD27 / RTH1 (S. cerevisiae, UniProt P26793) — curation notes

## Data provenance for this review

- `RAD27-uniprot.txt`, `RAD27-goa.tsv`: fetched via `just fetch-gene yeast RAD27`; 41 GOA rows seeded.
- Publications: all 15 PMIDs cited by GOA are cached under `publications/`. Abstract-only entries include
  PMID:15342630, PMID:16837458, PMID:7673186, PMID:9121462, PMID:9166764, PMID:11825897, PMID:10025407.
  Full text is available for PMID:41140146, PMID:40064914, PMID:36672839, PMID:20967232 and
  PMID:16079237. PMID:40064914 was added during the 2026 re-review after a newer-paper search.
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

**DNA:RNA hybrids and R-loops.** A 2025 study directly tested purified yeast Rad27 on synthetic R-loop
and 5' flap substrates. Wild-type Rad27 detectably cleaved R-loop 3' boundaries, but several orders of
magnitude less efficiently than flaps; Rad27-E176A failed to cleave R-loop substrates while retaining
flap cleavage. Importantly, Rad27-E176A fully suppressed DNA:RNA hybrid accumulation in Rad27-depleted
cycling cells, and EXO1 overexpression suppressed both the growth defect and hybrid accumulation,
supporting a model in which hybrids arise mainly after flap accumulation rather than because Rad27 is
the limiting direct R-loop resolvase.
[PMID:40064914 "In contrast, while the cleavage of R-loop 3′ boundaries was detectable (Fig. 3b,
right panels), it was several orders of magnitude less efficient than for flaps (Fig. 3d, e)."]
[PMID:40064914 "Using in vitro assays, we found that Rad27-E176A indeed failed to process R-loop substrates,
while it cleaved flaps as efficiently as the wt protein"]

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
misleading about site of action). PTN000871783 is the current PTHR11081 fungal cytoplasm IBD and RAD27
does descend from it, but the target-specific extranuclear site is mitochondrial rather than soluble
cytosolic. Recorded with `propagation_review` (root_cause TERM_SCOPING_PROBLEM; failure modes
COMPARTMENT_OR_COMPLEX_MISMATCH, GRANULARITY_MISMATCH).

**IBA re-review.** RAD27's current GOA IBA rows all trace to `PTHR11081`: PTN000118792 for nucleus and
DNA replication, PTN000118612 for 5'-flap endonuclease activity, PTN000118791 for 5'-3' exonuclease
activity, PTN000871783 for cytoplasm, and PTN008960732 for DNA repair and DNA recombination. The source
for a PAINT row is the PTN ancestral node, not every extant `WITH/FROM` member, so the revised
`propagation_review` blocks use the PTN as the source entity while retaining the full GOA
`supporting_entities` list for traceability. DNA replication remains a TERM_SCOPING_PROBLEM to Okazaki
fragment processing; DNA recombination is defensible but non-core; the other IBA rows are core except
for cytoplasm.

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

**GO:0005515 protein binding IPIs — REMOVE.** The PCNA and Dna2 interactions are real and biologically
important, but the four IntAct rows all use the generic `protein binding` molecular-function term. There
is no specific PCNA-binding or Dna2-binding MF replacement term supported by the cited experiments, and
the functional consequences are already captured by the Okazaki fragment processing, primer removal and
flap endonuclease annotations. These were migrated from the legacy `MARK_AS_OVER_ANNOTATED` action to
`REMOVE` during the 2026 re-review.

## Proposed new annotations

One, from PMID:36672839 (full text cached), with R-loop caveats from PMID:40064914:

- §3.1 and §3.2 (Figures 1–2) assay recombinant *S. cerevisiae* Rad27 alongside human FEN1 on
  lagging-strand RNA:DNA hybrid substrates — nicked RNA and RNA flaps.
  [PMID:36672839 "Recombinant Saccharomyces cerevisiae FEN1 (Rad27) was cloned into T7 expression
  vector pET-24b"]
- §3.3–§3.5 (the R-loop sections) are **human-only**: the reconstituted BER reactions use
  [PMID:36672839 "Recombinant human APE1, pol β, FEN1, and LIG I"] and the recruitment assays are in
  human fibroblasts.

Hence:

- **GO:0004523 RNA-DNA hybrid ribonuclease activity — IDA.** Directly assayed on purified Rad27.
  [PMID:36672839 "We found that both human and yeast FEN1 efficiently cleaved an RNA flap in the
  intermediates using its endonuclease activity."]

The human FEN1 GO:0062176 annotation *is* correctly IDA — those are the human experiments.
PMID:40064914 then assayed purified *S. cerevisiae* Rad27 on synthetic R-loop substrates and found
detectable but very weak R-loop 3' boundary cleavage; because the same paper argues that DNA:RNA
hybrid accumulation in cycling Rad27-depleted cells primarily follows flap accumulation rather than
loss of direct R-loop cleavage, direct yeast R-loop processing should stay a question rather than a
proposed process annotation.

## Citation hygiene notes

Several nucleus annotations originally carried quotes that did not support the compartment claimed
(most seriously, the IBA `GO:0005634 is_active_in nucleus` was supported by the *mitochondrial*
localization sentence from PMID:19699691). Rad27's nuclear localization is genuinely well established,
but it rests on **dataset-level** evidence — the genome-wide GFP-fusion collection (PMID:14562095) and
the curated UniProt subcellular location — not on any Rad27-specific sentence in a cached abstract.
Those entries now carry no `supporting_text` and say so explicitly in `reason`, which is more honest
than attaching a quote that is verbatim but irrelevant. PMID:19699691 is abstract-only, so its nucleus
IDA is accepted in deference to the SGD curator's full-text reading.

## Action tally

42 annotations (41 from GOA + 1 proposed NEW):
ACCEPT 29 · MODIFY 4 · KEEP_AS_NON_CORE 4 · REMOVE 4 · NEW 1.
