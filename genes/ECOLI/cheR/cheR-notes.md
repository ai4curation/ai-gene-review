# cheR (E. coli K-12, UniProt P07364) review notes

## 2026-11-03 session

Deep research: `just deep-research ECOLI cheR --provider perplexity` failed ("Provider 'perplexity' not
available"). `just mod-description-deep-research ECOLI cheR` skipped (no MOD provider for ECOLI).

Literature search (PubMed eutils esearch): "Springer Koshland 1977 cheR methyltransferase" -> PMID:322131;
"Djordjevic Stock 1997 crystal structure chemotaxis receptor methyltransferase" -> PMID:9115443;
"Simms 1987 purification CheR methyltransferase" -> PMID:3298235; "CheR pentapeptide NWETF binding
methyltransferase Escherichia" -> PMID:10760170; "receptor binding site for the methyltransferase of
bacterial chemotaxis is distinct" -> PMID:8664291. All fetched with `just fetch-pmid` (abstract-only).
PMID:322131, 3298235 and 9115443 are on the Salmonella orthologue (stated in their abstracts).

Nomenclature: cheX is the old name of cheR (UniProt GN line synonym), so the 1977-1980 cheX papers
(PMID:334749, 353036, 365357, 6782079) are about cheR.

### Key evidence
- Activity: [PMID:15916610 "we observed effective assistance in vitro for all three adaptational modifications: methylation, demethylation and deamidation"]
- Tethering to receptor C-terminus: [PMID:8664291 "The principal locus for binding interactions between the aspartate and serine receptors of escherichia coli and the methyltransferase was found to be in the last five amino acids of the receptor."]; [PMID:10760170 "CheR binds to major chemoreceptors through their C-terminal motif NWETF, which is distinct from the methylation sites."]
- Adaptation: [PMID:365357 "The results presented here establish a firm relationship between the methylation reaction and sensory adaptation."]
- Salmonella enzyme: [PMID:3298235 "catalyzes the S-adenosylmethionine-dependent methyl esterification of glutamyl residues in membrane chemoreceptor proteins has been purified to homogeneity"]

### Decisions (18 rows)
- protein binding IPI (Tsr): REMOVE (uninformative; tethering is in core function description).
- cytosol IDA: ACCEPT. plasma membrane IDA x3: MODIFY -> GO:0009898 cytoplasmic side of plasma membrane.
- protein methylation IMP x2: ACCEPT (current GO has no non-obsolete peptidyl-glutamate methylation BP).
- chemotaxis IBA/IMP: ACCEPT.
- protein methyltransferase activity IBA + 2 IMP and SAM-dependent MTase IEA: MODIFY -> GO:0008983.
- GO:0008983 IDA + IEA (EC 2.1.1.80): ACCEPT (core MF; module MF supported).
- intracellular signal transduction IDA: MODIFY -> GO:0023058 adaptation of signaling pathway (CheR
  does not relay the signal; it resets receptor output). Phosphorelay (GO:0000160) not assigned to CheR:
  it does not participate in the histidine-aspartate phosphotransfer.
- MCP complex IBA + IDA: KEEP_AS_NON_CORE (tethered, not a defined core subunit).
