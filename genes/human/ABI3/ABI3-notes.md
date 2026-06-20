# ABI3 - ABI Gene Family Member 3 (Human) Notes

## Overview

Human ABI3 (Q9P2A4), also known as NESH, is an ABI-family adaptor protein with
an N-terminal WAVE-binding region, proline-rich regions, and a C-terminal SH3
domain. Its most defensible core function is as an Abi-subunit option in the
WAVE regulatory complex (WRC/SCAR complex), where it modulates actin-dependent
cell projection, lamellipodium, and migration phenotypes.

Key evidence anchors:
- UniProt describes ABI3 as an ABI-family protein and records cytoplasmic
  localization: "Belongs to the ABI family" and "Cytoplasm"
  [file:human/ABI3/ABI3-uniprot.txt].
- The Falcon synthesis identifies ABI3 as an "ABI-family adaptor protein" and
  an "Abi subunit option" within the WRC [file:human/ABI3/ABI3-deep-research-falcon.md].
- The primary NESH/WAVE study supports WRC membership: "Immunoprecipitation
  revealed that NESH (Abi-3) is present in the Abi/WAVE complex" [PMID:17101133].
- The WAVE2-complex study supports ABI3-specific protrusion effects: "the
  formation of peripheral lamellipodial structures was disturbed" [PMID:26428302].
- The Falcon synthesis reports that ABI3 is microglia-enriched and that Abi3
  loss reduces microglial dynamic surveillance area to about 52-53% in knockout
  mice versus about 73-75% in wild type [file:human/ABI3/ABI3-deep-research-falcon.md].

## Core Function Synthesis

ABI3 should be curated primarily as a signaling adaptor/WRC component that tunes
Arp2/3-dependent actin organization. The review treats SCAR/WAVE complex
membership, actin cytoskeleton organization, regulation of cell migration, and
negative regulation of lamellipodium assembly as the main functional axis.

ABI3 is not an enzyme or transporter. Broad migration, tumor-suppression, immune,
or Alzheimer disease model phenotypes are best interpreted through the WRC and
microglial actin/surveillance mechanism unless direct biochemical evidence
supports a more specific molecular function.

The actin-filament-binding annotations remain an evidence gap. They are plausible
from ABI-family/WRC biology, but a direct intrinsic ABI3 actin-binding activity
should not be assumed without purified-protein assays.

## Alzheimer-Relevant Biology

ABI3 is a replicated late-onset Alzheimer disease risk gene, especially through
the S209F variant. For this GO review, the biologically grounded disease-relevant
axis is microglial actin regulation: WRC composition, process extension,
ramification, migration, phagolysosomal state, and plaque engagement. Hypotheses
about downstream disease progression should stay outside core GO function
curation unless they can be reduced to evolved ABI3 molecular or cellular
functions.

Mouse model evidence is useful but must be interpreted carefully. Several studies
use Abi3/Gngt2 locus perturbations, and the Falcon report notes model-dependent
effects on amyloid versus tau phenotypes. This supports mechanistic caution:
curate the actin-adaptor and microglial surveillance biology, not a generic
"Alzheimer progression" function.

## Second-Pass Review Notes

The ABI3 review already validated cleanly and had second-pass cleanup recorded
in the project log before this notes file was added. The remaining gap was the
absence of a local notes journal. No YAML action changes were made in this pass.

Open expert questions already captured in the YAML:
- Does ABI3 directly bind actin filaments, or does it only regulate actin through
  WRC/adaptor functions?
- How does ABI3 expression differ between microglia, neurons, and other CNS cell
  types under physiological conditions?
- How does the S209F Alzheimer risk variant alter WRC incorporation,
  phosphorylation, migration, phagocytosis, and microglial surveillance?
- How do phosphorylation sites S213, S216, and S342 regulate ABI3 stability and
  WRC incorporation in vivo?
