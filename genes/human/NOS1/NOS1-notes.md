# NOS1 review notes

Seed: NOS1, a reviewed human Swiss-Prot nitric-oxide synthase in PANTHER
PTHR43410.

`just deep-research-claude-code human NOS1` was attempted after `just
fetch-gene human NOS1`, but the provider failed before writing a
`NOS1-deep-research-claude-code.md` file:

> claude_code: success Not logged in - Please run /login -- the API key is
> missing, invalid, or lacks access to this endpoint.

No manual file was written under a provider-style `-deep-research-*.md` name.
The review instead used the fetched UniProt record, the GOA-seeded publication
caches, Reactome records, the cached PTHR43410 family review, and
`interpro/panther/PTHR43410/PTHR43410-paint.tsv`.

`just paint-losses human NOS1` reported that P29475 is not a leaf of the cached
PTHR43410 tree and therefore losses could not be checked at the leaf level; no
IRD or IKR loss was reported for the NOS1 lineage.

Main curation decisions:

- Keep nitric-oxide synthase activity, L-arginine catabolism, nitric oxide
  biosynthesis, calmodulin binding, heme, tetrahydrobiopterin, FMN, FAD and
  NADP binding as the conserved NOS catalytic core.
- Keep sarcolemmal, synaptic, dendritic and sarcoplasmic-reticulum contexts as
  non-core NOS1 local signaling locations or processes where they rest on human
  nNOS papers or conservative mammalian orthology.
- Remove every bare `GO:0005515` row under the project protein-binding policy,
  preserving each interaction row and its own `WITH/FROM` entity.
- Mark broad ARBA/Compara transfers such as generic signaling, broad blood
  circulation, LPS response, hormone response and transcriptional regulation as
  over-annotations because they do not name a direct NOS1 execution step.
- The `GO:0032991 protein-containing complex` ISS row was changed to MODIFY because
  the informative complex is the sarcolemmal dystrophin scaffold: the Cell paper
  showed that "nNOS partitions with skeletal muscle membranes owing to association
  of nNOS with dystrophin" [PMID:7545544].
- The `GO:0035605 peptidyl-cysteine S-nitrosylase activity` row was left
  UNDECIDED: the Alzheimer's disease paper shows NOS1-dependent changes in
  S-nitrosylation after miR-132/212 depletion, but does not separate direct
  transnitrosylase activity from excess diffusible NO produced by NOS1
  [PMID:28089352].
- A second review pass kept `GO:0045776 negative regulation of blood pressure`
  as a non-core NOS-family vascular-tone output instead of a bad-PAINT call,
  kept the human `PMID:28089352` neuron-apoptosis IMP as a non-core NOS1 neural
  output, and changed the `PMID:7545544` myoblast-fusion TAS row to UNDECIDED
  because the abstract verifies nNOS-dystrophin anchoring but cannot rule out a
  myoblast-fusion author statement in the full text.
