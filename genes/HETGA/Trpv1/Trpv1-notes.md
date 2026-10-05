# Trpv1 (naked mole rat, *Heterocephalus glaber*) — research notes

UniProt **G9DCX1** (TrEMBL, unreviewed), 840 aa, `PE 2: Evidence at transcript level`.
Gene name from EMBL `AEV53346.1` / mRNA `JF912492`, submitted with
[PMID:22174253 "The molecular basis of acid insensitivity in the African naked mole-rat."].
So this accession *is* the cDNA that Smith et al. cloned and characterised — the
protein in this entry is the one the electrophysiology below was done on. That matters:
unlike most naked-mole-rat GOA entries, the annotations here can be tied to a specific
characterised protein rather than to a genome-pipeline gene model.

## Headline conclusion

**The naked mole-rat TRPV1 channel is not the adaptation.** It is an ordinary,
polymodal, capsaicin/heat/proton-gated, Ca²⁺-permeable cation channel. The famous
capsaicin insensitivity of this species is a *circuit and neuropeptide* phenotype,
not a channel phenotype. The correct curation outcome for most of the eight seeded
annotations is therefore "the ortholog projection holds, and naked-mole-rat evidence
positively confirms it" — which is a stronger position than the usual HETGA case,
where projections can only be left unchallenged.

## What the naked-mole-rat literature establishes about this protein

### 1. It is capsaicin-gated, at normal (nanomolar) potency

Park et al. set out expecting a broken channel and found the opposite:

- [PMID:18232734 "We speculated that the reduced pain behavior in the naked mole-rat
  could simply be explained by a lack of functional TRPV1 ion channels."]
- [PMID:18232734 "In contrast, nociceptors do respond vigorously to capsaicin, and we
  also show that sensory neurons express a transient receptor potential vanilloid
  channel-1 ion channel that is capsaicin sensitive."]
- Fura-2 Ca²⁺ imaging on cultured naked-mole-rat DRG neurons
  [PMID:18232734 "We thus used cultures of naked mole-rat DRG neurons and applied low
  concentrations of capsaicin onto single cells and measured receptor activation using
  fura-2"], with the result
  [PMID:18232734 "The results of these experiments indicated that the incidence and
  magnitude of the capsaicin responses to both low (10 nM) and high (2 μM) capsaicin
  concentrations are equivalent to that found in the mouse"] and
  [PMID:18232734 "No significant differences were observed in the proportion of
  capsaicin-sensitive neurons between mouse and naked mole-rat."]

Independently reproduced in whole-cell voltage clamp fifteen years later:
[PMID:40705105 "In the same recordings, TRPV1 function was assessed in voltage clamp
configuration by applying 1 µM capsaicin"], and in Ca²⁺ imaging of NMR DRG neurons
[PMID:20497578 "10% (n = 35/343) were activated by 1 μM capsaicin"].

Skin-nerve recordings give the same answer at the fibre level
[PMID:32206859 "Capsaicin robustly activates naked mole-rat polymodal C-fibers as
determined by direct electrophysiological recordings"].

### 2. It is heat-gated, with a normal threshold (~44 °C)

The decisive experiment is heterologous expression of the cloned naked-mole-rat cDNA
in sensory neurons from *Trpv1*-null mice — i.e. the channel tested in isolation from
naked-mole-rat cellular context:

- [PMID:27732851 "Transfected Trpv1−/− sensory neurons had heat-gated currents with an
  activation threshold of 44.4°C ± 0.7°C (n = 5) and pH-gated currents sensitive to
  ruthenium red"]
- [PMID:27732851 "the naked mole-rat TRPV1 protein can rescue capsaicin and heat
  sensitivity in Trpv1−/− sensory neurons"]

Summarised by the same group as
[PMID:27732851 "The cloned naked mole-rat TRPV1 receptor (nmrTrpv1) displays biophysical
properties similar to its mouse counterpart with respect to proton, capsaicin, and heat
gating"] and
[PMID:32206859 "Indeed, subsequent analysis of naked mole-rat TRPV1 demonstrated that it
has normal heat, pH, voltage and capsaicin sensitivity"].

At the organism level the naked mole rat's *heat* nocifension is normal — this is
explicitly one of the corrections in the "myths" paper:
[PMID:34476892 "Normal nocifensive responses were reported for noxious heat and
mechanical stimuli."] and
[PMID:34476892 "Naked mole‐rats do respond to certain noxious stimuli (e.g. heat and
mustard oil), but lack responses to others, such as acid and capsaicin."]
Consistent with peripheral fibre physiology: [PMID:18232734 "We found that 57% of single
C-fibers (17/30 fibers) responded to heat and these were classified as CMH."]

**Heat and cold are separate claims and separate answers.** Cold is where the naked mole
rat genuinely differs, and that difference is not a TRPV1 matter: the cold paper reports
TRPM8/TRPA1 mRNA differences while explicitly noting TRPV1 transcript levels are the same
as mouse [PMID:32880221 "We also probed for TRPV1 mRNA transcripts as a further TRP
channel comparison and found that the average number of punctae per cell was similar
between the species"]. Nothing in the naked-mole-rat literature supports a cold-sensing
role for TRPV1, and I proposed no cold/cool term.

### 3. It is proton-gated, at normal proton sensitivity

This one is a genuinely informative negative, because the species *is* acid-insensitive —
just not through TRPV1:

- [PMID:22174253 "acid sensors (acid-sensing ion channels and the transient receptor
  potential vanilloid-1 ion channel) in naked mole-rat nociceptors are similar to those
  in other vertebrates"] (abstract-only cache; the quote is from the abstract)
- [PMID:32206859 "When examining the proton sensitivity of cloned acid-sensitive proteins,
  naked mole-rat TRPV1, ASIC1a and ASIC1b have a similar proton sensitivity to their
  mouse orthologues"]
- [PMID:31992138 "NMR TRPV1 is also expressed in sensory afferents and shows similar
  proton sensitivity to mouse TRPV1"]

Acid insensitivity is a Na_V1.7 story (a proton-block variant of *Scn9a*), not a TRPV1
story.

### 4. Expression: normal levels, normal fraction of DRG neurons, peripheral and central terminals

- [PMID:32880221 "the TRPV1 receptor is expressed at normal levels in DRG and functions
  despite a lack of behavioral response to capsaicin"]
- Quantified by immunohistochemistry: in NMR, 27.60 ± 2.29 % of DRG neurons express TRPV1
  vs 26.00 ± 1.92 % in mouse [PMID:40705105 "In summary, employing in vitro methods, we
  observed that artemin sensitizes both the intrinsic electrical properties of mouse and
  NMR DRG sensory neurons as well as sensitivity to capsaicin"] (the percentages are in
  the same paper's Fig. 1 legend/results text).
- Central terminals: TRPV1-immunoreactive fibres and varicosities are present in the
  dorsal horn and are synaptically functional
  [PMID:18232734 "Thus, TRPV1-responsive sensory fibers are synaptically connected to both
  superficial and deep dorsal horn neurons in the naked mole-rat."]

### 5. Why the animal does not feel capsaicin — and why that is *not* a TRPV1 defect

Two downstream explanations, both well supported, neither implicating the channel:

- Altered central wiring:
  [PMID:32206859 "This altered connectivity of TRPV1-positive nociceptors potentially
  explains why capsaicin elicits a robust nocifensive response in mice, but none in the
  naked mole-rat."] and
  [PMID:40705105 "capsaicin insensitivity occurs due to altered spinal cord sensory neuron
  wiring, rather than an alteration in primary afferent neuron activity"]
- Absent neuropeptides in cutaneous C-fibres:
  [PMID:32478202 "Experiments involving immunohistochemistry and intrathecal administration
  of SP showed that the behavioral insensitivity to capsaicin is attributable to a lack of
  neuropeptides in C-fibers of the naked mole-rat"]

Similarly, the *absence of capsaicin- and NGF-induced thermal hyperalgesia*
[PMID:21200438 "Capsaicin sensitizes heat-evoked foot withdrawal to heat in mice, but not
naked mole-rats."] is a TrkA defect, not a TRPV1 defect:
[PMID:27732851 "The sensitization of capsaicin-sensitive TRPV1 ion channels is necessary
for NGF-induced hyperalgesia, but naked mole-rats have fully functional TRPV1 channels."],
[PMID:27732851 "in naked mole-rat IB4-negative sensory neurons, NGF never sensitized TRPV1
currents"], but
[PMID:27732851 "they have sensory neurons that express a TRPV1 channel with ligand
sensitivity and biophysical properties indistinguishable from that found in mice or
humans"].

Note that sensitisation of the naked-mole-rat channel is *not* globally lost — artemin
(GFRα3 ligand) does sensitise it:
[PMID:40705105 "In summary, employing in vitro methods, we observed that artemin sensitizes
both the intrinsic electrical properties of mouse and NMR DRG sensory neurons as well as
sensitivity to capsaicin"]. The deficit is specific to the NGF/TrkA arm.

### 6. The one documented naked-mole-rat-specific substitution — and it is functionally silent

[PMID:27732851 "was substituted by a threonine in the naked mole-rat protein"] — the full
sentence identifies the position as Ser502 in rat TRPV1 numbering, a PKCε phospho-acceptor.
The same paper tests it and finds it makes no difference:
[PMID:27732851 "To measure PKCε sensitization of nmrTRPV1, we used a new naked mole-rat
fibroblast cell line"] and
[PMID:27732851 "We also generated a naked mole-rat TRPV1T502S mutant that was also sensitized
by PMA in naked mole-rat fibroblast cell lines"].

I checked the position directly against the two sequences rather than trusting the numbering:

```
rat  O35433 (838 aa)  ...FRGIQYFLQRRP S(502) LKSLFVDSYSEIL...
NMR  G9DCX1 (840 aa)  ...FRGIQYFLQRRP T(505) MKTLFVDSYSEIL...
```

Reproduce with:
```
curl -s https://rest.uniprot.org/uniprotkb/O35433.fasta   # rat, find QRRPS -> S at 502
grep -A20 '^SQ   SEQUENCE' genes/HETGA/Trpv1/Trpv1-uniprot.txt  # NMR, find QRRPT -> T at 505
```
Identical flanking context `QRRP[S/T]`, so the alignment is unambiguous: **NMR Thr505 = rat
Ser502**. This is a real, verifiable, species-specific difference — and, per the experiment
above, one with no functional consequence for sensitisation. It is therefore not a reason
to weaken any annotation. I record it because "TRPV1 must be the adaptation" is exactly the
kind of story a curator is tempted to build out of a single substitution.

## Curation decisions and their basis

| GO term | source | action | why |
|---|---|---|---|
| GO:0005216 monoatomic ion channel activity | InterPro2GO+PANTHER (GO_REF:0000120) | MODIFY | true but uninformative; the naked-mole-rat channel's gating is directly characterised, so the specific parents are available |
| GO:0005262 calcium channel activity | ARBA+PANTHER (GO_REF:0000120) | ACCEPT | Ca²⁺ influx measured directly in NMR DRG neurons and in NMR fibroblasts expressing nmrTRPV1 |
| GO:0005886 plasma membrane | ARBA+PANTHER (GO_REF:0000120) | ACCEPT | whole-cell surface currents and surface Ca²⁺ influx in NMR neurons |
| GO:0006811 monoatomic ion transport | InterPro2GO | ACCEPT | correct, general |
| GO:0016020 membrane | InterPro2GO | ACCEPT | correct, general; redundant with GO:0005886 |
| GO:0032591 dendritic spine membrane | UniProt SubCell SL-0285 (GO_REF:0000044) | MARK_AS_OVER_ANNOTATED | see below |
| GO:0055085 transmembrane transport | InterPro2GO | ACCEPT | correct, general |
| GO:0098703 calcium ion import across plasma membrane | TreeGrafter PTN000061681 (GO_REF:0000118) | ACCEPT | core; directly measured |

### The dendritic-spine call, in full

`GO:0032591 dendritic spine membrane` is the only annotation I downgraded. The argument is
positive, not merely "it was transferred electronically":

1. Its provenance is a UniProt subcellular-location **keyword** (`SL-0285`), reached via
   `ARBA00004332`; the UniProt record carries it as
   `SUBCELLULAR LOCATION: Cell projection, dendritic spine membrane` with an ARBA evidence
   tag only (verifiable in `Trpv1-uniprot.txt`). It is not derived from any naked-mole-rat
   observation.
2. It is **IEA in every well-curated ortholog**. I pulled the full QuickGO annotation sets
   for human `Q8NER1`, mouse `Q704Y3` and rat `O35433`: all three carry `GO:0032591` with
   evidence `IEA` and nothing else, while the neighbouring, genuinely experimental CNS
   locations on those orthologs are the *postsynaptic membrane* (`GO:0045211`, IDA/IMP in
   mouse and rat) and *dendrite* (`GO:0030425`, IDA in rat). So the spine-specific term is
   an unvalidated keyword artefact even in the source species, and what propagates to the
   naked mole rat is that artefact, not the underlying experimental finding.
3. Every naked-mole-rat observation of this protein is in **peripheral sensory neurons** —
   DRG somata, cutaneous C-fibre terminals, dorsal-horn central terminals. No naked-mole-rat
   study has looked at TRPV1 in brain, let alone at dendritic spines.

I did not use `REMOVE`: TRPV1 does have real postsynaptic/dendritic localisation in rodent
CNS, so the term is not false in the family, merely unsupported and over-specific for this
species. `MARK_AS_OVER_ANNOTATED` is the calibrated call.

### On the pain terms — deliberately not proposed

The seeded set contains **no** capsaicin/vanilloid-binding term and **no** pain-perception
term, and I did not add one.

- There is no GO term for vanilloid/capsaicin binding or "capsaicin receptor activity";
  `GO:0015276 ligand-gated monoatomic ion channel activity` is the closest existing term and
  is what I proposed. I logged the gap in `proposed_new_terms` rather than forcing an
  existing term to carry the meaning.
- For pain: the ortholog term `GO:0050965 detection of temperature stimulus involved in
  sensory perception of pain` is curated on mouse (IGI/IMP) and human (IEA). Transferring it
  to the naked mole rat would be exactly the trap this gene sets. Naked-mole-rat TRPV1
  activation demonstrably **does not** produce nocifensive behaviour, and while noxious-heat
  nocifension is normal in this species, nobody has shown that naked-mole-rat TRPV1 mediates
  it (in mice, C-fibre noxious-heat sensitivity survives *Trpv1* deletion —
  [PMID:18232734 "Heat sensitivity is not necessarily inseparable from capsaicin sensitivity,
  because C-fibers in TRPV1-null mutant mice apparently have normal noxious heat sensitivity
  but are capsaicin insensitive [65]."]). I put this in `suggested_questions` and
  `suggested_experiments` instead of asserting it.

## New annotations proposed (all naked-mole-rat-grounded)

| term | grounding |
|---|---|
| GO:0034605 cellular response to heat | heat-gated currents from nmrTRPV1, threshold 44.4 °C [PMID:27732851] |
| GO:0071468 cellular response to acidic pH | pH-gated, ruthenium-red-sensitive currents [PMID:27732851]; normal proton sensitivity [PMID:32206859, PMID:22174253] |
| GO:0071312 cellular response to alkaloid | capsaicin (an alkaloid) evokes Ca²⁺ influx and inward currents in NMR neurons [PMID:18232734, PMID:40705105] |

The MF replacements proposed on `GO:0005216` — `GO:0097603 temperature-gated ion channel
activity` and `GO:0015276 ligand-gated monoatomic ion channel activity` — are not repeated as
separate `NEW` rows, per the reviewer instructions.

## What the affinage human-ortholog record contributed, and what it missed

`Trpv1-deep-research-affinage-human-ortholog.md` is the Affinage record for **human TRPV1
(Q8NER1)**, supplied as a conserved-mechanism baseline. It is genuinely good on conserved
mechanism: cryo-EM gating trajectory, the capsaicin "tail-up, head-down" pose and
pull-and-contact with the S4–S5 linker, PIP₂ as a positive cofactor, PKA/AKAP150 and
PKC-S801 sensitisation, TRPV1::TRPA1 and TRPV1::TRPV4 heteromers, the MOR1/GRK5 non-channel
role. None of that is naked-mole-rat evidence and none of it is cited as such here.

What it **missed**, which is the whole substance of this review:

1. **Everything about this species.** Not one of its 22 citations is a naked-mole-rat paper.
   That is by construction (it is a human record), but it means the record is silent on the
   single most important curation question for G9DCX1 — whether the ortholog projection holds.
2. **The Ser→Thr substitution at the PKCε site**, and the fact that it is functionally silent.
   Its PKC section names S801 and T704/S502 as sensitisation sites but has no way to know
   that the naked-mole-rat protein carries Thr at the 502-equivalent position, nor that this
   was tested and found equivalent [PMID:27732851].
3. **The TrkA-not-TRPV1 dissociation** — that failure of NGF-induced sensitisation in a whole
   animal can sit entirely upstream of a normal channel. Its NGF entry (PI3K p85β trafficking,
   PMID:17074976) frames NGF sensitisation as a TRPV1-side mechanism, which is the natural but
   wrong inference to carry into this species.

I did **not** import its `mechanism_profile` GO ids (`GO:0005215`, `GO:0060089`,
`GO:0008289`, `GO:0140299`): they are coarse parents and, for the sensor/transducer terms,
not what a curator would assert for a channel with directly measured gating. Every term in
this review was grounded independently.

## Unresolved / left open

- **No naked-mole-rat data on TRPV1 outside the somatosensory system.** Brain, bladder, gut
  epithelium, vasculature — all of the organ-physiology roles that mouse and rat TRPV1 carry
  (GO:0001659 temperature homeostasis, GO:0035810 positive regulation of urine volume,
  GO:0003085 negative regulation of systemic arterial blood pressure, etc.) are untested here.
  I did not project any of them; they are the classic weak-transfer class this species is
  worst suited to.
- **Heteromerisation and the interactome.** No naked-mole-rat data on TRPV1::TRPA1 or
  TRPV1::TRPV4 assembly, calmodulin binding, ATP binding or PIP₂ binding. UniProt carries
  `ATP binding`, `calmodulin binding` and `metal ion binding` on its own DR/keyword lines for
  G9DCX1, but GOA has retired those keyword-derived rows, so none appear in the eight seeded
  annotations and I did not add them: they are keyword transfers with no naked-mole-rat
  evidence.
- **Voltage sensitivity** is asserted normal in the review literature
  [PMID:32206859 "Indeed, subsequent analysis of naked mole-rat TRPV1 demonstrated that it has
  normal heat, pH, voltage and capsaicin sensitivity"], but the primary paper
  (PMID:22174253) is abstract-only in the cache, so I could not read the voltage-clamp
  protocols myself; I did not annotate a voltage-gating term on that basis.
