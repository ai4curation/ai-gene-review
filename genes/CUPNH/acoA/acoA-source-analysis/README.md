# Cross-taxon acetoin-system identity and evidence trace

This directory records the eleven normally seeded reviews and their original annotation payloads. It is provenance, not an independent biochemical assay. Run `uv run python genes/CUPNH/acoA/acoA-source-analysis/check_preservation.py` from the repository root.

| Organism | Gene | Accession | Original rows | Primary source |
|---|---|---|---:|---|
| CUPNH | acoA | P27745 | 4 | 2061286 |
| CUPNH | acoB | P27746 | 1 | 2061286 |
| CUPNH | acoC | P27747 | 2 | 2061286 |
| SYNCB | acoA | Q57102 | 3 | 8110297 / 1898934 |
| SYNCB | acoB | Q57041 | 0 | 8110297 / 1898934 |
| SYNCB | acoC | Q59658 | 3 | 8110297 / 1898934 |
| SYNCB | acoL | Q60154 | 5 | 8110297 / 1898934 |
| BACSU | acoA | O31404 | 5 | 10368162 |
| BACSU | acoB | O34591 | 1 | 10368162 |
| BACSU | acoC | O31550 | 3 | 10368162 |
| BACSU | acoL | O34324 | 9 | 10368162 |

CUPNH is H16 (tax381666), with original M66060 and later AM260480 records. Current sequence version3 is not asserted to be identical to every original clone residue. SYNCB is the original-paper Pelobacter carbinolicus accession set, now Syntrophotalea carbinolica (tax19); U01100 and L24124 identify strain Gra Bd 1. Independent ENA U01100 retrieval confirms the strain and UniProt cross-references. Separate SYNC1 genome records were not substituted. BACSU is strain168 (tax224308); AcoC O31550 uses the reference rather than the slightly different AF006075 experimental clone.

Native Pelobacter components were purified and reconstituted (1898934), and N-terminal sequencing maps them to acoABCL (8110297). H16 E1 is a probable alpha2-beta2 complex; AcoC is native FMP assigned an E2 role by sequence/curated inference (2061286). The H16 AcoC lipoyl-plus-alpha/beta-hydrolase architecture differs from canonical E2 folds; no isolated H16 E2 assay is asserted. Bacillus acoA disruption eliminates E1 activity and stationary-cell acetoin use, with E2/E3 contributions supported by sequence/context (full PMID10368162).

The committed PAINT slices `interpro/panther/PTHR11516/PTHR11516-paint.tsv` and `interpro/panther/PTHR22912/PTHR22912-paint.tsv` were read. PTN008519424 contains positive GO0004739/GO0006086 IBDs; PTN000162370 contains GO0045254. Existing negative branches are not assigned to targets without tree-placement evidence. PTN000530299 contains GO0004148, GO0006103 and GO0050660. Conserved E3 chemistry is accepted while target-specific sharing with oxoglutarate metabolism remains unresolved.

Live QuickGO definitions distinguish pyruvate oxidative decarboxylation (4739) from acetoin cleavage and acetoin/diacetyl interconversion (19152). The broad E1 term16624 is retained as complex contribution. Three NEW IC rows are limited to the previously unrepresented AcoB contribution, justified by mapped native E1 component identity/comparative chemistry; no new BP assertion was made.

Normal Falcon/fallback and FEBA attempts failed without producing evidence artifacts. All initial publication jobs succeeded; additional normal force and full-text-chain attempts left the old scanned primaries abstract-only. Explicit positive abstract results are usable; absent assays are not fabricated. Publisher/EuropePMC PDF requests returned 403. PMID2200674 was a false literature lead and is excluded from functional evidence.
