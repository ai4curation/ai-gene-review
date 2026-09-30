# PTHR46106: source excerpts

Raw provenance: [family snapshot](family-sources/PTHR46106.json); [UniProt snapshot](uniprot-records.jsonl.gz), supplemented by [successful retries](uniprot-retries.jsonl.gz).

## Integrated InterPro IPR033522

Generated description flag: False; reviewed generated text flag: False. Generated prose is a source lead, not independent biological validation.

This entry includes mammalian receptor-type tyrosine-protein phosphatase-like N and N2, also known as islet antigen 2/2 beta (IA-2 and IA-2 beta). They are dense core vesicle (DCV) transmembrane proteins that play a role in vesicle-mediated secretory processes. They are major autoantigens in type 1 diabetes and are required for the accumulation of normal levels of insulin-containing vesicles and preventing their degradation [[cite:PUB00083237], [cite:PUB00078993]]. This entry also includes Ida-1 from Caenorhabditis elegans [[cite:PUB00094192]].

## Exact benchmark records

### HORSE/PTPRN2 — A0A9L0T4W6
UniProt record: https://www.uniprot.org/uniprotkb/A0A9L0T4W6/entry
Status: UniProtKB unreviewed (TrEMBL); length: 976 aa; sequence version: 1.

**CATALYTIC ACTIVITY**
{"name": "O-phospho-L-tyrosyl-[protein] + H2O = L-tyrosyl-[protein] + phosphate", "reactionCrossReferences": [{"database": "Rhea", "id": "RHEA:10684"}, {"database": "Rhea", "id": "RHEA-COMP:10136"}, {"database": "Rhea", "id": "RHEA-COMP:20101"}, {"database": "ChEBI", "id": "CHEBI:15377"}, {"database": "ChEBI", "id": "CHEBI:43474"}, {"database": "ChEBI", "id": "CHEBI:46858"}, {"database": "ChEBI", "id": "CHEBI:61978"}], "ecNumber": "3.1.3.48", "evidences": [{"evidenceCode": "ECO:0000256", "source": "PROSITE-ProRule", "id": "PRU10044"}]}
**SUBCELLULAR LOCATION**
{"location": {"evidences": [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00004212"}], "value": "Cytoplasmic vesicle, secretory vesicle membrane", "id": "SL-0245"}, "topology": {"evidences": [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00004212"}], "value": "Single-pass type I membrane protein", "id": "SL-9905"}}
{"location": {"evidences": [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00034103"}], "value": "Synapse", "id": "SL-0258"}}
InterPro: IPR033522 [{"key": "EntryName", "value": "IA-2/IA-2_beta"}]
InterPro: IPR029021 [{"key": "EntryName", "value": "Prot-tyrosine_phosphatase-like"}]
InterPro: IPR000242 [{"key": "EntryName", "value": "PTP_cat"}]
InterPro: IPR021613 [{"key": "EntryName", "value": "Receptor_IA-2_dom"}]
InterPro: IPR038112 [{"key": "EntryName", "value": "Receptor_IA-2_ectodomain_sf"}]
InterPro: IPR016130 [{"key": "EntryName", "value": "Tyr_Pase_AS"}]
InterPro: IPR003595 [{"key": "EntryName", "value": "Tyr_Pase_cat"}]
InterPro: IPR000387 [{"key": "EntryName", "value": "Tyr_Pase_dom"}]
PANTHER: PTHR46106 [{"key": "EntryName", "value": "IA-2 PROTEIN TYROSINE PHOSPHATASE, ISOFORM C"}, {"key": "MatchStatus", "value": "1"}]
PANTHER: PTHR46106:SF5 [{"key": "EntryName", "value": "RECEPTOR-TYPE TYROSINE-PROTEIN PHOSPHATASE N2"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF11548 [{"key": "EntryName", "value": "Receptor_IA-2"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF00102 [{"key": "EntryName", "value": "Y_phosphatase"}, {"key": "MatchStatus", "value": "1"}]

### human/PTPRN2 — Q92932
UniProt record: https://www.uniprot.org/uniprotkb/Q92932/entry
Status: UniProtKB reviewed (Swiss-Prot); length: 1015 aa; sequence version: 2.

**FUNCTION**
Plays a role in vesicle-mediated secretory processes. Required for normal accumulation of secretory vesicles in hippocampus, pituitary and pancreatic islets. Required for the accumulation of normal levels of insulin-containing vesicles and preventing their degradation. Plays a role in insulin secretion in response to glucose stimuli. Required for normal accumulation of the neurotransmitters norepinephrine, dopamine and serotonin in the brain. In females, but not in males, required for normal accumulation and secretion of pituitary hormones, such as luteinizing hormone (LH) and follicle-stimulating hormone (FSH) (By similarity). Required to maintain normal levels of renin expression and renin release (By similarity). May regulate catalytic active protein-tyrosine phosphatases such as PTPRA through dimerization (By similarity). Has phosphatidylinositol phosphatase activity; the PIPase activity is involved in its ability to regulate insulin secretion. Can dephosphorylate phosphatidylinositol 4,5-biphosphate (PI(4,5)P2), phosphatidylinositol 5-phosphate and phosphatidylinositol 3-phosphate (By similarity). Regulates PI(4,5)P2 level in the plasma membrane and localization of cofilin at the plasma membrane and thus is indirectly involved in regulation of actin dynamics related to cell migration and metastasis; upon hydrolysis of PI(4,5)P2 cofilin is released from the plasma membrane and acts in the cytoplasm in severing F-actin filaments (PubMed:26620550)
Evidence: [{"evidenceCode": "ECO:0000250", "source": "UniProtKB", "id": "P80560"}, {"evidenceCode": "ECO:0000250", "source": "UniProtKB", "id": "Q63475"}, {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "26620550"}]
**CATALYTIC ACTIVITY**
{"name": "O-phospho-L-tyrosyl-[protein] + H2O = L-tyrosyl-[protein] + phosphate", "reactionCrossReferences": [{"database": "Rhea", "id": "RHEA:10684"}, {"database": "Rhea", "id": "RHEA-COMP:10136"}, {"database": "Rhea", "id": "RHEA-COMP:20101"}, {"database": "ChEBI", "id": "CHEBI:15377"}, {"database": "ChEBI", "id": "CHEBI:43474"}, {"database": "ChEBI", "id": "CHEBI:46858"}, {"database": "ChEBI", "id": "CHEBI:61978"}], "ecNumber": "3.1.3.48", "evidences": [{"evidenceCode": "ECO:0000255", "source": "PROSITE-ProRule", "id": "PRU10044"}, {"evidenceCode": "ECO:0000305", "source": "PubMed", "id": "8798755"}]}
**SUBCELLULAR LOCATION**
{"location": {"evidences": [{"evidenceCode": "ECO:0000250", "source": "UniProtKB", "id": "P80560"}], "value": "Cytoplasmic vesicle, secretory vesicle membrane", "id": "SL-0245"}, "topology": {"evidences": [{"evidenceCode": "ECO:0000250", "source": "UniProtKB", "id": "P80560"}], "value": "Single-pass type I membrane protein", "id": "SL-9905"}}
{"location": {"evidences": [{"evidenceCode": "ECO:0000250", "source": "UniProtKB", "id": "P80560"}], "value": "Cytoplasmic vesicle, secretory vesicle, synaptic vesicle membrane", "id": "SL-0260"}, "topology": {"evidences": [{"evidenceCode": "ECO:0000250", "source": "UniProtKB", "id": "P80560"}], "value": "Single-pass type I membrane protein", "id": "SL-9905"}}
**SUBCELLULAR LOCATION**
{"location": {"evidences": [{"evidenceCode": "ECO:0000305"}], "value": "Cytoplasmic vesicle, secretory vesicle membrane", "id": "SL-0245"}}
**SIMILARITY**
Belongs to the protein-tyrosine phosphatase family. Receptor class 8 subfamily
Evidence: [{"evidenceCode": "ECO:0000305"}]
**CAUTION**
Has no tyrosine-protein phosphatase activity at mild acidic conditions (pH 5.5). The in vivo relevance of the low PPase activity at acidic conditions (pH 4.5) is questioned. This catalytic activity seems to be affected by the replacement of a highly conserved residue in the tyrosine-protein phosphatase domain
Evidence: [{"evidenceCode": "ECO:0000305"}, {"evidenceCode": "ECO:0000305", "source": "PubMed", "id": "8798755"}]
InterPro: IPR033522 [{"key": "EntryName", "value": "IA-2/IA-2_beta"}]
InterPro: IPR029021 [{"key": "EntryName", "value": "Prot-tyrosine_phosphatase-like"}]
InterPro: IPR000242 [{"key": "EntryName", "value": "PTP_cat"}]
InterPro: IPR021613 [{"key": "EntryName", "value": "Receptor_IA-2_dom"}]
InterPro: IPR038112 [{"key": "EntryName", "value": "Receptor_IA-2_ectodomain_sf"}]
InterPro: IPR029403 [{"key": "EntryName", "value": "RESP18_dom"}]
InterPro: IPR016130 [{"key": "EntryName", "value": "Tyr_Pase_AS"}]
InterPro: IPR003595 [{"key": "EntryName", "value": "Tyr_Pase_cat"}]
InterPro: IPR000387 [{"key": "EntryName", "value": "Tyr_Pase_dom"}]
PANTHER: PTHR46106 [{"key": "EntryName", "value": "IA-2 PROTEIN TYROSINE PHOSPHATASE, ISOFORM C"}, {"key": "MatchStatus", "value": "1"}]
PANTHER: PTHR46106:SF5 [{"key": "EntryName", "value": "RECEPTOR-TYPE TYROSINE-PROTEIN PHOSPHATASE N2"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF11548 [{"key": "EntryName", "value": "Receptor_IA-2"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF14948 [{"key": "EntryName", "value": "RESP18"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF00102 [{"key": "EntryName", "value": "Y_phosphatase"}, {"key": "MatchStatus", "value": "1"}]

