# Enterobacteria phage M13 — Gene II (G2P / pII and G10P / pX)

## Overview
- **UniProt Accession:** P69547 (`REP_BPM13`)
- **Gene Symbol:** `II`
- **Alternative Products:**
  - **Isoform G2P (pII, P69547-1):** Full-length 410 aa (~46.2 kDa) site-specific rolling-circle replication endonuclease/nickase-closing enzyme (`file:BPM13/II/II-uniprot.txt`).
  - **Isoform G10P (pX, P69547-2):** 111 aa (~12.6 kDa) protein translated from an internal in-frame start codon at Met-300 (missing residues 1–299). Acts as a dsDNA-binding inhibitor of viral DNA replication that regulates the switch from double-stranded replicative form (RF) amplification to progeny (+)ssDNA synthesis (`file:BPM13/II/II-uniprot.txt`).

## Biological Role in the M13 Lifecycle
- **Rolling-Circle Viral DNA Replication (pII):** Isoform pII recognizes and binds the viral (+) strand origin of replication on supercoiled double-stranded replicative form I (RFI) DNA, introduces a site-specific single-stranded nick in the (+) strand, and becomes covalently linked to the 5'-phosphate end via a phosphotyrosine bond, generating nicked RFII with a free 3'-OH primer for host DNA polymerase III holoenzyme elongation [PMID:4930572]. After one complete round of rolling-circle displacement synthesis, pII cleaves the regenerated origin and catalyses strand-transfer religation (joining the ends of the displaced (+)ssDNA without ATP cofactor consumption) to release a closed circular (+)ssDNA progeny genome (`file:BPM13/II/II-uniprot.txt`).
- **Note on EC:6.5.1.1 / ATP-Dependent Ligase Misannotation:** UniProt carries an automated `EC=6.5.1.1` (DNA ligase (ATP) activity) assignment and `ATP-binding` keyword, which propagate to `GO:0003910` (DNA ligase (ATP) activity), `GO:0016874` (ligase activity), and `GO:0005524` (ATP binding). However, inovirus pII is a HUH/relaxase-like rolling-circle replication initiator endonuclease/transesterase that conserves cleavage energy via a covalent 5'-phosphotyrosyl intermediate to rejoin the displaced single strand; it is not an ATP-dependent DNA ligase (`EC 6.5.1.1`).

## Key GO Annotations
- **Molecular Function:** `GO:0004519` (endonuclease activity) and `GO:0003677` (DNA binding).
- **Biological Process:** `GO:0039684` (rolling circle single-stranded viral DNA replication) [PMID:4930572].
