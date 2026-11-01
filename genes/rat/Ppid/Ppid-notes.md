# Ppid (rat) review notes

## Session 1 (2026-10-28)

- Fetched with `just fetch-gene rat Ppid`; UniProt Q6DGG0 (PPID_RAT, RGD:1303174,
  GeneID 361967) confirmed; 45 GOA rows.
- No deep-research API key; literature compiled by hand in Ppid-deep-research-manual.md.
- Key finding: the RGD experimental rows from PMID:12077116 and PMID:19832699 are about
  mitochondrial cyclophilin D (Ppif, P29117, RGD:628670), not cyclophilin 40. UniProt
  carries a CAUTION about exactly this confusion. 19832699 full text read: CyP-D
  is "a mitochondrial isoform that facilitates formation of the permeability transition
  pore in the mitochondrial inner membrane"; CyP40 not mentioned. 12077116 is abstract-only
  (JBC fetch blocked, 403), so its rows are UNDECIDED with PROBABLE WRONG_GENE_PRODUCT
  source defects rather than REMOVE.
- PMID:9488468 (abstract only): Cyp40 co-precipitates with mutant p53 together with hsp90,
  hsp70 and p23 (A1-5 rat cells); RGD IPI "enzyme binding" with Ptges3 (p23). The abstract
  shows co-complex membership, not a direct Cyp40-p23 contact -> UNDECIDED.
- Human GO:0000122 negative regulation of transcription by RNA pol II IMP rests on
  PMID:18708059, which shows CyP40 knockdown reduces AHR-driven CYP1A1/CYP1B1 induction
  (positive role). Rat ISO/ISS rows MODIFY to GO:0045944 with REGULATORY_SIGN_INVERSION;
  source defects logged for RGD (ISO) and UniProt (ISS).
- HCV-derived terms (lipid droplet organization, positive regulation of protein secretion,
  positive regulation of viral genome replication) are siRNA host-factor phenotypes in a
  human hepatoma HCV model; marked as over-annotated for rat.
- Core functions: PPIase activity; Hsp90-binding TPR co-chaperone (Hsp90 protein binding)
  with chaperone (holdase) activity in protein folding.
