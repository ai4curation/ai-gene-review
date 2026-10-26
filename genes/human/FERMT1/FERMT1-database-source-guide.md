# FERMT1 database evidence

This assessment covers 19 database source contexts. The [decision table](FERMT1-database-decisions.yaml) retains each complete original source object and its zero-based index. The three publication-source groups are assessed separately by the direct-evidence owner. No source identity, product definition or quotation is changed here.

## Orthology sources

The eleven GO_REF:0000107 rows explicitly name mouse Fermt1 P59113 and ENSMUSP00000047616. The actual donor record contains ten matching IMP annotations from [PMID:24681597](../../../publications/PMID_24681597.md) and an actin-filament-binding IDA annotation from [PMID:16876785](../../../publications/PMID_16876785.md). The [propagation evidence](FERMT1-propagation-evidence.yaml) gives the complete matching donor records and acquisition provenance. These remain IEA rows in the human source record.

The 2014 original's Results on adhesion, hair cycling, stem-cell compartments, latent TGF-beta release and Wnt signaling, with Figure 4 and Figure 5 captions, support distinct contextual roles. Mouse perturbations are distinguished from human Kindler-syndrome skin observations. Alpha-v-beta-6-dependent activation of a pre-existing extracellular latent ligand pool supports TGF-beta receptor signaling regulation; it does not establish cytokine biosynthesis or secretion. Nuclear beta-catenin/LEF1 redistribution is positive evidence, but does not isolate nuclear import from stability, export or retention. Wnt-related gene-expression changes have mixed directions. The proposed reviews therefore retain the supported skin signaling roles, refine the production claim, and leave the transport-specific step unresolved.

The complete 2006 article is available in the [author thesis](https://edoc.ub.uni-muenchen.de/8722/1/Wang_Hao-Ven.pdf), at journal pages 3142–3151. Operative Methods/Results and the Figure 6 caption describe tagged mouse Kindlin-1 microscopy and colocalization with adhesions and actin-associated structures. That evidence does not distinguish direct actin binding from indirect association. The historical construct is described as 637 residues and was not sequence-remapped to current P59113. The generated normal remains abstract-only; separate original access is recorded accurately. Original figure pixels were not independently inspected.

## PAINT

[FERMT1-phylogeny-evidence.yaml](FERMT1-phylogeny-evidence.yaml) records actual family membership and three literal positive IBD joins. PTHR16160 has the official name FERMITIN 2-RELATED; the human member belongs to PTHR16160:SF12, FERMITIN FAMILY HOMOLOG 1. The official labels are preserved, even though the family name foregrounds another member. The exact PAINT node/term/donor strings match the accepted TSV. The target's presence among its own descendant sources is expected.

The target gene-info, tree and MSA requests timed out. Literal IBD matches are not a reconstructed target-to-node path or an alignment proof. The annotations are retained because the curated inheritance assertion is consistent with independently recovered human function; access failure is not evidence of target-specific loss. No donor-count heuristic is used.

## Human mechanism and mapped locations

The original [PMID:14634021](../../../publications/PMID_14634021.md) was recovered through an [author upload](https://www.researchgate.net/publication/6742348_The_Kindler_Syndrome_Protein_Is_Regulated_by_Transforming_Growth_Factor-_and_Involved_in_Integrin-mediated_Adhesion). Relevant Methods, localization/ruffle Results and Figures 4–6, and integrin-tail association/spreading Results and Figures 8–9 were read. Endogenous human localization supports focal adhesions and stimulus-dependent ruffles. The integrin-tail assay uses a human-kindlin-containing lysate; it is not recast as an isolated binary affinity measurement. The reported lack of activation by kindlin alone is distinct from later talin-cooperation evidence. Figure captions/text, not original pixels, were inspected.

The actual [PMID:19804783](../../../publications/PMID_19804783.md) Results sections on integrin activation and focal-adhesion targeting, corresponding Methods and Figures 4–5 captions distinguish human full-length/artificially deleted functional constructs in CHO cells from the mouse purified structural F0 domain. Artificial F0/DeltaF0 constructs are not natural splice isoforms.

GO_REF:0000044 is the Swiss-Prot subcellular-location mapping: SL-0090 cytoskeleton and SL-0301 ruffle membrane. GO_REF:0000120 also includes SL-0118 focal adhesion and the mouse orthology evidence. These are not HPA assays. The inspected HPA XML did not supply a cell-line subcellular-location assay for these precise sites. Broad histological cytoplasmic/membranous staining is not promoted to precise organelle evidence.

## Electronic function and hierarchy

The actual target-specific InterPro response maps IPR037837 to residues 370–493 and IPR037843 to 3–676, both with integrin-signaling GO:0007229. Target functional evidence corroborates the mapping; domain presence does not establish every paralog's developmental role.

The actual ARBA00028907 consequent is positive regulation of cell migration. Its alternative family/taxon conditions were inspected, but target-specific rule satisfaction was not independently recomputed. Official GO gives the strict relation GO:1903691 is_a GO:0030335. The TOO_GENERAL decision for broad migration depends on preserving the direct lane's positive wound-spreading row 29; it does not reject migration. Conversely, the focal-adhesion-to-cytoskeleton query returned no strict is_a/part_of path, so the cytoskeleton location is not discarded using that hierarchy argument.

## Products and limits

The [product map](FERMT1-database-product-map.yaml) preserves the four official splice sequences and their exact accepted reconstruction results. The full-length chain feature is not remapped into a new processed product. No common activity is asserted for every shortened product; artificial laboratory deletions and historical mouse constructs remain separate from natural human products.

All 19 intake normal caches remain unchanged. Only actually used source dependencies are selected for this lane, with exact main reuse for PMID24681597 and a genuine additional repository fetch for PMID16876785. Source records, captions and cached abstracts are not rewritten. No new supporting-text quotation or annotation is introduced.
