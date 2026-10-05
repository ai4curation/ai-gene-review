# PTHR10139: source excerpts

Raw provenance: [family snapshot](family-sources/PTHR10139.json); [UniProt snapshot](uniprot-records.jsonl.gz), supplemented by [successful retries](uniprot-retries.jsonl.gz).

## Integrated InterPro IPR003701

Generated description flag: False; reviewed generated text flag: False. Generated prose is a source lead, not independent biological validation.

Mre11 and Rad50 are two proteins required for DNA repair and meiosis-specific double-strand break formation in Saccharomyces cerevisiae. Mre11 by itself has 3' to 5' exonuclease activity that is increased when Mre11 is in a complex with Rad50 [[cite:PUB00008183]].

## Exact benchmark records

### SCHPO/mre11 — Q09683
UniProt record: https://www.uniprot.org/uniprotkb/Q09683/entry
Status: UniProtKB reviewed (Swiss-Prot); length: 649 aa; sequence version: 1.

**FUNCTION**
Core component of the MRN complex, which plays a central role in double-strand break (DSB) repair, DNA recombination, maintenance of telomere integrity and meiosis (PubMed:15654094, PubMed:22705791, PubMed:23080121, PubMed:7885834). The MRN complex is involved in the repair of DNA double-strand breaks (DSBs) via homologous recombination (HR), an error-free mechanism which primarily occurs during S and G2 phases (By similarity). The complex (1) mediates the end resection of damaged DNA, which generates proper single-stranded DNA, a key initial steps in HR, and is (2) required for the recruitment of other repair factors and efficient activation of ATM and ATR upon DNA damage (By similarity). Within the MRN complex, rad32 possesses both single-strand endonuclease activity and double-strand-specific 3'-5' exonuclease activity (Probable) (PubMed:22705791). Rad32 first endonucleolytically cleaves the 5' strand at DNA DSB ends to prevent non-homologous end joining (NHEJ) and licence HR (By similarity). It then generates a single-stranded DNA gap via 3' to 5' exonucleolytic degradation, which is required for single-strand invasion and recombination (By similarity)
Evidence: [{"evidenceCode": "ECO:0000250", "source": "UniProtKB", "id": "P49959"}, {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "15654094"}, {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "22705791"}, {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "23080121"}, {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "7885834"}, {"evidenceCode": "ECO:0000305", "source": "PubMed", "id": "22705791"}]
**SUBCELLULAR LOCATION**
{"location": {"evidences": [{"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "12944482"}], "value": "Nucleus", "id": "SL-0191"}}
{"location": {"evidences": [{"evidenceCode": "ECO:0000250", "source": "UniProtKB", "id": "P49959"}], "value": "Chromosome, telomere", "id": "SL-0276"}}
{"location": {"evidences": [{"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "23080121"}], "value": "Chromosome", "id": "SL-0468"}}
**SIMILARITY**
Belongs to the MRE11/RAD32 family
Evidence: [{"evidenceCode": "ECO:0000305"}]
InterPro: IPR004843 [{"key": "EntryName", "value": "Calcineurin-like_PHP"}]
InterPro: IPR029052 [{"key": "EntryName", "value": "Metallo-depent_PP-like"}]
InterPro: IPR003701 [{"key": "EntryName", "value": "Mre11"}]
InterPro: IPR038487 [{"key": "EntryName", "value": "Mre11_capping_dom"}]
InterPro: IPR007281 [{"key": "EntryName", "value": "Mre11_DNA-bd"}]
InterPro: IPR041796 [{"key": "EntryName", "value": "Mre11_N"}]
PANTHER: PTHR10139 [{"key": "EntryName", "value": "DOUBLE-STRAND BREAK REPAIR PROTEIN MRE11"}, {"key": "MatchStatus", "value": "1"}]
PANTHER: PTHR10139:SF1 [{"key": "EntryName", "value": "DOUBLE-STRAND BREAK REPAIR PROTEIN MRE11"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF00149 [{"key": "EntryName", "value": "Metallophos"}, {"key": "MatchStatus", "value": "1"}]
Pfam: PF04152 [{"key": "EntryName", "value": "Mre11_DNA_bind"}, {"key": "MatchStatus", "value": "1"}]

