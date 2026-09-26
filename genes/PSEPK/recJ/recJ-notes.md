# recJ curation notes

## 2026-08-08 pathway pass

Q88MU1 is assigned to the single-stranded-DNA-specific RecJ exonuclease family
[file:PSEPK/recJ/recJ-uniprot.txt, "SINGLE-STRANDED-DNA-SPECIFIC EXONUCLEASE
RECJ"]. The generic GO:0008409 annotation is therefore modified to GO:0045145,
which preserves the 5'-3' direction and adds the single-stranded-DNA substrate.

Primary E. coli genetics places RecJ together with RecQ in presynaptic ssDNA-gap
extension [PMID:35653392, "the extension of the ssDNA gap (mediated by the
nuclease RecJ and the helicase RecQ)"].

## Mismatch-repair module pass

Q88MU1 has the DHH, DHHA1, and OB-domain architecture of a RecJ
single-stranded-DNA exonuclease. The imported GO:0008409 directional parent is
refined to GO:0045145, which captures both single-stranded DNA and 5'-to-3'
directionality. DNA repair and recombination were accepted as conserved RecJ
roles. Its MMR-specific role is kept as a testable module candidate because no
direct KT2440 evidence was found.

### OpenScientist adjudication

The OpenScientist report corroborated the DHH/DHHA1/OB-domain architecture,
5'-to-3' single-stranded-DNA exonuclease activity, and conserved repair and
recombination roles. Its mismatch-repair assignment remains orthology-based.
The report also incorrectly describes `recJ` (`PP_1477`) as adjacent to `recO`
(`PP_1435`); this genomic-context claim was rejected and is not used in the
review or module.

## 2026-09-26 merge reconciliation

`main` acquired an independent recJ review through the MutH-independent mismatch
repair curation (#2258) while this RecFOR branch was open. Both passes reach the
same verdict on every shared GOA row (`GO:0003676` MARK_AS_OVER_ANNOTATED,
`GO:0006281` ACCEPT, `GO:0006310` ACCEPT, `GO:0008409` MODIFY to `GO:0045145`),
so the RecFOR version was kept as the superset: it additionally reviews the
`GO:0003824` row present in the newer GOA fetch (20260727) and carries verbatim
supporting text throughout. The mismatch-excision question and the RecJ/ExoVII
redundancy experiment contributed by the `main` pass were retained.
