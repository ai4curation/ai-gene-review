# ABI3BP (Q7Z7G0, TARSH / NeshBP) — review notes

Human, UniProt Q7Z7G0 (TARSH_HUMAN), 1068 aa precursor, HGNC:17265, chromosome 3q12.

## 1. What the GOA record actually contains

The whole GOA record is ten rows and it is entirely about *where the protein is*, plus one
molecular function repeated three times:

| Term | Aspect | Evidence | Reference | Qualifier |
|---|---|---|---|---|
| GO:0005576 extracellular region | CC | IEA | GO_REF:0000044 | located_in |
| GO:0140149 non-collagenous component of interstitial matrix | CC | TAS | PMID:36399478 | located_in |
| GO:0031012 extracellular matrix | CC | HDA | PMID:28675934 | located_in |
| GO:0031012 extracellular matrix | CC | HDA | PMID:27559042 | located_in |
| GO:0031012 extracellular matrix | CC | HDA | PMID:20551380 | colocalizes_with |
| GO:0005576 extracellular region | CC | HDA | PMID:27068509 | located_in |
| GO:0005576 extracellular region | CC | HDA | PMID:20551380 | located_in |
| GO:0005201 extracellular matrix structural constituent | MF | RCA | PMID:28675934 | enables |
| GO:0005201 extracellular matrix structural constituent | MF | RCA | PMID:27559042 | enables |
| GO:0005201 extracellular matrix structural constituent | MF | RCA | PMID:20551380 | enables |

Facts worth stating plainly:

- **There is not a single biological-process annotation.** Zero BP rows.
- **There is no IBA/PAINT annotation at all.** The UniProt cross-reference states it:
  `DR   PAN-GO; Q7Z7G0; 0 GO annotations based on evolutionary models.`
  (verified in `ABI3BP-uniprot.txt`). PANTHER family PTHR23197 / subfamily PTHR23197:SF10
  has not been PAINT-curated for this protein.
- **There is no experimental molecular function and no experimental cellular-component
  annotation from a low-throughput assay.** Every CC row is either an IEA keyword mapping,
  a TAS from a database paper, or HDA from a shotgun ECM proteomics dataset.
- **The only WITH/FROM entry in the whole file** is `UniProtKB-SubCell:SL-0243` on the IEA row.
  Resolved via `https://rest.uniprot.org/locations/SL-0243.json`: SL-0243 = "Secreted",
  definition "Protein located outside the cell membrane(s)", GO mapping `GO:0005576
  extracellular region`. So the IEA is a faithful one-to-one keyword mapping — there is no
  ortholog/paralog transfer anywhere in this record to audit.

Meanwhile the primary literature contains a worked-out receptor-level mechanism, a knockout
mouse, and human loss-of-function tumour data. None of it is in GO.

## 2. Protein architecture (checked directly against `ABI3BP-uniprot.txt`)

- Signal peptide 1–21; mature chain 22–1068. Secretion is not just predicted: mouse TARSH is
  demonstrably secreted [PMID:19302145, "We also demonstrate that TARSH is a secreted protein."].
- Two fibronectin type-III domains, 116–214 and 833–926 (PROSITE PRU00316), plus a
  family-specific C-terminal domain (Pfam PF21731 TARSH_C; InterPro IPR049109 TARSH/FNDC1_C).
  No catalytic domain of any kind — consistent with the original description
  [PMID:11501947, "It possesses an SH3 binding motif, a nuclear targeting sequence, and no catalytic domain."].
- A very large disordered central region, 384–811 (MobiDB-lite), plus 315–351.
- N-glycosylated at Asn-37 (experimental, PMID:19159218); GlyConnect lists 25 N-linked glycans
  over 6 sites.

**Sequence checks I ran on the canonical sequence in `ABI3BP-uniprot.txt`:**

- *PxxP density.* 21 PxxP motifs in 1068 residues; **18 of them fall inside the disordered
  384–811 region** (4.2 per 100 aa) versus 3 in the remaining 640 residues (0.47 per 100 aa) —
  a ~9-fold enrichment. This is the physical basis of the "SH3-binding motif cluster in the
  middle of the gene" reported for mouse Tarsh
  [PMID:15752759, "diversity was derived from the SH3-binding motif cluster in the middle of the gene"],
  and it is where the alternative splicing happens.
- *Isoform arithmetic.* Isoform 2 (Q7Z7G0-2) = canonical minus residues 1–607 (VSP_010860)
  plus the 25-residue insertion at position 669 (VSP_010861) = 1068 − 607 + 25 = **486 aa**.
  The original human cDNA that named this gene encodes exactly 486 aa
  [PMID:11501947, "a predicted open reading frame that encodes 486 amino acids"]. So the
  Y2H clone recovered with the Nesh/ABI3 SH3 domain as bait was the short C-terminal isoform,
  not the full-length protein.
- *Thrombin site.* Residue 337 of the canonical sequence is **Arg**, and its context is
  `…E-T-V-P336-R337↓S338-T-K…`. P2 = Pro, P1 = Arg, P1' = Ser is a canonical thrombin
  recognition site. That independently corroborates the reported cleavage
  [PMID:41839242, "Thrombin hydrolyzed ABI3BP at arginine 337."] rather than taking it on trust.

## 3. The mechanism the GO record is missing

**Integrin-β1 is the receptor.** In mesenchymal stem cells, Abi3bp binds integrin-β1 and this
is what switches cells out of proliferation and into differentiation
[PMID:23666637, "Upon Abi3bp binding to integrin-β1 Src associated with paxillin which inhibited
proliferation."]. The binding is shown two ways in that paper — co-IP of integrin-β1 with a
myc-tagged Abi3bp from conditioned medium, and co-IP of integrin-β1 with *endogenous* Abi3bp
[PMID:23666637, "immunoprecipitation of endogenous Abi3bp from MSC-GFP-Akt1 cells resulted in the co-precipitation of integrin-β1"] — plus a function-blocking antibody screen in which only the β1 antibody
had an effect [PMID:23666637, "incubation with the β1 blocking antibody increased phospho-ERK1/2 levels ~3.5-fold."].

The downstream logic is explicit: [PMID:23666637, "In the absence of Abi3bp, the integrin-β1 is
maintained in a non-active state and the lack of phosphorylated paxillin prevents sequestration of
Src and ERK at the plasma membrane, leaving these kinases to activate cyclin-d1 and drive
proliferation."]. So ABI3BP is a **positive regulator of integrin activation** and a
**negative regulator of the ERK cascade and of proliferation**.

**Loss of function, in vivo.** [PMID:23666637, "MSCs from Abi3bp knockout mice displayed severe
deficiencies in osteogenic and adipogenic differentiation."] and
[PMID:23666637, "In vivo, Abi3bp knockout increased MSC number and proliferation in bone marrow,
lung, and liver."].

**The same axis in cardiac progenitors.** [PMID:25296984, "In vivo, genetic ablation of the Abi3bp
gene inhibited CPC differentiation, whereas CPC number and proliferative capacity were increased.
This correlated with adverse recovery after myocardial infarction."] and
[PMID:25296984, "Abi3bp controlled CPC differentiation via integrin-β1, protein kinase C-ζ, and
v-akt murine thymoma viral oncogene homolog."]. The receptor dependence was tested directly:
[PMID:25296984, "Integrin-β1 blocking antibodies completely abrogated the positive effects of
re-expression of Abi3bp (Figure 5B)"].

**Human loss-of-function evidence.** Re-expression in human thyroid carcinoma lines
[PMID:18559958, "Re-expression of ABI3BP in thyroid cells resulted in a decrease in transforming
activity, cell growth, cell viability, migration, invasion, and tumor growth in nude mice."];
overexpression in human NSCLC lines [PMID:40092729, "Overexpression of ABI3BP in NSCLC cells
resulted in a substantial reduction in cell growth and motility and induced cell cycle arrest."];
and in gallbladder cancer the gene is epigenetically silenced by MALAT1/EZH2
[PMID:31174563, "the expression of MALAT1 was up-regulated while that of the ABI family member 3
binding protein (ABI3BP) was down-regulated in GBC tissues and cell lines"].

Note the species split: the mechanism (integrin-β1, paxillin, Src, PKCζ, Akt) is **mouse**;
the growth-suppression phenotype is reproduced in **human** cells by three independent groups
in three tissues. That is why the mechanistic core function here is grounded as ISS from mouse
with human corroboration, not asserted as a human experimental result.

## 4. The senescence literature genuinely contradicts itself

This is not a reading error on my part; the field says so out loud
[PMID:23666637, "Abi3bp has been reported to have both a positive and negative role in senescence [13, 14]."].

- *Loss of ABI3BP → senescence:* [PMID:19338757, "the reduction of TARSH gene expression by short
  hairpin RNA (shRNA) system robustly inhibited the MEFs proliferation with increase in
  senescence-associated beta-galactosidase (SA-beta-gal) activity"] — p53/p21-dependent, in MEFs.
- *Gain of ABI3BP → senescence:* [PMID:18559958, "ABI3BP re-expression appears to trigger cellular
  senescence through the p21 pathway."] — human thyroid carcinoma lines.
- *Loss of ABI3BP → less senescence:* [PMID:40889718, "Downregulation of ABI3BP expression using
  siRNA significantly inhibited Ang II-induced senescence of VSMC."]; likewise in renal tubular
  cells [PMID:38812032, "ABI3BP gene knockout not only elevated Klotho expression but also reduced
  ferroptosis levels."] and in chondrocytes [PMID:41232761, "Its knockdown mitigated IL-1β-induced
  ECM degradation and reduced the level of senescence-associated markers"].

Both signs are supported by knockdown/knockout experiments in different cell types, so this is
a real biological conflict (cell-type-dependent, or stress-induced vs replicative senescence),
not a citation problem. **No senescence GO term should be asserted for this gene until the
conflict is resolved.** I have deliberately kept senescence out of `core_functions` and put it
in `suggested_questions` / `suggested_experiments` instead.

## 5. The naming problem

The gene is named for a binding partner the gene has never been shown to bind as a full-length
protein. The original clone was a yeast two-hybrid hit against the Nesh (ABI3) SH3 domain
[PMID:11501947, "By using a conventional two-hybrid technique with an Src homology 3 (SH3) domain
of Nesh as the bait protein, a novel full-length cDNA was isolated and sequenced from a human
placenta cDNA library."], and it was the 486-aa short isoform (see §2). Twelve years later the
caveat was still standing [PMID:23666637, "However, in vivo binding activity between full-length
Abi3bp and Abi3 awaits confirmation."]. UniProt encodes exactly this hedge:
`CC   -!- SUBUNIT: Probably interacts with ABI3.` — a `Probably`, not an assertion.

Consequently GOA carries **no** protein-binding annotation for ABI3BP–ABI3, and it is correct
that it does not. I have not proposed one.

## 6. Where GO:0005201 comes from, and why it is an over-annotation

All three `GO:0005201 extracellular matrix structural constituent` rows are RCA from BHF-UCL,
each citing an ECM-proteomics dataset or protocol:

- PMID:28675934 is a **methods paper** — [PMID:28675934, "We provide here optimized protocols to
  solubilize ECM proteins from normal or tumor tissues, digest the proteins into peptides, analyze
  ECM peptides by mass spectrometry, and interpret the mass spectrometric data."] — illustrated on
  breast and ovarian tissue. It establishes a workflow, not ABI3BP's structural role.
- PMID:20551380 is a human aorta ECM extraction study; PMID:27559042 is atrial glycoproteomics.

What these datasets show is that ABI3BP peptides are recovered from ECM-enriched fractions of
human tissue. That supports the **cellular component** (and the same three papers are indeed
cited for the HDA `GO:0031012`/`GO:0005576` rows, which I accept). It does not support the
**molecular function** claim, whose definition is specific:
"The action of a molecule that contributes to the structural integrity of the extracellular
matrix" (verified against QuickGO). Nobody has measured whether removing ABI3BP changes the
mechanical integrity of any matrix. The one assembly-relevant experiment is second-hand and is a
fragment, not the protein: [PMID:23666637, "Computational screening followed by in vitro assays
identified that a partial fragment of Abi3bp, containing one of the two Fibronectin type-III
domains found in the full length protein, promoted cell attachment and was capable of assembling
into an extracellular matrix"] — citing PMID:18757743, whose full text is not retrievable and
whose abstract does not name ABI3BP.

Contrast that with what *has* been measured: receptor binding, receptor activation, and a
signalling output. ABI3BP behaves as a matricellular protein — matrix-resident, cell-instructive,
not load-bearing.

The structural reading is also what the ontology *forces*. GO:0005201's children are all
mechanical — tensile strength (GO:0030020), compression resistance (GO:0030021), elasticity
(GO:0030023), lubricant (GO:0030197) — and GO has **no** term for the matricellular class at all
(confirmed: OLS `search_all_ontologies(query="matricellular", ontologies="go")` returns an empty
result set, and the QuickGO ontology search for "matricellular" likewise returns nothing). So a
pipeline that knows only "this is a core-matrisome ECM glycoprotein" has exactly one ECM-specific
molecular function available to it, and it is the wrong one. That is the gap recorded in
`proposed_new_terms`.

## 7. Other things worth flagging

- **`colocalizes_with` on the PMID:20551380 GO:0031012 row.** The same paper's `GO:0005576` row
  uses `located_in`. `colocalizes_with` is meant for imaging evidence that cannot resolve whether
  the protein is genuinely inside the structure; it is a strange qualifier for a biochemical
  fractionation experiment, and it makes the aorta dataset contribute two rows that disagree with
  each other about confidence. Raised as a question rather than acted on, since the schema has no
  qualifier-correction action.
- **UniProt lists `GO:0005615 extracellular space; HDA:BHF-UCL` in its DR block but that row is
  absent from the GOA TSV.** Not something this review can fix, but noted.
- **Disease link is weak.** A single de-novo `D663G` variant of uncertain significance in one
  coloboma patient, reported in a paper about a different gene (ACTG1)
  [PMID:28493397]. UniProt itself hedges: `CC   -!- DISEASE: Note=Defects in ABI3BP has been found in a patient with`.
  No eye-development GO term is justified from this.
- **Antiviral/interferon report** [PMID:38384000] is a single preliminary in vitro study
  ("A Preliminary Study In Vitro" in its own title) in one human fibroblast line, with no
  mechanism linking a secreted ECM protein to TBK1/IRF3. Not annotated.
- **Neuronal / dendritic-refinement role** [PMID:19302145] was originally listed here as
  "not annotated". That was wrong, and it is now annotated as `GO:0050774` following PR review —
  see §8 for why the original reasoning did not hold.
- **Thrombin cleavage / BBB protection** [PMID:41839242] is 2026, single-group, and the
  therapeutic arm uses supraphysiological recombinant protein. The cleavage site is
  independently plausible (§2) but the BBB function is not annotated here.

## 8. Decisions taken

**On the ten existing rows:**

- ACCEPT all seven CC rows. Secreted/ECM localisation is solid and independently reproduced in
  four human tissues plus antibody staining. `GO:0140149` is the most informative of them.
- MARK_AS_OVER_ANNOTATED all three `GO:0005201` MF rows (§6). Not REMOVE: the protein really is
  matrix-resident and a fragment really can assemble into matrix in vitro, so a structural
  contribution has never been *excluded* — it has never been *tested*. That distinction is what
  separates over-annotation from error.

**Eight NEW rows proposed**, all coded `ISS` with `supporting_entities: MGI:MGI:2444583` (mouse
Abi3bp, MGI id taken from the UniProt cross-reference on F7B3T6, not from memory), because every
perturbation experiment behind them is mouse:

| Term | Ref | Why |
|---|---|---|
| GO:0005178 integrin binding (MF) | PMID:23666637 | Co-IP with tagged *and* endogenous protein; β1-specific blocking-antibody panel |
| GO:0033625 positive regulation of integrin activation | PMID:23666637 | Ligand changes receptor state, measured as phospho-paxillin/paxillin ratio (see outside-in caveat below) |
| GO:1902461 negative regulation of mesenchymal stem cell proliferation | PMID:23666637 | Germline KO with in vivo phenotype in three organs + independent shRNA lines |
| GO:0070373 negative regulation of ERK1 and ERK2 cascade | PMID:23666637 | Perturbed at three points in the chain; vinculin knockdown is the specificity control |
| GO:0045669 positive regulation of osteoblast differentiation | PMID:23666637 | Osteogenesis fails in KO cells across all three isolations |
| GO:0045600 positive regulation of fat cell differentiation | PMID:23666637 | Adipogenesis fails in the same KO cells |
| GO:2000727 positive regulation of cardiac muscle cell differentiation | PMID:25296984 | In vivo ablation + marker analysis + antibody demonstration that it runs through integrin β1 |
| GO:0050774 negative regulation of dendrite morphogenesis | PMID:19302145 | Conditioned medium, purified protein at 500 ng/ml, and a cell-autonomous overexpression arm; expression time course matches the process |

The `GO:0050774` row was **added during PR review** (#2250). My first draft described the olfactory
dendritic-refinement role in the top-level `description` but proposed no annotation, on the grounds
that the work was single-laboratory and mouse-only and was "described in the gene description and
questions". The reviewer correctly pointed out that both halves of that fail: the same evidence
grade underpins the five rows drawn from PMID:23666637, PMID:25296984 is from the *same* laboratory
as PMID:23666637, and there was in fact no question about the nervous system anywhere in the file.
Withholding ISS from one body of mouse work while applying it to another of identical grade was
just inconsistent. Added, with two new questions (neuronal receptor; diffusible vs tethered).

It is kept out of `core_functions` for a stated reason rather than by omission: no receptor is known
for the neuronal effect, so there is no molecular function to attach the process to without assuming
that integrin β1 is involved, and it has not been reproduced outside the originating lab.

### The outside-in caveat on `GO:0033625`

`GO:0033622 integrin activation` is defined as *"The aggregation, arrangement and bonding together
of an integrin… that lead to the increased affinity of the integrin for its extracellular ligands"*,
and that branch is conventionally used for **inside-out** affinity modulation by talin and kindlin.
ABI3BP works from the opposite side — it *is* the extracellular ligand. The definition does not
restrict the term to inside-out signalling, and the paper's own wording ("the integrin-β1 is
maintained in a non-active state" without Abi3bp) supports the claim, but an outside-in ligand is
not the canonical filler and a curator may prefer to carry the point on `GO:0005178` alone. Recorded
in `review.reason` on that row.

### Two term-choice traps I fell into and had to back out of

**`GO:2000738 positive regulation of stem cell differentiation` is the wrong term, despite
looking exactly right.** My first draft used it as the lineage-agnostic way to say "knockout MSCs
fail to differentiate". But its target, `GO:0048863 stem cell differentiation`, is defined (QuickGO)
as *"The process in which a relatively unspecialized cell acquires specialized features of a stem
cell"* — differentiation **into** a stem cell. Annotating it would assert that ABI3BP promotes cells
*becoming* stem cells, which is the opposite of the observed biology. `GO:2000741 positive
regulation of mesenchymal stem cell differentiation` inherits the identical inversion via
`GO:0072497` (*"…acquires specialized features of a mesenchymal stem cell"*), so the
more-specific-looking term is wrong in the same way.

The whole GO `<cell type> differentiation` branch means "becoming that cell type", so the only
correct route is outcome-specific terms — hence `GO:0045669` (→ `GO:0001649` osteoblast
differentiation, "acquires the specialized features of an osteoblast" ✓) and `GO:0045600`
(→ `GO:0045444` fat cell differentiation, "…of an adipocyte" ✓). `GO:2000727` survives the same
test (`GO:0055007`: "a cardiac muscle precursor cell acquires specialized features of a cardiac
muscle cell" ✓), and so does `GO:1902461` (`GO:0097168` MSC proliferation = "multiplication or
reproduction of mesenchymal stem cells" ✓).

Lesson: fetch the definition of the *target* of every regulation term, not just the regulation
term itself. The label reads correctly in both directions; only the definition disambiguates.

**`GO:0098640 integrin binding involved in cell-matrix adhesion`** was also considered for the MF
and rejected — the demonstrated consequence of binding is receptor activation and downstream
signalling, not adhesion of the cell to the matrix. Plain `GO:0005178` is the honest choice.

**Also:**

- One new MF term proposed for the matricellular class (§6), parented under GO:0048018 receptor
  ligand activity alongside growth factor / cytokine / hormone / morphogen activity. **The
  distinguishing criterion was narrowed during PR review.** An earlier draft argued the term was
  distinguished from its siblings "by matrix residence rather than diffusion", claiming this was
  experimentally grounded because the growth-factor mode had been excluded. That overstated the
  evidence, and evidence in this very file contradicts it: concentrated medium from ABI3BP-expressing
  cells inhibits MSC proliferation [PMID:23666637, "Concentrated media prepared from HEK293 cells
  expressing the myc-tagged Abi3bp inhibited proliferation of both MSC and MSC-GFP-Akt1 cells when
  compared to control concentrated media (Supplementary Figure 3E) further validating the
  anti-proliferative effect of Abi3bp."], and purified secreted TARSH acts on neurons in dissociated
  culture — the protein demonstrably works at a distance. What the growth-factor control actually
  shows is only that Abi3bp is not a growth-factor-like ERK *agonist*. The proposal now rests on the
  ontology gap alone, which is where its weight always was, with the tethering question moved to
  `suggested_questions`.

  **The proposed *definition* had the same flaw and was fixed in a second pass.** It originally read
  "…without contributing appreciably to the mechanical integrity of the matrix" — an unmeasurable
  negative, and one that this review's own position ("never tested") means ABI3BP cannot be shown to
  satisfy. Proposing a term whose defining clause the motivating example cannot be demonstrated to
  meet would have been self-defeating in front of a GO editor. Reworded positively: the defining
  feature is the cell-instructive action on a receptor, and the term now explicitly neither asserts
  nor excludes a structural contribution.

  **That reword then went too far, and was tightened in a third pass.** Dropping the negative clause
  left the definition with no differentia at all: "acts on cells by engaging cell-surface receptors,
  thereby modulating their signalling, adhesion, proliferation or differentiation state" is satisfied
  in full by `GO:0008083` growth factor activity, since plenty of growth factors are matrix-resident
  (FGFs, HB-EGF, latent TGF-β complexes), and localization is a weak differentia for a molecular
  function in any case. The criterion the siblings genuinely fail is **receptor class**: `GO:0005125`
  cytokine activity is defined for a *soluble* extracellular product, growth factor activity for
  *stimulation* of growth, whereas a matricellular protein signals through an adhesion receptor
  (`GO:0004895`, whose own definition names integrins) and here *restrains* proliferation. The
  definition now carries that, and the justification records all three rejected candidates — the
  unmeasurable negative, matrix residence alone, and receptor class as the one that survives.

  **Fourth pass: the receptor-class version over-generalised in the other direction.** Writing "its
  output is characteristically restraint of proliferation" into the differentia was true of ABI3BP but
  false of the class — tenascin-C, periostin and CCN1/CCN2 signal through αVβ3, αVβ5 and α6β1 and are
  characteristically *pro*-proliferative, so the clause would have excluded most of the proteins the
  same justification cites as the reason the term is needed. A differentia hedged with
  "characteristically" is not usable as a differentia in any case, and receptor class alone does the
  whole exclusion job. Removed, along with the sibling comparison itself, which is reasoning *about*
  the ontology and belongs in `justification` (`ProposedOntologyTerm` has no `comment` slot).

  Two things were added instead. `GO:0004895` is not just a plausible parent class: production GO-CAM
  `689e7a5d00003515` assigns exactly `GO:0004895 cell adhesion receptor activity` to human ITGB1
  (`UniProtKB:P05556`), alongside `GO:0007229` and `GO:0005925` — verified at `gocams/index.tsv:8672`.
  So the differentia matches how GO already types the very receptor ABI3BP engages. And a
  reasoner-checkable form is now offered for the editors: `GO:0048018 and has-target some GO:0004895`,
  with matrix residence as a non-defining characteristic.

  Four passes on one definition is worth recording as a pattern. Unmeasurable negative → no
  differentia at all → a differentia that over-claimed at class level → receptor class alone. Each
  individual change was correct, and two of the intermediate states were genuine regressions. The
  lesson: when tightening a class definition, test it against the *other* members of the class you
  cited as motivation, not only against the gene in front of you.
- Senescence, antiviral and blood-brain-barrier roles left unannotated and moved into
  `suggested_questions` / `suggested_experiments`. The senescence literature contradicts itself
  (§4) and no term should be asserted until that is resolved. Note the contrast with the neuronal
  role, which *is* now annotated: the difference is not the number of laboratories but the kind of
  evidence. Dendritic refinement has three concordant gain-of-function arms plus a matching
  expression time course and an activity-independence control; the senescence claims contradict each
  other in sign, the antiviral report is self-described as preliminary in its own title, and the BBB
  arm depends on supraphysiological recombinant protein.
- The affinage record is cited once, on the `GO:1902461` row, and only for its high-level summary
  sentence, which is independently carried on the same row by two verbatim quotes from
  PMID:23666637 and one from PMID:18559958. No mechanistic claim in this review rests on it —
  every domain boundary, binding partner and mechanistic step is quoted from UniProt's own feature
  table or from the primary paper.

**Verification run before pushing:** `checkquotes.py` — 100 quotes, 0 problems (it checks `file:`
quotes as well as PMIDs, so the UniProt lines are verified too); `just validate human ABI3BP` —
`✓ Valid`, zero warnings; `cache/go/terms.csv` — 4 insertions, 0 deletions.

Two `cache/go/terms.csv` traps hit along the way, both worth remembering. First, a `just validate`
run silently drops unrelated cached terms (18 the first time, 1 each on two later runs), so the file
has to be restored from `origin/main` and the new terms re-added after every validation. Second,
**do not globally sort the file to re-insert them** — `origin/main` currently has at least one
out-of-order entry (`GO:0140312`), so a global sort relocates it and shows up as a spurious deletion.
Insert each new line in position without touching the rest.

A validator quirk also worth noting: for PMID:19302145 the locally cached record has
`full_text_available: true` and does contain the full text, but the reference validator's own record
holds only the abstract, so full-text-only passages are rejected as supporting_text even though
`checkquotes.py` accepts them. All quotations from that reference are therefore taken from the
abstract.
