# SEC23A (donkey, Equus asinus) - A0A9L0IQB9

DONKEY40 cohort review. Unreviewed TrEMBL entry, 739 aa, "Protein transport protein SEC23"; PANTHER PTHR11141:SF7 (SEC23A).

## Sources
- Donkey UniProt `SEC23A-uniprot.txt` (RuleBase RU365030 function; SEC23/SEC24 family, SEC23 subfamily).
- Donkey GOA `SEC23A-goa.tsv`: 11 IEA rows (3 TreeGrafter GO_REF:0000118, 4 SubCell GO_REF:0000044, 4 InterPro2GO GO_REF:0000002 incl. combined GO_REF:0000120 for COPII vesicle coat).
- Human ortholog Q15436 UniProt record fetched to `SEC23A-bioinformatics/human-Q15436-uniprot.txt`. No human/mouse SEC23A review in repo.
- PMID:21235735 (cached full text, human SAR1B/Anderson's disease paper) used for the COPII mechanism background including Sec23 GAP activity.

## Sequence
- 99.32% identity to human SEC23A over 739 aligned residues; lacks a 26-residue segment corresponding to human 554-579; Zn-finger Cys61/66/85/88 conserved [file:EQUAS/SEC23A/SEC23A-bioinformatics/RESULTS.md].

## Biology
- COPII inner-coat component: deforms ER membrane into vesicles and selects cargo [human UniProt "Component of the coat protein complex II (COPII)"].
- Sar1 GAP: "The outer coat stimulates the GTPase-activating protein Sec23 which activates Sar1 GTP hydrolysis" [PMID:21235735].
- Location: COPII vesicle membrane, ER membrane, cytosol, enriched at ER exit sites [human UniProt, PMID:8898360 via UniProt evidence].
- Sec23/24 recruits SEC22B cargo into COPII vesicles [human UniProt SUBUNIT].

## Decisions
All 11 rows accepted or kept: GAP activity, COPII coat, ER-to-Golgi transport, budding, cargo loading, locations ACCEPT; zinc ion binding and intracellular protein transport KEEP_AS_NON_CORE (structural Zn site; broad process).
