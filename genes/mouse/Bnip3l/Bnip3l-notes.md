# Bnip3l (NIX) — mouse (Q9Z2F7) curation notes

## Identity and structure

- Mouse Bnip3l / Nix, 218 aa, NIP3 family (PANTHER PTHR15186, subfamily PTHR15186:SF3;
  InterPro IPR010548; Pfam PF06553). UniProt features: C-terminal helical TM 187-207,
  BH3 motif 125-147, N-terminal disordered region 1-66 (file:mouse/Bnip3l/Bnip3l-uniprot.txt).
- Tail-anchored outer mitochondrial membrane protein; cytosolic N-terminus carries the LIR
  (W35/W36 region) and the minimal essential region (MER).
- First described as a pro-apoptotic homolog of Nip3/BNIP3 [PMID:9867803 "We have identified
  Nix, a homolog of the E1B 19K/Bcl-2 binding and pro-apoptotic protein Nip3"], localized with
  mitochondrial HSP60 [PMID:9867803 "Nix colocalizes with the mitochondrial matrix protein HSP60,
  and removal of the putative transmembrane domain (TM) results in general cytoplasmic and nuclear
  expression"]. Note: nuclear signal arises only when the TM is deleted.
- Self-association / dimer [PMID:9867803 "Nix encodes a 23. 8-kDa protein but it is expressed as a
  48-kDa protein, suggesting that it homodimerizes similarly to Nip3"]; TM-mediated homodimer is
  required for robust LC3 recruitment and mitophagy [PMID:32286918 "Forming stable homodimers,
  BNIP3L recruits autophagosomes more robustly than its monomeric form."].

## Core function: mitophagy receptor (mouse genetics)

- Two independent mouse knockouts establish NIX as required for programmed mitochondrial
  clearance in reticulocytes:
  - [PMID:18048346 "Here, we show that mitochondrial clearance in reticulocytes requires the
    BCL2-related protein NIX (BNIP3L)."]; independent of apoptotic machinery [PMID:18048346
    "Mitochondrial clearance does not require BAX, BAK, BCL-X(L), BIM, or PUMA, indicating that NIX
    does not function through established proapoptotic pathways."]; not an autophagy inducer
    [PMID:18048346 "Similarly, NIX is not required for the induction of autophagy during terminal
    erythroid differentiation."]; arrest point [PMID:18048346 "mitochondrial clearance, in the
    absence of NIX, is arrested at the stage of mitochondrial incorporation into autophagosomes"].
  - [PMID:18454133 "Nix(-/-) mice developed anaemia with reduced mature erythrocytes and compensatory
    expansion of erythroid precursors."]; [PMID:18454133 "Although the clearance of ribosomes
    proceeded normally in the absence of Nix, the entry of mitochondria into autophagosomes for
    clearance was defective."]; loss of membrane potential is Nix-dependent [PMID:18454133
    "Deficiency in Nix inhibited the loss of mitochondrial membrane potential (DeltaPsi(m))"].
- LIR-mediated receptor mechanism: [PMID:20010802 "Here, we show that the mitochondrial protein Nix
  is a selective autophagy receptor by binding to LC3/GABARAP proteins"]; in vivo [PMID:20010802
  "Furthermore, ablation of the Nix:LC3/GABARAP interaction retards mitochondrial clearance in
  maturing murine reticulocytes."]; LIR effect is partial [PMID:20010802 "The effect of the LIR
  mutation on Nix-mediated mitochondrial clearance in vivo is partial, indicating that other
  properties of Nix are also important in this process."].
- MER (second motif) in mouse reticulocytes: [PMID:22906961 "Here we showed in mice that BNIP3L
  activity localizes to a small region in its cytoplasmic domain, the minimal essential region
  (MER)."]; [PMID:22906961 "These findings support an adaptor model of BNIP3L, centered on the
  MER."]. The MER binds WIPI2 [PMID:37621214 "We find that the Nix MER interacts with the
  autophagy effector WIPI2 and recruits WIPI2 to mitochondria."].
- Kanki commentary summarising: [PMID:20200478 "Nix is a mitochondrial outer membrane protein that
  is required for mitochondrial clearance during erythrocyte maturation."]

GO mapping: MF GO:0140580 mitochondrion autophagosome adaptor activity (def: "brings together a
mitochondrial membrane and an autophagosome membrane during mitophagy"); BP GO:0000423 mitophagy;
CC GO:0005741 mitochondrial outer membrane. None of GO:0140580 / GO:0000423 is in mouse GOA.

## Other programmed / developmental mitophagy (mouse)

- Retinal ganglion cell differentiation and M1 macrophage polarization [PMID:28465321 "Retinas from
  NIX-deficient mice displayed increased mitochondrial mass, reduced expression of glycolytic
  enzymes and decreased neuronal differentiation."]; hypoxic induction [PMID:28465321 "Local hypoxia
  triggered expression of the mitophagy regulator BCL2/adenovirus E1B 19-kDa-interacting protein
  3-like (BNIP3L, best known as NIX) at peak RGC differentiation."]

## Cell death roles (context-dependent, non-core)

- Overexpression kills cells [PMID:9867803 "When transiently expressed, Nix and Nip3 but not TM
  deletion mutants rapidly activate apoptosis."].
- Erythroblast apoptosis [PMID:17420462 "Nix null mice exhibited massive splenomegaly, with splenic
  and bone marrow erythroblastosis and reduced apoptosis in vivo during erythrocyte maturation."]
  — Diwan et al. interpret Nix as pro-apoptotic in erythropoiesis, contrasting with the mitophagy
  interpretation from Schweers/Sandoval (Sandoval interpret the RBC loss as secondary to retained
  mitochondria).
- Cardiac/ER death pathways [PMID:20418503 "Thus, Nix stimulates dual autonomous death pathways,
  determined by its subcellular localization."]; ER-Nix dissipates potential via MPTP
  [PMID:20418503 "ER-Nix cells, but not mitochondrial-Nix cells, showed dissipation of mitochondrial
  inner membrane potential, Deltapsi(m), and were protected from cell death by cyclosporine A or
  ppif ablation, implicating the mitochondrial permeability transition pore (MPTP)."]
- POSH/JNK [PMID:17095503 "These results indicate that Nix promotes cell death via interaction with
  POSH and activation of the JNK/c-Jun pathway"] (overexpression, HEK293/PC12).
- Human orthologue B5 inhibits Nip3-induced apoptosis and localizes to NE/ER/mitochondria
  [PMID:10381623 "B5 does not induce apoptosis, but inhibits apoptosis induced by Nip3."].
- Hypoxia: BNIP3/BNIP3L promote survival autophagy [PMID:19273585 "Hypoxia-induced autophagy via
  BNIP3 and BNIP3L is clearly a survival mechanism that promotes tumor progression."].

## MALM (MIEAP) — human only

- [PMID:21264228 "A mitochondrial outer membrane protein NIX interacted with Mieap in a
  ROS-dependent manner via the BH3 domain of NIX and the coiled-coil domain of Mieap."] Human cancer
  cell work; transferred to mouse by ISO/ISS/IEA only. Non-core.

## Annotations judged problematic

- GO:0051607 defense response to virus (ISO/ISS/IEA from human IDA PMID:9973195): source paper
  only shows binding to viral anti-apoptotic E1B-19K — not host defense. REMOVE.
- GO:0016607 nuclear speck (from HPA antibody staining in human) and GO:0005634 nucleus (IBA):
  nuclear signal only for TM-deleted Nix [PMID:9867803]. Over-annotation.
- GO:1903747 is obsolete per QuickGO ("this term represents a phenotype and was added in error.
  Consider annotating to regulation of the specific process being regulated (e.g. regulation of
  mitophagy)"); verified 2026-10-10 via QuickGO API (OLS still showed it live).
- GO:0005515 protein binding rows: LC3/GABARAP partners -> MODIFY to GO:0140580; SH3RF1/POSH and
  ATG13 -> REMOVE (uninformative).

## PAINT / IBA observations (PTHR15186)

- From the PANTHER tree (treeinfo API, filtered to human/mouse/zebrafish/worm/fly), PTN002689506
  is the vertebrate BNIP3L (NIX) clade node, and PTN002689498 is the vertebrate BNIP3 clade node;
  PTN000795991 is the family root.
- The mitophagy IBD (GO:0000423) sits at PTN001032684 (seeds BNIP3, fly BNIP3, worm dct-1), but
  `projects/PANTHER_IBA_REVIEW/family_function_losses.tsv` lists an IRD for GO:0000423 at
  PTN002689506 — i.e. the NIX clade is pruned from mitophagy. This is contrary to the strongest
  mitophagy genetics in the family (mouse Nix knockouts). As a consequence mouse Bnip3l has no
  mitophagy IBA.
- PTN002689498 (BNIP3 clade) carries GO:0140580, GO:0005789, GO:0061709 seeded only by human BNIP3,
  so NIX gets no adaptor-activity IBA either. GO:0140580 should be placed at the BNIP3/BNIP3L
  duplication ancestor (or at PTN001032684), and the GO:0000423 IRD on PTN002689506 removed.
- GO:0043653 mitochondrial fragmentation involved in apoptotic process (PTN001032684) is seeded by
  BNIP3 only; no NIX evidence for apoptotic fragmentation.

## Deep research

- falcon deep research was launched by the parent agent; not available at time of writing.

## Addendum: falcon deep research (arrived after the review was written)

`Bnip3l-deep-research-falcon.md` (falcon, retried with a longer timeout after a first 600 s timeout)
landed after the annotation review was finished. It was cross-checked against the review and agrees
with its calls: the primary role is a LIR-bearing, tail-anchored mitochondrial autophagy receptor at
the outer mitochondrial membrane, and cell-death outputs are context-dependent and separable from
receptor function. It is cited on the core GO:0140580 annotation. No annotation decision changes.
