# phnW curation notes

## 2026-10-25: PhnWX cross-species module audit

Q88KT0 (PP_2209) is the KT2440 PhnW-family aminotransferase. The cached
UniProt record assigns the reaction and subfamily through curated HAMAP
MF_01376, with concordant InterPro IPR012703 and PANTHER PTHR42778:SF1.
This is family-based inference, not a direct assay of Q88KT0.

The primary biochemical reference is Kim et al., PMID:12107130, which
characterizes **Salmonella enterica serovar Typhimurium** PhnW:
"catalyzes the reversible reaction of AEP and pyruvate to form phosphonoacetaldehyde".
The retrieved PubMed abstract establishes the reaction, substrate specialization,
PLP-dependent family, and homodimeric form. The repository fetcher could only cache the abstract after its PMC fallbacks. No numerical
kinetic constant or Salmonella residue number is transferred to the KT2440 protein.

Ternan and Quinn, PMID:9841125, measured both pathway activities in **P. putida
NG2**, not KT2440: "contained 2-aminoethylphosphonic acid: pyruvate aminotransferase
and phosphonoacetaldehyde hydrolase (phosphonatase) activities". Murphy et al.,
PMID:35229442, studied regulatory control in **BIRD-1**, not KT2440. These studies
support the pathway role and motivate experiments; they do not establish KT2440
uptake, gene induction, or AepR/PhoBR regulation.

Both existing GO rows remain ACCEPT. The description no longer calls the
reversible transaminase reaction intrinsically committing, and now marks cytosolic
localization as expected rather than measured. Removed the GOA reference, EC-label
quote, and AI-report quotations as biological support; evidence now traces to
curated family assignment and primary publications. No new GO assertion was added.

`just fetch-fitness PSEPK phnW` failed because neither a local FEBA database nor
the remote source was reachable; no artifact was written. This is a data-access
limitation, not a negative fitness result.
