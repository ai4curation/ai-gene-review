---
title: "Microproteins (sORF-encoded peptides)"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human]
genes: [STRIT1, MRLN, ERLN, SLN, PLN, MTLN, UQCC6, NBDY, MYMX, SPAAR, PIGBOS1, SMIM43, TUNAR, ASDURF, MLDHR, MARCHF6-DT, CLMB, TZMP1, SMIM1, SMIM22, APELA, SNRPGP15, PMCHL1, DPH3P1, GNG5B, SMIM26, P3R3URF, ADIG, MICOS10, SMIM3, TINCR, FBXW7-AS1, SNURF, C18orf32, C8orf17, C2orf15, KIAA0040, LINC01587, SMIM10L1, NLRP2B, SMIM45, PRAC2, SEPTIN14P20]
---

# Microproteins (sORF-encoded peptides)

**Bottom line:** in human, the conventionally-defined microproteins (≤100 aa) are
not one class but several, and GO coverage splits sharply along that line. The
short proteins known for decades — OXPHOS subunits, ribosomal proteins,
secreted hormones, metallothioneins — are as well annotated as longer
proteins. The microproteins discovered from small open reading frames (sORFs)
in lncRNAs, uORFs and alternative frames since ~2013 are not: of 69 Swiss-Prot
entries of this kind with protein-level evidence, 54% have any experimental GO
annotation, and 23% have a molecular function annotation of any kind. Several of the best-studied
(DWORF/`STRIT1`, myoregulin/`MRLN`, endoregulin/`ERLN`) carry **no** human
experimental function annotation at all — only ISS/IEA transfers from mouse.
The thousands of Ribo-seq ORFs outside Swiss-Prot have essentially no GO.

## Scope and definitions

"Microprotein" (also micropeptide, SEP — sORF-encoded peptide) conventionally
means a polypeptide of ≤100 aa encoded by a small open reading frame, usually
one that genome annotation missed because it is short or sits in an RNA
labelled non-coding [PMID:28698598 "Classification and function of small open reading frames."].
This project cares mostly about that *sORF* sense: peptides
translated from lncRNAs (e.g. `MRLN`, `STRIT1`, `NBDY`, `MTLN`), from upstream
ORFs (uORFs) in 5′ leaders (e.g. `ASDURF`, the PRKCH and DDIT3 uORF peptides),
from alternative or overlapping frames (AltMIEF1), and from mitochondrial rRNA
(humanin, MOTS-c). Short *canonical* proteins are included only as a
comparison class.

The field is large and growing. Proteogenomics first showed that sORF peptides
are made in human cells
[PMID:23160002 "Peptidomic discovery of short open reading frame-encoded peptides in human cells."];
CRISPR screens then found hundreds of noncanonical ORFs that are needed for growth
[PMID:32139545 "we exploit a systematic CRISPR-based screening strategy to identify hundreds of
noncanonical CDSs that are essential for cellular growth"]; and GENCODE,
HGNC and UniProt agreed a shared catalogue of human Ribo-seq ORFs
[PMID:35831657 "a standardized catalog of 7,264 human Ribo-seq ORFs"].
The classic single-gene exemplars — muscle SERCA regulators, the
P-body protein NoBody — were first identified as "non-coding" RNAs
[PMID:25640239 "A micropeptide encoded by a putative long noncoding RNA regulates muscle performance."]
[PMID:26816378 "A peptide encoded by a transcript annotated as long noncoding RNA enhances SERCA activity in muscle."]
[PMID:27918561 "A human microprotein that interacts with the mRNA decapping complex."].

## Questions

1. **Which annotations exist?** How many human microproteins are in UniProt,
   at what evidence level, and under what names?
2. **Do they have GO annotations?** How much, which evidence codes, and is it informative?
3. **What do they do?** For the sORF-class ones with real evidence, what is
   the core function, and does GO say so?
4. **What are the curation hazards** specific to very short proteins?

## Findings so far (census, 2026-09-30)

Reproducible via `projects/MICROPROTEINS/scripts/microprotein_census.py`
(UniProt REST + current `goa_human.gaf`). Full per-entry table:
[human_microproteins.tsv](MICROPROTEINS/data/human_microproteins.tsv); summary with the
per-gene list: [census summary](MICROPROTEINS/data/census_summary.md).

### 1. What is in UniProt

- **776** reviewed (Swiss-Prot) human entries ≤100 aa (of 20,431 in total), plus
  **8,918** unreviewed, non-fragment entries ≤100 aa in the human reference proteome.
- Most of the 7,264 GENCODE Ribo-seq ORFs have **no UniProtKB entry at all** yet, so
  they cannot receive GAF annotations.
- The Swiss-Prot ≤100 aa set was split into classes with a rule-based script
  (see caveats):

| class | n | any GO | informative GO¹ | experimental² | MF | BP |
|---|---:|---:|---:|---:|---:|---:|
| other characterized small protein | 249 | 91% | 86% | 63% | 53% | 72% |
| secreted peptide / hormone / defensin | 168 | 99% | 99% | 54% | 60% | 76% |
| **sORF-class, putative (no protein-level evidence)** | 125 | 34% | 26% | 4% | 6% | 10% |
| **sORF-class, protein-level evidence** | 69 | 80% | 77% | 54% | 23% | 43% |
| OXPHOS subunit | 45 | 100% | 100% | 98% | 64% | 96% |
| keratin-associated / cornified envelope | 44 | 91% | 89% | 30% | 23% | 39% |
| Ig/TCR gene segment | 25 | 96% | 96% | 0% | 0% | 0% |
| mtDNA-rRNA-encoded (humanin, MOTS-c, SHLPs, HN-like) | 21 | 81% | 81% | 19% | 71% | 67% |
| ribosomal protein | 16 | 100% | 100% | 88% | 100% | 100% |
| metallothionein | 14 | 100% | 100% | 71% | 100% | 100% |

¹ excluding `protein binding` (GO:0005515) and root terms. ² ≥1 informative
annotation with EXP/IDA/IPI/IMP/IGI/IEP or an HT code.

For comparison, across the whole reviewed proteome, coverage falls steadily with length:
experimental informative GO is 81% for proteins >600 aa, 71% for 151–300 aa,
53% for 51–100 aa and **19% for ≤50 aa**
([by-length table](MICROPROTEINS/data/go_coverage_by_length.tsv)).

### 2. Do they have GO annotations?

Mostly not, and when they do it is usually thin:

- **Localization, not function.** The typical sORF-class annotation is a CC
  term (mitochondrion, ER, nucleus — often HTP/HDA from localization screens),
  or an IEA `membrane` from a predicted TM helix. Only 23% of the
  protein-level-evidence set have any MF term. The whole SMIM series
  (`SMIM2`, `SMIM5`, `SMIM10`, `SMIM11`, `SMIM13`, `SMIM15`, `SMIM18`, `SMIM36`, `SMIM40`, `SMIM41`)
  carries nothing beyond IEA `membrane`.
- **Human function in GOA is often only inferred from mouse.** The discovery work on
  the muscle SERCA regulators was done in mouse, so in GOA human `MRLN` (myoregulin)
  and `ERLN` have only ISS/IEA, and human `STRIT1` (DWORF) has ISS for
  SERCA activation plus **45 IPI `protein binding` rows** from one yeast two-hybrid
  screen. Small hydrophobic TM peptides are notoriously "sticky" in such
  screens. The Tier 1 reviews found that human-peptide experiments do exist for all
  three: reconstitution with purified SERCA, and cell assays with the human pump. So the
  gap is in GO coverage, not in the literature (see [Tier 1 results](#tier-1-results-2026-09-30)).
- **IBA reaches proteins that may not exist.** Several PE5 ("uncertain") products
  of pseudogenes inherit full sets of phylogenetic annotations: `SNRPGP15`
  (13 IBA spliceosome terms), `PMCHL1`/`PMCHL2` (neuropeptide signalling),
  `DPH3P1`, `GNG5B`. The Tier 3 audit confirmed this and removed 33 of 52 such rows
  (see [Tier 3 results](#tier-3-results-2026-10-04) and [IBA_REVIEW](IBA_REVIEW.md)).
  `GNG5B` itself turned out to be HGNC protein-coding now.
- **Where experimental annotation exists it is recent and good.** The best-annotated sORF
  products are `MIEF1`-altORF (AltMIEF1, 13 experimental: mitoribosome
  large-subunit assembly, complex I assembly), the PRKCH uORF2 peptide (10
  experimental: translation regulator/kinase inhibitor), `MARCHF6-DT`/PACMP
  (DNA repair, PAR binding), `SPAAR` (lysosomal v-ATPase / TORC1),
  `MTLN` (fatty-acid β-oxidation, respirasome), `NBDY` (P-body),
  `TUNAR` (ER Ca²⁺ homeostasis), `MLDHR`/PTEN-uORF MP31 (LDH inhibitor).

### 3. What do they do? (working picture)

Across the characterized sORF-class set, recurring themes are:

| theme | examples | typical mechanism |
|---|---|---|
| Regulators of membrane pumps and transporters | `SLN`, `PLN`, `MRLN`, `ERLN`, `STRIT1` (SERCA); `TUNAR`; `SMIM43`/NEMEP (glucose transporters) | single TM helix binds the pump and changes its kinetics — an *enzyme regulator* role |
| Mitochondrial assembly factors and complex subunits | `UQCC6` (BRAWNIN, complex III), AltMIEF1 (mitoribosome large subunit), `MTLN`, `PIGBOS1`, `SMIM26`, `MLDHR` (LDH inhibitor) | assembly/stabilisation of respiratory complexes or mitoribosome; organelle contact (`CEBPZOS` was listed here originally; its review found only localization evidence) |
| Membrane fusion | `MYMX` (myomixer, with myomaker) | fusogen partner |
| RNA-decay and translation control | `NBDY` (decapping), PRKCH-uORF2, `ASDURF` | scaffolding RNP complexes; *cis* uORF regulation |
| Signalling scaffolds / nuclear regulators | `SPAAR` (TORC1), `MARCHF6-DT`, PINT87aa, `HOXB-AS3` peptide, SEHBP | adaptor/binding partner of a larger protein |
| Secreted/hormone-like | `APELA` (Elabela/Toddler, apelin receptor ligand), humanin, MOTS-c | receptor ligand; humanin/MOTS-c receptor and mechanism claims are debated |

A recurring theme for GO: most of these peptides **regulate or are subunits of
a larger machine**, so the right MF is usually an *enzyme regulator*, *complex
subunit* or *binding* term, and the BP should be that machine's process — not
a new microprotein-specific branch. This needs to be tested gene by gene.

### 4. Curation hazards specific to microproteins

1. **Gene-symbol collisions.** UniProt files alternative/uORF peptides under
   the *host* gene: L0R8F8 (AltMIEF1) is gene `MIEF1`, P0DPQ6 is `DDIT3`, C0HM02 is
   `PRKCH`, C0HLU2 is `ZNF689`, C0HMA1 is `MIR155HG`; C0HM83 (SHMOOSE) and C0HMG9
   have no gene symbol. GOA's column 3 does the same. Anything keyed on
   symbol, including this repo's `genes/human/<SYMBOL>/` layout, will merge
   them with the canonical protein. See
   [Naming alternative-ORF peptides](#naming-alternative-orf-peptides-vs-isoforms-and-polyproteins)
   for the agreed convention.
2. **mtDNA-rRNA-encoded peptides** (humanin, MOTS-c, SHLP1–6) are filed under
   `MT-RNR1`/`MT-RNR2`, the rRNA genes; humanin and SHLP1–6 (seven entries)
   share the one symbol `MT-RNR2`. Nuclear `MTRNR2L1–13` ("humanin-like") are
   thought to derive from mitochondrial DNA inserted into the nuclear genome (NUMTs); most are PE2–3 and receive ISS/IEA only.
3. **Existence vs function.** A PE5 entry with IBA function terms (hazard
   above) asserts function for a protein that may not be made.
4. **Protein-binding inflation.** Single TM peptides give many false
   interactome hits (see `STRIT1`); these rows should not be read as a function.
5. **Orthology is weak.** Short, fast-evolving and often primate-specific ORFs
   make ISS/ISO and IBA transfers less reliable. The reverse also happens: human genes miss mouse
   experimental data because nobody made the ISS call.

## Tier 1 results (2026-09-30)

All 12 Tier 1 genes are reviewed; each review passes `just validate` with no annotation
left PENDING. Falcon deep research was run only for STRIT1, as a test. The wrapper reported
a 600 s timeout, but the run actually completed in 855 s and wrote
`genes/human/STRIT1/STRIT1-deep-research-falcon.md` (22 citations). The STRIT1 review was
written from the primary literature and does not cite that output. No deep research was run for
the other 11 genes. All 12 reviews rest on cached publications plus targeted PubMed retrieval.

| gene | existing rows | ACCEPT | NON_CORE | OVER | MODIFY | REMOVE | NEW | core MF |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `STRIT1` (DWORF) | 52 | 3 | 2 | 0 | 2 | 45 | 0 | transporter activator activity GO:0141109 |
| `MRLN` (myoregulin) | 6 | 3 | 1 | 0 | 2 | 0 | 1 | ATPase inhibitor activity GO:0042030 |
| `ERLN` (endoregulin) | 2 | 2 | 0 | 0 | 0 | 0 | 2 | ATPase inhibitor activity GO:0042030 |
| `MTLN` (mitoregulin) | 21 | 11 | 7 | 0 | 1 | 2 | 1 | cardiolipin binding GO:1901612 |
| `UQCC6` (BRAWNIN) | 11 | 9 | 0 | 1 | 0 | 1 | 0 | — (complex III assembly factor) |
| `NBDY` (NoBody) | 6 | 3 | 0 | 0 | 1 | 2 | 0 | — (P-body regulator) |
| `MYMX` (myomixer) | 19 | 7 | 7 | 4 | 1 | 0 | 1 | fusogenic activity GO:0140522 |
| `SPAAR` | 11 | 9 | 2 | 0 | 0 | 0 | 0 | — (TORC1 negative regulator) |
| `SMIM43` (NEMEP) | 8 | 5 | 2 | 0 | 1 | 0 | 1 | transporter activator activity GO:0141109 |
| `TUNAR` | 11 | 8 | 2 | 0 | 1 | 0 | 0 | ATPase binding GO:0051117 |
| `PIGBOS1` | 5 | 3 | 0 | 0 | 2 | 0 | 0 | transmembrane transporter binding GO:0044325 |
| `APELA` (Elabela) | 34 | 18 | 15 | 0 | 0 | 1 | 1 | hormone activity GO:0005179 |

### What Tier 1 shows

1. **The dominant role is regulating another protein.** Of the 12 genes:
   - Seven act on a partner protein. `STRIT1`, `MRLN`, `ERLN` and `TUNAR` act on SERCA;
     `SMIM43` on GLUT1/3; `PIGBOS1` on CLCC1; `SPAAR` on the lysosomal V-ATPase.
   - Two are assembly or scaffold factors (`UQCC6`, `MTLN`).
   - Only `MYMX` (a fusogen) and `APELA` (a hormone) have a stand-alone activity.
   - The GO MF terms that fit the regulators are the transporter/ATPase regulator terms:
     ATPase inhibitor activity GO:0042030, transporter activator activity GO:0141109.
     These are the terms curators already use for the classic regulins PLN and SLN.
   - **Several microproteins have no MF that GO can express yet**: BRAWNIN, NoBody, SPAAR,
     and MTLN's regulatory role. They were left without an MF rather than given
     `protein binding`.
2. **Direction and mechanism are often disputed.**
   - `TUNAR`: the papers disagree on whether it inhibits or activates SERCA, so it got only a
     neutral binding term.
   - `MRLN` and `ERLN`: the mouse and human-reconstitution studies disagree on whether the
     peptide changes the pump's Ca²⁺ affinity (KCa) or its maximum rate (Vmax).
   - `MTLN`: the papers disagree on whether it sits in the outer or inner membrane.
   - `STRIT1`: it is unclear whether it activates SERCA directly or only by displacing the
     inhibitors.
   - Each is recorded as a `suggested_question` rather than resolved by fiat.
3. **Interaction-screen inflation is the largest source of removals**: 45 of 52 STRIT1 rows
   (HuRI yeast two-hybrid), plus the bare `protein binding` rows on MTLN, NBDY and UQCC6.
4. **Downstream physiology outnumbers direct function.** Knockout phenotypes (triglyceride
   homeostasis, muscle differentiation, insulin secretion, neuron development, vasculogenesis)
   were kept as non-core; 38 rows across the set.
5. **Specific errors found in GOA:**
   - `APELA` adult heart development (ISS) was transferred from mouse **Aplnr**, the receptor
     (Q9WV08), not from an Apela ortholog. Removed; worth reporting to UniProt.
   - `MYMX` regeneration (IMP) cites a paper that contains no regeneration experiment.
   - `UQCC6` complex IV assembly (IDA) rests on a marginal knockdown effect. The cited paper
     itself credits complex IV assembly to a different gene, TMEM223.
6. **Evidence strength of the new annotations (NEW):**
   - `ERLN`: IDA from reconstitution with purified human peptide.
   - `MYMX`: IDA, fusogenic activity with purified ectodomain.
   - `APELA`: IDA, Gi-coupled signalling.
   - `MTLN`: ISS from mouse (cardiolipin binding).
   - `SMIM43`: ISS from mouse NEMEP. The direction-giving mutant experiments are mouse; the
     human data are binding and flux only. Moderate confidence.
   - `MRLN`: ISS from mouse Q9CV60 (IDA, PMID:27923914). It was originally coded as IMP from
     an AC16 knockdown graded LOW_QUALITY, and was re-coded after PR review; the AC16 data are
     kept as corroboration only.

## Tier 2 results (2026-10-03)

Tier 2 covered 49 gene products, each reviewed and validated. They are 9 named emerging
microproteins, 13 SMIMs, 6 alternative-ORF or uORF peptides, humanin with SHLP1–6, MOTS-c,
and MTRNR2L1–13. MTRNR2L8–13 were finished on 2026-10-04 by fresh agents, after the first
attempt was stopped by a safety classifier (see notes). Across the 49, the 336 existing GOA
rows came out as: 145 ACCEPT, 24 KEEP_AS_NON_CORE, 70 MARK_AS_OVER_ANNOTATED, 32 MODIFY,
62 REMOVE and 3 UNDECIDED. There were 9 NEW proposals.

| group | genes | main outcome |
|---|---|---|
| named emerging microproteins | `ASDURF`, `MLDHR`, `MARCHF6-DT`, `CLMB`, `TZMP1`, `SMIM22`, `CEBPZOS`, `HOXB-AS3`, `LINC-PINT` | mostly sound but single-lab, often abstract-only; generic binding rows turned into informative MFs (`MLDHR` LDH inhibitor GO:0160193; `CLMB` calcineurin binding GO:0030346 plus NEW protein-membrane adaptor GO:0043495; `MARCHF6-DT` PAR binding GO:0072572); `TZMP1` NEW MKS complex membership |
| alt-ORF / uORF peptides | AltMIEF1 (`MIEF1__L0R8F8`), DDIT3 uORF (`DDIT3__P0DPQ6`), PRKCH uORF2 (`PRKCH__C0HM02`), SEHBP (`ZNF689__C0HLU2`), miPEP155 (`MIR155HG__C0HMA1`), SHMOOSE (`C0HM83`) | the first reviews made under the `<HOST>__<ACC>` convention; see hazard 1 below |
| SMIM series | `SMIM2`, 5, 8, 10, 11, 12, 13, 14, 15, 18, 36, 40, 41 | no function known for any; 22 bare `protein binding` rows from yeast two-hybrid screens removed; what remains is accurate and almost empty |
| mtDNA-rRNA-encoded peptides | humanin (`MT-RNR2__Q8IVG9`), SHLP1–6 (`MT-RNR2__*`), MOTS-c (`MT-RNR1__A0A0C5B5G6`) | humanin keeps a sound core (receptor ligand GO:0048018, BH3 domain binding GO:0051434, amyloid-beta binding GO:0001540) once 12 binding rows are triaged; SHLP2 gets its first MFs (NEW); MOTS-c: two GOA errors fixed, three NEW antimicrobial terms |
| nuclear humanin-like loci | `MTRNR2L1`–`MTRNR2L13` | every row inherited from humanin; 59 of 79 marked over-annotated and 16 removed where the locus substitutes residues known to abolish humanin activity or to block secretion |

### What Tier 2 adds

1. **The mRNA's cis effect is being annotated to the peptide (uORF peptides).** In `PRKCH__C0HM02`,
   5 of 10 GOA rows describe how uORF2 controls PKC-eta translation. That is a property of the
   mRNA and the scanning ribosome, not of the released 26-aa peptide. The 2009 source paper never
   detected the peptide. The rows were removed. The peptide's own function, PKC inhibitor
   activity GO:0008426, is what remains. `DDIT3__P0DPQ6` shows the same split: the well-known
   repression of CHOP translation was deliberately *not* annotated to the peptide. This is
   probably systematic across uORF-peptide entries and is worth raising with GOA/UniProt.
2. **Signature-based IEA on peptides shorter than the signature.** SHLP5, a 24-aa peptide,
   carries an InterPro2GO aromatic-amino-acid hydroxylase activity from IPR019774. That entry
   describes a catalytic domain several hundred residues long. Removed. A length guard in
   InterPro2GO would prevent this whole class of error.
3. **Annotations inherited from a peptide that may not exist.** MTRNR2L1–13 are HGNC-classified
   pseudogenes. Every row on them traces back to humanin: through ISS, through IEA copies of
   UniProt's own by-similarity location lines (so one claim is counted twice), or through IBA
   from PANTHER node PTN002141596. That node spans MT-RNR2 plus 13 nuclear copies, so 13 gene
   products are annotated as receptor antagonists on the evidence of one mitochondrial peptide.
   Only `MTRNR2L5` has a peptide-level assay of its own, which used synthetic HN5.
4. **Interaction screens are still the largest source of removals.** That held in the SMIMs and
   again in humanin. Several partners, such as UBQLN1/2 and SGTA, are chaperones that catch any
   exposed transmembrane helix.
5. **Synthetic-peptide evidence and single labs dominate.** miPEP155, MOTS-c, humanin, SHMOOSE
   and the SHLPs are known almost entirely from exogenous peptide, often at µM doses or as an
   analogue. `MLDHR`, `MARCHF6-DT`, `LINC-PINT`, `SEHBP` and `MIR155HG__C0HMA1` each rest on
   one lab. Two cases are odd: for miPEP155 the ORF is not in the mouse genome, yet the disease
   models used mice; for SHMOOSE the reviewer's sequence check puts the start codon inside
   tRNA-Ser.
6. **GOA errors found and fixed** (each a candidate report to the source):
   - MOTS-c GO:2001145 names a PIP3 *5*-phosphatase, but the evidence concerns PTEN, a
     3-phosphatase. Modified to the parent term.
   - MOTS-c "involved in purine biosynthesis" has the wrong sign: the peptide blocks it.
   - HOXB-AS3 "protein stabilization" comes from a paper whose claim is about stabilising
     c-Myc *mRNA*.
   - Humanin "iron ion homeostasis" (NAS) rests only on co-occurrence with iron deposits.
7. **Evidence strength of the 9 new annotations (NEW):**
   - `CLMB`: IDA, calcineurin recruitment to membranes.
   - `TZMP1`: IDA, MKS complex by co-purification.
   - `MIR155HG__C0HMA1`: IDA, HSPA8 ATPase inhibition in a cell-free assay with the human protein.
   - SHLP2: 3 terms, receptor ligand for ACKR3 and misfolded-IAPP binding.
   - MOTS-c: 3 antimicrobial terms, resting mainly on one 2026 eLife paper. This is the most
     recent and least replicated evidence in the set.

## Tier 3 results (2026-10-04)

Tier 3 audited 7 entries that the census flagged as uncertain products of pseudogene-like loci
carrying function annotations. Across the 52 GOA rows: 33 REMOVE, 14 MARK_AS_OVER_ANNOTATED,
2 ACCEPT, 2 KEEP_AS_NON_CORE and 1 UNDECIDED. No NEW proposals. Each gene has a reproducible
`-bioinformatics/` folder comparing it with its parent protein.

| entry | HGNC locus type | product exists? | rows | outcome | how function reached it |
|---|---|---|---:|---|---|
| `SNRPGP15` | pseudogene | **no**: GRCh38 has a TGA stop at codon 75 (independently re-checked); the 16 MS peptides assigned to it are all shared with SNRPG | 18 | 16 REMOVE, 2 over-annotated (RNA binding, whose residues are intact and which the PTHR10553 family review scopes family-wide) | IBA from PTHR10553 nodes (snRNP, spliceosome, P granule); InterPro2GO; ARBA |
| `PMCHL1` | pseudogene | no: 5'-truncated PMCH copy with no signal peptide; antiserum found nothing in testis or brain; the authors propose a noncoding RNA | 7 | 7 REMOVE | IBA from PTN002636265 (seeded by rat Pmch); InterPro2GO prepro-MCH; GOC inference; NAS from a 1993 paper |
| `PMCHL2` | pseudogene | no: hominid duplicate of PMCHL1, testis-only transcript | 6 | 6 REMOVE | same routes as PMCHL1 |
| `DPH3P1` | pseudogene | probably not: processed pseudogene, no GTEx expression; residues intact | 5 | 3 REMOVE, 2 over-annotated (iron and metal ion binding, residues intact) | IBA from PTN000485452 (DPH3 orthologs); InterPro2GO |
| `GNG5B` | gene with protein product (formerly GNG5P2; MANE) | possibly: intact ORF, CaaX kept, but ≤0.29 TPM and no peptide | 8 | 8 MARK_AS_OVER_ANNOTATED | IBA (node placement sound); InterPro2GO; ISS from bovine GNG2 |
| `LITAFD` | gene with protein product (MANE, conserved to fish) | **yes**: a real gene, misfiled into this tier by the census | 6 | 2 ACCEPT, 2 non-core, 2 over-annotated | IBA; LITAF-specific nucleus and cytokine terms placed at deep nodes |
| `ZNF788P` | pseudogene | no: truncated KRAB-A only, no zinc fingers, stop codon between exons | 2 | 1 REMOVE, 1 UNDECIDED | InterPro2GO from the KRAB signature; the nucleus row came from a YFP-tagging screen against an older 615-aa UniProt sequence |

### What Tier 3 shows

**Action rule used for products of doubtful existence.** For each annotation, ask whether the
sequence still supports the specific activity or location:
- **MARK_AS_OVER_ANNOTATED** for a molecular activity whose residue basis is intact, e.g. RNA
  binding on `SNRPGP15` (Sm-site RNA contacts kept), or iron and metal binding on `DPH3P1` (all
  four CSL cysteines kept). The sequence does not contradict the activity; only the existence
  of a product is in doubt.
- **REMOVE** for terms that need more than the intact site, or whose basis is lost:
  - complex membership and processes that depend on altered interfaces (SNRPGP15 ring contacts);
  - secretion-dependent hormone activity without a signal peptide (`PMCHL1`, `PMCHL2`);
  - transcription regulation without DNA-binding zinc fingers (`ZNF788P`);
  - process and location terms with nothing locus-specific behind them.
- The locus type decides which half of the rule applies to process and location rows. On a
  pseudogene locus with weak protein evidence (PE5, no transcript support), those rows are
  removed and only residue-supported MF rows are flagged. On a protein-coding locus whose ORF
  is intact but whose product is undetected (`GNG5B`: HGNC protein-coding, MANE, CaaX motif
  kept, PE3), every row is flagged as over-annotated instead, because a real product is
  plausible and the inherited terms are not contradicted by anything.
- The rule was written down after PR review found it had been applied inconsistently. SNRPGP15's
  RNA binding had been changed to over-annotated, which also resolved a CI conflict with the
  PTHR10553 family review (which scopes RNA binding family-wide), while DPH3P1's equivalent rows
  were still removed. Both now follow the same rule.

1. **Pipelines do not check whether a product exists.** IBA (PAINT), InterPro2GO, ARBA and GOC
   inference all annotate UniProt entries regardless of PE5 status, a "Could be the product of a
   pseudogene" CAUTION, or HGNC `locus_type: pseudogene`. The node placements were mostly
   correct. The failure is at the leaf. The upstream fix is a filter: skip entries that are PE5,
   carry a pseudogene CAUTION, or are HGNC pseudogenes. Excluding the specific PANTHER
   subfamilies (PTHR12091:SF1 for PMCHL1/2, PTHR21454:SF23 for DPH3P1) would also work. The same
   mechanism produced the MTRNR2L findings in Tier 2.
2. **UniProt entries can drift away from the genome.** SNRPGP15's 76-aa sequence is not
   encoded by GRCh38, which has a stop at codon 75. ZNF788P's nucleus annotation was made against
   a 615-aa sequence that UniProt has since replaced with an 82-aa one. Annotations are not
   re-checked when the sequence changes.
3. **Shared peptides inflate proteomic evidence.** SNRPGP15's "proteomics identification"
   rests entirely on peptides identical to SNRPG. The two peptides that would tell them apart
   have never been observed.
4. **Census caveat.** The rule-based census was wrong for two of the seven: `LITAFD` is a
   real conserved gene, and `GNG5B` has been promoted to protein-coding. Tier assignments from
   the census should be read as leads to check, not conclusions.

## Tier 4 results (2026-10-08)

Tier 4 covered the rest of the census's sORF-class entries that carry GO rows (12 with
protein-level evidence, 4 without), plus the two classic regulins `SLN` and `PLN` as
comparators. All 18 are reviewed and validated: 386 GOA rows, of which 116 ACCEPT,
16 KEEP_AS_NON_CORE, 22 MARK_AS_OVER_ANNOTATED, 21 MODIFY, 208 REMOVE and 3 UNDECIDED,
plus 3 NEW. Bare `protein binding` accounts for 197 of the 208 removals: 58 of 60 rows on
`SMIM3`, 54 of 64 on `SMIM1` and 62 on `PLN`, almost all from HuRI-type yeast two-hybrid
screens with unrelated membrane partners. This is the STRIT1 pattern again: single-helix
microproteins are "sticky" in Y2H.

| entry | rows | outcome | note |
|---|---:|---|---|
| `PLN` | 139 | 39 ACCEPT, 65 REMOVE, 16 over-annotated, 10 MODIFY, 8 non-core, 1 UNDECIDED | core: ATPase inhibitor activity (GO:0042030) on SERCA2a, relieved by phosphorylation; homopentamer reservoir. Heart rate over-annotated (the null mouse has normal heart rate) |
| `SLN` | 29 | 15 ACCEPT, 5 MODIFY, 5 REMOVE, 3 non-core, 1 over-annotated | generic enzyme inhibitor/regulator terms → GO:0042030; Ca2+ transport terms → GO:1902081, since SLN regulates the pump and does not carry Ca2+ |
| `MICOS10` | 24 | 16 ACCEPT, 8 REMOVE, 1 NEW | NEW membrane bending activity (GO:0180020) by ISS from yeast Mic10 (glycine motifs conserved); SAM complex HDA row removed, as in the APOO/APOOL reviews |
| `SMIM1` | 64 | 8 ACCEPT, 54 REMOVE, 1 MODIFY, 1 non-core | Vel antigen; an IBA for *nucleate* erythrocyte development (zebrafish donor) on a species whose red cells lose the nucleus → erythrocyte differentiation |
| `SMIM3` | 60 | 1 ACCEPT, 58 REMOVE, 1 over-annotated | membrane only; no function known |
| `TINCR` | 8 | 6 ACCEPT, 2 non-core, 2 NEW | NEW SUMO binding (IDA) and positive regulation of epithelial cell differentiation (IMP, start-codon knockout with recoded rescue; one group, another saw no effect) |
| `FBXW7-AS1` (DEspR) | 9 | 4 ACCEPT, 4 MODIFY, 1 REMOVE | GPCR-defined terms on a single-pass 85-aa protein → transmembrane signaling receptor activity; "VEGF receptor" terms → the assayed ligand is the VEGF-A *signal peptide*. All ligand data from one lab; the authors' own MS did not detect the protein |
| `SNURF` | 5 | 4 ACCEPT, 1 REMOVE | **name collision**: the ATPase-binding IEA comes from a mouse IPI where "SNURF" is RNF4 (residues 20–177 cannot exist in a 71-aa protein); fix belongs at MGI |
| `C18orf32` | 9 | 5 ACCEPT, 3 REMOVE, 1 over-annotated | ER/lipid droplet. Its best-supported biology, a requirement for PGAP1-mediated GPI inositol deacylation (and a GPI-deficiency disorder), is not in GOA; not annotated because PGAP1 does the step |
| `NLRP2B` | 11 | 9 ACCEPT, 2 non-core | pyrin-only NF-κB dampener; endogenous protein never detected; the NOT IL-1β/NLRP3 rows are informative against the PYDC2 paralog |
| `SEPTIN14P20` (RBRP) | 3 | 2 ACCEPT, 1 MODIFY | residues 1–47 are identical to SEPTIN14 383–429, contradicting the paper's "no homologs" claim and weakening its antibody/MS existence evidence (marked DISPUTED) |
| `SMIM45` | 6 | 1 ACCEPT, 5 REMOVE | **sequence swap**: the experimental rows (PMID:36593289) describe the downstream 107-aa hominoid ORF; UniProt replaced the entry's sequence with the conserved 68-aa upstream ORF in 2023_03 and the rows stayed |
| `C8orf17` | 8 | 2 ACCEPT, 2 REMOVE, 2 over-annotated, 2 UNDECIDED | PE1, but Ensembl transcript is TEC with no orthologues |
| `C2orf15` | 6 | 5 REMOVE, 1 over-annotated | Y2H binding and one RNA-capture hit |
| `LINC01587` | 1 | 1 REMOVE | TAS nervous system development from a differential-display methods paper |
| `KIAA0040`, `SMIM10L1`, `PRAC2` | 1, 1, 2 | ACCEPT | location only |

### What Tier 4 adds

1. **Annotations outlive the sequence they were made on.** `SMIM45` is the third case after
   `ZNF788P` and `SNRPGP15`: the experiment was on a 107-aa product that no longer has an
   accession, and the rows now sit on an unrelated 68-aa protein. A bicistronic locus makes
   this worse, because both products share the symbol and the transcript. The upstream fix is
   for UniProt to give the 107-aa product its own entry and move the statements.
2. **Old names collide with new genes.** `SNURF` was once also a name for RNF4, and an
   IEA transferred an RNF4 interaction onto the 71-aa uORF peptide. Microprotein genes often
   reuse short, generic names, so symbol-based text mining and orthology transfer are both
   exposed.
3. **Existence claims for alt-ORF peptides need a parent check.** RBRP (`SEPTIN14P20`) is
   largely septin sequence, so antibody and MS evidence that does not exclude SEPTIN14 does
   not establish the peptide. This is the `SNRPGP15` shared-peptide problem in another form.
4. **Regulin MF pattern (Plan item 7).** `PLN`, `MRLN` and `ERLN` now carry GO:0042030
   ATPase inhibitor activity, and the `SLN` review recommends the same; GOA's SLN rows used
   only generic enzyme inhibitor/regulator terms, which are not parents of GO:0042030.
   `STRIT1` (DWORF) carries GO:0141109 transporter activator activity, which is the remaining
   asymmetry: either DWORF moves to ATPase activator activity (GO:0001671) or the inhibitors
   move to transporter inhibitor activity (GO:0141110, which PLN also has by IDA). Both reviews
   leave this as a suggested question for GO.

## Naming alternative-ORF peptides (vs isoforms and polyproteins)

The repo already has two ways to handle several products from one gene. Neither fits
alternative-ORF peptides, because an alt-ORF peptide is a **separate UniProt entry**
that happens to share a symbol with its host gene.

| case | example | UniProt | GOA rows keyed on | how the repo handles it |
|---|---|---|---|---|
| splice / alternative-initiation isoform (same frame) | PTEN-L (P60484-2) | isoform of the host accession | host accession (isoform in col 17) | one folder `genes/human/PTEN/`; `isoform:` on annotations, `functional_isoforms` type `SPLICE_VARIANT` |
| polyprotein cleavage product | POMC → ACTH, α-MSH, β-endorphin | `PRO_` chains of the host accession | host accession P01189 | one folder `genes/human/POMC/`; `functional_isoforms` type `CLEAVAGE_PRODUCT`, `maps_to: UNIPROT_CHAIN` plus `isoform_specific_terms` |
| **alternative ORF / uORF peptide** (different frame or non-overlapping ORF, own sequence) | AltMIEF1 = L0R8F8, gene `MIEF1` (canonical MIEF1 = Q9NQG6) | **own accession** | **own accession**; col 3 carries the host symbol | no convention yet |

Why alt-ORF peptides cannot go into the host folder as a `functional_isoform`:
- None of the host entry's isoforms or chains contain the peptide's sequence.
- `fetch-gene` pulls GOA by accession, so the peptide's annotations would never be seeded into the host folder.
- Host and peptide usually have unrelated functions. AltMIEF1 assembles the mitoribosome; MIEF1 recruits DRP1 for mitochondrial fission.

**Convention (agreed 2026-09-30, recorded in `CLAUDE.md`):**

1. **The peptide has its own HGNC symbol.** Use it as a plain folder name. This covers
   all the renamed lncRNA-derived peptides (`SPAAR`, `NBDY`, `MTLN`, `STRIT1`, `MRLN`) and
   the uORF peptides HGNC named with the `-URF` suffix (`ASDURF`, `HRURF`, `P3R3URF`).
   PTEN's uORF peptide is also named, as `MLDHR` (HGNC:55481), so the PTEN locus shows all three
   cases side by side: PTEN-L is an isoform in `PTEN/`, and MP31 goes in `MLDHR/`.
2. **The peptide shares its host's symbol, or has none.** Use `genes/<org>/<HOST>__<ACC>/`,
   with `id: <ACC>` and `gene_symbol: <HOST>` (which matches UniProt and GOA column 3).
   Examples: `MIEF1__L0R8F8`, `DDIT3__P0DPQ6`, `PRKCH__C0HM02`, `ZNF689__C0HLU2`,
   `MIR155HG__C0HMA1`, and `MT-RNR2__Q8IVG9` (humanin).
   - This reuses a precedent already in the repo: eight `SYMBOL__ACC` folders for same-symbol
     paralogues in *P. putida* (e.g. `genes/PSEPK/aroE__Q88K85`).
   - The double underscore is unambiguous because HGNC symbols contain single hyphens
     (`MT-RNR2`, `-AS1`, `-DT`) but never underscores.
   - If HGNC later assigns a symbol, rename using `target.superseded_by` in history.
   - For peptides with no symbol at all (SHMOOSE C0HM83, C0HMG9), use the accession
     as the folder name (the pattern already used for ~150 non-model-organism folders).
3. In the peptide's `description`, state the host locus and the ORF type (uORF,
   overlapping +1 frame, lncRNA). In the host review, if the two are easily confused, add one
   line in the notes pointing to the peptide folder. Do not add the peptide as a
   `functional_isoform` of the host.

Tested on 2026-09-30:
- `just fetch-gene human L0R8F8 --alias MIEF1__L0R8F8`, run in a scratch directory, seeded
  20 GOA annotations, all on L0R8F8 and none from canonical MIEF1.
- `fetch-gene` originally wrote `gene_symbol: L0R8F8`. It now takes UniProt's gene name when it is given an accession, so the stub gets `MIEF1`.
- After that edit the file passes `ai-gene-review validate`, and no check ties the folder name to `gene_symbol`.

What this does not solve:
- Anything outside this repo that joins on symbol will still merge host and peptide.
  This includes QuickGO symbol searches, GOA column 3, and gene-level enrichment sets.
- The peptide's GO annotations therefore leak onto the host gene in those symbol-keyed
  analyses. This is worth raising with UniProt/GOA as a `suggested_questions` item.

## Plan

1. Settle the naming/folder convention for alternative-ORF peptides (hazard 1).
2. Review Tier 1 genes (sORF-class, strong literature, GO gap or problem).
3. Audit IBA/IEA on PE4–5 pseudogene products (Tier 3).
4. Collect patterns → GO recommendations (e.g. how to annotate pump-regulatory
   peptides; whether HTP localization should count as characterisation).
5. Later: mouse orthologs (where most discovery was done), and the non-Swiss-Prot Ribo-seq ORFs.
6. Follow-up PR: file new-term requests (NTRs) for the activities GO cannot yet express. There
   are five so far:
   - BRAWNIN (`UQCC6`): cytochrome b stabilisation in the complex III assembly intermediate;
   - NoBody (`NBDY`): EDC4/decapping-complex modulation;
   - `SPAAR`: V-ATPase–Ragulator supercomplex stabilisation that limits mTORC1 recruitment;
   - `MTLN`: its regulatory role in respiratory supercomplex assembly;
   - SHMOOSE (`C0HM83`): MICOS complex binding.
   Each should become a `proposed_new_terms` entry with a scoped definition.
7. Follow-up: settle the regulin MF pattern. SLN and PLN are now reviewed; the inhibitors
   converge on GO:0042030, and the open choice is how to code DWORF (`STRIT1`) consistently
   (see "What Tier 4 adds").
8. Upstream reports: SMIM45 sequence swap (UniProt), SNURF/RNF4 name collision (MGI).
9. Next census slice: the remaining zero-GO sORF entries (mostly PE5 lncRNA ORFs) do not need
   review; the SLC35A4 uORF peptide (STREMI, reported MIC10-like) is a candidate if UniProt
   gives it an accession.

---
# STATUS

Last updated: 2026-10-08

## Census
- [x] Census script + tables (`MICROPROTEINS/scripts/microprotein_census.py`)
- [x] Naming/folder convention for alt-ORF / uORF peptides — `<HOST>__<ACC>`, or the HGNC symbol when one is assigned (agreed 2026-09-30; in `CLAUDE.md`)

## Tier 1 — sORF-class, well characterized, GO gap/problem (human)
- [x] STRIT1 (DWORF) — 45 IPI protein binding removed; human-peptide evidence exists but GOA uses ISS
- [x] MRLN (myoregulin) — MODIFY to ATPase inhibitor activity; NEW re-coded as ISS from mouse after PR review
- [x] ERLN (endoregulin) — NEW IDA from human reconstitution
- [x] MTLN (mitoregulin)
- [x] UQCC6 (BRAWNIN)
- [x] NBDY (NoBody)
- [x] MYMX (myomixer)
- [x] SPAAR
- [x] SMIM43 (NEMEP)
- [x] TUNAR
- [x] PIGBOS1
- [x] APELA (Elabela) — removed ISS transferred from the receptor Aplnr

## Tier 2 — sORF-class, emerging / thin evidence
- [x] ASDURF, MLDHR, MARCHF6-DT, CLMB, TZMP1, SMIM22, CEBPZOS, HOXB-AS3, LINC-PINT
- [x] SMIM series: SMIM2, 5, 8, 10, 11, 12, 13, 14, 15, 18, 36, 40, 41
- [x] Alt-ORF entries (`<HOST>__<ACC>` folders): AltMIEF1 (L0R8F8), DDIT3 uORF (P0DPQ6), PRKCH uORF2 (C0HM02), SEHBP (C0HLU2), miPEP155 (C0HMA1), SHMOOSE (C0HM83)
- [x] mtDNA-rRNA peptides: humanin, SHLP1–6, MOTS-c
- [x] MTRNR2L1–7
- [x] MTRNR2L8–13 (retried with fresh agents on 2026-10-04 after the first attempt was stopped)

## Tier 3 — over-annotation audit (PE4–5 with IBA/ISS function)
- [x] SNRPGP15, PMCHL1, PMCHL2, DPH3P1, GNG5B, LITAFD, ZNF788P (see [Tier 3 results](#tier-3-results-2026-10-04))

## Tier 4 — remaining sORF-class with GO rows, plus comparators
- [x] Protein-level: MICOS10, SMIM1, TINCR, FBXW7-AS1, SNURF, C18orf32, C8orf17, SMIM3, C2orf15, KIAA0040, LINC01587, SMIM10L1
- [x] Without protein-level evidence: NLRP2B, SMIM45, PRAC2, SEPTIN14P20
- [x] Comparators SLN, PLN (see [Tier 4 results](#tier-4-results-2026-10-08))

## Already reviewed in repo (≤100 aa, sORF-relevant)
- [x] SMIM26, P3R3URF, ADIG (plus canonical small proteins such as TOMM5/6/7, PIGY, UQCC3)

# NOTES

## 2026-10-08

- Tier 4: 18 reviews (16 census sORF-class entries with GO rows, plus SLN and PLN), one agent
  per gene or small group. The first FBXW7-AS1/C18orf32 agent was stopped by a safety
  classifier before writing anything; both genes were redone by fresh agents.
- Carried the four optional nits from the PR #3680 review: the GNG5B locus-type clause in the
  Tier 3 rule, DPH3P1's stale "removal" wording, TZMP1's replicate/negative-control wording,
  and named comparators (ATP5IF1, PLN, FNIP1, FNIP2) in the MIR155HG__C0HMA1 NEW reason.

## 2026-10-05

- PR #3680: merged `main` into the branch. APELA conflicted with the review merged in
  #4156, and main's version was kept; both reach the same conclusions, including the
  Aplnr-sourced ISS removal. This branch's extra proposal is a follow-up for that review:
  GO:0007193 adenylate cyclase-inhibiting GPCR signalling pathway (IDA, PMID:28137936 and
  PMID:25639753), which APLN carries.
- Changes from the review bot:
  - SMIM43 NEW re-coded from IDA to ISS (mouse A0A286YD83).
  - MRLN NEW re-coded from IMP to ISS (mouse Q9CV60).
  - Falcon wording corrected.
  - MTLN cardiolipin ISS given its mouse source (Q8BT35).
  - The census median is now a true median.

- PR #3680 CI (`validate-families`) flagged a family/gene disagreement: the PTHR10553 family review
  scopes RNA binding (GO:0003723) family-wide, but the SNRPGP15 review removed it. Both RNA-binding
  rows were changed to MARK_AS_OVER_ANNOTATED, because the Sm-site RNA-contact residues are intact
  and only the product's existence is in doubt. Tier 3 totals updated (35 removed, 12 over-annotated).

- Second PR review round: the reviewer found the Tier 3 actions inconsistent (SNRPGP15 RNA
  binding over-annotated, DPH3P1 metal binding removed, on the same argument). DPH3P1's two
  residue-intact binding rows are now over-annotated as well, and the action rule is written
  out under "What Tier 3 shows". Tier 3 totals are now 33 removed and 14 over-annotated.
- Optional review items also fixed:
  - the MTLN cardiolipin ISS now uses GO_REF:0000024, like the other ISS rows;
  - the TZMP1 NEW reason now leads with its direct evidence rather than the comparator gap;
  - the five-item NTR follow-up is added to the Plan.

## 2026-10-04

- MTRNR2L8–13 reviewed by two fresh agents, each editing one gene at a time. All six validate.
  Results: 26 rows marked over-annotated and 8 removed, with no core functions and no NEW
  proposals. MTRNR2L10 lost both IBA rows and both extracellular rows: it changes Ser14→Arg,
  a substitution known to abolish humanin activity, and both residues of the Pro19–Val20
  secretion segment.
- New family-level findings:
  - PANTHER IBA coverage follows subfamily assignment, not sequence. MTRNR2L12 lacks the IBA
    rows that its identical twin MTRNR2L8 carries.
  - Papers are now selecting MTRNR2L3/L10 via the propagated GO:1900118 term, so a propagated
    annotation is generating its own apparent confirmation.
  - Serum "humanin-like N" ELISAs cannot be locus-specific.
  - Recurring recommendation: restrict PTN002141596 to MT-RNR2 plus MTRNR2L5, the only two
    sequences with functional data.

- Tier 3 audit complete (7 entries, 52 rows; 37 removed). Two corrections to earlier work:
  - The census tier placed `LITAFD` here, but it is a real conserved gene.
  - My brief to the GNG5B agent claimed an experimental GOA row. That came from misreading a
    census column; the row is an ISS transfer from bovine GNG2.

## 2026-10-03

- Tier 2 (43 gene products) reviewed, one agent per gene or per small family batch; each
  committed once it passed validation. These were the first reviews in the `<HOST>__<ACC>`
  and bare-accession folders.
- MTRNR2L8–13: the agent was stopped by a safety classifier while writing the review files, and
  no gene files were changed. Its findings, recorded here only:
  - HGNC reclassified all six as pseudogenes in 2021.
  - No study detects a peptide from any of them.
  - Every row is inherited from humanin, or from synthetic HN5 for the apoptosis IBA.
  - MTRNR2L12 has the same sequence as MTRNR2L8 but lacks its IBA rows.
  - Its planned actions match MTRNR2L1–7: IBA and extracellular rows over-annotated,
    cytoplasm kept as non-core, no core functions.
  - Not retried pending a decision.
- Corrected the theme table: `CEBPZOS` has no evidence of an assembly role.

## 2026-09-30

- Project started. Census against UniProt release current on 2026-09-30 and
  GO Consortium `goa_human.gaf` (current). Numbers will change on re-run.
- Classification caveats: it is rule-based (keywords, name patterns, symbol
  patterns, creation date ≥2013). Some canonical proteins land in "sORF-class"
  (e.g. the SCYGR keratin-like family, `MICOS10`), and some sORF products land in
  other classes (`UQCC6`/BRAWNIN → OXPHOS; `APELA` → secreted; `SLN`, `STMP1` →
  other). The per-class percentages are indicative, not exact.
- Key literature cached: PMID:35831657 (GENCODE Ribo-seq ORFs), PMID:32139545
  (CRISPR screens of noncanonical ORFs), PMID:23160002 (peptidomics), PMID:28698598
  (sORF classification review; abstract only), PMID:25640239 (myoregulin),
  PMID:26816378 (DWORF), PMID:27918561 (NoBody).
- Existing reviews for ≤100 aa human genes (sORF-relevant): SMIM26, P3R3URF, ADIG.

- Naming: compared the three multi-product cases (isoform, polyprotein, alt-ORF).
  Alt-ORF peptides are separate UniProt accessions, so they cannot be `functional_isoforms`.
  Proposed a `<HOST>__<ACC>` folder, reusing the PSEPK paralogue precedent. Tested fetch and
  validate for MIEF1__L0R8F8 in a scratch directory; no folder was created in the repo.
- Convention agreed: `<HOST>__<ACC>` (double underscore). Added it to `CLAUDE.md`.
  `fetch-gene` now sets `gene_symbol` from the UniProt `GN Name=` line when it is given an accession.
- Tier 1 (12 genes) reviewed with one agent per gene, following the annotation-reviewer
  instructions; each was committed as it passed validation. Falcon deep research was tried
  only on STRIT1: the wrapper reported a 600 s timeout, but the run completed (855 s) and wrote
  `STRIT1-deep-research-falcon.md`. The review does not cite it. *(Corrected 2026-10-05 after
  PR review; the original note wrongly said no Falcon file existed.)*
- Corrected the census claim: human experimental evidence *does* exist for STRIT1, MRLN and
  ERLN, but GOA carries only ISS transfers from mouse for them.
- To check: the MRLN NEW (IMP, PMID:41348974) is weak. The reconstitution paper
  PMID:34445594 used synthetic MLN without stating its species, so it cannot replace that
  evidence as a human IDA. *(Resolved 2026-10-05: re-coded as ISS from mouse Q9CV60.)*
