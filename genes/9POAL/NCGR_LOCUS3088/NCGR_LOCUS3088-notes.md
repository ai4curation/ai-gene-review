# NCGR_LOCUS3088 - Inosine Triphosphate Pyrophosphatase (ITPase) Notes

## Gene Identity

- UniProt: A0A811MJ28 (TrEMBL, unreviewed)
- Organism: *Miscanthus lutarioriparius* (NCBITaxon:422564), a Poaceae grass
- ORF name: NCGR_LOCUS3088
- EC: 3.6.1.66
- Family: HAM1 NTPase family
- Domains: Ham1p_like (Pfam PF01725), ITPase (InterPro IPR027502), RdgB/HAM1 (InterPro IPR002637)
- PANTHER: PTHR11067:SF9 (Inosine triphosphate pyrophosphatase)
- HAMAP rule: MF_03148 (HAM1_NTPase)
- 201 amino acids, homodimer, Mg2+/Mn2+ cofactor

## Function Summary

ITPase/HAM1 family enzymes are highly conserved "nucleotide pool sanitizers" found across all domains of life. They hydrolyze non-canonical purine nucleoside triphosphates (ITP, dITP, XTP, dHAPTP) to the corresponding monophosphates and diphosphate. This prevents incorporation of aberrant bases into DNA and RNA, which could cause mutagenesis or chromosomal lesions.

## Key Literature

### Plant-specific ITPase function
- [PMID:36464781 "An inosine triphosphate pyrophosphatase safeguards plant nucleic acids from aberrant purine nucleotides", Straube et al. 2023, New Phytologist] - Characterized Arabidopsis ITPA. Loss of ITPA causes accumulation of (d)ITP, elevated inosine in RNA and deoxyinosine in DNA, salicylic acid accumulation, premature senescence, and upregulation of immune-related transcripts. Demonstrates ITPA is part of a molecular protection system in plants.

### Human ITPA function
- [PMID:22384212 "Pivotal role of inosine triphosphate pyrophosphatase in maintaining genome stability and the prevention of apoptosis in human cells", Menezes et al. 2012, PLoS One] - ITPA knockdown sensitizes cells to HAP-induced DNA breaks and apoptosis. Demonstrates role in genome stability.

### Reviews
- [PMID:36651037 "Inosine triphosphate pyrophosphatase: A guardian of the cellular nucleotide pool and potential mediator of RNA function", Schroader et al. 2023, WIREs RNA] - Comprehensive review of ITPase biology including nucleotide pool sanitization and emerging RNA-related functions.
- [PMID:24151201 "ITPA (inosine triphosphate pyrophosphatase): from surveillance of nucleotide pools to human disease and pharmacogenetics", Burgis 2013, PMC] - Review covering ITPase from nucleotide pool surveillance to clinical relevance.

## Annotation Assessment

All annotations are IEA (Inferred from Electronic Annotation) via HAMAP rule MF_03148, ARBA rules, or UniProtKB keywords. No experimental evidence exists for this specific *Miscanthus* protein. However, the HAM1/ITPase family is extremely well-characterized biochemically across multiple organisms (E. coli RdgB, yeast Ham1, human ITPA, Arabidopsis ITPA), and the HAMAP rule MF_03148 is well-supported.

The specific substrate annotations (dITP, ITP, XTP diphosphatase activities) are well-supported by the HAMAP rule and family biochemistry. The more general annotations (nucleotide binding, metal ion binding, nucleotide metabolic process) are redundant with the specific ones but not incorrect.

## Notes on Annotation Quality

- GO:0035870 (dITP diphosphatase activity) - core enzymatic activity, well-supported
- GO:0036220 (ITP diphosphatase activity) - core enzymatic activity, well-supported
- GO:0036222 (XTP diphosphatase activity) - core enzymatic activity, well-supported
- GO:0047429 (nucleoside triphosphate diphosphatase activity) - parent term of the specific activities; redundant
- GO:0046872 (metal ion binding) - true but very generic; Mg2+/Mn2+ cofactor binding is part of the catalytic mechanism
- GO:0000166 (nucleotide binding) - true but very generic; substrate binding
- GO:0009143 (nucleoside triphosphate catabolic process) - correct BP for the activity
- GO:0009204 (deoxyribonucleoside triphosphate catabolic process) - correct, more specific BP
- GO:0009117 (nucleotide metabolic process) - very broad, redundant with more specific BP terms
- GO:0005737 (cytoplasm) - well-supported by HAMAP and literature
