# ACAP1 (Q15027) — review notes

ArfGAP with coiled-coil, ANK repeat and PH domains 1; a.k.a. centaurin-beta-1, CENTB1, KIAA0050.
740 aa, chromosome 17, PANTHER PTHR23180 (CENTAURIN/ARF), subfamily SF197.
Domain order: BAR (1–226) — PH (265–360) — Arf-GAP (405–527, C4 Zn finger 420–443) — 3× ANK (606–702).

## 1. What the gene does

**ARF6 GAP.** Jackson et al. 2000 identified ACAP1 and ACAP2 as Arf6 GAPs and measured GAP activity
directly for both: [PMID:11062263 "In vitro, ACAP1 and ACAP2 preferred Arf6 as a substrate, rather than
Arf1 and Arf5, more so than did ASAP1."]. The activity is phosphoinositide-dependent
[PMID:11062263 "ACAP1 and ACAP2 are preferentially activated by phosphatidylinositol 4,5-bisphosphate
[PIP2; not shown] and do contain GAP activity."], and the arginine finger mutant is catalytically dead
[PMID:11062263 "[R448Q]ACAP1 and [R442Q]ACAP2 had no detectable activity using Arf6 as a substrate"].

**Where it acts.** ACAP1 is largely soluble at rest and is recruited to membranes by ARF6-GTP:
[PMID:11062263 "In untreated cells, although ACAP1 and ACAP2 were primarily cytosolic, they could be
observed on tubular portions of the Arf6 endosomal compartment"], and recruitment fails when ARF6 is
locked off [PMID:11062263 "ACAP1 remained cytosolic and was not recruited to the endosome or the plasma
membrane in cells expressing the dominant-negative Arf6, T27N, even in the presence of AlF4"]. So both
the endosomal and the plasma-membrane pools are real, and both are ARF6-dependent. It is also at the
cell surface during ruffling [PMID:11062263 "During PDGF stimulation of NIH 3T3 cells, ACAP1, ACAP2, and
ASAP1 colocalized in dorsal ruffles and at the edge of resting and protrusive HeLa cells."]. UniProt
records the steady-state location as recycling endosome membrane, peripheral, cytoplasmic side
(ECO:0000269|PubMed:16256741). Chen et al. place it on a tubular recycling endosome distinct from the
ARAP2/APPL1 compartment [PMID:25225293 "ARAP2 formed a complex with APPL1 and colocalized with Arf6 and
APPL in a compartment distinct from the Arf6/ACAP1 tubular recycling endosome."].

Note a useful dissociation: the GAP-dead mutant loses the endosomal pool but keeps the surface pool
[PMID:11062263 "A point mutant of ACAP1 that lacked GAP activity was not observed on the tubular
endosomes, but rather was associated with the plasma membrane protrusions"] — catalysis and
surface recruitment are separable.

**Coat component / cargo adaptor.** ACAP1 is a subunit of a clathrin coat that operates on the
recycling route rather than at endocytosis [PMID:17664335 "We find that ACAP1, a GTPase-activating
protein (GAP) for ADP-ribosylation factor (ARF) 6, is part of a novel clathrin coat complex that is
regulated by ARF6 for endocytic recycling in two key physiological settings, stimulation-dependent
recycling of integrin that is critical for cell migration and insulin-stimulated recycling of glucose
transporter type 4 (Glut4), which is required for glucose homeostasis."]. It binds CLTC directly and
also SLC2A4/GLUT4's third cytoplasmic loop (UniProt SUBUNIT).

**Regulated cargo capture.** Akt phosphorylates Ser-554; that is what licenses ITGB1 binding
[PMID:16256741 "the role of ACAP1 in beta1 recycling requires its phosphorylation by Akt"], and
S554A abolishes binding and migration while S554D enhances binding (UniProt MUTAGEN). Bai et al.
mapped the cargo signal and the switch [PMID:22645133 "We initially defined a critical sequence in the
cytoplasmic domain of integrin β1 recognized by ACAP1 and showed that this sequence acts as a recycling
sorting signal."].

**Membrane bending.** Unusually for a BAR protein, the curvature work is done by the PH domain
[PMID:25284369 "Here, we show that this BAR domain can neither bind membrane nor impart curvature, but
instead requires a neighboring PH (Pleckstrin Homology) domain to achieve these functions."], with the
BAR domain instead oligomerising ACAP1 into a lattice. The in vitro assay is liposome binding plus
negative-stain EM of purified BAR-PH [PMID:25284369 "We next found that ACAP1BAR-PH also induces
membrane curvature, as reflected by the tubulation of liposomes, which was visualized by negative-stain
electron microscopy (EM)"], and the BAR domain fails it on its own [PMID:25284369 "the BAR domain of
ACAP1 also showed little affinity to the generated liposomes, regardless of their size"]. The bilayer
contact comes from PH-domain Loop1, whose distal Phe-280 inserts into one leaflet
[PMID:25284369 "We found that F280 is also critical for the induction of membrane curvature"] and whose
mutants titrate the activity [PMID:25284369 "In particular, mutation of this residue to alanine (F280A)
reduced the ability of ACAP1BAR-PH to induce liposome tubulation, while a more conservative mutation
(F280W) preserved the ability to tubulate liposomes."]. The cryoEM reconstruction of a coated tubule
is explicit that the BAR domain never touches the membrane
[PMID:25284369 "Second, there is no significant interaction between the BAR domain and the underlying
membrane."] and that its role is the inter-molecular packing
[PMID:25284369 "Instead, the BAR domain contributes to the packing interfaces among ACAP1BAR-PH protein
in assembling the coating on liposome membrane."]. One PH domain per dimer suffices
[PMID:25284369 "this additional finding suggests that one PH domain is sufficient to confer the ability
of the ACAP1BAR-PH dimer to insert into membrane and impart curvature"]. Tubulation in cells needs both domains
[PMID:17010122 "Truncated and point mutations in the ACAP1 BAR and PH domains revealed that both BAR and
PH domains are required for tubulation."] and is strongly enhanced by PIP5K co-expression
[PMID:17010122 "While there were few tubules induced by the expression of ACAP1 alone, numerous
endosomal tubules were induced by coexpression of PIP5K and ACAP1."]. K274N in the PH domain kills
PIP2/PIP3 binding and endosomal-tubule association (UniProt MUTAGEN).

**Actin.** The actin readouts are real but downstream of ARF6 and obtained by overexpression:
[PMID:11062263 "In HeLa cells, overexpression of either ACAP blocked the formation of Arf6-dependent
protrusions."] and [PMID:25225293 "ARAP2 overexpression promoted large FAs, but ACAP1 overexpression
reduced FAs."]. Knockdown gives the converse traffic phenotype
[PMID:25225293 "ARAP2 knockdown slowed, whereas ACAP1 knockdown accelerated, integrin β1
internalization."].

## 2. The headline curation problem: an experimentally void GO record

ACAP1 has 19 GOA rows. Not one is IDA, IMP or IGI. Every functional statement is IBA (4), IEA (3),
or the 11 `protein binding` IPI rows; the only other experimental row is one HDA.

I queried QuickGO for ACAP1 annotations from each of its seven primary papers. All seven return zero:

| PMID | topic | ACAP1 GO annotations |
|---|---|---|
| 11062263 | ARF6 GAP activity, PIP2 dependence, R448Q | 0 |
| 16256741 | Akt-S554, ITGB1 recycling, cell migration | 0 |
| 17398097 | GULP1/ARF6 complex | 0 |
| 17664335 | ACAP1 clathrin coat, ITGB1 + GLUT4 recycling | 0 |
| 22645133 | ITGB1 recycling sorting signal, autoinhibition | 0 |
| 25284369 | PH-domain membrane curvature, BAR lattice | 0 |
| 25225293 | tubular recycling endosome, ARAP2 contrast | 0 |

UniProt has read all of these — its FUNCTION, SUBUNIT, DOMAIN and PTM blocks carry ECO:0000269 for
each — but none of it reached GO. So a protein with seven PDB entries and a 25-year literature is,
in GO, a phylogenetic inference.

## 3. Paralog check (the point of this campaign)

Every WITH/FROM accession resolved:

| Annotation | WITH/FROM | identity |
|---|---|---|
| GO:0005096 GTPase activator activity IBA | AT5G13300 | Arabidopsis AGD3 |
| | MGI:2153589 | **mouse Acap3** (paralog) |
| | SGD:S000002932 | yeast AGE1 (YDR524C) |
| | UniProtKB:Q15057 | **human ACAP2** (paralog) |
| | dictyBase:DDB_G0279649 | Dicty Q54WI0, BAR+PH+ArfGAP |
| GO:0005886 plasma membrane IBA | AT5G13300 / AT5G61980 | Arabidopsis AGD3 / AGD1 |
| | PomBase:SPBC17G9.08c | S. pombe csx2 |
| | UniProtKB:Q15057 | **human ACAP2** (paralog) |
| | WB:WBGene00000565 | C. elegans cnt-1 |
| | dictyBase:DDB_G0279649 | Dicty Q54WI0 |
| GO:0010008 endosome membrane IBA | RGD:1562939 | **rat Acap2** (paralog) |
| | WB:WBGene00000565 | C. elegans cnt-1 |
| GO:0030036 actin cytoskeleton organization IBA | FB:FBgn0004133 | **Drosophila blow** — PH domain only |
| | dictyBase:DDB_G0276395 | Dicty Q551Q8, PH+ArfGAP |
| | dictyBase:DDB_G0279649 | Dicty Q54WI0, BAR+PH+ArfGAP |

Three IBAs draw on ACAP2/ACAP3 orthologues or paralogues. That is legitimate PAINT practice — an
ancestral node may be supported by any experimentally annotated descendant — and the source functions
(GAP activity, endosome membrane, plasma membrane) are ancestral to the whole ACAP clade, so none of
these is a bad transfer. The `neuron migration` and `regulation of neuron projection development` IBAs
that mouse Acap3 supports are attached to a *different* node (PTN002754173) and correctly did **not**
reach ACAP1; the tree is discriminating properly there.

**But the paralog problem is real, and it runs the other way.** ACAP2 (Q15057) carries three IDAs from
PMID:11062263 — GO:0005096 GTPase activator activity, GO:0030029 actin filament-based process,
GO:0001726 ruffle. ACAP1 carries none, from the same paper, in which ACAP1 is the first-named protein,
was assayed in the same figures, and was the more potent of the two
[PMID:11062263 "9, ACAP1 was most effective at inhibiting protrusions."]. The consequence is an
inversion: ACAP1's ARF6-GAP activity now reaches ACAP1 only as an IBA whose WITH/FROM cites ACAP2 —
i.e. the gene is annotated by phylogenetic inference from its paralog for an activity that was measured
on the gene itself in the cited source. That is the finding for this gene.

For completeness, ACAP2's `endocytic recycling` (GO:0032456 ISS from rat Acap2 Q5FVC7) is a proper
ortholog transfer; ACAP1 has no endocytic recycling annotation at all, despite PMID:17664335 being
titled "An ACAP1-containing clathrin coat complex for endocytic recycling."

## 4. The one genuine tree oddity: Drosophila blow

`GO:0030036 actin cytoskeleton organization` IBA cites FB:FBgn0004133 = *blown fuse* (blow). PANTHER
places blow in PTHR23180 subfamily SF399, but blow has **only a PH domain** — UniProt annotates no BAR,
no Arf-GAP and no ANK repeats (checked A1Z714, P91678, E1JGZ4, Q8MSU1). Its actin annotation is a
myoblast-fusion IMP, a *Drosophila*-specific developmental phenotype.

This does **not** invalidate the annotation, because the other two sources are full-architecture ACAPs:
Dicty DDB_G0279649 (Q54WI0, BAR+PH+Arf-GAP) has actin cytoskeleton organization by both IMP and IGI
plus `regulation of filopodium assembly` IMP, `filamentous actin` IDA and `cell cortex` IMP, and
DDB_G0276395 (Q551Q8, PH+Arf-GAP) has it by IGI. And ACAP1 itself has human evidence for actin effects
(protrusions, focal adhesions). It is worth recording all the same: a domain-truncated family member
sitting inside the same PANTHER family is exactly the kind of node that produces a bad transfer when it
happens to be the *only* source, and here it is one of three.

## 5. The protein-binding rows are all screen noise

Eleven `GO:0005515 protein binding` IPI rows across four references. Resolved partners:

- PMID:17474147 — SH3 peptide-array screen (PATS): **GRB2**. ACAP1 has a Pro-rich stretch at 538–549
  (`PVPPKPSIRPRP…`), so an SH3 hit is chemically plausible, but this is a 1536-peptide array read out
  in bulk and this pair was not among the validated ones.
- PMID:25814554 — phospho-tyrosine Y2H network: **GRB2** again. GRB2 is therefore the one partner with
  two orthogonal screens behind it. No tyrosine phosphorylation of ACAP1 is on record in UniProt
  (only pSer-554 and nitro-Tyr-485), so what the pY-dependent hit means is unclear.
- PMID:32296183 — HuRI binary interactome: **NEBL** (nebulette, cardiac Z-disc), **FCHSD2**,
  **UQCRB** (respiratory complex III subunit 7).
- PMID:32814053 — neurodegeneration interactome: **PRKCA**, **UQCRC2** (complex III core protein 2),
  **YWHAG**, **SETDB1**, **LMO3**, **KAT5**.

Two mitochondrial inner-membrane respiratory-chain subunits and three nuclear chromatin/LIM proteins
are compartment-implausible for a cytosolic, ARF6-recruited peripheral protein on the recycling
endosome. FCHSD2 is the one hit with a mechanistically sensible shape (an F-BAR protein in
clathrin-mediated endocytosis), and is worth a directed test.

Set against that, **not one** of ACAP1's validated partners appears anywhere in the GO record:
ARF6, ITGB1, CLTC, GULP1 and SLC2A4 are all in UniProt SUBUNIT with ECO:0000269 and all have dedicated
papers, several with structures. UniProt's own INTERACTION block has the same problem — its ten
entries are the same screen hits, and none of the validated partners appears there either. Each is
marked `NbExp=3`; that count should not be read as three independent studies, since the underlying
references are the same high-throughput screens (HuRI alone used three Y2H assay versions), but I
have not traced the individual IntAct experiment records to confirm what the three are.

## 6. Ontology gap

`GO:0008060 ARF GTPase activator activity` no longer exists as a term: QuickGO reports it as a
secondary id of `GO:0005096 GTPase activator activity`, together with the other substrate-specific GAP
terms (GO:0005097 Rab, GO:0005098 Ras, GO:0005100 Rho, GO:0046582). GO's current design captures
substrate specificity through an annotation extension rather than a term, so the single most
strongly established fact about this protein — that it is an **ARF6** GAP, in vitro, with a measured
preference over ARF1 and ARF5 — cannot be stated in the term itself. Any future experimental
annotation of GO:0005096 on ACAP1 should carry `has_input UniProtKB:P62330` (ARF6). No new term is
proposed: the merge was a deliberate ontology decision, not an omission.

## 7. Annotations proposed

Seven `action: NEW` rows are added, all for terms absent from GOA entirely:

| Term | Qualifier | Evidence | Reference |
|---|---|---|---|
| GO:0032456 endocytic recycling | involved_in | IMP | PMID:17664335 |
| GO:0140312 cargo adaptor activity | enables | IDA | PMID:22645133 |
| GO:0030118 clathrin coat | part_of | IDA | PMID:17664335 |
| GO:0180020 membrane bending activity | enables | IDA | PMID:25284369 |
| GO:0042803 protein homodimerization activity | enables | IDA | PMID:25284369 |
| GO:0005546 PIP2 binding | enables | IDA | PMID:17010122 |
| GO:0072659 protein localization to plasma membrane | involved_in | IMP | PMID:17664335 |

A seventh was attempted and withdrawn: an IDA for `GO:0005096 GTPase activator activity` from
PMID:11062263, which is the single most warranted annotation on this gene. The repo validator
correctly rejects `action: NEW` for a term already present in GOA — GO:0005096 is there twice, by IBA
and IEA — so the recommendation is recorded in the review of the IBA row instead. It cannot be
expressed as a NEW row under the current schema even though the *evidence code* is what needs
changing, which is a small representational gap worth noting: this file can say "this term needs a
better evidence code" only in prose.

`GO:0180020 membrane bending activity` was created 2023-06-18, after all of ACAP1's primary
literature, which is a plausible reason the activity was never annotated.

## 8. Terms checked

Confirmed current and correctly branched via QuickGO `/ontology/go/terms/<id>/complete`:
GO:0005096, GO:0010008, GO:0055038, GO:0005886, GO:0005737, GO:0016020, GO:0030036, GO:0032456,
GO:0140312 (cargo adaptor activity), GO:0180020 (membrane bending activity, added 2023-06-18),
GO:0030118 (clathrin coat), GO:0005546, GO:0005547, GO:0072659.
`GO:0031532 actin cytoskeleton reorganization` is **obsolete** and was not used.

## 9. Follow-up round: PMID:25284369 full text, and the BAR-domain question

Three things were fixed or settled after the first review round merged.

**PMID:25284369 is not abstract-only.** The first round marked it `full_text_unavailable: true` and drew
its quotes from the abstract. `publications/PMID_25284369.md` in fact carries
`full_text_available: true`, `pmcid: PMC4198613`, `full_text_extraction_method: xml`. The flag is
removed and nine full-text findings are added. This matters beyond bookkeeping: the abstract states
the *conclusion* about domain division of labour, but only the Results give the **assay** that makes
the annotation an IDA — liposome binding plus negative-stain EM tubulation of purified BAR-PH — and
the negative BAR-domain result in two independent readouts (liposome sedimentation and the cryoEM
reconstruction). An IDA supported only by a conclusion sentence is weaker than one supported by the
assay, and here the assay was sitting in the cache unread.

**GO:0180020 landscape (QuickGO, taxon 9606, `goUsage=descendants`).** Four annotations, three gene
products, all IDA:

| Gene product | Term | Evidence | Reference |
|---|---|---|---|
| UniProtKB:O43633 CHMP2A | GO:0180020 | IDA | PMID:36604498 |
| UniProtKB:Q9Y3E7 CHMP3 | GO:0180020 | IDA | PMID:36604498 |
| UniProtKB:O60313 OPA1 | GO:0180020 | IDA | PMID:32228866 |
| UniProtKB:O60313 OPA1 | GO:0180020 | IDA | PMID:37612504 |

CHMP2A and CHMP3 are ESCRT-III subunits; OPA1 is a dynamin-family GTPase. **No BAR-domain protein
carries the term**, so ACAP1 would be the first — which is precisely why the PH-domain attribution has
to be spelled out on the row. A reader who sees a BAR protein on a membrane-bending term will assume
the BAR domain did it, and for ACAP1 that assumption is false.

**Second annotation considered and taken: `GO:0042803 protein homodimerization activity`.** The
BAR–BAR interaction is the only demonstrated function of ACAP1's BAR domain, and UniProt states it as
a domain property with experimental evidence for this PMID
[file:human/ACAP1/ACAP1-uniprot.txt "CC   -!- DOMAIN: The BAR domain mediates homodimerization, it can neither bind"].
The reason it survives the "co-complex membership is not stoichiometry" objection — the objection that
sank a heterodimerization claim on ACAP3 — is that three orthogonal readouts here each resolve the
oligomeric state rather than merely detecting association:
[PMID:25284369 "Dimerization of ACAP1BAR-PH was confirmed from size exclusion chromatography and light
scattering"],
[PMID:25284369 "The dimer interface has a large area (4100 Å2), and contains mainly hydrophobic residues
that likely mediate dimerization."],
[PMID:25284369 "The in vitro disassociation constant of the dimerization was calculated to be below
5 µM, according to the quantitative gel-filtration experiment"].
Crystallography, static light scattering and a measured Kd say *dimer*; an affinity capture would only
have said *interacts*.

Two limits are deliberately respected. (i) **Dimer, not lattice.** The paper's own wording for the
BAR–BAR function is "clustering at the membrane", and it describes tetramers and helical packing — but
those come from fitting the crystal structure into cryoEM maps of ~14 Å (Class I) and ~17 Å (Class II),
and "clustering" of an unspecified number of subunits is not a dimer. Reaching for an oligomerisation
or complex-assembly term would overstate the resolution, so the defensible parent-level dimer claim is
annotated and the lattice stays in prose. (ii) **Fragment, not full length.** All of this was measured
on BAR-PH (1–377 in the cryoEM work, 1–364 modelled), so it is a domain-attributed statement about
ACAP1, not a demonstration on the intact protein. Recorded as non-core: homodimerisation is the
structural precondition for the curved scaffold, not an output, and it is already described inside the
membrane-bending core function.
