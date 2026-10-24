# CYP79F1 (BUS1 / SPS / SUPERSHOOT; dihomomethionine N-hydroxylase) - Arabidopsis thaliana - review notes

UniProt: Q949U1 · At1g16410 · EC 1.14.14.42 · Taxon 3702
Context: entry step of aliphatic glucosinolate core structure formation
(modules/aliphatic_glucosinolate_myrosinase_defense.yaml, annoton cyp79f_activity).
No falcon deep-research file was present at review time.

## Core function
- ER-anchored P450 converting chain-elongated methionines to aldoximes (two
  N-hydroxylations, then dehydration/decarboxylation).
  [PMID:11133994 "We report that cytochrome P450 CYP79F1 catalyzes aldoxime formation in the biosynthesis of aliphatic glucosinolates in Arabidopsis thaliana."]
- Substrate range mono- to hexahomomethionine; short-chain (di-/tri-) preferred (Km ~34-37 uM
  vs ~200 uM for tetra/penta per UniProt from PMID:12609033).
  [PMID:12609033 "we show that CYP79F1 metabolizes mono- to hexahomomethionine, resulting in both short- and long-chain aliphatic glucosinolates."]
- Genetics: null mutant lacks short-chain aliphatic GSLs; long-chain GSLs increase (substrates
  undergo more elongation cycles). Double cyp79f1 cyp79f2 abolishes aliphatic GSLs.
  [PMID:11226190 "Short-chain glucosinolates derived from methionine were completely lacking in the null mutant and showed increased levels in the overexpressing plant"]
  [PMID:15194821 "Our analysis shows that aliphatic glucosinolate biosynthesis is completely abolished in the double-knockout plants"]

## Localization
- ER: N-terminal 62 aa-GFP fusion co-localizes with ER-GFP.
  [PMID:11226190 "the GFP fusions of CYP79F1 and CYP79F2 were both located in the ER"]
- Chloroplast (AtSubP ISM) contradicted -> REMOVE. Nucleus (HDA, PMID:28887381 fractionation)
  -> MARK_AS_OVER_ANNOTATED (likely ER/nuclear envelope co-fractionation).

## Pleiotropic phenotypes (not core)
- bushy/supershoot: loss of apical dominance, crinkled leaves, retarded vasculature; linked to
  altered auxin/IAN/indole-GSL or cytokinin levels -> indirect consequence of the metabolic block.
  [PMID:11226190 "The bus phenotype may result from either an altered content of methionine-derived glucosinolates and their biosynthetic intermediates or from an increase of indolyl glucosinolates and IAA concentrations."]
  [PMID:15194821 "supporting the involvement of this gene in cytokinin homeostasis"]
  No development/branching GO terms are proposed.

## Regulation
- Induced by MeJA [PMID:12529537]; repressed after aphid feeding [PMID:23144921] and by
  lepidopteran oral secretions [PMID:40546745] -> IEP response to insect kept as non-core.

## Decisions
- GO:0120526 homomethionine N-monooxygenase activity (IEA, Rhea/EC) -> ACCEPT (core MF)
- GO:0016709 IDA (PMID:12609033) -> MODIFY to GO:0120526
- GO:0016709 IBA -> MODIFY to GO:0016712 (P450 reductase = flavoprotein donor; GO:0120526 is_a GO:0016712)
- GO:0019761 IBA/IMP -> ACCEPT; ER (IBA/IDA), ER membrane, membrane -> ACCEPT
- monooxygenase, 0016705, heme, iron -> KEEP_AS_NON_CORE
- chloroplast ISM -> REMOVE; nucleus HDA -> MARK_AS_OVER_ANNOTATED; response to insect IEP x2 -> KEEP_AS_NON_CORE
- GO note: no "aliphatic glucosinolate biosynthetic process" term exists; GO:0033506 (from homomethionine)
  and CYP79F1-specific MF terms GO:0103096-8 are obsolete; GO:0120526 is the live replacement.
