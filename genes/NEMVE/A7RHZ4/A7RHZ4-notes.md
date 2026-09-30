# A7RHZ4 (Nematostella vectensis MyD88, NvMyD88) review notes

## Status of inputs

- No Falcon deep-research job was queued for NEMVE A7RHZ4 in this batch (no `dr-NEMVE-A7RHZ4` log
  and no `NEMVE A7RHZ4 dr=` line in the batch task output). Review done from UniProt, GOA and cached
  literature. No `-deep-research-*.md` file exists.
- UniProt A7RHZ4 (TrEMBL, PE 4 predicted, 245 aa, flagged Fragment with NON_TER at residue 1):
  Death domain 1-65 (PROSITE PS50017), TIR domain 104-236 (PS50104). InterPro IPR017281 (MyD88 family),
  PANTHER PTHR15079:SF3 (MYD88). ORF NEMVEDRAFT_v1g82163. Name from ProtNLM. The N-terminus is missing,
  so the death domain is probably incomplete at its start.
- All 5 GOA rows are IEA (4 InterPro2GO, 1 UniProt SubCell). No experimental annotation and, as far as
  I could find in PubMed, no functional study of the Nematostella MyD88 protein itself.

## What is known

- Nematostella has a single MyD88 homologue and a single TLR [PMID:17437634 "These include a single MyD88 homolog (NvMyD88) and a protein (NvTLR-1) clearly related to members of the Toll/TLR family (Figure 2)"];
  confirmed across actiniarians [PMID:27806695 "vectensis and confirmed single copies of TLR and MyD88."].
  MyD88 in these surveys is defined by death domain + TIR architecture
  [PMID:27806695 "MyD88 was identified by searching for a TIR (or TIR_2) domain, along with a death domain (DD)."].
- Nematostella also has IL-1R-like TIR proteins, which form a clade distinct from vertebrate IL-1Rs
  [PMID:17437634 "In the phylogenetic analysis based on TIR domains the Nematostella IL-1R-like proteins form a clade distinct from both the MyD88 and Toll/TLR types (Figure 3)"].
  There is no IL-1 cytokine in cnidarians to my knowledge (not sourced; not used for any annotation), so
  IL-1-mediated signalling terms should not transfer.
- The Nv-TLR TIR domain binds human MYD88 and MAL, and Nv-TLR activates NEMO-dependent NF-kappaB in
  HEK293 cells, responding to heat-killed Vibrio coralliilyticus and flagellin
  [PMID:29109290 "we show that the intracellular Toll/IL-1 receptor (TIR) domain of Nv-TLR can interact with the human TLR adapter proteins MAL and MYD88"],
  [PMID:29109290 "Neither Nv-TLR nor Hu-TLR4 activated the NF-κB–site luciferase reporter in 293 cells in which NEMO expression was genetically ablated"].
  This is evidence about the receptor with human adaptors; NvMyD88 itself was not tested.
- Coral (Orbicella) TLR TIR binds human MYD88 [PMID:29080785 "it can interact in vitro with the human TLR4 adapter MYD88"].
- Hydra MyD88 knockdown: role in bacterial colonisation and defence against Pseudomonas - the only
  in vivo cnidarian MyD88 loss-of-function evidence
  [PMID:23112184 "we use a MyD88 loss-of-function approach in Hydra to demonstrate that recognition of bacteria is an ancestral function of TLR signaling"].
- Nv-NF-kappaB is p50/p52-like, lacks C-terminal IkappaB-like repeats; separate IkappaB genes exist
  [PMID:17120026 "Nv-NF-kappaB lacks the C-terminal IkappaB-like sequences present in all other NF-kappaB proteins"].
  Nematostella NF-kappaB linked to immunity (starvation reduces NF-kappaB and increases P. aeruginosa
  susceptibility, PMID:37420095).

## Decisions

- GO:0070976 TIR domain binding (IEA): ACCEPT - core adaptor MF; homotypic TIR binding is the defining
  MyD88 activity; cnidarian TLR TIRs bind (human) MyD88.
- GO:0002755 MyD88-dependent TLR signaling pathway (IEA): ACCEPT - Nematostella has one TLR; Nv-TLR can
  respond to bacterial products and signal via MyD88 in a reconstituted system; Hydra MyD88 needed for
  bacterial sensing. The definition's "directly bind pattern motifs" clause is not shown for Nv-TLR, but
  the reconstitution data (flagellin, Vibrio) are consistent. Accept as an inference.
- GO:0043123 positive regulation of canonical NF-kappaB signal transduction (IEA): ACCEPT with caveat -
  Nematostella has separate NF-kappaB and IkappaB proteins and IKK homologues; Nv-TLR drives NEMO-dependent
  NF-kappaB activation in human cells. Not directly shown for NvMyD88.
- GO:0007165 signal transduction (IEA): ACCEPT (broad, correct).
- GO:0005737 cytoplasm (IEA): ACCEPT - no TM or signal peptide; MyD88 family is cytosolic.
- Not transferred: GO:0070498 interleukin-1-mediated signaling pathway and numbered TLR terms
  (e.g. GO:0034142 TLR4) - no IL-1 ligand, and no evidence of TLR4-type ligand specificity for Nv-TLR
  (TIR similarity to TLR4 does not imply LPS recognition).
- No NEW annotations: nothing experimental on this protein.
