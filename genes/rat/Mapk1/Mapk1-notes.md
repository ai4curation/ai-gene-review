# Mapk1 (rat ERK2, UniProt P63086) notes

## Re-review 2026-10-10

### What GOA changed
- 20 new GOA rows were seeded as PENDING. 13 were donor-split or qualifier-split duplicates
  of already-reviewed rows (MAPK cascade, MAP kinase activity, protein serine/threonine
  kinase activity, nucleus, cytoplasm, cytosol x3, phosphatase binding, identical protein
  binding, positive regulation of smoothened signaling, ERK1 and ERK2 cascade), now
  transferred from human MAPK1 (UniProtKB:P28482) as well as mouse Mapk1 (MGI:1346858).
  The rest were new terms or evidence: positive regulation of skeletal muscle tissue
  regeneration (ISO, mouse IMP PMID:38198890 per QuickGO), regulation of intracellular pH
  (ISO; replaces the retired row for the obsolete GO:0030641 regulation of cellular pH),
  cellular response to toxic substance (IEA, ARBA00027337), and protein serine kinase
  activity (IEA ARBA/RHEA:17989, ISO and ISS from human MAPK1).
- 16 rows are now retired (no longer in GOA), including the IEA ERK1 and ERK2 cascade and
  protein serine kinase activity rows, several protein phosphorylation and
  peptidyl-serine phosphorylation rows, and two GO:0005515 rows (PMID:19200235,
  PMID:15781236). Their reviews are kept, with a sentence noting the retirement.

### Actions changed
- GO:0005515 protein binding (5 IPI rows), per the protein-binding policy (reconciled with
  PR #3381 on main). None of the papers supports a specific binding MF for generic protein
  binding on the ERK2 side.
  - DCC and beta-arrestin2: MODIFY, keeping PR #3381's replacements. DCC
    [PMID:21070949 "we report that ERK2 directly interacts with DCC"] becomes signaling
    receptor binding (GO:0005102). Beta-arrestin2 [PMID:19200235 "beta-arrestin2 interacted
    with both p-ERK and D1 DA receptor"] becomes scaffold protein binding (GO:0097110). The
    beta-arrestin2 row is retired in GOA, so its MODIFY is kept only as a record.
  - Cavin-4, DOC1R/CDK2AP2 and caveolin-2: MARK_AS_OVER_ANNOTATED -> REMOVE. Cavin-4
    [PMID:24567387 "MURC/Cavin-4 bound to α1A- and α1B-ARs as well as ERK1/2 in caveolae"],
    DOC1R [PMID:12944431 "Using the same screen, we identify another MAPK partner, DOC1R"]
    and caveolin-2 [PMID:15781236 "Direct interaction between ERK and caveolin-2 was
    confirmed by immunoprecipitation"] are each a substrate or scaffold partner. Removing
    these rows does not mean the interactions are false.
- kinase activity (ISO, TAS PMID:11687663) and protein kinase activity (IEA, ISO):
  MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0004707 MAP kinase activity. These terms are too
  general but do not overshoot the evidence, so the action enum calls for MODIFY.
- protein-containing complex (IDA PMID:15781236): MARK_AS_OVER_ANNOTATED ->
  KEEP_AS_NON_CORE. The co-IP with caveolin-2 does support complex membership, so the
  term is generic but not an over-reach.
- protein kinase binding (IPI PMID:16943189, with Prkg1 RGD:1587390): KEEP_AS_NON_CORE ->
  UNDECIDED. The cached record is abstract-only, and the abstract is about PKG I and
  TAB1-p38 MAPK with no mention of ERK2. The full text is needed.
- MAP kinase activity (IMP PMID:16955078): ACCEPT kept. The abstract (TBI/mTOR) does not
  describe the ERK2 assay, so the reason now records that this defers to the curator.

### Other re-audit changes
- Added `supported_by` to about 135 ACCEPT/KEEP_AS_NON_CORE rows that had none. The
  quotes come from the cited abstracts where they mention ERK2 (e.g. [PMID:7768935
  "serine 220 was phosphorylated by p42 MAP kinase in vitro"], [PMID:7889942 "is a
  nuclear target of two members of the MAP kinase family, ERK1 and ERK2"]) or else
  from current UniProt CC text.
- Replaced the weak deep-research quote ("NHE1 ... membrane scaffold") on the IBA
  cytoplasm and ISO cytosol rows with UniProt localization text.
- Description: removed the sentence about the gene being "annotated to a very large number"
  of processes and replaced it with biology.
- No stale UniProt `DR GO;` quotes were found. The checker reports 0 stale.

### Open questions
- PMID:16943189: is there a real ERK2-PKG I interaction (see the UNDECIDED row)?
- The diadenosine tetraphosphate biosynthetic process and positive regulation of protein
  import into nucleus IMP rows (PMID:19524539) record ERK2 acting through its substrate
  LysRS. They are kept as non-core in deference to the curator, but ERK2 does none of the
  Ap4A synthesis itself.
- The postsynaptic density row uses IEP for a cellular component (PMID:7478291), which is
  an unusual evidence code for a location.

- Reconciled with the protein-binding migration merged on main in PR #3381: the DCC and beta-arrestin2 IPI rows keep that PR's MODIFY calls (signaling receptor binding, scaffold protein binding); the other three GO:0005515 rows are REMOVE in both versions.

### Review follow-up 2026-10-17 (PR #4626)
- Two generic UniProt sentences had been added as `supported_by` across many unrelated
  rows: "the MAPK/ERK cascade mediates diverse biological functions..." (36 rows) and
  "other substrates are found in the cytosol..." (13 rows). Neither bears on any specific
  term, and the second describes where substrates are, not ERK2. They are removed. On
  cytoplasm/cytosol rows the support is now the UniProt localization note "PEA15-binding
  and phosphorylated DAPK1 promote its cytoplasmic retention". Mitochondrion rows have no
  ERK2-specific quote, so their support is dropped and `reason` carries the judgment.
- Removed other quotes that did not bear on their terms. These were the KIT-cascade
  sentence on IL-34, ERBB2-ERBB3 and ERBB signalling, the translation-regulator list on
  amino acid starvation, the cytoskeletal-substrate list on pseudopodium, and the
  apoptosis-regulator list on DNA damage response. Also removed was "the cascade exhibits
  versatile and dynamic subcellular distribution" (PMID:19565474) on process rows. On the
  CC TAS rows from PMID:19565474, "targets at distinct subcellular compartments" (about
  targets) was replaced by that paper's sentence about the cascade's own distribution.
  39 rows now have no `supported_by`, and `reason` carries the orthology/non-core
  judgment.
- Regulation of intracellular pH is now supported by the deep-research quote "ERK2
  phosphorylates NHE1" instead of the Ser727/Ser730 fragment.
- core_functions: the PMID:15027896 title quote was dropped from both core functions. So
  was the ATPγS negative-result quote, from core function 2 and the IEA ATP binding row.
  All three now cite the UniProt Rhea serine-kinase reaction line, which names ATP as
  substrate. The redundant ancestor GO:0000165 was removed from directly_involved_in.
- The retired beta-arrestin2 GO:0005515 row now carries the GOA-retirement sentence.
- PMID:16943189 now has `full_text_unavailable` and a `reference_review` (UNVERIFIED). The
  mouse donor papers PMID:12721286 and PMID:15284227 are not rat references of this file.
  They are named only in propagation_review prose, so they were not added as references.
