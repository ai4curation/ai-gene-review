# SPNS1 review notes

## Curation scope

Falcon deep research was attempted with `just deep-research-falcon human SPNS1`, but the
provider timed out after 600 seconds and did not generate `SPNS1-deep-research-falcon.md`.
This review therefore relies on cached publications, UniProt/GOA-derived files, PN project
mappings, and these manual curation notes.

## Core function

SPNS1 is a lysosomal multi-pass major facilitator superfamily transporter. The
strongest current evidence supports a lysosomal lysophospholipid export/salvage
function, especially for LPC and LPE, with LPG and lysoplasmalogens also
transported in some assays. He et al. 2022 identified SPNS1 as a
proton-dependent LPC/LPE transporter and showed SPNS1-dependent efflux from
lysosomes followed by re-acylation into cytoplasmic phospholipid pools
[PMID:36161949 "Spns1 is a lysophospholipid transporter mediating lysosomal phospholipid salvage"].
Scharenberg et al. 2023 independently found SPNS1 in an endolysosomal CRISPR
screen under choline limitation and concluded that SPNS1 exports LPC from the
lysosome to support phospholipid synthesis and cell survival
[PMID:37075117 "An SPNS1-dependent lysosomal lipid transport pathway that enables cell survival under choline limitation"].

Chen et al. 2025 provide structural support for this molecular function: a
cryo-EM structure of human SPNS1 in an LPC-bound lumen-facing conformation,
transport assays for cavity residues, and a proton-sensing residue network
[PMID:39739806 "Molecular basis of Spns1-mediated lysophospholipid transport from the lysosome"].
He et al. 2025 extend the physiology to human disease, reporting biallelic
SPNS1 loss-of-function variants with lysosomal lysophospholipid/cholesterol
accumulation and altered triglyceride/cholesterol homeostasis
[PMID:40608416 "SPNS1 variants cause multiorgan disease and implicate lysophospholipid transport as critical for mTOR-regulated lipid homeostasis"].

## Proteostasis network context

The Proteostasis Network places SPNS1 under
`Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Efflux of autophagy products`.
That placement is biologically plausible because autophagy-derived membrane
lipids are degraded in autolysosomes and their products must exit the lysosomal
lumen for reuse. However, the PN row is a curation hypothesis, not primary
evidence. The relevant direct evidence is that SPNS1 exports lysosomal LPC/LPE
and that loss of SPNS1 disrupts lysosomal lipid homeostasis, lysosomal function,
and nutrient-stress survival [PMID:36161949; PMID:37075117; PMID:40608416].

The PN projected term `GO:0007041 lysosomal transport` is defensible as a new
annotation because SPNS1 transports lysosomal degradation products across the
lysosomal membrane. It is still broad and does not capture the specific cargo or
direction. A more precise GO term such as "lysosomal lysophospholipid export" or
"lysosomal phospholipid salvage" would better represent the biology.

## Annotation decisions

- Accept lysosomal membrane/lysosome localization as core, with PMID:36161949
  and UniProt supporting the lysosomal transporter model. The high-throughput
  placental lysosomal membrane proteomics study is consistent but not the main
  evidence [PMID:17897319].
- Accept lysophospholipid transport, phospholipid efflux, and the current
  GO:0051978 lysophospholipid transporter term as core. The GO label
  `lysophospholipid:sodium symporter activity` is mechanistically imperfect for
  SPNS1 because the papers describe proton-gradient dependence, so this review
  proposes a more specific ontology term.
- Modify broad `transmembrane transporter activity`, `transmembrane transport`,
  `lipid transport`, and generic `membrane` annotations to the more specific
  SPNS1 terms already supported by experiments.
- Keep the mitochondrial inner membrane annotation as non-core. UniProt records
  occasional mitochondrial localization from the early HSpin1 study, but the
  dominant conserved function is lysosomal.
- Mark `protein binding` as over-annotated. The BCL2/BCL2L1 interaction was
  reported in the early HSpin1 cell-death study [PMID:12815463], but GO:0005515
  is not informative for SPNS1's core molecular function.
