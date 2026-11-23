# EZR notes

## Scope

- Reviewed the seeded human EZR GOA rows for the PTHR23281 ERM family without refetching UniProt, GOA, publication, PAINT, or Reactome caches.
- `just paint-losses human EZR` reported no IRD or IKR loss on the human EZR lineage, so the EZR rows descending from PANTHER nodes PTN000589933, PTN000589934, and PTN001150648 were judged against the existing PANTHER/PAINT assertions rather than against a recorded EZR-specific loss.

## Key evidence used

- Core cortical ERM activity: Reactome R-HSA-374662 summarizes ezrin as a plasma-membrane to actin-cytoskeleton linker, and R-HSA-443779 records direct C-terminal F-actin binding by ERM proteins.
- Microvilli and apical membrane: PMID:10793131 places ezrin in a placental microvillus cytoskeletal complex, PMID:17825285 places ezrin and radixin at the apical membrane in Caco-2 cells, and PMID:22797597 places ezrin downstream of Rap2A/TNIK/MST4 in brush-border formation.
- Endothelial docking structures: PMID:12082081 supports direct VCAM-1 interaction and apical endothelial colocalization of ezrin and moesin during leukocyte docking; these rows were kept as contextual/non-core adhesion biology.
- Endosomal HOPS function: PMID:21148287 supports direct HOPS/ERM interaction and EGFR delivery to lysosomes, matching the PTN001150648 endosomal process IBAs for canonical EZR/MSN/RDX proteins.
- PKA anchoring: PMID:17911601 and PMID:25097019 support ezrin as an AKAP for PKA type I at lipid rafts through an RI-specifying amphipathic helix.

## Curation calls

- Retained core rows for actin binding, plasma membrane/apical plasma membrane/microvillus/filopodium locations, microvillus and filopodium assembly, cell-shape regulation, and the HOPS-dependent early-to-late endosome terms.
- Removed all 54 bare `GO:0005515` protein-binding rows under the protein-binding policy instead of trying to curate every partner interaction as a molecular function.
- Modified `GO:1903753` negative regulation of p38MAPK cascade to `GO:1900745` positive regulation of p38MAPK cascade with a UniProt `WRONG_TERM` source defect because the Dlg1/EZR TCR paper supports a positive p38 pathway requirement after EZR knockdown, not negative regulation.
- Accepted the NOT `GO:0022612` and NOT `GO:0030014` NHERF1/Caco-2 rows: PMID:24862762 placed both ezrin and moesin at the apical membrane but reported the morphogenesis and establishment-of-apical/basal-polarity defect after moesin depletion rather than ezrin depletion.
- Marked RNA-binding, cadherin-binding HDA, and disordered-domain binding rows as over-annotated because they were not supported by the curated ERM biology in the seeded evidence set.
- Left the ciliary basal body and postsynaptic actin-cytoskeleton Ensembl mouse transfers unresolved pending source-level mouse Ezr review.

## Follow-up

- `GO:0008017` microtubule binding remains `UNDECIDED`; the cached PMID:23857773 abstract foregrounds moesin, and the full-text EZR assay should be checked before either accepting or removing the human EZR row.
- The PTHR23281 family review accepts the broad apical-part node after EZR/MSN/RDX review and still leaves cell adhesion molecule binding, cell-shape regulation, and adherens junction unresolved for Merlin reach. The EZR rows themselves are biologically plausible or seed-backed.
