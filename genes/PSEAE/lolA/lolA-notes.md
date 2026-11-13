# lolA (PA2614, Q9I0M4) notes

Periplasmic lipoprotein carrier of the Lol pathway. No deep-research provider was available;
literature checked by hand (PMID:17350955 abstract only; PMID:26621210 full text, fetched with
`ai-gene-review fetch-pmid`; QuickGO for E. coli LolA P61316). Consistent with the PA2988 and
PA2986 (LolCDE permease) reviews of the same paper.

## Literature

- Tanaka, Narita & Tokuda 2007 (PMID:17350955, abstract): reconstituted P. aeruginosa LolCDE
  released lipoproteins to the P. aeruginosa LolA homologue ["When incubated in the presence of
  ATP and a LolA homologue, the reconstituted LolCDE homologue released lipoproteins, leading to
  the formation of a LolA-lipoprotein complex."], and LolB then inserted them in the outer
  membrane; E. coli LolCDE also transfers lipoproteins to P. aeruginosa LolA.
- Fernández-Piñar et al. 2015 (PMID:26621210, full text): lolA essential; LolA-depleted cells
  are SDS-sensitive and partly attenuated in Galleria and mouse infection ["In the whole, this
  experiment demonstrates that LptH and, to a lesser extent, LolA are the only proteins here
  investigated with a relevant role in cell envelope stability."]. Necessity evidence only.
- E. coli LolA P61316: IDA GO:0044874 (CACAO, PMID:7628437), IDA GO:0030288. The E. coli lolA
  review uses GO:0140598 lipoprotein carrier activity as the core MF.

## Review decisions

- GO:0044874 (IDA, IBA, IEA), GO:0042953 (IBA, IEA), GO:0030288 IBA: ACCEPT.
- GO:0042597 periplasmic space IEA: TOO_GENERAL (entailed by accepted GO:0030288).
- NEW GO:0140598 lipoprotein carrier activity, IDA PMID:17350955.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002185387 | GO:0044874 lipoprotein localization to outer membrane | 2 | 9 (9 taxa) | GO:0044874, IDA, PMID:17350955 (PseudoCAP; also CACAO) | SOUND | Abstract states the purified P. aeruginosa LolA accepts lipoproteins from LolCDE and LolB inserts them in the outer membrane: direct biochemical evidence. Node term suits a LolA clade. | E. coli LolA P61316 (CACAO IDA GO:0044874, PMID:7628437) | Yes, on E. coli LolA |

No PSEUDOCAP or GO_CENTRAL defect.
