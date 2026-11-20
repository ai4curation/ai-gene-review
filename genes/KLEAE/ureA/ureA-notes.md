# ureA (P18316) notes -- Klebsiella aerogenes urease gamma subunit

Deep research: `just deep-research KLEAE ureC --provider perplexity` was attempted once (2026-10-23) and failed ("Provider 'perplexity' not available. Available: falcon, openscientist"). No deep-research file was generated for any KLEAE ure gene; this review relies on cached primary literature and the reviewed UniProt entry.

- Urease is an (alpha beta gamma)3 trimer; the binickel center is in the alpha (UreC) subunit [PMID:8718850 "is an (alpha beta gamma)3 trimer with each alpha-subunit having an (alpha beta)8-barrel domain containing a binickel active center"].
- Gamma subunit is half buried in the assembly, supporting a structural role [PMID:8718850 "50% in the gamma-subunit"].
- ureA is one of three structural genes required for active urease [PMID:7909161 "requires the presence of three structural genes for the apoprotein (ureA, ureB, and ureC)"].
- Decisions: 3x GO:0005515 IPI (UreA-UreC, structures/native MS) REMOVE per protein-binding policy; nickel binding IEA REMOVE (no Ni ligands in UreA); urease activity IEA MARK_AS_OVER_ANNOTATED (contributes_to); urea metabolic process MODIFY -> GO:0043419; NEW urease complex and structural molecule activity (mirrors PSEPK ureA).
