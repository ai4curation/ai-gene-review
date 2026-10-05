# ced-5 (C. elegans) curation notes

UniProtKB:G5EEN3 (unreviewed TrEMBL entry, 1781 aa), WormBase WBGene00000419, C02F4.1.

Deep-research providers were not available for this review. These notes are a manual synthesis from the
cached publications in `publications/` (most are abstract-only; PMID:20126385, PMID:21527776,
PMID:22801495 and PMID:24225442 have full text cached).

## Identity and domains

- DOCK family (UniProt: "Belongs to the DOCK family"; InterPro IPR026791 DOCK, IPR027007 DOCK-type C2 / DHR-1,
  IPR027357 DOCKER / DHR-2, IPR001452 SH3; PANTHER PTHR45653:SF10 "MYOBLAST CITY, ISOFORM B").
- Orthologue of human DOCK180 and fly Myoblast City [PMID:9548255 "encodes a protein that is similar to the
  human protein DOCK180 and the Drosophila melanogaster protein Myoblast City (MBC)"]. Human DOCK180 rescues
  ced-5 [PMID:9548255 "The expression of human DOCK180 in C. elegans rescued the cell-migration defect of a
  ced-5 mutant"].

## Molecular function

- Bipartite Rac GEF with CED-12/ELMO [PMID:11595183 "CED-12/ELMO-1 binds directly to CED-5/Dock180; this
  evolutionarily conserved complex stimulates a Rac-GEF, leading to Rac1 activation and cytoskeletal
  rearrangements"]; [PMID:20126385 "the CED-12/ELMO-CED-5/DOCK180 complex, which acts as a GEF to activate
  CED-10/Rac"].
- Ternary complex with CED-2/CrkII [PMID:11703940 "CED-12 physically interacts with CED-5 and forms a ternary
  complex with CED-2 in vitro"]. CED-2 binds both a PXXP motif and the N-terminal region of CED-5; the PXXP
  contact is dispensable for rescue [PMID:21616056 "A CED-2 point mutation (F125G) disrupting its interaction
  with the PXXP motif of CED-5 did not affect its rescuing activity"].
- The CED-5 SH3 domain binds the proline-rich motif of CED-12 [PMID:11703939 "interacts physically with CED-5,
  which contains an SH3 domain"], so the SH3 domain binding IPI with CED-12 is reversed for CED-5; changed to
  proline-rich region binding.
- No direct in vitro exchange assay on CED-10 with worm CED-5 found in the cached papers; the GEF activity
  rests on orthology plus the mammalian ELMO/DOCK180 biochemistry and worm epistasis.
- GO:0030676 (Rac GEF activity) is obsolete; GO:0005085 is the most specific valid MF term.

## Processes

- Engulfment of apoptotic cells, acting in engulfing cells [PMID:9548255 "We present evidence that ced-5
  functions in engulfing cells during the engulfment of cell corpses"]; founding genetics [PMID:1936965
  "Electron microscopic studies reveal that mutations in each of these genes prevent engulfment"].
- Distal tip cell migration [PMID:9548255 "ced-5 mutants are defective not only in the engulfment of cell
  corpses but also in the migrations of two specific gonadal cells, the distal tip cells"].
- Wnt input (Cabello 2010, full text): MOM-5/Frizzled, GSK-3 and APR-1 act through CED-2/5/12 in engulfment and
  DTC migration [PMID:20126385 "The epistatic and bypass experiments indeed indicate that MOM-5/Fz activates
  CED-10/Rac through the GEF complex CED-2, CED-5, CED-12"]; [PMID:20126385 "overexpression of both CED-5 and
  CED-10 significantly suppressed the mom-5 DTC migration defect"]. ced-5 single mutants fail to engulf ~70% of
  first-wave embryonic corpses [PMID:20126385 "Approximately 70% of cells dying in the first wave of embryonic
  apoptosis failed to be engulfed in mom-5, ced-5, or ced-10 single mutants"].
- Spindle orientation / left-right: NOT through CED-2/5/12 per the same paper [PMID:20126385 "neither apr-1 nor
  any of the other ced genes showed a strong defect, suggesting that the link to CED-10 may not occur through
  CED-2/5/12 as is the case for engulfment and DTC migration"]; only rare defects in ced-1; ced-5 doubles. So,
  unlike engulfment and DTC migration, the spindle and L/R rows are over-annotations for ced-5 too.
- Gastrulation: partially redundant with hmr-1 [PMID:21527776 "ced-5, which encodes a DOCK180-like guanine
  exchange factor for Rac (Wu and Horvitz 1998) and hmr-1, which encodes a classical cadherin (Costa et al.
  1998), function redundantly in C. elegans gastrulation"]; ced-5 alone gastrulates normally. Non-core.
- Promotion of cell death by engulfment: [PMID:11449278 "mutations in engulfment genes enhance the frequency of
  this cell survival"]; [PMID:11449279 "genes that mediate corpse removal can also function to actively kill
  cells"]. Reddien's abstract lists ced-5 among engulfment genes, but neither abstract says which mutants were
  tested; ced-5-specific support is unconfirmed (both papers abstract-only).

## Clearance-defect / background-genotype rows

- PMID:24225442 (CED-8): ced-5(n1812) used as engulfment background [PMID:24225442 "ced-8(n1891) markedly
  enhanced the cell corpse engulfment defect of the ced-2, ced-5 or ced-12 mutants"]. GO:1902742 rows MODIFY to
  GO:1904747, per the APOPTOSIS project rule.
- PMID:22801495 (cell extrusion, full text): ced-5 is the engulfment-defective comparison; its floaters still
  die by CED-3-mediated apoptosis [PMID:22801495 "cells that undergo CED-3-mediated apoptosis and detach from
  the embryo because they cannot be internalized by engulfing cells"]. No support for ced-5 in apoptosis;
  REMOVE.

## IBA notes

- Myoblast fusion IBA (PTN000594048, seeded by fly mbc and a zebrafish gene): CED-5 is correctly in the DOCK-A
  clade, but C. elegans body wall muscle cells are mononucleate and do not arise by myoblast fusion. REMOVE
  with propagation_review (LINEAGE_OR_TAXON_MISMATCH).
- ced-5 (WB:WBGene00000419) appears among the sources of its own cell migration IBA; that is expected, not
  circular.
