# Dl (Delta) — curation notes (DROME, P10041)

## Session 2026-09-30 (Notch signaling module)

Symbol note: UniProt gene_exact search for "Dl" also matches dl (dorsal, P15330, case-insensitive);
the fetch was therefore run with `--uniprot-id P10041`.

Deep research: `Dl-deep-research-falcon.md` (falcon) was produced during this session.

### Key findings
- Heterotypic Notch-Delta/Serrate binding and Delta homotypic binding in aggregation assays
  [PMID:10504334 "Molecular evidence has established that direct heterotypic interactions occur
  between the Drosophila receptor Notch and the ligands Delta and Serrate"].
- Notch EGF 11-12 are the Delta-binding site [PMID:1657403].
- Ligand endocytosis driven by Mib1/Neur ubiquitination is required for activation
  [PMID:20176925 "Endocytosis of the transmembrane ligands Delta (Dl) and Serrate (Ser) is required
  for the proper activation of Notch receptors."].
- Kuzbanian sheds Delta; soluble ectodomain binds Notch [PMID:9872749].
- cis-inhibition: [PMID:41556123 "cis-Delta potently inhibits this non-canonical activation"];
  intracellularly truncated Delta is dominant negative [PMID:8756291].
- Deep research (falcon) notes that the first two EGF repeats of Delta resemble the DOS
  (Delta/OSM-11) motif, and that a lysine-less knock-in Delta retains signaling in some contexts
  (Troost et al. 2023, per deep research; the IMP row PMID:28960177 "Ubiquitylation-independent
  activation of Notch signalling by Delta" is consistent).

### Decisions
- Core MF: GO:0005112 Notch binding; GO:0048018 receptor ligand activity; location plasma
  membrane/apical PM; process Notch signaling pathway, lateral inhibition.
- REMOVE: GO:0005515 protein binding (Notch; Mib1 substrate interaction).
- IBA GO:0045746 negative regulation of Notch signaling (PTN001170801) kept as non-core
  (cis-inhibition is real for Dl).
- Developmental BPs kept as non-core; endocytic compartments kept as non-core.

### PANTHER
UniProt DR PANTHER: PTHR24049 ("CRUMBS FAMILY MEMBER"), no subfamily line.
IBA PTNs: GO:0005112 <- PANTHER:PTN002371879; GO:0005886, GO:0007219, GO:0045746 <-
PANTHER:PTN001170801.
