# Enterobacteria Phage P4 Gene int (Integrase Int) — Curation Notes

## Overview
Enterobacteria satellite phage P4 gene *int* (`P08320`, 440 aa, ~50.5 kDa) encodes the tyrosine-family site-specific recombinase (integrase) responsible for integrating the P4 genome into and excising it from the *Escherichia coli* chromosome [PMID:3119856, PMID:2183201, PMID:16847139].

## Biochemical and Biological Roles
1. **Site-Specific Viral Genome Integration and Proviral Latency**:
   - Pierson & Kahn (1987) sequenced the phage (`P4attP`) and host (`P4attB`) attachment regions and showed that P4 Int catalyzes site-specific recombination across a 20-bp core sequence located within the 3' end of the host *leuX* (tRNA-Leu5) gene (`GO:0044826`, `viral genome integration into host DNA`; `GO:0075713`, `establishment of integrated proviral latency`; `GO:0003677`, `DNA binding`) [PMID:3119856, PMID:16847139].
2. **Negative Autoregulation of `Pint` Transcription**:
   - Piazzolla et al. (2006) demonstrated that expression of P4 `int` from the `Pint` promoter is negatively regulated by both Int itself and the P4 excisionase Vis (`P12552`), establishing a direct role in regulating viral transcription (`GO:0039695`, `DNA-templated viral transcription`) [PMID:16847139, "Phage P4 int gene encodes the integrase responsible for phage integration into and excision from the Escherichia coli chromosome. Here, the data showing that P4 int expression is regulated in a complex manner at different levels are presented. First of all, the Pint promoter is regulated negatively by both Int and Vis, the P4 excisionase."].

## GO Annotation Review
- **Accept**: `GO:0003677` (`DNA binding`), `GO:0039695` (`DNA-templated viral transcription`), `GO:0044826` (`viral genome integration into host DNA`), and `GO:0075713` (`establishment of integrated proviral latency`).
- **Keep as non-core**: `GO:0016740` (`transferase activity`) and `GO:0016787` (`hydrolase activity`), which reflect the general phosphodiester bond cleavage/rejoining chemistry mapped from UniProt keywords `KW-0808` and `KW-0378`.
- **Modify**: Refine `GO:0006310` (`DNA recombination`) and `GO:0015074` (`DNA integration`) to the more specific viral child term `GO:0044826` (`viral genome integration into host DNA`).
- **Remove**: `GO:0046718` (`symbiont entry into host cell`, `IEA` `GO_REF:0000043` from `KW-1160`), as P4 integrase acts intracellularly after viral DNA entry to integrate the phage genome into the host chromosome and plays no role in virion entry across the host cell envelope.
