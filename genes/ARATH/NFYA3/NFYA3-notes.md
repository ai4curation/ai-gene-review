# NFYA3 review notes

## Session 1 (create review)

- fetch-gene resolved Q93ZH2 (NFYA3_ARATH, TAIR AT1G72830, GeneID 843614); 11 GOA rows.
- Literature work done manually (no deep-research API keys); see NFYA3-deep-research-manual.md.
- Key evidence: in vitro CCAAT binding as part of NF-Y trimer [PMID:22912760 "Figure 5B shows that an NF-Y complex was obtained with AtNF-YA3, AtNF-YA6, AtNF-YA8 and AtNF-YA9."];
  redundant requirement with NF-YA8 in early embryogenesis [PMID:24303077 "nf-ya3 nf-ya8 double mutants are embryo lethal"].
- Decisions: general MF/BP rows refined to the Pol II-specific terms already carried by IBA, DNA binding refined to
  GO:0000976 (in vitro only, so not the Pol II sequence-specific child), complex and nucleus rows accepted.
- Not proposed as NEW: embryo development (GO:0009793) and nutrient-response processes. The evidence is
  double-mutant lethality and expression/phenotype data; NF-YA3's role there is as a transcription factor whose
  targets are unknown, so this is recorded as a question rather than an annotation (CLAUDE.md NEW-term bar).
- Nuclear localization is inferred (UniProt ECO:0000305; AtSubP prediction); no GFP experiment found for NF-YA3.
