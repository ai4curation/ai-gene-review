# MTRNR2L8 curation notes

Journal for the review of MTRNR2L8 (nuclear humanin-like locus). Written 2026-10-04.

## MTRNR2L8 (P0CJ75, humanin-like 8, HN8) - locus-specific notes

- Chromosome 11 (`DR   Proteomes; UP000005640; Chromosome 11.`); PE2 (evidence at transcript level);
  24 aa `MAPRGFSCLLLSTSEIDLPVKRRA`.
- **The closest of all the nuclear loci to humanin: 23/24 identical.** The only difference from
  humanin (`MAPRGFSCLLLLTSEIDLPVKRRA`) is Leu12->Ser. Pro3, Ser7, Cys8, Leu9-Leu11, Thr13, Ser14,
  Pro19 and Val20 - every position humanin needs for neuroprotection or for secretion - are intact,
  and so is the C-terminal Ala24. If any of the thirteen nuclear loci encodes a peptide that behaves
  like humanin, HN8 is the single best candidate on sequence grounds. That is an argument for doing
  the experiment, not for annotating its outcome: no HN8 peptide has ever been detected.
- Expression: among the broadest of the family
  [PMID:35372353 "most of the HN-like protein encoding genes are also expressed in testis, whilst
  MTRNR2L1, MTRNR2L8, and MTRNR2L9 are also highly expressed in heart, kidney, and testis"].
  UniProt records for this locus that it is not expressed in skeletal muscle
  (`Not expressed in skeletal muscle. {ECO:0000269|PubMed:19477263}`), and that the transcript is
  down-regulated 6 h and up-regulated 24 h after staurosporine.
- MTRNR2L8 is the most-cited member of the family after humanin itself, but every citation is at the
  level of transcript abundance or promoter methylation, never peptide:
  - Hyperoxia before coronary artery bypass grafting raises its myocardial transcript
    [PMID:26769839 "including upregulation of two different humanins - MTRNR2L2 and MTRNR2L8"].
    An RNA-seq differential-expression hit in 24 patients; the paper reports no peptide measurement,
    and the "cell survival" network is an Ingenuity annotation enrichment, not an assay.
  - Its promoter is hypomethylated in large-artery atherosclerotic stroke
    [PMID:31084332 "We identified a differentially methylated region in the promoter of a humanin gene"],
    replicated in two cohorts and proposed as a diagnostic marker. This is evidence that the locus is
    regulated, which supports transcription; it says nothing about translation or function.
- Neither paper licenses any GO annotation: a differentially expressed or differentially methylated
  transcript is not a molecular function, and GO does not annotate response-to-stimulus from a
  microarray/RNA-seq expression change alone.
- Actions: 6 rows, all MARK_AS_OVER_ANNOTATED. `core_functions: []` - nothing is established for this
  gene product. No NEW terms: the participation test in CLAUDE.md cannot be met by a gene product
  that has not been shown to exist.

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
physiologically active peptide is open. HGNC classes these loci as pseudogenes ("MT-RNR2 like 8
(pseudogene)"). A 2022 review restates the position [PMID:35372353 "It is predicted that these
various isoforms might contribute to differential neuroprotective effects and receptor binding, but
their individual roles remain to be investigated."].

### What the GOA rows actually assert

MTRNR2L8 carries the same six rows as its siblings:

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
- Both IEA rows map UniProt's own `SUBCELLULAR LOCATION` lines for P0CJ75, and those lines are
  themselves `ECO:0000250|UniProtKB:Q8IVG9` - by similarity to humanin. So the IEA and the ISS are
  the same humanin claim, counted twice.
- Both IBA rows descend from **PANTHER:PTN002141596**, the humanin-family node. The MF row's
  grounding is humanin's IDA for receptor antagonist activity (PMID:15153530, FPRL1 competition with
  amyloid-beta); the BP row's co-listed donor is **UniProtKB:P0CJ72 = MTRNR2L5**, whose own evidence
  is the one functional assay ever run on a nuclear humanin-like sequence
  [PMID:19477263 "Cytoprotection against the STS-induced apoptosis conferred by the polymorphic HN5
  variant, in which threonine in position 13 is replaced with isoleucine, is reduced compared to the
  wild type HN5 peptide."].

So every row on MTRNR2L8 traces to humanin, by sequence similarity or by phylogenetic descent, and
none to an observation made on this locus.

### Residues: where similarity stops being an argument

Humanin has an unusually complete mutagenesis map (UniProt Q8IVG9). Positions where a single
substitution *abolishes* neuroprotective activity: Pro3, Ser7, Cys8, Leu9, Leu12, Thr13, Ser14,
Pro19. Secretion needs Leu9-Leu11 and Pro19-Val20
[PMID:35372353 "HN was found to be an extracellularly secreted factor whereby two amino acid
structures, Leu9-Leu11, and Pro19-Va120, appear to be essential for the secretion of HN peptide"].
Bodzioch et al. reached the same two positions from the alignment
[PMID:19477263 "Proline vs serine in position 19 may determine whether the peptide is secreted or
not, while threonine in position 13 may be important for cell surface receptor binding."].

HN8 vs humanin: **Leu12->Ser, and nothing else.** Humanin Leu12->Ala abolishes neuroprotective
activity, so this is not a silent change - but synthetic HN5, which carries the same Leu12->Ser
substitution, is still cytoprotective [PMID:19477263], so Leu12->Ser is a caution rather than a
refutation. There is therefore no residue-level argument against any of the six rows here, which is
why all six are marked over-annotated rather than removed: what is wrong with them is not that they
are implausible but that they are assertions about the humanin sequence rather than observations
about this gene product, and the gene product itself has never been shown to exist.

### Negative and orthogonal evidence

A lookup across all thirteen loci in CARDIoGRAMplusC4D found no significant association with
coronary artery disease and no significant expression QTL
[PMID:31753007 "None of the found associations were statistically significant after correction for
multiple testing."]. Note the tension with PMID:31084332: an epigenome-wide study finds a
replicated MTRNR2L8 promoter methylation difference in atherosclerotic stroke, while the
targeted genetic lookup finds nothing at the sequence level in coronary artery disease. Both can be
true, and neither speaks to a peptide.

### Methodological caution that applies to every clinical report on this family

HN8 matches humanin at 23 of 24 positions. No antibody, ELISA or mass-spectrometry method has been
shown to distinguish HN8 from humanin, so no immunoassay of "humanin" or of "humanin-like" peptides
in blood or tissue can be read as evidence that this locus makes a peptide - and conversely, part of
what is reported as circulating humanin could in principle come from here. Transcript-level work
(PMID:26769839, PMID:31084332) is locus-specific because primers and CpG probes can be designed
against the flanking sequence; peptide-level work is not.
