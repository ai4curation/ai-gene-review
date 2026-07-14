# PEMT (human) — gene review notes

UniProt: Q9UBM1 (PEMT_HUMAN). HGNC:8830. Gene ID 10400. Chromosome 17p11.2.
199 aa (isoform 1, displayed). EC 2.1.1.17 and EC 2.1.1.71.

## Core biology (grounded in local UniProt file)

PEMT is **phosphatidylethanolamine N-methyltransferase**, an integral ER-membrane enzyme that
provides the **liver-enriched alternative route to phosphatidylcholine (PC)**. It catalyzes
**three sequential SAM-dependent methylations of phosphatidylethanolamine (PE)** — PE → PMME
(monomethyl) → PDME (dimethyl) → PC — releasing S-adenosyl-L-homocysteine at each step.

- FUNCTION: "Catalyzes the three sequential steps of the methylation pathway for the biosynthesis of phosphatidylcholine, a critical and essential component for membrane structure" [file:human/PEMT/PEMT-uniprot.txt] (ECO:0000269|PubMed:12431977, PubMed:15927961).
- "Uses S-adenosylmethionine ... as the methyl group donor for the methylation of phosphatidylethanolamine ... to phosphatidylmonomethylethanolamine ..., PMME to phosphatidyldimethylethanolamine ..., and PDME to phosphatidylcholine ..., producing S-adenosyl-L-homocysteine in each step" [file:human/PEMT/PEMT-uniprot.txt].
- "Responsible for approximately 30% of hepatic PC with the CDP-choline pathway accounting for the other 70%" [file:human/PEMT/PEMT-uniprot.txt]. (The CDP-choline/Kennedy pathway is GO:0006657, a distinct route NOT used by PEMT.)
- ACTIVITY REGULATION: "The first methylation is rate-limiting." [file:human/PEMT/PEMT-uniprot.txt]
- PATHWAY: "Phospholipid metabolism; phosphatidylcholine biosynthesis." (ECO:0000305|PubMed:12431977) [file:human/PEMT/PEMT-uniprot.txt]. UniPathway UPA00753.

### Localization / topology
- SUBCELLULAR LOCATION: "Endoplasmic reticulum" (ECO:0000269|PubMed:15927961). Note: "localized in the endoplasmic reticulum (ER) of the liver and in a lipid metabolism-rich region of the ER known as mitochondria-associated membranes" [file:human/PEMT/PEMT-uniprot.txt].
- Isoform 1: "Endoplasmic reticulum membrane ...; Multi-pass membrane protein ...; Mitochondrion membrane ...; Multi-pass membrane protein" and "Found in endoplasmic reticulum where most PEMT activity is generated and in mitochondria." [file:human/PEMT/PEMT-uniprot.txt].
- Topology (PubMed:12431977): 4 TM/intramembrane helices, both termini cytosolic; SAM-binding residues 98–100 and 180–181 (MUTAGEN G98E/G100D/E180D/E181D impair/abolish SAM binding, PubMed:12842883).

### Tissue / clinical
- TISSUE SPECIFICITY: "Primarily expressed in liver (at protein level)." (ECO:0000269|PubMed:12431977) [file:human/PEMT/PEMT-uniprot.txt]. HPA: tissue-enhanced in epididymis and liver.
- PEMT variants (e.g. rs7946 V175M) associate with non-alcoholic fatty liver disease (NAFLD) and susceptibility to choline deficiency (background; not needed for annotation actions).

### Family
- SIMILARITY: "Belongs to the class VI-like SAM-binding methyltransferase superfamily. PEMT/PEM2 methyltransferase family." [file:human/PEMT/PEMT-uniprot.txt]. Pfam PF04191 (PEMT); InterPro IPR024960, IPR007318; HAMAP MF_03216.

## GO term id verification (OLS, claude_ai_OLS MCP, 2026)
- GO:0004608 phosphatidylethanolamine N-methyltransferase activity — "S-adenosyl-L-methionine + phosphatidylethanolamine = S-adenosyl-L-homocysteine + H+ + phosphatidyl-N-methylethanolamine" (first methylation; parent of whole activity). CORE MF.
- GO:0000773 phosphatidyl-N-methylethanolamine N-methyltransferase activity — 2nd/3rd methylation ("Also catalyzes the transfer of a further methylgroup, producing phosphatidylcholine"). PEMT performs this too.
- GO:0006656 phosphatidylcholine biosynthetic process — CORE BP.
- GO:0006657 = CDP-choline pathway (Kennedy) — DISTINCT route, NOT PEMT; must not be used for PEMT.
- GO:0008757 S-adenosylmethionine-dependent methyltransferase activity — generic parent MF (IEA/InterPro).
- GO:0032259 methylation — generic parent BP (KW only; not in GOA seed).
- GO:0005783 endoplasmic reticulum; GO:0005789 endoplasmic reticulum membrane; GO:0031966 mitochondrial membrane.
- GO:0120162 positive regulation of cold-induced thermogenesis — indirect/physiological, transferred from mouse Pemt.

## Reference assessments
- PMID:9989271 (Walkey 1999) — cloned three human PEMT2 cDNAs, mapped gene to 17p11.2, showed 27–115-fold PEMT activity elevation on expression. TAS support for MF GO:0004608 is reasonable (abstract confirms it is human PEMT that converts PE→PC). Abstract-only cache.
- PMID:26113536 (Gao 2015) — mouse Pemt-/- HF-fed cold-exposure/hypothermia study; basis for the ISS→human GO:0120162 thermogenesis annotation. Whole-body metabolic phenotype (hypoglycemia-linked), indirect w.r.t. PEMT molecular function. Abstract-only cache.
- Reactome R-HSA-1483174 "PE is methylated to PC by PEMT" and R-HSA-1483191 "Synthesis of PC" — TAS support for the ER-membrane PE→PC methylation reaction and PC synthesis; consistent with core function.

## Annotation-action reasoning (summary)
- Core MF: GO:0004608 (accept experimental TAS PMID:9989271 as core; IEA duplicate MARK_AS_OVER_ANNOTATED as redundant/uninformative-parent-level but experimental one carries it). GO:0000773 (2nd/3rd methyl) is a genuine sub-activity → KEEP_AS_NON_CORE.
- GO:0008757 SAM-dependent MT activity = generic parent of GO:0004608 → MARK_AS_OVER_ANNOTATED (IEA, less informative).
- Core BP: GO:0006656 phosphatidylcholine biosynthetic process (IBA experimental-tree ACCEPT; TAS/IEA duplicates KEEP or MARK_AS_OVER_ANNOTATED).
- Location: ER (GO:0005783) IDA from HPA is the strongest → ACCEPT; ER membrane (GO:0005789) is the more precise compartment → ACCEPT (TAS). Mitochondrial membrane (GO:0031966) IEA-SubCell: PEMT is enriched at MAMs and UniProt notes mitochondrion membrane for isoform 1 → KEEP_AS_NON_CORE (minor pool). IBA ER is_active_in → ACCEPT.
- GO:0120162 positive regulation of cold-induced thermogenesis (ISS from mouse, IEA duplicate): indirect physiological consequence of PC/choline metabolism in Pemt-/- mice, not a direct PEMT molecular role → KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED (do not REMOVE the ISS; use MARK_AS_OVER_ANNOTATED for the redundant IEA).
