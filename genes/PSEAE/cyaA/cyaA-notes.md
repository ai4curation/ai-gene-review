# cyaA (PA5272, Q9HTS8) review notes

Class I adenylate cyclase (Pfam PF01295 Adenylate_cycl; IPR000274; PANTHER
PTHR38760), 950 aa, four class I domains (UniProt FT DOMAIN 21..217 "Adenylate
cyclase class-I N-terminal", second, third and fourth regions).

## Literature (no deep-research provider available; own reading, 2026-11-05)

- Wolfgang et al. 2003 (abstract only; Dev Cell, not in PMC): microarray study
  of the TTSS regulon; mutants unable to make cAMP were profiled
  [PMID:12586068 "Transcriptome analysis of mutants lacking the ability to
  synthesize cAMP or the cAMP binding protein Vfr"]. The abstract does not name
  cyaA; the PseudoCAP IMP rows for cyaA likely come from the cyaA cyaB double
  mutant, which I could not check.
- Topal et al. 2012 (full text, PMC3269522): P. aeruginosa has three ACs
  [PMID:22226839 "The two other P. aeruginosa ACs, CyaA and CyaB, belong to
  Class I and III, respectively."]; CyaB dominates [PMID:22226839 "CyaB
  activity indeed accounts for the majority of intracellular cAMP"]; "As yet,
  the role of P. aeruginosa CyaA is unknown."
- PubMed MCP and NCBI eutils returned errors on 2026-11-05; a Europe PMC search
  ("cyaA" AND "cyaB" AND aeruginosa) found no CyaA-focused biochemical paper.
- E. coli CyaA (P00936), the other node seed: GO:0004016 IDA PMID:6300054 and
  GO:0006171 IMP PMID:4310317 (EcoCyc), checked in QuickGO 2026-11-05.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002215143 | GO:0004016 adenylate cyclase activity | 2 | 7 (7 taxa) | GO:0004016, IMP, PMID:12586068 (PseudoCAP) | UNVERIFIABLE | Abstract only; it does not separate cyaA from cyaB. The term is right for the gene (class I catalytic domain). | E. coli CyaA P00936 (IDA PMID:6300054) | Yes; the E. coli IDA seed is sufficient and the clade is class I ACs |
| PTN002215143 | GO:0006171 cAMP biosynthetic process | 2 | 7 (7 taxa) | GO:0006171, IMP, PMID:12586068 (PseudoCAP) | UNVERIFIABLE | As above. | E. coli CyaA P00936 (IMP PMID:4310317) | Yes |

No PSEUDOCAP or GO_CENTRAL defect: the rows are probably right, and the node
terms suit a class I AC clade. This is a different node from cyaB's
(PTN002454020, class III), so the two reviews do not share a node; both call
their PseudoCAP rows correct for the gene. The GO:0006171 IBD (dated
2026-06-16) has not yet reached this gene's GOA file.
