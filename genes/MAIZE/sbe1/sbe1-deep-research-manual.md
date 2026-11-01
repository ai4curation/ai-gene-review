# sbe1 (maize starch branching enzyme I, SBEI/BEI; UniProt Q41740) - manual literature review

No deep-research API was available for this session. This file summarises literature read
directly from the cached publications in `publications/` and PubMed searches
("maize branching enzyme I (SBEI OR BEI OR sbe1) starch"; "Guan H[Author] AND Preiss J[Author] AND maize branching").

## Identity
- UniProt Q41740 (TrEMBL, unreviewed), 823 aa, GeneID 542315, Gramene Zm00001eb228530. Gene is often called
  *Sbe1a* in the literature. cDNA from W64A x 182E endosperm [PMID:7630956 "A cDNA encoding starch branching enzyme I from maize endosperm."].
- Glycoside hydrolase family 13 (GlgB subfamily), PANTHER PTHR43651:SF2 (chloroplastic/amyloplastic branching
  enzyme). N-terminal CBM48, central GH13 (beta/alpha)8 catalytic domain (residues 274-634, SMART) with the nucleophile
  Asp415 and proton donor Glu470 (PIRSR000463-1), C-terminal alpha-amylase C domain, and a BEI-specific C-terminal
  extension (residues ~773-823, disordered) [UniProt Q41740].
- N-terminal plastid transit peptide; the mature protein is ~86 kDa
  [PMID:18281416 "The sequence of the maize BEI cDNA predicts a protein of approximately 86 kD after the plastid targeting peptide has been removed"].

## Enzymatic activity (direct biochemistry on the maize protein)
- Native BEI purified from developing endosperm free of amylase: highest activity on amylose; amylopectin branched at <5% of the amylose rate
  [PMID:12231902 "BEI had the highest activity in branching amylose, but its rate of branching amylopectin was less than 5% of that of branching amylose."].
- Recombinant mature BEI expressed in E. coli and purified to homogeneity reproduces native properties
  [PMID:8016271 "The recombinant enzyme showed properties very similar to those of BEI purified from developing maize endosperm with respect to branching amylose and amylopectin."].
- Maize BEI complements the branching defect of a glgB-deficient E. coli strain in vivo
  [PMID:7862674 "Transformation of the maize BE gene(s) in AC71 (glgB-) showed complementation in branching activity."].
- Chain-transfer specificity: BEI transfers longer chains than BEII
  [PMID:9185617 "SBEI predominantly transfers longer chains with dp greater than 10, while producing few shorter chains with dp 3 to 5."].
- No calcium or other cation requirement is reported in these papers. The reaction is a transglycosylation (EC 2.4.1.18), not hydrolysis.

## Localisation
- Studied as a soluble stromal protein of endosperm amyloplasts; also present at low levels inside starch granules
  [PMID:18281416 "three separate BE polypeptides (BEI, BEIIa, and BEIIb) from maize ( Zea mays ) amyloplasts"];
  [PMID:18653693 "In addition, SSIII, BEI, BEIIa, and starch phosphorylase were also found as internal granule-associated proteins."].
- Granule association increases strongly in *ae* (BEIIb-null) endosperm [PMID:18653693].
- Leaf expression is low; antibodies did not detect SBEI in leaves [PMID:11855730 "Antibodies failed to detect SBEI in leaf tissue of mutants or wild-type controls."].

## Complexes and interactions
- In gel permeation BEI runs exclusively as a monomer and is not part of the 300/600 kDa SS/BE complexes; one co-IP with SSI
  [PMID:18281416 "BEI stands out from the other five enzymes tested by its appearance exclusively as a monomer in the GPC analysis."].
- In *ae* amyloplasts BEI is recruited into SSI/SSIIa complexes and is phosphorylated [PMID:19805395 "in ae(-) amyloplasts,
  SSI and SSIIa interacted with SBEI, SBEIIa, and SP"] (abstract only; line wraps in cache).

## Genetics
- sbe1a::Mu null (Mu in exon 14): no SBEI protein in endosperm; starch size distribution and debranched chain-length
  profile indistinguishable from wild type [PMID:11855730 "Starches extracted from mutant leaves and endosperm have structures indistinguishable from starches of wild-type controls"].
- Finer analysis (beta-amylolysis followed by debranching) reveals altered branch-point distribution; mutant starch more resistant to
  pancreatic alpha-amylase; germinating mutant kernels have shorter coleoptiles and retain more starch [PMID:21599988
  "Molecular structure analysis suggests an important function of SBEI in modulating the branching pattern in normal starch by decreasing local clustering of amylopectin branch points."].
- The germination/coleoptile phenotype is a downstream consequence of starch structure, not a process SBEI performs.

## Synthesis
SBEI is a plastid (amyloplast) 1,4-alpha-glucan branching enzyme that introduces alpha-1,6 branch points during
starch synthesis, with a preference for amylose-like substrates and for transferring longer chains. It is largely
redundant with SBEIIa/SBEIIb for bulk starch structure but fine-tunes branch-point spacing in endosperm starch.
