# SPT16 re-review notes

## 2026-09-29 IBA and generic binding audit

- Current local PAINT for `PTHR13980` places `GO:0035101` FACT complex on
  `PANTHER:PTN000360139`, seeded by Spt16 descendants from fungi, animals and plants. The
  SPT16 IBA to FACT complex is therefore still a core, supported family transfer.

- GOA's 2025 SPT16 IBA rows for `GO:0006337` nucleosome disassembly and `GO:0032784`
  regulation of DNA-templated transcription elongation also point at `PTN000360139`, but
  the current 2026 local PAINT export no longer carries either exact term. The same node
  now carries `GO:0140673` transcription elongation-coupled chromatin remodeling, which
  is a sibling of nucleosome disassembly under chromatin remodeling and belongs to the
  elongation-process branch rather than the regulation branch. I left the
  `GO:0006337` GOA row accepted as correct yeast biology and modified `GO:0032784` to
  the current FACT-shaped GO:0140673 term.

- The same `PTN000360139` node also carries `GO:0000511` H2A-H2B histone complex
  chaperone activity, seeded by PomBase spt16. Because the 2025 S. cerevisiae Spt16
  IDR paper reports H2A-H2B eviction by Spt16 in vivo, I added a conservative
  `contributes_to` NEW row for this conserved molecular function and wired it into the
  core function as the complex-level chaperone activity.

- The 22 IntAct-derived SPT16 `GO:0005515` rows and the SGD Mot1 `GO:0005515` row were
  still marked `KEEP_AS_NON_CORE`. They were converted to `REMOVE`: the interaction
  evidence itself is not being disputed, but generic protein binding adds no specific FACT
  molecular function when the review already carries direct `GO:0031491` nucleosome
  binding and `GO:0042393` histone binding annotations.

- The two `GO:0042802` identical protein binding rows from high-throughput interactome
  papers were also converted to `REMOVE`. The retained self-interaction rows had only
  absence-of-contradiction support for an Spt16 homodimer, while the literature supports
  Spt16-Pob3 as the functional FACT heterodimer.

- PubMed/web searches for newer SPT16/FACT papers found two 2025 primary studies. PMID:40405832
  dissects how the Spt16 C-terminal IDR promotes H2A-H2B eviction at GAL promoters,
  preinitiation-complex formation and coding-sequence chromatin reassembly in vivo. PMID:39855624
  uses TAP-MS to profile Spt16/FACT-associated proteins and San1-dependent regulation of those
  interactions. These reinforce FACT chromatin/interaction biology but did not require a new GO
  annotation in this review.
