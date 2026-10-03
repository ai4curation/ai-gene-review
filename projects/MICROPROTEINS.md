---
title: "Microproteins (sORF-encoded peptides)"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human]
genes: [STRIT1, MRLN, ERLN, SLN, PLN, MTLN, UQCC6, NBDY, MYMX, SPAAR, PIGBOS1, SMIM43, TUNAR, ASDURF, MLDHR, MARCHF6-DT, CLMB, TZMP1, SMIM1, SMIM22, APELA, SNRPGP15, PMCHL1, DPH3P1, GNG5B, SMIM26, P3R3URF, ADIG]
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
  `DPH3P1`, `GNG5B`. These are candidates for an over-annotation audit (see
  [IBA_REVIEW](IBA_REVIEW.md)).
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
left PENDING. Falcon deep research timed out (600 s, tried on STRIT1), so the reviews rest on
cached publications plus targeted PubMed retrieval.

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
   - `SMIM43`: moderate confidence (co-IP plus binding-deficient mutants).
   - `MRLN`: IMP. The only human-cell evidence is shRNA knockdown in the AC16 transformed
     cardiac line, from a paper whose main topic is Wnt signalling. This is the weakest of
     the six and is a candidate to drop.

## Tier 2 results (2026-10-03)

Tier 2 covered 43 gene products, each reviewed and validated. They are 9 named emerging
microproteins, 13 SMIMs, 6 alternative-ORF or uORF peptides, humanin with SHLP1–6, MOTS-c,
and MTRNR2L1–7. **MTRNR2L8–13 are not reviewed**: a safety classifier stopped the agent
working on them before any file was written; see notes. Across the 43, the 302 existing GOA
rows came out as: 145 ACCEPT, 24 KEEP_AS_NON_CORE, 44 MARK_AS_OVER_ANNOTATED, 32 MODIFY,
54 REMOVE and 3 UNDECIDED. There were 9 NEW proposals.

| group | genes | main outcome |
|---|---|---|
| named emerging microproteins | `ASDURF`, `MLDHR`, `MARCHF6-DT`, `CLMB`, `TZMP1`, `SMIM22`, `CEBPZOS`, `HOXB-AS3`, `LINC-PINT` | mostly sound but single-lab, often abstract-only; generic binding rows turned into informative MFs (`MLDHR` LDH inhibitor GO:0160193; `CLMB` calcineurin binding GO:0030346 plus NEW protein-membrane adaptor GO:0043495; `MARCHF6-DT` PAR binding GO:0072572); `TZMP1` NEW MKS complex membership |
| alt-ORF / uORF peptides | AltMIEF1 (`MIEF1__L0R8F8`), DDIT3 uORF (`DDIT3__P0DPQ6`), PRKCH uORF2 (`PRKCH__C0HM02`), SEHBP (`ZNF689__C0HLU2`), miPEP155 (`MIR155HG__C0HMA1`), SHMOOSE (`C0HM83`) | the first reviews made under the `<HOST>__<ACC>` convention; see hazard 1 below |
| SMIM series | `SMIM2`, 5, 8, 10, 11, 12, 13, 14, 15, 18, 36, 40, 41 | no function known for any; 22 bare `protein binding` rows from yeast two-hybrid screens removed; what remains is accurate and almost empty |
| mtDNA-rRNA-encoded peptides | humanin (`MT-RNR2__Q8IVG9`), SHLP1–6 (`MT-RNR2__*`), MOTS-c (`MT-RNR1__A0A0C5B5G6`) | humanin keeps a sound core (receptor ligand GO:0048018, BH3 domain binding GO:0051434, amyloid-beta binding GO:0001540) once 12 binding rows are triaged; SHLP2 gets its first MFs (NEW); MOTS-c: two GOA errors fixed, three NEW antimicrobial terms |
| nuclear humanin-like loci | `MTRNR2L1`–`MTRNR2L7` | every row inherited from humanin; 33 of 45 marked over-annotated and 8 removed where the locus substitutes residues known to abolish humanin activity |

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

---
# STATUS

Last updated: 2026-09-30

## Census
- [x] Census script + tables (`MICROPROTEINS/scripts/microprotein_census.py`)
- [x] Naming/folder convention for alt-ORF / uORF peptides — `<HOST>__<ACC>`, or the HGNC symbol when one is assigned (agreed 2026-09-30; in `CLAUDE.md`)

## Tier 1 — sORF-class, well characterized, GO gap/problem (human)
- [x] STRIT1 (DWORF) — 45 IPI protein binding removed; human-peptide evidence exists but GOA uses ISS
- [x] MRLN (myoregulin) — MODIFY to ATPase inhibitor activity; NEW IMP is weak (see results)
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
- [ ] MTRNR2L8–13: data fetched, reviews not written (agent stopped by a safety classifier; awaiting decision whether to retry)

## Tier 3 — over-annotation audit (PE4–5 with IBA/ISS function)
- [ ] SNRPGP15, PMCHL1, PMCHL2, DPH3P1, GNG5B, LITAFD, ZNF788P

## Comparators (classic small proteins)
- [ ] SLN, PLN (SERCA regulators; well annotated — the template for MRLN/STRIT1/ERLN)

## Already reviewed in repo (≤100 aa, sORF-relevant)
- [x] SMIM26, P3R3URF, ADIG (plus canonical small proteins such as TOMM5/6/7, PIGY, UQCC3)

# NOTES

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
  instructions; each was committed as it passed validation. Falcon deep research timed out
  after 600 s (tested on STRIT1), so no `-deep-research-falcon.md` files exist for these genes.
- Corrected the census claim: human experimental evidence *does* exist for STRIT1, MRLN and
  ERLN, but GOA carries only ISS transfers from mouse for them.
- To check: the MRLN NEW (IMP, PMID:41348974) is weak. The reconstitution paper
  PMID:34445594 used synthetic MLN without stating its species, so it cannot replace that
  evidence as a human IDA.
