# Mechanosensation evidence criteria

This guide is for the sensor layer of the Mechanobiology project. It separates
the channel's mechanically gated molecular function from the biological process
that detects a mechanical stimulus in a cell or organism.

Use it when an existing annotation, a new proposed term, or a source claim says
a gene product is mechanosensitive, mechanically activated, stretch activated,
flow sensitive, or required for touch, pressure, shear, osmotic swelling, or
compression responses.

## Terms to keep separate

### Mechanosensitive ion-channel MF

`GO:0008381` is **mechanosensitive monoatomic ion channel activity**. Its
children specify the conducted ion class, not strict selectivity: for example,
a `mechanosensitive monoatomic cation channel activity` annotation means the
channel conducts cations. It does not require a demonstration that the channel
is selective for cations over every other possible ion.

Use this molecular-function branch when the evidence shows that the gene
product is a pore-forming or pore-contributing subunit of a channel gated by
mechanical force. The strongest evidence is a force-response curve for a
current in a patch-clamp assay, plus heterologous sufficiency or a purified
protein reconstituted into a bilayer. Cell-free gating is stronger than
heterologous expression because it shows that a lipid bilayer can transmit the
force without another cellular component.

MF annotations do not by themselves say which tissue uses the channel. A Piezo
channel expressed in HEK293T cells and gated by patch pressure supports
`GO:0008381`, but it does not prove detection of touch, flow, or cartilage
compression.

### Mechanical-detection BP

`GO:0050982` is **detection of mechanical stimulus**. Its children name
specialized contexts such as detection of mechanical stimulus involved in
sensory perception of touch, sound, or pain.

Use this biological-process branch when the gene product acts at the point of
conversion from force into the first biological signal in a real sensory or
mechanotransducing cell. For a mechanotransduction ion channel, require a
chain like this:

- the gene is expressed at the force-sensing site in the relevant cell
- loss or acute inhibition of the gene reduces the mechanically evoked response
- the loss is not just a developmental loss of the cell or organ
- a mutation, knockdown, rescue, or heterologous test links the same gene to
  the measured mechanically activated current
- where the product is a channel, pore or gating mutations alter the current
  itself, or purified protein is sufficient for channel activity

In vivo knockout phenotypes can support the BP when they are tied back to the
sensory cell. They do not license the ion-channel MF unless the same or another
paper measures channel activity.

## Assay-to-annotation mapping

| Assay or perturbation | MF support | BP support | Curation rule |
| --- | --- | --- | --- |
| Pressure clamp of a cell-attached, inside-out, or whole-cilium patch | Direct support for `GO:0008381` or a child when a pressure-response curve gates a defined current and loss, mutation, or expression identifies the channel | Alone, weak; combine with cell expression and loss of the native mechanical response | Record the pressure range. A clear monotonic response in the same operating range as established mechanosensitive channels is strong. In comparable cell-attached recordings, mouse Piezo1 was half-maximal at about 28-31 mm Hg; the PKD1L1/PKD2L1 complex had no measurable increase from 0 to 60 mm Hg and only responded at 80-100 mm Hg. Activation only at extreme pressure is a caution flag, not automatic support for a core BP. |
| Whole-cell indentation or poking with a blunt probe | Strong support when expression of the candidate gives a current to naive cells or loss of the candidate removes the native current | Strong in a native sensory cell when the candidate is expressed at that site and loss removes a mechanically evoked receptor current | The stimulus reaches the channel through cell shape, membrane, cortex, and attachments, so the assay can identify a cellular mechanotransducer without proving force-from-lipids gating. |
| Deflection of a calibrated pillar, probe, cilium, neurite, or hair bundle | Usually indirect for MF unless a channel current is measured or the candidate is independently shown to be the pore | Can be strong for the BP when the deflected structure is the physiological force-sensing organelle and gene loss specifically removes the response | Distinguish direct sensors from structural components that place the sensor correctly. A bundle scaffold may be required for sound detection without being a mechanosensitive channel. |
| Laminar or oscillatory fluid shear/flow | Insufficient for MF by itself | Strong for endothelial, ciliary, or other flow-detection BPs when shear is defined and gene loss blocks the immediate response | Flow can activate channels, junctions, cilia, ATP release, GPCRs, integrins, and nitric-oxide signaling. Annotate MF only when a channel is tied to a mechanically gated conductance. |
| Hypotonic swelling or osmotic shock | Supports a mechano-osmotic or osmosensitive channel only when the paper connects the swelling response to membrane tension or channel gating | Supports detection of osmotic stimulus more directly than detection of mechanical stimulus; use a mechanical-detection term only with independent force evidence | A Ca2+ imaging response to hypotonicity is still a downstream readout unless the assayed gene is the channel or osmosensor. |
| Purified protein reconstituted into liposomes, giant proteoliposomes, droplet interface bilayers, or planar lipid bilayers | Strongest sufficiency evidence for MF if mechanical tension, osmotic stress, or bilayer deformation gates a channel and controls rule out contaminating channels | No physiological BP support by itself | A constitutively open reconstituted channel shows pore activity but not mechanosensitive gating. Require an acute mechanical stimulus or a lipid-tension manipulation for `GO:0008381`. |
| In vivo knockout or conditional knockout with a mechanosensory phenotype | No MF support by itself | Strong for BP only when expression and physiology place the gene in the sensory cell and control for development, viability, and generic excitability | Behavior alone is too distal. Pair it with skin-nerve, cilium, endothelial, or hair-cell physiology whenever possible. |

## High-threshold or nonphysiological activation

Some channels open under pressure or stretch but only after the stimulus has
left the normal working range of an established mechanotransduction assay.
Treat these as high-threshold hits:

- do **not** use high-pressure opening as the sole evidence for a core
  `detection of mechanical stimulus` BP
- do **not** call a primary-cilium or flow role mechanical when the same paper
  tested physiological pressure and found no response
- for MF, record the applied range and whether lower pressures were inactive
- when the only response is at an extreme stimulus, leave the annotation
  `UNDECIDED` or mark it over-annotated until the project settles a threshold
- rescue the claim only with independent evidence that the cell truly reaches
  that force range or that another mechanical geometry gates the channel at a
  plausible membrane tension

The policy decision that remains open is numeric. The guide should make
reviewers record pressure in mm Hg, kPa, or membrane tension when the paper
provides it, but this project still needs cmungall to decide whether there is a
hard cutoff for cell-attached pressure clamp or a relative rule keyed to each
published assay.

## Worked examples

### PIEZO1: direct pressure gating plus reconstitution

Coste et al. discovered Piezo1 by knocking down candidates in mouse Neuro2A
cells and assaying mechanically activated cation currents. Full-length mouse
Piezo1 expression was sufficient to give large whole-cell indentation-evoked
currents in N2A, HEK293T, and C2C12 cells, and cell-attached negative pressure
elicited reversible pressure-current curves in Piezo1-transfected cells. The
endogenous Neuro2A channel had a half-maximal pressure, P50, of -28.0 +/- 1.8
mm Hg, and heterologous mouse Piezo1 was almost identical: -28.1 +/- 2.8 mm Hg
in N2A cells and -31.2 +/- 3.5 mm Hg in HEK293T cells (PMID:20813920).

Coste et al. then showed that overexpressed mouse Piezo1 produced a channel
with defined pore properties, that purified Piezo1 complexes lacked another
detectable ion-channel protein, and that purified mouse Piezo1 reconstituted
into both droplet bilayers and proteoliposomes produced Ruthenium Red-sensitive
cation channel activity (PMID:22343900). That paper established pore identity,
but its reconstituted channels were largely constitutive. Syeda et al. closed
the force-from-lipids gap by showing that purified Piezo1 in droplet bilayers
is acutely activated by an osmotic gradient or by solvent injection that
expands one droplet monolayer (PMID:27829145).

Those papers support `GO:0008381` and `GO:0140135` for PIEZO1 orthologs. The
shear-flow BP requires cellular evidence: Ranade et al. showed that Piezo1 is
expressed in developing mouse endothelium, is required for vascular remodeling,
and links endothelial shear stress to stress-fiber orientation (PMID:24958852).

### PIEZO2: channel MF and touch-detection BP

Coste et al. expressed mouse Piezo2 in N2A and HEK293T cells and recorded
large, rapidly inactivating mechanically activated cation currents after
whole-cell indentation, with conductance blocked by cation replacement,
gadolinium, and Ruthenium Red (PMID:20813920). That is sufficient for a
mechanosensitive cation-channel MF.

The touch-detection BP comes from native cells and mice, not from HEK293T
expression. Woo et al. removed Piezo2 from epithelial Merkel cells: purified
Piezo2-deficient Merkel cells lost mechanically activated currents to gentle
poking, and touch-dome afferents in skin-nerve preparations had impaired
sustained firing (PMID:24717433). Ranade et al. then induced Piezo2 loss in
adult sensory neurons and Merkel cells and found loss of low-threshold
mechanosensitivity in cultured DRG neurons, A-beta afferents, and behavioral
touch assays, with thermal and high-force pain responses spared
(PMID:25471886). Together those papers support detection of low-threshold
mechanical stimuli involved in touch sensation for mouse Piezo2; human PIEZO2
can inherit that claim only through the usual orthology-aware review.

### TRPV4: osmotic and compression responses are not proof of a direct pore

The earliest TRPV4 papers identify a Ca2+-permeable cation channel activated by
hypotonicity. Liedtke et al. cloned vertebrate VR-OAC/TRPV4 orthologs and
reported that hypotonicity in the physiological range gated the channel
(PMID:11081638). Strotmann et al. independently described OTRPC4/TRPV4 as a
nonselective cation channel whose activity changed with extracellular
osmolarity (PMID:11025659). Those papers are good evidence for TRPV4 as an
osmotic or mechano-osmotic channel, but hypotonic swelling alone should not be
expanded to every mechanical-detection BP.

Suzuki et al. found that Trpv4 knockout mice had impaired tail pressure and
acidic nociception and that TRPV4 expressed in CHO cells opened after membrane
inflation as well as low pH and citrate (PMID:12692122). Alessandri-Haber et
al. placed TRPV4 in rat primary afferent nociceptors required for hypotonic
stimulus-induced nociception (PMID:12895423). O'Conor et al. showed that TRPV4
Ca2+ signaling in agarose-embedded articular chondrocytes is needed for
dynamic compression to regulate anabolic and catabolic matrix programs
(PMID:24474754). These are real mechanotransduction roles, but in reviews the
action should be tied to the exact stimulus: osmotic swelling, noxious
pressure, or chondrocyte compression. Do not infer force-from-lipids gating or
touch/sound sensory detection from the chondrocyte loading paper.

### PKD1L1-PKD2L1: an extreme-pressure caution

DeCaen et al. identified a PKD1L1/PKD2L1 heteromer as a calcium-permeant
primary-cilium channel. They also tested the complex with pressure clamp and
found no change in single-channel activity from 0 to 60 mm Hg in primary cilia
or heterologous expression; activity increased only at 80 to 100 mm Hg, and the
paper concluded that the channel lacks the sensitivity of designated
mechanosensitive channels. That is at least 2.6-fold higher than the roughly
30 mm Hg P50 of heterologous mouse Piezo1 on the same pressure scale
(PMID:20813920, PMID:24336289).

That evidence supports PKD2L1 as part of a ciliary cation channel, not as a
normal-threshold mechanosensitive channel or as a detector of physiological
mechanical stimulus. Use it as the template for high-threshold rows: quote the
pressure range, avoid a core BP unless another paper supplies physiological
mechanosensation evidence, and list any cutoff decision for cmungall rather
than deciding it ad hoc inside one gene review.

## Open questions for cmungall

- Should this project adopt a hard pressure or membrane-tension cutoff for
  `GO:0008381`, or only require comparison with positive and negative controls
  in the same assay?
- Is activation only at 80 to 100 mm Hg in a cell-attached patch ever enough
  for non-core `GO:0008381`, or should it be treated as over-threshold noise
  unless a native cell reaches an equivalent force?
- Which BP should be preferred when hypotonicity activates a channel through
  membrane stretch: `detection of osmotic stimulus`, `detection of mechanical
  stimulus`, or both only after orthogonal mechanical assays?
- Should chondrocyte, endothelial, and other non-neuronal flow/compression
  systems use the root `detection of mechanical stimulus`, or should they be
  modeled only through process-specific mechanotransduction modules until GO
  has tissue-appropriate children?
