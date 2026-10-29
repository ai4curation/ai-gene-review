# hedgehog (hh), *Drosophila melanogaster* — curation notes

UniProt Q02936 · FlyBase FBgn0004644 · CG4637 · 471 aa precursor.
PANTHER family PTHR11889, subfamily PTHR11889:SF31 (protostome HEDGEHOG).

These are my working notes for the GO annotation review in `hh-ai-review.yaml`.
Assertions carry the citation they rest on; quoted text is verbatim from the cached
publication in `publications/`.

---

## 1. What the protein is

One gene, one ligand. Where vertebrates have SHH, IHH and DHH, the fly has a single
Hedgehog, which makes it the anchor for every pan-metazoan claim about the family — the
PANTHER family review (`interpro/panther/PTHR11889/PTHR11889-review.yaml`) says as much,
and the PAINT node PTN001726121 that carries *patched binding*, *smoothened signaling
pathway* and *extracellular region* is seeded by FB:FBgn0004644 alongside the vertebrate
genes.

The protein is made as a precursor with two functionally unrelated halves. UniProt's
feature table gives the anatomy: SIGNAL 1..?, PROPEP ?..84, CHAIN 85..471 (Protein
hedgehog), CHAIN 85..257 (Protein hedgehog N-product), SITE 257..258 "Cleavage; by
autolysis", LIPID 85 "N-palmitoyl cysteine", LIPID 257 "Cholesterol glycine ester".

### 1.1 The C-terminal half is an enzyme, not a signal

The 25 kDa C-terminal domain performs an intramolecular cleavage coupled to cholesterol
transfer:

> [PMID:9335337 "The approximately 25 kDa carboxy-terminal domain of Drosophila Hedgehog
> protein (Hh-C) possesses an autoprocessing activity that results in an intramolecular
> cleavage of full-length Hedgehog protein and covalent attachment of a cholesterol moiety
> to the newly generated amino-terminal fragment."]

That paper is a crystal structure of the *Drosophila* domain, with active-site residues
identified and probed by mutagenesis [PMID:9335337 "Residues in the Hh-C17 active site
have been identified, and their role in Hedgehog autoprocessing probed by site-directed
mutagenesis."]. UniProt records the outcome on the fly protein: SITE 303 "Involved in
cholesterol transfer" with MUTAGEN D303A "No cholesterol transfer"; SITE 326 "Involved in
auto-cleavage" with T326A "Greatly reduced autoprocessing activity"; SITE 329 "Essential
for auto-cleavage" with H329A "No autoprocessing activity". So the fly protein has its
*own* direct structural and mutational evidence for both halves of the reaction — the
ISS rows for GO:0140853 and GO:0016540 (transferred from mouse Q62226) are not the only
support.

The N-terminal product is the active species [PMID:7885476 "We show here that the N
product is the active species in both local and long-range signalling."], and the
cleavage site itself was mapped in the same paper.

**Intein homology is not splicing.** The same structure paper reports that "Aspects of
sequence, structure, and reaction mechanism are conserved between Hh-C17 and the
self-splicing regions of inteins" [PMID:9335337]. An InterPro2GO mapping turns this into
GO:0016539 *intein-mediated protein splicing*. Checked the term definition against
QuickGO: it requires excision of the intein **and** joining of the N- and C-terminal
exteins by a normal peptide bond. Hedgehog ligates nothing — the two products separate,
and one leaves with cholesterol on it. REMOVE. (The human SHH review made the same call.)

### 1.2 Palmitoylation is done by someone else

Rasp / Skinny hedgehog is the acyltransferase [PMID:11486055 "Our results suggest that
ski encodes an enzyme that acts within the secretory pathway to catalyze amino-terminal
palmitoylation of Hh, and further demonstrate that this lipid modification is required for
the embryonic and larval patterning activities of the Hh signal."]. Useful for the
participation test: palmitoylation of Hh is performed by Rasp, so it is not an hh
activity, and there is no GOA row asking me to pretend otherwise.

### 1.3 Calcium sites — resolving a question the family review left open

`PTHR11889-review.yaml` marks the PTN001726121 *calcium ion binding* row UNRESOLVED
because its three seeds are human paralogs while the node sits at Eumetazoa, and asks
whether the coordinating residues are conserved outside vertebrates. Two observations
from the cached UniProt record settle it in the affirmative, at least for the fly:

1. UniProt itself carries BINDING features for two Ca(2+) ions on Q02936 at residues
   149, 150, 155, 185, 186, 189 and 191, with evidence `ECO:0000250|UniProtKB:Q15465` —
   i.e. curators propagated the sites from human SHH onto the fly entry.
2. The fly residues at those positions, read off the SQ block, are E, E, D, T, E, D, D —
   the acidic/hydroxyl set a calcium shell needs.

This is consistent with the IBA rather than contradicting it, so the row is kept (as
non-core: the metal is a structural feature of the signalling domain, not an activity).
I have **not** added `residue_sites` anywhere, and I am not claiming the sites are
experimentally demonstrated in the fly — only that the sequence question the family
review asked has an answer consistent with the annotation.

---

## 2. Reception: where fly and vertebrate genuinely differ

Vertebrate SHH binds PTCH1 directly. In the fly, Patched alone was never shown to bind
Hh; the receptor is a two-component affair:

> [PMID:20048000 "We demonstrate that Ihog interacts directly with Ptc, is required for
> presentation of Ptc on the cell surface, and that Ihog and Ptc are both required for
> high-affinity Hh binding."]
> [PMID:20048000 "On the basis of their joint roles in ligand binding, signal
> transduction, and receptor trafficking, we conclude that Ihog and Ptc together
> constitute the Drosophila Hh receptor."]

Ihog binds Hh through the first of its two fibronectin type III repeats [PMID:16630821
"The first of two extracellular fibronectin type III (FNIII) domains of the Ihog protein
mediates a specific interaction with Hh protein in vitro"], heparin-dependently
[PMID:17077139 "These results establish that Hh directly binds Ihog and provide the first
demonstration of a specific role for heparin in Hh responsiveness."]. The structure of
the complex is in that paper.

This matters for the five GO:0005515 *protein binding* rows. Four of them record Ihog
(FB:FBgn0031872 = Q9VM64, confirmed via the UniProt cross-reference query, since the
FlyBase API was down). Per repo policy, a bare protein-binding row gets MODIFY when the
paper supports something more informative, otherwise REMOVE. GO:0005113 *patched binding*
would be wrong — the recorded partner is Ihog, not Ptc — so I proposed GO:0005102
*signaling receptor binding* (label verified against QuickGO), which says the partner is
a component of the receptor that transduces the signal, and nothing more. The fifth row
records Shifted (Q9W3W5), a secreted WIF-family modulator of Hh diffusion [PMID:15691765
"In contrast, Shf is required for Hh stability and for lipid-modified Hh diffusion."] —
no receptor, no catalysis, no evidence-backed specific term, so REMOVE.

The consequence of Hh–Ihog binding is also annotated as GO:0034111 *negative regulation
of homotypic cell-cell adhesion* [PMID:31209108 "We further demonstrate that Hh interferes
with Ihog-mediated homophilic interactions by competing for Ihog binding."]. Unusual in
that Hh really does perform this directly — by competition — but it is the same binding
event GO:0005113 already records, and the adhesive activity belongs to Ihog, so non-core.

---

## 3. Localisation: two errors worth removing

### 3.1 Nucleus and cytoplasm come from an RNA experiment

GOA carries GO:0005634 (EXP) and GO:0005737 (EXP) from PMID:1280560, plus IEA rows that
inherit the same statement through the UniProt SUBCELLULAR LOCATION lines ("Nuclear up to
embryonic stage 10 and then at stage 11 shifts to the cytoplasm"). The paper's own
abstract says what was observed:

> [PMID:1280560 "This RNA is localized predominantly within nuclei until stage 10, when
> the localization becomes primarily cytoplasmic."]

That is the *hh transcript*, not the Hh protein; the paper is a molecular-organisation and
in-situ expression study and reports no anti-Hh antibody data. A protein with a cleaved
signal sequence that autoprocesses in the ER lumen and is released from the cell has no
route to the nucleoplasm. This is not a case of second-guessing an assay I cannot see —
the abstract states the observation — so REMOVE all four rows, and flag PMID:1280560's
`reference_review` as MISCITED for this use.

### 3.2 Cytosol is a Reactome compartment default

Three GO:0005829 rows trace to cached Drosophila Reactome events. One is literally titled
"N-HH moves from the cytosol to the extracellular region" (R-DME-209271); the others are
"Autocleavage of HH" (R-DME-209313) and "N-HH is palmitoylated by RASP" (R-DME-209357).
All three steps happen in the secretory pathway. GO:0005829 is defined (QuickGO) as the
part of the cytoplasm that does not contain organelles, so this is wrong rather than
merely vague. REMOVE. The three *extracellular region* rows from the same Reactome model
(R-DME-209178/209271/209272) are fine and kept as core.

Note this differs from the human SHH review, which kept its cytosol TAS rows as non-core
on the reasoning that they concern retrotranslocated fragments destined for degradation.
The fly Reactome events are different events with a different justification, hence the
different call.

---

## 4. Morphogen behaviour

The term GO:0016015 asks for action over a concentration gradient. Fly Hh is the textbook
case, and the cited rows give threshold-specific responses at three levels:

- Target genes: [PMID:20412775 "Here, we show that interfering with the amount of apical
  Hh causes a dramatic change in the long-range activation of low-threshold Hh target
  genes, without similar effect on short-range, high-threshold targets."]
- Smo phosphorylation: [PMID:22537496 "Thus, the differential phosphorylation of Smo
  mediates the thresholds of Hh activity."]
- Ci phosphorylation: [PMID:36271509 "Phosphorylation at the N-terminal, middle, and
  C-terminal Fu/CK1 sites occurred independently of one another and each increased
  progressively in response to increasing levels of Hh or increasing amounts of Hh
  exposure time."]

Transport is cytoneme-borne as well as diffusive [PMID:28825565 "Previously we
demonstrated that Hedgehog (Hh) morphogen is transported via vesicles along cytonemes
emanating from signal-producing cells to form a gradient in Drosophila epithelia."], and
range is gated by the lipid anchors themselves [PMID:29522397 "Hence, palmitoylated
membrane anchors restrict morphogen spread until site-specific processing switches
membrane-bound Hh into bioactive forms with specific patterning functions."].

The DHH caveat recorded in the family review (juxtacrine, poorly autoprocessed) does not
apply to the fly gene; if anything the fly is the cleanest morphogen in the family.

---

## 5. The germ cell migration dispute

GOA carries both sides, which is the right thing for it to do:

- Positive: IMP from the chromosome-3 screen [PMID:9435287], IGI ×2 with disp and Hmgcr
  [PMID:16256738 "Consistent with this model, there are substantial germ cell migration
  defects in trans combinations between hmgcr and mutations in different components of the
  hh pathway."], and a TAS for GO:0035232 *germ cell attraction* from a 2003 review
  [PMID:12814944].
- Negative: a **NOT** annotation on GO:0008354 [PMID:19389345 "In contrast to previously
  reported findings and consistent with findings in zebrafish our data do not support the
  notion that Hh has a direct role in the guidance of migrating germ cells in flies."],
  from a study that deliberately repeated the earlier critical experiments
  [PMID:19389345 "We therefore repeated several critical experiments and carried out
  further experiments to test specifically whether Hh is a germ cell attractant in
  flies."].

How I resolved it. The repo's consistency rule wants one action per GO term, and the four
GO:0008354 rows (three positive plus the negation) therefore share KEEP_AS_NON_CORE: hh
mutants *do* show migration defects, but the likely route is the gonadal mesoderm, which is
annotated separately from the same screen [PMID:9435287 "Many of these genes are involved
in the development of gonadal mesoderm, the tissue that associates with germ cells to form
the embryonic gonad."]. The NOT row is retained and its reason says plainly that it
asserts absence and that the negation is well supported.

GO:0035232 *germ cell attraction* is the one I removed. It is the strongest form of the
claim — Hh as an attractant — it is exactly what PMID:19389345 tested and rejected, and its
only support is a traceable author statement in a review published before the refutation.

---

## 6. Everything else is a tissue outcome

Sixty-eight rows are KEEP_AS_NON_CORE, and almost all are of one kind: a fly developmental
phenotype. Segment polarity (the phenotype the gene is named for), morphogenetic furrow
progression [PMID:8252628 "We show that hh expression posterior to the morphogenetic
furrow is continuously required for its progression."], wing/leg/eye/labial/genital disc
patterning, tracheal branching, hindgut, heart (via wg — [PMID:8660881 "Here, we show that
wg is epistatic to hedgehog (hh), another secreted segmentation gene product, in its
requirement for heart formation."]), glial migration, ovarian stem cell maintenance
[PMID:11279500 "These cells cannot proliferate as stem cells in the absence of Hh
signalling, whereas excessive Hh signalling produces supernumerary stem cells."], and the
adult gut immune response [PMID:25639794 "Here, we show that the Hedgehog (Hh) signaling
pathway modulates uracil-induced DUOX activation."].

All are sound and worth keeping for retrieval. None is a *function of the protein*: one
ligand, one biochemical output, many tissues. Core status is reserved for autoproteolysis
with cholesterol transfer, Patched binding, and the smoothened signalling pathway.

A second family of non-core rows is the downstream-consequence terms: inhibition of Ci
proteolysis [PMID:9215627 "Hh inhibits proteolysis of Ci, and we suggest that this
inhibition leads to the observed patterns of expression of key target genes at the
compartment border."], Smo surface accumulation [PMID:19088085 "We further find that PP4
regulates the Hh-induced Smo cell-surface accumulation."], regulation of bnl/FGF
[PMID:24651658], and the IBA *regulation of gene expression*. In each the work is done by
something else — the proteasome, Smo trafficking machinery, Ci/Gli — and Hh sets the rate.

---

## 7. Two UNDECIDED rows

- GO:0048066 *developmental pigmentation*, TAS PMID:12957543.
- GO:0048099 *anterior/posterior lineage restriction, imaginal disc*, TAS PMID:10625531.

Both cited records have **no abstract** in the local cache, and an efetch query to PubMed
returns title and identifiers only for both. The standing rule is UNDECIDED when the
relevant publication cannot be accessed. Both claims are plausible on general grounds, but
plausibility is not evidence, and no other reference in this set covers either claim. Their
`reference_review` entries are marked UNVERIFIED with the reason.

(PMID:10625531 is also cited for GO:0048100 *wing disc anterior/posterior pattern
formation*, which I did **not** mark undecided: that term carries three further citations,
including [PMID:15104233 "Ci is regulated through communication of the membrane proteins
Patched (Ptc) and Smoothened (Smo) to the intracellular Hedgehog Signaling Complex (HSC)
in response to a graded concentration of Hh ligand."], so the term is not in doubt even
though one of its four anchors is unreadable.)

---

## 8. Divergences recorded deliberately

1. **GO:0004175 endopeptidase activity → GO:0140853.** The module
   `modules/hedgehog_signaling.yaml` types its `hh_autoprocessing` annoton with
   GO:0004175. I MODIFYed the fly ISS row to GO:0140853, matching the human SHH review,
   because endopeptidase activity is defined as *hydrolysis* of internal peptide bonds and
   Hedgehog self-processing resolves its thioester with cholesterol rather than water. The
   module may want revisiting; I have not touched it.
2. **GO:0010468 regulation of gene expression (IBA).** The human SHH review records
   ACCEPT; I recorded KEEP_AS_NON_CORE, agreeing with the family review's own assessment
   that this is "sound placement of a weak term" whose work is performed by Ci/GLI.
3. **GO:0005829 cytosol.** Human SHH keeps its Reactome cytosol rows as non-core; the fly
   Reactome events are different events and I removed them (§3.2).

## 9. Not proposed

No `NEW` rows. Two candidates were considered and rejected on the participation test:

- *Protein palmitoylation* — performed by Rasp on Hh as substrate, not by Hh
  [PMID:11486055].
- *Cytoneme assembly* already exists as an IMP row; I kept it non-core rather than
  promoting it, because the protrusion is built by the cytoskeleton of the cell that
  extends it, with Hh as an input.

`GO:0016015 morphogen activity`, `GO:0005113 patched binding`, `GO:0140853` and
`GO:0007224` were all already present, so the three core functions are drawn from accepted
rows and nothing needed to be manufactured.
