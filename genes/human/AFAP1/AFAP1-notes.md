# AFAP1 review journal

## OpenScientist follow-up (2026-10-05)

Evaluated `AFAP1-hypotheses/kgap-afap1-actin-crosslinking-vs-src-adaptor/openscientist.md`.
The report correctly separates AFAP1's direct actin-filament cross-linking capacity from
its Src/PKC adaptor role and usefully identifies `GO:7770064 actin-filament cross-linking
activity` as the ontology's more specific molecular-function shape. That is now recorded
as support on the existing `GO:0003779 actin binding` and `GO:0060090 molecular adaptor
activity` rows and on the structural/cross-linking knowledge gap.

Follow-up verification: QuickGO resolved `GO:7770064` on 2026-10-05 as current,
with official label `actin-filament cross-linking activity`; its synonyms include
`actin filament cross-linking activity`, `actin filament crosslinking activity`,
and `F-actin cross-linking activity`.

I did not add a `NEW` human `GO:7770064` assertion from this focused report alone.
The load-bearing purified-protein cross-linking papers used avian AFAP-110, not
purified human AFAP1, and the present review still lacks a species/orthology check
that would make an ISS-style human proposal as solid as the direct chicken
biochemistry. I also declined `GO:0051764 actin crosslink formation`: that BP
would require evidence that human AFAP1 itself performs the crosslink-formation
step in cells, not only purified avian MF evidence plus human stress-fiber
perturbation phenotypes. The conservative action is to generalize the existing
generic `GO:0003779 actin binding` row to `GO:0051015 actin filament binding`,
cite the new focused adjudication, and leave exact human cross-linking annotation
scope as the open curation question.
