---
title: "dismech vision disorders aligned with ai-gene-review"
maturity: IN_PROGRESS
description: Per-entry check that dismech's Mendelian non-syndromic vision disorders agree with the gene reviews, PANTHER family reviews, modules and GO-CAMs held here
species: [human]
genes: [ABCA4, ABCB6, AIPL1, ARL2BP, ARL6, ATF6, BBS1, BBS2, BBS9, BEST1, CABP4, CACNA1F, CACNA2D4, CAPN5, CEP290, CERKL, CFAP418, CHM, CHMP4B, CHST6, CNGA1, CNGA3, CNGB1, CNGB3, COL2A1, COL4A1, CRB1, CRX, CRYAA, CTNNB1, CYP1B1, CYP4V2, DCN, DHDDS, DNAJC30, EFEMP1, ELOVL4, EYS, FBN1, FBN2, FLVCR1, FOXC1, FOXE3, FTL, FZD4, GNAT1, GNAT2, GNB3, GPR179, GRK1, GRM6, GUCA1A, GUCY2D, IDH3B, IMPDH1, KCNV2, LRIT3, LRP5, MAK, MT-ND1, MT-ND6, NMNAT1, NYX, OAT, OPA1, OPN1LW, OPN1MW, OPN1SW, OPTN, OTX2, PAX6, PDE6A, PDE6B, PDE6C, PDE6G, PDE6H, RD3, RDH12, RDH5, RHO, RLBP1, RP2, RPE65, SAG, SLC24A1, SOX2, TRPM1, TTC8, WT1]
---

# dismech vision disorders aligned with ai-gene-review

**Bottom line (2026-11-27, work in progress):** dismech holds 126 entries for Mendelian,
eye-restricted vision disorders, caused by 171 genes. When this project started, 104 of
those genes had no review here, none of the 23 GO-CAM models that contain them had been
reviewed, and the PANTHER families of only 28 of them had a family review, so for most
of these diseases the two resources could not be compared at all. The first tranche, the
phototransduction cascade and the photoreceptor-to-bipolar-cell synapse, is now largely
done: all 22 of its unreviewed genes have a complete review (746 annotation rows), seven
GO-CAM models and ten PANTHER families are reviewed, the phototransduction module is
reconciled with the gene reviews, and the first 12 dismech entries carry their gene on a
mechanism node with a molecular function that agrees with the gene review. Comparing the
two resources found real errors on both sides and upstream: a dismech entry that bound
the wrong activity to the disease node, GO-CAM causal edges that cite papers about other
genes, PAINT nodes placed so deep that unrelated receptors inherit photoreceptor
activity, and annotations made from a paper about a different gene. They are listed
under Findings. Seven more tranches (about 115 genes) have not been started.

## Question

For each dismech vision-disorder entry: does the gene's dysfunction, as dismech models it
on its mechanism nodes, agree with the gene's normal function as reviewed here? And for
each gene, is the rest of the function record in place: the PANTHER family review that
says whether a function can be inherited across the family, the reviewed orthologues the
human annotations are often transferred from, the module the gene is a part of, and the
GO-CAM models that place its activity in a causal chain?

This is the vision counterpart of
[dismech metabolic disorders aligned with ai-gene-review](DISMECH_METABOLIC_ALIGNMENT.md).

## Scope

An entry is in scope when it is Mendelian, sits under MONDO "disorder of visual system",
has at least one germline causal gene, affects the visual pathway rather than eye
movement or the eyelids, and is eye-restricted. "Eye-restricted" is decided mechanically
where possible (MONDO does not class the disease as syndromic, and at least 80% of the
entry's HPO-bound phenotypes are abnormalities of the eye) and by hand for the
borderline entries, each with a recorded reason. An entry is **mixed** when it models a
non-syndromic disease together with a recognised syndromic arm of the same gene, as
dismech's gene-level retinopathy entries often do; mixed entries are kept.

The rule and the hand decisions are in
`projects/DISMECH_VISION_ALIGNMENT/build_scope.py` and `scope_overrides.yaml`; every
candidate, kept or dropped, is listed with its reason in `scope_decisions.yaml`.

<!-- BEGIN GENERATED: scope -->
126 entries are in scope (114 non-syndromic, 12 mixed), with 171 distinct causal genes; 94 candidates under the MONDO visual-system branch were excluded. MONDO releases/2026-11-03, HPO hp/releases/2026-09-01.

Entries kept or dropped by a hand decision rather than by the phenotype-share rule:

| Entry | Decision | Eye / all phenotypes | Reason |
|---|---|---|---|
| Aniridia | NONSYNDROMIC | 10/13 | isolated aniridia (PAX6); the WAGR and WT1 material is a contiguous-deletion differential |
| Autosomal_Recessive_Optic_Atrophy_OPA7_Type | MIXED | 7/12 | optic atrophy, with auditory or peripheral neuropathy in some patients |
| BBSome-Related_Retinitis_Pigmentosa | NONSYNDROMIC | 9/9 | eye-restricted by phenotype share; no disease_term bound; non-syndromic retinitis pigmentosa caused by BBSome genes |
| BEST1_Bestrophinopathies | NONSYNDROMIC | 23/23 | eye-restricted by phenotype share; no disease_term bound; every phenotype is ocular |
| BMP4-Related_Ocular_Growth_Disorder | EXCLUDED | 12/25 | syndromic microphthalmia (pituitary, digits, brain) |
| Blepharocheilodontic_Syndrome_1 | EXCLUDED | 0/19 | disorder of eye movement or of the eyelids and adnexa |
| Blepharophimosis_Ptosis_and_Epicanthus_Inversus_Syndrome | EXCLUDED | 4/10 | disorder of eye movement or of the eyelids and adnexa |
| CAPN5-Related_Vitreoretinopathy | NONSYNDROMIC | 6/8 | eye-limited disease; hearing loss and developmental delay are reported in a few carriers of particular alleles |
| CFAP418-related_Retinal_Ciliopathy | MIXED | 4/7 | isolated cone-rod dystrophy or retinitis pigmentosa at one end, Bardet-Biedl syndrome at the other |
| Cataract_40 | NONSYNDROMIC | 5/6 | X-linked cataract without the Nance-Horan features |
| Choroideremia-Deafness-Obesity_Syndrome | EXCLUDED | 4/7 | contiguous gene deletion syndrome |
| Congenital_Fibrosis_of_the_Extraocular_Muscles | EXCLUDED | 9/19 | disorder of eye movement or of the eyelids and adnexa |
| Corneal_Dystrophy | EXCLUDED | 6/6 | umbrella entry with no gene record |
| Duane_Retraction_Syndrome | EXCLUDED | 8/10 | disorder of eye movement or of the eyelids and adnexa |
| Duane_Retraction_Syndrome_3_With_Or_Without_Deafness | EXCLUDED | 4/12 | disorder of eye movement or of the eyelids and adnexa |
| FLVCR1-Related_Retinopathy | MIXED | 6/10 | non-syndromic retinitis pigmentosa and posterior column ataxia with retinitis pigmentosa in one gene-level entry |
| Familial_Progressive_Retinal_Dystrophy-iris_Coloboma-congenital_Cataract_Syndrome | NONSYNDROMIC | 7/7 | MONDO calls it a syndrome but every feature is ocular |
| Hereditary_Hyperferritinemia_With_Congenital_Cataracts | NONSYNDROMIC | 4/6 | cataract is the only clinical manifestation; hyperferritinaemia is a laboratory finding |
| Inherited_Retinal_Dystrophy | EXCLUDED | 8/8 | umbrella grouping of more than 280 genes, not an entry to align gene by gene |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | MIXED | 11/17 | MONDO concept is isolated anophthalmia or microphthalmia; several listed genes (SOX2, OTX2) usually cause syndromic disease |
| Leber-like_Hereditary_Optic_Neuropathy_Autosomal_Recessive_1 | MIXED | 5/8 | optic neuropathy in most patients; a Leigh-like presentation in a minority |
| Leber_Congenital_Amaurosis_with_Early-Onset_Deafness | EXCLUDED | 2/3 | deafness is part of the definition |
| Leber_Hereditary_Optic_Neuropathy | MIXED | 9/16 | eye-limited in most carriers, extra-ocular features in a minority; maternal (mtDNA) inheritance plus recessive DNAJC30 |
| Microcornea-Myopic_Chorioretinal_Atrophy | EXCLUDED | 10/13 | telecanthus and ear anomalies are part of the definition |
| NDP_Related_Vitreoretinopathy | MIXED | 2/5 | eye-limited X-linked vitreoretinopathies together with Norrie disease |
| Oculopharyngeal_Muscular_Dystrophy | EXCLUDED | 2/12 | disorder of eye movement or of the eyelids and adnexa |
| Optic_Atrophy_13_With_Retinal_And_Foveal_Abnormalities | MIXED | 8/10 | optic atrophy is constant; renal and other features occur in a minority |
| Optic_Atrophy_15 | MIXED | 9/16 | isolated optic atrophy and a more severe neurological presentation |
| Optic_Atrophy_3 | MIXED | 5/11 | optic atrophy and cataract; extrapyramidal signs in some families |
| Pre-descemet_Corneal_Dystrophy | EXCLUDED | 2/3 | the STS-linked form is X-linked ichthyosis with a corneal sign |
| Progressive_Retinal_Dystrophy_Due_To_Retinol_Transport_Defect | NONSYNDROMIC | 5/7 | retinal dystrophy; acne and one patent ductus are incidental |
| RCBTB1-Related_Retinopathy | MIXED | 5/9 | retinal dystrophy with or without extra-ocular anomalies |
| RTN4IP1-Related_Optic_Atrophy | EXCLUDED | 3/10 | the entry is dominated by the ataxia, intellectual disability and seizure presentation |
| Retinal_Arterial_Tortuosity | NONSYNDROMIC | 4/4 | eye-restricted by phenotype share; MONDO files it under vascular disease only; every phenotype is ocular |
| Retinitis_Pigmentosa_59 | NONSYNDROMIC | 11/16 | non-syndromic retinitis pigmentosa; the neurological phenotypes in the entry belong to other DHDDS disorders and need checking |
| Retinitis_Pigmentosa_With_or_Without_Situs_Inversus | MIXED | 6/13 | retinitis pigmentosa in all patients; situs inversus or ciliary dyskinesia in some |
| Retinoblastoma | EXCLUDED | 4/6 | neoplasm |
| Stickler_Syndrome_Type_1_Nonsyndromic_Ocular | NONSYNDROMIC | 8/8 | the ocular-only COL2A1 presentation |
| U4_and_U6_snRNA_Gene-Related_Retinitis_Pigmentosa | NONSYNDROMIC | 7/7 | eye-restricted by phenotype share; no disease_term bound; every phenotype is ocular |
| Uveal_Melanoma | EXCLUDED | 3/3 | neoplasm; its germline records are cancer predisposition |
| ornithine_aminotransferase_deficiency | NONSYNDROMIC | 8/11 | gyrate atrophy; the clinical disease is chorioretinal and hyperornithinaemia is its biochemical marker |
<!-- END GENERATED: scope -->

Mitochondrial DNA genes (MT-ND1, MT-ND4, MT-ND6 in Leber hereditary optic neuropathy) are
kept although their inheritance is maternal, not Mendelian in the strict sense: dismech
files the disease as Mendelian and the question asked of each gene is the same.

## Method

**Entry-by-entry comparison.** The audit script written for the metabolic project
(`projects/DISMECH_METABOLIC_ALIGNMENT/align_audit.py`) is run unchanged over
`scope.yaml`. For each gene bound in an entry's `genetic` records it compares the GO
molecular functions and biological processes on the mechanism nodes that name the gene
with the gene review's core functions, and looks for modules that contain the gene. The
metabolic page explains at length why "aligned" is a weak test (the relation is symmetric
and unbounded in ontology distance, node terms are pooled across genes that share a node,
and module membership is not module coverage). All of that applies here.

**Gene-side inventory.** `gene_state.py` records, for each gene, the review status, the
core molecular functions, whether its PANTHER family has a family review, which modules
contain it, which GO-CAM models contain it and whether they are reviewed, and which of
its orthologues have a review. Orthologues come from the PANTHER ortholog service
(`orthologs.yaml`).

**Reviews.** Gene reviews follow the repository's usual procedure. Deep research is from
OpenScientist; Falcon was not usable in the session that started this project. A gene
counts as done for this project when its review is COMPLETE, its family has a family
review, its GO-CAM activities are reviewed against it, and the dismech entries it causes
carry the gene on a mechanism node with a molecular function that agrees with the review.

## The gene side

<!-- BEGIN GENERATED: genes -->
171 genes. Gene reviews: 82 NONE, 55 COMPLETE, 28 DRAFT, 5 INITIALIZED, 1 IN_PROGRESS. 140 PANTHER families, of which the families of 44 genes have a family review. 55 genes are a part of at least one module. 21 genes appear in 23 GO-CAM models, 7 of them reviewed here. 37 genes have at least one reviewed orthologue.

| Gene | Entries | Review | Core molecular function | Family (review) | Modules | GO-CAMs reviewed / all | Reviewed orthologues |
|---|---|---|---|---|---|---|---|
| ABCA4 | 1 | DRAFT | GO:0140347 N-retinylidene-phosphatidylethanolamine flippase activity; GO:0090555 phosphatidylethanolamine flippase activity | PTHR19229 (none) | - | - | - |
| ABCB6 | 1 | COMPLETE | GO:0015439 ABC-type heme transporter activity; GO:0140359 ABC-type transporter activity | PTHR24221 (COMPLETE) | - | - | DROME Hmt-1 (DRAFT) |
| ADAM9 | 1 | - | - | PTHR11905 (none) | - | - | - |
| AIPL1 | 1 | DRAFT | GO:0051879 Hsp90 protein binding; GO:0001918 farnesylated protein binding | PTHR11242 (none) | - | - | - |
| ALDH1A3 | 2 | - | - | PTHR11699 (COMPLETE) | retinoic_acid_metabolism | - | yeast ALD6 (COMPLETE), yeast ALD4 (COMPLETE), yeast ALD5 (COMPLETE) |
| ANGPT1 | 1 | - | - | PTHR47221 (none) | - | 0 / 1 | DROME CG10359 (COMPLETE) |
| ARL2BP | 1 | COMPLETE | GO:0030695 GTPase regulator activity; GO:0140297 DNA-binding transcription factor binding | PTHR15487 (none) | - | - | - |
| ARL6 | 1 | COMPLETE | GO:0005525 GTP binding; GO:0003924 GTPase activity | PTHR11711 (COMPLETE) | bbsome | - | - |
| ATF6 | 2 | COMPLETE | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | PTHR46164 (none) | er_unfolded_protein_response | - | worm atf-6 (COMPLETE) |
| BBS1 | 1 | COMPLETE | GO:0031267 small GTPase binding; GO:0005102 signaling receptor binding | PTHR20870 (none) | bbsome | - | worm bbs-1 (COMPLETE) |
| BBS2 | 1 | COMPLETE | GO:0140378 protein complex scaffold activity | PTHR32465 (none) | bbsome | - | worm bbs-2 (COMPLETE) |
| BBS9 | 1 | COMPLETE | GO:0140378 protein complex scaffold activity | PTHR20991 (none) | bbsome | - | worm bbs-9 (COMPLETE) |
| BEST1 | 3 | COMPLETE | GO:0005229 intracellularly calcium-gated chloride channel activity; GO:0160133 bicarbonate channel activity | PTHR10736 (none) | - | 0 / 1 | - |
| BFSP1 | 1 | - | - | PTHR14069 (none) | - | - | - |
| BFSP2 | 1 | - | - | PTHR23239 (none) | - | - | - |
| CABP4 | 1 | COMPLETE | GO:0005246 calcium channel regulator activity | PTHR45917 (none) | - | - | - |
| CACNA1F | 3 | COMPLETE | GO:0008331 high voltage-gated calcium channel activity | PTHR45628 (none) | - | - | - |
| CACNA2D4 | 1 | COMPLETE | GO:0005246 calcium channel regulator activity | PTHR10166 (none) | - | - | - |
| CAPN5 | 1 | DRAFT | GO:0004198 calcium-dependent cysteine-type endopeptidase activity | PTHR10183 (none) | - | - | - |
| CEP290 | 1 | DRAFT | GO:0008017 microtubule binding; GO:0008289 lipid binding | PTHR18879 (none) | ciliary_transition_zone, primary_cilium_life_cycle | - | - |
| CERKL | 1 | COMPLETE | GO:0003729 mRNA binding | PTHR12358 (none) | - | - | - |
| CFAP418 | 1 | DRAFT | GO:0005543 phospholipid binding | PTHR33958 (none) | - | - | - |
| CHM | 1 | DRAFT | GO:0140318 protein transporter activity; GO:0004663 Rab geranylgeranyltransferase activity (contributes) | PTHR11787 (none) | - | - | - |
| CHMP4B | 1 | COMPLETE | GO:0180020 membrane bending activity | PTHR22761 (none) | escrt_iii_intralumenal_vesicle_formation | - | - |
| CHST6 | 1 | COMPLETE | GO:0001517 N-acetylglucosamine 6-O-sulfotransferase activity | PTHR10704 (none) | - | - | - |
| CNGA1 | 1 | COMPLETE | GO:0005223 intracellularly cGMP-activated cation channel activity (contributes) | PTHR45638 (none) | visual_phototransduction | - | worm tax-4 (COMPLETE) |
| CNGA3 | 3 | DRAFT | GO:0005223 intracellularly cGMP-activated cation channel activity (contributes) | PTHR45638 (none) | visual_phototransduction | - | worm tax-4 (COMPLETE) |
| CNGB1 | 1 | DRAFT | GO:0005221 intracellularly cyclic nucleotide-activated monoatomic cation channel activity (contributes); GO:0004857 enzyme inhibitor activity | PTHR45638 (none) | visual_phototransduction | - | worm tax-2 (COMPLETE) |
| CNGB3 | 3 | COMPLETE | GO:0005223 intracellularly cGMP-activated cation channel activity (contributes) | PTHR45638 (none) | visual_phototransduction | - | worm tax-2 (COMPLETE) |
| COL2A1 | 1 | DRAFT | GO:0030020 extracellular matrix structural constituent conferring tensile strength | PTHR24023 (COMPLETE) | collagen_ddr_signaling | 0 / 1 | - |
| COL4A1 | 1 | COMPLETE | GO:0030020 extracellular matrix structural constituent conferring tensile strength; GO:0005178 integrin binding | PTHR24023 (COMPLETE) | collagen_ddr_signaling | - | - |
| CRB1 | 1 | DRAFT | GO:0030165 PDZ domain binding | PTHR12916 (none) | - | - | - |
| CRX | 1 | DRAFT | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | PTHR45793 (none) | - | - | - |
| CRYAA | 1 | COMPLETE | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | PTHR45640 (none) | - | - | BOVIN CRYAA (IN_PROGRESS), DANRE cryaa (COMPLETE), worm hsp-12.3 (IN_PROGRESS), worm hsp-12.6 (IN_PROGRESS), worm hsp-16.1 (DRAFT), worm hsp-16.2 (COMPLETE), worm hsp-16.41 (DRAFT), worm hsp-16.48 (DRAFT), DROME Hsp26 (DRAFT), DROME Hsp27 (DRAFT), DROME Hsp22 (DRAFT), DROME Hsp23 (DRAFT) |
| CRYBB2 | 1 | - | - | PTHR11818 (none) | - | - | - |
| CRYGB | 1 | - | - | PTHR11818 (none) | - | - | - |
| CRYGC | 1 | - | - | PTHR11818 (none) | - | - | - |
| CRYGD | 1 | - | - | PTHR11818 (none) | - | - | - |
| CTNNB1 | 1 | DRAFT | GO:0003713 transcription coactivator activity; GO:0045296 cadherin binding; GO:0045294 alpha-catenin binding | PTHR45976 (none) | wnt_signaling | 0 / 1 | mouse Ctnnb1 (COMPLETE), rat Ctnnb1 (DRAFT) |
| CYP1B1 | 2 | COMPLETE | GO:0008395 steroid hydroxylase activity; GO:0016712 oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen | PTHR24289 (none) | - | - | - |
| CYP4V2 | 1 | DRAFT | GO:0102033 long-chain fatty acid omega-hydroxylase activity; GO:0140981 medium-chain fatty acid omega-hydroxylase activity; GO:0120319 long-chain fatty acid omega-1 hydroxylase activity | PTHR24291 (none) | - | - | - |
| DCN | 1 | COMPLETE | GO:0005518 collagen binding; GO:0050431 transforming growth factor beta binding; GO:0001968 fibronectin binding | PTHR45712 (none) | - | - | - |
| DHDDS | 1 | DRAFT | GO:0045547 ditrans,polycis-polyprenyl diphosphate synthase [(2E,6E)-farnesyl diphosphate specific] activity | PTHR10291 (COMPLETE) | dolichyl_phosphate_biosynthesis | 0 / 1 | - |
| DNAJC30 | 2 | DRAFT | GO:0140260 mitochondrial proton-transporting ATP synthase complex binding | PTHR44873 (none) | - | - | - |
| DNMBP | 1 | - | - | PTHR22834 (none) | - | - | - |
| EFEMP1 | 1 | DRAFT | GO:0005201 extracellular matrix structural constituent; GO:0005154 epidermal growth factor receptor binding | PTHR24050 (none) | - | - | worm mup-4 (COMPLETE) |
| ELOVL4 | 1 | DRAFT | GO:0009922 fatty acid elongase activity | PTHR11157 (COMPLETE) | fatty_acid_elongation_cycle | - | - |
| EYS | 1 | COMPLETE | GO:0005201 extracellular matrix structural constituent | PTHR12916 (none) | - | - | worm glp-1 (COMPLETE) |
| FBN1 | 1 | DRAFT | GO:0005201 extracellular matrix structural constituent; GO:0042802 identical protein binding; GO:0005509 calcium ion binding; GO:0005178 integrin binding; GO:0005179 hormone activity | PTHR47333 (none) | - | - | worm mup-4 (COMPLETE) |
| FBN2 | 1 | DRAFT | GO:0005201 extracellular matrix structural constituent; GO:0005509 calcium ion binding; GO:0005179 hormone activity | PTHR47333 (none) | - | - | worm mup-4 (COMPLETE) |
| FLVCR1 | 1 | DRAFT | GO:0015220 choline transmembrane transporter activity; GO:0034228 ethanolamine transmembrane transporter activity | PTHR10924 (none) | - | 0 / 2 | - |
| FOXC1 | 1 | DRAFT | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific; GO:0061629 RNA polymerase II-specific DNA-binding transcription factor binding | PTHR11829 (none) | - | - | - |
| FOXE3 | 3 | COMPLETE | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | PTHR11829 (none) | - | - | - |
| FTL | 1 | DRAFT | GO:0008199 ferric iron binding; GO:0005198 structural molecule activity; GO:0008198 ferrous iron binding | PTHR11431 (none) | - | - | DROME Fer3HCH (COMPLETE) |
| FZD4 | 1 | DRAFT | GO:0042813 Wnt receptor activity; GO:0004896 cytokine receptor activity | PTHR11309 (NEEDS_REVIEW) | - | - | - |
| FZD5 | 1 | - | - | PTHR11309 (NEEDS_REVIEW) | - | - | DROME fz2 (COMPLETE) |
| GCNT2 | 1 | - | - | PTHR19297 (none) | - | - | - |
| GDF3 | 1 | - | - | PTHR11848 (none) | - | - | - |
| GDF6 | 1 | - | - | PTHR11848 (none) | - | - | - |
| GJA8 | 1 | - | - | PTHR11984 (none) | - | - | - |
| GNAT1 | 1 | COMPLETE | GO:0003925 G protein activity | PTHR10218 (COMPLETE) | visual_phototransduction | 1 / 1 | - |
| GNAT2 | 2 | COMPLETE | GO:0003925 G protein activity | PTHR10218 (COMPLETE) | visual_phototransduction | 5 / 5 | - |
| GNB3 | 1 | COMPLETE | GO:0003925 G protein activity (contributes) | PTHR19850 (COMPLETE) | visual_phototransduction | - | - |
| GPR179 | 1 | COMPLETE | GO:0043495 protein-membrane adaptor activity | PTHR32546 (COMPLETE) | - | 1 / 1 | - |
| GRHL2 | 1 | - | - | PTHR11037 (none) | - | - | - |
| GRK1 | 1 | COMPLETE | GO:0050254 rhodopsin kinase activity | PTHR24355 (COMPLETE) | visual_phototransduction | - | - |
| GRM6 | 1 | COMPLETE | GO:0098988 G protein-coupled glutamate receptor activity | PTHR24060 (COMPLETE) | - | - | - |
| GUCA1A | 3 | DRAFT | GO:0030249 guanylate cyclase regulator activity | PTHR23055 (none) | visual_phototransduction | - | - |
| GUCY2D | 4 | DRAFT | GO:0004383 guanylate cyclase activity | PTHR11920 (none) | visual_phototransduction | - | - |
| HSF4 | 1 | - | - | PTHR10015 (none) | - | - | worm hsf-1 (COMPLETE), yeast HSF1 (COMPLETE) |
| IDH3B | 1 | COMPLETE | GO:0005198 structural molecule activity | PTHR11835 (COMPLETE) | - | - | yeast IDH1 (DRAFT), SCHPO idh1 (DRAFT) |
| IHH | 1 | - | - | PTHR11889 (NEEDS_REVIEW) | hedgehog_signaling | - | DROME hh (DRAFT) |
| IMPDH1 | 1 | INITIALIZED | GO:0003938 IMP dehydrogenase activity | PTHR11911 (COMPLETE) | purine_nucleotide_interconversion | - | yeast IMD2 (COMPLETE), yeast IMD4 (COMPLETE), yeast IMD3 (COMPLETE) |
| IMPG1 | 2 | - | - | PTHR12199 (none) | - | - | - |
| IMPG2 | 1 | - | - | PTHR12199 (none) | - | - | - |
| IRX1 | 1 | - | - | PTHR11211 (none) | - | - | - |
| KCNJ13 | 1 | - | - | PTHR11767 (none) | - | 0 / 1 | - |
| KCNV2 | 1 | COMPLETE | GO:0005249 voltage-gated potassium channel activity (contributes) | PTHR11537 (none) | - | - | - |
| KIF11 | 1 | - | - | PTHR47970 (none) | - | 0 / 1 | SCHPO cut7 (DRAFT) |
| KIZ | 1 | - | - | PTHR16299 (none) | - | - | - |
| LCA5 | 1 | - | - | PTHR16650 (none) | - | - | - |
| LRIT3 | 1 | COMPLETE | - | PTHR45842 (none) | - | - | - |
| LRP5 | 1 | COMPLETE | GO:0042813 Wnt receptor activity; GO:0015026 coreceptor activity | PTHR46513 (none) | - | - | - |
| LTBP2 | 1 | - | - | PTHR24034 (none) | - | - | - |
| MAB21L2 | 2 | - | - | PTHR10656 (none) | - | - | - |
| MAF | 1 | - | - | PTHR10129 (none) | efferocytosis_induced_macrophage_proliferation | - | - |
| MAK | 1 | DRAFT | GO:0004674 protein serine/threonine kinase activity | PTHR24055 (COMPLETE) | primary_cilium_life_cycle | - | worm dyf-5 (DRAFT) |
| MCAT | 1 | - | - | PTHR47170 (none) | - | - | yeast MCT1 (COMPLETE), SCHPO mct1 (DRAFT) |
| MERTK | 1 | - | - | PTHR24416 (IN_PROGRESS) | efferocytosis_induced_anti_inflammatory_programme, efferocytosis_induced_macrophage_proliferation, phagocytic_engulfment | - | - |
| MFRP | 1 | - | - | PTHR24251 (COMPLETE) | - | - | - |
| MIEF1 | 1 | - | - | PTHR16451 (none) | - | - | - |
| MIP | 1 | - | - | PTHR19139 (none) | - | - | - |
| MIR204 | 1 | - | - | - | - | - | - |
| MT-ND1 | 1 | COMPLETE | GO:0048039 ubiquinone binding; GO:0008137 NADH dehydrogenase (ubiquinone) activity (contributes) | PTHR11432 (COMPLETE) | mitochondrial_complex_i_core | - | - |
| MT-ND4 | 1 | - | - | PTHR43507 (COMPLETE) | - | - | - |
| MT-ND6 | 1 | COMPLETE | GO:0015078 proton transmembrane transporter activity; GO:0008137 NADH dehydrogenase (ubiquinone) activity (contributes) | PTHR11435 (none) | mitochondrial_complex_i_core | - | - |
| MYOC | 1 | - | - | PTHR23192 (COMPLETE) | - | - | - |
| MYRF | 1 | - | - | PTHR13029 (none) | - | - | - |
| NDP | 2 | - | - | PTHR28611 (none) | - | - | - |
| NHS | 1 | - | - | PTHR23039 (none) | - | - | - |
| NMNAT1 | 1 | INITIALIZED | GO:0000309 nicotinamide-nucleotide adenylyltransferase activity; GO:0004515 nicotinate-nucleotide adenylyltransferase activity | PTHR12039 (COMPLETE) | nad_biosynthesis_salvage | 0 / 1 | DROME Nmnat (DRAFT), yeast NMA2 (COMPLETE), yeast NMA1 (COMPLETE), SCHPO SPAC806.06c (DRAFT) |
| NR2E3 | 1 | - | - | PTHR24083 (none) | - | - | - |
| NYX | 1 | COMPLETE | - | PTHR24369 (none) | - | - | - |
| OAT | 1 | COMPLETE | GO:0004587 L-ornithine transaminase activity | PTHR11986 (COMPLETE) | arginine_catabolism_arginase_pathway, proline_metabolism | - | yeast CAR2 (COMPLETE), SCHPO car2 (COMPLETE) |
| OPA1 | 1 | COMPLETE | GO:0140523 GTPase-dependent fusogenic activity; GO:0180020 membrane bending activity | PTHR11566 (none) | mitochondrial_dynamics | - | DANRE opa1 (COMPLETE), worm eat-3 (IN_PROGRESS), yeast DNM1 (COMPLETE) |
| OPA3 | 1 | - | - | PTHR12499 (none) | - | - | - |
| OPN1LW | 2 | COMPLETE | GO:0008020 G protein-coupled photoreceptor activity; GO:0005502 11-cis retinal binding | PTHR24240 (COMPLETE) | visual_phototransduction | 1 / 1 | - |
| OPN1MW | 1 | COMPLETE | GO:0008020 G protein-coupled photoreceptor activity; GO:0005502 11-cis retinal binding | PTHR24240 (COMPLETE) | visual_phototransduction | 1 / 1 | - |
| OPN1SW | 1 | COMPLETE | GO:0008020 G protein-coupled photoreceptor activity; GO:0005502 11-cis retinal binding | PTHR24240 (COMPLETE) | visual_phototransduction | 1 / 1 | - |
| OPTN | 1 | COMPLETE | GO:0030674 protein-macromolecule adaptor activity; GO:0070530 K63-linked polyubiquitin modification-dependent protein binding | PTHR31553 (none) | mitophagy | - | - |
| OTX2 | 2 | DRAFT | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific; GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | PTHR45793 (none) | body_axis_specification, neural_ectoderm_anteroposterior_specification | - | - |
| OVOL2 | 1 | - | - | PTHR10032 (none) | - | 0 / 1 | - |
| PAX6 | 4 | COMPLETE | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific; GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding; GO:0001221 transcription coregulator binding | PTHR45636 (none) | retinal_determination_network | - | mouse Pax6 (COMPLETE), DANRE pax6a (COMPLETE), DROME ey (COMPLETE) |
| PDE6A | 1 | COMPLETE | GO:0047555 3',5'-cyclic-GMP phosphodiesterase activity | PTHR11347 (COMPLETE) | visual_phototransduction | - | - |
| PDE6B | 1 | COMPLETE | GO:0047555 3',5'-cyclic-GMP phosphodiesterase activity | PTHR11347 (COMPLETE) | visual_phototransduction | - | - |
| PDE6C | 3 | COMPLETE | GO:0047555 3',5'-cyclic-GMP phosphodiesterase activity | PTHR11347 (COMPLETE) | visual_phototransduction | 5 / 5 | - |
| PDE6G | 1 | COMPLETE | GO:0004857 enzyme inhibitor activity | PTHR12122 (COMPLETE) | visual_phototransduction | 1 / 1 | - |
| PDE6H | 1 | COMPLETE | GO:0004857 enzyme inhibitor activity | PTHR12122 (COMPLETE) | visual_phototransduction | 5 / 5 | - |
| PITPNM3 | 1 | - | - | PTHR10658 (none) | - | - | - |
| PITX2 | 1 | - | - | PTHR45882 (none) | - | - | - |
| POC1B | 1 | - | - | PTHR44019 (none) | - | - | - |
| PRDM13 | 1 | - | - | PTHR16515 (COMPLETE) | - | - | - |
| PROM1 | 1 | - | - | PTHR22730 (none) | - | - | DANRE prom1a (COMPLETE) |
| PRPF31 | 1 | - | - | PTHR13904 (none) | - | - | - |
| PRPF8 | 1 | - | - | PTHR11140 (none) | - | - | - |
| PRPH2 | 2 | - | - | PTHR19282 (none) | - | - | - |
| PRSS56 | 1 | - | - | PTHR24252 (none) | - | - | - |
| RAB28 | 1 | - | - | PTHR47978 (none) | - | - | - |
| RAX | 1 | - | - | PTHR46271 (none) | - | - | - |
| RBP4 | 2 | - | - | PTHR11873 (none) | retinoic_acid_metabolism | - | - |
| RCBTB1 | 1 | - | - | PTHR22872 (COMPLETE) | - | - | - |
| RD3 | 1 | COMPLETE | GO:0030251 guanylate cyclase inhibitor activity | PTHR28489 (COMPLETE) | - | - | - |
| RDH12 | 2 | INITIALIZED | GO:0052650 all-trans-retinol dehydrogenase (NADP+) activity; GO:0102354 11-cis-retinol dehydrogenase (NADP+) activity; GO:0050661 NADP binding | PTHR43157 (none) | retinoid_visual_cycle | - | - |
| RDH5 | 1 | INITIALIZED | GO:0106429 11-cis-retinol dehydrogenase (NAD+) activity; GO:0047044 androstan-3-alpha,17-beta-diol dehydrogenase (NAD+) activity | PTHR43313 (none) | retinoid_visual_cycle | - | - |
| RHO | 2 | COMPLETE | GO:0008020 G protein-coupled photoreceptor activity; GO:0005502 11-cis retinal binding | PTHR24240 (COMPLETE) | visual_phototransduction | 1 / 1 | - |
| RLBP1 | 1 | COMPLETE | GO:0005502 11-cis retinal binding; GO:0019841 retinol binding | PTHR10174 (none) | retinoid_visual_cycle | - | - |
| RNU4-2 | 1 | - | - | - | - | - | - |
| RNU6-1 | 1 | - | - | - | - | - | - |
| RNU6-2 | 1 | - | - | - | - | - | - |
| RNU6-8 | 1 | - | - | - | - | - | - |
| RNU6-9 | 1 | - | - | - | - | - | - |
| RP1 | 1 | - | - | PTHR23005 (none) | - | - | - |
| RP2 | 1 | DRAFT | GO:0005096 GTPase activator activity | PTHR15440 (none) | primary_cilium_life_cycle | - | - |
| RPE65 | 1 | INITIALIZED | GO:0052885 all-trans-retinyl-ester hydrolase, 11-cis retinol forming activity; GO:0052884 all-trans-retinyl-palmitate hydrolase, 11-cis retinol forming activity; GO:0005506 iron ion binding; GO:0016853 isomerase activity | PTHR10543 (none) | retinoid_visual_cycle | - | DANRE rpe65a (COMPLETE) |
| RPGR | 2 | - | - | PTHR22872 (COMPLETE) | - | - | - |
| RS1 | 1 | - | - | PTHR46806 (none) | - | - | - |
| SAG | 1 | COMPLETE | GO:0030547 signaling receptor inhibitor activity | PTHR11792 (COMPLETE) | visual_phototransduction | - | DROME krz (DRAFT) |
| SAMD7 | 1 | - | - | PTHR12247 (none) | - | - | - |
| SEMA4A | 1 | - | - | PTHR11036 (none) | - | - | - |
| SLC24A1 | 1 | COMPLETE | GO:0008273 calcium, potassium:sodium antiporter activity | PTHR10846 (COMPLETE) | visual_phototransduction | - | - |
| SLC39A5 | 1 | - | - | PTHR12191 (none) | - | - | - |
| SNRNP200 | 1 | - | - | PTHR47961 (none) | - | - | - |
| SOX2 | 2 | COMPLETE | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | PTHR10270 (none) | germ_layer_specification, maternal_to_zygotic_transition, neural_ectoderm_anteroposterior_specification | - | mouse Sox2 (COMPLETE) |
| SSBP1 | 1 | - | - | PTHR10302 (none) | - | - | DROME mtSSB (COMPLETE) |
| TEK | 1 | - | - | PTHR24416 (IN_PROGRESS) | - | 0 / 5 | - |
| TENM3 | 1 | - | - | PTHR11219 (none) | - | - | - |
| TGFBI | 2 | - | - | PTHR10900 (none) | - | - | - |
| TIMP3 | 1 | - | - | PTHR11844 (none) | - | - | - |
| TMEM126A | 1 | - | - | PTHR16296 (none) | - | - | - |
| TMEM98 | 1 | - | - | PTHR32510 (none) | - | - | - |
| TOPORS | 1 | - | - | PTHR46077 (none) | - | - | - |
| TRPM1 | 1 | COMPLETE | GO:0005261 monoatomic cation channel activity | PTHR13800 (COMPLETE) | - | - | worm gtl-2 (COMPLETE), worm gtl-1 (COMPLETE), worm gon-2 (COMPLETE) |
| TSPAN12 | 1 | - | - | PTHR19282 (none) | - | - | - |
| TTC8 | 1 | COMPLETE | - | PTHR44177 (none) | bbsome | - | worm bbs-8 (COMPLETE) |
| TTLL5 | 2 | - | - | PTHR12241 (none) | - | - | - |
| TULP1 | 1 | - | - | PTHR16517 (none) | - | - | - |
| UBIAD1 | 2 | - | - | PTHR13929 (none) | - | - | - |
| VSX2 | 1 | - | - | PTHR46892 (none) | - | - | - |
| WT1 | 1 | IN_PROGRESS | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific; GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific; GO:0003723 RNA binding | PTHR23235 (none) | - | - | - |
| ZEB1 | 1 | - | - | PTHR24391 (none) | - | - | - |
| ZNF408 | 1 | - | - | PTHR16515 (COMPLETE) | - | - | - |
<!-- END GENERATED: genes -->

## Orthologues

<!-- BEGIN GENERATED: orthologs -->
37 genes have at least one reviewed orthologue. The human rows of the reviewed genes were transferred (ISS, ISO, or the Ensembl Compara route) from 97 proteins of other species, of which 2 have a review here.

Reviewed orthologues, with the core molecular function on each side. "Same term" compares GO ids only; a different term can still be the same biology at another level of the ontology.

| Gene | Core molecular function | Orthologue | Orthologue core molecular function | Same term |
|---|---|---|---|---|
| ABCB6 | GO:0015439 ABC-type heme transporter activity; GO:0140359 ABC-type transporter activity | DROME Hmt-1 (DRAFT, least diverged) | GO:0140359 ABC-type transporter activity; GO:0015439 ABC-type heme transporter activity | yes |
| ALDH1A3 | - | yeast ALD6 (COMPLETE, other) | GO:0140088 acetaldehyde dehydrogenase (NADP+) activity | - |
| ALDH1A3 | - | yeast ALD4 (COMPLETE, other) | GO:0004030 aldehyde dehydrogenase [NAD(P)+] activity; GO:0140088 acetaldehyde dehydrogenase (NADP+) activity | - |
| ALDH1A3 | - | yeast ALD5 (COMPLETE, other) | GO:0004030 aldehyde dehydrogenase [NAD(P)+] activity | - |
| ANGPT1 | - | DROME CG10359 (COMPLETE, other) | - | - |
| ATF6 | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | worm atf-6 (COMPLETE, other) | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | no |
| BBS1 | GO:0031267 small GTPase binding; GO:0005102 signaling receptor binding | worm bbs-1 (COMPLETE, least diverged) | GO:0005198 structural molecule activity | no |
| BBS2 | GO:0140378 protein complex scaffold activity | worm bbs-2 (COMPLETE, least diverged) | GO:0005198 structural molecule activity | no |
| BBS9 | GO:0140378 protein complex scaffold activity | worm bbs-9 (COMPLETE, least diverged) | GO:0030674 protein-macromolecule adaptor activity | no |
| CNGA1 | GO:0005223 intracellularly cGMP-activated cation channel activity (contributes) | worm tax-4 (COMPLETE, other) | GO:0005223 intracellularly cGMP-activated cation channel activity; GO:0030553 cGMP binding | yes |
| CNGA3 | GO:0005223 intracellularly cGMP-activated cation channel activity (contributes) | worm tax-4 (COMPLETE, other) | GO:0005223 intracellularly cGMP-activated cation channel activity; GO:0030553 cGMP binding | yes |
| CNGB1 | GO:0005221 intracellularly cyclic nucleotide-activated monoatomic cation channel activity (contributes); GO:0004857 enzyme inhibitor activity | worm tax-2 (COMPLETE, other) | GO:0005216 monoatomic ion channel activity; GO:0005223 intracellularly cGMP-activated cation channel activity (contributes) | no |
| CNGB3 | GO:0005223 intracellularly cGMP-activated cation channel activity (contributes) | worm tax-2 (COMPLETE, least diverged) | GO:0005216 monoatomic ion channel activity; GO:0005223 intracellularly cGMP-activated cation channel activity (contributes) | yes |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | BOVIN CRYAA (IN_PROGRESS, least diverged) | GO:0044183 protein folding chaperone; GO:0005212 structural constituent of eye lens | yes |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | DANRE cryaa (COMPLETE, least diverged) | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | yes |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | worm hsp-12.3 (IN_PROGRESS, other) | GO:0031072 heat shock protein binding | no |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | worm hsp-12.6 (IN_PROGRESS, other) | GO:0042802 identical protein binding | no |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | worm hsp-16.1 (DRAFT, other) | proposed: holdase chaperone activity | - |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | worm hsp-16.2 (COMPLETE, other) | proposed: holdase chaperone activity | - |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | worm hsp-16.41 (DRAFT, other) | proposed: holdase chaperone activity | - |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | worm hsp-16.48 (DRAFT, other) | proposed: holdase chaperone activity | - |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | DROME Hsp26 (DRAFT, other) | proposed: holdase chaperone activity | - |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | DROME Hsp27 (DRAFT, other) | proposed: holdase chaperone activity | - |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | DROME Hsp22 (DRAFT, other) | GO:0140309 unfolded protein holdase activity | no |
| CRYAA | proposed: holdase chaperone activity; GO:0005212 structural constituent of eye lens | DROME Hsp23 (DRAFT, other) | GO:0140309 unfolded protein holdase activity | no |
| CTNNB1 | GO:0003713 transcription coactivator activity; GO:0045296 cadherin binding; GO:0045294 alpha-catenin binding | mouse Ctnnb1 (COMPLETE, least diverged) | GO:0045296 cadherin binding; GO:0003713 transcription coactivator activity | yes |
| CTNNB1 | GO:0003713 transcription coactivator activity; GO:0045296 cadherin binding; GO:0045294 alpha-catenin binding | rat Ctnnb1 (DRAFT, least diverged) | GO:0045296 cadherin binding; GO:0045294 alpha-catenin binding; GO:0003713 transcription coactivator activity | yes |
| EFEMP1 | GO:0005201 extracellular matrix structural constituent; GO:0005154 epidermal growth factor receptor binding | worm mup-4 (COMPLETE, other) | GO:0098631 cell adhesion mediator activity; GO:0140311 protein sequestering activity | no |
| EYS | GO:0005201 extracellular matrix structural constituent | worm glp-1 (COMPLETE, least diverged) | GO:0004888 transmembrane signaling receptor activity; GO:0003713 transcription coactivator activity | no |
| FBN1 | GO:0005201 extracellular matrix structural constituent; GO:0042802 identical protein binding; GO:0005509 calcium ion binding; GO:0005178 integrin binding; GO:0005179 hormone activity | worm mup-4 (COMPLETE, other) | GO:0098631 cell adhesion mediator activity; GO:0140311 protein sequestering activity | no |
| FBN2 | GO:0005201 extracellular matrix structural constituent; GO:0005509 calcium ion binding; GO:0005179 hormone activity | worm mup-4 (COMPLETE, other) | GO:0098631 cell adhesion mediator activity; GO:0140311 protein sequestering activity | no |
| FTL | GO:0008199 ferric iron binding; GO:0005198 structural molecule activity; GO:0008198 ferrous iron binding | DROME Fer3HCH (COMPLETE, other) | GO:0004322 ferroxidase activity; GO:0140315 iron ion sequestering activity | no |
| FZD5 | - | DROME fz2 (COMPLETE, least diverged) | GO:0042813 Wnt receptor activity | - |
| HSF4 | - | worm hsf-1 (COMPLETE, other) | GO:0003700 DNA-binding transcription factor activity; GO:0043565 sequence-specific DNA binding; GO:0042802 identical protein binding | - |
| HSF4 | - | yeast HSF1 (COMPLETE, other) | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | - |
| IDH3B | GO:0005198 structural molecule activity | yeast IDH1 (DRAFT, least diverged) | GO:0004449 isocitrate dehydrogenase (NAD+) activity (contributes) | no |
| IDH3B | GO:0005198 structural molecule activity | SCHPO idh1 (DRAFT, least diverged) | GO:0004449 isocitrate dehydrogenase (NAD+) activity (contributes) | no |
| IHH | - | DROME hh (DRAFT, other) | GO:0005113 patched binding; GO:0016015 morphogen activity; GO:0140853 cholesterol-protein transferase activity | - |
| IMPDH1 | GO:0003938 IMP dehydrogenase activity | yeast IMD2 (COMPLETE, other) | GO:0003938 IMP dehydrogenase activity | yes |
| IMPDH1 | GO:0003938 IMP dehydrogenase activity | yeast IMD4 (COMPLETE, other) | GO:0003938 IMP dehydrogenase activity | yes |
| IMPDH1 | GO:0003938 IMP dehydrogenase activity | yeast IMD3 (COMPLETE, other) | GO:0003938 IMP dehydrogenase activity | yes |
| KIF11 | - | SCHPO cut7 (DRAFT, least diverged) | GO:0008574 plus-end-directed microtubule motor activity; GO:0008017 microtubule binding | - |
| MAK | GO:0004674 protein serine/threonine kinase activity | worm dyf-5 (DRAFT, other) | GO:0004674 protein serine/threonine kinase activity | yes |
| MCAT | - | yeast MCT1 (COMPLETE, least diverged) | GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity | - |
| MCAT | - | SCHPO mct1 (DRAFT, least diverged) | GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity | - |
| NMNAT1 | GO:0000309 nicotinamide-nucleotide adenylyltransferase activity; GO:0004515 nicotinate-nucleotide adenylyltransferase activity | DROME Nmnat (DRAFT, other) | GO:0000309 nicotinamide-nucleotide adenylyltransferase activity; GO:0004515 nicotinate-nucleotide adenylyltransferase activity; GO:0051787 misfolded protein binding | yes |
| NMNAT1 | GO:0000309 nicotinamide-nucleotide adenylyltransferase activity; GO:0004515 nicotinate-nucleotide adenylyltransferase activity | yeast NMA2 (COMPLETE, other) | GO:0000309 nicotinamide-nucleotide adenylyltransferase activity; GO:0004515 nicotinate-nucleotide adenylyltransferase activity | yes |
| NMNAT1 | GO:0000309 nicotinamide-nucleotide adenylyltransferase activity; GO:0004515 nicotinate-nucleotide adenylyltransferase activity | yeast NMA1 (COMPLETE, other) | GO:0000309 nicotinamide-nucleotide adenylyltransferase activity; GO:0004515 nicotinate-nucleotide adenylyltransferase activity | yes |
| NMNAT1 | GO:0000309 nicotinamide-nucleotide adenylyltransferase activity; GO:0004515 nicotinate-nucleotide adenylyltransferase activity | SCHPO SPAC806.06c (DRAFT, other) | GO:0000309 nicotinamide-nucleotide adenylyltransferase activity; GO:0004515 nicotinate-nucleotide adenylyltransferase activity | yes |
| OAT | GO:0004587 L-ornithine transaminase activity | yeast CAR2 (COMPLETE, least diverged) | GO:0004587 L-ornithine transaminase activity | yes |
| OAT | GO:0004587 L-ornithine transaminase activity | SCHPO car2 (COMPLETE, least diverged) | GO:0004587 L-ornithine transaminase activity | yes |
| OPA1 | GO:0140523 GTPase-dependent fusogenic activity; GO:0180020 membrane bending activity | DANRE opa1 (COMPLETE, least diverged) | GO:0140523 GTPase-dependent fusogenic activity | yes |
| OPA1 | GO:0140523 GTPase-dependent fusogenic activity; GO:0180020 membrane bending activity | worm eat-3 (IN_PROGRESS, least diverged) | GO:0003924 GTPase activity | no |
| OPA1 | GO:0140523 GTPase-dependent fusogenic activity; GO:0180020 membrane bending activity | yeast DNM1 (COMPLETE, other) | GO:0003924 GTPase activity | no |
| PAX6 | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific; GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding; GO:0001221 transcription coregulator binding | mouse Pax6 (COMPLETE, least diverged) | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific; GO:0001227 DNA-binding transcription repressor activity, RNA polymerase II-specific; GO:0001221 transcription coregulator binding | yes |
| PAX6 | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific; GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding; GO:0001221 transcription coregulator binding | DANRE pax6a (COMPLETE, least diverged) | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | yes |
| PAX6 | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific; GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding; GO:0001221 transcription coregulator binding | DROME ey (COMPLETE, other) | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific; GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding | yes |
| PROM1 | - | DANRE prom1a (COMPLETE, least diverged) | - | - |
| RPE65 | GO:0052885 all-trans-retinyl-ester hydrolase, 11-cis retinol forming activity; GO:0052884 all-trans-retinyl-palmitate hydrolase, 11-cis retinol forming activity; GO:0005506 iron ion binding; GO:0016853 isomerase activity | DANRE rpe65a (COMPLETE, least diverged) | GO:0052885 all-trans-retinyl-ester hydrolase, 11-cis retinol forming activity | yes |
| SAG | GO:0030547 signaling receptor inhibitor activity | DROME krz (DRAFT, other) | GO:0001664 G protein-coupled receptor binding; GO:0051019 mitogen-activated protein kinase binding | no |
| SOX2 | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | mouse Sox2 (COMPLETE, least diverged) | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | yes |
| SSBP1 | - | DROME mtSSB (COMPLETE, least diverged) | GO:0003697 single-stranded DNA binding | - |
| TRPM1 | GO:0005261 monoatomic cation channel activity | worm gtl-2 (COMPLETE, other) | GO:0005261 monoatomic cation channel activity | yes |
| TRPM1 | GO:0005261 monoatomic cation channel activity | worm gtl-1 (COMPLETE, other) | GO:0005262 calcium channel activity | no |
| TRPM1 | GO:0005261 monoatomic cation channel activity | worm gon-2 (COMPLETE, other) | GO:0005262 calcium channel activity | no |
| TTC8 | - | worm bbs-8 (COMPLETE, least diverged) | GO:0060090 molecular adaptor activity | - |

Proteins that most human rows were transferred from, for genes with a review (rows, and whether the donor is reviewed):

- ABCA4: UniProtKB:F1MWM0 (8 rows, no review), UniProtKB:O35600 (1 rows, no review)
- ABCB6: UniProtKB:Q9DC29 (5 rows, no review), UniProtKB:O70595 (5 rows, no review)
- BBS1: UniProtKB:Q3V3N7 (6 rows, no review)
- BBS2: UniProtKB:Q9CWF6 (21 rows, no review), UniProtKB:Q98SP7 (1 rows, no review)
- BBS9: UniProtKB:Q811G0 (4 rows, no review)
- BEST1: UniProtKB:O88870 (10 rows, no review)
- CABP4: UniProtKB:Q8VHC5 (1 rows, no review)
- CACNA1F: UniProtKB:G3V9W8 (3 rows, no review)
- CAPN5: UniProtKB:O08688 (1 rows, no review)
- CEP290: UniProtKB:Q6A078 (5 rows, no review), UniProtKB:P85001 (4 rows, no review)
- CERKL: UniProtKB:A2AQH1 (5 rows, no review)
- CFAP418: UniProtKB:Q3UJP5 (2 rows, no review)
- CNGA1: UniProtKB:P29974 (4 rows, no review), UniProtKB:Q00194 (4 rows, no review), UniProtKB:Q28181 (1 rows, no review)
- CNGA3: UniProtKB:Q9ER33 (13 rows, no review), UniProtKB:Q9JJZ8 (1 rows, no review)
- CNGB1: UniProtKB:E1AZ71 (19 rows, no review), UniProtKB:A0A8I5ZN27 (5 rows, no review), UniProtKB:Q28181 (4 rows, no review), UniProtKB:A0A8I5ZN27-2 (2 rows, no review)
- CNGB3: UniProtKB:Q9JJZ9 (1 rows, no review), UniProtKB:Q9JJZ8 (1 rows, no review)
- COL2A1: UniProtKB:P28481 (12 rows, no review)
- COL4A1: UniProtKB:P02463 (1 rows, no review), UniProtKB:F1MA59 (1 rows, no review), UniProtKB:F1KQQ4 (1 rows, no review)
- CRB1: UniProtKB:Q8VHS2 (8 rows, no review)
- CRX: UniProtKB:O54751 (7 rows, no review), UniProtKB:Q9XSK0 (6 rows, no review)
- CTNNB1: UniProtKB:Q02248 (92 rows, reviewed), UniProtKB:Q9WU82 (1 rows, reviewed), UniProtKB:B6V8E6 (1 rows, no review)
- CYP1B1: UniProtKB:Q64429 (39 rows, no review)
- FBN1: UniProtKB:Q61554 (26 rows, no review), UniProtKB:G3V9M6 (4 rows, no review), UniProtKB:Q61554-PRO_0000436884 (1 rows, no review)
- FBN2: UniProtKB:Q61555 (8 rows, no review)
- FOXC1: UniProtKB:Q61572 (41 rows, no review), UniProtKB:Q61850 (2 rows, no review)
- FOXE3: UniProtKB:Q9QY14 (15 rows, no review)
- FTL: UniProtKB:P29391 (2 rows, no review)
- FZD4: UniProtKB:Q61088 (15 rows, no review), UniProtKB:P56706 (2 rows, no review), UniProtKB:Q9QZH0 (1 rows, no review)
- GNAT1: UniProtKB:P04695 (11 rows, no review), UniProtKB:D3ZSS5 (7 rows, no review), UniProtKB:P20612 (2 rows, no review), UniProtKB:Q9DG28 (2 rows, no review)
- GNAT2: UniProtKB:D4AA42 (3 rows, no review), UniProtKB:P04696 (2 rows, no review), UniProtKB:P50149 (2 rows, no review)
- GNB3: UniProtKB:Q61011 (2 rows, no review), UniProtKB:P52287 (2 rows, no review)
- GPR179: UniProtKB:E9PY61 (3 rows, no review)
- GRK1: UniProtKB:Q9WVL4 (1 rows, no review), UniProtKB:P28327 (1 rows, no review)
- GRM6: UniProtKB:Q5NCH9 (4 rows, no review), UniProtKB:P35349 (3 rows, no review)
- GUCA1A: UniProtKB:P46065 (5 rows, no review), UniProtKB:P43081 (3 rows, no review)
- GUCY2D: UniProtKB:P51840 (7 rows, no review)
- LRIT3: UniProtKB:W8DXL4 (5 rows, no review)
- LRP5: UniProtKB:Q91VN0 (6 rows, no review), UniProtKB:F1MAD0 (2 rows, no review)
- MAK: UniProtKB:Q04859 (6 rows, no review)
- MT-ND1: UniProtKB:P03887 (1 rows, no review), UniProtKB:P03888 (1 rows, no review)
- MT-ND6: UniProtKB:P03925 (3 rows, no review), UniProtKB:P03924 (1 rows, no review)
- NYX: UniProtKB:P83503 (1 rows, no review)
- OPA1: UniProtKB:P58281 (17 rows, no review)
- OPN1MW: UniProtKB:P04000 (2 rows, no review), UniProtKB:O35599 (1 rows, no review)
- OPN1SW: UniProtKB:P51491 (3 rows, no review), UniProtKB:P04000 (2 rows, no review)
- OTX2: UniProtKB:P80206 (4 rows, no review), UniProtKB:Q91981 (1 rows, no review)
- PDE6A: UniProtKB:P11541 (3 rows, no review), UniProtKB:P23439 (1 rows, no review)
- PDE6B: UniProtKB:P23440 (3 rows, no review), UniProtKB:P23439 (3 rows, no review), UniProtKB:P11541 (1 rows, no review), UniProtKB:D3ZDI8 (1 rows, no review)
- PDE6C: UniProtKB:Q91ZQ1 (3 rows, no review)
- PDE6G: UniProtKB:P04972 (4 rows, no review), UniProtKB:M0R4R9 (1 rows, no review)
- PDE6H: UniProtKB:P22571 (1 rows, no review), UniProtKB:P61249 (1 rows, no review), UniProtKB:Q91ZQ1 (1 rows, no review)
- RD3: UniProtKB:Q8BRE0 (8 rows, no review)
- RHO: UniProtKB:P02699 (7 rows, no review), UniProtKB:P15409 (5 rows, no review)
- RP2: UniProtKB:Q9EPK2 (3 rows, no review)
- SAG: UniProtKB:P20443 (3 rows, no review), UniProtKB:P15887 (1 rows, no review)
- SLC24A1: UniProtKB:Q9IAL8 (3 rows, no review), UniProtKB:Q91WD8 (2 rows, no review)
<!-- END GENERATED: orthologs -->

## Entry-by-entry alignment

The flags are those of the metabolic project. The four that describe the dismech entry
alone are `UNTYPED` (the gene record has no relationship type), `NO_ORIGIN` (no variant
origin), `GENE_ON_NO_NODE` (no mechanism node names the gene) and `NO_GO_ON_GENE_NODES`
(the nodes that name it carry no GO term). `NO_AIGR_REVIEW` and `AIGR_NOT_COMPLETE`
describe this repository. `NO_GO_ALIGNMENT` is the one that marks a possible
disagreement: the gene's nodes carry GO terms and none of them relates to a core
function in the review.

<!-- BEGIN GENERATED: audit -->
Audit run 2026-11-27T02:54:09Z over dismech `d0025c519` and ai-gene-review `41fdc3971` (GO adapter `sqlite:obo:go`, ai-gene-review tree had uncommitted changes). 126 entries, 224 gene rows, 215 of them causal or untyped.

Flag counts on causal and untyped rows: `NO_ORIGIN` 123, `NO_AIGR_REVIEW` 92, `UNTYPED` 49, `NO_MODULE_MEMBERSHIP` 47, `AIGR_NOT_COMPLETE` 44, `NO_GO_ON_GENE_NODES` 41, `ALIGNED_ON_SHARED_NODE_ONLY` 31, `PARTIAL_ALIGNMENT` 26, `GENE_ON_NO_NODE` 23, `NO_GO_ALIGNMENT` 14, `ALIGNED_NONCORE` 8, `MODULE_NOT_COVERING` 1.

| Entry | Gene | Relationship | Nodes | Review | Aligned node terms (node->core) | Unaligned node terms | Flags |
|---|---|---|---|---|---|---|---|
| ADAM9-Related_Retinopathy | ADAM9 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| AIPL1-Related_Retinopathy | AIPL1 | untyped | 1 | DRAFT | - | GO:0051087 | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE, NO_GO_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| ATF6-Related_Retinopathy | ATF6 | CAUSATIVE | 1 | COMPLETE | GO:0036500 | - | ok |
| Achromatopsia | CNGA3 | CAUSATIVE | 1 | DRAFT | GO:0007603->GO:0007602 | - | AIGR_NOT_COMPLETE, ALIGNED_ON_SHARED_NODE_ONLY |
| Achromatopsia | CNGB3 | CAUSATIVE | 1 | COMPLETE | GO:0007603->GO:0007602 | - | ALIGNED_ON_SHARED_NODE_ONLY |
| Achromatopsia | GNAT2 | CAUSATIVE | 1 | COMPLETE | GO:0007603->GO:0141190 | - | ok |
| Achromatopsia | PDE6C | CAUSATIVE | 1 | COMPLETE | GO:0007603->GO:0141190 | - | ok |
| Achromatopsia | PDE6H | CAUSATIVE | 1 | COMPLETE | GO:0007603->GO:0141190 | - | ok |
| Achromatopsia | ATF6 | CAUSATIVE | 1 | COMPLETE | - | - | NO_GO_ON_GENE_NODES |
| Aland_Island_Eye_Disease | CACNA1F | CAUSATIVE | 1 | COMPLETE | GO:0005245->GO:0008331 GO:0070588->GO:0008331/GO:0098703 | - | NO_MODULE_MEMBERSHIP |
| Aniridia | PAX6 | CAUSATIVE | 2 | COMPLETE | GO:0003700->GO:0000981 | GO:0010467 GO:0043010 | NO_ORIGIN, PARTIAL_ALIGNMENT |
| Aniridia | WT1 | CAUSATIVE | 1 | IN_PROGRESS | GO:0003700->GO:0000981/GO:0001228 | - | NO_ORIGIN, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Aniridia | TRIM44 | UNKNOWN | 0 | - | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Autosomal_Dominant_Optic_Atrophy | OPA1 | CAUSATIVE | 1 | COMPLETE | - | - | NO_GO_ON_GENE_NODES |
| Autosomal_Recessive_Optic_Atrophy_OPA7_Type | TMEM126A | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| BBSome-Related_Retinitis_Pigmentosa | ARL6 | untyped | 1 | COMPLETE | GO:0061512 | - | UNTYPED, NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| BBSome-Related_Retinitis_Pigmentosa | TTC8 | untyped | 1 | COMPLETE | - | GO:0061512 | UNTYPED, NO_ORIGIN, NO_GO_ALIGNMENT |
| BBSome-Related_Retinitis_Pigmentosa | BBS1 | untyped | 1 | COMPLETE | GO:0061512 | - | UNTYPED, NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| BBSome-Related_Retinitis_Pigmentosa | BBS2 | untyped | 1 | COMPLETE | GO:0061512 | - | UNTYPED, NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| BBSome-Related_Retinitis_Pigmentosa | BBS9 | untyped | 1 | COMPLETE | GO:0061512 | - | UNTYPED, NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| BEST1-Related_Dominant_Retinopathy | BEST1 | untyped | 1 | COMPLETE | GO:0005229->GO:0005229/GO:1902476 GO:0006821->GO:0005229/GO:1902476 | - | UNTYPED, NO_ORIGIN, NO_MODULE_MEMBERSHIP |
| BEST1-related_Vitreoretinochoroidopathy | BEST1 | CAUSATIVE | 1 | COMPLETE | GO:0005229->GO:0005229/GO:1902476 | - | NO_MODULE_MEMBERSHIP |
| BEST1_Bestrophinopathies | BEST1 | untyped | 2 | COMPLETE | GO:0005229->GO:0005229/GO:1902476 GO:0006821->GO:0005229/GO:1902476 | - | UNTYPED, NO_ORIGIN, NO_MODULE_MEMBERSHIP |
| Bietti_Crystalline_Dystrophy | CYP4V2 | CAUSATIVE | 0 | DRAFT | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Blue_Cone_Monochromacy | OPN1LW | CAUSATIVE | 3 | COMPLETE | GO:0007602->GO:0141190 GO:0008020 | GO:0006355 | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Blue_Cone_Monochromacy | OPN1MW | CAUSATIVE | 3 | COMPLETE | GO:0007602->GO:0141190 GO:0008020 | GO:0006355 | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Blue_Cone_Monochromacy | OPN1LW | CAUSATIVE | 3 | COMPLETE | GO:0007602->GO:0141190 GO:0008020 | GO:0006355 | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Blue_Cone_Monochromacy | OPN1MW | CAUSATIVE | 3 | COMPLETE | GO:0007602->GO:0141190 GO:0008020 | GO:0006355 | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Blue_Cone_Monochromacy | OPN1LW | CAUSATIVE | 3 | COMPLETE | GO:0007602->GO:0141190 GO:0008020 | GO:0006355 | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Blue_Cone_Monochromacy | OPN1LW | CAUSATIVE | 3 | COMPLETE | GO:0007602->GO:0141190 GO:0008020 | GO:0006355 | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Blue_Cone_Monochromacy | OPN1LW | CAUSATIVE | 3 | COMPLETE | GO:0007602->GO:0141190 GO:0008020 | GO:0006355 | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| CACNA1F-Related_Retinopathy | CACNA1F | CAUSATIVE | 0 | COMPLETE | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| CACNA2D4-related_Retinopathy | CACNA2D4 | CAUSATIVE | 1 | COMPLETE | GO:0005246 | - | NO_MODULE_MEMBERSHIP |
| CAPN5-Related_Vitreoretinopathy | CAPN5 | CAUSATIVE | 1 | DRAFT | GO:0004198 | - | NO_ORIGIN, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| CERKL-Related_Retinopathy | CERKL | untyped | 0 | COMPLETE | - | - | UNTYPED, NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| CFAP418-related_Retinal_Ciliopathy | CFAP418 | untyped | 1 | DRAFT | - | GO:0061512 | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE, NO_GO_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| CNGA1-Related_Retinopathy | CNGA1 | CAUSATIVE | 1 | COMPLETE | GO:0005223->GO:0098655 | - | ok |
| CNGA3-Related_Retinopathy | CNGA3 | CAUSATIVE | 4 | DRAFT | GO:0005223->GO:0098655 | GO:1903546 | NO_ORIGIN, AIGR_NOT_COMPLETE, PARTIAL_ALIGNMENT |
| CNGA3-Related_Retinopathy | CNGA3 | MODIFIER | 4 | DRAFT | GO:0005223->GO:0098655 | GO:1903546 | NO_ORIGIN, AIGR_NOT_COMPLETE, PARTIAL_ALIGNMENT |
| CNGB1-Related_Retinopathy | CNGB1 | CAUSATIVE | 1 | DRAFT | - | - | NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE |
| CNGB3-Related_Retinopathy | CNGB3 | CAUSATIVE | 1 | COMPLETE | GO:0005223->GO:0098655 | - | NO_ORIGIN |
| CRB1_Retinal_Dystrophies | CRB1 | CAUSATIVE | 2 | DRAFT | GO:0007163->GO:0045197 | GO:0034332 | NO_ORIGIN, AIGR_NOT_COMPLETE, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| CRX_Related_Retinopathy | CRX | untyped | 0 | DRAFT | - | - | UNTYPED, NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Cataract_12_Multiple_Types | BFSP2 | CAUSATIVE | 2 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Cataract_13_With_Adult_I_Phenotype | GCNT2 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Cataract_15 | MIP | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Cataract_1_Multiple_Types | GJA8 | CAUSATIVE | 2 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Cataract_21_Multiple_Types | MAF | CAUSATIVE | 2 | - | - | - | NO_AIGR_REVIEW |
| Cataract_2_Multiple_Types | CRYGC | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Cataract_31_Multiple_Types | CHMP4B | CAUSATIVE | 1 | COMPLETE | GO:0180020 | - | NO_ORIGIN |
| Cataract_33 | BFSP1 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Cataract_39_Multiple_Types | CRYGB | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Cataract_3_Multiple_Types | CRYBB2 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Cataract_40 | NHS | CAUSATIVE | 2 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Cataract_48 | DNMBP | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Cataract_4_Multiple_Types | CRYGD | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Cataract_5_Multiple_Types | HSF4 | CAUSATIVE | 3 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Cataract_9_Multiple_Types | CRYAA | CAUSATIVE | 2 | COMPLETE | GO:0005212 | GO:0044183 | NO_ORIGIN, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Central_Areolar_Choroidal_Dystrophy | PRPH2 | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Central_Areolar_Choroidal_Dystrophy | GUCY2D | untyped | 1 | DRAFT | GO:0004383->GO:0004383/GO:0006182 | GO:0005509 GO:0007602 GO:0030250 | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE, ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Central_Areolar_Choroidal_Dystrophy | GUCA1A | untyped | 1 | DRAFT | GO:0030250->GO:0030249 | GO:0004383 GO:0005509 GO:0007602 | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE, ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Choroideremia | CHM | CAUSATIVE | 0 | DRAFT | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Cone-rod_Dystrophy_10 | SEMA4A | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Cone-rod_Dystrophy_20 | POC1B | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Cone-rod_Dystrophy_5 | PITPNM3 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Cone_Dystrophy | GUCA1A | CAUSATIVE | 0 | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE |
| Cone_Dystrophy | GUCY2D | CAUSATIVE | 0 | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE |
| Cone_Dystrophy | PDE6C | CAUSATIVE | 0 | COMPLETE | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Cone_Dystrophy | RPGR | CAUSATIVE | 0 | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Cone_Dystrophy | TTLL5 | CAUSATIVE | 0 | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Cone_Dystrophy | CNGA3 | CAUSATIVE | 0 | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE |
| Cone_Dystrophy | CNGB3 | CAUSATIVE | 0 | COMPLETE | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Congenital_Glaucoma | CYP1B1 | CAUSATIVE | 1 | COMPLETE | GO:0001523->GO:0042572/GO:0042574 GO:0004497->GO:0008395/GO:0016712 | - | NO_MODULE_MEMBERSHIP |
| Congenital_Glaucoma | LTBP2 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Congenital_Glaucoma | TEK | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Congenital_Glaucoma | ANGPT1 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Congenital_Glaucoma | FOXC1 | CAUSATIVE | 1 | DRAFT | - | GO:0001755 GO:0002930 | AIGR_NOT_COMPLETE, ALIGNED_NONCORE, NO_MODULE_MEMBERSHIP |
| Congenital_Glaucoma | PITX2 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Congenital_Glaucoma | PAX6 | CAUSATIVE | 1 | COMPLETE | - | GO:0001755 GO:0002930 | ALIGNED_NONCORE |
| Congenital_Glaucoma | SVEP1 | MODIFIER | 0 | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Congenital_Stationary_Night_Blindness | NYX | CAUSATIVE | 1 | COMPLETE | - | GO:0007216 GO:0050808 | NO_ORIGIN, NO_GO_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Congenital_Stationary_Night_Blindness | GRM6 | CAUSATIVE | 1 | COMPLETE | GO:0007216 | GO:0050808 | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Congenital_Stationary_Night_Blindness | TRPM1 | CAUSATIVE | 1 | COMPLETE | GO:0007216 | GO:0050808 | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Congenital_Stationary_Night_Blindness | LRIT3 | CAUSATIVE | 1 | COMPLETE | GO:0050808->GO:0099084 | GO:0007216 | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Congenital_Stationary_Night_Blindness | GPR179 | CAUSATIVE | 1 | COMPLETE | GO:0007216 | GO:0050808 | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Congenital_Stationary_Night_Blindness | CACNA1F | CAUSATIVE | 1 | COMPLETE | GO:0070588->GO:0008331/GO:0098703 | GO:0007269 | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Congenital_Stationary_Night_Blindness | CABP4 | CAUSATIVE | 1 | COMPLETE | - | GO:0007269 GO:0070588 | NO_ORIGIN, NO_GO_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Congenital_Stationary_Night_Blindness | GNAT1 | CAUSATIVE | 1 | COMPLETE | GO:0007602->GO:0141190 | - | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| Congenital_Stationary_Night_Blindness | GNB3 | CAUSATIVE | 1 | COMPLETE | GO:0007602->GO:0141190 | - | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| Congenital_Stationary_Night_Blindness | RHO | CAUSATIVE | 1 | COMPLETE | GO:0007602->GO:0141190 | - | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| Congenital_Stationary_Night_Blindness | SAG | CAUSATIVE | 1 | COMPLETE | GO:0016059 | - | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| Congenital_Stationary_Night_Blindness | GRK1 | CAUSATIVE | 1 | COMPLETE | GO:0016059 | - | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| Congenital_Stationary_Night_Blindness | SLC24A1 | CAUSATIVE | 1 | COMPLETE | - | GO:0007602 | NO_ORIGIN, NO_GO_ALIGNMENT |
| Congenital_Stationary_Night_Blindness | PDE6B | CAUSATIVE | 1 | COMPLETE | GO:0007602->GO:0141190 | - | NO_ORIGIN, ALIGNED_ON_SHARED_NODE_ONLY |
| Congenital_Stationary_Night_Blindness | GUCY2D | CAUSATIVE | 1 | DRAFT | - | GO:0007602 | NO_ORIGIN, AIGR_NOT_COMPLETE, NO_GO_ALIGNMENT |
| Doyne_Honeycomb_Retinal_Dystrophy | EFEMP1 | CAUSATIVE | 1 | DRAFT | GO:0005201 | GO:0006457 GO:0009306 | AIGR_NOT_COMPLETE, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| EYS_Related_Retinitis_Pigmentosa | EYS | untyped | 1 | COMPLETE | GO:0045494 | GO:0060271 | UNTYPED, NO_ORIGIN, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Ectopia_Lentis_1_Isolated_Autosomal_Dominant | FBN1 | CAUSATIVE | 1 | DRAFT | GO:0005201 | - | NO_ORIGIN, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Enhanced_S-Cone_Syndrome | NR2E3 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| FLVCR1-Related_Retinopathy | FLVCR1 | CAUSATIVE | 0 | DRAFT | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| FOXE3_Anterior_Segment_Dysgenesis | FOXE3 | untyped | 1 | COMPLETE | GO:0000981 | GO:0002088 GO:0070306 | UNTYPED, NO_ORIGIN, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Familial_Exudative_Vitreoretinopathy | FZD4 | CAUSATIVE | 1 | DRAFT | GO:0060070 GO:0110135 | - | NO_ORIGIN, AIGR_NOT_COMPLETE, ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| Familial_Exudative_Vitreoretinopathy | NDP | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Familial_Exudative_Vitreoretinopathy | LRP5 | CAUSATIVE | 2 | COMPLETE | GO:0060070 GO:0110135 | - | NO_ORIGIN, NO_MODULE_MEMBERSHIP |
| Familial_Exudative_Vitreoretinopathy | TSPAN12 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Familial_Exudative_Vitreoretinopathy | KIF11 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Familial_Exudative_Vitreoretinopathy | ZNF408 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Familial_Exudative_Vitreoretinopathy | CTNNB1 | CAUSATIVE | 1 | DRAFT | GO:0060070 | GO:0110135 | NO_ORIGIN, AIGR_NOT_COMPLETE, ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Familial_Progressive_Retinal_Dystrophy-iris_Coloboma-congenital_Cataract_Syndrome | MIR204 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| GNAT2-Related_Retinopathy | GNAT2 | CAUSATIVE | 1 | COMPLETE | GO:0003925 GO:0141190 | - | ok |
| GUCA1A-Related_Retinopathy | GUCA1A | untyped | 2 | DRAFT | - | GO:0005513 GO:0006182 | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE, NO_GO_ALIGNMENT |
| GUCY2D-Related_Retinopathy | GUCY2D | untyped | 2 | DRAFT | GO:0004383->GO:0004383/GO:0006182 GO:0006182->GO:0004383/GO:0006182 | - | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE |
| Hereditary_Hyperferritinemia_With_Congenital_Cataracts | FTL | CAUSATIVE | 1 | DRAFT | - | - | NO_ORIGIN, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| IDH3B-Related_Retinopathy | IDH3B | untyped | 1 | COMPLETE | - | GO:0004449 | UNTYPED, NO_GO_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| IMPDH1-Related_Retinopathy | IMPDH1 | CAUSATIVE | 1 | INITIALIZED | GO:0003938 | - | AIGR_NOT_COMPLETE |
| IMPG1-related_Dominant_Retinopathy | IMPG1 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| IMPG1-related_Recessive_Retinopathy | IMPG1 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| IMPG2-related_Recessive_Retinopathy | IMPG2 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | SOX2 | CAUSATIVE | 1 | COMPLETE | - | GO:0060898 GO:0060900 | NO_ORIGIN, ALIGNED_NONCORE |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | OTX2 | CAUSATIVE | 1 | DRAFT | - | GO:0060898 GO:0060900 | NO_ORIGIN, AIGR_NOT_COMPLETE, NO_GO_ALIGNMENT |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | RAX | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | VSX2 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | ALDH1A3 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | FOXE3 | CAUSATIVE | 1 | COMPLETE | - | GO:0060898 GO:0060900 | NO_ORIGIN, ALIGNED_NONCORE, NO_MODULE_MEMBERSHIP |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | PAX6 | CAUSATIVE | 1 | COMPLETE | - | GO:0060898 GO:0060900 | NO_ORIGIN, ALIGNED_NONCORE |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | MAB21L2 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | GDF6 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | GDF3 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | MFRP | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | PRSS56 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | MYRF | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Isolated_Anophthalmia-Microphthalmia_Syndrome | TMEM98 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Juvenile_Open_Angle_Glaucoma | MYOC | CAUSATIVE | 0 | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Juvenile_Open_Angle_Glaucoma | CYP1B1 | CAUSATIVE | 1 | COMPLETE | GO:0004497->GO:0008395/GO:0016712 | - | NO_MODULE_MEMBERSHIP |
| KCNV2_Related_Retinopathy | KCNV2 | CAUSATIVE | 1 | COMPLETE | GO:0005249->GO:0071805 GO:0071805 | - | NO_MODULE_MEMBERSHIP |
| KIZ-related_Retinopathy | KIZ | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| LCA5-Related_Retinopathy | LCA5 | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Leber-like_Hereditary_Optic_Neuropathy_Autosomal_Recessive_1 | DNAJC30 | CAUSATIVE | 1 | DRAFT | GO:0034367 | GO:0019899 | AIGR_NOT_COMPLETE, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Leber_Congenital_Amaurosis_10 | CEP290 | untyped | 0 | DRAFT | - | - | UNTYPED, NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE |
| Leber_Congenital_Amaurosis_13 | RDH12 | CAUSATIVE | 1 | INITIALIZED | - | - | NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE |
| Leber_Congenital_Amaurosis_16 | KCNJ13 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Leber_Congenital_Amaurosis_9 | NMNAT1 | CAUSATIVE | 1 | INITIALIZED | GO:0000309 | - | AIGR_NOT_COMPLETE |
| Leber_Hereditary_Optic_Neuropathy | MT-ND4 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Leber_Hereditary_Optic_Neuropathy | MT-ND1 | CAUSATIVE | 1 | COMPLETE | GO:0008137->GO:1902600 | - | ALIGNED_ON_SHARED_NODE_ONLY |
| Leber_Hereditary_Optic_Neuropathy | MT-ND6 | CAUSATIVE | 1 | COMPLETE | GO:0008137->GO:0015078/GO:1902600 | - | ALIGNED_ON_SHARED_NODE_ONLY |
| Leber_Hereditary_Optic_Neuropathy | DNAJC30 | CAUSATIVE | 1 | DRAFT | - | GO:0008137 | AIGR_NOT_COMPLETE, NO_GO_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Leber_Hereditary_Optic_Neuropathy | NQO1 | MODIFIER | 0 | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| MAK-related_Retinopathy | MAK | CAUSATIVE | 1 | DRAFT | GO:0004674 | - | AIGR_NOT_COMPLETE |
| MERTK-Related_Retinopathy | MERTK | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Macular_Degeneration_Early-onset | FBN2 | CAUSATIVE | 1 | DRAFT | GO:0005201 | - | AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Macular_Dystrophy_With_Or_Without_Cone_Dysfunction | SAMD7 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Microphthalmia_with_Coloboma | SOX2 | untyped | 1 | COMPLETE | - | GO:0001654 GO:0048592 GO:0048593 | UNTYPED, NO_ORIGIN, ALIGNED_NONCORE |
| Microphthalmia_with_Coloboma | OTX2 | untyped | 2 | DRAFT | - | GO:0001654 GO:0048592 GO:0048593 | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE, NO_GO_ALIGNMENT |
| Microphthalmia_with_Coloboma | PAX6 | untyped | 1 | COMPLETE | - | GO:0001654 GO:0048592 GO:0048593 | UNTYPED, NO_ORIGIN, ALIGNED_NONCORE |
| Microphthalmia_with_Coloboma | MAB21L2 | untyped | 2 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Microphthalmia_with_Coloboma | FZD5 | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Microphthalmia_with_Coloboma | FOXE3 | untyped | 1 | COMPLETE | - | GO:0001654 GO:0048592 GO:0048593 | UNTYPED, NO_ORIGIN, ALIGNED_NONCORE, NO_MODULE_MEMBERSHIP |
| Microphthalmia_with_Coloboma | ALDH1A3 | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Microphthalmia_with_Coloboma | ABCB6 | CAUSATIVE | 1 | COMPLETE | - | GO:0048593 GO:0061386 | NO_ORIGIN, NO_GO_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Microphthalmia_with_Coloboma | TENM3 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Microphthalmia_with_Coloboma | RBP4 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Microphthalmia_with_Coloboma | IHH | CAUSATIVE | 1 | - | - | - | NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Myopia_24_Autosomal_Dominant | SLC39A5 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| NDP_Related_Vitreoretinopathy | NDP | untyped | 0 | - | - | - | UNTYPED, NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| North_Carolina_Macular_Dystrophy | PRDM13 | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| North_Carolina_Macular_Dystrophy | IRX1 | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| OPTN-related_Open_Angle_Glaucoma | OPTN | CAUSATIVE | 0 | COMPLETE | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| OPTN-related_Open_Angle_Glaucoma | OPTN | SUSCEPTIBILITY | 0 | COMPLETE | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Optic_Atrophy_13_With_Retinal_And_Foveal_Abnormalities | SSBP1 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Optic_Atrophy_14 | MIEF1 | CAUSATIVE | 1 | - | - | - | NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Optic_Atrophy_15 | MCAT | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Optic_Atrophy_3 | OPA3 | CAUSATIVE | 1 | - | - | - | NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| PDE6A-Related_Retinopathy | PDE6A | CAUSATIVE | 1 | COMPLETE | GO:0047555 | - | ok |
| PDE6C-Related_Retinopathy | PDE6C | CAUSATIVE | 1 | COMPLETE | GO:0007603->GO:0141190 GO:0047555 | - | ok |
| PDE6G-Related_Retinopathy | PDE6G | CAUSATIVE | 1 | COMPLETE | GO:0004857 | - | ok |
| PRPF31-Related_Retinopathy | PRPF31 | CAUSATIVE | 0 | - | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| PRPF31-Related_Retinopathy | CNOT3 | MODIFIER | 0 | DRAFT | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE |
| PRPF8-Related_Retinopathy | PRPF8 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| PRPH2-Related_Retinopathy | PRPH2 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| PRPH2-Related_Retinopathy | ROM1 | MODIFIER | 0 | - | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Posterior_Polymorphous_Corneal_Dystrophy | OVOL2 | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Posterior_Polymorphous_Corneal_Dystrophy | ZEB1 | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Posterior_Polymorphous_Corneal_Dystrophy | COL8A2 | UNKNOWN | 0 | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Posterior_Polymorphous_Corneal_Dystrophy | GRHL2 | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Progressive_Retinal_Dystrophy_Due_To_Retinol_Transport_Defect | RBP4 | CAUSATIVE | 0 | - | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Protan_Color_Vision_Deficiency | OPN1LW | CAUSATIVE | 2 | COMPLETE | GO:0008020 | - | ok |
| RAB28-Related_Retinopathy | RAB28 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| RCBTB1-Related_Retinopathy | RCBTB1 | untyped | 0 | - | - | - | UNTYPED, NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| RD3-Related_Retinopathy | RD3 | CAUSATIVE | 1 | COMPLETE | GO:0030251 | - | NO_MODULE_MEMBERSHIP |
| RDH12-Related_Dominant_Retinopathy | RDH12 | untyped | 2 | INITIALIZED | GO:0052650->GO:0001523/GO:0042572/GO:0052650 | - | UNTYPED, AIGR_NOT_COMPLETE |
| RDH5-Related_Retinopathy | RDH5 | untyped | 1 | INITIALIZED | GO:0001523->GO:0001523/GO:0042572 GO:0042572->GO:0001523/GO:0042572 | - | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE |
| RHO-Related_Retinopathy | RHO | CAUSATIVE | 2 | COMPLETE | GO:0007602->GO:0141190 GO:0008020 GO:0141190 | GO:0006457 GO:0034976 GO:0045494 | PARTIAL_ALIGNMENT |
| RLBP1-Related_Retinopathy | RLBP1 | untyped | 1 | COMPLETE | GO:0005501->GO:0005502/GO:0019841 GO:0019841 | - | UNTYPED, NO_ORIGIN, MODULE_NOT_COVERING |
| RP1-Related_Retinopathy | RP1 | CAUSATIVE | 2 | - | - | - | NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| RP2-Related_Retinopathy | RP2 | untyped | 1 | DRAFT | GO:0005096 | - | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE |
| RPE65-Related_Retinopathy | RPE65 | CAUSATIVE | 1 | INITIALIZED | GO:0001523->GO:0052884/GO:0052885 GO:0042572->GO:0052884/GO:0052885 GO:0052885 | - | AIGR_NOT_COMPLETE |
| RPGR-Related_Retinopathy | RPGR | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| Retinal_Arterial_Tortuosity | COL4A1 | untyped | 0 | COMPLETE | - | - | UNTYPED, NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Retinitis_Pigmentosa_59 | DHDDS | CAUSATIVE | 1 | DRAFT | GO:0045547 | - | AIGR_NOT_COMPLETE, ALIGNED_ON_SHARED_NODE_ONLY |
| Retinitis_Pigmentosa_59 | ALG6 | MODIFIER | 0 | COMPLETE | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Retinitis_Pigmentosa_With_or_Without_Situs_Inversus | ARL2BP | CAUSATIVE | 1 | COMPLETE | - | - | NO_ORIGIN, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| SNRNP200-Related_Dominant_Retinopathy | SNRNP200 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Schnyder_Corneal_Dystrophy | UBIAD1 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Sorsby_Fundus_Dystrophy | TIMP3 | CAUSATIVE | 1 | - | - | - | NO_AIGR_REVIEW |
| Stargardt_Disease | ABCA4 | untyped | 1 | DRAFT | GO:0006869->GO:0045332/GO:0090555/GO:0140347 GO:0140327->GO:0090555/GO:0140347 | - | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Stargardt_Disease | ELOVL4 | untyped | 1 | DRAFT | GO:0009922 | - | UNTYPED, NO_ORIGIN, AIGR_NOT_COMPLETE |
| Stargardt_Disease | PROM1 | untyped | 0 | - | - | - | UNTYPED, NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Stickler_Syndrome_Type_1_Nonsyndromic_Ocular | COL2A1 | CAUSATIVE | 1 | DRAFT | - | GO:0000184 | AIGR_NOT_COMPLETE, NO_GO_ALIGNMENT |
| Stromal_Corneal_Dystrophy | CHST6 | CAUSATIVE | 1 | COMPLETE | - | - | NO_ORIGIN, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| Stromal_Corneal_Dystrophy | UBIAD1 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Stromal_Corneal_Dystrophy | DCN | CAUSATIVE | 1 | COMPLETE | GO:0030198->GO:0030199 | - | NO_ORIGIN, NO_MODULE_MEMBERSHIP |
| Stromal_Corneal_Dystrophy | TGFBI | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| TGFBI_Corneal_Dystrophies | TGFBI | untyped | 1 | - | - | - | UNTYPED, NO_ORIGIN, NO_AIGR_REVIEW |
| TOPORS-Related_Retinopathy | TOPORS | CAUSATIVE | 2 | - | - | - | NO_AIGR_REVIEW |
| TTLL5-Related_Retinopathy | TTLL5 | CAUSATIVE | 1 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| TULP1-Related_Retinopathy | TULP1 | CAUSATIVE | 3 | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| Tritan_Color_Vision_Deficiency | OPN1SW | CAUSATIVE | 3 | COMPLETE | GO:0008020 | GO:0000398 GO:0006457 | PARTIAL_ALIGNMENT |
| U4_and_U6_snRNA_Gene-Related_Retinitis_Pigmentosa | RNU4-2 | CAUSATIVE | 1 | - | - | - | NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| U4_and_U6_snRNA_Gene-Related_Retinitis_Pigmentosa | RNU6-1 | CAUSATIVE | 1 | - | - | - | NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| U4_and_U6_snRNA_Gene-Related_Retinitis_Pigmentosa | RNU6-2 | CAUSATIVE | 1 | - | - | - | NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| U4_and_U6_snRNA_Gene-Related_Retinitis_Pigmentosa | RNU6-8 | CAUSATIVE | 1 | - | - | - | NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| U4_and_U6_snRNA_Gene-Related_Retinitis_Pigmentosa | RNU6-9 | CAUSATIVE | 1 | - | - | - | NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| X-linked_Retinoschisis | RS1 | CAUSATIVE | 0 | - | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| ornithine_aminotransferase_deficiency | OAT | untyped | 1 | COMPLETE | GO:0004587 GO:0055129 | GO:0006591 GO:0006593 | UNTYPED, NO_ORIGIN, PARTIAL_ALIGNMENT |
<!-- END GENERATED: audit -->

## Findings

Dated 2026-11-27. Each item is recorded, with quotes, in the review file named.

### The 22 new gene reviews

746 rows were reviewed (733 from GOA, 13 proposed as NEW): 256 MODIFY, 247 ACCEPT,
95 KEEP_AS_NON_CORE, 73 REMOVE, 54 MARK_AS_OVER_ANNOTATED, 5 UNDECIDED, 3 TOO_GENERAL.
Of the 73 removals, 52 are bare `protein binding` rows from interaction screens. The
other 21 are nine IEA, six IBA, three TAS, two NAS and one IDA row. The patterns:

- **Whole-family terms that do not fit the photoreceptor member.** Adenylate
  cyclase-modulating signalling on the transducins GNAT1 and GNAT2, whose effector is the
  cGMP phosphodiesterase; phosphodiesterase activity and cGMP binding mapped by family
  signature onto the inhibitory subunits PDE6G and PDE6H, which have neither domain;
  calcium channel activity and synaptic plasticity on the rod exchanger SLC24A1, from a
  node seeded by its neuronal paralog; signalling receptor activity on nyctalopin (NYX);
  receptor internalization on visual arrestin (SAG).
- **Activity assigned to the wrong partner.** GTPase activity on the G beta subunit GNB3;
  photoreceptor activity on cone transducin GNAT2; protein phosphatase inhibitor activity
  on arrestin, where the cited study shows arrestin shields the substrate.
- **Subunits that only contribute.** KCNV2 (Kv8.2) is silent alone and contributes to a
  heteromeric channel; GNB3 contributes to the G protein activity of the heterotrimer.
  NYX is given no molecular function, because it has none that GO can state: its role is
  holding the TRPM1 channel in place.
- **Species.** Much of the evidence is on bovine or mouse protein. The human rows were
  transferred from 97 proteins of other species, and only two of those have a review
  here (see Orthologues). The reviews say which species was assayed.

### Errors in the source records

Recorded as `source_defects` where the cached text shows the problem, and otherwise
reported in the review's notes as a lead.

- RHO: three location rows cite PMID:11767049, a kidney paper that does not mention
  rhodopsin. The mouse donor of an Ensembl-transferred cell-cell junction row cites a
  T cell immunological-synapse paper.
- GNAT2: a transferred synapse row rests on a mouse study that used Gnat2 mutants only
  as a cone-less background.
- GRM6: a mouse annotation uses the fission-yeast term "new growing cell tip" for
  bipolar-cell dendritic tips.
- SLC24A1: a 2002 annotation uses "outer membrane" where the paper says outer segments.
- PDE6C: a row for no-go mRNA decay, which matches a term error in four GO-CAM models.
- PDE6A and PDE6B: the two visual perception rows appear to cite each other's paper.
  Neither full text was available, so this is a lead, not a recorded defect.

### PANTHER families

- **Opsins (PTHR24240).** G protein-coupled photoreceptor activity, phototransduction
  and cellular response to light stimulus are placed at the family root (PTN008398221),
  so the orphan receptors GPR52 and GPR88 inherit them. Photoreceptor outer segment
  (PTN000662150) reaches OPN3, OPN5 and arthropod pteropsins. Both are judged too deep.
- **G alpha (PTHR10218).** Adenylate cyclase-modulating signalling at the family root
  needs pruning for the transducins. The bitter-taste node on GNAT2 rests on one chimera
  experiment in cultured cells and is judged to be on the wrong node.
- **Arrestins (PTHR11792).** Receptor internalization needs pruning for the two visual
  arrestin clades. An IRD that blocks cytoplasm for the S-arrestin clade is contradicted:
  rod arrestin is a soluble cytoplasmic protein.
- **Receptor kinases (PTHR24355), G beta (PTHR19850).** All assessed nodes are sound.

### GO-CAM models

The activation chain in all six visual-pigment models (opsin, transducin alpha, PDE6
gamma, PDE6 catalytic, CNG channel) agrees with the gene reviews. The defects are in
references and one term:

- Rod model (6918f23700000035): the rhodopsin-to-transducin edge and the all-trans-retinal
  input cite papers about opsin 3 in skin cells; the transducin-to-PDE6 gamma edge cites a
  serotonin receptor paper.
- Four cone models (OPN1MW, OPN1SW, OPN1MW2, OPN1MW3): the PDE6C activity is part of
  GO:0070966 no-go mRNA decay, where the OPN1LW model has GO:0141190.
- The OPN1MW2 and OPN1MW3 models have no gene review to compare with, and whether those
  gene copies contribute to vision is itself doubtful.

### Ontology

- The definition of GO:0141190 transducin-mediated opsin signaling pathway ends "Typical
  examples are rhabdomeric photoreceptors in the eyes of deuterostomes". Vertebrate rods
  and cones, which the rest of the definition describes, are ciliary photoreceptors.
- GO has a rod photoreceptor phosphodiesterase 6 complex (GO:7770030) and no cone
  counterpart; the PDE6C review proposes one.
- GO has no molecular function for inhibiting a phosphodiesterase; PDE6G and PDE6H use
  the general enzyme inhibitor activity.

### dismech entries

Twelve entries have been aligned so far (776 evidence snippets re-validated, none
changed). Most changes type the gene record and attach the gene to the node that already
describes its dysfunction. The substantive corrections:

- **GNAT2-Related_Retinopathy** bound decreased GTPase activity to the disease node.
  GTP hydrolysis is what ends the signal, so losing it would prolong signalling. The
  node now carries decreased G protein activity, the gene review's core function.
- **RHO-Related_Retinopathy** recorded the constitutively active night-blindness
  alleles as an increase in photoreceptor activity; it is now recorded as a gain of
  function, since the activity occurs in darkness. The misfolding node no longer carries
  a "decreased" modifier on the gene, because those alleles act by toxic gain of function
  or dominant-negative interference.
- **KCNV2_Related_Retinopathy** had the gene on no mechanism node. It is now on the
  Kv8.2/Kv2.1 heteromer node, with the channel activity stated as the heteromer's.

### Open disagreements

Rows where a dismech node term relates to no core function in a gene review, not yet
resolved. The current list is in the alignment table under `NO_GO_ALIGNMENT`.

- **IDH3B-Related_Retinopathy, IDH3B.** dismech binds isocitrate dehydrogenase (NAD+)
  activity to the IDH3B node; the gene review treats IDH3B as the non-catalytic beta
  subunit, with structural molecule activity.
- **Cataract_9_Multiple_Types, CRYAA.** dismech binds protein folding chaperone activity
  to the alpha-crystallin nodes; the gene review gives a structural lens role and a
  second core function for which GO has no term.
- **Congenital_Stationary_Night_Blindness.** NYX, CABP4, SLC24A1 and GUCY2D sit on
  shared nodes whose terms state none of their own functions (being worked on).
- **Microphthalmia_with_Coloboma, ABCB6**, and **BBSome-Related_Retinitis_Pigmentosa,
  TTC8**: the gene sits on a shared process-level node.

## Plan

Tranches follow mechanism, so that each one can be closed against a module:

1. **Phototransduction and the photoreceptor-to-bipolar synapse** (33 genes): RHO, the
   cone opsins, transducin, PDE6, the CNG channels, guanylate cyclase and its activators,
   rhodopsin kinase and arrestin, the exchanger, and the night-blindness synapse genes.
   Module `visual_phototransduction`; six GO-CAM models.
2. **Visual cycle and retinal pigment epithelium**: RPE65, RDH5, RDH12, RLBP1, ABCA4,
   RBP4, BEST1, MERTK, TIMP3, EFEMP1, CYP4V2, OAT, CHM. Module `retinoid_visual_cycle`.
3. **Photoreceptor structure and cilium**: PRPH2, PROM1, RP1, RPGR, RP2, TULP1, LCA5,
   CEP290, MAK, KIZ, TTLL5, RAB28, POC1B, the BBSome genes, EYS, CRB1, IMPG1, IMPG2, RS1.
4. **Photoreceptor gene regulation and splicing**: CRX, NR2E3, OTX2, PRPF31, PRPF8,
   SNRNP200, the snRNA genes, SAMD7, PRDM13, IRX1.
5. **Lens**: the crystallins, GJA8, MIP, BFSP1, BFSP2, HSF4, MAF, CHMP4B, NHS, FTL.
6. **Cornea**: TGFBI, CHST6, DCN, UBIAD1, ZEB1, OVOL2, GRHL2.
7. **Optic nerve**: OPA1, OPA3, TMEM126A, MIEF1, MCAT, SSBP1, DNAJC30, MT-ND1, MT-ND4,
   MT-ND6.
8. **Anterior segment, glaucoma, globe development and retinal vasculature**: PAX6,
   FOXC1, PITX2, FOXE3, CYP1B1, MYOC, OPTN, LTBP2, TEK, ANGPT1, the microphthalmia genes,
   and the exudative vitreoretinopathy genes.

---
# STATUS

Updated 2026-11-27.

- [x] Scope: 126 dismech entries, 171 causal genes, every inclusion and exclusion recorded
- [x] Gene-side inventory, orthologue table and entry-by-entry audit, all regenerable
- [x] Tranche 1 gene reviews: all 22 unreviewed genes now COMPLETE (RHO, OPN1LW, OPN1MW,
      OPN1SW, GNAT1, GNAT2, GNB3, PDE6A, PDE6B, PDE6C, PDE6G, PDE6H, RD3, GRK1, SAG,
      SLC24A1, KCNV2, CABP4, GRM6, TRPM1, NYX, GPR179), each with OpenScientist research
- [ ] Tranche 1 drafts written in other projects, left as they are: CNGA3, CNGB1,
      GUCY2D, GUCA1A, AIPL1
- [x] GO-CAM reviews: the six visual-pigment models and the pikachurin/GPR179 model
- [x] Family reviews: PTHR24240, PTHR24355, PTHR11792, PTHR10218, PTHR19850
- [ ] Family reviews in progress: PTHR10846, PTHR13800, PTHR24060, PTHR32546, PTHR12122,
      PTHR28489, PTHR11347 (extension), PTHR11537, PTHR45917, PTHR24369, PTHR45842
- [ ] Family reviews not started for tranche 1: PTHR45638, PTHR11920, PTHR23055,
      PTHR11242, PTHR46164, PTHR45628, PTHR10166
- [x] Module `visual_phototransduction` reconciled with the gene and GO-CAM reviews. It
      stays DRAFT: GNGT1, GNGT2, SLC24A2, GRK7, ARR3, RCVRN, RGS9, RGS9BP, GUCY2F and
      GUCA1B have no gene review
- [x] dismech, aligned: RHO-Related_Retinopathy, Protan_Color_Vision_Deficiency,
      Blue_Cone_Monochromacy, Tritan_Color_Vision_Deficiency, GNAT2-Related_Retinopathy,
      PDE6A-, PDE6C-, PDE6G-, RD3-, KCNV2_, CNGB1- and CNGA1-Related_Retinopathy
- [ ] dismech, in progress: Congenital_Stationary_Night_Blindness, Achromatopsia,
      Cone_Dystrophy
- [ ] dismech, tranche 1 entries not started: CACNA1F-Related_Retinopathy,
      Aland_Island_Eye_Disease, CACNA2D4-related_Retinopathy, CNGA3-, CNGB3-, GUCY2D-,
      GUCA1A- and AIPL1-Related_Retinopathy, Central_Areolar_Choroidal_Dystrophy
- [ ] Orthologues: of the 97 proteins of other species that the reviewed human rows were
      transferred from, 2 have a review; the main donors (bovine rhodopsin, transducin
      and PDE6, mouse orthologues) are the next reviews to write
- [ ] Report the upstream findings (PAINT nodes, GO-CAM references and term, the GO
      definition, the mouse and UniProt annotations); nothing has been sent
- [ ] Tranches 2 to 8 (about 115 genes without a complete review)

# NOTES

## 2026-11-16

Project started. The committed baseline audit ran over dismech `0669e13e5` and
ai-gene-review `d6828d1c9`, after gene data had been fetched for the 22 unreviewed
tranche 1 genes (their seeded stubs count as INITIALIZED reviews, which is why that run
showed fewer `NO_AIGR_REVIEW` rows than the 104 unreviewed genes the project started
with) and before any annotation had been reviewed. Deep research by Falcon failed to
authenticate; OpenScientist works and is used instead. The instructions given to the
workers who write the gene reviews, the family reviews and the dismech alignment are in
`projects/DISMECH_VISION_ALIGNMENT/briefs/`.

## 2026-11-27

Gene reviews are written from a prepared dossier (`tools/make_dossier.py`) and merged
from a decisions file (`tools/apply_review.py`), which cut the cost of a review by about
an order of magnitude. The audit table on this page is regenerated from the current
trees and no longer shows the baseline. The skill reference
`.claude/skills/gocam-curation/references/causal-relations.md` labels RO:0002413 as
"directly positively regulates"; a GO-CAM reviewer reports that RO:0002413 is "provides
input for" and RO:0002629 is the positive-regulation relation. Not checked or changed
here.
