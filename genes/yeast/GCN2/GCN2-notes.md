# GCN2 (YDR283C, P15442) review notes

## Literature search (2026-11-04)

No deep-research provider was available. Sources checked:

- SGD curated description (`GCN2-deep-research-sgd.md`, via `just mod-description-deep-research yeast GCN2`).
- UniProt P15442 curated free text (FUNCTION, SUBUNIT, PTM, DOMAIN, DISRUPTION PHENOTYPE).
- All 22 GOA-cited publications cached by `just fetch-gene-pmids yeast GCN2` (all abstract-only in the cache).
- Attempted full text of PMID:21849502 (PMC3196070) via Europe PMC and the BioC OA service: not retrievable (HTTP 500 / not in OA subset).
- Reactome R-SCE-9633467, R-SCE-9633480, R-SCE-9633750.
- Context only: integrated stress response module, gcn2_variant annoton (module proposed in ai4curation/ai-gene-review#5904).

## Findings

- GCN2 is the only eIF2alpha kinase of budding yeast; it phosphorylates eIF2alpha (Sui2) Ser51 (UniProt Ser-52) in starved cells, which mediates GCN4 translational derepression [PMID:1739968 "In vitro, GCN2 specifically phosphorylates the alpha subunit of rabbit or yeast eIF-2"; "Substitution of Ser-51 with alanine eliminates phosphorylation of eIF-2 alpha by GCN2 in vivo and in vitro and abolishes increased expression of GCN4"].
- Activation by uncharged tRNA via the HisRS-like domain plus C-terminal domain [PMID:10983975 "GCN2 bound several deacylated tRNAs with similar affinities, and aminoacylation of tRNAphe weakened its interaction with GCN2"; PMID:7623840 "uncharged tRNA can bind to the synthetase-related domain of GCN2"].
- Requires GCN1/GCN20 [PMID:7621831 "GCN1 and GCN20 are components of a protein complex that couples the kinase activity of GCN2 to the availability of amino acids"; PMID:11101534].
- Ribosome association, loose (salt-sensitive), via C-terminus [PMID:2038314 "GCN2 could be dissociated from 60S subunits by 0.5 M KCl, suggesting that it is loosely associated with ribosomes rather than being an integral ribosomal protein"]; C-terminal DRBD-like segment binds dsRNA in vitro [PMID:9430731].
- Dimerization [PMID:9566889]; autophosphorylation [PMID:2188100]; conserved salt bridge for activation [PMID:17202131].
- Responds to purine limitation too [PMID:8336737].
- Phosphorylates Kog1 to down-regulate TORC1 [PMID:28057755 "Gcn2 binds to TORC1 and phosphorylates Kog1, the unique regulatory subunit of TORC1, resulting in down-regulation of TORC1 kinase activity"].
- G1/S DNA-damage checkpoint role (abstract-less cache) [PMID:17890903 title].
- eEF1A binds Gcn2 CTD and inhibits it [PMID:21849502]. GOA row GO:0031369 translation initiation factor binding WITH P38912 (TIF11/eIF1A) from this paper; the abstract only names eEF1A (an elongation factor). UniProt SUBUNIT text also says "TIF11" for this interaction. Possible eEF1A/eIF1A conflation; full text not available, left UNDECIDED.

## Decisions summary

Core: GO:0004694 eIF2alpha kinase activity; GO:0140469 GCN2-mediated signaling; tRNA binding (sensor); ribosome binding; cytosol.
