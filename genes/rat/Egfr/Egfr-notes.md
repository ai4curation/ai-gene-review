# Egfr (rat) curation notes

## Re-review 2026-10-10

GOA refresh: 7 new rows (all genuinely new terms, IEA): GO:0000139 Golgi membrane, GO:0005789 ER membrane, GO:0010008 endosome membrane, GO:0031965 nuclear membrane (all GO_REF:0000044 UniProt SubCell mapping of ARBA locations), GO:0004713 protein tyrosine kinase activity (GO_REF:0000120), GO:0016301 kinase activity and GO:0016740 transferase activity (GO_REF:0000104, UniRule UR000416695). One row retired: GO:0004713 IEA from GO_REF:0000002 (InterPro2GO); the same term returns via GO_REF:0000120.

PENDING resolution: all 7 KEEP_AS_NON_CORE. The four compartments are biosynthetic-transit (Golgi, ER) or trafficking/noncanonical (endosome, nuclear membrane) locations supported by the UniProt SUBCELLULAR LOCATION line, not the plasma-membrane site of signalling. The three MF rows are correct parents of GO:0004714, supported by the UniProt catalytic activity ("L-tyrosyl-[protein] + ATP = O-phospho-L-tyrosyl-[protein] + ADP + H(+)").

Action changes:
- GO:0005515 protein binding (IPI, PMID:30574069): MARK_AS_OVER_ANNOTATED -> REMOVE, per the protein-binding policy. The interactor is mouse HIP1R (Q9JKY5); HIP1R is the endocytic adaptor and EGFR the cargo [PMID:30574069 "We found out that HIP1R interacts with EGFR and induces EGFR endocytosis to participate in dendritic development."]. No more specific EGFR MF follows from the interaction; removal does not dispute it.
- GO:0000166 nucleotide binding, GO:0004672 protein kinase activity, GO:0016020 membrane (IEA), and retired GO:0004713 (IEA): MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE. These are true generic parents of supported terms; nothing in them overshoots the evidence, so they are non-core rather than over-annotations (and the retired row now matches the new GO:0004713 row).
- Added positive `supported_by` to 14 ACCEPT/KEEP_AS_NON_CORE rows that had none (UniProt CC lines, falcon report, PMID:20639532, PMID:30574069). GO:0007611 learning or memory (IDA) now cites [PMID:20639532 "activation or deprivation of EGFR’s kinase activity by infusing EGF or gefitinib (23), respectively, in the brain, affects spatial learning and memory performance in mice."].
- Removed an unverifiable claim ("Supported by rat RGD IDA evidence in UniProt") from the GO:0009986 summary; the refreshed UniProt entry no longer carries GO cross-references.

No stale UniProt quotes (checker: 0). Status set to COMPLETE.

Open questions: the entry is the unreviewed TrEMBL record G3V6K6, so subcellular locations are ARBA-predicted; rat-specific evidence for nuclear/ER EGFR pools is lacking.
