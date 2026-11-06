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

## Leaf evidence check (2026-11-06)

Audit of the leaf claims in the `GO_CENTRAL` source defect on PTN002463206.
Membership confirmed with
`uv run python projects/PSEUDOCAP/panther_tree.py node PTN002463206 --leaves`
(7 leaves; PslC and RfbN in PTHR43685:SF13, the other five in SF2); UniProt
flat files fetched for all seven.

| Leaf | Name and its evidence | Experimental annotations | Verdict |
|---|---|---|---|
| P26403 (S. typhimurium RfbN) | RecName, curated (Reviewed, ECO:0000305); GN from ECO:0000303 PubMed:1710759; PE 1 | FUNCTION and PATHWAY by **ECO:0000269 PubMed:7684736**: rhamnosyltransferase adding rhamnose to the galactosyl-undecaprenyl-diphosphate LPS O-antigen intermediate | Claim **survives and strengthens**: experimentally characterised, product is LPS O-antigen, and it is PslC's closest relative (same subfamily SF13) |
| Q89D69 (B. diazoefficiens "exoU") | **SubName** "UDP-hexose transferase" {ECO:0000313\|EMBL}; PE 4 Predicted | none | "Succinoglycan ExoU" identity **does not survive**: predicted name only. What is checkable: PF00535 GT-2, 313 aa |
| Q9I4N8 (P. aeruginosa "FgtA", PA1091) | **SubName** "Flagellar glycosyl transferase, FgtA" {ECO:0000313\|EMBL}; PE 4 | none | Flagellin-glycosyltransferase identity **does not survive**. Stronger replacement fact: 1694 aa with Pfam PF04464 / InterPro IPR007554 TagF-like and **no GT-2 match at all**, so it does not even share PslC's catalytic domain |
| Q9I3V4 (P. aeruginosa PA1390) | **SubName** "Probable glycosyl transferase"; PE 4 | none | Uncharacterised; PF00535, 344 aa |
| Q74CL7 (G. sulfurreducens GSU1510.1) | **SubName** "Glycosyltransferase"; PE 4 | none | Uncharacterised; PF00535, 264 aa |
| Q8P4N7 (X. campestris XCC3670) | RecName derived from **ECO:0000259\|Pfam:PF00535**; PE 4 | none | Uncharacterised; PF00535, 231 aa |

Net effect: the "unrelated glycans" framing was overclaimed, because five of the
six leaves are uncharacterised and their glycan assignments were predicted
names. The argument is rebuilt on (a) RfbN's experimentally curated O-antigen
role, (b) the absence of any experimental annotation on the other six, (c)
domain content including FgtA's non-GT-2 architecture, and (d) the seed being a
deletion phenotype. Confidence held at PROBABLE: the checks strengthened the
one verifiable leaf but the "not a conserved function" step still rests partly
on absence of evidence.
