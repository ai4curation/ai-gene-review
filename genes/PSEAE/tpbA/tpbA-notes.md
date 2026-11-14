# tpbA (PA3885) review notes

## Literature search (2026-11-05)

No deep-research provider was available. PubMed MCP and Europe PMC search
endpoints failed during this session. Sources read: PMID:19543378 (full text,
Ueda and Wood 2009), PMID:25909591 (full text, Xu et al. 2015), and
PMID:21045298 (crystallisation note, abstract only, not used for claims).

## Findings

- Purified TpbA-cHis hydrolyses pNPP and two phosphotyrosine peptides; activity is
  inhibited by orthovanadate [PMID:19543378 "TpbA-cHis dephosphorylated both
  phosphotyrosine peptides"].
- Periplasmic by fractionation [PMID:19543378 "we found that TpbA exclusively
  localized in the periplasm"].
- Model: TpbA dephosphorylates TpbB (YfiN) and lowers c-di-GMP [PMID:19543378
  "Periplasmic TpbA dephosphorylates the membrane-anchored GGDEF protein TpbB at a
  tyrosine reside which deactivates GGDEF protein activity"].
- PAO1 TpbA structures and preference for TpbB pTyr48 [PMID:25909591 "TpbA
  efficiently catalyzes the hydrolysis of two phosphotyrosine peptides derived
  from the periplasmic domain of TpbB"]; dual specificity [PMID:25909591 "can
  dephosphorylate pTyr, pSer and pThr residues"].
- Strain: PMID:19543378 used PA14 (PA14_13660, UniProt A0A0H2ZFK2). Pairwise
  comparison of the UniProt sequences (2026-11-05): both 218 aa, 4 differences
  (98.2% identity). PseudoCAP's IDA on the PAO1 gene is a routine strain transfer
  and is not filed as a defect.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN001258896 | GO:0016791 phosphatase activity | 9 | 297 (77 taxa) | GO:0004725 protein tyrosine phosphatase activity, IDA, PMID:19543378 (PseudoCAP; also UniProt EXP PMID:25909591) | yeast SIW14 S000005043; Arabidopsis AT1G05000, AT2G32960, AT3G02800, AT5G16480; Q6K461 (rice DSP1); Q4QBX1 (Leishmania); I6WXK4 (M. tuberculosis PtpB) | Yes (eight other seeds, including SIW14 and the plant PFA-DSPs) | SOUND | Purified-enzyme assay with phosphotyrosine peptides, reproduced with PAO1 protein. Seed is more specific than the node term; generic phosphatase activity is the right level for an atypical DUSP clade whose members act on proteins or inositol pyrophosphates. |

No GO_CENTRAL defect.
