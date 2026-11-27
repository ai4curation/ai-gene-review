# CYP79B2 (At4g39950, O81346) curation notes

## Sources
- Falcon deep research (CYP79B2-deep-research-falcon.md), UniProt O81346, cached PMIDs.
- Added and cached: PMID:10922360 (Mikkelsen 2000), PMID:12464638 (Zhao 2002), PMID:15148388 (Glawischnig 2004), PMID:26352477 (Rajniak 2015). All verified via PubMed MCP.
- Abstract-only in cache: 10681464, 16167893, 17573535, 20023151, 20230487, 31511315, 10922360, 12464638, 15148388.

## Core biochemistry
- Trp -> IAOx, EC 1.14.14.156 [PMID:10922360 "Heterologous expression of CYP79B2 in Escherichia coli shows that CYP79B2 catalyzes the conversion of tryptophan to indole-3-acetaldoxime."]; independently [PMID:10681464 "We have identified two Arabidopsis cytochrome P450s (CYP79B2 and CYP79B3) that can convert Trp to indole-3-acetaldoxime (IAOx)"]. Km 21 uM.
- Electron donor is NADPH-P450 reductase (flavoprotein); Rhea uses reduced [NADPH--hemoprotein reductase]. In GO, GO:0090489 is_a GO:0016712 (flavoprotein donor), NOT GO:0016709 (NAD(P)H donor) -> MODIFY the IBA GO:0016709 to GO:0016712 (same as CYP79F1 review).

## Which downstream processes does CYP79B2 actually catalyse a step of?
- Camalexin: yes, first step [PMID:15148388 "camalexin ... is synthesized from tryptophan via indole-3-acetaldoxime (IAOx) in a reaction catalyzed by CYP79B2 and CYP79B3"]; also physically in the ER metabolon with CYP71A13 [PMID:31511315 "We detected increased substrate affinity of CYP79B2 in the presence of CYP71A13, indicating an allosteric interaction."]. ACCEPT GO:0010120.
- Indole glucosinolates: yes, first step [PMID:10922360 "Arabidopsis overexpressing CYP79B2 has increased levels of indole glucosinolates"]; [PMID:15148388 "only CYP79B2 and CYP79B3 contribute significantly to the IAOx pool from which camalexin and indole glucosinolates are synthesized"]. GO:0009759 is NOT in GOA for CYP79B2. Comparator: CYP83B1 (next enzyme) carries GO:0009759 IDA; CYP81F2 IMP. So the term is applied to catalysing enzymes. Proposed via MODIFY of ARBA GO:0044272 sulfur compound biosynthetic process -> GO:0009759 (is_a descendant) rather than NEW.
- IAA: a step in a minor, conditional IAOx->IAN->IAA route [PMID:15772288 "Root-localized IAA synthesis was diminished in a cyp79B2 cyp79B3 double knockout"]; KEEP_AS_NON_CORE.
- L-tryptophan catabolic process: Trp is consumed by the reaction; ACCEPT (not wrong, less informative).
- Defense rows (oomycete, bacterium, callose, ISR, generic defense): all necessity data from cyp79b2 cyp79b3; antimicrobial work done by downstream products (PEN2/CYP81F2 IGS hydrolysis, PAD3 camalexin). KEEP_AS_NON_CORE. Callose: context-dependent; Schlaeppi 2010 found WT-like callose in the double mutant with P. brassicae [PMID:20230487 "wild-type-like pathogen-induced hypersensitive cell death, stress hormone signaling and callose deposition"].
- Notably GOA has no "defense response to fungus" row for CYP79B2 (project question 3); not proposed as NEW (necessity, not participation).

## Location
- ER: CYP79B2-RFP ER-like, colocalizes with CYP71A13-GFP in N. benthamiana (deep research, Mucha 2019 Fig 6G-I). Chloroplast ISM -> REMOVE (AtSubP mis-call on N-terminal anchor). Membrane rows -> MODIFY to GO:0005789 ER membrane.

## Drought / insect
- Drought: single transcript decrease [PMID:23144921 "Transcript levels of the camalexin biosynthetic genes CYP79B2 and PAD3 were down-regulated by drought stress"] -> MARK_AS_OVER_ANNOTATED (as for PAD3 review). Insect: aphid-induced expression -> KEEP_AS_NON_CORE.
