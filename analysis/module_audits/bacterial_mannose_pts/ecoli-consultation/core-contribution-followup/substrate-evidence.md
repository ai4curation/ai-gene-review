# ManX coupled-transporter substrate scope

Read 2026-11-07. PMID9864311 was newly fetched normally; its cache is abstract-only and remains unchanged. Full primary text was separately acquired from https://pmc.ncbi.nlm.nih.gov/articles/PMC103530/?report=xml and also read at https://journals.asm.org/doi/10.1128/jb.181.1.47-54.1999 . Full HTML/text stays in ignored cache.

Figure1 exact excerpt:

> GlcNAc is transported by both the manXYZ -encoded transporter and its own specific transporter, encoded by nagE , producing intracellular GlcNAc-6-P

This is the paper’s pathway synthesis, not a new purified ManX assay. Methods additionally establish that manXYZ disruption in a nagE background prevents GlcNAc growth; the article uses several E. coli K-12 backgrounds listed in Table1, not a claim all assays used MG1655. The figure explicitly identifies the GlcNAc6-phosphate endpoint and therefore independently resolves the product specificity required by GO0022880.

The separately preserved2019 source excerpt documents the established glucose, mannose, fructose and amino-sugar repertoire. PMID2681202 directly assigns sugar phosphate transfer from ManX EIIB His175; the full transport reaction requires membrane partners. Current QuickGO GO0022855 and GO0022877 require histidyl donor and glucose/fructose phosphate without specifying the phosphorylated carbon. No fructose1-versus6 inference is manufactured. GO0022880 explicitly specifies GlcNAc6-phosphate and is supported by Figure1. All three are descendants of GO0008982 and GO0016773; the existing kinase replacement remains a reaction-specific interpretation, not a newly claimed kinase ancestry.
