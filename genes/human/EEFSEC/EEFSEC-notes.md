# EEFSEC (eEFSec) - Review Notes

## Gene Overview

EEFSEC encodes the selenocysteine-specific elongation factor (eEFSec), a specialized translational GTPase required for the cotranslational incorporation of selenocysteine (Sec, the 21st amino acid) at UGA codons in selenoprotein mRNAs. UniProt: P57772. 596 AA, 65.3 kDa.

## Key Literature

### Discovery (2000)
- **Fagegaltier et al. 2000** [PMID:10970870]: First characterization of the mammalian eEFSec (called mSelB). Identified as eukaryotic homolog of bacterial SelB. Demonstrated GTP binding, Sec-tRNA(Sec) recognition in vitro and in vivo, and requirement for efficient selenoprotein translation. Crucially showed that unlike bacterial SelB, mSelB alone cannot bind SECIS RNA directly — requires an additional factor (later identified as SBP2/SECISBP2).

### Crystal structure (2016)
- **Dobosz-Bartoszek et al. 2016** [PMID:27708257, "Crystal structures of the human elongation factor eEFSec suggest a non-canonical mechanism for selenocysteine incorporation"]: Solved crystal structures of human eEFSec in complex with GDP/Mg2+/Mn2+. Key findings:
  - Four-domain chalice-like structure (D1-D4)
  - Similar binding affinities for GDP, GTP, and other guanine nucleotides (unusual for translation GTPases)
  - Guanine nucleotide exchange does NOT cause major conformational change in D1 (unlike eEF1A/EF-Tu)
  - Instead, nucleotide exchange induces a swing of D4
  - Proposed non-canonical mechanism involving D4 for selenocysteinyl-tRNA release during decoding
  - GTPase activity demonstrated (IDA evidence)
  - Selenocysteine incorporation demonstrated (IDA evidence)
  - Mutagenesis: D229A, H230A, R285A, R285N all abolished selenocysteine incorporation; H96A abolished GTPase activity; R583A/Y584A had no effect

### Cryo-EM structure of the selenosome (2022) - BioReason-Pro case study
- **Hilal et al. 2022** [PMID:35709277, "Structure of the mammalian ribosome as it decodes the selenocysteine UGA codon"]: Landmark cryo-EM structure of the complete mammalian selenosome at 2.8 Å. Key findings:
  - Visualized the preaccommodated state of Sec UGA recoding on 80S ribosome
  - eEFSec, SBP2, SECIS, and Ser-tRNA(Sec) form an extended network on the ribosome
  - **eEFSec and SBP2 do NOT interact directly** — they deploy their C-terminal domains to engage opposite ends of the SECIS RNA
  - SBP2 binds 40S ribosome first via eS31 interaction, forming docking site for eEFSec ternary complex
  - eEFSec D1-D3 bind at GAC (GTPase-associated center), D4 contacts SECIS apical loop
  - tRNA(Sec) in A/T conformation, anticodon properly positioned in decoding center
  - Thr242 identified as key selectivity residue for amino acid selection
  - eEFSec is indiscriminate toward L-serine and can misincorporate it at Sec UGA codons
  - Mechanism: (1) SBP2 binds SECIS at kink-turn, (2) SBP2-SECIS complex binds 40S beak via eS31, (3) GTP-bound eEFSec delivers Sec-tRNA(Sec) to stalled ribosome, (4) GTP hydrolysis, eEFSec dissociates, Sec-tRNA accommodates

### Disease association (2025)
- **Laugwitz et al. 2025** [PMID:39753114, "EEFSEC deficiency: A selenopathy with early-onset neurodegeneration"]: Identified biallelic EEFSEC variants causing neurodevelopmental disorder with progressive spasticity and brain abnormalities (NEDPSB, MIM:621102). Autosomal recessive, onset in infancy/early childhood. Characterized pathogenic variants: P194T, R285Q, D390A, C426-P596 deletion — all showed decreased selenocysteine incorporation. A35V was likely benign.

## Functional Summary

1. **Molecular Function**: GTPase activity; translation elongation factor activity specialized for selenocysteine
2. **Biological Process**: Selenocysteine incorporation during translation
3. **Cellular Component**: Cytoplasm (primary), nucleus (also reported)
4. **Key Interactions**: Sec-tRNA(Sec) binding, SECIS RNA interaction via D4, forms functional complex with SBP2/SECISBP2 on the ribosome (but no direct protein-protein interaction with SBP2)
5. **Pathway**: Reactome R-HSA-2408557 (Selenocysteine synthesis)

## Annotation Assessment Notes

- IDA annotations for GTPase activity and selenocysteine incorporation are well-supported by PMID:27708257 and PMID:35709277
- IBA annotations from PANTHER are consistent
- IEA annotations for tRNA binding, SECIS binding, ribonucleoprotein complex binding are reasonable but need careful review
- The SECIS binding annotation is nuanced: eEFSec contacts SECIS via D4 but this is RNA binding, not strictly "SECIS binding" in the way SBP2 binds SECIS. In bacteria SelB binds SECIS directly, but in eukaryotes eEFSec's SECIS contact is different.
- The nucleus annotation is based on a predicted NLS (residues 547-553) but functional relevance unclear
- "Ribonucleoprotein complex" annotation is somewhat generic
