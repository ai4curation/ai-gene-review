# ift-139 (Q20255, ZK328.7) notes

## Provenance and process
- Accession: Q20255 (Swiss-Prot, 1324 aa, TTC21B/IFT139 ortholog); the only UniProt entry for the gene.
- Deep research: `just deep-research-falcon worm ift-139 --fallback perplexity-lite` failed (falcon timed out at 600 s; the perplexity fallback provider is not available in this environment). No deep-research file was written. The review uses cached publications and PubMed searches instead.

## Key findings
- Expressed only in ciliated neurons; IFT-139::GFP sits at the ciliary base and in cilia, with a weak diffuse dendritic signal [PMID:27515926 "IFT-139 is expressed in ciliated neurons and localises to basal bodies and cilia"].
- Moves on IFT trains [PMID:27515926 "Many IFT-139::GFP-positive particles were bidirectionally moving in the cilia"].
- Retrograde role from epistasis [PMID:27515926 "ift-139 mutations phenocopied che-3 but not klp-11 mutations"].
- Redundant with IFT-43 for dynein-2 motility [PMID:28479320 "IFT-A subunits IFT-139 and IFT-43 function redundantly to promote dynein-2 motility"].
- Ciliary gating [PMID:30293716 "IFT-43/121/139 controlling their ciliary removal"].
- Niwa 2016 calls ifta-1 "IFT122"; IFTA-1 is actually IFT121/WDR35 (daf-10 is IFT122).

## Curation decisions
- 9 GOA rows: 8 ACCEPT, 1 KEEP_AS_NON_CORE (dendrite IEA).
- 1 NEW row: ciliary basal body (IDA, PMID:27515926). UniProt records this location but GOA does not.
- Core MF is GO:0005198 structural molecule activity, matching the che-11, daf-10 and dyf-2 reviews.
