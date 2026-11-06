# pslC (PA2233, Q9I1N6) notes

## Identity

- PslC, 303 aa, glycosyltransferase family 2 (Pfam PF00535 Glycos_transf_2;
  PANTHER PTHR43685:SF13 "O ANTIGEN BIOSYNTHESIS RHAMNOSYLTRANSFERASE RFBN").
  Unreviewed TrEMBL entry. Its UniProt name (dTDP-Rha:alpha-D-Gal-
  diphosphoundecaprenol alpha-1,3-rhamnosyltransferase, EC 2.4.1.377) and the
  O-antigen FUNCTION/PATHWAY lines are ARBA-only predictions, not evidence; Psl is
  not the O antigen.
- Third gene of the 15-gene psl operon (pslA-pslO).
- No deep-research provider was available; notes are from cached publications
  and PubMed searches (no PslC-specific biochemistry found).

## Literature

- PseudoCAP seed paper (Byrd et al. 2009, full text): in-frame deletions of each
  psl gene; pslC is among 11 genes required for Psl production and attachment
  [PMID:19659934 "In this study we have demonstrated that eleven of the fifteen psl genes, pslACDEFGHIJKL, are required for Psl synthesis and solid surface attachment."];
  attachment by crystal violet microtiter assay
  [PMID:19659934 "The ability of these fifteen mutants to attach to a solid surface was first assessed by crystal violet staining (Fig."].
  These are mutant phenotypes (IMP), not direct assays of the PslC protein (the
  PseudoCAP row says IDA).
- Psl structure: a repeating pentasaccharide of D-Man, D-Glc and L-Rha
  [PMID:19659934 "We also present the first structural analysis of the psl-dependent polysaccharide, which consists of a repeating pentasaccharide containing d-mannose, d-glucose and l-rhamnose"].
- Review (Franklin et al. 2011): PslC is a soluble predicted GT-2 (GT-A fold,
  inverting) glycosyltransferase whose sugar donor is unknown
  [PMID:21991261 "The remaining soluble GT, PslC, is predicted to belong to the CAZy GT-2 family, which adopt a GT-A fold and catalyze glycosyl transfer by an inverting mechanism"];
  [PMID:21991261 "Enzymes in the GT-2 family transfer a wide variety of nucleotide activated sugars (including glucose, rhamnose, and mannose), so it is difficult to speculate which of these substrates PslC specifically recognizes."].

## Interpretation

PslC is a predicted glycosyltransferase that adds one sugar of the Psl repeat
unit. Its role in biofilm formation is through Psl synthesis (biofilm formation
by definition includes production of the matrix polymers, so the claim is true
but derived). The process it directly performs is polysaccharide (Psl)
biosynthesis; GO has no Psl-specific term, so GO:0000271 is proposed as NEW (IMP).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002463206 | GO:0044010 single-species biofilm formation | 1 (sole seed) | 7 (5 taxa) | GO:0044010 single-species biofilm formation, IDA, PMID:19659934 (PseudoCAP) | INDIRECT-PHENOTYPE | The paper shows a pslC deletion abolishes Psl and surface attachment: a mutant phenotype (should be IMP), and biofilm formation is the downstream outcome of Psl synthesis, not something conserved in the GT clade. The node's other leaves are glycosyltransferases for unrelated glycans: Salmonella RfbN O-antigen rhamnosyltransferase (P26403), Bradyrhizobium ExoU (Q89D69, succinoglycan-type), P. aeruginosa FgtA flagellin glycosyltransferase (Q9I4N8), PA1390 (Q9I3V4), Geobacter Q74CL7 and Xanthomonas Q8P4N7. Biofilm formation does not suit a clade of GT-2 enzymes with diverse acceptors. The IBD should be removed; the safe node-level claim is glycosyltransferase activity. |

Node leaves were taken from the PAINT leaf GAF (`.cache/paint/leaf.gaf.gz`).

## Decisions summary

- KEEP_AS_NON_CORE: single-species biofilm formation (IDA, IBA).
- ACCEPT: glycosyltransferase activity (ISS).
- NEW: polysaccharide biosynthetic process (GO:0000271), IMP PMID:19659934.
- PSEUDOCAP defect: IDA should be IMP (PROBABLE).
- GO_CENTRAL defect: remove the GO:0044010 IBD at PTN002463206 (PROBABLE).
