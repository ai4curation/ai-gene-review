# Curation Notes for Escherichia phage Mu C (P06022)

## Summary of Gene Function
- **Gene symbol**: `C` (locus tag `Mup21`; UniProt `P06022`, Late transcription activator C)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: Late transcription activator C (`Mup21`, 140 aa) is a homodimeric sequence-specific DNA-binding transcription activator (`GO:0001216` `DNA-binding transcription activator activity`, `GO:0003677` `DNA binding`) closely homologous to the middle operon regulator Mor (`Mup17`). Expressed from the Mor-activated middle operon, protein C governs the transition from middle to late viral gene expression (`GO:0045893` `positive regulation of DNA-templated transcription`, `GO:0019083` `viral transcription`) by activating the four phage Mu late promoters: `Plys`, `PI`, `PP`, and `Pmom` — driving synthesis of the viral lysis proteins, morphogenesis/structural proteins, and the Mom DNA modification system [file:BPMU/C/C-uniprot.txt].
- **Mechanism & Magnesium Cofactor**: Binding of `Mg2+` (`GO:0000287` `magnesium ion binding`) induces a conformational change in the C homodimer that promotes sequence-specific DNA binding at the late promoters [file:BPMU/C/C-uniprot.txt]. At `Pmom` (which has a suboptimal 6-bp spacer between `-10` and `-35` elements), C binding unwinds the promoter DNA to realign the promoter elements and directly recruits host RNA polymerase [file:BPMU/C/C-uniprot.txt].

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA): `ACCEPT`.
- `GO:0030430` (`host cell cytoplasm`, IEA): `ACCEPT`.
- `GO:0046872` (`metal ion binding`, IEA): `MODIFY` to `GO:0000287` (`magnesium ion binding`), supported by the UniProt `COFACTOR` annotation (`Name=Mg(2+); Xref=ChEBI:CHEBI:18420; Note=Binding magnesium induces a conformational change that allows DNA-binding`).
- `NEW` `GO:0001216` (`DNA-binding transcription activator activity`, `enables`): Captures protein C's primary molecular function as a transcriptional activator of the four late promoters (`Plys`, `PI`, `PP`, `Pmom`).
- `NEW` `GO:0045893` (`positive regulation of DNA-templated transcription`, `involved_in`): Captures positive regulation of late promoter transcription.
- `NEW` `GO:0019083` (`viral transcription`, `involved_in`): Captures protein C's role in late viral gene transcription.
