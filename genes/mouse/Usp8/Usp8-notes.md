# Usp8 (mouse, Q80U87) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This is a new review, written as the experimental reference for transfer to human USP8 (P40818).
ProtNLM2 output was not opened or used.

### Provenance and failures
- `just fetch-gene mouse Usp8` seeded 85 GOA rows and 17 references.
- `just deep-research-falcon mouse Usp8 --fallback perplexity-lite` FAILED. Falcon (Edison) returned
  "Failed to authenticate", and the perplexity-lite fallback returned HTTP 401 insufficient_quota.
  No deep-research file exists. This review uses the cached literature (abstracts, plus full text
  where available), the UniProt record and the local PAINT data only.
- I cached these extra papers: PMID:17452457, 20130268, 17121848, 17210635, 14661020, 26214742,
  34638628, 31845722, 41606310 and 42484147. PMID:42484147 expresses a human USP8 transgene in mouse;
  it was cached but is not cited.

### Evolutionary grounding
- PANTHER: PTHR21646:SF27 "UBIQUITIN CARBOXYL-TERMINAL HYDROLASE 8". Among the reviewed entries,
  only human USP8 (P40818) and mouse Usp8 (Q80U87) are in it
  (`interpro/panther/PTHR21646/PTHR21646-entries.csv`). This is a 1:1 orthology, so transfer of
  subfamily functions in either direction is justified.
- PAINT nodes (from `PTHR21646-paint.tsv`):
  - PTN002538135: cysteine-type deubiquitinase activity, regulation of protein stability (deep USP
    node, many seeds).
  - PTN008371010: cytosol and midbody (seeds mouse Usp8 and human USP8); postsynaptic density
    (seed rat Usp8 only).
  - PTN008578257: endosome organization and Ras protein signal transduction. The **only** seed is
    mouse Usp8 (MGI:1934029). The endosome organization IBA is well grounded (IMP plus knockout).
    The Ras IBA rests on one IPI/binding observation and is marked over-annotated.
  - PTN002728602 (Bilateria): positive regulation of canonical Wnt (Drosophila Usp8 and human USP8).
- PAINT did not propagate any acrosome/spermatid term from mouse Usp8 (the GOA set has only an IDA
  for acrosomal membrane, and no acrosome assembly process). I treat this as a deliberate omission
  and add no acrosome process term.

### What is experimentally established IN MOUSE (Usp8 protein or Usp8 mice)
- Cysteine-type deubiquitinase activity: in vitro EGFR [PMID:16120644] and Eps15 [PMID:16771824];
  testis enzyme acts on endogenous substrates [PMID:15342353]; C748 nucleophile mutants are inactive.
- Endosome membrane / early endosome; regulation of endosome morphology [PMID:16771824]. Knockout
  cells have enlarged early endosomes and reduced HRS and STAM2 [PMID:17452457].
- Knockout phenotypes: embryonic lethality; adult deletion causes liver failure and loss of EGFR,
  MET and ERBB3 [PMID:17452457]. These are phenotypes, not process terms.
- 14-3-3 binding via phospho-Ser680 inhibits activity and keeps the enzyme cytosolic; released in
  M phase [PMID:16944949 (embryonic mouse brain), PMID:17720156]. Added as NEW GO:0071889.
- SH3-binding motif PX(V/I)(D/N)RXXKP binds the STAM2/Hbp SH3 domain [PMID:10982817]. The protein
  binding row was modified to GO:0017124.
- Binds and stabilizes Nrdp1/RNF41 through the rhodanese and catalytic domains [PMID:15314180]. The
  protein binding row was modified to GO:0031625.
- Binds Ras-GRF1/CDC25(Mm), decreases its ubiquitination and extends its half-life [PMID:11500497].
- Spermatids: on the cytoplasmic face of the developing acrosome [PMID:15342353]; with ESCRT-0 and
  microtubules [PMID:20130268]. The latter is associative only. I did NOT add microtubule binding
  or acrosome assembly; both are recorded as suggested questions.
- Tissue-specific knockouts: T cells [PMID:26214742], osteoprogenitors with FZD5 stabilization
  against lysosomal degradation [PMID:34638628], endothelium/angiogenesis with VEGFR2 in endosome
  aggregates [PMID:41606310]. All are phenotypes; only the FZD5 mechanism is used, as support for the
  Wnt and lysosomal-catabolism rows.

### Inferred only (from human or rat orthologs)
- K48/K63 linkage specificity (human IDA); plasma membrane (human); midbody and cytokinesis (human
  PMID:18388320, also MGI IDA); BACE1/amyloid and lysosomal catabolism (human); postsynaptic density,
  glutamatergic synapse, postsynaptic protein catabolism and NGF response (rat RGD:1304979).

### Data issue found
- The MGI IPI row (GO:0007265, PMID:11500497) has WITH/FROM PR:P48967, which resolves in UniProt to
  Cdc25C (M-phase inducer phosphatase 3). The paper describes CDC25(Mm), which is Ras-GRF1, so this
  looks like a name collision. Raised in suggested_questions.

### Actions summary
- Protein binding: STAM2 → SH3 domain binding; RNF41 (mouse and human) → ubiquitin protein ligase
  binding; STAM1, GRB2, DNAJB3, EGFR and EPS15 removed as uninformative (the interactions are not
  disputed).
- MARK_AS_OVER_ANNOTATED: Ras protein signal transduction (IBA and IPI), cellular response to
  dexamethasone, positive regulation of amyloid fibril formation, cellular response to NGF.
- Core: cysteine-type deubiquitinase activity at endosomes and cytosol (protein deubiquitination,
  endosome organization); regulation of protein stability; 14-3-3 binding; SH3 domain binding.
