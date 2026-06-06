# ptxS (PtxS) — Pseudomonas putida KT2440 — Curation Notes

UniProt: Q88HH7 (PTXS_PSEPK). Locus PP_3380. 339 aa. LacI/GalR-family HTH-type
transcriptional regulator (repressor). PE 1: Evidence at protein level.

## FUNCTION

PtxS is a LacI/GalR-family transcriptional repressor that negatively controls the
2-ketogluconate (2-KG) peripheral pathway of glucose metabolism in P. putida.

- [UniProt "Negatively regulates glucose metabolism by binding directly to the promoter region of the kgu and gad operons (PubMed:20581202). It also negatively regulates its own synthesis (PubMed:20581202)."]
- [PMID:20581202 "The genes for the periplasmic and cytoplasmic set of reactions are clustered in the host chromosome and grouped within two independent operons that are under the control of the PtxS regulator, which also modulates its own synthesis."]
- [PMID:20581202 "Footprint analysis revealed that PtxS binds to an almost perfect palindrome that is present within the three promoters and whose consensus sequence is 5'-TGAAACCGGTTTCA-3'. This palindrome overlaps with the RNA polymerase binding site."]

DNA binding is experimentally demonstrated (footprinting, EMSA-type promoter
binding). The CollecTF-derived GOA annotations for DNA-binding transcription
repressor activity (GO:0001217), transcription cis-regulatory region binding
(GO:0000976) and protein-DNA complex (GO:0032993) are IPI experimental
annotations sourced from PMID:20581202. PtxS represses by binding a palindromic
operator overlapping the RNA polymerase binding site, consistent with classic
LacI/GalR-family steric repression.

## ACTIVITY REGULATION

2-ketogluconate (2-keto-D-gluconate) is the molecular effector; binding causes
de-repression (dissociation from the operator).

- [UniProt "2-ketogluconate acts as a molecular effector and causes dissociation of PtxS from its target promoter."]
- [PMID:20581202 "in vitro we found that only 2-ketogluconate binds to the regulator with an apparent K(D) (equilibrium dissociation constant) of 15 muM, as determined using isothermal titration calorimetry assays."]

## SUBUNIT

Homodimer in solution (IPI identical protein binding, PMID:20581202).

- [UniProt "Homodimer in solution. {ECO:0000269|PubMed:20581202}."]
- [PMID:20581202 "Purified PtxS is a dimer that binds to the target promoters with affinities in the range of 1 to 3 muM."]

## DOMAIN

- [UniProt "Contains an N-terminal helix-turn-helix DNA-binding domain and a C-terminal domain that binds the effector."]
- N-terminal HTH lacI-type domain (residues 12–67); H-T-H motif (14–33).
- C-terminal periplasmic-binding-protein-like (PBP1) effector-binding domain
  (LacI/GalR architecture).

## CURATION SYNTHESIS

Core molecular function: sequence-specific DNA-binding transcription repressor
activity (GO:0001217), enacted through binding of a cis-regulatory palindromic
operator (GO:0000976). Core biological process: negative regulation of
DNA-templated transcription (GO:0045892), specifically of carbohydrate
(2-ketogluconate/glucose) catabolic genes.

Annotation notes:
- GO:0042802 identical protein binding (IPI, homodimer) — accept, supported by
  documented homodimer; not the core informative function but specific and
  evidence-backed (avoid generic "protein binding").
- GO:0003700 DNA-binding transcription factor activity (IEA/TreeGrafter) — for a
  dedicated repressor, GO:0001217 (repressor activity) is the more precise child
  term; MODIFY toward GO:0001217.
- GO:0003677 DNA binding (IEA) — broad parent of the cis-regulatory region
  binding term; over-annotated/uninformative on its own.
- GO:0006355 regulation of DNA-templated transcription (IEA) — broad parent of
  the more specific negative regulation term; over-annotated.
