# HSD17B4 (P51659) — review notes

## Identity and overview

HSD17B4 encodes the **peroxisomal multifunctional enzyme type 2 (MFE-2 / MFP-2)**, also
called **D-bifunctional protein (DBP)** and historically "17-beta-hydroxysteroid
dehydrogenase type 4 (17β-HSD4)". It is a 736-aa peroxisomal-matrix enzyme that catalyzes
steps 2 and 3 of peroxisomal fatty-acid beta-oxidation with **D (R) stereochemistry**.

The protein is multidomain (UniProt P51659 FT):
- N-terminal **(3R)-hydroxyacyl-CoA dehydrogenase** domain (aa 1–305; SDR/Rossmann fold, NAD+
  binding), historically the "17β-HSD" part [file:human/HSD17B4/HSD17B4-uniprot.txt "REGION          1..305 /note=\"(3R)-hydroxyacyl-CoA dehydrogenase\""].
- Central **enoyl-CoA hydratase 2** / D-3-hydroxyacyl-CoA dehydratase domain (aa 322–622;
  MaoC-like hot-dog fold) [file:human/HSD17B4/HSD17B4-uniprot.txt "REGION          322..622 /note=\"Enoyl-CoA hydratase 2\""].
- C-terminal **SCP2 sterol-carrier / lipid-transfer** domain (aa 624–736)
  [file:human/HSD17B4/HSD17B4-uniprot.txt "DOMAIN          624..736 /note=\"SCP2\""].

The mature protein carries a C-terminal peroxisomal targeting motif (aa 734–736, "AKL")
[file:human/HSD17B4/HSD17B4-uniprot.txt "MOTIF           734..736 /note=\"Microbody targeting signal\""] and is imported
into the peroxisomal matrix. In vivo it is processed by the peroxisomal protease TYSND1 into
separate dehydrogenase and hydratase chains (PRO_0000400082 aa 1–311, PRO_0000400083 aa
312–736), but the full-length protein is bifunctional [PMID:9089413].

## Two catalytic activities (the core function)

DBP performs the 2nd (hydration) and 3rd (dehydrogenation) reactions of each beta-oxidation
cycle, in D/R stereochemistry:

1. **Enoyl-CoA hydratase 2 / D-3-hydroxyacyl-CoA dehydratase** (EC 4.2.1.119 for the general
   reaction; EC 4.2.1.107 for the THCA-CoA bile-acid substrate): (2E)-enoyl-CoA + H2O ⇌
   (3R)-3-hydroxyacyl-CoA. UniProt CATALYTIC ACTIVITY: "a (3R)-3-hydroxyacyl-CoA = a
   (2E)-enoyl-CoA + H2O; ... EC=4.2.1.119"
   [file:human/HSD17B4/HSD17B4-uniprot.txt "EC=4.2.1.119"].
2. **(3R)-3-hydroxyacyl-CoA dehydrogenase (NAD+)** (EC 1.1.1.n12): (3R)-3-hydroxyacyl-CoA +
   NAD+ ⇌ 3-oxoacyl-CoA + NADH + H+. UniProt CATALYTIC ACTIVITY: "a (3R)-3-hydroxyacyl-CoA +
   NAD(+) = a 3-oxoacyl-CoA + NADH + H(+); ... EC=1.1.1.n12"
   [file:human/HSD17B4/HSD17B4-uniprot.txt "EC=1.1.1.n12"].

The 3-oxoacyl-CoA product is handed to the peroxisomal thiolase step (SCPx/ACAA1) to complete
the cycle. UniProt FUNCTION: "Catalyzes two of the four reactions in fatty acid degradation:
hydration of 2-enoyl-CoA (trans-2-enoyl-CoA) to produce (3R)-3-hydroxyacyl-CoA, and
dehydrogenation of (3R)-3-hydroxyacyl-CoA to produce 3-ketoacyl-CoA (3-oxoacyl-CoA), which is
further metabolized by SCPx." [file:human/HSD17B4/HSD17B4-uniprot.txt "Catalyzes two of the four reactions in fatty"].

The bifunctional purified enzyme has both activities; a proteolytic C-terminal fragment
retains only the dehydratase [PMID:9089413 "The protein expressed by the cDNA with the entire coding region exhibited both the dehydratase and dehydrogenase activities, and that expressed by a truncated version covering the carboxyl-terminal side exhibited only the dehydratase activity"].
Original cloning identified the cDNA as identical to 17β-HSD IV [PMID:9089413 "The cloned cDNA was identical to the human 17 beta-hydroxysteroid dehydrogenase IV cDNA"].

## Physiological substrates: fatty acids, not steroids

Although first characterized as a 17β-hydroxysteroid dehydrogenase (from a porcine
17β-estradiol dehydrogenase probe), DBP's physiological substrates are **fatty acyl-CoAs**,
not steroids. It is the **main** bifunctional enzyme for:
- **Very-long-chain fatty acids (VLCFAs)** — DBP deficiency accumulates straight-chain VLCFA
  [PMID:9482850 "it is very striking that this patient, who is deficient in d -bifunctional enzyme, accumulates straight-chain fatty acids (VLCFA) both in plasma and fibroblasts"];
  the D enzyme is suspected to be the main VLCFA beta-oxidation enzyme [PMID:9482850 "it might well be that the d -specific enzyme is also the main enzyme involved in the β-oxidation of very-long-chain fatty acids"].
- **2-methyl-branched-chain (pristanic) acids and C27 bile-acid intermediates (DHCA/THCA)**
  [PMID:9482850 "primarily reacting with alpha-methyl fatty acids like pristanic acid and di- and trihydroxycholestanoic acid"].
- **Long-chain dicarboxylic acids** — DBP is among the main beta-oxidation enzymes for C16DCA
  [PMID:15060085 "the main enzymes involved in beta-oxidation of C16DCA are SCOX, both LBP and DBP, and sterol carrier protein X"].
- **DHA (C22:6n-3) biosynthesis** — peroxisomal beta-oxidation of C24:6n-3 to C22:6n-3 needs DBP
  [PMID:11734571 "the main enzymes involved in beta-oxidation of C24:6n-3 to C22:6n-3 are SCOX, DBP, and both 3-ketoacyl-CoA thiolase and SCPx"].

The 1995 cloning paper reports only a "specific unidirectional oxidative 17β-HSD activity"
when over-expressed [PMID:7487879 "the human 17 beta-HSD IV enzyme displays a specific unidirectional oxidative 17 beta-HSD activity"];
this is the source of the estradiol/androgen/estrogen-dehydrogenase annotations. Physiologically
these steroid activities are minor/secondary side reactions of the fatty-acid oxidoreductase;
UniProt's RecName is "Peroxisomal multifunctional enzyme type 2", and the FUNCTION section
describes only fatty-acid/bile-acid metabolism, not steroid metabolism. The steroid MF/BP
annotations (GO:0004303, GO:0008209, GO:0008210) are therefore over-annotations of the
enzyme's core evolved role, but they rest on an IDA experiment (PMID:7487879) and are not
removed per curation policy.

## Localization

Peroxisome / peroxisomal matrix. UniProt: "SUBCELLULAR LOCATION: Peroxisome"
[file:human/HSD17B4/HSD17B4-uniprot.txt "SUBCELLULAR LOCATION: Peroxisome"]. Supported by IDA
immunofluorescence (PMID:15599942, HPA GO_REF:0000052), Reactome peroxisomal-matrix TAS, and
the C-terminal PTS1-like microbody targeting signal. Cytosol/membrane/peroxisomal-membrane
annotations reflect the import route (PTS1 cargo transits cytosol before import; Reactome
R-HSA-9033235/9033236 model the PEX5 import machinery) or proteomics co-fractionation, not the
functional site of catalysis.

## Structure / subunit

Homodimer [file:human/HSD17B4/HSD17B4-uniprot.txt "SUBUNIT: Homodimer"]. Crystal structures
solved for each domain: SCP2-like domain (1IKT), hydratase 2 (1S9C), dehydrogenase+NAD (1ZBQ).
The hydratase-2 crystal structure shows a hot-dog-fold dimer able to accommodate bulky C26,
pristanic and DHCA/THCA CoA esters [PMID:15644212 "The ability of human hydratase 2 to utilize such bulky compounds ... e.g. CoA esters of C26 fatty acids, pristanic acid and di/trihydroxycholestanoic acids"].
Homodimerization annotations (GO:0042803) are IDA-supported (PMID:15644212, PMID:9089413).

## Disease

- **D-bifunctional protein deficiency (DBPD; MIM 261515)** — severe autosomal-recessive
  peroxisomal beta-oxidation disorder; Zellweger-like neonatal presentation. Caused by
  variants in either the dehydrogenase domain (e.g. Gly16Ser, abolishes dehydrogenase activity
  [PMID:9482850]) or the hydratase domain (e.g. Asn457Tyr, isolated hydratase deficiency,
  unstable protein [PMID:10400999]) [file:human/HSD17B4/HSD17B4-uniprot.txt "D-bifunctional protein deficiency (DBPD) [MIM:261515]"].
- **Perrault syndrome 1 (PRLTS1; MIM 233400)** — a milder allelic phenotype: sensorineural
  deafness + ovarian dysgenesis (Tyr217Cys) [PMID:20673864 via UniProt]
  [file:human/HSD17B4/HSD17B4-uniprot.txt "Perrault syndrome 1 (PRLTS1) [MIM:233400]"].

## Non-core / incidental annotations to flag

- **osteoblast differentiation (GO:0001649, HDA, PMID:16210410)** — from a proteomics
  differential-expression screen in a mesenchymal-stem-cell osteoblast model; DBP not even
  mentioned in the abstract. Expression change, not a functional role. Non-core.
- **membrane (GO:0016020) / peroxisomal membrane (GO:0005778)** — HDA proteomics
  co-fractionation; DBP is a matrix enzyme, not an integral membrane protein. Over-annotated
  location.
- **cytosol (GO:0005829, TAS Reactome)** — reflects the PTS1 import route, not the functional
  compartment.
- **PMID:21525035 (PEX14 microtubule motility)** — about PEX14, not HSD17B4; the
  HSD17B4→peroxisomal-membrane HDA links to a proteomics dataset in that paper. Location
  over-annotation.

## Core functions (for review)

Two catalytic MFs constitute the core evolved function:
1. **GO:0080023 (2E)-enoyl-CoA hydratase activity** — definition "a (3R)-3-hydroxyacyl-CoA = a
   (2E)-enoyl-CoA + H2O", i.e. the D-specific hydratase 2 (EC 4.2.1.119). (The GOA IDA
   annotations use the less specific parent GO:0004300 enoyl-CoA hydratase activity and
   GO:0018812 3-hydroxyacyl-CoA dehydratase activity; GO:0080023 is the D-specific,
   stereochemistry-correct term.)
2. **GO:0106386 (3R)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity** — EC 1.1.1.n12.

Directly involved in: GO:0006635 fatty acid beta-oxidation; bile acid biosynthesis. Location:
GO:0005782 peroxisomal matrix.
</content>
