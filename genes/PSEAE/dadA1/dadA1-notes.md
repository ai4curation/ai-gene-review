# dadA1 (PA5304, Q9HTQ0) notes

D-amino acid dehydrogenase of the dadRAX locus. No deep-research provider was available;
literature checked by hand (PMID:21378189 abstract; PMC full text not returned by the PubMed
MCP; UniProt curated text from the same paper; QuickGO for E. coli DadA P0A6J5).

## Literature

- He, Li & Lu 2011 (PMID:21378189, abstract): ["purified recombinant DadA alone was sufficient to
  demonstrate the proposed enzymatic activity with very broad substrate specificity"]; dadA mutant
  cannot use L-Ala, D-Ala and a set of D-amino acids as nitrogen source; DadR binds the dadA
  regulatory region and L-Ala is the inducing signal; ["the results from this study clearly
  demonstrate DadA to be the enzyme solely responsible for the proposed D-amino acid
  dehydrogenase activity of broad substrate specificity"]. UniProt records Km/kcat for nine
  D-amino acids from this paper.
- dadX review (genes/PSEAE/dadX) treats DadX-DadA as the L-alanine catabolic route; consistent.
- dsdA review records that D-serine use is abolished in a dadA mutant; consistent.

## Review decisions

- GO:0008718 (IDA, IBA, IEA): ACCEPT, core.
- GO:0055130 D-alanine catabolic process (IBA, IEA): ACCEPT. GO:0019478 D-amino acid catabolic
  process IEA: ACCEPT (several D-amino acids depend on DadA1, so not merely entailed by D-Ala).
- Cytoplasm and plasma membrane IBA: KEEP_AS_NON_CORE (homology to membrane-associated E. coli
  DadA; untested in P. aeruginosa).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008552203 | GO:0008718 D-amino-acid dehydrogenase activity | 3 | 10 (8 taxa) | GO:0008718, IDA, PMID:21378189 (PseudoCAP) | SOUND | The abstract states that purified recombinant DadA has the activity, with kinetics on many D-amino acids; UniProt ties it to PA5304. Node term suits a DadA clade. | E. coli DadA P0A6J5 (IDA PMID:13292, 6131836); DadA2 Q9HU99 (PseudoCAP IDA to PMID:17021207, WRONG reference; see dadA2 notes) | Yes, on E. coli DadA (and on this seed) |

No defect here. The shared-node problem (the DadA2 seed cites a P. putida paper) is recorded
once, as a PSEUDOCAP WRONG_REFERENCE defect on genes/PSEAE/dadA2. No GO_CENTRAL defect: the IBD
stands on E. coli DadA and DadA1.
