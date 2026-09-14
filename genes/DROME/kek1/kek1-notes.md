# kek1 (kekkon-1, Q9VK54, FBgn0015399) — curation notes

Drosophila melanogaster. Single-pass type-I transmembrane protein of the LRR + Ig
(immunoglobulin) superfamily. Founding member of the Kekkon family. Best-established
function: a dedicated, transcriptionally-induced negative-feedback inhibitor of the
Drosophila EGF receptor (DER/EGFR).

## Provenance of the cached literature

All 8 cached publications are abstract-only (`full_text_available: false`; the Genetics
papers include a "Full Text" block that is only the re-printed abstract). Supporting
quotes below are verbatim from those abstracts.

## Architecture (MF/domain)

- Originally cloned with kek2 as a novel class of transmembrane LRR+Ig proteins:
  [PMID:8812109 "We have identified two members of a novel class of genes in Drosophila that encode putative transmembrane proteins with six leucine-rich repeats and a single immunoglobulin loop."]
  and [PMID:8812109 "These two molecules, Kek1 and Kek2, show striking conservation in their extracellular domains and have large and more divergent intracellular regions."]
- UniProt Q9VK54 (880 aa): signal peptide 1–20, extracellular LRR array + Ig-like domain
  (329–430), single TM helix 444–467, and a long largely disordered cytoplasmic tail.
  InterPro/Pfam: LRR (PF13855 LRR_8 x2, SMART LRR_TYP x5, LRRCT), I-set Ig (PF07679).
- The LRRs form the EGFR-binding surface; the founding-family framing is repeated in
  [PMID:15166146 "Kek1 encodes a molecule containing leucine-rich repeats (LRR) and an immunoglobulin (Ig) domain and is the founding member of the Drosophila Kekkon family."]

## Molecular function: EGFR binding + signaling receptor inhibitor activity

- Kek1 was identified as a direct EGFR inhibitor:
  [PMID:10102272 "We have identified the Drosophila transmembrane molecule kekkon 1 (kek1) as an inhibitor of the epidermal growth factor receptor (EGFR) and demonstrate that it acts in a negative feedback loop to modulate the activity of the EGFR tyrosine kinase."]
- It physically associates with the receptor via its extracellular/TM domains:
  [PMID:10102272 "We show that the extracellular and transmembrane domains of Kek1 can inhibit and physically associate with the EGFR, suggesting potential models for this inhibitory mechanism."]
- The extracellular LRRs mediate direct binding; Kek1 forms a heterodimer with DER:
  [PMID:12900463 "Structure-function analysis reveals that the extracellular Leucine-Rich Repeat (LRR) domains of Kek1 are critical for its function through direct association with DER, whereas its cytoplasmic domain is required for apical subcellular localization."]
  and [PMID:12900463 "the use of chimeric proteins between Kek1 extracellular and transmembrane domains fused to DER intracellular domain indicates that Kek1 forms an heterodimer with DER in vivo"]
- Mechanism of inhibition (mammalian cell assays): blocks ligand binding and receptor
  activation, extends to all ErbB family members:
  [PMID:12900463 "We show that Kek1 is capable of physically interacting with each of the known members of the mammalian ErbB receptor family and that the Kek1/EGFR interaction inhibits growth factor binding, receptor autophosphorylation and Erk1/2 activation in response to EGF."]
- Binding vs. inhibition are separable: LRRs suffice for binding, but the
  juxta/transmembrane region is required for inhibition (bipartite mechanism):
  [PMID:15166146 "while the LRRs suffice for EGFR binding, inhibition in vivo requires the Kek1 juxta/transmembrane region"]
  and the receptor determinant maps to DER domain V:
  [PMID:15166146 "our results support a model in which the LRRs of Kek1 in conjunction with its juxta/transmembrane region direct association and inhibition of the Drosophila EGFR through interactions with receptor domain V."]
- Loss-of-function missense alleles pinpoint LRR1/LRR2 as the binding surface:
  [PMID:15020418 "All class I alleles map to the first and second LRRs of Kek1, suggesting a primary role for these two repeats in specifying association with and inhibition of EGFR."]
  with separable binding-affinity vs. localization classes:
  [PMID:15020418 "Class I alleles directly diminish Kek1's affinity for EGFR, while class II alleles disrupt Kek1's subcellular localization, thereby indirectly affecting its ability to associate with and inhibit the receptor."]
- Inhibition is specific to Kek1 among the family and not ligand/tissue restricted:
  [PMID:15166146 "EGFR inhibition is unique to Kek1 among Kek family members and that this function is not ligand or tissue specific"]

GO mapping: GO:0005154 (epidermal growth factor receptor binding) and GO:0030547
(signaling receptor inhibitor activity) are both directly supported and represent the
core molecular functions.

## Biological process: negative feedback on EGFR signaling

- kek1 is a transcriptional target of EGFR and acts in a feedback loop during oogenesis:
  [PMID:10102272 "During oogenesis, kek1 is expressed in response to the Gurken/EGFR signaling pathway, and loss of kek1 activity is associated with an increase in EGFR signaling."]
  restated in [PMID:15020419 "In D. melanogaster, kek1 is a transcriptional target of EGFR signaling during oogenesis, where it acts to attenuate receptor activity through an inhibitory feedback loop."]
- The same feedback role operates in other DER-mediated contexts, including the eye:
  [PMID:12900463 "The transmembrane protein Kekkon 1 (Kek1) has previously been shown to act in a negative feedback loop to downregulate the Drosophila Epidermal Growth Factor Receptor (DER) during oogenesis."]
  and [PMID:15020418 "Here we demonstrate that Kek1 inhibits EGFR activity during eye development and use this role to identify kek1 loss-of-function mutations that implicate the LRRs in directing receptor inhibition."]

GO mapping: GO:0042059 (negative regulation of EGFR signaling pathway) — core BP.

## Oogenesis / dorsoventral patterning (developmental context)

- kek1 is expressed in dorsal follicle cells mirroring the EGFR-activation profile during
  D/V axis formation:
  [PMID:15020419 "During formation of the dorsal-ventral axis Kek1 is expressed in dorsal follicle cells in a pattern that reflects the profile of receptor activation."]
- Early expression in follicle cells in a D/V gradient:
  [PMID:8812109 "kek1 is also expressed in other patterned epithelia, such as the follicle cells of the developing egg chamber, where it is found in a dorsal-ventral gradient around the oocyte."]

Oogenesis (GO:0048477) is a legitimate developmental setting but is the arena in which the
EGFR-inhibitor function acts, not an independent core function → best kept as non-core.

## Localization

- Kek1 localizes to the (apical) plasma membrane; the cytoplasmic tail directs apical
  targeting:
  [PMID:12900463 "Structure-function analysis reveals that the extracellular Leucine-Rich Repeat (LRR) domains of Kek1 are critical for its function through direct association with DER, whereas its cytoplasmic domain is required for apical subcellular localization."]
- Predicted membrane/cell-surface protein from sequence:
  [PMID:8812109 "The homology of the kek genes to other known adhesion and signaling molecules, together with their expression patterns, suggests that both genes are involved in interactions at the cell surface."]

GO mapping: GO:0016324 (apical plasma membrane) and the parent GO:0005886 (plasma membrane).

## Neuronal / CNS expression (family redundancy)

- kek1 and kek2 are expressed in differentiating CNS neurons; single kek1 deletion has no
  overt phenotype, consistent with family redundancy:
  [PMID:8812109 "Both genes are expressed in neurons as they differentiate in the embryonic central nervous system (CNS)."]
  and [PMID:8812109 "deletion of the kek1 gene causes no obvious developmental defects"]
- Note: broader synaptic-growth / Toll-family neuronal roles reported elsewhere for the
  Kekkon family are not represented in the current GOA set and are not annotated here.

## Evolutionary note

- Kek1 EGFR-inhibitor function is conserved in dipterans but absent from vertebrates and
  C. elegans:
  [PMID:15020419 "Kek1 was initially identified in Drosophila melanogaster and appears to be absent from vertebrates and the invertebrate Caenorhabditis."]

## Annotations that could not be verified from cached abstracts

- GO:0030547 IDA / PMID:11782411 (Ghiglione 2002): the cached abstract is about Gurken
  activation of EGFR (Star/Brho-mediated cleavage) and does not mention kek1. Full text
  unavailable → UNDECIDED (do not overrule an experimental FlyBase annotation).
- GO:0042059 IMP / PMID:11141565 (Duchek & Rørth 2001, Science): abstract is about EGFR
  guidance of border-cell migration and does not mention kek1. Full text unavailable →
  UNDECIDED.

## Core functions (synthesis)

1. MF: epidermal growth factor receptor binding (GO:0005154) — LRR-mediated direct
   association with DER/EGFR.
2. MF: signaling receptor inhibitor activity (GO:0030547) — forms an inactive heterodimer
   with EGFR, blocking ligand binding and autophosphorylation.
   Directly involved in: negative regulation of EGFR signaling pathway (GO:0042059).
   Location: apical plasma membrane (GO:0016324).
</content>
</invoke>
