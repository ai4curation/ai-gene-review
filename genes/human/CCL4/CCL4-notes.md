# CCL4 (MIP-1-beta) curation notes

## Session 2026-10-05

### Sources consulted
- UniProt P13236 (`CCL4-uniprot.txt`)
- Cached publications (abstracts unless noted): PMID:2462251, PMID:2521882, PMID:8525373,
  PMID:8699119, PMID:12070155, PMID:10540332, PMID:9521068, PMID:10383387, PMID:10679098,
  PMID:10841574, PMID:10929056, PMID:20959807, PMID:7545673, PMID:9558100, PMID:9743377,
  PMID:9759849; HuRI/CCSB interactome papers PMID:25416956, PMID:31515488, PMID:32296183 (full text).
- Deep research: `just deep-research-falcon human CCL4` launched in parallel at the start of the
  session (see status note at the end of this file).
- QuickGO comparator check of CCL3 (P10147) and CCL5 (P13501) annotation sets.

### Identity and structure
- Secreted CC chemokine, 92 aa precursor with signal peptide 1-23; mature chain 24-92; a
  naturally N-terminally truncated form MIP-1-beta(3-69) (chain 26-92) is generated after
  secretion [file:human/CCL4/CCL4-uniprot.txt "N-terminal processed form MIP-1-beta(3-69) is produced by
  proteolytic cleavage after secretion from peripheral blood lymphocytes."].
- Originally cloned as an activation-induced T-cell gene (Act-2, pAT 744)
  [PMID:2462251 "Using a baculovirus expression system, we have shown that this
  gene encodes a secreted product."]; [PMID:2521882 "The predicted peptides encoded by these two clones feature hydrophobic N-terminal
  leaders characteristic of secreted proteins."].
- Forms homodimers and heterodimers with CCL3; both MIP-1 chemokines polymerise into
  rod-shaped double-helical polymers [PMID:20959807 "Our crystal structures
  reveal that MIP-1 aggregation is a polymerization process and human MIP-1α and
  MIP-1β form rod-shaped, double-helical polymers."]. Polymerization buries
  receptor-binding sites and protects from IDE degradation of monomers.

### Receptors
- CCR5 is the principal receptor: MIP-1alpha, MIP-1beta and RANTES are potent CCR5 agonists
  with pertussis-toxin-sensitive Ca2+ flux [PMID:8699119 "Macrophage inflammatory protein-1alpha
  (MIP-1alpha), MIP-1beta, and RANTES were all potent agonists for CC CKR5 (EC50 =
  3-30 nM) when calcium flux was measured in transfected HEK 293 cells"].
- CCR5 extracellular disulfides required for MIP-1beta binding [PMID:10383387 "All cysteine mutants were unable to bind
  detectable levels of MIP-1beta"].
- Full-length CCL4 binds CCR1 poorly [PMID:7545673 "MCP1 and MIP1 beta had very
  limited capacity to compete for MCP3 binding on YT4/293 cells"], but the natural truncated
  MIP-1beta(3-69) gains CCR1 and CCR2b agonism [PMID:12070155 "unlike the full-length protein, it also triggers a
  Ca(2+) response via CCR1 and CCR2b"].
- CCR8: initial report of MIP-1beta as a CCR8 ligand [PMID:9521068] was not reproduced
  [PMID:10540332 "TARC and MIP-1beta
  did not bind to or induce chemotaxis through CCR8"]; UniProt CAUTION concurs.
- Atypical/scavenger receptor ACKR2 binds inflammatory CC chemokines (Reactome R-HSA-443986).

### HIV suppression
- One of the three major CD8+ T-cell HIV-suppressive factors [PMID:8525373 "The chemokines RANTES,
  MIP-1 alpha, and MIP-1 beta were identified as the major HIV-SF produced by CD8+
  T cells."]. Mechanism is ligand-mediated occupancy/down-modulation of the CCR5 coreceptor,
  i.e. blocking viral entry [PMID:12070155 "MIP-1 beta(3-69) retains the abilities to induce
  down-modulation of surface expression of the chemokine receptor CCR5 and to
  inhibit the CCR5-mediated entry of HIV-1 in T cells."]; thymocyte infection by R5 virus
  inhibited by MIP-1beta [PMID:9743377].
- HIV-2-infected individuals: beta-chemokine-mediated resistance to R5 HIV-1 [PMID:10841574].
  GOA has "host-mediated suppression of viral transcription" (GO:0043922) and "response to
  toxic substance" (GO:0009636) from this paper for CCL3, CCL4 and CCL5 alike. The mechanism is
  coreceptor-level entry blockade, not transcriptional; "toxic substance" has no basis in the
  abstract (full text not available in cache or via PMC MCP - returned empty).

### Cellular effects
- Chemotaxis/activation of monocytes, T cells, NK cells via CCR5; regulates NK polarization
  [PMID:9759849], CD44-dependent T-cell adhesion to hyaluronan [PMID:10929056 "chemokines (e.g. MIP-1beta, interleukin-8, and RANTES)"].
- CCR5 expression absent from eosinophils and neutrophils [PMID:8699119 "CC CKR5
  mRNA was detected constitutively in primary adherent monocytes but not in
  primary neutrophils or eosinophils"] - argues against eosinophil chemotaxis IBA being a
  core CCL4 function.

### Interactome rows
- 19 GO:0005515 IPI rows from CCSB Y2H screens (HuRI etc.), partners nearly all multi-pass
  membrane proteins (SLC30A2, SLC30A8, SLC7A1, CNR2, GPRC5D, TAS2R5, TMEM proteins...). No
  biological context; CCL4 is secreted. Per protein-binding policy: REMOVE (uninformative).

### Comparator check (QuickGO)
- CCL3 and CCL5 carry the same 10841574-derived GO:0043922 and GO:0009636; neither carries
  GO:0046597. Proposed MODIFY replacement GO:0046597 host-mediated suppression of symbiont
  invasion for the HIV-related process rows - CCL4 itself performs the step (occupies / triggers
  internalization of the CCR5 coreceptor), so this passes the participation test.

### Deep research status
- See bottom of file (updated after falcon job completion).

### Deep research outcome (falcon)
**Superseded (see 2026-10-05 reconciliation below): the falcon job did eventually complete late and
`CCL4-deep-research-falcon.md` now exists.** Original status note follows.

`just deep-research-falcon human CCL4` was launched in parallel with publication caching at the
start of the session and **failed**: the Edison/falcon API returned `429 Too Many Requests` and the
provider then timed out after 600 s ("Provider falcon exited with code 1 / All providers failed").
No `CCL4-deep-research-falcon.md` was produced. No perplexity key is configured, so no fallback was
possible. The review was therefore built from the UniProt record, the cached publications listed
above (several fetched during this session with `just fetch-pmid`), the PubMed MCP (PMC full text
for PMID:10841574 returned empty), OLS/QuickGO term lookups, and a QuickGO comparator check against
CCL3 and CCL5.

## Reconciliation with late falcon deep research (2026-10-05)

The falcon job completed after the review had been drafted (report end time 2026-10-05T01:31,
~30 min run), producing `CCL4-deep-research-falcon.md`. It was read in full and compared with the
review and these notes.

- **No contradictions.** The report's central claims - secreted CC chemokine acting extracellularly
  as a CCR5 agonist; natural MIP-1-beta(3-69) proteoform retaining CCR5 activity and gaining CCR1 and
  CCR2b responses; CCR5 down-modulation and blockade of R5 HIV-1 entry; one of three CD8+ T-cell
  HIV-suppressive factors; MIP-1 rod-shaped polymers - all match what the review already asserts
  from cached primary papers (PMID:12070155, PMID:8525373, PMID:20959807, PMID:8699119).
- **Additional material, not acted on:** (i) CD26/DPP4 identified as the protease generating
  MIP-1-beta(3-69) (Guan et al. 2004, J Cell Biochem; not cached, not independently verified here) -
  this is a property of DPP4 (the enzyme performs the step), so it does not change any CCL4
  annotation; (ii) rapid CCL4 secretion by target-activated NK cells (Fauriat 2010) - expression
  context only; (iii) mouse tumour (CD103+ DC recruitment) and cutaneous leishmaniasis/CCR5 models
  and 2024 disease-association studies - the report itself notes these do not isolate CCL4 from
  CCL3/CCL5 and are not grounds for new process annotations.
- The report does not address the PMID:10841574 GO:0043922 / GO:0009636 rows, so they stay UNDECIDED.
- Actions: added the falcon report to `references` (reference_review UNVERIFIED, not used as sole
  evidence) and set review `status: COMPLETE`. No annotation actions changed.
