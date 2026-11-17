# pvdD (PA2399, Q9I182) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I182 --alias pvdD`; accession matches the
worklist. Unreviewed TrEMBL entry. No deep-research provider was used. NCBI
E-utilities, Europe PMC and the PubMed MCP search were unavailable (errors/503);
the PMC copy of PMID:12700264 returned no body text. All three seed papers were
read as abstracts.

### Literature

- Two NRPS modules (C-A-PCP x2) plus a C-terminal thioesterase (PF00975), PTHR45527.
- [PMID:15271355 "PvdD, a nonribosomal peptide synthetase (NRPS) of Pseudomonas aeruginosa PAO1, incorporates two L-threonines into the siderophore pyoverdine."]
- [PMID:15271355 "A pvdD mutant did not synthesize pyoverdine and lacked a high Mr iron-regulated cytoplasmic protein (IRCP)."]
- [PMID:12700264 "L-Threonine, one of the amino acid residues in pyoverdine(PAO), was an effective substrate for the recombinant protein in ATP-PP(i) exchange assays, showing that PvdD has peptide synthetase activity."]
  The abstract describes only the purified first module, no mutant.
- [PMID:9770291 "lasR mutants were not altered with respect to expression of the pvdD gene involved in the synthesis of the peptide portion of pyoverdine"]
  pvdD is an expression read-out in this quorum-sensing paper.

### Decisions

- ACCEPT: pyoverdine biosynthetic process (IMP x3; two with defects), cytosol
  (IBA), phosphopantetheine binding (IBA, IEA).
- MODIFY: catalytic activity (IMP x3, IEA) -> GO:1904091 non-ribosomal peptide
  synthetase activity; obsolete GO:0043041 (IBA, IEA) -> GO:0002049.
- TOO_GENERAL: cytoplasm (IBA), secondary metabolite biosynthetic process (IBA, IEA).
- Counts: ACCEPT 6, MODIFY 6, TOO_GENERAL 3.

## PseudoCAP IBA-seed assessment

PTN002378821 is a broad NRPS node (72 leaf IBAs, 22 taxa) with 13 seeds; PvdD and
PvdJ (genes/PSEAE/pvdJ) are the two PAO1 seeds. The node-level assessment is
recorded here, on the gene with the most direct evidence; pvdJ cross-references it.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002378821 | GO:0044550 secondary metabolite biosynthetic process | 13 | 72 (22 taxa) | GO:0002049, IMP, PMID:15271355 (PseudoCAP) | SOUND | pvdD mutant makes no pyoverdine and is complemented; PvdD is the NRPS that incorporates two L-Thr, so it does part of the work. Pyoverdine biosynthesis is_a the node term. | E. coli EntF (P11454), S. pombe SPAC23G3.02c, Aspergillus NRPSs (Q4WYG2, Q5BFS3, Q4WMJ7, C8VPS9, Q4WR82, Q4WLW8, Q4WAW3, Q4WF53), M. tuberculosis P9WQ63, PvdJ (Q9I181) | Yes; eleven non-Pseudomonas NRPS seeds |
| PTN002378821 | same | 13 | 72 | GO:0002049, IMP, PMID:12700264 (PseudoCAP) | SOUND | Term right (purified module activates L-Thr, a pyoverdine residue); evidence should be IDA, not IMP (PSEUDOCAP WRONG_EVIDENCE_CODE, PROBABLE). | as above | Yes |
| PTN002378821 | same | 13 | 72 | GO:0002049, IMP, PMID:9770291 (PseudoCAP) | UNVERIFIABLE | Abstract uses pvdD as an expression read-out in lasR/lasI mutants and reports no pvdD mutant; a pvdD control strain could be in the full text (PSEUDOCAP WRONG_REFERENCE, SUSPECTED). | as above | Yes |

The node term is generic enough for a clade of NRPSs making different products and
suits it. No GO_CENTRAL defect. Defects: PSEUDOCAP 2 (one PROBABLE, one SUSPECTED),
each recorded once on the GO:0002049 row and covering the paired GO:0003824 row.
