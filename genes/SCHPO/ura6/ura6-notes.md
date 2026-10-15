# ura6 (SPCC1795.05c; UniProt O59771) notes

## Identity / naming
- PomBase symbol ura6; UniProt entry has no gene name, only ORF SPCC1795.05c [UniProt:O59771]. `just fetch-gene SCHPO ura6` failed ("Could not find any UniProt ID"); fetched with `-u O59771`.
- Adenylate kinase family, UMP-CMP kinase subfamily [UniProt:O59771 "Belongs to the adenylate kinase family. UMP-CMP kinase"].

## Function (inferred)
- Reaction UMP + ATP = UDP + ADP (HAMAP MF_03172) [UniProt:O59771 "Reaction=UMP + ATP = UDP + ADP; Xref=Rhea:RHEA:24400,"].
- Substrate range by rule: [UniProt:O59771 "dUMP as phosphate acceptors, but can also use CMP, dCMP and AMP."]
- No S. pombe biochemistry found; ortholog S. cerevisiae Ura6 [PMID:8391780 "The enzyme can use UMP and dUMP as phosphate acceptors with high activity"]; [PMID:1655742 "Thus, both molecular genetic and biochemical evidence supports a notion that the URA6 is SOC8 encoding a yeast uridine monophosphate kinase"].

## Location
- ORFeome GFP: cytoplasm + nucleus (PMID:16823372, abstract-only) [UniProt:O59771 "Note=Predominantly cytoplasmic."]. Budding yeast: [PMID:8391780 "the UMP kinase locates primarily in the cytoplasm (approximately 80%) and also in the nucleus (approximately 20%), but not in the mitochondria"].

## GO-CAM
- PomBase model 69a0c46f00003691: ura6 enables GO:0033862, occurs_in cytosol, part_of GO:0006225 (IBA basis). Agrees with this review.

## Decisions
- 'de novo' pyrimidine nucleobase biosynthetic process (IEA, ISO) -> MODIFY to GO:0006225, as for S. cerevisiae URA6.
- Generic kinase/phosphotransferase IEA -> MODIFY to GO:0033862.
- CDP biosynthetic process IBA kept non-core (CMP kinase side activity). CMP kinase activity (GO:0036430) is not annotated in GOA and no S. pombe data support it; not proposed as NEW, although the pyrimidine_salvage module uses ura6 as the CMP kinase representative.
