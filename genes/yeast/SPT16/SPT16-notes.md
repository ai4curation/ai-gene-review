# SPT16 re-review notes

## 2026-09-29 IBA and generic binding audit

- Current local PAINT for `PTHR13980` places `GO:0035101` FACT complex on
  `PANTHER:PTN000360139`, seeded by Spt16 descendants from fungi, animals and plants. The
  SPT16 IBA to FACT complex is therefore still a core, supported family transfer.

- GOA's 2025 SPT16 IBA rows for `GO:0006337` nucleosome disassembly and `GO:0032784`
  regulation of DNA-templated transcription elongation also point at `PTN000360139`, but
  the current 2026 local PAINT export no longer carries either exact term. The same node
  now carries `GO:0140673` transcription elongation-coupled chromatin remodeling, which is
  consistent with FACT's conserved role as a histone chaperone coupled to RNA polymerase
  elongation but is narrower than the old process terms. I left the two GOA rows accepted
  as correct yeast biology and recorded the source as stale for the exact transferred term.

- The 22 IntAct-derived SPT16 `GO:0005515` rows and the SGD Mot1 `GO:0005515` row were
  still marked `KEEP_AS_NON_CORE`. They were converted to `REMOVE`: the interaction
  evidence itself is not being disputed, but generic protein binding adds no specific FACT
  molecular function when the review already carries direct `GO:0031491` nucleosome
  binding and `GO:0042393` histone binding annotations.

- PubMed/web searches for newer SPT16/FACT papers found two 2025 primary studies. PMID:40405832
  dissects how the Spt16 C-terminal IDR promotes H2A-H2B eviction at GAL promoters,
  preinitiation-complex formation and coding-sequence chromatin reassembly in vivo. PMID:39855624
  uses TAP-MS to profile Spt16/FACT-associated proteins and San1-dependent regulation of those
  interactions. These reinforce FACT chromatin/interaction biology but did not require a new GO
  annotation in this review.
