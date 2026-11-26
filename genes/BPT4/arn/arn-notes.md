# Curation Notes: Bacteriophage T4 `arn` (UniProt P39510)

## Identity and Nomenclature
- **Gene symbol:** `arn` (synonym: `soc.4`)
- **UniProt accession:** `P39510` (`ARN_BPT4`)
- **Protein name:** Anti-restriction endonuclease (Anti-rgl nuclease; DNA-mimic protein Arn)
- **Length:** 92 AA (10,757 Da)
- **Organism:** Enterobacteria phage T4 (`NCBITaxon:10665`)

## Summary of Experimental and Structural Evidence
- **Function as an Anti-Restriction DNA-Mimic Protein:** `arn` encodes a 92-amino-acid protein (`Pfam:PF22134`, `DM_Arn`, `InterPro:IPR054354`) that protects non-glucosylated 5-hydroxymethylcytosine-containing T4 DNA against host modification-dependent restriction endonucleases (`rglA`/`mcrA` and `rglB`/`mcrBC`; Dharmalingam & Goldberg 1976, PubMed 768783; Behme et al. 1976, PubMed 785009; Kim et al. 1997, PubMed 9330320).
- **Crystal Structure and Mechanism (Ho et al. 2014, PDB `3WX4`):** X-ray crystallography of T4 Arn at 1.90 Å resolution (`PDB; 3WX4; X-ray; 1.90 A; A=1-92.`) and biochemical studies demonstrated that Arn is a homodimer whose negatively charged surface mimics the phosphate backbone of double-stranded B-form DNA, analogous to phage T7 Ocr. Arn binds directly to the DNA-binding domain of host modification-dependent restriction endonucleases (such as McrBC and McrA), competitively blocking their binding to and cleavage of modified phage DNA.
- **Critical Curation Finding — Mis-annotated Nuclease Keywords in UniProt:** Because the legacy protein name in UniProt is `"Anti-restriction endonuclease"` (intended to mean `anti-[restriction endonuclease]`, i.e., an inhibitor of restriction endonuclease), automated UniProt keyword assignment erroneously tagged `P39510` with `Endonuclease; Hydrolase; Nuclease`, generating false-positive IEA (`GO_REF:0000043`) annotations to `GO:0004518` (`nuclease activity`), `GO:0004519` (`endonuclease activity`), and `GO:0016787` (`hydrolase activity`). Arn has no catalytic nuclease or hydrolase activity whatsoever; it is a non-catalytic DNA-mimic inhibitor of host restriction endonucleases (`GO:0004857`, `enzyme inhibitor activity`).

## Review of Existing GO Annotations
1. `GO:0004518` (`nuclease activity`, IEA `GO_REF:0000043`), `GO:0004519` (`endonuclease activity`, IEA `GO_REF:0000043`), and `GO:0016787` (`hydrolase activity`, IEA `GO_REF:0000043`): **REMOVE**. These three IEA annotations are classic lexical false positives caused by parsing the protein name `"Anti-restriction endonuclease"` as an endonuclease rather than an inhibitor of restriction endonucleases. Arn is a 92-AA non-catalytic DNA-mimic protein (`PF22134`) that inhibits host McrA/McrBC endonucleases.
2. `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`, IEA `GO_REF:0000043`): **ACCEPT**. Directly captures the primary biological function of Arn in inhibiting host modification-dependent restriction systems.
3. `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA `GO_REF:0000043`) and `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`), the specific descendant term already present on the gene.
