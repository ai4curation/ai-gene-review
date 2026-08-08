# CYP39A1 (Q9NYL5) — Gene Review Notes

## Identity and family

- UniProt RecName: **24-hydroxycholesterol 7-alpha-hydroxylase**; EC **1.14.14.26**; AltNames "Cytochrome P450 39A1" / "Oxysterol 7-alpha-hydroxylase" [file:human/CYP39A1/CYP39A1-uniprot.txt, "RecName: Full=24-hydroxycholesterol 7-alpha-hydroxylase" / "EC=1.14.14.26"].
- Member of the **cytochrome P450 family** [file:human/CYP39A1/CYP39A1-uniprot.txt, "Belongs to the cytochrome P450 family"]. InterPro/PANTHER place it in the CYP7 clan (PTHR24304 "CYTOCHROME P450 FAMILY 7"; CDD cd20635 CYP39A1).
- HGNC:17449; gene on human chromosome 6; MANE-select NM_016593.5 / NP_057677.2; 469 aa precursor.

## Molecular function (well-established)

- A **cytochrome P450 monooxygenase** that catalyzes **7-alpha hydroxylation of (24S)-hydroxycholesterol**, a neural oxysterol, as a step toward bile acid synthesis [file:human/CYP39A1/CYP39A1-uniprot.txt, "Catalyzes 7-alpha hydroxylation of (24S)- hydroxycholesterol, a neural oxysterol that is metabolized to bile acids in the liver"].
- Mechanism: uses molecular O2, inserting one O atom into substrate and reducing the other to water, with two electrons from NADPH via cytochrome P450 reductase (CPR / NADPH-ferrihemoprotein reductase) [file:human/CYP39A1/CYP39A1-uniprot.txt, "uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase"].
- Catalytic-activity Rhea reaction RHEA:46124: (24S)-hydroxycholesterol + reduced [NADPH--hemoprotein reductase] + O2 = (24S)-7alpha-dihydroxycholesterol + oxidized [NADPH--hemoprotein reductase] + H2O + H(+) [file:human/CYP39A1/CYP39A1-uniprot.txt, "Xref=Rhea:RHEA:46124"].
- Cofactor: **heme** (ChEBI:CHEBI:30413); axial heme-Fe ligand at residue 414 [file:human/CYP39A1/CYP39A1-uniprot.txt, "Name=heme; Xref=ChEBI:CHEBI:30413" and "BINDING 414 ... /ligand="heme" ... axial binding residue"]. Heme/iron binding are standard P450 features (InterPro-based IEA GO:0020037, GO:0005506).
- Discovery / expression cloning: identified as a **second oxysterol 7-alpha-hydroxylase** distinct from CYP7B1, selective for 24-hydroxycholesterol; "microsomal cytochrome P450 enzyme that has preference for 24-hydroxycholesterol and is expressed in the liver" [PMID:10748047 "CYP39A1 is a microsomal cytochrome P450 enzyme that has preference for 24-hydroxycholesterol and is expressed in the liver"].
- Note on paralog division of labor: CYP7B1 (the other oxysterol 7-alpha-hydroxylase) acts on 25- and 27-hydroxycholesterol (GO:0033783 is the 25-OHC 7-alpha-hydroxylase term); CYP39A1 is selective for 24-OHC (GO:0033782). Do not conflate these two specific terms.

## Biological process

- **Bile acid biosynthetic process (GO:0006699)**: CYP39A1 acts in the alternative (acidic) bile-acid pathway. 24-hydroxycholesterol is made in the brain (by CYP46A1), exported to the liver, and converted to bile acids; this is a minor but important route for disposal of excess brain cholesterol [Reactome:R-HSA-193775 "24-hydroxycholesterol is synthesized in the brain, exported to the liver, and converted there to bile acids and bile salts. This pathway is only a minor source of bile acids and bile salts, but appears to be critical for the disposal of excess cholesterol from the brain"].
- UniProt PATHWAY annotations: "Steroid metabolism; cholesterol degradation" and "Lipid metabolism; bile acid biosynthesis" [file:human/CYP39A1/CYP39A1-uniprot.txt, "PATHWAY: Steroid metabolism; cholesterol degradation" / "PATHWAY: Lipid metabolism; bile acid biosynthesis"]. The UniProt FUNCTION frames the overall role as "neural cholesterol clearance through bile acid synthesis" [file:human/CYP39A1/CYP39A1-uniprot.txt, "involved in neural cholesterol clearance through bile acid synthesis"].
- Cholesterol catabolic process (GO:0006707) is the UniPathway-derived framing of the same catabolic/degradation role (cholesterol -> bile acids). It is broader/parallel to bile acid biosynthesis and is a defensible non-core BP for this enzyme.
- Cholesterol homeostasis (GO:0042632): P450s of this class contribute to whole-body cholesterol elimination; Reactome frames the "Endogenous sterols" module as CYPs "maintaining cholesterol homeostasis" [Reactome:R-HSA-211976 "playing an important role in maintaining cholesterol homeostasis"]. This is an IBA family-level, higher-level physiological process — plausible but non-core relative to the specific enzymatic step.

## Localization

- **Endoplasmic reticulum membrane / microsome membrane**; multi-pass membrane protein [file:human/CYP39A1/CYP39A1-uniprot.txt, "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane ... Multi-pass membrane protein ... Microsome membrane"]. Consistent with "microsomal cytochrome P450" in PMID:10748047 and Reactome ("located on the ER membrane" R-HSA-192178). Three predicted TM helices (267-287, 352-372, 412-432) plus a cleaved signal (1-23).

## Tissue expression and regulation

- **Liver specific** [file:human/CYP39A1/CYP39A1-uniprot.txt, "TISSUE SPECIFICITY: Liver specific"]; HPA "Tissue enriched (liver)".
- Hepatic mRNA is not regulated by dietary cholesterol/bile acids (unlike other sterol 7-alpha-hydroxylases) and shows sexually dimorphic expression (female > male, opposite to CYP7B1) [PMID:10748047 "levels of hepatic CYP39A1 mRNA do not change in response to dietary cholesterol, bile acids, or a bile acid-binding resin" / "Hepatic CYP39A1 expression is sexually dimorphic (female > male)"].

## Human genetics / disease

- Multiple **loss-of-function alleles** raise serum (24S)-hydroxycholesterol (substrate accumulates), demonstrating CYP39A1 acts on this oxysterol in vivo [PMID:25201972 "revealed multiple loss-of-function alleles with additive effects on serum levels of the oxysterol, 24S-hydroxycholesterol, a substrate of the encoded enzyme"]. UniProt records activity-reducing variants R23P, R103H, Y288H, N324K, K329Q.
- **Exfoliation syndrome / exfoliation glaucoma**: rare functionally-deficient CYP39A1 alleles are associated with exfoliation syndrome (OR ~2.03), and the G204E variant with increased glaucoma and blindness risk (JAMA 2021, PMID:33620406; Ophthalmology 2022, PMID:34763023). Not currently in the GOA set for this gene; recorded here as disease context only, not as a GO annotation.

## Interactions

- GOA has two IPI "protein binding" (GO:0005515) annotations both citing interactant HERC3 (UniProtKB:Q15034), from high-throughput interactome studies (PMID:28514442 BioPlex/HuRI-type; PMID:33961781 BioPlex 3.0). UniProt lists the HERC3 interaction (IntAct, NbExp=3). These are uninformative bare "protein binding" from HT screens; no specific molecular function is defined -> over-annotation (kept, not removed).

## Annotation review summary

- Core MF: **GO:0033782** 24S-hydroxycholesterol 7-alpha-hydroxylase activity (EXP PMID:25201972; also EC-mapped). Supporting cofactor/mechanism MFs: heme binding (GO:0020037), iron ion binding (GO:0005506).
- Core BP: **GO:0006699** bile acid biosynthetic process (IDA PMID:10748047).
- Core CC: **GO:0005789** endoplasmic reticulum membrane.
- Broader/related MF terms (GO:0008396 oxysterol 7-alpha-hydroxylase, GO:0008387 steroid 7-alpha-hydroxylase, GO:0008395 steroid hydroxylase, GO:0004497 monooxygenase, GO:0016705) are correct-but-general parents; kept, several marked over-annotated where a more specific term already exists.
- GO:0007586 digestion is an over-broad/indirect process framing (bile acids aid fat digestion downstream) — over-annotated, not core.
- GO:0043231 intracellular membrane-bounded organelle is a very general CC (parent of ER); over-annotated relative to GO:0005789.
