# Curation Notes: Mycobacterium phage L5 Gene 71 (gp71 / IMM, Q05286)

## Overview
- **UniProt ID:** Q05286 (`VG71_BPML5`)
- **Gene Symbol:** `71` (Synonym: `IMM`)
- **Length:** 183 amino acids (20.6 kDa)
- **Genomic Context:** Encoded on the leftwards-transcribed right arm of the Mycobacterium phage L5 genome at the boundary between the early lytic genes (`72`–`88`) and the replication/recombination genes (`56`–`70`) [PMID:8459766, PMID:8459767, PMID:8594325].

## Literature & Experimental Evidence
- **Discovery of superinfection immunity and lysogeny maintenance ([PMID:8459767]):**
  - Donnelly-Wu, Jacobs, and Hatfull (1993) demonstrated that the 183-amino-acid product of L5 gene 71 (gp71) confers immunity to L5 superinfection, is required for maintenance of the lysogenic state, and contains a helix-turn-helix (HTH) DNA-binding motif (residues 34–53) characteristic of temperate phage repressors [PMID:8459767].
- **Transcriptional regulation of gene 71 ([PMID:8594325]):**
  - Nesbit et al. (1995) showed that in an L5 lysogen, gene 71 is transcribed from three upstream promoters that do not require any phage-encoded proteins. During early lytic growth, gene 71 is also transcribed from the early lytic promoter `Pleft` at the right end of the genome, which is itself regulated by gp71 [PMID:8594325].
- **Mechanism of transcriptional silencing via operator and stoperator sites ([PMID:9312049]):**
  - Brown et al. (1997) purified and biochemically characterized gp71, demonstrating that it is an atypical phage repressor that binds to multiple asymmetric 13-bp consensus DNA sites (`5'-GGTGGATGTCAAG-3'`) distributed throughout the L5 genome [PMID:9312049].
  - gp71 binds operator sites at the early lytic promoter `Pleft` to repress transcription initiation, and also binds numerous 'stoperator' sites located within short intergenic spaces in both early and late lytic operons in a specific orientation relative to transcription [PMID:9312049].
  - Binding of gp71 to stoperator sites causes a strong orientation-dependent polar block to transcription elongation, resulting in global silencing of prophage lytic gene expression during lysogeny [PMID:9312049].
- **Comparative genomics ([PMID:9636706]):**
  - Ford et al. (1998) showed that the closely related lytic mycobacteriophage D29 lacks a 3.6 kb region encompassing gene 71, accounting for the inability of D29 to establish lysogeny while remaining sensitive to superinfection immunity conferred by L5 gp71 [PMID:9636706].

## Domain & Family Architecture
- **UniProt FT:** `DNA_BIND 34..53 /note="H-T-H motif"` (`ECO:0000255`), and mutagenesis sites at `Arg-108` (`R->L: Class I phenotype`), `Leu-123` (`L->P: Thermo-inducible phenotype`), and `Glu-124` (`E->G: Thermo-inducible phenotype`) (`ECO:0000269|PubMed:8459767`).
- **OrthoDB:** `8945at10239`
- **UniProt Keywords:** `DNA-binding`, `Reference proteome`, `Transcription`, `Transcription regulation` (`PE 1: Evidence at protein level`).

## GO Annotation Decisions
- Review of existing GOA annotation:
  - `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000043`, `UniProtKB-KW:KW-0238`): **MODIFY** to `GO:0000976` (`transcription cis-regulatory region binding`). While `GO:0003677` is true, direct biochemical experiments in [PMID:9312049] establish that gp71 specifically binds asymmetric operator (`Pleft`) and intergenic stoperator cis-regulatory DNA sequences to silence transcription.
- Propose `NEW` experimental annotations:
  - `GO:0000976` (`transcription cis-regulatory region binding`, IDA, `PMID:9312049`, `enables`): directly demonstrated by DNA binding to `Pleft` operator and genome-wide stoperator sites [PMID:9312049].
  - `GO:0003700` (`DNA-binding transcription factor activity`, IDA, `PMID:9312049`, `enables`): gp71 is a sequence-specific HTH transcriptional repressor that regulates transcription initiation at `Pleft` and elongation at stoperator sites [PMID:8459767, PMID:9312049].
  - `GO:0045892` (`negative regulation of DNA-templated transcription`, IDA, `PMID:9312049`, `involved_in`): gp71 represses transcription initiation at `Pleft` and causes orientation-dependent transcriptional silencing at stoperator sites [PMID:9312049].
  - `GO:0019042` (`viral latency`, IMP, `PMID:8459767`, `involved_in`): gp71 is required for maintenance of the lysogenic (prophage) state and confers superinfection immunity [PMID:8459767].
