# PA3761 (Q9HXN4) review notes

NagE-family PTS enzyme IIBC (TCDB 4.A.1.1.15; NCBIfam TIGR01998 PTS-II-BC-nag;
PANTHER PTHR30009:SF4). EIIC (3..371, 8 TM helices), EIIB (383..466, active-site
Cys405, checked in the sequence), second EIIB-like domain (491..570) that UniProt
cautions lacks conserved residues. No EIIA domain; PA3760 is the fused
EI/HPr/EIIA partner.

## Literature (no deep-research provider; own reading, 2026-11-05)

- Johnson et al. 2008 (full text, PMC2542419): Biolog screen of 78 transporter
  mutants. [PMID:18833300 "Knockouts in either PA3760 or PA3761 were defective
  in growth on N-acetylglucosamine as a sole carbon source, based on both Biolog
  and growth data (Table 2)."] and [PMID:18833300 "As for the fructose PTS
  genes, expression of the N-acetylglucosamine PTS genes was induced by their
  apparent transported substrate (Table 3)."] The genes sit at the end of a
  glucosamine utilisation operon. The mutant is listed under strain PAK.
- E. coli NagE (P09323), the other node seed: GO:0015764 IDA PMID:4919472,
  GO:0090586 IDA/EXP PMID:3056518, GO:0009401 IDA (EcoCyc; QuickGO 2026-11-05).
- PubMed MCP returned API errors on 2026-11-05.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000768523 | GO:0015764 N-acetylglucosamine transport | 2 | 14 (11 taxa) | GO:0015764, IMP, PMID:18833300 (PseudoCAP) | SOUND | Full text read: GlcNAc-specific growth defect plus GlcNAc induction, in a NagE-family EIIBC. A growth phenotype alone could be catabolic, but the family placement makes transport the right reading. | E. coli NagE P09323 (IDA PMID:4919472) | Yes; NagE IDA seed, and the node is a NagE subfamily clade |

No PSEUDOCAP or GO_CENTRAL defect.

## Other decisions

- GO:0090563 (IBA, PTN002011274) and GO:0008982 (IEA) MODIFY to the GlcNAc
  phosphocysteine PTS term GO:0090586, the term E. coli NagE carries by IDA.
- GO:0019866 organelle inner membrane (InterPro2GO) is an organelle term
  applied to a bacterium; MODIFY to plasma membrane.
