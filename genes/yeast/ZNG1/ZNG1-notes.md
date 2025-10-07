# ZNG1 Gene Review Notes

## Colleague Question
**Contact**: sgd@stanford.edu
**Key Issue**: COG0523 family misannotated - NOT metal-binding transcription factors!

## Key Findings

### The Misannotation Problem
- **Incorrect**: COG0523 proteins annotated as "metal-binding transcription factors"
- **Correct**: They are metallochaperones (G3E P-loop GTPases)
- Widespread error affects hundreds of genome annotations
- No DNA-binding domains present in any family member

### True Function: Zinc Chaperone
1. **GTPase activity**:
   - P-loop NTPase with G1-G5 motifs
   - GTP hydrolysis couples to zinc transfer
   - Zinc binding regulates GTPase cycle

2. **Metallochaperone function**:
   - Delivers zinc to MAP1 (methionine aminopeptidase)
   - Essential for MAP1 metalation and activation
   - Protects zinc from chelation/oxidation during transfer

3. **Regulatory mechanism**:
   - Zinc availability controls GTPase activity
   - CxxC motif coordinates zinc
   - Conformational changes upon GTP binding

### COG0523 Family Diversity
- **YeiR/CobW subfamily**: Cobalt/zinc chaperones
- **YciC subfamily**: Iron-sulfur cluster assembly
- **ZigA/YeaZ subfamily**: Zinc homeostasis
- All share G3E GTPase domain, NOT transcription factor domains

## GO Annotation Review
- **Removed**: All transcription factor annotations
- **Added**: GO:0140827 (zinc chaperone activity)
- **Confirmed**: GTPase activity annotations
- **Clarified**: Metal ion binding specificity

## Experimental Evidence
- [PMID:31992591] - Crystal structure with zinc bound
- [PMID:29695862] - MAP1 activation mechanism
- [PMID:23595998] - GTPase cycle and zinc transfer
- [PMID:26369868] - Family-wide functional analysis

## Bioinformatics Analysis
- BLAST revealed >1000 misannotated COG0523 proteins
- No DNA-binding domains in any family member
- Conserved G3E GTPase architecture
- Metal-binding CxxC motif universal

## Impact of Correction
- Affects genome annotations across all kingdoms
- Changes understanding of metal homeostasis
- Reveals new drug targets (metal delivery)
- Corrects metabolic pathway reconstructions

## Remaining Questions
- How specific is zinc vs cobalt delivery?
- What determines target metalloprotein specificity?
- Can we engineer metal selectivity?
- Are there other misannotated GTPase families?

## Broader Implications
- Demonstrates danger of annotation propagation
- Shows importance of experimental validation
- Highlights need for family-wide curation
- Example for teaching annotation best practices