# ade6 (SPCC1322.13, UniProt P15567) notes

Fetch: correct accession fetched (PUR6_SCHPO, P15567, 552 aa). Naming trap: S. pombe ade6 = AIR carboxylase = ortholog of S. cerevisiae ADE2 (genes/yeast/ADE2), not of S. cerevisiae ADE6 (FGAM synthase, which is S. pombe ade3).

## Evidence
- Domains: [UniProt:P15567 "IPR005875; PurK."], [UniProt:P15567 "IPR033747; PurE_ClassI."].
- Fungal ADE2 mechanism (C. neoformans): [PMID:9500840 "The N-terminal domain is related to E. coli PurK and a series of kinetic experiments show that the ADE2-PurK activity uses AIR, ATP, and HCO3- as substrates."]; [PMID:9500840 "thus confirming that the C-terminal domain contains a catalytic activity similar to that of the E. coli PurE"].
- Cytosol (ORFeome, PMID:16823372).

## Decisions
- GO:0004638 (class II direct carboxylase definition) MODIFIED to GO:0034028 + GO:0034023, as in genes/yeast/ADE2 and the module (which splits the step into two half-reactions).
- Nucleobase BP rows MODIFIED to GO:0006189.
- PomBase GO-CAM 663d668500001911 types ade6 as GO:0004638 - disagrees at term level with this review and the module.
