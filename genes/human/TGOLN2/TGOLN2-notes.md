# TGOLN2 (TGN46/TGN48/TGN51; O43493) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: TGOLN2 is reviewed as the closest experimentally characterised relative of
the fly benchmark gene rgn (M9PFV8), which shares PANTHER subfamily PTHR23211:SF0 and
the single PAINT node PTN000575073. No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon human TGOLN2 --fallback perplexity-lite` failed: falcon
returned "Edison API request failed: Failed to authenticate" (HTTP 403), and the
perplexity-lite fallback timed out after 600 s. No deep-research file exists. The review
is built from the GOA-cited papers plus papers found by PubMed E-utilities searches
(TGN46/TGOLN2/TGN38/TGN51 in title), cached with `just fetch-pmid`.

### Protein

- Type I single-pass membrane glycoprotein, 437 aa (isoform TGN46): signal peptide 1-21,
  heavily glycosylated mucin-like lumenal domain 22-381 (14 x 14-aa tandem repeats,
  mostly disordered), TM 382-402, short cytosolic tail 403-437 carrying the YQRL
  tyrosine sorting motif (UniProt MOTIF 430-433). Alternative 3' splice sites give
  TGN48 and TGN51, which carry one or two extra tyrosine motifs [PMID:9422759].
- Luminal Ser/Thr residues are phosphorylated by FAM20C (UniProt MOD_RES, PMID:26091039,
  not cached).

### Localization (human experimental)

- Human TGN46 is "localised primarily to the TGN but is present on the cell surface and
  returns via endosomes" [PMID:8907712].
- Quantitative immuno-EM in HeLa: 80% of TGN46 in tubules, little overlap with GalT in
  the stack [PMID:9084986].
- Tyrosine-motif mutation: "mutated hTGN48 and hTGN46 are no longer retrieved to the TGN"
  while hTGN51 stays in the TGN [PMID:9422759].
- Used ubiquitously as a TGN marker; the IDA rows from PMID:22456507 (Atg9),
  PMID:27435297 (LH3), PMID:18166528 (SLC24A5), PMID:23386608 (RHBDD2, anti-TGN38 in
  HEK293) and PMID:22797923 (ZNRF2) are all marker uses, so they support localization
  only.

### Function (human experimental)

- Lujan et al. 2024 eLife [PMID:38466628] (full text cached): CRISPR TGN46-KO HeLa cells
  show ~75% less PAUF secretion, fewer CARTS (PKD-dependent TGN-to-PM carriers), slower
  PAUF Golgi export; VSVG carriers unaffected. The lumenal domain is necessary and
  sufficient to sort TM chimeras into CARTS. No direct TGN46-PAUF binding was shown (they
  suggest PAUF, a putative lectin, could recognise TGN46 glycans). The authors state
  explicitly that whether TGN46 is an active player in CARTS biogenesis or a passive TM
  cargo is unknown. So: sorting role in Golgi-to-PM protein transport is experimentally
  supported (KO + lumenal domain mapping); "cargo receptor activity" (binding) is
  proposed, not demonstrated.
- UniProt FUNCTION is still "May be involved in regulating membrane traffic to and from
  trans-Golgi network".

### Rodent orthologs (same subfamily SF0; not transferred as annotations)

- Rat TGN38 (P19814, Ttgn1) tail binds AP-2 mu2 via the YQRL motif (Y2H) [PMID:9794796];
  rat TGN38 binds a p62/rab6 cytosolic complex (PMID:8349729, not cached), integrin beta1
  via its lumenal domain (PMID:11208159, not cached) and neurabin (PMID:10514494, not
  cached). These were not checked in human and are not annotated on TGOLN2 here.
- Retrograde endosome-to-TGN transport of TGN38 needs retromer/SNX2, syntaxin 16 and GCC88
  [PMID:20138391] - TGN38 is the cargo, not the machinery.

### PANTHER / PAINT

- PTHR23211:SF0 contains human TGOLN2, rat TGN38 and fly rgn. PAINT node PTN000575073
  (taxon:2759) carries only two CC IBDs: GO:0005802 (seeds MGI:105079, MGI:105080,
  RGD:620445, O43493) and GO:0030140 (seed MGI:105079). No MF or BP was propagated:
  treat that as deliberate. The fly relative lacks the TM and YQRL motif, so transfer of
  TGN/cycling behaviour to rgn is not supported by architecture.

### Decisions

- Accept TGN rows; MODIFY Golgi apparatus to TGN; MODIFY transport vesicle to TGN
  transport vesicle; keep plasma membrane and clathrin-coated endocytic vesicle membrane
  as non-core (transient cycling compartments); REMOVE ER lumen (membrane protein;
  Reactome FAM20C reaction compartment artifact); REMOVE generic protein binding.
- NEW: GO:0043001 Golgi to plasma membrane protein transport, IMP, PMID:38466628
  (TGN46 lumenal domain does the sorting work). No NEW MF (cargo receptor activity
  needs binding data).
