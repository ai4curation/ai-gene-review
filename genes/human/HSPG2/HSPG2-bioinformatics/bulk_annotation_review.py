#!/usr/bin/env python3
"""
Bulk annotation review for HSPG2/Perlecan GO annotations.
This script provides systematic reviews for the remaining annotations.
"""

# Annotation review decisions organized by annotation type

# All Golgi lumen annotations (Reactome TAS)
golgi_lumen_review = {
    'summary': 'TAS annotation from Reactome pathway for heparan sulfate biosynthesis. Perlecan transits through the Golgi lumen during biosynthesis where heparan sulfate chains undergo extensive enzymatic modifications including sulfation, epimerization, and chain extension by EXT1/EXT2, NDST, and various sulfotransferases. This is a transient biosynthetic localization.',
    'action': 'KEEP_AS_NON_CORE',
    'reason': 'Accurate but non-core. All heparan sulfate proteoglycans transit through the Golgi for glycosaminoglycan chain synthesis and modification. This is a biosynthetic compartment, not where perlecan carries out its biological functions. The numerous Reactome annotations document the complex biosynthetic machinery but do not represent functional localization.'
}

# Plasma membrane annotations (Reactome TAS)
plasma_membrane_review = {
    'summary': 'TAS annotation from Reactome pathways. Some annotations relate to perlecan interaction with cell surface receptors (HPSE2, LRP1) or degradation pathways. Perlecan can associate with cell surfaces through interactions with integrins and other receptors, but this is not its primary localization.',
    'action': 'KEEP_AS_NON_CORE',
    'reason': 'Peripheral localization. While perlecan can interact with plasma membrane receptors and cell surface HSPGs, its primary and functionally important localizations are basement membranes and extracellular matrix. Cell surface association is transient and related to endocytic uptake or receptor binding rather than core function.'
}

# Extracellular region annotations (multiple Reactome TAS)
extracellular_region_review = {
    'summary': 'TAS annotation from Reactome pathways documenting perlecan in various extracellular processes including proteolytic degradation, growth factor binding, integrin interactions, and amyloid plaque formation.',
    'action': 'ACCEPT',
    'reason': 'Core localization. Perlecan functions entirely in extracellular spaces including basement membranes, extracellular matrix, and extracellular space. Multiple annotations from different Reactome pathways appropriately document this fundamental localization.'
}

# Extracellular matrix structural constituent conferring compression resistance
ecm_structural_review = {
    'summary': 'RCA (Rapid Curation Algorithm) annotations from multiple proteomics studies of extracellular matrix. Perlecan contributes to ECM mechanical properties through its large proteoglycan structure with extended heparan sulfate chains that provide hydration and compressive resilience.',
    'action': 'ACCEPT',
    'reason': 'Core molecular function. Perlecan is a major structural constituent of basement membranes and cartilage ECM. Its high negative charge density from heparan sulfate chains attracts water and cations, providing compression resistance particularly important in cartilage and glomerular basement membrane. This represents an essential biophysical function.'
}

# Lysosomal lumen annotations
lysosomal_lumen_review = {
    'summary': 'TAS annotation from Reactome showing heparan sulfate-GAGs and HSPGs translocate to lysosomes for degradation by heparanase. This represents catabolic degradation rather than functional localization.',
    'action': 'KEEP_AS_NON_CORE',
    'reason': 'Catabolic localization. Perlecan undergoes degradation in lysosomes as part of normal ECM turnover, but this is not a functional site where perlecan carries out its biological activities. This is an endpoint of perlecan metabolism, not core function.'
}

# Extracellular exosome annotations (HDA from proteomics)
exosome_review = {
    'summary': 'HDA annotations from proteomics studies detecting perlecan in extracellular exosomes from various body fluids (urine, saliva, prostatic secretions, trabecular meshwork). These likely represent perlecan fragments or shed perlecan rather than functional localization.',
    'action': 'KEEP_AS_NON_CORE',
    'reason': 'Non-core localization. Detection in exosomes likely reflects perlecan shedding, proteolytic processing, or ECM turnover rather than a functional role in exosome biology. Endorepellin fragments are found in circulation and body fluids but this does not represent a primary site of action.'
}

# Focal adhesion annotation
focal_adhesion_review = {
    'summary': 'HDA annotation from proteomics study of focal adhesions. Perlecan can interact with integrins which are focal adhesion components, but focal adhesions are primarily intracellular structures.',
    'action': 'MARK_AS_OVER_ANNOTATED',
    'reason': 'Likely over-annotation. Focal adhesions are integrin-based adhesion complexes with extensive intracellular components. While perlecan interacts with integrins from the extracellular side, it is not properly a component of focal adhesions. Detection in focal adhesion proteomics likely reflects associated ECM rather than true focal adhesion localization.'
}

# Extracellular space annotations
extracellular_space_review = {
    'summary': 'HDA annotations from proteomics studies. Extracellular space is appropriate for perlecan which is secreted and functions in extracellular compartments.',
    'action': 'ACCEPT',
    'reason': 'Core localization. Perlecan is a secreted protein that functions in the extracellular space including basement membranes, ECM, and interstitial spaces.'
}

# Basement membrane TAS annotations
basement_membrane_tas_review = {
    'summary': 'TAS annotations from literature. Basement membrane is the canonical and most important localization for perlecan, where it cross-links laminin and collagen IV networks and regulates growth factor availability.',
    'action': 'ACCEPT',
    'reason': 'Core localization. Basement membrane represents perlecan\'s primary site of biological function. This is where perlecan carries out its essential structural and signaling roles.'
}

# Process-related annotations
inflammatory_response_review = {
    'summary': 'TAS annotation from PMID:21126803. Perlecan domain V has anti-inflammatory properties and can protect against amyloid-beta neurotoxicity. Perlecan\'s expression is upregulated by inflammatory signals like TNF-alpha through NFkB.',
    'action': 'KEEP_AS_NON_CORE',
    'reason': 'Secondary function. While perlecan expression responds to inflammatory signals and endorepellin has anti-inflammatory properties, this is not a core function of perlecan. This represents pleiotropic effects rather than primary biological role.'
}

# Negative regulation of angiogenesis
negative_regulation_angiogenesis_review = {
    'summary': 'TAS annotation from PMID:21126803 on endorepellin. The cleaved domain V fragment (endorepellin) exhibits potent anti-angiogenic activity through dual antagonism of VEGFR2 and α2β1 integrin. This opposes the pro-angiogenic activity of full-length perlecan.',
    'action': 'ACCEPT',
    'reason': 'Core function of the endorepellin fragment. While representing only a proteolytically-generated fragment rather than full-length perlecan, endorepellin\'s anti-angiogenic activity is well-characterized and represents an important regulatory mechanism. The annotation is appropriate for the gene product even though it requires proteolytic processing.'
}

# Lipid metabolic process
lipid_metabolic_review = {
    'summary': 'TAS annotation from PMID:21289173 on amyloid-beta uptake and LRP1-mediated endocytosis. This study shows perlecan/HSPG cooperates with LRP1 in receptor-mediated endocytosis which has connections to lipid metabolism. However, lipid metabolism is not a primary function of perlecan.',
    'action': 'MARK_AS_OVER_ANNOTATED',
    'reason': 'Over-annotation. While this paper documents perlecan/HSPG involvement in LRP1-mediated endocytosis (which LRP1 uses for lipoprotein uptake), perlecan\'s role is as a co-receptor for binding rather than direct involvement in lipid metabolism. This represents indirect connection rather than core function.'
}

# LDL particle receptor binding
ldl_receptor_binding_review = {
    'summary': 'TAS annotation from PMID:21289173 showing HSPG cooperates with LRP1 in cellular uptake. Perlecan/HSPG binds amyloid-beta and facilitates LRP1-mediated endocytosis. The connection to LDL receptor is indirect.',
    'action': 'KEEP_AS_NON_CORE',
    'reason': 'Non-core function. While perlecan can cooperate with LRP1 in endocytic processes, this is not a primary function. Perlecan acts as a co-receptor or binding partner rather than having direct LDL particle receptor binding activity itself. This represents a specialized context rather than core function.'
}

# Amyloid-beta binding
amyloid_beta_binding_review = {
    'summary': 'IC annotation from PMID:21289173 showing HSPGs including perlecan bind amyloid-beta through heparan sulfate chains and cooperate with LRP1 in cellular Aβ uptake. PMID:21126803 shows endorepellin domain V inhibits α2 integrin-mediated Aβ neurotoxicity.',
    'action': 'KEEP_AS_NON_CORE',
    'reason': 'Non-core function. While perlecan binds amyloid-beta through its heparan sulfate chains (like many HSPGs) and endorepellin can protect against Aβ toxicity, this is not a primary biological function of perlecan. This represents a pathological interaction relevant to Alzheimer\'s disease rather than normal perlecan function.'
}

# Receptor-mediated endocytosis
receptor_mediated_endocytosis_review = {
    'summary': 'ISS annotation based on mouse ortholog, with support from PMID:21289173 showing perlecan/HSPG cooperates with LRP1 in amyloid-beta uptake through receptor-mediated endocytosis. Perlecan serves as a cell surface binding site that facilitates LRP1-mediated internalization.',
    'action': 'KEEP_AS_NON_CORE',
    'reason': 'Non-core function. While experimentally validated, receptor-mediated endocytosis is not a primary function of extracellular matrix-localized perlecan. This represents a specialized activity when perlecan or perlecan fragments interact with cell surface receptors rather than core basement membrane functions.'
}

# Plasma membrane protein complex
plasma_membrane_complex_review = {
    'summary': 'TAS annotation from PMID:21289173 describing HSPG/LRP1 complex at plasma membrane for amyloid-beta uptake. This documents a specific context where perlecan/HSPG acts as co-receptor with LRP1.',
    'action': 'KEEP_AS_NON_CORE',
    'reason': 'Non-core localization. This represents a specialized interaction complex relevant to amyloid-beta metabolism rather than perlecan\'s primary basement membrane localization. While validated experimentally, this is not where perlecan carries out its essential functions.'
}

print("Bulk annotation review completed. Apply these reviews to remaining annotations based on GO term and evidence type.")
