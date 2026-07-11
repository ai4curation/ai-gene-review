# GALC (Galactocerebrosidase / Galactosylceramidase) review notes

UniProt: P54803 (GALC_HUMAN); HGNC:4115; EC 3.2.1.46; gene on chr14.
Glycosyl hydrolase family GH59 (CAZy GH59; Pfam PF02057).

## Core biology (verified)

GALC is a **lysosomal glycosidase** of glycosphingolipid catabolism. It hydrolyses the
terminal galactose from **galactosylceramide (galactocerebroside)** to yield **ceramide +
D-galactose** (EC 3.2.1.46, RHEA:14297), and also hydrolyses **galactosylsphingosine
(psychosine)** and other galactolipids.

- UniProt FUNCTION: "Hydrolyzes the galactose ester bonds of glycolipids such as
  galactosylceramide and galactosylsphingosine" ... "responsible for the lysosomal
  catabolism of galactosylceramide, a major lipid in myelin, kidney and epithelial cells
  of small intestine and colon" [PMID:8281145, PMID:8399327].
- Gene-structure paper: "This enzyme catalyzes the lysosomal hydrolysis of specific
  galactolipids including galactosylceramide (galactocerebroside) and galactosylsphingosine
  (psychosine)" [PMID:7601472].
- Enzyme purified from human urine, EC 3.2.1.46, low abundance, acid pH optimum (4.0-4.4),
  KM=10 uM for N-acyl-beta-D-galactosylsphingosine [PMID:8399327].
- cDNA cloned + expressed in COS-1; N-terminal sequence from 51 kDa human brain band
  [PMID:8281145].

## Cofactor / mechanism

Requires **saposin A (SapA, from PSAP)** for lipid presentation. GALC-SapA crystal
structure (murine) = 2:2 heterotetramer; open channel from GALC active site to SapA
hydrophobic cavity presents the polar glycosyl headgroup to the active site while shielding
the acyl chains. "This enzyme requires the saposin SapA for lipid processing and defects in
either of these proteins causes a severe neurodegenerative disorder, Krabbe disease"
[PMID:29323104]. Active-site residues (UniProt): proton donor/acceptor His... actually
ACT_SITE 198 (proton donor/acceptor), 274 (nucleophile). GH59 retaining glycosidase.

## Localization

Lysosome / lysosomal lumen. GO IC annotations place it in endolysosome lumen (GO:0036021),
inferred from the general finding that endolysosomes are the principal sites of acid
hydrolase activity [PMID:27498570] combined with GALC's acid-hydrolase MF (GO:0004336).
PMID:27498570 is a general endolysosome study and does NOT mention GALC by name; the
endolysosome-lumen call is a curator inference (IC). Lysosome localization is well
established (subcellular location "Lysosome"; typical acid hydrolase, mannose-6-phosphate
pathway implied).

## Disease

Deficiency causes **Krabbe disease / globoid cell leukodystrophy (KRB; MIM:245200)**,
autosomal recessive. Psychosine (galactosylsphingosine) accumulation is neurotoxic and
drives demyelination. Many pathogenic missense variants across the gene (UniProt lists
dozens of KRB variants). Four clinical forms; infantile form ~90% of cases.

## Annotation review decisions

GOA MF term present and current: **GO:0004336 galactosylceramidase activity** (verified via
OLS, not obsolete). This is the core MF used in core_functions.
Core BP: **GO:0006683 galactosylceramide catabolic process** (verified current).
Locations: **GO:0005764 lysosome**, **GO:0043202 lysosomal lumen** (both verified current).

Notes on individual annotations:
- PMID:15657896 is a *review* on GALC in cancer, annotated IDA to GO:0006683. IDA on a
  review is unusual, but it does correctly describe GALC degrading galactosylcerebroside to
  ceramide. Not a core-defining primary experiment; keep as non-core / accept the biology
  but flag the evidence type. Per policy do NOT REMOVE (can't see full curator context) —
  accept the biology, note the review nature.
- GO:0030149 sphingolipid catabolic process (IDA, PMID:8281145): broader parent-type BP;
  GALC does act in sphingolipid catabolism (galactosylceramide is a glycosphingolipid).
  Keep as non-core (galactosylceramide catabolic process is the precise term).
- GO:0046479 glycosphingolipid catabolic process (TAS, Reactome): correct, broader than the
  precise galactosylceramide catabolic process; keep as non-core.
- Reactome/GO_REF/IEA/ISS/IBA MF and BP annotations all consistent; accept.

## Deep research

Falcon deep research is OUT OF CREDITS (HTTP 402) — no -deep-research-falcon.md generated.
Review grounded in GALC-uniprot.txt, GALC-goa.tsv, and cached publications/PMID_*.md.
