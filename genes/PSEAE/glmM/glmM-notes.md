# glmM (PA4749, Q9HV50) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HV50 --alias glmM`; accession matches the worklist.
No deep-research provider was used; PubMed esearch unavailable. Seed paper PMID:10913078 full
text (PMC94616) cached and read.

### Literature

- PMID:10913078 (Tavares et al. 2000): PA4749 (ORF540) encodes GlmM; it complements an E. coli
  glmM thermosensitive mutant; His6-GlmM purified, specific activity similar to E. coli GlmM;
  [PMID:10913078 "Beside its phosphoglucosamine mutase activity, the P. aeruginosa enzyme is
  shown to exhibit phosphomannomutase and phosphoglucomutase activities, which represent about 20
  and 2% of its GlmM activity, respectively."]; [PMID:10913078 "when plasmid pIT352 was
  introduced by triparental mating into the algC mutant strain P. aeruginosa 8858, alginate
  synthesis was not restored"]. AlgC is the dedicated PMM/PGM of P. aeruginosa.

### Annotation decisions

- GO:0008966 (IBA, IDA seed, IEA), GO:0009252 (IBA, IDA seed, IEA), GO:0006048 (IBA),
  GO:0005829 (IBA), GO:0000287 (IEA): ACCEPT.
- GO:0004615 PMM (IBA, IDA seed, IEA): KEEP_AS_NON_CORE (genuine 20% secondary activity,
  conserved in E. coli GlmM, but not the evolved function; does not replace AlgC).
- GO:0004614 PGM (IDA, IEA): MARK_AS_OVER_ANNOTATED (2% side activity; AlgC dedicated).
- GO:0005975 (IEA): MODIFY to GO:0006048. GO:0016868 (IEA): TOO_GENERAL.
- Action counts: ACCEPT 9, KEEP_AS_NON_CORE 3, MARK_AS_OVER_ANNOTATED 2, MODIFY 1, TOO_GENERAL 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001096974 | GO:0004615 phosphomannomutase activity | 2 | 136 (85 taxa) | GO:0004615, IDA, PMID:10913078 (PseudoCAP) | SOUND | Measured on purified enzyme (20% of GlmM activity). It is a secondary activity, so the GlmM rows are kept as non-core, but the row faithfully records the assay. | T. kodakarensis PGM/PMM Q68BJ6 (bifunctional; UniProt now places it in PTHR43771) | Yes: the deep node includes bona fide PMMs (ManB, RfbK, Pmm) and Q68BJ6; GlmM leaves (30 of 136) retain a measurable PMM side activity. Placement is arguable (suggested question), no defect. |
| PTN000501735 | GO:0008966 phosphoglucosamine mutase activity | 2 | 38 (36 taxa) | GO:0008966, IDA, PMID:10913078 (PseudoCAP) | SOUND | Purified enzyme activity plus complementation of E. coli glmM. | E. coli GlmM P31120 | Yes |
| PTN000501735 | GO:0009252 peptidoglycan biosynthetic process | 2 | 32 (31 taxa) | GO:0009252, IDA, PMID:10913078 (PseudoCAP) | SOUND | Restores peptidoglycan synthesis in the E. coli mutant; the enzyme catalyses a precursor step (evidence is complementation, nearer IGI than IDA, but the claim is right). | E. coli GlmM P31120 | Yes |

No PSEUDOCAP or GO_CENTRAL defect on glmM.
