# Drosophila mad2 (CG17498, FBgn0035640, UniProt Q9VRQ2): manual literature synthesis

No deep-research API was available for this review. This synthesis comes from the cached
publications in `publications/` and from PubMed searches run during the review.

## Identity and domain architecture

- 207-aa HORMA-domain protein (HORMA domain residues 14-201, PROSITE PS50815). It belongs to the
  MAD2 family (PANTHER PTHR11842:SF11, MAD2A subfamily) and is the ortholog of human MAD2L1
  (Q13257) (UniProt Q9VRQ2 record).

## Localization

- Interphase: mainly nucleoplasmic, with a fraction on the nuclear envelope. After mitosis Mad2 is
  first imported into the nucleus and only then reassociates with the NE, together with Mad1 and
  Megator [PMID:18562695 "In Drosophila neuroblasts, Mad2 is primarily in the nucleoplasm, but a fraction of it is associated with the NE"].
  Mad1-C-Mad2 is docked on Megator (the TPR ortholog) at the nucleoplasmic side of nuclear pores
  [PMID:31913420 "Mad1-C-Mad2 is docked to Megator at the nucleoplasmic side of NPCs, where it catalyzes the assembly of premitotic MCC"].
- Mitosis: Mad2 sits on unattached kinetochores [PMID:15075237 "Bub1 and Mad2 only localize at the unattached kinetochore"],
  in the outer corona with Rod [PMID:15886105 "Mad2 and Rod colocalize to the outermost kinetochore region (the corona)"].
  Its recruitment needs Rod/Zw10 [PMID:15886105], Megator and Mps1 kinase activity [PMID:19273613].
- After attachment, dynein strips Mad2 along K-fibres to the poles. This needs Spindly
  [PMID:17576797 "Spindly is required for removing Rod and Mad2 from kinetochores."].
- A microtubule-independent pool sits in a Megator-defined spindle matrix
  [PMID:19273613 "a distinct pool of mRFP-Mad2 localizes to a nuclear derived spindle matrix"].

## Function

- SAC: Mad2 RNAi in S2 cells abolishes the arrest after spindle damage and speeds up
  prometaphase [PMID:17182852 "Depletion of Mad2 by RNAi from S2 cells shows that it is essential to prevent mitotic exit after spindle damage"].
- mad2-null flies have no SAC, yet they are viable and fertile. Their mitotic clock runs fast
  because cyclin B is degraded early [PMID:17417628 "mad2-null Drosophila are viable and fertile, and their cells almost always divide correctly despite having no SAC"].
- Mad2 binds Cdc20, and it does so independently of BubR1. Mad2 is not needed to recruit Cdc20 to
  kinetochores [PMID:20421417 "BubR1 and Mad2 can bind to Cdc20 independently"].
- Mad2 becomes essential when spindle assembly is slow:
  - with extra centrosomes, the SAC delay lets multipolar spindles turn bipolar
    [PMID:18555779 "This requires a delay in mitosis that is mediated by the spindle assembly checkpoint (SAC)."];
  - with reduplicated polytene chromosomes in papillar cells
    [PMID:27159240 "Both reduplication responses require the spindle assembly checkpoint protein Mad2."].
- Megator-Mps1 axis: Mps1 phosphorylates Megator, which releases Mad1. This release sets how much
  Mad1-C-Mad2 reaches the kinetochore, and that amount sets SAC strength
  [PMID:31913420 "The strength of SAC response is dictated by the amount of Mad1-C-Mad2 present at KTs"].

## Indirect or tool uses

- Mad2 RNAi has been used to induce chromosomal instability (CIN) in wing discs [PMID:24335260].
- Overexpressing UAS-mad2 partly rescues germline stem cell (GSC) loss in Megator mutants
  [PMID:26714316]. No mad2 loss-of-function GSC phenotype has been reported.
