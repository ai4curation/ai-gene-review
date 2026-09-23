# Mst27D / Q8IPI4

Q8IPI4 is the 424-residue Mst27D product. [PMID:37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/), DOI https://doi.org/10.1371/journal.pgen.1010837, uses Mst27D-PA and explicitly defines the C-terminal region as residues 151–424, consistent with the selected full-length model. Full text was inspected. It directly distinguishes intact Mst27D lattice binding from EB1 plus-end tracking, and native postmeiotic expression from premature expression caused by SV40-terminated transgenes. These are biological grounds to challenge specific EB1-derived IBA transfers rather than donor-count arguments. Nine original GOA rows are retained with one new bundling annotation. ProtNLM microtubule binding is CNN; a questionable finer GOA annotation is not used to force LSP.

## Sequence and research provenance

The selected frozen UniProt record is retained in [Mst27D-uniprot-source.json](Mst27D-uniprot-source.json), with the complete original prediction metadata in [Mst27D-predictions-source.json](Mst27D-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

## Completed provider readback

The wrapper timed out and its fallback reported insufficient quota, but the original Falcon job later produced a complete report. The report and primary sources were inspected; no duplicate provider submission was made. The report supports Nup358 linkage and lattice-wide binding. Its mention of meiotic spindle enrichment must be interpreted with the primary study’s explicit correction for premature expression from SV40-terminated constructs. The endogenous-terminator and antibody experiments establish native accumulation after meiosis.


## Full annotation re-review — 2026-09-20

Re-read all 10 annotation rows and the existing Falcon report against the full primary study PMID:37428798. Fetched and inspected PTHR10623 PAINT: the eight original IBA rows trace to eukaryotic PTN000065701. The primary paper supports native postmeiotic expression, direct microtubule binding/bundling and Nup358 recruitment. The existing NEW bundling term is retained on biochemical/cellular assembly evidence plus stage-resolved mutant/rescue data, not solely on a fertility phenotype.

Plus-end binding/location remain UNDECIDED pending focused adjudication: "Mst27D binds all along MTs, contrasting with Eb1’s preference for growing MT plus ends" demonstrates altered preference, whereas GO:0051010 requires binding and does not specify preference. The comet-forming construct was the isolated C-terminal region, not a protein lacking the C terminus; the authors discuss possible heterodimerization with endogenous EB-family proteins. MTOC localization is assessed separately from spindle midzone, because GO:0005815 includes nucleating/anchoring structures outside mitosis. Polymerization/depolymerization regulation remains unresolved because the demonstrated bundling mechanism does not by itself adjudicate dynamic regulation.

The spindle-assembly rejection remains supported by target-specific native timing ("endogenous Mst27D accumulation starts after meiosis in early spermatids") and null analysis ("Until after meiosis, abnormalities were not detectable."). Midzone remains cautiously over-annotated. This is a branch/context challenge, not an argument from sparse or distant donors.
