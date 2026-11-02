# Bacteriophage P2 Gene ogr (Regulatory protein Ogr; UniProt P08762)

## Overview
Gene **ogr** (*organelle/overcoming growth restriction*) of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes a 72-amino-acid C4-type zinc-finger transcriptional activator (8.3 kDa; `UniProt:P08762`) essential for turning on the four P2 late promoters (`PP`, `PO`, `PV`, `PF`) that drive morphogenetic and lysis gene expression (`PMID:3735430`, `PMID:3458177`, `file:BPP2/ogr/ogr-uniprot.txt`). Ogr binds upstream of the late promoters (around -55) and directly contacts the alpha subunit (`RpoA`) of *Escherichia coli* host DNA-dependent RNA polymerase: the host `rpoA109` mutation blocks P2 late transcription, and the compensatory `ogr52` (`Y42C`) mutation restores productive interaction and phage growth (`PMID:3458177`). Ogr coordinates one $\text{Zn}^{2+}$ ion via four conserved cysteines (`Cys-4`, `Cys-7`, `Cys-27`, `Cys-30`; `InterPro:IPR007684` `Znf_Ogr/Delta` / `Pfam:PF04606`; `file:BPP2/ogr/ogr-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:3735430** (*Coliphage P2 late control gene ogr. DNA sequence and product identification.*):
  - `"The bacteriophage P2 late control gene ogr was cloned and precisely localized by deletion analysis in vitro. The DNA sequence of the ogr gene containing the ogr1 mutation was determined. The sequence translates into a basic protein of a molecular weight of 8300."`
- **PMID:3458177** (*Regulation of bacteriophage P2 late-gene expression: the ogr gene.*):
  - `"The ogr gene product of bacteriophage P2 is a positive regulatory factor required for P2 late-gene transcription. We have determined the nucleotide sequence of the ogr gene, which encodes a basic polypeptide of 72 amino acids. P2 growth is blocked by a host mutation, rpoA109, in the alpha subunit of DNA-dependent RNA polymerase. The ogr52 mutation, which allows P2 to grow in an rpoA109 strain, was shown to be a single nucleotide change, in the codon for residue 42, that changes tyrosine to cysteine."`

## Curation Decisions
- **Existing GOA Annotations**: None (`[]` in stub).
- **Proposed `NEW` Annotations**:
  - `GO:0001216` (`DNA-binding transcription activator activity`, IMP, `PMID:3458177`)
  - `GO:0008270` (`zinc ion binding`, IEA/NAS, `file:BPP2/ogr/ogr-uniprot.txt`)
  - `GO:0045893` (`positive regulation of DNA-templated transcription`, IMP, `PMID:3458177`)
  - `GO:0030430` (`host cell cytoplasm`, NAS, `PMID:3458177`)
