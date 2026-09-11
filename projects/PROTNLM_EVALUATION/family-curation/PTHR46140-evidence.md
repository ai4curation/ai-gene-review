# PTHR46140: source excerpts

Raw provenance: [family snapshot](family-sources/PTHR46140.json); [UniProt snapshot](uniprot-records.jsonl.gz), supplemented by [successful retries](uniprot-retries.jsonl.gz).

## Integrated InterPro IPR051572

Generated description flag: True; reviewed generated text flag: False. Generated prose is a source lead, not independent biological validation.

This family of proteins functions as subunits of the vacuolar transporter chaperone (VTC) complex, which is involved in the synthesis and translocation of inorganic polyphosphate (polyP). The complex catalyzes the transfer of phosphate from ATP to a growing polyP chain, releasing ADP, and integrates cytoplasmic polymer synthesis with polyP membrane translocation. The complex contains multiple vacuolar transmembrane domains that likely form a channel for polyP transport into the vacuole lumen. This process is dependent on the proton gradient across the membrane. Additionally, these proteins play a role in vacuolar membrane fusion and are involved in various cellular processes such as microautophagy, SNARE priming, and the regulation of cytosolic phosphate concentrations through binding to inositol polyphosphates. The SPX domain present in some subunits has a high affinity for inositol polyphosphates and may integrate signaling to adapt phosphate concentrations.

## Exact benchmark records

### NEUCR/vtc-4 — Q7SCX0
UniProt record: https://www.uniprot.org/uniprotkb/Q7SCX0/entry
Status: UniProtKB unreviewed (TrEMBL); length: 771 aa; sequence version: 3.

**CATALYTIC ACTIVITY**
{"name": "[phosphate](n) + ATP = [phosphate](n+1) + ADP", "reactionCrossReferences": [{"database": "Rhea", "id": "RHEA:19573"}, {"database": "Rhea", "id": "RHEA-COMP:9859"}, {"database": "Rhea", "id": "RHEA-COMP:14280"}, {"database": "ChEBI", "id": "CHEBI:16838"}, {"database": "ChEBI", "id": "CHEBI:30616"}, {"database": "ChEBI", "id": "CHEBI:456216"}], "ecNumber": "2.7.4.1", "evidences": [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00050204"}]}
**SUBCELLULAR LOCATION**
{"location": {"evidences": [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00004128"}], "value": "Vacuole membrane", "id": "SL-0271"}, "topology": {"evidences": [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00004128"}], "value": "Multi-pass membrane protein", "id": "SL-9909"}}
**SIMILARITY**
Belongs to the VTC4 family
Evidence: [{"evidenceCode": "ECO:0000256", "source": "ARBA", "id": "ARBA00061390"}]
InterPro: IPR003807 [{"key": "EntryName", "value": "DUF202"}]
InterPro: IPR004331 [{"key": "EntryName", "value": "SPX_dom"}]
InterPro: IPR051572 [{"key": "EntryName", "value": "VTC_Complex_Subunit"}]
InterPro: IPR018966 [{"key": "EntryName", "value": "VTC_domain"}]
InterPro: IPR042267 [{"key": "EntryName", "value": "VTC_sf"}]
PANTHER: PTHR46140 [{"key": "EntryName", "value": "VACUOLAR TRANSPORTER CHAPERONE 1-RELATED"}, {"key": "MatchStatus", "value": "1"}]
PANTHER: PTHR46140:SF1 [{"key": "EntryName", "value": "VACUOLAR TRANSPORTER CHAPERONE COMPLEX SUBUNIT 4-RELATED"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF02656 [{"key": "EntryName", "value": "DUF202"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF09359 [{"key": "EntryName", "value": "VTC"}, {"key": "MatchStatus", "value": "1"}]

