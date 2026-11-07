# petA (Q88N95, PP_1317) — curation notes

Rieske 2Fe-2S subunit of the respiratory cytochrome bc1 complex of *Pseudomonas
putida* KT2440. Notes below record the provenance for the mechanistic claims made
in `petA-ai-review.yaml`, which the UniProt record alone does not carry.

## Identity: respiratory Rieske, not a ring-hydroxylating oxygenase

This discrimination matters in *Pseudomonas*, whose genomes encode many
Rieske-domain oxygenases for aromatic-compound catabolism. Three independent lines
place PP_1317 in the respiratory bc1 family instead:

- The petABC operon architecture. The bacterial bc1 complex "is encoded by the
  petABC operon" and comprises three subunits [PMID:15948965 "Bacterial cytochrome
  bc1-complex encoded by the petABC operon consists of three subunits, the Rieske
  iron-sulphur protein, the b-type cytochrome, and the c1-type cytochrome."].
  PP_1317/1318/1319 are exactly this triple; flanking genes are unrelated.
- The high-potential cluster. Purified bacterial PetA Rieske proteins give
  "E(m) values of +275 mV" [PMID:15948965 "Electron paramagnetic resonance (EPR)
  spectroscopy and midpoint potential measurements showed typical [2Fe-2S] signals
  and E(m) values of +275 mV for both Rieske proteins."], against roughly -150 mV
  for the low-potential oxygenase ferredoxins. UniProt records the same family-level
  property directly: "The Rieske protein is a high potential 2Fe-2S protein."
  (`petA-uniprot.txt`).
- Direct sequence markers. The OpenScientist synthesis
  (`petA-deep-research-openscientist.md`) reports the His2Cys2 ligand boxes
  Cys124/His126 and Cys154/His155, the cluster-stabilizing Cys129-Cys152 disulfide,
  and the redox-tuning Ser157. These were checked against the Q88N95 sequence in
  `petA-uniprot.txt` during PR review and match.

Also worth stating explicitly because the symbol collides: this is **not** the
chloroplast/cyanobacterial *petA* (apocytochrome f of the b6f complex). The
organism and the "iron-sulfur subunit" RecName exclude that reading.

## Topology and the Tat route

UniProt gives "Cell membrane" and "Single-pass membrane protein" but does not say
which side the head domain faces or how it gets there. Two experimental papers in
other bacteria supply that, and it is the reason `GO:0005886` rather than a
periplasm term is the right location call:

- The 2Fe-2S cluster is assembled in the cytoplasm, so PetA must be exported already
  folded — the twin-arginine translocation pathway's defining capability.
  In *Legionella pneumophila*, "the Tat pathway is necessary for correct membrane
  insertion of L. pneumophila PetA" [PMID:17188684 "We conclude that the Tat pathway
  is necessary for correct membrane insertion of L. pneumophila PetA."].
- In *Shewanella oneidensis*, PetA is identified as "the Rieske Fe-S subunit of the
  ubiquinol-cytochrome c reductase" and its Tat signal is **not** cleaved — it is
  retained as the N-terminal membrane anchor [PMID:23593508 "the signal sequence in
  PetA appears to be resistant to cleavage after the protein is inserted into the
  cytoplasmic membrane."].
- Consistent with both, the Q88N95 InterPro set includes `IPR006311 TAT_signal` and
  PROSITE `PS51318 TAT`, and the sequence opens with a twin-arginine motif at
  residues 10-12 (`petA-deep-research-openscientist.md`).

Whether the P. putida signal is cleaved has not been tested; that is recorded as a
`suggested_question` rather than asserted.

## Why GO:0008121 was MODIFYed rather than kept or simply flagged

`GO:0008121` quinol-cytochrome-c reductase activity (EC 7.1.1.8) is the whole-complex
reaction: "It couples electron transfer from ubiquinol to cytochrome c with generation
of proton motive force which fuels ATP synthesis" [PMID:21996020 "It couples electron
transfer from ubiquinol to cytochrome c with generation of proton motive force which
fuels ATP synthesis."]. PetA contributes one step of it — abstracting the first
electron from quinol and handing it to cytochrome c1 — and cannot perform the
reaction alone.

The earlier draft of this review used `MARK_AS_OVER_ANNOTATED` with no replacement,
which left petA with no molecular function at all: its GOA has no `GO:0009055` row
(only 0005886, 0008121, 0016020, 0051537, 1902600), so 2Fe-2S binding would have
been the only MF left standing. `MODIFY` to `GO:0009055` is both the accurate call
and the repo precedent for this exact subunit and term — see
`genes/human/UQCRFS1/UQCRFS1-ai-review.yaml` and
`genes/worm/isp-1/isp-1-ai-review.yaml`.

## Why GO:1902600 is non-core here but core for petB

Proton translocation is quinone chemistry at the Qo and Qi sites, and both sites lie
within PetB. PetA's contribution is to force the bifurcation that makes the Q cycle
protonmotive: "This bifurcation is the essence of the protonmotive Q-cycle, releasing
2 H⁺ to the periplasm per QH₂ oxidized" (`petA-deep-research-openscientist.md`). The
term is therefore kept as a complex-level consequence on petA and accepted as a
direct process on petB. `UQCRFS1-ai-review.yaml` treats this same term on this same
subunit type the same way. Note also that the GOA row is itself an inter-ontology
inference from `GO:0008121` (GO_REF:0000108), whose `enables` attribution this review
modifies.

## Physiological context

The bc1 complex is the obligatory entry point of the cytochrome *c* branch of a
branched chain: "Pseudomonas putida KT2440 contains a branched aerobic respiratory
chain with several terminal oxidases" [PMID:16958757 "Pseudomonas putida KT2440
contains a branched aerobic respiratory chain with several terminal oxidases."]. The
parallel quinol-oxidase branch gives partial redundancy, so loss of bc1 is not
necessarily lethal aerobically — relevant if knockout phenotypes are used as evidence
later.

## Evidence caveats

Every mechanistic paper cited here was performed in a bacterial homolog
(*Rubrivivax*, *Paracoccus*, *Legionella*, *Shewanella*), not in *P. putida*. The
one P. putida paper, PMID:16958757, concerns the terminal oxidases rather than petA.
The Q88N95 entry itself is unreviewed TrEMBL at PE 3 (inferred from homology). The
review's claims rest on family conservation plus the congruence of family, domains,
operon context and sequence markers — which is why the proposed complex-membership
and respiratory-chain annotations carry `ISS`, not an experimental code.
