# aroD (P05194, Escherichia coli K-12) review notes

## Provenance of this notes file

Provider deep research was unavailable for this review (no deep-research provider key in
the session), so no `aroD-deep-research-*.md` file exists. These notes were compiled by the
reviewer from the cached publications in `publications/`, the UniProt record
(`aroD-uniprot.txt`) and one UniProt REST query recorded below.

Family: PANTHER PTHR43699 (3-DEHYDROQUINATE DEHYDRATASE), subfamily PTHR43699:SF1;
InterPro IPR050146 / IPR001381 (type I DHQase), Pfam PF01487, NCBIfam TIGR01093, HAMAP MF_00214.
No PTHR43699 family review exists yet (being written separately).

## Function

- Type I 3-dehydroquinase; catalyses step 3 of the shikimate (chorismate) pathway,
  3-dehydroquinate = 3-dehydroshikimate + H2O (EC 4.2.1.10, RHEA:21096).
  [UniProt P05194 CC FUNCTION "Catalyzes the cis-dehydration of 3-dehydroquinate (DHQ) and introduces the first double bond of the aromatic ring to yield 3-dehydroshikimate."]
- Purified enzyme: [PMID:2950851 "Homogeneous enzyme with specific activity 163 units/mg of protein was obtained in 19% overall yield."]
  Catalytic properties [PMID:2950851 "shown to be very similar to those of the biosynthetic 3-dehydroquinase component of the arom multifunctional enzyme of Neurospora crassa"].
- Kinetics: Km 17-18 uM for 3-dehydroquinate, kcat 142 s-1 (UniProt BIOPHYSICOCHEMICAL PROPERTIES, from PMID:2950851 and PMID:7592767).
- Mechanism: Schiff base (imine) with Lys-170; His-143 is the general base.
  [PMID:7592767 "When the highly conserved, Schiff base-forming lysine residue was mutated (K170A) the resulting enzyme showed a approximately 10(6)-fold reduction in catalytic activity, but was still able to bind both substrate and product"]
  [PMID:7592767 "Substituting alanine for each shows that H146A retains full catalytic activity while H143A shows a 10(6)-fold loss of activity."]
  The H143A mutant accumulates the product Schiff base: [PMID:7592767 "the H143A mutant is isolated from overexpressing cells with a significant proportion of the enzyme monomers covalently bound to the product, 3-dehydroshikimate, via a Schiff base linkage."]
  The type I enzyme performs a syn elimination [PMID:7592767 "may explain why the elimination reaction catalyzed by the enzyme proceeds with syn stereochemistry."]
- Quaternary structure: dimer.
  [PMID:2950851 "The native Mr, estimated by gel permeation chromatography on Sephacryl S-200 (superfine) and on TSK G3000SW, was in the range 52,000-58,000, indicating that the enzyme is dimeric."]
- Historical: Mitsuhashi and Davis (1954) first described the E. coli 5-dehydroquinase
  activity converting 5-dehydroquinic acid to 5-dehydroshikimic acid (PMID:13198937; only
  the citation/title is cached, no abstract).

## Localization

- Soluble cytosolic enzyme. E. coli proteome fractionation studies (PMID:15911532,
  PMID:18304323) assigned proteins to the cytosolic fraction; aroD is not named in the
  cached text (gene-level data are in the supplementary tables, which are not cached), so
  these rows rest on the EcoCyc curators' reading of the supplements.
  [PMID:18304323 "we identified 1103 proteins from the cytosolic fraction of the Escherichia coli strain MC4100."]

## 3,4-dihydroxybenzoate (protocatechuate) biosynthesis rows

GOA carries GO:0046279 3,4-dihydroxybenzoate biosynthetic process on aroD by IDA (UniProt,
PMID:13198937 and PMID:7592767), IBA (PTN000472499) and IEA (ARBA). The cited papers
measure the dehydration of 3-dehydroquinate to 3-dehydroshikimate, not formation of
3,4-dihydroxybenzoate. 3-Dehydroshikimate is converted to protocatechuate only by a
3-dehydroshikimate dehydratase (EC 4.2.1.118; AroZ/QuiC/AsbF), which acts in quinate
catabolism (Pseudomonas, Acinetobacter, Neurospora) or petrobactin synthesis (Bacillus
anthracis).

Reviewer check (UniProt REST, 2026-11-11):
`query=ec:4.2.1.118 AND organism_id:83333` returned no entries, i.e. no E. coli K-12
protein carries EC 4.2.1.118. The reviewed EC 4.2.1.118 entries returned by
`query=ec:4.2.1.118 AND reviewed:true` were asbF (Bacillus anthracis), quiC1
(Pseudomonas putida KT2440, Pseudomonas aeruginosa PAO1), qa-4 (Neurospora crassa) and
quiC (Acinetobacter baylyi ADP1). E. coli K-12 therefore has no known route from
3-dehydroshikimate to protocatechuate, and the GO:0046279 rows describe a process the
organism does not carry out; the enzyme's product is used for chorismate biosynthesis.
The term likely reflects the organism-independent observation that 3-dehydroshikimate is
the protocatechuate precursor in organisms that have AroZ. Judged an over-annotation
(MARK_AS_OVER_ANNOTATED) rather than REMOVE, because DHQase does supply the direct precursor
when such a route exists (e.g. engineered E. coli expressing a heterologous AroZ).

## Pathway

- UniProt PATHWAY: chorismate biosynthesis, step 3/7 (HAMAP MF_00214). Reviewer check
  (UniProt REST, 2026-11-11): `query=ec:4.2.1.10 AND organism_id:83333` returned only
  P05194 (aroD), so AroD is the only annotated 3-dehydroquinase of E. coli K-12 (no type II
  aroQ paralog), and chorismate and hence
  aromatic amino acid, folate, ubiquinone, menaquinone and enterobactin precursors depend
  on it.
