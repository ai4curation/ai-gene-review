# Enterobacteria Phage P4 Gene psu (Polarity Suppression Protein Psu) — Curation Notes

## Overview
Enterobacteria satellite phage P4 gene *psu* (`P05460`, 190 aa, ~21.3 kDa) is the distal gene of the late `sid-delta-psu` operon (`PMID:3295254`, `PMID:2183201`) and encodes the polarity suppression (Rho-antitermination) protein Psu (`PMID:1938879`, `PMID:39788982`).

## Structural and Biochemical Mechanism
- **Antitermination of Rho-Dependent Transcription Termination in Phage and Host Operons**: Linderoth & Calendar (1991) demonstrated that Psu acts in *trans* in vivo to suppress Rho-dependent transcriptional polarity in the late morphogenetic operons of helper phage P2 (`GO:0050434`, `positive regulation of viral transcription`), in plasmid operons, and in the *Escherichia coli* chromosome (`GO:1990216`, `symbiont-mediated activation of host transcription`) [PMID:1938879, "In vivo, Psu protein acted in trans to suppress rho-dependent polarity in the late genes of an infecting P2 phage, in plasmid operons, and in the host chromosome."].
- **Cryo-EM Mechanism: Inhibition of Rho via Forced Hyper-Oligomerization**: Accomplished by homodimers of Psu (`GO:0042802`, `identical protein binding`) clamping two inactive, open hexameric/heptameric rings of host transcription termination factor ρ (Rho) and promoting their expansion into higher-order helical oligomers that cannot close around nascent RNA or hydrolyze ATP [PMID:39788982, "Our cryogenic electron microscopy structures of ρ-Psu complexes show that Psu dimers clamp two inactive, open ρ rings and promote their expansion to higher-oligomeric states."].

## GO Annotation Review
- **Accept**: `GO:0050434` (`positive regulation of viral transcription`, `IMP` `PMID:39788982`) and `GO:1990216` (`symbiont-mediated activation of host transcription`, `IDA` `PMID:1938879`).
- **New**: `GO:0042802` (`identical protein binding`, `IDA`, `PMID:39788982`), capturing the knotted V-shaped homodimerization of Psu required to cross-bridge two open Rho rings [PMID:39788982].
