# dxs (P77488) notes

## Sources examined

No deep-research file exists for this gene; none was generated. The review rests on the cached
publications for every GOA reference, the UniProt record, and PMC full text read for two papers
(PMC19265 = PMID:9482846, PMC94361 = PMID:10648511). The PMC entry for PMID:11115399 (PMC1221543) offers
only a PDF, which could not be retrieved. QuickGO was queried for GO term status and for comparator annotations.

## Activity

- Purified E. coli Dxs makes DXP from pyruvate and glyceraldehyde 3-phosphate in a ThDP-dependent acyloin
  condensation [PMID:9371765 "catalyzes a thiamin diphosphate-dependent acyloin condensation reaction between C atoms 2 and 3 of pyruvate and glyceraldehyde 3-phosphate to yield DXP"].
- Independently cloned as ORF2 of the ispA operon [PMID:9482846 "The dxs gene was identified as part of an operon that also contains ispA"].
- Structure with ThDP; active site within one monomer, unlike transketolase [PMID:17135236 "the active site of DXS is located at the interface of domains I and II in the same monomer"].

## Oligomeric state (full text of PMID:10648511, PMC94361)

"The native molecular mass of the enzyme was estimated to be 117 kDa by gel filtration chromatography,
suggesting that the E. coli enzyme is also likely to form a dimer." The same paper reports an E. coli
Mg2+/Mn2+ requirement and a pH optimum of 7.5-8.0. This full-text result supports the EcoCyc IDA
homodimerization row, although the cached abstract only describes the Streptomyces dimer.

## Ubiquinone and pyridoxine rows (full text of PMID:9482846, PMC19265)

The paper contains no new pathway-incorporation experiment. It cites earlier work: "In Escherichia coli,
d-1-deoxyxylulose (most likely in the form of d-1-deoxyxylulose 5-phosphate) is efficiently incorporated
into the prenyl side chain of menaquinone and ubiquinone". The EcoCyc acts_upstream_of_or_within rows
combine the demonstrated activity with that metabolic context.

## Branch to thiamine and vitamin B6: the involved_in judgement

- Who does the step: Dxs itself catalyses DXP formation, and DXP carbons are incorporated into the thiamine
  thiazole (via ThiG) and into the pyridoxine ring (via PdxJ). Dxs therefore catalyses a step on these
  routes; it is not merely a consumed substrate.
- GO convention: GO:0052865 (DXP biosynthetic process) is obsolete, described by QuickGO as "an unnecessary grouping
  term", which places DXP formation inside the downstream pathways.
- Comparator check (QuickGO, 2026-11-13): enzymes making the other vitamin B6 precursor branch carry the
  B6 term. E. coli SerC (P23721) has GO:0008615 IEA and GO:0042823 IMP, and Epd (P0A9B6) has GO:0008615 IMP
  and GO:0042823 IDA/IMP. A shared-precursor enzyme carrying the downstream vitamin process is therefore the
  standard convention.
- Decision: thiamine and pyridoxine rows are ACCEPTed and included in core_functions.directly_involved_in
  together with GO:0019288. Ubiquinone and terpenoid rows are kept as non-core because they sit beyond IPP,
  which is already captured by GO:0019288.

## Unverified items

- PMID:11115399 (IMP, isoprenoid biosynthesis) and PMID:11163766 (IMP, MEP pathway): the abstracts do not
  mention dxs and the full text was not retrievable (a PDF behind a browser check, or no PMC record). Both rows are accepted
  or refined on the curator's reading, since the claims agree with the biochemistry.
