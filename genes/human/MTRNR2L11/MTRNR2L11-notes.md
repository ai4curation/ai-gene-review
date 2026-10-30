# MTRNR2L11 curation notes

Journal for the review of MTRNR2L11 (nuclear humanin-like locus). Written 2026-10-04.
Written as a sibling of the completed MTRNR2L1-MTRNR2L7 reviews; the shared family
background below is deliberately consistent with those notes.

## MTRNR2L11 (S4R3Y5, humanin-like 11, HN11) - locus-specific notes

- HGNC:37168, `MT-RNR2 like 11 (pseudogene)`, locus_type `pseudogene`, 1q43 (REST lookup at
  rest.genenames.org, 2026-10-04). Chromosomal position in GRCh37 given as chr1:238107024-238108513
  [PMID:31753007].
- UniProt S4R3Y5 is **PE3, "Inferred from homology"** - unlike MTRNR2L1-L8, which are PE2
  (transcript evidence). This is the single most important locus-specific fact: for L11 there
  is not even transcript-level evidence recorded by UniProt. Consistent with this, Bodzioch et
  al. reported expression for only ten of the thirteen loci
  [PMID:19477263 "At least ten of these nuclear genes are expressed in human tissues, and
  respond to staurosporine (STS) and beta-carotene."], and the later lookup paper states the
  range explicitly
  [PMID:31753007 "The study showed that MTRNR2L1–MTRNR2L10 were expressed variably in most human
  tissues"] - i.e. L11, L12 and L13 are the three loci left out of that statement. (Ensembl
  does list ENSG00000270188 for the locus and Bgee reports testis-biased expression in the
  UniProt cross-references, so the locus is not transcriptionally silent in every dataset; what
  is missing is a published, locus-resolved measurement.)
- 24 aa `MATRGFSCLLLVISEIDLSVKRWV`; 18/24 vs humanin `MAPRGFSCLLLLTSEIDLPVKRRA`
  (computed in this session from the UniProt SQ records): P3T, L12V, **T13I**, **P19S**, R23W, A24V.
- Two of the six substitutions fall on the positions the family's defining paper singled out:
  [PMID:19477263 "Proline vs serine in position 19 may determine whether the peptide is secreted or
  not, while threonine in position 13 may be important for cell surface receptor binding."]
  L11 carries *both* changes - serine at 19 and isoleucine at 13.
- **Pro19->Ser** damages one of the two humanin secretion segments
  [PMID:35372353 "HN was found to be an extracellularly secreted factor whereby two amino acid
  structures, Leu9-Leu11, and Pro19-Va120, appear to be essential for the secretion of HN peptide"].
  Leu9-Leu11 is intact. As in MTRNR2L3, L4 and L7, this makes the extracellular rows positively
  doubtful rather than merely unverified -> REMOVE (both IEA and ISS).
- **Thr13->Ile** is exactly the natural HN5 polymorphism whose effect was measured:
  [PMID:19477263 "Cytoprotection against the STS-induced apoptosis conferred by the polymorphic HN5
  variant, in which threonine in position 13 is replaced with isoleucine, is reduced compared to the
  wild type HN5 peptide."]
  So the one quantitative statement in the literature about this precise substitution says the
  activity is *reduced*, not abolished. That is a strong argument for MARK_AS_OVER_ANNOTATED on the
  two IBA rows and against REMOVE: the inheritance assumption is weakened, measurably, but not
  refuted. Ser14, which humanin needs absolutely, is retained.
- **Leu12->Val** is a conservative change at a position where humanin Leu12->Ala abolishes
  neuroprotective activity (file:human/MT-RNR2__Q8IVG9/MT-RNR2__Q8IVG9-uniprot.txt). Synthetic HN5
  carries the more radical Leu12->Ser and is still cytoprotective [PMID:19477263], so a valine here
  is a caution at most.
- Literature search (PubMed E-utilities, 2026-10-04): `"MTRNR2L11"` returns **0 records**;
  `"humanin-like 11"` returns two records, neither of which is about this human locus
  (PMID:38630326 is a restless-legs-syndrome serum study of humanin-like 3 and 10; PMID:33763338 is
  an expression profile of the mouse gene Gm20594). The only papers that mention the locus at all
  are the two that enumerate all thirteen loci: the defining paper [PMID:19477263] and the CAD
  lookup [PMID:31753007], where the L11 region variants rs202137689 (P = 0.029) and rs12093187
  (P = 0.25) were among those failing correction
  [PMID:31753007 "None of the found associations were statistically significant after correction for
  multiple testing."].
- So there is **no locus-specific evidence of any kind** for MTRNR2L11: no peptide, no transcript
  measurement in a primary paper, no activity assay, no genetic association, no interaction.
- Actions: 2 REMOVE (extracellular, IEA + ISS), 4 MARK_AS_OVER_ANNOTATED (cytoplasm x2, the two
  IBA rows). `core_functions: []`, no NEW terms.

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
the functionality *potential*. UniProt agrees and says so in a CAUTION line on each entry: the
active peptide is the product of the mitochondrial gene, and whether any nuclear locus makes a
physiologically active peptide is open. A 2022 review restates the position
[PMID:35372353 "It is predicted that these various isoforms might contribute to differential
neuroprotective effects and receptor binding, but their individual roles remain to be investigated."].
HGNC classes every one of the thirteen as a pseudogene.

### What the GOA rows on MTRNR2L11 assert

| term | code | reference | WITH/FROM |
|---|---|---|---|
| GO:0005576 extracellular region | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0243 |
| GO:0005576 extracellular region | ISS | GO_REF:0000024 | UniProtKB:Q8IVG9 |
| GO:0005737 cytoplasm | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0086 |
| GO:0005737 cytoplasm | ISS | GO_REF:0000024 | UniProtKB:Q8IVG9 |
| GO:0048019 receptor antagonist activity | IBA | GO_REF:0000033 | PANTHER:PTN002141596, UniProtKB:Q8IVG9 |
| GO:1900118 neg. reg. execution phase of apoptosis | IBA | GO_REF:0000033 | PANTHER:PTN002141596, UniProtKB:P0CJ72 |

Tracing them:

- Both ISS rows name **UniProtKB:Q8IVG9 = humanin** as donor; humanin's own extracellular and
  cytoplasm annotations are IDA/EXP, so the donor side is sound.
- Both IEA rows map UniProt's own `SUBCELLULAR LOCATION` lines, and those lines are themselves
  `ECO:0000250|UniProtKB:Q8IVG9`. So IEA and ISS are the same humanin claim counted twice.
- Both IBA rows descend from **PANTHER:PTN002141596**, the humanin-family node. The MF row's
  grounding is humanin's IDA for receptor antagonist activity (PMID:15153530, FPRL1 competition with
  amyloid-beta); the BP row's co-listed donor is **UniProtKB:P0CJ72 = MTRNR2L5**, whose own evidence
  is the only functional assay ever run on a nuclear humanin-like sequence, and it used synthetic
  HN5 peptide.

Nothing on this gene traces to an observation made on MTRNR2L11.

### Residues: where similarity stops being an argument

Humanin has an unusually complete mutagenesis map (UniProt Q8IVG9). Single substitutions that
*abolish* neuroprotective activity: Pro3, Ser7, Cys8, Leu9, Leu12, Thr13, Ser14 (S14->A,R,W,E,P),
and secretion requires Leu9-Leu11 and Pro19-Val20. HN11 keeps Ser7, Cys8, Leu9-Leu11 and Ser14, and
substitutes Pro3, Leu12 (conservatively), Thr13 and Pro19.

Counterweight that stops this becoming a blanket purge: synthetic HN5, the product of one of these
very nuclear loci and carrying Leu12->Ser, *is* cytoprotective, and the Thr13->Ile form of it still
protects, just less well [PMID:19477263]. So for L11 the functional rows are over-annotations
(asserted of a peptide never shown to exist, with a measurably weakening substitution at position
13), not demonstrable errors.

### Methodological caution for any future clinical report on this locus

Serum ELISAs for "humanin-like" species are used in the clinical literature, and these peptides are
24-28 residues matching humanin at 16-23 of 24 positions. Locus-specific immunodetection has not
been demonstrated for any of them, so no antibody-based measurement should be read as evidence that
MTRNR2L11 in particular makes a peptide. Likewise, RNA-seq reads over a near-identical nuclear copy
of a highly expressed mitochondrial rRNA are a known source of mis-assignment; see the MTRNR2L12
notes for a concrete example.
