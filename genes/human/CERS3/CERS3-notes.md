# CERS3 (ceramide synthase 3, LASS3) — review notes

UniProtKB: Q8IU89. HGNC:23752. Chromosome 15q26.3. 383 aa.

## Function (grounded in UniProt + cached primary literature)

CERS3 is a ceramide synthase (sphingosine N-acyltransferase, EC 2.3.1.24; also
EC 2.3.1.297 / 2.3.1.298 for VLC/ULC variants) that catalyzes the N-acylation
step of de novo ceramide biosynthesis: transfer of an acyl chain from acyl-CoA
onto the amino group of a sphingoid base (sphinganine/dihydrosphingosine in de
novo synthesis; sphingosine in the salvage pathway) to form
dihydroceramide/ceramide, at the ER membrane.

- Among the six mammalian CerS, CERS3 is distinguished by high selectivity for
  **very-long- and ultra-long-chain (≥C22, up to ≥C26/C28) acyl-CoAs**
  [UniProt FUNCTION; PMID:22038835 "we identified human and mouse ceramide
  synthase 3 (CerS3), among ... to be exclusively required for the ULC-Cer
  synthesis in vitro"].
- CerS family members display "a high specificity towards acyl CoAs of different
  chain lengths"; K(m) toward sphinganine determined [PMID:17977534].
- CERS3 is crucial for synthesis of ultra-long-chain ceramides (including
  omega-hydroxy acylceramides) that build the epidermal permeability barrier
  [PMID:22038835 "are key components of extracellular lipid lamellae";
  PMID:23754960].

## Localization

ER membrane; multi-pass membrane protein (6 predicted TM helices; C-terminus
cytoplasmic) [UniProt SUBCELLULAR LOCATION; TOPO_DOM 319..383 cytoplasmic
ECO:0000305|PubMed:26887952]. Not nuclear — see homeobox CAUTION below.

## Tissue specificity

Expressed in epidermis (localizes at the interface between stratum granulosum
and stratum corneum, at protein level) and testis [UniProt TISSUE SPECIFICITY;
PMID:23754960]. HPA: tissue-enhanced esophagus, skin, vagina.

## Disease

Autosomal recessive congenital ichthyosis 9 (ARCI9, MIM:615023) — a
skin-barrier / keratinization disorder [PMID:23754960; UniProt DISEASE;
Reactome R-HSA-428185]. Mouse CerS3 knockout is neonatal-lethal from
transepidermal water loss [PMID:22038835].

## Homeobox / DNA binding — the notable over-annotation trap

CERS3 contains a **degenerate homeobox-like region (66..127)** and matches
InterPro IPR001356 (Homeodomain / HD), which drives an automated IEA
`GO:0003677 DNA binding` annotation. UniProt explicitly flags this as
spurious: CAUTION "Contains a predicted homeobox domain which is degenerated,
lacking residues important for DNA-binding. Moreover, the protein localizes in
the endoplasmic reticulum and not in the nucleus, which also argues against
homeobox function." The homeobox is a shared ancestral feature of the
LAG1/LASS/CerS family and is not functional in CerS. The catalytic domain is
the TLC (TRAM-LAG1-CLN8) domain (130..331). => `DNA binding` should be REMOVED
(demonstrably wrong IEA). Likewise the `nucleoplasm` IDA (HPA GO_REF:0000052)
conflicts with the ER localization and the CAUTION; mark as over-annotated
(HPA IF can pick up antibody signal that does not reflect functional site).

## Interactions (PMID:32296183, HuRI)

High-throughput binary interactome (Y2H) screen. Reports 5 partners
(ORMDL3/Q8N138, Q96FB2, NEU1/Q99519, PCBD2/Q9H0N5, SLC39A9/Q9NUM3). These are
bare `protein binding` (GO:0005515) IPIs — uninformative per curation policy;
mark as over-annotated (do NOT remove experimental IPIs). ORMDL3 interaction is
biologically plausible (ORMDL proteins regulate sphingolipid/SPT flux) but the
HuRI screen alone does not establish a specific MF.

## Term decisions summary

- MF core: **GO:0050291 sphingosine N-acyltransferase activity** (exact GOA
  label). Multiple IDA (PMID:17977534, PMID:22038835), ISS, IBA, TAS, IEA lines
  — ACCEPT the experimental/IBA ones as core.
- BP core: **GO:0046513 ceramide biosynthetic process** (IDA x2, IMP, IBA;
  ACCEPT). GO:0030148 sphingolipid biosynthetic process (TAS Reactome, broader —
  KEEP_AS_NON_CORE). GO:0006665 sphingolipid metabolic process (UniPathway IEA,
  broadest — KEEP_AS_NON_CORE).
- Epidermis-barrier BPs: GO:0008544 epidermis development,
  GO:0070268 cornification, GO:0030216 keratinocyte differentiation — real
  downstream physiological roles of CERS3-made ULC-ceramides but not the
  gene's core molecular activity => KEEP_AS_NON_CORE.
- CC: GO:0005789 ER membrane (ISS/IEA/TAS) — ACCEPT core location.
  GO:0005783 ER (IBA/ISS/IEA) — ACCEPT (correct but less precise than ER
  membrane). GO:0016020 membrane (IEA InterPro) — too general, MARK_AS_OVER_ANNOTATED.
  GO:0005654 nucleoplasm (IDA HPA) — MARK_AS_OVER_ANNOTATED (contradicts ER/CAUTION).
- GO:0003677 DNA binding (IEA InterPro homeodomain) — REMOVE (demonstrably
  wrong; UniProt CAUTION documents degenerate, non-DNA-binding homeobox).
- GO:0005515 protein binding IPIs x5 (PMID:32296183 HuRI) — MARK_AS_OVER_ANNOTATED
  (uninformative bare protein binding; per policy do not REMOVE experimental IPIs).
</content>
</invoke>
