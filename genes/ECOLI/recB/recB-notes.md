# recB (Escherichia coli K-12, P08394) - curation notes

Author: Claude (AI-assisted)

## Provenance

Deep research was not run for this gene (no deep-research provider API keys were
available in this session). These notes summarize the cached publications in
`publications/` (most are abstract-only; `full_text_available: false`) and the curated
UniProt record `recB-uniprot.txt`. Quotes are verbatim from those sources.

## Identity and architecture

- RecB is the 1180-residue largest subunit of the heterotrimeric RecBCD enzyme
  (Exonuclease V). UniProt: "Heterotrimer of RecB, RecC and RecD." (CC SUBUNIT,
  ECO:0000269 PubMed:15538360, 1618858).
- N-terminal UvrD-like SF1A helicase motor (UvrD-like ATP-binding domain 2-450, C-terminal
  helicase domain 480-746, Walker A ATP site 23-30, K29Q kills ATPase/helicase) and a
  C-terminal PD-(D/E)XK nuclease domain (region 900-1180; Mg2+ ligands D956, D1067, D1080,
  K1081; D1080A abolishes holoenzyme nuclease).
- PANTHER PTHR11070:SF23 (RECBCD ENZYME SUBUNIT RECB); NCBIfam TIGR00609; HAMAP MF_01485.

## Molecular functions

- 3'-5' DNA helicase / ssDNA translocase.
  [PMID:12815438 "For some time it has been clear that the RecB subunit possesses a 3' --> 5' DNA helicase activity"]
  [PMID:12815437 "RecB is a slow helicase acting on the 3'-ended strand on which the single-stranded loop accumulates"]
  [PMID:1311326 "The purified RecB protein can function as a DNA helicase, displacing oligonucleotides annealed to viral M13 DNA in an ATP-dependent and orientation-specific manner."]
  [PMID:9150267 "suggesting that the RecB protein translocates along the 60-mer in the 3' to 5' direction, displacing annealed 20-mers as it proceeds"]
- ATP binding and DNA-dependent ATP hydrolysis.
  [PMID:3155726 "The purified RecB protein has DNA-dependent ATPase activity but no exonuclease activity."]
  [PMID:3298248 "the label is largely confined to two peptides obtained by tryptic digestion of the photolabeled holoenzyme; one is derived from the recB subunit and the other from the recD subunit."]
- Exodeoxyribonuclease V (EC 3.1.11.5): RecB carries the only nuclease active site of the
  holoenzyme. [PMID:9448271 "These results show that the 30-kDa C-terminal domain of RecB has an important role in the nuclease activity of RecBCD."]
  [PMID:16388588 "These results provide direct evidence that RecB30 is the universal nuclease domain of RecBCD."]
  The isolated RecB30 domain also cleaves circular ssDNA and dsDNA endonucleolytically
  [PMID:16388588 "The endonucleolytic cleavage of circular dsDNA is consistent with the fact that RecB30 has amino acid sequence similarity to some restriction endonucleases."]
  Exonuclease activity needs RecB plus RecC (RecB alone is not a nuclease):
  [PMID:3155726 "when combined together, the RecB and RecC proteins show the ATP-dependent double-stranded exonuclease properties characteristic of the RecBC DNase."]
- DNA end binding: RecBC/RecBCD bind duplex ends and melt ~6 bp without ATP
  [PMID:16126227 "These data suggest that both RecBC and RecBCD helicases can destabilize or \"melt out\" six base-pairs upon binding to a blunt DNA duplex end in the absence of ATP."]
- RecA loading after Chi is a RecB nuclease-domain function (UniProt CC DOMAIN, PubMed:16483938);
  Chi itself is recognized by RecC [PMID:15538360 "Passage of the 3' tail through one of these tunnels provides a mechanism for the recognition of a Chi sequence by RecC within the context of double-stranded DNA."]

## Processes

- DSB repair via homologous recombination (core).
  [PMID:19052323 "The RecBCD enzyme of Escherichia coli is a helicase-nuclease that initiates the repair of double-stranded DNA breaks by homologous recombination."]
- Homologous recombination (conjugation/transduction) and joint-molecule formation in vitro.
  [PMID:2014257 "RecBCD enzyme initiates the process by unwinding the linear double-stranded DNA to produce single-stranded DNA, which is trapped by SSB and RecA."]
  [PMID:6389498 "the RecBC gene products, exonuclease V, is not essential for the growth of E. coli but is important for DNA repair and recombination."]
- Degradation of foreign linear DNA (phage defence).
  [PMID:19052323 "It also degrades linear double-stranded DNA, protecting the bacteria from phages and extraneous chromosomal DNA."]
  [PMID:123277 "we found that in vivo the effects of the double-strand exonucleolytic activity of the recBC nuclease predominated."]
- Radiation sensitivity of mutants (pleiotropic DNA-repair consequence): UniProt DISRUPTION
  PHENOTYPE (PubMed:6389498) "Cells are deficient in DNA recombination repair and have increased
  sensitivity to UV light." The Keio screen (PMID:27718375, abstract-only) does not name recB in
  its abstract; the curator's IMP is accepted on the basis of the gene's well-known UV/X-ray
  sensitivity.

## Interactions

- RecC (P07648): structural partner in the holoenzyme (PMID:15538360); captured by
  GO:0009338 part_of; bare protein binding row removed per policy.
- YgbT/Cas1 (Q46896): co-purification and co-IP (PMID:21219465 full text). Bare protein binding
  removed per policy; no informative MF follows.

## Decisions (summary)

- Correct-but-general MF/BP terms MODIFY to the specific terms the gene already carries:
  DNA helicase activity -> GO:0043138; ATP-dependent activity, acting on DNA -> GO:0043138 +
  GO:0015616; hydrolase activity -> GO:0008854 + GO:0016887; DNA binding -> GO:0045027 DNA end
  binding; DNA repair and recombinational repair -> GO:0000724; DNA recombination ->
  GO:0000724 + GO:0035825.
- Kept shared terms consistent with the P. putida KT2440 RecB review (genes/PSEPK/recB).
- PAINT: PTN000116141 (GO:0043138, GO:0000725), PTN000116249 (GO:0009338),
  PTN000869814 (GO:0005829); `just paint-losses ECOLI recB` reports no IRD/IKR loss.
