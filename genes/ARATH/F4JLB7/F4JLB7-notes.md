# F4JLB7 notes

## 2026-10-14 — UNDECIDED rows resolved (ARATH corpus project, PR #5024)

Three experimental rows from PMID:11752391 (RIC7: protein binding IPI, pollen tube
growth IMP, apical plasma membrane IDA) were set to REMOVE as attributed to the
wrong locus. The basis is sequence evidence, not the abstract's gene focus:

- The published RIC7 cloning primers map to the adjacent, oppositely oriented CRIB
  locus AT4G28556 (UniProtKB:Q1G3K8), not to F4JLB7; see
  `genes/ARATH/Q1G3K8/Q1G3K8-bioinformatics/RESULTS.md`.
- F4JLB7 has no CRIB motif, which the paper reports as required for Rop1 binding.
- The function is not lost: the Q1G3K8 review already carries ROP binding, pollen
  tube growth and plasma membrane from PMID:11752391.

The remapping should be reported to TAIR curators. The chloroplast ISM row was also
removed (contradicted by the signal peptide, LRR receptor architecture and accepted
plasma-membrane IBA).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** F4JLB7 (450 aa, sequence version 1 since 2011) is the only UniProt
entry for AT4G28560 (UniProt search for "AT4G28560", 2026-10-20, returned F4JLB7
plus an A. lyrata entry). It is the canonical product of its locus, not a fragment,
isoform or alternative gene model. The "RIC7" SubName/gene name is a symbol collision
with the adjacent CRIB locus AT4G28556 (Q1G3K8, reviewed separately in
genes/ARATH/Q1G3K8/). A positively controlled CRIB scan finds no CRIB motif in F4JLB7
(F4JLB7-bioinformatics/RESULTS-rereview.md).

**Deep research.** The falcon report is about the CRIB RIC7 (ROP2-RIC7-Exo70B1 guard
cell pathway). It wrongly asserts that F4JLB7 has a CRIB domain, so none of it is used.
It is recorded in references with relevance NONE.

**Phylogeny (PANTHER 19.0 API, 2026-10-20).** F4JLB7 is the only Arabidopsis member of
PTHR48004:SF38 ("ROP-INTERACTIVE CRIB MOTIF-CONTAINING PROTEIN 7", named after this
locus). The frozen UniProt record says SF58, which the family review also records as an
SF58/SF38 conflict. Both sources agree on the parent family PTHR48004. In the
Arabidopsis-pruned tree F4JLB7 is sister to the TMM (Q9SSD1) + RLP29 (Q9SJH6) clade
(SF42, node PTN008481374). That clade is sister to the PII-2 clade (SF55), and CLV2
(SF9) is in the other major clade. Closest characterised relative: TMM, a paralog in a
different subfamily. TMM-specific functions (EPF recognition, stomatal patterning) are
not transferred.

**PAINT.** Node PTN008274137 (family root in the PAINT release) carries plasma
membrane (seeds CLV2, TMM, PII-2, AT4G28560) and signaling receptor activity (seed CLV2
only). The curator propagated only those two broad terms and not coreceptor activity,
peptide recognition or developmental processes, and I treat that as deliberate. The
AT4G28560 PM seed may itself derive from the wrong-gene apical-PM IDA. The node does not
depend on it.

**C terminus.** F4JLB7 ends in a hydrophobic segment (431-449) with one residue after
it, like TMM. That fits either a TM anchor or a GPI signal. TAIR's two TAS "membrane"
rows cite the Borner 2002/2003 GPI-anchored-protein papers. Both are abstract-only in
the cache, and full text could not be retrieved from Europe PMC, so At4g28560's
inclusion is unverified.

**Action changes vs previous version:**
- The three `membrane` rows (IEA, 2x TAS): KEEP_AS_NON_CORE -> MODIFY to plasma
  membrane (GO:0005886), because a correct but general term is refined.
- The PM IBA, signaling receptor activity IBA and signal transduction IC stay ACCEPT,
  with reasons rewritten on phylogenetic grounds. The IC's GO:0005515 basis is noted as
  unusable.
- The chloroplast ISM REMOVE and the three PMID:11752391 wrong-gene REMOVEs are kept
  unchanged. They rest on primer-mapping evidence plus the absence of a CRIB motif.
- The description and core function were rewritten, questions and experiments were
  added, and status was set to COMPLETE.

Modules: none contain F4JLB7. modules/stomatal_lineage_development.yaml includes the
paralog TMM only.
