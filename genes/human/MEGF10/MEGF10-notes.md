# MEGF10 notes

## Deep research status (2026-10-03)

No provider deep-research file exists for this gene. `deep_research_wrapper.py human MEGF10 falcon --fallback perplexity-lite` failed: Falcon/Edison returned `402 Payment Required`, and the perplexity provider is not available in this environment. A retry with `openai` failed with `invalid_api_key`. The synthesis below was made by hand from cached publications. Every claim carries an inline citation and quote.

## Identity and architecture

- UniProtKB:Q96KG7, 1140 aa, single-pass type I membrane protein.
- Domain organization matches C. elegans CED-1: [PMID:17498693 "containing a signal peptide, a EMI domain, 17 atypical EGF-like repeats, a transmembrane domain, and a cytoplasmic domain with NPXY and YXXL motifs"].
- Classified as a class F scavenger receptor: [PMID:27170117 "Multiple EGF-like domains 10 (Megf10) is a class F scavenger receptor (SR-F3)"].
- Tyrosine phosphorylated: [PMID:23954233 "Y1030 was identified to be the major tyrosine phosphorylation site in MEGF10 and is phosphorylated at least in part by c-Src"].

## Family assignment (see projects/PANTHER_FAMILY_ASSIGNMENT_DISCREPANCIES.md)

- The UniProt `DR PANTHER` cross-reference (from InterPro) is PTHR24052:SF13. `fetch-gene` therefore pulled PTHR24052 family data.
- PANTHER 19.0's own classification places MEGF10 in PTHR24035:SF136. The CED-1/Draper subfamily, PTHR24035:SF109, sits in the same family.
- Its IBAs come from PAINT nodes PTN002372116, PTN009076277 and PTN002778616. Their sources include ced-1 (WB:WBGene00000415), Draper (FB:FBgn0027594) and mouse Megf10 (MGI:2685177).

## Core: engulfment receptor for apoptotic cells (CED-1 ortholog)

- Functional ortholog of CED-1: [PMID:17205124 "MEGF10, a novel receptor bearing striking structural similarities to CED-1, as a bona fide functional ortholog in mammals"].
- Gain of function: [PMID:27170117 "cells transfected with Megf10 gain the ability to phagocytose apoptotic neurons"].
- Loss of function (mouse): [PMID:27170117 "Megf10-deficient mice have increased apoptotic cells in the developing cerebellum and have impaired phagocytosis of apoptotic cells by astrocytes"].
- Ligand: C1q, which itself binds phosphatidylserine: [PMID:27170117 "Megf10 binds with high affinity to C1q, an eat-me signal for apoptotic cells"]. Disease mutations impair this binding: [PMID:27170117 "cells expressing Megf10 with EMARDD mutations have impaired apoptotic cell clearance and impaired binding to C1q"].
- Localization during engulfment: [PMID:17205124 "MEGF10 (M10: MEGF10 ECFP in green) is recruited at the bottom of the forming phagocytic cup"]. Also [PMID:17498693 "MEGF10 protein accumulated around the contact region during engulfment of apoptotic cells"].
- CED-1 pathway partners: GULP1 (the CED-6 ortholog) [PMID:17205124 "MEGF10 can interact with GULP as assessed by GST pull down"] and ABCA1 (the CED-7 ortholog) [PMID:17205124 "MEGF10 function can be modulated by the ATP binding cassette transporter ABCA1, ortholog to CED-7"].
- Endocytic adaptor: [PMID:17643423 "we identified an interaction between MEGF10 and clathrin assembly protein complex 2 medium chain (AP50)"].

## Astrocyte-mediated synapse elimination (mouse)

- [PMID:24270812 "requires the MEGF10 and MERTK phagocytic pathways"]. Also [PMID:24270812 "Both MEGF10 and MERTK function as engulfment receptors"]. MEGF10 acts as the engulfment receptor here, so it does part of the work of synapse pruning.

## Amyloid-beta uptake (cell lines)

- [PMID:20828568 "Overexpression of MEGF10 dramatically increased Aβ42 uptake in Hela cells"]. This fits the scavenger receptor activity definition, which lists amyloid-beta fibrils among ligands. Evidence comes only from overexpression and knockdown in cell lines, so no process annotation is proposed.

## Retinal mosaic spacing (mouse): homotypic repulsion, not adhesion

- [PMID:22407321 "mosaic spacing requires repellent homotypic interactions mediated by MEGF10 and 11"].
- [PMID:22407321 "these results suggest that a MEGF10-containing signaling complex mediates a homotypic interaction resulting in intercellular repulsion"].
- [PMID:22407321 "we have been unable to demonstrate MEGF10 homophilic binding using biochemical methods"].
- Consequence: GO:0034109 homotypic cell-cell adhesion (IDA, this paper) does not fit what the paper shows. The paper reports cell-cell recognition that leads to repulsion.

## Skeletal muscle (EMARDD myopathy)

- [PMID:22101682 "MEGF10 is highly expressed in activated satellite cells and regulates their proliferation as well as their differentiation and fusion into multinucleated myofibers"].
- [PMID:28498977 "leads to impaired proliferation and migration of C2C12 cells"]. Also [PMID:28498977 "Reciprocal co-immunoprecipitation studies show that Megf10 and Notch1 interact via their respective intracellular domains"].
- Muscle roles are real but distinct from the conserved engulfment-receptor function. The mechanism (Notch modulation, Y1030 signaling) is incompletely defined, so these annotations are treated as non-core.

## Open questions

- Does MEGF10 bind phosphatidylserine directly, or only through C1q (and other bridging molecules)?
- Which ligand drives the homotypic MEGF10 interaction in retina, given that no homophilic binding was detected?
- Is the Notch1 interaction direct, and does it explain the satellite-cell phenotypes?
