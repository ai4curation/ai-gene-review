# mcrA Gene Review Notes

## Colleague Question
**Contact**: sgtringe@lbl.gov
**Key Issue**: Difficulty distinguishing methanogens vs methanotrophs by sequence alone

## Key Findings

### Core Function
- Methyl-coenzyme M reductase catalyzes the **terminal step of methanogenesis**
- Converts methyl-CoM + CoB → methane + CoM-S-S-CoB
- Contains unique F430 nickel cofactor essential for catalysis

### Methanogen vs Methanotroph Distinction
**CRITICAL INSIGHT**: The same enzyme works in REVERSE in methanotrophs!
- **Methanogens**: Use mcrA for methane production (forward direction)
- **Methanotrophs (ANME)**: Use mcrA for methane oxidation (reverse direction)
- Sequence alone is insufficient - need ecological/metabolic context

### Distinguishing Features
1. **Phylogenetic context**: ANME lineages cluster separately
2. **Syntrophic partners**: ANME often with sulfate-reducing bacteria
3. **Environmental context**: Deep sea vs terrestrial/freshwater
4. **Gene neighborhood**: Look for associated electron transfer proteins
5. **Isotope signatures**: In environmental samples, δ13C values differ

### Evolutionary Significance
- Ancient enzyme, possibly predating oxygenic photosynthesis
- Horizontal transfer between archaea documented
- Key player in global carbon cycle and climate regulation

## GO Annotation Review
- Accepted core methanogenesis annotations
- Added note about bidirectional activity
- Emphasized nickel cofactor binding specificity

## References
- [PMID:9367957] - Crystal structure revealing F430 cofactor
- [PMID:21593753] - Reverse methanogenesis in ANME archaea
- [PMID:23539639] - Global importance in methane cycling

## Remaining Questions
- How do post-translational modifications affect directionality?
- Can mcrA be engineered for industrial methane conversion?
- What determines forward vs reverse operation at molecular level?
## Revision, 2026-10-15 (ARCHAEA pilot follow-up)

Deep research providers were unavailable; the existing `mcrA-falcon-research.md`
was left untouched. It contains an organism-level error: it says M. acetivorans
uses hydrogenotrophic methanogenesis, but the species description says
[PMID:16346552 "Sodium acetate, methanol, methylamine, dimethylamine, and trimethylamine were substrates for growth and methanogenesis; H(2)-CO(2) (80:20) and sodium formate were not."].
It is cited in the review only for the complex statement.

### GOA refresh
`just fetch-gene METAC mcrA --force` (UniProt entry version 112 -> 114). Current GOA
has 5 rows: cytoplasm (IEA GO_REF:0000044; ISS from P11558), methanogenesis (IEA
InterPro2GO GO_REF:0000002), coenzyme-B sulfoethylthiotransferase activity (IEA
GO_REF:0000120 now including ARBA:ARBA00098318; ISS from P11558). The keyword-mapped
transferase activity (KW-0808) and metal ion binding (KW-0479) rows, the
GO_REF:0000120 methanogenesis row, and the pre-ARBA GO_REF:0000120 activity row
are gone. Per docs/goa_source_refresh.md these four historical records are kept
with `retired: true` (a source change, not a biological REMOVE), with corrected reviews.

### Physiology
- Methanogenic substrates: acetate, methanol, methylamines; not H2/CO2 (PMID:16346552 above).
- CO: [PMID:15550538 "Methane formation surpassed acetate/formate formation only when the cultures entered stationary growth phase"];
  the abstract describes M. acetivorans as "a metabolically versatile methanogen devoid of significant hydrogen metabolism".
- Lab growth substrates in the structural study: [PMID:37307484 "strains were routinely maintained in 10 mL of high salt (HS) media with either acetate (40 mM), methanol (125 mM), or trimethylamine (50 mM) as the sole carbon and energy source"].
- Hence GO:0015948 methanogenesis (generic) is kept. GO children exist only for CO2
  (GO:0019386), acetate (GO:0019385) and methanol (GO:0019387) routes (QuickGO children
  query); methylamine and CO routes have no term, so narrowing would drop routes. This
  differs deliberately from METTH mcrA, an obligate hydrogenotroph narrowed to GO:0019386.

### Structure / cofactor (M. acetivorans MCR, cryo-EM, PDB 8GF5/8GF6)
- [PMID:37307484 "MCR is a C2-symmetric heterohexamer defined by α2β2γ2 subunit stoichiometry"]
- [PMID:37307484 "Strong density is present throughout the entire active-site cavity, allowing for unambiguous identification of CoM, CoB, and F430 as well as the loop containing Glnα161."]
- [PMID:37307484 "Notably, Glnα161 has shifted ~7 Å away from the active-site cavity, consistent with a lack of F430."]
- ChEBI: coenzyme F430 (CHEBI:28265) is_a nickel tetrapyrrole / tetrapyrrole (OLS ancestors).
  GO:0046906 tetrapyrrole binding has children heme, chlorophyll, cobalamin binding; no F430 term.

### PTM
- [PMID:29743535 "In our study, the missing methylation of Arg285 in MCR of Mko4551 led to impaired growth at elevated temperatures and under oxidative stress, although neither the coenzyme F430 content nor the cellular MCR concentration were significantly affected by the missing methyl group."]
  This paper is about the MA4551 methyltransferase; it does not assay MCR catalysis, so
  its earlier use as support for GO:0050524 was a miscitation.

### Decisions on flagged problems (from the METTH reviewer)
1. Transferase activity REMOVE -> TOO_GENERAL (confirmed: GO:0050524 is_a ... GO:0016740 in QuickGO). Row now retired from GOA.
2. Cytoplasm support "See deep research file..." was non-verbatim (confirmed); replaced by UniProt and PMID:30951290 quotes.
3. PMID:29743535 for GO:0050524 (confirmed miscited; reference_review MISCITED); replaced by PMID:37307484.
4. NEW GO:0051291 protein heterooligomerization (confirmed problem): assembly of the
   subunit into the hexamer is not a function the subunit performs for the cell;
   complex membership is captured by GO:0044674. NEW row and core_function entry deleted.
5. F430 binding as GO:0016151 nickel cation binding (confirmed problem): NEW row
   changed to GO:0046906 tetrapyrrole binding (IDA, PMID:37307484), retired
   metal ion binding row MODIFY -> GO:0046906, and "coenzyme F430 binding" proposed
   as a new term plus a suggested question.
6. Qualifiers backfilled by fetch-gene; status COMPLETE.
- GO:0044674 NEW kept; evidence changed IPI -> IDA (purified complex structure).
- Core function rewritten to match METTH structure (GO:0050524, GO:0044674, cytoplasm),
  with generic methanogenesis as the process.
- Removed a non-verbatim core_functions quote attributed to PMID:11932238
  ("MCR catalyzes the final step in methanogenesis" is not in the cached abstract).
