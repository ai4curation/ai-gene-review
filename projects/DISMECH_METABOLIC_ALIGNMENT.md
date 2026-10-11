---
title: dismech metabolic disorders aligned with ai-gene-review
maturity: IN_PROGRESS
description: Per-entry check that dismech metabolic disease mechanisms agree with ai-gene-review core functions and modules
species: [human]
---

# dismech metabolic disorders aligned with ai-gene-review

This page records, for every dismech metabolic disorder in scope, whether the causal gene's
dysfunction as modelled in the dismech pathograph agrees with the gene's normal function in its
ai-gene-review review, and whether the gene sits in an ai-gene-review module.

**Scope.** dismech entries with Harrison's chapter `ENDOCRINOLOGY_METABOLISM` or a metabolic
`category`, excluding primarily endocrine-gland, autoimmune, complex, neoplastic and gynecologic
conditions, plus two entries created in this work (Mitchell syndrome, SLC26A1-related hypersulfaturia).

**Method.** For each gene bound in an entry's `genetic` records, the GO molecular functions and
biological processes on the pathograph nodes naming that gene are compared with the gene's
ai-gene-review core functions. A match is the same term or one related through is_a/part_of
ancestry. Modules are matched by UniProt accession. The audit script, page generator and entry
list are in [DISMECH_METABOLIC_ALIGNMENT/](DISMECH_METABOLIC_ALIGNMENT/).

Flags: `UNTYPED`/`NO_ORIGIN` (genetic record lacks relationship type / variant origin),
`NO_GO_ON_GENE_NODES` (no node naming the gene carries a GO term), `NO_AIGR_REVIEW`,
`AIGR_NOT_COMPLETE`, `NO_GO_ALIGNMENT` (no node term matches a core function), `NO_MODULE`.

**Summary.** 116 entries; 161 principal gene rows (causative and untyped);
148 have no flag other than `NO_MODULE`. Flag counts on principal rows: `NO_AIGR_REVIEW` 13, `NO_MODULE` 16, `NO_ORIGIN` 13.

Polygenic entries (Type I diabetes, the MELAS mtDNA genes) and modifier/susceptibility genes are
listed but were not required to align: their genes are risk loci or mtDNA tRNAs, not the
normal-function owners of a single pathway step.

| Entry | Gene | Relationship | AIGR | Aligned GO terms | Modules | Flags |
|---|---|---|---|---|---|---|
| 3-hydroxyacyl-CoA_Dehydrogenase_Deficiency | HADH | CAUSATIVE | COMPLETE | GO:0003857 GO:0004857 | beta_cell_glucose_stimulated_insulin_secretion fatty_acid_beta_oxidation | ok |
| AHCY_Deficiency | AHCY | CAUSATIVE | COMPLETE | GO:0004013 | sam_cycle | ok |
| Adult-Type_Hypolactasia | LCT | CAUSATIVE | COMPLETE | GO:0000016 | - | NO_MODULE |
| Autosomal_Dominant_Hypercholesterolemia_3 | PCSK9 | CAUSATIVE | COMPLETE | GO:0050750 | ldl_receptor_mediated_endocytosis | ok |
| Autosomal_Recessive_Hypophosphatemic_Rickets_1 | DMP1 | CAUSATIVE | COMPLETE | GO:0005509 | - | NO_MODULE |
| Bachmann-Bupp_Syndrome | ODC1 | CAUSATIVE | COMPLETE | GO:0004586 GO:0006596 | polyamine_metabolism | ok |
| Biotinidase_Deficiency | BTD | CAUSATIVE | COMPLETE | GO:0006768 GO:0047708 | biotin_cycle | ok |
| CHILD_Syndrome | NSDHL | CAUSATIVE | COMPLETE | GO:0000252 | cholesterol_synthesis_post_lanosterol | ok |
| COQ2-Related_Primary_Coenzyme_Q10_Deficiency | COQ2 | CAUSATIVE | COMPLETE | GO:0008412 | coenzyme_q10_biosynthesis | ok |
| COX18-Related_COX_Deficiency | COX18 | CAUSATIVE | COMPLETE | GO:0032977 GO:0033617 | complex_iv_assembly_factors | ok |
| COX20-Related_COX_Deficiency | COX20 | CAUSATIVE | COMPLETE | GO:0030674 GO:0033617 | mitochondrial_complex_iv | ok |
| COX4I2-Related_Pancreatic_Insufficiency-Anemia-Hyperostosis_Syndrome | COX4I2 | CAUSATIVE | COMPLETE | GO:0004129 GO:0006123 | mitochondrial_complex_iv | ok |
| Chylomicron_Retention_Disease | SAR1B | CAUSATIVE | COMPLETE | GO:0003924 | chylomicron_assembly_secretion | ok |
| Chylomicron_Retention_Disease | SAR1A | MODIFIER | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Combined_Oxidative_Phosphorylation_Defect_Type_15 | MTFMT | CAUSATIVE | COMPLETE | GO:0004479 | mitochondrial_trna_charging_and_initiator_formylation | ok |
| Combined_Oxidative_Phosphorylation_Defect_Type_21 | TARS2 | CAUSATIVE | COMPLETE | GO:0004829 | mitochondrial_trna_charging_and_initiator_formylation | ok |
| Combined_Oxidative_Phosphorylation_Defect_Type_30 | TRMT10C | CAUSATIVE | COMPLETE | GO:0097745 | - | NO_MODULE |
| Congenital_Bile_Acid_Synthesis_Defect_5 | ABCD3 | CAUSATIVE | COMPLETE | GO:0015607 | bile_acid_synthesis_sidechain_conjugation peroxisomal_beta_oxidation | ok |
| Congenital_Isolated_Hyperinsulinism | ABCC8 | CAUSATIVE | COMPLETE | GO:0015272 GO:0050796 GO:0071805 | beta_cell_glucose_stimulated_insulin_secretion | ok |
| Congenital_Isolated_Hyperinsulinism | KCNJ11 | CAUSATIVE | COMPLETE | GO:0015272 GO:0050796 GO:0071805 | beta_cell_glucose_stimulated_insulin_secretion | ok |
| Congenital_Isolated_Hyperinsulinism | GLUD1 | CAUSATIVE | COMPLETE | GO:0004353 | beta_cell_glucose_stimulated_insulin_secretion glutamate_glutamine_ammonia_hub | ok |
| Congenital_Isolated_Hyperinsulinism | GCK | CAUSATIVE | COMPLETE | GO:0004340 | beta_cell_glucose_stimulated_insulin_secretion glycolysis_investment_phase | ok |
| Congenital_Isolated_Hyperinsulinism | HADH | CAUSATIVE | COMPLETE | GO:0004857 | beta_cell_glucose_stimulated_insulin_secretion fatty_acid_beta_oxidation | ok |
| Congenital_Isolated_Hyperinsulinism | HNF4A | CAUSATIVE | COMPLETE | GO:0001228 | - | NO_MODULE |
| Congenital_Isolated_Hyperinsulinism | SLC16A1 | CAUSATIVE | COMPLETE | GO:0015650 GO:1901475 | - | NO_MODULE |
| Congenital_Leptin_Deficiency | LEP | CAUSATIVE | COMPLETE | GO:0005179 | leptin_melanocortin_signaling | ok |
| Constitutional_Megaloblastic_Anemia_With_Severe_Neurologic_Disease | DHFR | CAUSATIVE | COMPLETE | GO:0004146 | thymidylate_synthesis | ok |
| Cystinosis | CTNS | CAUSATIVE | COMPLETE | GO:0015184 GO:0015811 GO:0022857 GO:1904919 | - | NO_MODULE |
| D-Bifunctional_Protein_Deficiency | HSD17B4 | CAUSATIVE | COMPLETE | GO:0033540 GO:0080023 GO:0106386 GO:0140493 | peroxisomal_beta_oxidation | ok |
| DPM2-congenital_disorder_of_glycosylation | DPM2 | CAUSATIVE | COMPLETE | GO:0008047 | dolichol_phosphate_sugar_donor_supply | ok |
| Developmental_And_Epileptic_Encephalopathy_116 | GLUL | CAUSATIVE | COMPLETE | GO:0004356 | glutamate_glutamine_ammonia_hub | ok |
| Developmental_And_Epileptic_Encephalopathy_50 | CAD | CAUSATIVE | COMPLETE | GO:0004070 GO:0004088 GO:0004151 | de_novo_pyrimidine_synthesis | ok |
| Dorfman_Chanarin_Disease | ABHD5 | CAUSATIVE | COMPLETE | GO:0010898 GO:0060229 | triacylglycerol_lipolysis | ok |
| Dysostosis_Multiplex_Ain-Naz_Type | LYSET | CAUSATIVE | COMPLETE | GO:0050821 | mannose_6_phosphate_lysosomal_targeting | ok |
| EEFSEC_Deficiency | EEFSEC | CAUSATIVE | COMPLETE | GO:0001514 GO:0003746 GO:0006414 | selenocysteine_biosynthesis_incorporation | ok |
| Encephalopathy_Due_To_Defective_Mitochondrial_And_Peroxisomal_Fission_2 | MFF | CAUSATIVE | COMPLETE | GO:0043495 | mitochondrial_dynamics peroxisome-lifecycle | ok |
| FBXL4-Related_Mitochondrial_DNA_Depletion_Syndrome | FBXL4 | CAUSATIVE | COMPLETE | GO:1990756 | mitophagy | ok |
| Familial_Defective_Apolipoprotein_B-100 | APOB | CAUSATIVE | COMPLETE | GO:0050750 | chylomicron_assembly_secretion ldl_receptor_mediated_endocytosis | ok |
| Familial_Defective_Apolipoprotein_B-100 | LDLR | MODIFIER | COMPLETE | - | ldl_receptor_mediated_endocytosis | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Familial_Defective_Apolipoprotein_B-100 | PCSK9 | MODIFIER | COMPLETE | - | ldl_receptor_mediated_endocytosis | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Fructose-1,6-Bisphosphatase_Deficiency | FBP1 | CAUSATIVE | COMPLETE | GO:0006094 GO:0042132 | gluconeogenesis_human gluconeogenesis_human_substrates | ok |
| GM1_Gangliosidosis_Type_1 | GLB1 | CAUSATIVE | COMPLETE | GO:0004565 GO:0006689 | glycosphingolipid_lysosomal_degradation keratan_chondroitin_sulfate_lysosomal_degradation lysosomal_glycoprotein_degradation | ok |
| GM1_Gangliosidosis_Type_3 | GLB1 | CAUSATIVE | COMPLETE | GO:0004565 GO:0006689 | glycosphingolipid_lysosomal_degradation keratan_chondroitin_sulfate_lysosomal_degradation lysosomal_glycoprotein_degradation | ok |
| GPD1_Deficiency | GPD1 | CAUSATIVE | COMPLETE | GO:0141152 | gluconeogenesis_human_substrates glycerol_phosphate_shuttle | ok |
| Glycogen_Storage_Disease_Type_I | G6PC1 | CAUSATIVE | COMPLETE | GO:0004346 GO:0006094 GO:0042593 | gluconeogenesis_human gluconeogenesis_human_substrates glucose_6_phosphatase_system | ok |
| Glycogen_Storage_Disease_Type_I | SLC37A4 | CAUSATIVE | COMPLETE | GO:0015152 GO:0042593 | gluconeogenesis_human gluconeogenesis_human_substrates glucose_6_phosphatase_system | ok |
| Glycoprotein_Storage_Disease | FUCA1 | CAUSATIVE | COMPLETE | GO:0004560 GO:0006516 | lysosomal_glycoprotein_degradation | ok |
| Glycoprotein_Storage_Disease | AGA | CAUSATIVE | COMPLETE | GO:0003948 GO:0006516 | lysosomal_glycoprotein_degradation | ok |
| Greenberg_Dysplasia | LBR | CAUSATIVE | COMPLETE | GO:0006695 GO:0050613 | cholesterol_synthesis_post_lanosterol | ok |
| HAO1-Related_Glycolate_Oxidase_Deficiency | HAO1 | CAUSATIVE | COMPLETE | GO:0003973 GO:0046296 | glyoxylate_oxalate_metabolism | ok |
| Heme_Oxygenase_1_Deficiency | HMOX1 | CAUSATIVE | COMPLETE | GO:0004392 GO:0042167 | heme_degradation | ok |
| Hyperinsulinemic_Hypoglycemia | ABCC8 | CAUSATIVE | COMPLETE | GO:0015272 GO:0050796 GO:0071805 | beta_cell_glucose_stimulated_insulin_secretion | ok |
| Hyperinsulinemic_Hypoglycemia | KCNJ11 | CAUSATIVE | COMPLETE | GO:0015272 GO:0050796 GO:0071805 | beta_cell_glucose_stimulated_insulin_secretion | ok |
| Hyperinsulinemic_Hypoglycemia | GLUD1 | CAUSATIVE | COMPLETE | GO:0004353 | beta_cell_glucose_stimulated_insulin_secretion glutamate_glutamine_ammonia_hub | ok |
| Hyperinsulinemic_Hypoglycemia | GCK | CAUSATIVE | COMPLETE | GO:0004340 GO:0050796 | beta_cell_glucose_stimulated_insulin_secretion glycolysis_investment_phase | ok |
| Hyperinsulinemic_Hypoglycemia | HADH | CAUSATIVE | COMPLETE | GO:0004857 GO:0050796 | beta_cell_glucose_stimulated_insulin_secretion fatty_acid_beta_oxidation | ok |
| Hyperinsulinemic_Hypoglycemia | HNF4A | CAUSATIVE | COMPLETE | GO:0001228 | - | NO_MODULE |
| Hyperinsulinemic_Hypoglycemia | HNF1A | CAUSATIVE | COMPLETE | GO:0001228 | - | NO_MODULE |
| Hyperinsulinemic_Hypoglycemia | SLC16A1 | CAUSATIVE | COMPLETE | GO:0015650 | - | NO_MODULE |
| Hyperinsulinemic_Hypoglycemia | UCP2 | DISPUTED | COMPLETE | - | - | NO_GO_ALIGNMENT, NO_MODULE |
| Hyperinsulinemic_Hypoglycemia | HK1 | CAUSATIVE | COMPLETE | GO:0004340 | glycolysis_investment_phase | ok |
| Hyperphosphatemic_Familial_Tumoral_Calcinosis | GALNT3 | CAUSATIVE | COMPLETE | GO:0004653 | fgf23_klotho_phosphate_homeostasis | ok |
| Hyperphosphatemic_Familial_Tumoral_Calcinosis | FGF23 | CAUSATIVE | COMPLETE | GO:0005179 | fgf23_klotho_phosphate_homeostasis fgfr_signaling | ok |
| Hyperphosphatemic_Familial_Tumoral_Calcinosis | KL | CAUSATIVE | COMPLETE | GO:0015026 | fgf23_klotho_phosphate_homeostasis fgfr_signaling | ok |
| Hyperprolinemia_Type_1 | PRODH | CAUSATIVE | COMPLETE | GO:0004657 GO:0006562 | proline_metabolism | ok |
| Hyperprolinemia_Type_2 | ALDH4A1 | CAUSATIVE | COMPLETE | GO:0003842 GO:0006562 | proline_metabolism | ok |
| Hypobetalipoproteinemia | APOB | CAUSATIVE | COMPLETE | GO:0034379 | chylomicron_assembly_secretion ldl_receptor_mediated_endocytosis | ok |
| Hypobetalipoproteinemia | PNPLA3 | MODIFIER | COMPLETE | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE |
| Hypobetalipoproteinemia | PCSK9 | CAUSATIVE | COMPLETE | GO:0050750 | ldl_receptor_mediated_endocytosis | ok |
| Hypobetalipoproteinemia | ANGPTL3 | CAUSATIVE | COMPLETE | GO:0055102 | - | NO_MODULE |
| Inborn_Disorder_of_Bile_Acid_Synthesis | - | - | - | - | - | NO_GENE_RECORD: Grouping-like entry; genes are carried by its subtypes. |
| Infantile-Onset_Pompe_Disease | GAA | CAUSATIVE | COMPLETE | GO:0004558 | lysosomal_glycogen_degradation | ok |
| LDLR-Related_Familial_Hypercholesterolemia | LDLR | CAUSATIVE | COMPLETE | GO:0005041 | ldl_receptor_mediated_endocytosis | ok |
| LPIN1-Related_Recurrent_Myoglobinuria | LPIN1 | CAUSATIVE | COMPLETE | GO:0008195 | triacylglycerol_biosynthesis | ok |
| Late-Onset_Pompe_Disease | GAA | CAUSATIVE | COMPLETE | GO:0004558 | lysosomal_glycogen_degradation | ok |
| Leber-like_Hereditary_Optic_Neuropathy_Autosomal_Recessive_1 | DNAJC30 | CAUSATIVE | COMPLETE | GO:0019899 GO:0034367 | - | NO_MODULE |
| MELAS_Syndrome | MT-TL1 | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-ND5 | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-ND1 | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-ND6 | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-TQ | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-TH | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-TK | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-TC | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-TS1 | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-TS2 | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-TV | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-TW | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MELAS_Syndrome | MT-TM | CAUSATIVE | - | - | - | NO_ORIGIN, NO_AIGR_REVIEW |
| MEND_Syndrome | EBP | CAUSATIVE | COMPLETE | GO:0006695 GO:0047750 | cholesterol_synthesis_post_lanosterol | ok |
| MEND_Syndrome | APOA5 | MODIFIER | - | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| MEND_Syndrome | ABCA1 | MODIFIER | COMPLETE | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE |
| MEND_Syndrome | APOB | MODIFIER | COMPLETE | - | chylomicron_assembly_secretion ldl_receptor_mediated_endocytosis | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| MSMO1_Deficiency | MSMO1 | CAUSATIVE | COMPLETE | GO:0000254 GO:0006695 | cholesterol_synthesis_post_lanosterol | ok |
| MTHFD1_Deficiency | MTHFD1 | CAUSATIVE | COMPLETE | GO:0004329 GO:0004477 GO:0004488 | folate_one_carbon_interconversion | ok |
| Methylmalonic_Acidemia_With_Homocystinuria_Type_cblJ | ABCD4 | CAUSATIVE | COMPLETE | GO:0015420 | cobalamin_intracellular_processing | ok |
| Mevalonate_Kinase_Deficiency | MVK | CAUSATIVE | COMPLETE | GO:0004496 GO:0008299 | mevalonate_pathway | ok |
| Mitchell_Syndrome | ACOX1 | CAUSATIVE | COMPLETE | GO:0003997 | peroxisomal_beta_oxidation | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_12 | NDUFA1 | CAUSATIVE | COMPLETE | GO:0008137 | complex_i_accessory_subunits | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_19 | FOXRED1 | CAUSATIVE | COMPLETE | GO:0016491 GO:0032981 | complex_i_assembly_factors | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_2 | NDUFS8 | CAUSATIVE | COMPLETE | GO:0051539 | mitochondrial_complex_i_core | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_21 | NUBPL | CAUSATIVE | COMPLETE | GO:0016226 | complex_i_assembly_factors | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_3 | NDUFS7 | CAUSATIVE | COMPLETE | GO:0051539 | mitochondrial_complex_i_core | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_6 | NDUFS2 | CAUSATIVE | COMPLETE | GO:0008137 GO:0048039 | mitochondrial_complex_i_core | ok |
| Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_1 | ATPAF2 | CAUSATIVE | COMPLETE | GO:0033615 GO:0044183 | mitochondrial_complex_v | ok |
| Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_2 | TMEM70 | CAUSATIVE | COMPLETE | GO:0030674 | mitochondrial_complex_v | ok |
| Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_3 | ATP5F1E | CAUSATIVE | COMPLETE | GO:0005198 | mitochondrial_complex_v | ok |
| Mucolipidosis_Type_II | GNPTAB | CAUSATIVE | COMPLETE | GO:0003976 GO:0006622 GO:0016256 | mannose_6_phosphate_lysosomal_targeting | ok |
| Muscular_Dystrophy_Congenital_Hearing_Loss_And_Ovarian_Insufficiency_Syndrome | GGPS1 | CAUSATIVE | COMPLETE | GO:0004311 | isoprenoid_diphosphate_biosynthesis | ok |
| Muscular_Dystrophy_Limb-girdle_Autosomal_Recessive_28 | HMGCR | CAUSATIVE | COMPLETE | GO:0004420 | mevalonate_pathway | ok |
| NAGA_Deficiency_Type_3 | NAGA | CAUSATIVE | COMPLETE | GO:0006516 GO:0008456 | lysosomal_glycoprotein_degradation | ok |
| Neuropathy_Hereditary_Motor_And_Sensory_Type_VIc_With_Optic_Atrophy | PDXK | CAUSATIVE | COMPLETE | GO:0008478 | vitamin_b6_plp_metabolism | ok |
| Neutral_Lipid_Storage_Myopathy | PNPLA2 | CAUSATIVE | COMPLETE | GO:0004806 GO:0019433 | triacylglycerol_lipolysis | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | LEP | CAUSATIVE | COMPLETE | GO:0038021 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | LEPR | CAUSATIVE | COMPLETE | GO:0038021 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | POMC | CAUSATIVE | COMPLETE | GO:0031782 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | PCSK1 | CAUSATIVE | COMPLETE | GO:0004252 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | MC4R | CAUSATIVE | COMPLETE | GO:0004980 GO:0007189 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | SH2B1 | SUSCEPTIBILITY | - | - | - | NO_AIGR_REVIEW |
| Obesity_Due_to_MC4R_Pathway_Disruption | NCOA1 | SUSCEPTIBILITY | - | - | - | NO_AIGR_REVIEW |
| Obesity_Due_to_MC4R_Pathway_Disruption | SIM1 | CAUSATIVE | COMPLETE | GO:0000981 | - | NO_MODULE |
| PET100-Related_COX_Deficiency | PET100 | CAUSATIVE | COMPLETE | GO:0033617 | complex_iv_assembly_factors | ok |
| PGM1-Congenital_Disorder_of_Glycosylation | PGM1 | CAUSATIVE | COMPLETE | GO:0004614 | glycogenolysis | ok |
| PNPO_Deficiency | PNPO | CAUSATIVE | COMPLETE | GO:0004733 | vitamin_b6_plp_metabolism | ok |
| Peroxisomal_Acyl-CoA_Oxidase_Deficiency | ACOX1 | CAUSATIVE | COMPLETE | GO:0003997 GO:0033540 GO:0140493 | peroxisomal_beta_oxidation | ok |
| Peroxisome_Biogenesis_Disorder_5B | PEX2 | CAUSATIVE | COMPLETE | GO:0007031 | peroxisome-lifecycle | ok |
| Peroxisome_Biogenesis_Disorder_6A_Zellweger | PEX10 | CAUSATIVE | COMPLETE | GO:0061630 | peroxisome-lifecycle | ok |
| Peroxisome_Biogenesis_Disorder_6B | PEX10 | CAUSATIVE | COMPLETE | GO:0061630 | peroxisome-lifecycle | ok |
| Pompe_Disease | GAA | CAUSATIVE | COMPLETE | GO:0004558 GO:0005980 | lysosomal_glycogen_degradation | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ2 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008412 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ4 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425 GO:0120539 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ5 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425 GO:0120539 | coenzyme_q10_biosynthesis ubiquinone_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ6 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425 GO:0106364 GO:0120539 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ8A | CAUSATIVE | COMPLETE | GO:0006744 GO:0016887 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ8B | CAUSATIVE | COMPLETE | GO:0006744 GO:0016887 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ7 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425 GO:0120539 GO:0160224 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ9 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425 GO:0120539 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | PDSS1 | CAUSATIVE | COMPLETE | GO:0006744 GO:0097269 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | PDSS2 | CAUSATIVE | COMPLETE | GO:0006744 GO:0097269 | coenzyme_q10_biosynthesis | ok |
| Primary_Hyperoxaluria_Type_1 | AGXT | CAUSATIVE | COMPLETE | GO:0008453 GO:0009436 | glyoxylate_oxalate_metabolism | ok |
| Primary_Hyperoxaluria_Type_2 | GRHPR | CAUSATIVE | COMPLETE | GO:0016618 GO:0030267 GO:0046487 | glyoxylate_oxalate_metabolism | ok |
| Primary_Hyperoxaluria_Type_3 | HOGA1 | CAUSATIVE | COMPLETE | GO:0008700 GO:0019470 | glyoxylate_oxalate_metabolism | ok |
| Primary_Hyperoxaluria_Type_3 | AGXT | MODIFIER | COMPLETE | - | glyoxylate_oxalate_metabolism | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Purine_Nucleoside_Phosphorylase_Deficiency | PNP | CAUSATIVE | COMPLETE | GO:0004731 GO:0006152 | purine_nucleotide_catabolism purine_salvage_and_catabolism | ok |
| Pyridoxine-Dependent_Epilepsy | ALDH7A1 | CAUSATIVE | COMPLETE | GO:0004029 GO:0004043 GO:0019477 | lysine_catabolism_saccharopine | ok |
| Pyruvate_Carboxylase_Deficiency_Disease | PC | CAUSATIVE | COMPLETE | GO:0004736 GO:0006094 | gluconeogenesis_human gluconeogenesis_human_substrates pyruvate_metabolism | ok |
| RFT1-congenital_disorder_of_glycosylation | RFT1 | CAUSATIVE | COMPLETE | GO:0140303 | n_glycan_llo_assembly_lumenal | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect | GNPAT | CAUSATIVE | COMPLETE | GO:0008611 GO:0016287 | ether_lipid_plasmalogen_biosynthesis | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect | AGPS | CAUSATIVE | COMPLETE | GO:0008609 GO:0008611 | ether_lipid_plasmalogen_biosynthesis | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect | FAR1 | CAUSATIVE | COMPLETE | GO:0008611 GO:0102965 | ether_lipid_plasmalogen_biosynthesis | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Type_1 | PEX7 | CAUSATIVE | COMPLETE | GO:0000268 GO:0016558 | peroxisome-lifecycle | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Type_5 | PEX5 | CAUSATIVE | COMPLETE | GO:0016558 GO:0140597 | peroxisome-lifecycle | ok |
| SCO1-Related_COX_Deficiency | SCO1 | CAUSATIVE | COMPLETE | GO:0016531 GO:0033617 | complex_iv_assembly_factors mitochondrial_complex_iv | ok |
| SECISBP2_Deficiency | SECISBP2 | CAUSATIVE | COMPLETE | GO:0001514 GO:0035368 | selenocysteine_biosynthesis_incorporation | ok |
| SEPSECS_Deficiency | SEPSECS | CAUSATIVE | COMPLETE | GO:0001717 GO:0016260 GO:0098621 | selenocysteine_biosynthesis_incorporation | ok |
| SLC26A1-Related_Hypersulfaturia | SLC26A1 | CAUSATIVE | COMPLETE | GO:0015383 GO:1902358 | - | NO_MODULE |
| SLC26A1-Related_Oxalate_Transporter_Deficiency | SLC26A1 | CAUSATIVE | COMPLETE | GO:0015116 GO:0019531 GO:0019532 GO:1902358 | - | NO_MODULE |
| SLC26A6-Related_Hyperoxaluria_and_Nephrolithiasis | SLC26A6 | CAUSATIVE | COMPLETE | GO:0019531 GO:0019532 | - | NO_MODULE |
| SLC35A1-Congenital_Disorder_of_Glycosylation | SLC35A1 | CAUSATIVE | COMPLETE | GO:0005456 | sialic_acid_metabolism | ok |
| STT3A-Congenital_Disorder_of_Glycosylation | STT3A | CAUSATIVE | COMPLETE | GO:0004579 | oligosaccharyltransferase_complex | ok |
| SUCLA2-Related_Mitochondrial_DNA_Depletion_Syndrome | SUCLA2 | CAUSATIVE | COMPLETE | GO:0004775 | tca_cycle | ok |
| Severe_X-linked_Mitochondrial_Encephalomyopathy | AIFM1 | CAUSATIVE | COMPLETE | GO:0043495 | apoptotic_execution_phase | ok |
| Short_Stature_Amelogenesis_Imperfecta_And_Skeletal_Dysplasia_With_Scoliosis | SLC10A7 | CAUSATIVE | COMPLETE | GO:0032468 GO:0051480 | - | NO_MODULE |
| Sitosterolemia | ABCG5 | CAUSATIVE | COMPLETE | GO:0015918 GO:0034041 | intestinal_sterol_absorption_and_efflux | ok |
| Sitosterolemia | ABCG8 | CAUSATIVE | COMPLETE | GO:0015918 GO:0034041 | intestinal_sterol_absorption_and_efflux | ok |
| Snyder-Robinson_Syndrome | SMS | CAUSATIVE | COMPLETE | GO:0006597 GO:0016768 | polyamine_metabolism | ok |
| Spastic_Paraparesis-cataracts-speech_Delay_Syndrome | FAR1 | CAUSATIVE | COMPLETE | GO:0102965 | ether_lipid_plasmalogen_biosynthesis | ok |
| Sphingosine_Phosphate_Lyase_Insufficiency_Syndrome | SGPL1 | CAUSATIVE | COMPLETE | GO:0008117 | sphingosine_1_phosphate_rheostat | ok |
| Sterol_Carrier_Protein_2_Deficiency | SCP2 | CAUSATIVE | COMPLETE | GO:0050632 | bile_acid_biosynthesis peroxisomal_beta_oxidation | ok |
| Triglyceride_Storage_Disease_Type_1 | - | - | - | - | - | NO_GENE_RECORD: Historical OMIM:190420 phenotype; no gene has been reported (ABHD5 content lives in Dorfman_Chanarin_Disease). |
| Type_I_Diabetes | INS | SUSCEPTIBILITY | COMPLETE | - | beta_cell_glucose_stimulated_insulin_secretion | NO_GO_ON_GENE_NODES |
| Type_I_Diabetes | PTPN22 | SUSCEPTIBILITY | IN_PROGRESS | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE |
| Type_I_Diabetes | IL2RA | SUSCEPTIBILITY | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE |
| Type_I_Diabetes | CTLA4 | SUSCEPTIBILITY | COMPLETE | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE |
| Type_I_Diabetes | TYK2 | SUSCEPTIBILITY | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Type_I_Diabetes | IFIH1 | SUSCEPTIBILITY | COMPLETE | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE |
| Type_I_Diabetes | BACH2 | SUSCEPTIBILITY | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE |
| Type_I_Diabetes | TNFAIP3 | SUSCEPTIBILITY | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE |
| Type_I_Diabetes | EGR2 | SUSCEPTIBILITY | IN_PROGRESS | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE |
| Type_I_Diabetes | IRF4 | SUSCEPTIBILITY | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE |
| Type_I_Diabetes | IKZF1 | SUSCEPTIBILITY | IN_PROGRESS | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE |
| Vitamin_D-Dependent_Rickets_Type_1A | CYP27B1 | CAUSATIVE | COMPLETE | GO:0004498 | fgf23_klotho_phosphate_homeostasis vitamin_d_activation_signaling | ok |
| Vitamin_D-Dependent_Rickets_Type_2B | - | - | - | - | - | NO_GENE_RECORD: Genetic basis unknown; HNRNPC is modelled as a mechanism actor, not a causal gene. |
| Wilsons_Disease | ATP7B | CAUSATIVE | COMPLETE | GO:0006825 GO:0035434 GO:0055070 GO:0140581 | cuproptosis | ok |
| Wolman_Disease | LIPA | CAUSATIVE | COMPLETE | GO:0004771 GO:0004806 GO:0019433 GO:0046461 | ldl_receptor_mediated_endocytosis | ok |
| X-linked_Chondrodysplasia_Punctata_2 | EBP | CAUSATIVE | COMPLETE | GO:0006695 GO:0047750 | cholesterol_synthesis_post_lanosterol | ok |

## Notes on remaining flags

- Every causative nuclear-gene row is free of flags other than `NO_MODULE`. The other flags fall on
  the MELAS mtDNA genes and on modifier, susceptibility and disputed genes, none of which were
  required to align.
- **MELAS mtDNA genes** (MT-TL1, MT-ND1/5/6 and the other tRNA genes): ai-gene-review has no
  reviews for mitochondrially encoded tRNA or complex I subunit genes, and the dismech record
  types them by relationship but not by variant origin (heteroplasmic mtDNA variants fit
  neither GERMLINE nor SOMATIC cleanly).
- **TMEM251** is the dismech/HGNC-build label for the gene now named LYSET; it is matched to
  the LYSET review.
- **Type I diabetes risk loci** (PTPN22, IL2RA, CTLA4, IFIH1, BACH2, TNFAIP3, EGR2, IRF4, IKZF1,
  TYK2) are SUSCEPTIBILITY records with no single pathway step; several ai-gene-review entries
  for them are still drafts from other projects.

## Causative genes without a module, and why

- **TRMT10C**: RNase P partners (HSD17B10, PRORP, ELAC2) lack completed reviews.
- **ANGPTL3**: No LPL / plasma triglyceride clearance module; LPL review still DRAFT.
- **CTNS**: Lysosomal cystine export is a single step.
- **SLC26A1**: Epithelial oxalate/sulfate transport has no coherent multi-part module yet; SLC26A1's oxalate role is contested.
- **SLC26A6**: As SLC26A1; a two-part oxalate-transport module is possible later.
- **DMP1**: Recorded as regulatory context in fgf23_klotho_phosphate_homeostasis; mechanism undefined.
- **SLC10A7**: Single gene with unknown transported substrate.
- **DNAJC30**: Complex I N-module repair is not assembly; no repair module exists.
- **LCT**: Brush-border disaccharide digestion: only LCT has a completed review (SI, MGAM, TREH missing).
- **HNF1A / HNF4A**: Transcription factors whose hyperinsulinism and MODY roles act through many target genes; no beta-cell transcriptional-network module exists yet.
- **SLC16A1**: Disease mechanism is ectopic beta-cell expression of a transporter whose normal role (lactate/pyruvate transport) belongs to no beta-cell pathway; a monocarboxylate-transport module would not include the disease mechanism.
- **SIM1**: Transcription factor needed for paraventricular hypothalamic neuron development and function; it acts on, rather than within, the leptin_melanocortin_signaling module, whose parts are the ligand, processing and receptor steps.
- **UCP2**: Causal role disputed (relationship DISPUTED); its transported substrate is itself contested.
