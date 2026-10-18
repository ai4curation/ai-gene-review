# TNFRSF21 (DR6) review notes

## Why this gene was selected

DR6 is an orphan TNF-receptor-superfamily member whose most famous claimed function - being the
receptor for an N-terminal fragment of APP, and thereby driving developmental axon pruning and
neuron death - has come apart in two separate steps: the founding paper was retracted in 2024, and
a 2026 eLife study failed to reproduce a separate, later claim that DR6 drives Wallerian
degeneration. The curation question is how much of GOA is actually exposed.

## What GOA actually carries (checked before judging)

`TNFRSF21-goa.tsv` was read column by column. Findings that constrain the whole review:

- **The only molecular function on the gene is bare `GO:0005515` protein binding**, four IntAct
  rows: `PMID:23559013` with `UniProtKB:P08138` (NGFR/p75NTR), `PMID:32296183` with
  `UniProtKB:O43765` (SGTA), and `PMID:35922511` with `UniProtKB:P05067` (APP) and
  `UniProtKB:Q6UXB8` (PI16). So an **APP-binding annotation does exist**, but only as
  uninformative `protein binding`; there is no "APP receptor", "amyloid-beta precursor protein
  binding" or death-receptor MF anywhere on the gene.
- **There is no `NOT` qualifier anywhere** in the file - every row is a positive assertion.
- **There is no axon-degeneration or axon-pruning term on the gene at all.** GO has no
  `axon degeneration` or `axon pruning` term (the nearest is `GO:0016322` neuron remodeling, which
  TNFRSF21 does not carry). The closest thing in GOA is `GO:0007413` axonal fasciculation, and
  `GO:0051402` neuron apoptotic process.
- **No GO annotation on human or mouse TNFRSF21 derives from the retracted paper.** Checking the
  mouse ortholog (`Q9EPU5`) in QuickGO, which is the ISS/IEA donor for most of the human BP set,
  the experimental sources are `PMID:11485735` (T cells), `PMID:12515813` (B cells),
  `PMID:21725297` (oligodendrocytes/myelination) and `PMID:23559013` (neuron apoptotic process).
  `PMID:19225519` (Nikolaev et al.) appears nowhere.

That last point is the single most important finding of this review: the exposure to the retraction
is essentially zero, and the exposure to the Wallerian refutation is limited to one propagated IEA.

## The retraction

The founding APP/DR6 paper is retracted:
[PMID:38110576 "The authors have retracted this article"], for image duplication and statistical
errors plus superseded conclusions
[PMID:38110576 "However, our later research also showed that certain conclusions reached in the
article were incorrect, notably the role of caspase-3, the necessity for beta-secretase enzyme
activity for APP-DR6 binding, and the model for the APP-DR6 interaction"] and
[PMID:38110576 "Certain biostatistical calculations underlying some figures contained errors."].

The retraction is *partial* in substance. The authors explicitly maintain the core genetic claim:
[PMID:38110576 "that DR6 and APP interact and function in a genetic pathway involving caspases to
control axon pruning and neuron death"]. That maintenance rests on a separate, non-retracted paper
which repeated the in vivo genetics:
[PMID:24806670 "We show that genetic deletion of APP similarly impairs pruning of retinal axons in
vivo and provide evidence that APP and DR6 act cell autonomously and in the same pathway to control
pruning."] and [PMID:24806670 "Genetic deletion of DR6 was previously shown to impair pruning of
retinal axons in vivo."], while correcting the mechanism
[PMID:24806670 "further genetic and biochemical analysis reveals that β-secretase activity is not
required and that high-affinity binding to DR6 requires a more C-terminal portion of the APP
ectodomain"].

So: developmental retinal axon pruning in vivo survives the retraction via PMID:24806670; the
beta-secretase/N-APP mechanistic model does not.

## The Wallerian refutation

The 2017 claim being tested:
[PMID:28285993 "We find that an orphan receptor, death receptor 6 (DR6), is required to drive axon
degeneration after axotomy in sympathetic and sensory neurons cultured in microfluidic devices."]
and [PMID:28285993 "Consistent with the in vitro findings, DR6-/- animals displayed preserved axons
up to 4 weeks after injury."]

The 2026 non-replication:
[PMID:41891813 "Here, we rigorously revisit the role of DR6 in WD using two independent DR6 knockout
mouse lines including the same model used in the previous study."]
[PMID:41891813 "Surprisingly, in contrast to the earlier report, we observed no impact of DR6
deletion on AxD kinetics or SC injury responses across a range of WD assays."]
[PMID:41891813 "Moreover, injured axons in primary neuronal cultures lacking DR6 degenerated at a
similar rate as wild-type axons."]
[PMID:41891813 "We conclude that DR6 is dispensable for the regulation of AxD and glial nerve injury
responses during WD."]

This is a strong non-replication: two independent knockout lines, one of them the original line,
both in vivo and in the in vitro assay format the original used. It is nonetheless a single
laboratory's non-replication with no response yet from the original authors.

## What the refutation does and does not cover

Covered: injury-induced Wallerian degeneration of **peripheral** axons after axotomy, Schwann cell
injury responses, and the associated in vitro axotomy assay. Also, by the authors' own framing,
the therapeutic rationale that runs through WD:
[PMID:41891813 "Our data argue that any therapeutic benefit from DR6 suppression in
neurodegeneration models occurs through mechanisms independent of WD."]

**Not covered:**
- **Developmental axon pruning in the CNS** (retinocollicular pruning in PMID:24806670). Different
  process, different context, different assay. Wallerian degeneration is injury-triggered
  disintegration of a severed distal axon; developmental pruning is a trophic-cue-driven,
  receptor-mediated removal of a branch on an intact neuron. A null result in one says nothing
  about the other, and PMID:24806670 has not been independently re-tested.
- **Trophic-deprivation-induced degeneration**, which the original 2009 work also assayed.
- **Aβ-induced neuron death**, an independent line: [PMID:23559013 "Here, we demonstrate that death
  receptor 6 (DR6) binds to p75(NTR) and is a component of the p75(NTR) signaling complex
  responsible for Aβ-induced cortical neuron death."] and [PMID:23559013 "Cortical neurons isolated
  from either DR6 or p75(NTR) null mice are resistant to Aβ-induced neurotoxicity."] This is the
  actual evidential basis for the `GO:0051402` neuron apoptotic process annotation.
- **The immune and oligodendrocyte roles**, which are entirely separate literatures (below).

## The well-supported functions, which are unaffected

T cells: [PMID:11485735 "However, DR6(-/-) CD4(+) T cells hyperproliferated in response to
TCR-mediated stimulation and protein antigen challenge."] and [PMID:11485735 "DR6, therefore,
functions as a regulatory receptor for mediating CD4(+) T cell activation and maintaining proper
immune responses."], with Th2 skewing
[PMID:11485735 "Enhanced Th2 cytokine production by activated DR6(-/-) CD4(+) T cells was associated
with the increased transcription factor NF-ATc in nuclei."]

B cells: [PMID:12515813 "In vitro, DR6(-/-) B cells undergo increased proliferation in response to
anti-immunoglobulin M, anti-CD40, and lipopolysaccharide."] and [PMID:12515813 "DR6(-/-) mice
exhibited enhanced germinal center formation and increased titers of immunoglobulins to T-dependent
as well as T-independent type I and II antigens."]

Oligodendrocytes: [PMID:21725297 "Here we show that death receptor 6 (DR6) is a negative regulator
of oligodendrocyte maturation."], [PMID:21725297 "Attenuation of DR6 function leads to enhanced
oligodendrocyte maturation, myelination and downregulation of casp3."] and
[PMID:21725297 "Consistent with the DR6 antagoinst antibody studies, DR6-null mice show enhanced
remyelination in both demyelination models."]

Localisation: [PMID:19654028 "Deletion of the entire linker region between CRDs and the
transmembrane domain, spanning over 130 amino acids, severely compromises the plasma membrane
localization of DR6 and leads to its intracellular retention."]

## Curation position taken

Nothing is removed. The refutation and the retraction land on claims that GOA never encoded.

- All plasma-membrane and immune-regulatory terms: **ACCEPT**. Grounded in two independent mouse
  knockout papers that the recent disputes do not touch.
- `GO:0051402` neuron apoptotic process (IBA + IEA): **ACCEPT**, with the provenance spelled out in
  `reason`. Its mouse source is `PMID:23559013` (Aβ/p75NTR), not the retracted paper, and the eLife
  study addressed axon degeneration, not neuronal apoptosis. Kept at ACCEPT rather than demoted
  partly because demoting an IBA would require a structured `propagation_review` that this review
  cannot honestly supply - the PAINT tree was not inspected - and partly because the annotation is
  in fact experimentally grounded in the ortholog.
- `GO:0097252`, `GO:0048713`, `GO:0031642`: **ACCEPT**. Mi et al. 2011 is independent of both
  disputes.
- `GO:0042552` myelination: **MODIFY** to `GO:0031642` negative regulation of myelination. DR6 is a
  negative regulator; the unqualified parent misstates the direction of the effect, and the gene
  already carries the correct child.
- `GO:0032693` / `GO:0032696` / `GO:0032714` (negative regulation of IL-10 / IL-13 / IL-5
  production): **KEEP_AS_NON_CORE**. These are readouts of the Th2 skewing seen in DR6-null CD4 T
  cells, i.e. downstream consequences of the T-cell regulatory role, not separate functions.
- `GO:0050852` T cell receptor signaling pathway: **KEEP_AS_NON_CORE**. DR6 restrains the
  proliferative outcome of TCR stimulation; it is not a component of the TCR signalling pathway.
- `GO:0006915` apoptotic process (IMP, PMID:22761420): **KEEP_AS_NON_CORE**. Real but derived from
  ectopic overexpression [PMID:22761420 "it was found that DR6 induces apoptosis when it is
  overexpressed"], with a Bax requirement [PMID:22761420 "Our data demonstrated that Bax
  translocation is absolutely required for DR6-induced apoptosis."]; overexpression of a
  death-domain receptor causing apoptosis is weak evidence for a physiological role, and the term is
  maximally general.
- `GO:0007413` axonal fasciculation (IEA, Ensembl transfer from rat `D3ZF92`):
  **MARK_AS_OVER_ANNOTATED**. The rat source is an IMP from `PMID:25898930`, a study of prion-peptide
  (PrP106-126)-induced **axonal degeneration** in cultured rat spinal neurons. `GO:0007413` is
  defined as "The collection of axons into a bundle of rods, known as a fascicle", which that paper
  does not address; and the underlying phenomenon - DR6-dependent axon degeneration - is precisely
  what `PMID:41891813` failed to reproduce in mouse. The rat experimental annotation is not
  overruled here (the curator saw the full text and this review has not); the human IEA that
  propagates it is flagged.
- `GO:0071356` cellular response to tumor necrosis factor (IDA, PMID:19654028): **UNDECIDED**. That
  paper is a study of N-/O-glycosylation, palmitoylation and lipid-raft targeting of DR6
  [PMID:19654028 "In this study we document that DR6 is an extensively posttranslationally modified
  transmembrane protein"]; the cached record is abstract-only and describes no TNF-stimulation
  experiment. DR6 has no known TNF-family ligand and is routinely described as orphan
  [PMID:41891813 "A prior study reported that eliminating the orphan tumor necrosis factor receptor
  DR6 (death receptor 6, encoded by Tnfrsf21) strongly delays AxD and alters SC injury responses
  during WD"]. Flagged rather than removed, per the rule against overruling an experimental
  annotation from an abstract.
- `GO:0005515` protein binding x3: **MARK_AS_OVER_ANNOTATED** per project guidance. Noted in the
  reason that one of these rows is the APP interaction, redetected independently of the retracted
  work in a systematic extracellular-interactome screen (`PMID:35922511`), and that a specific
  APP-binding MF term would be more informative than bare protein binding.

## Loose ends and honest uncertainty

- Whether DR6 is genuinely an APP receptor is not settled here. The physical interaction has
  independent support (the IntAct row from PMID:35922511) and the retraction notice affirms it, but
  the affirmation comes from the retracting authors, and the structural model of the interaction was
  one of the things retracted.
- Developmental CNS pruning rests on PMID:24806670, which has not been independently replicated and
  shares authorship with the retracted paper. It is not refuted; it is untested by others.
- `GO:0002250` adaptive immune response and `GO:0006959` humoral immune response are accepted but are
  grouping-level terms; the informative statements are the negative-regulation children.

## One annotation added

`GO:0004888` transmembrane signaling receptor activity is proposed as a **NEW** annotation (ISS from
the mouse ortholog). Without it the gene has no molecular function at all once bare `GO:0005515` is
set aside as uninformative. `GO:0005035` death receptor activity was considered and rejected: it
requires combining with an extracellular death ligand, and DR6 has none identified. This is also the
molecular function carried in `core_functions`.
