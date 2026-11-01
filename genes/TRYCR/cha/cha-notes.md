# Curation notes: *Trypanosoma cruzi* chagasin (cha, Q966X9)

**Deep research was unavailable for this review.** No deep-research API keys are
configured in this container, so `just deep-research` was not run and no
`-deep-research-<provider>.md` file exists for this gene. The literature below was
assembled directly from the cached publications in `publications/`, PubMed/PMC
lookups, and the curated UniProtKB record `cha-uniprot.txt`.

**The GONUTS wiki was unavailable.** `https://gowiki.tamu.edu/wiki/index.php/PMID:11719560`
returns only "This site is temporarily offline while we perform upgrades", matching
what `projects/CACAO.md` records for 2026-10-29, so the student's own evidence page
for the four CACAO rows could not be consulted. Fortunately the cached abstract of
PMID:11719560 states each annotated claim explicitly (see below), so no CACAO row on
this gene had to be judged blind.

## What chagasin is

Chagasin is a 110-residue, heat-stable protein of *T. cruzi* and the signature member
of MEROPS inhibitor family I42 (`DR MEROPS; I42.001`). It is a tight-binding,
reversible, 1:1 inhibitor of papain-family (clan CA, family C1) cysteine peptidases
[PMID:18201565 "It is a single 110-residue polypeptide chain with no sequence
similarity to other known groups of CP inhibitors and potently inactivates papain-like
enzymes through the formation of 1:1 tight–binding complexes."]. It has no sequence or
fold relationship to the cystatins: it adopts an immunoglobulin-like fold with homology
to human CD8alpha [PMID:17502099 "Chagasin has a unique variant of the immunoglobulin
fold with homology to human CD8alpha."], and presents three loops (L2/BC, L4/DE, L6/FG)
on one face as a tripartite inhibitory wedge
[PMID:17561110 "An inhibitory wedge composed of three loops (L2, L4, and L6) forms a
number of contacts responsible for high-affinity binding (K(i), 39 pM) to the enzyme."].
Loop L2 inserts directly into the catalytic cleft and contacts the catalytic residues
[PMID:17561110 "All three loops interact with the catalytic groove, with the central
loop L2 inserted directly into the catalytic center."]. UniProt records the same three
motifs as `FT MOTIF` BC (29-34), DE (59-68) and FG (91-100).

Affinities are picomolar and broad across the C1 family: papain K(i) = 5 pM
[PMID:18201565 "WT Ki = 5 ± 0.7 pM"], human cathepsin L K(i) = 39 pM
[PMID:17561110 "high-affinity binding (K(i), 39 pM) to the enzyme"], human cathepsin B
K(i) sub-nanomolar [PMID:18515357 "Ki for H110A cathepsin B, 0.35 nm"], and papain
association essentially diffusion-limited
[PMID:19143838 "inactivation of papain by chagasin is very fast (k(on) = 1.5 x 10(6)
M(-1) x s(-1)), and results in the formation of a very tight, reversible complex (K(i)
= 36 pM)"].

## Two different claims: parasite cruzipain versus host cathepsins

This gene's annotation hinges on keeping two claims apart.

1. **Chagasin regulates the parasite's own cruzipain *in vivo*.** This is the
   established biological role. Chagasin and cruzipain co-localise in the secretory
   and endocytic pathway, chagasin-cruzipain complexes are recovered from living
   epimastigotes, and raising chagasin levels genetically collapses parasite cysteine
   peptidase activity [PMID:15713748 "Ultrastructural studies showed that chagasin and
   cruzipain both localize to the Golgi complex and reservosomes (lysosome-like
   organelles), whereas free chagasin was found in small intracellular vesicles"];
   [PMID:15713748 "we obtained direct evidence that chagasin-cruzipain complexes are
   indeed formed in epimastigotes"]; [PMID:15713748 "These phenotypic changes were
   accompanied by a drastic reduction of soluble cruzipain activity and by upregulated
   secretion of cruzipain-chagasin molecular complexes."]. The consequences are
   parasite-intrinsic: reduced metacyclogenesis and reduced infectivity, both traced
   back to loss of parasite peptidase activity rather than to anything done to the host
   [PMID:15713748 "Chagasin transfectants (fourfold increase in CP inhibitory activity)
   displayed low rates of differentiation (metacyclogenesis) and exhibited increased
   resistance to a synthetic CP inhibitor."]; [PMID:15713748 "The deficiency of chagasin
   overexpressers is caused by lower activity of membrane-associated CPs, because
   membranes recovered from wild-type trypomastigotes restored infectivity and this
   effect was nullified by the CP inhibitor E-64."]; [PMID:18201565 "T. cruzi lines that
   overexpress chagasin have an 80% decrease in active CPs, are less capable to
   differentiate and are less infective to mammalian cells in vitro"]. Note the
   direction: the authors are explicit that the modulation of differentiation and
   invasion is **indirect**, via the endogenous peptidase [PMID:15713748 "our studies
   suggest that chagasin regulates the endogenous activity of CP, thus indirectly
   modulating proteolytic functions that are essential for parasite differentiation and
   invasion of mammalian cells."].

2. **Chagasin inhibits host cathepsins *in vitro*.** Chagasin binds and inhibits human
   cathepsin L and cathepsin B, and the complexes have been crystallised
   [PMID:17561110 "We have crystallized and solved the structure of chagasin in complex
   with the host cysteine protease, cathepsin L, at 1.75 A resolution."];
   [PMID:18515357 "we have analyzed the structure and function of cathepsin B in
   complexes with the Trypanosoma cruzi inhibitor, chagasin"]. It even inhibits the
   *Plasmodium* protease falcipain-2 (UniProtKB:Q9NBD4), which is the basis of the
   IntAct IPI row, and plant papain. But these are cross-reactivities of a broad-spectrum
   C1 inhibitor measured with purified enzymes. **No published work shows chagasin
   inhibiting a host protease inside an infected host cell**, and the family review is
   candid that the biological roles vary by species and rest mostly on transgenic work
   [PMID:26546840 "Studies on their biological roles were carried out in a few species,
   mainly using transgenic protozoa, and the conclusions vary."]. The host-protease
   affinity is also not merely incidental: chagasin makes contacts with cathepsin L
   helix 8 that it does not make with cruzipain [PMID:18201565 "These differential
   effects reflect the occurrence of direct interactions between chagasin and helix 8 of
   cathepsin L, interactions that do not occur with cruzipain."], so the two targets are
   discriminable and a host-directed role remains a live hypothesis rather than a
   finding.

Consequence for annotation: the molecular function `GO:0004869 cysteine-type
endopeptidase inhibitor activity` is target-agnostic and is supported by both lines.
A *biological process* term is only warranted for claim 1 — hence `GO:0010951 negative
regulation of endopeptidase activity` proposed here against the parasite's own
peptidases. No symbiont-mediated / interspecies term (the `GO:0052[0-9]*` branch, e.g.
modulation of host protease activity) is proposed, because claim 2 has never been
demonstrated in an infected cell. Likewise no `involved_in` term for metacyclogenesis or
host-cell invasion: the authors themselves call that modulation indirect, and chagasin
performs no step of either process — it only sets the level of the peptidase that does.

## Localization

Immunogold EM in PMID:11719560 gives three locations directly, in the two life stages
examined [PMID:11719560 "Gold-labeled antibodies localized chagasin to the flagellar
pocket and cytoplasmic vesicles of trypomastigotes and to the cell surface of
amastigotes."], and the cell-surface result is independently confirmed on living cells
by FITC-probe binding [PMID:11719560 "Binding assays performed by probing living
parasites with fluorescein (FITC)-cruzipain or FITC-chagasin revealed the presence of
both inhibitor and protease at the cell surface of amastigotes."]. "Flagellar pocket" is
an exact synonym of `GO:0020016 ciliary pocket` (verified in QuickGO), so the CACAO
term choice is a direct match rather than a stretch. UniProt curates the same three
locations from the same paper with `ECO:0000269|PubMed:11719560`, which is what the
three GO_REF:0000044 IEA rows restate.

PMID:15713748 adds two compartments that are absent from GOA: the Golgi complex and the
reservosome (`GO:0106123`, a term created specifically for the *Schizotrypanum*
organelle). Both are proposed as NEW rows here.

## CACAO row assessment (four rows, all PMID:11719560, all IDA, 2013-02-10)

All four CACAO rows on this gene are **sound as written**. The paper is about chagasin,
it is the paper that named the protein, every annotated claim is stated in the abstract
with the assay named, the evidence code IDA fits (immunogold EM; enzyme-inhibition
kinetics on the purified protein), and each term sits at the granularity the assay
resolved. None of the eight failure shapes catalogued in `projects/CACAO.md` applies:

- Not *phenotype read as process* — no BP row was written at all, and the obvious
  tempting ones (metacyclogenesis, host-cell invasion) were correctly left alone. The
  students stopped where the 2001 paper stops.
- Not *paper not about the gene* — this is the gene's discovery paper.
- Not *single-assay localization* — `cell surface` has two independent assays
  (immunogold EM and FITC-probe binding on living parasites), and the other two CC rows
  come from the same EM dataset that UniProt also curated as `ECO:0000269`.
- Not *wrong granularity* — `cytoplasmic vesicle` looks like a parent-level term, but
  the 2001 EM did not resolve the vesicle identity and the 2005 follow-up still calls
  the free-chagasin compartment "small intracellular vesicles", so the parent is as
  precise as the evidence goes. Correctly general, not over-general.

The one thing the students did not do is the part-of/located_in distinction (`part_of
cell surface` is odd for a non-complex), but qualifiers are inert for review purposes
per repository policy, and the underlying claim is right.

This makes chagasin a useful **negative control** for the CACAO project: a case where
community curation from a single classic paper produced four annotations that need no
correction. The one row that does need work (`GO:0005515 protein binding`) is not a
CACAO row — it is an IntAct IPI import.

## The IntAct protein-binding row

`GO:0005515` with `UniProtKB:Q9NBD4` (verified in UniProt as "Cysteine protease
falcipain-2", *Plasmodium falciparum*) comes from PMID:17502099, the chagasin-falcipain-2
crystal structure. The interaction is real but the term carries no functional
information, and the paper supports the informative replacement directly: UniProt cites
this very paper with `ECO:0000269` for chagasin's inhibitor function. Per the
protein-binding policy this is a `MODIFY` to `GO:0004869`, not a `REMOVE` and not an
`ACCEPT`. Worth noting the partner is a *Plasmodium* enzyme used as a crystallographic
surrogate — *T. cruzi* and *P. falciparum* share no host cell, so this is not a
physiological interaction and should not be read as evidence of a host- or
co-infection-directed role.

## Open questions carried into the review

- Is chagasin ever delivered to a compartment where it meets host cathepsin L or B? The
  secreted cruzipain-chagasin complexes of PMID:15713748 are the only hint of an
  extracellular pool.
- Is the reservosome/Golgi pool the functional site, or is the trafficking intersection
  the regulatory point the 2001 authors proposed [PMID:11719560 "The intersection of
  chagasin and cruzipain trafficking pathways may represent a checkpoint for downstream
  regulation of proteolysis in trypanosomatid protozoa."]?
- The genetic evidence is all gain-of-function (overexpression). A null has not been
  reported, so the loss-of-function phenotype of chagasin is unknown.
