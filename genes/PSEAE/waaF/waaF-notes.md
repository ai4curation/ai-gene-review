# waaF (PA5012, G3XD35, heptosyltransferase II) review notes

No deep-research provider was available. Sources: UniProt record (TrEMBL; its reaction and family notes
are ARBA-only, so they are not used as evidence), cached PMID:9171387 (abstract only; no full-text XML
obtainable for PMC179135). PubMed MCP searches on 2026-11-05 returned no hits (search service failing).

## Function

- Cloned by complementing a Salmonella waaF mutant with a PAO1 library
  [PMID:9171387 "Similarly, plasmid pCOREf1 was able to complement the Salmonella waaF mutant."].
- 49% identity to Salmonella WaaF; 38-kDa product by maxicell expression
  [PMID:9171387 "The sequence of the predicted protein was 49% identical to the sequence of the Salmonella WaaF protein."].
- Chromosomal knockouts could not be obtained (merodiploids only).
- Family: GT9; NCBIfam TIGR02195 heptsyl_trn_II; InterPro IPR011910 (RfaF). GO:0008713 is defined as
  the heptosyltransferase II reaction (heptosyl-Kdo2-lipid A acceptor), which fits WaaF.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001575314 | GO:0009244 LPS core region biosynthetic process | 7 | 64 (24 taxa) | GO:0009244, IDA, PMID:9171387 (PseudoCAP) | SOUND | Heterologous complementation of the Salmonella waaF mutant; term right for a core heptosyltransferase. Genetic evidence, so IDA is probably the wrong code (SUSPECTED PSEUDOCAP WRONG_EVIDENCE_CODE, abstract only), as for waaC. | E. coli WaaC P24173, WaaF P37692, WaaQ P25742; Salmonella WaaC P26469, WaaF P37421 (all IMP); PAO1 WaaC Q9HUF5 | Yes; five enterobacterial IMP seeds. No GO_CENTRAL defect for GO:0009244. |

Shared node with waaC (same paper, same verdict). The node-level GO_CENTRAL defect for the GO:0008713
IBD at PTN001575314 (Hep II term over a Hep I/II/III clade) is recorded once, on waaC; for WaaF itself
the GO:0008713 IBA is correct and is accepted here.

Other PseudoCAP row: ISS GO:0071968 lipid A-core heptosyltransferase activity with Salmonella WaaF
P37421: WRONG_TERM, CONFIRMED; the correct term is GO:0008713 (same error as on waaC).

Defects recorded: PSEUDOCAP 2 (WRONG_EVIDENCE_CODE SUSPECTED; WRONG_TERM CONFIRMED); GO_CENTRAL 0 here
(1 node-level defect on waaC).
