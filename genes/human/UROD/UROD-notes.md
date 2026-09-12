# UROD (Uroporphyrinogen decarboxylase) — curation notes

UniProt: P06132 (DCUP_HUMAN). HGNC:12591. EC 4.1.1.37. 367 aa. Chromosome 1.

## Core biology

UROD catalyzes the **fifth step of heme biosynthesis**: the sequential decarboxylation of
the four acetate side chains of uroporphyrinogen III to methyl groups, yielding
coproporphyrinogen III (plus 4 CO2), in the **cytosol**.

- UniProt FUNCTION: "Catalyzes the sequential decarboxylation of the four acetate side
  chains of uroporphyrinogen to form coproporphyrinogen and participates in the fifth step
  in the heme biosynthetic pathway" [file:human/UROD/UROD-uniprot.txt].
- Reaction (Rhea:19865, EC 4.1.1.37): uroporphyrinogen III + 4 H(+) = coproporphyrinogen III
  + 4 CO2. Also acts on uroporphyrinogen I → coproporphyrinogen I (Rhea:31239), less
  efficiently, but only the III isomer feeds heme synthesis.
- Cofactor-independent decarboxylase; **homodimer** (PubMed:9194196, 9564029, 14633982).
- PATHWAY (UniProt): protoporphyrin-IX biosynthesis; coproporphyrinogen-III from
  5-aminolevulinate: step 4/4.
- Subcellular location: Cytoplasm, cytosol.

## Key experimental references (verbatim anchors)

- [PMID:14633982 "Uroporphyrinogen decarboxylase (URO-D), an essential enzyme that functions in \nthe heme biosynthetic pathway, catalyzes decarboxylation of all four acetate \ngroups of uroporphyrinogen to form coproporphyrinogen"] — structural basis; Asp86 is the
  key catalytic residue; single active center decarboxylates all four acetate groups; crystal
  structures with coproporphyrinogen I and III products.
- [PMID:11719352] — 12 F-PCT mutations characterized; recombinant mutant activities 29–94%
  of normal; crystal structures of 3 mutants; confirms enzymatic activity (IDA).
- [PMID:21668429 "Hepatoerythropoietic porphyria (HEP) is a rare form of porphyria that results from a deficient activity of the heme biosynthetic enzyme uroporphyrinogen decarboxylase (UROD)"]
  — G170D HEP variant; recombinant UROD purified and assayed on uroporphyrinogen I and III
  (IDA for activity).
- [PMID:11069625 "deficiency of hepatic uroporphyrin-\nogen decarboxylase activity"] — F-PCT
  mutations (A80S etc.); disease + hemochromatosis co-inheritance.
- [PMID:12071824 "profound deficiency (<10% of normal activity) of uroporphyrinogen decarboxylase \n(UROD) activity"] — HEP F46L; recombinant expression confirms deleterious effect
  (IDA). Note: in vitro UROD also decarboxylates pentacarboxylate porphyrinogen I.
- [PMID:1634232 "A deficiency in the activity of uroporphyrinogen decarboxylase (UROD), the fifth \nenzyme of the haem biosynthetic pathway"] — R292G HEP; explicitly "the fifth enzyme"
  (TAS for MF).
- [PMID:18004775] — Primary focus is URO-synthase (UROS), but developed expression/
  purification for "these cytosolic enzymes of heme biosynthesis" including
  URO-decarboxylase, and probed the URO-decarboxylase complex by NMR; GOA anchors an IDA
  (GO:0004853) and IC (GO:0006783) here. Full text not in cache; curator judgment retained.
- Reactome R-HSA-189425 (URO3→COPRO3) and R-HSA-190182 (URO1→COPRO1): "Cytosolic
  uroporphyrinogen decarboxylase (UROD) catalyzes the seq[u]ential removal of four carboxylic
  groups from the acetic acid side chains of uroporphyrinogen ...". TAS cytosol.

## Disease

- **Familial porphyria cutanea tarda (FPCT, MIM:176100)**: autosomal dominant, low
  penetrance; commonest porphyria (~20% familial). Heterozygous UROD deficiency.
- **Hepatoerythropoietic porphyria (HEP)**: homozygous/biallelic UROD deficiency
  (<10–~40% residual activity); severe childhood-onset cutaneous porphyria; considered the
  homozygous form of PCT [PMID:21668429].

## Annotation-review decisions

- MF **GO:0004853 uroporphyrinogen decarboxylase activity** (IBA, IEA, multiple IDA, TAS):
  ACCEPT — this is the core MF, strongly supported experimentally and structurally.
- BP **GO:0006783 heme biosynthetic process** (IBA, IC): ACCEPT — core BP (fifth step of
  heme synthesis).
- BP **GO:0006785 heme B biosynthetic process** (IDA): ACCEPT — correct, coproporphyrinogen
  III feeds heme b synthesis; more specific but valid.
- BP **GO:0006779 porphyrin-containing compound biosynthetic process** (IEA): ACCEPT — correct
  parent-level biosynthetic term.
- BP **GO:0006778 porphyrin-containing compound metabolic process** (IDA): ACCEPT (parent
  metabolic term; correct but general).
- BP **GO:0006787 porphyrin-containing compound catabolic process** (IDA x4): MODIFY — this is
  DIRECTIONALLY WRONG. UROD is anabolic (biosynthesis); decarboxylating uroporphyrinogen III
  to coproporphyrinogen III is a heme-biosynthetic step, not porphyrin catabolism. Propose
  replacement GO:0006783 (heme biosynthetic process) / GO:0006779. Likely a systematic
  mis-mapping applied across the four disease/structural papers.
- CC **GO:0005829 cytosol** (IBA, IEA, IDA, ISS, TAS): ACCEPT — established localization.
- CC **GO:0005654 nucleoplasm** (IDA, HPA): MARK_AS_OVER_ANNOTATED — HPA immunofluorescence
  can detect nucleoplasmic signal, but UROD is a cytosolic heme-biosynthesis enzyme with no
  established nuclear function; not core.
- MF **GO:0005515 protein binding** (IPI x5, high-throughput interactome screens): all
  MARK_AS_OVER_ANNOTATED — uninformative bare protein-binding from proteome-scale Y2H/AP-MS
  maps (PMIDs 25416956, 28514442, 31515488, 32296183, 33961781); no functional partner
  established.

## Deep research

falcon deep-research provider is out of credits (HTTP 402); no -deep-research-falcon.md was
generated. Review grounded in UROD-uniprot.txt, the seeded GOA, and cached publications/PMID_*.md.
