# SYT1 (human, P21579) — curation notes

Journal of the GO annotation review of all 175 GOA rows.

## What the protein is

Synaptotagmin-1 is a single-pass synaptic vesicle membrane protein: a short glycosylated
lumenal N-terminus, one transmembrane helix, a charged juxtamembrane linker and two
cytoplasmic C2 domains. UniProt records the topology and the vesicle membrane location
[file:human/SYT1/SYT1-uniprot.txt "Cytoplasmic vesicle, secretory vesicle, synaptic vesicle membrane"],
and the human cloning paper establishes both the abundance on vesicles and the
phosphatidylserine binding of the human cytoplasmic domain
[PMID:1840599 "The cytoplasmic domains of human and Drosophila synaptotagmins produced as recombinant proteins in Escherichia coli specifically bound phosphatidylserine similar to rat synaptotagmin."].

The function is Ca2+ sensing coupled to membrane and SNARE binding, not catalysis or
transport [PMID:27191789 "Synaptotagmin I (Syt I) is a vesicle-localized integral membrane protein that senses the calcium ion (Ca(2+)) influx to trigger fast synchronous release of neurotransmitter."].
Both C2 domains form Ca2+/phospholipid complexes and Ca2+ drives C2-SNARE binding
[PMID:12526776 "Ca(2+) induces binding of the synaptotagmin C(2) domains to SNARE proteins"].

## Core functions settled on

1. `GO:0061891` calcium ion sensor activity, in
   `GO:0099502` / `GO:0098746`, on `GO:0030672`.
2. `GO:0005544` calcium-dependent phospholipid binding.
3. `GO:0000149` SNARE binding (C2B primary interface; oligomeric clamp).
4. `GO:0061891` again for the dense-core granule arm, in `GO:0045956` on `GO:0031045`.

The selectivity of the knockout for the fast phase is what makes this a sensor claim
rather than a required-cofactor claim
[PMID:12526776 "in synaptotagmin 1 knockout mice, the fast component of both Ca(2+)- and Sr(2+)-induced release is selectively impaired"].

## Judgement calls

- **21 bare `GO:0005515` protein binding rows removed.** The cited studies (Cav beta4a,
  SCAMP5, S100A13, NEMO microarray, GPCR mapping, the binary-interactome and
  cell-map papers) identify partners, not activities, and none supports a more
  informative MF for SYT1. The interactions are not being called false; the
  informative binding activities are annotated separately as SNARE binding,
  syntaxin-1 binding, Ca2+-dependent phospholipid binding and PI(4,5)P2 binding.
- **Fusion-execution terms modified to the activation term.** SYT1 does not perform
  fusion; the SNAREs do. `GO:0006906`, `GO:0031629`, `GO:0016192`, `GO:2000300` and
  `GO:0150037` were all modified to `GO:0099502`, which the gene already carries. Reactome
  states the role the same way [Reactome:R-HSA-210430 "Ca2+ influx initiates a cascade of events in which the Ca2+ sensing protein, synaptotagmin-1 (sty-1) is central."].
- **`GO:0061588` calcium activated phospholipid scrambling removed.** Scrambling is
  carried out by dedicated scramblases; Ca2+-dependent binding and loop penetration of
  an anionic membrane changes no leaflet composition. This row is an ortholog-based IEA
  with no human evidence. The rat SYT1 review reached the same verdict on the rodent rows.
- **`GO:0006855` xenobiotic transmembrane transport flagged, not removed.** The receptor
  role behind it is real — the lumenal domain exposed after fusion is the botulinum B/G
  receptor [Reactome:R-HSA-5244397 "binds ganglioside GT1b and syntagmin 1 or 2 (SYT1 or 2) on the plasma membrane of a human target cell"]
  — but translocation is done by the toxin heavy chain, not by SYT1.
- **Cytoplasm modified to synaptic vesicle membrane.** An integral membrane protein whose
  C2 domains face the cytosol is not a cytoplasmic protein, and no functional soluble
  pool is documented [file:human/SYT1/SYT1-deep-research-claude-code.md "I found no primary evidence for a functional soluble pool."].
  The IDA row cites a DYRK1A distribution study whose cached full text does not mention
  synaptotagmin at all; recorded as MISCITED in the reference review.
- **Postsynaptic terms flagged.** `GO:0014069`, `GO:0045211`, `GO:0099524` and
  `GO:0060080` are ortholog-based electronic rows on a presynaptic vesicle protein;
  recovery of an abundant presynaptic protein in postsynaptic preparations is the
  expected contaminant.
- **The clamp kept as a real, separate claim.** `GO:0046929` negative regulation of
  neurotransmitter secretion is kept (non-core) because loss of SYT1 raises spontaneous
  release [file:human/SYT1/SYT1-deep-research-claude-code.md "Loss of Syt1 increases spontaneous (miniature) release in many preparations and unmasks asynchronous release."].
  Keeping it beside the positively-signed evoked terms is deliberate: they are different
  claims about different phases.
- **Endocytosis kept non-core, in two senses.** SYT1 promotes the rate of retrieval
  [file:human/SYT1/SYT1-deep-research-claude-code.md "Syt1 promotes the rate of vesicle retrieval after exocytosis."]
  and is itself cargo retrieved through stonin 2, SV2 and AP-2
  [Reactome:R-HSA-8863463 "retrieve plasma-membrane localized synaptic vesicle proteins such as the synaptotagmin (SYT) family after synaptic vesicle release"].
  Only the first is participation; both are secondary to the fusion role.
- **`GO:0050750` LDL particle receptor binding left UNDECIDED.** The cited LRP1b
  knockout paper is cached abstract-only and the abstract does not mention
  synaptotagmin. The curator read the full text; nothing in reach lets me adjudicate it.
- **`GO:1903861` dendrite extension kept non-core with a caveat.** UniProt attributes
  the melanocyte dendrite role to SYT1 on the basis of PMID:23999003, whose abstract
  names SYT14L. Worth resolving against the full text.

## Divergences from the rat SYT1 review

Same verdict on almost everything. Three differences, all on terms where the rat rows
were experimental and the human rows are electronic: `GO:0031629` and `GO:0006906`
(rat ACCEPT from IDA, here MODIFY to `GO:0099502`, since the human rows are IEA and SYT1
activates rather than executes fusion), `GO:0014069` postsynaptic density and
`GO:0045211` postsynaptic membrane (rat KEEP_AS_NON_CORE from a proteomics IDA, here
MARK_AS_OVER_ANNOTATED for an IEA with no human evidence), and `GO:7770062` vesicle
membrane tethering activity (rat core; here non-core, because bridging is one of several
competing accounts of the triggering step).

## Open

How Ca2+-bound C2B triggers fusion is genuinely unresolved — curvature, bridging,
clamp release and the lever model are all live, and recent all-atom work argues against
curvature and bridging. This is the one recorded knowledge gap behind the suggested
experiments.
