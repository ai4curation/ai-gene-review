---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADAMTSL1
affinage_run_date: 2026-06-09T22:02:41
uniprot_accession: Q8N6G6
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADAMTSL1 (human)

## Current model (mechanistic narrative)

ADAMTSL1 (punctin) is a secreted, hatchet-shaped extracellular matrix glycoprotein built from four thrombospondin type I repeats but lacking the metalloprotease and disintegrin-like domains of catalytic ADAMTS family members, and it is deposited in a punctate pattern into the cell substratum [PMID:11805097]. Its secretion is governed by post-translational modification: C-mannosylation of Trp42 within a W-x-x-W motif is required for proper folding and export, and the disease-associated p.Trp42Arg substitution abolishes secretion, causing intracellular retention and a dominant-negative reduction in secretion of co-expressed wild-type protein [PMID:28722276]. Its thrombospondin repeats additionally carry the glucose-β1,3-fucose disaccharide added by B3GLCT [PMID:18720094], and the mature protein is a direct proteolytic substrate of MMP10 [PMID:24281761], placing ADAMTSL1 within a regulated ECM remodeling context. Functionally, the C. elegans ortholog MADD-4 acts as a secreted UNC-40/DCC-dependent midline guidance cue, implicating the family in nervous system patterning [PMID:22014523], while in mammals ADAMTSL1 marks a Pmp2+ myelinating Schwann cell subtype that ensheathes large-caliber motor axons [PMID:35115729]. ADAMTSL1 expression is also responsive to Hedgehog signaling and modulates chondrosarcoma proliferation [PMID:24634412]. Direct biochemical demonstration of an enzymatic activity for the mammalian protein has not been established in the available corpus.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** *(none)*
- **localization:** GO:0005576 extracellular region, GO:0031012 extracellular matrix
- **pathway (Reactome):** *(none)*
- **partners:** B3GLCT, MMP10
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | High | ADAMTSL1 (punctin) is a secreted glycoprotein that lacks the pro-metalloprotease and disintegrin-like domains of ADAMTS proteases but contains four thrombospondin type I repeats. It is processed by signal peptidase (N-terminus: EEDRD), contains a single N-linked glycosylation site, harbors disulfide bonds, and adopts a hatchet-shaped conformation with a globular region and short stem as shown by rotary shadowing. In transfected COS-1 cells, it is deposited in the cell substratum in a punctate fashion and excluded from focal contacts. | PMID:11805097 | The Journal of biological chemistry |
| 2009 | Medium | ADAMTSL1 carries the rare glucose-β1,3-fucose disaccharide modification on its thrombospondin type I repeats (TSRs), placed there by the β1,3-glucosyltransferase B3GLCT. This O-linked fucose modification on TSR-containing proteins is disrupted in Peters'-plus syndrome. | PMID:18720094 | Annals of medicine |
| 2013 | Medium | ADAMTSL1 is a direct substrate of matrix metalloproteinase 10 (MMP10); MMP10 cleaves ADAMTSL1 in fibroblast secretomes as identified by time-resolved terminal amine isotopic labeling of substrates (TAILS) degradomics. | PMID:24281761 | Molecular & cellular proteomics : MCP |
| 2014 | Medium | ADAMTSL1 regulates chondrosarcoma cell proliferation downstream of Hedgehog (Hh) pathway signaling; ADAMTSL1 expression is reduced by the SMO inhibitor IPI-926, and manipulation of ADAMTSL1 levels affects chondrosarcoma neoplastic proliferation. | PMID:24634412 | Molecular cancer therapeutics |
| 2017 | High | A heterozygous missense mutation p.Trp42Arg in ADAMTSL1 abolishes secretion of the protein; the mutant protein is retained intracellularly and exerts a dominant-negative effect by reducing secretion of co-transfected wild-type ADAMTSL1. Trp42 is the site of C-mannosylation, implicating this modification as necessary for proper ADAMTSL1 folding/secretion. | PMID:28722276 | Human mutation |
| 2021 | Medium | C-mannosylation of the first Trp in the W-x-x-W/C motif of ADAMTSL1 (at Trp42) is critical for protein folding, sorting, and secretion; a disease-associated variant disrupting this motif (p.Trp42Arg) confirms the functional importance of this modification in vivo. | PMID:34500691 | Molecules (Basel, Switzerland) |
| 2011 | Medium | The C. elegans ortholog MADD-4 (most closely related to mammalian ADAMTSL1 and ADAMTSL3) is a secreted guidance cue from dorsal and ventral nerve cords that attracts sensory axons and muscle arms; its activity requires the netrin receptor UNC-40/DCC acting cell-autonomously. This establishes a guidance function for the ADAMTSL family in nervous system patterning. | PMID:22014523 | Developmental cell |
| 2022 | Medium | ADAMTSL1 marks a distinct myelinating Schwann cell subtype (Pmp2+ SCs) in peripheral nerve that preferentially ensheathes large-caliber motor axons; this subtype is reduced in ALS model mice and human ALS nerve samples. | PMID:35115729 | Nature neuroscience |
| 2025 | Medium | Ablation of Pmp2+ Schwann cells (co-marked by Adamtsl1) using a tamoxifen-inducible diphtheria toxin system leads to significant loss of large-caliber motor axons with behavioral, electrophysiological, and ultrastructural deficits; withdrawal of tamoxifen restores both PMP2+ SCs and large-caliber motor axons. | PMID:39880678 | The Journal of neuroscience |
| 2019 | Low | Missense variants in ADAMTSL1 (c.176C>A and c.670C>G) segregate with mandibular prognathism in multiple Thai families; Adamtsl1 is strongly expressed in condensed mesenchymal cells of the mouse condyle but not in long bone cartilage, consistent with a tissue-specific role in mandibular condylar cartilage growth potentially through aggrecan cleavage regulation. | PMID:30714143 | Clinical genetics |

## Citations

- PMID:11805097
- PMID:18720094
- PMID:22014523
- PMID:24281761
- PMID:24634412
- PMID:28722276
- PMID:30714143
- PMID:34500691
- PMID:35115729
- PMID:39880678
