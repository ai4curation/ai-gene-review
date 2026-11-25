# flbB (Aspergillus nidulans) — curation notes

UniProt C8VBM8 (FLBB_EMENI). bZIP transcription factor; upstream developmental
activator. Upstream-activation tier of the module.

- bZIP TF controlling asexual development; binds DNA (IDA); dual hyphal-tip and
  nuclear localization. [PMID:17993569 "Basic-zipper-type transcription factor FlbB controls asexual development in Aspergillus nidulans"]; [PMID:19656299 "The bZIP-type transcription factor FlbB regulates distinct morphogenetic stages of colony formation in Aspergillus nidulans"].
- Associates with FlbE at the hyphal tip [PMID:19007409]. Core MF GO:0003700; all
  annotations ACCEPT.

## Re-review 2026-10-01 (GOA refresh)

- No new GOA rows and no vanished rows for flbB in the refreshed snapshot.
- Judgments unchanged. Added verbatim supporting quotes (PMID:17993569, PMID:21423749)
  to eight ACCEPT rows that previously lacked supported_by (conidium formation,
  positive regulation of conidium formation, hyphal tip, nucleus, DNA-binding TF
  activity, regulation of transcription by RNA polymerase II).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: flbB is the closest experimentally characterised relative of
NEUCR/NCU07379, and its experimental findings will serve as the reference for
transfer. This review keeps experimental (A. nidulans) facts separate from inferred
ones. ProtNLM2 output was not consulted.

**Deep research:** `just deep-research-falcon EMENI flbB --fallback perplexity-lite`
failed. Falcon raised "Failed to authenticate" and perplexity returned HTTP 401
(insufficient quota). No deep-research file was written. The review rests on cached
literature: six GOA PMIDs plus three newly cached papers (PMID:26256571,
PMID:25701285, PMID:31065746), found by a PubMed search for "FlbB AND Aspergillus".

### Evolutionary grounding
- UniProt places flbB in PANTHER PTHR40621:SF6 (AP-1-like TF YAP1-related). The
  repository phylogeny (file:NEUCR/NCU07379/NCU07379-bioinformatics/RESULTS-rereview.md)
  splits SF6 into a FlbB clade {FlbB, NCU07379, MGG_00342, CCM_01128, Sordaria}
  and a Yap1/NapA clade, each with 100% bootstrap support.
- The IBA donors (S. pombe Pap1, S. cerevisiae Yap1 and its paralogs, C. albicans
  Cap1) all belong to the Yap1 clade. The IBAs come from PTN008082960, the
  ancestor of both clades, and carry only generic bZIP terms (cis-regulatory
  binding, Pol II activator, Pol II TF complex). PAINT did not propagate the
  donors' oxidative-stress terms to this node. That omission is treated as
  deliberate, and no stress-response process is added for FlbB.
- PMID:21423749 lists 40 Pezizomycotina FlbB orthologs, NCU07379 among them, and
  reports that the NCU07379 knockout "conidiates normally" [PMID:21423749 "This
  mutant conidiates normally."]. The conidiation role is therefore experimentally
  established only in A. nidulans (and other Aspergillus species). It should not be
  transferred to Sordariomycetes without species-specific evidence.

### Experimentally established in A. nidulans
- bZIP TF needed for brlA expression; the null is fluffy and aconidial
  [PMID:17993569 "no brlA expression was detected in the flbB -null mutant"].
- Activates flbD, then FlbB and FlbD jointly activate brlA [PMID:20132447 "Both
  factors then jointly activate brlA"]. The ΔflbB RNA-seq confirms that FlbB
  activates flbD and brlA [PMID:25701285].
- ChIP: FlbB binds the brlA promoter, and needs FlbD to do so [PMID:31065746
  "chromatin immunoprecipitation assays showed that FlbB cannot bind brlA p in the
  absence of FlbD"].
- Localizes to the hyphal tip (needs FlbE, Cys382 and the bZIP domain) and to
  nuclei (needs a bipartite NLS; dynein-dependent retrograde transport;
  accumulation needs FlbD) [PMID:26256571; PMID:31065746].
- The C382A point mutant is fluffy [PMID:21423749 "flbB-C382A exhibited a fluffy
  phenotype with sparse conidiation"]. This confirms that PMID:21423749 contains
  genuine IMP evidence, not only bioinformatics.
- Other phenotypes (branching, osmotic autolysis, the dba cluster, urdA and sexual
  repression) are downstream or pleiotropic. No process terms were added for them.

### Inferred, not experimental
- Pol II specificity and activator sign are inferred: the targets are
  protein-coding genes and the effect is activation. No reporter assay of an
  activation domain is cited.
- The binding motif is unknown. The ChIP shows promoter occupancy, so the DNA
  binding term was refined only to GO:0000976, not to a sequence-specific child.
- The Pol II regulator complex (IBA) has no direct evidence and is kept as non-core.

### Action changes from the previous version
- GO:0003700 (IEA/ISM/IDA) → MODIFY to GO:0001228. GO:0006355 and GO:0006357
  (IMP/ISM/IDA) → MODIFY to GO:0045944. GO:0003677 IDA → MODIFY to GO:0000976.
  These terms are correct but general, and the gene already carries the specific
  descendants.
- Core MF changed from GO:0003700 to GO:0001228. Core processes are now GO:0045944
  and GO:0075307 (conidium formation itself is left out of the core: FlbB regulates
  it and does not execute it).
- Quotes added for every row. Three references added. The previous description was
  replaced with a fuller, project-independent summary.
