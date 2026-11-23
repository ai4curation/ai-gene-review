# dsbB1 (PA5256, P21482) review notes

DsbB family (Pfam PF02600; IPR003752; PANTHER PTHR36570), four TM helices,
two periplasmic disulfides (UniProt FT DISULFID). Reviewed together with its
paralog dsbB2 (genes/PSEAE/dsbB2); both reviews make the same calls.

## Naming caution

Arts et al. 2013 worked in PA14: [PMID:24327342 "PaDsbB1 [PA14_07000] and
PaDsbB2 [PA14_69400]"]. UniProt PA14 entries Q02TM7 (PA14_07000) and Q02EA7
(PA14_69400) are identical in sequence to PAO1 P57701 (PA0538, UniProt
"dsbB2") and P21482 (PA5256, UniProt "dsbB1") respectively (full sequences
compared, 2026-11-05). So this gene (PA5256) is the paper's PaDsbB2 (PA14_69400). Both paralogs
carry identical PseudoCAP rows, so the swap causes no annotation error; it is
raised as a suggested question.

## Literature (no deep-research provider; own reading, 2026-11-05)

- Arts et al. 2013 (full text, PMC3870256): either DsbB keeps DsbA1 oxidised
  [PMID:24327342 "These results indicate that both PaDsbB1 and PaDsbB2 control
  the redox state of PaDsbA1 and that both proteins are able to compensate for
  each other."]; in vitro reconstitution with decylubiquinone [PMID:24327342
  "We calculated a Km of 8.1 µM PaDsbA1 for PaDsbB1 and 9.0 µM for
  PaDsbB2."]; the double mutant loses pilus, flagellum and exoprotein folding
  and virulence, complemented by either gene [PMID:24327342 "the double
  PadsbB1B2 mutant being complemented by expression of either individual
  PadsbB1 or PadsbB2 gene"].
- E. coli DsbB (P0A6M2), the node's GO:0015035 seed: GO:0015035 IMP
  PMID:8430071, GO:0016672 IDA PMID:10428033 (EcoCyc; QuickGO 2026-11-05).
- Comparator for protein folding: E. coli DsbC (P0AEG6) carries GO:0006457 by
  IDA, so periplasmic disulfide oxidoreductases do carry this process term.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002195183 | GO:0006457 protein folding | 2 | 11 (8 taxa) | GO:0006457, IMP, PMID:24327342 (PseudoCAP) | SOUND | Full text read: double mutant fails to fold disulfide-containing envelope proteins, complemented by either gene; DsbB does a step of oxidative folding (DsbA reoxidation, shown in vitro). | the paralog (dsbB2 (genes/PSEAE/dsbB2)), same paper and same sound evidence | Yes. The other seed is equally sound; the node is a DsbB clade and the term suits it |

No PSEUDOCAP or GO_CENTRAL defect. The node's GO:0015035 IBD rests on
E. coli DsbB and is also sound.

## Other decisions

- NEW GO:0016672 (sulfur donor, quinone acceptor) IDA PMID:24327342, the
  precise DsbB reaction, as for E. coli DsbB; used as the core MF.
- GO:0009055 electron transfer activity MODIFY to GO:0016672.
- GO:0016020 membrane TOO_GENERAL (plasma membrane accepted).
