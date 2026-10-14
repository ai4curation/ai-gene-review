# MTRNR2L13 curation notes

Journal for the review of MTRNR2L13 (nuclear humanin-like locus). Written 2026-10-04.
Written as a sibling of the completed MTRNR2L1-MTRNR2L7 reviews; the shared family background is
kept consistent with those notes and summarised at the end of this file.

## MTRNR2L13 (S4R3P1, humanin-like 13, HN13) - locus-specific notes

- HGNC:37170, `MT-RNR2 like 13 (pseudogene)`, locus_type `pseudogene`, 4q26 (REST lookup at
  rest.genenames.org, 2026-10-04). GRCh37 position chr4:117220016-117221478 [PMID:31753007].
  UniProt S4R3P1 is **PE3, "Inferred from homology"** - like L11 and L12, and unlike L1-L8, there is
  no recorded transcript-level evidence. Bodzioch et al. reported expression for ten of the thirteen
  loci [PMID:19477263 "At least ten of these nuclear genes are expressed in human tissues, and respond
  to staurosporine (STS) and beta-carotene."], and the later lookup gives the range explicitly
  [PMID:31753007 "The study showed that MTRNR2L1–MTRNR2L10 were expressed variably in most human
  tissues"], leaving L11-L13 out. (Ensembl ENSG00000270394 exists and the Bgee cross-reference in the
  UniProt entry reports testis-biased expression, so the locus is not silent in every dataset; what is
  missing is a published, locus-resolved measurement.)
- 24 aa `MDTQGFSCLLLLISEIDLSVKRRI`; 18/24 vs humanin `MAPRGFSCLLLLTSEIDLPVKRRA`
  (computed in this session from the UniProt SQ records): A2D, P3T, R4Q, **T13I**, **P19S**, A24I.
- Residues retained: Ser7, Cys8, Leu9-Leu11, **Leu12** (one of only two of the thirteen reviewed so
  far to keep it) and Ser14. Residues lost that humanin needs: Pro3 (humanin P3A abolishes activity),
  Thr13, Pro19.
- The two decisive changes are the same pair the defining paper singled out
  [PMID:19477263 "Proline vs serine in position 19 may determine whether the peptide is secreted or
  not, while threonine in position 13 may be important for cell surface receptor binding."]:
  - **Pro19->Ser** damages one of the two humanin secretion segments
    [PMID:35372353 "HN was found to be an extracellularly secreted factor whereby two amino acid
    structures, Leu9-Leu11, and Pro19-Va120, appear to be essential for the secretion of HN peptide"],
    so the extracellular rows, which exist only by transfer from humanin, are contradicted by the
    source paper's own criterion -> REMOVE (both IEA and ISS). Same decision as L3, L4, L7 and L11.
  - **Thr13->Ile** is precisely the natural HN5 polymorphism whose effect was measured
    [PMID:19477263 "Cytoprotection against the STS-induced apoptosis conferred by the polymorphic HN5
    variant, in which threonine in position 13 is replaced with isoleucine, is reduced compared to the
    wild type HN5 peptide."].
    Reduced, not abolished - so the two IBA rows are MARK_AS_OVER_ANNOTATED, not REMOVE. This is the
    same reading as for L11, and it is the reason L13 is treated less harshly than L7, whose Ser14->Arg
    is on the list of humanin substitutions that abolish activity outright.
- The N-terminal Ala2->Asp is unique among the loci examined. Humanin tolerates deletion of residues
  1-2 without loss of neuroprotective activity, while deletion of 1-3 abolishes it
  (file:human/MT-RNR2__Q8IVG9/MT-RNR2__Q8IVG9-uniprot.txt), so position 2 is probably not critical;
  the loss of Pro3 in the same region is the more consequential change.
- Literature (PubMed E-utilities, 2026-10-04): `"MTRNR2L13"` returns 2 records, both of which are the
  papers that enumerate the whole family (PMID:31753007 and the humanin review PMID:35372353).
  `"humanin-like 13"` returns 5, none about this human locus - a tick mitogenome paper
  (PMID:41758291), a serum mtDNA study (PMID:41282786), buffalo sperm humanin-like immunoreactivity
  (PMID:36183493), a mouse Gm20594 expression profile (PMID:33763338), plus PMID:31753007 again.
  So there is **no locus-specific publication** for MTRNR2L13.
- Genetics: the CAD lookup found the L13 region variant rs78083998 to be the top within-gene variant
  of all thirteen loci (meta-analysis P = 0.042), and rs10020248 at P = 0.013, but
  [PMID:31753007 "None of the found associations were statistically significant after correction for
  multiple testing."]
  That is the only genetics-scale evidence touching this locus, and it is negative.
- Actions: 2 REMOVE (extracellular, IEA + ISS), 4 MARK_AS_OVER_ANNOTATED (cytoplasm IEA + ISS, the
  two PANTHER IBA rows). `core_functions: []`, no NEW terms.

## The family, and why these reviews look alike

Humanin is a 24-residue peptide encoded by a small open reading frame inside the mitochondrial 16S
rRNA gene MT-RNR2, and it is the member of this family with all the experimental evidence:
cytoprotection, BAX/BID/BIM binding, FPRL1/FPR2 engagement, the CNTFR-alpha/WSX-1/gp130 receptor
complex. Bodzioch et al. 2009 (PMID:19477263, PubMed-verified, Genomics 94:247-256) found thirteen
MT-RNR2-like sequences in the nuclear genome whose reading frames would encode humanin-like peptides
HN1-HN13
[PMID:19477263 "We provide bioinformatic and expression data suggesting the existence of 13
MT-RNR2-like nuclear loci predicted to maintain the open reading frames of 15 distinct full-length
HN-like peptides."].
That paper is the single primary source behind every UniProt MTRNR2L entry, and its own title calls
the functionality *potential*. UniProt says the same in a CAUTION line on each entry: the active
peptide is the product of the mitochondrial gene, and whether any nuclear locus makes a
physiologically active peptide is open. A 2022 review restates the position
[PMID:35372353 "It is predicted that these various isoforms might contribute to differential
neuroprotective effects and receptor binding, but their individual roles remain to be investigated."].
HGNC classes all thirteen as pseudogenes.

### What the GOA rows on MTRNR2L13 assert

| term | code | reference | WITH/FROM |
|---|---|---|---|
| GO:0005576 extracellular region | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0243 |
| GO:0005576 extracellular region | ISS | GO_REF:0000024 | UniProtKB:Q8IVG9 |
| GO:0005737 cytoplasm | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0086 |
| GO:0005737 cytoplasm | ISS | GO_REF:0000024 | UniProtKB:Q8IVG9 |
| GO:0048019 receptor antagonist activity | IBA | GO_REF:0000033 | PANTHER:PTN002141596, UniProtKB:Q8IVG9 |
| GO:1900118 neg. reg. execution phase of apoptosis | IBA | GO_REF:0000033 | PANTHER:PTN002141596, UniProtKB:P0CJ72 |

- Both ISS rows name **UniProtKB:Q8IVG9 = humanin**; humanin's own extracellular and cytoplasm
  annotations are IDA/EXP, so the donor side is sound.
- Both IEA rows map UniProt's own `SUBCELLULAR LOCATION` lines, themselves
  `ECO:0000250|UniProtKB:Q8IVG9`. So IEA and ISS are the same humanin claim counted twice.
- Both IBA rows descend from **PANTHER:PTN002141596**, the humanin-family node. The MF row's
  grounding is humanin's IDA for receptor antagonist activity (PMID:15153530, FPRL1 competition with
  amyloid-beta); the BP row's co-listed donor is **UniProtKB:P0CJ72 = MTRNR2L5**, whose evidence is
  the one functional assay ever run on a nuclear humanin-like sequence, using synthetic HN5 peptide.

Nothing on this gene traces to an observation made on MTRNR2L13. Note in passing that this locus,
with six substitutions from humanin, carries the IBA rows while MTRNR2L12, which differs from humanin
at one position, does not - the rows track PANTHER subfamily membership rather than sequence
similarity.

### Residues: where similarity stops being an argument

Humanin has an unusually complete mutagenesis map (UniProt Q8IVG9). Single substitutions that
*abolish* neuroprotective activity: Pro3, Ser7, Cys8, Leu9, Leu12, Thr13, Ser14 (S14->A,R,W,E,P);
secretion requires Leu9-Leu11 and Pro19-Val20. HN13 keeps Ser7, Cys8, Leu9-Leu12 and Ser14 and loses
Pro3, Thr13 and Pro19.

The counterweight that stops this becoming a blanket purge: synthetic HN5, the product of one of
these very nuclear loci, is cytoprotective, and its Thr13->Ile form - the same substitution HN13
carries - still protects, just less well [PMID:19477263]. So the functional rows here are
over-annotations (asserted of a peptide never shown to exist, with a measurably weakening
substitution at 13), not demonstrable errors; while the secretion-dependent rows are positively
doubtful and are removed.

### Methodological caution for any future report on this locus

Serum ELISAs for "humanin-like" species are used in the clinical literature and these peptides match
humanin at 16-23 of 24 positions; locus-specific immunodetection has not been demonstrated for any
member of the family. Likewise, short-read RNA-seq cannot resolve a nuclear copy of a highly abundant
mitochondrial rRNA segment from its siblings or its parent locus without dedicated controls. No
antibody- or short-read-based measurement should be read as evidence that MTRNR2L13 in particular
makes a peptide.
