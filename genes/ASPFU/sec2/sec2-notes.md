# ASPFU sec2 notes

## 2026-11-06

- Fetched `ASPFU/sec2` with UniProt accession `Q4WWM8`. The reviewed UniProtKB
  entry is new in Swiss-Prot and places sec2 in PANTHER `PTHR14430:SF0`.
- Queried PubMed for `"Aspergillus fumigatus" AND (Sec2 OR Sec2p OR
  AFUA_3G06430)` and a broader Aspergillus Rab-GEF query; both leave Liu et al.
  2025 as the only direct A. fumigatus sec2 paper in PubMed as of this review.
- Liu et al. 2025 [PMID:39852455] directly deleted and complemented
  `AFUA_3G06430/sec2`. The paper shows that `sec2` disruption slows colony
  growth, changes hyphal-tip morphology, causes autophagosome and
  cell-wall-stress phenotypes, and reduces fungal burden and mortality in a
  mouse infection model.
- The PTHR14430 IBA to `GO:0005085 guanyl-nucleotide exchange factor activity`
  is sound for ASPFU/sec2. The 2025 Aspergillus paper did not assay exchange
  activity directly, but ASPFU/sec2 is the full-length fungal `PTHR14430:SF0`
  member, not the short `SCHPO/spo13`-like branch.
- The PTHR14430 IBA to `GO:0051286 cell tip` is also retained. Its
  `PANTHER:PTN001024876` placement is a fungal Sec2 active-location node seeded
  by direct CGD and PomBase Sec2 rows; the A. fumigatus deletion phenotype at
  hyphal tips is consistent with that inherited localization even though Sec2
  itself has not yet been imaged in Aspergillus.
- Liu et al. noted that `AnSEC2` deletion produces only a mild phenotype in
  *Aspergillus niger*, so the stronger *A. fumigatus* deletion phenotypes should
  stay as species-specific context and should not be propagated into downstream
  autophagy, cell-wall-integrity, or virulence annotations without direct assays.
- No autophagy, cell-wall-integrity, or virulence process annotation was added.
  The 2025 mutant phenotypes show that sec2 is required for those outputs, but
  they do not by themselves show that Sec2 performs the autophagy, signaling, or
  virulence steps.
