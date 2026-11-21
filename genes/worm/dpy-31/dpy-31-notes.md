# dpy-31 notes

## 2026-11-20

- Seeded the review with `just fetch-gene worm dpy-31`; this fetched the
  reviewed UniProtKB P98060 record, the GOA rows, and the full text of PMID:
  15579684.
- `just deep-research-falcon worm dpy-31 --fallback perplexity-lite` could not
  run because neither provider was configured in this checkout. No provider
  deep-research file was written; manual evidence notes are kept here.
- `just mod-description-deep-research worm dpy-31` fetched the WormBase
  hand-written gene description as
  `dpy-31-deep-research-wormbase.md`. Its main claims trace back to Novelli et
  al. 2004: DPY-31 is a BMP-1/tolloid-family astacin zinc metalloprotease,
  dpy-31 mutants have defective collagenous cuticles and embryonic/larval
  lethality, and genetic suppressors in the SQT-3 C terminus implicate DPY-31
  in C-terminal procollagen processing [PMID:15579684].
- `just paint-losses worm dpy-31` reported no IRD or IKR loss on the P98060
  lineage, so there is no PAINT loss to reconcile for the DPY-31
  metalloendopeptidase or extracellular-region IBA rows.
- The abstract-only Stepek, McCormack and Page paper extends the C. elegans
  pathway to parasite orthologs: Haemonchus contortus dpy-31 rescues the C.
  elegans dpy-31 body-form defect, and recombinant H. contortus and Brugia
  malayi DPY-31 enzymes process C. elegans SQT-3 at the correct C-terminal
  procollagen processing site [PMID:19883650].
- Curation decision: accept the metalloendopeptidase, zinc-binding,
  extracellular, molting-cycle and cuticle-development rows as the direct DPY-31
  biology; keep the broad `proteolysis` process as non-core; mark generic
  `metallopeptidase activity` as too general beside the accepted
  `metalloendopeptidase activity` rows.
