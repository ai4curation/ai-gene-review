# trpA (PA0035, P07344) review notes

No deep-research provider was available; notes compiled from the UniProt entry and the cached publication.

- Tryptophan synthase alpha chain; HAMAP MF_00131, TIGR00262. UniProt function (HAMAP): "The alpha subunit is responsible for the aldol cleavage of indoleglycerol phosphate to indole and glyceraldehyde 3-phosphate."
- trpBA gene order with 4-bp overlap [PMID:3127651 "The gene order is trpBA as predicted from earlier genetic studies, and the two cistrons overlap by 4 bp"].
- In vivo complementation: [PMID:3127651 "We also report the construction of a recombinant plasmid that overproduces a slightly modified alpha subunit from P. aeruginosa that can form a functionally effective multimer with normal E. coli beta 2 subunit in vivo"]. Abstract only in cache; PMC full text not available (no PMCID).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN000034360 | GO:0000162 L-tryptophan biosynthetic process | 3 | 151 (80 taxa) | GO:0000162, IDA, PMID:3127651 (PseudoCAP) | E. coli TrpA P0A877; Arabidopsis TSA1 AT3G54640 | Yes (E. coli TrpA is the reference enzyme) | SOUND | Heterologous in vivo complementation shows the alpha subunit works in Trp synthesis; evidence is complementation rather than a direct assay, but the term is right. Node term suits a TrpA clade. |

No source defects. Actions: 7 ACCEPT.
