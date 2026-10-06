# erg9 (SPBC646.05c, UniProt P36596) notes

Module: `ergosterol_biosynthesis` (squalene synthase step); S. cerevisiae ortholog ERG9 (P29704).
Fetch verified: P36596 ERG9_SCHPO.

## Evidence
- S. pombe squalene synthase cDNA complements S. cerevisiae erg9 disruptants [PMID:8474436 "cerevisiae cells bearing ERG9 gene disruptions, showing that these enzymes can"]; C-terminal membrane anchor [PMID:8474436 "predicted to encode C-terminal membrane-spanning proteins of approximately 50"].
- Reaction 2 FPP + NAD(P)H -> squalene [UniProt:P36596 "Reaction=2 (2E,6E)-farnesyl diphosphate + NADPH + H(+) = squalene + 2"].
- Pof14 binds Erg9 and inhibits its activity under H2O2 stress [PMID:17016471 "Pof14 binds to and decreases Erg9 activity in vitro and a pof14 deletion strain quickly loses viability"].
- ER membrane [UniProt:P36596 "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"].

## Curation decisions
- protein binding (IPI, Pof14) REMOVE as uninformative; interaction not disputed. Regulatory edge belongs on Pof14.
- ergosterol metabolic process (IGI) MODIFY -> ergosterol biosynthetic process.
- transferase alkyl/aryl IEA MODIFY -> GO:0051996.
- GO-CAM 66c7d41500002088 places erg9 activity on GO:0098554 cytoplasmic side of ER membrane (IDA PMID:17016471); this review uses ER membrane in core_functions (as yeast ERG9) and accepts the IC row for the cytoplasmic side.
- Note: cached PMID:17016471 full text is truncated (intro/methods only).
