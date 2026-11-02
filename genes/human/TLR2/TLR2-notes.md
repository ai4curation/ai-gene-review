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

## Deep-research cross-check (2026-09-30)

Falcon deep research finished after the review was drafted (`TLR2-deep-research-falcon.md`;
the runner reported exit code 1 but the file was written). Cross-checked against the
completed review. **No annotation actions, descriptions or core functions were changed.**

Agreement:
- TLR2 is a signalling pattern recognition receptor, not an enzyme; TLR2:TLR1 for triacyl
  and TLR2:TLR6 for diacyl lipopeptides, with TLR6 lacking the TLR1 channel for the third
  acyl chain. Matches the two heterodimer core functions and the detection/binding rows.
- Plasma membrane as the principal functional location; cell-type-wide expression on
  myeloid and non-immune cells.
- MyD88-dependent signalling through TIRAP/MAL, myddosome, TRAF6, TAK1 to NF-kappaB and
  MAPK; no TRIF branch. Matches the accepted NF-kappaB row and the TIR-domain-binding
  MODIFY decisions for TIRAP and MyD88.
- TLR2 homodimer signalling is called controversial, supporting `identical protein binding`
  being kept as non-core rather than made a core function.
- Responses to purified peptidoglycan and lipoteichoic acid may reflect contaminating
  lipoproteins, which is exactly the open peptidoglycan question already recorded.
- TLR2/TLR4 recognition of LPS is described as context-dependent and incompletely
  established, consistent with UNDECIDED on the two LPS rows (GO:0001530 IDA
  PMID:11274165; GO:0001875 IDA PMID:16880211) and with the REMOVE of the TAS row.
- Amyloid-beta and alpha-synuclein as DAMPs, consistent with keeping amyloid-beta binding
  as non-core.

Additions not acted on (report cites only secondary reviews; no primary paper verified, so
per the "never cite deep research as sole support" rule nothing was asserted):
- TLR2/TLR10 and TLR2/CLEC2D heterodimers; CLEC2D/TLR2 is described as negatively
  regulating IRF5-mediated antifungal immunity. No `Toll-like receptor binding` or
  process row was added for these.
- Endosomal TLR2 pools with regulatory (IL-10) output, and soluble/vesicular TLR2 acting
  as a decoy. Not annotated; the review's Golgi and cytoplasm IDA rows stay non-core. The
  report asserts TLR2 is absent from the Golgi, which conflicts with the IDA Golgi row
  (PMID:16880211); the experimental row was left in place per the rule against overruling
  curators from incomplete evidence.
- TLR2 promoting monocyte chemotaxis, adhesion, transendothelial migration, tissue-factor
  expression and platelet interactions. These are downstream cellular consequences of
  signalling and would not pass the participation test for a NEW process term, so none
  was added.

Conflict: none that changes a decision.
