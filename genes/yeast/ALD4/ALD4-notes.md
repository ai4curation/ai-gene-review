# ALD4 (YOR374W, UniProt P46367) notes

## Identity / naming
- Major mitochondrial K+-activated ALDH. Called "ALD7" in Tessier et al. [PMID:9675847 "The gene is situated on the right arm of chromosome XV, bears the systematic name YOR374w"] and "ALDH2" (commercial enzyme, chromosome XV) in Wang et al. [PMID:9473035 "The commercial ALDH (designated ALDH2) was partially sequenced and appears to be a mitochondrial enzyme encoded by a gene located on chromosome XV."]
- Matrix location [UniProt:P46367]; part of a native mitochondrial dehydrogenase supercomplex [PMID:11502169 "and the acetaldehyde dehydrogenase Ald4p"]

## Activity
- Dual cofactor [PMID:9473035 "Like ALDH5, the commercial ALDH2 enzyme used either NAD or NADP as a cofactor."]; Km acetaldehyde 10 uM with NADP [UniProt:P46367]
- Deletion abolishes K+-ACDH, impairs ethanol growth [PMID:9675847 "Growth on glucose was not affected in the mutants lacking ALD7 (in contrast to the behaviour of ald6 mutants), whereas growth on ethanol was severely impaired."]

## Processes
- Acetate: backup for Ald6p [PMID:10919763 "In contrast, a strain lacking both Ald6p and Ald4p exhibited a long delay in growth and acetate production, suggesting that Ald4p can partially replace the Ald6p isoform."]; [PMID:15256563 "The absence of Ald6p was compensated by the mitochondrial isoforms and this involves the transcriptional activation of ALD4."]
- Mitochondrial NADPH [PMID:19158096 "evidence is presented that acetaldehyde dehydrogenases, and in particular Ald4p, play a prominent role in generating mitochondrial NADPH in the absence of the NADH kinase reaction."]
- Lipid: overexpression phenotype only, indirect [PMID:39462103 "Genetic validation demonstrated that overexpression of the mitochondrial acetaldehyde dehydrogenase (ALDH) gene ALD4 resulted in a 20.1% increase in lipid production."]

## Curation observations
- RCA cytosol is_active_in (from GLUCFERMEN-PWY compartment) contradicts matrix localization: removed.
- Bifid shunt RCA removed. Proposed NEW ethanol catabolic process (IMP, PMID:9675847).
- Mitochondrial nucleoid IDA (PMID:10869431): abstract does not name Ald4p; kept non-core.
