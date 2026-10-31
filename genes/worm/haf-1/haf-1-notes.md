# haf-1 (C30H6.6; UniProt O45278, unreviewed) review notes

## Deep research status
`just deep-research-falcon worm haf-1 --fallback perplexity-lite` failed on 2026-10-08 (falcon timeout; perplexity unavailable). No deep-research file was created. The review is based on the UniProt record, cached publications and PubMed/PMC full text read through the PubMed MCP: PMC2846537 for PMID:20188671 and PMC3518298 for PMID:22700657. The cached copies of both are abstract-only.

## Key findings
- HAF-1 is a mitochondrial ABC half-transporter needed for ATP-dependent peptide efflux [PMID:20188671 "Peptide efflux from isolated mitochondria was ATP dependent and required HAF-1 and the protease ClpP."]
- It is required for UPRmt signaling and for nuclear localisation of ATFS-1 [PMID:20188671 "Defective UPR(mt) signaling in the haf-1-deleted worms was associated with failure of the bZIP protein, ZC376.7, to localize to nuclei"]
- It is described as localised to the inner membrane [PMID:22719267 "the mitochondrial inner membrane-localized peptide transporter HAF-1"]
- From the full text of PMC2846537 (not cached): HAF-1 was localised to the inner membrane by fractionation of tagged protein in CHO cells, with the ABC domain on the matrix side. Peptide efflux from haf-1 mitochondria was about 3-fold lower, while protein degradation was not affected.
- From the full text of PMC3518298 (not cached): HAF-1 is "a general attenuator of mitochondrial protein import during stress". It is needed for UPRmt under moderate stress, but not under severe stress or direct block of import. This is why the IMP "protein import into mitochondrial matrix" is marked over-annotated: HAF-1 dampens import rather than taking part in it.

## Curation decisions
- Core MF: GO:0015440 ABC-type peptide transporter activity (matches the module). Process: GO:0090374 oligopeptide export from mitochondrion and GO:0034514 mitochondrial UPR. Location: GO:0005743.
- Transport by purified HAF-1 has not been reconstituted, so the MF rests on mutant-mitochondria efflux plus homology to Mdl1.
- GO has no live term for negative regulation of mitochondrial protein import (GO:1903215 is obsolete). This is raised as a suggested question.
