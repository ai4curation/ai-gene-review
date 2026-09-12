# Rat Arsb (P50430) — review notes

## Scope

This review is prompted by geneontology/go-annotation#6467, where Val
questioned the RGD-authored autophagy annotation on rat Arsb sourced from
PMID:8037 (a 1976 Biochem J paper by Sanghavi & Koenig, "Autophagy-related
changes of arylsulphatases A and B in rat liver lysosomes").

The concern raised in the issue: the abstract describes autophagy-related
**changes to arylsulphatases A and B** (they are targets/substrates of
autophagic processing), not a role for the enzymes **in** autophagy.

## Gene identity

- UniProt: [P50430](https://www.uniprot.org/uniprotkb/P50430/entry) (ARSB_RAT)
- Rat Arsb, ~80/85% nt/aa identity to human ARSB (PMID:8575749)
- Rat chromosome 2; MPR rat colony carries a homozygous 507insC frameshift
  that causes an MPS VI phenotype (PMID:8575749)
- EC 3.1.6.12 — N-acetylgalactosamine-4-sulfatase (arylsulfatase B)
- Ortholog of well-characterised human ARSB (P15848); see
  [genes/human/ARSB/ARSB-ai-review.yaml](../../human/ARSB/ARSB-ai-review.yaml)
  for a full annotation review of the human ortholog.

## Function

Rat Arsb is the mammalian ortholog of human ARSB — a lysosomal sulfohydrolase
that removes 4-sulfate groups from N-acetylgalactosamine-4-sulfate residues in
dermatan sulfate and chondroitin-4-sulfate glycosaminoglycan chains. Requires
Ca(2+) cofactor and a post-translationally generated formylglycine (from Cys)
for activity. Loss of function causes lysosomal accumulation of GAGs (MPS VI).

Beyond the classical lysosomal role, rat Arsb has been detected at the plasma
membrane of hepatocytes, sinusoidal endothelial cells, and Kupffer cells,
colocalising with heparan sulfate proteoglycan
[PMID:19536613 "we show that mammalian ARSA and ARSB exist on the cell
surface of sinusoidal endothelial cells, hepatocytes, and sinusoidal
macrophages (Kupffer cells), as well as in the lysosome"].

Rat Arsb (via astrocytes) modulates neurite outgrowth by controlling
chondroitin-4-sulfate and neurocan levels
[PMID:24311516 "ARSB modulates sulfated GAG and neurocan levels in
astrocytes and astrocyte-mediated neurite outgrowth in cocultured neurons"].

## The PMID:8037 autophagy annotation (issue #6467)

Sanghavi & Koenig (1976) measured total arylsulphatase activity and the
relative activities of the A and B forms in liver of control rats and rats
subjected to treatments that provoke hepatic autophagocytosis (starvation,
sham/subtotal hepatectomy, glucagon + starvation). Key finding
[PMID:8037 abstract, "the A form is more rapidly converted into the B form
during autophagy, owing to the digestive activity of the other lysosomal
hydrolases present in autophagic vacuoles"].

- The paper describes arylsulphatases A and B as **cargo/substrates** whose
  processing state (A→B conversion) shifts during enhanced autophagocytosis
  in liver lysosomes.
- It does **not** provide evidence that Arsb itself has a functional role in
  the autophagy process (e.g. autophagosome formation, cargo selection,
  membrane dynamics, lysosome fusion, or bulk autophagic flux).
- Val's concern in geneontology/go-annotation#6467 is well-founded from the
  abstract; the observation is autophagy-associated, not autophagy-effector.

Recommended action in the review: `MARK_AS_OVER_ANNOTATED` (rather than
`REMOVE`) because:
1. Only the abstract is available — the full text may contain further data.
2. The GO curator community is actively adjudicating this via issue #6467.
3. `MARK_AS_OVER_ANNOTATED` correctly signals that the propagation to the
   human ortholog (already flagged for `REMOVE` in the human ARSB review) is
   unlikely to be biologically meaningful, without overruling the original
   experimental annotator's full-text access.

## Other IDA annotations (rat-specific rationale)

- **GO:0007584 response to nutrient (PMID:2290353)** — Ferland et al. 1990
  measured Arsb activity in aged rats under dietary restriction. Finding:
  Arsb activity increases with age; dietary restriction elevates Arsb (and
  β-galactosidase, cathepsin D) activity in Kupffer/endothelial cells
  [PMID:2290353 "Rats exposed to dietary restriction (R) showed higher
  activities of beta-galactosidase, arylsulfatase B and cathepsin D"]. This
  is an expression/activity change in response to dietary state, not
  evidence that Arsb is a component of a nutrient-response pathway.
  → `MARK_AS_OVER_ANNOTATED`.

- **GO:0009268 response to pH (PMID:6137211)** — O'Fagain et al. 1983 is a
  biophysical characterisation of rat liver arylsulphatase kinetics vs pH
  [PMID:6137211 "The effect of pH on the kinetics of rat liver
  arylsulphatases A and B is very similar and shows that two groups with pK
  values of 4.4-4.5 and 5.7-5.8 are important for enzyme activity"]. This
  measures enzyme pH dependence (a property of the catalytic mechanism),
  not a biological "response to pH" process.
  → `REMOVE` (the annotation misinterprets an enzyme kinetics measurement
  as a biological process).

- **GO:0043627 response to estrogen (PMID:15040)** — Zachariah & Moudgal
  1977 show cervical Arsb activity is induced by estradiol in ovariectomised
  rats [PMID:15040 "A single subcutaneous injection of 0-02 microng
  oestradiol-17beta/rat increased the especific activity of arylsulphatase A
  and B ... Cycloheximide prevented the rise in arylsulphatase B activity
  occurring after oestrogen injection, suggesting a regulation of cervical
  arylsulphatase B at the level of protein biosynthesis"]. This is
  cervical-tissue-specific hormonal upregulation of enzyme expression, not
  a broadly applicable core function of Arsb.
  → `KEEP_AS_NON_CORE`.

- **GO:0051597 response to methylmercury (PMID:1682910)** — Vinay & Sood
  1991 report that methylmercury inhibits CNS arylsulfatase activity, and
  that thiol antagonists (NAHT, GSH) fail to restore it [PMID:1682910 "a
  dose and duration dependent inhibition of the enzymes ... none of the
  antagonists restored the enzymes significantly"]. The annotation captures
  that Arsb is **inhibited by** methylmercury (a chemical toxicology
  observation), not that Arsb is part of a "response to methylmercury"
  biological process.
  → `REMOVE`.

- **GO:0009986 cell surface (PMID:19536613, IDA)** — Solid experimental
  support for cell-surface localisation on liver sinusoidal endothelial
  cells, hepatocytes, and Kupffer cells. → `KEEP_AS_NON_CORE` (non-core
  because lysosome is the primary functional compartment, but this is a
  genuine and reproducible extra-lysosomal localisation).

- **GO:0008484 sulfuric ester hydrolase activity (PMID:2884099, IDA)** —
  Thompson & Daniel 1987 showed rat Arsb hydrolyses ascorbic acid-2-sulfate
  (in addition to the classical aryl sulfate substrates)
  [PMID:2884099 "arylsulfatase B hydrolyzed ascorbic acid-2-sulfate at
  0.6% the p-nitrocatechol sulfate rate"]. Supports the sulfatase MF.
  → `ACCEPT`.

- **GO:0010976 positive regulation of neuron projection development (IMP,
  PMID:24311516)** — Zhang et al. 2014 showed Arsb silencing in astrocytes
  reduces neurite outgrowth in cocultured neurons, and rArsb supplementation
  rescues ethanol-induced defects [PMID:24311516 "ARSB silencing increased
  the levels of sulfated GAGs, C4S, and neurocan in astrocytes and
  inhibited neurite outgrowth in cocultured neurons"]. → `KEEP_AS_NON_CORE`
  (a bona fide, mechanistically supported non-core role in the CNS).

- **GO:0004065 arylsulfatase activity (PMID:8575749, TAS)** — Kunieda et
  al. 1995 cloned rat Arsb cDNA and identified the causative MPS VI
  mutation, confirming its arylsulfatase identity [PMID:8575749 "MPS type
  VI, the lysosomal storage disorder caused by the deficiency of
  arylsulfatase B (ARSB) activity, occurs in humans, cats, and rats"].
  → `ACCEPT`.

## Approach to the ISO/IEA propagated annotations

Many rat annotations are ISO from human/mouse via GO_REF:0000121 (RGD ISO
annotations to rat from other mammalian species). Where the human ortholog
has well-supported experimental evidence for the same term (e.g. dermatan
sulfate proteoglycan catabolic process, chondroitin sulfate proteoglycan
catabolic process, N-acetylgalactosamine-4-sulfatase activity, lysosome,
regulation of epithelial cell migration), the ISO annotation is
`ACCEPT`ed. Where the human annotation is over-annotated or ISO-back-and-
forth to weak evidence, we track the human review's disposition.
