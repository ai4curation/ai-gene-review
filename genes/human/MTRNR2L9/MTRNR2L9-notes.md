# MTRNR2L9 curation notes

Journal for the review of MTRNR2L9 (nuclear humanin-like locus). Written 2026-10-04.

## MTRNR2L9 (P0CJ76, humanin-like 9, HN9) - locus-specific notes

- Chromosome 6, at 6q11.1 (the UniProt entry cites the chromosome 6 sequencing paper and lists the
  locus as `Unplaced` in the proteome mapping; the BE/EA GWAS places the flanking marker at 6q11.1
  [PMID:32918910 "1 variant at chromosome 6q11.1 (rs112894788, KHDRBS2-MTRNR2L9, PBONF = .039)"]);
  PE2 (evidence at transcript level); 24 aa `MARRGFSCLLLSTTATDLPVKRRT`.
- **The most divergent of the nuclear loci inside the humanin effector region.** Against humanin
  (`MAPRGFSCLLLLTSEIDLPVKRRA`) HN9 carries six substitutions: Pro3->Arg, Leu12->Ser, Ser14->Thr,
  Glu15->Ala, Ile16->Thr and Ala24->Thr. Three of them (Ser14, Glu15, Ile16) fall in the `SEIDLP`
  stretch, and the alignment that matters is:

  ```
  humanin  MAPRGFSCLLL L TSEIDLP VKRRA
  HN9      MARRGFSCLLL S TTATDLP VKRRT
                 ^       ^  ^^^        ^
  ```

- What is and is not altered, read against humanin's mutagenesis map (UniProt Q8IVG9):
  - **Lost**: Pro3 (humanin `P->A: Abolishes neuroprotective activity`), Leu12 (`L->A: Abolishes
    neuroprotective activity`), Ser14 (`S->A,R,W,E,P: Abolishes neuroprotective activity`; note that
    `S->G` *potentiates* it, so not every substitution at 14 is destructive, and Thr - the residue
    here - was not among those tested).
  - **Retained**: Ser7, Cys8, Leu9-Leu11, Thr13, Asp17, Leu18, **Pro19 and Val20**. Both secretion
    determinants are therefore intact, and so is position 13, the residue Bodzioch et al. flagged for
    cell-surface receptor binding.
  - So HN9's divergence is concentrated in the neuroprotective core but spares the secretion
    determinants - the opposite pattern to MTRNR2L3/L4/L10, which lose Pro19 but keep Ser14.
- Expression: among the broader-expressed members
  [PMID:35372353 "most of the HN-like protein encoding genes are also expressed in testis, whilst
  MTRNR2L1, MTRNR2L8, and MTRNR2L9 are also highly expressed in heart, kidney, and testis"]. UniProt
  records the staurosporine and beta-carotene transcript responses from Bodzioch et al.
- Literature naming this locus: essentially one paper, and it is a genomic-neighbourhood label rather
  than a study of the gene. A sex-stratified GWAS meta-analysis of Barrett's esophagus and esophageal
  adenocarcinoma found one male-specific variant whose nearest-gene annotation is the intergenic
  interval `KHDRBS2-MTRNR2L9`
  [PMID:32918910 "rs112894788, KHDRBS2-MTRNR2L9, PBONF = .039"]. The paper's own discussion does not
  resolve the signal to MTRNR2L9: it names the locus by its two flanking genes and offers no
  functional follow-up for this interval. A nearest-gene label on a single marker in a 6q11.1
  intergenic region, in a pericentromeric neighbourhood, is not evidence that this locus has a
  product or a function, and it supports no GO annotation.
- No peptide. No assay. No interaction. No function has been measured for HN9 in any system.
- Actions: 6 rows, all MARK_AS_OVER_ANNOTATED. `core_functions: []`. No NEW terms: the participation
  test in CLAUDE.md cannot be met by a gene product that has not been shown to exist.
- Why not REMOVE for the functional rows, given three substitutions in the effector region? Because
  the convention established across MTRNR2L1-7 is to remove only where a change matches a humanin
  substitution *annotated as abolishing* (MTRNR2L7's Ser14->Arg) or where it breaks a mapped secretion
  determinant (MTRNR2L3/L4's Pro19->Ser). HN9's Ser14->Thr is a conservative substitution at an
  important position but is not one of the tested abolishing variants, and Ser14->Gly at the same
  position potentiates activity. The honest reading is a strong caution, not a refutation - and the
  rows are objectionable anyway, for the prior reason that no peptide has been shown to exist.

## The family, and why these reviews look alike

Humanin is a 24-residue peptide encoded by a small open reading frame inside the mitochondrial 16S
rRNA gene MT-RNR2, and it is the member of this family with all the experimental evidence:
cytoprotection, BAX/BID/BIM binding, FPRL1/FPR2 engagement, the CNTFR-alpha/WSX-1/gp130 receptor
complex. Bodzioch et al. 2009 (PMID:19477263, verified - Genomics 94:247-256) found thirteen
MT-RNR2-like sequences in the nuclear genome whose reading frames would encode humanin-like peptides
HN1-HN13
[PMID:19477263 "We provide bioinformatic and expression data suggesting the existence of 13
MT-RNR2-like nuclear loci predicted to maintain the open reading frames of 15 distinct full-length
HN-like peptides."], and showed that at least ten are transcribed and respond to staurosporine and
beta-carotene [PMID:19477263 "At least ten of these nuclear genes are expressed in human tissues,
and respond to staurosporine (STS) and beta-carotene."].

That paper is the single primary source behind every UniProt MTRNR2L entry, and its own title calls
the functionality *potential*. UniProt agrees, and says so in a CAUTION line on each entry: the
active peptide is the product of the mitochondrial gene, and whether any of the nuclear loci makes a
physiologically active peptide is open. HGNC classes these loci as pseudogenes ("MT-RNR2 like 9
(pseudogene)"). A 2022 review restates the position [PMID:35372353 "It is predicted that these
various isoforms might contribute to differential neuroprotective effects and receptor binding, but
their individual roles remain to be investigated."].

### What the GOA rows actually assert

MTRNR2L9 carries the same six rows as its siblings:

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
- Both IEA rows map UniProt's own `SUBCELLULAR LOCATION` lines for P0CJ76, and those lines are
  themselves `ECO:0000250|UniProtKB:Q8IVG9` - by similarity to humanin. So the IEA and the ISS are
  the same humanin claim, counted twice.
- Both IBA rows descend from **PANTHER:PTN002141596**, the humanin-family node. The MF row's
  grounding is humanin's IDA for receptor antagonist activity (PMID:15153530, FPRL1 competition with
  amyloid-beta); the BP row's co-listed donor is **UniProtKB:P0CJ72 = MTRNR2L5**, whose own evidence
  is the one functional assay ever run on a nuclear humanin-like sequence
  [PMID:19477263 "Cytoprotection against the STS-induced apoptosis conferred by the polymorphic HN5
  variant, in which threonine in position 13 is replaced with isoleucine, is reduced compared to the
  wild type HN5 peptide."].

Every row on MTRNR2L9 traces to humanin, by sequence similarity or by phylogenetic descent, and none
to an observation made on this locus.

### Residues: where similarity stops being an argument

Humanin has an unusually complete mutagenesis map (UniProt Q8IVG9). Positions where a single
substitution *abolishes* neuroprotective activity: Pro3, Ser7, Cys8, Leu9, Leu12, Thr13, Ser14,
Pro19. Secretion needs Leu9-Leu11 and Pro19-Val20
[PMID:35372353 "HN was found to be an extracellularly secreted factor whereby two amino acid
structures, Leu9-Leu11, and Pro19-Va120, appear to be essential for the secretion of HN peptide"].
Bodzioch et al. reached the same two positions from the alignment
[PMID:19477263 "Proline vs serine in position 19 may determine whether the peptide is secreted or
not, while threonine in position 13 may be important for cell surface receptor binding."].

Set against that map, HN9 loses three mapped positions (Pro3, Leu12, Ser14) and keeps both secretion
segments. The counterweight that stops this becoming a refutation: synthetic HN5, which carries the
same Leu12->Ser substitution, *is* cytoprotective, and Ser14->Gly actually potentiates humanin
activity, so substitution at 14 is not automatically destructive. The conclusion is that the two
functional rows are poorly supported for this locus, not that they are demonstrably false - which is
what MARK_AS_OVER_ANNOTATED is for.

### Negative and orthogonal evidence

A lookup across all thirteen loci in CARDIoGRAMplusC4D found no significant association with
coronary artery disease and no significant expression QTL
[PMID:31753007 "None of the found associations were statistically significant after correction for
multiple testing."]. The BE/EA GWAS signal near this locus (PMID:32918910) is the only positive
human-genetics observation anywhere in its vicinity, and it is an intergenic nearest-gene label on a
single male-specific marker, not an association with the locus itself.

### Methodological caution that applies to every clinical report on this family

HN9 matches humanin at 18 of 24 positions, and matches its sibling nuclear peptides more closely
still. No antibody, ELISA or mass-spectrometry method has been shown to distinguish these peptides,
so no immunoassay of "humanin" or of "humanin-like" peptides can be read as evidence that this locus
makes a peptide. Transcript-level and methylation work can be locus-specific because primers and
probes can be designed against flanking sequence; peptide-level work has not been.
