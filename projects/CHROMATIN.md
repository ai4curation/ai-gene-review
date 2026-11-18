---
title: "Chromatin: complexes, locations and the GO chromatin subtree"
maturity: SCOPING
last_reviewed: '2026-11-18'
tags: [BIOLOGY_DOMAIN]
species: [yeast]
genes: [HAT1, HAT2, HIF1, RTT109, VPS75, ESA1, EPL1, YNG2, EAF6, GCN5, ADA2, NGG1, SGF29, SAS3, NTO1, YNG1, TAF14, SAS2, SAS4, SAS5]
---

# Chromatin: complexes, locations and the GO chromatin subtree

**Bottom line:** GO's chromatin term (GO:0000785) is deliberately not part of
the nucleus, which is defensible, but the terms below it are inconsistent.
Some chromatin-acting complexes are asserted to be part of chromatin while
their close relatives are not, and one of those assertions is wrong. This
project curates chromatin-acting complexes as modules, starting with the
*S. cerevisiae* histone acetyltransferases. Each module records where the
complex actually acts, so module curation and the ontology question inform
each other. The first module is the type B histone acetyltransferase (HAT-B,
Hat1-Hat2-Hif1).

## Why chromatin is not part of the nucleus

Chromatin is `part_of` chromosome, and chromosome has no link to nucleus. The
nucleus link sits on GO:0000228 nuclear chromosome. "Nuclear chromatin"
(GO:0000790) was merged into chromatin in
[geneontology/go-ontology#20000](https://github.com/geneontology/go-ontology/issues/20000),
because chromatin is outside a nucleus during open mitosis. Two other reasons
support keeping it that way:

- Nucleus is restricted to Eukaryota (`only_in` taxon 2759). A
  chromatin-`part_of`-nucleus link would make the archaeal annotations to
  chromatin and nucleosome (57 in QuickGO on 2026-11-14, all IEA) taxon
  violations, although some archaea do package DNA with histones.
- The practical cost is small. In the human GAF, 18 of 1,431 genes with a
  chromatin annotation (1.3%) have no annotation that reaches nucleus, so a
  "genes in the nucleus" query misses only 0.17% of its 10,810 genes. Several
  of the 18 look like questionable chromatin annotations in the first place.

For location-based drawing of GO-CAMs (AmiGO 3), 1,071 of 10,609 activity
locations in the cached GO-CAM index (10.1%) reach none of nucleus,
cytoplasm, plasma membrane or extracellular region by is_a/part_of. Of these,
497 are under chromosome (chromatin alone: 193 activities in 90 models). A
display-only default table (anything under chromosome is drawn in the nucleus
for eukaryotic models, flagged as a layout default) handles most of them
without asserting anything in the ontology.

## The problem in the chromatin subtree

The is_a children of chromatin mix four axes (state, composition, position
and condition). Logical definitions exist for only two of the position-based
terms. There is no constitutive or facultative heterochromatin term, and
nucleolus organizer region and sex chromatin have definitions that disagree
with their placement.

The bigger problem is in the part_of children:

| Complex | Asserted location |
|---|---|
| histone acetyltransferase complex (GO:0000123) | part_of chromatin |
| HDA1, Set3, Sin3-type, Rpd3L-Expanded, Snt2C complexes | part_of chromatin |
| histone deacetylase complex (GO:0000118), their parent | part_of nucleoplasm |
| histone methyltransferase complex (GO:0035097) | part_of nucleoplasm |
| chromatin silencing complex (GO:0005677) | part_of nucleus |
| cohesin, condensin | part_of chromosome |
| SWI/SNF superfamily-type, FACT, HULC, Swi5-Sfr1, Swi5-Swi2, dosage compensation | part_of chromatin |

GO:0000123 is logically defined as any complex capable of histone
acetyltransferase activity, so its `part_of chromatin` edge is inherited by
every such complex. That includes the type B enzyme, which acetylates histone
H4 before the histone is deposited into chromatin. The edge came in with
[geneontology/go-ontology#23892](https://github.com/geneontology/go-ontology/issues/23892),
because nucleoplasm is defined as "nuclear content other than the
chromosomes"; that definition makes the `part_of nucleoplasm` links on the
deacetylase and methyltransferase complexes equally questionable. Removing
`part_of chromatin` from the complexes (keeping nucleosome) would drop 120
human genes from chromatin queries, 109 of which still reach nucleus through
other annotations. A go-ontology issue setting this out has been drafted for
filing.

## Modules

| Module | Members | Status | Notes |
|---|---|---|---|
| [HAT-B complex](../modules/scer_hat_b_complex.html) (`modules/scer_hat_b_complex.yaml`) | HAT1, HAT2, HIF1 | DRAFT | Proposes a GO term for the type B HAT complex and records the GO:0000123 `part_of chromatin` edge as a proposed deletion. Two biology gaps: free H4 versus H3-H4 dimer as substrate, and HAT-B's role at double-strand breaks. |
| [Rtt109-Vps75 complex](../modules/scer_rtt109_vps75_complex.html) (`modules/scer_rtt109_vps75_complex.yaml`) | RTT109, VPS75 | DRAFT | Uses GO:0070775 H3 histone acetyltransferase complex, which is also inferred to be part of chromatin; the complex has no activity on nucleosomal H3, so it is a second counterexample to the GO:0000123 edge. Vps75 drives H3 tail (K9, K27) acetylation; K56 needs Asf1 and not Vps75. Two biology gaps: where the complex acts (before or after nuclear import), and Rtt109-independent roles of Vps75 (narrowed by PMID:19470761). |
| [NuA4 complex](../modules/scer_nua4_complex.html) (`modules/scer_nua4_complex.yaml`) | ESA1, EPL1, YNG2, EAF6 (plus unreviewed hub and TINTIN subunits) | DRAFT | Three parts: the piccolo HAT core (Esa1 H4 acetyltransferase, Epl1 activator and nucleosome binding, Yng2 H3K4me3 reader, Eaf6), the Tra1-Eaf1 hub, and TINTIN (Eaf3 H3K36me3 reader). Acts on nucleosomes, so the inherited chromatin location is fine. Proposes a `capable_of` H4 acetyltransferase axiom for GO:0032777 piccolo, which is otherwise not classified as a HAT complex. |
| [SAGA HAT module](../modules/scer_saga_hat_module.html) (`modules/scer_saga_hat_module.yaml`) | GCN5, ADA2, NGG1, SGF29 | DRAFT | The Gcn5-Ada2-Ada3 catalytic core (Ada2 as acetyltransferase activator, Ada3 contributing) plus Sgf29 as H3K4me3 reader. Proposes a GO term for the SAGA-type HAT module and a definition fix for GO:0070461 SAGA-type complex, whose definition requires TAFs that its children ADA and ATAC lack. |
| [NuA3 complex](../modules/scer_nua3_complex.html) (`modules/scer_nua3_complex.yaml`) | SAS3, NTO1, YNG1, EAF6, TAF14 (plus Pdp3) | DRAFT | Sas3 H3K14 acetyltransferase with Nto1, Yng1 (H3K4me3 reader), Eaf6 and Taf14 (H3K9ac reader); NuA3a and NuA3b as variants, with Pdp3 (H3K36me3 reader) in NuA3b. Records that the GO:1990468 NuA3b definition names H3K4me3 where Pdp3 reads H3K36me3. |
| [SAS-I complex](../modules/scer_sas_complex.html) (`modules/scer_sas_complex.yaml`) | SAS2, SAS4, SAS5 | DRAFT | Sas2 H4K16 acetyltransferase, Sas4 adaptor and Sas5. SAS-I has little or no activity on nucleosomes and has not been seen on chromatin by ChIP. Its GO term (GO:0033255) sits under piccolo rather than under the HAT complex hierarchy; the module proposes moving it under protein acetyltransferase complex. |

The HAT-B case is concrete: all three yeast subunits are annotated `part_of`
GO:0000123 (IDA, IPI), so they inherit `part_of chromatin`. Meanwhile
UniProt's curated text for Hat1 says it acetylates free histone H4 in the
cytoplasm and that modification of chromatin-packaged H4 is not established.

## Gene reviews

| Gene | Rows | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | TOO_GENERAL | REMOVE | UNDECIDED | NEW |
|---|---|---|---|---|---|---|---|---|---|
| HAT1 | 36 | 11 | 9 | 9 | 1 | 1 | 4 | 0 | 1 |
| HAT2 | 35 | 15 | 4 | 3 | 2 | 0 | 11 | 0 | 0 |
| HIF1 | 29 | 9 | 6 | 7 | 1 | 0 | 5 | 0 | 1 |
| VPS75 | 53 | 20 | 9 | 19 | 0 | 0 | 4 | 0 | 1 |
| EPL1 | 30 | 17 | 1 | 6 | 0 | 0 | 5 | 0 | 1 |
| YNG2 | 29 | 16 | 2 | 5 | 0 | 0 | 6 | 0 | 0 |
| EAF6 | 16 | 11 | 1 | 4 | 0 | 0 | 0 | 0 | 0 |
| ADA2 | 87 | 22 | 9 | 3 | 2 | 0 | 50 | 0 | 1 |
| NGG1 | 50 | 18 | 0 | 2 | 0 | 0 | 29 | 1 | 0 |
| SGF29 | 30 | 19 | 0 | 2 | 1 | 0 | 8 | 0 | 0 |
| NTO1 | 20 | 12 | 4 | 1 | 1 | 0 | 0 | 0 | 2 |
| YNG1 | 29 | 14 | 3 | 4 | 1 | 0 | 7 | 0 | 0 |
| TAF14 | 71 | 44 | 2 | 8 | 0 | 1 | 13 | 0 | 3 |
| SAS4 | 21 | 5 | 1 | 4 | 1 | 0 | 9 | 0 | 1 |
| SAS5 | 24 | 5 | 3 | 6 | 3 | 1 | 6 | 0 | 0 |

The main corrections for the HAT-B subunits:

- **Activity terms refined to the acetylation site.** "Histone acetyltransferase activity" and its broader parents on Hat1 are modified to histone H4K12 acetyltransferase activity (the primary site) and H4K5 (the minor site, shown in vivo). Hat2's `contributes_to` rows get the same refinement.
- **Rpd3L complex removed from Hat2.** Both Rpd3L rows on Hat2 come from a fungal PAINT node that sits above all three budding-yeast RbAp46/48 paralogs, with only Ume1 and *S. pombe* Prw1 as seeds. Ume1, not Hat2, is the WD40 subunit of Rpd3L. Hat2's "regulation of DNA-templated transcription" IBA is marked over-annotated for the same reason.
- **Hif1 histone binding refined.** Its histone binding rows are modified to H3-H4 histone complex chaperone activity.
- **Telomeric location marked over-annotated.** The electronic "chromosome, telomeric region" rows on all three genes are inferred from the silencing phenotype, and no study shows any of the three at telomeres. Telomeric silencing itself is kept as non-core: it needs histone H3 tail mutations to appear and is indirect.
- **New location rows.** Hat1 and Hif1 each get a NEW "site of double-strand break" row (ChIP, PMID:16612003).
- **Generic protein binding resolved by partner.** High-throughput rows whose partner is another HAT-B subunit are removed (18 rows): the interaction is already captured by the complex rows. Four Hif1 rows whose partner is histone H4 are modified to histone binding. The Hif1 row from the structural study, whose partner is Hif1 itself, is modified to protein homodimerization activity.
- **Complex rows kept.** The GO:0000123 histone acetyltransferase complex rows are accepted, because the membership claim is right; the chromatin problem lies in the ontology. HAT1 carries the proposed HAT-B complex term and the proposed edge deletion.
- **Catalytic base recorded as a gap.** UniProt annotates Glu255 as Hat1's active site from an author statement. Mutagenesis shows neither Glu255 nor any nearby acidic residue is needed for activity, so HAT1 records the catalytic base as a knowledge gap.

For VPS75:

- **Core functions.** Acetyltransferase activator activity (activating Rtt109) and H3-H4 histone complex chaperone activity are both accepted as core.
- **Histone binding refined.** All six histone binding rows (one IBA, one IDA and four IPI with histones H3 and H4) are modified to H3-H4 histone complex chaperone activity.
- **Protein binding resolved by partner.** Rows where a study measured Rtt109 activation are modified to acetyltransferase activator activity (six). Rows that only detect or map the Rtt109 interaction are removed (four). Self-interaction rows, including all four "identical protein binding" rows, are modified to protein homodimerization activity (seven).
- **Kept as non-core.** Chromatin location and chromatin binding are kept as non-core, because the core activity acts on histones not yet in chromatin. So are DNA replication-dependent chromatin assembly (the replication link runs mainly through Rtt109 and Asf1) and NHEJ (genetic and indirect).
- **Cytosol kept as non-core.** Table 2 of PMID:22932476 lists Vps75 among nuclear proteins that leave the nucleus under hypoxia and return on reoxygenation; the location is real but condition-specific.

For the other HAT complex members:

- **Generic protein binding.** Removed wherever the partner is a fellow subunit (50 rows on ADA2, 29 on NGG1, and most on the others). Rows with a histone partner were modified to the specific reader or binding activity.
- **Activator activity added where it was missing.** Ada2 (activating Gcn5, PMID:11773077) and Epl1 (activating Esa1, PMID:21984211) each get a NEW acetyltransferase activator activity row, the same term Vps75 carries for Rtt109.
- **Reader activities.** Yng2, Yng1 and Sgf29 are H3K4me3 readers. Taf14 gets NEW H3K9ac and H3K9cr reader rows.
- **Paralog and complex over-propagation removed.** Four complex IBA rows (TFIID, TFIIF, SWI/SNF, INO80) are removed from Sas5. They come from a node above the Sas5-Taf14 split that is seeded only by Taf14 and Tfg3.
- **Taf14's Mediator row removed.** It came from a 1994 Mediator preparation that contained co-purifying TFIIF, and is recorded as a source defect for SGD.
- **SAS-I subunits.** Sas4 and Sas5 get `contributes_to` H4K16 acetyltransferase activity, and their `enables` HAT rows are recorded as wrong-qualifier source defects, since Sas2 is the catalytic subunit. Their silencing rows become heterochromatin boundary formation, because SAS-I limits SIR spreading rather than forming heterochromatin.
- **New row.** Vps75 gets a NEW "nucleosome disassembly" row (PMID:19470761): independently of Rtt109, Vps75 and RSC remove H2A/H2B dimers from nucleosomes. The same paper narrows the module's open question about Vps75's Rtt109-independent roles.

## Plan

Yeast histone acetyltransferase complexes, each as its own module:

- [x] HAT-B (Hat1, Hat2, Hif1)
- [x] gene reviews for HAT1, HAT2 and HIF1
- [x] Rtt109-Vps75 (H3 acetylation of new histones; RTT109 already reviewed)
- [x] gene review for VPS75
- [x] NuA4 and piccolo NuA4, with reviews of EPL1, YNG2 and EAF6
- [x] SAGA HAT module, with reviews of ADA2, NGG1 and SGF29
- [x] NuA3, with reviews of NTO1, YNG1 and TAF14
- [x] SAS-I, with reviews of SAS4 and SAS5

Follow-ups from these reviews, on genes reviewed before this project:

- [ ] GCN5: its core function covers H3 only (Gcn5 also acetylates H2B, PMID:30224453), has no `in_complex`, and it accepts chromatin organization from PMID:9674426 where NGG1 refines the same paper's row to chromatin remodeling.
- [ ] SAS2: it accepts subtelomeric heterochromatin formation as core where SAS4 and SAS5 now use heterochromatin boundary formation, and it accepts IDA rows from PMID:11731479 whose full text reportedly shows the purified complex failing to acetylate histones (not yet read verbatim).
- [ ] ESA1: accepts the general histone acetyltransferase rows that EPL1 and YNG2 refine, and marks a transcription NAS row over-annotated where they modify it.

Then the deacetylase complexes asserted `part_of chromatin` (Rpd3L, Rpd3S,
Hda1, Set3, Snt2C) and the remodelers, so that every complex in the table
above has a module that records where it acts.

Ontology track:

- [ ] file the go-ontology issue on the chromatin subtree
- [ ] update the HAT-B module's `request_status` once filed
- [ ] add to the issue: SAS-I and piccolo sit outside the HAT complex hierarchy (GO:0033255 under GO:0032777, which has no `capable_of`), and the GO:0070461 and GO:1990468 definition errors

## Reproducing the numbers

Scripts are in [`CHROMATIN/scripts/`](CHROMATIN/scripts/). The figures above
came from go-basic.obo (`releases/2026-07-26`), goa_human.gaf (generated
2026-05-21) and `gocams/index.tsv` as committed on 2026-11-14:

```bash
python projects/CHROMATIN/scripts/chromatin_nucleus_queries.py go-basic.obo goa_human.gaf.gz
python projects/CHROMATIN/scripts/gocam_unplaced_locations.py go-basic.obo gocams/index.tsv
```

Both follow is_a and part_of only, and count protein rows only (NOT and
complex rows excluded).
