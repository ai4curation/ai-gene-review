# ampR (PA4109, P24734) notes

No deep-research provider was available. Literature: PMID:22479525 and PMID:16251297 (full text
cached and read); PMID:25182487 (abstract only).

## Biology

- Direct binding at PampC [PMID:25182487 "Gel shifts using membrane fractions showed that AmpR binds to
  PampC in vitro whereas in vivo binding was demonstrated using chromatin immunoprecipitation-quantitative
  PCR (ChIP-qPCR)."].
- Possible membrane association [PMID:25182487 "Alkaline phosphatase fusion and shaving experiments
  suggest that AmpR is likely to be membrane associated."].
- Regulon by mutant transcriptome [PMID:22479525 "Using DNA microarrays, we compared the expression
  profiles of PAO1 and PAOΔampR, without (uninduced) and with (induced) sub-MIC β-lactam stress to
  identify genes that are regulated under the different conditions"]; direct targets not determined
  [PMID:22479525 "Studies aimed at identifying the direct targets of AmpR are needed to identify genes
  that are directly regulated by AmpR"].
- Phenotypes: more biofilm [PMID:22479525 "over a period of 72 hours indicating that AmpR is a negative
  regulator of biofilm formation"]; less pyocyanin [PMID:22479525 "reduction in pyocyanin production by
  the ampR mutant, compared to PAO1"]. PMID:16251297 reported the opposite for pyocyanin and LasA.
- Consistency: ampD, ampDh2, ampDh3 and ampG (genes/PSEAE) are the peptidoglycan-recycling enzymes and
  permease whose muropeptides feed AmpR; none of those reviews assigns them regulation-of-transcription
  terms, which is consistent with AmpR being the only transcriptional component here.

### Annotation decisions

- GO:0003700 (IBA, IEA, IDA), GO:0006355 (IBA, IEA, IDA), GO:0005737 (IEA): ACCEPT.
- GO:0006351 (IDA, UniProt): MODIFY to GO:0006355.
- GO:0016020 (IEA, NAS), GO:0046677, GO:1900232, GO:1900378: KEEP_AS_NON_CORE.
- GO:0045862, GO:0050714 (PseudoCAP IMP): MARK_AS_OVER_ANNOTATED (gene-expression effects, probably
  indirect).
- Action counts: ACCEPT 7, MODIFY 1, KEEP_AS_NON_CORE 5, MARK_AS_OVER_ANNOTATED 2.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000794521 | GO:0006355 regulation of DNA-templated transcription | 6 | 174 (18 taxa) | GO:0006355, IDA, PMID:22479525 (PseudoCAP) | SOUND | Full text: the term is right (ampR deletion changes >500 transcripts; AmpR binds PampC per PMID:25182487), but the evidence is a mutant transcriptome, so IDA should be IMP (PSEUDOCAP WRONG_EVIDENCE_CODE, CONFIRMED). | trpI P11720 (SOUND), E. coli GcvA, TtdR, DmlR, PgrR | Yes; see the node record in genes/PSEAE/trpI/trpI-notes.md |

Node-level assessment for PTN000794521 is recorded once on trpI. No GO_CENTRAL defect.
