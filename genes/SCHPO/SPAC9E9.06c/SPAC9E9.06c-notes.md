# SPAC9E9.06c (threonine synthase, UniProt Q42598) - notes

## Identity / naming
- PomBase systematic ID SPAC9E9.06c, no standard PomBase gene name (PomBase product "threonine synthase"); UniProt gives Name=thrc [UniProt:Q42598].
- UniProt CAUTION: "Was originally (Ref.1) thought to originate from A.thaliana." [UniProt:Q42598] - the accession Q42598 is a historical plant-attributed record later reassigned to S. pombe. Key on the accession, not on the "THRC" name.
- S. cerevisiae ortholog: THR4 (P16120), the source of the UniProt ECO:0000250 assertions and the PomBase ISS rows.

## Function
- Threonine synthase, EC 4.2.3.1: "Reaction=O-phospho-L-homoserine + H2O = L-threonine + phosphate;" [UniProt:Q42598]; PLP cofactor [UniProt:Q42598]; final step (5/5) of L-threonine biosynthesis from L-aspartate [UniProt:Q42598].
- Budding-yeast THR4 encodes the activity [PMID:8082795 "we have determined that this activity depends on the presence in the cell of an active form of the THR4 gene"].
- No S. pombe-specific biochemistry found; function is by orthology to THR4 and the PANTHER IBA node PTN000034281.

## Localization
- Cytosol in the ORFeome YFP screen [PMID:16823372 "we determined the localization of 4,431 proteins"] (HDA, PomBase).

## GO-CAM
- gomodel:678073a900003175 (PomBase homoserine/threonine/glycine model): SPAC9E9.06c enables GO:0004795, occurs_in cytosol, part_of GO:0009088 (IBA evidence). Consistent with this review.

## Review decisions
- Threonine synthase activity, L-threonine biosynthesis, cytosol: accept.
- InterPro "amino acid metabolic process": MODIFY to L-threonine biosynthetic process (as for THR4).
- PLP binding: keep as non-core cofactor binding.


## 2026-10-26 systematic fungal threonine review

Reviewed all 9 rows and the core synthesis for SCHPO/SPAC9E9.06c. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'ACCEPT': 8, 'MODIFY': 1}.

The exact Q42598 record belongs to S. pombe; UniProt CAUTION documents an original erroneous Arabidopsis attribution. That provenance is recorded here rather than in the standalone protein summary. Conserved P16120 donor/ThrC-family evidence and PMID:8082795/11756443 support threonine synthase chemistry. The characterized donor is a monomeric PLP enzyme; no native S. pombe oligomer measurement is asserted. Both PLP-binding rows are core because the cofactor directly enables catalysis. PomBase cytosol localization is retained. Broad amino-acid metabolism refines to threonine biosynthesis. No plant SAM-activation phenotype is imported merely from historical taxon attribution.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-SCHPO-SPAC9E9.06c-research.log` and `threonine-SCHPO-SPAC9E9.06c-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.


## PR #5569 source-specific corrective review (2026-10-26)

Replaced duplicated summary/reason prose with enzyme-specific chemistry, provenance and cofactor explanations. Existing nuclear phenotypes remain distinct from metabolic rescue and catalytic activity; organelle assertions and all original machine fields are preserved.

Annotation actions are unchanged; revisions clarify evidence or narrative.

All 9 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.
