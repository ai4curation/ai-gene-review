# TFR2 manual deep research

## Research provenance

- `just deep-research-openscientist human TFR2` was attempted on 2026-07-19. The first
  attempt reached the provider wrapper's 600-second timeout without producing a report;
  a second OpenScientist attempt was started while the primary literature was reviewed.
- Gene, GOA, and reviewed UniProt records were fetched with `just fetch-gene human TFR2`.
  All nine PMIDs cited by the seeded review were cached with
  `just fetch-gene-pmids human TFR2`. Additional primary studies PMID:20576915 and
  PMID:20177050 were cached to cross-check the hepatic iron-sensing role.
- This file is a manual evidence synthesis, not an OpenScientist output.

## Identity, topology, and isoforms

Human TFR2 (UniProt Q9UP52) encodes transferrin receptor protein 2. The reviewed alpha
isoform is a type-II single-pass membrane protein and homodimer; the beta isoform lacks
the amino-terminal transmembrane region and is probably intracellular
[PMID:10409623, "The TfR2-beta protein lacked the amino-terminal portion of the TfR2-alpha"]
[file:human/TFR2/TFR2-uniprot.txt, "[Isoform Beta]: Cytoplasm"]. The original cloning
study found predominant liver expression of the alpha transcript and showed cell-surface
transferrin binding and transferrin-bound iron uptake in TFR2-alpha-transfected cells
[PMID:10409623, "marked increase in Tf-bound (55)Fe uptake."].

## Direct transferrin-receptor function

The strongest direct human molecular-function evidence is that TFR2 binds transferrin.
The initial cell study showed competitive cell-surface transferrin binding and increased
transferrin-bound iron uptake [PMID:10409623, "cells showed an increase in biotinylated Tf binding to the cell surface"].
A later full-length receptor study confirmed holo-transferrin binding and showed that
TFR2 uses binding/stabilization features distinct from TFRC; its affinity is lower than
TFRC's, but the interaction is specific and physiologically relevant
[PMID:29388418, "TfR1 and TfR2 have distinct mechanisms for stabilizing a complex with holo-Tf."].
Thus transferrin receptor activity, transferrin transport, receptor-mediated endocytosis,
and endocytic iron import are supported. The literature also emphasizes that bulk cellular
iron uptake is not TFR2's dominant physiological role, so these transport annotations
should not displace its systemic iron-sensing role
[PMID:29388418, "Though iron uptake is not thought to be the primary function of TfR2"].

## Hepatic iron sensing and hepcidin control

TFR2 is a hepatocyte transferrin-saturation sensor required for an appropriate hepcidin
response and organismal iron homeostasis. In primary human hepatocytes, holoferric
transferrin increased hepcidin expression and TFR2 abundance correlated positively with
hepcidin expression [PMID:20576915, "Hepcidin expression was increased in primary human hepatocytes following 24-h"].
Most compellingly, patients with TFR2 hemochromatosis had no acute hepcidin response to
oral iron [PMID:21173098, "iron-depleted HFE-hemochromatosis and absent in those with TFR2-hemochromatosis."].
Hepatocyte-targeted rescue in mice also showed that Tfr2 and Hfe are jointly required to
restore hepcidin and lower iron indices [PMID:20177050, "Expression of Tfr2 in Tfr2-deficient mice had a similar effect"].
These data support cellular response to iron, organismal iron homeostasis, and positive
regulation of hepcidin production/secretion as core biological roles.

## Complex assembly and regulatory partners

TFR2 forms an HFE-containing cell-surface complex. HFE co-expression increases TFR2
affinity for diferric transferrin and transferrin-dependent iron uptake and accelerates
HFE biosynthesis/late-Golgi maturation
[PMID:18353247, "increased affinity for diferric transferrin, increased transferrin-dependent"]
[PMID:18353247, "accelerated HFE biosynthesis and late-Golgi maturation"]. HFE and TFR2
also co-localize in a specialized vesicular compartment in intestinal cells
[PMID:12704209, "co-localized to a distinct CD63-negative vesicular compartment showing marked"].

HFE, TFR2, and the BMP co-receptor HJV physically form a membrane complex; TFR2 binds HJV
and RGMA via residues 120-139 of its extracellular domain
[PMID:22728873, "that HFE, TfR2, and HJV form a multi-protein membrane complex."]
[PMID:22728873, "required for the binding of both HFE and HJV."]. This supports the
HFE-transferrin receptor complex and co-receptor binding annotations and provides a
mechanistic bridge to hepcidin transcription. CD81 is a direct TFR2 interactor that
promotes TFR2 degradation yet is also required to maintain hepcidin mRNA
[PMID:25635054, "TfR2/CD81 complex is involved in the maintenance of hepcidin mRNA."].
The generic `protein binding` term is not an informative representation of any of these
interactions; transferrin binding should be represented by transferrin receptor activity,
and HFE association by the specific HFE-transferrin receptor complex.

## Annotation-review implications

- Accept transferrin receptor activity, transferrin transport, receptor-mediated
  endocytosis, endocytic iron import, plasma-membrane/external-side localization, cellular
  response to iron, hepcidin regulation, and systemic iron homeostasis.
- Retain cytoplasmic localization as non-core because it applies to the soluble beta
  isoform rather than the membrane alpha isoform that carries the principal functions.
- Modify transferrin-supported generic protein-binding annotations to transferrin receptor
  activity and the HFE interaction to HFE-transferrin receptor complex membership.
- Mark high-throughput OLFM4/SEC22A generic binding and the generic CD81 binding term as
  over-annotated: the former lacks gene-specific functional evidence in the cached paper,
  while the latter is real but not captured informatively by `protein binding`.
- Keep positive regulation of HFE maturation as a supported but non-core consequence of
  the HFE-TFR2 interaction.

## Remaining uncertainty

The exact conformational mechanism coupling transferrin occupancy to the HFE/HJV/BMP-SMAD
hepcidin pathway remains unresolved. The relative physiological contributions of direct
TFR2-mediated iron uptake versus iron sensing also vary by cell type and isoform. These
are mechanistic uncertainties, not reasons to reject the well-supported receptor,
localization, complex, or homeostasis annotations.
