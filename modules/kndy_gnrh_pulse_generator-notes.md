# KNDy GnRH pulse generator module — curation notes

`modules/kndy_gnrh_pulse_generator.yaml` (`MODULE:kndy_gnrh_pulse_generator`), status DRAFT,
scope CONCRETE, five root parts.

## What the module covers

The arcuate (infundibular) KNDy neuron oscillator and its output synapse on GnRH neurons:

| Part | Step | Annotons (MF) |
|---|---|---|
| 1 | Estradiol negative feedback onto KNDy neurons | ESR1 (`GO:0030284`), plus `module_ref: estrogen_receptor_signaling` for the generic receptor relay |
| 2 | Autosynaptic neurokinin B excitation and burst synchronisation | NKB precursors (`GO:0048018`), NK3R (`GO:0016498`), Gq/11 alpha (`GO:0003925`) |
| 3 | Dynorphin self-inhibition terminating the burst | prodynorphin (`GO:0001515`), KOR (`GO:0038048`) |
| 4 | Kisspeptin output onto the GnRH neuron | kisspeptin precursors (`GO:0048018`) in a two-route variant set; then KISS1R (`GO:0008188`), Gq/11 alpha (`GO:0003925`), TRPC channel (`GO:0005261`) |
| 5 | Pulsatile GnRH release | GnRH (`GO:0005183`) |

Molecular functions sit on the annotons; the process and context terms (`GO:0033686`,
`GO:0032278`, `GO:0030520`, `GO:0007209`, `GO:0007200`, `GO:0038003`, `GO:0051899`,
`GO:0000122`, `CL:4023125`, `CL:0011111`, `CL:0020073`, `UBERON:0001932`, `UBERON:0002197`,
`NCBITaxon:40674`) sit on module nodes, variants and context.

## Boundary decisions

- **Pituitary GnRHR signalling and gonadotropin secretion: out of scope.** They are downstream
  of part 5, in a different cell type, and already partly covered here by `genes/human/CGA`,
  `genes/human/FSHR` and the FSH GO-CAM reviews `gocams/59dc728000000351` and
  `gocams/69b3372b00003343`. A gonadotrope module should carry them. GNRHR (`UniProtKB:P30968`)
  is named only as the target of the GnRH annoton's hormone activity, which is how the module
  states where its output goes without modelling the response.
- **The median preoptic (MnPO) thermoregulatory output: out of scope.** The same KNDy neurons
  project to glutamatergic NK3R neurons of the median preoptic nucleus and engage heat-loss
  effectors; that is the hot-flush mechanism and the target of the NK3R antagonists. It reuses
  the NKB–NK3R pair but acts on a different postsynaptic population and is not a step of the
  pulse generator, so it belongs in a separate module. The four tachykinin gene reviews carry
  it as a distinct core function keyed to `GO:0001659` temperature homeostasis, not to the
  reproductive process terms used here.
- **Prohormone processing: out of scope.** PCSK1/PCSK2/CPE and the amidating enzyme are shared
  secretory machinery, not specific to this circuit.
- **The preovulatory surge arm: out of scope**, except as a route variant. Rostral (AVPV/PeN)
  kisspeptin neurons are stimulated rather than inhibited by estradiol, so the surge circuit has
  the opposite sign of feedback and is a separate module; only its possible role as a relay for
  arcuate output appears here.
- **Estradiol feedback: in scope as a regulatory input**, not as a peptide step. The validator
  flags that the feedback node has no incoming activating edge; that is right, because the
  steroid comes from the gonads via the pituitary, both outside the boundary. Estradiol is an
  exogenous input to this module.
- **Species scope: Mammalia as an envelope.** The complete loop has been tested in mouse; the
  three-peptide phenotype and ERα co-expression are also established in sheep; estradiol
  suppression of infundibular NKB in the ovariectomised cynomolgus monkey; and the human
  evidence is loss-of-function genetics for TAC3, TACR3, KISS1 and KISS1R plus the
  post-menopausal rise in infundibular NKB expression. Per-claim species are stated in the
  evidence statements, and the residual question is a knowledge gap at module level.

## Route variant (part 4)

`kisspeptin_source_route` is a `ROUTE` variant set with `selection: ONE_OR_MORE`, on the axis
"route from the arcuate oscillator to the GnRH neuron":

- `direct_arcuate_kisspeptin` — arcuate terminals release kisspeptin onto GnRH neuron somata,
  dendrites and terminals, including at the median eminence (the classical route, supported by
  human and sheep anatomy);
- `relayed_rostral_kisspeptin` — in mouse horizontal slices the arcuate burst excites rostral
  AVPV/PeN kisspeptin neurons through co-released glutamate, and those neurons excite GnRH
  neurons with their own kisspeptin.

The receptor step (`gnrh_neuron_depolarization`) is a conjunctive part of the same node, shared
by both routes. Which route carries the pulse in vivo is recorded as a knowledge gap, not
decided here. The glutamatergic arm of the relay is deliberately not given a transporter
annoton: the cached evidence for VGLUT2 in these neurons is a background citation within the
slice paper, which is enough to describe the route and not enough to assert a transporter's
role.

## Grounding

- **PANTHER** family and subfamily ids were read from `interpro/panther/panther.obo`:
  `PTHR15536:SF1` TACHYKININ-3, `PTHR16955:SF6` METASTASIS-SUPPRESSOR KISS-1,
  `PTHR11438:SF4` PROENKEPHALIN-B, `PTHR46925:SF1` NEUROMEDIN-K RECEPTOR, and the two Gq/11
  alpha subfamilies `PTHR10218:SF329` and `PTHR10218:SF328`. Family reviews exist for PTHR15536,
  PTHR16955 and PTHR11438; PTHR46925 has none yet, and `PTHR24229` (the opioid receptors) has a
  PAINT slice but no review.
- **Two descriptors deliberately assert no PANTHER id.** The kisspeptin receptor, because the
  PTHR45695 family review established that neither human nor mouse KISS1R is a leaf of that tree
  (both are in PTHR24230, which has no review here) while UniProt cross-references them to
  `PTHR45695:SF23`; and the TRPC channel, because the subunit that carries the kisspeptin current
  is not settled. Both keep verified UniProt exemplars instead.
- **PAINT nodes** come only from local slices: `PTN002704209`
  (`interpro/panther/PTHR16955/PTHR16955-paint.tsv`, carrying `GO:0031773` kisspeptin receptor
  binding among others, seeded in part by human KISS1) and `PTN009086039` (a PTHR24230 node
  present in the PTHR45695 slice, carrying `GO:0008188`, seeded by human KISS1R). PTHR15536's
  only PAINT node carries `GO:0045777` positive regulation of blood pressure, which this module
  does not assert, so the tachykinin ligand carries no ancestral node.
- **GO-CAM pins.** `gomodel:68d5ebd600000736` (NKB → NK3R → Gq) is pinned to the three annotons
  of part 2; `gomodel:68d5ebd600001111` (kisspeptin → KISS1R → GNAQ → TRPC4 → depolarisation) is
  pinned to the ligand annoton of the direct route and to the three annotons of the receptor
  step. The Gs sister model `gomodel:68d5ebd600000043` is named in the ligand annoton's
  description but not pinned: this module does not assert a Gs branch in the KNDy circuit.
- **UniProt accessions** were read from the REST API while the module was written: P03372 (ESR1),
  Q9UHF0 / P55099 (TAC3 / mouse Tac2), P29371 / P47937 (TACR3 / Tacr3), P50148 (GNAQ), P29992
  (GNA11), P01213 (PDYN), P41145 (OPRK1), Q15726 / Q6Y4S4 (KISS1 / Kiss1), Q969F8 / Q91V45
  (KISS1R / Kiss1r), Q9UBN4 (TRPC4), P01148 (GNRH1), P30968 (GNRHR, named but not modelled).
- **Gene reviews.** Present for TAC3, TACR3, KISS1, KISS1R, PDYN, GNAQ, GNA11 (human) and Tac2,
  Tacr3, Kiss1, Kiss1r (mouse). Absent for ESR1, OPRK1, GNRH1, TRPC4, and, downstream, GNRHR and
  LHB. ESR2 is reviewed but is not the receptor shown to mediate the arcuate feedback, so it was
  not substituted for ESR1. The rendered QC panel reports those four as "Review Missing"; every
  function asserted for a reviewed participant is reported as core-supported.

## Proposed new terms

1. **gonadotropin-releasing hormone secretion** (parent `GO:0030072` peptide hormone secretion).
   GO has response-to-GnRH terms, the hormone's activity, its receptor and the pituitary
   gonadotropin secretion it causes, but no class for the release of GnRH itself.
2. **regulation of gonadotropin-releasing hormone secretion** (parent `GO:0046883`). What this
   circuit does is set the frequency and amplitude of GnRH release; the available terms name the
   pituitary outcome two steps downstream.
3. **kisspeptin receptor activity** (parent `GO:0008188` neuropeptide receptor activity). The
   ligand side has `GO:0031773` kisspeptin receptor binding, and the sibling receptors have
   specific activities (`GO:0016498`, `GO:0038048`), but KISS1R has none. The pathway counterpart,
   kisspeptin receptor signaling pathway, is already requested in the KISS1 gene review.

## Knowledge gaps (all BIOLOGY, all OPEN)

1. Which tachykinin receptor carries endogenous NKB's excitation of KNDy neurons (NK3R-dependent
   slow EPSP versus the three-receptor requirement for bath-applied NKB).
2. Whether dynorphin–KOR signalling is what terminates each pulse, and what sets the interpulse
   interval; KOR antagonism does not start firing in quiescent KNDy neurons.
3. Which TRPC subunit or subunits carry the kisspeptin-activated current in GnRH neurons.
4. Whether the human infundibular KNDy network generates pulses by the rodent mechanism; the
   human evidence is genetic and expression-level.

No CURATION- or ONTOLOGY-only gap was recorded: the missing gene reviews and the missing GO terms
are in these notes and in `proposed_new_terms` respectively.

## Validation

```
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/kndy_gnrh_pulse_generator.yaml   # No issues found
uv run python -m ai_gene_review.validation.module_validator modules/kndy_gnrh_pulse_generator.yaml  # passed, 8 warnings
just validate-quotes modules/kndy_gnrh_pulse_generator.yaml  # 88 quotes verified, 0 not found
just render-module modules/kndy_gnrh_pulse_generator.yaml    # recommended-field compliance 100%
```

Seven of the eight module-validator warnings are the PANTHER member index not being built in this
checkout, so family membership was not checked; the eighth is the open feedback loop described
above. Every reference carries one `findings` entry and a `reference_review`; each title was
checked against the cached PubMed record by the validator and each quote verifies verbatim, which
is what `correctness: VERIFIED` records here. Seventeen of the 23 cached records are abstract-only
and are flagged `full_text_unavailable`, so their quotes are necessarily from the abstract. The
module is left at `status: DRAFT`: the four participants without gene reviews (ESR1, OPRK1, GNRH1,
TRPC4) and the missing PTHR46925 and PTHR24230 family reviews are the work that promotion should
wait on.
