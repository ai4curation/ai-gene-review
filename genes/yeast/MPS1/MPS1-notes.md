# MPS1 (YDL028C, P54199) — curation notes

## Identity

Serine/threonine-protein kinase MPS1 (Monopolar spindle protein 1; RPK1), 764 aa, kinase
domain 440–720, catalytic Asp563, kinase-dead D580A behaves as a null
[PMID:7737118 "A mutation predicted to abolish kinase function not only eliminates in vitro protein kinase activity, but also behaves like a null mutation in vivo"].
PANTHER PTHR22974:SF21 (TTK subfamily). Human orthologue TTK (genes/human/TTK, complete review).
The deep-research file (`MPS1-deep-research-falcon.md`) was present and was used for orientation only;
every claim in the review is anchored to the cached primary papers.

## Holistic picture

Two intranuclear sites, three related outputs:

1. **SPB duplication** — founding phenotype. mps1-1 blocks the earliest step, satellite
   formation [PMID:1869587 "The MPS1 gene is found by electron microscopy to be essential for proper formation of the site at which the new SPB normally arises adjacent to the existing one."].
   Substrates: Spc42 [PMID:11827982 "Spc42p is a substrate for Mps1p phosphorylation in vitro, and Spc42p phosphorylation is dependent on Mps1p in vivo."],
   Spc110 S60/T64/T68 [PMID:11278681 "Ser(60), Thr(64), and Thr(68) are the major sites in Spc110p phosphorylated by Mps1p in vitro"],
   Spc29 (UniProt FUNCTION, PMID:19269975 not in GOA).
2. **SAC apex** — separable from SPB duplication [PMID:8567717 "indicating that failure of checkpoint function in mps1 cells is independent of SPB duplication failure"].
   Overexpression arrests wild type but not mad/bub mutants [PMID:8688079 "the overexpression of Mps1p induces modification of Mad1p and arrests wild-type yeast cells in mitosis with morphologically normal spindles"].
   Mechanism: Spc105 MELT phosphorylation → Bub3-Bub1; Bub1 phosphorylation → Mad1
   [PMID:24402315 "Mad1 kinetochore association in budding yeast is mediated by phosphorylation of a region within the Bub1 checkpoint protein by the conserved protein kinase Mps1"];
   PP1/Glc7 on Spc105 antagonises [PMID:32307893 "mutations lowering PP1 levels at Spc105 or forced association of Bub1 with Spc105 reinstate both chromosome biorientation and SAC signalling in mps1-3 cells"].
3. **Biorientation / attachment / clustering** — [PMID:18060784 "Mps1 promotes re-orientation of kinetochore-spindle pole connections and eliminates those that do not generate tension between sister kinetochores."];
   Ndc80 as receptor and substrate [PMID:19300438 "Mps1 interacts physically with the N-terminal domain of Ndc80 (Ndc80(1-257))"];
   Dam1 complex [PMID:25382489]; Cnn1 [PMID:22561345, PMID:23334295];
   Stu1 MELT motifs → Slk19 → clustering of unattached kinetochores, checkpoint-independent
   [PMID:42461244 "Mps1 controls this pathway by phosphorylating two conserved MELT motifs in Stu1 to recruit Slk19 and mediate kinetochore clustering"].
   Kinetochore release by autophosphorylation [PMID:31405987 "Mps1 autophosphorylation, rather than phosphorylation of other kinetochore components, was responsible for this dissociation."].

Meiosis: anchor-away of Mps1 shortens the checkpoint delay in mek1Δ
[PMID:37018287 "anchoring away of either Ipl1 or Mps1 in mek1Δ cells shortened metaphase by 42 minutes and 53 minutes, respectively"].

## Decisions of note

- **REMOVE GO:0004708 MAP kinase kinase activity (IEA, EC:2.7.12.2) and GO:0000165 MAPK cascade (IEA, inter-ontology).**
  UniProt gives Mps1 EC 2.7.12.2 because it is a dual-specificity kinase
  [PMID:7737118 "this kinase can phosphorylate serine, threonine and tyrosine residues, identifying Mps1p as a dual specificity protein kinase"],
  and GO maps that EC number to MAP2K activity (T-X-Y activation-loop phosphorylation). Mps1 has no MAPK substrate
  and no MAPK cascade role; the correct activity term is GO:0004712, already annotated (IDA/IBA/IEA). The cascade
  row is a mechanical consequence of the MF row.
- **KEEP_AS_NON_CORE GO:0004713 protein tyrosine kinase activity (IEA, Rhea).** Chemically true in vitro, but every
  mapped in vivo site (Spc110, Cnn1, Spc105/Stu1 MELTs, Bub1) is Ser/Thr.
- **protein binding (5 IPI rows).** Two Ndc80 pairs (PMID:19300438, PMID:20489023) → MODIFY to GO:0043515
  kinetochore binding (Ndc80 complex is the kinetochore receptor; SGD already has kinetochore binding IDA from
  PMID:31405987). Bem1 ×2 and Sla1 (SH3 interactome PMID:19841731; AP-MS network PMID:20489023) → REMOVE as
  uninformative high-throughput pairs (removal does not assert the interactions are false). Mps1 is not mentioned
  in the cached text of PMID:19841731 at all.
- **MARK_AS_OVER_ANNOTATED GO:0005777 peroxisome (IDA, PMID:36164978).** Single high-content screen with every ORF
  expressed from the constitutive NOP1 promoter
  [PMID:36164978 "Although all proteins were expressed under a constitutive promoter"]; Mps1 is only listed, no
  follow-up; no endogenous-promoter study reports peroxisomal signal. Not demonstrably false, so not REMOVE.
- **MODIFY GO:0031134 sister chromatid biorientation → GO:1990758 mitotic sister chromatid biorientation**
  (PMID:18060784 is on the mitotic spindle); **MODIFY GO:0051225 spindle assembly → GO:0090307 mitotic spindle
  assembly** (PMID:15668173 mps1-as1; GO:0090307's definition runs to stable kinetochore attachment, which is the
  Mps1-governed step). Both ids verified in QuickGO.
- GO:0051988 (IMP, PMID:23334295) ACCEPTed: the Cnn1 S74 result is a modest input to attachment regulation, but the
  term is well supported for the gene overall (PMID:18060784, PMID:32307893 added as additional references).
- GO:0034501 protein localization to kinetochore (IGI with SPC105) ACCEPTed: Mps1 itself creates the phospho-docking
  sites for Bub3-Bub1 and Mad1, so it does the work rather than merely being required.
- GO:0007094 IGI (PMID:8688079) lists BUB2 among partners; Bub2 is a MEN component rather than a SAC protein, but
  that reflects the mutant panel of the paper and does not affect the Mps1 annotation.
- All IBA rows ACCEPTed; SGD:S000002186 (MPS1 itself) in WITH/FROM reflects the yeast IDA/IMP rows used to place
  the ancestral nodes (PTN001122082 Mps1/TTK subfamily; PTN000540737 deeper family node).
- No NEW terms proposed. Candidate considered and rejected: "repair of mitotic kinetochore microtubule attachment
  defect" (GO:0140273) as used for human TTK — in yeast the biorientation function is already captured by
  GO:0031134/GO:1990758 and adding a sibling would be redundant.

## Cache status

Abstract-only: PMID:15668173, 16319894, 1869587, 20489023, 7737118, 8567717, 8688079 (all abstracts explicitly
state the results used). Full text: all others. WITH/FROM SGD ids resolved via the SGD API: S000005783 CDC31,
S000003054 MAD1, S000003420 BUB1, S000003550 MAD3, S000003567 MAD2, S000004659 BUB2, S000005552 BUB3,
S000003061 SPC105, S000005878 MEK1.

## Validation

`just validate yeast MPS1` — valid, no warnings (2026-09-26). Rendered with `just render yeast MPS1`.
Actions: ACCEPT 38, REMOVE 5, MODIFY 4, KEEP_AS_NON_CORE 1, MARK_AS_OVER_ANNOTATED 1 (49 rows).
