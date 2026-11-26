# kgb-1 review notes

## GO-CAM 568b0f9600000284 consistency notes

- The KGB-1 activity in `gomodel:568b0f9600000284` is mis-typed as bare `GO:0005515` protein binding. The gene product is a JNK-like MAP kinase; the model should use `GO:0004705` JUN kinase activity or `GO:0004707` MAP kinase activity instead.
- The model's KGB-1 biological-process context, `GO:1900181` negative regulation of protein localization to nucleus, captures only the adult DAF-16 nuclear-localization effect from PMID:22554143. The same pathway has the opposite effect during development, and the activity is a side branch that never rejoins the intestinal antibacterial PMK-1 to ATF-7 to effector output.
- The model should either add the DAF-16 input and explicit adult context or drop KGB-1 from this antibacterial model; VHP-1's negative regulation of PMK-1 is the antibacterial contribution.

## Deep research

- 2026-11-24: Automated deep-research provider attempts were unavailable in this checkout. `deep-research-falcon` reported no usable Falcon or Perplexity provider, and `deep-research-claude-code` could not run because the provider was not logged in. The review used the fetched GOA, UniProt, WormBase MOD description, PAINT-loss check, GO-CAM review context, and local cached PMID files instead.
