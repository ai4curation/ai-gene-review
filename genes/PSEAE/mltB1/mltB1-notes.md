# mltB1 (PA4444, Q9HVX3) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HVX3 --alias mltB1`; accession matches the worklist. No
deep-research provider was used.

### Literature

- Blackburn & Clarke 2002 (PMID:11790124, abstract only): of two P. aeruginosa MltB homologs expressed
  in E. coli with [3H]palmitate, only one was labelled; this lipoprotein was named MltB, and a truncated
  form lacking the first 17 residues including Cys17 (sMltB) was purified in soluble form.
  [PMID:11790124 "Both enzymes produced the same three major soluble products which were identified as anhydromuropeptides based on ESI-MS analysis"].
  PA4444 (Q9HVX3) has a lipobox with lipidated Cys17 (UniProt FT LIPID 17, PROSITE-ProRule PRU00303),
  matching the paper's Cys17; PA4001 has no lipobox. So MltB in the paper is PA4444 (MltB1).
- Legaree & Clarke 2008 (PMID:18708507): [PMID:18708507 "One, MltB, is a lipoprotein, whereas three other homologues are produced in soluble form"].

### Annotation decisions

- GO:0008933 IBA and IDA: ACCEPT. GO:0009253 IBA: ACCEPT.
- Action counts: ACCEPT 3. No source defects.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002410022 | GO:0008933 peptidoglycan lytic transglycosylase activity | 4 | 34 (18 taxa) | GO:0008933, IDA, PMID:11790124 (PseudoCAP) | SOUND | Abstract states purified sMltB (the palmitoylated Cys17 enzyme, = PA4444) releases anhydromuropeptides from insoluble PG. Node term suits the GH103 MltB-like clade. | E. coli MltB P41052; P. aeruginosa SltB1 Q9HX24 and SltB3 Q9HX28 (both also SOUND) | Yes |

Shared node with sltB1 and PA3992 (see `genes/PSEAE/sltB1/sltB1-notes.md`): all seeds SOUND, no
GO_CENTRAL defect.
