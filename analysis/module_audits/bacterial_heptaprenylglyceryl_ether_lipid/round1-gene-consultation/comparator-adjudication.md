# PcrB ether-lipid proposal: comparator adjudication, 2026-11-07

The historical `GO:0008611` NEW row remains active. This is a manual proposal based on direct PcrB chemistry and the actual GO scope, with a documented mapping/convention question; it is not an inference from pathway necessity, annotation coverage, or CarF homology.

## Historical finding and corrected scope

The 2026-11-06 PcrB notes report approximately 5,192 annotations, sampled eukaryotic plasmalogen enzymes including GNPAT/AGPS, zero hits in Archaea and Bacillota, and absence from reviewed archaeal GGGPS. Those are the historical query scopes. The subsequent inference that no prokaryotic ether-lipid enzyme had been reviewed, and that PcrB would be the first prokaryotic use, was unwarranted and is withdrawn. A Bacillota query cannot establish absence across Bacteria. The original notes remain a dated journal; this adjudication supersedes their universal claims.

## Reproducible current queries

Official QuickGO API responses, the complete URL parameters and retrieval date are adjacent in `query-provenance.json`. These are annotation-state comparators, not functional evidence for PcrB; none is cited as `supported_by`.

| Query | Hits |
| --- | ---: |
| GO:0008611, `goUsage=exact` | 5,192 |
| GO:0008611, default descendant-inclusive | 5,432 |
| Bacteria NCBITaxon:2, exact | 17 |
| Bacteria, descendant-inclusive | 17 |
| Archaea NCBITaxon:2157, descendant-inclusive | 0 |
| Bacillota NCBITaxon:1239, descendant-inclusive | 0 |
| Eukaryota NCBITaxon:2759, descendant-inclusive | 5,414 |

Thus the historical numerical total matches today's exact-term total, not the descendant-inclusive total. No inference that all 5,192 rows were individually inspected or all were eukaryotic is justified.

All 17 bacterial rows are exact GO:0008611. Sixteen are electronic UniPathway UPA00781 mappings (`GO_REF:0000041`) on unreviewed proteins described as FAD oxidoreductases/oxidases or putative alkylglycerone-phosphate synthases. The attached UniProt responses retain the submitted labels and their evidence status. Those labels do not independently establish function and none of these proteins is used as biochemical evidence for PcrB.

The remaining bacterial row is IDA on Myxococcus xanthus CarF (Q9AE87), PMID:31604315. Its independently cached primary abstract reports plasmanylethanolamine desaturase activity in bacterial CarF; the reviewed UniProt FUNCTION statement links that activity to the same primary source. This is a plasmalogen vinyl-ether formation step, chemically distinct from G1P-isoprenoid prenyl transfer. It disproves a universal bacterial exclusion, but does not by itself settle how GGGPS should be annotated. The abstract, not inaccessible full assay details, is the scope used here.

## Same-role comparators and propagation

P0C882, O26652 and O29844 are archaeal GGGPS templates of the official HAMAP rule [MF_00112](https://hamap.expasy.org/rule/MF_00112), and occupy the same ether-forming prenyltransferase role as PcrB with a C20 donor. The complete biological-process query returns six rows: all three have GO:0006650 and GO:0046474, none has GO:0008611. The GO:0046474 annotations of P0C882/O26652 point to UniRule UR000076516; O29844 additionally includes InterPro IPR026438 and PANTHER PTN002219408 mapping support.

The archived MF_00112 rule describes ether-bond formation in its FUNCTION text while its GO block offers GO:0046474 and no GO:0008611. This is a concrete mapping mechanism maintaining the gap in a major propagation route. It is not proof that every annotation arises from that rule, that curators never examined GGGPS, or that a deliberate convention cannot exist. HAMAP's cytoplasm statement is conditional on Archaea; its Bacteroidota branch lacks that location, which also cautions against automatically accepting FLAJ1 cytoplasm.

## Definition, participation and redundancy

Current official GO:0008611 defines biosynthesis of ether lipids by a lipid alcohol ether-linked to a glycerol carbon, with the alcohol count and C-1 position qualified as normal cases. Plasmalogen biosynthesis is a **narrow**, not exact, synonym. Its parents include lipid biosynthesis, ether-lipid metabolism and glycerol-ether biosynthesis; it is not a protein-modification process or restricted to bulk membrane lipids. PcrB directly transfers a polyprenyl moiety to glycerol phosphate and forms that ether-linked product (PMIDs 21761520, 24684232), rather than merely supplying or being a substrate of another catalyst. Opposite sn-glycerophosphate stereochemistry does not negate the broad definition's chemically inclusive wording. Product phosphate also makes GO:0046474 true.

The archived `is_a,part_of` ancestor closures were checked in both directions: neither GO:0008611 nor GO:0046474 contains the other. GO:0006650 is refined to GO:0046474; there are no other retained/proposed BP claims in the PcrB review. The two supported BP assertions therefore describe intersecting chemical classes without an ancestor/descendant duplication.

On balance, the direct enzymatic participation, inclusive definition and lack of redundancy justify retaining the historical proposal. The same-role mapping absence remains an explicit ontology question about G1P-isoprenoid ethers; it is not concealed by the CarF precedent or dismissed as curator oversight. No new row is added, and no historical row is removed or retired.
