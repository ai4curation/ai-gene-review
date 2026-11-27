# SHR3 notes

## 2026-09-29 IBA re-review

SHR3 carries three IBA rows from `GO_REF:0000033`, all traced by GOA to
`PANTHER:PTN002000498` in the `PTHR28228` SHR3 family. The repository currently
has the PTHR28228 family and subfamily in `interpro/panther/panther.obo`, but no
cached PTHR28228 PAINT TSV or PTN record. I therefore recorded the PTN in each
`propagation_review` as `SOURCE_STALE_OR_MISSING` rather than inventing
source-node details that are not locally cached.

The `GO:0005789 endoplasmic reticulum membrane` and `GO:0006888 endoplasmic
reticulum to Golgi vesicle-mediated transport` IBAs are sound core functions for
Shr3. The original SHR3 paper established it as an integral ER-membrane protein
needed for amino acid permease export from the ER [PMID:1423607], and the COPII
paper specifically described Shr3-mediated coatomer-cargo interactions and
packaging of amino acid permeases into ER-derived vesicles [PMID:10564255].

The `GO:0051082 unfolded protein binding` IBA already had the right action,
`MODIFY` to `GO:0044183 protein folding chaperone`; I added structured
`TERM_SCOPING_PROBLEM` / `GRANULARITY_MISMATCH` metadata. Kota and Ljungdahl
showed that Shr3's membrane domain prevents aggregation of amino acid permeases
in the ER [PMID:15623581]. Myronidi et al. 2023 then used scanning mutagenesis
and split-ubiquitin substrate tests to show that Shr3 selectively engages
nascent amino acid permease segments in a cotranslational, transient way
[PMID:37477900]. Those papers support an activity term, not a generic
unfolded-protein-binding term.

I also reclassified the five `GO:0005515 protein binding` IPI rows from
`MARK_AS_OVER_ANNOTATED` to `REMOVE`, following the current review policy for
generic protein binding. The interactions are not treated as false; they are
just less informative than Shr3's direct client-specific chaperone function.

## Newer-literature search

I searched 2023-2026 SHR3/YDL212W and yeast amino-acid-permease literature. The
only newer direct experimental SHR3 paper I found was Myronidi et al. 2023
[PMID:37477900], which is now cached with full text. Later search results were
either database pages, theses, or contextual citations of the 2023 JCB work and
did not alter the GO action calls.
