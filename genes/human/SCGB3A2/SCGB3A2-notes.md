# SCGB3A2 (Q96PL1) curation notes

## Identity
- Secretoglobin family 3A member 2; synonyms UGRP1 (uteroglobin-related protein 1), PnSP-1 (pneumo secretory protein 1), HIN-2.
- 93 aa precursor; signal peptide 1-21; mature chain 22-93 [file:human/SCGB3A2/SCGB3A2-uniprot.txt "SIGNAL 1..21" / "CHAIN 22..93"].
- Secreted; disulfide-linked homodimer (interchain Cys70) and monomer forms [file:human/SCGB3A2/SCGB3A2-uniprot.txt "Homodimer; disulfide-linked (PubMed:24213919). Monomer"].
- Belongs to the secretoglobin family, UGRP subfamily [file:human/SCGB3A2/SCGB3A2-uniprot.txt "Belongs to the secretoglobin family. UGRP subfamily."].

## Expression / localization
- Highly lung/trachea-enriched; airway epithelium, submucosal gland serous cells, club cells of bronchioles; fetal lung [PMID:12406855; PMID:12175512; file:human/SCGB3A2/SCGB3A2-uniprot.txt "Highly expressed in lung and trachea"]. HPA: "Tissue enriched (lung)".
- Subcellular location: Secreted [file:human/SCGB3A2/SCGB3A2-uniprot.txt "SUBCELLULAR LOCATION: Secreted"].

## Molecular function / mechanism
- Secreted cytokine-like protein that binds the macrophage scavenger receptor MARCO; a lung-specific ligand-receptor pair; also copurifies with APOA1 and binds pathogens (L. monocytogenes, P. aeruginosa, yeast); LPS competes for MARCO binding [PMID:12847263 "we identified macrophage scavenger receptor with collagenous structure (MARCO) as a receptor for UGRP1", "secreted recombinant UGRP1 was copurified with apolipoprotein A-I", "UGRP1 also bound to bacteria and yeast. LPS, a previously identified MARCO ligand, competed with UGRP1 for binding to MARCO"]. Interpretation: proposed role in inflammation and pathogen clearance in the lung.
- Phospholipase A2 inhibitory activity: recombinant human SCGB3A2 "exhibited novel phospholipase A2 inhibitory activity" (direct biochemical assay) [PMID:24213919 "Human SCGB3A2, as well as mouse SCGB3A2, readily formed a dimer in solution and exhibited novel phospholipase A2 inhibitory activity"]. This parallels the well-established PLA2-inhibitor activity of the paralog SCGB1A1 and is the clearest biochemical MF for SCGB3A2. Supports GO:0019834 phospholipase A2 inhibitor activity (NEW).
- Growth-factor and anti-fibrotic activity in mouse models: promotes embryonic lung branching/development ex vivo and in vivo; antifibrotic in bleomycin lung fibrosis; crosses placenta [PMID:24213919 "human SCGB3A2 exhibited growth factor activity by promoting embryonic lung development in both ex vivo and in vivo systems and antifibrotic activity in the bleomycin-induced lung fibrosis model"]. These are in vivo mouse phenotypes of the human recombinant protein; treated as supporting context, not asserted as new GO BP annotations (participation vs necessity).
- UniProt also notes anti-inflammatory effect in respiratory epithelium (By similarity) and possible inhibition of FSH/LH in pituitary (By similarity) — not experimentally shown for human protein; not annotated.

## Disease association
- Asthma/atopy association: cloned as PnSP-1 "with potential association to atopy"; promoter polymorphisms of SCGB3A2/UGRP1 have been reported in asthma association studies (family/literature context). The gene was isolated in the respiratory/atopy context [file:human/SCGB3A2/SCGB3A2-uniprot.txt "a protein of the respiratory tract with potential association to atopy"]. Note: the strongest functional data (anti-inflammatory/antifibrotic/PLA2 inhibition) are consistent with a protective airway role, but the human asthma genetic association per se is epidemiological and not a GO-annotatable molecular function.
- One somatic K33N variant reported in a breast cancer sample (large-scale) [file:human/SCGB3A2/SCGB3A2-uniprot.txt "K -> N (in a breast cancer sample; somatic mutation)"] — incidental, not a driver claim.

## Annotation decisions (summary)
- GO:0005576 extracellular region (EXP/IBA/IEA/TAS): ACCEPT — core; secreted protein verified experimentally (PMID:12847263) and family-wide.
- GO:0071682 endocytic vesicle lumen (TAS Reactome, "MARCO:ligand is endocytosed"): KEEP_AS_NON_CORE — a valid but peripheral localization of the ligand after MARCO-mediated endocytosis by alveolar macrophages; reflects clearance, not the core secreted function.
- NEW GO:0019834 phospholipase A2 inhibitor activity — IDA from PMID:24213919 (human recombinant protein, biochemical assay).
