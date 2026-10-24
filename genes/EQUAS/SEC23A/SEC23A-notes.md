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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this re-review.

### Deep research
- `just deep-research-falcon EQUAS SEC23A --fallback perplexity-lite` failed: falcon "Failed to authenticate" (Edison client), perplexity-lite HTTP 401 insufficient_quota. No deep-research file exists; review is based on the primary literature cached below plus UniProt Q15436.

### Identity of the benchmark accession
- UniProt gene-centric canonical for donkey SEC23A is **A0A9L0JMP6 (765 aa)**; A0A9L0IQB9 (739 aa) is a non-canonical member of the same group (others: A0A8C4LKL1 771, A0A8C4LGG5 751, A0A8C4LJA7 736, A0A9L0ITE5 99). All six come from Ensembl gene ENSEASG00005007615 [file:EQUAS/SEC23A/SEC23A-bioinformatics/RESULTS-rereview.md].
- A0A9L0IQB9 = transcript ENSEAST00005045719 (19 exons); it skips one 78-nt exon present in the canonical transcript ENSEAST00005083518 (20 exons), an in-frame deletion of exactly the 26 residues equivalent to human 554-579 (linker between helical domain and gelsolin-like repeat). Human UniProt lists no isoform lacking this segment (human isoform 2 lacks 1-202 instead).
- All characterised functional residues retained: Zn ligands C61/C66/C85/C88, F382 (CLSD), gelsolin PPP-site F628/Y672/Y678/F681 (donkey F602/Y646/Y652/F655).
- So: alternative transcript (exon-skipping) gene model, not a fragment; function claims are transferred from the canonical product with the caveat that the deletion is untested.

### Evolutionary grounding
- Donkey SEC23A is in PANTHER PTHR11141:SF7 (SEC23A subfamily) with human Q15436, mouse Q01405, bovine, Xenopus and zebrafish Sec23a (`interpro/panther/PTHR11141/PTHR11141-entries.csv`); yeast Sec23 is SF0. No PANTHER family review file exists for PTHR11141 (only entries/metadata), so no subfamily disagreement to report.
- Donkey TreeGrafter rows cite PTN000124665; human SEC23A IBA rows (QuickGO) cite PTN000124617 for the same four terms (GAP activity, cargo loading, ER exit site, COPII vesicle coat), with SGD Sec23 donors for GAP. The relationship between the two PTN nodes was not verified.

### Literature added (cached)
- PMID:8451644 yeast Sec23p is a Sar1 GAP; PMID:12239560 Sec23/24-Sar1 structure, arginine finger; PMID:8898360 human SEC23A transitional ER/vesicles, cytosolic complex, complements sec23-1; PMID:16980979 CLSD F382L loss of budding function; PMID:17981132 mutant SEC23A poorly recruits Sec13-Sec31; PMID:17499046 Sec22 binds at Sec23/24 interface; PMID:27551091 (full text) TANGO1/cTAGE5 and Sec31 PPP motifs bind the Sec23a gelsolin-like domain.
- The zebrafish sec23a morpholino phenotype (PMID:16980979) was not used as process evidence.

### Decisions (unchanged actions, stronger support)
- All 11 rows retain their previous actions: GAP activity, ER membrane, cytosol, ER-to-Golgi transport, ER to Golgi transport vesicle membrane, COPII vesicle coat, ER exit site, cargo loading, budding ACCEPT; intracellular protein transport and zinc ion binding KEEP_AS_NON_CORE. OLS confirms GO:0006886 is not an ancestor of GO:0006888/GO:0090110/GO:0090114.
- Supporting evidence moved from the UniProt summary and a SAR1B background paper to primary SEC23 papers. Description rewritten to cover Sec31 recruitment, PPP-motif binding and CLSD, and to state the alternative-transcript identity. No NEW terms.

### Relative
- Same-gene canonical A0A9L0JMP6 has no review in the repo; it is the next relative (folder would be genes/EQUAS/SEC23A__A0A9L0JMP6). Closest characterised ortholog: human SEC23A Q15436 (same subfamily SF7), also unreviewed in the repo.
- Modules: `modules/dmel_copii_coat.yaml` (Drosophila COPII coat, Sec23 GAP node) and `modules/vesicle_coat_budding.yaml`, `modules/chylomicron_assembly_secretion.yaml` (COPII mention) are relevant; none includes mammalian SEC23A.
