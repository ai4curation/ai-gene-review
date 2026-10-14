# Snail (Sp-sna, Q6UCK0) — curation notes

## Identity
- UniProt Q6UCK0 (TrEMBL, "Zinc-finger transcription factor", gene name `Snail`), 341 aa, five
  C-terminal C2H2 zinc fingers (residues 199-341), N-terminal region with a SNAG-like basic
  stretch; "Belongs to the snail C2H2-type zinc-finger protein family" (UniProt SIMILARITY, ARBA).
  EMBL AY372519 / AAQ74988.1, RefSeq NP_999825.1, GeneID 378469. The sequence was a direct
  submission (Materna S.C., Davidson E.H., Aug-2003); there is no `RX PubMed=` line in the
  UniProt record. The accompanying publication is the genome-wide C2H2 survey
  [PMID:16997293 "we identified the C2H2 zinc finger genes indicated in the sequence, and examined their involvement in embryonic development"]
  (abstract only; the abstract does not name snail individually).
- PANTHER PTHR24388:SF54 ("PROTEIN ESCARGOT" subfamily); the IBA rows are seeded from the PAINT
  nodes PTN002810938 and PTN001227002; the WITH/FROM lists include human SNAI1 (O95863) and SNAI2
  (O43623), several Drosophila (FBgn) and mouse (MGI) Snail/Scratch-family genes, zebrafish and worm
  members.
- Community alias in the Davidson/McClay GRN literature: `snail`, `Sp-sna` (S. purpuratus),
  `Lv-snail` / `LvSnail2` (Lytechinus variegatus).

## What the gene product is
Snail-family zinc-finger transcriptional repressor. Snail proteins across animals repress
E-cadherin transcription and drive the de-adhesion step of epithelial-mesenchymal transition
(EMT) [PMID:24598159 "Snail and twist have been shown to directly repress transcription of E-cadherin ( Batlle et al., 2000 ; Cano et al., 2000 ; Vesuna et al., 2008 ) and snail upregulation destabilizes adherens junctions ( Kim et al., 2013 )"].

## Place in the sea urchin GRN (mostly Lytechinus variegatus data)
Important organism caveat: the functional work on sea urchin Snail was done in **Lytechinus
variegatus**, not S. purpuratus. Wu & McClay 2007 (Development; abstract only cached) is the
primary paper [PMID:17287249 "Here we identify a sea urchin ortholog of the Snail transcription factor, and focus on its roles regulating EMT during PMC ingression."]; the abstract itself does not state the species, but Shashikant et al. 2018 and Saunders & McClay 2014 both state it was L. variegatus [PMID:30264451 "Wu and McClay (2007), working with Lytechinus variegatus, provided evidence that this regulatory gene acts downstream of alx1 to regulate PMC ingression."].

Findings in L. variegatus:
- Required in micromeres for PMC ingression [PMID:17287249 "Functional knockdown analyses of Snail in whole embryos and chimeras demonstrate that Snail is required in micromeres for PMC ingression."].
- Represses cadherin transcription and is needed for cadherin endocytosis
  [PMID:17287249 "Snail represses the transcription of cadherin, a repression that appears evolutionarily conserved throughout the animal kingdom. Furthermore, Snail expression is required for endocytosis of cadherin, a cellular activity that accompanies PMC ingression."].
- GRN position: downstream of Pmar1 and Alx1, upstream of PMC-expressed genes
  [PMID:17287249 "Perturbation studies position Snail in the sea urchin micromere-PMC gene regulatory network (GRN), downstream of Pmar1 and Alx1, and upstream of several PMC-expressed proteins."].
- Timing: expressed just before EMT and switched off in PMCs shortly after ingression
  [PMID:18495103 "Snail is expressed just prior to EMT, and is necessary, shortly after its expression, for PMC ingression ( Wu and McClay, 2007 )"; "unlike snail expression , which disappears from PMCs shortly after ingression ( Wu and McClay, 2007 )"].
- Twist and snail both depend on Alx1, but a Twist->snail link is not established
  [PMID:18495103 "Here, expression of twist and snail both rely on Alx1, but as yet, one cannot conclude on the relationship between these two proteins in the sea urchin embryos."]. Lvtwist is downregulated in Sna morphants only at MB stage [PMID:18495103 "At MB stage Lvtwist is downregulated in Sna morphants, but not Alx1 or Ets1 morphants."].
- Saunders & McClay 2014 (full text cached): snail is one of the 13 pre-EMT TFs required for EMT
  [PMID:24598159 "Three TFs highest in the GRN specified and activated EMT (alx1, ets1, tbr) and the 10 TFs downstream of those (tel, erg, hex, tgif, snail, twist, foxn2/3, dri, foxb, foxo) were also required for EMT."]. Snail knockdown specifically blocks the de-adhesion sub-circuit while the other four cell-state changes still occur [PMID:24598159 "Our analysis of both snail and twist knockdowns showed a failure of PMCs to complete EMT in spite of four other successful cell state changes"]; alx1, twist and snail form the de-adhesion sub-circuit [PMID:24598159 "In L. variegatus , alx1, twist and snail constitute a functional sub-circuit in the GRN that controls the repression and endocytosis of cadherin required for de-adhesion ( Wu and McClay, 2007 ; Wu et al., 2008 )"]. Snail is NOT required for apical constriction [PMID:24598159 "in the sea urchin (a deuterostome) snail and twist, along with their upstream regulator alx1, are not required for apical constriction"]. In the Lv GRN snail also feeds erg [PMID:24598159 "In the Lv PMC GRN, snail regulates erg and erg regulates hex"]. The MASO used is called LvSnail2 [PMID:24598159 "1.0 mM LvSnail2 ( Wu and McClay, 2007 )"].
- Hardin & Illingworth 2006 (L. variegatus, abstract only): a snail homologue is also expressed
  transiently in subsets of non-skeletogenic (secondary) mesenchyme and in the ciliated band, and
  this expression is lost in radialized embryos [PMID:16958110 "these patterns are consistent with expression of SNAIL by novel subsets of SMCs that are largely distinct from skeletogenic mesenchyme. In radialized embryos lacking normal bilateral symmetry, mesenchymal expression of Lv-SNAIL is abolished."].

## S. purpuratus-specific evidence (sparse and conflicting)
Shashikant et al. 2018 (review, full text) summarise the situation
[PMID:30264451 "The possible role of the transcriptional repressor, snail, in the PMC GRN is currently unsettled."]:
- Oliveri et al. 2008 considered Sp-snail irrelevant to early PMC specification because it is
  expressed at very low levels until gastrulation [PMID:30264451 "Oliveri et al., (2008) concluded that, in S. purpuratus, snail is irrelevant with respect to early PMC specification because it is expressed at an extremely low level until gastrulation."]. (The cached text of PMID:18413610 does not itself mention snail.)
- Barsi et al. 2014 found Sp-sna enriched in PMCs at mesenchyme blastula; Rafiq et al. 2014 did
  not, and found Sp-sna *up* in Alx1 morphants, opposite to Lv [PMID:30264451 "One gene expression study (Barsi et al., 2014) reported a substantial enrichment of Sp-sna in PMCs at the mesenchyme blastula stage, as reported in L. variegatus, while another did not (Rafiq et al., 2014). In addition, the latter study reported that levels of Sp-sna mRNA increased in Alx1 morphants, in contrast to the findings in L. variegatus."]. (The cached text of PMID:24604781 and the abstract of PMID:24496631 do not name snail; the statements are taken from the review.)
- Saunders & McClay note snail/twist are in the Lv model but not the S. purpuratus GRN model
  [PMID:24598159 "The biggest difference between the current S. purpuratus GRN model and that shown in Fig. 1 is the observation that snail and twist are part of the L. variegatus GRN (Wu et al., 2007; Wu et al., 2008 )."].

## Curation decisions
- All six GOA rows are electronic (4 IBA, 2 IEA) and are sign-neutral TF / nucleus terms; all
  consistent with a Snail-family zinc-finger repressor. ACCEPT all.
- NEW rows kept minimal and flagged ISS (ortholog in L. variegatus): GO:0001227 (repressor
  activity; cadherin repression) and GO:0001837 (EMT; Snail executes the de-adhesion step via
  cadherin repression and is required for PMC ingression). Comparator check via QuickGO: human
  SNAI1 (O95863) carries GO:0001227 (IBA), GO:0001837 and GO:0010718 (ISS), GO:0000122 (ISS);
  Drosophila sna (P08044) carries GO:0000122 (IDA). So the EMT/repressor terms are the convention
  for Snail-family proteins that repress cadherin, not a gap in curation.
- Participation test: Snail is the repressor that directly silences the cadherin gene, i.e. it
  performs the de-adhesion step of EMT rather than merely being required upstream.
- No S. purpuratus perturbation data exist; the Sp-specific expression data are conflicting, so no
  NEW row is given an S. purpuratus IMP/IEP code. `gocams/index.tsv` has no entry for Q6UCK0.
- GO:0000122 is not added as a separate NEW row (descendant of the existing GO:0006355 row; the
  sign is captured by GO:0001227).
