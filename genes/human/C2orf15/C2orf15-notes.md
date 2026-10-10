# C2orf15 notes

## 2026-10-08 Tier 4 microprotein review

### Locus
- UniProt Q8WU43 (CB015_HUMAN), "Uncharacterized protein C2orf15", 91 aa, PE1. Single
  domain annotation: Pfam PF17701 / InterPro IPR041537 DUF5547 (domain of unknown function).
  No transmembrane segment or signal peptide annotated; no FUNCTION or SUBCELLULAR LOCATION
  comment. N-terminus MGFSLSKS (Gly2 followed by Ser6 fits an N-myristoylation consensus;
  untested, my own observation from the sequence).
- HGNC: locus_type "gene with protein product". Ensembl ENSG00000273045 protein_coding, chr2.
- HPA (ENSG00000273045 JSON, 2026-10-08): RNA low tissue specificity, "Detected in many";
  no subcellular-location (IF) data.

### Literature
- PubMed "C2orf15" (2026-10-08): 2 hits, both expression-only (pituitary adenoma proteomics,
  PMID:39806458, reports C2orf15 up-regulated in invasive tumours; breast cancer EMT RBP
  screen PMID:38783078). Neither tests C2orf15 function; not cached.
- GOA rows come from three high-throughput sources:
  - HuRI Y2H [PMID:32296183]: DYNLT3.
  - Neurodegeneration Y2H map [PMID:32814053, abstract only]: AGER, EZR, PKN1,
    UQCRC1 per GOA WITH column; "systematic yeast two-hybrid interaction screening of ∼500
    ND-related proteins".
  - mRNA interactome capture in HEK293 [PMID:22681889, abstract only] for RNA binding.

### Decisions
- 5 x protein binding IPI: REMOVE (bare binding; screens; no informative MF; UQCRC1 is a
  mitochondrial matrix-facing subunit and AGER an extracellular-domain receptor, so the
  partner set is not coherent).
- RNA binding HDA: MARK_AS_OVER_ANNOTATED (single proteome-wide capture hit, no RNA-binding
  domain, not followed up).
- No core MF; no NEW.
