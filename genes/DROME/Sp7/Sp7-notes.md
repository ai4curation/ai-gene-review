# Sp7 (Q9V3Z2, CG3066; synonyms MP2, PAE1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Sp7 was requested as the closest experimentally characterised fly relative
of the ProtNLM2 benchmark gene CG4793 (Q8IP30). This review treats Sp7 in its own
right. No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon DROME Sp7 --fallback perplexity-lite` failed: the Edison
(falcon) API returned "Failed to authenticate", and the perplexity-lite fallback timed
out after 600 s. No deep-research file was produced. The review is built from the
UniProt Swiss-Prot record and the cached primary literature listed below.

### Evolutionary placement

- PANTHER 19.0 classification (`.cache/panther/PTHR19.0_fruit_fly`): Sp7 is in
  PTHR24256:SF537 "CLIP DOMAIN-CONTAINING SERINE PROTEASE-RELATED", whose only fly
  members are Sp7, c-SP10 (Q9VA87) and c-SP11 (Q9VA44). Easter (P13582) is in a
  different subfamily, PTHR24256:SF527. CG4793 (Q8IP30) is in PTHR24256:SF462.
  MP1 (A0A126GUP6) is in a different family altogether (PTHR24260:SF135).
- PAINT (`interpro/panther/PTHR24256/PTHR24256-paint.tsv`): node PTN001207268 carries
  IBD assertions for GO:0004252 serine-type endopeptidase activity, GO:0006508
  proteolysis and GO:0005576 extracellular region. Sp7 (FB:FBgn0037515) is itself a
  seed for the extracellular region IBD; easter (FBgn0000533) seeds all three.
  PAINT did not propagate melanization or any immune process from this node, so the
  immune role of Sp7 is a lineage-level/gene-level finding, not a family property.
- The catalytic triad is intact in the Sp7 sequence (checked directly from the UniProt
  sequence): His182, Asp244 and Ser341 (in the GDSGGP motif "SCDGDSGGPLM"). The chain
  is a clip-domain zymogen: signal peptide 1-27, clip domain 30-84, activation
  propeptide 28-136, and catalytic chain from Ile137 (IVYNGN...). This contrasts
  with CG4793, a serine protease homolog whose catalytic Ser is replaced by Gly
  (family review PTHR24256-review.yaml).

Consequence for transfer: Sp7's experimentally established functions (PPO1
cleavage, melanization) belong to a catalytically active clip-domain SP in a
different subfamily from CG4793. Only the family-level IBD properties (secreted,
S1A protease fold) are shared at the PTN001207268 level, and even the catalytic
activity does not transfer to SPHs that lack the triad.

### Experimental findings in D. melanogaster

- Castillejo-Lopez & Hacker 2005 (PMID:16256951, abstract only): Sp7 RNAi impairs
  melanization upon injury; Sp7 is required for PO activation; expressed in blood
  cells (crystal cells); transcription up-regulated by injury and by activated Toll,
  but Toll/IMD mutants do not abolish expression.
  [PMID:16256951 "Silencing of the gene impairs the melanization reaction upon injury."]
- Leclerc et al. 2006 (PMID:16322759, full text): PAE1 (=Sp7) mutants fail to
  activate PO in the haemolymph after microbial challenge, yet survive infections
  as well as wild type. [PMID:16322759 "PAE1 mutants fail to activate phenoloxidase in the haemolymph following microbial challenge"]
- Tang et al. 2006 (PMID:16861233, abstract only): MP1 and MP2 act in a Spn27A-regulated
  melanization cascade; MP2 mainly in fungal infection; genetic data placed MP2
  upstream of MP1.
- Ayres & Schneider 2008 (PMID:19071960, full text): CG3066 mutants alter both
  resistance and tolerance in a microbe-dependent way; reduced survival after
  S. aureus, L. monocytogenes, S. typhimurium; longer survival with S. pneumoniae.
- An et al. 2013 (PMID:24260243, full text): recombinant Factor Xa-activatable
  proMP2 has amidase activity on IEAR-pNA when activated, cleaves recombinant and
  native PPO1, and in vivo overexpression/RNAi increases/decreases PPO1 cleavage;
  Spn27A forms SDS-stable complexes with MP2 and inhibits it. This is the direct
  biochemical evidence for serine-type endopeptidase activity.
- Dudzic et al. 2019 (PMID:31018123, abstract only): with compound mutants, Hayan is
  required for wound blackening, whereas Sp7 controls an alternate melanization that
  clears S. aureus; Sp7 is regulated by the Toll-activating SPs ModSP and Grass.
- Bidla et al. 2007 (PMID:17356067, abstract only): crystal cell rupture and PPO
  release; the abstract does not mention Sp7, the IMP annotation must come from
  the full text (deferred to the FlyBase curator).
- Cao & Jiang 2018 (PMID:30367934, full text) note the conflict over whether MP2 is
  the terminal PAP (in vitro) or acts upstream of MP1 (genetics).

### Decisions summary

- Serine-type endopeptidase activity: ACCEPT (all rows), supported by An 2013
  biochemistry plus intact triad.
- Proteolysis: ACCEPT (true, supported by direct PPO1 cleavage); broad but consistent.
- Extracellular region: ACCEPT (signal peptide, hemolymph protease).
- Melanization defense response: ACCEPT (core process).
- Positive regulation of melanization defense response: ACCEPT. Sp7 activates PPO1 (or
  proMP1) and so positively regulates the melanization effector; FlyBase curators used
  this term from two independent papers.
- Defense response to Gram-positive bacterium: KEEP_AS_NON_CORE. Sp7-dependent
  melanization clears S. aureus, so it acts in the defense, but the term is a broad
  organismal context of the core melanization role.
- No NEW terms. GO:0031638 zymogen activation would describe PPO1 cleavage
  (participation test passes: Sp7 does the cleaving) but the comparator check was
  not run, so it is raised as a question instead.
