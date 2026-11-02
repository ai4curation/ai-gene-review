# TRIT1 review notes

## Deep research

Automated deep research could not be generated: `just deep-research-falcon` failed
(Edison API 402 Payment Required; perplexity-lite fallback unavailable) and
`just deep-research-openai` failed with 401. The review uses cached literature and the
UniProt record directly.

## Literature used

- Golovko et al. 2000 [PMID:11111046 "Expression of the gene in a Saccharomyces cerevisiae mutant lacking the endogenous tRNA isopentenyl transferase MOD5 resulted in functional complementation and reintroduction of isopentenyladenosine into tRNA"] (abstract only).
- Lamichhane et al. 2013 [PMID:24126054 "only tRNA(Ser)AGA, tRNA(Ser)CGA, tRNA(Ser)UGA, and selenocysteine tRNA with UCA"] - the cytosolic substrate set; mt-tRNA(Ser)UGA and mt-tRNA(Trp) also carry i6A37.
- Yarham et al. 2014, COXPD35 [PMID:24901367 "We show that patient cells bearing the p.Arg323Gln TRIT1 mutation are severely deficient in i6A37 in both cytosolic and mitochondrial tRNAs"]; dual cytosol/matrix localization by sub-fractionation.
- Schöller et al. 2021 (METTL8) [PMID:34774131 "our biochemical reconstitution revealed that METTL8 requires prior TRIT1 activity"].

## Curation decisions

- `ATP binding` (InterPro, P-loop) removed: the P-loop of IPTases binds the DMAPP
  pyrophosphate (UniProt BINDING 32..37, ligand dimethylallyl diphosphate); no ATP step.
- `nucleic acid binding` modified to `tRNA binding`.
- `zinc ion binding` kept as non-core (predicted matrin-type zinc finger).
- Two core functions: the same dimethylallyltransferase activity in the mitochondrial
  matrix (mt-tRNAs) and in the cytoplasm (cytosolic tRNA(Ser)/tRNA(Sec)).

## Disease context (dismech)

dismech `Combined_Oxidative_Phosphorylation_Deficiency_35` used only as a literature lead.
