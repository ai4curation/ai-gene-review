# Cellular component: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- A cellular component (CC) annotation says where a gene product is. `located_in` is the
  default; `is_active_in` is a stronger claim that needs evidence the molecular function
  happens there; `part_of` is only for protein-containing complexes. Do not use
  `colocalizes_with`.
- Annotate residence, not transit. A secreted or plasma-membrane protein passing through the
  ER and Golgi does not get ER or Golgi rows unless the protein is retained or acts there.
- A root organelle term (mitochondrion, ER, Golgi, peroxisome, lysosome) is informative and is
  never `TOO_GENERAL`. When two independent lines of evidence agree on the sub-compartment,
  add the sub-compartment beside the root; do not replace the root.
- Membrane topology is no longer encoded by "integral" terms. Use the membrane term, and the
  side-of-membrane terms only when the leaflet is known. Correct a generic plasma-membrane row
  when it misleads about which side the protein is on.
- High-throughput localization (Human Protein Atlas, organelle proteomics, GFP screens) and
  overexpression data support `located_in` at the resolution of the assay, no more. Being
  in a condensate is a location; building one is a function.

## Scope

This document covers gene-product-to-CC annotations in standard GO annotation (GAF/GPAD) and
their review: the four CC relations, organelle and sub-compartment terms, transit versus
residence, membrane topology, extracellular and cell-surface terms, condensates, nucleus and
cytoplasm defaults, localization evidence from overexpression and high-throughput assays, and
locations in another organism. Membership of protein-containing complexes is covered in
[protein-complexes.md](protein-complexes.md). The `occurs_in` extension and GO-CAM
compartments are covered in [annotation-extensions.md](annotation-extensions.md) and
[gocam-modeling.md](gocam-modeling.md); evidence codes in general in
[evidence-codes.md](evidence-codes.md).

## Principles

1. **A CC annotation is a claim about a place, and the relation states how strong the claim
   is.** The 2017 Cambridge GOC session asked what a CC annotation means and listed four
   cases: known active there, plausibly active there, known not active there (sequestration,
   transit), and unknown
   ([Drive: GOC 2017-10 Cellular_Component_Annotations](https://drive.google.com/open?id=19QGQd6Ps0xQssV6LBPgPwVHNhuDmXFPgFDGjPRehUkM)).
   GAF 2.2 answered with two relations: `located_in` (detected there) and `is_active_in` (enables
   its function there). We hold curators to that split.
2. **Annotate to the precision of the evidence, and review to the precision of the biology.**
   A row records what its source could resolve. A review asks whether the gene, as a whole,
   is described as precisely as the combined evidence allows, and adds rows where it is not.
3. **Location is not function.** A protein seen in a stress granule, an exosome or the nucleus
   has a location. Whether it does anything there is a separate question for MF and BP.
4. **Topology is a fact about the protein; GO CC terms describe places.** GO dropped "integral
   component" terms because they described proteins rather than locations
   ([wiki: Membrane proteins](https://wiki.geneontology.org/index.php/Membrane_proteins)).
   The side-of-membrane terms survive because a leaflet is a place.

## Rules

<a id="cc-1"></a>

### CC-1. Use `located_in` by default, `is_active_in` only when the activity is shown at that location, and `part_of` only for complex terms.

`located_in` links a gene product to a cellular anatomical entity where it has been detected.
`is_active_in` says the gene product enables its molecular function there; it follows from
`enables` some MF that `occurs_in` the location
([wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)). `part_of` links a
gene product to a protein-containing complex (`GO:0032991` or a descendant) and is not used for
cellular anatomical entities
([wiki: Part of relation](https://wiki.geneontology.org/index.php/Part_of_relation);
[Drive: Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)).

Choose `is_active_in` only when the paper (or the combined literature) shows the MF happening
in that compartment: an activity assay on the purified compartment, a substrate that exists
only there, or a function that requires that side of a membrane. A fractionation or
immunofluorescence result alone is `located_in`.

*Example.* Mouse Tent2 (a cytoplasmic poly(A) polymerase) was annotated to nucleus from a
fractionation figure. The 2021 review agreed the protein is found in both fractions but that
the nucleus is not where its activity has been shown, so the nuclear row should be
`located_in`, not `is_active_in`
([go-annotation#3595](https://github.com/geneontology/go-annotation/issues/3595)).

*Example.* *C. elegans* CED-3 `is_active_in` `GO:0005829` cytosol: the caspase cleaves its
substrates there ([wiki: Is active in](https://wiki.geneontology.org/index.php/Is_active_in)).

[GOC] Sources: [wiki: Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations),
[wiki: Located in](https://wiki.geneontology.org/index.php/Located_in),
[Annotation Conf. Call 2023-05-30](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-30)
(External2GO and HTP CC annotations use `located_in`).

<a id="cc-2"></a>

### CC-2. Do not make new `colocalizes_with` annotations; resolve existing ones to `located_in`, `is_active_in`, a binding term, or removal.

`colocalizes_with` was used for transient or peripheral association and for assays too coarse
to show membership. Curators read it in incompatible ways, and GO now marks it as deprecated
([wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with);
[Annotation Conf. Call 2023-11-28](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-11-28)).
When reviewing an existing row:

- **On a protein-containing complex term**, the 2018 Protein Complex Working Group ruled the
  combination invalid. Replace it with `GO:0044877` protein-containing complex binding (or a
  specific complex-binding child) if there is interaction evidence, or remove it
  ([go-annotation#1940](https://github.com/geneontology/go-annotation/issues/1940)).
- **On a cellular anatomical entity**, ask what the paper showed. If the protein acts there,
  even transiently, the relation is `is_active_in`
  ([wiki: Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with)). If it is
  only detected there, `located_in`. If the "colocalization" is a receptor trafficking through
  the endomembrane system with no activity there, remove it (the 2023 Padua breakout's
  "low-hanging fruit": Frizzled, insulin-family and vitellogenin receptors annotated to
  endomembrane system;
  [Drive: Reviewing colocalizes_with annotations](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o)).

In a review YAML, a `colocalizes_with` row is judged as a claim about the location; if the
location stands but the relation is wrong, say so in `reason` and record the corrected
relation (see [qualifiers-and-negation.md](qualifiers-and-negation.md)).

[GOC+] GOC deprecated the relation but left the per-row replacement to curators; the decision
list above is ours, assembled from the three sources.

<a id="cc-3"></a>

### CC-3. Treat an `is_active_in` row from IBA, a root-term ND, or a pipeline default as no stronger than `located_in` until the activity location is checked.

Several pipelines emit `is_active_in` by default. PAINT uses `is_active_in` for all CC IBA rows
and ignores the qualifiers of the experimental seed annotations when placing an IBD
([wiki: 5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)).
GAF 2.2 also set `is_active_in` as the relation for root CC annotations
([wiki: Manager Call 2020-11-04](https://wiki.geneontology.org/index.php/Manager_Call_2020-11-04)),
while the Annotation Relations page names `located_in` as the CC default. So an IBA
`is_active_in GO:0005739` may rest entirely on `located_in` seeds from proteomics.

A reviewer should not ACCEPT an `is_active_in` row on the strength of its relation. Judge the
location; then, if the activity is not shown there, say in `reason` that the row is accepted
as a location claim only.

*Example.* In the repo's mitochondrion survey, IBA `is_active_in GO:0005739` rows on ADO and
BRAF sit beside reviews arguing that ADO's N-degron oxidation is cytosolic and that BRAF's
mitochondrial pool has no assigned activity
([ORGANELLES](../../ORGANELLES.md), open question on `is_active_in`).

[NEW] GOC sets the PAINT default but has no guidance on reading it. We treat the relation on a
default-emitting pipeline row as uninformative.

<a id="cc-4"></a>

### CC-4. Annotate residence, not transit.

Every secreted, plasma-membrane and lysosomal protein passes through the ER and Golgi. That
passage is real, but the protein does not carry out its function there, and the GOC position
since 2017 is that secreted proteins are not annotated to the secretory pathway
([Manager Call 2017-04-19](https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19);
[Annotation Conf. Call 2017-05-09](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09)).
The 2023 discussion of UniProt keyword mappings restated this: Golgi localization of a protein
destined for the plasma membrane is not where it acts and is inappropriate for GO; Swiss-Prot
likewise omits ER and Golgi locations seen only when secretion is blocked with drugs
([go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)).

Operational tests (from the repo's ER and Golgi batches, [ORGANELLES](../../ORGANELLES.md) rule 7):

| Evidence for an ER or Golgi row on a protein that acts elsewhere | Action |
|---|---|
| Direct evidence on the gene: endogenous protein in its native cell, marker-confirmed, without secretion block | keep, `KEEP_AS_NON_CORE` |
| Wild-type tagged protein showing a minor marker-confirmed pool beside the main location | keep, `KEEP_AS_NON_CORE` |
| Retention only of an overexpressed or disease-mutant protein, or only under brefeldin A or similar | `MARK_AS_OVER_ANNOTATED` |
| A synthesis row (IBA, ISS, IEA) whose source shows only transit | `MARK_AS_OVER_ANNOTATED` |
| Regulated retention as part of the protein's control (for example ER retention by modification) | keep; may be core if the regulation is the function |

Topology does not force a sub-compartment on a transit pool: a TM protein passing through the
ER gets no `GO:0005789` endoplasmic reticulum membrane row.

*Example.* ATP1A1's ISS Golgi row rests on a rat paper that measured ER-to-Golgi transit with
reporters; the alpha subunit was never shown in a marker-defined Golgi compartment. The row is
`MARK_AS_OVER_ANNOTATED`, matching the ER call for the same source
([ORGANELLES](../../ORGANELLES.md), Golgi batch 1).

Three non-resident pools are distinct from biosynthetic transit and are real locations:
retrograde or ligand-driven pools reached from the plasma membrane (ADRB2 palmitoylation at the
Golgi), adaptor-dependent recycling stops, and internalized receptors that signal from
endosomes. Annotate these with `located_in` (or `is_active_in` when signalling from that
compartment is shown, as for endosomal GPCR signalling cited in the 2017 call), as non-core
unless the activity is core.

[GOC+] GOC stated the transit rule in minutes but never in a guideline page. The evidence tiers
are ours.

<a id="cc-5"></a>

### CC-5. Record sequestration and regulated relocation with `located_in`; reserve `is_active_in` for the compartment where the protein works.

A transcription factor held in the cytoplasm until signalled, a recombination protein excluded
from the nucleus in interphase, or an ER-anchored SREBP precursor are all in a real place by a
specific mechanism. PomBase argued that such locations should be annotated because they
reflect purpose
([go-annotation#1226](https://github.com/geneontology/go-annotation/issues/1226)); the
GOC location-of-action view argued they should not
([Annotation Conf. Call 2017-05-09](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09)).
GAF 2.2's two relations let both views coexist: annotate the sequestering compartment with
`located_in`, the working compartment with `is_active_in`.

*Example.* DAF-16: `located_in` cytoplasm (sequestered, inactive), `is_active_in` nucleus
(transcription factor activity), the categories used in the 2017 GOC deck
([Drive: GOC 2017-10 Cellular_Component_Annotations](https://drive.google.com/open?id=19QGQd6Ps0xQssV6LBPgPwVHNhuDmXFPgFDGjPRehUkM)).
If the sequestering protein has its own activity there (a sequestering protein in the cytosol),
that protein `is_active_in` the cytosol and its target is the `has_input`
([go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)).

Material released by cell lysis is not a location. Histones spilled from a lysed cell are not
`located_in` extracellular region; neutrophil extracellular traps, which are a physiological
structure, are a defensible exception
([go-annotation#1226](https://github.com/geneontology/go-annotation/issues/1226)).

[GOC+] Resolves the 2014 PomBase-versus-location-of-action disagreement by relation choice.

<a id="cc-6"></a>

### CC-6. A root organelle term is informative: never `TOO_GENERAL`, and never `MODIFY` it to a sub-compartment.

This rule covers `GO:0005739` mitochondrion, `GO:0005783` endoplasmic reticulum, `GO:0005794`
Golgi apparatus, `GO:0005777` peroxisome and `GO:0005764` lysosome. Every protein in a
membrane-bounded organelle sits in a membrane or a lumen, but "in the mitochondrion" is still a
real claim, and many assays (organelle proteomics, whole-organelle co-staining, GFP-fusion
screens) cannot resolve further. Direct evidence (IDA, EXP, HDA, HTP, IMP) from such an assay
is `ACCEPT`, or `KEEP_AS_NON_CORE` if the location is peripheral to the function. The
exception to the general "correct but general is `MODIFY`" rule
([reviewing-annotations.md](reviewing-annotations.md)) applies to these five terms only. A
generic term such as `GO:0016020` membrane is not a root organelle term and is still refined
(CC-10).

*Example.* In the repo's 2026-10 survey, 1,576 of 2,134 mitochondrion rows on genes that also
had a sub-compartment were `ACCEPT`, and no review had used `TOO_GENERAL` on a root organelle
row ([ORGANELLES](../../ORGANELLES.md)).

The nucleus, the series organelles (endosome, vacuole, autophagosome) and plastids are not yet
covered; for the nucleus see CC-16.

[NEW] Sources: [ORGANELLES](../../ORGANELLES.md) policy rules 1-2;
[CLAUDE.md](../../../CLAUDE.md) "Root organelle terms". GOC has no stated policy on
organelle-level granularity.

<a id="cc-7"></a>

### CC-7. Examine every root organelle row that comes from synthesis (IBA, ISS, ISO, IEA, IC, RCA); keep it only if the organelle claim survives the check.

A propagated or inferred row has no assay limit to excuse a coarse term. Either the source knew
the sub-compartment and the propagation lost it, or the source did not know the location.
Check the source:

- **IBA:** read the PAINT node's experimental descendants. Is the target inside the clade that
  shares the location, or does the node mix cytosolic and organellar paralogs? GO's own advice
  for mixed trees is not to propagate CC at all
  ([go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546), alanyl-tRNA
  synthetases); see [phylogenetic-propagation.md](phylogenetic-propagation.md).
- **IEA:** check the mapping (UniProt subcellular-location keyword, InterPro2GO, ARBA) and
  whether the gene has the feature the mapping assumes. Read the evidence tag on each location
  item of a UniProt SUBCELLULAR LOCATION line separately.
- **ISS/ISO and Ensembl projections:** trace to the donor paper; several rest on an unmarked
  staining pattern or "data not shown".

If the organelle claim holds, `ACCEPT` (or `KEEP_AS_NON_CORE`) and record the check in
`reason`. If not, `MARK_AS_OVER_ANNOTATED`, or `REMOVE` for a demonstrably wrong mapping or
over-propagation.

*Example.* CEPT1's IBA Golgi row comes from a PAINT node seeded only by the CHPT1 lineage;
brefeldin A moves CPT1 but not CEPT1, which sits in the ER and nuclear membranes. The row is
`MARK_AS_OVER_ANNOTATED` ([ORGANELLES](../../ORGANELLES.md), Golgi batch 1).

[NEW] Sources: [ORGANELLES](../../ORGANELLES.md) rule 3; [CLAUDE.md](../../../CLAUDE.md).

<a id="cc-8"></a>

### CC-8. Add the sub-compartment as a separate row when at least two independent lines agree; do not substitute it for the root.

Lines of evidence: a predicted TM segment or tail anchor; a cleavable matrix presequence, PTS1
or PTS2; an ER signal peptide with or without a retention motif; a sub-organelle assay
(protease protection, sub-fractionation with markers, immuno-EM); a function that only makes
sense on one side (a matrix TCA enzyme, an inner-membrane carrier). With two agreeing lines,
add the matrix, membrane or lumen term as a `NEW` row (usually IC) beside the root rows, and
list the lines in `reason`. With one line, or lines that disagree, stay at the root and say why.

Keeping the root rows follows GO's own practice: DARS2 and MMUT carry `GO:0005759`
mitochondrial matrix and keep their `mitochondrion` rows. It also keeps rows on one term
consistent, so no exception to the action-consistency check is needed. The lasting fix for an
IEA root row is upstream: UniProt keyword SL-0170 (Mitochondrion matrix) maps to the matrix
term where SL-0173 (Mitochondrion) maps to the root.

For ER rows, a `NEW` `GO:0005789` endoplasmic reticulum membrane row needs a TM or tail anchor
plus an ER-specific assay on the endogenous protein; a `NEW` `GO:0005788` endoplasmic reticulum
lumen row needs a soluble signal-peptide protein shown to be retained (a KDEL-type motif, or
protease protection). `GO:0070971` endoplasmic reticulum exit site needs a marker of
transitional ER. Microsomes are not ER without an ER marker, and a "mitochondrial" fraction not
checked for an ER marker cannot separate mitochondria from mitochondria-associated membranes.

When a new sub-compartment row is added, the gene's generic `GO:0016020` membrane rows become
`MODIFY` to it, all rows on that term alike.

*Example.* The 2026-10 pilot added `NEW` IC `GO:0005759` matrix rows to AARS2, CLYBL and
MMADHC, each from a predicted presequence with no TM segment plus matrix-only substrates or
partners. None rested on a direct sub-mitochondrial assay. PYCR2 stayed at the root: its
N-terminus has been sequenced and carries no presequence, it has a cytoplasmic pool, and the
only fractionation was two-way, so there was one functional hint and nothing else
([ORGANELLES](../../ORGANELLES.md), pilot note).

[NEW] Sources: [ORGANELLES](../../ORGANELLES.md) rules 4-5 and 7.

<a id="cc-9"></a>

### CC-9. A soluble protein stably tethered to an organelle by a named integral partner gets the cytoplasmic-side term; brief or regulated recruitment stays at the root.

GO's intrinsic and extrinsic component terms do not say which side a protein is on. The
"cytoplasmic side of X membrane" terms do, and are defined to include proteins "peripherally
associated" with that leaflet. `GO:0098554` cytoplasmic side of endoplasmic reticulum membrane
is `part_of` `GO:0005789`, so it refines the membrane term rather than avoiding it. The route
needs all four of: (a) direct evidence the endogenous protein is at the organelle; (b) a named
integral membrane protein of the organelle that binds it; (c) dependence on that partner
(knockout or a binding mutant releases or destabilises the protein); (d) cytosolic synthesis
with no signal peptide or targeting sequence, checked in the literature as well as UniProt
features. A protein failing (d), such as a matrix protein held by an inner-membrane partner,
gets the side term for its own compartment (`GO:0099617` matrix side of mitochondrial inner
membrane).

Other side terms exist for the mitochondrial outer membrane (`GO:0032473`), lysosome
(`GO:0098574`) and trans-Golgi network (`GO:0160281`), but none for the Golgi stack or the
peroxisome; a case there becomes a `proposed_new_terms` entry, not a forced narrower term.
Signalling, stress or autophagy recruitment, Rab-dependent docking, and cycling complexes such
as SRP are not tethering.

*Example.* UFSP2 has no TM or signal peptide; endogenous UFSP2 is lost in ODR4-knockout cells;
ODR4 is a transmembrane ER protein. UFSP2 gains a `NEW` IC `GO:0098554` row beside its ACCEPTed
ER root rows. UFL1 and CDK5RAP3, held by DDRGK1, keep their direct-evidence `GO:0005789` rows
([ORGANELLES](../../ORGANELLES.md), 2026-11-11 note).

GO's answer to the question of when to use `GO:0042406` extrinsic component of endoplasmic
reticulum membrane versus `GO:0098554` is that the two hierarchies classify different things
(loosely bound versus leaflet) and a protein may carry both
([go-annotation#5694](https://github.com/geneontology/go-annotation/issues/5694)). We prefer the
side term because it says more and because the extrinsic terms were slated for obsoletion
(CC-10).

[NEW] Sources: [ORGANELLES](../../ORGANELLES.md) rule 7, tethering bullet.

<a id="cc-10"></a>

### CC-10. Do not encode membrane topology with "integral" or "anchored" terms; use the membrane term, refine generic `membrane`, and use side terms only when the leaflet is known.

In 2022 GO decided that capturing membrane protein topology is no longer GO's job and obsoleted
the integral, intrinsic and anchored component terms
([Annotation Conf. Call 2022-05-24](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-05-24);
[Annotation Conf. Call 2022-07-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-07-19)).
In the release we checked, `GO:0016021` integral component of membrane, `GO:0005887` integral
component of plasma membrane, `GO:0031225` anchored component of membrane and `GO:0031226`
intrinsic component of plasma membrane are obsolete. Topology is now queried in UniProt's
subcellular-location topology vocabulary. Consequences:

1. A TM protein spanning several compartments gets one annotation, to the membrane it sits in,
   not separate rows for the cytosol and periplasm its domains reach. The 2020 answer for E. coli
   histidine kinases recommended a single membrane annotation
   ([go-annotation#2929](https://github.com/geneontology/go-annotation/issues/2929)); with the
   integral terms gone, that is now `GO:0005886` plasma membrane.
2. The 2013-era rule that experimental membrane localization plus predicted TM segments support
   an integral term
   ([wiki: Transmembrane Proteins](https://wiki.geneontology.org/index.php/Transmembrane_Proteins))
   now supports the specific membrane term (plasma membrane, ER membrane). Its caution stands:
   a single N-terminal hydrophobic segment may be a signal peptide, in which case the protein
   may be secreted.
3. `GO:0016020` membrane on a gene whose membrane is known is `MODIFY` to the specific
   membrane. Unlike root organelle terms, "membrane" alone says little.
4. Side terms (`GO:0098552` side of membrane and its children `GO:0009897` external side of
   plasma membrane, `GO:0009898` cytoplasmic side of plasma membrane, `GO:0098554`) are places
   and remain valid. Monotopic proteins may go to `GO:0098552` or a child
   ([wiki: Membrane proteins](https://wiki.geneontology.org/index.php/Membrane_proteins)).
   `GO:0009897` was kept deliberately
   ([Annotation Conf. Call 2022-07-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-07-19)).
5. The extrinsic component terms were announced for obsoletion in 2022 because curators could
   not tell membrane from membrane-associated proteins
   ([Annotation Conf. Call 2022-08-23](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-08-23)),
   but `GO:0019898` extrinsic component of membrane and its children are still live in the
   release we checked. Do not make new extrinsic-component annotations; prefer the side term
   (CC-9).

[GOC+] Restates the 2022 decisions, which never reached a guideline page; points 3 and 5 are
ours.

<a id="cc-11"></a>

### CC-11. When a generic plasma-membrane row misleads about which side the protein is on, or whether it is in the plasma membrane at all, `MODIFY` it; otherwise accept it at its own resolution and add the specific term as a `NEW` row.

`GO:0005886` plasma membrane reads to most users as "surface protein". For inner-leaflet
proteins that reading is wrong. The deciding question per row is whether the specific term
corrects the generic one or adds resolution to it:

- **`MODIFY`** when the row's own evidence fixes the side or subdomain and the generic term
  misleads: KRAS and other inner-leaflet proteins `GO:0005886` → `GO:0009898`; STIM1, which stays
  in the ER membrane and gates ORAI from the ER side, `GO:0005886` → `GO:0140268`
  endoplasmic reticulum-plasma membrane contact site; MSLN `GO:0016020` → `GO:0009897`.
- **`ACCEPT` at own resolution plus a `NEW` row** when several rows on the term come from
  sources that stop at plasma membrane (IBA, IEA, a localization quote that does not resolve
  the leaflet) while separate, cited evidence fixes the subdomain. The generic rows' `reason`
  must say they are accepted at the resolution their evidence supports and must not argue that
  the term is too general; the subdomain evidence is quoted on the `NEW` row. GUCY2C and MUC16
  keep their `GO:0005886` rows and gain `NEW` `GO:0016324` apical plasma membrane rows; CA9 gains
  `NEW` `GO:0009897` for its ectoenzyme topology
  ([SURFACEOME](../../SURFACEOME.md), settled convention, signed off 2026-11).

`GO:0140268` is asserted in GO as overlapping both the ER membrane and the plasma membrane; it
denotes the junction, not insertion into the plasma membrane. Desmosome and gap junction terms
are not under plasma membrane at all, so a query on plasma-membrane descendants misses
junctional proteins.

[NEW] Sources: [SURFACEOME](../../SURFACEOME.md) "Generic GO:0005886 row" and settled
convention; [CLAUDE.md](../../../CLAUDE.md) "Correct but general terms are MODIFY".

<a id="cc-12"></a>

### CC-12. Annotate secreted proteins to `GO:0005576` extracellular region (or a specific extracellular structure), never to `GO:0005615`; use cell surface for proteins held on the outer face.

`GO:0005615` extracellular space is obsolete; OLS records it as a duplicate of `GO:0005576`
([BIOREASON_COMPARISON](../../BIOREASON_COMPARISON.md) records the obsoletion in the
2026-03-25 release). Existing rows on it are not rewritten (GOA ids are trusted in review), but
any reviewer-authored location uses `GO:0005576` or a more specific term such as `GO:0031012`
extracellular matrix.

- **Secreted proteins** act extracellularly; `GO:0005576` is their location of action and is
  normally core. Do not add ER, Golgi or secretory-vesicle rows for them (CC-4).
- **Surface-bound extrinsic proteins.** `GO:0009986` cell surface is defined as the external
  part of the cell wall and/or plasma membrane, and includes ligands bound to receptors and
  proteins held on glycans (thrombin on its receptors, transferrin on TFRC, VEGFA on heparan
  sulfate). It is not an `is_a`/`part_of` descendant of plasma membrane. `GO:0009897` external
  side of plasma membrane is `part_of` both plasma membrane and cell surface. A GPI-anchored
  protein now goes to `GO:0005886` (and `GO:0009897` when the outer leaflet is the point),
  since the anchored-component terms are obsolete
  ([SURFACEOME](../../SURFACEOME.md) §5).
- **Cell-type-restricted surface.** Prefer a cell-type CC term when GO has one
  (`GO:0097524` sperm plasma membrane for CRISP1); otherwise a `part_of` CL or UBERON extension
  on the generic row (ITPR3 `GO:0005886` part_of platelet)
  ([SURFACEOME](../../SURFACEOME.md), annotation extensions). See
  [annotation-extensions.md](annotation-extensions.md).
- **Extracellular vesicles.** `GO:0070062` extracellular exosome is `part_of` extracellular
  region. An exosome row from vesicle or body-fluid proteomics (HDA) is a high-throughput
  location (CC-14). Such rows are real but almost never informative: of 712 reviewed
  vesicle-type rows in the repo, 6% were accepted as core, 59% kept as non-core and 26%
  rejected ([OMICS_EVIDENCE](../../OMICS_EVIDENCE.md)). Default to `KEEP_AS_NON_CORE`; accept as
  core only for a protein with a specific role in vesicle biogenesis (the repo accepts ALIX on
that basis, while ESCRT-III CHMP3 and common cargo such as GAPDH stay non-core).

[GOC+] Sources: [Manager Call 2017-04-19](https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19)
(raised, unresolved, whether bound hormones are annotated to the receiving cell's surface; we
say yes, via cell surface); [SURFACEOME](../../SURFACEOME.md).

<a id="cc-13"></a>

### CC-13. Localization from overexpression, tagging or mutants supports a CC row only when a marker resolves the compartment and the protein is wild type.

Light microscopy of an overexpressed protein often shows a perinuclear haze that authors call
"Golgi-like". That is not a location.

| Evidence | Counts as direct evidence for the compartment? |
|---|---|
| Endogenous protein, specific antibody, co-stain with a compartment marker | yes |
| Wild-type tagged protein at moderate expression, marker co-stain | yes; a minor marker-confirmed pool beside the main location counts |
| Overexpressed protein with a "pattern resembling" the compartment and no marker | no |
| Disease mutant or misfolded protein retained in the ER | no, for the wild-type gene product |
| Fraction (microsomes, membrane fraction, synaptosome) without a marker | no; map to a real compartment only when markers support it ([wiki: Annotations to Cell Fraction-type terms](https://wiki.geneontology.org/index.php/Annotations_to_Cell_Fraction-type_terms), archived) |
| Location only under a viral protein, drug or other perturbation | no, unless the perturbation is the biology being annotated |

Experiments in heterologous systems are IDA or IMP per
[evidence-codes.md](evidence-codes.md); this rule is about whether the observation shows the
compartment at all.

Curator deference (do not overrule an experimental annotation whose full text you cannot read;
[reviewing-annotations.md](reviewing-annotations.md)) stops at a readable paper. If the paper
can be read and shows no marker, the row is `MARK_AS_OVER_ANNOTATED`.

*Example.* CABP2's IDA Golgi row: in the full text, overexpressed CaBP2 is only "resembling the
Golgi apparatus"; all marker work was on CaBP7 and CaBP8. The row moved from
`KEEP_AS_NON_CORE` to `MARK_AS_OVER_ANNOTATED`. By contrast, ABCA1's minor intracellular pool
co-stains with giantin in stably transduced cells and stays non-core. BST2's trans-Golgi network
pool was seen with the TGN46 marker only in cells carrying a Vpu-encoding provirus, which traps
tetherin there, so no TGN row was added ([ORGANELLES](../../ORGANELLES.md), Golgi batch 1).

[NEW] Sources: [ORGANELLES](../../ORGANELLES.md) Golgi lessons and rule 7.

<a id="cc-14"></a>

### CC-14. High-throughput localization supports `located_in` at the assay's resolution; weigh the source's grade, and treat "additional" locations as non-core by default.

Organelle proteomics, GFP-fusion screens and antibody atlases detect many proteins at low levels
and cannot tell residence from contamination or transit. Their rows carry HDA (or IDA for the
Human Protein Atlas) and `located_in`
([Annotation Conf. Call 2023-05-30](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-30)).

The Human Protein Atlas (HPA) exports immunofluorescence calls to GOA as IDA with
`GO_REF:0000052`. Read them with four facts in mind
([HPA evidence re-evaluation](../../HUMAN_PROTEIN_ATLAS/hpa-evidence-reevaluation.md)):

1. **Grades.** *Enhanced* means an orthogonal antibody validation. *Supported* means the call
   agrees with existing literature or UniProt; it is not independent evidence for a location
   the literature already supports. *Approved* and *Uncertain* calls do not normally reach GOA;
   a GOA row whose location HPA has since downgraded is a stale export.
2. **Vocabulary.** HPA's classes are coarse; an inner-membrane translocase is called
   "Mitochondria". Accept the organelle row (CC-6) and add the sub-compartment from other
   evidence (CC-8).
3. **Main versus additional.** Additional locations were kept as non-core far more often than
   main locations in the repo's reviews (38% versus 20%); default an additional location to
   `KEEP_AS_NON_CORE` unless other evidence makes it core.
4. **Scope.** HPA supplies CC evidence only. A `GO_REF:0000052` citation on an MF or BP row
   (for example a reviewer's `NEW` peroxisome-biogenesis row) is a citation error.

Assays differ. In the repo's audit of high-throughput rows, one-by-one tagged-protein screens
(yeast GFP collections, the *S. pombe* ORFeome) and confidence-scored organelle proteomes were
accepted 63-89% of the time, while a membrane-fraction proteome mapped to `GO:0016020` membrane
was accepted 22% of the time: the fraction carries soluble contaminants and the term is
uninformative ([OMICS_EVIDENCE](../../OMICS_EVIDENCE.md)). Weigh a row by its assay, not by
its evidence code.

For core ciliary proteins, the HPA grade said little about whether the location is real:
CEP83, CEP164, CEP290 and IFT52 carry only Approved or Uncertain cilium calls. Module
membership and literature were the better guide
([HUMAN_PROTEIN_ATLAS](../../HUMAN_PROTEIN_ATLAS.md)).

[NEW] GOC's 2017 HTP working group framed the problem (whole-organelle proteomics as a
high-false-positive dataset;
[Drive: HTP working group discussion points](https://drive.google.com/open?id=1I2PiQ7ApuE5K5-FFUQ9rGH71D6tpS_ui),
legacy) but issued no CC-specific rule. The `GO_REF:0000052` description still says only
literature-supported calls are exported, which the current data contradict.

<a id="cc-15"></a>

### CC-15. Annotate presence in a condensate as a location; claim condensate formation only with condensate-grade evidence, and never infer a localization process from co-localization.

Stress granules (`GO:0010494` cytoplasmic stress granule), P-bodies, the nucleolus
(`GO:0005730`) and nuclear speckles are heavily annotated as locations, but GO and this
repository rarely record which proteins build them; in the repo's audit 238 gene folders carry
a condensate CC term and 9 carry `GO:0140693` molecular condensate scaffold activity
([CONDENSATES](../../CONDENSATES.md)).

1. **Client, scaffold or regulator: say which.** A protein that partitions into a stress
   granule gets `located_in GO:0010494`. A protein shown to nucleate it may get `GO:0140693`
   and `GO:0034063` cytoplasmic stress granule assembly.
2. **Condensate CC alone is rarely core.** Reviewers had already downgraded 37% of 399
   condensate-space rows without a shared rule; make non-core the default for clients.
3. **Condensate-grade evidence** for a scaffold or assembly claim: FRAP recovery,
   1,6-hexanediol sensitivity with controls, endogenous-tag imaging, loss-of-function that
   abolishes the structure while other components remain. In vitro droplets at
   non-physiological concentrations and puncta in overexpressing cells are weaker; flag them
   in `reason`.
4. **No localization process from co-localization.** In 2026 GO proposed obsoleting
   `protein localization to cytoplasmic stress granule`; seven of its eight experimental
   annotations were component or co-localization evidence and were recommended to become
   `located_in GO:0010494`
   ([go-annotation#6484](https://github.com/geneontology/go-annotation/issues/6484)).

`GO:0043228` membraneless organelle is not a condensate class: the ribosome and the
cytoskeleton are under it, and `GO:0000407` phagophore assembly site, a liquid-like condensate,
is not. Do not use membership of `GO:0043228` to decide that a location is a condensate.

[GOC+] Point 4 restates GO's 2026 review; points 1-3 are the repo's draft principles
([CONDENSATES](../../CONDENSATES.md), not yet tested on a calibration batch).

<a id="cc-16"></a>

### CC-16. Prefer `GO:0005829` cytosol to `GO:0005737` cytoplasm, and refine `GO:0005634` nucleus to its interior structures when the evidence allows; keep the nucleus row when the refinement is chromatin.

`GO:0005737` cytoplasm includes the organelles; a soluble cytosolic enzyme annotated to
cytoplasm is under-described, and an organellar protein annotated to cytoplasm is true but
uninformative. When the evidence (fractionation with a cytosolic marker, or function) places
the protein in the cytosol, `MODIFY` cytoplasm to cytosol. When the paper only shows
"cytoplasmic" staining by light microscopy, cytoplasm is the honest term.

For the nucleus, what matters is the interior: `GO:0005654` nucleoplasm, `GO:0000785`
chromatin, `GO:0005730` nucleolus, speckles, the pore. ChIP supports `GO:0000785` chromatin (or
a child), not DNA binding unless the study is built to show direct binding
([wiki: Annotation consistency : ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments)).
Chromatin is `part_of` chromosome, and chromosome is not `part_of` nucleus because prokaryotes
have chromosomes, so a chromatin row does not imply the nucleus
([GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md)). Keep the nucleus row beside a chromatin
row for a eukaryotic protein, or use `GO:0000228` nuclear chromosome where it fits.

For nucleus and cytosol together, check the reference for each row; annotate the compartment
where the protein performs its function as `is_active_in` and the other as `located_in`
([wiki: 7 April 2015 PAINT Conference Call](https://wiki.geneontology.org/index.php/7_April_2015_PAINT_Conference_Call);
CC-5).

*Example.* The *E. coli* lipoyl synthase lipA review MODIFYs cytoplasm to cytosol
([RADICAL_SAM](../../RADICAL_SAM.md)). Compartment is not an MF distinction: cytosolic and
mitochondrial tRNA ligases take the same MF term
([go-annotation#6525](https://github.com/geneontology/go-annotation/issues/6525)); the
compartment belongs in CC.

[GOC+] The ChIP rule is GOC; the cytosol preference and the chromatin-plus-nucleus rule are
ours. A full nucleus policy (CC-6 currently excludes it) is an open question.

<a id="cc-17"></a>

### CC-17. Do not propagate a location across paralogs that live in different compartments.

When a family contains cytosolic and organellar members (aminoacyl-tRNA synthetases,
CHPT1/CEPT1, many dual-targeted enzymes), a CC IBD at a node above the split assigns one
paralog's compartment to the other. GO's view is that not propagating CC is then correct
([go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546)), and that
localization processes are poor PAINT targets
([go-annotation#5691](https://github.com/geneontology/go-annotation/issues/5691)). In review,
such a row is `MARK_AS_OVER_ANNOTATED` when the target's own data place it elsewhere, and the
fix is reported to PAINT (see [phylogenetic-propagation.md](phylogenetic-propagation.md)).

[GOC]

<a id="cc-18"></a>

### CC-18. A gene product acting in another organism is annotated to that organism's compartment; a host protein co-opted by a pathogen keeps its own.

Symbiont proteins that act inside the host take the host-cell terms (for example `GO:0030430`
host cell cytoplasm for a cobra cardiotoxin that enters mammalian cells), with the interacting
taxon recorded
([wiki: Multi-species processes](https://wiki.geneontology.org/index.php/Multi-species_processes)).
A host protein recruited to a viral replication compartment is annotated with ordinary CC terms
and should not receive viral-process terms
([go-annotation#1507](https://github.com/geneontology/go-annotation/issues/1507)). See
[multi-organism-and-ncrna.md](multi-organism-and-ncrna.md) for the process side.

[GOC]

<a id="cc-19"></a>

### CC-19. In `core_functions`, name the location where the core activity is shown to happen, not every well-supported location.

`core_functions.locations` answers "where does this function act". A well-supported location is
not automatically that place: MMADHC's matrix location is well supported and kept as a `NEW`
row, but no matrix-side partner or step has been shown, and a cytosolic branch-point model fits
the data as well, so the matrix was removed from its core function's locations
([ORGANELLES](../../ORGANELLES.md), MMADHC note). Add the root as well only when the
organelle-level claim is independently supported. Secretory transit, sequestration pools and
condensate client locations do not belong in `core_functions.locations`.

[NEW] Source: [ORGANELLES](../../ORGANELLES.md) rule 6.

## Decision aid

**Relation for a single CC observation**

| What the evidence shows | Relation | Typical action in review |
|---|---|---|
| Detected there (IF, fractionation, proteomics) | `located_in` | ACCEPT or KEEP_AS_NON_CORE |
| Activity measured there, or function requires that compartment | `is_active_in` | ACCEPT; candidate core location |
| Stable member of a protein-containing complex | `part_of` | see [protein-complexes.md](protein-complexes.md) |
| Binds a complex but is not a member | MF `GO:0044877` or child, not CC | MODIFY a `part_of` or `located_in` row |
| Transient, peripheral, low resolution | not `colocalizes_with`; pick one of the above | resolve per CC-2 |

**Root organelle row**

1. Is the organelle claim true for this gene? No: `MARK_AS_OVER_ANNOTATED` or `REMOVE`.
2. Direct assay that cannot resolve further? `ACCEPT` / `KEEP_AS_NON_CORE`.
3. Synthesis row? Check the source (CC-7), then `ACCEPT` / `KEEP_AS_NON_CORE` with the check in
   `reason`.
4. Does the gene lack a sub-compartment row, with two agreeing lines? Add a `NEW` row (CC-8).
5. Soluble, tethered by a named integral partner, cytosolic synthesis? Add the cytoplasmic-side
   term (CC-9).

**Organelle row on a protein that acts elsewhere**

| Pool | Example | Action |
|---|---|---|
| Biosynthetic transit only | ATP1A1 Golgi | MARK_AS_OVER_ANNOTATED |
| Overexpression or mutant retention only | CABP2 Golgi | MARK_AS_OVER_ANNOTATED |
| Endogenous, marker-confirmed minor pool | ABCA1 Golgi | KEEP_AS_NON_CORE |
| Regulated retrograde or recycling pool | ADRB2 Golgi | KEEP_AS_NON_CORE |
| Sequestration (inactive reservoir) | DAF-16 cytoplasm | `located_in`, KEEP_AS_NON_CORE |
| Signalling from that compartment shown | endosomal GPCR | `is_active_in`, may be core |

**Plasma membrane row**

| Situation | Action |
|---|---|
| Inner-leaflet protein (KRAS, LYN, BTK) | MODIFY to `GO:0009898` |
| ER protein acting at ER-PM junctions (STIM1) | MODIFY to `GO:0140268` |
| Generic `GO:0016020` and the membrane is known | MODIFY to the specific membrane |
| Several sources stop at PM; subdomain known from other evidence | ACCEPT at own resolution, add NEW subdomain row |
| Ligand bound to its receptor on the surface | `GO:0009986` cell surface |

## Common errors

| Pattern | Example | Fix |
|---|---|---|
| Secretory-pathway rows on secreted or surface proteins | ATP1A1 ISS Golgi; mainly perinuclear overexpression calls | CC-4: MARK_AS_OVER_ANNOTATED unless direct evidence of a resident pool |
| `TOO_GENERAL` or MODIFY on a root organelle row | early drafts of the repo's matrix pilot MODIFYed IBA mitochondrion rows | CC-6: keep the root; add the sub-compartment |
| Sub-compartment substituted for the root, splitting actions on one term | PR #5208 first version | CC-8: add, do not substitute |
| IBA `is_active_in` accepted as an activity claim | ADO, BRAF mitochondrion IBA | CC-3: judge as `located_in` |
| Paralog-seeded CC IBD | CEPT1 Golgi (CHPT1 seeds); AlaRS mitochondrion in fly | CC-17 |
| Plain plasma membrane on inner-leaflet proteins | KRAS, LYN, JAKs | CC-11: MODIFY to `GO:0009898` |
| ER protein annotated to plasma membrane | STIM1 SOCE IDA rows | CC-11: MODIFY to `GO:0140268` |
| Topology terms requested or proposed | "integral component of plasma membrane" in a `NEW` row | CC-10: obsolete; use the membrane term |
| Reviewer-authored `GO:0005615` | `NEW` extracellular space rows | CC-12: use `GO:0005576` |
| HPA citation on an MF or BP row | PEX19 `NEW` peroxisome membrane biogenesis citing `GO_REF:0000052` | CC-14: HPA supports CC only |
| Stress-granule co-localization turned into a localization process | GO:1903608 annotations | CC-15: `located_in GO:0010494` |
| Microsomal or crude mitochondrial fraction read as ER or mitochondrion | "mitochondrial" fraction without ER marker | CC-8: require markers |
| UniProt location item read with another item's evidence tag | AP3S2 Golgi read as by-similarity | CC-7: read the tag per item |
| Location under perturbation taken as native | BST2 TGN with Vpu | CC-13 |
| Chromatin row taken to imply nucleus in a model | SMAD1 activity in chromatin (GO-CAM `600ced8500002343`) | CC-16: keep nucleus, or use `GO:0000228` |
| Spilled contents annotated as extracellular | histones from lysed cells | CC-5 |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations) (CC default `located_in`) vs [Manager Call 2020-11-04](https://wiki.geneontology.org/index.php/Manager_Call_2020-11-04) and [PAINT call 2020-05-05](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call) (`is_active_in` default for root CC and IBA) | Two defaults for the same aspect | `located_in` is the default; read pipeline `is_active_in` as `located_in` until checked (CC-3) | PAINT ignores seed qualifiers, so the IBA relation carries no information about activity |
| [Ashburner et al. 2000](https://europepmc.org/article/MED/10802651) as quoted in the 2017 GOC deck; [2017-05-09 call](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09) | CC is where the gene product is active | CC records presence (`located_in`) and activity (`is_active_in`) separately; sequestration pools are annotated (CC-5) | Reconciles the location-of-action view with PomBase's practice ([#1226](https://github.com/geneontology/go-annotation/issues/1226)) |
| [Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with) (2018) and 2023 calls | Relation deprecated; existing rows "under review"; proposal to migrate automatically to `located_in` ([2023-05-16](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-16)) | Per-row decision: `is_active_in`, `located_in`, complex binding, or removal (CC-2) | Automatic migration to `located_in` keeps trafficking-only rows that should go |
| Old GO annotation conventions page (quoted in the 2017-05-09 call) | Transient or peripheral association to an organelle or complex may use `colocalizes_with` | Never on complexes; for organelles use `is_active_in` if it acts there | [#1940](https://github.com/geneontology/go-annotation/issues/1940), [#1500](https://github.com/geneontology/go-annotation/issues/1500) |
| [Transmembrane Proteins](https://wiki.geneontology.org/index.php/Transmembrane_Proteins); [#2929](https://github.com/geneontology/go-annotation/issues/2929) | Annotate TM proteins to a child of `GO:0016021` integral component of membrane | Annotate to the membrane itself; topology is out of scope (CC-10) | `GO:0016021` and related terms are obsolete ([2022-05-24](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-05-24)); the wiki page was never updated |
| [2022-08-23 call](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-08-23) | Extrinsic component terms to be obsoleted with "consider" parent | Do not use them for new annotations; prefer side-of-membrane terms (CC-9, CC-10) | The terms are still live in the current release; the obsoletion appears unfinished |
| [#5694](https://github.com/geneontology/go-annotation/issues/5694) (2025, open) | Cytoplasmic side and extrinsic component are separate hierarchies; a protein may carry both | Use the cytoplasmic-side term for stably tethered soluble proteins, only under the four-part test (CC-9) | Gives a decision rule where the thread gave a structure; avoids terms slated for obsoletion |
| No GOC policy | Organelle granularity unaddressed | Root organelle terms are informative; synthesis rows are red flags; add sub-compartments, do not substitute (CC-6 to CC-8) | Repo survey of ~3,000 mitochondrion rows ([ORGANELLES](../../ORGANELLES.md)) |
| [Manager Call 2017-04-19](https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19); [#4573](https://github.com/geneontology/go-annotation/issues/4573) | Secreted proteins not annotated to the secretory pathway; no documentation; UniProt keeps "real" retention | Transit is not residence, with evidence tiers for keeping a resident pool (CC-4) | The GOC rule was stated only in minutes and a ticket; curators need a test |
| [#4573](https://github.com/geneontology/go-annotation/issues/4573) (Swiss-Prot view) | Locations visible only under secretion block are not real; retention by modification is | Adopted, and extended to overexpression and mutant retention (CC-13) | Same reasoning applies to any non-native condition |
| `GO_REF:0000052` description (HPA) | Only literature-supported HPA calls are exported | Enhanced calls are exported too; Supported is not independent evidence (CC-14) | [HPA re-evaluation](../../HUMAN_PROTEIN_ATLAS/hpa-evidence-reevaluation.md): 223 Enhanced rows in reviewed genes |
| [SURFACEOME](../../SURFACEOME.md) §5 | ER-PM contact site "is under plasma membrane" in the reasoned hierarchy | It is asserted as overlapping both membranes; it denotes the junction (CC-11) | Checked in the GO release used here; queries should not treat it as plasma membrane insertion |
| Earlier GO practice (GO:0005615 widely used) | Extracellular space for secreted proteins | `GO:0005576` extracellular region (CC-12) | `GO:0005615` is obsolete as a duplicate of `GO:0005576` |
| [Annotations to Cell Fraction-type terms](https://wiki.geneontology.org/index.php/Annotations_to_Cell_Fraction-type_terms) (archived proposal) | Map fraction terms to specific CC terms | Map only when markers support the compartment (CC-13) | Microsomes and crude mitochondrial fractions mix compartments |
| [CONDENSATES](../../CONDENSATES.md) draft principles | Not yet adopted | Adopted provisionally as CC-15 | Repo audit; GO's own 2026 review of GO:1903608 reached the same conclusion for localization processes |

## Open questions

1. **Nucleus, series organelles and plastids.** CC-6 to CC-8 cover five organelles. Should
   `GO:0005634` nucleus rows be refined to nucleoplasm or chromatin as eagerly as the
   mitochondrion is refined to matrix? Is the maturation stage of endosomes and autophagosomes
   the analogue of the sub-compartment?
2. **Side-of-membrane terms for every organelle.** GO lacks cytoplasmic-side terms for the
   Golgi stack and the peroxisome (CC-9). Should GO add them, or retire side terms in favour of
   UniProt topology as it did for integral terms?
3. **Extrinsic component terms.** Announced for obsoletion in 2022, still live. GOC should
   finish or withdraw the obsoletion.
4. **`is_active_in` from PAINT.** Should PAINT emit `located_in` for CC IBDs whose seeds are
   all `located_in`? This would make CC-3 unnecessary.
5. **Main versus additional location.** HPA distinguishes them; GO cannot. An extension or flag
   would let users filter.
6. **Ligands in the receiving cell.** Is a membrane-bound ligand (ZP3, Delta) annotated to a
   location in the cell it signals to? Raised in 2017, never answered; we have no rule.
7. **Condensate class.** GO has no term for "biomolecular condensate" that excludes ribosome and
   cytoskeleton and includes the phagophore assembly site.
8. **Validation.** Should the repo warn on ACCEPTed root-only synthesis rows whose `reason`
   records no check (CC-7)?

## Sources

**GO wiki**
- [Annotation Relations](https://wiki.geneontology.org/index.php/Annotation_Relations)
- [Located in](https://wiki.geneontology.org/index.php/Located_in)
- [Is active in](https://wiki.geneontology.org/index.php/Is_active_in)
- [Part of relation](https://wiki.geneontology.org/index.php/Part_of_relation)
- [Colocalizes with](https://wiki.geneontology.org/index.php/Colocalizes_with)
- [Membrane proteins](https://wiki.geneontology.org/index.php/Membrane_proteins)
- [Transmembrane Proteins](https://wiki.geneontology.org/index.php/Transmembrane_Proteins) (out of date)
- [Annotation consistency : ChIP experiments](https://wiki.geneontology.org/index.php/Annotation_consistency_%3A_ChIP_experiments)
- [Multi-species processes](https://wiki.geneontology.org/index.php/Multi-species_processes)
- [Annotations to Cell Fraction-type terms](https://wiki.geneontology.org/index.php/Annotations_to_Cell_Fraction-type_terms) (archived)
- [5 May 2020 PAINT Conference Call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call); [7 April 2015 PAINT Conference Call](https://wiki.geneontology.org/index.php/7_April_2015_PAINT_Conference_Call)
- Annotation calls: [2017-05-09](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2017-05-09), [2022-05-24](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-05-24), [2022-07-19](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-07-19), [2022-08-23](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2022-08-23), [2023-05-16](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-16), [2023-05-30](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-05-30), [2023-11-28](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2023-11-28)
- Manager calls: [2017-04-19](https://wiki.geneontology.org/index.php/Manager_Call_2017-04-19), [2020-11-04](https://wiki.geneontology.org/index.php/Manager_Call_2020-11-04)

**GO Drive (GOC-internal)**
- [Drive: Annotation guidelines/Annotation relations - Guidelines for P2GO](https://drive.google.com/open?id=1DXdjAuNf7u8CKXYlgW5kyzPgq7vnp-Aai0S5Sh63guc)
- [Drive: GOC 2017-10 Cambridge/Cellular_Component_Annotations](https://drive.google.com/open?id=19QGQd6Ps0xQssV6LBPgPwVHNhuDmXFPgFDGjPRehUkM) (2017 proposal)
- [Drive: GOC 2023-04 Padua/Reviewing colocalizes_with annotations](https://drive.google.com/open?id=1T9ww92HdP291B7tbeqAD91xvTPxdwwjM9bHJwh6d56o)
- [Drive: HTP working group initial discussion points](https://drive.google.com/open?id=1I2PiQ7ApuE5K5-FFUQ9rGH71D6tpS_ui) (legacy, frozen)

**GitHub issues (geneontology/go-annotation)**
- [#1226](https://github.com/geneontology/go-annotation/issues/1226) extracellular annotations from lysed cells
- [#1500](https://github.com/geneontology/go-annotation/issues/1500), [#1940](https://github.com/geneontology/go-annotation/issues/1940) `colocalizes_with` on complexes
- [#1507](https://github.com/geneontology/go-annotation/issues/1507) host proteins and viral processes
- [#2929](https://github.com/geneontology/go-annotation/issues/2929) TM proteins spanning compartments
- [#3595](https://github.com/geneontology/go-annotation/issues/3595) `located_in` versus `is_active_in`
- [#4573](https://github.com/geneontology/go-annotation/issues/4573) Golgi transit and keyword mappings
- [#5546](https://github.com/geneontology/go-annotation/issues/5546), [#5691](https://github.com/geneontology/go-annotation/issues/5691) CC and localization in PAINT
- [#5694](https://github.com/geneontology/go-annotation/issues/5694) extrinsic component versus cytoplasmic side
- [#6484](https://github.com/geneontology/go-annotation/issues/6484) protein localization to stress granule
- [#6525](https://github.com/geneontology/go-annotation/issues/6525) compartment is not an MF distinction

**Papers**
- [PMID:10802651](https://europepmc.org/article/MED/10802651) Ashburner et al. 2000, Gene Ontology: tool for the unification of biology (CC definition, as quoted in the 2017 GOC deck)

**Repository pages**
- [ORGANELLES](../../ORGANELLES.md) (policy, ER and Golgi batches, tethering rule)
- [SURFACEOME](../../SURFACEOME.md) (plasma-membrane subdomain convention, cell surface)
- [HUMAN_PROTEIN_ATLAS](../../HUMAN_PROTEIN_ATLAS.md) and [HPA evidence re-evaluation](../../HUMAN_PROTEIN_ATLAS/hpa-evidence-reevaluation.md)
- [CONDENSATES](../../CONDENSATES.md); [STRESS_GRANULES](../../STRESS_GRANULES.md)
- [GOCAM_COMPARTMENTS](../../GOCAM_COMPARTMENTS.md)
- [PEROXISOME](../../PEROXISOME.md); [MITO_INTERACTOME](../../MITO_INTERACTOME.md); [ORGANELLE_LIFECYCLES](../../ORGANELLE_LIFECYCLES.md)
- [OMICS_EVIDENCE](../../OMICS_EVIDENCE.md); [BIOREASON_COMPARISON](../../BIOREASON_COMPARISON.md); [RADICAL_SAM](../../RADICAL_SAM.md)
- [CLAUDE.md](../../../CLAUDE.md) "Root organelle terms", "Correct but general terms are MODIFY"
