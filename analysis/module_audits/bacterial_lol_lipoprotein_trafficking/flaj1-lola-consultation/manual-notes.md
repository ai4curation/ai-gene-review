# Fjoh_2111 / LolA1 manual source assessment

2026-11-07. Review preparation only while the normal GOA importer is repaired; no gene raw files or review scaffold were hand-created.

The full primary PMID:40050408 explicitly uses F. johnsoniae ATCC 17061 UW101 and identifies Fjoh_2111 as lolA1. Official UniProt A5FI22 is a 215-aa UW101 protein (taxon376686) with the same locus, LolA signatures and predicted SignalP1–21; no curated functional free text is present. The original official identity response already captured in the frozen family consultation supplies independent identity and architecture evidence. No assumption that all PTHR35869:SF1 members share the same substrate is needed: LolA1 has its own native evidence.

Deletion and complementation demonstrate effects on motility and amylase secretion. Outer-membrane proteomics directly shows depletion of GldJ and GldK in the lolA1 mutant. These observations, combined with the specific LolA fold, support lipoprotein-carrier function as a mechanistic inference and native participation in lipoprotein trafficking. They do not constitute purified binding/transfer kinetics, a target structure, or direct membrane-insertion activity. Downstream gliding/T9SS effects are biological consequences; no NEW process terms for those outputs are planned.

The predicted cleavable signal peptide and LolA carrier architecture support a soluble periplasmic location, consistent with the paper's explicit prediction. Any core location must be described as inferred, not as a direct localization assay. No claim of intrinsic membrane insertion is warranted. In the quintuple LolAB mutant, the engineered LES-SiaC reporter remains surface exposed, limiting assertions that this route handles every surface lipoprotein.

GO:0042953 lipoprotein transport and GO:0044874 lipoprotein localization to outer membrane are not in a simple parent–child relationship in current QuickGO. The native transport participation claim is sound; there is no reason to call it false or falsely label an OM-localization replacement as hierarchical refinement. The final decision awaits the normally seeded original row. Its literal ECO:0007744 provenance will be retained; no IMP/ISS replacement will be invented to fit an enum.

The existing source annotation combines computational and experimental evidence, including an E. coli donor reference, rather than documenting an isolated LolA1 carrier assay. Final reasons should distinguish the source's evidence description from the exact primary native observations. A core carrier MF can be synthesized with explicit inference and sources without manufacturing redundant NEW rows.

## Completed review after normal seeding

The normal seed is now frozen in `../flaj1-lola-seed-baseline.json`. The sole original GO:0042953 row is ACCEPT, with its exact literal ECO:0007744, relationship, reference and donor preserved. No NEW rows were added. The carrier/periplasm/OM-delivery core is explicitly inferred from native UW101 evidence and specific architecture. The actual Falcon attempt failed authentication (403); no provider report was created. PAINT leaf lookup was unavailable for A5FI22, so no loss-free lineage assertion is made.

The ECO-fix validator's first run found local files in the wrong worktree because its root is derived from the imported package path. A byte-identical source overlay linked to the Lol data resolves this without editing code, sources or file citations. Commit2564a3fb412d7a561ca8fd165128294e2e496016 is a publication dependency; normal validation should be rerun after that code is integrated. The passing focused check has three disclosed core-coverage warnings, not scientific errors.
