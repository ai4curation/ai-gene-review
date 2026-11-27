# ybjN (P0AAY6, b0853) — curation notes

*E. coli* K-12 YbjN, "putative sensory transduction regulator" (Pfam PF10722 YbjN;
InterPro IPR019660; CDD cd17511 YbjN_AmyR-like). 158 aa, no catalytic motifs,
no transmembrane segment, no signal peptide in the UniProt record.

## Provenance of these notes

**Deep research was unavailable for this gene.** No deep-research API keys are
configured in this container, so `just deep-research` was not run and no
`-deep-research-<provider>.md` file exists. Everything below comes from the
cached publications in `publications/`, from PubMed searches (the complete
PubMed hit list for `ybjN Escherichia coli` is five papers: PMID:38822378,
PMID:28426806, PMID:23028751, PMID:21980417, PMID:16701556), and from the
UniProt flat file.

**The GONUTS wiki could not be consulted.** `https://gowiki.tamu.edu/wiki/index.php/PMID:21980417`
returns only "This site is temporarily offline while we perform upgrades"
(checked 2026-10-29), matching the note in `projects/CACAO.md`. The four CACAO
rows were therefore judged from the paper alone — which is sufficient here,
because the single cited paper (PMID:21980417) has full text cached.

## What is actually known

### It is an enterobacterial orphan gene with no assigned biochemistry

YbjN orthologs are restricted to *Enterobacteriaceae*
[PMID:21980417 "As listed in Table S1, YbjN orthologs are conserved in Enterobacteriaceae."].
The gene sits immediately upstream of the *potFGHI* putrescine transport operon,
with *rimK* and *nfsA* upstream in *E. coli*
[PMID:21980417 "Downstream of the ybjN orthologues is the potFGHI operon, which is predicted to encode a putrescine ABC transport system"].

The one structure of the family, *Erwinia amylovora* AmyR (the functionally
conserved YbjN ortholog), is a homodimer with a class I type III secretion
chaperone-like fold
[PMID:28426806 "The structure of AmyR was solved at 1.95 Å resolution, revealing a class I type III secretion (T3C) chaperone-like fold."],
despite no secretion role; the authors read this as a protein–protein
interaction module rather than an enzyme
[PMID:28426806 "Class I T3C-type proteins such as AmyR are capable of forming very specific interactions with one or more partner proteins."].
Byrne et al. independently note the structural resemblance
[PMID:25049088 "The ybjN gene encodes a protein with structural homology to the DR1245 protein of Deinococcus radiodurans and type III secretion system chaperones"].
Note that the fold is from the *Erwinia* ortholog, not from *E. coli* YbjN
itself, so it is family-level evidence and is not used here to assert a
molecular function.

### Discovery: multicopy suppressor of ts9 (coaA) temperature sensitivity

ybjN was isolated as a multicopy suppressor of the temperature-sensitive
*coaA1* (pantothenate kinase L236F) allele
[PMID:16701556 "ybjN, which encodes a putative sensory transduction regulator"],
and also suppresses *coaA14*, *coaA15* and *ilu-1*, leading the authors to
propose a chaperone/stabilizer role
[PMID:16701556 "general stabilizer for some other unstable proteins"].
This is an over-expression (multicopy) phenotype throughout, and no direct
holdase or stabilizer assay has been reported for YbjN.

Wang et al. confirmed the suppression and showed the *ybjN* transcript is
~10-fold lower in ts9 than in BW25113, and ~10-fold higher than BW when
supplied on a multicopy plasmid (Fig. 1).

### Loss-of-function phenotypes (the solid, annotatable core)

All from Wang et al. 2011 (PMID:21980417), comparing BW25113 (BW), ΔybjN, and
BW carrying multicopy *ybjN*:

- **Fimbriae / type 1 pili (Fig. 3C, 3D).** ΔybjN over-produces fimbriae by
  TEM; multicopy *ybjN* abolishes them
  [PMID:21980417 "Deletion of the ybjN gene led to over-production of fimbriae, and the ybjN mutant produced about three times more fimbriae than that of the BW"]
  [PMID:21980417 "In contrast, no pili were observed on cells over-expressing ybjN."].
  *fimD* (outer-membrane usher) up 8-fold in the mutant, down 12-fold on
  overexpression
  [PMID:21980417 "The fimD gene was up-regulated 8-fold in the ybjN mutant, but it was down-regulated 12-fold in strain over-expressing ybjN as compared to that of the BW"],
  with *fimC*, *fimD*, *fimG* confirmed by microarray
  [PMID:21980417 "Genes encoding major components of bacterial pili including fimC, fimD and fimG were significantly up-regulated in the ybjN mutant, but down-regulated in the ybjN over-expression strain"].
  The authors' conclusion is explicitly a **negative** one
  [PMID:21980417 "These results indicate that YbjN negatively regulated fimbriae formation by suppressing fimbrial gene expression"].
  **This is why the CACAO `GO:0009297 pilus assembly` row has the sign
  inverted: YbjN suppresses pilus formation, it does not build pili.**

- **Motility (Fig. 4A, 4B).** ΔybjN spreads further on 0.25% agar
  [PMID:21980417 "The ybjN mutant exhibited enhanced motility compared with that of the BW strain 12 h following inoculation"],
  0.84 mm (BW) vs 1.88 (ΔybjN) vs 0.41 (overexpression)
  [PMID:21980417 "These results suggest that the YbjN is a negative regulator of bacterial motility in E. coli."].

- **Flagellar gene expression (Fig. 4C, Table 1).** *fliA* and *flgD* up 12.5-
  and 11.3-fold in the mutant
  [PMID:21980417 "Expression of fliA and flgD in the ybjN mutant was up-regulated by 12.5 and 11.3 fold, as compared to that of the BW"],
  with structural/assembly genes following
  [PMID:21980417 "Several FliA controlled genes including flgB, flgD, flgE, fliL and fliM were up-regulated in the ybjN mutant, but down-regulated in the ybjN over-expression strains"]
  [PMID:21980417 "These findings indicate that YbjN negatively regulates flagellar gene expression"].

- **Biofilm (Fig. 6).** Crystal violet on PVC microtitre plates: ΔybjN ~3-fold
  more, overexpression ~half
  [PMID:21980417 "The amount of biofilm formed by the ybjN mutant was much more than that of BW strain, whereas biofilm formation of BW strain with multi-copy plasmids containing ybjN was greatly impaired"]
  [PMID:21980417 "These results indicate that YbjN suppresses normal biofilm formation in E. coli."].

- **Capsule / colanic acid (Fig. 5).** ΔybjN is highly mucoid on 700 mM NaCl
  LB; multicopy *ybjN* makes colonies non-mucoid and also suppresses the
  mucoidy of *ackA* and *ackA/rcsC* mutants
  [PMID:21980417 "These observations indicate that YbjN negatively regulates capsule formation."].
  This phenotype is **not** in GOA and is the one gap worth filling
  (`GO:1901914 negative regulation of capsule organization`). The orthologous
  phenotype in *E. amylovora* is the same sign
  [PMID:23028751 "a mutation of ybjN gene in E. amylovora, an ortholog of E. coli ybjN gene, results in about eight-fold more amylovoran than that of the wild type strain, suggesting that this gene may act as a negative regulator of amylovoran production"].

- **Ionizing radiation.** TraDIS plus direct deletion/survival curves put
  *ybjN* in the mildest validated group
  [PMID:25049088 "The genes in group 1 ( rdgC , ftsP , radA , rsxB , topB , recX , speA , yabI , yhgF , ybjN , tolA , and ompA ) exhibit relatively modest effects when deleted, with a decline in survival of just over an order of magnitude or less at 2,000 Gy."]
  [PMID:25049088 "In three cases ( yabI , yhgF , and ybjN ), elimination of gene function has just a modest effect on IR survival and the genes fall into group 1."].
  So the EcoCyc `response to ionizing radiation` row rests on real
  loss-of-function data, but it is one of several stress survival phenotypes
  rather than the gene's defining role.

- **Independent corroboration of the motility direction** comes from avian
  pathogenic *E. coli*, where loss of FdeC raises motility via YbjN
  down-regulation
  [PMID:38822378 "a protein known to supress motility"].

### Phenotypes seen ONLY on overexpression (do not annotate)

- **Growth.** BW and ΔybjN are indistinguishable; only multicopy *ybjN* slows
  growth
  [PMID:21980417 "both BW and ybjN mutant showed a similar growth curves and growth rate constants for BW and the ybjN mutant were 2.26 and 2.28, respectively, compared to 1.72 for ybjN over-expressing strains grown in LB broth"]
  [PMID:21980417 "These results indicate that over-expression of ybjN slowed bacterial growth in E. coli."],
  with mqsR/ygiT and relE/relB toxin–antitoxin pairs induced 15.8/9.9/5.6/3.1-fold.
  **The CACAO `GO:0030308 negative regulation of cell growth` row therefore has
  no loss-of-function support at all**, and GO's "cell growth" means increase
  in cell size or mass, not population growth rate. Marked over-annotated.
- **Acid susceptibility.** All three strains survive equally at pH 7
  [PMID:21980417 "All three strains exhibited similar survival rate at pH 7.0"];
  only the overexpression strain is killed at pH 2.5
  [PMID:21980417 "The results clearly indicate that over-expressing of ybjN leads to increased acid susceptibility."].
  Not annotated here.

### Interaction data

The only GOA molecular-function row is a bare `GO:0005515 protein binding`
(IntAct IPI, PMID:24561554) with YpjF (Q46953), from the Rajagopala *E. coli*
binary interactome screen; the cached full text does not mention either
protein by name (the pair is in the supplementary interaction tables, and
UniProt records it as `P0AAY6; Q46953: ypjF; NbExp=3`). Suggestive, given that
multicopy *ybjN* induces toxin–antitoxin modules and YpjF is a YpjF/YfjZ-type
toxin, but a Y2H pair is not a molecular function. Removed under the
protein-binding policy (removal does not dispute the interaction).

## Reading for the CACAO audit

Four of the seven GOA rows are CACAO, all IMP from PMID:21980417, all on the
right gene and the right paper with an evidence code that fits the assay. Two
are right (biofilm, flagellum assembly). Two fail:

- `GO:0009297 pilus assembly` — **sign inverted**: the figure shows the mutant
  making *more* fimbriae. GO has no "negative regulation of pilus assembly"
  term, so the row cannot be fixed by substitution; proposed as an NTR.
- `GO:0030308 negative regulation of cell growth` — **overexpression-only
  phenotype annotated as the gene's process**, compounded by a term-sense
  mismatch (cell growth vs population growth rate). This looks like a new
  shape for the taxonomy: not a downstream phenotype of the gene's activity,
  but a phenotype of a dosage artefact that the knockout explicitly does not
  show, carried on an IMP (`ECO:0000315`, mutant phenotype) code.
