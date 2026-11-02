# CSN2 (human beta-casein, P05814) - review notes

## Identity and biochemistry

- Secreted milk phosphoprotein, 226 aa precursor with a 15 aa signal peptide; mature
  chain 16-226. Belongs to the beta-casein family (Pfam PF00363, PANTHER PTHR11500),
  part of the secretory calcium-binding phosphoprotein (SCPP) cluster
  [PMID:12646701 "Many of these genes encode secretory Ca-binding phosphoproteins, which regulate the Ca-phosphate concentration of the extracellular environment"].
- Exists in six phosphoforms, 0-5 P per molecule, with all sites near the N-terminus
  [PMID:6715339 "For each form of this multiphosphorylated protein (0-5 P/molecule), phosphorylated sites at specific seryl and threonyl residues have been identified"];
  confirmed by 2-DE/MS [PMID:18847231 "The abundant beta-casein was resolved as a train of 6 spots differing in phosphorylation level with 0-5 phosphates attached"].
- Phosphorylated N-terminal cluster carries the calcium-binding capacity
  [PMID:2387396 "The highly phosphorylated site, which is responsible for the calcium-binding capacity of beta-casein, the signal peptide, and a sequence encoding for an inhibitor to the angiotensin-converting enzyme seem highly conserved among the beta-caseins with known sequences."].

## Role in the human casein micelle

- Beta-casein is the dominant human casein [PMID:11949848 "Human beta-casein (CN) is the major protein of the human milk casein fraction (approximately 80%) and exists in six calcium-sensitive forms"];
  human milk lacks alpha-s2 and has little alpha-s1 [PMID:36903269 "Human milk lacks αS2-casein, and the relative ratio of αS1-, β-, and κ-caseins in human milk is 3:70:27."].
- Micelles deliver calcium phosphate [PMID:7979373 "The function of human milk micelles is to deliver nutrients, particularly insoluble minerals such as the necessary calcium phosphate, to the child in a readily ingested suspension"].
- Low-P forms may provide a framework with colloidal calcium phosphate
  [PMID:9149957 "nonphosphorylated and singly phosphorylated human beta-CN may form a framework, as proposed for alpha s1-CN for bovine milk, along with the colloidal calcium phosphate for the development of the final micelle structure"].
- Reconstitution: beta-CN-4P forms reconstituted micelles with kappa-casein; Ca2+ bridges and hydrophobic interactions [PMID:11949848 "both hydrophobic interactions and Ca+2 bridges or crosslinks may contribute to protein aggregation and micelle building"]; inorganic phosphate enhances it [PMID:16283545 "while micelles will form with Ca+2 alone, added Pi has a significant enhancing effect on micelle formation"].

## Genetics (mouse ortholog)

- Csn2 knockout mice lactate and rear young; micelles smaller; pups grow slower
  [PMID:8016126 "Homozygous beta-casein mutant mice are viable and fertile; females can lactate and successfully rear young."]
  [PMID:8016126 "Despite the deficiency of beta-casein, casein micelles were assembled in heterozygous and homozygous mutants, albeit with reduced diameters."]
  [PMID:8016126 "The growth of pups feeding on the milk of homozygous mutants was reduced relative to those feeding on the milk of wild-type mice."]
  So beta-casein contributes to milk protein/micelle composition but is not individually essential (contrast Csn3 KO, PMID:16698927).
  Note: the batch prompt suggested "PMID:9671715" for the Csn2 KO; that PMID is a plasmid ParC paper. The correct Csn2 KO paper is PMID:8016126 (Kumar et al. 1994 PNAS).

## Peptide-derived activities

- Cysteine protease inhibition: reverse zymography of milk beta-casein and a synthetic
  L133-Q151 peptide [PMID:12788072 "beta-Casein and the active domain, synthesized L(133)-Q(151), peptide inhibited cysteine proteases."]. Single in vitro study,
  abstract-only, no in vivo evidence; marked as over-annotated (matching bovine, mouse and rat beta-casein).
- ACE inhibitor: only a sequence statement that a peptide encoded within beta-casein is an
  ACE inhibitor (PMID:2387396); no assay on human beta-casein in that paper. Fragment
  activity, not an activity of the intact secreted protein.
- Glycosylated C-terminal peptide reported to be antimicrobial [PMID:36903269 "which has antimicrobial functionality"]. Digestion product.

## Interactome

- Y2H hits with FHL2 and UBQLN2 (HuRI / Fragoza variant screen). Both are intracellular
  proteins; beta-casein is a secreted luminal protein. No functional significance.

## Expression / regulation

- Reactome R-HSA-1254290 describes ERBB4s80:STAT5A stimulating CSN2 transcription; this
  is regulation of the gene, not a function of the protein.

## Deep research

- OpenScientist run was in progress during this review; see report for integration status.

## Deep research integration (OpenScientist, 2026-10-24)

All PMIDs cited by the report were fetched into publications/ and the points used were
checked against the abstracts (or full text where cached).

- No contradictions with the review. The report's primary function (phosphoseryl-cluster
  calcium phosphate sequestration, micelle self-association, extracellular, lactation)
  matches the core function; it also treats beta-casomorphins, casein phosphopeptides and
  antimicrobial peptides as digestion products, consistent with the over-annotation calls
  on the peptide-derived rows.
- Added to GO:0140314 (NEW): PMID:38318529 ("β- and αS-caseins are highly effective mineral
  chaperones", unlike kappa-casein), PMID:31928725 (nanocluster sequestration by
  multiply-phosphorylated sequences) and a quote from the report.
- Added reference PMID:31826378 (beta-casein share of human milk protein rises from 33.8% in
  colostrum to 40.3% in mature milk).
- Not used: STAT5/GR/Oct-1 promoter regulation (PMID:23313770, 27130254, 24861805, 27044595;
  expression control, not beta-casein activity), bovine A1/A2 and BCM-7 work, FAM20C
  (kinase property), CPP metal binding (PMID:26434306; peptide fragment).

## Reviewer feedback (PR #5352, 2026-10-24)

- GO:0004869 cysteine-type endopeptidase inhibitor activity, IBA and IDA (PMID:12788072):
  KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED, matching bovine, mouse and rat beta-casein;
  added the missing propagation_review on the IBA row (same structure as mouse Csn2).
- GO:0005509 calcium ion binding: reason now records the OLS check that GO:0140314's only
  ancestors are metal ion sequestering activity (GO:0140487) and molecular sequestering
  activity (GO:0140313), so it is not under calcium ion binding. No action change.
- Status COMPLETE.
