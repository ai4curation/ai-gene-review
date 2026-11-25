# New-member annotation-reviewer consultation

Scope: BACSU proA/proB/proJ and CORGL proA/proB. Independently inspected the initial curation script, all five reviews, frozen UniProt records and cached primary evidence. The consultation retains all annotation decisions and core functional assertions; no NEW rows are added.

The target reactions are supported by curated HAMAP MF_00412 (ProA) and MF_00456 (ProB/ProJ), not inferred solely from mutant necessity. ProA's NADPH-dependent reduction entails NADP(H) interaction; the current GO:0050661 definition explicitly includes oxidized NADP+ and reduced NADPH. Kinase ATP-binding rows now quote the ATP-containing target reaction and a HAMAP ATP-contact feature. These remain computational/mechanistic inferences without measured target binding constants.

The BACSU reference sequences are strain 168; PMID:21784929 experiments use JH642 derivatives. Its explicit anabolic ProB-ProA-ProI and osmoadaptive ProJ-ProA-ProH evidence now supports the branch-specific core descriptions, without being represented as purified target enzyme assays. ProJ feedback resistance is not asserted as measured. PAINT checks for all three BACSU targets report no IRD/IKR loss.

PMID:8755867 describes C. glutamicum ATCC 17965, not the ATCC 13032 reference targets. Its proB complementation/mutants and proA bypass findings corroborate pathway roles across strains. The abstract-only access limit remains explicit. PMID:8083159 supports B. subtilis gene organization; its multicopy protease phenotype does not establish direct protease regulation by ProB.

Cytosol refinements for ProB/ProJ remain localization inferences from the cytoplasmic HAMAP assignment and soluble enzyme architecture. An existing annotation is not cited as independent location evidence. ProA retains its existing cytoplasm term. RNA binding stays UNDECIDED for all three kinase targets: the positive E. coli ProB SELEX/EMSA result in PMID:37511294 rules out a family-wide rejection, but does not establish activity on these targets or assign binding to the PUA domain.

Findings now contain biological statements and matching source quotations instead of duplicate workflow/access notes. The unavailable flag on PMID:25367752 was removed after independently inspecting its [publisher full text](https://onlinelibrary.wiley.com/doi/10.1111/brv.12146); the repository abstract cache was not rewritten. All five real Falcon failures remain documented honestly. No provider report was fabricated.

Standard record-section backfilling added 79 fields, then 13 more after ambiguous location snippets were expanded with their verbatim SUBCELLULAR LOCATION headings. No manual section assignments were made, and the final pass left no ambiguous or unplaceable quotes.

The machine-readable companion records exact payload/order preservation, raw/publication hashes, unchanged decisions and core assertions, focused validation, renders, histories and the changed-path manifest. No module, family, comparator, tracker or publication file was edited by this consultation; no full validation, commit or push was performed. Root owns mechanism-capacity validation and integration.
