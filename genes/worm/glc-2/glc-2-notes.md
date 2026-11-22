# glc-2 curation notes

## 2026-11-22

`just fetch-gene worm glc-2` seeded 17 GOA rows for reviewed UniProtKB Q17328.
The seeded set is compact: Cys-loop receptor molecular-function parents,
plasma-membrane and postsynaptic-membrane component rows, generic ion-transport
parents, the GluCl-specific molecular-function row, chloride transmembrane
transport, and the automated excitatory-postsynaptic-potential row.

Follow-on fetches:

- `just fetch-gene-pmids worm glc-2` confirmed PMID:7935817 was cached for the
  three direct IDA rows.
- `just mod-description-deep-research worm glc-2` fetched the WormBase curated
  description as `glc-2-deep-research-wormbase.md`.
- `just paint-losses worm glc-2` reported no IRD or IKR loss on the Q17328
  lineage.
- `just deep-research-falcon worm glc-2 --fallback perplexity-lite` could not
  run here because the deep-research client reported that only `claude_code` was
  available and `agentapi` was missing; no provider deep-research file was
  written.

Evidence notes:

- PMID:7935817 is abstract-only in the local cache but is the paper behind the
  direct IDA channel, chloride-transport and plasma-membrane rows. The abstract
  establishes that two C. elegans cDNAs were cloned by Xenopus-oocyte expression
  as avermectin-sensitive glutamate-gated chloride-channel subunits; UniProt
  maps the beta subunit to `glc-2`.
- The Swiss-Prot record gives useful hand-curated detail for the Cully result:
  GLC-2 homomeric channels are activated by glutamate but not by ivermectin,
  while GLC-1/GLC-2 heteromers respond to glutamate and avermectin. I used it to
  avoid overfitting the sparse abstract-only PMID cache.
- The PTHR18945 family review places Q17328 inside the anion-selective
  `PTN001055382` GluCl/glycine-receptor lineage. The lineage is right, but its
  `GO:0005231` excitatory-channel IBD is the sign-bearing assertion that the
  family review flagged as unresolved for this anion-selective node.
- PMID:37811674 shows that `glc-2` and `glc-4` reporters are expressed in
  enteric and anal-depressor muscles, and that loss of either receptor subunit
  suppresses the `ubr-1` expulsion and enteric-muscle calcium defects. This is
  solid native support for inhibitory glutamatergic signaling through GLC-2/4 in
  that circuit, but not a reason to add a broad defecation-process term to
  `glc-2`: the strongest phenotype is in an elevated-glutamate `ubr-1`
  background.

- PMID:9407104 later cached as an abstract and supports coassembly of GluClbeta
  with another alpha subunit, GluClalpha2, into channels gated by both glutamate
  and avermectin.
- PMID:9192499 later cached as an abstract and supports the early pharyngeal
  glc-2 promoter-reporter expression result; PMID:37811674 expands that native
  reporter picture to enteric and anal-depressor muscles, making WormBase's
  pharynx-restricted expression statement outdated.
