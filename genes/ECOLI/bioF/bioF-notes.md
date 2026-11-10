# bioF (Escherichia coli K-12, P12998) review notes

UniProtKB P12998 (BIOF_ECOLI), b0776. EC 2.3.1.47. Reference protein of PANTHER PTHR13693
(family review interpro/panther/PTHR13693/PTHR13693-review.yaml; subfamily SF100).

## Deep research

Not available in this session (no provider keys; template missing). Built from UniProt and
cached literature.

## Biology

- PLP-dependent decarboxylative condensation of L-alanine with pimeloyl-CoA; first committed
  step of biotin synthesis. [PMID:10642176 "This is the first committed step in biotin biosynthesis."]
- Homodimer; apo and PLP structures. [PMID:9813126 "The protein is a symmetrical homodimer"]
- Physiological donor is pimeloyl-ACP. [PMID:20693992 "We believe that pimeloyl-ACP rather than pimeloyl-CoA is the physiological substrate of BioF."]

## Decisions

All AONS activity, biotin biosynthesis and PLP binding rows ACCEPT (IMP row on abstract-less
PMID:4921685 accepted in deference to the curator). catalytic activity and transferase activity
TOO_GENERAL. homodimerization KEEP_AS_NON_CORE. GO:0008710 is CoA-defined while the physiological
donor is ACP: raised as a suggested question.
