# CYP11B2 (P19099) review notes

## Identity / core biology
CYP11B2 = aldosterone synthase (cytochrome P450 11B2, mitochondrial; P450c11AS / P450aldo / P450C18).
Mitochondrial inner-membrane heme-thiolate cytochrome P450 of the adrenal cortex zona glomerulosa.
Catalyses the final three steps of mineralocorticoid (aldosterone) synthesis on a single active site:
11beta-hydroxylation (11-deoxycorticosterone -> corticosterone), 18-hydroxylation (corticosterone ->
18-hydroxycorticosterone), and 18-oxidation (-> aldosterone). Uses the adrenodoxin/adrenodoxin-reductase
(FDX1/FDX2 + FDXR) electron-transfer system with O2 and NADPH-derived electrons.

- UniProt FUNCTION: "A cytochrome P450 monooxygenase that catalyzes the biosynthesis of aldosterone...
  Catalyzes three sequential oxidative reactions of 11-deoxycorticosterone... 11-beta hydroxylation,
  followed by two successive oxidations at C18 yielding 18-hydroxy and then 18-oxo intermediates...
  ending with the formation of aldosterone." Electron system: "flavoprotein FDXR (adrenodoxin/ferredoxin
  reductase) and nonheme iron-sulfur protein FDX1 or FDX2 (adrenodoxin/ferredoxin)."
- >93% identical to CYP11B1; the distinguishing capability is 18-oxidase activity, required to make
  aldosterone (CYP11B1 lacks it) [PMID:1741400; PMID:2256920].
- EC 1.14.15.4 (steroid 11beta-monooxygenase) and EC 1.14.15.5 (corticosterone 18-monooxygenase /
  aldosterone synthase).

## Localization
Mitochondrion inner membrane (peripheral membrane protein), UniProt SUBCELLULAR LOCATION
(ECO:0000250|UniProtKB:P14137). Reactome reactions place CYP11B2 "associated with the inner
mitochondrial membrane". HTP mito-proteome (PMID:34800366) supports mitochondrion. Core CC =
GO:0005743 mitochondrial inner membrane.

## Disease
- Aldosterone synthase deficiency = corticosterone methyloxidase (CMO) deficiency type I (CMO-1,
  MIM:203400) and type II (CMO-2, MIM:610600); autosomal recessive salt-wasting.
- CYP11B1/CYP11B2 chimera (unequal crossover) -> glucocorticoid-remediable aldosteronism / familial
  hyperaldosteronism type I [PMID:1518866].

## Curation decisions summary
Core:
- GO:0047783 corticosterone 18-monooxygenase activity (18-oxidase = aldosterone synthase; distinguishes
  from CYP11B1) — ACCEPT (IBA + IEA present)
- GO:0004507 steroid 11-beta-monooxygenase activity — ACCEPT (IDA PMID:23322723, PMID:1741400,
  PMID:2256920; IBA; TAS; IEA)
- GO:0032342 aldosterone biosynthetic process — ACCEPT (IDA PMID:23322723, PMID:1741400, PMID:2256920;
  IBA; IMP; IEA)
- GO:0005743 mitochondrial inner membrane — ACCEPT (IBA/IC/ISS/TAS/IEA)
- GO:0020037 heme binding — ACCEPT (IDA PMID:23322723; secondary/cofactor)

Non-core / accept:
- GO:0006705 mineralocorticoid biosynthetic process (Reactome TAS) — ACCEPT (parent BP)
- GO:0005506 iron ion binding, GO:0004497 monooxygenase activity, GO:0016705 oxidoreductase... —
  ACCEPT (correct, general P450 IEAs)
- GO:0008395 steroid hydroxylase activity (Reactome TAS) — ACCEPT (correct grouping term)
- GO:0005739 mitochondrion — ACCEPT (correct, less specific than inner membrane)
- Downstream physiology (blood volume, water/Na/K homeostasis, response to K+/hormone) —
  KEEP_AS_NON_CORE (real but pleiotropic downstream consequences of aldosterone, not molecular core)

Notable judgement calls:
- Cortisol/glucocorticoid: CYP11B2 is NOT the physiological cortisol producer (that is CYP11B1). It can
  make cortisol / 18-hydroxycortisol / 18-oxocortisol in vitro and in primary aldosteronism.
  - GO:0034651 cortisol biosynthetic process NOT|involved_in (IMP PMID:9703385) — ACCEPT the negation.
  - GO:0034651 cortisol biosynthetic process involved_in (IMP PMID:19342457) — MARK_AS_OVER_ANNOTATED
    (in vitro / non-physiological; contradicted by the NOT annotation and by the CYP11B1/CYP11B2 division
    of labour).
  - GO:0006704 glucocorticoid biosynthetic process (IBA) — MARK_AS_OVER_ANNOTATED (CYP11B1's role;
    IBA over-broadens across the CYP11B clade).
  - GO:0034650 cortisol metabolic process (IBA) — MARK_AS_OVER_ANNOTATED (same reasoning; metabolic parent).
- GO:0008203 cholesterol metabolic process (IBA) and GO:0016125 sterol metabolic process (IEA/TAS):
  CYP11B2 acts on C21 steroids (deoxycorticosterone), well downstream of cholesterol; it does not
  metabolize cholesterol or free sterols. MARK_AS_OVER_ANNOTATED (over-broad clade/Reactome grouping).
- GO:0006700 C21-steroid hormone biosynthetic process (IDA PMID:2256920) — ACCEPT (aldosterone is a
  C21 steroid; correct broader BP).
</content>
