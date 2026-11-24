# Enterobacteria phage P4 `P12552` (Excisionase and transcriptional regulator Vis, `P12552`)

## Identity & Genomic Context
- **UniProt**: `P12552` (`Y98_BPP4`, historical annotation: `Uncharacterized 9.8 kDa protein`, 88 aa, ~9.8 kDa).
- **Locus**: `ORF88` (`vis`), located immediately upstream of `sid` in the P4 genome ([PMID:3295254], [PMID:2183201], [PMID:16847139]).
- **Domains**: Putative DNA-binding domain superfamily (`InterPro:IPR009061` `DNA-bd_dom_put_sf`), Prophage regulatory activator (`InterPro:IPR052931`), and Bacteriophage P4 Vis / AlpA excisionase family (`InterPro:IPR010260` `AlpA`, `Pfam:PF05930` `Phage_AlpA`).

## Molecular Function & Biological Role
- Although originally annotated in sequence records as an uncharacterized 9.8 kDa ORF (`ORF88`) upstream of `sid` ([PMID:3295254], [PMID:2183201]), subsequent genetic and biochemical characterization identified this 88-aa winged-helix protein as **Vis**, the P4 excisionase and transcriptional regulator ([PMID:16847139]).
- **Excisionase activity**: Together with P4 integrase (`Int`), Vis promotes site-specific excisive recombination of the integrated P4 prophage from the host *Escherichia coli* chromosome ([PMID:16847139]).
- **Transcriptional and post-transcriptional regulation of `int`**: Vis binds directly to the `Pint` promoter region to negatively regulate `int` transcription, and also binds the 5' untranslated region of the `int` mRNA (where a stable stem-loop overlaps the ribosome-binding site) to modulate `int` expression ([PMID:16847139]).

## Curation Summary
- **Accepted**:
  - `GO:0003677` (`DNA binding`, `IEA`, `GO_REF:0000043`) -> `ACCEPT` (supported by [PMID:16847139] and `IPR009061`).
- **Added (`NEW`)**:
  - `GO:0006310` (`DNA recombination`, `IMP`, [PMID:16847139]) for its role as the P4 excisionase required for excisive site-specific recombination.
  - `GO:0039695` (`DNA-templated viral transcription`, `IMP`, [PMID:16847139]) for its direct negative regulation of viral transcription from the `Pint` promoter.
