# ASP1 notes (P38986, YDR321W)

- Asparaginase I, cytoplasmic and constitutive [UniProt:P38986 "SUBCELLULAR LOCATION: Cytoplasm."]; [PMID:238936 "The internal enzyme appears to be constitutive."]. No signal peptide.
- Recombinant enzyme: allosteric, catalytic residues T64/Y78/T141/K215 [PMID:27824095 "the T64-Y78-T141-K215 residues are involved in catalysis"].
- Natural null allele in wine strains [PMID:17537182 "targeted the catalytic core of asparaginase type I (ASP1) and abolished its activity"].
- IBA cell wall-bounded periplasmic space (PTN000194670, donors only ASP3 copies) -> REMOVE (compartment of secreted paralog).


## 2026-10-26 comparative annotation audit

Reviewed all 17 existing rows and the core-function synthesis for yeast/ASP1; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'ACCEPT': 12, 'MODIFY': 4, 'REMOVE': 1}.

PMID:27824095 full enzyme/mutagenesis data supports intracellular asparaginase catalysis and essential catalytic residues. PMID:17537182 directly connects an ASP1 active-site variant to loss of enzyme activity in wine strains, with nitrogen-source-dependent fermentation effects; those peripheral phenotypes are not manufactured as new processes. PMID:8026756 cloning/mapping identifies the structural gene for cytoplasmic ASP I: “confirms that ASP1 is the structural gene encoding cytoplasmic ASP I in S. cerevisiae.”

The periplasmic IBA is rejected on target-specific compartment evidence, not donor count, generic sequence length or inferred absence. PTHR11707 includes intracellular ASP1 and secreted ASP3 in the same subfamily; its PTN000194670 assessment places the location too deep. The source entity is named by its actual PTN identifier. This compartmental conclusion remains valid independently of the disputed evolutionary origin of ASP3. General amino-acid metabolism refines to asparagine catabolism; cytoplasm refines to cytosol.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP 403 authentication failure; Perplexity returned HTTP 401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-yeast-ASP1-research.log` and `aspartate-yeast-ASP1-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-yeast-ASP1-*`. Final results and machine-payload proof are in the panel validation/payload manifests.


## PR #5568 follow-up, 2026-10-26

Repaired authored citation spacing and fused numeric prose while preserving original annotation payloads, every action, raw UniProt/GOA records and all existing supporting quotations. Source-cited passages in notes were protected from rewriting.
