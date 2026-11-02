# so (sine oculis) - curation notes

Automated deep research was not available for this review (falcon 402, OpenAI 401), so no
`-deep-research-<provider>.md` file exists. Notes below are from cached publications and UniProt Q27350.

## Identity
- SIX/Sine oculis homeobox family (Six1/2 subfamily; PANTHER PTHR10390:SF61), SIX domain + SIX-type homeodomain (UniProt).
- [PMID:9428512 "so encodes a highly diverged homeobox transcription factor and eya encodes a novel nuclear protein"]

## Molecular function
- DNA binding / motif: [PMID:15901665 "By systematic analysis of the DNA-binding specificity of so we identified the most important nucleotides for this interaction."]
- Direct targets: atonal eye enhancer [PMID:17108002 "the RD factors Eyeless and Sine oculis function as direct regulators"]; lozenge [PMID:14597205 "We provide evidence that Sine oculis and Glass are the two major activators of Lz expression during eye development."]; so autoregulation, ey, hh [PMID:15901665 "have thereby been able to identify eyeless as well as the signalling gene hedgehog as putative targets of so"].
- So/Eya complex: [PMID:17714699 "Two members of this network, Eyes absent (EYA) and Sine oculis (SO), form a transcriptional complex in which EYA provides the transactivation function while SO provides the DNA binding activity."]
- Groucho repression: [PMID:12917324 "GROUCHO-SINE OCULIS (SO) interactions provide another mechanism for negative regulation of EYA-SO target genes"]
- Other partners: Sobp (PMID:16125693), Ey (PMID:17108002), Fl(2)d/WTAP (PMID:24690230; functional significance unclear).

## Upstream
- [PMID:10207149 "the EY protein activates transcription of sine oculis by direct interaction with an eye-specific enhancer in the long intron of the so gene"]

## Processes
- Eye disc, optic lobe primordium: [PMID:7910468 "So is expressed in the optic lobe primordium prior to its invagination from the embryonic ectoderm; in so mutants, the optic lobe primordium fails to invaginate."]
- Bolwig's organ: [PMID:10704398 "Neither Atonal expression nor Bolwig's organ formation occurred in the absence of hedgehog, eyes absent or sine oculis activity."]
- Sufficiency: [PMID:17137572 "expression of so on its own is sufficient to induce eye development within non-retinal tissues"]
- Testis cyst cells (PMID:12781687), corpus cardiacum (PMID:15385159).

## Curation decisions
- Protein binding rows: Sobp -> MODIFY GO:0001221; Ey -> MODIFY GO:0140297; Fl(2)d -> REMOVE (no informative MF).
- Circadian rhythm (PMID:3097291) and clock entrainment (PMID:12417651) used so as an eye/optic-lobe-ablating tool -> MARK_AS_OVER_ANNOTATED.
- Module annoton GO:0000981 for the Six family agrees with this review.
