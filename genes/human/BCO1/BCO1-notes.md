# BCO1 notes

Perplexity deep research could not run in this checkout because the provider is unavailable in
the retained runtime. This review therefore uses the local UniProt, QuickGO, PAINT, Reactome and
cached publication evidence directly.

## Core biology

BCO1 is the cytosolic central-cleavage enzyme for dietary provitamin A carotenoids. Human
BCO1 was cloned and expressed in baculovirus, and the abstract reports:
"Biochemical analysis of baculovirus expressed human BCDO demonstrates the predicted
beta,beta-carotene-15,15'-dioxygenase activity" [PMID:11401432].

PMID:24668807 used purified recombinant human BCO1 with beta-carotene and oxygen-isotope
labeling; it supports the current dioxygenase wording for the molecular function because it found
that BCO1 incorporates oxygen from O2 into retinal.

PMID:17951468 supports the patient T170M loss-of-function row: the mutation reduces purified
enzyme activity by about 90%, establishing that the wild-type protein performs the same central
beta-carotene cleavage.

BCO1 is already represented in `modules/intestinal_retinoid_absorption.yaml` as the cytosolic
beta-carotene to all-trans-retinal step. That module is sufficient; no BCO-specific module edit is
needed here.

## Annotation decisions

The central cleavage activity (`GO:0003834`), carotene catabolism, retinal metabolism, retinol
metabolism and vitamin A biosynthesis rows are retained. The broad `retinoid metabolic process`,
`isoprenoid metabolic process` and generic dioxygenase rows are true but imprecise given the
specific rows already present, so they are marked `TOO_GENERAL`.

All BCO1 PAINT rows are acceptable for the BCO1 branch. PTHR10543 itself is heterogeneous:
RPE65 is a retinyl-ester isomerohydrolase, BCO2 is an eccentric carotenoid cleaver, and other
non-human clades include plant NCED/CCD and bacterial/fungal stilbene-cleavage enzymes.
