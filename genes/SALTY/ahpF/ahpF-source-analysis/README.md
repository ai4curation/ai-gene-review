# AhpCF source and identity checks

This analysis accompanies the SALTY and BACSU AhpC/AhpF reviews. Run from the repository root:

```sh
uv run python genes/SALTY/ahpF/ahpF-source-analysis/reproduce_scope.py
```

The script reads immutable source caches and exact target records, verifies inspected literal passages and AhpF-specific domains, and records SHA-256 hashes in `source-scope-proof.json`. It does not fetch or alter a source. `ontology-context.json` preserves the normally retrieved QuickGO definitions used to distinguish obsolete peroxidase wording, protein-disulfide reduction and the proton-translocating respiratory reaction.

The complete publisher-formatted primary for PMID:10828978 was recovered through the normal `linkml-reference-validator lookup` URL route from CiteSeerX. Its automatically extracted title is “No Job Name”; the PDF heading, authors, journal, pages and DOI identify Poole et al., Biochemistry 39:6602–6615. No metadata or publication text was manually rewritten. The paper studies recombinant Salmonella AhpF and fragments; free thioredoxin/thioredoxin reductase are E. coli comparators. It reports no effective standard-assay Trx reduction, but detects very slow transfer after 20 hours. Neither an absolute absence of side activity nor a native E. coli AhpF assay is inferred.

PMID:8555198 and PMID:8555199 remain abstract caches; their explicit positive catalytic results are corroborated by the complete primary above and the normally recovered Poole mechanistic review. The NADH/NADPH comparison is an apparent Km comparison in DTNB reductase assays, not a physiological flux ratio. Native-isolated and E. coli-expressed Salmonella proteins are separately identified in the original abstract.

Bacillus PMID:8932314 and PMID:8932315 remain abstract-only after normal canonical, PMC PDF, publisher and EuropePMC attempts. A 306-byte PMC download interstitial is **not** evidence or full text and is excluded from the staging/source-closure manifest. Bacillus native operon, induction and mutant phenotypes are explicit, while purified partner kinetics are inferred only through specific orthology and architecture. Increased H2O2 resistance in ahpC mutants reflects compensatory peroxide-regulon induction rather than disproving the enzyme's peroxide chemistry.

The Bacillus AhpF record's old respiratory assignment is evaluated separately from membrane localization. GO:0008137 explicitly includes four-proton translocation. The complete target has the AhpF N-terminal relay and native ahpCF locus, supporting correction to protein-disulfide reduction and rejection of the derived proton-transport assertion. This is not an experimental claim of zero quinone side activity. Peripheral membrane localization remains unresolved because soluble architecture and cytosol inference do not exclude a peripheral pool.

PAINT nodes PTN005133404, PTN000530716 and PTN000073874 were inspected in the existing committed source slices. The TrxR/AhpF specificity distinction does not depend on donor count. Modernizing the obsolete AhpC term does not assert loss of its conserved peroxiredoxin function. Family review files remain owned by the integration agent and were not edited here.
