# ARGAH1 and ARGAH2 matrix-localization evidence

Canonical paper: PMID:18567826, Flores et al. (2008),
[Arginase-negative mutants of Arabidopsis exhibit increased nitric oxide signaling
in root development](https://doi.org/10.1104/pp.108.121459).

The original paper tests the two Arabidopsis proteins as myc-tagged constructs
in tobacco BY-2 cells. These are heterologous localization experiments with the
target proteins, not native Arabidopsis fractionation. E1β marker colocalization
and selective digitonin permeabilization resolve the internal mitochondrial pool.
They do not exclude a distinct chloroplast pool under other conditions.

Normal PMID refresh and full-text warming did not recover the body into the PMID
cache. This script extracts the exact inspected passage from the normally cached
PMC source; it never edits a source cache. Reproduce from the repository root:
`uv run python genes/ARATH/ARGAH1/ARGAH1-source-analysis/extract_localization.py`.

Source SHA256: `8ea67fd0a52dc1ba97227c9235db269350b4f2052f539fb3f966102a68cb218f`.

## Verbatim Results passage accompanying Figure 2

> As shown in Figure 2, immunofluorescence microscopic analysis revealed that both myc-tagged ARGAH1 and ARGAH2 colocalized exclusively with the endogenous E1β-subunit of the pyruvate dehydrogenase complex, a well-known mitochondrial matrix marker protein (Luethy et al., 1995). Neither mock transformation nor omission of anti-myc and/or anti-E1 antibodies yielded immunofluorescence (data not shown). Neither myc-tagged ARGAH1 nor ARGAH2 was immunodetected in transformed tobacco cells permeabilized with digitonin rather than Triton X-100 (data not shown). Therefore, each protein was actually localized in the mitochondrial interior (matrix), since digitonin permeabilizes only the plasma membrane and only cytosolically exposed antigens are accessible to the applied anti-myc IgGs.

## Curation consequence

Retain the informative mitochondrial organelle assertions. Add the experimentally
resolved matrix location alongside them for both paralogs; do not substitute the
subcompartment for the organelle or convert a paper title into localization evidence.

## Additional cited Results passages

> T-DNA disruption mutant argah1-1
