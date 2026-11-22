# KNAT1 / BREVIPEDICELLUS (AT4G08150, UniProt P46639) - manual literature synthesis

No deep-research provider was available in this environment; this file was written by
hand from the cached publications in `publications/` and the UniProt record. Every
statement carries inline provenance.

## Identity and family

- KNAT1 (KNOTTED-LIKE FROM ARABIDOPSIS THALIANA 1), also BREVIPEDICELLUS (BP), is a
  class I KNOX TALE homeodomain protein of 398 aa (UniProt P46639; TAIR AT4G08150;
  GeneID 826364).
- Domain architecture: KNOX1 and KNOX2 (together the MEINOX domain), ELK domain
  (279-299) and a TALE-type homeodomain (300-363)
  [file:ARATH/KNAT1/KNAT1-uniprot.txt "DNA_BIND        300..363"].
- Cloned with the maize kn1 homeobox as probe; homeodomain 78-95% identical to maize
  class 1 KNOX proteins [PMID:7866029 "The homeodomains of KNAT1 and KNAT2 are very
  similar to the homeodomains of proteins encoded by class 1 maize genes"].
- `bp` mutants are KNAT1 alleles [PMID:11917137 "BP encodes the homeodomain protein
  KNAT1, a member of the KNOX family"].

## Molecular function

- TALE heterodimerization with BELL partners via the MEINOX domain
  [PMID:11701881 "the Arabidopsis BELL1 (BEL1) homeodomain protein can selectively
  heterodimerize with specific KNAT homeodomain proteins"; "Interaction is mediated by
  BEL1 sequences N terminal to the homeodomain and KNAT sequences including the MEINOX
  domain"]. In yeast only the heterodimer activates transcription [PMID:11701881 "BEL1
  and KNAT proteins can activate transcription only as a heterodimeric complex"].
- Partners include PNY/BLH9 [PMID:12897247 "The physical association of the PNY and
  BP proteins suggests that they participate in a complex"], VAN/BLR
  [PMID:15019989 "VAN interacts specifically with the class I KNOX proteins
  SHOOTMERISTEMLESS (STM), BREVIPEDICELLUS (BP), and KNAT6 (K6)"], and SAW1/SAW2
  [PMID:17873098 "form heterodimeric complexes with the Class 1 KNOX TALE homeodomain
  proteins, including SHOOTMERISTEMLESS (STM) and BREVIPEDICELLUS (BP)"]. BP is needed
  for nuclear localisation of VAN in tobacco [PMID:15019989 "nuclear localisation of a
  VAN-GFP fusion depends on co-expression of STM or BP in tobacco leaves"].
- DNA binding: UniProt states KNAT1 probably binds TGAC
  [file:ARATH/KNAT1/KNAT1-uniprot.txt "Probably binds to the DNA sequence 5'-TGAC-3'"].
  An eY1H vascular network screen recorded KNAT1 binding the MONOPTEROS (AT1G19850)
  promoter (PMID:31806676; the interaction is in supplementary data, not the cached text).
- Other reported interactors (mostly Y2H screens): OFP family proteins
  (PMID:15781858), CCT chaperonin subunits (PMID:21868675, a maize KN1 trafficking
  study), AGO10/PNH (PMID:26390296), bZIP30/DKM (PMID:27402171), and large
  interactome screens (PMID:21798944, PMID:28650476, PMID:32612234, PMID:36088536).

## Localization

- Nuclear [PMID:15781858 "BELL and KNOX proteins such as BLH1 and KNAT1 were located
  exclusively in the nucleus but not in the nucleolus"]. Can move between meristem
  layers [file:ARATH/KNAT1/KNAT1-uniprot.txt "Able to traffic from the L1 to the L2/L3
  layers of the meristem, presumably through plasmodesmata"].

## Expression

- SAM, downregulated in leaf primordia; after floral transition restricted to the
  cortex of the inflorescence stem [PMID:7866029 "KNAT1 transcript is localized
  primarily to the shoot apical meristem; down-regulation of expression occurs as leaf
  primordia are initiated"]. Expressed at stem/lateral organ boundaries
  [PMID:16038894 "BP expression in a reporter line marked boundaries between the
  inflorescence stem and lateral organs"]. Repressed in lateral organs by AS1, YABBY
  genes, SAW1/SAW2 and HAN [PMID:17873098; PMID:23133401; PMID:26390296].

## Biological roles (genetic)

- Inflorescence architecture: pedicel and internode growth and differentiation
  [PMID:11917137 "In both bp alleles, the pedicels and internodes were compact because
  of fewer cell divisions; in addition, defects in epidermal and cortical cell
  differentiation and elongation were found in the affected regions"].
- Radialised growth of pedicels and stem, with ERECTA; vascular patterning
  [PMID:16038894 "Analysis of pedicel vascular patterns revealed biasing of vasculature
  towards the abaxial side, consistent with a role for BP and ER in regulating a
  vascular-borne growth inhibitory signal"].
- Internode patterning with PNY [PMID:12897247 "Both bp and pny have randomly shorter
  internodes"].
- Vascular/xylem differentiation with BLR and REV [PMID:23148846 "in conjunction with
  BP and REV, playing a part in determining the composition and organisation of the
  vascular system"]; BP negatively regulates lignin biosynthesis (cited in
  PMID:23148846 "BP negatively regulates biosynthesis of lignin").
- Fruit mediolateral patterning: BP with RPL promotes replum development and represses
  the lateral JAG/FIL genes [PMID:23133401 "the cooperating genes BREVIPEDICELLUS (BP)
  and REPLUMLESS (RPL) promote replum development"; "Medial factors autonomously
  constrain lateral factors so that they only express outside the replum"].
- Overexpression produces lobed leaves [PMID:7866029 "Misexpression of KNAT1 and kn1
  resulted in highly abnormal leaf morphology that included severely lobed leaves"].

## Not found / gaps

- No cached biochemical demonstration (EMSA/ChIP) of KNAT1 binding a specific target
  promoter; direct targets in pedicel/stem (e.g., lignin genes, FIL/JAG) are inferred.
