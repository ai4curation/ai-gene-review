# CACNA2D1 (alpha-2/delta-1) review notes

## Why this gene was selected

Two separable contested claims sit on top of an uncontested core. The core is that alpha-2/delta-1 is
an auxiliary subunit of high-voltage-activated calcium channels:
[PMID:40367942 "The α2δs are a family of extracellular synaptic molecules that are auxiliary subunits
of voltage-gated Ca2+ channel (CaV) complexes."]

Neither contested claim is in GOA. That is itself worth stating: the curation exposure here is not a
bad annotation to fix but a pair of high-profile models that have *not* leaked into the annotation set,
and should not be added on current evidence.

## Claim (a): is alpha-2/delta-1 the thrombospondin receptor that drives synaptogenesis?

Original claim (Cell 2009):
[PMID:19818485 "Here, we identify the neuronal thrombospondin receptor involved in CNS synapse
formation as alpha2delta-1, the receptor for the anti-epileptic and analgesic drug gabapentin."]
with the key mechanistic detail that the requirement is **postsynaptic**:
[PMID:19818485 "alpha2delta-1 overexpression increases synaptogenesis in vitro and in vivo and is
required postsynaptically for thrombospondin- and astrocyte-induced synapse formation in vitro."]

Challenge (Neuron 2025), a presynaptic triple conditional knockout at the calyx of Held:
[PMID:40367942 "We found that mammalian synapse development, presynaptic CaV2.1 organization, and the
transsynaptic alignment of presynaptic release sites and postsynaptic glutamate receptors are
independent of presynaptic α2δs."] The authors say plainly that this contradicts the field:
[PMID:40367942 "Our findings are in contrast with current paradigms of α2δ function with respect to
synapse development and maintenance"] and offer a mechanism for the earlier results:
[PMID:40367942 "Therefore, phenotypes previously attributed to presynaptic α2δs may be due to
compensation for the loss of α2δ during axonal outgrowth."] The positive finding reassigns
alpha-2/delta to release-site organisation:
[PMID:40367942 "We identified presynaptic α2δs as positive regulators of Munc13-1 levels, an essential
neurotransmitter release protein."]

**Position taken: narrowed, not overturned.** Two reasons for restraint.

1. The 2025 experiment is **presynaptic**; the 2009 claim was **postsynaptic**. The two results are
   logically compatible. The discussion of the 2025 paper argues against transsynaptic alignment and
   CaV2 coupling models, not against a postsynaptic thrombospondin receptor:
   [PMID:40367942 "However, we found no change in AP-evoked EPSC or mEPSC kinetics between
   Cacna2d1,2,3−/− and Cacna2d1,2,3+/+ calyces, suggesting that presynaptic α2δs are not essential for
   transsynaptic alignment."]
2. It ablates **three paralogues together**, so it cannot isolate alpha-2/delta-1.
3. The astrocyte arm of the model is still in active use and support by an independent group in 2026:
   [PMID:41549518 "While astrocyte-conditioned medium (ACM) from control mice promotes excitatory
   synaptogenesis through thrombospondin-1/α2δ-1 neuronal receptor signaling, ACM from senescent SAMP8
   astrocytes lacks this capacity."]

GOA carries no synaptogenesis or thrombospondin-binding term for CACNA2D1, so **no annotation action
was needed**. The dispute is recorded in `description`, in `reference_review` on PMID:19818485
(`DISPUTED`) and in `suggested_questions`. What survives the 2025 paper and *is* annotated is the
channel-trafficking role, which that paper confirms:
[PMID:40367942 "Our data supports previous studies demonstrating that α2δs are positive regulators of
CaV2 at the plasma membrane"]

## Claim (b): a gabapentin-sensitive alpha-2/delta-1-NMDAR complex, independent of calcium channels

The model, in the proponents' own summary:
[PMID:40191897 "The α2δ-1 protein, encoded by Cacna2d1 and historically recognized as a subunit of
voltage-activated Ca2+ channels, is the primary target of gabapentinoids, such as gabapentin and
pregabalin, which are widely prescribed for neuropathic pain and epilepsy."] with the channel-independent
premise [PMID:40191897 "However, gabapentinoids have minimal effects on Ca2+ channel activity."] and the
mechanism [PMID:40191897 "This action is mediated through its dynamic physical interactions with
phosphorylated NMDARs and GluA1/GluA2 subunits via its intrinsically disordered C-terminal region."]

Applications published 2025-2026 using the same two reagents (gabapentin; an alpha-2/delta-1 C-terminal
interfering peptide):
[PMID:42225412 "Importantly, gp120-induced hyperactivity of both presynaptic and postsynaptic NMDARs
was eliminated by the α2δ-1 inhibitory ligand gabapentin or by an α2δ-1 C-terminal peptide that disrupts
α2δ-1-NMDAR interactions."] and [PMID:41006062 "These effects were abolished by silencing neuronal
activity with tetrodotoxin or in Cacna2d1 knock-out (KO) mice."]

**Provenance check.** PMID:40191897, PMID:41006062, PMID:42225412 and the further 2025-2026 papers
found in this area (PMID:40510021, Circ Res 2025; PMID:42640998, Sci Signal 2026) all come from the
**same laboratory** (Pan/Chen, Center for Neuroscience and Pain Research, MD Anderson). The nearest
out-of-house use found was [PMID:41740819 "Additionally, studies involving GBP treatment and
Cacna2d1-knockout confirmed that α2δ-1 plays a regulatory role in NR2B expression and synaptic
plasticity."] - but that is a herbal-medicine efficacy study relying on molecular docking, and one
co-author has a long publication record with the originating group. It does not count as independent
replication.

**Position taken: recorded as under-replicated, neither endorsed nor refuted.** I searched for an
explicit 2025-2026 rebuttal and found none; absence of a rebuttal is not evidence of correctness when
the model has also not been independently tested. No annotation was added for NMDAR binding or for
regulation of NMDAR trafficking. The concern is recorded in `reference_review` (PMID:40191897 marked
`UNVERIFIED` for the scientific claim, not the citation) and as a `suggested_question` with the two
experiments that would settle it.

## Curation position on the core function

**`contributes_to_molecular_function` + `in_complex`, as used for LRRC8A in this project, is the right
modelling** - and GOA already half-agrees with itself.

GO:0005245 voltage-gated calcium channel activity appears **six times** on this gene, three with
`enables` (IBA; IGI PMID:21883149; IDA PMID:1309651) and three with `contributes_to` (IEA GO_REF:0000107;
IDA PMID:17224476; IDA PMID:11160515). Alpha-2/delta-1 has no pore: the mature protein is an
extracellular alpha-2 chain disulphide-linked to a membrane-attached delta chain and GPI-anchored to the
outer leaflet. `contributes_to` is therefore correct and `enables` is not. Strikingly, the 1992 paper
cited for one of the `enables` rows says so itself:
[PMID:1309651 "Thus, the beta 2 subunit appears to serve an obligatory function, whereas the alpha 2b
subunit appears to play an accessory role that potentiates expression of the channel."]

All six rows were given the same action (`ACCEPT`, per the project's same-term-same-action rule), with
the qualifier problem recorded in `reason` and raised in `suggested_questions`. `MODIFY` would have been
wrong: the term needs no replacement, only a qualifier change, and the schema has no slot for proposing
one.

### What was added: `GO:0005246` calcium channel regulator activity (NEW)

The six GO:0005245 rows and the complex terms describe what the *complex* does and what
alpha-2/delta-1 *belongs to*. None of them states what the subunit itself contributes. GO:0005246
("Modulates the activity of a calcium channel") does, and the evidence is clean because it separates
surface density from current density in the same experiment:
[PMID:25527503 "CaVα2δ increases the peak current density and improves the voltage-dependent activation
gating of CaV1.2 channels without increasing the surface expression of the CaVα1 subunit."] Consistent
across the literature: [PMID:35293990 "They play important roles in trafficking and function of the CaV
channel complexes."] and the 2025 triple knockout's own positive result.

This is the second `core_functions` entry, and it is deliberately the one that survives both disputes.

## Other annotation-set problems found

- **`GO:0070062` extracellular exosome** (HDA x2, urinary and prostatic-secretion proteomics):
  `MARK_AS_OVER_ANNOTATED`. Plasma-membrane proteins are routinely recovered in exosome preparations.
- **`GO:0016529` sarcoplasmic reticulum** (IEA from mouse): alpha-2/delta-1 is a T-tubule
  plasma-membrane protein; the SR call most likely reflects triad co-purification. `KEEP_AS_NON_CORE`
  rather than `REMOVE`, because the mouse source is an experimental curator call not read here.
- **`GO:0098992` neuronal dense core vesicle, `is_active_in`** (IEA from mouse): a GPI-anchored
  extracellular subunit of a surface channel being *active in* a secretory vesicle is hard to
  interpret. Flagged, kept non-core.
- **`GO:1904646` cellular response to amyloid-beta** (IGI PMID:21883149): the measurement is an applied
  synthetic Abeta globulomer shifting activation of a reconstituted P/Q-type channel in *Xenopus*
  oocytes. Real, but a pharmacological effect on a heterologously expressed complex, not a cellular
  response programme. `KEEP_AS_NON_CORE`.
- **Over-general transport terms**: `GO:0006816` calcium ion transport (x2) and `GO:0060402` calcium ion
  transport into cytosol `MODIFY` to `GO:0098703` calcium ion import across plasma membrane;
  `GO:0051924` regulation of calcium ion transport `MODIFY` to `GO:1902514`. All targets are terms the
  gene already carries.
- **Cardiac cell-type-qualified MF terms** (`GO:0086007`, `GO:0086057`): `KEEP_AS_NON_CORE`. These are
  the same molecular function restated per tissue; alpha-2/delta-1 does not have a bundle-of-His-specific
  activity.

## PMID verification

Every PMID was checked against PubMed metadata before citing. One initial guess for the Eroglu 2009
thrombospondin paper (19797056) turned out to be a D-AKAP2/Rab11 paper and was discarded; the correct
PMID is **19818485**.
