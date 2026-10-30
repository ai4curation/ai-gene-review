# BT_3086 (Q8A369) curation notes

## Why this gene, and how it was identified

Curated from a KBase Dark Protein Atlas review request for query
`CAJJOJ010000014.1_29` (https://gene-annotate-dashboard.kbase.us/review/CAJJOJ010000014.1_29),
an 834-aa metagenome-derived *Bacteroides thetaiotaomicron* protein. Its sequence
is 99.5% identical to *B. thetaiotaomicron* VPI-5482 BT_3086 (UniProt Q8A369, also
834 aa; the two differ at a handful of positions), so the curation was done against
that reference entry rather than the contig id. The dashboard's LLM call for the
query was "GH31 endodextranase hydrolyzing dextran and catalyzing transglycosylation
of isomaltooligosaccharides, including IG3 and IG4" with GO:0033904, GO:0016757 and
GO:0016052 proposed.

## What is actually known

- **Genomic context.** BT_3086 sits in PUL48, the *B. thetaiotaomicron* dextran
  utilization locus: "PUL48 comprises a SusD-like surface-associated nutrient-binding
  protein (BT3089), a SusC-like TonB-dependent importer protein (BT3090), a SusR-like
  sensor-regulator protein (BT3091), and two GHs: α-glucosidase II (BT3086) and
  dextranase (BT3087)" [PMID:38376161 full text, PMC10936149].
- **Direct experimental data on BT_3086 itself** comes only from Wong et al. 2024
  [PMID:38376161]: recombinant BT3086 "produced glucose and isomaltose as major
  degradation products", the ΔBT3086 mutant shows only a "marginal growth defect" on
  dextran, and BT3086 and BT4581 "play import roles in liberating glucose from
  dextran—oligosaccharides" while BT3087 is "the key GH for the initial debranching".
  The cached publication record is abstract-only; these statements were read from the
  Europe PMC full text and are quoted here, not in `supported_by`.
- **The characterized ortholog.** *Flavobacterium johnsoniae* FjDex31A (Fjoh_4430,
  A5FBI1) is a GH31 dextranase: it "hydrolyzed dextran and pullulan to produce
  isomaltooligosaccharides and isopanose" and did *not* act on "trehalose, kojibiose,
  nigerose, maltose, maltotriose, or soluble starch" [PMID:27170214]. Its crystal
  structures [PMID:31552702] show a four-domain GH31 fold whose active site, outside
  subsite -1, "is markedly different from that of other GH31 enzymes", with Gly273,
  Tyr524, Trp376 and Leu308-cisGln309 "especially unique to FjDex31A"; mutating Gly273
  or Tyr524 reduced hydrolysis of dextran, pullulan and isomaltose.
- **Locus conservation.** FjDexUL and homologous GH66+GH31 loci occur across
  Bacteroidota including *B. thetaiotaomicron* VPI-5482 [PMID:37269952], and in such
  loci the GHs with type I signal peptides are periplasmic — "FjDex31A, FjGH97A, and
  FjGH65A are likely periplasmic" [PMID:37269952].

## Own analysis

`BT_3086-bioinformatics/residue_check.py` (reproducible; sequences fetched from
UniProt) gives 64.5% identity over 830 aligned positions between Q8A369 and A5FBI1,
and finds all six FjDex31A positions of interest conserved in BT_3086: G273→G271,
L308→L306, Q309→Q307, W376→W374, D412→D410 (catalytic nucleophile position, the
D412A mutant used for the substrate complex) and Y524→Y522. So BT_3086 is not merely
a GH31 family member but carries the specific subsite -2 architecture that
distinguishes the dextranase from exo-acting GH31 α-glucosidases. This is the main
argument against the inherited "alpha-glucosidase II" name.

## Curation decisions

- Both GO:0004553 rows (IBA from PTHR22762/PTN000509739, IEA from InterPro
  IPR000322) are sound but family-level; MODIFY. The IBA node's seeds are eukaryotic
  GH31 alpha-glucosidases, which is why it stops at the family property - a granularity
  issue, not a bad propagation.
- **The MODIFY target is a proposed term, not GO:0033904.** The first draft of this
  review used GO:0033904 dextranase activity, which is wrong in a way worth recording:
  that term is defined as the *endo*hydrolysis of 1,6-alpha-D-glucosidic linkages, so
  asserting it commits to a cleavage mode that the same review's `reason` called
  unresolved. The alternative, GO:0043896 glucan 1,6-alpha-glucosidase activity, has a
  mechanism-neutral definition text but is the name of exo-acting EC 3.2.1.70, so it
  commits the other way. GO has no common parent that asserts only the linkage and the
  substrate, so this review proposes `alpha-1,6-glucan hydrolase activity` (see
  `proposed_new_terms`) and uses `proposed_molecular_function` with
  `molecular_function` unset, per the repo convention for an activity with no GO term.
  The previously drafted NEW GO:0033904 (ISS) row was dropped for the same reason.
- **Why the cleavage mode is genuinely open.** The six conserved FjDex31A residues
  include the subsite -2 pair (G273/Y524 in FjDex31A numbering). A productive subsite
  -2 excludes a classic single-glucose alpha-glucosidase pocket, which is what kills the
  "alpha-glucosidase II" name - but it does not discriminate endo from exo, because an
  exo enzyme releasing the *disaccharide* isomaltose also needs -2/-1 (cf. beta-amylase
  releasing maltose). BT_3086's reported products are glucose **and isomaltose**.
  Further, Wong's product data is an overnight endpoint digest ("dextran medium treated
  overnight"), and an endo enzyme run to completion also arrives at small products; and
  FjDex31A "produced glucose from the initial stage of the reaction when
  isomaltooligosaccharides were used as substrates" while also transglycosylating, so
  product spectra are a weak mechanistic readout for this enzyme class. Note Wong et al.
  are themselves internally inconsistent: their introduction lists GH31 among the
  *endo*dextranase families ("GH families 31, 49, and 66") and omits it from the exo
  list ("13, 15, 27, and 49"), then calls BT3086's products "consistent with products
  formed by exodextranases (GH31)". Pathway position (periplasmic, downstream of
  BT3087, "liberating glucose from dextran-oligosaccharides") argues exo; the ortholog's
  structure argues endo. Neither is assertable yet.
- GO:0005975 carbohydrate metabolic process → MODIFY to GO:0000272 polysaccharide
  catabolic process. GO has **no dextran catabolic process term** (checked via OLS);
  that gap is noted here rather than as a `proposed_new_terms` entry, since
  GO:0000272 covers the claim adequately.
- GO:0030246 carbohydrate binding → MARK_AS_OVER_ANNOTATED. The IPR011013 mapping is
  the N-terminal β-sandwich of the GH31 catalytic unit (part of the four-domain fold
  seen in the FjDex31A structures), not a CBM; catalytic-site substrate binding is
  part of the hydrolase activity.
- NEW rows: GO:0042597 periplasmic space (IC from the SignalP type I signal peptide
  1-22 with no TM helix or lipobox, plus the PUL convention that GHs with type I
  signal peptides act in the periplasm), GO:0000272 (IC, the MODIFY target). No NEW
  molecular-function row: the activity is carried by the proposed term above.

## Open points

- **Endo versus exo is unresolved**, as set out under Curation decisions. Resolving it
  is what the first `suggested_experiment` is for (time-course kinetics plus
  reducing-end assays, which separate the two where endpoint products do not), and it
  is also what would let the proposed term be replaced by GO:0033904 or GO:0043896.
- **Transglycosylation (GO:0016757) was not asserted.** FjDex31A has high
  transglucosylation activity [PMID:27170214, PMID:37269952], but no transglycosylation
  assay has been reported for BT_3086, and glycosyltransferase activity for a GH31
  retaining hydrolase is a side reaction of the same catalytic machinery rather than a
  separate function. Transferring it on 64% identity alone would over-annotate; this
  is the one place where the dashboard's call goes beyond what the evidence carries.
- The dashboard's GO:0016052 carbohydrate catabolic process is a reasonable call; this
  review uses the more specific GO:0000272 polysaccharide catabolic process, since the
  substrate is a polysaccharide.
