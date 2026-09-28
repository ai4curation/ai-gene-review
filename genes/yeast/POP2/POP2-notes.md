# POP2 IBA re-review notes

POP2/CAF1 is the budding-yeast CAF1-family nuclease-module subunit of CCR4-NOT. The four current IBA
rows all trace to `PANTHER:PTN000084083`, the eukaryotic CAF1-family node in `PTHR10797`; none are
pairwise transfers.

## IBA assessment

- `GO:0000288 nuclear-transcribed mRNA catabolic process, deadenylation-dependent decay`: sound.
  The 2024-07-29 IBD at `PTN000084083` is seeded broadly across plants, animals, fission yeast and
  budding yeast. POP2 has direct budding-yeast evidence: Daugeron et al. showed that a `pop2` mutant
  has impaired reporter mRNA degradation and deadenylation intermediates, while Tucker et al. showed
  that Caf1p/Pop2p is required for normal mRNA deadenylation in vivo and co-purifies with a
  Ccr4p-dependent poly(A)-specific exonuclease activity [PMID:11410650; PMID:11239395].
- `GO:0004535 poly(A)-specific ribonuclease activity`: sound. The IBD was refreshed on 2026-05-28 and
  is grounded in experimentally characterized CAF1-family nucleases from fly, mouse, human and fission
  yeast. Yeast Pop2 is divergent and Ccr4 is the primary in vivo catalytic deadenylase, but the
  abstract-only cached Daugeron and Thore papers are enough to verify that recombinant Pop2 degrades
  poly(A) and that active-site mutagenesis localizes intrinsic RNase activity to the Pop2 RNase D
  domain [PMID:11410650; PMID:14618157]. Ohn et al. then refine the in vivo interpretation:
  budding-yeast CAF1 catalytic activity is not required for its deadenylation function, so the
  annotation should be kept as an intrinsic MF, not treated as the main source of CCR4-NOT catalytic
  flux in vivo [PMID:17439972].
- `GO:0000932 P-body`: sound. The 2017 IBD is seeded by budding yeast, mouse and nematode CAF1/CNOT7
  descendants. The budding-yeast seed is not circular; it is direct target evidence used by PAINT to
  place the localization on the ancestral CAF1 node. Reijns et al. report reduced P-body accumulation
  of Ccr4p, Pop2p and Dhh1p after deletion of Q/N-rich regions, which supports Pop2 recruitment to
  P-bodies [PMID:18611963].
- `GO:0030015 CCR4-NOT core complex`: sound. The 2017 IBD is narrower, seeded by budding and fission
  yeast, but it sits exactly on the CAF1-family CCR4-NOT subunit. Yeast complex work placed CAF1/Pop2
  in the 1.0 MDa CCR4-NOT complex, and Basquin et al. later resolved the nuclease-module architecture
  in which Not1 binds Caf1 and Caf1 binds Ccr4 to tether the Ccr4 nuclease domain
  [PMID:11733989; PMID:22959269].

## Cached and newer papers

The core cached literature supports the existing review: PMID:11410650 and PMID:11239395 establish the
deadenylation phenotype and cytoplasmic deadenylase complex; PMID:11889048 establishes Ccr4 as the
main catalytic subunit; PMID:14618157 establishes intrinsic Pop2 RNase activity; PMID:17439972 and
PMID:31611247 show that Pop2's structural/tethering role is often more important in vivo than its own
catalytic activity; PMID:22959269 explains that architecture structurally. The broad protein-binding
rows are still uninformative compared with the complex and activity annotations and should remain
`REMOVE`. The cached transcription papers, PMID:11404327 and PMID:21406554, support the existing
non-core transcription elongation decisions.

The new 2024 EMBO Journal papers retrieved during this re-review make the mRNA-decay model more
nuanced without changing POP2 annotation actions. Audebert et al. rapidly depleted Ccr4/Pop2 and found
that poly(A)-tail changes were often uncoupled from mRNA-stability changes, concluding that
deadenylation is critical for selected regulatory mechanisms but not universally required for yeast
decapping and degradation [PMID:39322754]. Czarnocka-Cieciura et al. used nanopore direct RNA
sequencing and modeling to estimate a transcriptomic enzymatic deadenylation rate near 10 A/min and to
show that heat-stressed ribosomal-protein mRNAs can decay even when Ccr4 and Pan2 are both deleted
[PMID:39394354].
