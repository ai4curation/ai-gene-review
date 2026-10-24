# MTRNR2L10 curation notes

Journal for the review of MTRNR2L10 (nuclear humanin-like locus). Written 2026-10-04.

## MTRNR2L10 (P0CJ77, humanin-like 10, HN10) - locus-specific notes

- Chromosome X (`DR   Proteomes; UP000005640; Chromosome X.`); PE2 (evidence at transcript level);
  24 aa `MTTRGFSCLLLLIREIDLSAKRRI`.
- Against humanin (`MAPRGFSCLLLLTSEIDLPVKRRA`) HN10 carries seven substitutions: Ala2->Thr,
  Pro3->Thr, Thr13->Ile, Ser14->Arg, Pro19->Ser, Val20->Ala and Ala24->Ile:

  ```
  humanin  MAPRGFSCLLLL TS EIDL PV KRRA
  HN10     MTTRGFSCLLLL IR EIDL SA KRRI
            ^^          ^^      ^^    ^
  ```

- This is the **worst-case residue profile in the family**, and it is the profile that drives the
  review. Read against humanin's mutagenesis map (UniProt Q8IVG9):
  - **Ser14->Arg** is literally one of the humanin substitutions annotated as destructive:
    `MUTAGEN 14 /note="S->A,R,W,E,P: Abolishes neuroprotective activity."`
  - **Thr13->Ile** is the one change in this family with a direct measurement: the polymorphic HN5
    variant carrying exactly Thr13->Ile has reduced cytoprotection
    [PMID:19477263 "Cytoprotection against the STS-induced apoptosis conferred by the polymorphic HN5
    variant, in which threonine in position 13 is replaced with isoleucine, is reduced compared to the
    wild type HN5 peptide."]. Position 13 is also the residue Bodzioch et al. flagged for cell-surface
    receptor binding.
  - **Pro19->Ser and Val20->Ala** together alter *both* residues of the second secretion determinant.
    Humanin needs Leu9-Leu11 and Pro19-Val20 for secretion
    [PMID:35372353 "HN was found to be an extracellularly secreted factor whereby two amino acid
    structures, Leu9-Leu11, and Pro19-Va120, appear to be essential for the secretion of HN peptide"],
    and `P->R` and `V->R` each abolish secretion in humanin. Bodzioch et al. reached position 19 from
    the alignment as well [PMID:19477263 "Proline vs serine in position 19 may determine whether the
    peptide is secreted or not, while threonine in position 13 may be important for cell surface
    receptor binding."]. HN10 is the only member of MTRNR2L1-10 that loses both Pro19 *and* Val20.
  - **Pro3->Thr** is a third abolishing position (`P->A: Abolishes neuroprotective activity`).
  - **Retained**: Ser7, Cys8, Leu9-Leu12 (it is one of the few that keep Leu12), Glu15-Leu18.
- So: the secretion claim is positively doubtful (both determinants of the Pro19-Val20 segment
  changed) and the activity claims rest on a sequence that carries one annotated-abolishing
  substitution (Ser14->Arg), one measured activity-reducing substitution (Thr13->Ile) and a third
  abolishing position (Pro3). This is the same situation as MTRNR2L7, which was handled as 2 REMOVE
  (extracellular) + 2 REMOVE (functional IBA) + 2 MARK_AS_OVER_ANNOTATED (cytoplasm), and I follow it.
- Literature naming this locus - two papers, both problematic:
  - **PMID:38630326** (Acta Neurol Belg 2024): microarray of peripheral blood in restless legs
    syndrome, with serum ELISA follow-up for "humanin-like 10" and "humanin-like 3". Two problems.
    First, **circularity**: the genes were picked out of the differential-expression list *by the GO
    term that is itself the propagated IBA under review here*
    [PMID:38630326 "Two genes, MTRNR2L10 and MTRNR2L3, involved negative regulation of the execution
    phase of apoptosis were highlighted in GO analysis."]. Using a GO-term enrichment that exists only
    because of PANTHER propagation from humanin as evidence for that same propagation would be a
    closed loop, and the paper's framing of these loci as "neuroprotective genes" inherits the
    annotation rather than testing it. Second, **assay specificity**: HN10 matches humanin at 17 of 24
    positions and matches its sibling nuclear peptides more closely still; no humanin-like ELISA has
    been shown to discriminate among them, so a reduced "humanin-like 10" serum level
    [PMID:38630326 "their levels, along with CSF-1, linked to neurodegeneration, were reduced in RLS
    patients"] cannot be attributed to this locus. Supports no GO annotation.
  - **PMID:42289503** (J Mol Neurosci 2026): rat status-epilepticus study of an
    "MTRNR2L1/MTRNR2L10 axis" with overexpression and knockdown
    [PMID:42289503 "Ninety SPF SD rats (10 per group) were used"], prioritised from a GEO dataset
    because the genes were annotated to "regulation of signal transduction"
    [PMID:42289503 "the MTRNR2L1/MTRNR2L10 axis is associated with NLRP3 inflammasome-related
    signaling in the cerebral cortex of rats subjected to status epilepticus"]. The human MTRNR2L loci
    are nuclear copies of a mitochondrial rRNA segment; the abstract does not state how the
    corresponding rat sequences were identified, nor how construct specificity among near-identical
    MT-RNR2-derived sequences was established, and the human/rat locus correspondence for these
    pericentromeric insertions is not an obvious one-to-one mapping. Logged with
    `correctness: LOW_QUALITY`, `relevance: LOW`, and used for no annotation. (The same paper is
    logged the same way in the MTRNR2L1 review.)
- No peptide has been detected from this locus by mass spectrometry; no activity, binding partner or
  receptor interaction has been measured for HN10.
- Actions: 6 rows. 4 REMOVE (both GO:0005576 extracellular rows; both IBA functional rows),
  2 MARK_AS_OVER_ANNOTATED (both GO:0005737 cytoplasm rows). `core_functions: []`. No NEW terms: the
  participation test in CLAUDE.md cannot be met by a gene product that has not been shown to exist.

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
physiologically active peptide is open. HGNC classes these loci as pseudogenes ("MT-RNR2 like 10
(pseudogene)"). A 2022 review restates the position [PMID:35372353 "It is predicted that these
various isoforms might contribute to differential neuroprotective effects and receptor binding, but
their individual roles remain to be investigated."].

### What the GOA rows actually assert

MTRNR2L10 carries the same six rows as its siblings:

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
- Both IEA rows map UniProt's own `SUBCELLULAR LOCATION` lines for P0CJ77, and those lines are
  themselves `ECO:0000250|UniProtKB:Q8IVG9` - by similarity to humanin. So the IEA and the ISS are
  the same humanin claim, counted twice.
- Both IBA rows descend from **PANTHER:PTN002141596**, the humanin-family node. The MF row's
  grounding is humanin's IDA for receptor antagonist activity (PMID:15153530, FPRL1 competition with
  amyloid-beta); the BP row's co-listed donor is **UniProtKB:P0CJ72 = MTRNR2L5**, whose own evidence
  is the one functional assay ever run on a nuclear humanin-like sequence.
- Note the loop closed by PMID:38630326: that paper selected MTRNR2L10 for study *because* of the
  GO:1900118 annotation, which exists only by propagation from humanin. The literature on this locus
  is therefore partly downstream of the annotation, which is a reason to be more careful with the
  row, not less.

### Residues: where similarity stops being an argument

Humanin has an unusually complete mutagenesis map (UniProt Q8IVG9). Positions where a single
substitution *abolishes* neuroprotective activity: Pro3, Ser7, Cys8, Leu9, Leu12, Thr13, Ser14,
Pro19. Secretion needs Leu9-Leu11 and Pro19-Val20.

HN10 loses Pro3, Thr13, Ser14, Pro19 and Val20 - five mapped positions, including a substitution
(Ser14->Arg) that UniProt records as abolishing, and a substitution (Thr13->Ile) measured to reduce
cytoprotection in the one nuclear peptide that was ever assayed. The usual counterweight for this
family - synthetic HN5, carrying Leu12->Ser, remains cytoprotective - does not help HN10, because
HN10 keeps Leu12 and diverges instead exactly where HN5 remained humanin-like. That is why this
review removes four rows where most of the siblings only flag them: the inheritance assumption fails
on the target side, not merely for want of confirmation.

### Negative and orthogonal evidence

A lookup across all thirteen loci in CARDIoGRAMplusC4D found no significant association with
coronary artery disease and no significant expression QTL
[PMID:31753007 "None of the found associations were statistically significant after correction for
multiple testing."].

### Methodological caution that applies to every clinical report on this family

Serum "humanin-like 10" is measured by ELISA and reported as reduced in restless legs syndrome
[PMID:38630326 "their levels, along with CSF-1, linked to neurodegeneration, were reduced in RLS
patients"]. HN10 matches humanin at 17 of 24 positions and its siblings more closely; locus-specific
immunodetection has not been demonstrated anywhere in this family, so no such measurement is used
here as evidence that this particular locus makes a peptide.
