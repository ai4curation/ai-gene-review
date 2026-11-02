# parP (Q9KQE0, VC_2060) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_VSFT01000037.1_102` (*Vibrio cholerae*, 341 aa), https://gene-annotate-dashboard.kbase.us/review/NZ_VSFT01000037.1_102
- Dashboard strata: Human Pathogen, Core, Annotation-Promoted, GLOB. Homologs come from one genus only (*Vibrio*, 5 organisms).
- Mapped to the N16961 reference entry Q9KQE0 (VC_2060, 338 aa). Identity is 98.8% over the 338 aligned residues and 97.9% over the query length (hackathon run `20261030T212629Z-finalize-vibch-mapping`, `final_mapping.tsv`). The query has a 3-residue offset: its AIF-domain residues sit at query positions +3 relative to Q9KQE0.
- DeepTMHMM on the dashboard sequence predicts a globular, cytoplasmic protein.

## Gene directory name: `VC_2060`

The directory is named by locus tag because UniProt gives no gene symbol, only `OrderedLocusNames=VC_2060` (project rule: use the UniProt gene symbol when there is one, else the locus tag). An earlier draft filed it as `parP`; it was moved back on 2026-10-30. The published name *parP* (Ringgaard et al. 2014, PMID:24379357; Alvarado et al. 2017, PMID:29058677) is kept as an alias, together with `VC2060` and the dashboard id.

## Dashboard LLM call under review

> ParP chemotaxis-array assembly and polar-localization protein interacting with methyl-accepting chemotaxis proteins, CheA, and ParC. (Tier A; GO:0005515, GO:0065003, GO:0008104, GO:0060187)

Verdict: **supported**. The "97.9%-identical V. cholerae homolog" the annotator relied on is this gene itself, VC_2060 in N16961, which Alvarado et al. 2017 characterized directly.

- All four GO terms are biologically correct and absent from GOA, so all are scored COR.
- GO:0005515 protein binding is true but uninformative. The review uses GO:0030674 protein-macromolecule adaptor activity instead.
- GO:0065003 complex assembly is correct but generic. The review uses GO:0043113 receptor clustering.
- GO:0008104 is labelled "intracellular protein localization" in current GO. The brief said "protein localization"; the page shows the current label.
- GO:0060187 cell pole is a CC term, and it is supported directly: YFP-ParP is polar in 97% of V. cholerae cells.

## Literature caveats

- The brief cited PMID 21764851 for Ringgaard et al. 2011 Genes Dev. That PMID is an unrelated NFIB small-cell lung cancer paper. The ParC paper is **PMID:21764856**. It names VC2061 as ParC; ParP had not yet been named.
- Ringgaard et al. 2014 PNAS (PMID:24379357) worked mainly in *V. parahaemolyticus* (VP2226). Its V. cholerae data are limited to a supplementary localization phenotype (Fig. S3C-D). Statements about chemotaxis and swimming reversals, and about the CheA LID, come from the *V. parahaemolyticus* ortholog (about 50% identity, per the dashboard's PaperBLAST data).
- Alvarado et al. 2017 eLife (PMID:29058677) is V. cholerae N16961 work on VC2060 itself: interactions, AIF mutants (L209A, W305A), array formation, polar localization and FRAP.
- Yang et al. 2018 PNAS (PMID:30541885) places ParP in the cluster II array baseplate (CheW1:CheA2:ParP = 35:5.3:1). Note that the CheA numbering in this paper (CheA2) differs from the eLife paper (CheA1).
- Residue check (beril run `20261030T213718Z-parp-aif-residues`): L196, L209, L212, I215 and W305 are present in Q9KQE0, and at positions 199, 212, 215, 218 and 308 in the dashboard sequence.

## Tooling notes

- Seeded via `ubergraph:` (EBI OLS down); `just fetch-gene` was not rerun.
- `just fetch-fitness VIBCH parP` failed: there is no FEBA organism mapping for VIBCH, and no FEBA data source was reachable. No fitness artifact was written.
- `just fetch-gene-pmids` found no PMIDs (the UniProt entry has none). Key papers were fetched with `just fetch-pmid`. PMID 27573843 initially failed with a PMC HTTP 429 error; the retry cached the abstract only.
- `just validate-terms` on the predictions sidecar fails with "No such slot locus_tag as an attribute of GeneReview": the recipe validates against the GeneReview class, not PredictionReview. `just validate-predictions` (which runs `validate-prediction-terms`) passes.
- Deep research: `just deep-research-claude-code VIBCH parP`.
