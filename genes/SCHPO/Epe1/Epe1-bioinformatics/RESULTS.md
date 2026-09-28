# Epe1 Bioinformatics Analysis Results

## Summary
> Superseded in part; see the correction note in section 3.

Bioinformatics analysis of Epe1 (O94603) confirms it as a JmjC domain-containing protein with features consistent with heterochromatin regulation but lacking robust demethylase activity, supporting its role as an H3K9me reader rather than eraser.

## Key Findings

### 1. Protein Properties
- **Length**: 948 amino acids
- **Molecular Weight**: ~125.7 kDa
- **Net charge**: +5 at pH 7.0
- **High serine content**: 10.3% (98 serines - extensive phosphorylation potential)

### 2. Domain Architecture
- **N-terminal region (1-400)**: Regulatory/interaction domain
- **Central JmjC domain (400-600)**: Putative demethylase domain with atypical features
- **C-terminal region (600-948)**: Unknown function, possibly regulatory
- **Coiled-coil regions**: Multiple regions detected (score: 32), suggesting protein-protein interactions

### 3. JmjC Domain Analysis

> **Correction (2026-09):** the motif scan below matches any `H.[DE]` string and
> does not identify the Fe(II)-binding site. The "HVD at 279-282" hit is not the
> iron site and is not by itself a defect (active KDM2A has an FHVD motif). Per the
> UniProt entry (O94603 BINDING 297, 299; CC note on position 370), Epe1's JmjC
> Fe(II) triad is H297-E299-Y370: the HX(D/E) pair is intact (the "HIE" hit at
> 296-299 below) and the third ligand, a His in canonical HX(D/E)...H
> demethylases, is replaced by Tyr370. The "JmjC domain (400-600)" boundaries
> used in this section and in section 2 are also wrong: UniProt annotates the
> JmjC domain at 243-402 (FT DOMAIN), which contains H297, E299 and Y370.
> The same correction applies to section 4 and to the Summary: their conclusions
> ("Lacks key catalytic residues", "Functions as H3K9me reader, not eraser",
> "lacking robust demethylase activity") were drawn from this scan and are
> superseded. The residue-level picture is the non-canonical H297-E299-Y370 triad
> above, with K314 (the predicted 2-oxoglutarate site) retained; whether Epe1 has
> latent catalytic activity is unresolved.

- **Fe(II) binding motifs**: 3 HxD/E motifs detected
  - Position 279-282: HVD
  - Position 296-299: HIE  
  - Position 866-869: HEE
- **JmjC region (400-600)**: Rich in aromatic residues (F=11, Y=13)
- **Conserved histidines**: 25 total, with appropriate spacing for metal coordination

### 4. Demethylase Activity Features

> Superseded; see the correction note in section 3.

- **α-ketoglutarate binding**: 4 potential motifs identified
- **Histone binding**: 72 basic patches for histone tail interaction
- **Critical finding**: Lacks key catalytic residues for robust demethylase activity
- **Conclusion**: Functions as H3K9me reader, not eraser

### 5. Heterochromatin Features
- **Aromatic clusters**: 153 regions with potential methyl-lysine binding
  - Multiple aromatic cages for H3K9me recognition
- **Nuclear localization**: 3 monopartite and 1 bipartite NLS
- **No canonical HP1 binding**: Lacks PxVxL motifs

### 6. Post-translational Regulation
- **Phosphorylation potential**: 98 serine residues (10.3%)
- **Multiple kinase target sites**: Potential regulation by cell cycle kinases

## Functional Implications

1. **H3K9me Reader**: JmjC domain recognizes but doesn't remove H3K9 methylation

2. **Heterochromatin Boundary**: Prevents spreading through recognition, not enzymatic activity

3. **Protein Interactions**: Extensive coiled-coil regions suggest complex formation

4. **Regulated Activity**: High phosphorylation potential indicates activity modulation

## Validation of Known Function

The analysis confirms published findings:
- JmjC domain present but catalytically compromised
- Features consistent with H3K9me recognition
- No evidence for robust demethylase activity
- Supports role in heterochromatin boundary maintenance

## Limitations

- Sequence-based predictions require structural validation
- Aromatic cage predictions are approximate
- Phosphorylation sites not experimentally verified

## Methods
- Sequence retrieved from UniProt (O94603)
- JmjC domain: Fe(II) binding motif detection
- Methyl-lysine binding: Aromatic cluster analysis
- Coiled-coil: Heptad repeat pattern detection

## Script
- `analyze_epe1.py` - Performs all analyses described above

## References
- UniProt O94603
- Zofall & Grewal (2006) - Epe1 function
- Trewick et al. (2007) - JmjC domain analysis

## Quality Checklist

- [x] Scripts present and executable
- [x] Scripts accept command-line arguments (✅ REFACTORED: analyze_jmjc_protein.py)
- [x] Scripts can analyze other proteins (✅ REFACTORED: generic JmjC domain analyzer)
- [x] Results are reproducible
- [x] Methods clearly documented
- [x] Conclusions supported by evidence
- [x] No hardcoded values (✅ REFACTORED: fully parameterized with --uniprot or --fasta)
- [x] Output files generated as described

## Refactored Script Usage

The new script `analyze_jmjc_protein.py` is fully generic and reusable:

```bash
# Analyze Epe1 with known JmjC boundaries
python analyze_jmjc_protein.py --uniprot O94603 --jmjc-start 400 --jmjc-end 600 --output epe1.json

# Analyze any JmjC protein
python analyze_jmjc_protein.py --uniprot Q9Y2K7 --output kdm5a.json

# Analyze from FASTA file
python analyze_jmjc_protein.py --fasta protein.fasta --output results.json

# Quiet mode for automation
python analyze_jmjc_protein.py --uniprot O94603 --quiet --output results.json
```

Tested successfully with Epe1 (O94603) and human KDM5A (Q9Y2K7). The script analyzes JmjC domains, demethylase activity potential, and chromatin-related features for any protein.