# SPNS1 review notes

## Curation scope

Falcon deep research has now completed successfully and is saved as
`SPNS1-deep-research-falcon.md` (15 citations; see the synthesis section below).
This review draws on that report together with cached publications,
UniProt/GOA-derived files, PN project mappings, and these manual curation notes.
(An earlier attempt had timed out before the `deep_research_unified` template/ID
bugs were fixed.)

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
- Accept lysophospholipid transport and phospholipid efflux as core. Treat
  GO:0051978 `lysophospholipid:sodium symporter activity` as mechanistically
  incorrect for SPNS1 because the papers describe proton-gradient dependence;
  use the broad transmembrane transporter activity term pending the proposed
  proton-specific ontology term.
- Accept broad `transmembrane transporter activity` as accurate pending a
  proton-specific lysophospholipid symporter term. Modify `transmembrane
  transport`, `lipid transport`, and generic `membrane` annotations to more
  specific SPNS1 terms already supported by experiments.
- Keep the mitochondrial inner membrane annotation as non-core. UniProt records
  occasional mitochondrial localization from the early HSpin1 study, but the
  dominant conserved function is lysosomal.
- Mark `protein binding` as over-annotated. The BCL2/BCL2L1 interaction was
  reported in the early HSpin1 cell-death study [PMID:12815463], but GO:0005515
  is not informative for SPNS1's core molecular function.

## Falcon deep research synthesis (2026-06-21)

The Falcon deep research report (`file:human/SPNS1/SPNS1-deep-research-falcon.md`)
corroborates the lysosomal lysophospholipid-salvage model above and adds three
strands of newer evidence not previously captured in these notes. Citations
below use the DOIs given in the Falcon report; PMIDs already verified for the
core papers are reused from the sections above.

**Structural / mechanistic detail (Chen et al. 2025, PMID:39739806;
doi:10.1073/pnas.2409596121).** The 3.2 Å cryo-EM structure captures SPNS1 in an
outward/lumen-facing state with LPC bound in a lateral opening between TM5 and
TM8 (substrate residues Y203, G200, L201, I204 on TM5 and S322, G326, L327, C330
on TM8; G200L/G326L/Y203A abolish transport). Proton coupling is mediated by a
hydrophilic network rather than a single residue: D94 is central, with E87, S97,
R300 and S442 forming a salt-bridge/H-bond network (D94A abolishes, D94N partly
rescues; R300A nearly abolishes). Chimeric transfer of E87/S97 into the
pH-independent paralog SPNS2 confers pH dependence, and the reciprocal SPNS1
E87Q/S97A makes SPNS1 active at neutral pH — strong evidence that this network is
the proton sensor. The TM5/TM8 lateral-entry geometry parallels the plasma-
membrane Na+-dependent LPC transporter Mfsd2a (convergent handling of
amphipathic lysolipids), reinforcing that SPNS1 is a lysosomal **proton-coupled**
exporter, not a Na+-symporter (supports keeping GO:0051978
`lysophospholipid:sodium symporter activity` as mechanistically incorrect).

**Mouse-genetic confirmation of substrate range and physiology (Ha et al. 2024,
JCI Insight, doi:10.1172/jci.insight.175462).** Spns1 knockout causes lysosomal
accumulation of LPC, LPE, lysoplasmalogens, LPG, LPI and **sphingosine** (the
sphingosine buildup rivals NPC1-deficient models), with localization to LAMP1+/
Rab7+ late endosomes-lysosomes (not Rab5+ early endosomes). Global KO is
embryonic-lethal (~E12.5–E13.5) with brain/eye defects; liver-specific KO causes
inflammation/injury accompanied by reduced Akt phosphorylation and lower ATF4.
This places SPNS1 loss upstream of PI3K/AKT–ATF4 dysregulation and broadens the
transported-cargo set beyond LPC/LPE, while noting sphingosine export remains
indirectly (not yet directly) demonstrated.

**New developmental roles.** (i) In zebrafish, endocardial lysosomal SPNS1
activity drives cardiac valve morphogenesis via **Notch1 signaling**; endocardial
re-expression of SPNS1 *or* Notch1 rescues valve defects (Chávez et al. 2024,
iScience, doi:10.1016/j.isci.2024.111406). (ii) Nervous-system–specific Spns1
loss causes **dysmyelination and white-matter dysplasia** with oligodendrocyte
loss and epilepsy (Ichimura et al. 2024, doi:10.1101/2024.05.29.596535,
preprint). These are tissue-specific developmental consequences of the lysosomal
lipid-salvage defect and are best treated as **non-core** (downstream of the core
transporter function) rather than as primary molecular-function annotations.

**Upstream/coupled lipid handling.** The report notes lysosomal PLA2G15 generates
the LPC/LPE that SPNS1 exports, exported LPC is re-acylated by ER LPCATs (Lands'
cycle), and accumulated lyso-ether-phospholipids inhibit NPC1-mediated cholesterol
egress — the mechanistic link between SPNS1 loss and the lysosomal cholesterol
accumulation reported by He et al. 2025 (PMID:40608416).

**Net effect on the review:** no change to the core molecular-function call
(proton-coupled lysosomal lysophospholipid exporter / phospholipid salvage). The
new material strengthens (a) rejection of the Na+-symporter MF, (b) the case for a
proton-coupled lysophospholipid-export NTR, and (c) the framing of the
neurodevelopmental, cardiac, and hepatic phenotypes as non-core downstream
consequences.
