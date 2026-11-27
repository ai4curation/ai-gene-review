# trpC (PA0651, P20577) review notes

Indole-3-glycerol phosphate synthase (IGPS, EC 4.1.1.48; HAMAP MF_00134_B, Pfam IGPS).
In P. aeruginosa TrpC is a monofunctional IGPS (no fused PRAI domain; 278 aa).

## Literature (no deep-research provider available; own reading)

- Gerth et al. 2012 (abstract only; no PMC full text): purified PaIGPS
  characterised [PMID:22555873 "PaIGPS was expressed heterologously in
  Escherichia coli, and purified with high yields."], with the highest turnover
  of any characterised IGPS [PMID:22555873 "has the highest turnover number of any
  characterized IGPS (k (cat) = 11.1 ± 0.1 s(-1))"]. A trpC deletion reduced
  fitness in synthetic CF sputum [PMID:22555873 "deleting the gene for PaIGPS
  reduces the fitness of P. aeruginosa strain PAO1 in synthetic cystic fibrosis
  sputum"].
- The PseudoCAP IMP for GO:0000162 is coded from the deletion; the abstract
  reports a fitness defect in sputum medium, not a tryptophan auxotrophy, so the
  IMP observation as stated in the abstract is indirect for the process. The
  process claim is nevertheless correct: the purified enzyme catalyses a step of
  tryptophan biosynthesis, which is direct participation (the enzyme does the
  work). The full text may report auxotrophy; not filed as a defect.
- PubMed MCP search returned API errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

Seed support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000523336 | GO:0004425 indole-3-glycerol-phosphate synthase activity | 4 | 126 (77 taxa) | GO:0004425, IDA, PMID:22555873 (PseudoCAP) | SOUND | Purified enzyme, kcat measured; direct evidence. | E. coli TrpC P00909 (IDA PMID:5332729), M. tuberculosis TrpC P9WFX7 (IDA x2), Arabidopsis IGPS P49572 (EXP) | Yes; three independent experimental seeds |
| PTN000523336 | GO:0000162 L-tryptophan biosynthetic process | 3 | 126 (77 taxa) | GO:0000162, IMP, PMID:22555873 (PseudoCAP) | SOUND | Term correct (the enzyme catalyses step 4/5 of Trp synthesis, shown in the same paper); the abstract's mutant phenotype is a sputum-fitness defect, so IDA from the enzyme assay would be the cleaner basis. | M. tuberculosis TrpC P9WFX7 (IDA x2), E. coli TrpC P00909 (IMP, acts_upstream_of_or_within) | Yes; M. tuberculosis IDA seeds suffice |

No PSEUDOCAP or GO_CENTRAL defect. IGPS is a single-reaction enzyme family; both terms suit the node.
