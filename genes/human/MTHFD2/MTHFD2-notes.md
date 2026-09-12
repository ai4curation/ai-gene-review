# MTHFD2 (P13995) review notes

Gene: MTHFD2 (HGNC:7434), a.k.a. NMDMC. Human, taxon 9606.
Protein: Bifunctional methylenetetrahydrofolate dehydrogenase/cyclohydrolase, mitochondrial. 350 aa precursor; residues 1-35 = mitochondrial transit peptide; mature chain 36-350.

## Core biology (from UniProt file: human/MTHFD2/MTHFD2-uniprot.txt)

MTHFD2 is a **bifunctional mitochondrial** enzyme of mitochondrial one-carbon (folate) metabolism with two catalytic activities encoded on one polypeptide:

1. **NAD-dependent methylenetetrahydrofolate dehydrogenase** (EC 1.5.1.15):
   Reaction=(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + NAD(+) = (6R)-5,10-methenyltetrahydrofolate + NADH
   [file:human/MTHFD2/MTHFD2-uniprot.txt "NAD-dependent methylenetetrahydrofolate dehydrogenase"; EC=1.5.1.15]
2. **Methenyltetrahydrofolate cyclohydrolase** (EC 3.5.4.9):
   Reaction=(6R)-5,10-methenyltetrahydrofolate + H2O = (6R)-10-formyltetrahydrofolate + H(+)
   [file:human/MTHFD2/MTHFD2-uniprot.txt "Methenyltetrahydrofolate cyclohydrolase"; EC=3.5.4.9]

Together these convert 5,10-methylene-THF, via 5,10-methenyl-THF, to 10-formyl-THF, supplying one-carbon units (ultimately formate) from mitochondrial serine/glycine catabolism for cytosolic biosynthetic reactions (purine synthesis, formylmethionyl-tRNA for mitochondrial translation) [Reactome:R-HSA-6801328; Reactome:R-HSA-6801462].

### NAD+ vs NADP+ specificity (KEY)
- The dehydrogenase is **NAD-specific** but "can also utilize NADP at a reduced efficiency" [file:human/MTHFD2/MTHFD2-uniprot.txt "Although its dehydrogenase activity is NAD-specific, it can"].
- Kinetics [file: uniprot]: KM=202 uM for NAD, KM=352 uM for NADP; Vmax=22.5 (NAD) vs 2.92 (NADP) umol/min/mg — i.e. NADP activity is ~8-fold lower Vmax and higher KM. So NAD+ activity (GO:0004487) is the physiological/core MF; NADP+ activity (GO:0004488) is a real but minor in-vitro capability → non-core.
- Unique property: requires an enzyme-Mg2+ complex and inorganic phosphate to bind NAD [file:human/MTHFD2/MTHFD2-uniprot.txt "requires formation of an"; "enzyme-magnesium complex to allow binding of NAD"]. This is why Mg2+ (GO:0000287) and phosphate (GO:0042301) binding are annotated.

### Distinction from MTHFD1 (cytosolic)
"This NAD-dependent bifunctional enzyme has very different kinetic properties than the larger NADP-dependent trifunctional enzyme" [file:human/MTHFD2/MTHFD2-uniprot.txt]. MTHFD2 is bifunctional (DH + cyclohydrolase, no synthetase) and NAD-dependent; cytosolic MTHFD1 is trifunctional and NADP-dependent.

## Supporting publications (all abstract-only for the two primary enzymology papers)

### PMID:8218174 (Yang & MacKenzie 1993, Biochemistry) — full_text_available: false
Recombinant human bifunctional NAD-dependent enzyme; "unique in its absolute requirement for Mg2+ and inorganic phosphate. Both ions affect the affinity of the enzyme for NAD and have no effect on the binding of methylenetetrahydrofolate. The NAD cofactor can be replaced by NADP with a much higher KM and lower VMAX." Establishes: NAD+ dehydrogenase (IDA), NADP+ dehydrogenase as minor (IDA), Mg2+ binding (IDA), phosphate binding (IDA), THF metabolic process (IDA), cyclohydrolase by similarity (ISS to P09440 = MTHFD1). Also proposes mitochondrial role (homolog of yeast MIS1). Supports the mitochondrial localization ISS.

### PMID:16100107 (Christensen et al. 2005, JBC) — full_text_available: false
Homology model + mutagenesis (D168/R201/D225/R233 in mature numbering; abstract uses model numbering Arg166/Asp190/Arg198/Asp133). "It is unique in its absolute requirement for inorganic phosphate and magnesium ions to support dehydrogenase activity." "NMDMC uses Pi and magnesium to adapt an NADP binding site for NAD binding." Establishes mechanistic basis for Mg2+ (IMP) and phosphate (IMP) requirement, NAD+ dehydrogenase (IMP), NADP+ dehydrogenase (IMP), cyclohydrolase (IDA). UniProt cites this for both catalytic activities (EC 1.5.1.15 experimental; EC 3.5.4.9 by ECO:0000305 inference).

## Localization
- Mitochondrion / mitochondrial matrix: strongly supported. IDA (HPA immunofluorescence, GO_REF:0000052), HTP (PMID:34800366 mito proteome), IBA, ISS, ARBA, SubCell mapping, plus Reactome TAS. All consistent with matrix enzyme. UniProt: "SUBCELLULAR LOCATION: Mitochondrion."
- GO:0005576 extracellular region (HDA, PMID:22664934): from a tear-fluid proteomics screen of breast cancer patients. Bulk MS detection in a secretome/biofluid; not a curated functional location for this matrix enzyme. Keep as non-core (do not REMOVE HDA experimental annotation). UniProt DR lists GO:0005615 extracellular space HDA — same origin.

## Interactions
- GO:0005515 protein binding (IPI, PMID:32296183, with UniProtKB:Q9UJ70-2 = NAGK): from the HuRI human binary interactome (Y2H). UniProt records this interaction (P13995; Q9UJ70-2: NAGK; NbExp=3). Bare "protein binding" — uninformative MF; mark as over-annotated (do not REMOVE IPI).

## Action summary rationale
- Both real catalytic MFs assigned to core: GO:0004487 (NAD+ dehydrogenase) and GO:0004477 (cyclohydrolase).
- GO:0004488 (NADP+ dehydrogenase): genuine measured but reduced-efficiency activity → KEEP_AS_NON_CORE (all instances).
- Mg2+ and phosphate binding: required for NAD binding/catalysis → core supporting MFs.
- BP: tetrahydrofolate interconversion (GO:0035999) / THF metabolic process (GO:0046653) core; folic acid metabolic process (GO:0046655) is broader/parent-ish, keep non-core.
- catalytic activity (GO:0003824, IEA): trivially true root-ish MF; over-annotated (redundant with specific MFs).
</content>
