# CRYAA Gene Review Notes

## 2026-05-30 - PROTEOSTASIS PN small-HSP positive-control pass

Full review is present and marked complete. The local review supports CRYAA/HSPB4 as a small heat-shock-protein holdase and lens structural protein. It explicitly treats the chaperone activity as ATP-independent aggregation suppression rather than active refolding: the existing `GO:0051082 unfolded protein binding` annotation is marked `MODIFY` to `GO:0140309 unfolded protein carrier activity`, and `GO:0042026 protein refolding` is rejected. [file:human/CRYAA/CRYAA-ai-review.yaml; PMID:8943244; PMID:18407550]

PN curation conclusion: the PN placement under `Cytonuclear proteostasis > Chaperone > small HSP system > small HSP` is a good positive control. Propagation to a broad chaperone term such as `GO:0044183 protein folding chaperone` is biologically reasonable as a bridge from PN small-HSP membership, but curator-facing displays should keep the local holdase distinction visible so this is not interpreted as evidence for foldase/refolding activity.
