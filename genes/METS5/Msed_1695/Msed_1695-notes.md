# Msed_1695 (A4YHE8, Metallosphaera sedula DSM 5348) notes

## Provenance

Automated deep research was unavailable for this review; no `-deep-research-*.md`
file exists. Literature was found with NCBI E-utilities (PubMed esearch/esummary) and
read from cached `publications/PMID_*.md` files. Family, orthology and synteny checks
used UniProt REST and are reproducible in `Msed_1695-bioinformatics/` (see RESULTS.md).
GO term checks used the OLS4 and QuickGO REST APIs (2026-10-15).

## Identity: Msed_1695 is the M. sedula CdvB2 ortholog

- UniProt names the protein only "Snf7" (unreviewed, PE 4). The NCBIfam match places it
  in the CdvB1/CdvB2 family: [file:METS5/Msed_1695/Msed_1695-uniprot.txt "NCBIfam; NF041005; cell_div_CdvB1_B2; 1."]
- M. sedula has four Cdv ESCRT-III proteins: Msed_1671 (CdvB, NF041008, in the
  cdvA-cdvB-cdvC cluster with Msed_1670 CdvA-like and Msed_1672 AAA ATPase), Msed_1695
  and Msed_2179 (both NF041005, CdvB1/B2 family) and Msed_1969 (NF041009, CdvB3).
- Pairwise identity: Msed_1695 is 64.8% identical to S. acidocaldarius CdvB2 (Saci_1416,
  Q4J8Y4) and 60.5% to CdvB1 (Saci_0451, Q4JBG6); Msed_2179 is 61.1% to CdvB1 and 57.0%
  to CdvB2. These are reciprocal best-hit pairs, but the margin is small because B1 and
  B2 are close paralogs. [PMID:32502411 "close paralogs that share 65% amino-acid identity and 80% similarity"]
- Synteny decides it: the Msed_1695 neighbourhood (PEP synthase, inositol-1-phosphate
  synthase, arCOG07220, UbiD-family decarboxylase, threonine synthase) matches the
  Saci_1416 (cdvB2) neighbourhood (5 shared arCOGs, 0 with cdvB1); Msed_2179 sits next to
  TrpRS like Saci_0451 (cdvB1).
  [file:METS5/Msed_1695/Msed_1695-bioinformatics/RESULTS.md "Msed_1695 is the CdvB2 ortholog of M. sedula"]
- Independent confirmation: a 2022 study names Msed_2179 as M. sedula CdvB1, leaving
  Msed_1695 as CdvB2.
  [PMID:35238034 "The gene for CdvB1 from Metallosphaera sedula (Msed_2179, UniProtID A4YIR6) was obtained from the Gen Bank database"]

## M. sedula-specific experimental data

- None for Msed_1695. No PubMed hit for the locus. M. sedula Cdv biochemistry exists for
  the cdv-cluster proteins (CdvA, CdvB = Msed_1671, CdvC):
  [PMID:21760923 "Here, we report the biochemical and biophysical characterization of the three Cdv proteins from the hyperthermophilic archaeon Metallosphaera sedula, a member of the order Sulfolobales."]
  and for M. sedula Vps4/CdvC structure (PMID:26632262) and M. sedula CdvB1 (Msed_2179)
  polymerization and CdvC-driven depolymerization (PMID:35238034). None tests Msed_1695.

## What the S. acidocaldarius ortholog (CdvB2, Saci_1416) does

- CdvB forms a non-contractile template ring that recruits CdvB1 and CdvB2 into a
  contractile ESCRT-III copolymer; degradation of CdvB triggers constriction.
  [PMID:32764038 "CdvB both templates the assembly of a contractile ESCRT-III copolymer, composed of the paralogs CdvB1 (Saci_0451) and CdvB2 (Saci_1416), and prevents their constriction"]
- Loss of CdvB2 causes asymmetric division, rescued by ectopic CdvB2; CdvB2 keeps the
  ring centred as it constricts.
  [PMID:32502411 "the impact of CdvB2 loss on division was much more profound than the loss of CdvB1 at 75°C"]
  [PMID:32502411 "These data suggested that CdvB2 is recruited (along with CdvB1) to the correct position at the cell center by the CdvB ring and functions, following the loss of CdvB, to prevent the division ring from slipping as it constricts."]
- CdvB2 occupies the midzone of the cytokinetic bridge and its Vps4-dependent
  disassembly is linked to scission.
  [PMID:36921039 "membrane scission depends on disassembly of polymeric CdvB2 from the cytokinetic bridge"]
  [PMID:36921039 "CdvB2 was seen coating the membrane bridge connecting the two daughter cells"]
- CdvB2 binds archaeal-lipid liposomes via short N-terminal amphipathic helices, forms
  helical filaments, and coats membrane nanotubes.
  [PMID:41543908 "CdvB and CdvB2 efficiently pelleted with archaeal liposomes, while CdvB1 remained mainly in the soluble fraction"]
  [PMID:41543908 "We instead turned to CdvB2, which is thought to perform the final membrane abscission during cytokinesis, in the better-characterized S. acidocaldarius system (10)."]
- S. islandicus ESCRT-III paralog functional assignment (PMID:28557139) is abstract-only
  in the cache; not relied on.

## GO decisions

- **GO:0007034 vacuolar transport (IEA, InterPro2GO via IPR005024)**: REMOVE. Archaea
  have no vacuole; the Snf7-family-to-vacuolar-transport mapping encodes the eukaryotic
  ESCRT-III role in MVB/vacuole sorting, which does not exist here. Not MODIFY: the
  claimed process (transport into/within a vacuole) is a different process from cell
  division, not a less specific version of it.
- **GO:0061639 Cdv-dependent cytokinesis**: proposed NEW with ISS from Q4J8Y4 (Saci_1416).
  Participation test: CdvB2 is a structural component of the constricting ESCRT-III
  division polymer and its disassembly is linked to scission (does work in the process,
  not a substrate). Orthology is supported by family, reciprocal best hit, synteny and an
  independent literature assignment of the sister paralog. Comparator check: QuickGO
  shows zero annotations to GO:0061639 for any gene product, including Q4J8Y4, Q4JBG6
  and Q4J924 (no S. acidocaldarius Cdv protein has any GO annotation beyond Q4J924's
  nucleoid IEA). The absence is a curation gap for an archaea-specific term coined for
  these proteins, the same conclusion reached in the SULAC/cdvB review.
- Not proposed as NEW: ESCRT III complex (GO:0000815) and cell division site
  (GO:0032153). They are likely by orthology but kept in core_functions only, to keep
  orthology-only NEW rows minimal. No MF NEW: no GO MF fits "contractile ESCRT-III
  polymer subunit"; membrane bending activity (GO:0180020) is not directly shown for CdvB2
  in vivo.

## Error-pattern scope (ARCHAEA pattern 3)

- QuickGO (taxon Archaea, descendants, 2026-10-15): 51 archaeal GO:0007034 rows; 41 come
  from InterPro2GO (GO_REF:0000002) via IPR005024, the rest from TreeGrafter
  (GO_REF:0000118) on PANTHER nodes. The 41 IPR005024 rows span roughly 36 taxa across
  Sulfolobales (e.g. M. sedula, Sulfurisphaera tokodaii, Acidianus manzaensis),
  Thermoplasmatales (Thermoplasma acidophilum, T. volcanium), Thaumarchaeota
  (Nitrosopumilus maritimus, Nitrosarchaeum koreense) and Asgard archaea
  (Promethearchaeum syntrophicum, Candidatus Lokiarchaeum ossiferum).
- Within M. sedula only Msed_1695 is hit, because only it also matches Pfam PF03357 /
  IPR005024; its CdvB1 paralog Msed_2179 (IPR053492 only) and S. acidocaldarius CdvB2
  (IPR053492 only) escape. So the error depends on whether the HMM for Pfam Snf7 happens
  to match a given CdvB1/B2 sequence, not on biology.
- Fix: taxon-restrict the IPR005024 -> GO:0007034 InterPro2GO mapping to Eukaryota.
