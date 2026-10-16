---
title: dismech metabolic disorders aligned with ai-gene-review
maturity: IN_PROGRESS
description: Per-entry check that dismech metabolic disease mechanisms agree with ai-gene-review core functions and modules
species: [human]
genes: [ABCA1, ABCC8, ABCD3, ABCD4, ABCG5, ABCG8, ABHD5, ACOX1, AGA, AGPS, AGXT, AHCY, AIFM1, ALDH4A1, ALDH7A1, ANGPTL3, APOB, ATP5F1E, ATP7B, ATPAF2, BACH2, BTD, CAD, COQ2, COQ4, COQ5, COQ6, COQ7, COQ8A, COQ8B, COQ9, COX18, COX20, COX4I2, CTLA4, CTNS, CYP27B1, DHFR, DMP1, DNAJC30, DPM2, EBP, EEFSEC, EGR2, FAR1, FBP1, FBXL4, FGF23, FOXRED1, FUCA1, G6PC1, GAA, GALNT3, GCK, GGPS1, GLB1, GLUD1, GLUL, GNPAT, GNPTAB, GPD1, GRHPR, HADH, HAO1, HK1, HMGCR, HMOX1, HNF1A, HNF4A, HOGA1, HSD17B4, IFIH1, IKZF1, IL2RA, INS, IRF4, KCNJ11, KL, LBR, LCT, LDLR, LEP, LEPR, LIPA, LPIN1, LYSET, MC4R, MFF, MSMO1, MT-ND1, MT-ND5, MT-ND6, MT-TC, MT-TH, MT-TK, MT-TL1, MT-TM, MT-TQ, MT-TS1, MT-TS2, MT-TV, MT-TW, MTFMT, MTHFD1, MVK, NAGA, NDUFA1, NDUFS2, NDUFS7, NDUFS8, NSDHL, NUBPL, ODC1, PC, PCSK1, PCSK9, PDSS1, PDSS2, PDXK, PET100, PEX10, PEX2, PEX5, PEX7, PGM1, PNP, PNPLA2, PNPLA3, PNPO, POMC, PRODH, PTPN22, RFT1, SAR1B, SCO1, SCP2, SECISBP2, SEPSECS, SGPL1, SIM1, SLC10A7, SLC16A1, SLC26A1, SLC26A6, SLC35A1, SLC37A4, SMS, STT3A, SUCLA2, TARS2, TMEM70, TNFAIP3, TRMT10C, UCP2]
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
table (`report.yaml`) are in the `projects/DISMECH_METABOLIC_ALIGNMENT/` directory of the repository, with `check_page_guards.py` exercising the generator's refusals (`just check-alignment-page-guards`, also run by the pytest suite), together with the second report the audit self-check page beside this one ([audit-self-check](DISMECH_METABOLIC_ALIGNMENT/audit-self-check.md)) is derived from (`report-branch-local.yaml`), the same audit run over `132532cf6`.

**What "aligned" does and does not claim.** Five properties of the test make it a weak
check, and any of them can turn a row green that a curator would not:

- The relation is **symmetric** and **unbounded in distance**. A node term counts as aligned
  when either it or the core term is an is_a/part_of ancestor of the other, at any depth. So a
  dismech node bound to something broad aligns with a specific core function, and the reverse,
  and two terms many levels apart still align. The table therefore prints the core term each
  node term matched (`node->core`, or the term alone where the two are identical), so the
  distance behind a match is visible per row. `DMP1 | GO:0005509` (calcium ion binding) is the
  clearest row where the verdict carries little information; reading a row as agreement means
  reading its pair.
- A dismech node binds its GO terms **at node level**, and a node may name several genes.
  dismech has no per-gene attribution inside a node, so every term on a shared node is read
  for every gene on it, and a row can align on a co-named partner's activity. The column
  marks such a term `s`, and `ALIGNED_ON_SHARED_NODE_ONLY` fires where *every* term a row
  aligned on came from a shared node. The hyperinsulinism node naming both GLUD1 and HADH,
  which carries glutamate dehydrogenase activity and enzyme inhibitor activity together, is
  the case to read: each gene is credited with both, and here that happens to be right in
  both directions (HADH does inhibit GLUD1), which is exactly why it needs marking rather
  than trusting. The flag is conservative by construction and fires on a large minority of
  rows, so read it with this alongside: of the 48 principal rows it fires on,
  31 align **only** on node terms identical to one of the gene's own core
  functions, so the review asserts each of those activities in its own right and the shared
  node earned none of the match. A further 12 have at least one
  such identical term but not all of them, so part of the verdict still rests on a
  partner-derived term, and 5 have none at all. GLUD1 and its
  `GO:0004353` are of the first shape. Only the identical terms license reading the flag as
  harmless, which is why the three figures are given separately rather than summed.
- `contributes_to_molecular_function` is compared **alongside** core molecular function. A
  subunit that contributes to a complex-level activity without enabling it is doing what the
  dismech node describes, so excluding it would lose real agreement; but it is a weaker claim,
  so a term matched only that way is marked `c` and `ALIGNED_CONTRIBUTES_ONLY` fires where a
  row's whole alignment rests on one.
- Node MF and BP terms are compared against **one pooled set** of the review's core molecular
  functions and `directly_involved_in` processes, so a node activity term can be satisfied by
  a core process and the reverse. Such a match is genuine agreement but weaker than a
  same-aspect one; the cross-aspect paragraph below gives the figures and a worked row.
- Module **membership** is not module **coverage**. Membership says the gene is a part of some
  module; coverage says a module is about the function the row aligned on, which is a different
  and stronger claim. They are flagged separately in three states: `NO_MODULE_MEMBERSHIP` means
  no module contains the gene; `MODULE_NOT_COVERING` means one does but no term anywhere in any
  of those modules is related to the aligned terms, and such a module is marked
  `(not covering)` in the Modules column; and `PARTIAL_COVERAGE` (14 principal
  rows) means a module covers some of the aligned terms while no module term reaches the rest,
  which the Modules column names term by term after `- uncovered:`. The third state is not a
  defect to fix: a module is scoped to a process, so it will often reach the aligned term that
  names that process and not a second term naming a different activity of the same gene.
  AIFM1 is the row `MODULE_NOT_COVERING` exists to catch: it sits
  in `apoptotic_execution_phase`, whose AIFM1 annoton carries DNA binding, nucleus and
  positive regulation of apoptotic process, while the aligned function is the mitochondrial
  disulfide relay. No module covers the relay.

Coverage reads the module's declared `concepts`, at module level and per node, as well as its
annotons' terms: a module states its scope as processes while its annotons carry the molecular
functions of individual parts, so annotons alone miss what the module is about. One limitation
survives that and is left visible rather than waived: coverage is asymmetric about complex
membership. It accepts a `contributes_to_molecular_function` term from the review, but cannot
read a module's GO-idiomatic way of saying the same thing - a subunit given `GO:0005198`
structural molecule activity as part of the complex - as the same claim, because a structural
role and the activity it supports are unrelated branches of molecular function. NDUFA1 is the
row where that decides the verdict.

`is_a`/`part_of` ancestry does cross between molecular function and biological process, and
that crossing is a real source of alignment here: GO asserts `part_of` from transporter
activities to the transport processes they carry out.
29 rows of all 183 - not only the principal ones - carry at least one such pair, and on 2 of them the row has no same-aspect pair at all, so the crossing is what earns the verdict - MT-ND1 matches `GO:0008137` (MF) to `GO:1902600` (BP).
Where a particular pair does not meet, that is a fact about the pair rather than about the
aspects - `GO:0008137` does not reach `GO:0006120`. Two things follow. Cross-aspect
`part_of` is a real source of
alignment in this table, not an artefact - and since node MF and BP terms are compared against
one pooled set of the review's core molecular functions and `directly_involved_in` processes,
a node activity term can be satisfied by a core process and the reverse. Such a match is
genuine agreement but weaker than a same-aspect one, and `aligned_pairs` records which core
term each node term matched so a reader can see which shape any given row is.

Membership is read from the module structure (`parts[].node.annotons[]`, following the
participant whichever selector it uses - `gene_product`, `gene`, `ortholog_of`, `homolog_of`,
a `FAMILY` participant's `representative_members`, and a protein complex's `active_units`) and
following nested parts and variant sets, so a gene named only in a module's notes or evidence
does not count as a part. The run records both counts in its provenance below, so the gap
between reading the structure and reading the file text is a measured figure rather than a
quoted one.

Flags, with the qualifying ones marked - a qualifying flag says the verdict is weaker than
`ok` would suggest, so those are counted separately below rather than absorbed into one
clean figure:

- `GENE_ON_NO_NODE` - no pathophysiology node names the gene
- `NO_GO_ON_GENE_NODES` - no node naming the gene carries a GO term
- `NO_ORIGIN` - the dismech genetic record carries no variant origin
- `UNTYPED` - the dismech genetic record carries no relationship type - not emitted by either run
- `NO_AIGR_REVIEW` - no ai-gene-review review exists for the gene
- `AIGR_NOT_COMPLETE` - a review exists but its status is not COMPLETE
- `NO_CORE_FUNCTION_TERMS` - a review exists but has no core-function GO term to compare against
- `NO_MODULE_MEMBERSHIP` - no module contains the gene's accession
- `MODULE_NOT_COVERING` - a module contains it, but no annoton term there relates to the aligned terms
- `PARTIAL_COVERAGE` *(qualifying)* - a module covers some aligned terms and no module term reaches the rest
- `ALIGNED_CONTRIBUTES_ONLY` *(qualifying)* - every aligned term matched only a contributes-to function, not an enabled one
- `ALIGNED_NONCORE` - node terms match only annotations the review keeps as non-core
- `ALIGNED_ON_SHARED_NODE_ONLY` *(qualifying)* - every aligned term came from a node the gene shares with another gene
- `ALIGNED_PROPOSED` - node terms match only terms the review proposes as NEW, which are not yet annotations - not emitted by either run
- `NO_GO_ALIGNMENT` - no node term matches a core function, an annotation the review keeps, or a term it proposes - not emitted by either run
- `PARTIAL_ALIGNMENT` *(qualifying)* - some node terms aligned and others matched nothing in the review

**Provenance of this run.** The table is generated, so it is only as current as the inputs it
was generated from, and those inputs live in two repositories.

- run date: `2026-10-16T19:52:02Z`
- dismech revision: `048e13ca1cce71320ff1789f01ba353af6da6bf8` (048e13ca1 2026-10-16 curate: Add AKT3-Related Overgrowth Spectrum (MONDO:0800485) (#14361))
- ai-gene-review revision: `c8848254e9e1dfa8e8c98dd2cc485d36e8750d65` (branch `claude/cool-edison-o9wvf0-alignment-project`)
- GO release: `2026-07-26`, adapter `sqlite:obo:go`
- audit script: `906bd065421d` (sha256 of `align_audit.py`), last committed at `c8848254e`
- The primary run's tree (`c8848254e`) is on a pushed ref, so the same comparison can be made for the table's own figures.
- modules read: `489`; UniProt accessions reached as parts: `5228`, against `5298` matching the accession pattern anywhere in the module file text. Both are sums over modules of that module's distinct accessions, so a protein in several modules counts once per module; the difference is accessions mentioned in notes or evidence of a module they are not a part of, which this audit does not count as membership.

The gene reviews and modules this table asserts `COMPLETE` for are on `main`: the ten
themed PRs split out of #4690 have all merged, so an ordinary checkout holds them.
The run above read a clean checkout, so the revision above describes its tree in full.

The same audit was run a second time over a different tree, and the two runs' flag counts are reconciled row by row in [the audit self-check](DISMECH_METABOLIC_ALIGNMENT/audit-self-check.md). That is a check on the generator rather than a finding about the two resources, so it is kept beside the page rather than in it.
**Summary.** 116 entries; 161 principal gene rows (all causative in this run; the predicate also admits untyped), of which 105 align every GO term their dismech nodes carry and 56 align some and leave others unaligned. Read that split first: the flag-free count below is close to true by construction, because `NO_GO_ALIGNMENT` is the only hard flag while `PARTIAL_ALIGNMENT`, `ALIGNED_ON_SHARED_NODE_ONLY` and `PARTIAL_COVERAGE` are all soft, so it is not a measure of full agreement.

161 principal rows carry no flag other than a module flag or one of the qualifying flags - none carries `NO_GO_ALIGNMENT`, `NO_CORE_FUNCTION_TERMS`, `NO_GO_ON_GENE_NODES` or `GENE_ON_NO_NODE`. That count also tolerates `ALIGNED_NONCORE` and `ALIGNED_PROPOSED`, which say a row aligned only against a retained non-core or a proposed term rather than a core function; no principal row in this run carries either. Flag counts on principal rows: `ALIGNED_CONTRIBUTES_ONLY` 1, `ALIGNED_ON_SHARED_NODE_ONLY` 48, `MODULE_NOT_COVERING` 4, `NO_MODULE_MEMBERSHIP` 26, `PARTIAL_ALIGNMENT` 56, `PARTIAL_COVERAGE` 14. These are principal rows only, so they are smaller than the all-row counts in the provenance section above wherever a flag also falls on a modifier, susceptibility or disputed row.

**Agreement is partial on many rows, and the table shows both halves.** 105 principal
rows align every GO term their dismech nodes carry; 56 align some and leave others
matching nothing in the gene review. A partial row is usually not a defect in either
repository - it is dismech modelling a step of the disease mechanism that is not part of the
gene's normal function, which is what the two resources are each for. `LCT` is the clearest
case: the row aligns `GO:0000016` lactase activity and leaves `GO:0006366` transcription by
RNA polymerase II unaligned, because the hypolactasia mechanism is the enhancer that switches
the gene off, and transcribing its own gene is not a function of lactase. Reading such a row
as full agreement would be wrong in the other direction, so the unaligned terms are printed
rather than dropped.

Polygenic entries (Type I diabetes) and modifier/susceptibility genes are
listed but were not required to align: their genes are risk loci or modifiers, not the
normal-function owners of a single pathway step.

In the GO-term columns, <sup>c</sup> marks a term matched only through the review's
`contributes_to_molecular_function`, and <sup>s</sup> a term the gene holds only because
another gene is named on the same dismech node. Where a node term relates to several core
terms, all of them are shown separated by `/`.

| Entry | Gene | Relationship | AIGR | Aligned GO terms (node&rarr;core) | Unaligned node terms | Modules | Flags |
|---|---|---|---|---|---|---|---|
| 3-hydroxyacyl-CoA_Dehydrogenase_Deficiency | HADH | CAUSATIVE | COMPLETE | GO:0003857 GO:0004857 | - | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0004857->GO:0004857) [fatty_acid_beta_oxidation](../modules/fatty_acid_beta_oxidation.html) (GO:0003857->GO:0003857, GO:0003857->GO:0016509) | ok |
| AHCY_Deficiency | AHCY | CAUSATIVE | COMPLETE | GO:0004013 | - | [methionine_cycle](../modules/methionine_cycle.html) (GO:0004013->GO:0004013) [sam_cycle](../modules/sam_cycle.html) (GO:0004013->GO:0004013) | ok |
| Adult-Type_Hypolactasia | LCT | CAUSATIVE | COMPLETE | GO:0000016 | GO:0006366 | - | PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Autosomal_Dominant_Hypercholesterolemia_3 | PCSK9 | CAUSATIVE | COMPLETE | GO:0050750 | - | [ldl_receptor_mediated_endocytosis](../modules/ldl_receptor_mediated_endocytosis.html) (GO:0050750->GO:0050750) | ok |
| Autosomal_Recessive_Hypophosphatemic_Rickets_1 | DMP1 | CAUSATIVE | COMPLETE | GO:0005509 | - | - | NO_MODULE_MEMBERSHIP |
| Bachmann-Bupp_Syndrome | ODC1 | CAUSATIVE | COMPLETE | GO:0004586 GO:0006596&rarr;GO:0009446 | - | [polyamine_metabolism](../modules/polyamine_metabolism.html) (GO:0004586->GO:0004586, GO:0006596->GO:0006596) | ok |
| Biotinidase_Deficiency | BTD | CAUSATIVE | COMPLETE | GO:0006768 GO:0047708 | - | [biotin_cycle](../modules/biotin_cycle.html) (GO:0006768->GO:0006768, GO:0047708->GO:0047708) | ok |
| CHILD_Syndrome | NSDHL | CAUSATIVE | COMPLETE | GO:0000252 | - | [cholesterol_synthesis_post_lanosterol](../modules/cholesterol_synthesis_post_lanosterol.html) (GO:0000252->GO:0000252) | ok |
| COQ2-Related_Primary_Coenzyme_Q10_Deficiency | COQ2 | CAUSATIVE | COMPLETE | GO:0008412 | - | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0008412->GO:0008412) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0008412->GO:0008412) | ok |
| COX18-Related_COX_Deficiency | COX18 | CAUSATIVE | COMPLETE | GO:0032977 GO:0033617 | - | [complex_iv_assembly_factors](../modules/complex_iv_assembly_factors.html) (GO:0032977->GO:0032977, GO:0033617->GO:0033617) | ok |
| COX20-Related_COX_Deficiency | COX20 | CAUSATIVE | COMPLETE | GO:0030674 GO:0033617 | - | [mitochondrial_complex_iv](../modules/mitochondrial_complex_iv.html) (GO:0030674->GO:0030674, GO:0033617->GO:0033617) | ok |
| COX4I2-Related_Pancreatic_Insufficiency-Anemia-Hyperostosis_Syndrome | COX4I2 | CAUSATIVE | COMPLETE | GO:0004129 <sup>c</sup> GO:0006123 | GO:0001666 | [mitochondrial_complex_iv](../modules/mitochondrial_complex_iv.html) (GO:0006123->GO:0006123) - uncovered: GO:0004129 | PARTIAL_ALIGNMENT, PARTIAL_COVERAGE |
| Chylomicron_Retention_Disease | SAR1B | CAUSATIVE | COMPLETE | GO:0003924 | - | [chylomicron_assembly_secretion](../modules/chylomicron_assembly_secretion.html) (GO:0003924->GO:0003924) | ok |
| Chylomicron_Retention_Disease | SAR1A | MODIFIER | - | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Combined_Oxidative_Phosphorylation_Defect_Type_15 | MTFMT | CAUSATIVE | COMPLETE | GO:0004479&rarr;GO:0004479/GO:0071951 | - | [mitochondrial_trna_charging_and_initiator_formylation](../modules/mitochondrial_trna_charging_and_initiator_formylation.html) (GO:0004479->GO:0004479, GO:0004479->GO:0071951) | ok |
| Combined_Oxidative_Phosphorylation_Defect_Type_21 | TARS2 | CAUSATIVE | COMPLETE | GO:0004829 | - | [mitochondrial_trna_charging_and_initiator_formylation](../modules/mitochondrial_trna_charging_and_initiator_formylation.html) (GO:0004829->GO:0004829) | ok |
| Combined_Oxidative_Phosphorylation_Defect_Type_30 | TRMT10C | CAUSATIVE | COMPLETE | GO:0097745 | - | - | NO_MODULE_MEMBERSHIP |
| Congenital_Bile_Acid_Synthesis_Defect_5 | ABCD3 | CAUSATIVE | COMPLETE | GO:0015607 | GO:0007031 | [bile_acid_synthesis_sidechain_conjugation](../modules/bile_acid_synthesis_sidechain_conjugation.html) (GO:0015607->GO:0015607) [peroxisomal_beta_oxidation](../modules/peroxisomal_beta_oxidation.html) | PARTIAL_ALIGNMENT |
| Congenital_Isolated_Hyperinsulinism | ABCC8 | CAUSATIVE | COMPLETE | GO:0015272&rarr;GO:0071805 <sup>s</sup> GO:0050796 <sup>s</sup> GO:0071805 <sup>s</sup> | - | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0015272->GO:0015272, GO:0015272->GO:0071805, ...) | ALIGNED_ON_SHARED_NODE_ONLY |
| Congenital_Isolated_Hyperinsulinism | KCNJ11 | CAUSATIVE | COMPLETE | GO:0015272&rarr;GO:0015272/GO:0071805 <sup>s</sup> GO:0050796&rarr;GO:0046676 <sup>s</sup> GO:0071805&rarr;GO:0015272/GO:0071805 <sup>s</sup> | - | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0015272->GO:0015272, GO:0015272->GO:0071805, ...) | ALIGNED_ON_SHARED_NODE_ONLY |
| Congenital_Isolated_Hyperinsulinism | GLUD1 | CAUSATIVE | COMPLETE | GO:0004353 <sup>s</sup> | GO:0004857 <sup>s</sup> GO:0030073 <sup>s</sup> | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0004353->GO:0004353) [glutamate_glutamine_ammonia_hub](../modules/glutamate_glutamine_ammonia_hub.html) (GO:0004353->GO:0004353) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Congenital_Isolated_Hyperinsulinism | GCK | CAUSATIVE | COMPLETE | GO:0004340 | - | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0004340->GO:0004340) [glycolysis_investment_phase](../modules/glycolysis_investment_phase.html) (GO:0004340->GO:0004396) | ok |
| Congenital_Isolated_Hyperinsulinism | HADH | CAUSATIVE | COMPLETE | GO:0004857 <sup>s</sup> | GO:0004353 <sup>s</sup> GO:0030073 <sup>s</sup> | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0004857->GO:0004857) [fatty_acid_beta_oxidation](../modules/fatty_acid_beta_oxidation.html) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Congenital_Isolated_Hyperinsulinism | HNF4A | CAUSATIVE | COMPLETE | GO:0001228&rarr;GO:0001228/GO:0045944 | GO:0030073 | - | PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Congenital_Isolated_Hyperinsulinism | SLC16A1 | CAUSATIVE | COMPLETE | GO:0015650&rarr;GO:0015355 GO:1901475 | GO:0030073 | - | PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Congenital_Leptin_Deficiency | LEP | CAUSATIVE | COMPLETE | GO:0005179 | - | [leptin_melanocortin_signaling](../modules/leptin_melanocortin_signaling.html) (GO:0005179->GO:0005179) | ok |
| Constitutional_Megaloblastic_Anemia_With_Severe_Neurologic_Disease | DHFR | CAUSATIVE | COMPLETE | GO:0004146 | - | [thymidylate_synthesis](../modules/thymidylate_synthesis.html) (GO:0004146->GO:0004146) | ok |
| Cystinosis | CTNS | CAUSATIVE | COMPLETE | GO:0015184 GO:0015811&rarr;GO:0015184/GO:1904919 GO:0022857&rarr;GO:0015184/GO:0015295 GO:1904919 | GO:0080145 | - | PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| D-Bifunctional_Protein_Deficiency | HSD17B4 | CAUSATIVE | COMPLETE | GO:0033540 GO:0080023 GO:0106386 GO:0140493 | - | [peroxisomal_beta_oxidation](../modules/peroxisomal_beta_oxidation.html) (GO:0033540->GO:0006635, GO:0033540->GO:0033540, ...) - uncovered: GO:0106386 GO:0140493 | PARTIAL_COVERAGE |
| DPM2-congenital_disorder_of_glycosylation | DPM2 | CAUSATIVE | COMPLETE | GO:0008047 | GO:0004582 | [dolichol_phosphate_sugar_donor_supply](../modules/dolichol_phosphate_sugar_donor_supply.html) (GO:0008047->GO:0008047) | PARTIAL_ALIGNMENT |
| Developmental_And_Epileptic_Encephalopathy_116 | GLUL | CAUSATIVE | COMPLETE | GO:0004356 | - | [glutamate_glutamine_ammonia_hub](../modules/glutamate_glutamine_ammonia_hub.html) (GO:0004356->GO:0004356) | ok |
| Developmental_And_Epileptic_Encephalopathy_50 | CAD | CAUSATIVE | COMPLETE | GO:0004070 GO:0004088 GO:0004151 | - | [de_novo_pyrimidine_synthesis](../modules/de_novo_pyrimidine_synthesis.html) (GO:0004070->GO:0004070, GO:0004088->GO:0004088, ...) | ok |
| Dorfman_Chanarin_Disease | ABHD5 | CAUSATIVE | COMPLETE | GO:0010898 GO:0060229 | GO:0019433 | [triacylglycerol_lipolysis](../modules/triacylglycerol_lipolysis.html) (GO:0060229->GO:0060229) - uncovered: GO:0010898 | PARTIAL_ALIGNMENT, PARTIAL_COVERAGE |
| Dysostosis_Multiplex_Ain-Naz_Type | LYSET | CAUSATIVE | COMPLETE | GO:0050821 | - | [mannose_6_phosphate_lysosomal_targeting](../modules/mannose_6_phosphate_lysosomal_targeting.html) (GO:0050821->GO:0050821) | ok |
| EEFSEC_Deficiency | EEFSEC | CAUSATIVE | COMPLETE | GO:0001514 GO:0003746 GO:0006414&rarr;GO:0001514/GO:0003746 | - | [selenocysteine_biosynthesis_incorporation](../modules/selenocysteine_biosynthesis_incorporation.html) (GO:0001514->GO:0001514, GO:0003746->GO:0003746, ...) | ok |
| Encephalopathy_Due_To_Defective_Mitochondrial_And_Peroxisomal_Fission_2 | MFF | CAUSATIVE | COMPLETE | GO:0043495 | GO:0005096 | [mitochondrial_dynamics](../modules/mitochondrial_dynamics.html) (GO:0043495->GO:0043495) [peroxisome-lifecycle](../modules/peroxisome-lifecycle.html) (GO:0043495->GO:0043495) | PARTIAL_ALIGNMENT |
| FBXL4-Related_Mitochondrial_DNA_Depletion_Syndrome | FBXL4 | CAUSATIVE | COMPLETE | GO:1990756 | - | [mitophagy](../modules/mitophagy.html) (GO:1990756->GO:0030674, GO:1990756->GO:0060090, ...) | ok |
| Familial_Defective_Apolipoprotein_B-100 | APOB | CAUSATIVE | COMPLETE | GO:0050750 | - | [chylomicron_assembly_secretion](../modules/chylomicron_assembly_secretion.html) [ldl_receptor_mediated_endocytosis](../modules/ldl_receptor_mediated_endocytosis.html) (GO:0050750->GO:0050750) | ok |
| Familial_Defective_Apolipoprotein_B-100 | LDLR | MODIFIER | COMPLETE | - | - | [ldl_receptor_mediated_endocytosis](../modules/ldl_receptor_mediated_endocytosis.html) | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Familial_Defective_Apolipoprotein_B-100 | PCSK9 | MODIFIER | COMPLETE | - | - | [ldl_receptor_mediated_endocytosis](../modules/ldl_receptor_mediated_endocytosis.html) | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Fructose-1,6-Bisphosphatase_Deficiency | FBP1 | CAUSATIVE | COMPLETE | GO:0006094 GO:0042132 | - | [gluconeogenesis_human](../modules/gluconeogenesis_human.html) (GO:0006094->GO:0006094, GO:0042132->GO:0042132) [gluconeogenesis_human_substrates](../modules/gluconeogenesis_human_substrates.html) (GO:0006094->GO:0006094, GO:0042132->GO:0042132) | ok |
| GM1_Gangliosidosis_Type_1 | GLB1 | CAUSATIVE | COMPLETE | GO:0004565 GO:0006689 | - | [glycosphingolipid_lysosomal_degradation](../modules/glycosphingolipid_lysosomal_degradation.html) (GO:0004565->GO:0004565, GO:0006689->GO:0006689, ...) [keratan_chondroitin_sulfate_lysosomal_degradation](../modules/keratan_chondroitin_sulfate_lysosomal_degradation.html) (GO:0004565->GO:0004565) [lysosomal_glycoprotein_degradation](../modules/lysosomal_glycoprotein_degradation.html) (GO:0004565->GO:0004565) | ok |
| GM1_Gangliosidosis_Type_3 | GLB1 | CAUSATIVE | COMPLETE | GO:0004565 GO:0006689 | - | [glycosphingolipid_lysosomal_degradation](../modules/glycosphingolipid_lysosomal_degradation.html) (GO:0004565->GO:0004565, GO:0006689->GO:0006689, ...) [keratan_chondroitin_sulfate_lysosomal_degradation](../modules/keratan_chondroitin_sulfate_lysosomal_degradation.html) (GO:0004565->GO:0004565) [lysosomal_glycoprotein_degradation](../modules/lysosomal_glycoprotein_degradation.html) (GO:0004565->GO:0004565) | ok |
| GPD1_Deficiency | GPD1 | CAUSATIVE | COMPLETE | GO:0141152 | - | [gluconeogenesis_human_substrates](../modules/gluconeogenesis_human_substrates.html) (GO:0141152->GO:0141152) [glycerol_phosphate_shuttle](../modules/glycerol_phosphate_shuttle.html) (GO:0141152->GO:0141152) | ok |
| Glycogen_Storage_Disease_Type_I | G6PC1 | CAUSATIVE | COMPLETE | GO:0004346 <sup>s</sup> GO:0006094 <sup>s</sup> GO:0042593 <sup>s</sup> | GO:0005980 <sup>s</sup> GO:0015152 <sup>s</sup> | [gluconeogenesis_human](../modules/gluconeogenesis_human.html) (GO:0004346->GO:0004346, GO:0006094->GO:0006094) [gluconeogenesis_human_substrates](../modules/gluconeogenesis_human_substrates.html) (GO:0004346->GO:0004346, GO:0006094->GO:0006094) [glucose_6_phosphatase_system](../modules/glucose_6_phosphatase_system.html) (GO:0004346->GO:0004346, GO:0006094->GO:0006094) - uncovered: GO:0042593 | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, PARTIAL_COVERAGE |
| Glycogen_Storage_Disease_Type_I | SLC37A4 | CAUSATIVE | COMPLETE | GO:0015152&rarr;GO:0015760/GO:0061513 GO:0042593 | GO:0004346 <sup>s</sup> GO:0005980 <sup>s</sup> GO:0006094 <sup>s</sup> | [gluconeogenesis_human](../modules/gluconeogenesis_human.html) (GO:0015152->GO:0061513) [gluconeogenesis_human_substrates](../modules/gluconeogenesis_human_substrates.html) (GO:0015152->GO:0015152) [glucose_6_phosphatase_system](../modules/glucose_6_phosphatase_system.html) (GO:0015152->GO:0061513) - uncovered: GO:0042593 | PARTIAL_ALIGNMENT, PARTIAL_COVERAGE |
| Glycoprotein_Storage_Disease | FUCA1 | CAUSATIVE | COMPLETE | GO:0004560 <sup>s</sup> GO:0006516 <sup>s</sup> | GO:0003948 <sup>s</sup> | [lysosomal_glycoprotein_degradation](../modules/lysosomal_glycoprotein_degradation.html) (GO:0004560->GO:0004560, GO:0006516->GO:0006516) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Glycoprotein_Storage_Disease | AGA | CAUSATIVE | COMPLETE | GO:0003948 <sup>s</sup> GO:0006516 <sup>s</sup> | GO:0004560 <sup>s</sup> | [lysosomal_glycoprotein_degradation](../modules/lysosomal_glycoprotein_degradation.html) (GO:0003948->GO:0003948, GO:0006516->GO:0006516) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Greenberg_Dysplasia | LBR | CAUSATIVE | COMPLETE | GO:0006695 GO:0050613 | - | [cholesterol_synthesis_post_lanosterol](../modules/cholesterol_synthesis_post_lanosterol.html) (GO:0006695->GO:0006695, GO:0050613->GO:0050613) | ok |
| HAO1-Related_Glycolate_Oxidase_Deficiency | HAO1 | CAUSATIVE | COMPLETE | GO:0003973 GO:0046296 | GO:0046487 | [glyoxylate_oxalate_metabolism](../modules/glyoxylate_oxalate_metabolism.html) (GO:0003973->GO:0003973, GO:0046296->GO:0046296) | PARTIAL_ALIGNMENT |
| Heme_Oxygenase_1_Deficiency | HMOX1 | CAUSATIVE | COMPLETE | GO:0004392 GO:0042167 | GO:0034599 | [heme_degradation](../modules/heme_degradation.html) (GO:0004392->GO:0004392, GO:0042167->GO:0042167) | PARTIAL_ALIGNMENT |
| Hyperinsulinemic_Hypoglycemia | ABCC8 | CAUSATIVE | COMPLETE | GO:0015272&rarr;GO:0071805 <sup>s</sup> GO:0050796 <sup>s</sup> GO:0071805 <sup>s</sup> | GO:0030073 <sup>s</sup> | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0015272->GO:0015272, GO:0015272->GO:0071805, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Hyperinsulinemic_Hypoglycemia | KCNJ11 | CAUSATIVE | COMPLETE | GO:0015272&rarr;GO:0015272/GO:0071805 <sup>s</sup> GO:0050796&rarr;GO:0046676 <sup>s</sup> GO:0071805&rarr;GO:0015272/GO:0071805 <sup>s</sup> | GO:0030073 <sup>s</sup> | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0015272->GO:0015272, GO:0015272->GO:0071805, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Hyperinsulinemic_Hypoglycemia | GLUD1 | CAUSATIVE | COMPLETE | GO:0004353 <sup>s</sup> | GO:0004857 <sup>s</sup> GO:0050796 <sup>s</sup> | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0004353->GO:0004353) [glutamate_glutamine_ammonia_hub](../modules/glutamate_glutamine_ammonia_hub.html) (GO:0004353->GO:0004353) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Hyperinsulinemic_Hypoglycemia | GCK | CAUSATIVE | COMPLETE | GO:0004340 <sup>s</sup> GO:0050796&rarr;GO:0032024 <sup>s</sup> | - | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0004340->GO:0004340, GO:0050796->GO:0046676, ...) [glycolysis_investment_phase](../modules/glycolysis_investment_phase.html) (GO:0004340->GO:0004396) | ALIGNED_ON_SHARED_NODE_ONLY |
| Hyperinsulinemic_Hypoglycemia | HADH | CAUSATIVE | COMPLETE | GO:0004857 <sup>s</sup> GO:0050796&rarr;GO:0046676 <sup>s</sup> | GO:0004353 <sup>s</sup> | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) (GO:0004857->GO:0004857, GO:0050796->GO:0046676, ...) [fatty_acid_beta_oxidation](../modules/fatty_acid_beta_oxidation.html) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Hyperinsulinemic_Hypoglycemia | HNF4A | CAUSATIVE | COMPLETE | GO:0001228&rarr;GO:0001228/GO:0045944 <sup>s</sup> | GO:0050796 <sup>s</sup> | - | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Hyperinsulinemic_Hypoglycemia | HNF1A | CAUSATIVE | COMPLETE | GO:0001228&rarr;GO:0001228/GO:0045944 <sup>s</sup> | GO:0050796 <sup>s</sup> | - | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Hyperinsulinemic_Hypoglycemia | SLC16A1 | CAUSATIVE | COMPLETE | GO:0015650&rarr;GO:0015355 | GO:0050796 | - | PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| Hyperinsulinemic_Hypoglycemia | UCP2 | DISPUTED | COMPLETE | - | GO:0050796 | - | ALIGNED_NONCORE, NO_MODULE_MEMBERSHIP |
| Hyperinsulinemic_Hypoglycemia | HK1 | CAUSATIVE | COMPLETE | GO:0004340&rarr;GO:0004396 <sup>s</sup> | GO:0050796 <sup>s</sup> | [glycolysis_investment_phase](../modules/glycolysis_investment_phase.html) (GO:0004340->GO:0004396) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Hyperphosphatemic_Familial_Tumoral_Calcinosis | GALNT3 | CAUSATIVE | COMPLETE | GO:0004653 | - | [fgf23_klotho_phosphate_homeostasis](../modules/fgf23_klotho_phosphate_homeostasis.html) (GO:0004653->GO:0004653) | ok |
| Hyperphosphatemic_Familial_Tumoral_Calcinosis | FGF23 | CAUSATIVE | COMPLETE | GO:0005179 | - | [fgf23_klotho_phosphate_homeostasis](../modules/fgf23_klotho_phosphate_homeostasis.html) (GO:0005179->GO:0005179) [fgfr_signaling](../modules/fgfr_signaling.html) | ok |
| Hyperphosphatemic_Familial_Tumoral_Calcinosis | KL | CAUSATIVE | COMPLETE | GO:0015026 | - | [fgf23_klotho_phosphate_homeostasis](../modules/fgf23_klotho_phosphate_homeostasis.html) (GO:0015026->GO:0015026) [fgfr_signaling](../modules/fgfr_signaling.html) (GO:0015026->GO:0015026) | ok |
| Hyperprolinemia_Type_1 | PRODH | CAUSATIVE | COMPLETE | GO:0004657 GO:0006562 | - | [proline_metabolism](../modules/proline_metabolism.html) (GO:0004657->GO:0004657, GO:0006562->GO:0006562) | ok |
| Hyperprolinemia_Type_2 | ALDH4A1 | CAUSATIVE | COMPLETE | GO:0003842 GO:0006562 | - | [arginine_catabolism_arginase_pathway](../modules/arginine_catabolism_arginase_pathway.html) (GO:0003842->GO:0003842, GO:0006562->GO:0006562) [proline_metabolism](../modules/proline_metabolism.html) (GO:0003842->GO:0003842, GO:0006562->GO:0006562) | ok |
| Hypobetalipoproteinemia | APOB | CAUSATIVE | COMPLETE | GO:0034379 | - | [chylomicron_assembly_secretion](../modules/chylomicron_assembly_secretion.html) (not covering) [ldl_receptor_mediated_endocytosis](../modules/ldl_receptor_mediated_endocytosis.html) (not covering) | MODULE_NOT_COVERING |
| Hypobetalipoproteinemia | PNPLA3 | MODIFIER | COMPLETE | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| Hypobetalipoproteinemia | PCSK9 | CAUSATIVE | COMPLETE | GO:0050750 | - | [ldl_receptor_mediated_endocytosis](../modules/ldl_receptor_mediated_endocytosis.html) (GO:0050750->GO:0050750) | ok |
| Hypobetalipoproteinemia | ANGPTL3 | CAUSATIVE | COMPLETE | GO:0055102 | - | - | NO_MODULE_MEMBERSHIP |
| Inborn_Disorder_of_Bile_Acid_Synthesis | - | - | - | - | - | - | NO_GENE_RECORD: Grouping-like entry; genes are carried by its subtypes. |
| Infantile-Onset_Pompe_Disease | GAA | CAUSATIVE | COMPLETE | GO:0004558 | - | [lysosomal_glycogen_degradation](../modules/lysosomal_glycogen_degradation.html) (GO:0004558->GO:0004558) | ok |
| LDLR-Related_Familial_Hypercholesterolemia | LDLR | CAUSATIVE | COMPLETE | GO:0005041 | GO:0030169 | [ldl_receptor_mediated_endocytosis](../modules/ldl_receptor_mediated_endocytosis.html) (GO:0005041->GO:0005041) | PARTIAL_ALIGNMENT |
| LPIN1-Related_Recurrent_Myoglobinuria | LPIN1 | CAUSATIVE | COMPLETE | GO:0008195 | - | [triacylglycerol_biosynthesis](../modules/triacylglycerol_biosynthesis.html) (GO:0008195->GO:0008195) | ok |
| Late-Onset_Pompe_Disease | GAA | CAUSATIVE | COMPLETE | GO:0004558 | GO:0000398 | [lysosomal_glycogen_degradation](../modules/lysosomal_glycogen_degradation.html) (GO:0004558->GO:0004558) | PARTIAL_ALIGNMENT |
| Leber-like_Hereditary_Optic_Neuropathy_Autosomal_Recessive_1 | DNAJC30 | CAUSATIVE | COMPLETE | GO:0019899 GO:0034367 | - | - | NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TL1 | CAUSATIVE | COMPLETE | GO:0032543 | GO:0002098 GO:0006418 | - | PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-ND5 | CAUSATIVE | COMPLETE | GO:0008137&rarr;GO:0015078 <sup>s</sup> | - | [mitochondrial_complex_i_core](../modules/mitochondrial_complex_i_core.html) (GO:0008137->GO:0003954, GO:0008137->GO:0008137, ...) | ALIGNED_ON_SHARED_NODE_ONLY |
| MELAS_Syndrome | MT-ND1 | CAUSATIVE | COMPLETE | GO:0008137&rarr;GO:1902600 <sup>s</sup> | - | [mitochondrial_complex_i_core](../modules/mitochondrial_complex_i_core.html) (GO:0008137->GO:0003954, GO:0008137->GO:0008137, ...) | ALIGNED_ON_SHARED_NODE_ONLY |
| MELAS_Syndrome | MT-ND6 | CAUSATIVE | COMPLETE | GO:0008137&rarr;GO:0015078/GO:1902600 <sup>s</sup> | - | [mitochondrial_complex_i_core](../modules/mitochondrial_complex_i_core.html) (GO:0008137->GO:0003954, GO:0008137->GO:0008137, ...) | ALIGNED_ON_SHARED_NODE_ONLY |
| MELAS_Syndrome | MT-TQ | CAUSATIVE | COMPLETE | GO:0032543 <sup>s</sup> | - | - | ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TH | CAUSATIVE | COMPLETE | GO:0032543 <sup>s</sup> | - | - | ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TK | CAUSATIVE | COMPLETE | GO:0032543 <sup>s</sup> | - | - | ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TC | CAUSATIVE | COMPLETE | GO:0032543 <sup>s</sup> | - | - | ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TS1 | CAUSATIVE | COMPLETE | GO:0032543 <sup>s</sup> | - | - | ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TS2 | CAUSATIVE | COMPLETE | GO:0032543 <sup>s</sup> | - | - | ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TV | CAUSATIVE | COMPLETE | GO:0032543 <sup>s</sup> | - | - | ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TW | CAUSATIVE | COMPLETE | GO:0032543 <sup>s</sup> | - | - | ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| MELAS_Syndrome | MT-TM | CAUSATIVE | COMPLETE | GO:0032543 <sup>s</sup> | - | - | ALIGNED_ON_SHARED_NODE_ONLY, NO_MODULE_MEMBERSHIP |
| MEND_Syndrome | EBP | CAUSATIVE | COMPLETE | GO:0006695 GO:0047750 | - | [cholesterol_synthesis_post_lanosterol](../modules/cholesterol_synthesis_post_lanosterol.html) (GO:0006695->GO:0006695, GO:0047750->GO:0047750) | ok |
| MEND_Syndrome | APOA5 | MODIFIER | - | - | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| MEND_Syndrome | ABCA1 | MODIFIER | COMPLETE | - | - | - | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| MEND_Syndrome | APOB | MODIFIER | COMPLETE | - | - | [chylomicron_assembly_secretion](../modules/chylomicron_assembly_secretion.html) [ldl_receptor_mediated_endocytosis](../modules/ldl_receptor_mediated_endocytosis.html) | NO_ORIGIN, GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| MSMO1_Deficiency | MSMO1 | CAUSATIVE | COMPLETE | GO:0000254 GO:0006695 | - | [cholesterol_synthesis_post_lanosterol](../modules/cholesterol_synthesis_post_lanosterol.html) (GO:0000254->GO:0000254, GO:0006695->GO:0006695) | ok |
| MTHFD1_Deficiency | MTHFD1 | CAUSATIVE | COMPLETE | GO:0004329 GO:0004477 GO:0004488 | - | [folate_one_carbon_interconversion](../modules/folate_one_carbon_interconversion.html) (GO:0004477->GO:0004477, GO:0004488->GO:0004488) - uncovered: GO:0004329 | PARTIAL_COVERAGE |
| Methylmalonic_Acidemia_With_Homocystinuria_Type_cblJ | ABCD4 | CAUSATIVE | COMPLETE | GO:0015420&rarr;GO:0015420/GO:0015889 | - | [cobalamin_intracellular_processing](../modules/cobalamin_intracellular_processing.html) (GO:0015420->GO:0015420, GO:0015420->GO:0015889) | ok |
| Mevalonate_Kinase_Deficiency | MVK | CAUSATIVE | COMPLETE | GO:0004496 GO:0008299&rarr;GO:0019287 | GO:0006695 | [mevalonate_pathway](../modules/mevalonate_pathway.html) (GO:0004496->GO:0004496, GO:0008299->GO:0019287) | PARTIAL_ALIGNMENT |
| Mitchell_Syndrome | ACOX1 | CAUSATIVE | COMPLETE | GO:0003997 | - | [peroxisomal_beta_oxidation](../modules/peroxisomal_beta_oxidation.html) (GO:0003997->GO:0003997) | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_12 | NDUFA1 | CAUSATIVE | COMPLETE | GO:0008137 <sup>c</sup> | - | [complex_i_accessory_subunits](../modules/complex_i_accessory_subunits.html) (not covering) | ALIGNED_CONTRIBUTES_ONLY, MODULE_NOT_COVERING |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_19 | FOXRED1 | CAUSATIVE | COMPLETE | GO:0016491 GO:0032981 | - | [complex_i_assembly_factors](../modules/complex_i_assembly_factors.html) (GO:0016491->GO:0016491, GO:0032981->GO:0032981) | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_2 | NDUFS8 | CAUSATIVE | COMPLETE | GO:0051539 | - | [mitochondrial_complex_i_core](../modules/mitochondrial_complex_i_core.html) (GO:0051539->GO:0051539) | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_21 | NUBPL | CAUSATIVE | COMPLETE | GO:0016226 | - | [complex_i_assembly_factors](../modules/complex_i_assembly_factors.html) (not covering) | MODULE_NOT_COVERING |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_3 | NDUFS7 | CAUSATIVE | COMPLETE | GO:0051539 | - | [mitochondrial_complex_i_core](../modules/mitochondrial_complex_i_core.html) (GO:0051539->GO:0051539) | ok |
| Mitochondrial_Complex_I_Deficiency_Nuclear_Type_6 | NDUFS2 | CAUSATIVE | COMPLETE | GO:0008137 <sup>c</sup> GO:0048039 | GO:0051539 | [mitochondrial_complex_i_core](../modules/mitochondrial_complex_i_core.html) (GO:0008137->GO:0003954, GO:0008137->GO:0008137, ...) | PARTIAL_ALIGNMENT |
| Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_1 | ATPAF2 | CAUSATIVE | COMPLETE | GO:0033615 GO:0044183 | - | [mitochondrial_complex_v](../modules/mitochondrial_complex_v.html) (GO:0033615->GO:0033615, GO:0044183->GO:0044183) | ok |
| Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_2 | TMEM70 | CAUSATIVE | COMPLETE | GO:0030674 | GO:0033615 | [mitochondrial_complex_v](../modules/mitochondrial_complex_v.html) (GO:0030674->GO:0030674) | PARTIAL_ALIGNMENT |
| Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_3 | ATP5F1E | CAUSATIVE | COMPLETE | GO:0005198 | - | [mitochondrial_complex_v](../modules/mitochondrial_complex_v.html) (GO:0005198->GO:0005198) | ok |
| Mucolipidosis_Type_II | GNPTAB | CAUSATIVE | COMPLETE | GO:0003976 GO:0006622&rarr;GO:0016256 GO:0016256 | - | [mannose_6_phosphate_lysosomal_targeting](../modules/mannose_6_phosphate_lysosomal_targeting.html) (GO:0003976->GO:0003976, GO:0006622->GO:0007041, ...) | ok |
| Muscular_Dystrophy_Congenital_Hearing_Loss_And_Ovarian_Insufficiency_Syndrome | GGPS1 | CAUSATIVE | COMPLETE | GO:0004311 | - | [isoprenoid_diphosphate_biosynthesis](../modules/isoprenoid_diphosphate_biosynthesis.html) (GO:0004311->GO:0004311) | ok |
| Muscular_Dystrophy_Limb-girdle_Autosomal_Recessive_28 | HMGCR | CAUSATIVE | COMPLETE | GO:0004420 | - | [mevalonate_pathway](../modules/mevalonate_pathway.html) (GO:0004420->GO:0004420) | ok |
| NAGA_Deficiency_Type_3 | NAGA | CAUSATIVE | COMPLETE | GO:0006516 GO:0008456 | - | [lysosomal_glycoprotein_degradation](../modules/lysosomal_glycoprotein_degradation.html) (GO:0006516->GO:0006516, GO:0008456->GO:0008456) | ok |
| Neuropathy_Hereditary_Motor_And_Sensory_Type_VIc_With_Optic_Atrophy | PDXK | CAUSATIVE | COMPLETE | GO:0008478 | - | [vitamin_b6_plp_metabolism](../modules/vitamin_b6_plp_metabolism.html) (GO:0008478->GO:0008478) | ok |
| Neutral_Lipid_Storage_Myopathy | PNPLA2 | CAUSATIVE | COMPLETE | GO:0004806 GO:0019433 | - | [triacylglycerol_lipolysis](../modules/triacylglycerol_lipolysis.html) (GO:0004806->GO:0004806, GO:0019433->GO:0019433) | ok |
| Obesity_Due_to_MC4R_Pathway_Disruption | LEP | CAUSATIVE | COMPLETE | GO:0038021&rarr;GO:0033210 <sup>s</sup> | GO:0000981 <sup>s</sup> GO:0004252 <sup>s</sup> GO:0004980 <sup>s</sup> GO:0007189 <sup>s</sup> GO:0031782 <sup>s</sup> | [leptin_melanocortin_signaling](../modules/leptin_melanocortin_signaling.html) (GO:0038021->GO:0033210, GO:0038021->GO:0038021) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Obesity_Due_to_MC4R_Pathway_Disruption | LEPR | CAUSATIVE | COMPLETE | GO:0038021&rarr;GO:0033210/GO:0038021 <sup>s</sup> | GO:0000981 <sup>s</sup> GO:0004252 <sup>s</sup> GO:0004980 <sup>s</sup> GO:0007189 <sup>s</sup> GO:0031782 <sup>s</sup> | [leptin_melanocortin_signaling](../modules/leptin_melanocortin_signaling.html) (GO:0038021->GO:0033210, GO:0038021->GO:0038021) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Obesity_Due_to_MC4R_Pathway_Disruption | POMC | CAUSATIVE | COMPLETE | GO:0031782 <sup>s</sup> | GO:0000981 <sup>s</sup> GO:0004252 <sup>s</sup> GO:0004980 <sup>s</sup> GO:0007189 <sup>s</sup> GO:0038021 <sup>s</sup> | [leptin_melanocortin_signaling](../modules/leptin_melanocortin_signaling.html) (GO:0031782->GO:0031782) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Obesity_Due_to_MC4R_Pathway_Disruption | PCSK1 | CAUSATIVE | COMPLETE | GO:0004252 <sup>s</sup> | GO:0000981 <sup>s</sup> GO:0004980 <sup>s</sup> GO:0007189 <sup>s</sup> GO:0031782 <sup>s</sup> GO:0038021 <sup>s</sup> | [leptin_melanocortin_signaling](../modules/leptin_melanocortin_signaling.html) (GO:0004252->GO:0004252) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Obesity_Due_to_MC4R_Pathway_Disruption | MC4R | CAUSATIVE | COMPLETE | GO:0004980 <sup>s</sup> GO:0007189 <sup>s</sup> | GO:0000981 <sup>s</sup> GO:0004252 <sup>s</sup> GO:0031782 <sup>s</sup> GO:0038021 <sup>s</sup> | [leptin_melanocortin_signaling](../modules/leptin_melanocortin_signaling.html) (GO:0004980->GO:0004980) - uncovered: GO:0007189 | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, PARTIAL_COVERAGE |
| Obesity_Due_to_MC4R_Pathway_Disruption | SH2B1 | SUSCEPTIBILITY | - | - | - | - | NO_AIGR_REVIEW |
| Obesity_Due_to_MC4R_Pathway_Disruption | NCOA1 | SUSCEPTIBILITY | - | - | - | - | NO_AIGR_REVIEW |
| Obesity_Due_to_MC4R_Pathway_Disruption | SIM1 | CAUSATIVE | COMPLETE | GO:0000981&rarr;GO:0000981/GO:0006357 <sup>s</sup> | GO:0004252 <sup>s</sup> GO:0004980 <sup>s</sup> GO:0007189 <sup>s</sup> GO:0031782 <sup>s</sup> GO:0038021 <sup>s</sup> | - | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT, NO_MODULE_MEMBERSHIP |
| PET100-Related_COX_Deficiency | PET100 | CAUSATIVE | COMPLETE | GO:0033617 | - | [complex_iv_assembly_factors](../modules/complex_iv_assembly_factors.html) (GO:0033617->GO:0033617) | ok |
| PGM1-Congenital_Disorder_of_Glycosylation | PGM1 | CAUSATIVE | COMPLETE | GO:0004614 | GO:0045214 | [glycogenolysis](../modules/glycogenolysis.html) (GO:0004614->GO:0004614) | PARTIAL_ALIGNMENT |
| PNPO_Deficiency | PNPO | CAUSATIVE | COMPLETE | GO:0004733&rarr;GO:0004733/GO:0042823 | - | [vitamin_b6_plp_metabolism](../modules/vitamin_b6_plp_metabolism.html) (GO:0004733->GO:0004733, GO:0004733->GO:0042816, ...) | ok |
| Peroxisomal_Acyl-CoA_Oxidase_Deficiency | ACOX1 | CAUSATIVE | COMPLETE | GO:0003997 GO:0033540 GO:0140493 | - | [peroxisomal_beta_oxidation](../modules/peroxisomal_beta_oxidation.html) (GO:0003997->GO:0003997, GO:0033540->GO:0006635, ...) - uncovered: GO:0140493 | PARTIAL_COVERAGE |
| Peroxisome_Biogenesis_Disorder_5B | PEX2 | CAUSATIVE | COMPLETE | GO:0007031&rarr;GO:0016558/GO:0016562 | - | [peroxisome-lifecycle](../modules/peroxisome-lifecycle.html) (GO:0007031->GO:0007031, GO:0007031->GO:0016558, ...) | ok |
| Peroxisome_Biogenesis_Disorder_6A_Zellweger | PEX10 | CAUSATIVE | COMPLETE | GO:0061630 | - | [peroxisome-lifecycle](../modules/peroxisome-lifecycle.html) (GO:0061630->GO:0061630) | ok |
| Peroxisome_Biogenesis_Disorder_6B | PEX10 | CAUSATIVE | COMPLETE | GO:0061630 | - | [peroxisome-lifecycle](../modules/peroxisome-lifecycle.html) (GO:0061630->GO:0061630) | ok |
| Pompe_Disease | GAA | CAUSATIVE | COMPLETE | GO:0004558 GO:0005980 | GO:0007040 | [lysosomal_glycogen_degradation](../modules/lysosomal_glycogen_degradation.html) (GO:0004558->GO:0004558, GO:0005980->GO:0005980) | PARTIAL_ALIGNMENT |
| Primary_Coenzyme_Q10_Deficiency | COQ2 | CAUSATIVE | COMPLETE | GO:0006744 <sup>s</sup> GO:0008412 <sup>s</sup> | GO:0097269 <sup>s</sup> | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Primary_Coenzyme_Q10_Deficiency | COQ4 | CAUSATIVE | COMPLETE | GO:0006744&rarr;GO:0006744/GO:0120539 <sup>s</sup> GO:0008425&rarr;GO:0006744 <sup>s</sup> GO:0120539&rarr;GO:0006744/GO:0120539 <sup>s</sup> | GO:0106364 <sup>s</sup> GO:0160224 <sup>s</sup> | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Primary_Coenzyme_Q10_Deficiency | COQ5 | CAUSATIVE | COMPLETE | GO:0006744&rarr;GO:0006744/GO:0008425 <sup>s</sup> GO:0008425&rarr;GO:0006744/GO:0008425 <sup>s</sup> GO:0120539&rarr;GO:0006744 <sup>s</sup> | GO:0106364 <sup>s</sup> GO:0160224 <sup>s</sup> | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Primary_Coenzyme_Q10_Deficiency | COQ6 | CAUSATIVE | COMPLETE | GO:0006744&rarr;GO:0006744/GO:0120538 <sup>s</sup> GO:0008425&rarr;GO:0006744 <sup>s</sup> GO:0106364 <sup>s</sup> GO:0120539&rarr;GO:0006744 <sup>s</sup> | GO:0160224 <sup>s</sup> | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Primary_Coenzyme_Q10_Deficiency | COQ8A | CAUSATIVE | COMPLETE | GO:0006744 <sup>s</sup> GO:0016887 <sup>s</sup> | - | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY |
| Primary_Coenzyme_Q10_Deficiency | COQ8B | CAUSATIVE | COMPLETE | GO:0006744 <sup>s</sup> GO:0016887 <sup>s</sup> | - | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY |
| Primary_Coenzyme_Q10_Deficiency | COQ7 | CAUSATIVE | COMPLETE | GO:0006744 <sup>s</sup> GO:0008425&rarr;GO:0006744 <sup>s</sup> GO:0120539&rarr;GO:0006744 <sup>s</sup> GO:0160224 <sup>s</sup> | GO:0106364 <sup>s</sup> | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Primary_Coenzyme_Q10_Deficiency | COQ9 | CAUSATIVE | COMPLETE | GO:0006744 <sup>s</sup> GO:0008425&rarr;GO:0006744 <sup>s</sup> GO:0120539&rarr;GO:0006744 <sup>s</sup> | GO:0106364 <sup>s</sup> GO:0160224 <sup>s</sup> | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Primary_Coenzyme_Q10_Deficiency | PDSS1 | CAUSATIVE | COMPLETE | GO:0006744 <sup>s</sup> GO:0097269 <sup>cs</sup> | GO:0008412 <sup>s</sup> | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Primary_Coenzyme_Q10_Deficiency | PDSS2 | CAUSATIVE | COMPLETE | GO:0006744 <sup>s</sup> GO:0097269 <sup>cs</sup> | GO:0008412 <sup>s</sup> | [coenzyme_q10_biosynthesis](../modules/coenzyme_q10_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) [ubiquinone_biosynthesis](../modules/ubiquinone_biosynthesis.html) (GO:0006744->GO:0006744, GO:0006744->GO:0008425, ...) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Primary_Hyperoxaluria_Type_1 | AGXT | CAUSATIVE | COMPLETE | GO:0008453 GO:0009436 | - | [glycine_serine_interconversion](../modules/glycine_serine_interconversion.html) (GO:0008453->GO:0008453) [glyoxylate_oxalate_metabolism](../modules/glyoxylate_oxalate_metabolism.html) (GO:0008453->GO:0008453, GO:0009436->GO:0046487) | ok |
| Primary_Hyperoxaluria_Type_2 | GRHPR | CAUSATIVE | COMPLETE | GO:0016618 GO:0030267 GO:0046487 | - | [glyoxylate_oxalate_metabolism](../modules/glyoxylate_oxalate_metabolism.html) (GO:0030267->GO:0030267, GO:0046487->GO:0046487) - uncovered: GO:0016618 | PARTIAL_COVERAGE |
| Primary_Hyperoxaluria_Type_3 | HOGA1 | CAUSATIVE | COMPLETE | GO:0008700 GO:0019470 | GO:0046487 | [glyoxylate_oxalate_metabolism](../modules/glyoxylate_oxalate_metabolism.html) (GO:0008700->GO:0008700) - uncovered: GO:0019470 | PARTIAL_ALIGNMENT, PARTIAL_COVERAGE |
| Primary_Hyperoxaluria_Type_3 | AGXT | MODIFIER | COMPLETE | - | - | [glycine_serine_interconversion](../modules/glycine_serine_interconversion.html) [glyoxylate_oxalate_metabolism](../modules/glyoxylate_oxalate_metabolism.html) | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES |
| Purine_Nucleoside_Phosphorylase_Deficiency | PNP | CAUSATIVE | COMPLETE | GO:0004731 GO:0006152&rarr;GO:0006148/GO:0006161 | - | [purine_nucleotide_catabolism](../modules/purine_nucleotide_catabolism.html) (GO:0004731->GO:0004731, GO:0006152->GO:0072523) [purine_salvage_and_catabolism](../modules/purine_salvage_and_catabolism.html) (GO:0004731->GO:0004731) | ok |
| Pyridoxine-Dependent_Epilepsy | ALDH7A1 | CAUSATIVE | COMPLETE | GO:0004029 GO:0004043 GO:0019477 | - | [lysine_catabolism_saccharopine](../modules/lysine_catabolism_saccharopine.html) (GO:0004043->GO:0004043, GO:0019477->GO:0019477) - uncovered: GO:0004029 | PARTIAL_COVERAGE |
| Pyruvate_Carboxylase_Deficiency_Disease | PC | CAUSATIVE | COMPLETE | GO:0004736 GO:0006094 | GO:0006090 GO:0006099 | [gluconeogenesis_human](../modules/gluconeogenesis_human.html) (GO:0004736->GO:0004736, GO:0006094->GO:0006094) [gluconeogenesis_human_substrates](../modules/gluconeogenesis_human_substrates.html) (GO:0004736->GO:0004736, GO:0006094->GO:0006094) [pyruvate_metabolism](../modules/pyruvate_metabolism.html) (GO:0004736->GO:0004736) | PARTIAL_ALIGNMENT |
| RFT1-congenital_disorder_of_glycosylation | RFT1 | CAUSATIVE | COMPLETE | GO:0140303 | - | [n_glycan_llo_assembly_lumenal](../modules/n_glycan_llo_assembly_lumenal.html) (GO:0140303->GO:0140303) | ok |
| Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect | GNPAT | CAUSATIVE | COMPLETE | GO:0008611 <sup>s</sup> GO:0016287 <sup>s</sup> | GO:0008609 <sup>s</sup> GO:0102965 <sup>s</sup> | [ether_lipid_plasmalogen_biosynthesis](../modules/ether_lipid_plasmalogen_biosynthesis.html) (GO:0008611->GO:0008611, GO:0016287->GO:0016287) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect | AGPS | CAUSATIVE | COMPLETE | GO:0008609 <sup>s</sup> GO:0008611 <sup>s</sup> | GO:0016287 <sup>s</sup> GO:0102965 <sup>s</sup> | [ether_lipid_plasmalogen_biosynthesis](../modules/ether_lipid_plasmalogen_biosynthesis.html) (GO:0008609->GO:0008609, GO:0008611->GO:0008611) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect | FAR1 | CAUSATIVE | COMPLETE | GO:0008611 <sup>s</sup> GO:0102965 <sup>s</sup> | GO:0008609 <sup>s</sup> GO:0016287 <sup>s</sup> | [ether_lipid_plasmalogen_biosynthesis](../modules/ether_lipid_plasmalogen_biosynthesis.html) (GO:0008611->GO:0008611, GO:0102965->GO:0102965) | ALIGNED_ON_SHARED_NODE_ONLY, PARTIAL_ALIGNMENT |
| Rhizomelic_Chondrodysplasia_Punctata_Type_1 | PEX7 | CAUSATIVE | COMPLETE | GO:0000268 GO:0016558 | GO:0006625 | [peroxisome-lifecycle](../modules/peroxisome-lifecycle.html) (GO:0000268->GO:0000268, GO:0016558->GO:0007031, ...) | PARTIAL_ALIGNMENT |
| Rhizomelic_Chondrodysplasia_Punctata_Type_5 | PEX5 | CAUSATIVE | COMPLETE | GO:0016558&rarr;GO:0016558/GO:0016560/GO:0016562 GO:0140597 | - | [peroxisome-lifecycle](../modules/peroxisome-lifecycle.html) (GO:0016558->GO:0007031, GO:0016558->GO:0016558, ...) - uncovered: GO:0140597 | PARTIAL_COVERAGE |
| SCO1-Related_COX_Deficiency | SCO1 | CAUSATIVE | COMPLETE | GO:0016531 GO:0033617 | GO:0006825 | [complex_iv_assembly_factors](../modules/complex_iv_assembly_factors.html) (GO:0016531->GO:0016531, GO:0033617->GO:0033617) | PARTIAL_ALIGNMENT |
| SECISBP2_Deficiency | SECISBP2 | CAUSATIVE | COMPLETE | GO:0001514 GO:0035368 | - | [selenocysteine_biosynthesis_incorporation](../modules/selenocysteine_biosynthesis_incorporation.html) (GO:0001514->GO:0001514, GO:0035368->GO:0035368) | ok |
| SEPSECS_Deficiency | SEPSECS | CAUSATIVE | COMPLETE | GO:0001717 GO:0016260 GO:0098621 | - | [selenocysteine_biosynthesis_incorporation](../modules/selenocysteine_biosynthesis_incorporation.html) (GO:0001717->GO:0001717, GO:0016260->GO:0016260, ...) | ok |
| SLC26A1-Related_Hypersulfaturia | SLC26A1 | CAUSATIVE | COMPLETE | GO:0015383&rarr;GO:0015383/GO:1902358 GO:1902358&rarr;GO:0015383/GO:1902358 | - | - | NO_MODULE_MEMBERSHIP |
| SLC26A1-Related_Oxalate_Transporter_Deficiency | SLC26A1 | CAUSATIVE | COMPLETE | GO:0015116&rarr;GO:0015383/GO:1902358 GO:0019531&rarr;GO:0019531/GO:0019532 GO:0019532&rarr;GO:0019531/GO:0019532 GO:1902358&rarr;GO:0015383/GO:1902358 | - | - | NO_MODULE_MEMBERSHIP |
| SLC26A6-Related_Hyperoxaluria_and_Nephrolithiasis | SLC26A6 | CAUSATIVE | COMPLETE | GO:0019531 GO:0019532&rarr;GO:0019531/GO:0046724 | - | - | NO_MODULE_MEMBERSHIP |
| SLC35A1-Congenital_Disorder_of_Glycosylation | SLC35A1 | CAUSATIVE | COMPLETE | GO:0005456&rarr;GO:0005456/GO:0015782 | - | [sialic_acid_metabolism](../modules/sialic_acid_metabolism.html) (GO:0005456->GO:0005456) | ok |
| STT3A-Congenital_Disorder_of_Glycosylation | STT3A | CAUSATIVE | COMPLETE | GO:0004579 | - | [oligosaccharyltransferase_complex](../modules/oligosaccharyltransferase_complex.html) (GO:0004579->GO:0004579) | ok |
| SUCLA2-Related_Mitochondrial_DNA_Depletion_Syndrome | SUCLA2 | CAUSATIVE | COMPLETE | GO:0004775 | - | [tca_cycle](../modules/tca_cycle.html) (GO:0004775->GO:0004775) | ok |
| Severe_X-linked_Mitochondrial_Encephalomyopathy | AIFM1 | CAUSATIVE | COMPLETE | GO:0043495 | GO:0050660 | [apoptotic_execution_phase](../modules/apoptotic_execution_phase.html) (not covering) | PARTIAL_ALIGNMENT, MODULE_NOT_COVERING |
| Short_Stature_Amelogenesis_Imperfecta_And_Skeletal_Dysplasia_With_Scoliosis | SLC10A7 | CAUSATIVE | COMPLETE | GO:0032468&rarr;GO:0006874 GO:0051480&rarr;GO:0006874 | - | - | NO_MODULE_MEMBERSHIP |
| Sitosterolemia | ABCG5 | CAUSATIVE | COMPLETE | GO:0015918&rarr;GO:0033344 <sup>s</sup> GO:0034041 <sup>cs</sup> | - | [intestinal_sterol_absorption_and_efflux](../modules/intestinal_sterol_absorption_and_efflux.html) (GO:0015918->GO:0030301, GO:0034041->GO:0034041) | ALIGNED_ON_SHARED_NODE_ONLY |
| Sitosterolemia | ABCG8 | CAUSATIVE | COMPLETE | GO:0015918 <sup>s</sup> GO:0034041 <sup>cs</sup> | - | [intestinal_sterol_absorption_and_efflux](../modules/intestinal_sterol_absorption_and_efflux.html) (GO:0015918->GO:0030301, GO:0034041->GO:0034041) | ALIGNED_ON_SHARED_NODE_ONLY |
| Snyder-Robinson_Syndrome | SMS | CAUSATIVE | COMPLETE | GO:0006597 GO:0016768 | - | [polyamine_metabolism](../modules/polyamine_metabolism.html) (GO:0006597->GO:0006596, GO:0016768->GO:0016768) | ok |
| Spastic_Paraparesis-cataracts-speech_Delay_Syndrome | FAR1 | CAUSATIVE | COMPLETE | GO:0102965 | - | [ether_lipid_plasmalogen_biosynthesis](../modules/ether_lipid_plasmalogen_biosynthesis.html) (GO:0102965->GO:0102965) | ok |
| Sphingosine_Phosphate_Lyase_Insufficiency_Syndrome | SGPL1 | CAUSATIVE | COMPLETE | GO:0008117 | - | [sphingosine_1_phosphate_rheostat](../modules/sphingosine_1_phosphate_rheostat.html) (GO:0008117->GO:0008117) | ok |
| Sterol_Carrier_Protein_2_Deficiency | SCP2 | CAUSATIVE | COMPLETE | GO:0050632 | - | [peroxisomal_beta_oxidation](../modules/peroxisomal_beta_oxidation.html) (GO:0050632->GO:0050632) | ok |
| Triglyceride_Storage_Disease_Type_1 | - | - | - | - | - | - | NO_GENE_RECORD: Historical OMIM:190420 phenotype; no gene has been reported (ABHD5 content lives in Dorfman_Chanarin_Disease). |
| Type_I_Diabetes | INS | SUSCEPTIBILITY | COMPLETE | - | - | [beta_cell_glucose_stimulated_insulin_secretion](../modules/beta_cell_glucose_stimulated_insulin_secretion.html) | NO_GO_ON_GENE_NODES |
| Type_I_Diabetes | PTPN22 | SUSCEPTIBILITY | IN_PROGRESS | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | IL2RA | SUSCEPTIBILITY | DRAFT | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | CTLA4 | SUSCEPTIBILITY | DRAFT | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | TYK2 | SUSCEPTIBILITY | - | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_AIGR_REVIEW |
| Type_I_Diabetes | IFIH1 | SUSCEPTIBILITY | COMPLETE | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | BACH2 | SUSCEPTIBILITY | DRAFT | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | TNFAIP3 | SUSCEPTIBILITY | DRAFT | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | EGR2 | SUSCEPTIBILITY | IN_PROGRESS | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | IRF4 | SUSCEPTIBILITY | DRAFT | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Type_I_Diabetes | IKZF1 | SUSCEPTIBILITY | IN_PROGRESS | - | - | - | GENE_ON_NO_NODE, NO_GO_ON_GENE_NODES, AIGR_NOT_COMPLETE, NO_MODULE_MEMBERSHIP |
| Vitamin_D-Dependent_Rickets_Type_1A | CYP27B1 | CAUSATIVE | COMPLETE | GO:0004498&rarr;GO:0004498/GO:1901755 | - | [fgf23_klotho_phosphate_homeostasis](../modules/fgf23_klotho_phosphate_homeostasis.html) (GO:0004498->GO:0004498, GO:0004498->GO:1901755) [vitamin_d_activation_signaling](../modules/vitamin_d_activation_signaling.html) (GO:0004498->GO:0004498, GO:0004498->GO:1901755) | ok |
| Vitamin_D-Dependent_Rickets_Type_2B | - | - | - | - | - | - | NO_GENE_RECORD: Genetic basis unknown; HNRNPC is modelled as a mechanism actor, not a causal gene. |
| Wilsons_Disease | ATP7B | CAUSATIVE | COMPLETE | GO:0006825&rarr;GO:0015677/GO:0060003/GO:0140581 GO:0035434&rarr;GO:0060003/GO:0140581 GO:0055070&rarr;GO:0006878 GO:0140581 | GO:0004322 | [cuproptosis](../modules/cuproptosis.html) (GO:0006825->GO:0005375, GO:0006825->GO:0098705, ...) - uncovered: GO:0055070 | PARTIAL_ALIGNMENT, PARTIAL_COVERAGE |
| Wolman_Disease | LIPA | CAUSATIVE | COMPLETE | GO:0004771 GO:0004806 GO:0019433 GO:0046461&rarr;GO:0019433 | - | [ldl_receptor_mediated_endocytosis](../modules/ldl_receptor_mediated_endocytosis.html) (GO:0004771->GO:0004771) - uncovered: GO:0004806 GO:0019433 GO:0046461 | PARTIAL_COVERAGE |
| X-linked_Chondrodysplasia_Punctata_2 | EBP | CAUSATIVE | COMPLETE | GO:0006695 GO:0047750 | - | [cholesterol_synthesis_post_lanosterol](../modules/cholesterol_synthesis_post_lanosterol.html) (GO:0006695->GO:0006695, GO:0047750->GO:0047750) | ok |

## Notes on remaining flags

- **No causative row carries `NO_GO_ALIGNMENT`**, which is the flag that would mark a real
  contradiction: every causative gene has at least one node term matching a core function.
  The flags causative rows do carry say something weaker. The three module flags
  (`NO_MODULE_MEMBERSHIP`, `MODULE_NOT_COVERING`, `PARTIAL_COVERAGE`) are about what is
  modelled elsewhere in ai-gene-review, not about this gene's function.
  `PARTIAL_ALIGNMENT` marks non-overlap rather than conflict - dismech modelling a step the
  gene's normal function does not include - and `ALIGNED_CONTRIBUTES_ONLY` and
  `ALIGNED_ON_SHARED_NODE_ONLY` mark a match that rests on a weaker relation than the row
  looks. `ALIGNED_NONCORE` falls only on UCP2, a DISPUTED gene that was never required to
  align, as do the `NO_AIGR_REVIEW` and `AIGR_NOT_COMPLETE` rows.
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

## Genes with a module flag, and why

`NO_MODULE_MEMBERSHIP` means no module contains the gene; `MODULE_NOT_COVERING` means
one does but nothing in it is about the function the row aligned on. Rows that are not
causative are marked, since they were never required to align. `PARTIAL_COVERAGE` is
the third module flag and is deliberately absent from this list: it reports which of a
row's aligned terms a module reached and which it did not, so the covering pairs and the
`- uncovered:` list in the Modules column already say everything a hand-written reason
could, and the generator
does not require one. The distinction is obligation, not importance.

- **TRMT10C** (`NO_MODULE_MEMBERSHIP`): RNase P partners (HSD17B10, PRORP, ELAC2) lack completed reviews.
- **ANGPTL3** (`NO_MODULE_MEMBERSHIP`): No LPL / plasma triglyceride clearance module; LPL review still DRAFT.
- **CTNS** (`NO_MODULE_MEMBERSHIP`): Lysosomal cystine export is a single step.
- **SLC26A1 (SLC26A1-Related_Hypersulfaturia, SLC26A1-Related_Oxalate_Transporter_Deficiency)** (`NO_MODULE_MEMBERSHIP`): Epithelial oxalate/sulfate transport has no coherent multi-part module yet; SLC26A1's oxalate role is contested.
- **SLC26A6** (`NO_MODULE_MEMBERSHIP`): As SLC26A1; a two-part oxalate-transport module is possible later.
- **DMP1** (`NO_MODULE_MEMBERSHIP`): No module contains DMP1 as a part. It is named in the notes of fgf23_klotho_phosphate_homeostasis as regulatory context, which this audit deliberately does not count as membership, and its mechanism is undefined.
- **SLC10A7** (`NO_MODULE_MEMBERSHIP`): Single gene with unknown transported substrate.
- **DNAJC30** (`NO_MODULE_MEMBERSHIP`): Complex I N-module repair is not assembly; no repair module exists.
- **LCT** (`NO_MODULE_MEMBERSHIP`): Brush-border disaccharide digestion: only LCT has a completed review (SI, MGAM, TREH missing).
- **HNF1A / HNF4A (Congenital_Isolated_Hyperinsulinism, Hyperinsulinemic_Hypoglycemia)** (`NO_MODULE_MEMBERSHIP`): Transcription factors whose hyperinsulinism and MODY roles act through many target genes; no beta-cell transcriptional-network module exists yet.
- **SLC16A1 (Congenital_Isolated_Hyperinsulinism, Hyperinsulinemic_Hypoglycemia)** (`NO_MODULE_MEMBERSHIP`): Disease mechanism is ectopic beta-cell expression of a transporter whose normal role (lactate/pyruvate transport) belongs to no beta-cell pathway; a monocarboxylate-transport module would not include the disease mechanism.
- **SIM1** (`NO_MODULE_MEMBERSHIP`): Transcription factor needed for paraventricular hypothalamic neuron development and function; it acts on, rather than within, the leptin_melanocortin_signaling module, whose parts are the ligand, processing and receptor steps.
- **MT-TL1 / MT-TQ / MT-TH / MT-TK / MT-TC / MT-TS1 / MT-TS2 / MT-TV / MT-TW / MT-TM** (`NO_MODULE_MEMBERSHIP`): No mitochondrial translation module exists; in mitochondrial_trna_charging_and_initiator_formylation a tRNA would appear only as a synthetase substrate, which the substrate guidance excludes, and module parts are UniProt proteins.
- **UCP2** (`NO_MODULE_MEMBERSHIP`, not causative): Causal role disputed (relationship DISPUTED); its transported substrate is itself contested.
- **AIFM1** (`MODULE_NOT_COVERING`): The aligned function is the mitochondrial disulfide relay (CHCHD4 anchoring); no module covers the relay. AIFM1 is a part of apoptotic_execution_phase, whose AIFM1 annoton carries DNA binding, nucleus and positive regulation of apoptotic process: a different AIFM1 activity, and not the encephalomyopathy mechanism.
- **APOB (Hypobetalipoproteinemia)** (`MODULE_NOT_COVERING`): The aligned term is GO:0034379 very-low-density lipoprotein particle assembly, and there is no VLDL-assembly module. APOB is a part of chylomicron_assembly_secretion, whose scope is GO:0034378 chylomicron assembly, and of ldl_receptor_mediated_endocytosis, which is about the receptor taking the particle up. GO:0034378 and GO:0034379 are siblings, not one inside the other, so the hepatic VLDL step is genuinely unmodelled. APOB's other row, the LDL-receptor-binding one, is covered.
- **NUBPL** (`MODULE_NOT_COVERING`): The aligned term is GO:0016226 iron-sulfur cluster assembly. NUBPL is a part of complex_i_assembly_factors, whose scope is GO:0032981 mitochondrial respiratory chain complex I assembly: NUBPL delivers an Fe-S cluster to the assembling complex, and the cluster's own assembly is a different process that no module covers.
- **NDUFA1** (`MODULE_NOT_COVERING`): A limitation of the coverage test rather than a modelling gap, and left flagged rather than waived. The module is the right one; the cause is an asymmetry in how the two sides may say the same thing. The dismech node binds GO:0008137 NADH dehydrogenase (ubiquinone) activity, which the review carries as contributes_to_molecular_function, so the row aligns. complex_i_accessory_subunits says the identical relation the GO-idiomatic way, giving its NDUFA1 annoton GO:0005198 structural molecule activity as part of complex I, and GO:0005198 does not relate to GO:0008137 by is_a/part_of ancestry: a structural role and the activity it supports are different branches of molecular function. Coverage accepts a contributes-to term from the review but has no way to read the module's structural-plus-part_of idiom as the same claim. (The module also declares GO:0006120 as its process scope, which ancestry does not reach from GO:0008137 either - but that is a fact about this particular pair, not about the aspects: is_a/part_of does cross between molecular function and biological process, and MT-ND1 in this same table aligns GO:0008137 to GO:1902600 by doing so. Either way the aspect question is not what decides this row.)
