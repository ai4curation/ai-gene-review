# TPK1 (human) — gene review notes

UniProt: Q9H3S4 (TPK1_HUMAN), 243 aa. HGNC:17358. Gene on chr 7q34.

## Identity and core function

TPK1 = thiamine pyrophosphokinase 1 (thiamin diphosphokinase), EC 2.7.6.-.
Catalyzes transfer of a pyrophosphate group from a nucleoside triphosphate to
thiamine (vitamin B1) to make thiamine diphosphate (ThDP / thiamine
pyrophosphate, TPP), the active vitamin-B1 cofactor.

- UniProt FUNCTION: "Catalyzes the phosphorylation of thiamine to thiamine
  pyrophosphate (TPP) utilizing UTP and therefore links the biosynthesis of TPP
  to pyrimidines metabolism (PubMed:38547260). By producing thiamine
  pyrophosphate, a cofactor of the mitochondrial pyruvate dehydrogenase
  indirectly regulates pyruvate oxidation and lipogenesis"
  [file:human/TPK1/TPK1-uniprot.txt].
- UniProt CATALYTIC ACTIVITY: "Reaction=thiamine + UTP = thiamine diphosphate +
  UMP + H(+);" (RHEA:79423) [file:human/TPK1/TPK1-uniprot.txt].
- UniProt PATHWAY: "Cofactor biosynthesis; thiamine diphosphate biosynthesis;
  thiamine diphosphate from thiamine: step 1/1."
  [file:human/TPK1/TPK1-uniprot.txt]. Single committed step.
- UniProt SUBUNIT: "Homodimer." [file:human/TPK1/TPK1-uniprot.txt].
- Kinetics: KM=0.33 mM for UTP; KM=5 mM for ATP [file:human/TPK1/TPK1-uniprot.txt].
- Reactome R-HSA-196761: "Cytosolic thiamin pyrophosphokinase (TPK1) catalyzes
  the reaction of thiamin (THMN) and ATP to form thiamin diphosphate (ThDP aka
  thiamin pyrophosphate) and ADP. ThDP is an active cofactor for transketolase,
  pyruvate dehydrogenase and alpha-ketoglutarate dehydrogenase ... Its
  homodomeric structure and association with Mg2+ are inferred from properties
  of the homologous yeast enzyme (Baker et al. 2001)." [Reactome:R-HSA-196761].

## Phosphodonor: classic ATP, but UTP-preferring (key finding)

PMID:38547260 (Sahu et al., Science 2024; full text available):
- "UTP was the preferred substrate for TPK1 in producing TPP" and "TPK1 showed a
  ~10-fold higher affinity for UTP than ATP (Km-UTP = 0.33 mM; Km-ATP = 5 mM)".
- "Genetic depletion of TPK1 decreased abundance of TPP, pyruvate catabolism,
  and amounts of the product of TKT sedoheptulose 7-phosphate".
- IMP for regulation of pyruvate decarboxylation to acetyl-CoA (GO:0010510):
  "cells expressing D100A TPK1 displayed decreased pyruvate catabolism compared
  to that of sgTPK1 cells reconstituted with wild-type TPK1".
- Catalytic residues D100 (both UTP and ATP catalysis) and F101 (UTP-specific);
  UniProt MUTAGEN 100 D->A loss of activity, 101 F->A loss of UTP-specific
  activity.

## Founding characterization

PMID:11342111 (Nosaka et al. 2001; abstract only, full_text_available: false):
- "A human thiamine pyrophosphokinase cDNA clone (hTPK1) was isolated and
  sequenced." When expressed in E. coli "marked enzyme activity was detected in
  the bacterial cells." Chromosome 7q34.

## Protein interactions (GOA IPI annotations)

- Identical protein binding (GO:0042802) reported 4x (PMID:25502805,
  PMID:29892012, PMID:31515488, PMID:32296183) — all consistent with the
  documented homodimer and the IntAct TPK1-TPK1 self-interaction (NbExp=8 in the
  UniProt INTERACTION block). These are high-throughput
  interactome / systematic-mutation studies (HuRI, disease-mutation pipelines),
  not TPK1-focused, but they correctly capture homodimerization → kept as
  non-core.
- Bare "protein binding" (GO:0005515, PMID:32296183) = TPK1-OPLAH interaction
  (WITH:O14841, UniProt INTERACTION lists "Q9H3S4; O14841: OPLAH; NbExp=3").
  Uninformative and no established functional consequence → MARK_AS_OVER_ANNOTATED
  (experimental IPI, not removed per policy).

## Disease

THMD5: UniProt DISEASE "Thiamine metabolism dysfunction syndrome 5, episodic
encephalopathy type (THMD5) [MIM:614458]: An autosomal recessive metabolic
disorder due to an inborn error of thiamine metabolism ... acute encephalopathic
episodes associated with increased serum and CSF lactate."
[file:human/TPK1/TPK1-uniprot.txt]. Variants Pro-40, His-50, Ser-219
(PMID:22152682).

## GO term verification (QuickGO, 2026-07)

All ids confirmed current (not obsolete), correct aspect:
- GO:0004788 thiamine diphosphokinase activity (MF)
- GO:0141200 UTP thiamine diphosphokinase activity (MF)
- GO:0009229 thiamine diphosphate biosynthetic process (BP)
- GO:0006772 thiamine metabolic process (BP)
- GO:0036172 thiamine salvage (BP)
- GO:0010510 regulation of pyruvate decarboxylation to acetyl-CoA (BP)
- GO:0030975 thiamine binding (MF)
- GO:0005829 cytosol (CC); GO:0005524 ATP binding (MF)
- GO:0005515 protein binding (MF); GO:0042802 identical protein binding (MF)

## Review decisions (summary)

- Core MF: GO:0004788 (thiamine diphosphokinase activity) and GO:0141200 (UTP
  thiamine diphosphokinase activity, physiological preference).
- Core BP: GO:0009229 (thiamine diphosphate biosynthetic process); location
  cytosol GO:0005829.
- ACCEPT: both catalytic MF terms (IDA + IBA + IEA duplicates), GO:0009229
  (IBA/IEA/IDA), cytosol (IBA/IEA/TAS), GO:0005524 ATP binding.
- KEEP_AS_NON_CORE: thiamine salvage, thiamine metabolic process (general),
  thiamine binding (substrate-binding component), identical protein binding
  (homodimer), regulation of pyruvate decarboxylation to acetyl-CoA (downstream
  consequence).
- MARK_AS_OVER_ANNOTATED: bare protein binding (GO:0005515, OPLAH IPI).
- No REMOVE actions. No experimental annotation removed.
