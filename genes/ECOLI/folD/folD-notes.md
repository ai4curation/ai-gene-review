# folD (P24186, b0529) notes

## Deep research status

`just deep-research ECOLI folD --provider perplexity` failed on 2026-11-13
("Provider 'perplexity' not available. Available: falcon, openscientist,
claude_code"); no provider API key is configured in this session. These notes
are my own reading of the UniProt record and the cached publications, not
provider output.

## Literature reviewed

- D'Ari & Rabinowitz 1991 (abstract only). Enzyme purified ~2,000-fold from
  E. coli; NADP-specific dehydrogenase that also carries cyclohydrolase activity;
  homodimer [PMID:1748668 "The purified enzyme is specific for NADP. The
  protein also contains 5,10-methenyltetrahydrofolate cyclohydrolase (EC
  3.5.4.9) activity."] [PMID:1748668 "suggest that the enzyme is a dimer of
  identical subunits"].
- Donaldson, Scott & Scott 1965 (no abstract in cache). Early purification of
  E. coli 5,10-methylene-THF dehydrogenase; title only
  [PMID:4378935 "Purification and properties of 5,10-methylenetetrahydrofolate
  dehydrogenase from Escherichia coli."]. Deferred to the EcoCyc curator for the
  IDA.
- Shen et al. 1999 (abstract only). 2.5 A crystal structure of E. coli FolD,
  conserved basic cluster for the polyglutamate tail, modelled NADP/CH2-THF in
  the dehydrogenase site [PMID:10386884 "this binding site would allow
  interaction of the nicotinamide and pterin rings in the dehydrogenase active
  site"].
- Sah & Varshney 2015 (abstract only). Purified wild-type and point mutants
  from a folD-deleted host carrying C. perfringens fhs; both activities
  measured; K54S separates cyclohydrolase from dehydrogenase, R191E the reverse
  [PMID:25988590 "the K54S mutant lacked the cyclohydrolase activity but
  possessed high dehydrogenase activity"]. The abstract also states that the
  essential 10-formyl-THF requirement can alternatively be fulfilled by Fhs, which
  E. coli itself lacks.
- Ishihama et al. 2008: FolD among 1,103 proteins identified in the cytosolic
  fraction [PMID:18304323].

## Synthesis

FolD is the only E. coli route from 5,10-methylene-THF to 10-formyl-THF (no Fhs
in E. coli K-12), so it supplies 10-CHO-THF for purine synthesis (PurN, PurH)
and fMet-tRNA formylation (Fmt), and 5,10-methenyl-THF. Both activities sit in
one 288-aa polypeptide (shared active site in the N-terminal domain, NADP-binding
Rossmann domain C-terminal). Location: soluble cytosolic.

Decisions: IDA/IBA/IEA rows for both activities ACCEPT; catalytic activity and
oxidoreductase activity MODIFY to the specific activities; cytoplasm (ARBA)
MODIFY to cytosol; homodimerization KEEP_AS_NON_CORE.
