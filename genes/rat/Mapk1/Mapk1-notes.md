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
- GO:0005515 protein binding (5 IPI rows): MARK_AS_OVER_ANNOTATED -> REMOVE, per the
  protein-binding policy. None of the papers supports a specific binding MF on the ERK2
  side; each partner is a substrate or scaffold: DCC [PMID:21070949 "we report that ERK2
  directly interacts with DCC"], Cavin-4 [PMID:24567387 "MURC/Cavin-4 bound to α1A- and
  α1B-ARs as well as ERK1/2 in caveolae"], DOC1R/CDK2AP2 [PMID:12944431 "Using the same
  screen, we identify another MAPK partner, DOC1R"], beta-arrestin2 [PMID:19200235
  "beta-arrestin2 interacted with both p-ERK and D1 DA receptor"] and caveolin-2
  [PMID:15781236 "Direct interaction between ERK and caveolin-2 was confirmed by
  immunoprecipitation"]. Removing these rows does not mean the interactions are false.
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
