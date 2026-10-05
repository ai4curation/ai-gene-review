# wdr-23 (S6FN32): evidence and exact-input prediction review

The DCAF11/WDR-23 identity and qualified substrate-receptor prediction are supported by direct worm studies and preservation of the common WD-repeat region. The nucleus prediction requires isoform-specific evidence; the two ribosome-related GO predictions derive from RACK1 rather than WDR-23 evidence.

## Input identity and functional boundary

S6FN32/D2030.9d is exactly residues 74–571 of the longer P90794 WDR-23A sequence and residues 33–530 of P90794-2/WDR-23B. It therefore is not identical to either tested isoform. Every annotated WD repeat is retained. The missing isoform-specific N termini matter because primary experiments establish different nuclear and cytoplasmic behavior. The GO donor P69103 is trypanosome small ribosomal subunit protein RACK1, a different WD-repeat protein.

## Biological evidence

- [PMID:19273594 — The WD40 repeat protein WDR-23 functions with the CUL4/DDB1 ubiquitin ligase to regulate nuclear abundance and activity of SKN-1 in Caenorhabditis elegans.](https://pubmed.ncbi.nlm.nih.gov/19273594/): The primary worm study establishes association of WDR-23 with CUL-4/DDB-1 and regulation of SKN-1 abundance and activity.

> WDR-23, which interacts with the 
> CUL-4/DDB-1 ubiquitin ligase

- [PMID:31409866 — Nuclear and cytoplasmic WDR-23 isoforms mediate differential effects on GEN-1 and SKN-1 substrates.](https://pubmed.ncbi.nlm.nih.gov/31409866/): Primary worm isoform experiments show that compartment and regulatory outcome cannot be assigned independently of the N terminus.

> These opposing roles are mediated by two distinct isoforms: WDR-23A
> in the cytoplasm and WDR-23B in the nucleus.


> we identify
> GEN-1, a Holliday junction resolvase, as an evolutionarily conserved WDR-23
> substrate


> the N-terminal domain of WDR-23B that mediates nuclear localization does not interfere with binding of GEN-1 in vitro.

## Exact non-GO claims

The complete emitted record is preserved in [wdr-23-protnlm-source.json](wdr-23-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> DDB1- and CUL4-associated factor 11

CNN (CS 2). DDB1- and CUL4-associated factor 11 correctly identifies the WDR-23 lineage, independently supported by direct C. elegans interaction and substrate-regulation experiments. It does not specify the untested isoform localization.

### Function

> May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex

CNN (CS 2). The qualified “may function as a substrate receptor” wording is consistent with preservation of the complete common WD-repeat region and direct worm evidence for WDR-23–CUL-4/DDB-1 association. The prediction does not establish that the short product has all regulatory effects measured for WDR-23A or WDR-23B. [PMID:19273594](https://pubmed.ncbi.nlm.nih.gov/19273594/); [PMID:31409866](https://pubmed.ncbi.nlm.nih.gov/31409866/).

### Location

> Nucleus

UNC (CS 1). Both nuclear and cytoplasmic WDR-23 isoforms are experimentally documented. S6FN32 starts downstream of the distinctive N termini of both tested products, so it cannot simply inherit the WDR-23B localization. The missing N terminus does not by itself prove exclusion from the nucleus. [Isoform comparison](wdr-23-bioinformatics/isoform-b-comparison.json); [primary localization study](https://pubmed.ncbi.nlm.nih.gov/31409866/).

## Emitted GO claims

All 2 emitted GO claims are individually assessed in [wdr-23-protnlm-predictions-review.yaml](wdr-23-protnlm-predictions-review.yaml).

## Family integration

PTHR19847/SF7 identifies the DCAF11/WDR23 substrate-receptor lineage. A WD-repeat fold alone is insufficient to transfer the ribosome-associated functions of RACK1. Substrate identity and compartmental effects require finer resolution than family membership; nuclear inhibition and cytoplasmic activation of substrates are both compatible with a common adaptor architecture.

## Evidence limits

The 2019 report is available in full text; the 2009 cache is abstract-only. Neither directly assays D2030.9d/S6FN32. The genuine Falcon report provides useful primary leads, but its gene-level nuclear and SKN-1 conclusions require the exact isoform boundary documented here. No NEW experimental annotation is assigned to an untested protein product. No direct assay was found either establishing or refuting ribosome association.

Exact sequence mapping: [wdr-23-bioinformatics/RESULTS.md](wdr-23-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.
