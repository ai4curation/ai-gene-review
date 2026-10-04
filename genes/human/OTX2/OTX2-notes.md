# OTX2 curation notes

UniProt: P32243 (OTX2_HUMAN). HGNC: OTX2. Locus 14q22.3.
PANTHER family: PTHR45793 (Paired homeobox transcription factors); bicoid subfamily
of the paired-like homeodomain class.

Journal-style working notes. Provenance is recorded inline as
`[PMID:xxxxx "<verbatim supporting text>"]`. Anything without a citation is my own
synthesis and is flagged as such.

---

## 2026-09-20 — initial pass

Seeded with `ai-gene-review fetch-gene human OTX2` (36 GOA annotations, 15 seeded
references). Deep research run with the falcon provider →
`OTX2-deep-research-falcon.md`. That report is good on the disease/cancer side and on
the hypothalamic–pituitary axis, but it under-covers three things I had to research
separately: (1) the classic mouse null phenotypes, (2) the OTX2/GBX2 boundary that
positions the isthmic organizer, and (3) the non-cell-autonomous homeoprotein transfer
biology. Those are filled in below.

The immediate trigger for this review is
[PMID:42760324](https://pubmed.ncbi.nlm.nih.gov/42760324/), *Two parallel neural
ectoderm progenitors contribute to the developing brain* (Jokhai, Dundes et al., Nat
Neurosci 2026), which makes OTX2 the marker of one of the two parallel brain
progenitors. That paper is the reason the `neural_ectoderm_anteroposterior_specification`
module needs OTX2 grounded, and this review is the prerequisite.

### 1. What the protein is

A 289/297-aa bicoid-class homeodomain transcription factor; the homeodomain spans
residues ~38–97 and is the DNA-binding module. Recognizes bicoid-type `TAATCC` sites;
binds as monomer or dimer. DNA binding alone does not determine output — activation
vs. repression depends on cofactors and promoter context.

Worth noting for the molecular-function call: OTX2 belongs to the **extended homeodomain
family that prefers CpG-methylated sites**, established by methyl-SELEX across 542 human
TFs [PMID:28473536 "we found that there are also many TFs that prefer CpG-methylated
sequences. Most of these are in the extended homeodomain family"]. So the
`GO:1990837 sequence-specific double-stranded DNA binding` IDA from that paper is a
high-throughput-but-careful in-vitro binding measurement, not a functional assay.

### 2. Core developmental role: anterior neural ectoderm

This is the function the gene is named for and the one the 2026 paper turns on.

Mouse `Otx2` nulls delete the entire forebrain and midbrain, and the defect is traced
to a *specification* failure during gastrulation, not to later degeneration
[PMID:7588062 "By 9.5 dpc, homozygous mutant embryos are characterized by the absence of
forebrain and midbrain regions"], with the authors concluding
[PMID:7588062 "These data suggest that Otx2 expression in endomesoderm and ectoderm is
required for anterior neuroectoderm specification"]. Independently replicated with
different alleles by Matsuo et al. [PMID:7590242] and Ang et al. [PMID:8565836], the
latter also showing gastrulation and axial-mesoderm defects — i.e. OTX2 acts earlier
than the neural plate proper.

The posterior limit of the OTX2 domain *is* the midbrain–hindbrain organizer. GBX2
represses OTX2 and positions that border
[PMID:10490024 "in Gbx2-/- mutants, the earliest phenotype is a posterior expansion of
the Otx2 domain during early somite stages"], and the relationship is instructive, not
merely correlative — ectopic GBX2 shifts the OTX2 border and a new organizer forms at
the new border
[PMID:10490024 "we transiently expressed Gbx2 in the caudal Otx2 domain and found that
the Otx2 caudal border was indeed shifted rostrally and a normal appearing organizer
formed at this new Otx2 border"]. Their conclusion
[PMID:10490024 "formation of a normal MHB organizer depends on a sharp Otx2 caudal
border and that Gbx2 is required to position and sharpen this border"].

This mutual-repression pair is exactly the aNE/pNE axis of
[PMID:42760324 "Two parallel brain progenitors emerge simultaneously during gastrulation:
anterior neural ectoderm (forebrain/midbrain progenitor) and posterior neural ectoderm
(hindbrain progenitor)"]. The new contribution is *commitment*: challenged with
hindbrain-inducing signals, human OTX2+ aNE does not convert
[PMID:42760324 "revealed these were lineage committed to forebrain/midbrain versus
hindbrain fates, respectively"], with a chromatin correlate
[PMID:42760324 "They harbored diverging chromatin landscapes foreshadowing future
forebrain/midbrain versus hindbrain identities"]. Conservation extends to hemichordates
[PMID:42760324 "these dual progenitors may be evolutionarily conserved across
550 million years from hemichordates to mammals"].

**Curation consequence.** GOA has `GO:0030900 forebrain development` and
`GO:0030901 midbrain development` only as **TAS from PMID:15705863**, a medulloblastoma
digital-karyotyping paper. The terms are right; the citation is thin (see §6). The much
better support is the mouse null series above, and there is no human-specific
experimental annotation for the anterior-patterning role at all — the strongest,
best-replicated OTX2 function is the one with the weakest evidence code in GOA. That is
worth saying out loud in the review.

### 3. Retina, RPE and pineal

Second well-established program, and the one behind the human ocular phenotypes.

Photoreceptor fate determination and pineal development, by conditional ablation
[PMID:14625556 "Otx2-deficiency converted differentiating photoreceptor cells to
amacrine-like neurons and led to a total lack of pinealocytes in the pineal gland"],
acting through CRX [PMID:14625556 "Otx2 transactivates the cone-rod homeobox gene Crx,
which is required for terminal differentiation and maintenance of photoreceptor cells"],
and sufficient as well as necessary [PMID:14625556 "retroviral gene transfer of Otx2
steers retinal progenitor cells toward becoming photoreceptors"].

In human RPE specifically, OTX2 drives RPE-restricted target genes. Direct promoter
occupancy and functional requirement for DCT
[PMID:12559959 "OTX2 binds to the DCT gene promoter in vivo, as judged by chromatin
immunoprecipitation assays"] and
[PMID:12559959 "Transient expression assays revealed that OTX2 activated the DCT gene
promoter through the OTX-2-binding site in an RPE-specific manner"]. This is the
experiment behind the human `GO:0000978` / `GO:0001228` / `GO:0045944` IDAs — a genuine,
human, promoter-level activator assay.

The second human RPE target is BEST1, where OTX2 works combinatorially rather than alone
[PMID:20530484 "SOX9 physically interacted with MITF and OTX2 and orchestrated
synergistic activation of the BEST1 promoter"]. Note this is the sole basis for the
`GO:0005515 protein binding`, `GO:0032991 protein-containing complex` and
`GO:0065003 protein-containing complex assembly` annotations — the interaction is real,
but "protein binding" is uninformative per project guidance and the complex terms are
generic restatements of the same co-activation result.

Human fetal expression is consistent and RPE-restricted at these stages
[PMID:19414065 "OTX2 was localized to the nuclei of retinal pigment epithelium"] — this
is the `GO:0005634 nucleus` EXP.

### 4. Hypothalamic → pituitary axis (non-cell-autonomous, via FGF10)

The mechanism is worth stating precisely because it is a case where OTX2's effect on
another tissue is mediated entirely by transcriptional control of a secreted ligand —
OTX2 itself is not secreted here. Patient-derived organoid work with R127W: reduced
hypothalamic FGF10 → reduced LHX3 in oral ectoderm → pituitary progenitor apoptosis,
rescued by CRISPR correction [PMID:31845906]. Human embryonic expression supports a
hypothalamic origin for the endocrine phenotype rather than an autonomous anterior-
pituitary defect [PMID:33950863].

This is the mechanistic basis on which a `regulation of fibroblast growth factor receptor
signaling pathway` annotation could be defended — but note GOA's actual citation for
`GO:0040036` is again PMID:15705863, not this work (§6).

### 5. Non-nuclear / moonlighting biology (homeoprotein transfer, eIF4E)

OTX2 is one of the homeoproteins that transfers between cells and engages the
translation machinery. Two strands:

**eIF4E binding.** Direct, demonstrated by GST pull-down with *human* OTX2 protein
[PMID:15247416 "we show that two other brain-expressed homeoproteins, Otx2 and Engrailed
2, also bind eIF4E, indicating that several homeoproteins may modulate eIF4E functions in
the developing and adult nervous system"]. Construct provenance confirms the human
protein was used [PMID:15247416 "Mouse Emx1, Emx2 (pCMV-Emx2), and human Otx2 cDNAs were
provided by A. Simeone"]. **This is the real evidence for `GO:0008190`, and it is not the
reference GOA cites.** See §6.

**Growth cone localization and axon turning.** In the Brunet et al. Engrailed-2 paper,
OTX2 was the specificity control and *was* assayed — so this is not a paralog
mis-attribution despite the title
[PMID:16267555 "we tested Otx2, another homeodomain transcription factor that shares the
secretion, internalization and eIF4E-binding properties of En-2"]. Internalization into
growth cones is positive [PMID:16267555 "FITC–Otx2 is internalized in retinal growth
cones (Fig. 2d)"], supporting `GO:0030426 growth cone`. But the guidance result is
explicitly *negative* for the property the assay was measuring
[PMID:16267555 "Thus, unlike En-2, Otx2 does not elicit opposite turning responses in the
two populations of retinal axons, indicating that En-2 acts specifically to induce these
divergent behaviours"] — OTX2 only "weakly attracted both the nasal and temporal
populations". Annotating human OTX2 to `GO:0007411 axon guidance` from the experiment
whose published conclusion is that OTX2 *lacks* the guidance behaviour is an
over-annotation. Flagging rather than removing: a weak bidirectional attraction was
measured, so the term is not flatly false.

**Critical-period plasticity.** The most important instance of transfer, though not
currently in GOA: visual experience drives non-cell-autonomous OTX2 accumulation in
cortical PV interneurons and this times the critical period
[PMID:18692473 "Visual experience promoted the accumulation of non-cell-autonomous Otx2
in PV-cells, and cortical infusion of exogenous Otx2 accelerated both PV-cell development
and critical period timing"], and it is required
[PMID:18692473 "conditional removal of Otx2 from non-PV cells or from the visual pathway
abolished plasticity"]. I considered proposing a NEW term here and decided against it —
see §7.

### 6. Reference problems found (the main QC finding of this review)

**Five annotations hang off one reference that probably does not support most of them.**
GOA has a block of five TAS annotations, all UniProt, all dated 20050607, all citing
PMID:15705863 (Boon, Eberhart & Riggins, *Genomic amplification of orthodenticle
homologue 2 in medulloblastomas*, Cancer Res 2005):

| term | plausible from that paper? |
|---|---|
| GO:0030900 forebrain development | yes — abstract does state the neuroectoderm role |
| GO:0030901 midbrain development | yes — same sentence |
| GO:0040036 reg. of FGFR signaling | not from the abstract; would be intro/discussion |
| GO:0008589 reg. of smoothened signaling | not from the abstract; would be intro/discussion |
| GO:0008190 eIF4E binding | **no** — and the real source is PMID:15247416 |

The paper is a digital-karyotyping/copy-number study; its abstract's only functional
statement is "OTX2 functions to specify the fate of neuroectoderm in various regions of
the developing brain". It is **not open access** (Europe PMC: `isOpenAccess: N`,
`inEPMC: N`), so I cannot read the intro/discussion to check whether the FGFR and
smoothened statements are traceable there. Per project policy I do not overrule a curator
on evidence I cannot see, so those two are kept and flagged rather than removed.

For `GO:0008190` the situation is different: I found affirmative evidence for the
*claim* in a different paper (PMID:15247416, human OTX2 GST pull-down), so the annotation
is scientifically sound and only its citation is wrong. Recorded as
`reference_review.replacement` on PMID:15705863 rather than by editing the GOA-supplied
`original_reference_id`.

**`GO:0071542 dopaminergic neuron differentiation` (TAS, PMID:24431302)** cites a Wnt
*review* (Arenas 2014, J Mol Cell Biol) — review-derived TAS, weaker than the companion
IGI from PMID:19951692, where OTX2 is genuinely part of the tested combination
(Lmx1a + Otx2 + FoxA2 synergy).

**`GO:0005634 nucleus` (IDA, PMID:24399192)** cites a hEPI-NCSC→dopaminergic-neuron
differentiation protocol paper. Nucleus is certainly right for OTX2, so this is
harmless, but the citation is incidental (OTX2 used as a marker), not a localization
study.

**ISS block (GO_REF:0000024, WITH UniProtKB:P80206 = mouse Otx2).** `GO:0090009 primitive
streak formation`, `GO:2000543 positive regulation of gastrulation`,
`GO:0040019 positive regulation of embryonic development`,
`GO:0045893 positive regulation of DNA-templated transcription`. The mouse source is
sound (Ang et al. gastrulation defects, PMID:8565836) and these are legitimate transfers,
but they sit at a much lower resolution than what is actually known — "positive regulation
of embryonic development" says almost nothing for a gene whose null deletes the forebrain.
Keeping as non-core; the informative content lives in the anterior-patterning terms.

### 7. NEW terms considered and rejected

Running the project's `NEW` discipline over the candidates:

- **Critical-period / PV-interneuron plasticity (PMID:18692473).** Tempting — the
  evidence is strong and the biology is distinctive. Rejected for this review because the
  work is mouse visual cortex with no human experimental counterpart, and because the
  cleanest candidate terms describe the *plasticity* process, which the PV interneuron
  network performs; OTX2's role is as the transferred signal that times it. Better raised
  as a `suggested_questions` item about whether a "homeoprotein transfer" representation
  exists, than asserted as human involvement.
- **`GO:0021999 neural plate anterior/posterior regionalization`.** This is the term the
  new paper is nominally about, and it is *not* on OTX2. Comparator check settles it
  against proposing: in mammals the term is annotated to CELSR2, NOG and SSBP3 (all IEA),
  and its experimental annotations are zebrafish `axin1`, `bptf`, `smad2`, `sfpq`,
  `sbno1` and `gsc` — morphogen and chromatin machinery, not regional selector
  transcription factors. A systematic absence across species and MODs is a convention, not
  a gap. The claim belongs in the module, where a developmental program is the right unit.
- **`GO:0009952 anterior/posterior pattern specification`.** Proposed, then withdrawn. The
  comparator evidence was good — mouse Otx2 carries it by both IMP and IGI, as does Hoxa1
  (IMP, IGI), and Gbx2 (`GO:0030917`) and Six3 (`GO:0021797`) carry terms that entail it,
  while the human orthologues GBX2, SIX3, EN1 and HOXA1 have none, which reads as a species
  artefact rather than a convention. The redundancy check is what killed it: human OTX2
  already carries `GO:0090009 primitive streak formation` by ISS, and an annotation to
  `GO:0090009` already entails `GO:0009952`, so proposing the latter would have added an
  ancestor of an existing annotation — which the project rules reject outright.
- **The `GO:0090009` → `GO:0009952` edge, stated precisely.** An earlier draft of the bullet
  above (and of the YAML `reason`, and of the `2026-09-20T163726Z` history record) called
  `GO:0090009` a *descendant* of `GO:0009952` without qualifying the relation. That wording
  was retracted on 2026-10-03, because the whole withdrawal rests on this single edge and
  the unqualified word is wrong for it. Queried against the local oaklib `sqlite:obo:go`
  `entailed_edge` closure — the same artefact the module validator resolves labels through,
  GO release 2026-07-26:
  - `GO:0090009` has exactly **one** `is_a` parent, `GO:0048646 anatomical structure
    formation involved in morphogenesis`, and its `is_a` closure contains no term in the
    regionalization branch. There is no `is_a` path to `GO:0009952`.
  - `GO:0009952` is reached from `GO:0090009` only through `BFO:0000050 part_of` (and
    `RO:0002131 overlaps`).
  - The same holds for `GO:0030917`, the term that *did* survive: it reaches `GO:0009952`
    through `BFO:0000050`, not `is_a`. `GO:0021797` is the one genuine `rdfs:subClassOf`
    descendant of the four checked.
  The conclusion is unchanged, because GO's true-path rule propagates annotations over
  `part_of` as well as `is_a`: an annotation to `GO:0090009` entails `GO:0009952` either
  way. Recorded because an `is_a`-only reading of the closure would make `GO:0009952` look
  proposable, and that reading was argued four times across review passes before the
  closure was actually queried.
- **`GO:0021978 telencephalon regionalization`.** Mouse Otx2 carries it by IMP. Rejected on
  the same ground: it reaches `GO:0030900 forebrain development`, which human OTX2 already
  has, by `BFO:0000050` (it is not under `GO:0009952` at all).
- **`GO:0030917 midbrain-hindbrain boundary development` — this one survived, and is
  proposed.** The claim is narrower and better grounded than the AP-patterning one: the
  organizer forms *at* the OTX2 caudal border, and moving that border with ectopic GBX2
  moves the organizer [PMID:10490024 "we transiently expressed Gbx2 in the caudal Otx2
  domain and found that the Otx2 caudal border was indeed shifted rostrally and a normal
  appearing organizer formed at this new Otx2 border"]. Comparator check is favourable
  rather than merely neutral — queried against QuickGO, `GO:0030917` has 8 experimental
  annotations in mouse (Gbx2, Fgf8, Wnt1, En1, Lrp6, all IMP) and 138 in zebrafish, so GO
  does not withhold it from this class of gene. Redundancy check passes: checked against all
  37 OTX2 annotations in the `part_of`-inclusive closure, only the self-match comes back;
  `GO:0030900` and `GO:0030901` are siblings of `GO:0030917` under `GO:0007420 brain
  development`, which OTX2 does not itself carry.
- **The `GO:0030917` ISS donor was wrong, and the qualifier was too strong.** Both found on
  2026-10-04 after a reviewer asked whether the `ISS WITH` actually pointed at a holder of
  the term. It did not.
  - **Donor.** The row cited `UniProtKB:P80206` (mouse Otx2). QuickGO returns **zero**
    `GO:0030917` annotations for P80206 — and zero for human P32243 — so the `WITH` named a
    gene that does not carry the term, which is not a transfer at all. The actual holders
    among the orthologues are zebrafish: `otx2` (`UniProtKB:Q91981`, Swiss-Prot), `otx2a`
    and `otx2b`, all IGI from [PMID:16611693]. The donor is now Q91981, the reviewed entry.
    My earlier note said "zebrafish `otx2a`, by IGI" — the right species and evidence code,
    but the paralog I named is a TrEMBL entry when a reviewed one carrying the same
    annotation exists.
  - **Qualifier.** The row said `involved_in`. All 146 experimental `GO:0030917` rows in
    mouse and zebrafish use `acts_upstream_of_or_within`; every `involved_in` row on the term
    is IEA/ARBA. An ISS must not strengthen what it transfers, and this one was doing exactly
    that. Now `acts_upstream_of_or_within`, which is also what the project's own `NEW` rule
    requires: the boundary structure is built by the isthmic organizer genes, and what OTX2
    contributes is *where* it forms. The zebrafish paper puts it well — loss of Otx function
    turns the presumptive midbrain into extended r1 [PMID:16611693 "lack of Otx function in
    zebrafish leads to transformation of the presumptive mesencephalon into an extended
    rhombomere 1 (r1)"], and Fgf8 only *maintains* the boundary that the Otx domain defines
    [PMID:16611693 "Fgf8 is required to maintain, rather than induce, the posterior boundary
    of Otx expression."].
  - Consequence for `core_functions`: `GO:0030917` is deliberately **not** in
    `directly_involved_in`, since listing it there would re-assert the participation the
    annotation now declines to claim. The border-positioning role stays in the prose.
  - Worth recording because the error was invisible to every check that ran. The term id and
    label were right, the comparator argument was right, the mechanism was right, and the
    donor accession was a real mouse Otx2 entry — so schema validation, label validation and
    the redundancy check all passed. Only asking "does the `WITH` gene actually carry this
    term?" catches it, and nothing in the pipeline asks that.
- **Anything medulloblastoma.** Oncogenic re-expression (PMID:21964830, PMID:28213356,
  PMID:32686664, PMID:39025928) is disease biology, not normal gene function. The
  chromatin/enhancer work (PMID:28213356) and the LASR/splicing work (PMID:39025928) are
  mechanistically interesting and I cite them in `references`, but they establish what
  OTX2 can do when aberrantly retained in a tumour, not a normal-physiology process term.

### 8. Open questions for experts

Carried into `suggested_questions` / `suggested_experiments`:

- Is the eIF4E-binding activity used physiologically by OTX2, or is it a shared
  homeodomain-family property with no OTX2-specific readout?
- Should the GOA TAS block from PMID:15705863 be re-refereed by UniProt? Three of the
  five look unsupported by the cited paper.
- Does human OTX2 have a demonstrable role at the aNE stage that could be annotated
  directly, now that PMID:42760324 provides a human in-vitro system?
