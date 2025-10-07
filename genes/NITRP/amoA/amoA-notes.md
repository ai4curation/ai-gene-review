# amoA Gene Review Notes

## Colleague Question
**Contact**: nitrogen@whoi.edu
**Key Issue**: Very difficult to distinguish amoA from pmoA by sequence alone

## Key Findings

### The amoA/pmoA Confusion Problem
- **High sequence similarity**: ~40% identity, ~60% similarity
- Both are copper-dependent monooxygenases
- Both have similar membrane topology
- Both oxidize small hydrocarbons
- Functional annotation often wrong

### Distinguishing Features
1. **Active site residues**:
   - amoA: His residues coordinating Cu centers
   - Specific motifs in transmembrane regions
   - Conservation patterns differ subtly

2. **Phylogenetic clustering**:
   - amoA clusters with nitrifiers
   - pmoA clusters with methanotrophs
   - Need robust tree with many sequences

3. **Gene context**:
   - amoA: Found with amoB, amoC genes
   - pmoA: Found with pmoB, pmoC genes
   - Metabolic gene neighborhoods differ

### Functional Differences
- **amoA**: NH₃ + O₂ → NH₂OH (hydroxylamine)
- **pmoA**: CH₄ + O₂ → CH₃OH (methanol)
- Different substrate binding pockets
- Different product release mechanisms

## Environmental Importance
- Nitrosopumilus dominates ocean nitrification
- Critical for nitrogen cycling
- Climate impact (N₂O production)
- Key biomarker for ammonia oxidizers

## GO Annotation Review
- Modified general monooxygenase to specific ammonia monooxygenase
- Added nitrification process
- Confirmed membrane localization
- Specified archaeal-specific annotations

## Practical Tips for Distinction
1. **Never trust BLAST alone** - too similar
2. Check gene synteny (amoB/C presence)
3. Use specialized databases (FunGene)
4. Consider environmental context
5. Look for diagnostic residues

## Key Publications
- [PMID:15574881] - Discovery of archaeal ammonia oxidation
- [PMID:22775980] - Environmental distribution
- [PMID:26923429] - Structure-function relationships
- [PMID:31796959] - Evolution of copper monooxygenases

## Biotechnology Applications
- Wastewater treatment monitoring
- Nitrogen removal systems
- Climate change indicators
- Bioremediation markers

## Remaining Questions
- Can single enzyme oxidize both NH₃ and CH₄?
- What determines substrate specificity?
- How to design specific inhibitors?
- Evolutionary relationship to pmoA?

## Bioinformatics Resources
- FunGene database for functional genes
- Specific amoA primers for PCR
- Curated reference alignments
- Diagnostic HMM profiles