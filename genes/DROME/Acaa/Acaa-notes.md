# Acaa (Yip2 / CG4600) — Drosophila melanogaster — Research Notes

UniProt: Q9VL70 (unreviewed TrEMBL). FlyBase: FBgn0040064. Gene symbol Acaa; synonyms
Yip2 / yip2 / YIP2 ("Yippee interacting protein 2"), Dmel\CG4600. Ortholog of human ACAA2
(mitochondrial 3-ketoacyl-CoA thiolase, P42765; DIOPT 14/14 per FlyBase).

## Identity and family

- 398 aa protein (MW ~41.6 kDa). Belongs to the thiolase-like superfamily, thiolase family
  [UniProt Q9VL70, "Belongs to the thiolase-like superfamily. Thiolase family."].
- Two-domain thiolase architecture: Thiolase N-terminal (Pfam PF00108, res 8–268) and
  Thiolase C-terminal (Pfam PF02803, res 275–396) [UniProt Q9VL70 FT DOMAIN records].
- Conserved catalytic residues predicted by PIRSR: ACT_SITE 94 "Acyl-thioester intermediate"
  (nucleophilic Cys), ACT_SITE 354 and 384 "Proton acceptor" [UniProt Q9VL70 FT ACT_SITE].
  These correspond to the human ACAA2 catalytic Cys92 / His/Cys pair, consistent with a
  degradative (chain-shortening) thiolase mechanism.
- UniProt EC assignments (from EMBL submission AAF52826.1): EC 2.3.1.16 (acetyl-CoA
  C-acyltransferase / 3-ketoacyl-CoA thiolase, the beta-oxidation reaction) plus EC 2.3.1.9
  (acetyl-CoA C-acetyltransferase, the acetoacetyl-CoA reaction) and the parent EC 2.3.1.-,
  2.3.-.- [UniProt Q9VL70 DE lines]. PE 1: Evidence at protein level (PeptideAtlas).
- UniProt PATHWAY: "Lipid metabolism" [UniProt Q9VL70, ARBA:ARBA00005189].
- Reactome: R-DME-77289 "Mitochondrial Fatty Acid Beta-Oxidation" [UniProt Q9VL70 DR line].

## Function (ortholog-grounded)

Like human ACAA2, Acaa/Yip2 is predicted to catalyze the fourth and final (thiolytic) step of
each cycle of the mitochondrial fatty acid beta-oxidation spiral: 3-ketoacyl-CoA + CoA ->
acetyl-CoA + acyl-CoA(n-2), releasing acetyl-CoA and a fatty acyl-CoA shortened by two carbons.
The reaction (EC 2.3.1.16) corresponds to GO:0003988 (acetyl-CoA C-acyltransferase activity).
The domain architecture, active-site residues, and 14/14 DIOPT orthology to ACAA2 all support
this assignment. No direct Drosophila enzyme-assay of Yip2 was located; the fly annotations are
sequence/orthology-based (ISS/IBA/IEA), which is appropriate for a well-conserved metabolic
enzyme.

## Fly-specific literature

- Palanker, Tennessen, Lam & Thummel, "Drosophila HNF4 regulates lipid mobilization and
  beta-oxidation" (Cell Metab 2009; PMID:19254568; full text cached). This is the principal
  fly-specific functional context. Yip2 is one of a set of beta-oxidation genes coordinately
  regulated by the nuclear receptor dHNF4:
  - [PMID:19254568 "CG5321, CG2107, fatp, yip2, CG9577, CG6178, and Acox57D-d, many of which
    are predicted to act in β-oxidation"] — up-regulated in starved controls, down in dHNF4
    mutants (transcriptional target evidence, not a direct enzymatic assay of Yip2).
  - [PMID:19254568 "These include yip2, Acox57D-d, thiolase, scully, and CPTI (carnitine
    palmitoyltransferase) among the most highly down-regulated genes in fed dHNF4 mutants"].
  - dHNF4 mutants fail to mobilize lipid stores and are starvation-sensitive
    [PMID:19254568 "dHNF4 mutants are unable to properly mobilize their lipid stores upon
    nutrient deprivation"]. This places Yip2 in the fly mitochondrial beta-oxidation program
    but does not itself demonstrate Yip2's molecular activity.
  Note: the paper treats yip2 and "thiolase" (CG9149) as separate genes in the list, and
  distinguishes yip2 from "scully" (the fly MFE/HADH-type gene) — Yip2 is the degradative
  3-ketoacyl-CoA thiolase (ACAA2 ortholog).

- Faust, Verma, Peng & McNew, "An inventory of peroxisomal proteins and pathways in
  Drosophila melanogaster" (Traffic 2012; PMID:22758915; abstract-only cache). A proteome
  inventory / prediction study. It is the source of the ISM (predicted-from-sequence-model)
  GO:0005739 mitochondrion annotation on Yip2 in GOA. The abstract is about peroxisomes and
  does not describe Yip2 specifically; the associated GO annotation is a bioinformatic
  targeting-signal prediction (CG4600 carries a mitochondrial rather than peroxisomal signal).
  full_text_available: false.

- The "Yippee interacting protein 2" (Yip2) name derives from a two-hybrid interaction with
  the Drosophila Yippee protein (historical naming). No characterized, functionally meaningful
  Yippee–Yip2 complex activity is documented in GOA, and there is no protein-binding annotation
  in the fly GOA for Q9VL70. I did not find a validated fly interaction dataset to cite for a
  binding function, so no binding annotation is proposed.

## GOA annotation set (14 rows) — quick map

MF:
- GO:0003985 acetyl-CoA C-acetyltransferase activity (EC 2.3.1.9) — IBA, IEA(EC), ISS. The
  biosynthetic/acetoacetyl-CoA reaction. Secondary capability (thiolase reversibility), not core.
- GO:0003988 acetyl-CoA C-acyltransferase activity (EC 2.3.1.16) — IEA(ARBA), ISS. CORE MF.
- GO:0016746 / GO:0016747 acyltransferase activity (InterPro2GO) — over-general ancestors of 0003988.

BP:
- GO:0006635 fatty acid beta-oxidation — IBA, ISS. CORE process.
- GO:0006629 lipid metabolic process — IEA(ARBA). Over-general ancestor of 0006635.
- GO:1902109 negative regulation of mitochondrial membrane permeability involved in apoptotic
  process — ISS from human ACAA2 (BNIP3 story, PMID:18371312 in human). Transferred by orthology;
  the underlying human evidence is a single overexpression study. Non-core / contextual at best.

CC:
- GO:0005759 mitochondrial matrix — ISS (from ortholog). CORE location (soluble matrix thiolase).
- GO:0005739 mitochondrion — IBA, ISM(PMID:22758915). Correct but less specific than matrix.

## Reviewer decisions summary

- CORE: GO:0003988 (MF) + GO:0006635 (BP) + GO:0005759 (CC). Grounded in orthology (ACAA2),
  conserved domains/active sites, and fly beta-oxidation program membership (PMID:19254568).
- KEEP_AS_NON_CORE: GO:0003985 (biosynthetic acetoacetyl-CoA activity ×3), GO:0005739
  mitochondrion (IBA, ISM), GO:1902109 apoptotic-permeability (ortholog-transferred, single
  human overexpression study).
- MARK_AS_OVER_ANNOTATED: GO:0016746, GO:0016747 (generic acyltransferase ancestors),
  GO:0006629 lipid metabolic process (generic ancestor of beta-oxidation).
- No REMOVE actions: all fly annotations are defensible orthology/EC/InterPro inferences; none
  is contradicted by evidence. (The human cholesterol-biosynthesis NAS annotation that was
  REMOVE'd in the ACAA2 review does not exist in the fly GOA.)
