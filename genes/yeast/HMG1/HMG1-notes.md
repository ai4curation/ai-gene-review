# HMG1 (YML075C) notes

UniProt P12683; HMG-CoA reductase 1, EC 1.1.1.34; polytopic ER/nuclear-envelope protein with SSD [UniProt:P12683].

## 2026-10-24 PTHR10572 PAINT alignment

- Re-ran `just fetch-gene yeast HMG1`; UniProt P12683, GOA, and the PTHR10572 cache were already current.
- Falcon deep research was attempted, but no external research provider/API key was available after the wrapper extracted the UniProt context.
- Searched for newer HMG1 literature. The 2026 Process Biochemistry ergosterol-production paper uses engineered truncated `tHMG1` to improve ergosterol yield, but it does not change the native Hmg1 GO calls.
- PTHR10572 PAINT alignment: keep `GO:0004420`, `GO:0005789`, `GO:0006696`, and broad `GO:0008299` IBAs as sound; continue removing the stale `GO:0005778` peroxisomal-membrane IBA from eukaryotic node `PANTHER:PTN000060347`.
- Tightened the peroxisomal `propagation_review` to trace the bad IBA to the proximate PAINT node rather than to the single human HMGCR seed, and replaced truncated UniProt `Reaction=` quotes with complete catalytic text.
- Aligned the broad `GO:0008299` process calls after review: the PANTHER/InterPro family-level assertions remain correct broad isoprenoid parent calls, while the YeastPathways `IPPSYN-PWY` RCA should narrow to `GO:0019287`.

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
