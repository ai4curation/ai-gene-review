# ACADVL (P49748) — Gene Review Notes

Human very-long-chain specific acyl-CoA dehydrogenase (VLCAD), mitochondrial. EC 1.3.8.9 (very-long-chain) / EC 1.3.8.8 (long-chain). HGNC:92. NCBITaxon:9606.

## Core identity and function

VLCAD catalyzes the first (rate-limiting committed) step of each cycle of mitochondrial fatty acid beta-oxidation (FAO): the FAD-dependent alpha,beta-dehydrogenation of acyl-CoA thioesters to the corresponding trans-2-enoyl-CoA, with the electron-transfer flavoprotein (ETF) as the physiological electron acceptor.

- VLCAD "is one of four flavoproteins which catalyze the initial step of the mitochondrial beta-oxidation spiral" [PMID:9461620 "Very long-chain acyl-CoA dehydrogenase (VLCAD) is one of four flavoproteins which catalyze the initial step of the mitochondrial beta-oxidation spiral"].
- The UniProt record describes the reaction as "the proR-proR stereospecific alpha, beta-dehydrogenation of fatty acyl-CoA thioesters using the electron transfer flavoprotein (ETF) as their physiologic electron acceptor, resulting in the formation of trans-2-enoyl-CoA" (file ACADVL-uniprot.txt FUNCTION section).
- Substrate specificity: VLCAD "acts specifically on fatty acyl-CoAs with saturated 12 to 24 carbons long primary chains" with optimum in the very-long-chain range; it is distinguished from MCAD/SCAD by its preference for C14-C24 substrates (ACADVL-uniprot.txt FUNCTION). Catalytic activity entries assign EC 1.3.8.9 (very-long-chain) [PMID:21237683] and EC 1.3.8.8 (long-chain).

## Catalytic / cofactor residues

- The catalytic base abstracting the alpha-proton: "Glu-422 of VLCAD has been presumed to be the catalytic residue that abstracts the alpha-proton in the alphabeta-dehydrogenation reaction. Replacing Glu-422 with glutamine (E422Q) caused a loss of enzyme activity by preventing the formation of a charge transfer complex between VLCAD and palmitoyl-CoA" [PMID:9461620 "Glu-422 of VLCAD has been presumed to be the catalytic residue that abstracts the alpha-proton in the alphabeta-dehydrogenation reaction. Replacing Glu-422 with glutamine (E422Q) caused a loss of enzyme activity by preventing the formation of a charge transfer complex between VLCAD and palmitoyl-CoA"]. (Numbering is for the mature protein; UniProt lists ACT_SITE at residue 462 in the precursor numbering.)
- FAD is the essential cofactor. Phe-418 (mature numbering) is required for FAD binding/reduction: "F418L and F418V contained no bound FAD... These data suggest that Phe-418 is involved in the binding and subsequent reduction of FAD" [PMID:9461620 "These data suggest that Phe-418 is involved in the binding and subsequent reduction of FAD"]. Loss of FAD destabilizes folding: "FAD-deficient VLCADs (F418L, F418V, and apo-VLCAD) showed increased sensitivity to trypsinization. Loss of FAD may change the folding of VLCAD subunit" [PMID:9461620 "FAD-deficient VLCADs (F418L, F418V, and apo-VLCAD) showed increased sensitivity to trypsinization"].
- UniProt COFACTOR: "Name=FAD" with evidence from PMID:18227065 and PMID:9461620.

## Quaternary structure and localization

- VLCAD is a homodimer of ~70 kDa subunits associated with the mitochondrial inner membrane: "Mature VLCAD is a homodimer of a 70-kDa protein associated with the mitochondrial membrane" [PMID:9599005 "Mature VLCAD is a homodimer of a 70-kDa protein associated with the mitochondrial membrane"]. This contrasts with the soluble, matrix tetrameric MCAD/SCAD/LCAD.
- Inner-membrane association precedes and is required for dimer assembly: "Newly synthesized VLCAD was present as a monomer and the major fraction was associated with the mitochondrial inner membrane... association of VLCAD protein with mitochondrial inner membrane is necessary for dimer assembly and formation of mature VLCAD" [PMID:9599005 "association of VLCAD protein with mitochondrial inner membrane is necessary for dimer assembly and formation of mature VLCAD"].
- The monomeric disease mutant S583W fails to associate with the membrane and remains soluble in the matrix: "a VLCAD monomeric mutant S583W... did not associate with the mitochondrial membrane after import and the major fraction remained in the mitochondrial matrix" [PMID:9599005 "a VLCAD monomeric mutant S583W, a novel mutation identified from a patient with VLCAD deficiency, did not associate with the mitochondrial membrane after import and the major fraction remained in the mitochondrial matrix"].
- UniProt SUBCELLULAR LOCATION: "Mitochondrion inner membrane; Peripheral membrane protein" (evidence PMID:9461620, PMID:9599005). The N-terminal 40-aa transit peptide is cleaved on import: "encoding the entire protein of 655 amino acids, including a 40-amino acid leader peptide and a 615-amino acid mature polypeptide" [PMID:7668252 "including a 40-amino acid leader peptide and a 615-amino acid mature polypeptide"].

## Tissue distribution

- "Predominantly expressed in heart and skeletal muscle" (ACADVL-uniprot.txt TISSUE SPECIFICITY, evidence PMID:17564966, PMID:8845838). This matches the clinical phenotype (cardiomyopathy, rhabdomyolysis).
- Unlike ACAD9/ACAD11, VLCAD is not the principal long-chain ACAD in cerebellum; in human cerebellum the ACAD9/ACAD11 pair "accommodates the full spectrum of long chain fatty acid substrates" [PMID:21237683 "The combination of ACAD11 with the newly characterized ACAD9 accommodates the full spectrum of long chain fatty acid substrates presented to mitochondrial β-oxidation in human cerebellum"].

## Disease

- VLCAD deficiency (ACADVLD; MIM:201475) is an inborn error of FAO. Three phenotypes: severe early-onset with cardiomyopathy/high mortality; a milder hepatic/hypoketotic-hypoglycemia form; and an adult myopathic form with rhabdomyolysis (ACADVL-uniprot.txt DISEASE).
- VLCAD was discovered as a novel FAO disorder: "Two of the patients... were found to have a novel disease, VLCAD deficiency, as judged from the results of very low palmitoyl-CoA dehydrogenase activity and the lack of immunoreactivity toward antibody raised to purified VLCAD" [PMID:8466512 "found to have a novel disease, VLCAD deficiency, as judged from the results of very low palmitoyl-CoA dehydrogenase activity and the lack of immunoreactivity toward antibody raised to purified VLCAD"].
- Restoring VLCAD partially restores beta-oxidation flux: "raising VLCAD activity to approximately 20% of normal control fibroblast activity raised palmitic acid beta-oxidation flux to the level found in control fibroblasts" [PMID:7668252 "raising VLCAD activity to approximately 20% of normal control fibroblast activity raised palmitic acid beta-oxidation flux to the level found in control fibroblasts"]. This is an IMP-grade functional demonstration of the FAO role.
- Cardiac/sudden death link: "VLCAD deficiency reduces myocardial fatty acid beta-oxidation and energy production and is associated with cardiomyopathy and sudden death in childhood" [PMID:7479827 "VLCAD deficiency reduces myocardial fatty acid beta-oxidation and energy production and is associated with cardiomyopathy and sudden death in childhood"]. This supports the BP "energy derivation by oxidation of organic compounds".

## Notes on specific GOA annotations

- **GO:0017099 very-long-chain fatty acyl-CoA dehydrogenase activity** (IDA PMID:9461620, IBA, IEA): core MF. This is the defining activity (EC 1.3.8.9). Strongly supported.
- **GO:0004466 long-chain fatty acyl-CoA dehydrogenase activity** (IDA PMID:7668252, TAS PMID:8466512, IEA): VLCAD also handles long-chain (C12-C18); EC 1.3.8.8. Acceptable; somewhat less specific than GO:0017099 but biologically correct (VLCAD activity is classically assayed with palmitoyl-CoA, C16).
- **GO:0003995 acyl-CoA dehydrogenase activity** (IMP PMID:9599005, IMP PMID:9461620, IEA): parent/general ACAD term. The two IMP annotations rest on mutant studies (S583W dimer-assembly mutant; E422Q/F418 catalytic-and-FAD mutants) that abolish/impair dehydrogenase activity — these are legitimate experimental annotations even though the abstracts foreground mechanism/assembly. Keep as non-core (subsumed by the specific VLCAD/LCAD terms).
- **GO:0050660 flavin adenine dinucleotide binding** (IDA PMID:9461620, IEA): core; FAD is the essential redox cofactor. Supported by PMID:9461620 FAD-binding mutant data and UniProt COFACTOR.
- **GO:0042802 identical protein binding** (IDA PMID:9461620, PMID:9599005): VLCAD is a homodimer; this captures homodimerization, supported by PMID:9599005. Keep (informative, not generic "protein binding").
- **GO:0000062 fatty-acyl-CoA binding** (IBA): substrate binding; reasonable IBA, non-core.
- **GO:0016627 oxidoreductase activity, acting on the CH-CH group of donors** (IEA InterPro): correct intermediate parent of ACAD activity. Non-core.
- **GO:0070991 medium-chain fatty acyl-CoA dehydrogenase activity** (IEA RHEA): VLCAD does have measurable activity toward shorter (C10-C12) substrates per the in-vitro Rhea mappings, but its physiological specificity is long/very-long chain. This is an over-annotation by Rhea EC mapping; mark as over-annotated.
- **GO:0006635 / GO:0033539 fatty acid beta-oxidation (using ACAD)** (multiple IDA/IMP/IEA/ISS): core BP. Well supported.
- **GO:0005743 mitochondrial inner membrane** (IEA SubCell): core CC, matches UniProt and PMID:9599005.
- **GO:0031966 mitochondrial membrane** (IDA PMID:16020546, IEA): PMID:16020546 is the ACAD9 paper (Ensenauer 2005); the membrane-association statement is for ACAD-9, not VLCAD. However VLCAD is independently and robustly localized to the inner/mitochondrial membrane (PMID:9599005), so the term itself is correct; less specific than inner membrane. Keep as non-core; do not REMOVE (experimental membrane localization of VLCAD is established).
- **GO:0005759 mitochondrial matrix** (TAS Reactome x2): VLCAD is a peripheral inner-membrane protein on the matrix side; Reactome places the beta-oxidation reactions in the matrix compartment. The mature dimer is membrane-associated, not soluble-matrix (PMID:9599005). Matrix is a less accurate CC than inner membrane; keep as non-core (the catalytic face is matrix-side).
- **GO:0042645 mitochondrial nucleoid** (IDA PMID:18063578): PMID:18063578 is a nucleoid proteomics study; metabolic enzymes co-purify with native nucleoids but were "not observed to cross-link to mtDNA" [PMID:18063578 "Several other metabolic proteins and chaperones identified in native nucleoids, including ATAD3, were not observed to cross-link to mtDNA"]. This is a co-purification artifact / peripheral association, not a genuine nucleoid localization. Mark as over-annotated.
- **GO:0030855 epithelial cell differentiation** (IEP PMID:21492153): from a Caco-2 differentiation proteomics screen where many lipid-metabolism proteins were up-regulated on differentiation. This is a correlative expression change, not a role of VLCAD in differentiation. Over-annotation.
- **GO:0001659 temperature homeostasis; GO:0045717 negative regulation of fatty acid biosynthetic process; GO:0046322 negative regulation of fatty acid oxidation; GO:0090181 regulation of cholesterol metabolic process** (IEA GO_REF:0000107 from mouse P50544; and ISS GO_REF:0000024 from P50544): these are all transferred from the **mouse LCAD ortholog (Acadl, P50544)**, NOT from a VLCAD ortholog. They derive from Acadl-knockout mouse phenotypes (thermoregulation, lipid regulation). Mapping LCAD-knockout phenotypes onto human VLCAD by ortholog transfer is a mis-transfer (the human ortholog of mouse Acadl is human ACADL, not ACADVL). These regulatory/whole-organism phenotypes are not demonstrated for human VLCAD and should be removed as incorrect electronic over-propagations.
- **GO:0005515 protein binding** (IPI PMID:32296183, with TAF1B/Q53T94): a single binary Y2H interaction from HuRI with the RNA Pol I factor TAF1B. Uninformative generic term and biologically implausible as a functional interaction for a mitochondrial inner-membrane FAO enzyme; mark as over-annotated.
- **GO:0015980 energy derivation by oxidation of organic compounds** (TAS PMID:7479827): legitimate higher-level BP; VLCAD-mediated FAO supplies myocardial energy (PMID:7479827). Keep as non-core (parent of beta-oxidation/energy role).

## Paralog/ortholog caution

- Mouse P50544 = Acadl (LCAD), not VLCAD. Several IEA/ISS annotations on human ACADVL were transferred from P50544 and reflect LCAD-knockout mouse biology (temperature homeostasis, regulation of fatty acid/cholesterol metabolism). These are not appropriate for human ACADVL.
- PMID:16020546 (Ensenauer 2005) and PMID:21237683 (He 2011) primarily characterize ACAD9/ACAD10/ACAD11. Where they touch VLCAD it is comparative; do not over-rely on them for VLCAD-specific claims, but the VLCAD membrane localization they support is independently established.

## Core function summary (for synthesis)

1. **Very-long-chain/long-chain acyl-CoA dehydrogenase (EC 1.3.8.9/1.3.8.8)** — FAD-dependent alpha,beta-dehydrogenation of C12-C24 acyl-CoA, first step of FAO; ETF electron acceptor; catalytic Glu, essential FAD. MF GO:0017099; BP GO:0006635; CC GO:0005743.
2. **FAD binding** as the obligate redox cofactor (GO:0050660).
3. **Homodimerization on the inner membrane** (GO:0042802 / inner-membrane CC) — quaternary-structure requirement for activity.
