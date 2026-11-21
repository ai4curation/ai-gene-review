# SEC2 notes

## PTHR14430 / Sec2 review, 2026-11-06

- `just deep-research yeast SEC2 --provider perplexity` did not run in this
  workspace because only the `claude_code` provider is configured. I used the
  cached GOA references plus a manual newer-paper search instead.
- PANTHER `PTHR14430` is the Rabin3/Sec2 Rab GEF family. The relevant PAINT
  rows are `PTN000374167` for inherited Opisthokonta guanyl-nucleotide exchange
  factor activity and `PTN001024876` for a fungal cell-tip active compartment.
  The animal cytosol placement at `PTN002683547` does not cross the fungal
  Sec2 clade.
- The core budding-yeast evidence remains Walch-Solimena et al. 1997 for Sec4
  nucleotide exchange [PMID:9199166], Ortiz et al. 2002 for Ypt31/32-dependent
  recruitment to secretory vesicles [PMID:12045183], and Mizuno-Yamasaki et
  al. 2010 for PI4P binding and the switch between Ypt32 and Sec15 engagement
  [PMID:20493815].
- Sato et al. 2007 resolved the Sec2 coiled-coil GEF-domain dimer
  [PMID:17292842] and Sec4-bound exchange intermediate [PMID:17488829],
  validating both the direct Sec4 interaction and Sec2 self-association without
  making those generic binding rows the main function.
- Geng et al. 2010 showed that the Sec2-Sec4 module contributes to Atg9
  anterograde transport and autophagosome biogenesis during starvation
  [PMID:20444978]. Suda et al. 2018 showed the same GEF module is needed to
  localize Sec4 on prospore membranes during sporulation [PMID:29293994].
  Both are direct but secondary uses of the post-Golgi module.
- Newer primary papers refine the timing and lipid model rather than changing
  the GO decisions. Gingras et al. 2022 imaged the late secretory timeline and
  found Sec2 recruited to Ypt31-positive TGN compartments just before Sec4 and
  Myo2 [PMID:36331188]. Heckle and Kozminski 2023 challenged the older model
  that vesicle-associated PI4P steadily declines between the TGN and plasma
  membrane, but retained the Sec2-centered Ypt32/Sec4/Sec15 handoff near
  docking [PMID:37556206].

## ai4c-reviewer follow-up, 2026-11-06

- Revised the PAINT `GO:0051286` cell-tip IBA from `ACCEPT` to
  `MARK_AS_OVER_ANNOTATED`: the fission-yeast and Candida source species are
  true tip growers, while budding-yeast Sec2 is at the cellular bud tip and bud
  neck during mitotic polarized growth. The supported cell-tip descendant in
  budding yeast is the condition-specific `GO:0043332` mating projection tip.
- Requoted the `GO:0043332` HDA row from the direct SEC2 sentence in
  PMID:19053807 and removed a generic SWAT-methods quote from the bud-neck HDA
  row.
- Clarified that the non-core `GO:0005829` cytosol row corresponds to
  unanchored/diffuse Sec2 rather than the functional vesicle-associated pool.
- Changed the broad sporulation row to `TOO_GENERAL` because the specific
  GO:0032120 prospore membrane formation row is already present from the same
  Suda et al. paper.
