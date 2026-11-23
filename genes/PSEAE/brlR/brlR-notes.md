# brlR (PA4878, Q9HUT5) review notes

No deep-research provider was available. Sources: UniProt record, cached
publications (PMID:23935054 and PMID:24612375 full text; PMID:22730129 abstract
only, PMC full text not returned by the PubMed MCP).

## Function

- MerR-family regulator required for biofilm drug tolerance [PMID:22730129 "the
  transcriptional regulator BrlR, a member of the MerR family of multidrug transport
  activators, plays a role in the high-level drug tolerance of biofilms"].
- Represses oprH-phoPQ; EMSA on the oprH promoter [PMID:23935054 "our findings
  indicate that BrlR is involved in transcriptional regulation of the oprH-phoPQ
  operon, acting as a repressor"].
- Binds own promoter and c-di-GMP [PMID:24612375 "BrlR binds to its own promoter";
  "BrlR was found to bind c-di-GMP in vitro at a ratio of one c-di-GMP per two
  BrlR"]. Added as NEW GO:0035438 cyclic-di-GMP binding (IDA).
- Activates mexAB-oprM, mexEF-oprN and ABC transporters by direct promoter binding
  (UniProt FUNCTION, PubMed:23687276, 24612375, 29180529).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001575588 | GO:0006355 regulation of DNA-templated transcription | 9 | 114 (31 taxa) | GO:0045892 negative regulation of DNA-templated transcription, IDA, PMID:23935054 (PseudoCAP) | SOUND | Full text read: EMSA with tagged BrlR on the oprH-phoPQ promoter plus qRT-PCR; direct evidence of BrlR's own repressor activity. | E. coli CueR P0A9G4, ZntR P0ACS5, BluR P75989; Xanthomonas SoxR Q8P6Y4; M. tuberculosis HspR O06302; B. subtilis TnrA Q45666; S. coelicolor HspR P40183; PAO1 CueR Q9HV30 | Yes. No GO_CENTRAL defect. |
| PTN001575588 | same | 9 | 114 | GO:0045893 positive regulation of DNA-templated transcription, IDA, PMID:22730129 (PseudoCAP) | UNVERIFIABLE (claim true) | Abstract only: it reports genetics and drug tolerance and does not describe the direct assay an IDA implies, but the full text may. The positive-regulation claim is independently well supported (direct activation of mex operons, PMID:24612375 and UniProt). No defect raised. | as above | Yes. No GO_CENTRAL defect. |

Node shared with cueR (PA4778), whose seed is also SOUND; neither gene needs a
node-level defect, and the node term (generic regulation of transcription) suits a
MerR clade containing both activators and repressors. BrlR also seeds the
GO:0003700 IBD at this node (not a PseudoCAP-supported seeding in the worklist).

PseudoCAP defects from this gene: none.
