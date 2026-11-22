# WHY1 (At1g14410, Q9M9S3) — manual literature synthesis

No deep-research API was available for this review. This file is a manual
synthesis from cached publications (`publications/PMID_*.md`) and PubMed
searches (query `(WHIRLY1 OR AtWHY1 OR "Whirly 1") AND Arabidopsis`, 38 hits,
October 2026). Quotes are verbatim from the cached abstracts or full texts.

## Identity and family

- WHY1 (synonym PTAC1) is one of three Arabidopsis Whirly proteins, a
  plant-specific family of single-stranded nucleic-acid-binding proteins with
  a tetrameric "whirligig" fold and a conserved KGKAAL motif.
  [PMID:21911368 "Whirlies constitute a small family of single-stranded DNA-binding proteins (SSB) that are mainly found in plants"]
- WHY1 and WHY3 are plastid-targeted; WHY2 is mitochondrial.
  [PMID:21911368 "In Arabidopsis, where there are three genes coding for Whirly proteins, WHY1 and WHY3 are directed to the chloroplasts whereas WHY2 is directed to the mitochondria."]
- The crystal structure of the Arabidopsis WHY1 Whirly domain (residues
  74-241; PDB 4KOO) is a tetramer.
  [PMID:24192350 "reveals that these structurally similar proteins assemble into tetramers"]

## Localization

- Plastid: GFP fusions and in vitro import (Krause et al. 2005).
  [PMID:15967440 "Transient expression of GFP fusion proteins in protoplasts and onion epidermal cells confirmed the localisation of these proteins in plastids or mitochondria, respectively."]
- Plastid nucleoid: identified as pTAC1 in transcriptionally active plastid
  chromosome preparations (PMID:16326926, abstract only); part of the
  chloroplast WHY1/3 pool is in large DNA-containing complexes.
  [PMID:21911368 "in extracts enriched in Arabidopsis chloroplasts, part of the WHY1/3 population is found in large complexes that contain DNA"]
- Nucleus: functional nuclear pool supported by several groups.
  [PMID:23269926 "In plants overexpressing the full-length sequence, WHIRLY1 accumulated in both plastids and the nucleus"]
  [PMID:22154598 "Although the tagged protein was synthesized in plastids, it was detected in nuclei."] (tobacco transplastomic)
  [PMID:23922267 "only WHY1 in the nucleus had a suppressing effect on the activity of the WRKY53 promoter at the early stage of senescence"]
  The 2005 GFP study did not detect a nuclear signal, which is the basis of a
  TAIR NOT|nucleus row; later work contradicts a categorical absence.

## Molecular function

- Non-sequence-specific ssDNA binding (structural mechanism from potato WHY2
  complexes, conserved in AtWHY1).
  [PMID:20551348 "These reveal a nonsequence-specific ssDNA binding mechanism in which DNA is stabilized between domains of adjacent subunits and rendered unavailable for duplex formation and/or protein interactions."]
- ssDNA binding by AtWHY1 in plastid extracts; the K91A mutation does not
  reduce binding.
  [PMID:21911368 "Figure 6C indicates that the ssDNA-binding activity is also similar in 35S:WHY1 and 35S:WHY1 K91A lines and proportional to the protein level."]
- Single-stranded telomeric DNA binding.
  [PMID:17217467 "AtWHY1 specifically binds the single-stranded plant telomeric DNA sequences, but not double-stranded telomeric DNA."]
- Promoter binding in the nucleus (KPRE element of AtKP1; ERE-like element
  of WRKY53).
  [PMID:19669906 "A ChIP assay showed that AtWHY1 and AtWHY3 bind to the upstream region of AtKP1 gene in vivo."]
  [PMID:23922267 "WHY1 bound to the sequence region that contains an elicitor response element motif-like sequence, GNNNAAATT, plus an AT-rich telomeric repeat-like sequence in the WRKY53 promoter"]
- Recruits histone deacetylase HDA15 to co-repress targets.
  [PMID:35510566 "We found that WHIRLY1 interacts with Histone Deacetylase (HDA)15"]
- RNA binding: captured in two Arabidopsis RNA interactome studies.
  [PMID:32344669 "ptRIC also assigned RNA-binding activity to all the members of the Alba- and the Whirly (WHY)-domain-containing protein families."]

## Biological roles

- Plastid genome stability / DNA repair: why1 why3 plants accumulate
  microhomology-mediated plastid DNA rearrangements; Whirlies negatively
  regulate the error-prone MMBIR pathway.
  [PMID:19666500 "Here, we report that the plastid-localized Whirly ssDNA-binding proteins are required for plastid genome stability in Arabidopsis."]
  [PMID:20551348 "This pathway is negatively regulated by the single-stranded DNA (ssDNA) binding proteins from the Whirly family"]
  [PMID:21911368 "Nevertheless, this mutation interferes with the biological function of Whirly proteins in DNA repair."]
- Telomere length homeostasis (negative regulation of telomerase).
  [PMID:17217467 "AtWHY1-deficient plants show a steady increase in the length of telomere tracts over generations. This telomere elongation is correlated with a significant increase in telomerase activity."]
- Defense: required for full SA-dependent disease resistance.
  [PMID:14960277 "DNA binding activity of AtWhy1, the Arabidopsis StWhy1 ortholog, is induced by SA and is required for both SA-dependent disease resistance and SA-induced expression of an SAR response gene."]
- Transcriptional repression of AtKP1, WRKY53 and senescence/flowering genes
  (with HDA15); why1 shows early senescence (PMID:23922267, PMID:35510566).
- ABA responsiveness of seeds requires the plastid pool (PMID:23269926).
- Plastid genome instability in why1 why3 is suppressed by reducing
  transcription/R-loops (PMID:30943245).
