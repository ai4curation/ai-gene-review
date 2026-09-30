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
- **Human function is often only inferred from mouse.** The discovery work on
  the muscle SERCA regulators was done in mouse, so human `MRLN` (myoregulin)
  and `ERLN` have only ISS/IEA, and human `STRIT1` (DWORF) has ISS for
  SERCA activation plus **45 IPI `protein binding` rows** from interactome
  screens. Small hydrophobic TM peptides are notoriously "sticky" in such
  screens. This is the clearest case where a well-established function is
  invisible as experimental GO for the human gene.
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
| Mitochondrial assembly factors and complex subunits | `UQCC6` (BRAWNIN, complex III), AltMIEF1, `MTLN`, `PIGBOS1`, `SMIM26`, `CEBPZOS`, `MLDHR` | assembly/stabilisation of respiratory complexes or mitoribosome; organelle contact |
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
   them with the canonical protein. **A folder convention is needed before any
   of these can be reviewed** (proposal: `genes/human/<HOSTGENE>-<ACC>/` or the
   HGNC symbol if one is assigned).
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
- [ ] Naming/folder convention for alt-ORF / uORF peptides (needs maintainer decision)

## Tier 1 — sORF-class, well characterized, GO gap/problem (human)
- [ ] STRIT1 (DWORF) — no human experimental function; 45 IPI protein binding
- [ ] MRLN (myoregulin) — ISS/IEA only
- [ ] ERLN (endoregulin) — ISS/IEA only
- [ ] MTLN (mitoregulin)
- [ ] UQCC6 (BRAWNIN)
- [ ] NBDY (NoBody)
- [ ] MYMX (myomixer)
- [ ] SPAAR
- [ ] SMIM43 (NEMEP)
- [ ] TUNAR
- [ ] PIGBOS1
- [ ] APELA (Elabela)

## Tier 2 — sORF-class, emerging / thin evidence
- [ ] ASDURF, MLDHR, MARCHF6-DT, CLMB, TZMP1, SMIM22, CEBPZOS, HOXB-AS3, LINC-PINT
- [ ] SMIM series with IEA-only `membrane` (SMIM2, 5, 10, 11, 13, 15, 18, 36, 40, 41) and HTP/IDA localization only (SMIM8, 12, 14)
- [ ] Alt-ORF entries blocked on naming: AltMIEF1 (L0R8F8), DDIT3 uORF (P0DPQ6), PRKCH uORF2 (C0HM02), SEHBP (C0HLU2), miPEP155 (C0HMA1), SHMOOSE (C0HM83)
- [ ] mtDNA-rRNA peptides: humanin, MOTS-c, SHLPs; MTRNR2L1–13

## Tier 3 — over-annotation audit (PE4–5 with IBA/ISS function)
- [ ] SNRPGP15, PMCHL1, PMCHL2, DPH3P1, GNG5B, LITAFD, ZNF788P

## Comparators (classic small proteins)
- [ ] SLN, PLN (SERCA regulators; well annotated — the template for MRLN/STRIT1/ERLN)

## Already reviewed in repo (≤100 aa, sORF-relevant)
- [x] SMIM26, P3R3URF, ADIG (plus canonical small proteins such as TOMM5/6/7, PIGY, UQCC3)

# NOTES

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
