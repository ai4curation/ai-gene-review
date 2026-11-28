# rpoS notes

## Identity

- UniProt Q88ME8 encodes RNA polymerase sigma factor RpoS, also called Sigma S or Sigma-38, a cytoplasmic sigma-70 family protein in the RpoS subfamily. [file:PSEPK/rpoS/rpoS-uniprot.txt]

## Core role in KT2440

- In KT2440, the rpoS mutant showed reduced survival of carbon starvation and reduced cross-protection against other types of stress in cells starved for carbon, and RpoS controlled expression of more than 50 peptides after short carbon starvation. [PMID:9642197 Cloning, sequencing, and phenotypic characterization of the rpoS gene from Pseudomonas putida KT2440., "showed reduced survival of carbon starvation and reduced cross-protection against other types of stress in cells starved for carbon" and "controls the expression of more than 50 peptides"]
- This supports treating sigma factor activity and DNA-templated transcription initiation as the core GO-level functions, with response to starvation as a justified downstream biological process. [PMID:9642197 Cloning, sequencing, and phenotypic characterization of the rpoS gene from Pseudomonas putida KT2440., "reduced survival of carbon starvation"]

## Upstream regulation

- PsrA activates rpoS expression: psrA mutants showed a 90% decrease in rpoS promoter activity and lost the ability to induce rpoS expression at stationary phase. [PMID:11371535 Regulation of rpoS gene expression in Pseudomonas: involvement of a TetR family regulator., "showed a 90% decrease in rpoS promoter activity" and "lost the ability to induce rpoS expression at stationary phase"]
- PsrA binds directly to the rpoS promoter from positions -59 to -35 relative to the transcription start site. [PMID:11914368 TetR family member psrA directly binds the Pseudomonas rpoS and psrA promoters., "PsrA binds from positions -59 to -35 in the rpoS promoter"]

## Biofilm and lifestyle outputs

- RpoS directly bound the major wspA promoter and was required for tetracycline to induce wspA activity and promote biofilm formation. [PMID:39589111 Tetracycline induces wsp operon expression to promote biofilm formation in Pseudomonas putida., "RpoS directly bound to PwspA and positively regulated its activity under tetracycline stress" and "RpoS was required for tetracycline to induce PwspA activity and promote biofilm formation"]
- Expression of cfcR is transcriptionally regulated by RpoS, and cfcR provides most free c-di-GMP during stationary phase in static conditions. [PMID:28677348 The Pseudomonas putida CsrA/RsmA homologues negatively affect c-di-GMP pools and biofilm formation through the GGDEF/EAL response regulator CfcR., "Expression of cfcR ... is transcriptionally regulated by RpoS" and "cfcR ... is responsible for most of the free c-di-GMP during stationary phase in static conditions"]
- lapA transcription is initiated from six promoters, three of which show moderate RpoS dependence, while lapF transcription responds to the stationary-phase sigma factor RpoS. [PMID:28945818 The promoter region of lapA and its transcriptional regulation by Fis in Pseudomonas putida., "transcription of lapA ... is initiated from six promoters, three of which display moderate RpoS-dependence"] [PMID:24488315 Roles of cyclic Di-GMP and the Gac system in transcriptional control of the genes coding for the Pseudomonas putida adhesins LapA and LapF., "lapF transcription was previously shown to take place at late times of growth and to respond to the stationary-phase sigma factor RpoS"]

## Curation take

- GO:0016987 sigma factor activity is the precise molecular function term for RpoS and is more informative than the generic GO:0003700 DNA-binding transcription factor activity.
- GO:0006352 DNA-templated transcription initiation and GO:2000142 regulation of DNA-templated transcription initiation capture the direct process-level role better than GO:0006355 regulation of DNA-templated transcription or GO:0010468 regulation of gene expression.
- GO:0003677 DNA binding is too generic for a sigma factor whose core activity is promoter specificity within RNA polymerase holoenzyme rather than a standalone DNA-binding regulator.
- Biofilm formation is well supported but should be treated as a non-core pleiotropic output of the RpoS regulon rather than the main evolved function of the protein.

## 2026-11-16 — TF batch 2: sigma-factor activity and PwspA

All eight machine-seeded annotations were re-reviewed. Generic DNA binding is true and is refined to GO:0001046 core promoter sequence-specific DNA binding, supported by the experimentally required -10 motif. Sigma factor activity is the specific TF activity. Transcription/gene-expression regulation refines to the already annotated transcription-initiation regulation. A lack of standalone enzymatic activity does not negate promoter binding by a sigma factor.

[PMID:9642197, Cloning, sequencing, and phenotypic characterization of the rpoS gene from Pseudomonas putida KT2440] replaces notes-as-evidence for the retained starvation-response IMP. The generic stress-response NEW is an ancestor of starvation response and was withdrawn as redundant. The authored biofilm-formation execution proposal and secondary non-core biofilm core-function block were withdrawn. The proposed stationary-phase-specific sigma MF is unnecessary: existing sigma activity plus biological context suffice.

[PMID:39589111, Tetracycline induces wsp operon expression to promote biofilm formation in Pseudomonas putida] full text supports direct activation of PwspA/PP_1488. Purified His-RpoS EMSA with competitor probes and CTATACT→TCGGCAC -10 mutation agree with promoter-lacZ deletion/complementation assays. Standard motif reporter assays used ten-hour LB cultures; the separate tetracycline assays added 6 µg/mL for four hours after six-hour preculture at 28°C. The quoted Fig. 5 motif experiments are not themselves labeled tetracycline-treated. The sidecar represents the major promoter, not seven independent contacts. PwspF effects were indirect. This evidence establishes transcriptional regulation of Wsp/c-di-GMP signaling; WspR and downstream biofilm machinery execute the other processes. No additional biofilm GO proposal was introduced without a separate comparator audit.

The 2026 sigma-regulon study's full PDF is accessible at https://link.springer.com/content/pdf/10.1186/s13036-026-00769-z_reference.pdf and was inspected during annotation-reviewer consultation. Its unproductive-initiation model remains proposed; supplementary target table S6 was not inspected, so no bulk target import was made.

Provider research and existing machine/publication sources remain byte-identical. FEBA was unavailable and no fitness artifact was created. No MOD-description provider applies to PSEPK.
