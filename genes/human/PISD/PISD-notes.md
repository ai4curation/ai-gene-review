# PISD manual review notes

`just deep-research-falcon human PISD --fallback perplexity-lite` could not run in this checkout because the Falcon and Perplexity providers were unavailable; only the `claude_code` provider was configured. I therefore reviewed the UniProt record, the GOA rows, the existing PTHR10067 family review, the CDP-DAG phospholipid-synthesis module, and the cached publications manually.

## Core function

PISD is the human eukaryotic type I phosphatidylserine decarboxylase. The PANTHER family review already scopes GO:0004609 and GO:0006646 to the PSD subfamilies and marks PTN000007430 as sound for the type I branch. The patient-fibroblast paper directly supports the human activity: PISD fibroblasts had decreased conversion of radiolabeled PS into PE and disease alleles impaired the processing/activity of the protein [PMID:30858161, "Patient fibroblasts have decreased ability to convert PS into PE."; PMID:30858161, "the paternal variant impairs autocatalytic self-processing of the PISD protein required for its activity"].

## Compartments

The canonical PISD-M isoform is mitochondrial and is curated by UniProt as a mitochondrial inner-membrane enzyme. Kumar et al. observed PISD-M-GFP colocalization with MitoTracker and identified the alternatively spliced PISD-LD isoform, whose targeting sequence partitions between lipid droplets and mitochondria according to lipid state [PMID:33593792, "PISD-M-GFP co-localized precisely with mitotracker"; PMID:33593792, "The cores of all of the punctate organelles decorated by PISD-LD-GFP stained with BODIPY dye, identifying them as LDs"].

The nucleus row is from a LIFEdb expressed-fusion screen and is not corroborated by the native/curated localization picture, so it is over-annotated rather than a third functional compartment.

## Downstream phenotype rows

The regulation-of-mitochondrion-organization IMP is plausible as non-core downstream biology: mitochondrial fragmentation in patient fibroblasts was rescued by lyso-PE and by wild-type PISD [PMID:30858161, "genetic complementation with WT-PISD rescued mitochondrial fragmentation in 2DG-treated patient cells"].

The mitochondrial protein catabolism row overstates a proteostasis phenotype as a direct PISD process. Zhao et al. found altered OMA1, PGAM5, OPA1 and MRPL32 levels/processing, but they interpret this as an indirect consequence of altered inner-membrane PE rather than direct proteolysis by PISD [PMID:30858161, "the global reduction of PISD activity and subsequent decrease in PE levels contributes indirectly to impaired mitochondrial protein homeostasis"].

The lipid-droplet-formation row is also over-annotated. Depleting both PISD isoforms reduced incorporation of oleate into TAG, but did not change gross LD number or size, and the authors could not separate a direct PISD-LD effect from secondary mitochondrial effects [PMID:33593792, "The gross appearance of LDs (number/cell, size), visualized by BODIPY staining and fluorescence microscopy, in these cells was indistinguishable from that of control cells."; PMID:33593792, "Although these data indicate that PISD promotes TAG storage, they do not resolve if this is attributed to PISD-LD, PISD-M, or both."].
