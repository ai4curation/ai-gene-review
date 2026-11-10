# yihQ (P32138) notes

## Session 2026-11-10

Deep research: `just deep-research ECOLI yihQ --provider perplexity` failed (the
deep-research-client dependency could not be resolved offline: "All providers
failed"). No provider file was written; this review is built from the UniProt record
and cached primary literature.

Literature checked (PubMed searches "sulfoquinovosidase", "sulfoglycolysis
Escherichia"): PMID:26878550 (abstract only), PMID:30276262 (full text, fetched this
session), PMID:24463506 (abstract only), PMID:33791429 (full text), PMID:41676062
(review, full text).

### Function

- YihQ is the first dedicated sulfoquinovosidase [PMID:26878550 "We have identified
  Escherichia coli YihQ as the first dedicated sulfoquinovosidase and the gateway
  enzyme to sulfoglycolytic pathways."]
- Retaining GH31 mechanism with D405 nucleophile and D472 acid/base; sulfonate
  recognised by an RWY triad [PMID:30276262 "a stereochemically retaining glycoside
  hydrolase that utilizes a classical Koshland retaining mechanism involving a
  catalytic nucleophilic carboxylate (D405) and acid/base (D472) residue."]
- Hydrolyses SQGro, preferring the natural 2'R diastereomer; SQGro supports growth of
  E. coli [PMID:30276262 "the 2′R stereoisomer, which corresponds to the natural
  stereochemistry of SQDG, hydrolyzed 6-fold faster than the 2′S stereoisomer"].
- No other SQase homologues in E. coli [PMID:30276262 "there are no SQase homologues
  of YihQ within E. coli"].
- The alpha-SQ product needs mutarotation (YihR) before YihS acts on beta-SQ
  [PMID:33791429 "it ensures that the α-SQ product of the sulfoquinovosidase YihQ can be
  efficiently utilized by the SQ-SF isomerase YihS"].
- Minor alpha-glucosidase activity on alpha-glucosyl fluoride (UniProt CC:FUNCTION,
  PubMed:15294295) - not reviewed as a GO row; no GOA row asserts it.

### Annotation decisions

- GO:1990929 (IBA, IDA, IEA) ACCEPT. GO definition is the SQDG reaction; UniProt
  curates RHEA:49452 with ECO:0000269 PubMed:26878550.
- GO:0004553 MODIFY -> GO:1990929.
- GO:0005975 carbohydrate metabolic process: MODIFY -> GO:0019377 glycolipid catabolic
  process (YihQ hydrolyses the sulfolipid SQDG and its delipidated glycoside); no GO term
  for sulfoquinovosyl-glyceride catabolism exists (OLS search). Not GO:1902777: YihQ
  produces SQ and does not break it down.
- GO:0030246 carbohydrate binding (InterPro IPR011013 galactose-mutarotase-like
  superfamily domain): MARK_AS_OVER_ANNOTATED - substrate binding inside the
  catalytic activity, no separate carbohydrate-binding module function shown.
- PAINT node PTN002333608 belongs to PTHR46959 (owned by another worker); not
  re-adjudicated here.
