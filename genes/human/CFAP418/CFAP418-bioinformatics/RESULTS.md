> **SUPERSEDED — wrong protein (2026-10-10).** The historical analysis below used human Q6ZT21 (TMPPE, 453 aa), not human CFAP418 Q96NL8 (207 aa). Its coiled-coil, WD40 and TPR conclusions do not establish CFAP418 function. The original report and analysis outputs are retained as historical provenance, not current evidence. The mouse FASTA was also mislabeled: its unchanged 363-aa sequence is Etnk1 (historical accession Q8BXQ0, now a secondary accession of Q9D4V0), not mouse Cfap418 Q3UJP5 (209 aa). Only that FASTA header has been corrected; no sequence was replaced. See the [current source evidence](../CFAP418-source-evidence.json) and [dated review notes](../CFAP418-notes.md).

# CFAP418 Bioinformatics Analysis Results

## Summary
Bioinformatics analysis of CFAP418 (Q6ZT21) reveals a 453 amino acid protein with characteristics consistent with ciliary/flagellar associated proteins, including potential coiled-coil regions and protein interaction domains.

## Key Findings

### 1. Protein Properties
- **Length**: 453 amino acids
- **Molecular Weight**: ~57.6 kDa
- **Theoretical pI**: Basic (>7.0)
- **Charge distribution**: 45 basic residues vs 34 acidic residues

### 2. Structural Features

#### Coiled-Coil Regions
- **Multiple potential coiled-coil regions detected**
- Major coiled-coil domain spanning positions 0-259 (high confidence)
- Additional regions at positions 273-315 and 350-441
- Consistent with protein-protein interaction and structural roles

#### Domain Predictions (Pattern-based)
- 4 potential WD40-like repeat patterns detected
- 6 potential TPR-like motifs identified
- Note: These are simplified predictions requiring validation with HMM-based tools

### 3. Ciliary Localization Signals
- 3 VxPx-like motifs detected
- No canonical RVxP ciliary targeting signals found
- Pattern consistent with ciliary/flagellar localization (CFAP family)

### 4. Composition Analysis
- Proline content: 4.2% (normal range)
- Glycine content: 6.6% (slightly elevated)
- Serine content: 8.4% (elevated, potential phosphorylation sites)

## Functional Implications

1. **Ciliary/Flagellar Function**: Name (CFAP = Cilia and Flagella Associated Protein) and sequence features support ciliary localization

2. **Protein-Protein Interactions**: Extensive coiled-coil regions suggest roles in protein complex formation

3. **Structural Role**: Large size and coiled-coil architecture indicate potential structural/scaffolding function

## Limitations and Recommendations

### Current Analysis Limitations:
- Pattern-based domain predictions are approximate
- Coiled-coil prediction uses simplified algorithm
- No structural modeling performed

### Recommended Follow-up Analyses:
1. InterProScan for comprehensive domain annotation
2. COILS or Paircoil2 for refined coiled-coil prediction
3. AlphaFold structure prediction for 3D modeling
4. Ciliary proteomics database cross-reference

## Methods
- Sequence retrieved from UniProt (Q6ZT21)
- Coiled-coil prediction: Heptad repeat pattern analysis
- Domain detection: Regular expression pattern matching
- Molecular weight: Sum of amino acid weights
- pI estimation: Basic/acidic residue ratio

## Script
- `analyze_cfap418.py` - Performs all analyses described above

## References
- UniProt Q6ZT21
- Pattern definitions based on PROSITE patterns

## Quality Checklist

- [x] Scripts present and executable
- [ ] Scripts accept command-line arguments (hardcoded UniProt ID Q6ZT21)
- [ ] Scripts can analyze other proteins (some CFAP-specific assumptions in analysis)
- [x] Results are reproducible
- [x] Methods clearly documented
- [x] Conclusions supported by evidence
- [ ] No hardcoded values (hardcoded UniProt ID Q6ZT21, CFAP family assumptions)
- [x] Output files generated as described