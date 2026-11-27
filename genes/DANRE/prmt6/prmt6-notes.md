# prmt6 (Danio rerio) review notes


## Batch 05 curation notes
- Core interpretation: prmt6 encodes a nuclear protein arginine methyltransferase that catalyzes asymmetric dimethylation of protein and histone arginine residues, including H3R2, H2AR3, and H4R3. The core function is nuclear/chromatin-associated protein arginine methyltransferase activity; developmental retina/glial annotations are downstream phenotypic contexts.
- Key UniProt support: Arginine methyltransferase that can catalyze the formation of both omega-N monomethylarginine.
- Existing GOA annotations were reviewed against this core role; broad, inferred, or downstream phenotype annotations were kept as non-core unless they overstate the direct function.

## Re-review 2026-09-29

Re-reviewed all 26 GOA rows against UniProt Q6NWG4 and the three cached papers; replaced the
templated "is supported for prmt6" blocks and dropped deep-research quotes that merely paraphrased
UniProt. Removed one stale yaml row (GO:0006338 IEA GO_REF:0000120) that is no longer in GOA.

- Resolved 4 PENDING IBA rows (PTN008510054): GO:0016274, GO:0042054 ACCEPT (the zebrafish gene is
  itself among the node's experimental descendants, which is expected, not circular); GO:0006355
  ACCEPT; GO:0006338 chromatin remodeling ACCEPT rather than the earlier MARK_AS_OVER_ANNOTATED,
  because Prmt6 itself installs the H3R2me2a mark that reorganizes chromatin state
  [PMID:26487724 "application of which led to early epiboly defects and significantly reduced the
  level of H3R2me2a marks. prmt6 mRNA could rescue the epiboly defects and the H3R2me2a reduction
  in the prmt6 morphants"] and GO's definition is not restricted to ATP-dependent remodelers.
- Core activity: GO:0035242 (IEA Rhea/EC, ISS x2) and GO:0070611 (IEA, IMP, ISS) ACCEPT; the IMP is
  the only direct zebrafish activity evidence (morphant loss, mRNA rescue). GO:0035241 ISS ACCEPT
  (obligatory first step). GO:0008757 ISS (2004 orthology paper, PMID:15475159) MODIFY to
  GO:0035242.
- GO:0010468 IEA (ARBA) MODIFY to GO:0045892, matching the zebrafish promoter evidence
  [PMID:26487724 "the results of ChIP quantitative real time PCR and luciferase reporter assay
  indicated that gadd45 α a is a repressive target of Prmt6"]. GO:0010629 IMP and GO:0045892 ISS
  ACCEPT.
- GO:0042393 histone binding ISS changed KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED (substrate
  contact already implicit in the methyltransferase terms). H4R3/H2AR3 ISS stay KEEP_AS_NON_CORE.
- GO:2000059 ISS (mouse donor) KEEP_AS_NON_CORE: downstream consequence of non-histone substrate
  methylation, no zebrafish evidence, donor is experimental so not removed.
- GO:0021782 / GO:0060041 IMP (PMID:30924555, F0 CRISPR Muller glia screen) KEEP_AS_NON_CORE
  [PMID:30924555 "prmt6 mutants have defects in cell body position and ILM."].
- Localization: nucleus rows now cite the SUBCELLULAR LOCATION line and the ChIP result, not the
  FUNCTION line.
- Description rewritten without curation commentary; core_functions now cite primary literature.
- Validation: zero errors, zero warnings.
