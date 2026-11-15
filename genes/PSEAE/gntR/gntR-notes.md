# gntR (PA2320, Q9I1F6) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I1F6 --alias gntR`; accession matches the worklist.
Swiss-Prot entry. No deep-research provider was used. Literature search: PubMed esearch was
unavailable (NCBI SOLR 500 errors) during the session; a Europe PMC query
(`GntR AND PA2320`) returned no further P. aeruginosa GntR papers. The only paper on this gene
product is the seed paper PMID:28752954 (abstract cached; full text not available).

### Literature

- PMID:28752954 (Daddaoua et al. 2017). GntR is a LacI-family regulator in PAO1:
  [PMID:28752954 "GntR repressed its own expression as well as that of the GntP gluconate
  permease."]; [PMID:28752954 "GntR was found to bind to promoters PgntR and PgntP"]; operator
  overlaps the RNA polymerase site; [PMID:28752954 "The release of promoter bound GntR is
  induced by gluconate and 6-phosphogluconate"]; GntR does not affect toxA; [PMID:28752954
  "GntR and PtxS are paralogous and may have evolved from a common ancestor."]
- UniProt FUNCTION text (ECO:0000269, PubMed:28752954) restates the above.

### Annotation decisions

- GO:0003700 (IBA, IDA seed): MODIFY to GO:0001217 DNA-binding transcription repressor activity.
- GO:0006355 (IBA, IEA): MODIFY to GO:0045892 negative regulation of DNA-templated transcription.
- GO:0000976 (IBA): ACCEPT. GO:0003677 (IEA): TOO_GENERAL.
- GO:0010906 regulation of glucose metabolic process (IMP): KEEP_AS_NON_CORE (gluconate uptake
  is a route of glucose catabolism in Pseudomonas; consequence of gntP repression).
- Action counts: ACCEPT 1, MODIFY 4, KEEP_AS_NON_CORE 1, TOO_GENERAL 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001248758 | GO:0003700 DNA-binding transcription factor activity | 11 | 219 (28 taxa) | GO:0003700, IDA, PMID:28752954 (PseudoCAP) | SOUND | Abstract states purified GntR binds PgntR/PgntP operators, effector release, and repression in vivo; DNA binding plus repression is direct TF evidence. Generic node term suits a LacI/GalR clade. | E. coli LacI, MalI, XylR, RbsR, PurR, AscG, TreR; B. subtilis CcpA; Shewanella NagR; P. aeruginosa PtxS | Yes |

Confidence note: abstract-only reading, but the abstract states the binding and repression data
outright, so the SOUND call does not depend on what the abstract omits.

PtxS (`genes/PSEAE/ptxS/ptxS-notes.md`) shares PTN001248758; the node-level verdict (all three
IBDs at this node stand, no GO_CENTRAL defect) is recorded there. No PSEUDOCAP or GO_CENTRAL
defect on gntR.
