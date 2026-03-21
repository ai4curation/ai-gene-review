# xylR Gene Review Notes

## Identity And Organism Context

- Requested target: `genes/PSEPK/xylR`, but the canonical reviewed accession recovered for `xylR` is `P06519`, where UniProt explicitly records `OG   Plasmid TOL pWW0.` and `OX   NCBI_TaxID=303;` [file:PSEPK/xylR/xylR-uniprot.txt, "OG   Plasmid TOL pWW0."] [file:PSEPK/xylR/xylR-uniprot.txt, "OX   NCBI_TaxID=303;"].
- The xylR literature is therefore anchored to the plasmid-borne TOL regulator from the `P. putida` mt-2 lineage, not to the native KT2440 chromosome [PMID:2430049 Genetic, functional and sequence analysis of the xylR and xylS regulatory genes of the TOL plasmid pWW0., "Genetic, functional and sequence analysis of the xylR and xylS regulatory genes of the TOL plasmid pWW0."].
- KT2440 is still a relevant experimental host for this system, because later work explicitly studies `Pseudomonas putida KT2440 pWW0` [PMID:16085802 Integration of signals through Crc and PtsN in catabolite repression of Pseudomonas putida TOL plasmid pWW0., "Toluene degradation in Pseudomonas putida KT2440 pWW0 plasmid is subjected to catabolite repression."].

## Core Biological Role

- `xylR` is the positive transcriptional regulator of the TOL plasmid `xyl` operons for toluene/xylene utilization [PMID:2993247 Determination of the transcription initiation site and identification of the protein product of the regulatory gene xylR for xyl operons on the TOL plasmid., "The xylR gene is a regulatory gene on the TOL plasmid, which acts in a positive manner on xyl operons for degradation of toluene and xylenes in Pseudomonas putida."].
- The reviewed UniProt entry summarizes the same regulatory scope and notes induction by aromatic effectors: `In the presence of m-xylene or m-methylbenzyl alcohol XylR activates both the xylCMABN operon and the regulatory gene xylS` [file:PSEPK/xylR/xylR-uniprot.txt, "In the CC       presence of m-xylene or m-methylbenzyl alcohol XylR activates both the"].
- `xylR` encodes a 566 aa, ~67 kDa protein [PMID:3169574 Nucleotide sequence of the regulatory gene xylR of the TOL plasmid from Pseudomonas putida., "The 1698-bp sequence for a 566-amino acid (aa) protein (Mr 63741) was identified as the XylR-encoding sequence."] [PMID:2993247 Determination of the transcription initiation site and identification of the protein product of the regulatory gene xylR for xyl operons on the TOL plasmid., "The product of the xylR gene was identified by the maxicell system as a protein with an approximate molecular weight of 67,000."].

## Mechanism

- XylR is an NtrC/NifA-like enhancer-binding regulator with a central sigma-factor interaction region and a C-terminal DNA-binding region [PMID:3169574 Nucleotide sequence of the regulatory gene xylR of the TOL plasmid from Pseudomonas putida., "The central region of XylR (aa 234-473) corresponds to the region that was proposed to interact with RNA polymerase having a sigma factor, NtrA"] [PMID:3169574 Nucleotide sequence of the regulatory gene xylR of the TOL plasmid from Pseudomonas putida., "The C-terminal region (aa 515-558) has a putative DNA-binding structure."].
- UniProt also marks the ATP-binding and DNA-binding features directly: `FT   BINDING         263..270` / `ligand="ATP"` and `FT   DNA_BIND        534..553` [file:PSEPK/xylR/xylR-uniprot.txt, "FT   BINDING         263..270"] [file:PSEPK/xylR/xylR-uniprot.txt, "FT                   /ligand=\"ATP\""] [file:PSEPK/xylR/xylR-uniprot.txt, "FT   DNA_BIND        534..553"].
- ATP is mechanistically relevant because activation involves ATP-dependent multimerization of XylR at upstream activating sequences (UAS) [PMID:9489676 Activation of the toluene-responsive regulator XylR causes a transcriptional switch between sigma54 and sigma70 promoters at the divergent Pr/Ps region of the TOL plasmid., "The addition of ATP, known to trigger multimerization of the regulator at the UAS, enhanced the repression of Pr by XylRdeltaA."].
- Activated XylR drives a promoter switch: it activates the sigma54-dependent `Ps` promoter while repressing the divergent `Pr` promoter [PMID:9489676 Activation of the toluene-responsive regulator XylR causes a transcriptional switch between sigma54 and sigma70 promoters at the divergent Pr/Ps region of the TOL plasmid., "These results support the notion that activation of XylR by aromatic inducers in vivo triggers a transcriptional switch between Pr and Ps."].

## Regulatory Context

- Catabolite repression acts on the TOL system partly by reducing translation of `xylR` and `xylS` [PMID:20529863 The Crc global regulator inhibits the Pseudomonas putida pWW0 toluene/xylene assimilation pathway by repressing the translation of regulatory and structural genes., "This study reports that Crc binds to sites located at the translation initiation regions of the mRNAs coding for XylR and XylS"].
- In KT2440 carrying pWW0, the global regulators Crc and PtsN modulate XylR-dependent expression from `Pu`/`Ps` [PMID:16085802 Integration of signals through Crc and PtsN in catabolite repression of Pseudomonas putida TOL plasmid pWW0., "Pu and P(S1) promoters of the pWW0 TOL plasmid are down-regulated in vivo during exponential growth in rich medium."].

## GO Assessment

- `GO:0043565 sequence-specific DNA binding`: strong keep. Supported by the C-terminal DNA-binding structure and the UAS-binding regulatory mechanism [PMID:3169574 Nucleotide sequence of the regulatory gene xylR of the TOL plasmid from Pseudomonas putida., "The C-terminal region (aa 515-558) has a putative DNA-binding structure."] [PMID:9489676 Activation of the toluene-responsive regulator XylR causes a transcriptional switch between sigma54 and sigma70 promoters at the divergent Pr/Ps region of the TOL plasmid., "which overlap the upstream activating sequences (UAS) for XylR"].
- `GO:0006355 regulation of DNA-templated transcription`: real but too broad. `GO:0045893 positive regulation of DNA-templated transcription` is a better primary BP term because XylR is mainly an activator of `Pu`/`Ps`, even though it also participates in autoregulatory repression at `Pr`.
- `GO:0005524 ATP binding`: mechanistically valid, but generic and less biologically informative than the activator function.
- Missing terms worth adding:
  - `GO:0141097 ligand-modulated transcription activator activity`
  - `GO:0042203 toluene catabolic process`
  - `GO:0042184 xylene catabolic process`

## Review Position

- This review should explicitly state that the curated protein is the plasmid-borne `xylR` regulator (`P06519`, taxon 303) placed under the `PSEPK` folder only because the request was framed around the KT2440 project bucket.
