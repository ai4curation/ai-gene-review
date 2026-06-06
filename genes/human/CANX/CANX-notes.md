# CANX (Calnexin, P27824) curation notes

## Overview
CANX is a type I single-pass ER membrane lectin chaperone, one of the two central
ER lectins of the calnexin/calreticulin cycle. It binds monoglucosylated N-glycans
(Glc1Man9GlcNAc2) on nascent glycoproteins, recruits ERp57 (PDIA3) for oxidative
folding, retains misfolded glycoproteins for ER quality control, and binds calcium.

## Core function evidence

- UniProt FUNCTION [file:human/CANX/CANX-uniprot.txt]:
  "Calcium-binding protein that interacts with newly synthesized monoglucosylated
  glycoproteins in the endoplasmic reticulum. It may act in assisting protein
  assembly and/or in the retention within the ER of unassembled protein subunits.
  It seems to play a major role in the quality control apparatus of the ER by the
  retention of incorrectly folded proteins."

- Topology: lumenal (21-481), transmembrane (482-502), cytoplasmic (503-592). The
  lumenal globular lectin domain + extended P domain (276-409) recruit ERp57 and PPIB.
  Ca2+ binding sites at residues 74, 117, 436; alpha-D-glucoside (glycan) binding at
  164, 166, 185, 192, 425. [file:human/CANX/CANX-uniprot.txt]

- Palmitoylation/translocon: [PMID:22314232 "calnexin, a major ER chaperone involved in
  glycoprotein folding is palmitoylated and that this modification is mediated by the
  ER palmitoyltransferase DHHC6"] and "palmitoylation mediates the association of calnexin
  with the ribosome-translocon complex (RTC)". When supercomplex formation was disrupted,
  "folding of glycoproteins was impaired." This is direct experimental support for ER
  membrane localization and the glycoprotein-folding core function.

- ERAD / quality control: calnexin retains misfolded glycoproteins; the IBA ERAD pathway
  annotation reflects the well-established role of the CNX/CRT cycle feeding terminally
  misfolded clients to ERAD.

- Client-specific chaperone examples (all consistent with the core lectin-chaperone role,
  but client-specific, not the generic function):
  - CHRNA7/α7 nicotinic receptor assembly via NACHO: [PMID:32783947 "NACHO associates with
    the ER oligosaccharyltransferase machinery and with calnexin... NACHO-mediated effects
    on α7 assembly and channel function require N-glycosylation and calnexin chaperone activity."]
  - hERG/KCNH2 [PMID:16361248], CFTR [PMID:16546175, 26618866, 31324722, 36012204],
    SERPINA1/SERPINA2 [PMID:23826168], delta opioid receptor [PMID:20528919], NPC2/Nogo-B
    receptor [PMID:19723497].

## Localization
- ER membrane is the core compartment (IDA, EXP PMID:22314232, multiple IDA).
- Melanosome membrane (PMID:12643545, 17081065): mass-spec detection in melanosome
  fractions; secondary localization of an ER protein, non-core.
- Mitochondrial membrane / MAM contact site (PMID:23455425): MAM localization is real;
  the bare "mitochondrial membrane" subcell mapping is an over-call (calnexin is at the
  ER side of ER-mitochondria contact sites).
- Extracellular exosome (HDA PMID:23533145): high-throughput proteomic; non-core. Note a
  NEGATED exosome annotation from PMID:21235781.
- Presynapse / synaptic vesicle endocytosis / clathrin-dependent endocytosis: derived from
  ortholog (rodent) SGIP1-related receptor-mediated endocytosis role; UniProt notes "may
  play a role in receptor-mediated endocytosis at the synapse." Speculative for human,
  non-core.
- Nuclear membrane (IEA Ensembl): over-call, the ER membrane is continuous with the nuclear
  envelope so this is a propagated contiguity artifact.

## Over-annotations / uninformative
- The large block of GO:0005515 "protein binding" (IPI) annotations come from interactome
  maps (PMID:26496610, 28514442, 29568061, 33961781, 35271311, 40205054, 30021884, 32296183
  via BioPlex/OpenCell/etc.), virus host factor screens (HIV PMID:22190034, 25170080),
  and individual client studies. Per curation guidelines, bare "protein binding" is
  uninformative -> MARK_AS_OVER_ANNOTATED (a few that pinpoint the chaperone-client
  relationship could in principle be MODIFY to unfolded protein binding, but most are
  generic interactome hits).
- RNA binding (HDA PMID:22658674, 22681889): from global mRNA-interactome capture; calnexin
  is not a bona fide RNA-binding protein in a functional sense -> over-annotated.
- Viral protein processing (TAS Reactome, SARS-CoV-2 spike): client-specific application of
  the chaperone cycle; non-core.

## Calcium
- Ca2+ binding (IBA, IEA, TAS PMID:8136357): supported; calnexin contributes to ER Ca2+
  via high-capacity Ca2+ binding in its acidic regions. Core ER property. [PMID:8136357
  cDNA cloning "identification of potential calcium binding motifs"]

## Summary of core functions
1. MF: carbohydrate (monoglucosylated N-glycan) binding lectin / unfolded protein binding
   chaperone activity in the ER.
2. MF: calcium ion binding (ER Ca2+ buffering).
3. BP: protein folding in the ER / glycoprotein quality control (calnexin/calreticulin cycle).
4. BP: ERAD pathway (retention/triage of terminally misfolded clients).
5. CC: ER membrane (lumenal-facing lectin domain).
