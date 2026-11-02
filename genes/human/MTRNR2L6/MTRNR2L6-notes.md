# MTRNR2L6 curation notes

Journal for the review of MTRNR2L6 (nuclear humanin-like locus). Written 2026-10-03.

## MTRNR2L6 (P0CJ73, humanin-like 6, HN6) - locus-specific notes

- Chromosome 7; PE2; 24 aa `MTPRGFSCLLLPTSETDLPVKRRT`; 20/24 (A2T, L12P, I16T, A24T).
- Distinctive residue fact: it is the only one of the seven in which **Leu12 is replaced by proline**
  rather than serine. Leu9-Leu12 is a poly-Leu stretch and humanin L12A abolishes neuroprotective
  activity, so a proline inside that stretch is the substitution least likely to be structurally
  tolerated. Untested, so it is recorded as the strongest available caution rather than as grounds
  for REMOVE - especially since synthetic HN5 with L12S retains activity.
- Pro19-Val20 and Leu9-Leu11 intact; Thr13 and Ser14 intact.
- Expression is the narrowest profile among the seven alongside MTRNR2L7: skeletal muscle and testis
  (UniProt TISSUE SPECIFICITY, from PMID:19477263).
- Literature: PubMed "MTRNR2L6" returns 2 hits, both transcriptomic surveys that merely list the gene
  (an aging muscle transcriptome, a KSHV miRNA target study). Neither tests function; neither cited.
- Actions: 6 rows, all MARK_AS_OVER_ANNOTATED. `core_functions: []`.

## The family, and why these seven reviews look alike

Humanin is a 24-residue peptide encoded by a small open reading frame inside the
mitochondrial 16S rRNA gene MT-RNR2, and it is the member of this family with all the
experimental evidence: cytoprotection, BAX/BID/BIM binding, FPRL1/FPR2 engagement, the
CNTFR-alpha/WSX-1/gp130 receptor complex. Bodzioch et al. 2009 (PMID:19477263, verified -
Genomics 94:247-256) found thirteen MT-RNR2-like sequences in the nuclear genome whose
reading frames would encode humanin-like peptides HN1-HN13
[PMID:19477263 "We provide bioinformatic and expression data suggesting the existence of 13
MT-RNR2-like nuclear loci predicted to maintain the open reading frames of 15 distinct
full-length HN-like peptides."], and showed that at least ten are transcribed and respond to
staurosporine and beta-carotene [PMID:19477263 "At least ten of these nuclear genes are
expressed in human tissues, and respond to staurosporine (STS) and beta-carotene."].

That paper is the single primary source behind every UniProt MTRNR2L entry, and its own
title calls the functionality *potential*. UniProt agrees, and says so in a CAUTION line on
each entry: the active peptide is the product of the mitochondrial gene, and whether any of
the nuclear loci makes a physiologically active peptide is open. A 2022 review restates the
position [PMID:35372353 "It is predicted that these various isoforms might contribute to
differential neuroprotective effects and receptor binding, but their individual roles remain
to be investigated."].

### What the GOA rows actually assert

Each of MTRNR2L1-7 carries the same six rows (MTRNR2L5 has three more):

| term | code | reference | WITH/FROM |
|---|---|---|---|
| GO:0005576 extracellular region | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0243 |
| GO:0005576 extracellular region | ISS | GO_REF:0000024 | UniProtKB:Q8IVG9 |
| GO:0005737 cytoplasm | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0086 |
| GO:0005737 cytoplasm | ISS | GO_REF:0000024 | UniProtKB:Q8IVG9 |
| GO:0048019 receptor antagonist activity | IBA | GO_REF:0000033 | PANTHER:PTN002141596, UniProtKB:Q8IVG9 |
| GO:1900118 neg. reg. execution phase of apoptosis | IBA | GO_REF:0000033 | PANTHER:PTN002141596, UniProtKB:P0CJ72 |

Tracing them:

- Both ISS rows name **UniProtKB:Q8IVG9 = humanin** as donor. Humanin's own extracellular and
  cytoplasm annotations are IDA/EXP, so the donor side is sound.
- Both IEA rows map UniProt's own `SUBCELLULAR LOCATION` lines, and those lines are themselves
  `ECO:0000250|UniProtKB:Q8IVG9` - by similarity to humanin. So the IEA and the ISS are the same
  humanin claim, counted twice.
- Both IBA rows descend from **PANTHER:PTN002141596**, the humanin-family node. The MF row's
  grounding is humanin's IDA for receptor antagonist activity (PMID:15153530, FPRL1 competition
  with amyloid-beta); the BP row's co-listed donor is **UniProtKB:P0CJ72 = MTRNR2L5**, whose own
  evidence is the one functional assay ever run on a nuclear humanin-like sequence.

So the answer to the central question is: with one exception, every row on MTRNR2L1-7 traces to
humanin, by sequence similarity or by phylogenetic descent, and none to an observation made on
the locus itself. The exception is MTRNR2L5, where synthetic HN5 peptide was assayed
[PMID:19477263 "Cytoprotection against the STS-induced apoptosis conferred by the polymorphic HN5
variant, in which threonine in position 13 is replaced with isoleucine, is reduced compared to the
wild type HN5 peptide."].

### Residues: where similarity stops being an argument

Humanin has an unusually complete mutagenesis map (UniProt Q8IVG9). Positions where a single
substitution *abolishes* neuroprotective activity: Pro3, Ser7, Cys8, Leu9, Leu12, Thr13, Ser14,
Pro19. Secretion needs Leu9-Leu11 and Pro19-Val20
[PMID:35372353 "HN was found to be an extracellularly secreted factor whereby two amino acid
structures, Leu9-Leu11, and Pro19-Va120, appear to be essential for the secretion of HN peptide"].
Bodzioch et al. reached the same two positions from the alignment
[PMID:19477263 "Proline vs serine in position 19 may determine whether the peptide is secreted or
not, while threonine in position 13 may be important for cell surface receptor binding."].

Alignment of the seven against humanin (MAPRGFSCLLLLTSEIDLPVKRRA):

| locus | len | identity | substitutions vs humanin | P19 | T13 | S14 | L12 |
|---|---|---|---|---|---|---|---|
| MTRNR2L1 | 24 | 22/24 | L12S A24T | P | T | S | S |
| MTRNR2L2 | 28 | 21/24 | L12S R23L A24L +SSVF | P | T | S | S |
| MTRNR2L3 | 24 | 19/24 | P3T G5R L12S P19S A24I | **S** | T | S | S |
| MTRNR2L4 | 28 | 16/24 | P3T R4Q L12S T13V P19S V20M R23Q A24Y +KQIR | **S** | **V** | S | S |
| MTRNR2L5 | 24 | 19/24 | P3T R4P L12S V20M A24V | P | T | S | S |
| MTRNR2L6 | 24 | 20/24 | A2T L12P I16T A24T | P | T | S | **P** |
| MTRNR2L7 | 24 | 16/24 | P3T R4G S7G T13I S14R P19S R23Q A24I | **S** | **I** | **R** | L |

(computed in this session from the UniProt `SQ` records; Cys8 and Leu9-Leu11 are intact in all seven.)

This is what makes the reviews differ from one another:

- **Pro19 lost** (L3, L4, L7): the secretion claim is actively doubtful, by humanin's own secretion
  determinants and by Bodzioch's position-19 criterion. The two extracellular rows are REMOVEd.
- **Thr13/Ser14 lost** (L4: T13V; L7: T13I + S14R + S7G): the functional rows lose their premise.
  Ser14->Arg is literally one of the humanin substitutions annotated as abolishing activity, so L7's
  two functional rows are REMOVEd. L4 keeps Ser14 and its T13 change parallels the HN5 Thr13->Ile
  variant, which *reduces* rather than abolishes protection, so its functional rows are marked
  over-annotated instead.
- **Everything else**: MARK_AS_OVER_ANNOTATED. Not wrong, not demonstrated, and asserted of a gene
  product that has never been shown to exist.

Note the counterweight that stops this becoming a blanket purge: synthetic HN5, which carries the
same Leu12->Ser substitution as most of the set, *is* cytoprotective. So Leu12 divergence is a
caution, not a refutation, and the family-wide antiapoptotic claim is plausible - just untested
per locus.

### Negative and orthogonal evidence

A lookup across all thirteen loci in CARDIoGRAMplusC4D found no significant association with
coronary artery disease and no significant expression QTL
[PMID:31753007 "None of the found associations were statistically significant after correction for
multiple testing."]. That does not show the loci are inert, but it is the only genetics-scale
evidence covering them.

### Methodological caution that applies to every clinical report on this family

Serum "humanin-like 3" and "humanin-like 10" ELISAs exist and are used
[PMID:41777515 "Humanin-like 3 levels were measured by ELISA in sera of 30 RRMS patients"], and
antibody-based detection of MTRNR2L2 has been reported
[PMID:38221658 "The expression of MIR22, TET3, and MTRNR2L2 in the synovium of patients with RA and
arthritic mice were determined by fluorescence in situ hybridization, quantitative polymerase chain
reaction (qPCR), immunohistochemistry, and Western blot."]. These peptides are 24-28 residues long
and match humanin at 16-22 of 24 positions. Locus-specific immunodetection has not been demonstrated,
so none of these measurements is used here as evidence that a *particular* locus makes a peptide.
