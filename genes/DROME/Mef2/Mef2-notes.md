# Mef2 (Drosophila melanogaster, P40791) - curation notes

Automated deep research failed for this run (falcon 402, OpenAI 401); notes from cached publications.

## Function
- MADS-box TF; MADS mutants lose DNA binding and are lethal [PMID:12366381 "Mutation of these invariant residues results in the inability of mutant D-MEF2 proteins to bind DNA in vitro, muscle defects within the embryo, and adverse effects on the structure of indirect flight muscles within the adult"].
- Direct targets: sing [PMID:25797154 "This enhancer was active during myoblast fusion, and mutation of two MEF2 sites significantly decreased enhancer activity"]; miR-92b [PMID:22899845 "Mef2 directly activates miR-92b through three conserved Mef2-binding sites in the cis-regulatory region of miR-92b"]; actin and muscle genes with CF2 [PMID:18160709 "MEF2 and CF2 synergistically activate the enhancers of a number of muscle-specific genes"].

## Development
- Required for differentiation, not specification, of all muscle types [PMID:7839146 "In loss-of-function embryos, somatic, cardiac, and visceral muscle cells did not differentiate, but myoblasts were normally specified and positioned"]; cardial cells lack MHC [PMID:7729689 "In the heart, the cardial cells do not express MHC"].
- Direct Tinman target in heart [PMID:9034334 "D-mef2 expression in the developing Drosophila heart requires a novel upstream enhancer containing two Tinman binding sites, both of which are essential for enhancer function in cardiac muscle cells"].
- Adult myoblast fusion [PMID:22008792 "MEF2 is critical at the early stages of adult myoblast fusion"].

## Non-muscle roles
- Clock neurons [PMID:20427646 "Knocking down Mef2 expression via RNAi or expressing a repressor form of Mef2 caused flies to lose circadian behavioral rhythms"].
- Fat body immune-metabolic switch, TBP partner [PMID:24075010 "MEF2 now associates with the TATA binding protein to bind a distinct TATA box sequence and promote antimicrobial peptide expression"].

## Review decisions
- protein binding (TBP) -> MODIFY GO:0017025 TBP-class protein binding.
- GO:0032968 elongation and GO:0010468 -> MODIFY GO:0045944.
- NEW GO:0055007 cardiac muscle cell differentiation (module annoton process; absent from GOA).
- PMID:25747460 (troponin-I cis mutation) abstract does not mention Mef2; accepted deferring to curator.
