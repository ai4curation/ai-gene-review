# FDXR database evidence

The [decision table](FDXR-database-decisions.yaml) preserves all 19 owned source contexts and complete review objects. Eighteen are retained; generic oxidoreductase activity is TOO_GENERAL relative to the retained, typed descendant ferredoxin-NADP+ reductase activity. The broad mitochondrial organelle remains informative even with more specific location annotations.

## Catalytic and pathway provenance

Actual target UniProt, ARBA00095261, InterPro target hits and seven Reactome event/entity routes support the redox role. Reactome identifies FDXR entity 2395499, reference 49738/P22570, modeled residues 33–491 in mitochondrial matrix. Events 2395512 and 2395517 explicitly assign GO:0004324 through catalyst 9954152. FDXR supplies electrons; CYP11A1 performs cholesterol hydroxylation and cleavage. A disease-event title does not remove FDXR from its actual nested complex. Model coordinates are not new processing measurements for every splice product.

The ARBA condition set was read, but exact historical FunFam matching was not replayed. UniPathway UPA00296 is archived; actual target and reaction context still support cholesterol metabolism, without asserting de novo cholesterol synthesis. The Rhea standalone endpoint was inaccessible; the same exact reaction is available in official GO and UniProt.

## Location and source organisms

HPA supports a mitochondrial pool with CAB008597 and two enhanced HPA antibodies. Actual selected U2OS/Hep-G2 image pixels were read. Antigen mappings are canonical residues 1–134 and 372–464. These images do not resolve inner membrane versus matrix, establish exclusive localization, or distinguish all products.

The inner-membrane ISS and UniProt mapping trace to yeast ARH1/P48360. The original [PMID:9727014](../../../publications/PMID_9727014.md) submitochondrial Results and Figure 7 caption identify positive inner-membrane co-fractionation with compartment controls. The authentic cache remains abstract-only; separate original author-uploaded text was read. Bovine localization also points to this yeast donor and is not independent mammalian evidence. Human submitochondrial localization remains an inference, separate from human mitochondrial observations.

## Phylogenetic boundaries

[Phylogeny evidence](FDXR-phylogeny-evidence.yaml) records the actual imported nodes and family-version boundary. Current PTHR48467 membership is genuine despite its surprising official name. The live release-19 record instead gives PTHR11938:SF91. No target ancestry or IBD was verified: global PAINT exceeded the download guard and bounded historical tree/MSA requests timed out. Independent biological support justifies retention without describing these access limits as loss, or treating donor count or self-WITH as defects. The fly dare source paper was abstract/preview-only.

## Product-specific evidence

[PMID:41511346](../../../publications/PMID_41511346.md), Methods 2.4, Results 3.1 and Figure 1H compare tagged human products in MCF7 cells. Paper isoforms 1/4 overlap mitochondria; paper isoform 7 is predominantly cytosolic. [Exact source joins](FDXR-isoform-source-joins.yaml) distinguish the paper's numbering from UniProt: paper 4 corresponds to P22570-7, paper 7 to P22570-4. Figure S1 pixels and actual sequence alterations support these joins. They do not establish a cytosolic molecular substrate or endogenous cleavage site. Results and caption disagree about the cell line in Figure 1F; the localization panel Figure 1H and its Methods consistently use MCF7.

The seven seeded products are unchanged. The 1988 primary is cloning/expression and prior enzyme-context evidence, while the 2024 COQ6 reconstitution uses reconstructed tetrapod-ancestral proteins; these are not relabeled as extant-human activity comparisons. Complete assessments of the five original experimental-paper groups belong to the direct review lane.

## Shared provenance retained after reason shortening

The literal PAINT IBD, target ancestry and alignment remain unavailable. The declared global download was 401,856,535 bytes and was rejected before its body under the 100 MiB cap; bounded release-19 tree/MSA requests timed out. Historical PTHR11938:SF91 and current PTHR48467 remain distinct. Those limits are not evidence of loss or circularity.

For inner-membrane inference, the yeast original PMID:9727014 checks antiserum against recombinant protein/control extracts and uses ATP/ADP carrier and porin as fraction controls. Bovine P08165 points to the same P48360 donor and does not add independent mammalian evidence. For the matrix routes, a matrix-facing peripheral inner-membrane pool is compatible with the curated donor inference; that compatibility does not constitute a human topology measurement. Reactome's 33–491 entity is not a measured processing site for all seven products. Each shortened reason retains its own event route and role.

The unchanged [UniProt record](FDXR-uniprot.txt), ALTERNATIVE PRODUCTS and MISCELLANEOUS, identifies **Long = P22570-2**, VSP_003416, and reports 10–20% of adrenodoxin reductase mRNAs with tentative inactivity (ECO:0000305). VAR_SEQ 203 replaces E with EALLLCQ, attributed to the 1988 sequence paper. This is a curated inference, not a purified comparison of all isoforms; the 1988 Discussion leaves the splice difference's function unresolved. It is distinct from the 2025 paper's reversed numbering of isoforms 4/7.

FAD is already explicit in the biological description and the reductase chemistry. The cofactor binds within the enzyme's electron-transfer mechanism; this follow-up does not manufacture an additional binding annotation or a separate binding core. The specific reductase activity remains the functional summary.
