# ECHS1 (P30084) research notes

Human short-chain enoyl-CoA hydratase 1 / mitochondrial enoyl-CoA hydratase ("crotonase"); EC 4.2.1.17. HGNC:3151, chromosome 10q26.2-q26.3.

## Core enzymatic function

ECHS1 catalyses the second step of the mitochondrial beta-oxidation spiral: reversible hydration of a 2-trans-enoyl-CoA to the corresponding (3S)-3-hydroxyacyl-CoA.

- UniProt FUNCTION: "Converts unsaturated trans-2-enoyl-CoA species ((2E)-enoyl-CoA) to the corresponding (3S)-3hydroxyacyl-CoA species through addition of a water molecule to the double bond" and "Plays a key role in the beta-oxidation spiral of short- and medium-chain fatty acid oxidation" (UniProtKB P30084, ECO:0000269|PubMed:25125611, PubMed:26251176).
- Catalyzes hydration of medium- and short-chain enoyl-CoA from C4 up to C16 [UniProt: "Catalyzes the hydration of medium- and short-chained fatty enoyl-CoA thioesters from 4 carbons long (C4) up to C16"].
- Catalytic activity EC 4.2.1.17 experimentally established [UniProt EC=4.2.1.17 {ECO:0000269|PubMed:26251176}].
- Also has a slower secondary delta(3)-delta(2)-enoyl-CoA isomerase activity (EC 5.3.3.8), by similarity to rat (P14604); UniProt: "At a lower rate than the hydratase reaction, catalyzes the isomerase reaction of trans-3-enoyl-CoA species ... to trans-2-enoyl-CoA species" (ECO:0000250|UniProtKB:P14604). This isomerase activity is NOT experimentally demonstrated in human ECHS1 (electronic/by-similarity only).

### Substrate range (PMID:26251176, abstract)
"Human ECHS1 catalyses the hydration of five substrates via different metabolic pathways, with the highest specificity for crotonyl-CoA and the lowest specificity for tiglyl-CoA." [PMID:26251176 abstract]. UniProt records experimental KM/Vmax: KM=12.75 uM crotonyl-CoA, 34.04 uM acryloyl-CoA, 45.83 uM 3-methylcrotonyl-CoA, 57.87 uM tiglyl-CoA. So ECHS1 acts on crotonyl-CoA (beta-oxidation), acryloyl-CoA, 3-methylcrotonyl-CoA, methacrylyl-CoA, tiglyl-CoA — bridging fatty-acid beta-oxidation and branched-chain amino acid catabolism.

## Branched-chain amino acid / valine catabolism role

ECHS1 deficiency (ECHS1D, MIM:616277) is "A severe, autosomal recessive inborn error affecting valine metabolism" [UniProt DISEASE]. Disease attributed largely to toxic accumulation of valine-pathway intermediates (methacrylyl-CoA, acryloyl-CoA) rather than the beta-oxidation defect.

- PMID:26251176 abstract: "Short-chain enoyl-CoA hydratase-ECHS1-catalyses many metabolic pathways, including mitochondrial short-chain fatty acid β-oxidation and branched-chain amino acid catabolic pathways". The mild patients "have a mild form of ECHS1 deficiency harbouring defective valine catabolic and β-oxidation pathways." Affected patients excrete "N-acetyl-S-(2-carboxypropyl)cysteine, a metabolite of methacrylyl-CoA."
- In valine catabolism, ECHS1 hydrates methacrylyl-CoA to (S)-3-hydroxyisobutyryl-CoA (Reactome R-HSA-70870 "ECHS1 hydrates methacrylyl-CoA"; UniProt CATALYTIC ACTIVITY: "2-methylpropenoyl-CoA + H2O = (S)-3-hydroxyisobutanoyl-CoA"). HIBCH acts downstream. ECHS1 also hydrates 3-methylcrotonyl-CoA (leucine pathway) and tiglyl-CoA (isoleucine pathway), per substrate panel.
- PMID:40056416 (Cell Rep 2025, abstract): loss of ECHS1 or HIBCH causes "abnormal mitochondrial morphology and respiratory defects"; "Elevated lysine methacrylation (Kmea) is observed in both HIBCH- and ECHS1-deficient cells and fly tissues." Provides the FlyBase IMP for L-valine catabolic process (PMID:40056416) and IDA for mitochondrial matrix localization. The proposed mechanism is that accumulating methacrylyl-CoA drives ectopic protein lysine methacrylation. Supports ECHS1's role in valine catabolism (its loss accumulates valine-pathway intermediate methacrylyl-CoA).

## Subcellular localization

- Soluble homohexamer (dimer of trimers) in the mitochondrial matrix [UniProt SUBUNIT: "Homohexamer; dimer of trimers"; SUBCELLULAR LOCATION: "Mitochondrion matrix"]. Crystal/EM structures: PDB 2HW5 (with crotonyl-CoA), 8ZRU-8ZRY.
- N-terminal mitochondrial transit peptide (residues 1-27), cleaved after Phe-27 [UniProt TRANSIT 1..27; PubMed:25944712].
- Experimental localization: mitochondrial matrix IDA from PMID:40056416 (FlyBase); mitochondrion IDA from HPA; mitochondrion HTP from PMID:34800366 (mitochondrial proteome). All consistent.

## Protein-protein interactions (IPI annotations, GO:0005515)

All "protein binding" annotations are from interaction screens; none is the core function, and bare "protein binding" is uninformative per curation guidelines.
- STAT3 (P40763, P42227 mouse): PMID:23416296 "ECHS1 interacts with STAT3 and negatively regulates STAT3 signaling" — yeast two-hybrid + GST-pulldown + co-IP; "ECHS1 specifically represses STAT3 activity ... through inhibiting STAT3 phosphorylation." Possible moonlighting/regulatory role but not metabolic core function.
- LRRK2 (Q5S007): PMID:24510904 (LRRK2 interactor screen, Parkinson disease), PMID:24947832 (LRRK1/LRRK2 interactome), PMID:31046837 (LRRK2-G2019S/SERCA in astrocytes). These are large-scale interactor screens; ECHS1 appears as a hit but no dedicated functional follow-up establishing a metabolic role.
- AIP/Tom20 system (Q15388 = AIP, Q9NS69 = ?): PMID:14557246 "AIP is a mitochondrial import mediator that binds to both import receptor Tom20 and preproteins." ECHS1 is a model mitochondrial preprotein/import substrate here, not a functional partner.

## Annotation-specific notes

- GO:0003824 "catalytic activity" (IEA, InterPro): correct but uninformatively broad; subsumed by enoyl-CoA hydratase activity. MARK_AS_OVER_ANNOTATED / generalize-down.
- GO:0004165 "delta(3)-delta(2)-enoyl-CoA isomerase activity" (IEA, EC 5.3.3.8): by-similarity only (ECO:0000250 from rat P14604); not experimentally shown in human. Keep as non-core (plausible secondary activity).
- GO:0004300 "enoyl-CoA hydratase activity": the CORE MF. EXP/IDA from PMID:26251176 directly support.
- GO:0018812 "3-hydroxyacyl-CoA dehydratase activity" (IEA RHEA): RHEA:16105 = EC 4.2.1.17 reaction written in dehydratase direction; this is the same reaction as enoyl-CoA hydratase activity. Essentially synonymous/parent-ish of the hydratase MF.
- GO:0043956 "3-hydroxypropionyl-CoA dehydratase activity" (IDA PMID:26251176 + IEA RHEA:26518): acryloyl-CoA hydration (3-hydroxypropanoyl-CoA <=> acryloyl-CoA + H2O). Experimentally supported (acryloyl-CoA in substrate panel). Specific, valid.
- GO:0120092 "(2E)-butenoyl-CoA hydratase activity" (IEA RHEA): crotonyl-CoA hydration — the highest-specificity substrate, experimentally measured. Valid, specific.
- GO:0006635 "fatty acid beta-oxidation": core BP; IDA from PMID:26251176, plus IBA/IEA/TAS. ACCEPT.
- GO:0006574 "L-valine catabolic process": core BP; IMP from PMID:40056416 (FlyBase), IEA. ACCEPT.
- GO:0009083 "branched-chain amino acid catabolic process": valid BP (parent of valine catabolism); TAS Reactome + IEA. Keep; valine catabolism is the more specific term.
- GO:0170035 "L-amino acid catabolic process" (IEA ARBA): overly broad parent of valine/BCAA catabolism. MARK_AS_OVER_ANNOTATED.
- GO:0019477 "L-lysine catabolic process" (IMP PMID:37198486, FlyBase): PMID:37198486 (glioma stem cells) shows ECHS1 is the crotonyl-CoA HYDRATASE whose downregulation accumulates crotonyl-CoA (a product of lysine catabolism via GCDH) and drives histone crotonylation. ECHS1 consumes crotonyl-CoA (a lysine-catabolism intermediate); whether ECHS1 is truly "involved in" L-lysine catabolic process vs. acting on a shared crotonyl-CoA pool is debatable. The IMP is curator-assigned from experimental data (full text available, confirms ECHS1 KD increases crotonyl-CoA). Defer to curator; keep as non-core.
- GO:0005759 "mitochondrial matrix" / GO:0005739 "mitochondrion": correct localization (IDA PMID:40056416, IDA HPA, TAS Reactome). Matrix is the precise term. ACCEPT matrix as core location; mitochondrion is the less specific parent.
- GO:0005515 "protein binding" (multiple IPI): keep as non-core (real interactions, uninformative term).

## Disease (context, not for GO core)

ECHS1D (MIM:616277): Leigh-like mitochondrial encephalopathy; basal ganglia lesions, neurodegeneration, psychomotor delay, hypotonia, spasticity, lactic acidosis [UniProt DISEASE; PMIDs 25125611, 25393721, 26000322, 26251176, 26741492, 27221955]. PMID:25125611 (Brain 2014) framed it as "a new inborn error of metabolism affecting valine metabolism" (title). Note: PMID:25125611 NOT cached in publications/ (abstract-only / not available); cited in UniProt only, not a GOA reference here.
