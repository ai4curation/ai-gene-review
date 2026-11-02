# AMDHD1 (Q96NU7) review notes

Human gene **AMDHD1** = amidohydrolase domain-containing protein 1 = **probable
imidazolonepropionase** (EC 3.5.2.7). UniProt entry name HUTI_HUMAN. HGNC:28577,
GeneID 144193, chromosome 12.

## Core enzymatic function (from UniProt Q96NU7, authoritative)

AMDHD1 catalyses the **third step of the universal histidine degradation pathway**:
hydrolytic cleavage of the C–N bond in 4-imidazolone-5-propanoate to form
N-formimidoyl-L-glutamate (= N-formimino-L-glutamate).

- FUNCTION: "Catalyzes the hydrolytic cleavage of the carbon-nitrogen bond in
  imidazolone-5-propanoate to form N-formimidoyl-L-glutamate. This reaction
  represents the third step of the universal histidine degradation pathway."
  [file:human/AMDHD1/AMDHD1-uniprot.txt]
- CATALYTIC ACTIVITY: "Reaction=4-imidazolone-5-propanoate + H2O =
  N-formimidoyl-L-glutamate; ... EC=3.5.2.7" [file:human/AMDHD1/AMDHD1-uniprot.txt]
- PATHWAY: "Amino-acid degradation; L-histidine degradation into L-glutamate;
  N-formimidoyl-L-glutamate from L-histidine: step 3/3."
  [file:human/AMDHD1/AMDHD1-uniprot.txt]

The catalytic-activity and EC assignments in the human entry are propagated by
similarity (ECO:0000250|UniProtKB:P42084 = HUTI_BACSU, the characterised *Bacillus
subtilis* HutI ortholog; the other two donors in the feature table are A0KF84 =
HUTI_AERHH, *Aeromonas hydrophila*, and Q8U8Z6 = HUTI_AGRFC, *Agrobacterium fabrum*);
hence UniProt labels the human protein "**Probable**
imidazolonepropionase" and Reactome notes the human enzyme's existence is inferred
from high-throughput screening (Yamada et al. 2004) rather than direct human enzyme
assay [reactome:R-HSA-70906]. The activity is nonetheless strongly supported by
family membership and phylogeny (IBA to GO:0050480 by GO_Central).

### Metal cofactor / metal binding

- COFACTOR: "Name=Zn(2+) ... Name=Fe(3+) ... Note=Binds 1 zinc or iron ion per
  subunit." [file:human/AMDHD1/AMDHD1-uniprot.txt]
- Metal-coordinating residues by similarity: BINDING 260 and BINDING 334 each ligate
  Fe(3+)/Zn(2+) — the Zn lines carry `ECO:0000250|UniProtKB:P42084`, the Fe lines
  `ECO:0000250|UniProtKB:A0KF84` [file:human/AMDHD1/AMDHD1-uniprot.txt].
  Substrate-binding residues 159, 192, 263; residues 159 and 336 bind the *product*
  N-formimidoyl-L-glutamate (`ECO:0000250|UniProtKB:Q8U8Z6`)
  [file:human/AMDHD1/AMDHD1-uniprot.txt].
- SIMILARITY: "Belongs to the metallo-dependent hydrolases superfamily. HutI family."
  [file:human/AMDHD1/AMDHD1-uniprot.txt]

So the enzyme is a **Zn/Fe metal-dependent amidohydrolase** (metallo-dependent
hydrolase superfamily, cd01296 Imidazolone-5PH; Pfam PF01979 Amidohydro_1). Metal
ion binding is well supported, but the *identity* of the metal is not: UniProt lists
Zn(2+) and Fe(3+) as two `COFACTOR` entries at equal evidential strength (both
`ECO:0000250|UniProtKB:P42084`), the Note reads "Binds 1 zinc or iron ion per
subunit", and residues 260/334 each carry a BINDING line for either metal. COFACTOR
order is not a ranking, so **GO:0046872 metal ion binding** is the term used in
core_functions rather than GO:0008270 zinc ion binding or GO:0005506 iron ion
binding — it asserts exactly what the source asserts. GOA carries *no* metal-binding
term for AMDHD1 at all — neither GO:0046872 nor either child — so as of 2026-10-09
GO:0046872 is also proposed as an `action: NEW` annotation with ISS evidence (see the
compliance-pass entry below for the comparator check that justifies it). Substitute
the specific child term once the human enzyme's metal content is measured.

## Localization

- SUBCELLULAR LOCATION: "Cytoplasm {ECO:0000269|PubMed:39143229}."
  [file:human/AMDHD1/AMDHD1-uniprot.txt] — experimental (cholangiocarcinoma paper).
- Reactome places the reaction in cytosol (GO:0005829, TAS) [reactome:R-HSA-70906].
- GOA has cytoplasm (GO:0005737, IEA UniProtKB-SubCell) and cytosol (GO:0005829, TAS
  Reactome). Both consistent; cytosol is the more precise soluble-enzyme location.

## Histidine catabolism pathway context

Reactome R-HSA-70921 "Histidine catabolism": His → urocanate (HAL/histidase) →
4-imidazolone-5-propanoate (UROC1/urocanase) → **N-formimino-L-glutamate (AMDHD1,
step 3)** → glutamate + formimino-THF (FTCD). AMDHD1 is the third of four steps.
[reactome:R-HSA-70921 summary: "proceeds in four steps to yield glutamate"]

GOA carries two UniPathway-derived BP variants:
- GO:0019556 L-histidine catabolic process to glutamate and formamide (IEA UniPathway)
- GO:0019557 L-histidine catabolic process to glutamate and formate (IEA UniPathway)
These two describe the two alternative downstream fates of the formimino/formamido
group; they are pathway-variant descriptors auto-emitted from the UniPathway mapping.
The parent/experimentally-supported BP is GO:0006548 L-histidine catabolic process
(IBA + TAS Reactome). NOTE: GO:0019556/GO:0019557 are NOT seeded in the ai-review
YAML (they are in the UniProt DR block but not in the GOA TSV rows), so no review row
is required for them; they are mentioned here for completeness.

## Secondary / moonlighting function (single paper)

PubMed:39143229 (Ma et al., Cell Death Differ 2025) reports AMDHD1 as a tumor
suppressor in cholangiocarcinoma that promotes TGF-beta signaling by stabilizing
SMAD4 (inhibiting its ubiquitination/proteasomal degradation) and enhancing SMAD2/3
phosphorylation; it interacts with SMAD2, SMAD3, SMAD4 [file:human/AMDHD1/AMDHD1-uniprot.txt
FUNCTION + SUBUNIT]. This paper is NOT cached locally (abstract not in publications/)
and is a single primary report; the TGF-beta/tumor-suppressor role is not (yet) an
existing GO annotation in the GOA TSV, so it does not require an annotation-review
row. It informs the description as a secondary/putative moonlighting activity but is
kept out of core_functions (single study, mechanism = adaptor/stabilizer, not the
defining enzymatic function).

## Protein-binding (IPI) annotations — KLHL23

Two GO:0005515 "protein binding" IPI rows, both with_from UniProtKB:Q8NBE8 (=KLHL23),
from the BioPlex AP-MS interactome papers:
- PMID:28514442 (BioPlex 2.0, Huttlin 2017) [publications/PMID_28514442.md]
- PMID:33961781 (BioPlex 3.0, Huttlin 2021) [publications/PMID_33961781.md]
UniProt IntAct: "Q96NU7; Q8NBE8: KLHL23; NbExp=3" [file:human/AMDHD1/AMDHD1-uniprot.txt].
Both are proteome-scale HA-FLAG AP-MS screens (HEK293T/HCT116); neither paper mentions
AMDHD1 specifically or assigns it a function — AMDHD1 is one of thousands of
bait/prey entries. KLHL23 is a Kelch-like BTB adaptor; no defined biological meaning
for AMDHD1's metabolic role. Both are marked **REMOVE** (revised 2026-10-09; they
were MARK_AS_OVER_ANNOTATED until then). The generic-protein-binding policy
excludes MARK_AS_OVER_ANNOTATED for GO:0005515 by name — the defect is absence of
functional information, not a claim exceeding the evidence — and `just validate`
warns on it. Removal does **not** assert the interaction is false; it is
reproduced across both screens with NbExp=3. MODIFY is unavailable because neither
screen tests whether AMDHD1 is a CUL3–KLHL23 substrate, so no more informative MF
is supportable. Kept out of core_functions per curation guideline (avoid bare
protein binding).

## Evidence-code summary for review actions

- IBA GO:0050480 imidazolonepropionase activity → ACCEPT (core MF; phylogenetically
  supported, matches UniProt EC and family).
- IBA GO:0006548 L-histidine catabolic process → ACCEPT (core BP).
- IEA GO:0050480 (RHEA/EC) → ACCEPT (redundant with IBA but correct catalytic MF).
- IEA GO:0016787 hydrolase activity; GO:0016810 (C-N bonds); GO:0016812 (cyclic
  amides) → these are correct-but-general ancestors of GO:0050480. MODIFY →
  GO:0050480 (the specific catalytic term is available and evidenced).
- TAS GO:0016812 (Reactome) → same generalization; MODIFY → GO:0050480.
- GO:0006548 IEA (InterPro) and TAS (Reactome) → ACCEPT (correct BP).
- GO:0005737 cytoplasm IEA and GO:0005829 cytosol TAS → cytosol is more precise;
  cytosol ACCEPT (core location); cytoplasm KEEP_AS_NON_CORE (correct parent, and
  the granularity at which UniProt's experimental SUBCELLULAR LOCATION line asserts
  it, so not MODIFY).
- GO:0003674 molecular_function ND (root, GO_REF:0000015) → this is the
  "no-data" placeholder now superseded by real MF annotations. REMOVE (ND root
  placeholder is obsolete once informative MF exists; it is not experimental).
- GO:0008270 zinc ion binding → NEW (ISS), added 2026-10-09; not in GOA.

## Core functions selected

1. GO:0050480 imidazolonepropionase activity (catalytic MF)
2. GO:0046872 metal ion binding (catalytic metal cofactor; Zn or Fe, see above)
3. GO:0006548 L-histidine catabolic process (BP)

## 2026-10-09 — weekly compliance pass

Evidence-aware compliance (`just compliance-all`) had AMDHD1 at 44.44 weighted.
Almost all of the deficit was missing justification/provenance rather than wrong
biology. Changes:

- **`review.reason` added to all 14 pre-existing annotations.** For each generic
  hydrolase row the reason now names the InterPro signature that actually fired,
  which is what makes those rows subsumed-but-true: **IPR006680** (Amidohydro_1,
  Pfam-level, shared across the whole metallo-dependent hydrolase superfamily) →
  GO:0016787; **IPR011059** (metal-dependent hydrolase composite domain) →
  GO:0016810; **IPR005920** (family-specific imidazolonepropionase) → the correct
  GO:0006548. The one InterPro2GO row that is accepted and the two that are
  modified differ precisely in signature specificity.
- **GO:0005515 ×2 migrated `MARK_AS_OVER_ANNOTATED` → `REMOVE`.** `just validate`
  warned on both; the generic-protein-binding policy excludes
  MARK_AS_OVER_ANNOTATED for GO:0005515 by name. MODIFY was not available:
  KLHL23 (Q8NBE8) is a Kelch/BTB adaptor, but neither BioPlex screen tests whether
  AMDHD1 is a CUL3 substrate, so a substrate-recognition term would exceed the
  evidence. The one paper that gives AMDHD1 a protein-stabilising role names
  SMAD2/3/4, *not* KLHL23, so it licenses nothing here either. Reasons state
  explicitly that removal does not assert the interaction is false (NbExp=3).
- **NEW annotation: GO:0046872 metal ion binding (ISS).** This closes the
  pre-existing `just validate` warning that `core_functions[1]` was not reflected
  in `existing_annotations`. The NEW bar is met on the cofactor reading: AMDHD1's
  own side chains hold the metal (BINDING 260, BINDING 334, each annotated for
  both Zn(2+) and Fe(3+)), and that metal is the Lewis acid activating water for
  C–N hydrolysis — the protein does the binding, so this is not a
  necessity-only relationship.
  **Comparator check run before proposing** (per CLAUDE.md): the *P. putida* HutI
  ortholog carries both GO:0008270 and GO:0005506 (IEA, GO_REF:0000104), and human
  ACMSD — same metallo-dependent hydrolase superfamily — carries GO:0008270 by IDA
  ×2. Metal binding is the family convention, so AMDHD1's absence is a coverage gap
  in the UniProt cofactor pipeline for this entry, not a curatorial decision.
  Evidence is ISS, not IDA: cofactor and both ligating residues are
  ECO:0000250 by similarity (Zn sites from P42084, Fe sites from A0KF84).
- **`findings` added to all 9 references**, including four on the UniProt entry
  itself. Verbatim `supporting_text` where a source exists; the four GO_REF
  findings are statement-only because GO_REF documents are not cached and any
  quote would be unverifiable.
- **4 `suggested_questions` and 3 `suggested_experiments`** where there were none.
  The central one is the gap this review kept running into: the human enzyme has
  never been purified or assayed. UniProt says "**Probable** imidazolonepropionase"
  and Reactome is candid that "existence of the human enzyme is inferred only from
  high-throughput screening studies" [Reactome:R-HSA-70906]. The proposed
  experiment pairs recombinant kinetics with ICP-MS metal quantification, which
  would settle both the activity and the Zn/Fe question at once.

Result: 44.44 → **92.00** weighted, `just validate` clean (all three prior
warnings resolved). Remaining gaps are deliberate: four GO_REF
`findings[].supporting_text` slots (nothing citable), and `literature_support` on
the three Reactome TAS rows — the rule requires a `PMID:`/`DOI:` quote and no
primary paper in this review assays the human enzyme or its localization. Padding
either would mean inventing provenance.

## 2026-10-19 — review response (PR #4448)

The `CHANGES_REQUESTED` review raised one blocking item and three suggestions. All
four are addressed; every claim below was re-derived from the sources rather than
taken from the review.

- **Blocking — the metal was over-specified.** The `NEW` row and
  `core_functions[1]` asserted **GO:0008270 zinc ion binding**, resolved from
  UniProt's two `COFACTOR` entries by treating the listed order as a ranking. It is
  not. `Name=Zn(2+)` and `Name=Fe(3+)` both carry `ECO:0000250|UniProtKB:P42084`,
  the Note reads "Binds 1 zinc or iron ion per subunit", and residues 260 and 334
  each have a `BINDING` line for *either* metal (Zn from P42084, Fe from A0KF84)
  [file:human/AMDHD1/AMDHD1-uniprot.txt]. The review also noted that the comparator
  argued against the narrower claim: the *P. putida* HutI ortholog carries **both**
  GO:0008270 and GO:0005506, so if family convention is the warrant it covers both
  metals. Both slots now assert **GO:0046872 metal ion binding**, which is exactly
  what the source asserts, with the Zn-vs-Fe specifics kept in `review.reason` and
  in `suggested_questions`. `supporting_entities` gained `UniProtKB:A0KF84`
  alongside P42084, since the Fe site assignments come from A0KF84. GOA carries
  neither GO:0046872 nor either child, so `action: NEW` still stands.
- **Suggestion 1 — the Q9HU91 genus.** Resolved against UniProt: **Q9HU91 =
  HUTI_PSEAE, *Pseudomonas aeruginosa* PAO1** imidazolonepropionase. The
  "Pseudomonas/Agrobacterium enzyme" phrasing in the GO:0006548 reason was wrong —
  one accession cannot be both — and is now pinned to *P. aeruginosa*. While
  checking, the same error turned up in these notes: P42084 was described as the
  "*Agrobacterium*/bacterial" ortholog, but **P42084 = HUTI_BACSU, *Bacillus
  subtilis***. *Agrobacterium fabrum* is **Q8U8Z6 = HUTI_AGRFC**, the donor for the
  product-binding sites, and **A0KF84 = HUTI_AERHH, *Aeromonas hydrophila***
  supplies the Fe sites. All three are now named correctly above.
- **Suggestion 2 — residue 336 binds the product, not the substrate.** Confirmed
  from the `FT` block: 159 and 336 bind `N-formimidoyl-L-glutamate`
  (`ECO:0000250|UniProtKB:Q8U8Z6`), so the substrate-only sites are 159, 192 and
  263. The GO:0050480 reason and the metal-cofactor section are corrected.
- **Suggestion 3 — provenance for "liver and skeletal muscle".** It does exist, in
  the UniProt cross-references rather than in a `TISSUE SPECIFICITY` line:
  `DR   HPA; ENSG00000139344; Tissue enhanced (liver, skeletal muscle).`
  [file:human/AMDHD1/AMDHD1-uniprot.txt]. Recording it here, as the review asked,
  so the qualifier in `description` and `suggested_questions[0]` is anchored. Note
  this is an expression-atlas cross-reference, not a curated statement tied to a
  publication, so it supports where the transcript is enriched and nothing about
  where the enzyme is catalytically active.
- **Suggestion 4** (follow up on the uncached Reactome "Yamada et al. 2004"
  citation and backfill the three TAS `literature_support` slots) agrees with the
  existing deliberate gap and is left for a follow-up PR; nothing here invents a
  PMID for it.
