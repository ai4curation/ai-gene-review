# CYP7A1 (Cytochrome P450 7A1 / cholesterol 7-alpha-hydroxylase) — review notes

UniProt: P22680 (CP7A1_HUMAN). HGNC:2651. 504 aa. Liver-enriched (HPA "Tissue enriched (liver)").
EC 1.14.14.23 (cholesterol 7alpha-monooxygenase) and EC 1.14.14.26 (24-hydroxycholesterol 7alpha-hydroxylase).

## Core biology
CYP7A1 is the rate-limiting, committed first enzyme of the **classic (neutral) bile-acid
biosynthesis pathway**. It is a microsomal cytochrome P450 monooxygenase that hydroxylates
cholesterol at the 7-alpha position to give 7alpha-hydroxycholesterol, using O2 and electrons
from NADPH via cytochrome P450 reductase (CPR).

- UniProt FUNCTION [file:human/CYP7A1/CYP7A1-uniprot.txt]: "Functions as a critical regulatory
  enzyme of bile acid biosynthesis and cholesterol homeostasis. Catalyzes the hydroxylation of
  carbon hydrogen bond at 7-alpha position of cholesterol, a rate-limiting step in cholesterol
  catabolism and bile acid biosynthesis."
- Catalytic activity (RHEA:21812, EC=1.14.14.23): cholesterol + reduced [NADPH--hemoprotein
  reductase] + O2 = 7alpha-hydroxycholesterol + oxidized [NADPH--hemoprotein reductase] + H2O + H(+).
- Cofactor: heme (Ref.12, SGC crystal structure 3DAX/3SN5/3V8D); axial heme-Fe binding residue = Cys444.
- SUBCELLULAR LOCATION: Endoplasmic reticulum membrane; single-pass membrane protein; also
  "Microsome membrane". TRANSMEM 4..24.
- PATHWAY: "Lipid metabolism; bile acid biosynthesis." and "Steroid metabolism; cholesterol degradation."

## Substrate range (oxysterols) — from primary literature
- [PMID:2384150 Noshiro & Okuda 1990] cloned the human cDNA (504 aa), 82% similarity to rat
  P-450ch7alpha; heme + steroid binding domains conserved. Basis for the classic
  cholesterol 7alpha-hydroxylase activity (EC 1.14.14.23). (Abstract-only; is the cloning +
  sequence paper. UniProt attaches CATALYTIC ACTIVITY / FUNCTION / PATHWAY / SUBCELLULAR
  LOCATION to this ref — full text carried the activity assay.)
- [PMID:11013305 Norlin et al. 2000] "Human CYP7A, recombinantly expressed in Escherichia coli
  and in simian COS cells, showed 7alpha-hydroxylase activity toward both cholesterol and the two
  isomers of 24-hydroxycholesterol, with a preference for the (24S)-isomer." Basis for
  GO:0033782 (24S-hydroxycholesterol 7-alpha-hydroxylase activity, EC 1.14.14.26). KM 3 uM
  cholesterol, 6 uM 24-OHC.
- [PMID:12077124 Bodin et al. 2002] "4 beta-hydroxycholesterol was 7 alpha-hydroxylated at a
  slower rate than cholesterol by recombinant human CYP7A1." Supports GO:0008123 IDA
  (recombinant human CYP7A1 7alpha-hydroxylates a sterol) and, biologically, bile acid
  biosynthesis / oxysterol elimination.
- [PMID:21813643 Shinkyo et al. 2011] (not in GOA; UniProt ref) CYP7A1 oxidizes 7-dehydrocholesterol
  to 7-ketocholesterol and lathosterol; additional catalytic activities.

## Regulation / transcription
- [PMID:19965590 Li et al. 2010] "High glucose stimulated bile acid synthesis and induced mRNA
  expression of cholesterol 7alpha-hydroxylase (CYP7A1), the key regulatory gene in bile acid
  synthesis." Glucose -> ATP up -> AMPK inhibited -> HNF4alpha up -> CYP7A1 transcription;
  also epigenetic (histone acetylation). This is a transcriptional-regulation study of the
  CYP7A1 *gene*; GOA uses it (IDA) for GO:0006699 (bile acid biosynthetic process),
  GO:0070857 (regulation of bile acid biosynthetic process) and GO:0071333 (cellular response
  to glucose stimulus). Note: the gene *responds to* glucose; the "regulation of bile acid
  biosynthetic process" here reflects CYP7A1's rate-limiting role, but as an IDA it is somewhat
  a transcriptional-response readout rather than a direct regulatory MF/BP of the protein.
- [PMID:15796896 Abrahamsson et al. 2005] (UniProt ref, not in GOA) feedback regulation of bile
  acid synthesis; HNF-4alpha important; down-regulated by chenodeoxycholic acid (FXR feedback),
  up by cholestyramine. Liver-specific.

## Disease
- CYP7A1 deficiency (Orphanet 209902, OMIM gene 118455): "Hypercholesterolemia due to cholesterol
  7alpha-hydroxylase deficiency" — hepatic cholesterol accumulation, hypercholesterolemia,
  premature gallstones / gallstone disease.

## Reactome
- R-HSA-192051 "CYP7A1 7-hydroxylates CHOL": cholesterol + NADPH+H+ + O2 -> 7alpha-cholesterol
  + NADP+ + H2O, in the ER membrane; expressed only in liver; transcriptionally regulated.
- R-HSA-193368 "Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol": classic
  pathway initiated by CYP7A1.
- R-HSA-211976 "Endogenous sterols": CYPs in cholesterol homeostasis.
- R-HSA-1989746 "Expression of CYP7A1": gene transcription/translation event.

## Annotation review decisions (summary)
Core MF: GO:0008123 cholesterol 7-alpha-monooxygenase activity (EXP/IDA/ISS/IBA/IEA all ACCEPT).
Core BP: GO:0006699 bile acid biosynthetic process; GO:0006707 cholesterol catabolic process.
Core CC: GO:0005789 endoplasmic reticulum membrane.
Cofactor MF (core-supporting): GO:0020037 heme binding, GO:0005506 iron ion binding.
GO:0033782 (24S-OHC 7alpha-hydroxylase) — ACCEPT (real minor activity, EXP PMID:11013305), keep non-core.
Regulatory/response BP (GO:0070857, GO:0071333, GO:0071397, GO:0042632) — KEEP_AS_NON_CORE / ACCEPT
as appropriate; these are downstream/physiological, not the enzyme's molecular action.

Over-annotation flags (Ensembl ortholog-transfer, GO_REF:0000107, from rat P18125):
- GO:0032966 negative regulation of collagen biosynthetic process — MARK_AS_OVER_ANNOTATED
  (indirect, ortholog-transferred; not a direct CYP7A1 function).
- GO:0045542 positive regulation of cholesterol biosynthetic process — MARK_AS_OVER_ANNOTATED
  (CYP7A1 is catabolic; any effect on cholesterol synthesis is indirect/homeostatic feedback).
- GO:0045717 negative regulation of fatty acid biosynthetic process — MARK_AS_OVER_ANNOTATED.
- GO:0045471 response to ethanol — KEEP_AS_NON_CORE (plausible physiological response, ortholog IEA).
</content>
