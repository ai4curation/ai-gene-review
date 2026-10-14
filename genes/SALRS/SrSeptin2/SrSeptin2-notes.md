# SrSeptin2 (Salpingoeca rosetta, F2UEE2 / PTSG_07215) - notes

Automated deep research was not available in this session (no provider API
keys configured), so there is no `-deep-research-*.md` file. These notes were
compiled manually from the cached full text of Booth et al. 2018 (PMID:30281390)
and the UniProt record. SrSeptin6 (F2UDE9, PTSG_06009) was reviewed in the same
session; see `genes/SALRS/SrSeptin6/SrSeptin6-notes.md`.

## Identity

- UniProt F2UEE2 (TrEMBL, unreviewed), 412 aa, ORF PTSG_07215, EMBL EGD74992.1.
  UniProt name "Septin-type G domain-containing protein".
- Literature name SrSeptin2 [PMID:30281390 "We started by examining the localization of the S. rosetta septin protein SrSeptin2 (PTSG_07215)"].
- Phylogenetic group: the three S. rosetta septins PTSG_04106, PTSG_06009 and
  PTSG_07215 were placed with animal/fungal septins in Groups 1A, 1B and 4,
  respectively [PMID:30281390 "with animal and fungal septins in Groups 1A (mammalian Septin 3 family), 1B (mammalian Septin 6 family), and 4 (S. cerevisiae Cdc12 family), respectively"].
  So PTSG_07215 (SrSeptin2) is the **Group 4 (Cdc12-family)** septin. The
  name "SrSeptin2" therefore does not imply orthology with mammalian SEPT2.
  The UniProt FunFam hit is "septin-7 isoform X1" (3.40.50.300:FF:000162).
- Domains (UniProt): septin-type G domain 21-294 (PS51719) with G1 (31-38),
  G3 (89-92) and G4 (170-173) motifs and PIRSR GTP-binding sites; C-terminal
  disordered region 369-412. The paper describes a C-terminal coiled-coil
  [PMID:30281390 "a septin with the diagnostic G-domain and coiled-coil domain that typify human and fungal septins"].
- Family: PANTHER PTHR18884 (SEPTIN); Pfam PF00735; PIRSF006698.

## Localisation (only direct evidence)

- N-terminal mTFP1 fusion expressed from a transfected plasmid. Enriched at the
  basal pole of single cells and rosette cells, and at contacts between
  adjacent rosette cells [PMID:30281390 "Strikingly, mTFP1-SrSeptin2 was enriched at the basal poles of single and rosettes cells (Figure 4, B and E) and at points of contact between adjacent cells in rosettes (Figure 4E)."].
- Also diffuse in the cytosol [PMID:30281390 "revealed SrSeptin2 distributed throughout the cytosol and enriched at the basal pole"].
- Forms filaments that intercalate between cortical microtubules at the basal
  pole [PMID:30281390 "Fluorescence microscopy showed that septin filaments intercalate between cortical microtubules at the basal pole of the cell (Figure 4G)."].
- Basal enrichment requires the coiled-coil domain; the deletion forms
  ectopic rings around (presumed) food vacuoles [PMID:30281390 "We further found that the basal localization of SrSeptin2 requires the coiled-coil domain"].
- Colocalises with SrSeptin6; heteromeric assembly is inferred, not shown
  biochemically [PMID:30281390 "strongly suggest that SrSeptin2 and SrSeptin6 assemble together at the basal pole."].
- Caveat: tagged, plasmid-driven expression; no antibody to endogenous protein.
  The authors argue tagged septins match native localisation in other systems.

## Function

- No loss-of-function, biochemical (GTP binding/hydrolysis, filament
  reconstitution) or interaction data for SrSeptin2.
- A role in rosette development is a hypothesis
  [PMID:30281390 "a family of paralogous genes hypothesized to contribute to multicellular development in S. rosetta"];
  [PMID:30281390 "perhaps supporting intercellular contacts at the basal ends of cells in rosettes"].

## Knockout literature check (2026-10-01)

Searched the cached texts of PMID:32496191 (CRISPR genome editing, full text),
PMID:41037400 (selection-based knockouts, abstract only) and the bioRxiv
preprint DOI:10.1101/2024.07.13.603360 (full text) for "septin", PTSG_07215
and PTSG_06009. None reports a septin knockout; the preprint mentions septins
only in its bibliography (Booth et al. 2018). The full text of PMID:41037400 is
not cached, so its supplementary target list was not checked.

## Review decisions (summary)

- GTP binding (IEA, GO_REF:0000120): ACCEPT - intact septin G-domain motifs.
- cytoplasm (ARBA): ACCEPT - tagged protein is cytosolic plus basally enriched.
- cytoskeleton (ARBA): ACCEPT - filaments observed; NEW IDA septin cytoskeleton.
- septin complex (UniRule): ACCEPT - canonical for the family; colocalisation
  with SrSeptin6 consistent.
- NEW: basal part of cell (IDA), septin cytoskeleton (IDA).
- Track C: all rows are IEA from domain/family rules or ARBA; no animal
  tissue or developmental term has propagated. No propagation problem.
