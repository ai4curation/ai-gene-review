# abp1 (P49777, SPBC1105.04c) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: abp1 is the closest experimentally characterised relative (same PANTHER subfamily
PTHR19303:SF73, co-donor of PAINT node PTN002712198) of SCHPO/cbh1. This is a de novo review
of Abp1 in its own right. No ProtNLM2 output was consulted.

### Provenance / process
- `just fetch-gene SCHPO abp1` (first attempt hit an EBI timeout; second succeeded). 18 seeded rows.
- `just deep-research-falcon SCHPO abp1 --fallback perplexity-lite` FAILED: Edison API
  "Failed to authenticate"; the perplexity-lite fallback timed out after 600 s. No deep-research
  file exists. Review is based on cached primary literature only.
- Additional papers located by PubMed esearch (abp1/cbh1/CENP-B + pombe) and cached with
  `just fetch-pmid`: 18094683, 21151105, 22907751, 26354768, 27345571, 12130537, 11238404,
  9237993, 17112379, 27343236.

### Evolutionary grounding
- Abp1, Cbh1 and Cbh2 are S. pombe CENP-B-like proteins from a single pogo-transposase
  domestication in the fission-yeast lineage, independent of mammalian CENP-B
  [PMID:17940212 "These data are consistent with a scenario whereby Abp1 , Cbh1 and Cbh2 arose from a single domestication event of a pogo -like transposase in the lineage of S."].
  No fungal orthologs outside Schizosaccharomyces
  [PMID:17940212 "Similarly, no ortholog of the fission yeast centromeric proteins was identified in any of the various fungal genomes currently available."].
- Consequence: nothing subfamily-specific should be transferred to Abp1 from human CENP-B,
  TIGD/POGK, or S. cerevisiae Pdc2 (which the IBA node also spans). Only family-generic
  properties (DNA binding, nucleus) are inherited at PTN002712198. All specific Abp1 functions
  below are experimentally established in S. pombe on Abp1 itself.

### Experimentally established in S. pombe (Abp1 itself)
- Sequence-specific dsDNA binding: purified as ARS3002/Maundrell-consensus binding protein,
  binds poly[d(A.T)] [PMID:8552670 "Abp1 preferentially binds to multiple sites in ARS 3002 and to the DNA polymer poly[d(A.T)]."].
- Centromeric DNA binding: cc2 central core sites [PMID:9024682 "Abp1p binds in vitro specifically to at least three sites in centromeric central core DNA of S. pombe chromosome II (cc2)."],
  Ks = 7e9 M-1 [PMID:10733588]. NMR structure of the N-terminal two DNA-binding domains (aa 1-141, PDB 1IUF)
  bound to a 21-bp recognition site [PMID:12018481].
- LTR motif: 10-bp AT-rich motif in LTRs [PMID:22907751].
- Chromatin location: centromeric heterochromatin and replication origins [PMID:11238404], mat silent
  region [PMID:18354497], Tf2 LTRs [PMID:18094683, PMID:21151105], rDNA [PMID:40132111, PMID:27345571],
  swi2 promoter in M cells [PMID:22042869, PMID:29610759].
- Recruitment (adaptor) activity: recruits class I/II HDACs to Tf2 [PMID:22907751, PMID:18094683];
  required for Mc localization at swi2 and LTRs [PMID:22042869]; recruits Cbh1 to LTRs (as summarised
  in PMID:21151105).
- Processes: Tf2 retrotransposon silencing and Tf body organisation [PMID:18094683, PMID:22907751];
  centromeric heterochromatin nucleation (Swi6 recruitment, H3 tail modifications) redundantly with
  Cbh1/Cbh2 [PMID:12130537]; donor selection in mating-type switching [PMID:18354497, PMID:22042869];
  replication fork progression through Sap1-blocked LTRs [PMID:21151105]; suppression of pervasive
  RNAPII transcription at Tf2 and rDNA [PMID:27345571]; preventing RNAi-dependent rDNA heterochromatin
  [PMID:40132111]; meiotic HR suppression at Tf2 [PMID:26354768]. Interacts with Mcm10/Cdc23 in Y2H,
  S-phase delay in null [PMID:17112379].
- Not required for imprint / MPS1 pausing at mat1 [PMID:29610759].
- No transposase/nuclease catalytic activity has been reported; the DDE region is needed for
  silencing [PMID:22907751] but no catalytic role is claimed.

### Decisions
- MF: core = GO:0019237 centromeric DNA binding (ACCEPT), GO:1990837 sequence-specific dsDNA
  binding (MODIFY target for generic DNA-binding rows), GO:0140463 chromatin-protein adaptor activity (ACCEPT).
- BP: donor selection and negative regulation of rDNA heterochromatin formation KEEP_AS_NON_CORE
  (experimental, real, but peripheral/regulatory). chromatin organization (IEA via adaptor activity)
  MODIFY -> GO:0031508 pericentric heterochromatin formation (Nakagawa 2002: CENP-Bs are
  "site-specific nucleation factors"; PomBase gives this term to many heterochromatin factors).
- NEW: GO:0010526 transposable element silencing. Participation test: Abp1 binds the LTR and
  recruits the HDACs that perform the deacetylation (adaptor/scaffold role, as with other
  DNA-binding recruiters); comparator: PomBase annotates Fft2/Fft3 (IMP) and Set1 (EXP) to this
  branch. Abp1 is the primary Tf2 silencing factor, so this is a gap rather than a deliberate omission.
  Did NOT add replication-fork terms or meiotic-recombination terms (indirect/genome-integrity
  phenotypes; raised as questions instead).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions (review file completed)

- Retried `just deep-research-falcon SCHPO abp1 --fallback perplexity-lite`: failed again (falcon,
  then perplexity-lite timeout at 600 s). No deep-research file; review rests on the 21 cached papers
  listed above (abstracts for most; full text for 22042869, 29610759, 29852001, 17940212, 21151105,
  27345571, 17112379, 27343236). No ProtNLM2 file was opened.
- `abp1-ai-review.yaml` written from the stub, all 18 GOA rows actioned, plus one NEW row:
  - ACCEPT: centromeric DNA binding (2x IDA), chromatin-protein adaptor activity (EXP), chromatin
    (EXP, IDA), condensed chromosome centromeric region (IC), nucleus (HDA, IBA, IEA).
  - MODIFY -> GO:1990837 sequence-specific dsDNA binding: nucleic acid binding (IEA), DNA binding
    (EXP NMR; IBA), sequence-specific DNA binding (IDA). The IBA row is sound (target is its own
    donor; Pdc2 co-donor is an independent domestication so only generic DNA binding is read across
    the node); recorded as propagation_review NO_FAILURE_CORE.
  - MODIFY chromatin organization (IEA) -> GO:0031508 pericentric heterochromatin formation and
    GO:0010526 transposable element silencing.
  - KEEP_AS_NON_CORE: donor selection (IDA 29852001, where Abp1 appears as synonym Cbp1; IMP
    18354497), mating-type region heterochromatin (IDA), negative regulation of rDNA heterochromatin
    formation (IMP; abstract-only, authors suggest an indirect route through RNAPII control).
  - NEW GO:0010526 transposable element silencing (IMP, PMID:18094683) as the one added process.
- Not annotated (deliberately): replication-fork progression through LTRs (21151105), meiotic HR
  suppression at Tf2 (26354768), S-phase timing / Mcm10 interaction (17112379), chromosome
  segregation phenotypes. These are genome-integrity or phenotypic outcomes, so they are raised as
  questions.
- Transfer note for cbh1: experimentally established on Abp1 in S. pombe = centromeric and
  sequence-specific dsDNA binding, chromatin adaptor (HDAC/Cbh1/Mc recruitment), Tf2 silencing,
  centromeric heterochromatin nucleation (redundant with Cbh1/Cbh2), donor selection. Only DNA binding
  and nucleus are phylogenetically inherited (PTN002712198); the rest is Abp1-specific experimental data.
- `just validate SCHPO abp1` and `just validate-goa SCHPO abp1` pass.
