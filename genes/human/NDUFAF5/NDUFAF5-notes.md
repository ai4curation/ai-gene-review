# NDUFAF5 (Q5TEU4) research notes

Human gene **NDUFAF5** (HGNC:15899; formerly **C20orf7**), UniProt **Q5TEU4** (NDUF5_HUMAN),
GeneID 79133, chromosome 20. 345 aa precursor with an N-terminal mitochondrial transit peptide
(residues 1-36); mature chain 37-345.

## One-line summary

NDUFAF5 is a mitochondrial **arginine hydroxylase** that hydroxylates a conserved arginine of the
Complex I core subunit **NDUFS7** at an early stage of respiratory Complex I (NADH:ubiquinone
oxidoreductase) assembly. Despite belonging to the SAM-dependent 7β-strand methyltransferase
structural family, its catalytic output is hydroxylation (an oxidoreductase reaction), not methyl
transfer. It is an **assembly factor**, NOT a structural subunit of the mature holoenzyme.

## Catalytic function — the key biochemistry

- UniProt RecName is "Arginine-hydroxylase NDUFAF5, mitochondrial" with **EC=1.-.-.-**
  (ECO:0000305|PubMed:27226634), i.e. classed as an **oxidoreductase**, and an AltName
  "Putative methyltransferase NDUFAF5" (EC=2.1.1.-, ECO:0000305).
  [file:human/NDUFAF5/NDUFAF5-uniprot.txt "FUNCTION: Arginine hydroxylase that mediates hydroxylation of 'Arg-111'"]
  (UniProt numbers Arg-111 on the NDUFS7 precursor; the primary paper reports Arg-73 of mature NDUFS7.)

- Rhein et al. 2016 (JBC) is the defining mechanistic study. NDUFAF5 "is another member of the
  7β-strand family of SAM-dependent methyltransferases"
  [PMID:27226634 "NDUFAF5 is another member of the 7β-strand family of SAM-dependent methyltransferases"],
  but like the anthracycline enzyme RdmB it performs hydroxylation:
  "RdmB has no methyltransferase activity, and SAM acts as a cofactor in the process of hydroxylation"
  [PMID:27226634 "RdmB has no methyltransferase activity, and SAM acts as a cofactor in the process of hydroxylation"].
  The precedent is explicit: "that a member of the family of SAM-dependent 7β-strand methyltransferases
  is a hydroxylase has a precedent"
  [PMID:27226634 "that a member of the family of SAM-dependent 7β-strand methyltransferases is a hydroxylase has a precedent"].
  SAM is required but not consumed as a methyl donor:
  [PMID:27226634 "SAM is a crucial feature of the hydroxylation reaction as S-adenosylhomocysteine cannot substitute for SAM"].

- Substrate/site: NDUFS7's conserved arginine is fully hydroxylated —
  [PMID:27226634 "the conserved arginine residue (residues 73 and 77 in the human and bovine complexes, respectively) is completely hydroxylated"].
  siRNA knockdown of NDUFAF5 (but not the paralogous methyltransferase NDUFAF7) reduces this hydroxylation:
  [PMID:27226634 "suppression of the expression of NDUFAF5 with 50 nm siRNA reduced the relative hydroxylation of Arg-73 by 49%"].

### GO MF term choice

- **GO:0016491 oxidoreductase activity** is the chosen catalytic core-function term. It matches
  UniProt's authoritative RecName/EC classification (Arginine-hydroxylase, EC 1.-.-.-,
  ECO:0000305|PubMed:27226634) and the GOA IEA-KW annotation, and is mechanism-agnostic given that the
  exact hydroxylase subclass (cofactor requirements, oxygen incorporation) is not fully defined.
- **GO:0106157 peptidyl-arginine 3-dioxygenase activity** was considered and **rejected**: its
  definition is a **2-oxoglutarate/O2-dependent dioxygenase** reaction
  (2-oxoglutarate + [protein]-L-arginine + O2 → [protein]-(3R)-3-hydroxy-L-arginine + CO2 + succinate),
  which does NOT match NDUFAF5's **SAM-dependent, RdmB-like** mechanism. Asserting it would over-specify
  a mechanism the literature contradicts. Flagged in `proposed_new_terms` instead (a SAM-dependent
  peptidyl-arginine hydroxylase MF term would be ideal but does not yet exist).
- **GO:0008757 SAM-dependent methyltransferase activity** (IEA:InterPro): NDUFAF5 has the SAM-binding
  Rossmann fold but does **not** transfer a methyl group to NDUFS7; the direct substrate assay shows
  hydroxylation, not methylation. This is a family-fold-based over-annotation → MARK_AS_OVER_ANNOTATED.
- **GO:0008137 NADH dehydrogenase (ubiquinone) activity** is NOT assigned: NDUFAF5 is an assembly
  factor, not a catalytic/structural subunit of the holoenzyme; it dissociates before the mature
  complex forms.

## Biological process

- Core BP: **GO:0032981 mitochondrial respiratory chain complex I assembly** (multiple independent
  experimental IMP annotations + IBA). NDUFAF5 acts early:
  [PMID:27226634 "The suppression of NDUFAF5 affected the biogenesis of complex I at an early stage of assembly"]
  and its loss affects both arms:
  [PMID:27226634 "the participation of NDUFAF5 in the pathway of assembly of complex I affects both arms of the complex"].
- Sugiana et al. 2008 established the disease link and assembly role:
  [PMID:18940309 "crucial in the assembly of complex I and that mutations in C20orf7 cause"] mitochondrial disease;
  RNAi decreases Complex I activity and patient fibroblasts show near-complete loss of holoenzyme.
- Reactome places NDUFAF5 in the MT-ND1:NDUFAF5:NDUFAF6 intermediate of Complex I biogenesis
  (R-HSA-6799191, R-HSA-6799198 "Complex I biogenesis").

## Localization

- **Mitochondrial inner membrane, matrix (peripheral) face.**
  [file:human/NDUFAF5/NDUFAF5-uniprot.txt "Peripherally localized on the matrix"] face of the inner membrane.
  Sugiana et al.: [PMID:18940309 "peripherally associated with the matrix face of the"] mitochondrial inner membrane.
  Rhein et al. localized tagged NDUFAF5 to mitochondria:
  [PMID:27226634 "NDUFAF5 with a C-terminal FLAG tag was found uniquely in the mitochondria of human 143B cells"].
- GO:0099617 (matrix side of mitochondrial inner membrane, IDA) is the most precise CC and captures
  both the membrane association and matrix-face topology.

## Interactions / stabilization

- **NDUFS7** (O75251) — the catalytic substrate; direct interactor
  [PMID:27226634] (IPI, UniProtKB:O75251). This is the mechanistically meaningful "protein binding".
- **NDUFAF8** (A1L188) — interacts with and stabilizes NDUFAF5 [PMID:27499296] (IntAct NbExp=11);
  also picked up in BioPlex interactome screens [PMID:28514442, PMID:33961781] (all IPI to A1L188).
- **PYURF** (Q96I23, "protein preY"/NDUFAFQ) — direct interaction via TRM112 domain stabilizes NDUFAF5
  [PMID:35614220]; PYURF is a SAM-dependent methyltransferase chaperone
  [PMID:35614220 "methyltransferase chaperone that supports both complex I assembly"].
- All these are captured by GOA as bare "protein binding" (GO:0005515) IPI annotations. Per curation
  policy these are marked MARK_AS_OVER_ANNOTATED (uninformative MF); the biology is better captured by
  the assembly BP and, for NDUFS7, the substrate relationship.

## Disease

Biallelic NDUFAF5 variants cause **Mitochondrial complex I deficiency, nuclear type 16 (MC1DN16;
MIM:618238)**, autosomal recessive, presenting as lethal neonatal mitochondrial disease and Leigh
syndrome. Reported variants: L159F [PMID:19542079], L229P [PMID:18940309], G250V [PMID:21607760].

## Annotation-review disposition (summary)

- GO:0032981 complex I assembly — ACCEPT (core BP); experimental IMP ×2 + IBA + IEA.
- GO:0016491 oxidoreductase activity (KW-IEA) — ACCEPT (best available catalytic MF); this is the
  correct broad class per UniProt EC 1.-.-.-.
- GO:0008757 SAM-dependent methyltransferase activity (IEA:InterPro) — MARK_AS_OVER_ANNOTATED
  (fold-based; enzyme is a hydroxylase, not a methyltransferase, per PMID:27226634).
- GO:0099617 matrix side of mito inner membrane (IDA) — ACCEPT (most precise localization).
- GO:0005743 mito inner membrane (EXP ×3, IEA-SubCell, TAS-Reactome) — ACCEPT/KEEP (correct, less specific).
- GO:0005739 mitochondrion (IDA, IBA, IEA, HTP) — ACCEPT/KEEP (correct, general).
- GO:0005515 protein binding (IPI): NDUFS7 (O75251), NDUFAF8 (A1L188 ×3), PYURF (Q96I23) —
  MARK_AS_OVER_ANNOTATED (bare "protein binding" uninformative; do not REMOVE experimental IPI).

## Candidate new term

A **SAM-dependent peptidyl-arginine hydroxylase** molecular-function term (analogous to RdmB-type
SAM-cofactor hydroxylases) would precisely capture NDUFAF5's activity; the existing peptidyl-arginine
3-dioxygenase term (GO:0106157) is mechanistically inappropriate (2-oxoglutarate-dependent).
