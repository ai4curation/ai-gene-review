# TLR2 (human, O60603) review notes

## Sources used
- UniProt O60603 record (TLR2-uniprot.txt)
- 44 GOA-cited publications cached in `publications/` (most abstract-only; full text for PMID:16893894, 18765807, 19509286, 19509287, 20067962, 20406817, 20802527, 23155421, 23376921, 23626692, 26649771, 29990310, 31980649, 33576548)
- Falcon deep research: see status note at the end.

## Core biology
- Recognition of Gram-positive cell-wall components: [PMID:10384090 "Heterologous expression of human TLR2, but not TLR4, in fibroblasts conferred responsiveness to Staphylococcus aureus and Streptococcus pneumoniae"]
- Heterodimers set ligand specificity: [PMID:19931471 "Its ligand specificity is controlled by whether it heterodimerizes with TLR1 or TLR6"]
- TLR1-TLR2 structure: [PMID:17889651 "the two ester-bound lipid chains are inserted into a pocket in TLR2, while the amide-bound lipid chain is inserted into a hydrophobic channel in TLR1"]
- TLR2-TLR6-diacyl lipopeptide and TLR2-LTA structures: [PMID:19931471 "We have determined the crystal structures of TLR2-TLR6-diacylated lipopeptide, TLR2-lipoteichoic acid, and TLR2-PE-DTPA complexes"]
- Preformed heterodimers, rafts, Golgi trafficking: [PMID:16880211 "Our data show that TLR2 forms heterodimers with TLR1 and TLR6 and that these heterodimer pre-exist and are not induced by the ligand"]; [PMID:16880211 "Activation occurs at the cell surface, and the observed trafficking is independent of signaling"]
- Phagosome recruitment: [PMID:11095740 "TLR6 and TLR2 both are recruited to the macrophage phagosome, where they recognize peptidoglycan, a Gram-positive pathogen component"]
- TIR adaptors: [PMID:19509286 "It is thought that Mal acts as a bridging adapter between the receptor (TLR2 or TLR4) and MyD88 and, thus, physically interacts with both"]
- LTA: [PMID:12594207 "Human embryonic kidney (HEK) 293/CD14 cells and Chinese hamster ovary (CHO) cells were responsive to LTA only after transfection with TLR-2"]
- Amyloid-beta: [PMID:22198949 "demonstrate a direct interaction between TLR2 and the aggregated 42-aa form of human Aβ (Aβ42)"]

## LPS question
TLR2 is not an LPS receptor:
- [PMID:11521063 "TLR2 without MD-2 does not respond to pure protein-free endotoxic LPS, ReLPS, and lipid A"]
- [PMID:11986301 "In contrast, sTLR2 exhibited a very weak binding to lipopolysaccharide"]
- [PMID:12443841 "might be mediated by TLR2-dependent recognition of non-LPS bacterial components contaminating in commercial LPS preparations"]
- The TAS review cited for GO:0001875 attributes LPS recognition to TLR4 [PMID:11518816 "Mammalian TLR4 is the signal-transducing receptor activated by the bacterial lipopolysaccharide"], so that row was removed. The two IDA rows (GO:0001530 PMID:11274165; GO:0001875 contributes_to PMID:16880211) are UNDECIDED because the full texts are not cached and the abstracts do not describe TLR2 binding LPS.

## Decisions (summary)
- Core: pattern recognition receptor activity; triacyl lipopeptide binding; Toll-like receptor binding; TLR1:TLR2 and TLR6:TLR2 pathways; detection of di/triacyl lipopeptide; plasma membrane, rafts, phagosome membrane; TLR1-TLR2 and TLR2-TLR6 complexes.
- NEW: GO:0042498 diacyl lipopeptide binding (IDA, PMID:19931471 structure). An MF from direct structural evidence; no NEW process terms.
- protein binding (24 rows): MODIFY to Toll-like receptor binding where the partner is TLR1/6/10 (PMID:15728506, 20067962, 23155421 x3); MODIFY to TIR domain binding for TIRAP (PMID:19509286) and MyD88 (PMID:29990310); REMOVE the rest (microbial ligands, EGFR, CXCR4, Tollip, TRIP6, ATG16L1, PAUF).
- Downstream cytokine/NF-kappaB outputs kept as non-core; indirect terms (Wnt regulation, Pol II transcription, MMP secretion, responses to IFN-gamma/M-CSF where TLR2 is the regulated target) marked over-annotated; mouse ISS neural terms (learning, microglia development, synapse assembly) marked over-annotated.
- Defense response to virus (IEP, PMID:32634389) removed: the paper states [PMID:32634389 "However, additional studies are required to determine the functional role of TLRs in monocytes and MDMs"].
- PMID:23626692 has a 2024 expression of concern; its TLR6:TLR2 row accepted because other papers support it.

## Project questions
- GO:0034134 / 0038123 / 0038124 are correctly on human TLR2; IBA GO:0002224 fits.
- No TLR-specific MF exists; GO:0038187 is used as the core MF.

## Deep research status
Falcon deep research finished after the review was drafted. The runner reported exit code 1, but it wrote `TLR2-deep-research-falcon.md`. I read it afterwards and it agrees with the decisions above:
- It calls TLR2 homodimers controversial, which supports keeping identical protein binding as non-core.
- It notes that TLR2 responses to purified peptidoglycan or LTA may reflect contaminating lipoproteins, which matches the suggested question on peptidoglycan.
- It says TLR2/TLR4 recognition of LPS is context-dependent and not fully established, which is consistent with UNDECIDED on the LPS IDA rows.
- It describes TLR2/TLR10 heterodimers as a newer partnership.

Nothing in it changed an action. Its citations are secondary (Falcon-summarised reviews) and none are cited in the YAML.
