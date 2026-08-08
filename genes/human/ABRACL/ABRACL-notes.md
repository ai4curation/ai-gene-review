# ABRACL (Q9P1F3) — review notes

Human ABRACL, "ABRA C-terminal like", formerly C6orf115 / HSPC280 / PRO2013. 81 aa, ~9 kDa,
usually one copy per genome, but not universally: PANTHER PTHR46334 resolves into two subfamilies,
SF1 (human, Dictyostelium and most plants) and a plant-restricted SF3, and Arabidopsis has 2 members
while maize has 3.

## Starting position: three annotations, no molecular function

The whole GOA record is three rows:

| Term | Aspect | Evidence | Reference | WITH/FROM |
|---|---|---|---|---|
| GO:0032970 regulation of actin filament-based process | BP | IBA | GO_REF:0000033 | PANTHER:PTN000507089 \| dictyBase:DDB_G0272861 |
| GO:0005929 cilium | CC | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0066 |
| GO:0030027 lamellipodium | CC | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0291 |

Nothing is experimental, and there is **no molecular function annotation at all** — despite a
2021 paper that reports a direct in-vitro binding assay and a direct in-vitro activity assay
on purified recombinant protein.

## What the primary literature actually shows

### Dictyostelium: the origin of the phylogenetic annotation

cosA was found in a chemotaxis screen. cosA-null cells move slower but steer normally
[PMID:20940261 "Analysis of cell motion in cAMP gradients revealed decreased speed but
wild-type-like directional persistence of cosA(-) cells, suggesting a defect in the cellular
machinery for motility rather than for chemotactic orientation."], and their actin cytoskeleton
is disturbed [PMID:20940261 "cosA(-) cells exhibited changes in the actin cytoskeleton, showing
aberrant distribution of F-actin in fluorescence cell staining and an increased amount of
cytoskeleton-associated actin."].

The decisive point for the IBA is functional complementation: [PMID:20940261 "Expressing cosA
or its human counterpart mCostars eliminated abnormalities of cosA(-) cells."] The human
protein does the Dictyostelium protein's job in Dictyostelium cells. That is a stronger basis
for an ortholog transfer than sequence identity alone.

### Human: cofilin, F-actin, and the leading edge

All from PMID:33670794 (Hsiao et al. 2021, full text available):

- Direct, weak F-actin binding by purified untagged recombinant protein in a co-sedimentation
  assay: [PMID:33670794 "These results indicated that purified recombinant ABRACL bound to
  F-actin, although very weakly, under the in vitro experimental conditions."]
- Colocalisation of endogenous protein with F-actin at the leading edge:
  [PMID:33670794 "fluorescence signals for endogenous ABRACL and F-actin were colocalized at the
  leading edge of lamellipodia"]
- Cofilin interaction in cells, three ways — colocalisation especially at lamellipodia,
  proximity ligation that disappears on knockdown of either partner, and co-IP:
  [PMID:33670794 "Fluorescence PLA signals were detected in the control cells but greatly
  diminished in ABRACL- or cofilin-knockdown cells"] and [PMID:33670794 "endogenous cofilin was
  detected together with the immunoprecipitated ABRACL-Myc-His"]
- The functional interaction, on purified proteins: [PMID:33670794 "the addition of ABRACL in
  the reaction blunted this effect of cofilin in a dose-dependent manner"], and the necessary
  control ruling out simple displacement: [PMID:33670794 "We found that ABRACL did not inhibit
  the co-sedimentation of cofilin with F-actin"]
- Loss-of-function: [PMID:33670794 "All five ABRACL-knockout clones examined displayed
  significantly reduced migration in the Transwell assay"]

### The sign problem — why the vague GO term is the right one

Three lines of evidence disagree about which way ABRACL pushes the F-/G-actin balance.

1. Losing the Dictyostelium ortholog *raises* cytoskeleton-associated actin
   [PMID:20940261 "an increased amount of cytoskeleton-associated actin"].
2. Losing human ABRACL *lowers* it [PMID:33670794 "both ABRACL-knockdown and ABRACL-knockout
   cells displayed lower cellular F-/G-actin ratios compared to the control cells"].
3. Purified ABRACL on its own *inhibits* polymerisation [PMID:33670794 "the results showed that
   ABRACL inhibited actin polymerization in a dose-dependent manner"], which the authors
   themselves flag as inconsistent with (2) [PMID:33670794 "These in vitro results appeared to
   contradict the above-mentioned finding of decreased F/G-actin ratios in cells lacking
   ABRACL"].

Only in the presence of cofilin does ABRACL clearly favour F-actin. So `GO:0030835 negative
regulation of actin filament depolymerization` and `GO:0030837 negative regulation of actin
filament polymerization` are each supported by part of the evidence and contradicted by another
part. The unsigned parent GO:0032970 is not a lazy annotation here — it is the only claim all
three datasets support. Left as ACCEPT for exactly that reason.

## The cilium annotation: a four-step chain with nothing at the end

This is the main finding of the review.

`GO:0005929 cilium` is IEA from GO_REF:0000044, i.e. a mechanical mapping of the UniProt
subcellular-location line `Cell projection, cilium {ECO:0000305|PubMed:37759737}`. Tracing back:

1. **GOA** transfers `UniProtKB-SubCell:SL-0066` without judgement — as designed.
2. **UniProt** flags its own statement ECO:0000305 (curator inference, not observation).
3. **PMID:37759737** is an *expression* study of mouse and cat embryonic telencephalon. It
   reports no ciliary localisation of its own. It says only:
   [PMID:37759737 "a high-throughput proteomics study in non-neuronal cell lines has shown that
   Abracl is associated with the primary cilia"] — a citation of somebody else's work. In the
   same paragraph it reports data pointing the other way:
   [PMID:37759737 "our results show that neither Abracl mRNA nor Abracl were expressed in the
   VZ"] — the ventricular zone being where the ciliated progenitors are.
4. That "high-throughput proteomics study" is PMID:26638075, the Gupta et al. centrosome-cilium
   BioID interactome. It is the *only* source of physical-interaction data for ABRACL in IntAct:
   five proximity-labelling hits, one publication, one detection method, with baits SASS6,
   CNTRL, DCTN1 and RPGRIP1L (see `ABRACL-bioinformatics/RESULTS.md`).

So a proximity-labelling neighbourhood became, three citations later, a subcellular location on
the human protein. Nobody along the chain did anything unreasonable; the failure is that no step
re-examined the one before it.

The phyletic check in `ABRACL-bioinformatics/RESULTS.md` adds a family-level argument: Costars is
retained in *Arabidopsis*, rice, maize and *Dictyostelium*, none of
which builds a cilium, basal body or centriole, while IFT88, IFT52, BBS1 and ARL13B are absent
from all four. Whatever the family is conserved for, it is not ciliary. That does not exclude a
human-specific ciliary role, and the notes say so — but there is no evidence for one either.

## The lamellipodium annotation is the opposite problem

`GO:0030027 lamellipodium` is also IEA-from-SubCell, but here the underlying UniProt statement is
ECO:0000269 (experimental) and the human experiment exists: endogenous protein, endogenous
antibody, colocalised with F-actin at the leading edge, in the paper's Figure 4D. This
annotation deserves to be IDA. Kept as ACCEPT with a recommendation to upgrade the evidence code
rather than the term.

## What is missing from GO itself

ABRACL binds cofilin and reduces cofilin-stimulated filament disassembly without displacing
cofilin from the filament. GO has a molecular function for the opposite sign — `GO:0000513 actin
severing activator activity`, "Binds to and increases the activity of a actin severing protein" —
and no inhibitor counterpart. The absence of that sibling term is a large part of why this gene
has no MF annotation. Proposed as a new term in the review.

`GO:0051015 actin filament binding` is proposed as a NEW annotation in the meantime: it is
directly demonstrated (purified protein, co-sedimentation, quantified against a no-actin
control), and it is honest about being weak.

## Loose ends not annotated

- **Nuclear localisation.** [PMID:26537243] reports HSPC280/Abracl in the subventricular zone and
  that overexpression in Neuro2a inhibits neuronal differentiation. Nuclear localisation there is
  hard to reconcile with the lamellipodial pool; the protein is 9 kDa and would diffuse through
  nuclear pores regardless, so this needs a targeted experiment, not an annotation.
- **Winged-helix fold without DNA binding.** [PMID:21082705] solved the NMR structure (PDB 2L2O).
  The fold is winged-helix-like but the groove is hydrophobic and the recognition helix negatively
  charged, so the natural reading is protein interaction, not DNA. No DNA-binding annotation
  exists and none should be added.
- **Cancer biology.** Multiple knockdown papers in oesophageal, breast, gastric and glioma lines,
  plus upstream regulators MYBL2, CBX4 and miR-145-5p. These are disease-context studies of a
  normal actin regulator; they do not add a distinct GO process for the gene and are not
  annotated here.


## Correction: the family is not single-copy, and the subfamily structure matters

A first draft of this review called PTHR46334 a single-copy family, in five places. **The PR's own
fetched data contradicts that** — `RESULTS.md` shows *Arabidopsis* = 2 and *Zea mays* = 3, and the
PANTHER metadata records `subfamilies: 2`.

Resolving the entries file:

| Subfamily | Members | Composition |
|---|---|---|
| `PTHR46334:SF1` | 13 | animals, *Dictyostelium*, and most plant entries — includes **human ABRACL (Q9P1F3)** and **Dicty cosA (Q558Y7)** |
| `PTHR46334:SF3` | 2 | plant-restricted: *Arabidopsis* Q8LBN7, *Eutrema* B4YYA9 |

This does **not** weaken the `GO:0032970` ACCEPT — it strengthens the provenance argument. The IBA
donor (*Dictyostelium* cosA) and the human target are **both SF1**, so the transfer is
*within-subfamily* and is not crossing the one boundary the family contains. The `propagation_review`
now names that boundary rather than denying one exists.

The lesson: the copy-number claim was a summary written alongside the analysis rather than read out
of it, and the analysis script printed it as hardcoded prose regardless of the counts fetched. Any
claim a script asserts should be derived from what the script fetched.


## Two verifications added after review

**`GO:0000513` is real.** It is absent from the local ontology cache, so the reviewer could not
check it. QuickGO confirms: `GO:0000513 actin severing activator activity`, molecular_function,
not obsolete, defined as *"Binds to and increases the activity of a actin severing protein."* That
is exactly the positive counterpart of the inhibitor activity proposed under `proposed_new_terms`,
so the asymmetry the proposal rests on is genuine.

**RPGRIP1L is genuinely ciliary.** Conceded in the review rather than glossed: of the four BioID
baits that labelled ABRACL, three (SASS6, CNTRL, DCTN1) are centriolar or dynactin proteins, but
RPGRIP1L is a transition-zone protein. The bait panel is therefore not uniformly non-ciliary. It
does not rescue the annotation — proximity to one ciliary bait over hours of labelling is a
neighbourhood observation, not a localisation — but the argument is stronger for stating the
inconvenient part.
