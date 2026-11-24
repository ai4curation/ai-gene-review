# hsp10 notes

## 2026-11-24

- Seeded `genes/SCHPO/hsp10` with `just fetch-gene SCHPO hsp10`.
- Cached GOA PMIDs with `just fetch-gene-pmids SCHPO hsp10`; only `PMID:16823372` was present and it was already cached.
- Ran `just mod-description-deep-research SCHPO hsp10`; SCHPO is skipped because no MOD description provider is configured.
- Tried `just deep-research-falcon SCHPO hsp10 --fallback perplexity-lite`; both providers failed because only `claude_code` is available to `deep-research-client` in this environment. Wrote `hsp10-deep-research-manual.md` from cached primary literature instead.
- Ran `just paint-losses SCHPO hsp10`; no IRD or IKR lies on the hsp10 lineage.

### Review decisions

- Accepted the conserved mitochondrial Cpn10/Hsp10 role: binding Hsp60/Cpn60, contributing to its protein-folding chaperone activity, and supporting mitochondrial protein folding in the matrix.
- Removed `GO:0005524 ATP binding`: ATP binding and hydrolysis are properties of Hsp60/Cpn60, while Hsp10/Cpn10 regulates the cycle.
- Kept `GO:0030150 protein import into mitochondrial matrix` as non-core pathway context. hsp10 acts on imported matrix proteins after translocation rather than driving membrane crossing itself.
- Marked `GO:0046872 metal ion binding` over-annotated. PAINT transfers it from the PTHR10772 root based on a single Mycobacterium tuberculosis Cpn10 crystal structure; no fission- or budding-yeast evidence establishes metal binding as a mitochondrial Hsp10 function.

### GO-CAM consistency queue

- Add a final consistency note after the gene PRs merge: the Hsp10 GO-CAM activity is biologically consistent with the hsp10 review, but both the GO-CAM enabled_by ISO and the PomBase GOA ISO row cite `SGD:S000000004` as their budding-yeast donor. That identifier is SSA1/YAL005C; the S. cerevisiae ortholog for S. pombe hsp10 is HSP10/YOR020C, `SGD:S000005546`.
