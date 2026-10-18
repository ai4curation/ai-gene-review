---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T15:26:10.372170'
end_time: '2026-09-27T15:36:05.856529'
duration_seconds: 595.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: vha-1
  gene_symbol: vha-1
  uniprot_accession: Q21898
  protein_description: 'RecName: Full=V-type proton ATPase 16 kDa proteolipid subunit
    c 1 {ECO:0000305}; Short=V-ATPase 16 kDa proteolipid subunit c 1 {ECO:0000305};
    AltName: Full=Vacuolar proton pump 16 kDa proteolipid subunit c 1 {ECO:0000305};'
  gene_info: Name=vha-1 {ECO:0000312|WormBase:R10E11.8}; ORFNames=R10E11.8 {ECO:0000312|WormBase:R10E11.8};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the V-ATPase proteolipid subunit family.
  protein_domains: ATPase_proteolipid_c-like_dom. (IPR002379); ATPase_proteolipid_csu.
    (IPR000245); ATPase_proteolipid_su_C_euk. (IPR011555); F/V-ATP_Csub_sf. (IPR035921);
    ATP-synt_C (PF00137)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: vha-1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q21898
- **Protein Description:** RecName: Full=V-type proton ATPase 16 kDa proteolipid subunit c 1 {ECO:0000305}; Short=V-ATPase 16 kDa proteolipid subunit c 1 {ECO:0000305}; AltName: Full=Vacuolar proton pump 16 kDa proteolipid subunit c 1 {ECO:0000305};
- **Gene Information:** Name=vha-1 {ECO:0000312|WormBase:R10E11.8}; ORFNames=R10E11.8 {ECO:0000312|WormBase:R10E11.8};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the V-ATPase proteolipid subunit family.
- **Key Domains:** ATPase_proteolipid_c-like_dom. (IPR002379); ATPase_proteolipid_csu. (IPR000245); ATPase_proteolipid_su_C_euk. (IPR011555); F/V-ATP_Csub_sf. (IPR035921); ATP-synt_C (PF00137)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "vha-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'vha-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **vha-1** (gene ID: vha-1, UniProt: Q21898) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q21898
- **Protein Description:** RecName: Full=V-type proton ATPase 16 kDa proteolipid subunit c 1 {ECO:0000305}; Short=V-ATPase 16 kDa proteolipid subunit c 1 {ECO:0000305}; AltName: Full=Vacuolar proton pump 16 kDa proteolipid subunit c 1 {ECO:0000305};
- **Gene Information:** Name=vha-1 {ECO:0000312|WormBase:R10E11.8}; ORFNames=R10E11.8 {ECO:0000312|WormBase:R10E11.8};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the V-ATPase proteolipid subunit family.
- **Key Domains:** ATPase_proteolipid_c-like_dom. (IPR002379); ATPase_proteolipid_csu. (IPR000245); ATPase_proteolipid_su_C_euk. (IPR011555); F/V-ATP_Csub_sf. (IPR035921); ATP-synt_C (PF00137)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "vha-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'vha-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **vha-1** (gene ID: vha-1, UniProt: Q21898) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *C. elegans vha-1* / VHA-1 (UniProt Q21898)

## Executive conclusion

The requested target is correctly identified as *Caenorhabditis elegans vha-1*, ORF **R10E11.8**, encoding **V-type proton ATPase 16-kDa proteolipid subunit c1**. A worm V-ATPase gene table directly maps *vha-1* to R10E11.8 on chromosome III, while comparative analysis maps worm VHA-1/VHA-c1 to the V0 c-subunit family that includes human ATP6V0C and yeast Vma3. The retrieved papers did not print UniProt accession Q21898, so the accession-to-locus link rests on the supplied UniProt record; no conflicting same-symbol gene was used. (allan2005genomewidesurveyof pages 7-8, syntichakiUnknownyearsupplementaldatathe pages 2-3)

VHA-1 is not the ATP-hydrolyzing enzyme subunit. It is a small integral-membrane **rotor proteolipid** in the V0 c-ring. Its primary substrate is **H+**: ATP hydrolysis in the cytosolic V1 motor drives rotation of the central rotor and c-ring, moving protons through two offset aqueous half-channels in V0 subunit a. In cells, the usual outcome is proton movement from cytosol into an organelle lumen—or across a specialized plasma membrane—creating an acidic lumen and electrochemical gradient. This molecular assignment is strongly supported by comparative family mapping and modern V-ATPase structures, although purified Q21898-specific transport kinetics have not been reported in the retrieved literature. (bidaudmeynard2018thelossof pages 1-6, kishikawa2024rotarymechanismof pages 1-3, oot2024humanvatpasefunction pages 1-3)

| Annotation topic | Best-supported conclusion | Evidence type | Experimental basis | Representative source and date | Confidence / limitations |
|---|---|---|---|---|---|
| Exact gene identity | *C. elegans* **vha-1** corresponds to ORF **R10E11.8** on chromosome III. The target UniProt accession is **Q21898** according to the supplied UniProt record. | Direct gene-specific | A *C. elegans* V-ATPase gene table directly maps *vha-1* to R10E11.8 and chromosome III. | Syntichaki, Samara & Tavernarakis, supplemental data associated with the 2005 study (syntichakiUnknownyearsupplementaldatathe pages 2-3) | **High** for *vha-1*–R10E11.8 and organism; the retrieved literature did not independently print Q21898, so accession linkage relies on the supplied UniProt record. |
| Protein family and subunit identity | VHA-1 is the **V0 proteolipid subunit c1**—the worm counterpart of human ATP6V0C and yeast Vma3—not a V1 catalytic subunit. | Direct comparative mapping plus family-level inference | Cross-species V-ATPase tables map worm VHA-1/VHA-c1 to the V0 c-subunit family; worm experiments classify VHA-1 within the transmembrane V0 sector. | Allan et al., July 2005; Bidaud-Meynard et al., September 2018 / Development 2019 (allan2005genomewidesurveyof pages 7-8, bidaudmeynard2018thelossof pages 1-6) | **High** for family assignment. The retrieved primary passages do not provide a Q21898-specific biochemical reconstitution. |
| Primary molecular role | VHA-1 is a **membrane rotor/proton-carrier component of the c-ring**. It participates directly in proton translocation but does **not** hydrolyze ATP; ATP hydrolysis occurs at catalytic A/B interfaces in V1. | Direct complex-level plus family-level structural inference | V0/V1 division-of-labor experiments and modern structures place c proteolipids in the rotating membrane ring and ATP-hydrolyzing sites in the A3B3 head. | Bidaud-Meynard et al., September 2018; Oot & Wilkens, July 2024 (bidaudmeynard2018thelossof pages 1-6, oot2024humanvatpasefunction pages 1-3) | **High** for conserved subunit function; direct ATPase or proton-flux measurements on purified Q21898 are unavailable. |
| Transported substrate and energy coupling | The transported substrate is **H+**. ATP hydrolysis in V1 generates torque that rotates the central rotor and proteolipid c-ring past subunit-a aqueous half-channels, pumping protons across the membrane. | Direct complex-level plus family-level structural inference | Human V-ATPase architecture identifies three catalytic ATP sites and ATP-driven rotation; prokaryotic V/A-ATPase cryo-EM and molecular dynamics resolve proton transfer through subunit-a half-channels and c-ring acidic sites. | Oot & Wilkens, July 2024; Kishikawa et al., November 2024 (kishikawa2024rotarymechanismof pages 1-3, oot2024humanvatpasefunction pages 1-3) | **High** for the conserved rotary mechanism. Direction in eukaryotic organelles is normally cytosol-to-lumen, but this was not measured directly for purified worm VHA-1. |
| Membrane topology and proton-binding residue | VHA-1 is strongly expected to be a small, multipass membrane proteolipid carrying a conserved acidic proton-binding site, as required for c-ring function. | Family-level inference only | A 2.8-Å prokaryotic V/A-ATPase structure identifies c-subunit Glu63 protonation and its state-dependent interaction with the stator arginine. | Kishikawa et al., November 2024 (kishikawa2024rotarymechanismof pages 1-3) | **Moderate** for transfer to Q21898. The retrieved evidence does not experimentally determine Q21898 topology or identify its corresponding residue; residue numbering must not be transferred directly. |
| Excretory-system expression | *vha-1* is expressed in the **excretory cell in larvae and adults**, consistent with a role in the worm’s renal/osmoregulatory tubular system. | Direct gene-specific | Reporter/expression compilation explicitly records larval and adult excretory-cell expression. | Hahn-Windgassen & Van Gilst, July 2009 (hahnwindgassen2009thecaenorhabditiselegans pages 6-8) | **High** for tissue expression. Functional excretory-canal RNAi phenotypes in that study were measured for other V-ATPase subunits, not directly for *vha-1*. |
| Intestinal localization context | Intestinal assays place V0-ATPase activity at or near the **apical brush border/microvillar membrane** and associated trafficking compartments; V0 signal colocalizes with ERM-1/ezrin, and *vha-1* knockdown reduces apical VHA-6 reporter signal. | Direct gene-specific perturbation plus direct complex-level imaging | Intestinal RNAi and fluorescence/super-resolution imaging assessed apical V0 organization, brush-border markers and polarity proteins. | Bidaud-Meynard et al., September 2018 / Development 2019 (bidaudmeynard2018thelossof pages 1-6, bidaudmeynard2018thelossof pages 15-18) | **Moderate–high**. Evidence establishes the V0-dependent compartment and *vha-1* requirement but is not a localization study of endogenously tagged VHA-1 itself. |
| Intestinal epithelial trafficking and polarity | VHA-1 is required to maintain the polarized apical brush border. Its depletion causes basolateral or cytoplasmic redistribution of ERM-1, ACT-5, CDC-42, PAR-6 and PKC-3, microvillus atrophy and microvillus inclusions. | Direct gene-specific RNAi | A screen of 408 conserved trafficking/cytoskeletal genes followed by intestinal imaging identified *vha-1* and other V0 genes; 72-hour *vha-1* RNAi produced polarity and organelle defects. | Bidaud-Meynard et al., September 2018 / Development 2019 (bidaudmeynard2018thelossof pages 50-54, bidaudmeynard2018thelossof pages 30-32, bidaudmeynard2018thelossof pages 15-18, bidaudmeynard2018thelossof pages 1-6) | **High** for the RNAi-dependent phenotype; RNAi cannot by itself separate proton-pumping from possible V0 membrane-fusion functions. |
| Quantitative polarity effect | Across tested V0/V1-subunit knockdowns, apical-to-cytoplasmic ratios of ERM-1, PAR-6 and PKC-3 fell by approximately **15–40%**; V0 depletion additionally produced characteristic basolateral mislocalization. | Direct complex-level; partially gene-specific | Quantitative fluorescence analysis after V-ATPase RNAi. VHA-1 was among the directly tested V0 subunits, but the 15–40% range summarizes the subunit series rather than a uniquely isolated VHA-1 effect size. | Bidaud-Meynard et al., September 2018 / Development 2019 (bidaudmeynard2018thelossof pages 1-6) | **Moderate–high**. The full range should not be reported as a Q21898-only measurement. |
| RAB-11/SNAP-29 pathway | VHA-1-dependent V0 activity supports a **late apical trafficking step involving RAB-11-positive endosomes and SNAP-29**. Knockdown reduces apical RAB-11/SNAP-29 organization and disrupts delivery or retention of selected brush-border and polarity proteins. | Direct gene-specific perturbation plus complex-level pathway evidence | RNAi, marker localization, genetic interaction and live/super-resolution intestinal imaging. | Bidaud-Meynard et al., September 2018 / Development 2019 (bidaudmeynard2018thelossof pages 50-54, bidaudmeynard2018thelossof pages 15-18) | **High** for pathway association. Physical binding of Q21898 itself to RAB-11 or SNAP-29 was not demonstrated. |
| Lysosomal association | VHA-1 is associated with the **lysosomal V-ATPase proteome**, supporting residence of at least a VHA-1-containing pool on lysosomal membranes and participation in organelle acidification. | Direct complex-level proteomics; limited gene-specific detection | Adult-worm Lyso-IP proteomics detected V0 subunits including VHA-1; lysosome-enriched proteins were selected at at least 10-fold enrichment over flow-through, using four biological replicates. | Yu et al., January 2024 (yu2024organelleproteomicprofiling pages 5-6) | **Moderate–high** for lysosomal association. Proteomic detection does not establish exclusive localization or independently measure VHA-1-mediated proton flux. |
| Lysosomal signaling and proteostasis | Through V-ATPase-dependent acidification, VHA-1 is expected to support lysosomal degradation, autophagy and nutrient signaling; worm *vha-1* also appeared in a miR-1/V-ATPase screen affecting muscle performance under proteotoxic stress. | Direct gene-specific screening plus family-level inference | RNAi thrashing assays identified *vha-1* among likely mediators, while detailed mechanistic validation centered on another subunit, VHA-13. | Schiffer et al., July 2021, following the January 2021 preprint (schiffer2021mir1coordinatelyregulates pages 8-12) | **Moderate**. The lysosomal role is strongly supported for the complex, but detailed *vha-1*-specific acidification and regulatory measurements remain limited. |
| 2024 structural update | Current structural work supports an alternating-access rotary model: protonation of a c-ring glutamate disrupts or rearranges its interaction with the conserved subunit-a arginine, biasing c-ring movement; deprotonation permits proton release through the opposite half-channel. | Family-level inference | A 2.8-Å cryo-EM structure of a *Thermus thermophilus* V/A-ATPase V0 motor plus molecular-dynamics simulations; the studied ring contained 12 c subunits. | Kishikawa et al., November 2024 (kishikawa2024rotarymechanismof pages 1-3) | **High** for the rotary proton-transfer principle; c-ring stoichiometry, residue numbering and detailed energetics cannot be assumed identical for *C. elegans* Q21898. |
| Overall functional annotation | **VHA-1/Q21898 is an integral V0 c-ring proteolipid that couples V1 ATP hydrolysis to H+ transport, thereby enabling acidification-dependent lysosomal/endosomal physiology and specialized membrane-trafficking functions in excretory and intestinal epithelia.** | Integrated conclusion | Concordance among locus mapping, comparative family assignment, worm RNAi/imaging, lysosomal proteomics and modern rotary-ATPase structures. | Multiple sources, 2005–2024 (hahnwindgassen2009thecaenorhabditiselegans pages 6-8, allan2005genomewidesurveyof pages 7-8, bidaudmeynard2018thelossof pages 15-18, yu2024organelleproteomicprofiling pages 5-6, kishikawa2024rotarymechanismof pages 1-3, oot2024humanvatpasefunction pages 1-3) | **High** at the functional-class level; exact Q21898 topology, proton-binding residue, c-ring stoichiometry and purified transport kinetics remain unverified in the retrieved literature. |


*Table: Evidence-ranked annotation of *C. elegans* VHA-1/Q21898, separating direct gene-specific findings from V-ATPase complex evidence and cross-species structural inference. Limitations are highlighted to prevent overinterpretation of topology, residue identity and quantitative phenotypes.*

## 1. Identity and nomenclature verification

The evidence satisfies the mandatory identity checks:

1. **Gene-symbol match:** *vha-1* maps to **R10E11.8**, rather than to a similarly named protein from another organism. (syntichakiUnknownyearsupplementaldatathe pages 2-3)
2. **Organism:** the locus and experimental studies are from ***Caenorhabditis elegans***. (hahnwindgassen2009thecaenorhabditiselegans pages 6-8, syntichakiUnknownyearsupplementaldatathe pages 2-3)
3. **Protein-family match:** cross-species mapping identifies VHA-1 as **VHA-c1**, a V0 c proteolipid homologous to human ATP6V0C and yeast Vma3. This agrees with the supplied InterPro/Pfam assignments ATPase_proteolipid_c-like, ATPase_proteolipid_c, eukaryotic ATPase proteolipid C, F/V-ATPase C-subunit superfamily, and ATP-synt_C. (allan2005genomewidesurveyof pages 7-8)
4. **Ambiguity control:** literature about VHA “a,” “A,” “C,” or other numbered worm subunits was not treated as direct VHA-1 evidence. In particular, ATP6V0A proteins are large V0 a subunits, and VHA-13/ATP6V1A is a catalytic V1 subunit; neither is Q21898.

The historical literature describes three *C. elegans vha* genes encoding V-ATPase proteolipids, making paralog-specific nomenclature important. The available evidence nevertheless consistently places R10E11.8/*vha-1* in the c1 proteolipid class rather than in another V-ATPase subunit family. (allan2005genomewidesurveyof pages 7-8, syntichakiUnknownyearsupplementaldatathe pages 2-3)

## 2. Primary molecular function

### 2.1 Role in the V-ATPase

V-ATPase is a rotary proton pump comprising a soluble V1 ATPase and membrane-embedded V0 proton-translocation sector. VHA-1 belongs to V0 and forms part of the oligomeric proteolipid c-ring. By contrast, ATP is hydrolyzed at three catalytic sites located at alternating A/B interfaces in the V1 A3B3 head. Rotation is transmitted through the central rotor to the c-ring, which turns against stationary subunit a. Human V-ATPase is approximately 1 MDa, and structural analyses resolve three principal rotational states separated by approximately 120°. (oot2024humanvatpasefunction pages 1-3)

Thus, VHA-1 should be annotated as a **proton-translocating structural/mechanical component of an ATP-driven transporter**, not as an independently active ATPase. There is no organic-solute specificity analogous to that of a metabolite transporter: the transported substrate is the proton, **H+**. Its broader structural role is to supply proton-binding sites and the rotating membrane ring that converts V1-generated torque into vectorial proton movement. (kishikawa2024rotarymechanismof pages 1-3, oot2024humanvatpasefunction pages 1-3)

### 2.2 Proton-transfer mechanism

The best recent mechanistic evidence comes from a 2.8-Å cryo-EM structure and molecular-dynamics analysis of the *Thermus thermophilus* V/A-ATPase V0 motor, published in *Nature Communications* in November 2024: https://doi.org/10.1038/s41467-024-53504-x. In that system, protonation of the conserved acidic residue on a c subunit—Glu63 in the studied protein—alters its interaction with a conserved stator arginine and biases c-ring rotation; an unprotonated glutamate can maintain a salt bridge that blocks movement. The c-ring sequentially accepts and releases protons through spatially separated subunit-a half-channels. (kishikawa2024rotarymechanismof pages 1-3)

This is powerful **family-level inference**, not a structure of Q21898. The precise residue number, topology, c-ring stoichiometry, and proton/ATP coupling ratio should therefore not be transferred directly to worm VHA-1 without sequence-specific or structural confirmation. The conserved proteolipid architecture nevertheless makes an acidic proton-binding residue and multipass membrane topology highly likely.

A complementary 2024 human study describes a V0 sector containing a c9/c″ proteolipid ring and shows how ATP hydrolysis rotates the D/F/d rotor and c-ring past subunit-a half-channels. That work also emphasizes reversible V1–V0 disassembly as a major regulatory mechanism. Published July 2024 in *Structure*: https://doi.org/10.1016/j.str.2024.03.009. (oot2024humanvatpasefunction pages 1-3, oot2024humanvatpasefunction pages 8-10)

## 3. Cellular and tissue localization

### 3.1 Excretory system

Direct expression evidence places *vha-1* in the single H-shaped **excretory cell** during both larval and adult stages. This cell constitutes a major part of the worm’s renal/osmoregulatory tubular system. The expression pattern is consistent with V-ATPase-dependent control of luminal or vesicular pH and membrane traffic, although the cited study’s functional RNAi tests concentrated on other V-ATPase subunits; an excretory-canal phenotype cannot therefore be assigned uniquely to VHA-1 from that paper. Hahn-Windgassen and Van Gilst, *PLoS Genetics*, July 2009: https://doi.org/10.1371/journal.pgen.1000553. (hahnwindgassen2009thecaenorhabditiselegans pages 6-8)

### 3.2 Intestinal apical membrane and trafficking compartments

Intestinal RNAi and imaging place VHA-1 function in the **apical brush-border/microvillar system and associated apical endosomes**. V0-ATPase signal colocalized with ERM-1/ezrin in microvilli, and *vha-1* knockdown reduced apical VHA-6::mCherry signal, consistent with destabilization or defective positioning of V0 complexes. However, because these experiments did not image an endogenously tagged VHA-1 protein, they define the functional compartment more securely than the exact steady-state distribution of Q21898 itself. (bidaudmeynard2018thelossof pages 1-6, bidaudmeynard2018thelossof pages 15-18)

### 3.3 Lysosomes and endolysosomal membranes

A 2024 adult-worm Lyso-IP study detected VHA-1 among lysosomal V0 components, supporting a VHA-1-containing pool on lysosomal membranes. The proteomic analysis used four biological replicates and an enrichment criterion of at least tenfold over flow-through; 216 proteins were more than twofold enriched over non-tagged controls. The authors inferred that both free V1 and V0-associated complexes occur at lysosomes under well-fed conditions. Yu et al., *eLife*, January 2024: https://doi.org/10.7554/eLife.85214. (yu2024organelleproteomicprofiling pages 5-6)

This evidence supports lysosomal association but does not show that VHA-1 is lysosome-exclusive or directly measure Q21898-dependent proton flux. Given the conserved function of assembled V-ATPase, its expected local reaction is effectively:

**ATP hydrolysis in V1 → c-ring rotation in V0 → H+ movement from cytosol to organelle lumen.**

The resulting acidic lumen enables hydrolase activity, cargo degradation, endosomal maturation, autophagic flux, and ion-coupled transport. These downstream functions are well established for V-ATPase complexes but should be described as complex-level consequences rather than separately catalyzed reactions of VHA-1. (oot2024humanvatpasefunction pages 1-3, falace2024vatpasedysfunctionin pages 6-8)

## 4. Direct biological-process evidence

### 4.1 Apical trafficking and epithelial polarity

The strongest gene-specific functional evidence comes from an intestinal RNAi screen and subsequent imaging. The screen examined **408 conserved trafficking and cytoskeletal genes** and identified ten V-ATPase subunits, including *vha-1*. After *vha-1* depletion, apical markers such as ERM-1/ezrin and CDC-42 were redistributed basolaterally or into the cytoplasm. Across the tested V0/V1 knockdown series, apical-to-cytoplasmic ratios for ERM-1, PAR-6, and PKC-3 declined by approximately **15–40%**; that range describes the series and is not a VHA-1-only effect size. (bidaudmeynard2018thelossof pages 1-6)

Seventy-two-hour *vha-1* RNAi caused reduced apical PAR-6, PKC-3, and ERM-1; cytoplasmic SNAP-29; reduced RAB-11 signal; accumulation of LMP-1, RAB-7, and RAB-10 compartments; lucent vesicles and mixed organelles; microvillus atrophy; and intracellular microvillus inclusions. These phenotypes show that VHA-1 is required to maintain the polarized absorptive membrane, not merely bulk organelle acidity. (bidaudmeynard2018thelossof pages 50-54, bidaudmeynard2018thelossof pages 30-32)

Mechanistically, V0-ATPase supports a late apical trafficking step involving **RAB-11-positive recycling endosomes and the SNARE SNAP-29**. VHA-1 depletion perturbed their apical organization and selectively disrupted brush-border and CDC-42/PAR components, whereas several transmembrane proteins—PEPT-1, PGP-1, and SLCF-1—were comparatively unaffected. This selectivity argues against a nonspecific collapse of all membrane traffic. Physical binding of VHA-1 itself to RAB-11 or SNAP-29 was not shown, so VHA-1 should be placed upstream or within the V0-dependent trafficking machinery rather than annotated as a direct RAB-11/SNAP-29 adaptor. (bidaudmeynard2018thelossof pages 15-18)

The peer-reviewed final report was Bidaud-Meynard et al., *Development*, January 2019, DOI https://doi.org/10.1242/dev.174508; the retrieved detailed evidence also came from its September 2018 preprint, https://doi.org/10.1101/412122. (bidaudmeynard2018thelossof pages 50-54, bidaudmeynard2018thelossof pages 1-6)

### 4.2 Lysosomal proteostasis and muscle aging

A 2021 study identified *vha-1* among predicted miR-1-regulated V-ATPase genes and tested it in a muscle-thrashing assay under polyglutamine proteotoxic stress. VHA-1 was among the likely mediators of improved motility in the *mir-1* mutant background. However, detailed target validation centered on VHA-13/ATP6V1A rather than VHA-1; consequently, direct miR-1 binding to the *vha-1* 3′ UTR and a VHA-1-specific acidification mechanism remain unproven. Schiffer et al., *eLife*, July 2021: https://doi.org/10.7554/eLife.66768. (schiffer2021mir1coordinatelyregulates pages 8-12)

### 4.3 Signaling implications

V-ATPase-dependent lysosomal pH and assembly state are connected to nutrient sensing and mTOR/TORC1 signaling. Modern mammalian work places V-ATPase in lysosomal mTOR recruitment and amino-acid-sensitive regulation, while worm studies establish broad V-ATPase involvement in stress and proteostasis pathways. These are important pathway contexts, but they should not be interpreted as proof that VHA-1 alone is a receptor or signaling enzyme. (falace2024vatpasedysfunctionin pages 6-8, oot2024humanvatpasefunction pages 8-10)

The available literature therefore supports three mechanistically distinct but connected levels of VHA-1 action:

- **Direct molecular level:** proton-binding c-ring rotor component.
- **Organelle level:** enables endosomal/lysosomal and specialized membrane acidification.
- **Cell-biological level:** supports RAB-11/SNAP-29-dependent apical traffic, brush-border integrity, and epithelial polarity.

## 5. Recent developments, 2023–2024

Direct, mechanistically deep 2023–2024 studies devoted specifically to worm VHA-1 are sparse. The most relevant advances are:

1. **Worm lysosomal proteomics (January 2024):** VHA-1 was detected in lysosome-associated V0 assemblies, embedding the protein in a tissue- and state-dependent lysosomal proteome rather than treating lysosomes as uniform organelles. (yu2024organelleproteomicprofiling pages 5-6)
2. **High-resolution rotary mechanism (November 2024):** a 2.8-Å V0 structure and simulations provided an updated physical model in which asymmetric protonation of c-ring glutamates and interaction with subunit-a arginine bias ring rotation. This substantially strengthens the mechanistic interpretation of VHA-1’s conserved acidic site, although it is not a worm structure. (kishikawa2024rotarymechanismof pages 1-3)
3. **Human enzyme regulation (July 2024):** purified human V-ATPase was shown to be positively or negatively regulated by TLDc proteins. NCOA7’s TLDc domain produced approximately 50% inhibition after overnight incubation at a 75-fold molar excess, while mEAK7 activated the enzyme; 2 mM ATP increased inhibition by several TLDc proteins by about 20%. These findings illustrate dynamic control of rotary catalysis and assembly but remain cross-species, whole-complex evidence. (oot2024humanvatpasefunction pages 5-7)
4. **Native-vesicle structure (April/July 2024):** cryo-EM of V-ATPase in approximately 40-nm mammalian synaptic vesicles visualized the native pump and its role in generating the proton gradient used for neurotransmitter loading. This provides a compelling real-membrane implementation of the same conserved c-ring mechanism. (coupland2024highresolutioncryoem pages 1-3)

## 6. Applications and real-world implementations

### Disease modeling

VHA-1-depleted worm intestine phenocopies central features of **microvillus inclusion disease**, including brush-border atrophy, polarity loss, trafficking defects, and intracellular microvillus inclusions. This makes *C. elegans* V0 perturbation an in vivo system for dissecting enterocyte polarity and testing modifiers. Cholesterol supplementation partially rescued structural and polarity defects in the experimental model, although this does not establish a clinical treatment. (bidaudmeynard2018thelossof pages 50-54, bidaudmeynard2018thelossof pages 15-18)

### Lysosomal and neurodegenerative biology

Human genetic and model-organism evidence links V-ATPase impairment to defective lysosomal acidification, reduced cathepsin activity, autophagy disruption, neuronal dysfunction, and altered mTORC1 activity. VHA-1 is therefore useful as a conserved genetic handle for studying how proton-pump failure affects proteostasis. These disease associations concern V-ATPase dysfunction broadly and must not be interpreted as evidence that worm Q21898 itself causes a human disorder. (falace2024vatpasedysfunctionin pages 6-8)

### Transport and pharmacology

V-ATPases are experimentally manipulated using inhibitors such as bafilomycin A1 to test whether a phenotype depends on organelle acidification. Because the c-ring is indispensable to proton translocation, VHA-1 knockdown offers a genetic counterpart to pump inhibition in worms. However, its deep conservation and broad physiological requirement predict substantial toxicity from nonspecific inhibition; contemporary therapeutic strategies generally seek tissue-, isoform-, assembly-, or regulator-selective modulation rather than indiscriminate c-ring blockade. The 2024 identification of TLDc proteins as nanomolar-range turnover modulators illustrates this shift toward regulatory interfaces. (falace2024vatpasedysfunctionin pages 6-8, oot2024humanvatpasefunction pages 5-7)

## 7. Evidence-quality assessment and unresolved questions

The **highest-confidence annotation** is that VHA-1/Q21898 is the V0 c1 proteolipid rotor subunit required for ATP-coupled proton transport. Direct worm evidence firmly supports excretory-cell expression, lysosomal association, and a requirement for intestinal apical trafficking and brush-border polarity. (hahnwindgassen2009thecaenorhabditiselegans pages 6-8, allan2005genomewidesurveyof pages 7-8, bidaudmeynard2018thelossof pages 15-18, yu2024organelleproteomicprofiling pages 5-6)

Important unresolved points are:

- no retrieved study purified Q21898 and measured proton flux, ATP/H+ coupling, or inhibitor sensitivity;
- the exact Q21898 membrane topology and proton-binding residue number were not experimentally established in the retrieved sources;
- worm VHA-1 c-ring stoichiometry is not directly known from these papers;
- endogenous VHA-1 localization at single-organelle resolution remains less secure than RNAi and complex-level reporter evidence;
- some trafficking phenotypes may reflect V0-dependent membrane-fusion/scaffolding functions in addition to loss of acidification;
- detailed 2023–2024 gene-specific work is limited, so current mechanistic interpretation necessarily combines direct worm genetics with conserved structural evidence.

## Final annotation

**VHA-1 is an integral V0 proteolipid c1 subunit of the *C. elegans* vacuolar H+-ATPase. Multiple VHA-1 molecules contribute to the membrane rotor ring that accepts and releases H+ while rotating against subunit a, coupling ATP hydrolysis in V1 to proton pumping. VHA-1-containing complexes function on lysosomal/endosomal and specialized epithelial membranes. In worms, *vha-1* is expressed in the excretory cell and is directly required in the intestine for RAB-11/SNAP-29-associated apical trafficking, maintenance of the microvillar brush border, and apicobasal polarity.** This conclusion is strongly supported at the functional-class level, while residue-level mechanism and transport stoichiometry remain inferred from conserved V-ATPase structures rather than measured directly for Q21898. (hahnwindgassen2009thecaenorhabditiselegans pages 6-8, allan2005genomewidesurveyof pages 7-8, bidaudmeynard2018thelossof pages 15-18, yu2024organelleproteomicprofiling pages 5-6, kishikawa2024rotarymechanismof pages 1-3, oot2024humanvatpasefunction pages 1-3)

References

1. (allan2005genomewidesurveyof pages 7-8): Adrian K. Allan, Juan Du, Shireen A. Davies, and Julian A. T. Dow. Genome-wide survey of v-atpase genes in drosophila reveals a conserved renal phenotype for lethal alleles. Physiological genomics, 22 2:128-38, Jul 2005. URL: https://doi.org/10.1152/physiolgenomics.00233.2004, doi:10.1152/physiolgenomics.00233.2004. This article has 165 citations and is from a peer-reviewed journal.

2. (syntichakiUnknownyearsupplementaldatathe pages 2-3): P Syntichaki, C Samara, and N Tavernarakis. Supplemental data the vacuolar h-atpase mediates intracellular acidification required for neurodegeneration in c. elegans. Unknown journal, Unknown year.

3. (bidaudmeynard2018thelossof pages 1-6): Aurélien Bidaud-Meynard, Ophélie Nicolle, Markus Heck, and Grégoire Michaux. The loss of v0-atpase induces microvillus inclusion-like disease in c. elegans. bioRxiv, Sep 2018. URL: https://doi.org/10.1101/412122, doi:10.1101/412122. This article has 1 citations.

4. (kishikawa2024rotarymechanismof pages 1-3): Jun-ichi Kishikawa, Yui Nishida, Atsuki Nakano, Takayuki Kato, Kaoru Mitsuoka, Kei-ichi Okazaki, and Ken Yokoyama. Rotary mechanism of the prokaryotic vo motor driven by proton motive force. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-53504-x, doi:10.1038/s41467-024-53504-x. This article has 10 citations and is from a highest quality peer-reviewed journal.

5. (oot2024humanvatpasefunction pages 1-3): Rebecca A. Oot and Stephan Wilkens. Human v-atpase function is positively and negatively regulated by tldc proteins. Jul 2024. URL: https://doi.org/10.1016/j.str.2024.03.009, doi:10.1016/j.str.2024.03.009. This article has 23 citations and is from a domain leading peer-reviewed journal.

6. (hahnwindgassen2009thecaenorhabditiselegans pages 6-8): Annett Hahn-Windgassen and Marc R. Van Gilst. The caenorhabditis elegans hnf4α homolog, nhr-31, mediates excretory tube growth and function through coordinate regulation of the vacuolar atpase. PLoS Genetics, 5:e1000553, Jul 2009. URL: https://doi.org/10.1371/journal.pgen.1000553, doi:10.1371/journal.pgen.1000553. This article has 62 citations and is from a domain leading peer-reviewed journal.

7. (bidaudmeynard2018thelossof pages 15-18): Aurélien Bidaud-Meynard, Ophélie Nicolle, Markus Heck, and Grégoire Michaux. The loss of v0-atpase induces microvillus inclusion-like disease in c. elegans. bioRxiv, Sep 2018. URL: https://doi.org/10.1101/412122, doi:10.1101/412122. This article has 1 citations.

8. (bidaudmeynard2018thelossof pages 50-54): Aurélien Bidaud-Meynard, Ophélie Nicolle, Markus Heck, and Grégoire Michaux. The loss of v0-atpase induces microvillus inclusion-like disease in c. elegans. bioRxiv, Sep 2018. URL: https://doi.org/10.1101/412122, doi:10.1101/412122. This article has 1 citations.

9. (bidaudmeynard2018thelossof pages 30-32): Aurélien Bidaud-Meynard, Ophélie Nicolle, Markus Heck, and Grégoire Michaux. The loss of v0-atpase induces microvillus inclusion-like disease in c. elegans. bioRxiv, Sep 2018. URL: https://doi.org/10.1101/412122, doi:10.1101/412122. This article has 1 citations.

10. (yu2024organelleproteomicprofiling pages 5-6): Yong Yu, Shihong M. Gao, Youchen Guan, Pei-Wen Hu, Qinghao Zhang, Jiaming Liu, Bentian Jing, Qian Zhao, David M Sabatini, Monther Abu-Remaileh, Sung Yun Jung, and Meng C. Wang. Organelle proteomic profiling reveals lysosomal heterogeneity in association with longevity. eLife, Jan 2024. URL: https://doi.org/10.7554/elife.85214, doi:10.7554/elife.85214. This article has 45 citations and is from a domain leading peer-reviewed journal.

11. (schiffer2021mir1coordinatelyregulates pages 8-12): Isabelle Schiffer, Birgit Gerisch, Kazuto Kawamura, Raymond Laboy, Jennifer Hewitt, Martin S. Denzel, Marcelo A. Mori, Siva Vanapalli, Yidong Shen, Orsolya Symmons, and Adam Antebi. Mir-1 coordinately regulates lysosomal v-atpase and biogenesis to affect muscle contractility upon proteotoxic challenge during ageing. bioRxiv, Jan 2021. URL: https://doi.org/10.1101/2021.01.21.427623, doi:10.1101/2021.01.21.427623. This article has 0 citations.

12. (oot2024humanvatpasefunction pages 8-10): Rebecca A. Oot and Stephan Wilkens. Human v-atpase function is positively and negatively regulated by tldc proteins. Jul 2024. URL: https://doi.org/10.1016/j.str.2024.03.009, doi:10.1016/j.str.2024.03.009. This article has 23 citations and is from a domain leading peer-reviewed journal.

13. (falace2024vatpasedysfunctionin pages 6-8): Antonio Falace, Greta Volpedo, Marcello Scala, Federico Zara, Pasquale Striano, and Anna Fassio. V-atpase dysfunction in the brain: genetic insights and therapeutic opportunities. Cells, 13:1441, Aug 2024. URL: https://doi.org/10.3390/cells13171441, doi:10.3390/cells13171441. This article has 30 citations.

14. (oot2024humanvatpasefunction pages 5-7): Rebecca A. Oot and Stephan Wilkens. Human v-atpase function is positively and negatively regulated by tldc proteins. Jul 2024. URL: https://doi.org/10.1016/j.str.2024.03.009, doi:10.1016/j.str.2024.03.009. This article has 23 citations and is from a domain leading peer-reviewed journal.

15. (coupland2024highresolutioncryoem pages 1-3): Claire E. Coupland, Ryan Karimi, Stephanie A. Bueler, Yingke Liang, Gautier M. Courbon, Justin M. Di Trani, Cassandra J. Wong, Rayan Saghian, Ji-Young Youn, Lu-Yang Wang, and John L. Rubinstein. High resolution cryo-em of v-atpase in native synaptic vesicles. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.01.587493, doi:10.1101/2024.04.01.587493. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](vha-1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. kishikawa2024rotarymechanismof pages 1-3
2. hahnwindgassen2009thecaenorhabditiselegans pages 6-8
3. bidaudmeynard2018thelossof pages 1-6
4. yu2024organelleproteomicprofiling pages 5-6
5. allan2005genomewidesurveyof pages 7-8
6. oot2024humanvatpasefunction pages 1-3
7. bidaudmeynard2018thelossof pages 15-18
8. oot2024humanvatpasefunction pages 5-7
9. coupland2024highresolutioncryoem pages 1-3
10. falace2024vatpasedysfunctionin pages 6-8
11. bidaudmeynard2018thelossof pages 50-54
12. bidaudmeynard2018thelossof pages 30-32
13. oot2024humanvatpasefunction pages 8-10
14. https://doi.org/10.1038/s41467-024-53504-x.
15. https://doi.org/10.1016/j.str.2024.03.009.
16. https://doi.org/10.1371/journal.pgen.1000553.
17. https://doi.org/10.7554/eLife.85214.
18. https://doi.org/10.1242/dev.174508;
19. https://doi.org/10.1101/412122.
20. https://doi.org/10.7554/eLife.66768.
21. https://doi.org/10.1152/physiolgenomics.00233.2004,
22. https://doi.org/10.1101/412122,
23. https://doi.org/10.1038/s41467-024-53504-x,
24. https://doi.org/10.1016/j.str.2024.03.009,
25. https://doi.org/10.1371/journal.pgen.1000553,
26. https://doi.org/10.7554/elife.85214,
27. https://doi.org/10.1101/2021.01.21.427623,
28. https://doi.org/10.3390/cells13171441,
29. https://doi.org/10.1101/2024.04.01.587493,