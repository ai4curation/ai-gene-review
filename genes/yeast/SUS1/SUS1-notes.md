# SUS1 (YBR111W-A, Q6WNK7) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: SUS1 is the experimentally best-characterised member of the ENY2/Sus1 family
(PANTHER PTHR12514, no subfamily split assigned to Q6WNK7, Q7LL15 or Q9NPA8). It is the
main experimental donor (SGD:S000028510) of the IBA rows propagated from PAINT node
PTN000282153, so this review records which functions are experimentally established in
*S. cerevisiae* itself. ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon yeast SUS1 --fallback perplexity-lite` failed: falcon raised
"Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (insufficient
quota). No deep-research file was produced; this review uses the cached primary literature
(publications/) and the curated UniProt entry.

### Evidence summary (yeast experiments)

- Identification; dual membership of SAGA and Sac3-Thp1 (TREX-2); concentrated at nuclear
  pores; required for transcription regulation and mRNA export
  [PMID:14718168 "Sus1 is a nuclear protein with a concentration at the nuclear pores."]
  [PMID:14718168 "mRNA export is impaired in sus1 mutants"].
- TREX-2: the Sac3 CID helix recruits Sus1 and Cdc31 [PMID:15311284]; crystal structure of
  Sac3CID:Sus1(x2):Cdc31; Sus1 required for NPC targeting of the CID
  [PMID:19328066 "Moreover, the CID motif is targeted to NPCs, and Sus1 is necessary for this targeting."].
- Gene gating: Sus1, Ada2 and Sac3 confine activated GAL genes to the nuclear envelope
  [PMID:16760982]; Sus1-Sac3-Thp1 needed for post-transcriptional tethering of genes and
  mRNA dots [PMID:18003937].
- DUB module: Sus1 binds SAGA via Ubp8/Sgf11 and is required for H2B deubiquitination
  [PMID:16855026 "We demonstrate that Sus1 is involved in the SAGA-dependent histone H2B deubiquitinylation and maintenance of normal H3 methylation levels."];
  Ubp8 activation needs Sgf73-ZnF and Sgf11-Sus1 [PMID:18488019]; crystal structures show
  Sus1 clamping the Sgf11 N-terminal helix onto the Ubp8 ZnF-UBP domain [PMID:20434206,
  PMID:20395473, PMID:20007317]; all four subunits required for active complex
  [PMID:20395473 "active complex formation requires the presence of all four DUBm subunits"].
  Sus1 is noncatalytic: it is an activating/assembly subunit, not the DUB itself.
- Separation-of-function alleles sus1-10/-12 (lose TREX-2, keep SAGA) and sus1-11 (lose both)
  [PMID:19269973].
- Elongation: Sus1 associates with Ser5/Ser2-phosphorylated Pol II and coding regions
  [PMID:18923079]; TREX-2 mutants show elongation/R-loop genome instability [PMID:18667528].
- Genome-wide: Sus1 occupies UASs of many genes; sus1 deletion alters synthesis and
  stability of many transcripts [PMID:29598828].
- Cell wall stress: Sus1 recruited to CWI genes via Slt2/Rlm1/SWI-SNF/SAGA; needed for PIC
  assembly and H3/nucleosome eviction, independent of Ubp8 and additive with gcn5
  [PMID:42047951].
- Cytoplasmic P-body/stress granule localisation was seen on Sus1 overexpression; genetic
  interactions with LSM1/PAT1 [PMID:20230609]. Treated as non-core.

### Evolutionary grounding

All IBA rows (SAGA complex, DUBm complex, TREX-2, poly(A)+ mRNA export, transcription
coactivator activity, regulation of transcription by Pol II) come from PTN000282153, with
SUS1 itself among the donors, so for this gene they restate yeast experimental findings.
PAINT did not propagate enzyme activator activity, chromatin binding, nuclear pore or the
stress/nucleosome terms; those rest only on yeast data here and should not be transferred
to orthologs without their own evidence. GO:0016578 histone deubiquitination is obsolete
(it was an MF disguised as a BP), so the DUB-module role is expressed as
GO:0035800 deubiquitinase activator activity (is_a GO:0008047, verified via OLS ancestors).

### Decisions (summary)

- 14 GO:0005515 protein binding rows: REMOVE (uninformative; the Sac3, Sgf11, Cdc31 and Tra1
  interactions are real and are captured by complex membership).
- enzyme activator activity -> MODIFY to deubiquitinase activator activity.
- regulation of transcription by RNA polymerase II / positive regulation of DNA-templated
  transcription -> MODIFY to positive regulation of transcription by RNA polymerase II.
- mRNA export from nucleus -> MODIFY to poly(A)+ mRNA export from nucleus.
- nucleus -> MODIFY to nucleoplasm / nuclear pore; cytoplasm -> MODIFY to P-body (non-core).
- regulation of protein localization -> MODIFY to protein localization to nuclear pore.
- cellular response to stress -> MODIFY to cellular response to cell wall damage
  (GO:1990394; the evidence is Congo red cell wall stress).
- nucleosome organization, chromatin binding, nuclear mRNA surveillance, transcription
  elongation: KEEP_AS_NON_CORE.
