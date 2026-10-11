---
title: dismech metabolic disorders aligned with ai-gene-review
maturity: IN_PROGRESS
description: Per-entry check that dismech metabolic disease mechanisms agree with ai-gene-review core functions and modules
species: [human]
genes: [ABCA1, ABCC8, ABCD3, ABCD4, ABCG5, ABCG8, ABHD5, ACOX1, AGA, AGPS, AGXT, AHCY, AIFM1, ALDH4A1, ALDH7A1, ANGPTL3, APOA5, APOB, ATP5F1E, ATP7B, ATPAF2, BACH2, BTD, CAD, COQ2, COQ4, COQ5, COQ6, COQ7, COQ8A, COQ8B, COQ9, COX18, COX20, COX4I2, CTLA4, CTNS, CYP27B1, DHFR, DMP1, DNAJC30, DPM2, EBP, EEFSEC, EGR2, FAR1, FBP1, FBXL4, FGF23, FOXRED1, FUCA1, G6PC1, GAA, GALNT3, GCK, GGPS1, GLB1, GLUD1, GLUL, GNPAT, GNPTAB, GPD1, GRHPR, HADH, HAO1, HK1, HMGCR, HMOX1, HNF1A, HNF4A, HOGA1, HSD17B4, IFIH1, IKZF1, IL2RA, INS, IRF4, KCNJ11, KL, LBR, LCT, LDLR, LEP, LEPR, LIPA, LPIN1, LYSET, MC4R, MFF, MSMO1, MT-ND1, MT-ND5, MT-ND6, MT-TC, MT-TH, MT-TK, MT-TL1, MT-TM, MT-TQ, MT-TS1, MT-TS2, MT-TV, MT-TW, MTFMT, MTHFD1, MVK, NAGA, NCOA1, NDUFA1, NDUFS2, NDUFS7, NDUFS8, NSDHL, NUBPL, ODC1, PC, PCSK1, PCSK9, PDSS1, PDSS2, PDXK, PET100, PEX10, PEX2, PEX5, PEX7, PGM1, PNP, PNPLA2, PNPLA3, PNPO, POMC, PRODH, PTPN22, RFT1, SAR1A, SAR1B, SCO1, SCP2, SECISBP2, SEPSECS, SGPL1, SH2B1, SIM1, SLC10A7, SLC16A1, SLC26A1, SLC26A6, SLC35A1, SLC37A4, SMS, STT3A, SUCLA2, TARS2, TMEM70, TNFAIP3, TRMT10C, TYK2, UCP2]
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
ai-gene-review core functions. The audit script (`align_audit.py`), the page generator
(`make_page.py`), the entry list (`scope.yaml`) and the committed report of the run behind this
table (`report.yaml`) are in the `projects/DISMECH_METABOLIC_ALIGNMENT/` directory of the
repository.

**What "aligned" does and does not claim.** Two properties of the test make it a weak check,
and either can turn a row green that a curator would not:

- The relation is **symmetric** and **unbounded in distance**. A node term counts as aligned
  when either it or the core term is an is_a/part_of ancestor of the other, at any depth. So a
  dismech node bound to something broad aligns with a specific core function, and the reverse,
  and two terms many levels apart still align. The table therefore prints the core term each
  node term matched (`node->core`, or the term alone where the two are identical), so the
  distance behind a match is visible per row. `DMP1 | GO:0005509` (calcium ion binding) is the
  clearest row where the verdict carries little information; reading a row as agreement means
  reading its pair.
- Module **membership** is not module **coverage**. Membership says the gene is a part of some
  module; coverage says a module is about the function the row aligned on, which is a different
  and stronger claim. They are flagged separately: `NO_MODULE_MEMBERSHIP` means no module
  contains the gene, and `MODULE_NOT_COVERING` means one does but no term anywhere in any of
  those modules is related to the aligned terms. Such a module is marked
  `(not covering)` in the Modules column. AIFM1 is the row this flag exists to catch: it sits
  in `apoptotic_execution_phase`, whose AIFM1 annoton carries DNA binding, nucleus and
  positive regulation of apoptotic process, while the aligned function is the mitochondrial
  disulfide relay. No module covers the relay.

Coverage reads the module's declared `concepts`, at module level and per node, as well as its
annotons' terms: a module states its scope as processes while its annotons carry the molecular
functions of individual parts, so annotons alone miss what the module is about. One limitation
survives that and is left visible rather than waived: is_a/part_of ancestry does not cross
between molecular function and biological process, so a dismech node bound to an activity and
a module scoped to the corresponding process cannot be related, however plainly they are the
same chemistry. NDUFA1 is that row.

Membership is read from the module structure (`parts[].node.annotons[]`, following the
participant whichever selector it uses, including a `FAMILY` participant's
`representative_members` and a protein complex's active units and components), and following
nested parts and variant sets, so a gene named only in a module's notes or evidence does not
count as a part. Reading the files as text instead finds 3,707 accessions against 3,659 real
parts; the 48 extra are mentions rather than parts.

Flags: `UNTYPED`/`NO_ORIGIN` (genetic record lacks relationship type / variant origin),
`NO_GO_ON_GENE_NODES` (no node naming the gene carries a GO term), `NO_AIGR_REVIEW`,
`AIGR_NOT_COMPLETE`, `NO_CORE_FUNCTION_TERMS` (the review has no core-function GO term to
compare against), `NO_GO_ALIGNMENT` (no node term matches a core function, an annotation the
review keeps, or a term it proposes), `ALIGNED_NONCORE` (node terms match only annotations the
review keeps as non-core), `ALIGNED_PROPOSED` (node terms match only terms the review proposes
as NEW, which are not yet annotations), `NO_MODULE_MEMBERSHIP`, `MODULE_NOT_COVERING`. The last
four are informational, not defects.

**Provenance of this run.** The table is generated, so it is only as current as the inputs it
was generated from, and those inputs live in two repositories.

- run date: `2026-10-11T12:45:03Z`
- dismech revision: `c0ef3d0d5a5c519fab45d814a79709df266076e1` (c0ef3d0d5 2026-10-11 Add review records for nine unchanged entries and 16 gene pages)
- ai-gene-review revision: `67c18a542ed73a015faa82876d3774f5d2bf139d` (branch `claude/cool-edison-o9wvf0`)
- GO release: `2026-07-26`, adapter `sqlite:/root/.data/oaklib/go.db`

Many of the gene reviews and modules this table asserts `COMPLETE` for are added by the ten
themed PRs split out of #4690, so on a branch without those merged the audit cannot be
re-run to reproduce these rows. `report.yaml` is committed as the record of the run above.

**Summary.** 116 entries; 161 principal gene rows (causative and untyped);
161 carry no flag other than a module flag, `ALIGNED_NONCORE` or `ALIGNED_PROPOSED`. Flag counts on principal rows: `MODULE_NOT_COVERING` 4, `NO_MODULE_MEMBERSHIP` 26.

Polygenic entries (Type I diabetes) and modifier/susceptibility genes are
listed but were not required to align: their genes are risk loci or modifiers, not the
normal-function owners of a single pathway step.

| Entry | Gene | Relationship | AIGR | Aligned GO terms (node&rarr;core) | Modules | Flags |
|---|---|---|---|---|---|---|
| 3-hydroxyacyl-CoA_Dehydrogenase_Deficiency | HADH | CAUSATIVE | COMPLETE | GO:0003857 GO:0004857 | beta_cell_glucose_stimulated_insulin_secretion fatty_acid_beta_oxidation | ok |
| AHCY_Deficiency | AHCY | CAUSATIVE | COMPLETE | GO:0004013 | sam_cycle | ok |
| Adult-Type_Hypolactasia | LCT | CAUSATIVE | COMPLETE | GO:0000016 | - | NO_MODULE_MEMBERSHIP |
| Autosomal_Dominant_Hypercholesterolemia_3 | PCSK9 | CAUSATIVE | COMPLETE | GO:0050750 | ldl_receptor_mediated_endocytosis | ok |
| Autosomal_Recessive_Hypophosphatemic_Rickets_1 | DMP1 | CAUSATIVE | COMPLETE | GO:0005509 | - | NO_MODULE_MEMBERSHIP |
| Bachmann-Bupp_Syndrome | ODC1 | CAUSATIVE | COMPLETE | GO:0004586 GO:0006596&rarr;GO:0009446 | polyamine_metabolism | ok |
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
| Combined_Oxidative_Phosphorylation_Defect_Type_30 | TRMT10C | CAUSATIVE | COMPLETE | GO:0097745 | - | NO_MODULE_MEMBERSHIP |
| Congenital_Bile_Acid_Synthesis_Defect_5 | ABCD3 | CAUSATIVE | COMPLETE | GO:0015607 | bile_acid_synthesis_sidechain_conjugation peroxisomal_beta_oxidation | ok |
| Congenital_Isolated_Hyperinsulinism | ABCC8 | CAUSATIVE | COMPLETE | GO:0015272 GO:0050796 GO:0071805&rarr;GO:0015272 | beta_cell_glucose_stimulated_insulin_secretion | ok |
| Congenital_Isolated_Hyperinsulinism | KCNJ11 | CAUSATIVE | COMPLETE | GO:0015272 GO:0050796&rarr;GO:0046676 GO:0071805&rarr;GO:0015272 | beta_cell_glucose_stimulated_insulin_secretion | ok |
| Congenital_Isolated_Hyperinsulinism | GLUD1 | CAUSATIVE | COMPLETE | GO:0004353 | beta_cell_glucose_stimulated_insulin_secretion glutamate_glutamine_ammonia_hub | ok |
| Congenital_Isolated_Hyperinsulinism | GCK | CAUSATIVE | COMPLETE | GO:0004340 | beta_cell_glucose_stimulated_insulin_secretion glycolysis_investment_phase | ok |
| Congenital_Isolated_Hyperinsulinism | HADH | CAUSATIVE | COMPLETE | GO:0004857 | beta_cell_glucose_stimulated_insulin_secretion fatty_acid_beta_oxidation (not covering) | ok |
| Congenital_Isolated_Hyperinsulinism | HNF4A | CAUSATIVE | COMPLETE | GO:0001228 | - | NO_MODULE_MEMBERSHIP |
| Congenital_Isolated_Hyperinsulinism | SLC16A1 | CAUSATIVE | COMPLETE | GO:0015650&rarr;GO:0008028 GO:1901475&rarr;GO:0015718 | - | NO_MODULE_MEMBERSHIP |
| Congenital_Leptin_Deficiency | LEP | CAUSATIVE | COMPLETE | GO:0005179 | leptin_melanocortin_signaling | ok |
| Constitutional_Megaloblastic_Anemia_With_Severe_Neurologic_Disease | DHFR | CAUSATIVE | COMPLETE | GO:0004146 | thymidylate_synthesis | ok |
| Cystinosis | CTNS | CAUSATIVE | COMPLETE | GO:0015184 GO:0015811&rarr;GO:0015184 GO:0022857&rarr;GO:0015184 GO:1904919 | - | NO_MODULE_MEMBERSHIP |
| D-Bifunctional_Protein_Deficiency | HSD17B4 | CAUSATIVE | COMPLETE | GO:0033540&rarr;GO:0006635 GO:0080023 GO:0106386 GO:0140493 | peroxisomal_beta_oxidation | ok |
| DPM2-congenital_disorder_of_glycosylation | DPM2 | CAUSATIVE | COMPLETE | GO:0008047 | dolichol_phosphate_sugar_donor_supply | ok |
| Developmental_And_Epileptic_Encephalopathy_116 | GLUL | CAUSATIVE | COMPLETE | GO:0004356 | glutamate_glutamine_ammonia_hub | ok |
| Developmental_And_Epileptic_Encephalopathy_50 | CAD | CAUSATIVE | COMPLETE | GO:0004070 GO:0004088 GO:0004151 | de_novo_pyrimidine_synthesis | ok |
| Dorfman_Chanarin_Disease | ABHD5 | CAUSATIVE | COMPLETE | GO:0010898 GO:0060229 | triacylglycerol_lipolysis | ok |
| Dysostosis_Multiplex_Ain-Naz_Type | LYSET | CAUSATIVE | COMPLETE | GO:0050821 | mannose_6_phosphate_lysosomal_targeting | ok |
| EEFSEC_Deficiency | EEFSEC | CAUSATIVE | COMPLETE | GO:0001514 GO:0003746 GO:0006414&rarr;GO:0001514 | selenocysteine_biosynthesis_incorporation | ok |
| Encephalopathy_Due_To_Defective_Mitochondrial_And_Peroxisomal_Fission_2 | MFF | CAUSATIVE | COMPLETE | GO:0043495 | mitochondrial_dynamics peroxisome-lifecycle | ok |
| FBXL4-Related_Mitochondrial_DNA_Depletion_Syndrome | FBXL4 | CAUSATIVE | COMPLETE | GO:1990756 | mitophagy | ok |
| Familial_Defective_Apolipoprotein_B-100 | APOB | CAUSATIVE | COMPLETE | GO:0050750 | chylomicron_assembly_secretion (not covering) ldl_receptor_mediated_endocytosis | ok |
| Familial_Defective_Apolipoprotein_B-100 | LDLR | MODIFIER | COMPLETE | - | ldl_receptor_mediated_endocytosis | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Familial_Defective_Apolipoprotein_B-100 | PCSK9 | MODIFIER | COMPLETE | - | ldl_receptor_mediated_endocytosis | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Fructose-1,6-Bisphosphatase_Deficiency | FBP1 | CAUSATIVE | COMPLETE | GO:0006094 GO:0042132 | gluconeogenesis_human gluconeogenesis_human_substrates | ok |
| GM1_Gangliosidosis_Type_1 | GLB1 | CAUSATIVE | COMPLETE | GO:0004565 GO:0006689 | glycosphingolipid_lysosomal_degradation keratan_chondroitin_sulfate_lysosomal_degradation lysosomal_glycoprotein_degradation | ok |
| GM1_Gangliosidosis_Type_3 | GLB1 | CAUSATIVE | COMPLETE | GO:0004565 GO:0006689 | glycosphingolipid_lysosomal_degradation keratan_chondroitin_sulfate_lysosomal_degradation lysosomal_glycoprotein_degradation | ok |
| GPD1_Deficiency | GPD1 | CAUSATIVE | COMPLETE | GO:0141152 | gluconeogenesis_human_substrates glycerol_phosphate_shuttle | ok |
| Glycogen_Storage_Disease_Type_I | G6PC1 | CAUSATIVE | COMPLETE | GO:0004346 GO:0006094 GO:0042593 | gluconeogenesis_human gluconeogenesis_human_substrates glucose_6_phosphatase_system | ok |
| Glycogen_Storage_Disease_Type_I | SLC37A4 | CAUSATIVE | COMPLETE | GO:0015152&rarr;GO:0015760 GO:0042593 | gluconeogenesis_human gluconeogenesis_human_substrates glucose_6_phosphatase_system | ok |
| Glycoprotein_Storage_Disease | FUCA1 | CAUSATIVE | COMPLETE | GO:0004560 GO:0006516 | lysosomal_glycoprotein_degradation | ok |
| Glycoprotein_Storage_Disease | AGA | CAUSATIVE | COMPLETE | GO:0003948 GO:0006516 | lysosomal_glycoprotein_degradation | ok |
| Greenberg_Dysplasia | LBR | CAUSATIVE | COMPLETE | GO:0006695 GO:0050613 | cholesterol_synthesis_post_lanosterol | ok |
| HAO1-Related_Glycolate_Oxidase_Deficiency | HAO1 | CAUSATIVE | COMPLETE | GO:0003973 GO:0046296 | glyoxylate_oxalate_metabolism | ok |
| Heme_Oxygenase_1_Deficiency | HMOX1 | CAUSATIVE | COMPLETE | GO:0004392 GO:0042167 | heme_degradation | ok |
| Hyperinsulinemic_Hypoglycemia | ABCC8 | CAUSATIVE | COMPLETE | GO:0015272 GO:0050796 GO:0071805&rarr;GO:0015272 | beta_cell_glucose_stimulated_insulin_secretion | ok |
| Hyperinsulinemic_Hypoglycemia | KCNJ11 | CAUSATIVE | COMPLETE | GO:0015272 GO:0050796&rarr;GO:0046676 GO:0071805&rarr;GO:0015272 | beta_cell_glucose_stimulated_insulin_secretion | ok |
| Hyperinsulinemic_Hypoglycemia | GLUD1 | CAUSATIVE | COMPLETE | GO:0004353 | beta_cell_glucose_stimulated_insulin_secretion glutamate_glutamine_ammonia_hub | ok |
| Hyperinsulinemic_Hypoglycemia | GCK | CAUSATIVE | COMPLETE | GO:0004340 GO:0050796&rarr;GO:0032024 | beta_cell_glucose_stimulated_insulin_secretion glycolysis_investment_phase | ok |
| Hyperinsulinemic_Hypoglycemia | HADH | CAUSATIVE | COMPLETE | GO:0004857 GO:0050796&rarr;GO:0046676 | beta_cell_glucose_stimulated_insulin_secretion fatty_acid_beta_oxidation (not covering) | ok |
| Hyperinsulinemic_Hypoglycemia | HNF4A | CAUSATIVE | COMPLETE | GO:0001228 | - | NO_MODULE_MEMBERSHIP |
| Hyperinsulinemic_Hypoglycemia | HNF1A | CAUSATIVE | COMPLETE | GO:0001228 | - | NO_MODULE_MEMBERSHIP |
| Hyperinsulinemic_Hypoglycemia | SLC16A1 | CAUSATIVE | COMPLETE | GO:0015650&rarr;GO:0008028 | - | NO_MODULE_MEMBERSHIP |
| Hyperinsulinemic_Hypoglycemia | UCP2 | DISPUTED | COMPLETE | - | - | ALIGNED_NONCORE, NO_MODULE_MEMBERSHIP |
| Hyperinsulinemic_Hypoglycemia | HK1 | CAUSATIVE | COMPLETE | GO:0004340&rarr;GO:0004396 | glycolysis_investment_phase | ok |
| Hyperphosphatemic_Familial_Tumoral_Calcinosis | GALNT3 | CAUSATIVE | COMPLETE | GO:0004653 | fgf23_klotho_phosphate_homeostasis | ok |
| Hyperphosphatemic_Familial_Tumoral_Calcinosis | FGF23 | CAUSATIVE | COMPLETE | GO:0005179 | fgf23_klotho_phosphate_homeostasis fgfr_signaling (not covering) | ok |
| Hyperphosphatemic_Familial_Tumoral_Calcinosis | KL | CAUSATIVE | COMPLETE | GO:0015026 | fgf23_klotho_phosphate_homeostasis fgfr_signaling | ok |
| Hyperprolinemia_Type_1 | PRODH | CAUSATIVE | COMPLETE | GO:0004657 GO:0006562 | proline_metabolism | ok |
| Hyperprolinemia_Type_2 | ALDH4A1 | CAUSATIVE | COMPLETE | GO:0003842 GO:0006562 | proline_metabolism | ok |
| Hypobetalipoproteinemia | APOB | CAUSATIVE | COMPLETE | GO:0034379 | chylomicron_assembly_secretion (not covering) ldl_receptor_mediated_endocytosis (not covering) | MODULE_NOT_COVERING |
| Hypobetalipoproteinemia | PNPLA3 | MODIFIER | COMPLETE | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| Hypobetalipoproteinemia | PCSK9 | CAUSATIVE | COMPLETE | GO:0050750 | ldl_receptor_mediated_endocytosis | ok |
| Hypobetalipoproteinemia | ANGPTL3 | CAUSATIVE | COMPLETE | GO:0055102 | - | NO_MODULE_MEMBERSHIP |
| Inborn_Disorder_of_Bile_Acid_Synthesis | - | - | - | - | - | NO_GENE_RECORD: Grouping-like entry; genes are carried by its subtypes. |
| Infantile-Onset_Pompe_Disease | GAA | CAUSATIVE | COMPLETE | GO:0004558 | lysosomal_glycogen_degradation | ok |
| LDLR-Related_Familial_Hypercholesterolemia | LDLR | CAUSATIVE | COMPLETE | GO:0005041 | ldl_receptor_mediated_endocytosis | ok |
| LPIN1-Related_Recurrent_Myoglobinuria | LPIN1 | CAUSATIVE | COMPLETE | GO:0008195 | triacylglycerol_biosynthesis | ok |
| Late-Onset_Pompe_Disease | GAA | CAUSATIVE | COMPLETE | GO:0004558 | lysosomal_glycogen_degradation | ok |
| Leber-like_Hereditary_Optic_Neuropathy_Autosomal_Recessive_1 | DNAJC30 | CAUSATIVE | COMPLETE | GO:0019899 GO:0034367 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TL1 | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-ND5 | CAUSATIVE | COMPLETE | GO:0008137 | mitochondrial_complex_i_core | ok |
| MELAS_Syndrome | MT-ND1 | CAUSATIVE | COMPLETE | GO:0008137 | mitochondrial_complex_i_core | ok |
| MELAS_Syndrome | MT-ND6 | CAUSATIVE | COMPLETE | GO:0008137 | mitochondrial_complex_i_core | ok |
| MELAS_Syndrome | MT-TQ | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TH | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TK | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TC | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TS1 | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TS2 | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TV | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TW | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TM | CAUSATIVE | COMPLETE | GO:0032543 | - | NO_MODULE_MEMBERSHIP |
| MEND_Syndrome | EBP | CAUSATIVE | COMPLETE | GO:0006695 GO:0047750 | cholesterol_synthesis_post_lanosterol | ok |
| MEND_Syndrome | APOA5 | MODIFIER | - | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| MEND_Syndrome | ABCA1 | MODIFIER | COMPLETE | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| MEND_Syndrome | APOB | MODIFIER | COMPLETE | - | chylomicron_assembly_secretion ldl_receptor_mediated_endocytosis | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| MSMO1_Deficiency | MSMO1 | CAUSATIVE | COMPLETE | GO:0000254 GO:0006695 | cholesterol_synthesis_post_lanosterol | ok |
| MTHFD1_Deficiency | MTHFD1 | CAUSATIVE | COMPLETE | GO:0004329 GO:0004477 GO:0004488 | folate_one_carbon_interconversion | ok |
| Methylmalonic_Acidemia_With_Homocystinuria_Type_cblJ | ABCD4 | CAUSATIVE | COMPLETE | GO:0015420 | cobalamin_intracellular_processing | ok |
| Mevalonate_Kinase_Deficiency | MVK | CAUSATIVE | COMPLETE | GO:0004496 GO:0008299&rarr;GO:0019287 | mevalonate_pathway | ok |
| Mitchell_Syndrome | ACOX1 | CAUSATIVE | COMPLETE | GO:0003997 | peroxisomal_beta_oxidation | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_12 | NDUFA1 | CAUSATIVE | COMPLETE | GO:0008137 | complex_i_accessory_subunits (not covering) | MODULE_NOT_COVERING |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_19 | FOXRED1 | CAUSATIVE | COMPLETE | GO:0016491 GO:0032981 | complex_i_assembly_factors | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_2 | NDUFS8 | CAUSATIVE | COMPLETE | GO:0051539 | mitochondrial_complex_i_core | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_21 | NUBPL | CAUSATIVE | COMPLETE | GO:0016226 | complex_i_assembly_factors (not covering) | MODULE_NOT_COVERING |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_3 | NDUFS7 | CAUSATIVE | COMPLETE | GO:0051539 | mitochondrial_complex_i_core | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_6 | NDUFS2 | CAUSATIVE | COMPLETE | GO:0008137 GO:0048039 | mitochondrial_complex_i_core | ok |
| Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_1 | ATPAF2 | CAUSATIVE | COMPLETE | GO:0033615 GO:0044183 | mitochondrial_complex_v | ok |
| Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_2 | TMEM70 | CAUSATIVE | COMPLETE | GO:0030674 | mitochondrial_complex_v | ok |
| Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_3 | ATP5F1E | CAUSATIVE | COMPLETE | GO:0005198 | mitochondrial_complex_v | ok |
| Mucolipidosis_Type_II | GNPTAB | CAUSATIVE | COMPLETE | GO:0003976 GO:0006622&rarr;GO:0016256 GO:0016256 | mannose_6_phosphate_lysosomal_targeting | ok |
| Muscular_Dystrophy_Congenital_Hearing_Loss_And_Ovarian_Insufficiency_Syndrome | GGPS1 | CAUSATIVE | COMPLETE | GO:0004311 | isoprenoid_diphosphate_biosynthesis | ok |
| Muscular_Dystrophy_Limb-girdle_Autosomal_Recessive_28 | HMGCR | CAUSATIVE | COMPLETE | GO:0004420 | mevalonate_pathway | ok |
| NAGA_Deficiency_Type_3 | NAGA | CAUSATIVE | COMPLETE | GO:0006516 GO:0008456 | lysosomal_glycoprotein_degradation | ok |
| Neuropathy_Hereditary_Motor_And_Sensory_Type_VIc_With_Optic_Atrophy | PDXK | CAUSATIVE | COMPLETE | GO:0008478 | vitamin_b6_plp_metabolism | ok |
| Neutral_Lipid_Storage_Myopathy | PNPLA2 | CAUSATIVE | COMPLETE | GO:0004806 GO:0019433 | triacylglycerol_lipolysis | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | LEP | CAUSATIVE | COMPLETE | GO:0038021&rarr;GO:0033210 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | LEPR | CAUSATIVE | COMPLETE | GO:0038021&rarr;GO:0033210 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | POMC | CAUSATIVE | COMPLETE | GO:0031782 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | PCSK1 | CAUSATIVE | COMPLETE | GO:0004252 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | MC4R | CAUSATIVE | COMPLETE | GO:0004980 GO:0007189 | leptin_melanocortin_signaling | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | SH2B1 | SUSCEPTIBILITY | - | - | - | NO_AIGR_REVIEW |
| Obesity_Due_to_MC4R_Pathway_Disruption | NCOA1 | SUSCEPTIBILITY | - | - | - | NO_AIGR_REVIEW |
| Obesity_Due_to_MC4R_Pathway_Disruption | SIM1 | CAUSATIVE | COMPLETE | GO:0000981 | - | NO_MODULE_MEMBERSHIP |
| PET100-Related_COX_Deficiency | PET100 | CAUSATIVE | COMPLETE | GO:0033617 | complex_iv_assembly_factors | ok |
| PGM1-Congenital_Disorder_of_Glycosylation | PGM1 | CAUSATIVE | COMPLETE | GO:0004614 | glycogenolysis | ok |
| PNPO_Deficiency | PNPO | CAUSATIVE | COMPLETE | GO:0004733 | vitamin_b6_plp_metabolism | ok |
| Peroxisomal_Acyl-CoA_Oxidase_Deficiency | ACOX1 | CAUSATIVE | COMPLETE | GO:0003997 GO:0033540 GO:0140493 | peroxisomal_beta_oxidation | ok |
| Peroxisome_Biogenesis_Disorder_5B | PEX2 | CAUSATIVE | COMPLETE | GO:0007031&rarr;GO:0016558 | peroxisome-lifecycle | ok |
| Peroxisome_Biogenesis_Disorder_6A_Zellweger | PEX10 | CAUSATIVE | COMPLETE | GO:0061630 | peroxisome-lifecycle | ok |
| Peroxisome_Biogenesis_Disorder_6B | PEX10 | CAUSATIVE | COMPLETE | GO:0061630 | peroxisome-lifecycle | ok |
| Pompe_Disease | GAA | CAUSATIVE | COMPLETE | GO:0004558 GO:0005980 | lysosomal_glycogen_degradation | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ2 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008412 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ4 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425&rarr;GO:0006744 GO:0120539&rarr;GO:0006744 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ5 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425&rarr;GO:0006744 GO:0120539&rarr;GO:0006744 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ6 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425&rarr;GO:0006744 GO:0106364 GO:0120539&rarr;GO:0006744 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ8A | CAUSATIVE | COMPLETE | GO:0006744 GO:0016887 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ8B | CAUSATIVE | COMPLETE | GO:0006744 GO:0016887 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ7 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425&rarr;GO:0006744 GO:0120539&rarr;GO:0006744 GO:0160224 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | COQ9 | CAUSATIVE | COMPLETE | GO:0006744 GO:0008425&rarr;GO:0006744 GO:0120539&rarr;GO:0006744 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | PDSS1 | CAUSATIVE | COMPLETE | GO:0006744 GO:0097269 | coenzyme_q10_biosynthesis | ok |
| Primary_Coenzyme_Q10_Deficiency | PDSS2 | CAUSATIVE | COMPLETE | GO:0006744 GO:0097269 | coenzyme_q10_biosynthesis | ok |
| Primary_Hyperoxaluria_Type_1 | AGXT | CAUSATIVE | COMPLETE | GO:0008453 GO:0009436 | glyoxylate_oxalate_metabolism | ok |
| Primary_Hyperoxaluria_Type_2 | GRHPR | CAUSATIVE | COMPLETE | GO:0016618 GO:0030267 GO:0046487 | glyoxylate_oxalate_metabolism | ok |
| Primary_Hyperoxaluria_Type_3 | HOGA1 | CAUSATIVE | COMPLETE | GO:0008700 GO:0019470 | glyoxylate_oxalate_metabolism | ok |
| Primary_Hyperoxaluria_Type_3 | AGXT | MODIFIER | COMPLETE | - | glyoxylate_oxalate_metabolism | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Purine_Nucleoside_Phosphorylase_Deficiency | PNP | CAUSATIVE | COMPLETE | GO:0004731 GO:0006152&rarr;GO:0006148 | purine_nucleotide_catabolism purine_salvage_and_catabolism | ok |
| Pyridoxine-Dependent_Epilepsy | ALDH7A1 | CAUSATIVE | COMPLETE | GO:0004029 GO:0004043 GO:0019477 | lysine_catabolism_saccharopine | ok |
| Pyruvate_Carboxylase_Deficiency_Disease | PC | CAUSATIVE | COMPLETE | GO:0004736 GO:0006094 | gluconeogenesis_human gluconeogenesis_human_substrates pyruvate_metabolism | ok |
| RFT1-congenital_disorder_of_glycosylation | RFT1 | CAUSATIVE | COMPLETE | GO:0140303 | n_glycan_llo_assembly_lumenal | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect | GNPAT | CAUSATIVE | COMPLETE | GO:0008611 GO:0016287 | ether_lipid_plasmalogen_biosynthesis | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect | AGPS | CAUSATIVE | COMPLETE | GO:0008609 GO:0008611 | ether_lipid_plasmalogen_biosynthesis | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect | FAR1 | CAUSATIVE | COMPLETE | GO:0008611 GO:0102965 | ether_lipid_plasmalogen_biosynthesis | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Type_1 | PEX7 | CAUSATIVE | COMPLETE | GO:0000268 GO:0016558 | peroxisome-lifecycle | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Type_5 | PEX5 | CAUSATIVE | COMPLETE | GO:0016558 GO:0140597 | peroxisome-lifecycle | ok |
| SCO1-Related_COX_Deficiency | SCO1 | CAUSATIVE | COMPLETE | GO:0016531 GO:0033617 | complex_iv_assembly_factors | ok |
| SECISBP2_Deficiency | SECISBP2 | CAUSATIVE | COMPLETE | GO:0001514 GO:0035368 | selenocysteine_biosynthesis_incorporation | ok |
| SEPSECS_Deficiency | SEPSECS | CAUSATIVE | COMPLETE | GO:0001717 GO:0016260 GO:0098621 | selenocysteine_biosynthesis_incorporation | ok |
| SLC26A1-Related_Hypersulfaturia | SLC26A1 | CAUSATIVE | COMPLETE | GO:0015383 GO:1902358&rarr;GO:0015383 | - | NO_MODULE_MEMBERSHIP |
| SLC26A1-Related_Oxalate_Transporter_Deficiency | SLC26A1 | CAUSATIVE | COMPLETE | GO:0015116&rarr;GO:0015383 GO:0019531 GO:0019532&rarr;GO:0019531 GO:1902358&rarr;GO:0015383 | - | NO_MODULE_MEMBERSHIP |
| SLC26A6-Related_Hyperoxaluria_and_Nephrolithiasis | SLC26A6 | CAUSATIVE | COMPLETE | GO:0019531 GO:0019532&rarr;GO:0019531 | - | NO_MODULE_MEMBERSHIP |
| SLC35A1-Congenital_Disorder_of_Glycosylation | SLC35A1 | CAUSATIVE | COMPLETE | GO:0005456 | sialic_acid_metabolism | ok |
| STT3A-Congenital_Disorder_of_Glycosylation | STT3A | CAUSATIVE | COMPLETE | GO:0004579 | oligosaccharyltransferase_complex | ok |
| SUCLA2-Related_Mitochondrial_DNA_Depletion_Syndrome | SUCLA2 | CAUSATIVE | COMPLETE | GO:0004775 | tca_cycle | ok |
| Severe_X-linked_Mitochondrial_Encephalomyopathy | AIFM1 | CAUSATIVE | COMPLETE | GO:0043495 | apoptotic_execution_phase (not covering) | MODULE_NOT_COVERING |
| Short_Stature_Amelogenesis_Imperfecta_And_Skeletal_Dysplasia_With_Scoliosis | SLC10A7 | CAUSATIVE | COMPLETE | GO:0032468&rarr;GO:0006874 GO:0051480&rarr;GO:0006874 | - | NO_MODULE_MEMBERSHIP |
| Sitosterolemia | ABCG5 | CAUSATIVE | COMPLETE | GO:0015918&rarr;GO:0033344 GO:0034041 | intestinal_sterol_absorption_and_efflux | ok |
| Sitosterolemia | ABCG8 | CAUSATIVE | COMPLETE | GO:0015918 GO:0034041 | intestinal_sterol_absorption_and_efflux | ok |
| Snyder-Robinson_Syndrome | SMS | CAUSATIVE | COMPLETE | GO:0006597 GO:0016768 | polyamine_metabolism | ok |
| Spastic_Paraparesis-cataracts-speech_Delay_Syndrome | FAR1 | CAUSATIVE | COMPLETE | GO:0102965 | ether_lipid_plasmalogen_biosynthesis | ok |
| Sphingosine_Phosphate_Lyase_Insufficiency_Syndrome | SGPL1 | CAUSATIVE | COMPLETE | GO:0008117 | sphingosine_1_phosphate_rheostat | ok |
| Sterol_Carrier_Protein_2_Deficiency | SCP2 | CAUSATIVE | COMPLETE | GO:0050632 | peroxisomal_beta_oxidation | ok |
| Triglyceride_Storage_Disease_Type_1 | - | - | - | - | - | NO_GENE_RECORD: Historical OMIM:190420 phenotype; no gene has been reported (ABHD5 content lives in Dorfman_Chanarin_Disease). |
| Type_I_Diabetes | INS | SUSCEPTIBILITY | COMPLETE | - | beta_cell_glucose_stimulated_insulin_secretion | NO_GO_ON_GENE_NODES |
| Type_I_Diabetes | PTPN22 | SUSCEPTIBILITY | IN_PROGRESS | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | IL2RA | SUSCEPTIBILITY | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | CTLA4 | SUSCEPTIBILITY | COMPLETE | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | TYK2 | SUSCEPTIBILITY | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Type_I_Diabetes | IFIH1 | SUSCEPTIBILITY | COMPLETE | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | BACH2 | SUSCEPTIBILITY | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | TNFAIP3 | SUSCEPTIBILITY | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | EGR2 | SUSCEPTIBILITY | IN_PROGRESS | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | IRF4 | SUSCEPTIBILITY | DRAFT | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | IKZF1 | SUSCEPTIBILITY | IN_PROGRESS | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Vitamin_D-Dependent_Rickets_Type_1A | CYP27B1 | CAUSATIVE | COMPLETE | GO:0004498 | fgf23_klotho_phosphate_homeostasis vitamin_d_activation_signaling | ok |
| Vitamin_D-Dependent_Rickets_Type_2B | - | - | - | - | - | NO_GENE_RECORD: Genetic basis unknown; HNRNPC is modelled as a mechanism actor, not a causal gene. |
| Wilsons_Disease | ATP7B | CAUSATIVE | COMPLETE | GO:0006825&rarr;GO:0015677 GO:0035434&rarr;GO:0060003 GO:0055070&rarr;GO:0006878 GO:0140581 | cuproptosis | ok |
| Wolman_Disease | LIPA | CAUSATIVE | COMPLETE | GO:0004771 GO:0004806 GO:0019433&rarr;GO:0046461 GO:0046461 | ldl_receptor_mediated_endocytosis | ok |
| X-linked_Chondrodysplasia_Punctata_2 | EBP | CAUSATIVE | COMPLETE | GO:0006695 GO:0047750 | cholesterol_synthesis_post_lanosterol | ok |

## Notes on remaining flags

- Every causative gene row is free of flags other than the two module flags. The other flags
  fall on modifier, susceptibility and disputed genes, none of which were required to align.
- **MELAS mtDNA genes**: MT-ND1, MT-ND5 and MT-ND6 have reviews and are parts of
  mitochondrial_complex_i_core, aligning with the dismech complex I node (NADH:ubiquinone
  oxidoreductase activity, DECREASED). The ten mt-tRNA genes (MT-TL1, MT-TQ, MT-TH, MT-TK,
  MT-TC, MT-TS1, MT-TS2, MT-TV, MT-TW, MT-TM) have ncRNA reviews (RNAcentral ids) whose core
  function, triplet codon-amino acid adaptor activity in mitochondrial translation, matches
  the dismech translation-defect nodes.
- **UCP2** (DISPUTED): dismech binds regulation of insulin secretion (GO:0050796), which
  is the parent of a UCP2 annotation the review keeps as non-core (GO:0061179), so the row
  is `ALIGNED_NONCORE`. dismech deliberately binds no UCP2
  activity, because its causal role in hyperinsulinism and its transported substrate
  are both disputed.
- **TMEM251** is the dismech/HGNC-build label for the gene now named LYSET; it is matched to
  the LYSET review.
- **Type I diabetes risk loci** (PTPN22, IL2RA, CTLA4, IFIH1, BACH2, TNFAIP3, EGR2, IRF4, IKZF1,
  TYK2) are SUSCEPTIBILITY records with no single pathway step; several ai-gene-review entries
  for them are still drafts from other projects.

## Causative genes without a covering module, and why

- **TRMT10C**: RNase P partners (HSD17B10, PRORP, ELAC2) lack completed reviews.
- **ANGPTL3**: No LPL / plasma triglyceride clearance module; LPL review still DRAFT.
- **CTNS**: Lysosomal cystine export is a single step.
- **SLC26A1**: Epithelial oxalate/sulfate transport has no coherent multi-part module yet; SLC26A1's oxalate role is contested.
- **SLC26A6**: As SLC26A1; a two-part oxalate-transport module is possible later.
- **DMP1**: No module contains DMP1 as a part. It is named in the notes of fgf23_klotho_phosphate_homeostasis as regulatory context, which this audit deliberately does not count as membership, and its mechanism is undefined.
- **SLC10A7**: Single gene with unknown transported substrate.
- **DNAJC30**: Complex I N-module repair is not assembly; no repair module exists.
- **LCT**: Brush-border disaccharide digestion: only LCT has a completed review (SI, MGAM, TREH missing).
- **HNF1A / HNF4A**: Transcription factors whose hyperinsulinism and MODY roles act through many target genes; no beta-cell transcriptional-network module exists yet.
- **SLC16A1**: Disease mechanism is ectopic beta-cell expression of a transporter whose normal role (lactate/pyruvate transport) belongs to no beta-cell pathway; a monocarboxylate-transport module would not include the disease mechanism.
- **SIM1**: Transcription factor needed for paraventricular hypothalamic neuron development and function; it acts on, rather than within, the leptin_melanocortin_signaling module, whose parts are the ligand, processing and receptor steps.
- **MT-TL1 / MT-TQ / MT-TH / MT-TK / MT-TC / MT-TS1 / MT-TS2 / MT-TV / MT-TW / MT-TM**: No mitochondrial translation module exists; in mitochondrial_trna_charging_and_initiator_formylation a tRNA would appear only as a synthetase substrate, which the substrate guidance excludes, and module parts are UniProt proteins.
- **UCP2**: Causal role disputed (relationship DISPUTED); its transported substrate is itself contested.
- **AIFM1**: The aligned function is the mitochondrial disulfide relay (CHCHD4 anchoring); no module covers the relay. AIFM1 is a part of apoptotic_execution_phase, whose AIFM1 annoton carries DNA binding, nucleus and positive regulation of apoptotic process: a different AIFM1 activity, and not the encephalomyopathy mechanism.
- **APOB**: The aligned term is GO:0034379 very-low-density lipoprotein particle assembly, and there is no VLDL-assembly module. APOB is a part of chylomicron_assembly_secretion, whose scope is GO:0034378 chylomicron assembly, and of ldl_receptor_mediated_endocytosis, which is about the receptor taking the particle up. GO:0034378 and GO:0034379 are siblings, not one inside the other, so the hepatic VLDL step is genuinely unmodelled. APOB's other row, the LDL-receptor-binding one, is covered.
- **NUBPL**: The aligned term is GO:0016226 iron-sulfur cluster assembly. NUBPL is a part of complex_i_assembly_factors, whose scope is GO:0032981 mitochondrial respiratory chain complex I assembly: NUBPL delivers an Fe-S cluster to the assembling complex, and the cluster's own assembly is a different process that no module covers.
- **NDUFA1**: A limitation of the coverage test rather than a modelling gap, and left flagged rather than waived. The dismech node binds the molecular function GO:0008137 NADH dehydrogenase (ubiquinone) activity, while complex_i_accessory_subunits declares its scope as the biological process GO:0006120 mitochondrial electron transport, NADH to ubiquinone. Those are the same chemistry in two GO aspects, and is_a/part_of ancestry does not cross between molecular function and biological process, so no amount of ontology walking will relate them. The module is the right one.
