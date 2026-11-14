# speH (PA4773, Q9HV35) review notes

No deep-research provider was available. Sources: UniProt Q9HV35 (Swiss-Prot, HAMAP MF_00464),
cached PMID:22155771 (abstract only; the PubMed MCP returned the PMC record with an empty body).
Europe PMC / PubMed searches did not find a PA4773-specific biochemical study.

## Function

- Prokaryotic class 1a AdoMetDC, pyruvoyl-dependent, self-processing proenzyme
  [file:PSEAE/speH/speH-uniprot.txt "Catalyzes the decarboxylation of S-adenosylmethionine to S-adenosylmethioninamine (dcAdoMet)"].
- PA4773-PA4775 are DNA/Mg2+-limitation-induced speD/speE homologs [PMID:22155771 "annotated as homologs of the spermidine
  synthesis genes speD (PA4773) and speE"]; the mutant phenotypes in the abstract are for PA4774 [PMID:22155771 "Mutation of PA4774"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002140323 | GO:0004014 adenosylmethionine decarboxylase activity | 4 | 29 (20 taxa) | GO:0004014, IMP, PMID:22155771 (PseudoCAP) | UNVERIFIABLE | The term is right for SpeH (HAMAP, active-site Ser73), but the abstract reports only a PA4774 (speE2) mutant and no decarboxylase assay; a PA4773 experiment may be in the full text, which could not be read. PSEUDOCAP defect OTHER/CHECK, SUSPECTED. | E. coli SpeD (P0A7F6), S. solfataricus SpeD (Q9UWY8), M. jannaschii (Q57763) | Yes; E. coli SpeD is the characterised prototype. No GO_CENTRAL defect. |

## Consistency with speE2

speE2 (PA4774) cites the same paper and its seed was judged SOUND because the mutant described is
PA4774 itself. That is consistent with this review: the same abstract names no PA4773 mutant, so the
speH IMP cannot be verified from it. The two genes are on different PAINT nodes (speE2 PTN000168372;
speH PTN002140323); there is no shared node.
