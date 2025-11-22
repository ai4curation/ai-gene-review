#!/usr/bin/env python3
"""Helper script to generate review text for remaining HSPG2 annotations"""

# Mapping of Reactome pathway IDs to descriptions and actions
reactome_golgi_hs_biosynthesis = {
    "R-HSA-2022856": "EXT1:EXT2 transfers GlcA to heparan",
    "R-HSA-2022860": "NDST1-4 can sulfate a glucosamine residue in heparan to form heparan sulfate (HS)",
    "R-HSA-2022887": "NDST1-4 N-deacetylates GlcNAc residues in heparan",
    "R-HSA-2024108": "Some HSPGs are secreted to the plasma membrane",
    "R-HSA-2076383": "HS3ST1 sulfates GlcN at C3 in heparan sulfate",
    "R-HSA-2076392": "EXT1:EXT2 transfers GlcA to heparan",
    "R-HSA-2076419": "HS6STs sulfate GlcN at C6 in heparan sulfate/heparin",
    "R-HSA-2076508": "HS2ST1 trimer sulfates IdoA at C2 in heparan sulfate",
    "R-HSA-2076611": "HS3ST2-6 sulfate GlcN at C3 in heparan sulfate",
    "R-HSA-3656254": "Defective EXT2 (in EXT1:EXT2) does not transfer GlcNAc to the heparan chain",
    "R-HSA-3656257": "Defective EXT1 (in EXT1:EXT2) does not transfer GlcA to heparan",
    "R-HSA-3656261": "Defective EXT1 (in EXT1:EXT2) does not transfer GlcNAc to the heparan chain",
    "R-HSA-3656267": "Defective EXT2 (in EXT1:EXT2) does not transfer GlcA to heparan",
    "R-HSA-9036285": "Defective EXT1 (in EXT1:EXT2) does not transfer GlcA to heparan",
    "R-HSA-9036289": "Defective EXT2 (in EXT1:EXT2) does not transfer GlcA to heparan",
    "R-HSA-9953259": "EXTL3 dimer transfers GlcNAc to the GAG linker",
    "R-HSA-1667005": "Heparanase (HPSE) cleaves heparan sulfate from its proteoglycan (lysosome)",
    "R-HSA-1889955": "B3GAT dimers transfer GlcA to tetrasaccharide linker",
    "R-HSA-1889978": "B3GALT6 transfers Gal to the tetrasaccharide linker",
    "R-HSA-3560802": "Defective B3GAT3 does not transfer GlcA to tetrasaccharide linker",
    "R-HSA-4420365": "Defective B3GALT6 does not transfer Gal to the tetrasaccharide linker",
}

reactome_plasma_membrane = {
    "R-HSA-1678694": "Heparanase 2 (HPSE2) binds heparan sulfate proteoglycans",
    "R-HSA-2024084": "HS-GAGs translocate to the lysosome for degradation",
    "R-HSA-2024108": "Some HSPGs are secreted to the plasma membrane",
    "R-HSA-2404131": "LRPs transport extracellular CR:atREs:HSPG:apoE to cytosol",
    "R-HSA-2423785": "CR:atREs binds apoE and HSPG",
    "R-HSA-2429643": "NREH hydrolyses atREs (HSPG:apoE) to atROL and FAs",
    "R-HSA-9694579": "Spike glycoprotein of SARS-CoV-2 binds ACE2 on host cell",
    "R-HSA-9694661": "TMPRSS2 Mediated SARS-CoV-2 Spike Protein Cleavage and Endocytosis",
    "R-HSA-9698988": "Direct Host Cell Membrane Fusion and Release of SARS-CoV-2 Nucleocapsid",
    "R-HSA-9699007": "FURIN Mediated SARS-CoV-2 Spike Protein Cleavage and Endocytosis",
    "R-HSA-9836899": "sG binds to HSPGs",
}

# Generate review text for Golgi HS biosynthesis annotations
for pathway_id, description in reactome_golgi_hs_biosynthesis.items():
    if "Defective" in description:
        action = "KEEP_AS_NON_CORE"
        summary = f'TAS annotation from Reactome pathway "{description}". Documents disease-causing mutations affecting heparan sulfate biosynthesis machinery that processes perlecan in the Golgi.'
        reason = "Non-core biosynthetic localization. This documents disease mutations in HS biosynthesis enzymes, not core perlecan function. Golgi is a transient biosynthetic compartment where perlecan receives its heparan sulfate modifications."
    else:
        action = "KEEP_AS_NON_CORE"
        summary = f'TAS annotation from Reactome pathway "{description}". Documents heparan sulfate chain synthesis/modification in Golgi during perlecan biosynthesis.'
        reason = "Non-core biosynthetic localization. All heparan sulfate proteoglycans undergo complex enzymatic modifications in the Golgi during biosynthesis. This is a required transient biosynthetic step, not a functional localization where perlecan carries out its biological activities."

    print(f"\n- term:")
    print(f"    id: GO:0005796")
    print(f"    label: Golgi lumen")
    print(f"  evidence_type: TAS")
    print(f"  original_reference_id: Reactome:{pathway_id}")
    print(f"  review:")
    print(f"    summary: {summary}")
    print(f"    action: {action}")
    print(f"    reason: {reason}")

# Generate review text for plasma membrane annotations
print("\n\n# Plasma membrane annotations:")
for pathway_id, description in reactome_plasma_membrane.items():
    if "SARS-CoV-2" in description:
        action = "KEEP_AS_NON_CORE"
        summary = f'TAS annotation from Reactome pathway "{description}". Documents perlecan as one of many HSPGs that SARS-CoV-2 may interact with at the cell surface during viral entry.'
        reason = "Non-core and peripheral function. While HSPGs including perlecan may facilitate SARS-CoV-2 attachment to cells, this is not a physiological function but rather a pathogen exploitation of cell surface glycans. This does not represent a core function or characteristic localization of perlecan."
    elif "apoE" in description or "LRP" in description:
        action = "KEEP_AS_NON_CORE"
        summary = f'TAS annotation from Reactome pathway "{description}". Documents perlecan participation in lipoprotein uptake processes at the plasma membrane.'
        reason = "Non-core localization. While perlecan can participate in receptor-mediated processes at the plasma membrane involving LRP and apoE, this is not a primary localization. Perlecan's core functions occur in basement membranes and extracellular matrix, not at the plasma membrane."
    elif "HPSE2" in description:
        action = "KEEP_AS_NON_CORE"
        summary = f'TAS annotation from Reactome pathway "{description}". Documents heparanase 2 binding to perlecan and other HSPGs.'
        reason = "Non-core annotation. While heparanase 2 binds perlecan's heparan sulfate chains, this interaction can occur wherever perlecan is localized. The annotation implies plasma membrane as a site for this interaction, but this is not a primary perlecan localization."
    elif pathway_id == "R-HSA-2024084" or pathway_id == "R-HSA-2024108":
        # Already covered above
        continue
    else:
        action = "KEEP_AS_NON_CORE"
        summary = f'TAS annotation from Reactome pathway "{description}".'
        reason = "Non-core localization. Plasma membrane is not a primary localization for perlecan, which functions in basement membranes and extracellular matrix."

    print(f"\n- term:")
    print(f"    id: GO:0005886")
    print(f"    label: plasma membrane")
    print(f"  evidence_type: TAS")
    print(f"    original_reference_id: Reactome:{pathway_id}")
    print(f"  review:")
    print(f"    summary: {summary}")
    print(f"    action: {action}")
    print(f"    reason: {reason}")
