# SEC23A (horse, Equus caballus) — A0A3Q2H5Z6

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ProtNLM2 benchmark target A0A3Q2H5Z6, horse partner (DONKEY40_HORSE_PARTNER) of donkey
SEC23A (genes/EQUAS/SEC23A, A0A9L0IQB9, reviewed by a separate agent). No ProtNLM2 file or
prediction-evidence folder was opened for this review.

### Setup
- Folder created with `just fetch-gene HORSE A0A3Q2H5Z6 --alias SEC23A`; stub id confirmed as A0A3Q2H5Z6.
- Deep research: `just deep-research-falcon HORSE SEC23A --fallback perplexity-lite` FAILED
  (falcon: Edison API `403 Forbidden` on /auth/login; perplexity-lite fallback timed out at 600 s).
  No deep-research file exists; the review uses cached literature read directly.

### Identity
- A0A3Q2H5Z6 (TrEMBL, Ensembl ENSECAP00000029229.1, VGNC:22789 SEC23A), 765 aa, five Sec23
  Pfam domains (zinc finger 58-98, trunk 126-390, beta-sandwich 401-504, helical 518-616,
  gelsolin-like 632-718).
- Global alignment to human SEC23A Q15436 (765 aa): gap-free, 99.3% identical (5 substitutions);
  to human SEC23B Q15437: 85% [file:HORSE/SEC23A/SEC23A-bioinformatics/RESULTS.md].
  Full-length canonical product; not an isoform, fragment or alternative gene model.
- PANTHER: PTHR11141:SF7 (PROTEIN TRANSPORT PROTEIN SEC23A), same subfamily as human/mouse/bovine/
  frog/zebrafish SEC23A (Swiss-Prot members in interpro/panther/PTHR11141/PTHR11141-entries.csv).
  Note: chicken Q5ZK03 "Sec23A" is placed in SF10 (SEC23B) in that file — a family-level oddity,
  not relevant to the horse placement.
- IBA rows derive from PTN000124617 (whole SEC23 clade; donors yeast Sec23, human SEC23A,
  fly Sec23, Arabidopsis, worm, trypanosome), so they encode functions ancestral to all SEC23s.

### Literature
- Sec23 is a GTPase-activating protein for Sar1 [PMID:8451644 "The isolated Sec23p subunit and
  the oligomeric complex stimulated guanosine triphosphatase (GTPase) activity of Sar1p 10- to
  15-fold"].
- Human SEC23A is the functional counterpart of yeast Sec23p (complements sec23-1), cytosolic in a
  ~350 kDa complex and localised to transitional ER and associated vesicles [PMID:8898360].
- CLSD F382L in SEC23A causes loss of function in budding assays, ER dilation, SEC31 mislocalisation
  [PMID:16980979]. Zebrafish morphant craniofacial phenotype is organismal; not used for process
  annotation.
- SEC23-SEC24 inner coat; SEC23 binds SAR1 and is its GAP; SEC23A and SEC23B largely
  interchangeable [PMID:36594468].

### Decisions
- Core: Sar1 GAP activity (GO:0005096), part of COPII vesicle coat, at ER exit sites, COPII
  budding / cargo loading / ER-to-Golgi transport.
- GO:0006886 intracellular protein transport -> MODIFY to GO:0006888 (not an ancestor; lateral
  refinement to the COPII process).
- GO:0012507 ER to Golgi transport vesicle membrane -> MODIFY to GO:0030127 (coat is part_of it).
- zinc ion binding: structural zinc finger, KEEP_AS_NON_CORE. cytosol: soluble pool, KEEP_AS_NON_CORE.

### Relative
- Closest characterised relative by phylogeny: human SEC23A Q15436 (same PANTHER subfamily SF7,
  PAINT donor for PTN000124617). No review exists in the repo (no genes/human/SEC23A).
