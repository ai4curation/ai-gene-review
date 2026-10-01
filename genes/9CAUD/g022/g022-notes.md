# g022 Yersinia phage phiR8-01 DNA Polymerase Gene Reference Enhancement Notes

## Status: ENHANCED ✅

### Initial State
- **Literature references**: 0 PMIDs/PMCs
- **Total references**: 5 (GO_REF only)
- **Gene context**: Bacteriophage DNA polymerase I (family A) from Yersinia phage phiR8-01 (NCBITaxon:1206556; Autographivirales, Autonotataviridae, Pienvirus). Earlier versions of these notes said Tequatrovirus; see the 2026-10-01 correction below.

### Enhancements Made (2025-09-13)

#### Added Literature References
1. **PMID:35357498** - "The DNA polymerase of bacteriophage YerA41 replicates its T-modified DNA in a primer-independent manner" (2022, J Virol)
   - **Yersinia phage focus**: Direct relevance to Yersinia phage DNA polymerases
   - Key findings: Family A conservation, primer-independent activity, high processivity
   - 6 specific findings extracted with supporting text

#### Impact
- **Literature references**: 0 → 1 PMID (functional characterization)
- **Total references**: 5 → 6
- **Total findings**: 0 → 6 findings with experimental evidence
- **Quality**: Now includes mechanistic insights into bacteriophage DNA polymerases

### Research Strategy Used

1. **Related phage approach**: Searched for Yersinia phage DNA polymerase studies
2. **Family A focus**: Emphasized conserved DNA polymerase family characteristics
3. **Functional context**: Highlighted viral genome replication mechanisms
4. **Comparative approach**: Used related bacteriophage systems for functional insights
5. **Mechanistic detail**: Extracted structural and biochemical properties

### Key Scientific Insights Added

- **Family A conservation**: Contains conserved PolA motifs A, B, and C
- **Primer-independent activity**: Can initiate replication without external primers
- **High processivity**: Efficient DNA synthesis with minimal incubation time
- **Viral packaging**: Delivered within phage particles during infection
- **C-terminal domain**: Contains the active polymerase function
- **Modified DNA templates**: Specialized to handle hypermodified viral DNA
- **Template specificity**: Adapted to replicate viral genomic material

### Tequatrovirus Context

g022 represents a DNA polymerase from the Tequatrovirus genus:
- **Host range**: Tequatroviruses infect Enterobacteriaceae including Yersinia
- **Viral replication**: Essential for autonomous viral DNA synthesis
- **Family A properties**: Shares conserved motifs with other DNA polymerases
- **Viral packaging**: Likely packaged in virion for immediate use post-infection
- **Template adaptation**: May handle modified DNA bases unique to the phage

### Next Steps for g022
- Search for specific Tequatrovirus genome analyses
- Look for structural studies of viral DNA polymerases
- Check for comparative studies of phage vs bacterial DNA polymerases
- Review viral DNA modification and replication mechanisms

### Lessons Learned
- Related phage systems provide valuable functional insights
- Bacteriophage DNA polymerases have unique properties vs bacterial ones
- Family A motifs are highly conserved across viral and cellular polymerases
- Viral DNA polymerases often have specialized functions for modified templates

### Quality Metrics
- PMID:35357498 provides detailed functional characterization of related Yersinia phage DNA polymerase
- Comprehensive coverage of family A DNA polymerase properties
- Strong mechanistic and biochemical insights
- Direct relevance to viral genome replication established
## 2026-10-01 correction (GOA refresh, PR #3503)

- **Taxon.** g022 (I7J3R9) is from Yersinia phage phiR8-01, NCBITaxon:1206556
  (UniProt OC: Autographivirales; Autonotataviridae; Melnykvirinae; Pienvirus). It
  is **not** a Tequatrovirus (T4-like, NCBITaxon:10663), so the "Tequatrovirus
  Context" section above is wrong and is superseded. The review YAML taxon and
  gene_symbol were corrected to match GOA/UniProt.
- **PMID:35357498 is homolog evidence only.** It characterises DNAP01 of the
  jumbo phage YerA41 (polymerase domain at residues 946-1306), not g022 (815 aa).
  This is now recorded as `reference_review` (relevance LOW, MISCITED) in the review.
  The accepted g022 terms rest on family-level InterPro/EC/keyword inference.
- **3'-5' exonuclease withdrawn.** The NEW proposal for GO:0008296 has been
  removed from existing_annotations and core_functions. It never had a GOA row,
  so it cannot stay there under UNDECIDED (the GOA check exempts only NEW and
  retired rows). It is now a suggested_question plus a suggested_experiment. g022 sits in PANTHER
  PTHR10133:SF27 (DNA polymerase nu), alongside proofreading-deficient Bacillus
  subtilis and Thermus PolA. UniProt shows no 3'-5' exonuclease domain, and the
  deep research only inferred the activity from family membership.
- **Follow-up.** The deep-research file was generated under the wrong taxon
  framing; regenerate it (`just deep-research 9CAUD g022 ...`) rather than
  hand-editing it. g022-pathway.md also mentions Tequatrovirus once and
  should be regenerated after the deep research is.
