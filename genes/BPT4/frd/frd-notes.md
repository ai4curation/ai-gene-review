# frd manual review notes

## 2026-05-21 deeper SPKW-BPT4 review

Reviewed the AIGR review skill, `frd-ai-review.yaml`, `frd-goa.tsv`, `frd-uniprot.txt`, `frd-deep-research-falcon.md`, and cached publications `PMID_4936128.md`, `PMID_10818362.md`, `PMID_6327673.md`, and `PMID_1560001.md`. Attempted to fetch additional T4 baseplate-contestation papers (`PMID:7884858`, `PMID:894793`, `PMID:1202242`, `PMID:1238580`), but NCBI returned HTTP 429. I used web/PubMed/PMC snippets only to decide whether the YAML should present the baseplate claim as settled.

Core molecular function remains DHFR activity: [PMID:4936128 T4 bacteriophage-specific dihydrofolate reductase: purification to homogeneity by affinity chromatography., "T4 bacteriophage-specific dihydrofolate reductase"] and [PMID:10818362 Overexpression, crystallization and preliminary X-ray crystallographic analysis of dihydrofolate reductase from bacteriophage T4., "Dihydrofolate reductase (DHFR) from bacteriophage T4 is a homodimer"].

The original description overstated the virion/baseplate structural role. Older work argued for a baseplate component [PMID:894793 Bacteriophage T4 virion baseplate thymidylate synthetase and dihydrofolate reductase, "Additional evidence is presented that both the phage T4D-induced thymidylate synthetase (gp td) and the T4D-induced dihydrofolate reductase (gp frd) are baseplate structural components."]. However, the later immunoblot paper directly disputes this: [PMID:7884858 An immunoblot assay reveals that bacteriophage T4 thymidylate synthase and dihydrofolate reductase are not virion proteins, "both enzymes are present only as minor contaminants (<0.05 copy per phage) and as such cannot be bona fide structural proteins"].

YAML decision: do not add a `virus tail, baseplate` or `virion component` annotation for frd in this pass. Chen et al. 1995 concluded that T4 thymidylate synthase and DHFR are present only as minor contaminants, less than 0.05 copy per phage, and cannot be bona fide structural proteins. The safe curation call is DHFR/THF metabolism core; baseplate localization remains a contested historical claim.

The drug-response removals remain appropriate. T4 DHFR can be inhibited by antifolates, but being a drug target is not a phage biological response to antibiotic or methotrexate.
