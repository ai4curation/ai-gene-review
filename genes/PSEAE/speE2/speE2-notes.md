# speE2 (PA4774, Q9HV34) review notes

No deep-research provider was available. Sources: UniProt record (Q9HV34,
HAMAP MF_00198), cached PMID:22155771 (abstract only; PMC full text body not
returned by the PubMed MCP). speC (PA ornithine decarboxylase) was reviewed
earlier; it sits on a different PANTHER node (PTN000159726), so there is no
shared node to coordinate.

## Function

- Spermidine synthase (EC 2.5.1.16): putrescine + decarboxy-AdoMet -> spermidine
  [file:PSEAE/speE2/speE2-uniprot.txt "Catalyzes the irreversible transfer of a
  propylamine group from the amino donor S-adenosylmethioninamine (decarboxy-AdoMet)
  to putrescine (1,4-diaminobutane) to yield spermidine"].
- PA4774 mutant makes no surface spermidine; restored by complementation; surface
  spermidine stabilises the OM [PMID:22155771 "mutant did not produce spermidine on
  the cell surface, but genetic complementation restored surface spermidine
  production"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000168372 | GO:0006596 polyamine biosynthetic process | 2 | 120 (56 taxa) | GO:0008295 spermidine biosynthetic process, IMP, PMID:22155771 (PseudoCAP) | SOUND | SpeE2 is the spermidine synthase, so the mutant's loss of spermidine coincides with its own catalytic step (participation). The broad BP node term suits an aminopropyltransferase clade; the seed's GO:0008295 is a descendant. | S. solfataricus SpeE (Q9UXE4), a multifunctional aminopropyltransferase | Yes; Q9UXE4 is experimentally characterised. No GO_CENTRAL defect for the GO:0006596 BP IBD. |

### Separate issue: the GO:0010487 MF IBD at the same node over-propagates

PTN000168372 also carries a thermospermine synthase activity (GO:0010487) MF IBD,
seeded by Q9UXE4 and Arabidopsis ACL5 (AT5G19530, a dedicated thermospermine
synthase). This is NOT a PseudoCAP-seeded row, but it propagates a GO:0010487 IBA
onto SpeE2, which is a putrescine aminopropyltransferase (spermidine synthase) by
HAMAP curation, not a thermospermine synthase. I MODIFY the GO:0010487 IBA on
SpeE2 to GO:0004766 spermidine synthase activity (the enzyme's curated activity,
already present by IEA) and raise a PROBABLE `resource: GO_CENTRAL` defect that the
thermospermine-synthase MF IBD should sit on the thermospermine-synthase sub-clade
rather than the whole-family node. Full enzymatic characterisation of SpeE2 would
confirm whether it has any thermospermine side activity.

PseudoCAP defects from this gene: none. GO_CENTRAL defects: 1 (PTN000168372
GO:0010487 over-propagation, PROBABLE).
