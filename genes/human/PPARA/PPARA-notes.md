# PPARA curation notes

Deep research status: OpenAI deep research was unavailable in this lane, and the only configured fallback was `claude_code`; no generated `PPARA-deep-research-*` file was created. These notes summarize the fetched UniProt record, GOA rows, Reactome entries and PTHR24082 PAINT rows.

## Core biology

PPARA is PPAR-alpha, the lipid-activated NR1 receptor best known for fasting and hepatic lipid catabolism. UniProt describes it as a "Ligand-activated transcription factor. Key regulator of lipid metabolism", states that it "Regulates the peroxisomal beta-oxidation pathway of fatty acids", and records that its "Transactivation activity requires heterodimerization with RXRA" (`file:human/PPARA/PPARA-uniprot.txt`, CC:FUNCTION).

The review therefore accepts the PPARA rows for:

- nuclear receptor activity and RXRA-dependent DNA-binding transcription activation or repression;
- PPRE/RNA polymerase II cis-regulatory DNA binding and nucleus/chromatin localization;
- PPAR signaling and positive regulation of Pol II transcription;
- regulation of fatty-acid transport, fatty-acid beta-oxidation, lipid metabolism, ketone metabolism and linked energy production.

## Boundary decisions

PPARA is pleiotropic because the same direct nuclear-receptor activity is used in hepatocytes, cardiomyocytes, macrophages and circadian contexts. Rows for inflammation, virus defense, hypoxia, insulin or circadian behavior were kept as non-core rather than rejected when their source was orthology or a direct experimental paper. Broad DNA binding, sequence-specific DNA binding, signaling receptor activity and regulation of DNA-templated transcription were marked `TOO_GENERAL` beside the accepted nuclear receptor and Pol II cis-regulatory DNA-binding rows.

Rows on `GO:0003707 nuclear steroid receptor activity` and `GO:0030518 nuclear receptor-mediated steroid hormone signaling pathway` were marked as over-annotations: PPAR-alpha is a nuclear receptor activated by fatty acids, phospholipids and fibrate drugs rather than by steroid hormones.

The broad `GO:0006631 fatty acid metabolic process` transfer was modified to
`GO:0019217 regulation of fatty acid metabolic process`, because PPARA induces
the fatty-acid metabolic program without itself catalyzing fatty-acid
metabolism. The lipoprotein-metabolism transfer was marked over-annotated
instead of accepted for the same effector-process reason.

All generic `GO:0005515` interaction rows were removed without disputing the physical interactions.

## PANTHER and modules

`just paint-losses human PPARA` found no PAINT loss on the human PPARA lineage. The PPARA GO-CAMs in `gocams/index.tsv` cover SIK2/p300 regulation and PAQR3/HUWE1-mediated PPARA turnover; they are specific regulatory branches and did not call for a new module in this family PR.
