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
- GO:0005887 (integral component of plasma membrane) is **obsolete** — cannot be used

## GO Hierarchy Analysis: Intramembrane Lipid Transporter Activity

The GO:0140303 branch reveals an important ontology gap for ArnF:

```
GO:0140303 intramembrane lipid transporter activity
  "Enables the transport of a lipid from a region of a membrane
   to a different region on the same membrane."
  ├── GO:0017128 phospholipid scramblase activity
  │     (ATP-independent, non-selective, bidirectional)
  └── GO:0140326 ATPase-coupled intramembrane lipid transporter activity
        "Catalysis of the movement of lipids from one membrane leaflet
         to the other, driven by ATP hydrolysis."
        ├── GO:0140327 flippase activity
        │     (exoplasmic → cytosolic, ATP-dependent)
        │     ├── GO:0015247 aminophospholipid flippase activity
        │     ├── GO:0140333 glycerophospholipid flippase activity
        │     ├── GO:0140345 phosphatidylcholine flippase activity
        │     ├── GO:0140351 glycosylceramide flippase activity
        │     └── GO:0140347 N-retinylidene-PE flippase activity
        └── GO:0140328 floppase activity
              (cytosolic → exoplasmic, ATP-dependent)
              ├── GO:0015161 lipid III floppase activity (ECA assembly)
              ├── GO:0015437 lipopolysaccharide floppase activity
              ├── GO:0034202 glycolipid floppase activity
              ├── GO:0046623 sphingolipid floppase activity
              └── GO:0090554 phosphatidylcholine floppase activity
```

### Why GO:0140303 is the correct (and only correct) MF term for ArnF

ArnE/ArnF flips undecaprenyl phosphate-α-L-Ara4N from **cytosolic → periplasmic** leaflet.
This is the **floppase direction** (cytosolic → exoplasmic). However:

- GO:0140328 (floppase activity): requires **ATP hydrolysis** — ArnE/ArnF is a small 4-TM
  protein with NO ATPase domain. Not applicable.
- GO:0140327 (flippase activity): wrong direction AND requires ATP. Not applicable.
- GO:0017128 (scramblase activity): ATP-independent but defined as non-selective and
  bidirectional — ArnE/ArnF is directional and substrate-specific. Not applicable.
- GO:0015161 (lipid III floppase activity): closest analog (also undecaprenyl-linked
  substrate, also bacterial inner membrane), but defined as ATP-dependent. Not applicable.

**Conclusion**: GO:0140303 is the only term that correctly captures ArnF's function without
making false claims about energy coupling. All children either require ATP or don't match
the directionality/selectivity.

### Ontology gap

There is no GO term for "ATP-independent, directional intramembrane lipid transporter
activity" — the space between scramblase (non-selective, bidirectional) and
flippase/floppase (ATP-dependent, directional). ArnE/ArnF falls in this gap: it is
directional and substrate-specific, but not ATP-coupled.

This could be flagged as a potential new term request: something like
"energy-independent intramembrane lipid transporter activity" or
"non-ATPase floppase activity" under GO:0140303.

The closest existing term by analogy is GO:0015161 (lipid III floppase activity) which
also handles undecaprenyl-linked substrates flipped across the bacterial inner membrane
during cell surface polysaccharide assembly — but for ECA rather than L-Ara4N lipid A
modification, and classified as ATP-dependent.

## IBA Analysis: PANTHER PTHR30561

### WITH/FROM proteins in the IBA annotations

The IBA annotation to GO:0022857 (transmembrane transporter activity) was inferred from:

| Protein | Gene | Function | Mechanism |
|---------|------|----------|-----------|
| P23895 | emrE | Multidrug efflux pump | Transmembrane export (H+ antiport) |
| P69210 | mdtI | Spermidine export | Transmembrane export |
| P69212 | mdtJ | Spermidine export | Transmembrane export |
| P69937 | gdx (sugE) | Guanidinium export | Transmembrane export |
| P9WGF1 | mmr (Rv3065) | M. tuberculosis multidrug resistance | Transmembrane export |
| Q47377 | arnE | L-Ara4N flippase subunit | Intramembrane flip |
| P76474 | arnF | L-Ara4N flippase subunit | Intramembrane flip |

All non-ArnE/ArnF members are genuine **solute exporters** — they move substrates from
cytoplasm across the membrane to the periplasm/exterior. ArnE/ArnF does something
fundamentally different: it flips a **lipid-linked** substrate between membrane leaflets.

The PANTHER family PTHR30561 groups these by shared SMR/DMT fold (4-TM helices), but the
functional annotation "transmembrane transporter activity" correctly describes only the
exporters, not the flippase pair.

### PANTHER subfamily structure

From PTHR30561-entries.csv, the family contains at least these subfamilies:
- **SF9**: ArnF-related (4-amino-4-deoxy-L-arabinose-phosphoundecaprenol flippase subunit)
- **SF23**: ArnE-related
- **SF6**: MdtI (spermidine export)
- **SF2**: MdtJ (spermidine export)
- Family-level (not assigned to SF): EmrE, Gdx/SugE

This means the IBA could in principle be refined at the subfamily level — SF9/SF23
should get intramembrane lipid transporter annotations, while SF2/SF6 and family-level
members keep transmembrane transporter annotations.

## EcoCyc Annotation Quality Assessment

EcoCyc contributed 5 of the 18 total GO annotations for arnF:

| Term | Evidence | Assessment |
|------|----------|------------|
| GO:0010041 response to iron(III) ion | IGI (PMID:12139617) | **Over-annotated** — conflates operon regulation with gene function |
| GO:0010041 response to iron(III) ion | IEP (PMID:15322361) | **Over-annotated** — expression pattern ≠ function |
| GO:1901264 carbohydrate derivative transport | IMP (PMID:17928292) | **Good** — supported by sulfo-NHS-biotin assay |
| GO:1901505 carbohydrate derivative transmembrane transporter activity | IMP (PMID:17928292) | **Good** — complementation + biotinylation evidence |
| GO:0005886 plasma membrane | IDA (PMID:15919996) | **Good** — GFP/PhoA topology study |

The iron response annotations are a textbook case of over-annotation: iron activates
BasS-BasR → induces arn operon → ArnF expressed. But ArnF doesn't sense, bind, or
detoxify iron. By this logic, every gene in an iron-responsive regulon would be annotated
to "response to iron(III) ion," which is clearly inappropriate.

The EcoCyc IMP annotations are well-supported and accurate. The IDA for plasma membrane
is the strongest CC evidence available.
