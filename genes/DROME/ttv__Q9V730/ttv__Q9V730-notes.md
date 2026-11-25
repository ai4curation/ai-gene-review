# ttv (Q9V730, tout-velu / DEXT1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: Q9V730 is the reviewed Swiss-Prot canonical product of FlyBase FBgn0265974 (ttv),
760 aa. The sibling folder `genes/DROME/ttv` is keyed to D5SHU8 (the 299-aa ttv-PC
product). This folder reviews Q9V730 in its own right; no ProtNLM2 file or prediction
evidence folder was opened or used.

### Setup / provenance

- `just fetch-gene DROME Q9V730 --alias ttv__Q9V730` seeded 35 GOA rows and 18 references.
- `just fetch-gene-pmids` cached all 12 GOA PMIDs. Only PMID:17409068 and PMID:19389345
  (the germ-cell-migration pair) have cached full text; the rest are abstract-only.
- **Deep research failed**: `just deep-research-falcon DROME ttv__Q9V730 --fallback
  perplexity-lite` exited 1. Falcon: "Exception: Failed to authenticate"; perplexity-lite
  fallback: HTTP 401 "You exceeded your current quota". No deep-research file exists for
  this folder; the review is built from the cached literature, the UniProt record and
  PANTHER/PAINT data.
- Additionally cached PMID:23720043 (Rotini/GOLPH3 regulates EXT retrograde trafficking),
  PMID:14729575 (glypicans Dally/Dly are Ttv substrates) and used the already-cached
  PMID:12586063 (Hh movement depends on Ttv-made proteoglycans).

### Molecular function (experimental, in Drosophila)

- Izumikawa et al. 2006 [PMID:16303756 "Here we demonstrated that TTV/DEXT1 and SOTV/DEXT2
  had GlcNAcT-II and GlcAT-II activities required for the biosynthesis of repeating
  disaccharide units of the HS backbone, and the coexpression of TTV with SOTV markedly
  augmented both glycosyltransferase activities"]. So both co-polymerase half-reactions
  (GO:0050508 GlcNAcT-II, GO:0050509 GlcAT-II) are directly assayed for Ttv itself.
- Ttv-Sotv lacks GlcNAcT-I (chain initiation): [PMID:16303756 "In contrast to human,
  TTV-SOTV exhibited no GlcNAcT-I activity"]. Initiation is Botv (DEXT3/EXTL3 ortholog)
  [PMID:11832488]. So Ttv must NOT be given chain-initiation (GlcNAcT-I, alpha-1,4-GlcNAc
  transfer to the linkage tetrasaccharide) activity — a deliberate difference from the
  claim that human EXT1 can do this.
- Complex: [PMID:14998928 "We demonstrate further that Ttv and Sotv form a complex and are
  co-localized in vivo."]. GO:0120504 EXT1-EXT2 complex definition explicitly says "In
  Drosophila, the complex consists of ttv and sotv."

### Biological process

- In vivo HS loss: [PMID:10806213 "A mutation in tout-velu ... likewise does not affect
  chondroitin sulfate synthesis but reduces all forms of heparan sulfate to below the limit
  of detection."]; [PMID:10644674 marked reductions in HS but not CS].
- Non-redundant with sotv/botv: [PMID:14645127 "Mutation in any of these genes impaired
  biosynthesis of HSPGs in vivo"]; [PMID:15056609 HS levels "dramatically reduced in the
  absence of Sotv or its partner co-polymerase Tout velu (Ttv)"].
- Glypicans Dally/Dly are substrates [PMID:14729575].
- Morphogen (Hh, Dpp, Wg) movement/gradient defects are downstream consequences of loss of
  HSPGs, not Ttv participating in signal transduction. Per CLAUDE.md "Do not add what
  curators deliberately declined", no NEW signaling/morphogen process terms are proposed.
  (The GOA set itself carries no Hh/Wg/Dpp pathway term for Q9V730.)

### Germ cell migration (contested)

- Deshpande et al. 2007 [PMID:17409068] — deficiency/zygotic mutant and germline clone
  defects; overexpression phenotypes; argue the requirement is somatic ("it seems likely
  that ttv activity is required in the soma, not the germline").
- Renault et al. 2009 [PMID:19389345] — using the verified null ttv l(2)00681, M-Z+ and
  M+Z- embryos show wild-type germ cell migration; "Taken together our results suggest that
  ttv loss of function has no effect on germ cell migration." FlyBase carries both the
  positive IMP and the NOT IMP.
- Decision: the positive row is REMOVE (contradicted by a later null-allele
  study and, even if real, an indirect consequence of extracellular HSPG/Hh distribution in
  somatic tissue, not Ttv doing the work of germ cell migration). The NOT row is kept as
  non-core.

### Localization

- ER and Golgi IDA (PMID:10549295, PMID:14998928). UniProt: ER membrane and Golgi membrane,
  single-pass type II (TM 7-25, lumenal 26-760). Rotini (Drosophila GOLPH3) controls
  retrograde intra-Golgi trafficking of EXTs [PMID:23720043]. HS polymerization is a Golgi
  process; ER localization is consistent with complex assembly/ER exit of EXT proteins.

### Evolutionary grounding

- UniProt DR: PANTHER PTHR48261:SF3 (EXOSTOSIN GLYCOSYLTRANSFERASE 1) — same subfamily
  label as vertebrate EXT1 (the task brief states human EXT1 is in SF3).
- Caveat recorded: the cached PANTHER 19.0 HMM classification files used by this repo
  (`.cache/panther/PTHR19.0_*`, build artifact, not cited) place ttv in
  PTHR11062:SF129 "EXOSTOSIN-1" (with C. elegans rib-1) and human/mouse EXT1 in
  PTHR11062:SF97 "EXOSTOSIN-1", and sotv with human EXT2 in PTHR11062:SF381 "EXOSTOSIN-2".
  So the family id/subfamily numbering differs between PANTHER releases, but in both
  versions ttv falls in an EXT1 ("Exostosin-1") subfamily distinct from the EXT2 (sotv)
  and EXTL3 (botv) subfamilies. Ttv is the EXT1 ortholog, consistent with its paralog
  partner Sotv being the EXT2 ortholog.
- PAINT: the MF IBAs (GO:0008375, GO:0015020) come from PTN000869020 (donors include ttv
  itself FBgn0265974, mouse Ext1, human EXT1; GO:0008375 also EXTL1 Q92935). The Golgi IBA
  comes from a deeper EXT-family node PTN000115158 (donors include botv, sotv, ttv, EXT1,
  EXT2, EXTL3). Ttv appearing in its own donor list reflects its own experimental grounding.
- PAINT curators propagated only the generic parent MF terms, not the specific
  GlcNAcT-II/GlcAT-II terms; for Ttv the specific terms are directly IDA-supported, so the
  IBA rows are refined (MODIFY) rather than contradicted.

### What is experimentally established in Drosophila vs inferred

Established (Drosophila experiments on Ttv): GlcNAcT-II and GlcAT-II co-polymerase
activities (in vitro, IDA), activity enhanced in complex with Sotv, Ttv-Sotv complex and
co-localization, ER/Golgi localization, in vivo requirement for HS (not CS) synthesis,
glypicans as in vivo substrates, requirement for Hh/Dpp/Wg morphogen distribution.
Not established / explicitly absent: GlcNAcT-I chain initiation (absent in Ttv-Sotv).
Inferred only: Mn2+ cofactor (UniProt ECO:0000250 by similarity), heparin (as opposed to
heparan sulfate) biosynthesis (UniPathway mapping; Drosophila has no mast-cell heparin).
