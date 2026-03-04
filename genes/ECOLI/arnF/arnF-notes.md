# arnF (ArnF / PmrM / YfbJ) - Research Notes

## Gene Identity
- **UniProt**: P76474 (ARNF_ECOLI)
- **Gene names**: arnF (preferred), pmrM (old), yfbJ (old)
- **Ordered locus names**: b2258, JW5373
- **Organism**: E. coli K12
- **Size**: 128 AA, 14 kDa
- **Structure**: 4 transmembrane helices, inner membrane protein

## Core Function

ArnF is one subunit of an undecaprenyl phosphate-alpha-L-Ara4N flippase heterodimer (ArnE/ArnF). This flippase translocates 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol (alpha-L-Ara4N-phosphoundecaprenol) from the cytoplasmic to the periplasmic side of the inner membrane [PMID:17928292 "PmrL and PmrM could specifically function to flip undecaprenyl phosphate-α-L-Ara4N from the cytosolic to the periplasmic side of the inner membrane, possibly functioning as a heterodimer"].

This flipping step is essential for the L-Ara4N modification of lipid A by ArnT (whose active site faces the periplasm), which in turn is required for polymyxin resistance [PMID:17928292 "Cells lacking this gene are polymyxin sensitive"].

## Pathway Context

ArnF operates in the L-Ara4N lipid A modification pathway:
1. UDP-glucose → UDP-glucuronic acid (Ugd)
2. UDP-glucuronic acid → UDP-4-ketopentose (ArnA C-terminal domain)
3. UDP-4-ketopentose → UDP-beta-L-Ara4N (ArnB, transamination)
4. UDP-beta-L-Ara4N → N-formylated form (ArnA N-terminal domain)
5. N-formyl-L-Ara4N → undecaprenyl-phosphate-L-Ara4N (ArnC, transfer to carrier lipid)
6. Deformylation (ArnD)
7. **Flipping of undecaprenyl-phosphate-L-Ara4N across inner membrane (ArnE/ArnF)** ← arnF acts here
8. Transfer of L-Ara4N to lipid A on periplasmic face (ArnT)

## Key Evidence (PMID:17928292 - Yan, Guan, Raetz 2007)

### Deletion phenotype
- arnF deletion (pmrM deletion) in pmrAc background: polymyxin-sensitive [PMID:17928292 "the pmrL and the pmrM deletion mutants (as well as the double deletion mutant) were sensitive to 15 μg/ml polymyxin"]
- Lipid A lacks L-Ara4N modification (>95% reduction) [PMID:17928292 "In the pmrL or pmrM deletion mutants, over 95% of each of the L-Ara4N-modified lipid A species was missing"]
- Undecaprenyl phosphate-alpha-L-Ara4N levels NOT reduced - the substrate accumulates but can't be flipped [PMID:17928292 "undecaprenyl phosphate-α-L-Ara4N levels were the same or slightly higher in the mutants"]

### Flippase evidence (sulfo-NHS-biotin assay)
- Membrane-impermeable sulfo-NHS-biotin labeling of undecaprenyl-phosphate-L-Ara4N reduced 4-5 fold in arnF mutant vs parent [PMID:17928292 "4–5-fold reduction in ratio of the monoisotopic peak areas for biotinylated undecaprenyl phosphate-α-L-Ara4N"]
- Membrane-permeable NHS-biotin labeling unaffected - ruling out sequestration or degradation
- arnT mutant shows NO reduction in sulfo-NHS-biotin labeling, proving ArnT is not the flippase

### Complementation
- Polymyxin resistance restored by pWSK29-PmrM (arnF) but NOT by pWSK29-PmrL (arnE), demonstrating non-redundant, indispensable roles [PMID:17928292 "polymyxin resistance was recovered in the pmrM deletion mutant AY101 by transforming with pWSK29-PmrM"]

### Subunit
- Forms heterodimer with ArnE (PmrL) [PMID:17928292 "PmrL and PmrM could specifically function to flip...possibly functioning as a heterodimer"]

## Protein Family
- Related to small multidrug resistance (SMR) transporters / EmrE-like
- DMT (Drug/Metabolite Transporter) superfamily (TCDB 2.A.7.22.1)
- Distantly related to EmrE, but functionally distinct (lipid flippase vs drug efflux)
- PANTHER: PTHR30561 (SMR family)

## Regulation
- Induced by BasR (PmrA homolog in E. coli) [PMID:15569938]
- Part of the arnBCADTEF operon (previously yfbE operon / pmrHFIJKLM in Salmonella)
- The BasS-BasR two-component system responds to iron [PMID:15322361 "the BasS-BasR system is essential for this iron-dependent induction of yfbE"]

## Response to Iron
- The yfbE operon (now arn operon) is induced in response to external iron [PMID:15322361]
- BasS-BasR system is involved in iron responses [PMID:15322361]
- Fe(III) toxicity studies show PmrA/PmrB system important for resistance to Fe(III) [PMID:12139617]
- Note: arnF's role in iron response is INDIRECT - iron induces BasR which induces the arn operon, leading to lipid A modification with L-Ara4N

## Subcellular Localization
- Inner membrane, multi-pass membrane protein (4 TM helices)
- IDA from global topology study [PMID:15919996 - C-terminal GFP/PhoA fusion]
- Labeled "plasma membrane" in GO (GO:0005886) - this is the E. coli inner membrane
