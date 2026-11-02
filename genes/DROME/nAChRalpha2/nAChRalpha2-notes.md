# nAChRalpha2 (Dalpha2 / SAD / CG6844; UniProt P17644) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of
DROME/NtR (Q9W288). No ProtNLM2 output was consulted. This review covers
nAChRalpha2 in its own right.

### Deep research

`just deep-research-falcon DROME nAChRalpha2 --fallback perplexity-lite` failed:
falcon raised "Exception: Failed to authenticate", and the perplexity-lite
fallback returned HTTP 401 "insufficient_quota". No deep-research file exists.
The review was written from the primary literature cached in `publications/`
(PubMed searched via E-utilities for Dalpha2/SAD/nAChRalpha2 and recent
TMX3-enabled expression papers).

### Evolutionary placement

- PANTHER 19.0 (fruit-fly HMM classification file, `PTHR19.0_fruit_fly`) places
  P17644 (FBgn0000039) in PTHR18945:SF430 "ACETYLCHOLINE RECEPTOR SUBUNIT
  ALPHA-LIKE 2-RELATED", together with NtR (Q9W288). The other fly nAChR alphas
  are in other subfamilies: nAChRalpha1 SF927, nAChRalpha3 SF895, nAChRalpha4
  SF928, nAChRalpha5 SF926, nAChRalpha6 SF876, nAChRalpha7 SF865.
- PAINT: nAChRalpha2 (FB:FBgn0000039) is itself one of three seeds of the IBD
  for GO:0022848 at PTN001825467, with nAChRalpha1 (FBgn0000036) and nAChRalpha3
  (FBgn0015519) (`interpro/panther/PTHR18945/PTHR18945-paint.tsv`). Its other
  IBAs come from deeper nodes: PTN000435923 (ACh-gated channel complex),
  PTN001054635 (plasma membrane), PTN001054960 (cholinergic synaptic
  transmission), PTN000434994 (eukaryote-level node: ion transmembrane
  transport, regulation of membrane potential, calcium ion transport). The
  calcium ion transport IBD at PTN000434994 is seeded only by vertebrate and
  worm genes; no Drosophila subunit has an experimental Ca2+ annotation.
- Caveat relevant for transfer to NtR: the Matthews 2018 tree places NtR outside
  the whole nAChR clade, so a shared PANTHER subfamily is not, on its own,
  enough to transfer subunit-specific properties from Dalpha2 to NtR.

### What is experimentally established for Dalpha2 in Drosophila

1. **Gene / expression.** Ligand-binding-type alpha subunit (vicinal Cys pair in
   loop C), gene at 96A next to ALS (nAChRalpha1) and SBD (nAChRbeta2)
   [PMID:2117557 "The deduced D alpha 2 protein shows the structural features
   of ligand-binding nAChR alpha-subunits"]. Transcripts and protein only in CNS;
   protein in synaptic neuropil [PMID:7861114 "Transcripts and protein from the
   D alpha 2 gene were detected exclusively in the central nervous system"].
2. **Native complex.** Co-immunoprecipitates with ALS from fly heads
   [PMID:10820216 "ALS-specific antibodies coprecipitate Dalpha2, and vice
   versa"]; ALS, Dalpha2 and SBD are integral components of one native complex
   [PMID:11796753 "revealed the existence of nAChR complexes that include ALS,
   D(alpha)2 and SBD as integral components"].
3. **Channel function only as a heteromer subunit.**
   - Early report: SAD cRNA alone gave nicotine-gated cation channels in oocytes
     [PMID:1697262]. Not reproduced later.
   - Dalpha2 alone or with other fly subunits (no cofactors) gave no channels;
     Dalpha2 + chick beta2 gave large ACh/nicotine currents, alpha-Bgt
     insensitive [PMID:8075828].
   - With cofactors TMX3/RIC-3/UNC-50, individual Dalpha2 and Dalpha2/Dbeta1 or
     Dalpha2/Dbeta2 pairings fail; Dalpha1/Dalpha2/Dbeta1 and
     Dalpha1/Dalpha2/Dbeta1/Dbeta2 form robust ACh-gated receptors and Dalpha2
     shifts ACh pEC50 [PMID:32611810]. Dalpha2 lowers neonicotinoid affinity
     [PMID:36795653].
   - Hybrid Dalpha2/vertebrate-beta2 receptors were the long-time workhorse for
     neonicotinoid pharmacology [PMID:9504393, PMID:15963641, PMID:10728888].
   So the correct MF claim is contributes_to GO:0022848; "enables" is not
   supported for the subunit alone.
4. **In vivo synaptic role.** In mushroom body output neurons (MBONs), an
   endogenously GFP-tagged alpha2 subunit is present in MBON dendrites; RNAi of
   alpha2 in M4/6 MBONs impairs 3-h appetitive memory expression and abolishes
   training-induced depression of MBON odor responses; alpha2 FRAP dynamics
   change with training [PMID:36250621]. This is good evidence for a
   postsynaptic cholinergic receptor role. I did not convert the memory
   phenotype into a process annotation (memory is a downstream organismal
   readout; the receptor's work is postsynaptic transmission).
5. **Deletion mutant.** Dalpha2attP flies are viable, with reduced fecundity
   and climbing [PMID:35576366] — organismal phenotypes, not annotated.
6. Expression in Tm2 neurons (single-cell RT-PCR, "Dalpha1/2") [PMID:22137471]
   — expression only, and the assay does not separate alpha1 from alpha2.

### Decisions summary

- MF: ACCEPT GO:0022848 (all four rows, incl. IEA "enables"; the subunit
  contributes to the heteromer's activity) and GO:0015464 contributes_to.
  MODIFY broad IEA MFs (GO:0004888, GO:0005216, GO:0005230) to GO:0022848.
- CC: ACCEPT GO:0005892 (IBA, IDA, IPI), plasma membrane, postsynaptic
  membrane; MODIFY GO:0016020 membrane -> plasma membrane / postsynaptic
  membrane.
- BP: ACCEPT cholinergic synaptic transmission, postsynaptic chemical
  transmission, EPSP, regulation of postsynaptic membrane potential,
  GO:0098655 monoatomic cation transmembrane transport. MODIFY ion transport
  generalities to GO:0098655 and GO:0042391 to GO:0060078. Calcium ion
  transport IBA kept as non-core (plausible for nAChRs; untested for Dalpha2).
- No NEW annotations.
