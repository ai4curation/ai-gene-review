# FOXO1 notes

## 2026-10-25 ORGANELLES batch 3 (mitochondrion rows)

Row: GO:0005739 mitochondrion, ISS, PMID:22510882, WITH/FROM UniProtKB:P0DJI6 (UniProt, 2013). No sub-compartment rows; qualifier located_in.

Checks:
- P0DJI6 is mouse FCoR (Foxo1-corepressor, 106 aa; UniProt REST, fetched 2026-10-25), not a FOXO homologue. Its curated location is "Cytoplasm, cytosol {ECO:0000269|PubMed:22510882}. Nucleus {ECO:0000269|PubMed:22510882}". QuickGO shows FCoR carries an IDA mitochondrion row from PMID:22510882, so the ISS on FOXO1 looks like a partner's location transferred as if by similarity.
- PMID:22510882 (full text cached) places FCoR in cytosol and nucleus: "In these cells, FCoR localized to both the cytosol and nucleus" [PMID:22510882]. Its "mitochondrial" mentions concern mitochondrial biogenesis gene expression in BAT, not Foxo1 location.
- Human UniProt CC location for FOXO1 is cytoplasm and nucleus only [file:human/FOXO1/FOXO1-uniprot.txt]; no TRANSIT/TRANSMEM.
- Independent report: Lettieri-Barbato et al. 2019 [PMID:30974111, abstract only] "We demonstrated that FoxO1 not exclusively localizes to cytosol and nucleus of adipocytes but also to mitochondria where it binds to mitochondrial DNA." and "Mitochondrial FoxO1 responds to starvation leaving mitochondrial compartment by ROS-mediated activation of the mitochondrial phosphatase PTPMT1." One group, mouse adipocytes; abstract does not say whether fractions were checked for ER.

Outcome: UNDECIDED -> KEEP_AS_NON_CORE (claim supported independently, peripheral). Source defect recorded (WRONG_WITH_FROM, UNIPROT, CHECK, PROBABLE). Stays at root: mtDNA binding is a single line toward matrix/nucleoid. Added PMID:30974111 to references.
