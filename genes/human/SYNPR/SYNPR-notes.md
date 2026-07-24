# SYNPR review notes

## 2026-07-18

- Initialized the review with `just fetch-gene human SYNPR`; the fetched GOA contained eight collapsed annotation groups: five cellular-component rows and three generic protein-binding groups.
- The Falcon deep-research request returned HTTP 402 and the configured Perplexity-lite fallback returned HTTP 401 because quota was exhausted. I continued with a clearly labeled manual report in `SYNPR-deep-research-manual.md` and did not create a provider-named deep-research file.
- Added and read cached primary publications PMID:2206533, PMID:8229211, PMID:12974474, PMID:23312519, and PMID:38985768.
- The localization evidence is strong: rodent biochemical fractionation and immunoelectron microscopy place synaptoporin in small synaptic-vesicle membranes; the human record is strongly conserved and brain enriched.
- The recent functional evidence supports redundant organization/clustering of small synaptic vesicles and control of vesicle size. It does not show that synaptoporin is required for all synaptic vesicle formation.
- A separate rodent-neuron study supports a specialized presynaptic requirement at hippocampal mossy-fiber–CA3 synapses during homeostatic structural plasticity.
- I found no direct ion-conductance or solute-flux assay for SYNPR. The early "putative channel" wording is not sufficient for an ion-channel GO molecular-function annotation.
- The three proteome-scale `protein binding` groups are retained only as over-annotation flags; no specific core molecular function is inferred from them.
- Knowledge boundary recorded for validation: "The direct molecular activity of SYNPR has not been established; the early channel designation is putative, and the recent vesicle-size study leaves the mechanism open."
- Independent QA corrected the evidence codes on the five proposed human annotations to `ISS`. PMID:23312519 explicitly used E19 rat hippocampal cultures, so its knockdown, rescue, localization, and plasticity results are ortholog evidence for human SYNPR rather than direct `IMP`/`IDA` evidence. [PMID:23312519, "Hippocampal cultures prepared from E19 rat embryos"]
- PMID:38985768 combines mammalian-protein reconstitution with mouse family genetics, but neither the cached article nor its supporting methods identifies the transfected synaptoporin construct as human Q8TBG9. Its proposed human process annotations are therefore also conservatively represented as `ISS`. [PMID:38985768, "mice lacking all these four proteins have larger SVs"]
