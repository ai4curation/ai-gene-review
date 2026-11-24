# EPS8L2 (human, Q9H6S3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review (no prior review existed). ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon human EPS8L2 --fallback perplexity-lite` failed for both
providers: falcon returned `403 Forbidden` at the Edison auth endpoint ("Failed to
authenticate"), and the perplexity-lite fallback returned HTTP 401 `insufficient_quota`.
No deep-research file was produced. The review is built from the primary literature
cached in `publications/` (PubMed search `EPS8L2[tiab]`, 28 hits, triaged by title).

### Evolutionary grounding

- PANTHER PTHR12287 (EPS8 family) splits the four mammalian paralogs into separate
  subfamilies: EPS8 = SF21, EPS8L1 = SF19, EPS8L2 = SF20, EPS8L3 = SF22
  (`interpro/panther/PTHR12287/PTHR12287-entries.csv`). Human Q9H6S3, mouse Q99K30 and
  orangutan Q5RC07 are all SF20, so mouse Eps8l2 is a same-subfamily ortholog and its
  experimental findings can be transferred to human EPS8L2. Eps8 (SF21) data cannot be
  transferred as subfamily-specific function (e.g. Eps8's IRSp53-dependent bundling,
  MyoXVa-dependent tip targeting, stereocilia elongation).
- IBA rows come from PAINT nodes PTN000958212 (actin binding, plasma membrane, Rho
  signal transduction, regulation of Rho signalling) and PTN000264860 (ruffle membrane,
  positive regulation of ruffle assembly); donors are mouse Eps8 (MGI:104684), human
  EPS8L1 (Q8TE68) and EPS8L2 itself (Q9H6S3). EPS8L2 appearing in its own WITH/FROM is
  expected: it has its own experimental annotations from PMID:14565974.

### Experimental evidence in human EPS8L2 (PMID:14565974, Offenhauser et al. 2004)

Human EPS8L2 cDNA cloned from placenta; experiments used flag-tagged human EPS8L2 in
293T cells and in mouse fibroblasts / eps8-/- MEFs.
- Co-IPs with endogenous ABI1; under triple transfection forms ABI1-dependent complex
  with SOS1 [PMID:14565974 "all of the eps8 family members could be found in association with Abi1 and Sos-1"].
- Immunocomplexes show Rac-GEF activity (Abi1-dependent) [PMID:14565974 "Eps8-, eps8L1-, and eps8L2-, but not eps8L3-containing immunocomplexes displayed RacGEF activity"].
- C-terminal fragment binds native SOS1 in vitro.
- C-terminal fragment binds F-actin directly in co-sedimentation [PMID:14565974 "eps8, eps8L1, and L2, but not eps8L3 could directly associate to F-actin"].
- Localises to PDGF-induced F-actin-rich ruffles; rescues PDGF ruffling in eps8-/- MEFs,
  as efficiently as eps8 [PMID:14565974 "Notably, eps8L2 was as efficient as eps8"].

EPS8L2 itself is not a GEF: SOS1 is the catalytic subunit. GOA correctly uses
`contributes_to` for GO:0005085.

### Mouse Eps8l2 (Q99K30, same SF20) — PMID:23918390 (Furness et al. 2013)

- Localised at tips of cochlear and vestibular stereocilia, mostly middle/short rows;
  tip localisation independent of Eps8 and of MyoXVa.
- KO: late-onset progressive hearing loss, progressive loss of the hair bundle staircase,
  thinner intermediate stereocilia, reduced cuticular plate thickness. MET currents
  normal in immature hair cells. Double Eps8/Eps8l2 KO strongly enhances disorganisation.
- Mechanism not established: the paper speculates barbed-end capping or bundling, but
  notes Eps8L2 lacks IRSp53 binding and its hair-cell partners were unknown.
- BAIAP2L2 binds EPS8L2 as part of the "row 2" tip complex (PMID:34346063, abstract only).

### Human genetics

- DFNB106: homozygous frameshift c.1014delC (p.Ser339Alafs*15) in an Algerian family with
  childhood-onset progressive ARNSHL (PMID:26282398); novel frameshift in a Pakistani
  family (PMID:28281779); additional families, progressive / U-shaped audiograms, zebrafish
  eps8l2 expression in inner ear and pronephros (PMID:41514136). Dog EOAD in Rhodesian
  Ridgebacks with an in-frame EPS8L2 deletion (PMID:35385474).
- These support necessity of EPS8L2 for hearing; they do not show which step EPS8L2
  performs. Sensory perception of sound is retained as a non-core, organism-level term
  (it is an existing annotation, ISS/IEA from mouse); I did not add stereocilium
  maintenance (GO:0120045) as NEW: MGI curators annotated PMID:23918390 to localisation
  and sensory perception of sound but not to stereocilium maintenance/organisation, and
  the KO evidence is necessity evidence. Raised as a suggested question instead.

### Other reports (not used for annotation)

- Ctdnep1-Eps8L2 direct interaction and dorsal actin cables for nuclear positioning in
  migrating fibroblasts (PMID:33567288; species of construct not checked in detail;
  NIH3T3/U2OS). Not added as NEW.
- Colorectal cancer driver via YBX1/S6K1 (PMID:40783393) — cancer-cell overexpression
  phenotype, not a normal-function annotation.

### Decisions summary

- actin binding (IBA, IDA) -> MODIFY to actin filament binding (GO:0051015); co-sedimentation
  with F-actin. MGI already carries GO:0051015 ISO from the same paper on mouse.
- Rho protein signal transduction / regulation thereof -> MODIFY laterally to Rac protein
  signal transduction (GO:0016601) / positive regulation of Rac protein signal transduction
  (GO:0035022). Verified with OLS that GO:0016601 is not a descendant of GO:0007266 (the
  Rho term is now defined as Rho subfamily); the complex activates Rac.
- plasma membrane IBA -> MODIFY to ruffle membrane.
- stereocilium, stereocilium bundle -> MODIFY to stereocilium tip (part_of chain verified).
- 8x protein binding -> REMOVE (policy); ABI1 interaction is captured by GEF contributes_to.
- cadherin binding HDA -> MARK_AS_OVER_ANNOTATED.
- exosome/vesicle HDA, cytosol (HPA), cytoplasm, protein-containing complex -> KEEP_AS_NON_CORE.
