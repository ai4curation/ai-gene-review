---
title: "Archaea"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [METJA, SULAC, METAC, METTP, FERPA, 9ARCH, NITRP]
autolink_exclude: [ftsZ]
genes: [ureC1, ureC2, Ferp_0128, mcrA, MJ1511, nadX, thiL, gatC, amoA, Hsp14, Hsp20]
---

# Archaea

**Bottom line:** Archaea are one of the three domains of life, yet this
repository barely covers them. Of roughly 7,200 gene folders under `genes/`,
only 13 belong to archaea, and they cover 12 distinct proteins from seven
species (plus one archaeal virus protein). Nothing has been reviewed yet for
the classic archaeal model organisms (*Haloferax volcanii*, *Halobacterium
salinarum*, *Saccharolobus solfataricus*, *Pyrococcus furiosus*,
*Thermococcus kodakarensis*). This project sets out to (1) review a
representative set of archaeal genes across the processes where archaea
differ most from bacteria and eukaryotes, and (2) list the recurring ways GO
annotation goes wrong for archaea, so that those failure patterns can be
reported upstream. The project is at **SCOPING**: the inventory below is
complete, and the target gene list is a proposal that has not yet been
reviewed.

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
| METAC | *Methanosarcina acetivorans* | mcrA | Q8THH1 | DRAFT | 8 | 3 ACCEPT, 1 MODIFY, 1 REMOVE, 3 NEW |
| METTP | *Methanothrix thermoacetophila* | gatC | A0B5K3 | COMPLETE | 10 | 2 ACCEPT, 1 KEEP_AS_NON_CORE, 5 REMOVE, 2 NEW |
| FERPA | *Ferroglobus placidus* | Ferp_0128 | D3S180 | DRAFT | 6 | 3 ACCEPT, 1 KEEP_AS_NON_CORE, 1 REMOVE, 1 UNDECIDED |
| 9ARCH | *Nitrososphaera viennensis* | ureC1 | A0A060HK93 | DRAFT | 6 | 4 ACCEPT, 2 KEEP_AS_NON_CORE |
| 9ARCH | *N. viennensis* | ureC2 | A0A060HQC5 | DRAFT | 6 | 4 ACCEPT, 2 KEEP_AS_NON_CORE |
| NITRP | *Nitrosopumilus maritimus* | amoA | D9J262 | DRAFT | 4 | 1 MODIFY, 3 NEW |
| NITRP | *N. maritimus* | D9J262 | D9J262 | COMPLETE | 3 | 1 ACCEPT, 2 NEW |
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

1. **Duplicate amoA reviews.** `genes/NITRP/amoA/` and `genes/NITRP/D9J262/`
   both review accession D9J262 and reach different conclusions (1 MODIFY + 3
   NEW versus 1 ACCEPT + 2 NEW). They need merging into one folder.
2. **Folder code does not match the entry.** The UniProt entry name of D9J262
   is `D9J262_9ARCH`, not `_NITRP`. Before moving anything, check which
   species code the repo convention expects for unreviewed TrEMBL entries
   with a `9ARCH` mnemonic.
3. **Stray taxon-id folder.** `genes/188937/mcrA/` holds only a UniProt file
   for MCRA_METAC (Q8THH1). This duplicates `genes/METAC/mcrA/` and was
   probably left by a fetch that used a taxon id instead of a species code.
   It can be deleted.
4. **Status drift.** Seven of the twelve reviews are still DRAFT. The Hsp14
   and Hsp20 reviews contain only NEW rows, which means GOA had no
   annotations for either protein when they were fetched.

## Proposed review targets

All accessions below are reviewed (Swiss-Prot) entries, checked against
UniProt on 2026-10-14. The themes are ordered by how much they are expected
to expose archaea-specific annotation problems.

### 1. Cell division and the archaeal cytoskeleton

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| SULAC | cdvA | Q4J923 | Cell division protein A |
| SULAC | cdvB | Q4J924 | Cell division protein B (ESCRT-III homolog) |
| SULAC | cdvC | F2Z6D2 | Cell division protein C (Vps4 homolog) |
| HALVD | ftsZ1 | Q48327 | Cell division protein FtsZ 1 |
| HALVD | sepF | D4H018 | Cell division protein SepF |

Question: do ESCRT-III/Vps4 homologs pick up eukaryotic endosome or
multivesicular-body terms by orthology?

### 2. Archaellum (archaeal flagellum)

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| SULAC | flaI | Q4J9L0 | Archaeal flagellar ATPase motor FlaI |

Extend to the rest of the *S. acidocaldarius* *fla*/*arl* operon once the
FlaI review has shown which flagellum terms GOA actually carries.

### 3. Information processing (eukaryote-like machinery)

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| SACS2 | MCM | Q9UXG1 | Minichromosome maintenance protein MCM |
| SACS2 | pcn1 | P57766 | DNA polymerase sliding clamp 1 (PCNA1) |
| SACS2 | pcn2 | Q97Z84 | DNA polymerase sliding clamp 2 (PCNA2) |
| SACS2 | pcn3 | P57765 | DNA polymerase sliding clamp 3 (PCNA3) |
| SACS2 | albA1 | P60849 | DNA/RNA-binding protein Alba 1 |
| SACS2 | sso7d | P39476 | DNA-binding protein 7d (Sso7d) |
| METFE | hmfB | P19267 | Archaeal histone B (HMf-2) |
| PYRFU | rgy | P95479 | Reverse gyrase |

Question: are there nucleus or nucleosome rows on proteins from cells that
have no nucleus? The three PCNA paralogs form an obligate heterotrimer,
which makes them a test of `contributes_to` handling.

### 4. Protein degradation and modification

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| HALVD | psmA1 | Q9V2V6 | Proteasome subunit alpha 1 |
| HALVD | pan1 | D4GUJ7 | Proteasome-activating nucleotidase 1 |
| HALVD | samp1 | D4GUF6 | Small archaeal modifier protein 1 (SAMP1) |
| HALVD | ubaA | D4GSF3 | SAMP-activating enzyme E1 |
| HALVD | aglB | D4GYH4 | Oligosaccharyltransferase AglB (N-glycosylation) |

SAMP1 and UbaA have two roles: they act as ubiquitin-like protein modifiers
and as sulfur carriers in molybdopterin and tRNA thiolation. That makes
them good candidates for a core versus non-core split.

### 5. Ether-lipid membrane biosynthesis

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| METJA | — | Q58647 | Geranylgeranylglyceryl phosphate synthase (GGGPS) |
| METJA | — | Q57727 | Digeranylgeranylglyceryl phosphate synthase (DGGGPS) |
| METJA | carS | Q58995 | CDP-archaeol synthase |
| METJA | — | Q60352 | Isopentenyl phosphate kinase |
| HALVD | mvaD | D4GXZ3 | Phosphomevalonate decarboxylase |

UniProt gives no gene symbol for the rows marked "—". Take the folder
name from the ordered locus name in the fetched UniProt record; do not
guess it.

### 6. Energy metabolism

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| METJA | mcrA | Q58256 | Methyl-coenzyme M reductase I subunit alpha |
| METJA | mtrA | Q58261 | Tetrahydromethanopterin S-methyltransferase subunit A |
| METJA | hdrA | P60200 | CoB-CoM heterodisulfide reductase subunit A |
| METJA | cofC | Q58297 | 2-phospho-L-lactate guanylyltransferase (F420 biosynthesis) |
| PYRFU | gor | Q8U3K2 | Glyceraldehyde-3-phosphate:ferredoxin oxidoreductase (GAPOR) |
| PYRFU | pfkC | Q9V2Z7 | ADP-specific phosphofructokinase |

The METJA mcrA review would pair with the existing METAC mcrA review: the
same enzyme reviewed in two methanogen lineages.

### 7. Phototrophy and sensory signalling

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| HALSA | bop | P02945 | Bacteriorhodopsin |
| HALSA | htr1 | P0DMI3 | Sensory rhodopsin I transducer (HTR-I) |

Bacteriorhodopsin is one of the best-characterized membrane proteins known,
so it is a good calibration case for what full experimental GO coverage of
an archaeal protein looks like.

## Plan

1. **Housekeeping** (above): merge the amoA duplicates, delete the stray
   `genes/188937/` folder, and move the DRAFT reviews to COMPLETE or record
   why they cannot be.
2. **Pilot (5 genes):** bop, flaI, cdvB, MCM and psmA1, one from each of the
   main themes. Fetch them with `just fetch-gene <CODE> <gene>`, then run deep
   research and a full review.
3. **Error catalogue:** after the pilot, write `ARCHAEA/annotation-patterns.md`
   to record each recurring archaea-specific error (pipeline, term,
   example rows) and cross-link it to
   [IBA_REVIEW](IBA_REVIEW.md) where the source is PAINT.
4. **Breadth:** review the remaining targets theme by theme. Where a whole
   complex or pathway is covered, consider a module (for example archaeal
   ether-lipid biosynthesis or the methanogenesis core).
5. **Coverage measure:** add a script under `ARCHAEA/` that counts GOA rows
   by evidence code for the target species. It will show how far archaeal GO
   coverage depends on IEA, and can be re-run as the project progresses.

## Open questions

- Which species code should a TrEMBL entry with a `9ARCH` mnemonic use
  (`9ARCH` versus a strain-specific code)? This decides where the amoA review
  ends up.
- Should *Haloferax volcanii* (genetically tractable, the most experimental
  annotation) or *Sulfolobus*/*Saccharolobus* (crenarchaeal cell biology) be
  the anchor organism, in the way *B. subtilis* is for [BACSU](BACSU.md)?
- No GO-CAM model in `gocams/index.tsv` uses any of the archaeal taxa
  listed here (checked at scoping). Should the project build the first
  archaeal model, for example methanogenesis from CO2 in *M. jannaschii*?
