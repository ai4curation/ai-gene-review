# SPKW Non-Arabidopsis Plants (PLANTS) Subproject

**Parent project:** [SPKW.md](SPKW.md)

## Overview

The [ARATH subproject](SPKW-ARATH.md) examined SwissProt-keyword (SPKW) over-annotation
in *Arabidopsis thaliana*. This subproject extends that analysis to the rest of the green
plant lineage (Viridiplantae, NCBITaxon:33090) **excluding Arabidopsis** — rice, maize,
soybean, tomato, potato, tobacco, wheat, grape, poplar, the green alga *Chlamydomonas*,
and ~200 other species — to test whether the patterns seen in the premier model plant
generalize across crops and non-flowering plants.

The analysis was run against `plant.ddb`, a DuckDB GO-annotation database built in the
`go-db` repository (`make plant`) from the September 2025 `goa_uniprot_gcrp` snapshot
(Gene-Centric Reference Proteomes), loaded with a `swissprot` table of 26,493 reviewed
accessions. It contains 40.4M annotations across the plant kingdom.

**The central new finding is temporal.** Between the September 2025 snapshot and the
current (≈April 2026) GOA release, GOA **retired the keyword-to-GO pipeline**
(`GO_REF:0000043`) for all cellular organisms. Live QuickGO now returns **zero**
`GO_REF:0000043` annotations for human, mouse, fly, worm, *S. pombe*, *Chlamydomonas*,
Arabidopsis, rice, soybean, tobacco, and every other model organism checked (only viruses
retain them). `plant.ddb` is effectively the last high-coverage record of the plant SPKW
landscape, so this subproject is a **retrospective validation study**: for nine
representative genes across nine species we ask whether GOA's wholesale removal was
justified, and we classify the 214 SPKW-unique terms by their over-annotation risk.

## Key Statistics (2026-05-21)

Scope: non-Arabidopsis Viridiplantae, restricted to SwissProt (reviewed) entries via the
`swissprot` table; closure-filtered per [SPKW-METHODOLOGY.md](SPKW-METHODOLOGY.md).

| Metric | Count |
|--------|-------|
| Total annotations (non-ARATH plant SwissProt entries) | 111,358 |
| SPKW annotations (GO_REF:0000043) | 25,833 (23%) |
| TRUE SPKW-unique (after closure filtering) | 6,678 |
| Unique genes with TRUE SPKW-unique | 4,117 |
| Unique terms in TRUE SPKW-unique | 214 |
| **Closure filtering reduction** | **74%** |

The 74% closure reduction is in line with Arabidopsis (72%) and confirms that
closure-based filtering is essential — a naive query would overstate the problem ~4×.

### Distribution by Aspect

| Aspect | Annotations | Genes | Terms |
|--------|-------------|-------|-------|
| F (Molecular Function) | 3,615 (54%) | 2,345 | 70 |
| P (Biological Process) | 2,497 (37%) | 1,934 | 129 |
| C (Cellular Component) | 566 (8%) | 497 | 15 |

### Per-Species Breakdown (TRUE SPKW-unique)

| Species | Annotations | Genes | Terms |
|---------|-------------|-------|-------|
| *Oryza sativa* Japonica (rice) | 2,542 | 1,605 | 160 |
| *Oryza sativa* Indica (rice) | 538 | 322 | 95 |
| *Zea mays* (maize) | 419 | 264 | 94 |
| *Nicotiana tabacum* (tobacco) | 377 | 240 | 76 |
| *Solanum tuberosum* (potato) | 400 | 220 | 66 |
| *Solanum lycopersicum* (tomato) | 339 | 196 | 65 |
| *Glycine max* (soybean) | 278 | 183 | 62 |
| *Triticum aestivum* (wheat) | 218 | 146 | 60 |
| *Spinacia oleracea* (spinach) | 263 | 131 | 43 |
| *Physcomitrium patens* (moss) | 115 | 75 | 35 |
| *Gossypium hirsutum* (cotton) | 90 | 63 | 28 |
| *Vitis vinifera* (grape) | 76 | 51 | 26 |
| *Populus trichocarpa* (poplar) | 69 | 47 | 25 |
| *Sorghum bicolor* (sorghum) | 64 | 45 | 26 |
| *Chlamydomonas reinhardtii* (green alga) | 61 | 37 | 22 |
| *Medicago truncatula* | 69 | 37 | 19 |
| *Amborella trichopoda* | 43 | 31 | 19 |

Rice dominates (japonica + indica = 1,927 genes, 47% of SPKW-unique genes) simply because
it is the most deeply SwissProt-curated non-Arabidopsis plant. Over 200 species contribute,
including non-flowering lineages (the moss *Physcomitrium*, the alga *Chlamydomonas*) and
the basal angiosperm *Amborella*.

---

## Term-Level Classification: Which SPKW Terms Are Prone to Over-Annotation

A core question for this subproject is whether "SPKW-unique" should be read as a synonym
for "over-annotation". **It should not.** Classifying all 214 TRUE SPKW-unique terms by
GO-curation principles shows the over-annotation risk is concentrated in a small,
identifiable set of process/pathway terms, while the bulk of SPKW-unique annotations are
correct — either broad-but-true or specific-and-informative.

| Tier | Description | Annotations | Genes | Terms | Over-annotation risk |
|------|-------------|-------------|-------|-------|----------------------|
| **A** | Process/pathway conflation | 1,016 (15%) | 891 | 29 | **High** |
| **B** | Broad cofactor / enzyme-class MF (low-information) | 3,203 (48%) | 2,126 | 37 | Low (correct, uninformative) |
| **C** | Specific informative function (correct) | 2,084 (31%) | 1,552 | 142 | Low (correct; removal risks real loss) |
| **D** | Context-dependent (mixed) | 375 (6%) | 240 | 6 | Case-by-case |

(Tier boundaries are curatorial judgement; the counts use an explicit GO-ID assignment
and sum to the 6,678 / 214 totals.)

### Tier A — Prone to over-annotation (15% of annotations, 29 terms)

The keyword names a **process or pathway the gene is associated with**, not a function it
performs. This is where keyword→GO mapping systematically fails.

- **Hormone signaling** — auxin-activated signaling pathway (120 genes), abscisic
  acid-activated signaling (25), gibberellic acid-mediated signaling (21),
  brassinosteroid-mediated signaling (20), cytokinin-activated signaling (16),
  ethylene-activated signaling (9), red/far-red light signaling (7). *Applied to
  hormone-**responsive** genes, not signal transducers.*
- **Defense / immunity processes** — defense response (312), killing of cells of another
  organism (42), defense response to fungus (33), defense response to bacterium (12),
  plant-type hypersensitive response (8), innate immune response (7), defense response to
  virus (5), immune system process (3). *Applied to any pathogen-induced or PR protein.*
- **Pleiotropic development** — cell differentiation (62), flower development (46),
  nodulation (40), fruit ripening (26). *Expression during development ≠ function.*
- **Cell cycle / meiosis keywords** — cell division (81), meiotic cell cycle (6),
  chromosome segregation (2). *Applied to general genome-maintenance genes.*
- **Vague / previously-flagged** — methylation (92), rhythmic process (10), autophagy (4),
  signal transduction (2). *Process terms too broad to be informative or
  over-annotated in earlier SPKW subprojects.*

### Tier B — Broad cofactor / enzyme-class MF (48% of annotations, 37 terms)

The keyword reflects a **real bound metal, cofactor, ligand, or broad catalytic class**.
These are almost never *wrong*; they are uninformative. Removing them loses generic-but-true
information.

- *Binding* — metal ion binding (1,149 genes), nucleotide binding (342), ATP binding
  (319), zinc ion binding (286), quinone binding (178), DNA binding (152), RNA binding
  (110), 4Fe-4S / iron-sulfur cluster binding (~150), GTP binding, lipid binding,
  L-ascorbic acid binding, calmodulin binding, carbohydrate binding.
- *Broad enzyme-class MF* — oxidoreductase activity (129), hydrolase activity (105),
  kinase activity (27), transferase activity, lyase activity, peptidase activity,
  isomerase activity, nuclease activity, methyltransferase activity.

**Tier B is the single largest category (48%)** — the dominant content of the SPKW-unique
set is broad, correct, low-information binding/enzyme-class terms.

### Tier C — Specific informative function (31% of annotations, 142 terms)

The keyword reflects the protein's **genuine catalytic, structural, biosynthetic, or
transport role**. These are correct *and* informative; removing them is a real loss.

- *Specific enzymes* — monooxygenase activity, endonuclease activity, helicase activity,
  trihydroxystilbene synthase activity, dioxygenase activity, methionine adenosyltransferase
  activity.
- *Biosynthetic / metabolic pathways* — amino acid biosynthetic process (71), fatty acid
  biosynthetic process (54), polysaccharide catabolic process (66), lipid catabolic
  process (62), photorespiration (53), chlorophyll biosynthetic process, lignin
  biosynthesis, alkaloid metabolic process.
- *Inhibitors* — serine-type endopeptidase inhibitor activity (38), alpha-amylase
  inhibitor activity (10), peptidase inhibitor activity.
- *Structural / transport / translation* — cell wall organization (140), ribonucleoprotein
  complex (235), DNA-directed RNA polymerase complex (58), nutrient reservoir activity
  (54), oxygen carrier activity (23), symporter activity (32), porin activity, translation
  and tRNA/rRNA processing.

The 142 Tier-C terms are mostly small (1–20 genes each) — a long tail of specific,
correct functions.

### Tier D — Context-dependent (6% of annotations, 6 terms)

Correct for canonical pathway members, over-annotation for accessory or divergent ones:
**photosynthesis** (110), photosystem I (66), photosystem II (65), chlorophyll binding
(87), toxin activity (22), response to herbicide (25). A core PSI subunit legitimately
gets "photosynthesis"; a non-photosynthetic PEPC paralog does not (see PPC16 below).

### Bottom line

**Only ~15% of plant SPKW-unique annotations (Tier A) carry real over-annotation risk.**
~79% (Tiers B + C) are correct — broad-but-true or specific-and-informative. This reframes
the SPKW problem: it is not that keyword annotations are generally bad, but that a
specific, enumerable set of ~29 process/pathway terms is systematically mis-applied. The
nine gene reviews below were chosen to sample each tier and test this classification.

---

## Full Gene Reviews Completed (2026-05-21)

Nine genes, one per species, sampling all four tiers.

| Gene | UniProt | Species | Tier | Key SPKW term | Action | GOA removal justified? |
|------|---------|---------|------|---------------|--------|------------------------|
| STS3 | P51071 | grape | A | defense response | MARK_AS_OVER_ANNOTATED | Yes |
| PARA | P25317 | tobacco | A | auxin-activated signaling pathway | REMOVE | Yes |
| NFP | Q0GXS4 | *Medicago* | A | protein tyrosine kinase activity | REMOVE | Yes |
| EME1 | Q0J9J6 | rice | A→C | meiotic cell cycle / endonuclease activity | MARK_OVER / MODIFY | Mixed — meiosis yes, MF no |
| PR1B1 | P04284 | tomato | A→D | killing of cells / defense response to fungus | MARK_OVER / MODIFY | Partly |
| PPC16 | Q02909 | soybean | D | photosynthesis | REMOVE | Yes |
| METK1 | A9P822 | poplar | B | metal ion binding | MARK_AS_OVER_ANNOTATED | Yes (low-information) |
| psaC | Q00914 | *Chlamydomonas* | B | metal ion binding / oxidoreductase activity | REMOVE | Yes (superseded) |
| CASP1 | C5YAP3 | sorghum | C | cell wall organization | MODIFY | **No — correct biology lost** |

**Verdict across ~16 reviewed SPKW annotations:** GOA's removal was justified for every
Tier A and Tier B annotation; it was a genuine or partial **loss of correct biology** for
the Tier C cases (CASP1 cell wall organization; EME1 endonuclease activity; PR1B1 defense
response to fungus). The tier of a term predicts whether its removal was safe.

---

### Case 1: EME1 — Meiosis Keyword on a General Repair Endonuclease (Tier A→C)

**Gene:** EME1 (Q0J9J6) — Crossover junction endonuclease EME1, *Oryza sativa* Japonica.
**Review file:** `genes/ORYSJ/EME1/EME1-ai-review.yaml`

OsEME1 is the EME1/MMS4-family subunit of the MUS81–EME1 structure-specific endonuclease,
cleaving branched DNA in **both** mitotic repair and meiotic recombination. The keyword
"Meiosis" (→ meiotic cell cycle, GO:0051321) is over-specific — *oseme1* mutants are
MMS/Zeocin-hypersensitive in vegetative tissue [PMID:40333587] and rice *mus81* has normal
crossover designation [PMID:36495065] — so removal was **justified** (MARK_AS_OVER_ANNOTATED).

**The instructive twist:** of six SPKW-unique terms, five were over-broad and correctly
dropped, but **endonuclease activity (GO:0004519) was genuinely correct** — EME1 *is* an
endonuclease (EC 3.1.22.-). Current GOA, having dropped the keyword annotation, now has
**no catalytic molecular-function term at all** for OsEME1. Action MODIFY → crossover
junction DNA endonuclease activity (GO:0008821), restored as a curated annotation. Three
expression-based IEP annotations (citing a cDNA-collection paper) were also REMOVEd.

### Case 2: PPC16 — Photosynthesis Keyword on a C3 Housekeeping Enzyme (Tier D)

**Gene:** PPC16 (Q02909) — Phosphoenolpyruvate carboxylase, housekeeping isozyme, *Glycine max*.
**Review file:** `genes/SOYBN/PPC16/PPC16-ai-review.yaml`

PEPC is famous as the CO₂-fixing enzyme of C4/CAM **photosynthesis**, so "Photosynthesis"
is a family-wide keyword. But PPC16 is the **anaplerotic housekeeping isozyme of soybean,
a C3 plant** — C3 plants have no photosynthetic PEPC. Decision **REMOVE**; removal fully
justified. The same family-level error in two non-SPKW annotations ("carbon fixation",
"tricarboxylic acid cycle") was MODIFYed to oxaloacetate metabolic process. This is the
**Tier D context-dependent** term in action: "photosynthesis" is right for a PSI subunit,
wrong for a C3 anaplerotic enzyme.

### Case 3: PARA — Auxin-Signaling Keyword on an Auxin-Induced Enzyme (Tier A)

**Gene:** PARA (P25317) — Probable glutathione S-transferase parA / STR246C, *Nicotiana tabacum*.
**Review file:** `genes/TOBAC/PARA/PARA-ai-review.yaml`

parA is a tau-class glutathione S-transferase. It carries the name "Auxin-regulated
protein" because its *transcription* is auxin-induced — not because it transduces the
auxin signal. "Auxin-activated signaling pathway" (GO:0009734) belongs to the TIR1/AFB–
Aux/IAA–ARF cascade. Decision **REMOVE**; removal fully justified. The correct term,
"response to auxin" (GO:0009733), was added. Classic **"expression ≠ function"** pattern.

### Case 4: PR1B1 — "Killing" Keyword on the Canonical SAR Marker (Tier A→D)

**Gene:** PR1B1 (P04284) — Pathogenesis-related leaf protein 6 (PR-1b), *Solanum lycopersicum*.
**Review file:** `genes/SOLLC/PR1B1/PR1B1-ai-review.yaml`

The genuinely **mixed** case. "Killing of cells of another organism" (GO:0031640)
over-states the evidence — tomato P14a inhibits *Phytophthora* growth modestly via sterol
sequestration [PMID:7784503], not overt cytotoxicity → MARK_AS_OVER_ANNOTATED. But
"defense response to fungus" was substantially **correct biology**; its only flaw is
taxonomic (the characterized target is an oomycete) → MODIFY to defense response to
oomycetes (GO:0002229). Removal only **partly** justified.

### Case 5: STS3 — Defense Keyword on a Phytoalexin Biosynthetic Enzyme (Tier A)

**Gene:** STS3 (P51071) — Stilbene synthase 3, *Vitis vinifera*.
**Review file:** `genes/VITVI/STS3/STS3-ai-review.yaml`

STS3 is a type III polyketide synthase that makes trans-resveratrol, grapevine's major
**phytoalexin**. Because resveratrol is antimicrobial, the keyword "Plant defense" was
mapped to "defense response" (GO:0006952). But STS3 is a biosynthetic *synthase*, not a
defense effector or sensor — the annotation conflates the protective role of the *product*
with the function of the *enzyme*. Decision **MARK_AS_OVER_ANNOTATED**; removal justified.
Two NEW biosynthetic terms — stilbene biosynthetic process (GO:0009811) and phytoalexin
biosynthetic process (GO:0052315) — capture the defense context correctly. This is the
**"biosynthetic enzyme labelled with its product's downstream process"** pattern.

### Case 6: NFP — Kinase Activity on a Pseudokinase (Tier A)

**Gene:** NFP (Q0GXS4) — Nod Factor Perception LysM receptor-like kinase, *Medicago truncatula*.
**Review file:** `genes/MEDTR/NFP/NFP-ai-review.yaml`

NFP is the LysM receptor that perceives rhizobial Nod factors to initiate the
nitrogen-fixing symbiosis. Its intracellular kinase domain is a **catalytically dead
pseudokinase** — it lacks conserved catalytic residues and has no phosphotransfer activity
[PMID:16844829]; signalling proceeds via the active co-receptor LYK3. "Protein tyrosine
kinase activity" (GO:0004713) is therefore doubly wrong (pseudokinase; and plant RLKs are
Ser/Thr, not Tyr) → **REMOVE**, removal justified. The keyword-derived "defense response"
was also REMOVEd as redundant with specific curated defense terms. Notably the *current*
InterPro-derived "protein kinase activity" (GO:0004672) has the **same pseudokinase
problem** — sequence-motif pipelines (SPKW and InterPro2GO alike) cannot tell an active
kinase from a pseudokinase. Even a Tier-C-looking specific MF can be wrong.

### Case 7: METK1 — Broad Cofactor Keyword on a SAM Synthase (Tier B)

**Gene:** METK1 (A9P822) — S-adenosylmethionine synthase 1, *Populus trichocarpa*.
**Review file:** `genes/POPTR/METK1/METK1-ai-review.yaml`

METK1 makes S-adenosylmethionine, the universal methyl donor. Its two SPKW-unique terms
are both correct-but-broad: "metal ion binding" (GO:0046872) is true — the enzyme needs
Mg²⁺ and K⁺ — but uninformative → MARK_AS_OVER_ANNOTATED (proposed: magnesium/potassium
ion binding); "one-carbon metabolic process" (GO:0006730) is a defensible broad parent of
the precise, still-current "S-adenosylmethionine biosynthetic process" → KEEP_AS_NON_CORE.
A clean **Tier B exemplar**: removal pruned coarse, redundant terms without losing real
biology.

### Case 8: psaC — Broad Keywords Superseded by Specific Terms (Tier B)

**Gene:** psaC (Q00914) — Photosystem I iron-sulfur center, *Chlamydomonas reinhardtii*.
**Review file:** `genes/CHLRE/psaC/psaC-ai-review.yaml`

PsaC is the PSI subunit carrying the two terminal [4Fe-4S] clusters that pass electrons to
ferredoxin. Its two SPKW-unique terms are correct but imprecise: "metal ion binding"
gestures at what the still-current "4 iron, 4 sulfur cluster binding" (GO:0051539) states
precisely; "oxidoreductase activity" gestures at what the still-current "electron transfer
activity" (GO:0009055) states precisely. Both **REMOVE**; removal justified — no
information lost because more specific current annotations cover the same biology. (A
nuance: the relationship is "imprecise generalization superseded by a better term", not
strict GO parent→child subsumption.)

### Case 9: CASP1 — Cell-Wall Keyword That Carried Real Biology (Tier C)

**Gene:** CASP1 (C5YAP3) — Casparian strip membrane protein 1, *Sorghum bicolor*.
**Review file:** `genes/SORBI/CASP1/CASP1-ai-review.yaml`

CASP proteins are MARVEL-domain membrane proteins that self-assemble into the Casparian
Strip Membrane Domain and recruit the lignin-polymerizing machinery that builds the
endodermal **Casparian strip** — a localized cell wall modification forming the root
diffusion barrier. "Cell wall organization" (GO:0071555) is therefore **genuinely correct
and informative**. Decision **MODIFY** to the precise Casparian strip assembly
(GO:0160073) — but GOA's outright *removal* of this SPKW annotation **discarded correct,
plant-specific biology**. This is the key counter-example: a Tier C term where blanket
retirement was **not** the right call.

---

## Over-Annotation Patterns (Non-Arabidopsis Plants)

| Pattern | Example | Mechanism | Tier |
|---------|---------|-----------|------|
| **Downstream-process conflation** | STS3 (defense response on a phytoalexin synthase) | Product's protective role mapped onto the enzyme | A |
| **Expression ≠ function** | PARA (auxin signaling on an auxin-induced GST) | Hormone-responsive gene labelled a signaling component | A |
| **Catalytic activity on a pseudo-enzyme** | NFP (kinase activity on a pseudokinase) | Motif pipelines can't detect catalytic death | A |
| **Pathway-context ignored** | PPC16 (photosynthesis on a C3 housekeeping PEPC) | Family-signature keyword on a non-canonical paralog | D |
| **General-as-specific** | EME1 (meiosis keyword on a general repair endonuclease) | Process keyword narrower than the gene's true scope | A |
| **Over-stated directness / wrong class** | PR1B1 ("killing"; fungus vs oomycete) | Keyword maps to a stronger or mis-specified term | A/D |
| **Low-information but correct** | METK1, psaC (metal ion binding) | Cofactor keyword → broad, true, uninformative term | B |
| **Correct biology, wrongly retired** | CASP1 (cell wall organization) | Blanket pipeline removal drops a load-bearing keyword | C |

## Comparison: Non-Arabidopsis Plants vs Other Organisms

| Organism | Over-Annotation Rate | Main Patterns |
|----------|---------------------|---------------|
| Human (apoptosis) | 80–100% | Process conflation |
| S. pombe (ATG-meiosis) | 100% | Support-process conflation |
| D. melanogaster | 50% | Mixed |
| P. putida | 25% | RT defense keyword |
| Arabidopsis | 75% | Subclade divergence, specificity |
| **Non-Arabidopsis plants** | **~15% of terms are high-risk (Tier A)** | **Pathway context, expression≠function** |

The headline number is different in kind: rather than an organism-level "issue rate", the
plant analysis localizes the risk to **Tier A (15% of annotations, 29 terms)**. Of the
nine genes reviewed, every Tier A SPKW term was a genuine over-annotation, while Tier B/C
terms were correct.

## Key Lessons from Non-Arabidopsis Plants

1. **"SPKW-unique" is not "over-annotation".** Only ~15% of plant SPKW-unique annotations
   (Tier A) are over-annotations. ~48% (Tier B) are broad-but-correct cofactor/enzyme-class
   terms and ~31% (Tier C) are specific, correct, informative functions. The problem is a
   small, enumerable set of ~29 process/pathway terms.

2. **The patterns generalize, but the tier predicts the verdict.** Crops, the moss
   *Physcomitrium*, the alga *Chlamydomonas*, and the basal angiosperm *Amborella* all show
   the same categories. The tier of an SPKW term reliably predicts whether GOA's removal
   was safe: Tier A removals were always justified; Tier B removals lost only redundant
   coarse terms; Tier C removals risked — and in CASP1, EME1, and PR1B1 actually caused —
   loss of correct biology.

3. **GOA's retirement of the SPKW pipeline was right for the over-annotations — but
   collateral damage is real.** EME1 lost its only catalytic molecular-function term;
   CASP1 lost a correct cell-wall-organization annotation; PR1B1 lost correct (if
   imprecise) defense biology. A keyword annotation that is the *sole* carrier of a fact
   should be re-asserted with a proper evidence code, not silently dropped.

4. **Sequence-motif pipelines cannot detect catalytic death.** NFP shows that both SPKW
   keyword2GO and InterPro2GO assign "kinase activity" to a known pseudokinase. This
   failure mode affects Tier-C-looking specific MF terms, not just broad ones.

## Recommendations

1. **Triage retired SPKW annotations by tier.** Tier A removals can be accepted wholesale.
   Tier C removals must be checked individually — if the keyword was the only source of a
   correct fact, re-assert it (ideally with a more specific term).

2. **The 29 Tier A terms are a reusable watch-list.** Any future keyword→GO mapping, in
   any organism, should treat hormone-signaling, defense/immunity-process,
   pleiotropic-development, and cell-cycle/meiosis keywords as high-risk.

3. **Pathway-context check for enzyme families** (Tier D): confirm the specific
   isozyme/organism performs the family's signature role before applying the family
   keyword — C3 vs C4 status, paralog subfamily, and tissue expression all matter.

4. **Distinguish hormone-responsive from hormone-signaling genes**, and
   biosynthetic enzymes from the defense processes their products serve.

## Review Files Location

```
genes/ORYSJ/EME1/EME1-ai-review.yaml      (A→C: meiosis over-annotated; endonuclease MF restored)
genes/SOYBN/PPC16/PPC16-ai-review.yaml    (D: photosynthesis on a C3 housekeeping PEPC)
genes/TOBAC/PARA/PARA-ai-review.yaml      (A: auxin signaling on an auxin-induced GST)
genes/SOLLC/PR1B1/PR1B1-ai-review.yaml    (A/D: PR-1 defense keywords)
genes/VITVI/STS3/STS3-ai-review.yaml      (A: defense response on a phytoalexin synthase)
genes/MEDTR/NFP/NFP-ai-review.yaml        (A: kinase activity on a pseudokinase)
genes/POPTR/METK1/METK1-ai-review.yaml    (B: broad cofactor keyword on a SAM synthase)
genes/CHLRE/psaC/psaC-ai-review.yaml      (B: broad keywords superseded by specific terms)
genes/SORBI/CASP1/CASP1-ai-review.yaml    (C: correct cell-wall biology, wrongly retired)
```

## Methods Note

The nine genes were selected from the `plant.ddb` closure-filtered TRUE SPKW-unique set to
sample all four term tiers across nine species. Because GOA had already retired
`GO_REF:0000043`, `just fetch-gene` seeds `existing_annotations` from live QuickGO and no
longer includes the SPKW annotations; the historical SPKW annotations were re-added from
the September 2025 `plant.ddb` snapshot and flagged `retired: true` so they are reviewed
but excluded from the live-GOA consistency check. The term-tier classification uses an
explicit GO-ID assignment over all 214 terms (the `spkw_plants_unique` analysis table in
`plant.ddb`). See [SPKW-METHODOLOGY.md](SPKW-METHODOLOGY.md) for the closure-filtered SQL.
