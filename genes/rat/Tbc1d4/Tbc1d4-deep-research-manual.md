# Tbc1d4 (rat, D3Z881) - manual literature synthesis

No deep-research provider was available in this session; this summary was assembled
by hand from cached publications (`publications/PMID_*.md`) and PubMed searches.

## Identity
- Rat Tbc1d4 (AS160, Akt substrate of 160 kDa), RGD:1561609, GeneID 306117; TrEMBL
  entry D3Z881 (1245 aa). Ortholog of human TBC1D4 (UniProtKB:O60343) and mouse Tbc1d4
  (MGI:2429660). PANTHER PTHR47219:SF14 (TBC1 domain family member 4).
- Domain architecture (UniProt FT/DR lines): two N-terminal phosphotyrosine-binding
  (PTB/PID) domains (Pfam PF00640, 2 copies), DUF3350, a C-terminal Rab-GAP TBC domain
  (PROSITE PS50086, residues 865-1059), coiled coils.
- Local analysis (`Tbc1d4-bioinformatics/RESULTS.md`): the TBC arginine finger (ILVDLGR,
  R919) and glutamine finger (YCQ, Q956) are both present, so the rat protein is predicted
  to be a catalytically competent Rab GAP.

## Biochemical function (orthologs)
- AS160 has a functional Rab GAP domain: "The GAP domain was active against Rabs 2A, 8A,
  10 and 14." and the "recombinant GAP domain with the predicted catalytic arginine residue
  replaced by lysine was inactive" [PMID:15971998]. Assays used human AS160 GAP domain.
- Insulin-stimulated Akt phosphorylation of AS160 inactivates its GAP function, which is
  required for GLUT4 translocation in 3T3-L1 adipocytes: "this phosphorylation signals
  translocation through inactivation of the Rab GAP function" [PMID:12637568, abstract only].

## Rat-specific evidence
- Rat adipocytes (Koumanov et al. 2011) [PMID:21454690, full text]:
  - Rat AS160 PTB-domain constructs (cloned from a rat adipocyte cDNA library) inhibit
    insulin-stimulated GLUT4 vesicle fusion with the plasma membrane in a cell-free assay
    reconstituted from rat adipocyte fractions, and the tandem PTB construct inhibits
    insulin-stimulated GLUT4 translocation in intact rat adipocytes.
  - AS160 is present on immunoisolated GLUT4 vesicles from rat adipocytes, and its level
    there increases with insulin; "in rat adipose cells, AS160 is continuously associated
    with GLUT4 vesicles".
  - Model: insulin-stimulated 14-3-3gamma binding to phospho-AS160 generates a
    "fusion-activating GAP-inactive form of AS160"; otherwise "AS160 remains in its
    GAP-active form, the associated Rab remains in the GDP form, and fusion activity is
    therefore low".
- Rat L6 muscle cells (Sun et al. 2010) [PMID:21041651]: insulin activates Rab8A and
  Rab13; "Constitutively active AS160 lowered basal and insulin-stimulated levels of
  surface GLUT4, effects that were reversed by overexpressing Rab8A or Rab13".
- Rat skeletal muscle (Bruss et al. 2005) [PMID:15616009, abstract only]: AS160 is
  phosphorylated on Akt motifs in isolated rat epitrochlearis muscle in response to
  insulin, contraction and AICAR (AMPK).

## Synthesis
Tbc1d4 is a cytosolic Rab GTPase-activating protein that, in the basal state, keeps
GLUT4-vesicle Rabs (Rab8A/Rab10/Rab13/Rab14 class) GDP-bound and so restrains GLUT4
vesicle exocytosis. Insulin (Akt) and contraction/AMPK phosphorylate it, 14-3-3 binds,
the GAP is inactivated and GLUT4 vesicles become fusion competent, increasing glucose
uptake in adipocytes and muscle.
