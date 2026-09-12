# PSAP (Prosaposin) review notes

UniProtKB: P07602 (SAP_HUMAN), HGNC:9498, gene PSAP (syn. GLBA, SAP1). 524 aa precursor.

Deep research: falcon provider is OUT OF CREDITS (HTTP 402); no `-deep-research-falcon.md`
was generated. Review grounded in `PSAP-uniprot.txt`, the seeded GOA (`PSAP-goa.tsv`),
and cached `publications/PMID_*.md` (all 23 GOA-cited PMIDs are cached).

## Core biology
Prosaposin is the **precursor of four saposins (A, B, C, D)** — small (~80 aa), heat-stable,
non-enzymatic lysosomal **sphingolipid-activator proteins** produced by sequential proteolytic
cleavage of prosaposin in the lysosome. Each saposin binds/extracts a membrane glycosphingolipid
and presents it to the cognate acid hydrolase:
- Saposin A -> galactosylceramidase (GALC, EC 3.2.1.46); patient SapA deficiency phenocopies Krabbe (KRBSAPA).
- Saposin B -> arylsulfatase A (ARSA, sulfatide), beta-galactosidase (GM1), alpha-galactosidase A (Gb3); SapB deficiency = MLD (MLDSAPB).
- Saposin C -> acid beta-glucosidase/glucosylceramidase (GBA1); also protects GCase from proteolysis; SapC deficiency = atypical Gaucher (GDSAPC).
- Saposin D -> acid ceramidase (ASAH1) and acid sphingomyelinase.
[file:human/PSAP/PSAP-uniprot.txt FUNCTION lines 502-538]

Intact secreted prosaposin is also a **neurotrophic/myelinotrophic factor** acting through
GPCRs GPR37 and GPR37L1 (ERK signaling) [UniProt FUNCTION 511-515; PMID:10383054].

Localization: **Lysosome** (SUBCELL 560-561) and **Secreted** as a 70 kDa glycoprotein
(SUBCELL 562-565). Sortilin/SORT1 mediates lysosomal targeting (C-terminus).

Disease: complete PSAP loss = combined saposin deficiency (PSAPD, MIM 611721), fatal storage
disorder in infancy. Individual saposin deficiencies phenocopy the cognate enzyme disease.
PARK24 (autosomal dominant Parkinson) from SapD-domain variants.

## Chosen core_functions terms (verified current via OLS)
- MF **GO:0030290 sphingolipid activator protein activity** — def: "Any of a group of peptide
  cofactors of enzymes for the lysosomal degradation of sphingolipids. They stimulate various
  enzymes, including glucosylceramidase, galactosylceramidase, cerebroside-sulfatase,
  alpha-galactosidase, beta-galactosidase, and sphingomyelin phosphodiesterase." This is the exact
  non-catalytic activator MF for saposins (do NOT assign a catalytic/EC activity).
- BP **GO:0046479 glycosphingolipid catabolic process** (current) / GO:0030149 sphingolipid catabolic process.
- CC **GO:0005764 lysosome** / GO:0043202 lysosomal lumen (both in GOA), plus GO:0005576 extracellular region.

Note: GOA MF for PSAP is spread across lipid/ganglioside binding (GO:0008289 lipid binding IEA;
GO:1905573-77 ganglioside binding IDA; GO:0005543 phospholipid binding IDA; GO:0030882 lipid
antigen binding IBA) plus protein-binding IPIs. GO:0030290 is NOT currently in the GOA TSV but is
the most informative activator MF; added as a core_functions MF (author-supplied, validated).

## Key verbatim-quote sources (grep-verified in cache)
- Ganglioside binding/transport: PMID:1454804 (abstract).
- SapC phospholipid/membrane binding: PMID:14674747.
- Saposin homodimerization: PMID:18462685.
- PSAP<->progranulin lysosomal trafficking: PMID:26370502, PMID:28541286, PMID:28835281.
- PSAP regulates progranulin levels/oligomerization: PMID:27356620.
- SapC deficiency & autophagy: PMID:22949512.
- Prosaposin processing by mesotrypsin/caspase-14 (protease binding): PMID:24872419.

## Annotation-specific judgments
- Lysosome / lysosomal lumen / extracellular region CC: all ACCEPT (well supported, multiple lines).
- IBA lipid metabolic process (GO:0006629) ACCEPT; IEA sphingolipid metabolic process (GO:0006665)
  MODIFY -> glycosphingolipid catabolic process is more informative but keep essence; I ACCEPT the
  KW-based process terms as broadly correct and add specific core_functions.
- GO:0030882 lipid antigen binding (IBA): saposins do present lipid antigens (CD1); KEEP_AS_NON_CORE.
- GO:0060736 prostate gland growth (IBA), GO:0007193 adenylate cyclase-inhibiting GPCR pathway (IBA),
  GO:0019216 regulation of lipid metabolic process (IBA): non-core secreted-prosaposin/GPR37 roles ->
  KEEP_AS_NON_CORE.
- GO:0010467 gene expression (IEA ARBA; IDA/IMP PMID:27356620): the ARBA IEA is a vague/spurious
  mapping -> MARK_AS_OVER_ANNOTATED. The IDA/IMP (PMID:27356620) are experimental (PSAP regulates
  PGRN levels); keep but non-core, "gene expression" is a coarse term for a post-translational
  effect -> KEEP_AS_NON_CORE with note.
- Bare protein binding IPIs (GO:0005515): MARK_AS_OVER_ANNOTATED (uninformative), never REMOVE.
- GO:0097110 scaffold protein binding (PMID:23555801): cached paper is about BANK1/BLK/PLCg2 and does
  NOT mention PSAP; cannot verify -> MARK_AS_OVER_ANNOTATED + reference_review flag (likely wrong paper).
- GO:0002020 protease binding (PMID:24872419): experimental IPI, prosaposin interacts with
  caspase-14/mesotrypsin during processing -> ACCEPT (non-core).
- Lysosomal transport (GO:0007041) IMP/IDA (PMID:26370502, 28541286, 28835281): experimental; PSAP
  mediates progranulin lysosomal delivery -> ACCEPT (non-core, moonlighting chaperone role).
- Ganglioside binding GO:1905573-77 + GM1 transport GO:1905572 (IDA PMID:1454804): ACCEPT.
- GO:0042803 protein homodimerization (IDA PMID:18462685): saposin dimers -> ACCEPT.
- GO:0010506 regulation of autophagy (TAS PMID:22949512): downstream consequence of SapC deficiency ->
  KEEP_AS_NON_CORE.
- Exosome / plasma membrane / azurophil granule membrane CC (HDA/TAS): secreted-protein
  proteomics detections -> KEEP_AS_NON_CORE.
- ISS extracellular region (Q61207 mouse ortholog; F1SU97): ACCEPT.
