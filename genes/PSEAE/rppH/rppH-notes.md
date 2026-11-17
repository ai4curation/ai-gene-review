# rppH (PA0336, Q9X4P2) notes

PubMed search tools (MCP and E-utilities) returned API errors on 2026-11-05, so
no newer PA0336 literature could be searched; the review rests on the cached
PseudoCAP paper, UniProt/HAMAP and live QuickGO queries for the co-seed.

## Literature

- PA0336 is a Nudix RppH homologue that substitutes for E. coli RppH
  [PMID:28833678 "Trans-complementation experiments showed that the P. aeruginosa enzyme can functionally substitute for RppH in E. coli cells"].
- Mutant overproduces pyocyanin, rescued by wild type but not catalytically
  inactive PA0336 [PMID:28833678 "This phenotype was reversed by complementation with the wild type but not catalytically inactive PA0336"].
- RNA-seq: 537 transcripts changed [PMID:28833678 "The level of 537 transcripts coding for proteins involved in a variety of cellular processes"].
- Abstract only (Mol Microbiol 2017, not in PMC).

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001500664 | GO:0034353 mRNA 5'-(triphosphate) diphosphatase activity | 2 | 11 (11 taxa) | GO:0034353, IMP, PMID:28833678 (PseudoCAP) | SOUND | Heterologous complementation of E. coli RppH plus a catalytic-mutant control; abstract only. Node term suits the bacterial RppH clade. | E. coli RppH P0A776 (IDA PMID:18202662, EcoCyc) | Yes |

No PSEUDOCAP defect. No GO_CENTRAL defect on the seeded node.

## Other IBA problem (not a seeded node)

GO:0000290 deadenylation-dependent decapping of nuclear-transcribed mRNA
arrives from PTN000561806, whose seeds are all eukaryotic Dcp2-type enzymes.
Removed as a taxon mismatch; a PROBABLE GO_CENTRAL defect asks for the IBD to
be moved or negated on the bacterial RppH subclade. Added NEW GO:0006402 mRNA
catabolic process (IMP, PMID:28833678) as the bacterial counterpart.

Note: GOA labels GO:0034353 "mRNA 5'-triphosphate diphosphatase activity";
the local ontology still has "mRNA 5'-diphosphatase activity" (label-change
warning only).
