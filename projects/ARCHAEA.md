---
title: "Archaea"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [METJA, SULAC, METAC, METTP, FERPA, 9ARCH, NITRP, METS5, ACIAM, SACS2, METTH, HALSA, HALVD]
autolink_exclude: [ftsZ]
genes: [ureC1, ureC2, Ferp_0128, mcrA, MJ1511, nadX, thiL, gatC, amoA, Hsp14, Hsp20, Msed_0709, sor, lacS, cdvB, Msed_1700, Msed_1695, bop, psmA1, Msed_1456, Msed_2001, Msed_1424, Msed_0406, Msed_0147, Msed_0148, Msed_1375, Msed_1993, Msed_1426, Msed_0638, Msed_0639, Msed_1321, Msed_0399, Msed_0656, Msed_1423, Msed_2055]
---

# Archaea

**Bottom line:** Archaea are one of the three domains of life, yet this
repository barely covered them. When the project started (2026-10-14),
only 13 of roughly 7,200 gene folders under `genes/` were archaeal,
holding 12 review files for 11 distinct proteins, and nothing had been
reviewed for the classic archaeal model organisms. The project (1) reviews
a representative set of archaeal genes across the processes where archaea
differ most from bacteria and eukaryotes, and (2) collects the recurring
ways GO annotation goes wrong for archaea, so that those failure patterns
can be reported upstream. It is anchored on the **Sulfolobales** (CO2
fixation, bioleaching and thermostable enzymes), with **methanogens**
(biomethane and power-to-gas) as a second DOE-facing theme and the
haloarchaea (*Haloferax*, *Halobacterium*) as a calibration set.

So far, twenty-five new archaeal reviews are complete (a five-gene pilot, a
second round of four, and two rounds on the *M. sedula* CO2-fixation
cycle), the cycle is built as a module, METAC mcrA has been revised, and the duplicate amoA
reviews have been merged. Most archaeal annotation turns out to be
electronic: of the 20 GOA rows on the pilot genes, only two were
experimental, and even the two best-studied haloarchaeal proteins have
thin, old experimental coverage. Sixteen recurring error patterns are
collected in [annotation-patterns](ARCHAEA/annotation-patterns.md). The
largest affect hundreds of archaeal proteins each: InterPro2GO mappings
that put catalytic activity on non-catalytic proteasome alpha subunits
and ubiquitin-dependent catabolism on organisms without ubiquitin.

## Why archaea need their own project

Several features make archaeal genes a distinctive test of GO annotation
quality:

- **Bacteria-trained pipelines.** Most prokaryotic electronic annotation
  (InterPro2GO, UniRule/ARBA, PANTHER IBA) was calibrated mainly on bacteria.
  When those transfers reach archaeal homologs, they can carry
  bacterial-only processes or components with them. Ferp_0128 already shows
  this: one of its six rows was removed.
- **Eukaryote-like information machinery inside a prokaryotic cell.** Archaeal
  replication (MCM, PCNA, Orc1/Cdc6), transcription (TBP/TFB, a multi-subunit
  RNA polymerase), histones, the proteasome and ESCRT-III-based cell division
  (Cdv) are homologous to eukaryotic machinery. Orthology transfer from
  eukaryotes can therefore attach nucleus-, chromatin- or organelle-specific
  terms to proteins in a cell that has no nucleus.
- **Analogous but non-homologous structures.** The archaellum looks like a
  bacterial flagellum but is built like a type IV pilus. GO keeps them apart:
  `GO:0097589` archaeal-type flagellum and `GO:0097590` archaeal-type
  flagellum-dependent cell motility. The grouping term `GO:0097588` archaeal
  or bacterial-type flagellum-dependent cell motility exists only for
  UniProt-keyword mapping, and its definition says not to use it for manual
  annotation. Rows on that grouping term, or on bacterial-flagellum terms
  attached to archaellum proteins, are a predictable error class.
- **Unique biochemistry.** Ether-linked isoprenoid membrane lipids,
  methanogenesis, ammonia oxidation by AOA, the modified glycolytic pathways
  of hyperthermophiles (ADP-dependent kinases, GAPOR) and the archaeal
  mevalonate-pathway variants have few close homologs outside archaea. That
  makes GO coverage there thin and makes the existing terms worth checking.

## Current inventory (existing reviews)

| Species code | Organism | Gene | UniProt | Status | Rows | Actions |
|---|---|---|---|---|---|---|
| METJA | *Methanocaldococcus jannaschii* | nadX | Q58325 | COMPLETE | 7 | 1 ACCEPT, 2 KEEP_AS_NON_CORE, 3 MODIFY, 1 NEW |
| METJA | *M. jannaschii* | thiL | Q60337 | COMPLETE | 6 | 4 ACCEPT, 1 KEEP_AS_NON_CORE, 1 NEW |
| METJA | *M. jannaschii* | MJ1511 | Q58906 | IN_PROGRESS | 1 | 1 REMOVE |
| METAC | *Methanosarcina acetivorans* | mcrA | Q8THH1 | COMPLETE | 11 (4 retired) | 7 ACCEPT, 1 MODIFY, 1 TOO_GENERAL, 2 NEW |
| METTP | *Methanothrix thermoacetophila* | gatC | A0B5K3 | COMPLETE | 10 | 2 ACCEPT, 1 KEEP_AS_NON_CORE, 5 REMOVE, 2 NEW |
| FERPA | *Ferroglobus placidus* | Ferp_0128 | D3S180 | DRAFT | 6 | 3 ACCEPT, 1 KEEP_AS_NON_CORE, 1 REMOVE, 1 UNDECIDED |
| 9ARCH | *Nitrososphaera viennensis* | ureC1 | A0A060HK93 | DRAFT | 6 | 4 ACCEPT, 2 KEEP_AS_NON_CORE |
| 9ARCH | *N. viennensis* | ureC2 | A0A060HQC5 | DRAFT | 6 | 4 ACCEPT, 2 KEEP_AS_NON_CORE |
| NITRP | *Nitrosopumilus maritimus* | amoA | D9J262 | COMPLETE | 2 | 1 MODIFY (retired GOA row), 1 NEW |
| SULAC | *Sulfolobus acidocaldarius* | Hsp14 | Q4J8A6 | DRAFT | 4 | 4 NEW |
| SULAC | *S. acidocaldarius* | Hsp20 | Q4JA95 | DRAFT | 4 | 4 NEW |

The archaeal virus protein SIRV1/orf114 (Q8QL27, the AcrIII-1 anti-CRISPR
ring nuclease) is covered by [CRISPR_ANTI_CRISPR](CRISPR_ANTI_CRISPR.md).
Related archaeal content also appears in [NITROGEN_CYCLE](NITROGEN_CYCLE.md)
(ammonia oxidation, archaeal nitrous-oxide reductase) and
[GERANYLGERANYL_REDUCTASE_OBSOLETION](GERANYLGERANYL_REDUCTASE_OBSOLETION.md)
(the archaeal lipid saturation step).

### Housekeeping found during the inventory

These are curation gaps, not biology. They should be fixed early so the
counts above stay meaningful.

1. **Duplicate amoA reviews. Done (2026-10-15).** `genes/NITRP/D9J262/`
   was merged into `genes/NITRP/amoA/` and retired (its history record
   points to the successor with `superseded_by`). Conflicting actions were
   reconciled on evidence. D9J262 is a 208-residue environmental clone
   fragment, not the type strain's own AmoA. GOA now returns no rows for
   it; the old row is kept as `retired: true`.
2. **Folder code does not match the entry.** The UniProt entry name of D9J262
   is `D9J262_9ARCH`, not `_NITRP`. The folder was kept as `NITRP/amoA`
   because PROTEOME_REMOVAL links to it (that page also had the organism
   wrong as "Nitrobacter sp."; corrected). Still open: whether to move it.
3. **Stray taxon-id folder.** `genes/188937/mcrA/` holds only a UniProt file
   for MCRA_METAC (Q8THH1). This duplicates `genes/METAC/mcrA/` and was
   probably left by a fetch that used a taxon id instead of a species code.
   **Deleted (2026-10-15).**
4. **Status drift.** Five of the eleven pre-project reviews are still
   DRAFT (ureC1, ureC2, Ferp_0128, Hsp14, Hsp20); METAC mcrA was revised
   and completed on 2026-10-15. The Hsp14
   and Hsp20 reviews contain only NEW rows, which means GOA had no
   annotations for either protein when they were fetched.

## Pilot results (October 2026)

All five reviews are COMPLETE and validated. Automated deep research was
unavailable (both provider API keys failed authentication), so each gene
has hand-written literature notes in `<gene>-notes.md` instead.

| Code | Gene | UniProt | GOA rows | Actions | Main finding |
|---|---|---|---|---|---|
| METS5 | Msed_0709 | A4YEN2 | 7 | 2 ACCEPT, 1 KEEP_AS_NON_CORE, 4 REMOVE, 1 NEW | Inherits aspartate-semialdehyde dehydrogenase and threonine biosynthesis terms from its ancestral family; GO lacks terms for its activities and for the 3HP/4HB cycle (3 terms proposed) |
| ACIAM | sor | P29082 | 2 | 2 ACCEPT, 2 NEW | Under-annotated: sulfur oxidation and iron ion binding added from experimental evidence |
| SACS2 | lacS | P22498 | 4 | 1 ACCEPT, 2 MODIFY, 1 REMOVE | Galactosyltransferase IBA from a plant-seeded PAINT node removed; activity refined to beta-glucosidase, beta-galactosidase and beta-fucosidase; process to lactose catabolism |
| METTH | mcrA | O27232 | 6 | 5 ACCEPT, 1 MODIFY, 1 NEW | Methanogenesis narrowed to methanogenesis from CO2; MCR complex added |
| SULAC | cdvB | Q4J924 | 1 | 1 MODIFY, 3 NEW | Nucleoid changed to cell division site; Cdv-dependent cytokinesis, ESCRT III complex and structural molecule activity added |

Follow-ups raised by the pilot:

All three were done in round 2 (below):

- The METAC mcrA review had problems found while reviewing the
  *Methanothermobacter* ortholog. All six were confirmed and fixed.
- Archaeal ESCRT-III homologs carrying vacuolar transport: Msed_1695
  reviewed.
- *M. sedula* Msed_1700, named malonyl-CoA reductase by ARBA: reviewed.

## Round 2 results (October 2026)

| Code | Gene | UniProt | GOA rows | Actions | Main finding |
|---|---|---|---|---|---|
| METS5 | Msed_1700 | A4YHF3 | 7 | 2 ACCEPT, 2 MODIFY, 2 KEEP_AS_NON_CORE, 1 UNDECIDED | The genuine aspartate-semialdehyde dehydrogenase; its ASD terms are right, but ARBA names it malonyl-CoA reductase. No experiments exist for this protein. Showed that TIGR00978 does not separate it from Msed_0709 (the earlier claim was corrected); CDD models do |
| METS5 | Msed_1695 | A4YHE8 | 1 | 1 REMOVE, 1 NEW | CdvB2 ortholog (identity, synteny, literature). Vacuolar transport removed; Cdv-dependent cytokinesis added by ISS from *S. acidocaldarius* CdvB2 |
| HALSA | bop | P02945 | 8 | 3 ACCEPT, 3 MODIFY, 1 REMOVE, 1 KEEP_AS_NON_CORE, 2 NEW | Calibration: accurate but thin, mostly from one 1973 abstract. Ion channel activity (a pump, not a channel) removed; proton transporter activity and retinal binding added; a light-driven proton transporter term proposed |
| HALVD | psmA1 | Q9V2V6 | 14 | 7 ACCEPT, 6 MODIFY, 1 REMOVE | Calibration: moderate, all IDA rows from two papers by one lab. Catalytic endopeptidase rows on the non-catalytic alpha subunit moved to structural constituent of proteasome; ubiquitin-dependent catabolism removed |
| METAC | mcrA | Q8THH1 | 11 (4 retired) | 7 ACCEPT, 1 MODIFY, 1 TOO_GENERAL, 2 NEW | Revised: GOA refreshed; miscited and non-verbatim support replaced; NEW heterooligomerization dropped; generic methanogenesis kept because *M. acetivorans* uses several routes but not H2/CO2 |

**Calibration verdict.** The two haloarchaeal proteins chosen as the
best-annotated archaeal baseline are not well annotated either. Their
experimental rows are correct but come from one or two old papers each,
and decades of later work never reached GO. So the archaeal deficit is
not only in poorly studied organisms.

## Round 3 results: the M. sedula 3HP/4HB cycle (October 2026)

With Msed_0709 from the pilot, all five reviewed enzymes of the cycle are
now done.

| Code | Gene | UniProt | GOA rows | Actions | Main finding |
|---|---|---|---|---|---|
| METS5 | Msed_1456 | A4YGR1 | 7 | 2 ACCEPT, 2 MODIFY, 1 MARK_AS_OVER_ANNOTATED, 1 REMOVE, 1 KEEP_AS_NON_CORE, 1 NEW | The IDA pathway row uses the Chloroflexus cycle term GO:0043427; modified to the proposed 3HP/4HB term. Acetyl-CoA synthetase and biosynthesis terms come from the acyl-CoA synthetase family; M. sedula's acetate-CoA synthetase is a different paralog (Msed_1353) |
| METS5 | Msed_2001 | A4YI89 | 4 | 2 ACCEPT, 1 MODIFY, 1 MARK_AS_OVER_ANNOTATED, 2 NEW | Also the cell's main crotonyl-CoA hydratase (86% of the activity), so it serves both halves of the cycle; fatty acid beta-oxidation comes from the ECHS1-named crotonase subfamily |
| METS5 | Msed_1424 | A4YGN0 | 2 | 1 ACCEPT, 1 MODIFY, 1 NEW | Purified and identified as the NADPH succinic semialdehyde reductase (PMID:19684143), the step after succinyl-CoA reduction; Swiss-Prot names it for the upstream step (EC 1.2.1.76), which Msed_0709 performs |
| METS5 | Msed_0406 | A4YDT1 | 11 | 5 KEEP_AS_NON_CORE, 3 MODIFY, 3 REMOVE, 1 NEW | The physiological 4-hydroxybutyrate-CoA ligase, though 4HB is its poorest in-vitro substrate; GO holds only the non-physiological acetate, propionate and butyrate activities, and has no 4HB-CoA ligase term |

Answer to the A1 question: GO records every substrate measured in vitro and
not the physiological one. The reviews keep the measured activities as
non-core and propose the missing physiological terms. Across the cycle the
reviews now propose five GO terms: malonyl-CoA reductase (NADP+),
succinyl-CoA reductase (NADP+), succinate-semialdehyde reductase (NADPH) and
4-hydroxybutyrate-CoA ligase activities, and carbon fixation by the
3HP/4HB cycle.

**Module.** The cycle is modelled in
`modules/hydroxypropionate_hydroxybutyrate_cycle.yaml` (DRAFT): two branches,
16 reaction steps, each grounded to an *M. sedula* protein identified in the
literature. Enzymes that act twice are modelled as separate steps with the
same participant. The acetyl-CoA/propionyl-CoA carboxylase (Msed_0147 biotin
carboxylase, Msed_0148 carrier, Msed_1375 carboxyltransferase) and the
methylmalonyl-CoA mutase (Msed_0638 with the B12-binding subunit Msed_2055)
are modelled as complexes whose subunits carry only their own activities.
Four steps have no GO activity term; their gene reviews propose one.

## Round 4 results: the rest of the module (November 2026)

Ten more proteins reviewed, so 15 of the module's 17 proteins had
reviews at this point (the last two follow below) (QC: 13 function checks match reviewed core functions, 0 conflicts).

| Gene(s) | Finding |
|---|---|
| Msed_0147, Msed_0148, Msed_1375 | Each carboxylase subunit enables only its own half-reaction and contributes to both carboxylase activities (PMID:12581213); TreeGrafter and InterPro2GO had put the whole-complex activity on the carboxyltransferase subunit; the carrier subunit had no GO rows |
| Msed_1993 | Malonic semialdehyde reductase; L-gulonate 3-dehydrogenase removed (lambda-crystallin subfamily transfer), NAD+ binding corrected to NADP binding |
| Msed_1426 | Acryloyl-CoA reductase; an IDA row uses the NADH-dependent term although the cited paper shows the enzyme does not use NADH (corrected to the NADPH term); alcohol dehydrogenase (NAD+) removed |
| Msed_0638, Msed_0639 | Confirmed as the cycle's mutase and epimerase by recombinant activity and autotrophic induction (PMID:22752162); the mutase needs the separate B12-binding subunit Msed_2055 |
| Msed_1321 | 4-hydroxybutyryl-CoA dehydratase; its main activity was missing from GOA because UniProt names it after an untested isomerase activity |
| Msed_0399 | Not the main enzyme for either of its activities: Msed_2001 hydrates crotonyl-CoA and Msed_1423 oxidizes (S)-3-hydroxybutyryl-CoA (PMID:32218776), so Msed_1423 replaces it as the module's representative |
| Msed_0656 | Beta-ketothiolase; general acyltransferase rows refined |

Msed_1423, now the main representative of the (S)-3-hydroxybutyryl-CoA
dehydrogenase step, and Msed_2055, the mutase's B12-binding subunit, were
reviewed afterwards, so all 17 module proteins now have reviews. Msed_1423 is
NAD+-specific (about 170-fold over NADP+) and inactive on C8, so its fatty acid
metabolism term is marked over-annotated. Msed_2055's isomerase row was a
whole-complex activity on a cofactor subunit (pattern 16). What remains open
for the module is biological: no step has genetic (knockout) evidence.

## Anchor organisms

Chosen on 2026-10-14 for relevance to DOE missions (bioenergy, critical
minerals, carbon management) and to industrial biotechnology. The
rationale below is the scoping view. Each claim still needs a citation in
the gene notes as the reviews are done.

| Role | Organisms (species code) | Why |
|---|---|---|
| **Anchor** | Sulfolobales: *Saccharolobus solfataricus* (SACS2), *Sulfolobus acidocaldarius* (SULAC), *Metallosphaera sedula* (METS5), *Acidianus ambivalens* (ACIAM) | Thermoacidophiles used for high-temperature bioleaching of metal sulfides. *M. sedula* fixes CO2 by the 3-hydroxypropionate/4-hydroxybutyrate (3HP/4HB) cycle and has been engineered as a CO2-to-chemicals host. *S. solfataricus* is a source of thermostable glycoside hydrolases for biomass processing, and of biotech tools (Sso7d, Dpo4). *S. acidocaldarius* has genetics and crenarchaeal cell biology (Cdv division, archaellum). |
| **Co-theme** | Methanogens: *Methanocaldococcus jannaschii* (METJA), *Methanosarcina acetivorans* (METAC), *Methanothermobacter thermautotrophicus* (METTH) | Methanogenesis underlies biogas and power-to-gas (electricity and CO2 to grid methane), and drives biogenic methane emissions. The repo already has METJA and METAC reviews. |
| **Calibration** | Haloarchaea: *Haloferax volcanii* (HALVD), *Halobacterium salinarum* (HALSA) | The most genetically tractable archaea, and so the richest in experimental GO annotation. They show what good archaeal annotation looks like. Their industrial use (PHBV bioplastic, salt-tolerant enzymes) comes mainly from *H. mediterranei*, which is outside the current target list. |

## Proposed review targets

Accessions were checked against UniProt on 2026-10-14. All are reviewed
(Swiss-Prot) entries except the *M. sedula* iron-oxidation proteins in A2. Where UniProt gives no gene symbol, the ordered
locus name from the UniProt record is shown and should be used as the
folder name.

### Part A. DOE-facing: Sulfolobales and methanogens

#### A1. CO2 fixation by the 3HP/4HB cycle (*Metallosphaera sedula*)

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| METS5 | Msed_0709 | A4YEN2 | Malonyl-CoA reductase (NADP) |
| METS5 | Msed_1456 | A4YGR1 | 3-hydroxypropionyl-CoA synthetase |
| METS5 | Msed_2001 | A4YI89 | 3-hydroxypropionyl-CoA dehydratase |
| METS5 | Msed_1424 | A4YGN0 | Succinic semialdehyde reductase (UniProt: succinate-semialdehyde dehydrogenase (acetylating); see Round 3) |
| METS5 | Msed_0406 | A4YDT1 | 4-hydroxybutyrate--CoA ligase 1 |

The cycle has no GO-CAM model in the repo, and its enzymes are
multifunctional. The two 4-hydroxybutyrate--CoA ligase paralogs (Msed_0406
and Msed_0394) also accept acetate, butyrate and propionate. That makes them
a test of whether GO records the physiological substrate or every substrate
seen in vitro. All five are now reviewed (Round 3), and the cycle is built
as the first archaeal module, `modules/hydroxypropionate_hydroxybutyrate_cycle.yaml`.

#### A2. Sulfur oxidation and bioleaching

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| ACIAM | sor | P29082 | Sulfur oxygenase/reductase (SOR) |
| ACIAM | doxD | P97207 | Thiosulfate:quinone oxidoreductase large subunit |
| ACIAM | doxA | P97224 | Thiosulfate:quinone oxidoreductase small subunit |
| METS5 | foxA | A4YE09 | Fox terminal oxidase, subunit I (heme-copper oxidase family) |
| METS5 | foxB | A4YE05 | Fox terminal oxidase, subunit II |
| METS5 | foxC | A4YE03 | FoxC |
| METS5 | foxD | A4YE02 | FoxD |
| METS5 | Msed_0323 | A4YDJ8 | Sulfocyanin (blue copper protein) |

The *M. sedula* iron-oxidation (*fox*) proteins and sulfocyanin are
unreviewed (TrEMBL) entries. They are in scope: they are the proteins that
link archaeal iron oxidation to bioleaching, and their GO annotation is
expected to come entirely from the generic heme-copper oxidase and cupredoxin
families.

#### A3. Thermostable carbohydrate and glycolytic enzymes

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| SACS2 | lacS | P22498 | Beta-galactosidase (broad-specificity beta-glycosidase) |
| SACS2 | xylS | Q9P999 | Alpha-xylosidase |
| PYRFU | gor | Q8U3K2 | Glyceraldehyde-3-phosphate:ferredoxin oxidoreductase (GAPOR) |
| PYRFU | pfkC | Q9V2Z7 | ADP-specific phosphofructokinase |

#### A4. Methanogenesis and power-to-gas

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| METTH | mcrA | O27232 | Methyl-coenzyme M reductase subunit alpha |
| METTH | frhA | P19496 | Coenzyme F420 hydrogenase subunit alpha |
| METJA | mcrA | Q58256 | Methyl-coenzyme M reductase I subunit alpha |
| METJA | mtrA | Q58261 | Tetrahydromethanopterin S-methyltransferase subunit A |
| METJA | hdrA | P60200 | CoB-CoM heterodisulfide reductase subunit A |
| METJA | cofC | Q58297 | 2-phospho-L-lactate guanylyltransferase (F420 biosynthesis) |

Together with the existing METAC mcrA review, this puts the same enzyme in
three methanogen lineages: hydrogenotrophic (METTH, METJA) and
methylotrophic/acetoclastic (METAC). The CO2-reduction pathway of
*M. jannaschii* or *Methanothermobacter* would be a good first archaeal
GO-CAM.

#### A5. Sulfolobales cell biology and information processing

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| SULAC | cdvA | Q4J923 | Cell division protein A |
| SULAC | cdvB | Q4J924 | Cell division protein B (ESCRT-III homolog) |
| SULAC | cdvC | F2Z6D2 | Cell division protein C (Vps4 homolog) |
| SULAC | flaI | Q4J9L0 | Archaeal flagellar ATPase motor FlaI |
| SACS2 | MCM | Q9UXG1 | Minichromosome maintenance protein MCM |
| SACS2 | pcn1 | P57766 | DNA polymerase sliding clamp 1 (PCNA1) |
| SACS2 | pcn2 | Q97Z84 | DNA polymerase sliding clamp 2 (PCNA2) |
| SACS2 | pcn3 | P57765 | DNA polymerase sliding clamp 3 (PCNA3) |
| SACS2 | dbh | Q97W02 | DNA polymerase IV (Dpo4) |
| SACS2 | albA1 | P60849 | DNA/RNA-binding protein Alba 1 |
| SACS2 | sso7d | P39476 | DNA-binding protein 7d (Sso7d) |
| METFE | hmfB | P19267 | Archaeal histone B (HMf-2) |
| PYRFU | rgy | P95479 | Reverse gyrase |

Questions to check:
- Do the ESCRT-III/Vps4 homologs pick up eukaryotic endosome or
  multivesicular-body terms by orthology?
- Are there nucleus or nucleosome rows on proteins from cells that have no
  nucleus?
- The three PCNA paralogs form an obligate heterotrimer, so they test
  `contributes_to` handling.
- Extend the archaellum set to the rest of the *fla*/*arl* operon once the
  FlaI review has shown which flagellum terms GOA carries.

#### A6. Ether-lipid membrane biosynthesis

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| METJA | MJ1250 | Q58647 | Geranylgeranylglyceryl phosphate synthase (GGGPS) |
| METJA | MJ0279 | Q57727 | Digeranylgeranylglyceryl phosphate synthase (DGGGPS) |
| METJA | carS | Q58995 | CDP-archaeol synthase |
| METJA | MJ0044 | Q60352 | Isopentenyl phosphate kinase |
| HALVD | mvaD | D4GXZ3 | Phosphomevalonate decarboxylase |

### Part B. Calibration set: haloarchaea

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| HALSA | bop | P02945 | Bacteriorhodopsin |
| HALSA | htr1 | P0DMI3 | Sensory rhodopsin I transducer (HTR-I) |
| HALVD | ftsZ1 | Q48327 | Cell division protein FtsZ 1 |
| HALVD | sepF | D4H018 | Cell division protein SepF |
| HALVD | psmA1 | Q9V2V6 | Proteasome subunit alpha 1 |
| HALVD | pan1 | D4GUJ7 | Proteasome-activating nucleotidase 1 |
| HALVD | samp1 | D4GUF6 | Small archaeal modifier protein 1 (SAMP1) |
| HALVD | ubaA | D4GSF3 | SAMP-activating enzyme E1 |
| HALVD | aglB | D4GYH4 | Oligosaccharyltransferase AglB (N-glycosylation) |

These are the archaeal proteins most likely to carry experimental (IDA/IMP)
annotation. They provide a baseline for how much the Part A organisms rely
on electronic annotation. SAMP1 and UbaA have two roles: they act as
ubiquitin-like protein modifiers and as sulfur carriers in molybdopterin and
tRNA thiolation, so they are good candidates for a core versus non-core
split.

## Plan

1. **Housekeeping** (above): amoA merged and stray folder deleted. Still
   to do: move the five DRAFT reviews to COMPLETE or record why they
   cannot be.
2. **Pilot (5 genes, DOE-facing): done.** Msed_0709 (malonyl-CoA
   reductase), sor, lacS, METTH mcrA and cdvB. See Pilot results above.
3. **Calibration pair: done.** bop and psmA1 (see Round 2 results).
4. **Error catalogue: started.** [annotation-patterns](ARCHAEA/annotation-patterns.md)
   records each recurring archaea-specific error (pipeline, term, example
   rows). Cross-link PAINT-derived entries to [IBA_REVIEW](IBA_REVIEW.md)
   and add new patterns as reviews are done.
5. **Breadth and modules:** review the rest of Part A theme by theme, then
   Part B. The 3HP/4HB CO2-fixation cycle module is built (DRAFT); remaining
   candidates are hydrogenotrophic methanogenesis and archaeal ether-lipid
   biosynthesis.
6. **Coverage measure:** add a script under `ARCHAEA/` that counts GOA rows
   by evidence code for each target species. It will show how far archaeal
   GO coverage depends on IEA, and can be re-run as the project progresses.

## Open questions

- Which species code should a TrEMBL entry with a `9ARCH` mnemonic use
  (`9ARCH` versus a strain-specific code)? This decides where the amoA review
  ends up.
- No GO-CAM model in `gocams/index.tsv` uses any of the archaeal taxa
  listed here (checked at scoping). Should the first archaeal model be the
  3HP/4HB cycle in *M. sedula* or CO2-reducing methanogenesis?
- Should *Haloferax mediterranei* PHBV biosynthesis (bioplastics) be added
  as a Part A theme? It is the main industrial use of haloarchaea, but the
  species has few reviewed UniProt entries.
