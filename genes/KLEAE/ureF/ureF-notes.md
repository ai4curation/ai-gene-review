# ureF (P18318) notes -- Klebsiella aerogenes urease accessory protein UreF

Deep research: `just deep-research KLEAE ureC --provider perplexity` was attempted once (2026-10-23) and failed ("Provider 'perplexity' not available. Available: falcon, openscientist"). No deep-research file was generated for any KLEAE ure gene; this review relies on cached primary literature and the reviewed UniProt entry.

- UreF surface residues define the UreG binding site; nine variants give <10% activity [PMID:22369361 "cell-free extracts of nine site-directed mutants had less than 10% of the wild-type urease activity"].
- UreF gates UreG GTPase rather than acting as a GAP [PMID:22369361 "UreF gates the GTPase activity of UreG to enhance the fidelity of urease metallocenter assembly"].
- UreF alters UreD-urease conformation [PMID:7721685 "we propose that UreF alters the conformation of the UreD-urease complexes"]; UreF C-terminus needed for complex, N-terminus for activation [PMID:17041056].
- Decisions: GO:0005515 REMOVE; cytoplasm ACCEPT; nickel binding (UniRule) MARK_AS_OVER_ANNOTATED (no direct measurement; PSEPK used REMOVE); NEW GO:0018237 (core), GO:0030695 (second core), GO:0150006, GO:0043419.
