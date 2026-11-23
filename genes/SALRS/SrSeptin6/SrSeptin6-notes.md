# SrSeptin6 (Salpingoeca rosetta, F2UDE9 / PTSG_06009) - notes

Automated deep research was not available in this session (no provider API
keys configured), so there is no `-deep-research-*.md` file. These notes were
compiled manually from the cached full text of Booth et al. 2018 (PMID:30281390)
and the UniProt record. SrSeptin2 (F2UEE2, PTSG_07215) was reviewed in the same
session; see `genes/SALRS/SrSeptin2/SrSeptin2-notes.md`.

## Identity

- UniProt F2UDE9 (TrEMBL, unreviewed), 420 aa, ORF PTSG_06009, EMBL EGD74644.1;
  UniProt name "Septin".
- Literature name SrSeptin6 [PMID:30281390 "another septin paralogue, SrSeptin6 (PTSG_06009)"].
- Phylogenetic group: PTSG_04106, PTSG_06009 and PTSG_07215 map to Groups 1A,
  1B and 4 respectively [PMID:30281390 "with animal and fungal septins in Groups 1A (mammalian Septin 3 family), 1B (mammalian Septin 6 family), and 4 (S. cerevisiae Cdc12 family), respectively"].
  So PTSG_06009 (SrSeptin6) is the **Group 1B (mammalian SEPT6-family)** septin.
- Domains (UniProt): septin-type G domain 36-290 (PS51719) with G1 (46-53), G3
  (97-100) and G4 (180-183) motifs and PIRSR GTP-binding sites; coiled coil
  317-366; C-terminal disordered/basic region 392-420.
- Family: PANTHER PTHR18884 (SEPTIN); Pfam PF00735.
- Whether SrSeptin6 hydrolyses GTP was not examined. (In mammals SEPT6-group
  septins are often described as GTPase-deficient; this has not been tested for
  the choanoflagellate protein and is not asserted here.)

## Localisation (only direct evidence)

- mTFP1 fusion mirrors SrSeptin2 enrichment at the basal pole of single cells
  [PMID:30281390 "mTFP1-SrSeptin6 mirrored the enrichment of mTFP1-SrSeptin2 at the basal pole"];
  [PMID:30281390 "found that SrSeptin6 displays the same basal localization as SrSeptin2 (Figure 4C)."].
- Colocalisation with SrSeptin2 suggests co-assembly [PMID:30281390 "strongly suggest that SrSeptin2 and SrSeptin6 assemble together at the basal pole."].
- The figure panels showing rosettes (E, F) and microtubule intercalation (G)
  use SrSeptin2, not SrSeptin6; the paper's discussion refers to basal and
  lateral localisation "of SrSeptin2 and SrSeptin6 in rosettes", but the
  results shown for SrSeptin6 are single-cell (Fig. 4C) plus supplementary
  colocalisation (Fig. S9, not cached). I therefore assert only basal part of
  cell for SrSeptin6.

## Function

- No loss-of-function, biochemical or interaction data. Rosette-development
  role is a hypothesis [PMID:30281390 "a family of paralogous genes hypothesized to contribute to multicellular development in S. rosetta"].

## Knockout literature check (2026-10-01)

No septin knockout in PMID:32496191 (full text), PMID:41037400 (abstract only)
or DOI:10.1101/2024.07.13.603360 (full text; septins appear only in the
bibliography).

## Review decisions (summary)

- GTP binding (IEA, GO_REF:0000120): ACCEPT.
- septin complex (UniRule): ACCEPT.
- NEW: basal part of cell (IDA).
- Track C: both rows are domain/family-rule IEAs for a biochemical activity and
  a family-defining complex; nothing animal- or tissue-specific propagated.
