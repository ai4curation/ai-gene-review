# HEXA (Beta-hexosaminidase subunit alpha, UniProtKB:P06865) — review notes

## Summary of biology (grounded in UniProt P06865, GOA, cached publications)

HEXA encodes the alpha subunit of lysosomal beta-hexosaminidase, a glycoside
hydrolase family 20 (GH20) enzyme (EC 3.2.1.52). Three isozymes exist, defined by
subunit composition [file:human/HEXA/HEXA-uniprot.txt "isozyme A ... is a heterodimer
composed of one subunit alpha and one subunit beta"; "isozyme S (hexosaminidase S) is
a homodimer of two alpha subunits"]:
- Hex A = alpha-beta heterodimer (HEXA + HEXB)
- Hex B = beta-beta homodimer (HEXB only)
- Hex S = alpha-alpha homodimer (HEXA only)

The enzyme hydrolyses terminal non-reducing beta-linked N-acetyl-D-hexosamine
(beta-GalNAc/GlcNAc, including sulfated hexosamine) residues from glycoconjugates
[file:human/HEXA/HEXA-uniprot.txt "Hydrolyzes the non-reducing end N-acetyl-D-hexosamine
and/or sulfated N-acetyl-D-hexosamine of glycoconjugates"].

The alpha-subunit active site is uniquely able, together with the GM2-activator
protein (GM2A), to hydrolyse the GM2 ganglioside (removing terminal GalNAc to give
GM3). Only Hex A (which contains alpha) does this in vivo
[PMID:16698036 "Only the alpha-subunit active site can hydrolyze GM2 gangliosides";
PMID:8672428 "Heterodimeric hexosaminidase A (alpha beta) is the only isozyme that can
hydrolyze GM2 ganglioside in vivo, requiring the presence of the GM2 activator protein"].
The alpha active site preferentially handles negatively charged/sulfated substrates,
so Hex A/Hex S also degrade sulfated glycosaminoglycan (GAG) fragments (dermatan
sulfate, keratan sulfate) and the sulfated glycosphingolipid SM2
[PMID:11707436 "active on water-soluble and amphiphilic glycoconjugates including
artificial substrates, sulfated GAG fragments, and the sulfated glycosphingolipid SM2";
PMID:6458607 "Incubation of keratan sulfate-derived oligosaccharides with
beta-N-acetylhexosaminidase A analogously resulted in the liberation of
N-acetylglucosamine-6-sulfate"].

Localisation: lysosome / lysosomal lumen (acidic acid-hydrolase compartment)
[file:human/HEXA/HEXA-uniprot.txt "Lysosome"]. The alpha chain requires association with
the beta chain for catalytic maturation and lysosomal transport
[PMID:6230359 "association with beta-chains is necessary not only for acquisition of
catalytic activity but also for transport of alpha-chains to lysosomes"].

Disease: loss of HEXA activity causes GM2-gangliosidosis type 1 (Tay-Sachs disease),
an autosomal-recessive lysosomal storage disorder with neuronal GM2 accumulation
[file:human/HEXA/HEXA-uniprot.txt "GM2-gangliosidosis 1 (GM2G1)"; "accumulation of GM2"].

## Core functions selected
- MF: GO:0004563 beta-N-acetylhexosaminidase activity (exact GOA term/label; EC 3.2.1.52)
- BP: GO:0006689 ganglioside catabolic process (GM2 degradation; alpha-specific)
- BP: GO:0030203 glycosaminoglycan metabolic process (dermatan/keratan sulfate GAG turnover)
- CC: GO:0043202 lysosomal lumen; GO:0005764 lysosome
- Complex (in_complex): GO:1905379 beta-N-acetylhexosaminidase complex (Hex A alpha-beta)

## Notable curation decisions
- GO:0008375 acetylglucosaminyltransferase activity (IEA ARBA + IDA PMID:25645918):
  biologically wrong direction — HEXA is a hydrolase (GH20), not a glycosyltransferase.
  The PMID:25645918 azurophil-granule paper describes N-glycan **trimming (hydrolysis)**,
  not sugar transfer. REMOVE the electronic ARBA inference; the experimental IDA is
  marked MARK_AS_OVER_ANNOTATED (do not REMOVE an experimental annotation) — the
  underlying activity is hydrolytic N-glycan trimming, better captured by GO:0004563.
- GO:0006024 glycosaminoglycan biosynthetic process (IDA PMID:25645918): mis-assigned
  process direction — the paper is about catabolic N-glycan trimming, not GAG
  biosynthesis. Experimental → MARK_AS_OVER_ANNOTATED (retain hydrolytic/catabolic
  reading via GO:0004563 / GO:0030203).
- GO:0005515 protein binding (3× IPI, all HEXA-HEXB IntAct): uninformative bare
  protein-binding; MARK_AS_OVER_ANNOTATED. The biologically meaningful heterodimerization
  is separately captured by GO:0046982 (IDA) and GO:1905379 complex membership.
- Extracellular region / azurophil granule / exosome / membrane: peripheral secretion/
  proteomics detections of a normally lysosomal enzyme → KEEP_AS_NON_CORE.
- Reactome R-HSA-9035976 "Defective HEXA does not cleave..." (TAS): a *defective*-variant
  reaction; the enables GO:0004563 annotation derived from it is retained (activity is
  correct for wild-type) but flagged in reason.
