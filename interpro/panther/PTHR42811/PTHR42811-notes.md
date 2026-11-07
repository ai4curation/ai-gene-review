# PTHR42811 serine acetyltransferase: curation notes

## 2026-11-03 PAINT seed localisation check

The PTHR42811 PAINT slice (`PTHR42811-paint.tsv`) places cytosol at
PTN000602332, withdraws it for an angiosperm clade (IRD at PTN000602385,
taxon 3398), and adds chloroplast (PTN005130398, seed AT1G55920) and
mitochondrion (PTN005130403, seed AT3G13110) for two Brassicaceae nodes. To
check the seeds, the reviewed UniProt entries for the Arabidopsis seed loci
were retrieved on 2026-11-03 with

```
curl -s "https://rest.uniprot.org/uniprotkb/search?query=gene:<AGI>+AND+reviewed:true&fields=accession,gene_names,cc_subcellular_location,protein_name&format=tsv"
```

Results (accession, AGI, subcellular location as returned):

- Q42588 At1g55920 SAT1: SUBCELLULAR LOCATION: Plastid, chloroplast {ECO:0000269|PubMed:9830017}. Cytoplasm {ECO:0000269|PubMed:9830017}. Note=First chloroplastic and progressively cytoplasmic during aging.
- Q39218 At3g13110 SAT3: SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:9830017}.
- Q42538 At5g56760 SAT5: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9830017}.
- Q8S895 At2g17640 SAT2: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:15579666}.
- Q8W2B8 At4g35640 SAT4: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:15579666}.

So the cytosol seeds (AT2G17640, AT4G35640, AT5G56760) are experimentally
cytoplasmic SATs, and the chloroplast and mitochondrion seeds are the
experimentally organellar SAT1 and SAT3. This is consistent with the PANTHER
subfamily names: Q42588 is in PTHR42811:SF11 (SERINE ACETYLTRANSFERASE 1,
CHLOROPLASTIC) and Q39218 in PTHR42811:SF10 (SERINE ACETYLTRANSFERASE 3,
MITOCHONDRIAL), whereas the cytosolic SAT5 sits with the bacterial CysE
proteins in SF5.

## Subfamily membership (PANTHER 19.0 organism classifications)

From the `.cache/panther/PTHR19.0_*` classification files: PTHR42811:SF5
(SERINE ACETYLTRANSFERASE-RELATED) holds E. coli CysE P0A9D4, Salmonella CysE
P29847, B. subtilis CysE Q06750, M. tuberculosis CysE P95231, P. aeruginosa
CysE Q9HXI6 and its paralog PA2105 (Q9I210), S. pombe SPAC1039.08 (Q9US33)
and Arabidopsis SAT5 Q42538. P. putida KT2440 CysE Q88PL0 is classified only
to the family level in the member index. E. coli WcaB (P0ACC9) appears in the
InterPro-derived `PTHR42811-entries.csv` but not in the PANTHER E. coli
classification file under PTHR42811.

Deep research for this family was not run (no provider API keys in this
session).
