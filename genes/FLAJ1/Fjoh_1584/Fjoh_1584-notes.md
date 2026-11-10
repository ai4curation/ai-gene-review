# FLAJ1/Fjoh_1584 evidence notes

## Evidence review — 2026-11-07

The primary source and structure/accession checks are documented in analysis/module_audits/bacterial_heptaprenylglyceryl_ether_lipid/comparative-members/identity-and-scope.md and immutable official mapping snapshots. All original GOA payloads are preserved. The glycerophospholipid definition includes mono-O-alkyl glycerophosphate, so direct ether synthesis supports the broad biosynthetic process without assigning a complete downstream native pathway.

Actual Falcon research was attempted with `just deep-research FLAJ1 Fjoh_1584 --provider falcon` but returned403 authentication failure. No report was invented. Primary PubMed/official PDB searches and cached full-text or curated experimental evidence support this manual review. The PAINT-loss command reported the accession absent from the family tree; it cannot establish absence of lineage losses.

A5FJK8 is the UW101 group II C20 GGGPS represented in4JEJ, not the archaeal4MM1 protein. The curated experimental record supplies the substrate-specific reaction and the mutant result [UniProt A5FJK8, “I->A: Accepts HepPP as substrate.”]. Ile90 mutagenesis expands donor length; it does not convert wild-type activity into a C35 PcrB claim. The record's PTHR21235 broad family label is dominated by HisF, while the subfamily and experimental data identify GGGPS. GO0000107 catalyzes a different glutamine-dependent histidine-biosynthetic reaction; its TreeGrafter transfer is removed with a source defect, not a fictional negative biochemical assay. Cytoplasm remains UNDECIDED: a soluble recombinant structure alone does not localize the native protein.

### Primary-access follow-up

PMID24684232 publisher full text was subsequently obtained and independently read at https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.12596 . Its Figure2 uses a Bacillus delta-pcrB assay host. Figure5 distinguishes fjGGGPS I90A from wild type; groupII magnesium is modeled, not observed density. The local abstract cache remains unchanged. The separate full-text-scope note records these boundaries.


## PR6167 round1 evidence correction — 2026-11-07

Twenty-four copies of the I90A sentence were an authoring artifact, not independent evidence. Remove triplication and keep one copy only in each of the two specific-MF rows and the core where mutant-versus-wild-type specificity is discussed. The HisF REMOVE and source defect instead use the established GGGPS reaction plus the independently checked structural-relative distinction in the publisher scope note. The chemical BP and broad-MF refinements use the cached primary abstract's ether-formation statement, not an off-target mutation. All eight original row payloads and actions remain unchanged.

The full publisher text was read again at https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.12596 on 2026-11-07. Results compare HisF by DALI structural similarity, not catalytic equivalence. The GGGPS reaction itself is independently recorded in the target's curated experimental FUNCTION statement. Native feeding experiments were unsuccessful and the paper leaves the physiological role unresolved. Figure 2 tests long donors in a Bacillus deletion host; Figure 5 tests an engineered fjGGGPS mutant. These do not establish native downstream processing. Row-specific reasons now state only relevant evidence; the knowledge gap concerns native C20 product fate, without unrelated sugar-loading or carrier-bypass wording.

Cytoplasm remains UNDECIDED because native location is unresolved, not because full text is unavailable. Soluble recombinant purification or lack of transmembrane segments is insufficient. The official HAMAP MF_00112 rule places cytoplasm only in its archaeal branch, not the Bacteroidota branch. Bacillus PcrB has additional explicit cytosolic-pathway context in PMID:40626731, so its different decision need not be imposed on this target.
