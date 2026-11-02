# CORGL thrB research notes

## 2026-11-01 — native-template enzyme, recombinant assays

P07128 is the reviewed ATCC13032 homoserine kinase (taxon196627). The native route uses a standalone ThrB of the GHMP kinase family (TIGR00191 thrB; PTHR20861, SF1 HOMOSERINE KINASE). The broader PTHR20861 family also includes CDP-ME kinase, so the whole family name alone is insufficient to specify the reaction.

PMID:30023797 full text provides the key direct evidence: the gene was amplified using ATCC13032 genomic DNA and expressed in E.coli. Purified wild-type and engineered A20 variants were assayed with homoserine and ATP; ADP production was measured. Wild-type target protein and A20G were structurally characterized. The substrate-bound structures used for comparative interpretation are Methanocaldococcus jannaschii, not C.glutamicum structures containing bound homoserine or threonine. This boundary avoids overclaiming direct target ligand occupancy.

Wild-type ThrB Ki for threonine is4.73mM; A20G is25.22mM. The mutant reduces feedback inhibition while preserving activity, but this does not show the engineered behavior or increased production is basal native physiology. ATP binding and homoserine kinase MF are directly supported. The native gene produces phosphohomoserine for ThrC; broad threonine metabolism is MODIFY to threonine biosynthesis. Cytoplasm is retained at the precision supported by the reviewed record (ECO0000305), without a fabricated localization assay or unsupported refinement to cytosol.

The paper's introduction explicitly lists the five successive LysC/Asd/Hom/ThrB/ThrC reactions. That is useful pathway synthesis, not a single experiment reconstituting all five enzymes. All five seeded rows adjudicated; no NEW.

## Source acquisition and scope

Normal `just fetch-gene` generated the UniProt record, GOA export and seeded review. The 41 original rows across this five-gene panel and all ten raw files were snapshotted before curation. An initial folder-code misunderstanding was corrected to canonical CORGL; the five new folders were moved without changing raw bytes or machine annotation payloads. The original and migrated baselines and an explicit migration record are retained in `.cache/module-audit-logs/bacterial-threonine-corgl-20261101/`.

A normal Falcon research request failed with HTTP403 authentication failure. This is a provider failure, not a research report; no provider-named report was fabricated. The shared authentication failure was not repeatedly retried for the other four genes. The nonhuman MOD-description command was run for all five under canonical CORGL and reported no configured MOD provider. Research below is manual synthesis of immutable primary caches and the reviewed UniProt record.

No raw annotation was removed or rewritten. Ordinary relationship qualifiers played no part in the judgment. No NEW annotation was proposed: the original set and supported refinements already cover the supported biosynthetic functions. No unverified universal bacterial architecture or native production flux is inferred from recombinant protein or engineered production strains.
