# HCFC1 Reactome compartment checks

Official Reactome ContentService assertions retrieved 2026-11-15T03:29:02.774894+00:00. The selected facts below are extracted from JSON, not quoted publication prose. The companion reactome-checks.json retains response URL/hash pins and the selected participant paths, without full API payloads.

- This verifies Reactome assertions, not an independent localization experiment.
- Event and complex localization do not assign histone acetyltransferase, methyltransferase, or deubiquitinase catalysis to HCFC1.
- Cached event markdown omits compartment fields and must not be described as the source of those fields.
- Selected relationship statements are derived factual extracts from JSON, not literal publication quotations.
- No whole-complex traversal, new GO annotation, full payload retention, or curated file edit performed.

## R-HSA-1592250

Reactome R-HSA-1592250: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-1592250)

- R-HSA-1592250 -- input --> R-HSA-1592209: HCFC1 [nucleoplasm]
- R-HSA-1592250 -- output --> R-HSA-2466381: TFB1M gene:NRF1:NRF2:HCFC1:PPRC1 [nucleoplasm]

## R-HSA-2466367

Reactome R-HSA-2466367: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-2466367)

- R-HSA-2466367 -- input --> R-HSA-1592209: HCFC1 [nucleoplasm]
- R-HSA-2466367 -- output --> R-HSA-2466365: TFB2M gene:NRF1:NRF2:HCFC1:PPRC1 [nucleoplasm]

## R-HSA-3321805

Reactome R-HSA-3321805: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-3321805)

- R-HSA-3321805 -- catalystActivity --> 3321793: histone acetyltransferase activity of NSL (PHF20) [nucleoplasm]
- 3321793 -- physicalEntity --> R-HSA-3321855: NSL (PHF20) [nucleoplasm]

Event compartment and named nucleoplasmic NSL catalyst are directly verified. The hasComponent path from this exact NSL(PHF20) entity to HCFC1 was not traversed. HCFC1 NSL membership is independently supported by PMID20018852 and the explicit HCFC1 input in row80. This is a retained location assertion, not a claim that HCFC1 performs acetyltransferase catalysis.

## R-HSA-5689630

Reactome R-HSA-5689630: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-5689630)

- R-HSA-5689630 -- input --> R-HSA-5689653: BAP1-interacting complex [nucleoplasm]
- R-HSA-5689653 -- hasComponent --> R-HSA-5689678: BAP1-interacting core complex [nucleoplasm]
- R-HSA-5689678 -- hasComponent --> R-HSA-1592209: HCFC1 [nucleoplasm]

## R-HSA-5690759

Reactome R-HSA-5690759: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-5690759)

- R-HSA-5690759 -- input --> R-HSA-5690760: BAP1:K48polyUb,K63polyUb-HCFC1 [nucleoplasm]
- R-HSA-5690759 -- output --> R-HSA-5690817: BAP1:HCFC1 [nucleoplasm]
- R-HSA-5690817 -- hasComponent --> R-HSA-1592209: HCFC1 [nucleoplasm]

## R-HSA-5690785

Reactome R-HSA-5690785: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-5690785)

- R-HSA-5690785 -- input --> R-HSA-5690821: K48polyUb,K63polyUb-HCFC1 [nucleoplasm]
- R-HSA-5690785 -- output --> R-HSA-5690760: BAP1:K48polyUb,K63polyUb-HCFC1 [nucleoplasm]

## R-HSA-5690790

Reactome R-HSA-5690790: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-5690790)

- R-HSA-5690790 -- catalystActivity --> 5690792: cysteine-type deubiquitinase activity of PR-DUB complex [nucleoplasm]
- 5690792 -- physicalEntity --> R-HSA-5690807: PR-DUB complex [nucleoplasm]
- R-HSA-5690807 -- hasComponent --> R-HSA-1592209: HCFC1 [nucleoplasm]

## R-HSA-9821235

Reactome R-HSA-9821235: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-9821235)

- R-HSA-9821235 -- input --> R-HSA-9821240: HCFC1,HCFC2 [nucleoplasm]
- R-HSA-9821240 -- hasMember --> R-HSA-1592209: HCFC1 [nucleoplasm]

## R-HSA-9821486

Reactome R-HSA-9821486: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-9821486)

- R-HSA-9821486 -- input --> R-HSA-1592209: HCFC1 [nucleoplasm]
- R-HSA-9821486 -- output --> R-HSA-9821487: SET1A complex:WDR82:CXXC1:HCFC1 [nucleoplasm]

## R-HSA-9828175

Reactome R-HSA-9828175: event compartment GO:0005654 nucleoplasm.

[Official event](https://reactome.org/ContentService/data/query/R-HSA-9828175)

- R-HSA-9828175 -- input --> R-HSA-1592209: HCFC1 [nucleoplasm]
- R-HSA-9828175 -- output --> R-HSA-9828237: NSL [nucleoplasm]
