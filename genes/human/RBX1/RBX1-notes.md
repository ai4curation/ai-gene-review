# RBX1 (ROC1, RNF75; UniProt P62877) — curation notes

## What the protein is

A 108-residue RING-H2 protein, the catalytic subunit shared by most human cullin-RING
ubiquitin ligases (CRLs). Two structural elements do all the work: an N-terminal strand
that pairs with the cullin C-terminal domain through an intermolecular beta-sheet, and a
cross-braced RING domain that coordinates two zinc ions (a third is seen in SCF
structures) and binds a modifier-charged E2.

- Identified as one of two conserved cullin partners with associated ligase activity
  [PMID:10230407 "ROC1, a homolog of APC11, represents a family of cullin partners with an associated ubiquitin ligase activity."];
  the RING is the catalytic element, since
  [PMID:10230407 "ROC1 mutations completely abolished their ligase activity without noticeable changes in associated proteins."]
- Architecture from the SCF crystal structure
  [PMID:11961546 "The globular domain binds the RING finger protein Rbx1 through an intermolecular beta-sheet, forming a two-subunit catalytic core that recruits the ubiquitin-conjugating enzyme."]
- The RING domain is required for activity and coordinates an extra zinc ion
  [file:human/RBX1/RBX1-uniprot.txt "The RING-type zinc finger domain is essential for ubiquitin ligase activity"]
- RBX1 does not form its own thioester; it activates the E2~ubiquitin conjugate
  [file:human/RBX1/RBX1-deep-research-falcon.md "Its N-terminal region binds the C terminus of a cullin scaffold, whereas its RING domain recruits a modifier-loaded E2 enzyme."]
  and
  [PMID:36372232 "RBX1 is a RING protein that recruits a ubiquitin-charged E2 to the E3 ligase."]
- E2 recruitment in SCF is of CDC34/UBE2R
  [file:human/RBX1/RBX1-uniprot.txt "Recruits the E2 ubiquitin-conjugating enzyme CDC34 to the complex and brings it into close proximity to the substrate."]
  and RBX1 also stimulates the E2's autoubiquitination
  [file:human/RBX1/RBX1-uniprot.txt "Probably also stimulates CDC34 autoubiquitination."]

## Two catalytic roles

**Ubiquitin ligase.** The RING activates E2~ubiquitin for direct transfer onto a lysine
of a receptor-bound substrate, with mostly K48 chains
[PMID:33234069 "Rbx1 engages an E2 enzyme conjugated to activated ubiquitin, thus enabling the direct transfer of ubiquitin to the substrate"].
Independent confirmation that the RING is the catalytic site: Glomulin binds it and
inhibits ligase activity
[PMID:22405651 "The glomuvenous malformation protein Glomulin binds Rbx1 and regulates cullin RING ligase-mediated turnover of Fbw7."],
and arsenite binding to the RING blocks CUL3-KEAP1-dependent NRF2 turnover
[PMID:29658272 "It is well established that Nrf2 is ubiquitinated by the Keap1–Cul3–Rbx1 E3 ligase complex."].

**NEDD8 ligase.** With UBE2M/UBC12 the same RING neddylates the conserved cullin lysine
[file:human/RBX1/RBX1-uniprot.txt "Promotes the neddylation of CUL1, CUL2, CUL4 and CUL4 via its interaction with UBE2M."];
the E2 split is UBE2M/RBX1 versus UBE2F/RBX2
[PMID:19250909 "The E2s have distinct functions, with UBE2M/RBX1 and UBE2F/RBX2 displaying different target cullin specificities."],
and the mechanism is RING rotation, caught in a trapped intermediate
[PMID:24949976 "Nonetheless, RING E3 mechanisms matching a specific UBL and acceptor lysine remain elusive, including for RBX1, which mediates NEDD8 ligation to cullins and >10% of all ubiquitination."],
[PMID:21765416 "We propose RING domain rotation as a general mechanism for UBL transfer for the largest family of E3s."].
Neddylation then reorients the cullin-RING arm and removes the CAND1 site
[PMID:18805092 "Second, in a model of Rbx1 bound to a ubiquitin E2, a predicted ~60Å gap between an E2’s Cys and the substrate bind"].
DCN-type co-E3s (DCUN1D1-5) deliver UBE2M~NEDD8 to the cullin-RBX1 module
[PMID:26906416 "Cullin-RING ligases (CRL) are ubiquitin E3 enzymes that bind substrates through variable substrate receptor proteins"].

## Where specificity lives (the key curation point)

Substrate choice belongs to the receptor, not to RBX1
[file:human/RBX1/RBX1-uniprot.txt "The functional specificity of the E3 ubiquitin-protein ligase complexes depends on the variable substrate recognition components."],
[file:human/RBX1/RBX1-deep-research-falcon.md "RBX1 supplies catalytic E2 recruitment but ordinarily does **not** select protein substrates by itself."].
This drives most of the grading below: pathway-level processes that follow from one
F-box/BTB/DCAF receptor are kept but marked non-core, and vague downstream phenotypes
(proliferation, apoptosis regulation, epigenetic regulation, MAPK cascade) are marked
over-annotated. The processes RBX1 itself executes — ubiquitination of all linkage
types, neddylation, and the CRL/SCF-dependent proteolysis that follows — are accepted.

## Complex membership

RBX1 sits in CRL1/SCF [PMID:15520277 "CUL1 interacts with RBX1 through its C terminus and with SKP1 through its N terminus."],
CRL2 (elongin BC plus VHL-box receptors; CUL2-Rbx1 versus CUL5-Rbx2 selectivity)
[PMID:15601820 "VHL-box and SOCS-box domains determine binding specificity for Cul2-Rbx1 and Cul5-Rbx2 modules of ubiquitin ligases."],
CRL3 [PMID:14528312 "Targeting of protein ubiquitination by BTB-Cullin 3-Roc1 ubiquitin ligases."],
CRL4A/B [PMID:22118460 "The DDB1-CUL4-RBX1 (CRL4) ubiquitin ligase family regulates a diverse set of cellular pathways through dedicated su"],
CUL7-FBXW8 and the hexameric CUL9 assembly
[PMID:24793696 "Together, these results indicate that ROC1 mediates CUL7-CUL9 heterodimerization."].
Two structural caveats worth recording: in CRL7(FBXW8) the RBX1 RING is held
non-productively and the ubiquitination is done by a separate neddylated CUL1-RBX1 module
[PMID:35982156 "Several observations are consistent with CUL7 recruiting TP53 for neddylated CUL1–RBX1-mediated ubiquitination."],
and in the tetrameric CRL4(DCAF1) resting state the RING is occluded until neddylation
[PMID:34595758 "This architecture renders the RING domain of RBX1 inaccessible for the E2 ubiquitin‐conjugating enzyme."].
CUL5-RBX1 is retained but treated as non-core, since SOCS-box receptors select CUL5-RBX2.

## Localisation

Nucleus and cytoplasm, with the effective site set by the assembled ligase
[file:human/RBX1/RBX1-deep-research-falcon.md "RBX1 is reported in both the **nucleus and cytoplasm**, consistent with degradation of substrates in both compartments."].
ROC1 binding itself promotes nuclear accumulation of CUL1
[PMID:11027288 "The CUL1 C-terminal sequence and ROC1 are required for efficient nuclear accumulation, NEDD8 modification, and ubiq"].
"Site of DNA damage" is accepted: the CRL4(CSA) ligase ubiquitinates stalled Pol II at
lesions [PMID:34526721 "RBX1 and the E2 enzyme–donor ubiquitin complex were modelled as described in the Methods."].
Golgi (from a CRL4-DCAF12 study) and centrosome (SCF(cyclin F)) are kept as non-core
receptor-driven pools.

## Grading decisions and their rationale

- **GO:0005515 (55 rows).** Cullin partners from focused studies → MODIFY to
  GO:0097602 cullin family protein binding. UBE2M rows → MODIFY to GO:0031624 ubiquitin
  conjugating enzyme binding. Receptor/complex co-purifications → MODIFY to the relevant
  complex term (GO:0019005, GO:0031462, GO:0031463). DCUN1D rows → MODIFY to GO:0061663
  NEDD8 ligase activity, the bipartite NEDD8 E3 the interaction defines. Proteome-scale
  interactome rows (HuRI, BioPlex, Hein, HNSCC network, the E2/E3-RING Y2H map) → REMOVE
  as uninformative, not as false. SESN2: the 2018 study makes RBX1 the ligase for SESN2
  [PMID:29294217 "RBX1-mediated ubiquitination of SESN2 promotes cell death upon prolonged mitochondrial damage in SH-SY5Y neuroblast"]
  → MODIFY to GO:0061630; the earlier sestrin-KEAP1-p62 paper stays uninformative → REMOVE.
- **GO:0061629 (RNA Pol II transcription factor binding, partner JUN)** → REMOVE: c-Jun is
  the substrate and is recruited by COP1/DET1, not by RBX1
  [PMID:14739464 "Human De-etiolated-1 regulates c-Jun by assembling a CUL4A ubiquitin ligase."].
- **GO:0060090 molecular adaptor activity** → MODIFY to GO:0031624: the scaffolding is
  CUL1's job; RBX1 recruits and activates the E2.
- **GO:0000109 nucleotide-excision repair complex** → MODIFY to GO:0031464: the complex
  RBX1 belongs to is CRL4(DDB2), not the NER incision machinery.
- **GO:0045732 / GO:0032436 (positive regulation of catabolism)** → MODIFY to GO:0043161:
  RBX1 executes the degradative step rather than regulating it from outside.
- **GO:0051298 centrosome duplication** → MODIFY to GO:0010824: the cited PMID:34388369 is
  the signal peptidase complex structure (same misattribution as in the CUL1 review), and
  the real evidence has SCF ligases restraining, not executing, duplication.
- **IBA rows (6)** are accepted as placed at the RING-box family node PTN000129805, whose
  descendants include human RBX1 itself, mouse Rbx1, fly Roc1a/Roc1b and yeast
  Hrt1/Rbx1 and Apc11; RBX1 appearing in its own WITH/FROM is the expected marker of
  experimental grounding on the target, not circularity.
- **Essentiality** (not annotatable, but relevant context): mouse Rbx1 disruption causes
  p27 accumulation, hypoproliferation and early embryonic lethality only partly delayed by
  deleting p27, and the yeast orthologue is essential
  [PMID:10230407 "YeastROC1 encodes an essential gene whose reduced expression resulted in multiple, elongated buds and accumulation of Sic1p and Cln2p."].

## Consistency with sibling reviews

Graded alongside `genes/human/CUL1` (the scaffold: GO:0160072 scaffold activity, receptor
outputs non-core) and `genes/human/ANAPC11` (the paralogous APC/C RING). ANAPC11 shares
the PTN000129805 IBA node with RBX1, and the cullin-binding split between them —
ROC1/ROC2 bind all cullins while APC11 is restricted to APC2 — comes from the same 1999
paper.
