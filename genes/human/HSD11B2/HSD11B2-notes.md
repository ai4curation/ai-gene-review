# HSD11B2 (P80365) review notes

## Verified core biology (from UniProt P80365 + PMID:8538347 abstract + Reactome)

HSD11B2 = 11-beta-hydroxysteroid dehydrogenase type 2 (corticosteroid 11-beta-dehydrogenase
isozyme 2; SDR9C3). Short-chain dehydrogenase/reductase (SDR) family, Rossmann-fold NAD-binding
domain (UniProt: Pfam PF00106 adh_short; PROSITE ADH_SHORT; act site Tyr232 proton acceptor;
NAD binding 82..111).

**Molecular function.** NAD(+)-dependent 11beta-hydroxysteroid dehydrogenase. Oxidises active
11beta-hydroxyglucocorticoids to inactive 11-oxosteroids: cortisol -> cortisone (RHEA:50208),
corticosterone -> 11-dehydrocorticosterone (RHEA:42204), and the generic reaction
"11beta-hydroxysteroid + NAD+ = 11-oxosteroid + NADH + H+" (RHEA:53116). PhysiologicalDirection
is left-to-right (unidirectional dehydrogenase in vivo), in contrast to HSD11B1 which acts as an
11-oxosteroid reductase. UniProt FUNCTION: "Catalyzes the conversion of biologically active
11beta-hydroxyglucocorticoids (11beta-hydroxysteroid) such as cortisol, to inactive
11-ketoglucocorticoids (11-oxosteroid) such as cortisone, in the presence of NAD(+)".
KM for cortisol ~26-84 nM; for corticosterone ~5-6 nM (high-affinity). Uses NAD+ (not NADP+)
as cofactor — Glu115 in cofactor-binding domain dictates NAD+ specificity (mutagenesis
E115K/Q abolishes cofactor specificity, PubMed:11238516).

**Physiological role.** UniProt: "Functions as a dehydrogenase (oxidase), thereby decreasing
the concentration of active glucocorticoids, thus protecting the nonselective mineralocorticoid
receptor from occupation by glucocorticoids." In aldosterone-target epithelia (distal nephron,
colon, salivary gland) it pre-receptor destroys cortisol locally, conferring aldosterone
specificity on the (intrinsically non-selective) mineralocorticoid receptor NR3C2. PMID:8538347
abstract: "11 beta-hydroxysteroid dehydrogenase (11 beta-HSD) catalyses the interconversion of
hormonally active cortisol to inactive cortisone and is vital for dictating specificity for the
mineralocorticoid receptor." Highly expressed in placenta (shields fetus from maternal
glucocorticoid) — HPA tissue enrichment: intestine, kidney, salivary gland. Also interacts with
ligand-free cytoplasmic NR3C2 (PubMed:11350956).

**Localization.** ER membrane (GO:0005789), microsome. N-terminal anchor sequence determines
orientation in the ER membrane (PubMed:10497248). SubCell keyword -> GO:0005783 ER (IEA).

**Disease.** Loss-of-function variants cause Apparent Mineralocorticoid Excess (AME, MIM:218030),
an autosomal-recessive low-renin juvenile hypertension with hypokalemia/metabolic alkalosis,
nephrocalcinosis; cortisol illicitly activates the MR. Many characterized AME variants in UniProt
(R208C/H, R213C, A328V, RY337-338->H, R374X truncation etc.), all reducing/abolishing enzyme
activity. Liquorice (glycyrrhetinic acid) inhibits the enzyme -> acquired AME-like hypertension.
PMID:8538347 = R374X (374..405 del) truncation in AME kindred; supports both cortisol metabolic
process (IMP) and 11beta-HSD (NAD+) activity (IMP).

## Secondary / minor activities (over-annotation candidates)

- **11-oxidation of 11beta-hydroxyandrogens** to 11-ketoandrogens (11beta-hydroxytestosterone ->
  11-ketotestosterone; 11beta-OH-androstenedione -> 11-ketoandrostenedione), RHEA:69368/69408
  (PubMed:22796344, 23685396, 27927697). Real human activity but part of same 11beta-HSD MF
  (same enzyme, extended substrate set) — captured by the general 11beta-HSD MF term.
- **7-beta-hydroxysteroid dehydrogenase (NADP+) activity** GO:0047022: only By similarity to
  P51661 (mouse) / one in-vitro oxysterol paper (7beta-hydroxycholesterol -> 7-ketocholesterol,
  and 7beta,25-diOH-chol -> 7-oxo,25-OH-chol, PubMed:30902677). NADP+, opposite cofactor to the
  physiological NAD+ dehydrogenase; a minor side activity -> MARK_AS_OVER_ANNOTATED (not the
  core/evolved MF; wrong cofactor for the enzyme's physiological role).
- **positive regulation of smoothened signaling pathway** GO:0045880 (IEA GO_REF:0000107 from
  mouse P51661; ISS GO_REF:0000024 from MGI): distal, By-similarity-only, via 7-ketocholesterol ->
  7-keto,27-OH-cholesterol (an SMO activator). Not demonstrated for human HSD11B2 and downstream/
  indirect -> MARK_AS_OVER_ANNOTATED.

## Ensembl-projected (GO_REF:0000107, ECO:0000265 from rat P50233) BP terms

These are electronically projected from rat ortholog experimental data. Adjudication:
- GO:0008211 glucocorticoid metabolic process — CORE, well supported (dup of IBA). ACCEPT.
- GO:0002017 regulation of blood volume by renal aldosterone — mechanistically apt (pre-receptor
  protection of MR in distal nephron confers aldosterone specificity; AME is low-renin
  hypertension). KEEP_AS_NON_CORE (downstream physiology, not the molecular core).
- GO:0007565 female pregnancy — placental 11beta-HSD2 shields fetus from maternal glucocorticoid;
  plausible, high placental expression. KEEP_AS_NON_CORE.
- GO:0051384 response to glucocorticoid — substrate/context term; KEEP_AS_NON_CORE.
- GO:0048545 response to steroid hormone — broad parent of the above; KEEP_AS_NON_CORE.
- GO:0001666 response to hypoxia — HSD11B2 is placental/hypoxia-regulated in rat; peripheral.
  KEEP_AS_NON_CORE.
- GO:0009410 response to xenobiotic stimulus — inhibited by liquorice/xenobiotics but "response
  to" implies a regulated cellular response, weak for this enzyme; MARK_AS_OVER_ANNOTATED.
- GO:0032094 response to food, GO:0032868 response to insulin — physiological-context projections
  from rat; peripheral, not the gene's molecular role. MARK_AS_OVER_ANNOTATED.
- GO:0005496 steroid binding (MF, ECO:0000265) — substrate binding implicit in the catalytic MF;
  keep as supporting/non-core. KEEP_AS_NON_CORE.

## MF / broad-parent electronic terms

- GO:0016616 oxidoreductase activity, acting on CH-OH group of donors, NAD or NADP as acceptor
  (ARBA IEA) — correct but a broad parent of GO:0070523. ACCEPT (acceptable broader IEA).
- GO:0051287 NAD binding (MF) — correct (NAD+-dependent enzyme, Rossmann fold). KEEP_AS_NON_CORE
  (supporting MF, not the core catalytic function).

## Core function synthesis

- MF: GO:0070523 11-beta-hydroxysteroid dehydrogenase (NAD+) activity
- BP: GO:0034650 cortisol metabolic process (and its parent GO:0008211 glucocorticoid metabolic process)
- CC: GO:0005789 endoplasmic reticulum membrane
</content>
