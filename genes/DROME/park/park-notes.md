# park review notes

## Session 1 (initial review)

- `just fetch-gene DROME park` resolved Q7KTX7 (PRKN_DROME, FlyBase FBgn0041100, GeneID 40336);
  GOA has 87 rows, all on Q7KTX7. PMID:22219196 fetched and read (GstO1 rescue of parkin
  mutants; parkin is the genetic background, so it informs phenotypes only).
- No deep-research provider; literature synthesis is in `park-deep-research-manual.md`.

### Key decisions

- Core MF: GO:0061630 ubiquitin protein ligase activity (RBR E3; catalytic Cys449
  [PMID:23770917]). The IEA GO:0004842 row is MODIFIED to it.
- Core BP: mitophagy / type 2 mitophagy, protein mono- and polyubiquitination of OMM
  substrates (Marf, Porin), negative regulation of mitochondrial fusion via Marf turnover.
- Mitochondrial fission IGI rows (PMID:18230723): parkin does not execute fission; the paper
  concludes the pathway "promotes" fission, and PMID:18799731 says parkin is not a core fission
  component. MODIFY to GO:0090141 and record a WRONG_TERM source defect.
- GO:1901526 positive regulation of mitophagy IMP from PMID:28435104: the full text (cached)
  assays memory, circadian rhythm and clock-neuron electrophysiology, not mitophagy. The claim is
  true for parkin from other papers, so the row is accepted on the claim but a WRONG_REFERENCE
  source defect is recorded.
- Mitochondrion (root organelle): IDA rows accepted. No NEW OMM row: parkin recruitment to the
  outer membrane is transient and stimulus-dependent (the ORGANELLES policy says transient
  recruitment is not an outer-membrane location).
- ER and Golgi IBA rows (PTN000188399, seeded only by mammalian PRKN): no fly evidence;
  MARK_AS_OVER_ANNOTATED. Ubiquitin ligase complex IBA (PTN000188395, RBR family node seeded by
  ARIH1/ARIH2/pdr-1/PRKN): the stable complex membership is an Ariadne/CRL property; parkin acts
  as a monomer with transient E2s; MARK_AS_OVER_ANNOTATED.
- ARBA GO:0022603 regulation of anatomical structure morphogenesis: no biological basis in fly;
  REMOVE. Other ARBA broad terms MODIFIED to the specific terms the gene carries.
- Phenotype-only BP rows (spermatogenesis, oogenesis, locomotory behaviour, neuron cellular
  homeostasis, JNK, oxidative stress) kept as non-core; locomotor rhythm and neuronal action
  potential (PMID:28435104) and eye pigmentation (PMID:19692353) marked as over-annotations.
- Many experimental papers are abstract-only (17456438, 16002472, 18799731, 18957282 etc.);
  experimental rows from these were not removed.
