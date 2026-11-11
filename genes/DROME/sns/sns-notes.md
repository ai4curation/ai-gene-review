# sns / Q0E9F2

Forty GOA rows were reviewed using gene-specific primary evidence. [PMID:10859168](https://pubmed.ncbi.nlm.nih.gov/10859168/) establishes the unfused-myoblast phenotype and membrane localization; [PMID:19270174](https://pubmed.ncbi.nlm.nih.gov/19270174/) identifies Sns as the ligand of Kirre/Roughest; [PMID:18971929](https://pubmed.ncbi.nlm.nih.gov/18971929/) and [PMID:19515699](https://pubmed.ncbi.nlm.nih.gov/19515699/) establish the nephrocyte diaphragm function. [PMID:24485456](https://pubmed.ncbi.nlm.nih.gov/24485456/) directly measures Drosophila adhesion heterocomplexes despite its worm-focused title. Binding to Mec2 and Unc-5 is kept noncore; Roughest binding is specified as cell adhesion molecule binding. Abstract-only evidence leaves homophilic adhesion and the specific actin-focus result unresolved, without rejecting the experiments.

The [sequence analysis](sns-bioinformatics/RESULTS.md) finds that selected Q0E9F2 isoform B contains all 1479 residues of RefSeqA identically, plus 63 residues around the membrane-entry region. The insert has its own predicted transmembrane segment. This is a concrete topology concern, not absence of a separate assay for every isoform. Gene-level annotations are reviewed as gene-level evidence; the two broad developmental ProtNLM claims remain UNC for this exact longer sequence pending topology/functional assessment. Membrane localization remains supported and is LSP. These findings do not imply wrong predictor input or prove the longer isoform inactive.

## Sequence and research provenance

The selected frozen UniProt record is retained in [sns-uniprot-source.json](sns-uniprot-source.json), with the complete original prediction metadata in [sns-predictions-source.json](sns-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

## Completed provider readback

The wrapper timed out and its fallback reported insufficient quota, but the original Falcon job later produced a complete report. The report and primary sources were inspected; no duplicate provider submission was made. The report correctly summarizes gene-level adhesion/fusion and nephrocyte functions, and cautions that foundational constructs are not isoform-B-specific. The exact hydrophobic insertion remains established by the local analysis; report statements about the standard single-pass model do not resolve its topology.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not consulted. All 40 GOA rows were re-examined against the cached primary literature
and the PANTHER/PAINT placement.

**Identity.** Q0E9F2 is the unreviewed TrEMBL entry for FlyBase isoform B (CG33141-RB, 1542 aa). The
gene has no Swiss-Prot entry; the other UniProt products are A1Z7J1 (isoform A, 1479 aa), A0A0B4LEH1
(isoform C, 1492 aa) and Q9V4Y0 (SNS, 1482 aa), all in PTHR11640:SF136. Per the existing
[sequence analysis](sns-bioinformatics/RESULTS.md), isoform B contains all 1479 residues of isoform A plus
a 63-residue insertion (1060–1122) with an extra predicted TM segment (1089–1112). All Ig/FN3 domains and
the shared cytoplasmic tail are retained. Q0E9F2 is the entry that carries every gene-level GOA row, so it is
the de facto annotated product of the gene and not a fragment. Gene-level experiments are reviewed here.

**Evolutionary placement.** PANTHER PTHR11640:SF136 (NEPHRIN) holds Sns, its paralog Hbs, human/mouse/rat
nephrin (NPHS1) and C. elegans SYG-2. The partners Kirre/Duf and Rst are in SF31 (Kirre/Neph1-type).
The IBA rows come from PTN002267852, with sns itself among the donors. That is expected and not circular.
Family review interpro/panther/PTHR11640/PTHR11640-review.yaml also places Q0E9F2 in SF136, so the placement
is the same. One minor wording point: its SF136 description reuses the family-level heterogeneity text
("extends beyond nephrin to kin-of-irre proteins"). That describes the whole PTHR11640 family and not SF136,
because Kirre/Rst sit in SF31.

**Changes from the previous review**
- GO:0001751 compound eye photoreceptor cell differentiation (NAS, PMID:20599904): KEEP_AS_NON_CORE → MODIFY
  to GO:0001745 compound eye morphogenesis. The paper is about ommatidial separation by preferential adhesion,
  not photoreceptor differentiation.
- Two bare GO:0005515 rows (Mec-2 Y2H, Unc-5 interactome): KEEP_AS_NON_CORE → REMOVE under the protein-binding
  policy. The interactions themselves are not disputed. The Rst rows remain MODIFY → cell adhesion molecule binding.
- GO:0016020 membrane: ACCEPT → MODIFY to plasma membrane, which the gene already carries.
- GO:0009653 / GO:0030154 / GO:0160108 (ARBA): KEEP_AS_NON_CORE → TOO_GENERAL. OLS ancestry confirms each is
  entailed by retained specific terms (compound eye/chaeta morphogenesis, myoblast fusion, garland nephrocyte
  differentiation, larval visceral muscle development).
- GO:0016202 regulation of striated muscle tissue development and GO:1901739 regulation of myoblast fusion
  (ComplexPortal NAS): MODIFY → GO:0007520 myoblast fusion. Sns does part of the work of fusion (it is the FCM
  ligand of Duf/Rst) and has no shown regulatory role.
- GO:0030036 actin cytoskeleton organization (IMP, PMID:18003739): UNDECIDED → KEEP_AS_NON_CORE. Full text
  was not retrievable (PMC publisher restriction). The abstract says known fusion components regulate the
  actin foci, and the reconstitution work cited in the Falcon report supports an Sns–WASP/SCAR link. The
  Arp2/3 machinery carries out the polymerization, so the row is not core.
- GO:0007156 homophilic cell-cell adhesion (IGI with kirre): stays UNDECIDED. The IGI partner and the known
  Sns–Kirre trans binding suggest heterophilic adhesion between homotypic cells, but the full text is not
  available, so the curator is not overruled.
- Rows citing PMID:18971929, PMID:38878170 and PMID:15955848 now quote those papers directly.
- The description was rewritten around nephrin-subfamily placement. Status set to COMPLETE.

**Relative for next review.** Human NPHS1 (nephrin, O60500) is in the same PANTHER subfamily SF136 and is
named as the Sns ortholog (PMID:19515699 title). It is the best-characterised member, and the repo has no
human NPHS1 review. The paralog hbs (same SF136) already has a complete review.

**Modules.** modules/dmel_irm_myoblast_adhesion.yaml (kirre_sns and rst_sns complexes) includes Q0E9F2.
