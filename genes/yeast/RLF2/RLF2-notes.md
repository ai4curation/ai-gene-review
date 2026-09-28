# RLF2 curation notes

## 2026 IBA re-review

Re-checked all six current RLF2/CAC1 IBA annotations against GOA and the cached
`PTHR15272` PAINT table. Every row traces to the same eukaryotic CAF-1 subunit A
ancestral node, `PANTHER:PTN000392234`:

- `GO:0000510 H3-H4 histone complex chaperone activity`
- `GO:0000785 chromatin`
- `GO:0005634 nucleus`
- `GO:0006334 nucleosome assembly`
- `GO:0006335 DNA replication-dependent chromatin assembly`
- `GO:0033186 CAF-1 complex`

The current actions are sound. Cac1/Rlf2 is the large scaffold subunit of yeast
CAF-1, is part of CAF-1, carries histone- and DNA-binding surfaces, and acts in the
nucleus on chromatin to deposit H3-H4 during replication-coupled assembly. The YAML
already had GOA `supporting_entities`; this pass adds `propagation_review` blocks
that point at the PTN ancestral node as the propagation source and mark all six
rows as `NO_FAILURE_CORE`.

The newer-paper search found a 2026 centromeric-H3-variant review mentioning yeast
CAF-1/Cac1 and the 2024 fission-yeast CAF-1 structural work already discussed in the
Falcon report, but no newer direct budding-yeast Cac1 paper that changes these IBA
calls.
