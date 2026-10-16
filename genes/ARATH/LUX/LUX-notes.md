# LUX (PCL1, At3g46640; UniProt Q9SNB4) curation notes

## 2026-10-06: initial review (module plant_circadian_clock_oscillator)

- Fetched with `just fetch-gene ARATH Q9SNB4 --alias LUX`. Falcon deep research failed; review based on cached publications.

### Key findings
- GARP/MYB DNA-binding protein essential for the clock [PMID:16164597 "the PCL1 gene encodes a novel DNA binding protein belonging to the GARP protein family and is essential for a functional clock oscillator in A. thaliana"]; lux mutants lose rhythm robustness in LL/DD [PMID:16006522].
- Direct repression of PRR9 and negative autoregulation [PMID:21236673 "We also show that LUX binds to its own promoter, defining a new negative autoregulatory feedback loop within the core clock."].
- DNA-binding subunit of the EC [PMID:21753751 "LUX targets the complex to the promoters of PIF4 and PIF5 in vivo"]; LBS consensus GAT(A/T)CG, with a crystal structure of the MYB domain bound to DNA [PMID:32165537].
- EC binding is temperature-dependent [PMID:28650433].

### Decisions
- DNA-binding TF activity (IBA/IEA/ISS): MODIFY to GO:0001227 (repressor), keeping all three rows consistent.
- Positive regulation of circadian rhythm IMP (UniProt): KEEP_AS_NON_CORE; better captured as an oscillator component.
- Regulation of gene expression IMP (RVE8 paper): KEEP_AS_NON_CORE (indirect).
