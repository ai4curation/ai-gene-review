# GLI2 curation notes

Working journal for the GO annotation review of human GLI2 (UniProt P10070, HGNC:4318).
Provenance convention: `[PMID:xxxxx "verbatim supporting text"]`. Quotes are taken from
the cached records under `publications/`; where a cache is abstract-only this is stated
explicitly, because a quote that is not in the cache cannot be used as `supporting_text`.

No deep-research file was supplied for this gene and none was generated (the repo rule is
that a hand-written file must never be named `-deep-research-<provider>.md`). This notes
file is therefore the research record.

## 1. What the gene is

GLI2 is one of three vertebrate paralogs of *Drosophila* `cubitus interruptus` (Ci), the
zinc-finger transcription factor at the bottom of the Hedgehog pathway. UniProt records five
C2H2 zinc fingers (FT ZN_FING 437..464, 475..497 "degenerate", 503..527, 533..558, 564..589),
an N-terminal repressor region (REGION 1..328) and large disordered stretches between the
fingers and the C terminus. The recommended name is "Transcription activator GLI2" and the
entry additionally defines a processed chain, "Transcription repressor GLI2R".

The family assignment relevant to this repo is PANTHER PTHR45718
(`TRANSCRIPTIONAL ACTIVATOR CUBITUS INTERRUPTUS`), with PAINT ancestral node
`PANTHER:PTN001836086` carrying `GO:0007224 smoothened signaling pathway`. Both are recorded
in `modules/hedgehog_signaling.yaml`, where GLI2 is one of the three representative members
of the `ci_gli_activator` annoton. PTHR45718 has no family review of its own in
`interpro/panther/` yet; PTHR11309 (Smoothened) and PTHR11889 (Hedgehog ligand) do, and those
were used as the tone/standard reference for this review.

## 2. The division of labour among GLI1/GLI2/GLI3

This is the single most important fact for grading GLI2's annotations, and it is what the
term `GO:0001228` (activator) versus `GO:0001227` (repressor) is tracking:

- GLI2 is the principal **activator-forming** paralog. UniProt states it directly:
  "The transcriptional activator form constitutes the major form of GLI2" and, for the
  processed chain, "Constitutes a minor form of GLI2, while the transcription activator GLI2
  form plays a major role in smoothened signaling".
- GLI3 is the principal **repressor-forming** paralog (the `ci_gli_repressor` annoton of the
  module names GLI3 as "the principal vertebrate repressor-forming paralog").
- GLI1 is an obligate activator and a transcriptional **target** of GLI2, not an upstream
  input — it amplifies rather than initiates.

The mouse literature states the activator asymmetry plainly:
[PMID:15994174 "Zinc finger-containing Gli proteins mediate responsiveness to Hedgehog (Hh)
signaling, with Gli2 acting as the major transcriptional activator in this
pathway in mice."] (cache is abstract-only).

Consequence for the review: GLI2 legitimately carries **both** `GO:0045944` (positive
regulation of transcription by RNA Pol II) and `GO:0000122` (negative regulation), but they
are not symmetric. The activator side is core; the repressor side is real but secondary, and
is graded `KEEP_AS_NON_CORE`.

## 3. Evidence that GLI2 is a sequence-specific Pol II activator (the core claim)

**Direct promoter binding.** GLI2 binds the GLI consensus in the human *GLI1* promoter and
activates it:
[PMID:15175043 "Using band shift and luciferase reporter assays, we now show that GLI2 binds
the GLI-binding consensus sequence in the GLI1 promoter."] and
[PMID:15175043 "These data suggest that GLI2 directly activates GLI1 and that retrovirally
expressed GLI2 induces expression of endogenous GLI1 in human primary keratinocytes."]
(abstract-only cache; both sentences are in the abstract).

**GLI1 is the target, GLI2 the driver.** The time-course dissection that establishes
directionality:
[PMID:12165851 "Detailed time course experiments monitoring the transcriptional response of
keratinocytes either to GLI1 or to GLI2 suggest that GLI1 is a direct target of GLI2, while
activation of GLI2 by GLI1 is likely to be indirect."] (abstract-only cache). This matches
Reactome R-HSA-5635846 "GLI proteins bind GLI1 gene", whose summary calls GLI1 "a direct
target of the GLI transcription factors".

**Chromatin occupancy at a native promoter, and EMSA on the same site.** The FOXC1 paper
provides both assays on endogenous/expressed GLI2:
[PMID:26565916 "Using the chromatin immunoprecipitation (ChIP) assay, we found that FOXC1
enhanced the binding of Gli2 to the FAM38B promoter in MDA-MB-231 cells, and this enhancement
was eliminated by Gli2-knockdown (Figure 5A)."] and
[PMID:26565916 "These data indicate that FOXC1 promotes the DNA-binding capacity of Gli2 in
breast cancer cells."]. This is the grounding for `GO:1990841 promoter-specific chromatin
binding` (IDA) as well as for the sequence-specific DNA-binding rows.

**The N-terminal repressor domain.** The domain that makes GLI2 bifunctional, and the reason
`GO:0000122` exists on this gene:
[PMID:15994174 "In vitro, transcriptional activity of full-length GLI2 is up to 30 times lower
than that of GLI2DeltaN (previously thought to represent the entire GLI2 protein), revealing
the presence of an amino-terminal repressor domain in the full-length protein."] and
[PMID:15994174 "Our results establish the presence of an amino-terminal transcriptional
repressor domain that plays a critical role in modulating the function of wild-type GLI2 and
is essential for dominant-negative activity of a GLI2 mutant associated with human disease."].

SKI is the corepressor that domain works through — the same paper that characterised
Gli3Rep/SKI also assayed Gli2:
[PMID:12435627 "In fact, we observed that Ski directly binds to Gli2 and is required for the
Gli2Ν-dependent transcriptional repression."] and
[PMID:12435627 "Thus, a loss of Ski abrogated the Gli3CT2- or Gli2N-induced transcriptional
repression, suggesting that the amounts of Sno in MEFs are relatively low."].
Note this is a case where the paper's *title* is about Gli3 but the full text (cached, and
`full_text_available: true`) assays Gli2 explicitly — exactly the pattern the repo rules warn
against mis-reading as paralog confusion.

## 4. How GLI2 is switched on — and why the ciliary rows are not the active location

The activation step is a phosphorylation cascade downstream of SMO that releases GLI2 from
SUFU and lets it enter the nucleus. Three cached papers cover three kinase routes, and all
three have matching cached GO-CAMs (`gocams/index.tsv`):

- **Fused-family kinases (ULK3, STK36).** [PMID:31279575 "Furthermore, we provide evidence
  that Sonic hedgehog (Shh) activates Gli2 by stimulating its phosphorylation on conserved
  sites through the Fu-family kinases ULK3 and mFu/STK36 in a manner depending on Gli2 ciliary
  localization."] (abstract-only cache). GO-CAMs `696022cd00001523` (ULK3 route) and
  `696022cd00001645` (STK36 route).
- **DYRK2.** [PMID:38968120 "DYRK2 phosphorylates highly conserved serine residues
  (GLI2S252/GLI3S313) by a mechanism that is dependent on the activation of SMO, facilitating
  the dissociation of GLI2/GLI3 from SUFU, and their subsequent nuclear translocation."] and
  [PMID:38968120 "Furthermore, a phosphomimetic mutant (GLI2S252E) demonstrated distinct
  nuclear localization in contrast to the predominant cytoplasmic distribution of wild-type
  GLI2 and the alanine mutant (GLI2S252A)"]. GO-CAM `693b3c0900001575` (DYRK2 route).
- **SUFU sequestration is the off-state.** [PMID:38968120 "Another negative regulator, SUFU,
  inhibits Hh signaling by retaining GLI2 and GLI3 in the cytoplasm and blocking their nuclear
  translocation."] — this is what the `GO:0005737 cytoplasm` and `GO:0005829 cytosol` rows are
  really recording.

**Ciliary accumulation is real and is directly demonstrated for endogenous GLI2:**
[PMID:20154143 "By generating antibodies capable of detecting endogenous pathway transcription
factors Gli2 and Gli3, we monitored their kinetics of accumulation in cilia upon Hh
stimulation."] and [PMID:20154143 "Localization occurs within minutes of Hh addition, making
it the fastest reported readout of pathway activity, which permits more precise temporal and
spatial localization of Hh signaling events."] (abstract-only cache). Note the paper's title
foregrounds Gli3, but the abstract itself names the Gli2 antibody and the Gli2 measurement, so
the `GO:0097730 non-motile cilium` IDA is properly grounded.

**Curation call.** Cilium / ciliary tip / ciliary base / basal body / centrosome / cytosol /
cytoplasm are all genuine GLI2 locations, but none is where GLI2 executes its molecular
function. They are the transit and storage compartments of the regulatory circuit. Both the
module (`ci_gli_activator` → `locations: GO:0005634 nucleus`) and every cached GO-CAM row for
P10070 (`GO:0001228 / GO:0007224 / GO:0005634`) put the *active* location in the nucleus. So
the nuclear rows are `ACCEPT` and the extranuclear rows are `KEEP_AS_NON_CORE`. This is a
deliberate agreement with the module, not an oversight.

## 5. Things that needed a second look

**`GO:0008270 zinc ion binding` (IDA, PMID:8378770).** The cited crystal structure is of
"the five Zn fingers from the human GLI oncogene", i.e. GLI1, not GLI2
[PMID:8378770 "The crystal structure of a complex containing the five Zn fingers from the
human GLI oncogene and a high-affinity DNA binding site has been determined at 2.6 A
resolution."]. This is precisely the situation the repo rules cover: do **not** REMOVE an
experimental annotation on a paralog-title argument. Independently, GLI2 demonstrably has five
C2H2 fingers of its own (UniProt FT ZN_FING x5, one flagged degenerate), so the *claim* — that
GLI2 binds zinc — is unambiguously correct for this gene. Accepted, with the structural-cofactor
reading spelled out in the row.

**`GO:0045740 positive regulation of DNA replication` (IDA, PMID:12165851).** The evidence is
[PMID:12165851 "Furthermore, expression of either GLI2 or GLI1 led to an increase in
DNA-synthesis in confluent human keratinocytes."]. A DNA-synthesis readout after
overexpressing a transcription factor is a proliferation phenotype, not evidence that GLI2
acts in the replication machinery or regulates replication initiation. GLI2 performs no step
of DNA replication; it drives a transcriptional program whose downstream consequence is
proliferation. Marked as over-annotated rather than removed — the observation is real, the
term over-reaches.

**`GO:0005730 nucleolus` (IDA, GO_REF:0000052 = immunofluorescence curation).** Within the
nucleus, so not wrong in the crude sense, but there is no functional correlate: no reported
rDNA/Pol I role for GLI2, and nucleolar staining is a common IF artefact for abundant nuclear
proteins. Over-annotated.

**The five `GO:0005515 protein binding` rows.** Repo policy forbids ACCEPT/MARK_AS_OVER_ANNOTATED
here; MODIFY where the paper supports a more informative MF, else REMOVE. Four of the five
papers identify what kind of partner it is, so four become MODIFY:
- SKI (P12755), PMID:12435627 → `GO:0001222 transcription corepressor binding`.
- SMAD3 (P84022), PMID:25670079 → `GO:0046332 SMAD binding`
  [PMID:25670079 "Smads can directly bind to Gli2 protein to upregulate PTHrP transcription."].
- BTRC (Q9Y297), PMID:25670079 → `GO:0031625 ubiquitin protein ligase binding`
  [PMID:25670079 "while 14-3-3ζ stabilizes Gli2 by blocking Gli2’s binding with its E3 ligase
  β-TrCP"]. GLI2 is the substrate of the SCF(BTRC) complex here; the binding is to the
  ligase's substrate-recognition subunit.
- FOXC1 (Q12948), PMID:26565916 → `GO:0008134 transcription factor binding`
  [PMID:26565916 "We have identified FOXC1 as a Smoothened (SMO)-independent activator of
  Hedgehog (Hh) signaling via direct interaction with the Gli2 transcription factor."].
- TSG101 (Q99816), PMID:35044719 → REMOVE. This is an untargeted proteome-scale
  peptide-phage-display screen of disordered regions
  [PMID:35044719 "Here, we describe an optimized proteomic peptide-phage display library that
  tiles all disordered regions of the human proteome and allows the screening of ~ 1,000,000
  overlapping peptides in a single binding assay."]; the cached text does not name GLI2 and no
  functional consequence is established. Removal does not assert the interaction is false.

**The ISS block (GO_REF:0000024).** All 25 developmental rows transfer from
`UniProtKB:Q0VGT2` — verified by lookup to be **mouse Gli2**, a true 1:1 ortholog — except
`GO:0033089` which transfers from `UniProtKB:Q0VGV1`, also mouse Gli2 (an unreviewed entry for
the same gene). These are genuine mouse knockout phenotypes and the transfers are sound. They
are nonetheless downstream developmental *outcomes* of GLI2-driven transcription rather than
things GLI2 does molecularly, so all are `KEEP_AS_NON_CORE`. The pituitary row is the one with
independent human genetic corroboration: UniProt's DISEASE lines record holoprosencephaly 9
"characterized by defective anterior pituitary formation and pan-hypopituitarism" and
Culler-Jones syndrome, both caused by GLI2 variants — corroborating, but still an outcome.

**Two too-general terms.** `GO:0010468 regulation of gene expression` (ARBA) is modified to
`GO:0006357 regulation of transcription by RNA polymerase II`, which GLI2 already carries by
IBA and which is the right grain for a Pol II transcription factor. The four
`GO:0043565 sequence-specific DNA binding` rows are modified to
`GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding`: every
characterised GLI2 site is a Pol II cis-regulatory element (the GLI1 promoter, the FAM38B
promoter, the HTLV-1 LTR), so the parent term discards information the assays supply. Note the
term-consistency rule forces one action across all rows of a term, which is satisfied here.

## 6. The HTLV-1 / Tax isoform literature

`PMID:9557682` is the isoform-cloning paper and is the source of the `alternative_products`
block (isoforms alpha/beta/gamma/delta plus the later-added full-length form). It establishes
DNA binding by all four isoforms
[PMID:9557682 "Four possible isoforms (hGli2 alpha, beta, gamma, and delta) are formed by
combinations of two independent alternative splicings, and all the isoforms could bind to a
DNA motif, TRE2S, in the LTR."] and Gal4-fusion transactivation
[PMID:9557682 "Fusion proteins of the hGli2 isoforms with the DNA-binding domain of Gal4
activated transcription when the reporter contained a Gal4-binding site and one copy of the
21-bp sequence, to which CREB binds."]. UniProt marks the Tax-dependent activity as
"(Microbial infection)" and separately records `[Isoform 1]: Nucleus` and `[Isoform 2]:
Nucleus` from this paper, which is what the `GO:0005634` EXP row rests on. The cached record
is abstract-only and the abstract does not state the localisation, so that row is accepted on
the strength of the curator's full-text reading plus the two independent IDA nuclear rows,
and its `supported_by` quotes those instead.

## 7. Why no `NEW` annotation was proposed

The obvious candidate was `GO:0045880 positive regulation of smoothened signaling pathway`.
It fails the participation test as applied in `CLAUDE.md`. GLI2 is the *terminal effector* of
the pathway, not a regulator of it: the entities that positively regulate the pathway are the
kinases acting on GLI2 (ULK3, STK36, DYRK2, CDK1), and in every cached GO-CAM that is exactly
how it is modelled — `GO:0045880` sits on ULK3/STK36/DYRK2/CDK1 while GLI2 carries
`GO:0001228` + `GO:0007224`. The module agrees: its `ci_gli_activation` node assigns
`GO:0045880` to the kinase tier, and `ci_gli_activator` gives the GLI protein `GO:0007224`.
Adding `GO:0045880` to GLI2 would assert that the output of a pathway regulates that pathway,
and would in any case be redundant against `GO:0007224`, which GLI2 already holds six times
over. The GLI1 feedback loop is a genuine amplification circuit but it is captured as
transcriptional activation of a target gene, which `GO:0045944` already covers.

No contradiction with `modules/hedgehog_signaling.yaml` or with the PTHR11309/PTHR11889 family
reviews was found; every GLI2 decision here lines up with the `ci_gli_activator` annoton.

## 8. Open questions recorded in the review

- Whether the GLI2R repressor chain warrants its own `GO:0001227` annotation, or whether the
  existing `GO:0000122` on full-length GLI2 is the right representation given that UniProt
  calls GLI2R the minor form and its processing is asserted only "By similarity".
- Whether the four ciliary/basal-body locations should be modelled as a single transit step
  rather than as five independent CC rows.
