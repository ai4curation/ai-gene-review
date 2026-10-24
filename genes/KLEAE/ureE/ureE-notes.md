# ureE (P18317) notes -- Klebsiella aerogenes urease accessory protein UreE

Deep research: `just deep-research KLEAE ureC --provider perplexity` was attempted once (2026-10-23) and failed ("Provider 'perplexity' not available. Available: falcon, openscientist"). No deep-research file was generated for any KLEAE ure gene; this review relies on cached primary literature and the reviewed UniProt entry.

- Cytoplasmic (immunogold); dimer binds ~6 Ni (Kd 9.6 uM), His-rich sites; proposed nickel donor [PMID:8318889 "We hypothesize that UreE binds intracellular nickel ion and functions as a nickel donor during metallocenter assembly into the urease apoprotein."].
- ureE deletion gives partially active urease [PMID:1624427 "or only partially active (deletions in ureE)"].
- Not required for UreD-urease complex formation [PMID:7721685 "The ureE, ureF, and ureG gene products were found not to be required for formation of the UreD-urease complexes"].
- Decisions: nickel binding, cytoplasm ACCEPT; protein folding and protein-containing complex assembly REMOVE (InterPro2GO over-propagation); urea metabolic process MODIFY -> GO:0043419; NEW GO:0170061 nickel chaperone activity (TAS, PMID:22369361) as second core function, primary core = GO:0016151 per module design.
- Note: the task brief listed P17317; the actual accession in the UniProt file is P18317.
