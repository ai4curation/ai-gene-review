# Deep research: rpoS in Pseudomonas putida KT2440

## Summary

rpoS encodes the stationary-phase sigma factor RpoS (Sigma S, Sigma-38), an alternative sigma-70 family subunit that redirects RNA polymerase to promoters used during stationary phase and stress adaptation. In P. putida KT2440, the direct experimental core is not an enzymatic stress-defense activity, but promoter-specific transcription initiation and global transcriptional reprogramming during carbon starvation and related stress conditions. [PMID:9642197 Cloning, sequencing, and phenotypic characterization of the rpoS gene from Pseudomonas putida KT2440., "reduced survival of carbon starvation" and "controls the expression of more than 50 peptides"] [file:PSEPK/rpoS/rpoS-uniprot.txt]

## Direct evidence for core function

The defining KT2440 paper showed that loss of rpoS reduced survival during carbon starvation, weakened starvation-associated cross-protection, and altered the stationary/starvation proteome. This supports the view that the core GO curation should center on sigma factor activity, DNA-templated transcription initiation, and regulation of transcription initiation during starvation-associated stress adaptation. [PMID:9642197 Cloning, sequencing, and phenotypic characterization of the rpoS gene from Pseudomonas putida KT2440., "reduced survival of carbon starvation and reduced cross-protection against other types of stress in cells starved for carbon" and "controls the expression of more than 50 peptides"]

UniProt is consistent with this assignment, describing Q88ME8 as RNA polymerase sigma factor RpoS, placing it in the sigma-70 family RpoS subfamily, and localizing it to the cytoplasm. [file:PSEPK/rpoS/rpoS-uniprot.txt]

## Regulation of rpoS itself

Two early Pseudomonas studies established PsrA as a direct upstream regulator. First, psrA mutants showed a 90% decrease in rpoS promoter activity and lost stationary-phase induction of rpoS. Second, PsrA was shown to bind directly to the rpoS promoter from positions -59 to -35. These papers matter for review because they confirm that rpoS is embedded in a dedicated regulatory cascade rather than acting as a constitutive housekeeping sigma factor. [PMID:11371535 Regulation of rpoS gene expression in Pseudomonas: involvement of a TetR family regulator., "showed a 90% decrease in rpoS promoter activity" and "lost the ability to induce rpoS expression at stationary phase"] [PMID:11914368 TetR family member psrA directly binds the Pseudomonas rpoS and psrA promoters., "PsrA binds from positions -59 to -35 in the rpoS promoter"]

## Downstream outputs and non-core biology

Recent work expands the downstream RpoS regulon into surface-associated lifestyles. Under tetracycline stress, RpoS directly bound the major wspA promoter and was required for tetracycline-induced biofilm formation. Independent studies also place RpoS upstream of cfcR and parts of the lapA/lapF adhesin program, linking RpoS to c-di-GMP signaling and biofilm maturation. These are biologically real functions, but they are best treated as conditional or pleiotropic outputs rather than the single core function of RpoS. [PMID:39589111 Tetracycline induces wsp operon expression to promote biofilm formation in Pseudomonas putida., "RpoS directly bound to PwspA" and "RpoS was required for tetracycline to induce PwspA activity and promote biofilm formation"] [PMID:28677348 The Pseudomonas putida CsrA/RsmA homologues negatively affect c-di-GMP pools and biofilm formation through the GGDEF/EAL response regulator CfcR., "Expression of cfcR ... is transcriptionally regulated by RpoS"] [PMID:28945818 The promoter region of lapA and its transcriptional regulation by Fis in Pseudomonas putida., "three of which display moderate RpoS-dependence"] [PMID:24488315 Roles of cyclic Di-GMP and the Gac system in transcriptional control of the genes coding for the Pseudomonas putida adhesins LapA and LapF., "lapF transcription was previously shown to take place at late times of growth and to respond to the stationary-phase sigma factor RpoS"]

## GO curation implications

- Accept GO:0016987 sigma factor activity as the best core molecular function.
- Accept GO:0006352 DNA-templated transcription initiation as the direct process executed by RpoS-containing holoenzyme.
- Accept GO:2000142 regulation of DNA-templated transcription initiation as the best specific regulatory BP term already present.
- Treat GO:0003700 DNA-binding transcription factor activity as too generic and better replaced by sigma factor activity.
- Treat GO:0006355 regulation of DNA-templated transcription and GO:0010468 regulation of gene expression as overly broad relative to GO:2000142.
- Add response to starvation as a justified new BP term supported by the KT2440 mutant phenotype.
- Biofilm formation is supportable but non-core.
