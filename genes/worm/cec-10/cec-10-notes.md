# cec-10 (ZK973.2, Q9N4L7) curation notes

## Status of literature

- Automated deep research (falcon) failed in this environment (authentication), so no
  `-deep-research-*.md` file exists. These notes are a manual literature search via PubMed.
- PubMed search for `"cec-10" OR ZK973.2` returned no hits (2026-10-19). No publication
  characterises cec-10 directly. The UniProt entry is unreviewed (TrEMBL) and the only
  reference it cites is the genome paper [PMID:9851916].
- Expression: Bgee summary in UniProt
  ["Expressed in germ line (C elegans) and 4 other cell types or tissues."].

## Domain architecture (UniProt / InterPro)

- N-terminal chromodomain, residues 49-110 [UniProt Q9N4L7 "FT   DOMAIN          49..110"; PROSITE PS50013, SMART SM00298].
- One ankyrin repeat, 520-552 (PROSITE PS50088), in an ankyrin superfamily region 451-589.
- Long disordered regions (1-47, 116-135, 141-381, 814-865).
- No KilA-N / APSES DNA-binding domain (see `cec-10-bioinformatics/RESULTS.md`).
- PANTHER PTHR43828 ("ASPARAGINASE" in the PANTHER OBO; InterPro calls it "Cell Cycle
  Transcription Regulator" / IPR051642 "SWI6-like"), subfamily SF3, named
  "CHROMO DOMAIN-CONTAINING PROTEIN". Per the InterPro entries list in
  `interpro/panther/PTHR43828/PTHR43828-entries.csv`, SF3 also contains budding yeast Swi6
  (P09959) and fission yeast Cdc10 (P01129), the non-DNA-binding subunits of SBF/MBF.

## Why cec-10 sits under the MBF node

- PTN000917496 is a PANTHER ancestral node in PTHR43828, seeded by fission-yeast MBF
  subunits (Res2 SPAC22F3.09c, Cdc10 SPBC336.12c, Res1 SPBC725.16) and budding-yeast
  Swi4 (S000000913), Mbp1 (S000002214) and Swi6 (S000004172), plus Candida and Aspergillus
  members. cec-10 descends from it because the PTHR43828 HMM matches across residues
  17-793, probably through the ankyrin region and what lies around it.
- Pairwise alignment to the six yeast seeds is weak: Z 1.9-5.5 against shuffles, 23-32%
  identity, mostly over low-complexity stretches. The DNA-binding seeds' KilA-N/APSES
  domain has no counterpart in cec-10
  [file:worm/cec-10/cec-10-bioinformatics/RESULTS.md].
- SBF/MBF DNA-binding subunits are fungal-specific, derived from a viral KilA-N protein
  [PMID:27162172 "We were unable to find any eukaryotic homologs of SBF or Whi5 outside of fungi"];
  animals use E2F [PMID:27162172 "SBF and its ancestral animal counterpart E2F"].
- Conclusion: the PAINT IBD is placed at a node deep enough to take in a sporadic
  metazoan ankyrin/chromodomain lineage. That lineage cannot form an MBF complex, since
  animals have no MBF DNA-binding subunit. In IBA_REVIEW terms this is `PROPAGATION_BAD` with
  `LINEAGE_OR_TAXON_MISMATCH` (node too deep). Wei et al. 2020
  [PMID:32470107] flagged GO:0030907 and GO:0033309 for this protein. The flag holds.
  - The InterPro API lists 48 metazoan PTHR43828 proteins (cnidarians, molluscs, an
    annelid, a priapulid, insects); cec-10 is the only Caenorhabditis member. A few
    coral/octopus entries are named "MBP1"/"SWI4-like" and may carry KilA-N domains
    (not checked). That would be a separate question.

## Related CEC proteins (context only)

- CEC-4 is a C. elegans chromodomain protein that binds methylated H3K9 and anchors
  heterochromatin at the nuclear periphery [PMID:26607792 "CEC-4 binds preferentially
  mono-, di-, or tri-methylated H3K9 and localizes at the nuclear envelope independently
  of H3K9 methylation and nuclear lamin."]. No such data exist for CEC-10. Shared
  "CEC" nomenclature reflects the chromodomain only. It does not show that CEC-10 binds
  H3K9me.

## Decisions

- All MBF/SBF-derived IBA rows (MBF complex, contributes_to RNAPII cis-regulatory DNA
  binding, DNA-binding activator activity, positive regulation of RNAPII transcription,
  G1/S transition) are removed.
- Cytoplasm IBA (donor: budding-yeast Swi6, which shuttles) marked as over-annotated.
- Nucleus (ARBA IEA) accepted as plausible for a chromodomain protein, without evidence
  of any specific function.
- No core function can be stated honestly. The knowledge gaps are recorded in the review.
