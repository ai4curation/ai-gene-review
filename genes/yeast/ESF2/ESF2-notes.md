# ESF2 (YNR054C, P53743) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ESF2 is the experimental donor (SGD:S000005337) behind PAINT node
PTN000267771 in PANTHER PTHR12311:SF7, the subfamily that also contains human ABT1
(Q9ULW3) and fly CG32706 (Q8IRM9) (`interpro/panther/PTHR12311/PTHR12311-entries.csv`).
This review was written without consulting any ProtNLM2 output.

### Deep research

`just deep-research-falcon yeast ESF2 --fallback perplexity-lite` failed: Edison/falcon
returned `403 Forbidden` at authentication, and the perplexity fallback returned
`401 insufficient_quota`. No deep-research file exists. The review is based on the
cached primary literature (all GOA-cited PMIDs cached by `just fetch-gene-pmids`) and
the UniProt record.

### What is experimentally established in S. cerevisiae

- **Required for early pre-rRNA cleavages A0, A1, A2 and 18S synthesis** (Tet-shutoff
  depletion; pulse-chase, Northern, primer extension). [PMID:15964808 "Esf2p-depleted
  cells are defective for pre-rRNA processing at the early nucleolar cleavage sites A 0
  through A 2 and consequently are inhibited for 18S rRNA synthesis"]. 27S/25S/5.8S
  pathways not affected.
- **Required for SSU processome assembly and compaction** (Miller chromatin spreads):
  fewer terminal knobs, delayed, loose not compact; no cotranscriptional cleavage.
  [PMID:15964808 "in the absence of Esf2p, terminal knob deposition and SSU processome
  assembly upon nascent rRNA are kinetically delayed and that once assembled, the SSU
  processomes fail to rearrange into a compact structure"]
- **Component of 90S preribosome / SSU processome (accessory, transient)**: TAP
  co-purifies UTPs, Esf1, helicases Has1, Dbp4/Hca4, Dbp8; co-sediments with 90S and
  with 5'ETS particles; not in pre-40S. Authors call it "a novel accessory component of
  the SSU processome" and "not a core constituent of the U3 RNP".
- **Nucleolar** (Esf2-eGFP "unambiguously restricted to the nucleolus"; the
  high-throughput GFP screen PMID:14562095 additionally reported minor cytoplasm, which
  Hoang et al. explicitly failed to reproduce).
- **RNA binding**: in vivo associated with 5'ETS fragments, U3 and other box C/D snoRNAs
  (snoRNA association likely indirect via Nop1); in vitro GST-Esf2 binds rRNA fragments
  (5'ETS, 18S, 25S) "albeit likely without any apparent sequence specificity"
  [PMID:16772403].
- **ATPase activator of the DEAD-box helicase Dbp8**: direct binding (Y2H, GST pull-down
  with recombinant proteins, co-IP); Esf2 lowers Km(ATP) of Dbp8 from 194 to 86 uM and
  raises kcat 17 to 52 min-1; C-terminal region (206-317) required for Dbp8 binding,
  stimulation and viability; RRM deletion also lethal [PMID:16772403].
- Essential gene.
- Interactions from large-scale screens: Esf1, Dbp8, Has1, Hca4 (PMID:29054886 Y2H matrix +
  co-IP; PMID:37968396; PMID:14690591; PMID:11805837). These underlie the GO:0005515 rows.

### Not established

- No intrinsic catalytic (nuclease or ATPase) activity: GST-Esf2 alone shows background
  ATP hydrolysis only. Esf2 does not perform the endonucleolytic cleavages; it is an
  assembly/cofactor component of the processome that does.
- Mouse ABT1 was reported to bind TBP and activate basal transcription; Hoang et al. and
  large-scale studies did not find yeast Esf2-TBP association. No yeast evidence for
  transcription roles.
- Mechanism of compaction defect (primary assembly vs U3 release) unresolved by the authors.

### Evolutionary grounding for transfer

- ESF2, human ABT1 and fly CG32706 are all in PTHR12311:SF7 (single subfamily).
- PAINT node PTN000267771 (donor SGD:S000005337) propagates: RNA binding, nucleolus
  (is_active_in), A0/A1/A2 cleavage terms (GO:0000480, GO:0000472, GO:0000447), and
  SSU processome assembly (GO:0034462). These are the IBA terms seen on both ESF2 and
  fly CG32706 (fly GOA file).
- **PAINT did not propagate GO:0001671 ATPase activator activity**, although yeast has an
  IDA for it. Treat this as a deliberate curator decision: the Dbp8-specific cofactor
  activity is established only in yeast and should not be transferred to orthologs
  without independent evidence (e.g. conservation of the C-terminal Dbp8-binding region and
  a test against the Dbp8 ortholog, human DDX49).

### Decisions

- Cleavage terms (IMP + IBA): ACCEPT. GO convention annotates SSU processome components
  to the A0-A2 cleavage processes; Esf2 contributes to the structural assembly/compaction of
  the RNP machine that performs the cleavages (participation by structure), not as
  nuclease. Core function framed as processome assembly.
- GO:0034462 IMP + IBA: ACCEPT (core).
- GO:0001671 IDA: ACCEPT (core MF in yeast).
- RNA binding IDA + IBA: ACCEPT (no sequence specificity shown, so RNA binding is as
  precise as warranted). nucleic acid binding IEA: TOO_GENERAL.
- Nucleolus (HDA/IDA/IBA/IEA): ACCEPT.
- Cytoplasm HDA: REMOVE — directly contradicted by the dedicated GFP re-examination and
  absence from pre-40S particles.
- 10 GO:0005515 rows: REMOVE per protein-binding policy; the informative Dbp8 interaction
  is captured by GO:0001671 IDA.
- NEW: GO:0032040 small-subunit processome (IDA, PMID:15964808) — component claim
  directly supported by TAP, gradients and the authors' conclusion.
