# Oaz1 (rat) notes

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d): 3 new rows, all donor-split duplicates of existing reviewed rows; no rows retired.

- GO:0008073 ornithine decarboxylase inhibitor activity, ISO from human OAZ1 (UniProtKB:P54368): ACCEPT, consistent with the mouse-donor ISO sibling.
- GO:0045732 positive regulation of protein catabolic process, ISO from human OAZ1 (P54368): ACCEPT.
- GO:0045732, ISS from mouse Oaz1 (UniProtKB:P54369): ACCEPT.

Action changes: none. All existing actions were re-audited and kept; reasons were rewritten from a generic template to row-specific justifications:

- GO:0072750 cellular response to leptomycin B (IDA): MARK_AS_OVER_ANNOTATED retained; leptomycin B was a CRM1-inhibitor tool to reveal export [PMID:12941943 "treatment with leptomycin B, a specific inhibitor of chromosomal region maintenance 1 (CRM1) induced nuclear accumulation of EGFP-AZ1"].
- GO:0002931 response to ischemia (IEP): MARK_AS_OVER_ANNOTATED retained; mRNA-level change only [PMID:8649218 "Expression of both ODC and AZ mRNAs initially decreased to 70% of control levels 1 hr after recirculation"].
- GO:0090650 cellular response to oxygen-glucose deprivation (IEP): MARK_AS_OVER_ANNOTATED retained; Oaz1 was assayed as a candidate qPCR reference gene [PMID:19531214 "The expression was stable at the first four analysis times but decreased significantly at 24 h (p < 0.01) and 48 h (p < 0.05)"].

Quote hygiene: 13 UniProtKB quotes were a paraphrase of the old FUNCTION text and no longer match the refreshed P54370 entry; replaced with verbatim FUNCTION/INDUCTION text. Nucleus/cytoplasm rows now cite the PMID:12941943 abstract ("EGFP-AZ1 was predominantly localized in the cytoplasm") instead of the UniProt FUNCTION line, which says nothing about localization. Title-only quotes for PMID:12359729 and PMID:8166639 were replaced with abstract sentences (e.g. [PMID:8166639 "is now shown also to mediate the rapid feedback inhibition of polyamine uptake into mammalian cells"]).

Description rewritten to remove curation commentary ("The review accepts...").

Open questions: PMID:12941943 and PMID:12359729 are abstract-only in the cache; the species of the AZ1 construct is not stated in the abstracts (cell lines were CHO/NIH3T3 and reticulocyte lysate). The rat IDA attributions are left to the curators.
