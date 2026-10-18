# RASGEF1A (donkey, A0A9L0J8J4) notes

DONKEY40 cohort review (ProtNLM2 evaluation). Unreviewed TrEMBL entry from the Ensembl donkey annotation, 516 aa; the donkey record carries no curated CC comments.

## Identity and sequence
- Domains: N-terminal Ras-GEF (REM) 76-205 and catalytic Ras-GEF 249-496 [file:EQUAS/RASGEF1A/RASGEF1A-uniprot.txt "FT   DOMAIN          249..496"]; PANTHER PTHR23113:SF172 (RAS-GEF DOMAIN-CONTAINING FAMILY MEMBER 1A).
- 96.25% identity to human Q8N9B8 across 480 paired residues; donkey has a 36-residue N-terminal extension; both GEF domains complete [file:EQUAS/RASGEF1A/RASGEF1A-bioinformatics/RESULTS.md "The donkey sequence A0A9L0J8J4 (516 residues) aligns to human Q8N9B8 (481 residues) with 96.25% identity across 480 paired residues"].

## Function (human ortholog)
- Human Swiss-Prot: GEF for Rap2A and Ras proteins in vitro, and a role in cell migration [file:EQUAS/RASGEF1A/RASGEF1A-bioinformatics/RASGEF1A-human-Q8N9B8-uniprot.txt "Guanine nucleotide exchange factor (GEF) with specificity for"; "Plays a role in cell migration."]. The underlying papers (PMID:17121879, cholangiocarcinoma growth/migration; PMID:19645719, Rap2-specific exchange) are not cached locally, so the evidence is taken from the Swiss-Prot summary and the human GO lines (GEF activity IDA, cell migration IDA, positive regulation of Ras signal transduction IDA, plasma membrane and Ras signal transduction IBA).
- No experimental subcellular localization in the human record apart from Reactome cytosol (TAS).

## Annotation decisions
- GEF activity: ACCEPT (core).
- Ras protein signal transduction (TreeGrafter) and small GTPase-mediated signal transduction (InterPro): ACCEPT; the broader term also covers the preferred Rap2 substrate.
- plasma membrane (TreeGrafter): KEEP_AS_NON_CORE (PAINT inference only; no experimental localization).
- cell migration and positive regulation of Ras protein signal transduction (Ensembl orthology from human IDA): KEEP_AS_NON_CORE.

## ProtNLM2
- GO:0007264 small GTPase-mediated signal transduction: exact term in donkey GOA -> CNN.
- Non-GO output (not scored): subcellular location "Nucleus" (no supporting evidence in the human record; human has cytosol by Reactome TAS and plasma membrane by IBA).
