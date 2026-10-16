# TMEM120A (TACAN / NET29 / TMPIT) — review journal

UniProt: Q9BXJ8. HGNC: TMEM120A. Paralog: TMEM120B (Q9BXJ9).
Reviewed 2026-09.

## Why this gene is on the "contested function" list

TMEM120A carries two mutually incompatible stories in the literature, and GOA carries
both of them at once. The review has to adjudicate which one the annotations should
reflect.

**Story A (2020-2021, "TACAN"):** a plasma-membrane mechanosensitive ion channel in
nociceptors. [PMID:32084332 "Here we report identification of TACAN (Tmem120A), an ion
channel involved in sensing mechanical pain."] and [PMID:32084332 "Finally, a
nociceptor-specific inducible knockout of TACAN decreases the mechanosensitivity of
nociceptors and reduces behavioral responses to painful mechanical stimuli but not to
thermal or touch stimuli."]

**Story B (2021-2026):** an ER membrane protein that binds coenzyme A and works in
glycerolipid synthesis.

## Story A did not survive replication (2021)

Four independent structural/electrophysiology groups published within weeks of each other
in 2021 and none could reproduce the channel activity:

- [PMID:34374645 "However, we were unable to reproduce the mechanosensitive activity of
  TMEM120A expressed in HEK293 or CHO cells, nor did we observe any mechanosensitive
  channel activity in giant liposome patching using TMEM120A protein reconstituted into
  lipid vesicles."] and [PMID:34374645 "While we are unable to define the physiological
  function of TMEM120A in this study, its structural similarity to ELOVL7 leads us to
  suspect that TMEM120A may function as an enzyme for lipid metabolism rather than an ion
  channel."]
- [PMID:34409941 "Thus, under our experimental conditions with the use of Piezo channels
  and HsTMEM63a as proper positive controls, we conclude that TMEM120A is not sufficient
  to mediate poking- or stretch-induced currents in P1-KO-HEK cells."]
- [PMID:34465718 "We even cannot conclude TMEM120A is an ion channel as conducting
  currents were also measured for several non-channel proteins in the bilayer system8."]
- [PMID:34374644 "Using cellular patch-recording methods, we failed to identify
  mechanosensitive ion channel activity."] and [PMID:34374644 "Whilst its physiological
  function remains unclear, we anticipate that TACAN is not a mechanosensitive ion
  channel."]

All four instead found a coenzyme A molecule bound in a deep cavity of the
six-transmembrane barrel, and a fold homologous to the fatty-acid elongase ELOVL7:
[PMID:34374645 "Instead, the six TMs form an α-barrel with a deep pocket where a coenzyme
A (CoA) molecule is bound."], [PMID:34409941 "Within the transmembrane domain, a CoASH
molecule is hosted in a deep cavity and forms specific interactions with nearby amino acid
residues."], [PMID:34409941 "Mutation of a central tryptophan residue involved in binding
CoASH dramatically reduced the binding affinity of HsTMEM120A with CoASH."]

**GO has already ruled on this.** In `TMEM120A-goa.tsv` the QUALIFIER column shows
`GO:0005216 monoatomic ion channel activity` three times, and every one is `NOT|enables`:
IMP/PMID:34374645, IDA/PMID:34409941, IDA/PMID:34465718. These are negative assertions —
GO is stating that TMEM120A does *not* enable ion channel activity.

## The stray positive ISS

One row contradicts the three negatives on the same term in the same protein:

```
UniProtKB Q9BXJ8 TMEM120A enables GO:0005216 ... ECO:0000250 ISS GO_REF:0000024 UniProtKB:Q8C1E7 ... 20200311
```

Provenance traced: the source is mouse Q8C1E7, whose QuickGO record carries
`enables GO:0005216` from **PMID:32084332** — i.e. the original Beaulieu-Laroche TACAN
paper. The transfer is dated **2020-03-11**, three weeks after that paper and more than a
year before the 2021 refutations. It is a stale orthology projection of the very claim
that the three later human experimental annotations negate. Removing it is not
second-guessing an experimentalist: it is retiring a curator-judgment sequence-similarity
transfer whose donor evidence has been superseded on the same protein. Action: `REMOVE`.
The three negated rows are `ACCEPT`ed — negated and non-negated annotations of one term
are opposite assertions, so they legitimately take different actions.

The same 2020-03-11 GO_REF:0000024 block also projected `GO:0034220 monoatomic ion
transmembrane transport`, `GO:0050966 detection of mechanical stimulus involved in sensory
perception of pain` and `GO:0005886 plasma membrane` from the same mouse paper, and
GO_REF:0000107 (Ensembl Compara) later duplicated the first two. Those are handled as a
block.

## Story B: what TMEM120A actually appears to do

**It is an ER protein.** [PMID:41423633 "Our findings clarify this ambiguity by
demonstrating that in adipocytes, TMEM120A is localized to the ER rather than the nuclear
envelope, where it functions not as an ion channel or fatty acid elongase, but as a
CoA-binding protein that facilitates lipid metabolic flux."] Independently, with endogenous
tagging in *C. elegans*: [PMID:42098142 "Taken together, our results firmly suggest that
TMEM-120 is an ER-resident protein, with its N- and C-termini both oriented towards the
cytoplasm."]

**It partners acyl-CoA synthetases.** [PMID:41423633 "TMEM120A interacts with the
ER-localized acyl-CoA synthetase ACSL1 and ACSL3 to promote long-chain acyl-CoA synthesis
and channeling into the ER, thereby facilitating FA re-esterification and lipid cycling
during lipolysis."] The interaction depends on the CoA pocket:
[PMID:41423633 "Interestingly, TMEM120AW193A mutant displayed markedly reduced interaction
with ACSL1 and ACSL3, implying that CoA binding is required for the TMEM120A-ACSL1/3
interactions (Fig."]

**It activates GPAT4.** [PMID:42098142 "Here, we have used genetic, biochemical, and
imaging techniques to identify TMEM120A as GPAT4-activating protein."] and
[PMID:42098142 "We show that ER-localized TMEM120A and CHP1 synergistically activate GPAT4
and promote the incorporation of medium and long chain acyl-CoA into glycerolipid."] The
activation is measured directly in vitro: [PMID:42098142 "We reproduced the observation
that CHP1 enhanced GPAT4 activity23, and so did TMEM120A (Fig."] and
[PMID:42098142 "Taken together, our results indicate that TMEM120A and CHP1 act
synergistically to enhance GPAT4 activity."] It is not itself the acyltransferase — CHP1
was previously "the only known GPAT4 activator" [PMID:42098142 "The lipid-modified,
myristoylated form of calcineurin B homologous protein (CHP) 1 is the only known GPAT4
activator thus far23."] — and the phenotype is conserved to worm
[PMID:42098142 "C. elegans mutants of TMEM120A or CHP1 ortholog are susceptible to
high-fat diet induced sterility, in part due to their deficiency in lipid droplet
expansion."]

**It is not an elongase.** Despite the ELOVL7-like fold, the pocket cannot hold an acyl
chain: [PMID:41423633 "As previously noted20, although TMEM120A contains a CoA-binding
site, it lacks a defined hydrophobic pocket capable of accommodating long-chain fatty acyl
chain."] So the right MF altitude is *not* a catalytic term.

## The reconciliation that makes the pain data make sense

TMEM120A modulates mechanotransduction without being a mechanosensor, by changing membrane
lipid composition:

- [PMID:35819364 "Here, we find that Tmem120a coexpression decreased the amplitudes of
  mechanically activated PIEZO2 currents and increased their threshold of activation."] and
  [PMID:35819364 "Our data identify TMEM120A as a negative modulator of PIEZO2 channel
  activity, and do not support TMEM120A being a mechanically activated ion channel."]
- The mediator was then identified as a glycerolipid:
  [PMID:39147733 "Here we find that TMEM120A expression elevates cellular levels of
  phosphatidic acid and lysophosphatidic acid (LPA), aligning with its structural
  resemblance to lipid-modifying enzymes."] and [PMID:39147733 "Intracellular application
  of phosphatidic acid or LPA inhibits PIEZO2 but not PIEZO1 activity."]

LPA is precisely the product of the GPAT4 reaction that TMEM120A activates
[PMID:42098142 "NBD- palmitoyl-CoA was used as the substrate to measure GPAT4 activity,
based on the detection of fluorescent NBD-labeled lysophosphatidic acid (LPA), which is
the product of the GPAT4 reaction (Fig."]. So: TMEM120A → GPAT4 activation → LPA/PA →
PIEZO2 inhibition. That is a coherent, lipid-metabolic explanation for why manipulating
TMEM120A in sensory neurons changes mechanical sensitivity, with no channel required.

Caveat recorded honestly: the sign does not obviously line up. Beaulieu-Laroche found KO
*reduces* mechanical pain; Del Rosario found knockdown *increases* PIEZO2 currents and
lowers thresholds. Both cannot be the whole story. This goes into `suggested_questions`.

## The channel framing has not gone away in 2026

- A 2026 review still lists TMEM120A among pain-transducing channels:
  [PMID:41967766 "Key TMEM family members, including TMEM100, TMEM16A/F, TMEM175, TMEM97,
  TMEM120A/TACAN, and TMEM233, orchestrate pain transmission by modulating ion channels,
  inflammatory mediators, and intracellular signaling cascades across peripheral and
  central pathways."] Note the wording is "modulating ion channels" — which is actually
  compatible with the PIEZO2/lipid model, not with TMEM120A being the channel.
- A 2026 methods paper assays TMEM120A M207A against the mechanosensitive-channel
  gating-modifier peptide GsMTx4: [PMID:42184262 "As a model system, the gating-modifier
  peptide Grammostola mechanotoxin 4 (GsMTx4) was tested against the multifunctional
  membrane protein mutant TMEM120A M207A."] This is a *biolayer interferometry binding*
  protocol paper — it demonstrates a protocol, not channel gating, and the authors
  themselves call TMEM120A "multifunctional" rather than a channel. It is not evidence for
  channel activity.

Neither is grounds to reinstate `enables GO:0005216` against three experimental negatives.

## Other annotated roles

- **Nuclear envelope / inner nuclear membrane.** Original assignment as NET29:
  [PMID:26024229 "Here we present two nuclear envelope trans-membrane proteins TMEM120A and
  TMEM120B that are paralogs encoded by the Tmem120A and Tmem120B genes."] Supported by the
  adipocyte-specific KO genome-organisation phenotype [PMID:35027552 "Here we report that
  adipocyte-specific knockout of the gene encoding nuclear envelope transmembrane protein
  Tmem120a disrupts fat genome organisation, thus causing a lipodystrophy syndrome."]. But
  the 2025/2026 papers explicitly dispute the compartment
  [PMID:42098142 "Intriguingly, a consensus has yet to emerge regarding the subcellular
  localization of TMEM120A."]. Kept as non-core rather than removed — the INM claim rests on
  real experiments and INM is continuous with the ER.
- **Adipocyte differentiation.** [PMID:26024229 "Accordingly, TMEM120A and B knockdown
  individually and together impacted on adipocyte differentiation/metabolism as measured by
  lipid accumulation through binding of Oil Red O and coherent anti-Stokes Raman scattering
  microscopy (CARS)."] Real, but downstream of lipid handling — non-core.
- **Antiviral / STING.** [PMID:35013224 "Mechanistically, the antiviral activity of
  TMEM120A is dependent on STING, as TMEM120A interacts with STING, promotes the
  translocation of STING from the endoplasmic reticulum (ER) to ER-Golgi intermediate
  compartment (ERGIC) and enhances the phosphorylation of downstream TBK1 and IRF3,
  resulting in the expression of multiple antiviral cytokines and interferon-stimulated
  genes."] A single-lab gain-of-function screen result; an ER-membrane protein affecting ER
  export of another ER protein is mechanistically plausible. Non-core.
- **Homodimer.** Every structure agrees: [PMID:34374644 "TACAN is an α-helical TM protein
  that forms a symmetric dimer (Figure 3A)."] Core architecture — accepted.
  Heterooligomerization with TMEM120B rests on the 2015 co-IP only; kept non-core.
- **PKD2.** [PMID:36420836] is abstract-only in the cache; UniProt records that TMEM120A
  inhibits PKD2 channel activity through physical association. Captured only as the IPI
  protein-binding row.

## MF altitude decision

`GO:0120225 coenzyme A binding` is directly demonstrated (cryo-EM density, CoA assay kit,
native MS, W193/W193A loss-of-binding) and is mechanistically load-bearing rather than
incidental — W193A abolishes both the ACSL1/3 interaction and, in worm, function
[PMID:42098142 "Therefore, we conclude that the G195E mutation most likely attenuates
TMEM-120 function by interfering with CoASH binding, as predicted by the TMEM120A
structure."]. So it is kept as a core MF, not modified away.

But CoA binding alone does not say what the protein *does* with the CoA. The 2026 result is
an explicit enzyme-activation activity. GO has `GO:0008047 enzyme activator activity`
(checked via QuickGO: "A molecular function regulator that increases a catalytic activity")
and has precedent for acyltransferase-specific children, e.g.
`GO:0060228 phosphatidylcholine-sterol O-acyltransferase activator activity`. There is **no**
`glycerol-3-phosphate O-acyltransferase activator activity` term (QuickGO search returns
none), so one is proposed, with `GO:0008047` used as the core-function MF in the interim.

Deliberately **not** proposed: a CoA transmembrane transporter term. The authors hedge
their own mechanism [PMID:41423633 "By contributing to ER CoA availability, possibly
through recycling CoA in ER, TMEM120A may facilitate LC-acyl-CoA formation and support FA
re-esterification in the ER, thereby helping to maintain intracellular lipid
homeostasis."] — "channeling" in their title is metabolic channelling, not demonstrated
transport. Asserting a transporter term would repeat exactly the error that produced the
TACAN channel annotation.

## Validation note

The same-term-consistency rule does not model negation. For `GO:0005216` the three
`ACCEPT`ed negated rows are anchored to PMIDs and the single `REMOVE`d positive row is
anchored to GO_REF:0000024; because the REMOVE reference is disjoint from every kept
reference and all kept rows share one action, the validator's citation-specific-rejection
exemption applies and no inconsistency warning is raised.
