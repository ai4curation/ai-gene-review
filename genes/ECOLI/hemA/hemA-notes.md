# hemA (P0A6X1) notes, Escherichia coli K-12

## Sources and deep research

- Deep research was attempted once with `just deep-research ECOLI hemA --provider perplexity`
  (2026-11-10); it failed with a template error ("Template file not found:
  templates/gene_research_go_focused.md"; "All providers failed"). No deep-research file
  exists. This review is built from the UniProt record and the cached GOA-cited abstracts.
- All three cited primary papers (PMID:12370189, PMID:15757895, PMID:1990004) are
  abstract-only in the cache.

## Function

- GluTR catalyses the first step of the C5 route: [PMID:12370189 "glutamyl-tRNA reductase
  (GluTR, encoded by hemA) catalyzes the NADPH-dependent reduction of glutamyl-tRNA to
  glutamate-1-semialdehyde"].
- Mechanism: active-site Cys50 forms a thioester with tRNA-bound glutamate, reduced by NADPH;
  without NADPH the enzyme acts as an esterase [PMID:12370189 "In the absence of NADPH, E. coli
  GluTR exhibited substrate esterase activity"]. The esterase is a partial reaction of the
  same catalytic cycle, not a separate function.
- hemA mutants are ALA auxotrophs [PMID:12370189 "Eight 5-aminolevulinic acid auxotrophic E.
  coli hemA mutants were genetically selected"].
- Substrate specificity for E. coli tRNA(Glu) [PMID:1990004 "E. coli Glu-tRNA(2Glu) is a good
  substrate"].

## Quaternary structure and partner

- Homodimer [PMID:12370189 "Soluble homodimeric E. coli GluTR"]. PMID:1990004 (the source of
  the GO:0042802 IDA row) reported an 85 kDa native enzyme it interpreted as monomeric; with a
  418-residue (about 46 kDa) HemA chain, the 85 kDa species fits the later homodimer
  assignment. Treated as homodimer evidence.
- Complex with HemL (GSA-AM) for channeling of glutamate 1-semialdehyde [PMID:15757895
  "Co-immunoprecipitation experiments using antibodies directed against E. coli GluTR and
  GSA-AM demonstrated the physical interaction of both enzymes"]. Dimerization needed for
  complex formation. No GO MF term captures "channeling partner"; the bare protein-binding row
  is removed per policy, the interaction is real.

## Verdict summary

- GO:0008883 (IBA, IDA, IEA): ACCEPT, core.
- GO:0033014 (IEA InterPro2GO): ACCEPT; ALA is the common precursor of all tetrapyrroles
  (heme b and siroheme in E. coli). Same verdict as genes/PSEPK/hemA.
- GO:0050661 NADP binding: KEEP_AS_NON_CORE (cofactor; consistent with PSEPK hemA).
- GO:0042802 identical protein binding: MODIFY to GO:0042803 protein homodimerization activity.
- GO:0005515 protein binding (HemL IPI): REMOVE per protein-binding policy.
