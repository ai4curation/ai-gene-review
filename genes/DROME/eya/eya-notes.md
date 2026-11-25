# eya (eyes absent) - curation notes

Automated deep research was not available for this review (falcon 402, OpenAI 401), so no
`-deep-research-<provider>.md` file exists. Notes below are from cached publications and UniProt Q05201.

## Coactivator function
- [PMID:17714699 "Two members of this network, Eyes absent (EYA) and Sine oculis (SO), form a transcriptional complex in which EYA provides the transactivation function while SO provides the DNA binding activity."]
- [PMID:12917324 "We have mapped the transactivation potential of EYA to an internal proline-, serine-, and threonine-rich region"]
- Genomic rescue: [PMID:26980695 "a primary function of Eya during this process is transcriptional coactivation, while the phosphatase activity plays only a minor role."]
- Partners: So [PMID:9428512], Dac [PMID:9428513 "we show that the Dachshund and Eyes Absent proteins can physically interact through conserved domains"].

## Phosphatase
- [PMID:14628052 "Eyes absent is the prototype for a class of protein tyrosine phosphatases that use a nucleophilic aspartic acid in a metal-dependent reaction."]
- [PMID:14628053 "Eyes absent has intrinsic protein tyrosine phosphatase activity and can autocatalytically dephosphorylate itself."]
- But: [PMID:23554934 "We conclude that the tyrosine phosphatase activity of Eya is not required for normal eye development or survival in Drosophila."]
- Cytoplasmic role: [PMID:19217428 "Abl-mediated phosphorylation recruits Eya to the cytoplasm, where in vivo studies reveal a requirement for its phosphatase function."]
- Threonine phosphatase motif / immunity: PMID:22916150; TPM acts mainly as transactivation region in eye (PMID:26980695).

## Other roles
- Eye progenitor survival (PMID:8431945), ectopic eye induction (PMID:9428418), follicle cells (PMID:12403709), SGPs/gonad (PMID:21377458), testis cyst cells (PMID:12781687), somatic muscle downstream of Tinman (PMID:19217429), Ap neurons (PMID:26092715).

## Curation decisions
- response to light stimulus (PMID:17307880): cli-eya used as eyeless tool -> MARK_AS_OVER_ANNOTATED.
- salivary gland morphogenesis (PMID:16171793): abstract does not mention eya; likely indirect -> UNDECIDED.
- Module: GO:0003713 coactivator annoton fully supported. GO:0004725 PTP annoton is biochemically correct,
  but the in vivo eye role of the phosphatase is minor/dispensable (PMID:23554934, PMID:26980695); the
  mammalian phosphatase repression-to-activation switch (PMID:14628042) is not borne out by fly genomic rescue.
