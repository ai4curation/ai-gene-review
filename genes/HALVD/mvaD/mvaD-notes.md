# mvaD (HVO_1412, UniProt D4GXZ3) - Haloferax volcanii DS2

## 2026-11-18 review notes

### Literature search

No deep-research provider was available in this session, so no deep-research file exists.
Searches run (NCBI E-utilities PubMed; Europe PMC search was returning HTTP 503):

- `Haloferax[tiab] AND (mevalonate[tiab] OR isoprenoid[tiab] OR isopentenyl[tiab])` (17 hits)
- `"phosphomevalonate decarboxylase"[tiab] OR "mevalonate phosphate decarboxylase"[tiab] OR
  "mevalonate 5-phosphate decarboxylase"[tiab] OR "monophosphate decarboxylase"[tiab] AND
  mevalonate` (11 hits)
- `PTO1356 OR Ta0893 OR SSO2989 OR HVO_1412 OR "HVO 1412"` (1 hit: PMID:24375100)

Only one primary paper assays this protein: PMID:24375100 (VanNice et al. 2014). The cached
copy is abstract-only (PMC full text publisher-restricted; Europe PMC full-text service
returned HTTP 500). Kinetic values below are from the curated UniProt record, which cites
that paper with ECO:0000269. No genetic (knockout) study of HVO_1412 was found.

### Reaction

- HVO_1412 is phosphomevalonate decarboxylase (PMD; EC 4.1.1.99; RHEA:40955):
  (R)-5-phosphomevalonate + ATP = isopentenyl phosphate + ADP + CO2 + phosphate.
  [PMID:24375100 "It catalyzes the synthesis of isopentenyl phosphate from mevalonate
  monophosphate, a reaction that has been proposed but never demonstrated by direct
  experimental proof, which is provided in this account."]
- Substrate is the 5-monophosphate, not the 5-diphosphate: strong inhibition by
  6-fluoromevalonate 5-phosphate, negligible by 6-fluoromevalonate 5-diphosphate.
  [PMID:24375100 "exhibits strong inhibition by 6-fluoromevalonate monophosphate but negligible
  inhibition by 6-fluoromevalonate diphosphate (a potent inhibitor of the classical mevalonate
  pathway), reinforcing its selectivity for monophosphorylated ligands."]
- ATP-dependent: Km ATP 289 uM; Km (R)-MVAP 75 uM; kcat 3.5 s-1; pH optimum ~7.5 (UniProt
  D4GXZ3, ECO:0000269 PubMed:24375100).
- Mechanism (by analogy, not shown for this enzyme): ATP phosphorylates the C3 hydroxyl, then
  the 3-phosphate leaves with decarboxylation of C1. [PMID:24375100 "Inhibition by the
  fluorinated analog also suggests that the PMD utilizes a reaction mechanism similar to that
  demonstrated for the classical MVA pathway decarboxylase."] The two-step mechanism of the
  related R. castenholzii enzyme (MMD/MPD) was shown by its activity on mevalonate
  3,5-bisphosphate [PMID:28004831 "we show that MMD from Roseiflexus castenholzii can accept its
  intermediate, mevalonate 3,5-bisphosphate, and carry out the second step of its dual function
  independently of the first step."]
- Downstream partner: isopentenyl phosphate kinase HVO_2762 [PMID:24375100 "one enzyme is an
  isopentenyl phosphate kinase that forms isopentenyl diphosphate (in a reaction analogous to that
  of Methanococcus jannaschii MJ0044)"].

### Phylogeny and family context

- Haloarchaeal MDD-annotated proteins cluster with the Chloroflexi MPD and carry MPD-like active
  sites [PMID:24327557 "archaeal MDDs from Haloarchaea and Thermoplasmata contain MPD-like active
  site residues associated with MVAP (3) binding and turnover and their protein sequences cluster
  with the MPD from Chloroflexi (Table 4)"]. Haloarchaea encode IPK but no PMK
  [PMID:24327557 "the two archaeal classes that also encode an IPK but no PMK, the Haloarchaea
  and Thermoplasmata classes"].
- PANTHER PTHR10977:SF3 member by HMM. Not a leaf of the PANTHER 19 tree. Its UniRef50
  cluster-mate Halobacterium salinarum VNG_0593G (Q9HRQ4) sits in node PTN004212759 with
  Chloroflexus aurantiacus A9WEU8, outside the PAINT IBD node PTN000104601
  (`mvaD-bioinformatics/RESULTS.md`). No IBA reaches D4GXZ3 in GOA.
- Q9HRQ4 (unreviewed, H. salinarum) is named "Diphosphomevalonate decarboxylase (EC 4.1.1.33)" and
  carries GO:0004163 IEA via IPR029765 + UniRule UR001995844 + EC 4.1.1.33. Given that it shares a
  UniRef50 cluster with the biochemically confirmed H. volcanii PMD, this is a probable
  misannotation (PMD vs DMD), consistent with [PMID:38674651 "haloarchaea-type
  phosphomevalonate decarboxylase (PMD) and eukaryote-type diphosphomevalonate decarboxylase
  (DMD) are often misannotated in the automated annotation workflow"]. Not this gene; reported to
  the coordinator, not recorded as a source defect here.

### Annotation decisions

| Term | Evidence | Action | Note |
|---|---|---|---|
| GO:0090710 phosphomevalonate decarboxylase activity | IEA (EC/Rhea) | ACCEPT | core MF |
| GO:0016831 carboxy-lyase activity | IEA (IPR005935) | TOO_GENERAL | family spans 3 reactions; row evidence cannot select one, so not MODIFY |
| GO:0008299 isoprenoid biosynthetic process | IEA (IPR005935) | ACCEPT | broad but informative |
| GO:0019287 IPP biosynthesis, mevalonate pathway | IDA PMID:24375100 | NEW | definition is "via the intermediate mevalonate", covers the alternate route |

No CC annotation exists and none was added: there is no localization study for this protein.
