# IBSP manual literature synthesis

## Scope

This synthesis was prepared because Falcon returned HTTP 402 and Perplexity-lite returned HTTP 401. The evidence base includes the reviewed UniProt P21815 record, GOA and QuickGO metadata, the cached Reactome event, cached primary publications, and manual searches of PubMed and open-access primary articles.

## Molecular functions

Bone sialoprotein is a secreted, phosphorylated, sulfated, and heavily glycosylated SIBLING protein. Its acidic regions bind the bone mineral hydroxyapatite, while its C-terminal RGD motif binds integrins. Human material directly demonstrates both activities: [PMID:11459848 "The affinity for hydroxyapatite was higher for bone-derived BSP than for recombinant BSP"] and [PMID:24103036 "replacement of the RGD (arg-gly-asp) peptide moiety with peptide KAE (lys-ala-glu) resulted in a dramatic loss of cell-attachment activity"].

The broad GO small molecule binding term refers to ChEBI:52254, hydroxyapatite, and should therefore be made specific as GO:0046848 hydroxyapatite binding. Generic structural molecule activity is not what the cited peptide study assays; integrin binding is the supported specific activity.

## Mineralized extracellular matrix

Human developmental studies localize BSP protein and transcript to differentiated bone-forming cells and the bone matrix [PMID:1818768 "These findings show that BSP is primarily an osteoblast-derived component of the bone matrix expressed at late stages of differentiation"]. Mouse knockout provides causal conserved evidence: [PMID:24816232 "In BSP-/- newborns, µCT analysis revealed a delay in membranous primary ossification"]. The combination supports extracellular-matrix organization, bone mineralization, and a noncollagenous bone-matrix localization.

## Integrin-dependent cell behavior

BSP is an alpha-V/beta-3 ligand that supports cell attachment and migration. Direct assays found [PMID:10640428 "Stimulation of lymphoblastoid, osteoblastoid, and human umbilical vein endothelial cells (HUVEC) with PMA or Mn(2+) markedly enhanced alpha(V)beta(3)-dependent adhesion to BSP"]. The RGD peptide experiment independently supports integrin binding and positive regulation of cell adhesion. A later glioblastoma study establishes a disease-context migratory effect [PMID:36261010 "IBSP, enhances tumor growth and promotes the migration of GTCs along the vasculature"].

## Complement regulation

BSP forms a tight complex with complement factor H and can protect cells from complement attack [PMID:10747989 "Recombinant OPN and BSP can protect murine erythroleukemia cells from attack by human complement"]. The paper describes initial alpha-V/beta-3 engagement followed by factor H sequestration. This supports negative regulation of complement-dependent cytotoxicity but does not justify retaining the uninformative protein binding term when integrin binding is already available.

## Curation boundaries

The membrane and osteoblast-differentiation HDA annotations from PMID:16210410 cannot be adjudicated confidently from the abstract, which does not expose the IBSP-specific result. They remain UNDECIDED in accordance with the rule against overruling experimental curators from incomplete evidence.

HuRI binary interactions with FAM9B and FXYD3 are not incorporated into the core function. They are topologically difficult to reconcile with a secreted mature matrix ligand, have no established endogenous mechanism, and are represented only by generic protein binding.

Transferred vesicle localization derives from direct rat growth-plate matrix-vesicle detection. The conserved idea is plausible, but extracellular vesicle is the informative replacement for generic vesicle. The transferred growth-factor response reflects expression control and is kept as non-core.

## Synthesis

IBSP is best understood as a mineralized-matrix ligand with two coupled molecular activities: hydroxyapatite binding and RGD-dependent integrin binding. These activities organize the bone cell-matrix interface, support adhesion and migration, and contribute to bone formation and mineralization. Tumor migration and complement evasion are experimentally supported extensions of the same extracellular ligand biology, not the primary skeletal core.

