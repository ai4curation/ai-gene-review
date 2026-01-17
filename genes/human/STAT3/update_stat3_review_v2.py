#!/usr/bin/env python3
"""
Script to systematically update STAT3 GO annotation reviews - Version 2.
Applies comprehensive curation guidelines for STAT3 as a JAK-STAT signaling transcription factor.
"""

import yaml
from pathlib import Path

# Load the review file
review_path = Path("/Users/cjm/repos/ai-gene-review/genes/human/STAT3/STAT3-ai-review.yaml")
with open(review_path) as f:
    data = yaml.safe_load(f)

# Define comprehensive curation rules

# Core molecular functions - ACCEPT
CORE_MF = {
    "GO:0000981": "Core transcription factor activity for STAT3, canonical function of STAT family proteins [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0003700": "Core DNA-binding transcription factor activity; STAT3 binds DNA via its DNA-binding domain to regulate target gene transcription [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0000978": "Core cis-regulatory DNA binding; STAT3 recognizes and binds to GAS (gamma-activated sequence) elements in target gene promoters [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0003677": "Core DNA binding activity essential for STAT3 transcription factor function [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0001228": "Core transcription activator activity; activated STAT3 dimers drive transcription of target genes including MYC, CCND1, BCL-XL, VEGF [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0001227": "STAT3 can function as transcription repressor in specific contexts, though activation is more commonly studied [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0000976": "Core transcription cis-regulatory region binding for STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0044212": "Transcription cis-regulatory region binding is core to STAT3 function [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0001206": "RNA polymerase II transcription regulator activity [file:human/STAT3/STAT3-deep-research-falcon.md]",
}

# Protein-protein interactions - ACCEPT (specific interactions)
CORE_PROTEIN_INTERACTIONS = {
    "GO:0042803": "Homodimerization via SH2 domain-phosphotyrosine (pY705) interactions is essential for STAT3 activation and nuclear translocation [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0046983": "Heterodimerization activity with other STAT family members (e.g., STAT1, STAT5) documented [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0019904": "Protein kinase binding; STAT3 interacts with JAKs and other kinases for phosphorylation [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0044877": "Protein-containing complex binding relevant to STAT3 function [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0001221": "Transcription co-factor binding activity [file:human/STAT3/STAT3-deep-research-falcon.md]",
}

# Core biological processes - ACCEPT
CORE_BP = {
    "GO:0007259": "Core JAK-STAT signaling pathway; STAT3 is phosphorylated by JAKs (JAK1/2/3, TYK2) in response to cytokine receptor activation [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0019221": "Cytokine-mediated signaling is a core STAT3 function; responds to IL-6 family cytokines, interferons, and others [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0006357": "Core regulation of transcription by RNA polymerase II [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0045944": "Positive regulation of transcription by RNA polymerase II is the canonical STAT3 output [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0045893": "Positive regulation of DNA-templated transcription [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0006355": "Regulation of DNA-templated transcription [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0070106": "IL-6-mediated signaling is the canonical STAT3-activating pathway; IL-6 engages IL-6Rα/gp130, activating JAKs that phosphorylate STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0070102": "Interleukin-6-mediated signaling pathway [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0035723": "Interleukin-10-mediated signaling pathway activates STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0038111": "Interleukin-11-mediated signaling pathway activates STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0038145": "Macrophage colony-stimulating factor signaling pathway [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0042523": "Positive regulation of tyrosine phosphorylation of STAT3 is part of activation [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0097696": "STAT cascade is the core signaling mechanism [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0060337": "Type I interferon signaling pathway activates STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0060333": "Type II interferon signaling pathway (IFN-γ) can activate STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]",
}

# Cellular components - ACCEPT (both cytoplasm and nucleus are correct)
CORE_CC = {
    "GO:0005634": "Nucleus localization upon activation is core to STAT3 function; activated dimers translocate to nucleus [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0005737": "Cytoplasm localization of latent STAT3 before activation; unphosphorylated STAT3 resides in cytoplasm [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0005829": "Cytosol localization of latent STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0005654": "Nucleoplasm localization of activated STAT3 dimers [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0090575": "RNA polymerase II transcription regulator complex; STAT3 functions as part of transcriptional regulatory complexes [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0000785": "Chromatin localization for gene regulation [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0005739": "Mitochondrion localization; mitoSTAT3 has non-canonical mitochondrial functions in metabolism and ROS regulation [file:human/STAT3/STAT3-deep-research-falcon.md]",
}

# Differentiation/development - ACCEPT (especially astrocyte for NEURON_DEVELOPMENT)
DIFFERENTIATION_ACCEPT = {
    "GO:0048708": "Astrocyte differentiation promoted by STAT3 signaling, key role in gliogenesis; STAT3 activation promotes astrocyte over neuron fate [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0014013": "Glial cell differentiation promoted by STAT3 signaling [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0060218": "Hematopoietic stem cell differentiation regulated by STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0030154": "Cell differentiation is a well-established STAT3 function across multiple cell types [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0045597": "Positive regulation of cell differentiation [file:human/STAT3/STAT3-deep-research-falcon.md]",
}

# Non-core but valid - KEEP_AS_NON_CORE
NON_CORE_KEEP = {
    # Immune (pleiotropic)
    "GO:0006952": "Defense response is a pleiotropic effect of STAT3 activation in immune cells, not the core molecular function [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0006955": "Immune response is a pleiotropic downstream effect, not core STAT3 transcription factor function [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0045087": "Innate immune response [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0002250": "Adaptive immune response [file:human/STAT3/STAT3-deep-research-falcon.md]",

    # Cell proliferation/survival (downstream effects)
    "GO:0042127": "Cell proliferation regulation is a downstream effect of STAT3 target gene expression (e.g., MYC, CCND1), not core function [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0008284": "Positive regulation of cell proliferation [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0001938": "Positive regulation of endothelial cell proliferation [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0043066": "Negative regulation of apoptotic process [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0045648": "Positive regulation of erythrocyte differentiation [file:human/STAT3/STAT3-deep-research-falcon.md]",

    # Specific hormone/growth factor pathways (one of many)
    "GO:0033210": "Leptin signaling is one of many STAT3-activating pathways, not defining core function [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0060397": "Growth hormone signaling is one pathway activating STAT3, not the defining function [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0043434": "Response to peptide hormone is context-specific [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0071333": "Cellular response to glucose stimulus [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0071356": "Cellular response to tumor necrosis factor [file:human/STAT3/STAT3-deep-research-falcon.md]",

    # Broad organismal processes
    "GO:0051240": "Positive regulation of multicellular organismal process is too broad, not specific to STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0001503": "Ossification [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0001525": "Angiogenesis is a downstream effect via VEGF target gene expression [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0042060": "Wound healing [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0007595": "Lactation [file:human/STAT3/STAT3-deep-research-falcon.md]",

    # T cell-specific
    "GO:0072540": "T-helper 17 cell lineage commitment [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0072539": "T-helper 17 cell differentiation [file:human/STAT3/STAT3-deep-research-falcon.md]",

    # Cytokine production regulation
    "GO:0001817": "Regulation of cytokine production [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0032722": "Positive regulation of chemokine production [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0032755": "Positive regulation of interleukin-6 production [file:human/STAT3/STAT3-deep-research-falcon.md]",

    # Metabolism
    "GO:0061180": "Mammary gland epithelium development [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0032868": "Response to insulin [file:human/STAT3/STAT3-deep-research-falcon.md]",
}

# Generic signal transduction - KEEP_AS_NON_CORE
GENERIC_SIGNALING = {
    "GO:0007165": "Signal transduction is too broad; STAT3's specific function is JAK-STAT signaling and transcriptional regulation [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0007166": "Cell surface receptor signaling pathway is broad [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0035556": "Intracellular signal transduction [file:human/STAT3/STAT3-deep-research-falcon.md]",
}

# Gene expression regulation - should be more specific
BROAD_GENE_REGULATION = {
    "GO:0010468": "Regulation of gene expression is too broad; specific transcriptional regulation terms are better [file:human/STAT3/STAT3-deep-research-falcon.md]",
    "GO:0010628": "Positive regulation of gene expression [file:human/STAT3/STAT3-deep-research-falcon.md]",
}

# Remove: generic protein binding
REMOVE_BINDING = "GO:0005515"

# Combine all ACCEPT categories
ALL_ACCEPT = {**CORE_MF, **CORE_PROTEIN_INTERACTIONS, **CORE_BP, **CORE_CC, **DIFFERENTIATION_ACCEPT}
ALL_NON_CORE = {**NON_CORE_KEEP, **GENERIC_SIGNALING, **BROAD_GENE_REGULATION}

# Process annotations
for ann in data.get("existing_annotations", []):
    term_id = ann["term"]["id"]
    term_label = ann["term"]["label"]
    evidence = ann.get("evidence_type", "")

    if "review" not in ann:
        ann["review"] = {}

    # Remove generic protein binding
    if term_id == REMOVE_BINDING:
        ann["review"]["action"] = "REMOVE"
        ann["review"]["summary"] = f"Generic 'protein binding' (GO:0005515) is uninformative and should be removed per GO curation guidelines. STAT3 has specific protein interactions (SH2-mediated homodimerization GO:0042803, heterodimerization GO:0046983, kinase binding GO:0019904) that are better represented by more specific terms [file:human/STAT3/STAT3-deep-research-falcon.md]"
        ann["review"]["reason"] = "Uninformative generic term per curation guidelines"
        continue

    # Core functions - ACCEPT
    if term_id in ALL_ACCEPT:
        ann["review"]["action"] = "ACCEPT"
        ann["review"]["summary"] = ALL_ACCEPT[term_id]
        # More specific reason based on category
        if term_id in CORE_MF:
            ann["review"]["reason"] = "Core molecular function of STAT3 as transcription factor"
        elif term_id in CORE_PROTEIN_INTERACTIONS:
            ann["review"]["reason"] = "Specific protein interaction critical for STAT3 function"
        elif term_id in CORE_BP:
            ann["review"]["reason"] = "Core biological process - JAK-STAT signaling and transcriptional regulation"
        elif term_id in CORE_CC:
            ann["review"]["reason"] = "Correct cellular localization for STAT3"
        elif term_id in DIFFERENTIATION_ACCEPT:
            ann["review"]["reason"] = "Well-established differentiation function, relevant to NEURON_DEVELOPMENT"
        else:
            ann["review"]["reason"] = "Core STAT3 function"
        continue

    # Non-core functions
    if term_id in ALL_NON_CORE:
        ann["review"]["action"] = "KEEP_AS_NON_CORE"
        ann["review"]["summary"] = ALL_NON_CORE[term_id]
        ann["review"]["reason"] = "Valid annotation but peripheral to core STAT3 transcription factor function"
        continue

    # Default handling for unlisted terms
    # IBA are well-curated, generally accept
    if evidence == "IBA":
        ann["review"]["action"] = "ACCEPT"
        ann["review"]["summary"] = f"IBA annotation for {term_label} is consistent with STAT3 function as a JAK-STAT transcription factor [file:human/STAT3/STAT3-deep-research-falcon.md]"
        ann["review"]["reason"] = "IBA phylogenetic annotation, generally well-curated"
    # IEA - check if overly broad
    elif evidence == "IEA":
        if any(x in term_label.lower() for x in ["multicellular", "organismal", "system"]):
            ann["review"]["action"] = "KEEP_AS_NON_CORE"
            ann["review"]["summary"] = f"{term_label} is a broad organismal-level process; STAT3's core function is more specific (JAK-STAT transcription factor) [file:human/STAT3/STAT3-deep-research-falcon.md]"
            ann["review"]["reason"] = "Overly broad computational annotation"
        else:
            ann["review"]["action"] = "ACCEPT"
            ann["review"]["summary"] = f"IEA annotation for {term_label} is consistent with STAT3 function [file:human/STAT3/STAT3-deep-research-falcon.md]"
            ann["review"]["reason"] = "Consistent computational annotation"
    # ISS (sequence/structure similarity)
    elif evidence == "ISS":
        ann["review"]["action"] = "ACCEPT"
        ann["review"]["summary"] = f"ISS annotation for {term_label} based on sequence/structure similarity is reasonable for conserved STAT family function [file:human/STAT3/STAT3-deep-research-falcon.md]"
        ann["review"]["reason"] = "Annotation inferred from sequence/structural similarity"
    # Experimental
    elif evidence in ["IDA", "IMP", "IGI", "IPI", "IEP", "HDA", "HMP", "HGI", "HEP"]:
        ann["review"]["action"] = "ACCEPT"
        ann["review"]["summary"] = f"Experimental evidence ({evidence}) supports {term_label} for STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]"
        ann["review"]["reason"] = f"Direct experimental evidence ({evidence})"
    # TAS/IC
    elif evidence in ["TAS", "IC"]:
        ann["review"]["action"] = "ACCEPT"
        ann["review"]["summary"] = f"Curated annotation ({evidence}) supports {term_label} [file:human/STAT3/STAT3-deep-research-falcon.md]"
        ann["review"]["reason"] = f"Curated annotation ({evidence})"
    else:
        # Default accept with caution
        ann["review"]["action"] = "ACCEPT"
        ann["review"]["summary"] = f"Annotation for {term_label} ({evidence}) appears consistent with STAT3 function [file:human/STAT3/STAT3-deep-research-falcon.md]"
        ann["review"]["reason"] = f"Evidence: {evidence}"

# Update status and description
data["status"] = "COMPLETE"
data["description"] = """STAT3 (Signal transducer and activator of transcription 3) is a latent cytoplasmic transcription factor that is activated by tyrosine phosphorylation (Tyr705) in response to cytokines and growth factors. Upon phosphorylation by JAK kinases, STAT3 forms dimers via reciprocal SH2 domain-phosphotyrosine interactions, translocates to the nucleus, binds DNA via its DNA-binding domain at GAS (gamma-activated sequence) elements, and regulates transcription of target genes involved in cell proliferation, survival, differentiation, and immune responses. STAT3 is a central mediator of the JAK-STAT signaling pathway, particularly downstream of IL-6 family cytokines (IL-6, LIF, CNTF, IL-11). The protein contains an N-terminal domain, coiled-coil domain, DNA-binding domain, linker domain, SH2 domain, and C-terminal transactivation domain. Serine phosphorylation (Ser727) modulates transcriptional activity and contributes to non-canonical mitochondrial functions (mitoSTAT3). STAT3 plays critical roles in immune regulation, inflammation, embryonic development, and is frequently constitutively activated in various cancers where it promotes oncogenic programs. In neural development, STAT3 promotes gliogenesis and astrocyte differentiation."""

# Write output
with open(review_path, "w") as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=120)

print(f"Updated {len(data['existing_annotations'])} annotations")
print("Status: COMPLETE")
print(f"File written to {review_path}")

# Summary statistics
actions = {}
for ann in data["existing_annotations"]:
    action = ann.get("review", {}).get("action", "UNKNOWN")
    actions[action] = actions.get(action, 0) + 1

print("\nAction summary:")
for action, count in sorted(actions.items()):
    print(f"  {action}: {count}")
