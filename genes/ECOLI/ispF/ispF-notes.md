# ispF (P62617) notes

## Literature checked

- Enzymology [PMID:10694574 "The recombinant protein was found to convert 4-diphosphocytidyl-2C-methyl-D-erythritol 2-phosphate into 2C-methyl-D-erythritol 2,4-cyclodiphosphate and CMP."]; metal requirement [PMID:10694574 "The enzyme-catalyzed reaction requires Mn(2+) or Mg(2+) but no other cofactors."]. Abstract only; PMC15955 not retrievable. The ubiquinone IDA row cites this paper but the abstract has no ubiquinone data.
- Structures: homotrimer, one Zn2+ per subunit [PMID:11829504 "The protein forms homotrimers that tightly bind one zinc ion per subunit at the active site"]; Zn2+ plus phosphate-bridging Mn2+ [PMID:11997478]; active sites between monomers, Asp8/His10/His42 metal ligands [PMID:11786530].
- Regulation in vitro: MEP activates, FDP inhibits the IspF-MEP complex [PMID:22839733, full text cached].
- Essential; depletion causes filamentation [PMID:12270818 "E. coli cells depleted of MEC synthase revealed a filamentous phenotype."].

## Decisions

- Protein binding (HldD, Butland) REMOVE per policy.
- Ubiquinone biosynthesis (acts_upstream_of_or_within) and terpenoid biosynthesis KEEP_AS_NON_CORE as downstream isoprenoid context.
- Zinc ion binding ACCEPT; manganese ion binding and identical protein binding (homotrimer) KEEP_AS_NON_CORE; metal ion binding TOO_GENERAL.
- No location annotation exists; core_functions has none.
- No PAINT losses on the lineage.
