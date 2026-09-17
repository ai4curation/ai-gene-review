# PTHR46622: source excerpts

Raw provenance: [family snapshot](family-sources/PTHR46622.json); [UniProt snapshot](uniprot-records.jsonl.gz), supplemented by [successful retries](uniprot-retries.jsonl.gz).

## Integrated InterPro IPR053000

Generated description flag: True; reviewed generated text flag: False. Generated prose is a source lead, not independent biological validation.

This family of proteins includes metalloendopeptidases that selectively target DNA-binding proteins in the presence of DNA, which facilitates the interaction between the protease and its substrates. These enzymes play a critical role in the repair of toxic DNA-protein cross-links (DPCs), such as those formed by trapped topoisomerase 1 on DNA lesions or induced by reactive compounds like formaldehyde. They are involved in the DNA damage response and the processing of stalled or collapsed replication forks by excising covalently trapped topoisomerase 1 from chromatin. The proteolysis of DPCs allows for subsequent repair through downstream DNA repair pathways. Recruitment to DPCs may occur via the SUMOylation of substrate proteins at sites of DNA damage.

## Exact benchmark records

### SCHPO/wss1 — Q9P7B5
UniProt record: https://www.uniprot.org/uniprotkb/Q9P7B5/entry
Status: UniProtKB reviewed (Swiss-Prot); length: 262 aa; sequence version: 2.

**FUNCTION**
Metalloendopeptidase that acts selectively on DNA-binding proteins. DNA is needed to bring the protease and substrates together to enable proteolysis. Involved in the repair of toxic DNA-protein cross-links (DPCs) such as covalently trapped topoisomerase 1 (top1) adducts on DNA lesions or DPCs induced by reactive compounds such as formaldehyde. Involved in DNA damage response and processing of stalled or collapsed replication forks by removing the covalently trapped top1 from chromatin. DPC proteolysis enables the repair of the lesions via downstream DNA repair pathways. May be recruited to DPCs via the SUMOylation of substrate proteins at damaged DNA sites (By similarity)
Evidence: [{"evidenceCode": "ECO:0000250", "source": "UniProtKB", "id": "P38838"}]
**SUBCELLULAR LOCATION**
{"location": {"evidences": [{"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "16823372"}], "value": "Nucleus", "id": "SL-0191"}}
**SIMILARITY**
Belongs to the peptidase M3 family. WSS1-like metalloprotease (WLM) subfamily
Evidence: [{"evidenceCode": "ECO:0000305"}]
InterPro: IPR013536 [{"key": "EntryName", "value": "WLM_dom"}]
InterPro: IPR053000 [{"key": "EntryName", "value": "WSS1-like_metalloprotease"}]
PANTHER: PTHR46622 [{"key": "EntryName", "value": "DNA-DEPENDENT METALLOPROTEASE WSS1"}, {"key": "MatchStatus", "value": "1"}]
PANTHER: PTHR46622:SF1 [{"key": "EntryName", "value": "DNA-DEPENDENT METALLOPROTEASE WSS1"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF08325 [{"key": "EntryName", "value": "WLM"}, {"key": "MatchStatus", "value": "1"}]

