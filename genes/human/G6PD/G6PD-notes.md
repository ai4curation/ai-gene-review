# G6PD (human, P11413) review notes

## Summary of verified biology

G6PD is **glucose-6-phosphate dehydrogenase** (EC 1.1.1.49), the committed, rate-limiting
first enzyme of the **oxidative branch of the pentose phosphate pathway (PPP / hexose
monophosphate shunt)**. It oxidises **D-glucose-6-phosphate to 6-phospho-D-glucono-1,5-lactone,
reducing NADP+ to NADPH** (Rhea:RHEA:15841). It is the principal cytosolic source of NADPH for
reductive biosynthesis (fatty acids, cholesterol, nucleotides) and, critically in erythrocytes,
for regenerating reduced glutathione and defending against oxidative stress.

- UniProt FUNCTION: "Catalyzes the rate-limiting step of the oxidative pentose-phosphate pathway,
  which represents a route for the dissimilation of carbohydrates besides glycolysis. The main
  function of this enzyme is to provide reducing power (NADPH) and pentose phosphates for fatty
  acid and nucleic acid synthesis." [file:human/G6PD/G6PD-uniprot.txt]
- Active as a **homodimer / homotetramer (dimer of dimers)** requiring a tightly bound
  **structural NADP+** for stability, in addition to the catalytic (cosubstrate) NADP+.
  UniProt MISCELLANEOUS: "Binds two molecules of NADP. The first one is a cosubstrate (bound to
  the N-terminal domain), the second is bound to the C-terminal domain and functions as a
  structural element." [file:human/G6PD/G6PD-uniprot.txt]
- Cytosolic (UniProt SUBCELLULAR LOCATION: Cytoplasm, cytosol).
- **G6PD deficiency is the most common human enzyme defect (~400 million people), X-linked**
  (CNSHA1, MIM:300908), causing acute oxidant-induced hemolytic anemia (favism, drugs,
  infection), neonatal jaundice, and in severe class-I variants chronic nonspherocytic
  hemolytic anemia.

## Key experimental references (cached)

- **PMID:15858258** (Kotaka 2005, Acta Cryst D): crystal structures of human G6PD binary
  complexes with G6P and with NADP+; substrate + cosubstrate + structural NADP+ binding;
  tetramer interface. Supports GO:0004345, GO:0050661 NADP binding, GO:0005536 D-glucose
  binding, GO:0042803 homodimerization. (abstract-only cache)
- **PMID:24769394** (Wang 2014, EMBO J): G6PD acetylation on K403 by KAT9/ELP3 blocks dimer
  formation and abolishes activity; SIRT2 deacetylates and activates G6PD; PPP/NADPH homeostasis
  during oxidative stress; SIRT2 interaction (Q8IXJ6). Supports GO:0004345 (EXP), GO:0005515
  (SIRT2), GO:0042802.
- **PMID:26479991** (Warny 2015): case report, severe G6PD deficiency, novel Arg198Ser missense;
  very low enzymatic activity, neonatal jaundice + hemolysis. Supports GO:0004345 (EXP).
- **PMID:38066190** (Zgheib 2023, Commun Biol, full text): Arg219Gly mutant — 50-fold reduced
  catalytic activity, impaired dimerization/stability; WT is dimeric. Supports GO:0004345 (IDA),
  GO:0042803 homodimerization, GO:0051156 G6P metabolic process.
- **PMID:35122041** (Li 2020, Nat Cancer): ALDOB directly binds and inhibits G6PD, forming a
  ternary complex with p53 (TP53); restrains PPP in liver; suppresses HCC. Supports GO:0004345
  (IDA), GO:0005515 (TP53 P04637; ALDOB P05062), GO:0005829.
- **PMID:743300** (Benatti 1978): G6PD activity in erythrocyte membranes, normal vs Mediterranean
  deficiency. Supports GO:0004345 (IMP), and the membrane-associated (GO:0009898) / cytosol
  localization annotations.
- **PMID:5643703** (Beutler 1968, Blood): biochemical G6PD variants causing CNSHA; classic
  deficiency phenotype work. Supports GO:0004345, GO:0005536, GO:0051156, GO:0043249 erythrocyte
  maturation, GO:0019322 pentose biosynthesis (IMP/IDA). (abstract-only cache)
- **PMID:2420826** (Roth 1986, JCI): ribose/PRPP metabolism in normal vs G6PD-deficient
  P. falciparum-infected RBCs; oxidative-branch contribution to pentose. Supports GO:0004345,
  GO:0006749 glutathione metabolism, GO:0009051 oxidative branch, GO:0046390 ribose-phosphate
  biosynthesis.
- **PMID:17516514** (Ayene 2008): G6PD deficiency → loss of control of protein glutathionylation;
  reduced NADPH; reintroducing G6PD normalises phenotype. Supports GO:0006749, GO:0034599
  cellular response to oxidative stress.
- **PMID:2297768** (Thomas 1990): hormonal modulation of G6PD and NADPH utilization in MCF-7;
  cited for GO:0006098 pentose-phosphate shunt (IDA).
- **PMID:21157431** (Cosentino 2011, EMBO J, full text): ATM activates PPP; Hsp27 (HSPB1, P04792)
  binds and directly stimulates G6PD. Basis of the GO:0005515 IPI with HSPB1.
- **PMID:12027950** (Batetta 2002): G6PD-deficient PBMC show reduced cholesterol synthesis;
  basis of GO:0006695 cholesterol biosynthetic process (IMP) — indirect / NADPH-supply role.
- **PMID:17361089** (Sanna 2007): inflammatory molecules in severely G6PD-deficient PBMC;
  cited for GO:0006629 lipid metabolic process (TAS) — indirect.

## Localization / proteomics (high-throughput, non-core)

- PMID:23533145, PMID:19056867: extracellular exosome (HDA) — mass-spec exosome inventories.
- PMID:19946888: membrane (HDA) — NK cell membrane proteome; G6PD is a soluble cytosolic enzyme
  that can associate peripherally with membranes (cf. PMID:743300).
- PMID:22926577: substantia nigra proteomics (HEP) — GO:0021762 substantia nigra development is
  an expression-context over-annotation, not a G6PD function.

## Curation stance

- **Core**: GO:0004345 glucose-6-phosphate dehydrogenase activity (MF); GO:0009051 pentose-phosphate
  shunt, oxidative branch and GO:0006098 pentose-phosphate shunt (BP); GO:0005829 cytosol (CC);
  GO:0050661 NADP binding; GO:0042803 homodimerization.
- **Ensembl orthology IEA transfers (GO_REF:0000107) from rat P05370** import several
  context/phenotype terms (response to iron(III), response to food, response to ethanol,
  regulation of neuron apoptotic process, negative regulation of cardiac muscle cell growth,
  positive regulation of HVGCC calcium transport) that are downstream/pleiotropic physiological
  responses, not molecular functions of the human enzyme → MARK_AS_OVER_ANNOTATED or REMOVE
  (clearly wrong-context IEA).
- Do NOT REMOVE experimental annotations whose full text I cannot verify; bare `protein binding`
  IPIs → MARK_AS_OVER_ANNOTATED (informative interactors noted: HSPB1, SIRT2, TP53, ALDOB).
