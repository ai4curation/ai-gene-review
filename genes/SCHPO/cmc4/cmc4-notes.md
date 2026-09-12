# cmc4 (SPAC4F10.22 / tam2) — S. pombe — review notes

UniProt: G2TRJ8 (CMC4_SCHPO). 70 aa. Reviewed. PE 1 (protein-level evidence,
via MS identification in PMID:21270388). Standard name cmc4; synonym tam2
("transcripts altered in meiosis protein 2"); systematic name SPAC4F10.22.

## Identity / domain reasoning (from UniProt record, inline)

- RecName: "Cx9C motif-containing protein 4, mitochondrial"; SIMILARITY: "Belongs
  to the CMC4 family" (ECO:0000305). PANTHER PTHR15590 / PTHR15590:SF0 =
  "CX9C MOTIF-CONTAINING PROTEIN 4" (family is dedicated to CMC4; 1673 members,
  1528 proteomes). Pfam PF08991 (CMC4). InterPro IPR027179 (CMC4) +
  IPR009069 (Cys_alpha_HP_mot_SF, cysteine alpha-hairpin motif superfamily).
- Domain features (UniProt): CHCH domain 1..43 (PROSITE PS51808, PRU01150);
  MOTIF "Cx9C motif 1" 4..14; MOTIF "Cx9C motif 2" 25..35; DISULFID 4..35 and
  14..25. This is the canonical **twin CX9C** arrangement forming a helical
  hairpin stabilized by two disulfide bonds — the diagnostic feature of the
  CHCH/twin-CX9C IMS protein class.
- Sequence (70 aa): MVDCQKEACN LQSCIQRNQY NQGNCEKFVN DLLLCCKRWY DKNSLTGNEA
  PHTCPELKPL LRQLSSRNLT. Cys at 4,9,14,25,30,35 (the twin CX9C: C4..C14 and
  C25..C35 spacing) plus additional Cys (C39,C40 region "LLLCCKRWY", C63). This
  matches the review's statement that yeast CMC4 has eight cysteines, four in the
  twin CX9C motif [PMID:33498264 "In yeast, CMC4 has eight cysteine residues,
  four of which comprise the twin CX9C motif."].
- SUBCELLULAR LOCATION (UniProt, ECO:0000250 by similarity): "Mitochondrion
  intermembrane space"; Note "Imported into the mitochondria via the
  mitochondrial mia40-erv1 machinery." DOMAIN: "The twin Cx9C motifs are involved
  in the recognition by the mitochondrial mia40-erv1 disulfide relay system and
  the subsequent transfer of disulfide bonds by dithiol/disulfide exchange
  reactions to the newly imported protein."

Domain reasoning: the twin CX9C + CHCH fold, the MIA40/Erv1 import route, and
membership in the CMC4/PTHR15590 family are all mutually consistent and
well-established for this protein class. IMS localization and MIA40-dependent
import are therefore domain-defensible, high-confidence inferences even though
the pombe protein itself has not been localized experimentally (the UniProt
localization is ECO:0000250 = by similarity, and the sole GOA experimental-type
support is phylogenetic IBA + IEA SubCell mapping).

## Orthology (PANTHER PTHR15590:SF0, file interpro/panther/PTHR15590/)

One-to-one CMC4 orthologs across fungi and animals: S. cerevisiae CMC4
(Q3E7A9, 73 aa), human CMC4 (P56277, 68 aa), mouse Cmc4 (Q61908), Candida,
Yarrowia, etc. Family is a single-subfamily (SF0) group — cmc4 is the sole
pombe member; no pombe paralog. Human/yeast ~30% identity; 7 of 8 cysteines
conserved to human [PMID:33498264].

NOTE ON FAMILY NOMENCLATURE: CMC4 is a DISTINCT member of the broader
"conserved mitochondrial (twin CX9C) COX assembly / CMC" grouping. The
well-characterized copper chaperones **Cmc1 and Cmc2** (metallation of COX and
IMS-Sod1) are SEPARATE proteins/families — do NOT transfer their specific
copper-chaperone function to CMC4. CMC4 itself is much less characterized.

## KNOWN (evidence-supported)

1. It is a small (70 aa) mitochondrial IMS protein of the twin-CX9C / CHCH
   (CMC4) family, imported by the MIA40(Mia40)-Erv1 disulfide relay. Domain +
   family + orthology; GOA IBA to GO:0005758 (mitochondrial intermembrane space,
   PANTHER:PTN000400520). [UniProt G2TRJ8; PMID:33498264]
2. cmc4 = tam2: transcript differentially expressed during meiosis in pombe;
   protein detected by MS. tam2Δ is VIABLE (no essential vegetative role).
   [PMID:21270388 "Fourteen transcripts were differentially expressed during
   meiosis"; "While tam2 .Δ was viable, new21 was not"]
3. Across the family, CMC4 is non-essential for respiration: yeast CMC4 knockdown
   produces no respiratory defect. [PMID:33498264 "The limited studies in yeast
   show that CMC4 knockdown produces no defect in respiration"]
4. Human CMC4 interacts with SCO1 (COX II copper-delivery assembly factor) in an
   affinity-purification/proximity-labeling study → suggested non-essential role
   in COX II sub-assembly. [PMID:33498264 "an affinity purification–mass
   spectrometry proximity labeling study determined that CMC4 interacts with SCO1
   in human cell cultures ... This suggests that CMC4 plays a non-essential role
   in COX II sub-assembly."]

## NOT known / knowledge gaps

- No defined **molecular function** for cmc4/CMC4: GOA has GO:0003674 ND (root,
  "no data"). No enzymatic activity; no demonstrated ligand/metal binding for
  CMC4 specifically (unlike Cmc1/Cmc2 which bind Cu(I)). Whether CMC4 is a
  metallochaperone, a redox/disulfide-relay accessory, or an adaptor is unknown.
- No demonstrated **biological process** for cmc4 in pombe: GOA has GO:0008150 ND.
  The COX II sub-assembly role is (a) inferred from human, (b) non-essential,
  (c) not tested in pombe. Meiotic transcript induction (tam2) has no assigned
  meiotic function; tam2Δ viable, no reported meiotic/sporulation phenotype.
- No experimental **localization** in pombe (IMS is by-similarity / IBA / IEA).
- The specific **client/target** of CMC4 in COX assembly (does it act on SCO1,
  COX2/CuA delivery, or elsewhere?) and its **in-vivo pombe phenotype** are open.

## Annotation plan

GOA has 4 annotations:
1. GO:0005758 IMS, IBA (GO_REF:0000033) → ACCEPT (core; domain+family+orthology
   support; the one substantive annotation).
2. GO:0005758 IMS, IEA SubCell (GO_REF:0000044) → ACCEPT (redundant electronic
   version of same well-supported localization).
3. GO:0003674 MF root, ND (GO_REF:0000015) → ACCEPT (honestly reflects unknown MF;
   ND root placeholder is correct given no defined MF).
4. GO:0008150 BP root, ND (GO_REF:0000015) → ACCEPT (honestly reflects unknown BP).

core_functions: one MF-less entry anchored on the IMS location + twin-CX9C
identity (avoid inventing a COX-assembly MF for pombe). Actually core_functions
requires molecular_function; use the mitochondrial IMS protein-of-the-twin-CX9C
family framing carefully — see FUNCTION_KNOWLEDGE_GAPS guidance. Emphasize
knowledge_gaps as the primary deliverable.

Refs to cite: PMID:11859360 (genome), PMID:21270388 (tam2/meiosis/viable, MS),
PMID:33498264 (CMC4 review: IMS, twin CX9C, MIA40, non-essential, SCO1).

## Deep research provenance

Automated deep research was attempted via
`scripts/deep_research_wrapper.py SCHPO cmc4 falcon --fallback perplexity-lite`
(foreground/background, ~35 min) and produced NO output before hanging; it was
terminated (exit 144) with no `-deep-research-*.md` file generated. This review
is therefore grounded directly in: the UniProt record (G2TRJ8), the QuickGO GOA
(4 annotations), PANTHER PTHR15590 orthology (interpro/panther/PTHR15590/), and
two PubMed-verified publications with full text in the cache — PMID:21270388
(tam2 identity, meiotic regulation, tam2Δ viable) and PMID:33498264 (the twin
CX9C / COX review with the only CMC4-specific functional statements: IMS
localization, MIA40 import, non-essential for respiration, SCO1 interaction).
No function was invented; all supporting_text quotes are verbatim substrings of
the cached publications.
