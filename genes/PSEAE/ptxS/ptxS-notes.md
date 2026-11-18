# ptxS (PA2259, G3XD97) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE G3XD97 --alias ptxS`; accession matches the worklist.
No deep-research provider was used. PubMed esearch was unavailable (NCBI SOLR errors); Europe
PMC searches were used. The cited papers are cached: PMID:22844393 (full text, PMC3402500,
read), PMID:10438759 (full text cached; abstract read), PMID:10894751 (abstract only).

### Literature

- PMID:22844393 (Daddaoua et al. 2012): [PMID:22844393 "PtxS operates as a repressor that binds
  to the -10 region of the target promoters and occludes RNA polymerase access"]; PtxS regulates
  its own promoter and Pkgu/Pgad in response to 2-ketogluconate; PtxS does not bind PtoxA but
  [PMID:22844393 "In vitro, PtxS recognises PtxR with nanomolar affinity, but this interaction
  does not occur in the presence of 2-ketogluconate, the specific effector of PtxS."]; DNA loop
  between PtxS and PtxR operators at Pkgu/Pgad.
- PMID:10438759 (Swanson et al. 1999): PtxS-dependent gel shift of a 52-bp ptxS upstream
  fragment, lost in PAO1::ptxS and restored by complementation; ptxS-lacZ 4-5 fold higher in
  the mutant; negative autoregulation.
- PMID:10894751 (Swanson and Hamood 2000): 14-bp palindrome TGAAACCGGTTTCA is the PtxS operator;
  [PMID:10894751 "PtxS binding was eliminated upon the deletion of the 14-bp palindromic sequence
  from the 52-bp fragment."]

### Annotation decisions

- GO:0045892 (IDA, seed), GO:0001217 (IEA, IPI x3, IMP), GO:0000976 (IBA, IEA, IPI x3, IMP): ACCEPT.
- GO:0003700 (IBA), GO:0006355 (IBA, IEA), GO:0003677 (IEA): TOO_GENERAL (entailed by GO:0001217,
  GO:0045892, GO:0000976).
- GO:0032993 protein-DNA complex (IEA, IPI x3, IMP): KEEP_AS_NON_CORE (CollecTF convention).
- NEW GO:0140297 DNA-binding transcription factor binding (IDA, PMID:22844393): PtxS-PtxR
  binding by ITC is how PtxS controls toxA.
- Action counts: ACCEPT 12, TOO_GENERAL 4, KEEP_AS_NON_CORE 5, NEW 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001248758 | GO:0006355 regulation of DNA-templated transcription | 19 | 219 (28 taxa) | GO:0045892, IDA, PMID:22844393 (PseudoCAP) | SOUND | Full text read: DNaseI footprints of PtxS at Pkgu/Pgad, repression in lacZ fusions in the deletion. Generic node term suits the LacI/GalR clade. | 18 others incl. E. coli LacI, PurR, RbsR, MalI, CytR (P0ACP1/P0ACN7 etc.), B. subtilis CcpA, Shewanella NagR | Yes |

PtxS also appears in the WITH/FROM of the GO:0003700 and GO:0000976 IBDs at the same node.

Node-level verdict for PTN001248758 (shared with gntR, `genes/PSEAE/gntR/gntR-notes.md`): all
three IBDs (GO:0003700, GO:0000976, GO:0006355) rest on many experimentally characterised
LacI/GalR repressors and suit the clade. No GO_CENTRAL defect; no PSEUDOCAP defect on ptxS.
