# SNORD3A (U3 snoRNA) Gene Review Notes

## Gene Identity and Classification

SNORD3A is also known as U3 snoRNA (Small Nucleolar RNA U3), a C/D box small nucleolar RNA.
- RNAcentral ID: URS000053962A_9606
- Length: 217 nucleotides
- Classification: C/D box snoRNA

## Core Function

SNORD3A/U3 is **essential for ribosome biogenesis**, specifically for the processing and maturation of 18S ribosomal RNA (the SSU-rRNA component). Unlike most other C/D box snoRNAs that guide 2'-O-methylation of rRNA, U3 snoRNA plays a unique role in guiding site-specific cleavage during pre-rRNA processing.

### Key Functional Evidence

1. **Essential for 18S rRNA maturation** [Oxford Academic NAR "The initial U3 snoRNA:pre-rRNA base pairing interaction required for pre-18S rRNA folding revealed by in vivo chemical probing" https://academic.oup.com/nar/article/39/12/5164/2411137]
   - "The U3 snoRNA is indeed required for folding of the pre-18S rRNA"
   - U3 snoRNP, via base pairing and its associated proteins, orchestrates the folding of pre-rRNA that results in assembly of the small ribosomal subunit

2. **Component of SSU-processome** [PMC "snoRNPs: Functions in Ribosome Biogenesis" https://pmc.ncbi.nlm.nih.gov/articles/PMC7277114/]
   - "The U3 snoRNP is essential for the formation of the small subunit (SSU) processome, a multi-subunit complex that directs maturation of the 18S rRNA and 40S small subunit"
   - "Unlike other C/D box snoRNAs, U3 has not been shown to guide any chemical modifications. Rather, U3 is thought to guide site-specific cleavage of ribosomal RNA (rRNA) during pre-rRNA processing"

3. **Required for early pre-rRNA cleavages** [Oxford Academic NAR "Synergistic defects in pre-rRNA processing from mutations in the U3-specific protein Rrp9 and U3 snoRNA" https://academic.oup.com/nar/article/48/7/3848/5717751]
   - "U3 snoRNA and the associated Rrp9/U3-55K protein are essential for 18S rRNA production by the SSU-processome complex"
   - "U3 and Rrp9 are required for early pre-rRNA cleavages at sites A0, A1 and A2"

## Molecular Mechanism

U3 snoRNA functions through base-pairing interactions with pre-rRNA rather than through chemical modification:
- Forms base-pairing interactions with pre-18S rRNA sequences
- These interactions are required for proper folding of the pre-18S rRNA
- Works in conjunction with U3-associated proteins (including Rrp9/U3-55K) to direct cleavage events

## Expression and Disease Associations

### Tissue Expression
- Overexpressed in testis (4.5-fold) [GeneCards]
- Expressed in adrenal tissue, sural nerve, bone marrow, and 101 other cell types/tissues [GeneCards]

### Disease Association
- **Prion Disease Progression** [RNAcentral URS000053962A]
  - "SNORD3A levels were indicative of prion disease progression rather than a response to general stress"
  - Shows positive correlation with UMPS levels in brain tissue
  - Shows inverse relationship with miR-185-5p expression

## Relevant Gene Ontology Terms

Based on the functional evidence:

### Biological Process
- **GO:0030490** (maturation of SSU-rRNA) - CORE FUNCTION
- **GO:0000462** (maturation of SSU-rRNA from tricistronic rRNA transcript)
- **GO:0006364** (rRNA processing)

### Molecular Function
- **GO:0042134** (rRNA primary transcript binding) - binds to pre-rRNA
- **GO:0070181** (small ribosomal subunit rRNA binding) - binds to SSU rRNA

### Cellular Component
- Nucleolus (expected for snoRNAs, but should verify specific GO term)
- Part of SSU-processome complex

## Database Annotations

Indexed in 9 databases:
- RefSeq, Rfam, GeneCards, HGNC, ENA, IntAct, LNCipedia, PDBe, snOPY

## miRNA Interactions

Targeted by 19 different human miRNAs including:
- hsa-miR-185-5p
- hsa-miR-320a-3p
- hsa-miR-34a-5p
- hsa-miR-4429

## Literature

127 publications reference this RNA, with key research in PMC3549992 and PMC7205983.

## Distinction from Other C/D Box snoRNAs

**CRITICAL**: U3 snoRNA is atypical among C/D box snoRNAs:
- Most C/D box snoRNAs guide 2'-O-methylation of rRNA
- U3 does NOT guide methylation
- Instead, U3 guides site-specific cleavage through base-pairing with pre-rRNA
- This makes it functionally distinct and essential for a different aspect of ribosome biogenesis

## Curation Notes

The existing YAML file incorrectly listed:
- GO:0030620 (U2 snRNA binding) - INCORRECT, this is for U2 snRNA, not U3 snoRNA
- The description mentions "2'-O-methylation" - INCORRECT for U3, which does cleavage not methylation

Need to correct these to reflect U3's actual function in pre-rRNA cleavage and 18S rRNA maturation.
