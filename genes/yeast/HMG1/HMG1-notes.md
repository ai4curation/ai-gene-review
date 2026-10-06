# HMG1 (YML075C) notes

UniProt P12683; HMG-CoA reductase 1, EC 1.1.1.34; polytopic ER/nuclear-envelope protein with SSD [UniProt:P12683].

## Evidence journal
- [PMID:3526336 "Assays of HMG-CoA reductase activity in extracts from hmg1- and hmg2- mutants indicate that HMG1 contributes at least 83% of the activity found in wild-type cells."]; double mutant lethal [PMID:3526336].
- Redundancy [PMID:2828155 "Although cells bearing null mutations in both genes are inviable, cells bearing a null mutation in either gene are viable."]
- Localisation [PMID:8744950 "At endogenous expression levels, Hmg1p and Hmg2p were both primarily localized in the nuclear envelope."]; overexpression induces ER proliferations.
- Catalytic-domain overexpression raises squalene [PMID:9292983 "This overproduction leads to an enhancement of squalene production, implying that HMG-R has been deregulated."]
- Hmg1-Hmg2 heteromer in 4 interactome datasets (PMID:16429126, 18467557, 31454312, 37968396).

## Decisions
- protein binding IPI x4 REMOVE (uninformative; interaction not disputed).
- Peroxisomal membrane IBA (human HMGCR only) REMOVE. Cytosol RCA x3 MODIFY -> ER membrane.
- CoA metabolic process IEA MARK_AS_OVER_ANNOTATED; oxidoreductase IEA MODIFY -> GO:0004420. Rest ACCEPT.
