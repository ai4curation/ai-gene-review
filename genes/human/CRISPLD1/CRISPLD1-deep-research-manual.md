# Manual deep research: human CRISPLD1 (Q9H336)

Date: 2026-07-18

The configured automated research providers were attempted before this manual review.
Falcon/Edison returned HTTP 402, and the `perplexity-lite` fallback returned HTTP 401
because its quota was exhausted. This file records a manual synthesis from the local
UniProt/GOA/PANTHER/GO-CAM data and cached primary literature; it is deliberately not
named for either failed provider.

## Summary

CRISPLD1 is a 500-aa secreted CAP-superfamily protein with an N-terminal signal
peptide, one SCP/CAP domain, and two C-terminal LCCL domains. Its direct biochemical
activity and extracellular target are unknown. A focused human iPSC-cardiomyocyte study
provides the clearest functional evidence: CRISPR/Cas9 loss of function increased the
amplitude of calcium transients and altered their rise and decay kinetics, leading the
authors to conclude that CRISPLD1 normally inhibits cardiomyocyte calcium cycling
[PMID:32146539, "This loss-of-function and rescue experiments support the converse
argument, that CRISPLD1 plays an inhibitory role in CM Ca2+ cycling."]. CRISPLD1 is
also upregulated during the transition from pressure-overload hypertrophy to heart
failure, but the causal molecular mechanism remains unresolved.

Two human extracellular-fluid proteomic studies detected CRISPLD1 in exosome-enriched
fractions (parotid saliva and expressed prostatic secretions). These observations
corroborate secretion but are contextual localization evidence, because the isolation
methods can co-enrich soluble secreted proteins or contaminants.

A human family study of nonsyndromic cleft lip/palate reported statistical interactions
between CRISPLD1, CRISPLD2, and folate-pathway variants, but explicitly found no
significant etiologic contribution from CRISPLD1 alone
[PMID:21254358, "variation in CRISPLD1 alone does not play a significant etiologic
role in NSCLP"]. It does not establish a direct CRISPLD1 perturbation phenotype, so
face morphogenesis should not be treated as a core CRISPLD1 function.

## Annotation implications

- Accept extracellular-region annotations based on signal peptide/secretion evidence.
- Retain exosome HDA annotations only as non-core high-throughput localization context.
- Mark face morphogenesis as over-annotated pending direct developmental perturbation
  and rescue evidence.
- Remove the molecular-adaptor IBA: its only PAINT seed is mouse Glipr1l1, a divergent
  CAP-only sperm/acrosome protein, and no CRISPLD1-specific evidence demonstrates an
  adaptor mechanism.
- Add GO:0051481 (negative regulation of cytosolic calcium ion concentration) from the
  human cardiomyocyte loss-of-function phenotype.
- Do not add calcium channel regulator activity: no direct channel target, binding
  assay, or current measurement has established that molecular activity.

Full evidence excerpts and the seven-group decision log are in `CRISPLD1-notes.md`.
