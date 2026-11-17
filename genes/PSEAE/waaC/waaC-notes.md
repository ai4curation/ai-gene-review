# waaC (PA5011, Q9HUF5, heptosyltransferase I) review notes

No deep-research provider was available. Sources: UniProt record (Swiss-Prot), cached PMID:9171387
(abstract only; PMC179135 has no full-text XML: PubMed MCP returned an empty body and NCBI efetch
reports the publisher does not allow XML download). PubMed MCP searches ("Pseudomonas aeruginosa waaC
heptosyltransferase mutant", 2026-11-05) returned no hits (search service failing).

## Function

- Cloned by complementing a Salmonella waaC mutant with a PAO1 library
  [PMID:9171387 "Two plasmids, pCOREc1 and pCOREc2, which restored smooth LPS production in the waaC mutant, were isolated."].
- 53% identity to Salmonella WaaC; 40-kDa product seen by maxicell expression; chromosomal knockouts
  could not be isolated (only merodiploids), suggesting the gene is needed for viability in PAO1
  [PMID:9171387 "Despite multiple attempts to isolate true knockout mutants, all transconjugants were identified as merodiploids."].
- UniProt (by similarity to E. coli WaaC P24173): adds the first heptose to Kdo2-lipid A, EC 2.4.99.23;
  peripheral inner-membrane protein, cytoplasmic side. Family: GT9; NCBIfam TIGR02193 heptsyl_trn_I;
  InterPro IPR011908 LipoPS_heptosylTferase-I.
- GO has no term for the heptosyltransferase I reaction (Kdo2-lipid A acceptor). Its children of
  GO:0008920 are GO:0008713 (heptosyl-Kdo2-lipid A acceptor = heptosyltransferase II, WaaF),
  GO:0071967 (heptosyltransferase III) and GO:0071968 (lipid A-core heptosyltransferase). The most
  specific correct term for WaaC is the parent GO:0008920.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001575314 | GO:0009244 LPS core region biosynthetic process | 7 | 64 (24 taxa) | GO:0009244, IDA, PMID:9171387 (PseudoCAP) | SOUND | Heterologous complementation of the Salmonella waaC mutant restores smooth LPS; the term is right for a core heptosyltransferase. The evidence is genetic (complementation), not a direct assay, so IDA is probably the wrong code (SUSPECTED PSEUDOCAP WRONG_EVIDENCE_CODE, abstract only). | E. coli WaaC P24173, WaaF P37692, WaaQ P25742; Salmonella WaaC P26469, WaaF P37421 (all IMP GO:0009244); PAO1 WaaF G3XD35 | Yes; five enterobacterial seeds carry IMP evidence. No GO_CENTRAL defect for GO:0009244. |

Other PseudoCAP row: ISS GO:0071968 lipid A-core heptosyltransferase activity, with Salmonella WaaC
P26469. GO:0071968 is the reaction that completes lipid A-core, not the first heptose transfer: WRONG_TERM,
CONFIRMED (definitions and the with/from protein's reviewed reaction checked). Same error on waaF.

Node-level GO_CENTRAL defect (recorded here, cross-referenced from waaF): PTN001575314 also carries an
IBD of GO:0008713 (the heptosyltransferase II reaction) seeded only by E. coli WaaF P37692. The node
spans WaaC (Hep I), WaaF (Hep II) and WaaQ (Hep III) orthologs, as its own GO:0009244 seed list shows,
so WaaC proteins, including E. coli WaaC P24173 (experimentally GO:0008920), receive the Hep II reaction.
The IBD should move to the WaaF subclade, or be generalised to GO:0008920 at this node. CONFIRMED.

Defects recorded: PSEUDOCAP 2 (WRONG_EVIDENCE_CODE SUSPECTED; WRONG_TERM CONFIRMED); GO_CENTRAL 1
(WRONG_TERM at PTN001575314 for GO:0008713, CONFIRMED).
