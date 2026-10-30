# Native bacterial nitrate reduction audit

This audit links 21 exact UniProt products to four native nitrate-to-ammonium implementations: Synechococcus elongatus PCC 7942, Bacillus subtilis 168-lineage bacteria, Pseudomonas putida KT2440, and Mycobacterium smegmatis mc2 155. The E. coli K-12 NarU/NirBD comparison requires an upstream respiratory nitrate reductase outside the panel. It is not a fifth complete route.

The YAML tables and generated reports live in [`analysis/module_audits/bacterial_assimilatory_nitrate_reduction`](../../analysis/module_audits/bacterial_assimilatory_nitrate_reduction/), because repository module discovery treats every YAML beneath `modules/` as a module record. There, `members.yaml` identifies the complete panel, including all 14 original exemplars and seven additions needed to examine native implementations. The 21 gene reviews contain 169 active annotation rows. All 165 original machine-sourced annotation payloads and all 42 raw GOA/UniProt files were preserved. Four inherited NEW proposals remain; one duplicate inherited PSEPK NirD proposal is archived, in full, under that gene's source analysis. This audit adds no NEW gene annotations.

## Reproduction

Run from the repository root after `uv sync`:

```sh
uv run python modules/bacterial_assimilatory_nitrate_reduction-source-analysis/check_nasN_identity.py --fetch
uv run linkml-validate --schema src/ai_gene_review/schema/gene_review.yaml --target-class ModuleReview modules/bacterial_assimilatory_nitrate_reduction.yaml
uv run python modules/bacterial_assimilatory_nitrate_reduction-source-analysis/check_module.py
uv run python modules/bacterial_assimilatory_nitrate_reduction-source-analysis/check_routes.py
```

The identity command prints a result comparable to `nasN-identity-proof.json`. It downloads missing versioned ENA inputs to the ignored `.cache/module-audit-logs/nitrate-foundation` directory; `--cache-dir` selects another input location. It compares CP000480.1's MSMEG_4206 pseudogene with corrected DQ866862.1 and translates the corrected sequence. Inserting G at corrected nucleotide 1850 produces a 1351-residue sequence identical to the committed A4ZHT3 UniProt record. The proof records sequence hashes, source URLs and the protein-record hash. The whole genome is not duplicated in git. DQ866862's older MSMEG4211 name does not imply another protein.

`check_module.py` calls the production module validator with a bounded family-member index read from the unedited target UniProt records. Official family names are checked against the committed PANTHER ontology. It also verifies exact panel membership, species identities, evidence presence and completed gene decisions. Results are written to `validation-results.yaml`. Its NO_FUNCTION_ID advisories concern descriptive subunit roles: the complete complex carries the catalytic GO activity, rather than claiming that every isolated chain catalyses the whole reaction. These prose roles require manual review.

`check_routes.py` invokes the production Boolean compiler with an explicit oracle requiring every named native subunit. It writes `route-results.yaml`: 80 positive and negative cases cover complete routes, missing reduction or uptake components, incomplete complexes, cross-species mixtures and the incomplete E. coli route. Taxonomy and subunit expansion are enforced by this oracle; the generic compiler does not infer them. A positive result establishes consistency with the represented inventory, not a new physiological experiment.

## Evidence boundaries

The module and individual review notes give source-specific findings and access limits. In particular:

- Uptake is optional only when intracellular nitrate is supplied. Extracellular-input scenarios require the represented native uptake mechanism. MYCS2 has no modeled uptake implementation. These checks do not exclude unrepresented or redundant transporters.
- SYNE7 uses ferredoxin-class nitrate and nitrite enzymes. NarB donor experiments and the heterologous ferredoxin comparison do not establish an exclusive native donor accession. Native NirA methyl-viologen assays do not directly determine physiological donor preference.
- BACSU NasBC uses a donor-generic nitrate-reductase term. NADH assignment comes from architecture and review-level synthesis; native primary nitrate assays used methyl viologen. NasDE's main NADH reaction is directly supported; NADPH activity was less than 10% of NADH activity in the cited study.
- PSEPK PP_1703's historical KT2442 catalytic fragment matches Q88M71 residues 1–724 exactly. The accompanying gene-local ENA analysis establishes identity, not purified full-fusion activity or KT2440 donor preference. The native NirBD assembly and NAD(P)H class combine expression, lysate activity and conserved classification; the lysate assay used methyl viologen.
- MYCS2 NasN has direct native genetics and purified NADPH-preferred activity, with measurable NADH turnover. It remains oxygen sensitive. The downstream NirB/MSMEG_0428 assembly is inferred from native expression and conserved classifications, without a purified native subunit-requirement experiment.
- Connections describe chemical continuity, not a physical reductase supercomplex. Reducing equivalents, cofactor synthesis, maturation, regulation and downstream ammonium incorporation into glutamine/glutamate are outside the inventory.

The canonical PMID:32111737 cache contains only the abstract. Full NasN quotations cite the separately fetched PMC XML URL record. The canonical PMID:7868621 cache is also abstract-only; the BACSU source analysis distinguishes direct reading of its publisher PDF from cached quotations. Failed provider requests and browser challenge pages are not evidence and are excluded from the curated source registry.

`go-terms.json` is the unedited QuickGO response for all 45 GO identifiers appearing in the panel and module at final review. The analysis directory's `go-terms-provenance.yaml` records the exact request, retrieval time and checksum. None was obsolete in that snapshot. Machine-sourced GOA terms were preserved even where the review recommends a different activity.
