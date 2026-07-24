# Manual literature synthesis for human ARSJ

## Research provenance

Manual synthesis was required because the Falcon request failed with HTTP 402 and its Perplexity-lite fallback failed with HTTP 401 on 2026-07-18. Sources checked were the reviewed UniProt record, current GOA, cached primary publications, Reactome, PubMed, and the Human Protein Atlas. This file is deliberately manual and is not named for a provider.

## Evidence synthesis

ARSJ encodes a 599-aa class-I sulfatase-family precursor. The reviewed sequence contains an N-terminal signal peptide and the conserved catalytic cysteine that class-I sulfatases convert to formylglycine. The comparative-genomics paper that discovered the complete human family includes ARSJ among four newly recognized members and emphasizes conservation of the catalytic site [PMID:16174644, "the active site, which is the target of the post-translational modification, is the most evolutionarily constrained region of sulfatases"]. These features support a broad sulfuric ester hydrolase assignment by phylogeny, but they do not identify the substrate.

The most important contrary/limiting evidence is the lack of a positive direct enzyme assay. The ARSI characterization paper summarizes the earlier ARSJ experiment as follows: [PMID:19262745, "ARSI and ARSJ cDNAs have been cloned and expressed in HeLa cells, but no ARS activity has been detected"]. A negative assay with a standard artificial aryl sulfate does not establish that ARSJ is inactive against its unknown native substrate. It does, however, make the narrow GO arylsulfatase term less defensible than the parent sulfuric ester hydrolase activity. Accordingly, both GO:0004065 records should be modified to GO:0008484, while the IBA and InterPro-derived GO:0008484 records can be accepted with an explicit uncertainty statement.

Localization is not settled. UniProt predicts cleavage of residues 1-49 as a signal peptide and assigns secretion. Reactome places the protein in the ER lumen during SUMF1-mediated formylglycine generation, which is expected for secretory-pathway sulfatases but does not establish where the mature protein acts. Human Protein Atlas reports enhanced actin-filament immunofluorescence in BJ fibroblasts with two antibodies and no staining in the other listed cell lines. The actin annotation should be retained as non-core rather than overruled, while its relationship to the secretory-pathway topology is tested experimentally.

Expression studies offer hypotheses rather than functions. Mouse embryonic in situ hybridization found ArsJ expression in joints [PMID:20503373, "novel expression patterns for ArsG in choroid plexus, ArsI in hypertrophic chondrocytes and ArsJ in joints were identified"]. A human RNA panel found lung enrichment [PMID:30760748, "ARSJ showed the highest expression in the lung compared to all other tissues"]. Neither observation supports a biological-process annotation without perturbation or substrate evidence.

## Curation conclusion

The defensible core is a probable formylglycine-dependent sulfuric ester hydrolase with an unidentified substrate. The extracellular and ER-lumen annotations describe predicted mature routing and biosynthetic processing, respectively; actin-filament staining is an unresolved cell-context localization. No new biological-process or substrate-specific molecular-function annotation is justified.
