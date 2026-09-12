---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T13:54:02.209175'
end_time: '2026-09-08T14:04:48.548185'
duration_seconds: 646.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: VAPA
  gene_symbol: VAPA
  uniprot_accession: Q9P0L0
  protein_description: 'RecName: Full=Vesicle-associated membrane protein-associated
    protein A {ECO:0000305}; Short=VAMP-A; Short=VAMP-associated protein A; Short=VAP-A;
    AltName: Full=33 kDa VAMP-associated protein {ECO:0000303|Ref.2}; Short=VAP-33
    {ECO:0000303|PubMed:10523508, ECO:0000303|PubMed:9657962};'
  gene_info: Name=VAPA {ECO:0000312|HGNC:HGNC:12648}; Synonyms=VAP33;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the VAMP-associated protein (VAP) (TC 9.B.17)
  protein_domains: Ig-like_fold. (IPR013783); MSP_dom. (IPR000535); PapD-like_sf.
    (IPR008962); VAP. (IPR016763); Motile_Sperm (PF00635)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: VAPA-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9P0L0
- **Protein Description:** RecName: Full=Vesicle-associated membrane protein-associated protein A {ECO:0000305}; Short=VAMP-A; Short=VAMP-associated protein A; Short=VAP-A; AltName: Full=33 kDa VAMP-associated protein {ECO:0000303|Ref.2}; Short=VAP-33 {ECO:0000303|PubMed:10523508, ECO:0000303|PubMed:9657962};
- **Gene Information:** Name=VAPA {ECO:0000312|HGNC:HGNC:12648}; Synonyms=VAP33;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the VAMP-associated protein (VAP) (TC 9.B.17)
- **Key Domains:** Ig-like_fold. (IPR013783); MSP_dom. (IPR000535); PapD-like_sf. (IPR008962); VAP. (IPR016763); Motile_Sperm (PF00635)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VAPA" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VAPA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VAPA** (gene ID: VAPA, UniProt: Q9P0L0) in human.

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
- **UniProt Accession:** Q9P0L0
- **Protein Description:** RecName: Full=Vesicle-associated membrane protein-associated protein A {ECO:0000305}; Short=VAMP-A; Short=VAMP-associated protein A; Short=VAP-A; AltName: Full=33 kDa VAMP-associated protein {ECO:0000303|Ref.2}; Short=VAP-33 {ECO:0000303|PubMed:10523508, ECO:0000303|PubMed:9657962};
- **Gene Information:** Name=VAPA {ECO:0000312|HGNC:HGNC:12648}; Synonyms=VAP33;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the VAMP-associated protein (VAP) (TC 9.B.17)
- **Key Domains:** Ig-like_fold. (IPR013783); MSP_dom. (IPR000535); PapD-like_sf. (IPR008962); VAP. (IPR016763); Motile_Sperm (PF00635)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VAPA" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VAPA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VAPA** (gene ID: VAPA, UniProt: Q9P0L0) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human VAPA (UniProt Q9P0L0): Functional-Annotation Research Report

## Executive summary

The requested target is correctly identified. **Human VAPA** encodes vesicle-associated membrane protein-associated protein A (**VAP-A**, historically **hVAP-33/VAP33**), corresponding to **UniProt Q9P0L0**. It is not an enzyme or solute transporter. Its primary function is to act as a **tail-anchored endoplasmic-reticulum (ER) receptor, scaffold, and membrane-contact-site tether**: its cytosolic MSP domain binds FFAT-family motifs in lipid-transfer proteins and other effectors, thereby recruiting them to the ER and bridging the ER to Golgi, plasma-membrane, endosomal, and other organelle membranes. The actual transport substrates—such as ceramide, cholesterol, phosphatidylserine (PS), or phosphatidylinositol-4-phosphate (PI4P)—are carried by recruited lipid-transfer proteins, not through VAPA itself. (kodama2025beyondstatictethering pages 4-6, kodama2025beyondstatictethering pages 1-2, levine2025updateonvap pages 1-2, james2021theinteractomeof pages 1-2)

The best-supported VAPA-specific functions are: (1) docking FFAT-containing proteins at the cytoplasmic ER surface; (2) organizing ER–plasma-membrane contacts near focal adhesions and supporting local phosphoinositide homeostasis and adhesion turnover; (3) forming an ER-side docking site for ORP1L-dependent cholesterol transfer to endosomes; and (4) recruiting a pool of LSG1 to the ER. Many other commonly cited functions—especially ER–Golgi lipid exchange, autophagosome biogenesis, and neuronal mitochondrial stabilization—are supported by combined VAPA/VAPB perturbation and should be annotated as partly redundant rather than uniquely VAPA-specific. (james2021theinteractomeof pages 7-9, siegfried2024theertether pages 9-11, bapat2024vapspatiallystabilizes pages 8-10, sutjita2024theribosomeassembly pages 5-8, peretti2008coordinatedlipidtransfer pages 1-2, eden2016annexina1tethers pages 1-4)

## 1. Mandatory identity verification

### 1.1 Gene, protein, and organism

The literature explicitly maps **human VAPA to UniProt Q9P0L0** and identifies the protein historically as **hVAP-33**. VAPA is one of the principal human VAMP-associated proteins, alongside the paralog VAPB; it should not be confused with similarly named VAP proteins from *Aplysia*, yeast Scs2/Scs22, or the human MSP-domain proteins MOSPD1–3. No conflicting same-symbol gene was identified in the retrieved human literature. (james2021theinteractomeof pages 1-2, kodama2025beyondstatictethering pages 4-6, kodama2025beyondstatictethering pages 1-2, levine2025updateonvap pages 1-2)

### 1.2 Family and domain consistency

The literature agrees with the supplied InterPro/Pfam annotations. Human VAPA contains:

- an N-terminal **major sperm protein domain (MSP domain)**, approximately residues 14–131, forming an immunoglobulin-like β-sandwich;
- an intrinsically disordered linker;
- a predicted **coiled-coil region**, approximately residues 169–205;
- a second short disordered/juxtamembrane segment; and
- one C-terminal **transmembrane helix**, with predictions around residues 224–247. (james2021theinteractomeof pages 1-2, kodama2025beyondstatictethering pages 4-6, levine2025updateonvap pages 2-4)

Thus, the supplied Ig-like-fold, MSP, PapD-like-superfamily, VAP-family, and Motile_Sperm-domain calls are mutually consistent. The C-terminal helix makes VAPA a post-translationally inserted, tail-anchored integral membrane protein. Nearly the entire N-terminal portion—including the ligand-binding MSP domain—faces the cytosol, while only a very short tail extends into the ER lumen. Coiled-coil and transmembrane interactions support homo- and hetero-oligomerization with VAP-family proteins. (james2021theinteractomeof pages 1-2, levine2025updateonvap pages 2-4, kodama2025beyondstatictethering pages 1-2)

## 2. Primary molecular function

### 2.1 A receptor and adaptor, not a catalytic protein

VAPA’s core biochemical activity is **protein recognition and spatial recruitment**. Its MSP domain binds short linear motifs termed **FFAT motifs**—“two phenylalanines in an acidic tract”—and related FFAT-like, FFNT, and phosphorylation-dependent motifs. This places soluble or peripheral proteins on the cytoplasmic surface of the ER. When the recruited protein is simultaneously attached to another organelle, VAPA becomes the ER-side component of an inter-organelle bridge. (levine2025updateonvap pages 1-2, james2021theinteractomeof pages 1-2)

Accordingly, VAPA has no known catalytic reaction, pore, or transported substrate of its own. A more precise annotation than “lipid transporter” is **ER membrane-contact-site receptor/tether for lipid-transfer and signaling proteins**. CERT transports ceramide; OSBP-family proteins transport or exchange sterols and phosphoinositides; ORP9/ORP11 exchange PS and PI4P. VAPA supplies ER anchoring and favorable geometry for these reactions. (kodama2025beyondstatictethering pages 20-22, kodama2025beyondstatictethering pages 19-20, wakana2015cartsbiogenesisrequires pages 1-4, peretti2008coordinatedlipidtransfer pages 1-2)

### 2.2 Dynamic rather than rigid tethering

Current structural interpretation treats VAP proteins as dynamic, multivalent scaffolds rather than static rods. Flexible disordered regions allow the MSP domain to sample the cytosolic space, capture FFAT-bearing proteins, and transiently draw an opposing membrane toward the ER. Coiled-coil and transmembrane oligomerization can increase avidity and organize larger interaction assemblies. Proposed Brownian-ratchet-like capture does not require VAPA to hydrolyze ATP. This mechanistic model is plausible and structurally informed, although many whole-molecule conformations remain predictions rather than high-resolution structures of intact membrane-embedded VAPA. (kodama2025beyondstatictethering pages 12-14, kodama2025beyondstatictethering pages 20-22, kodama2025beyondstatictethering pages 19-20)

## 3. Cellular localization

VAPA is broadly expressed and resides predominantly throughout the **ER membrane**, including specialized cortical and perinuclear ER subdomains. Its MSP domain is exposed on the cytoplasmic ER face, where it can recognize proteins on the Golgi, plasma membrane, endosomes, lipid droplets, mitochondria, or peroxisomes. Contact sites generally bring bilayers within tens of nanometres without fusion; representative reported separations are approximately 3–15 nm for ER–endosome, 6–15 nm for ER–mitochondria, and 19–22 nm for ER–plasma-membrane contacts. These dimensions are contact-site context rather than invariant properties of VAPA complexes. (levine2025updateonvap pages 2-4, kodama2025beyondstatictethering pages 19-20, james2021theinteractomeof pages 1-2)

VAPA has occasionally been detected outside its canonical ER topology, but the well-established functional pool is the cytoplasm-facing ER protein. Annotation should therefore prioritize **cytoplasmic face of the ER and ER-derived membrane-contact sites**. (kodama2025beyondstatictethering pages 1-2, kodama2025beyondstatictethering pages 2-4)

## 4. Pathways and biological processes

### 4.1 ER–Golgi lipid exchange and secretory trafficking

At ER–Golgi contacts, VAPA/VAPB bind FFAT motifs in **CERT**, **OSBP**, **Nir2**, and other OSBP-related proteins. CERT transfers ceramide from the ER to trans-Golgi membranes, where sphingomyelin synthase uses ceramide and phosphatidylcholine to generate sphingomyelin and diacylglycerol. OSBP transfers cholesterol toward the Golgi while counter-transporting PI4P to the ER, where SAC1 hydrolyses PI4P. VAPA therefore couples ER anchoring to lipid gradients and Golgi membrane identity without directly carrying these lipids. (wakana2015cartsbiogenesisrequires pages 1-4, peretti2008coordinatedlipidtransfer pages 1-2)

Combined VAPA/VAPB RNA interference reduced Golgi PI4P, diacylglycerol, and sphingomyelin and substantially inhibited Golgi-mediated transport. In a later HeLa-cell study, approximately 80% depletion of both isoforms reduced secretion through CARTS by more than 50%; VAP depletion lowered TGN diacylglycerol and impaired transport-carrier formation. These are strong mechanistic data for the VAP family, but they do not establish that VAPA alone is indispensable because both paralogs were depleted. (wakana2015cartsbiogenesisrequires pages 1-4, peretti2008coordinatedlipidtransfer pages 1-2)

A 2024 eLife study extended this pathway by screening **90 intracellular lipid-transfer genes**. ORP9–ORP11 was shown to exchange PS from ER to trans-Golgi for PI4P in the reverse direction; knockout lowered Golgi PS, increased Golgi PI4P, and impaired local sphingomyelin production. In vitro assays demonstrated transfer of both lipids and enhanced transfer in a reconstructed VAP–ORP contact complex. However, the reconstitution used **VAPB**, so it establishes the mechanistic compatibility of a VAP anchor but not a VAPA-specific ORP9–ORP11 function. (cabukusta2024theorp9orp11dimer pages 1-2, cabukusta2024theorp9orp11dimer pages 9-11)

### 4.2 ER–plasma-membrane contacts, phosphoinositides, and focal adhesions

The clearest recent VAPA-specific advance is the 2024 eLife study in migrating Caco2 epithelial cells. VAPA knockout disrupted collective and individual migration, actin organization, protrusive activity, and focal-adhesion dynamics. VAPA maintained plasma-membrane PI4P/PI(4,5)P2 while Golgi and endosomal PI4P remained relatively unaffected, consistent with VAPB compensation at those other contacts. VAPA also stabilized ventral ER–plasma-membrane contacts adjacent to focal adhesions and supported microtubule-dependent adhesion disassembly. (siegfried2024theertether pages 11-12, siegfried2024theertether pages 1-2)

Quantitatively, **75%** of central focal adhesions in control cells were near an ER–PM-contact focus, compared with **30%** after VAPA knockout. Approximately half of the nearest signal peaks were separated by 50–150 nm. In control cells, **71.4%** of first contact-site arrivals occurred after adhesion assembly but before disassembly, typically during the preceding 10 minutes, and contacts persisted for about 6 minutes. The physical proximity could be rescued independently of the MSP domain, whereas regulation of adhesion dynamics required the MSP domain. This suggests two separable VAPA functions: an incompletely defined structural anchoring mechanism and FFAT-partner-dependent regulation, potentially involving Nir2 or ORP3. (siegfried2024theertether pages 9-11, siegfried2024theertether pages 11-12, siegfried2024theertether pages 12-13)

### 4.3 ER–endosome cholesterol transfer and EGFR signaling

At late or multivesicular endosomes, ER-localized VAPA binds the FFAT-containing sterol-transfer protein **ORP1L**. Annexin A1–S100A11 helps tether a subpopulation of EGFR-positive endosomes to the ER. Under low endosomal cholesterol, the VAPA–ORP1L interaction supports ER-derived cholesterol transport to endosomes, intraluminal-vesicle formation, and spatial attenuation of EGFR signaling before lysosomal degradation. This is direct evidence connecting VAPA-mediated contact organization to lipid transfer, membrane remodeling, and receptor signaling. (eden2016annexina1tethers pages 1-4)

The important mechanistic distinction is that annexin A1/S100A11 contributes physical tethering, ORP1L carries sterol, and VAPA provides the ER receptor. These membrane contacts are defined as close appositions below approximately 30 nm, not fusion intermediates. (eden2016annexina1tethers pages 1-4)

### 4.4 Mitochondrial organization, calcium, and neuronal plasticity

VAP-family proteins participate in ER–mitochondria communication, which affects lipid supply, calcium exchange, mitochondrial dynamics, and bioenergetics. Nevertheless, the canonical PTPIP51 tether and much of the disease literature are **VAPB-centered** and should not automatically be assigned to VAPA. (james2021theinteractomeof pages 7-9, kodama2025beyondstatictethering pages 2-4)

A 2024 Nature Communications study identified VAP proteins as ER/actin-associated stabilizers of dendritic mitochondrial compartments in primary hippocampal neurons. Combined Vapa/Vapb knockdown or knockout shortened and destabilized mitochondria and prevented sustained spine structural plasticity. VAP-dependent mitochondrial compartments supported an approximately **30-µm dendritic segment for about 60 minutes**. Reported control-versus-knockout differences during successive time intervals had p values of **8.77×10⁻⁴** and **3.36×10⁻⁴**. VAPA was enriched near both dendritic and axonal mitochondria, whereas VAPB showed stronger dendritic enrichment; because both genes were perturbed together for key functional assays, the causal phenotype remains family-level rather than uniquely VAPA-specific. (bapat2024vapspatiallystabilizes pages 8-10, bapat2024vapspatiallystabilizes pages 1-2)

### 4.5 Autophagy and protein homeostasis

VAPA and VAPB bind FFAT-bearing autophagy regulators including **FIP200 and ULK1**, supporting autophagosome biogenesis. The retrieved evidence is mainly VAPA/VAPB-combined and should be annotated as a shared VAP-family function. (james2021theinteractomeof pages 7-9)

VAP proteins also connect lipid homeostasis to ER proteostasis. VAP-family MSP domains interact with components of the unfolded-protein-response and ER-associated-degradation machinery and can inhibit degradation of misfolded ΔF508-CFTR in experimental systems. This suggests that competition among MSP-domain ligands can coordinate lipid sorting with protein quality control. However, much of the detailed perturbation work emphasizes VAPB or isolated VAP MSP domains; it supports VAPA plausibility but not a uniquely established VAPA-specific CF mechanism. (ernst2016vampassociatedproteins(vap) pages 1-2)

### 4.6 ER recruitment of LSG1: a recent non-lipid interaction

In 2024, human LSG1—a GTPase required for late 60S-ribosomal-subunit maturation—was shown to bind VAPA through a noncanonical FFAT-like region within LSG1 residues 254–324. Removing this region abolished VAPA association and ER localization of an LSG1 pool. Nevertheless, the mutant still rescued NMD3 recycling, and purified VAPA MSP domain did not measurably alter 60S/NMD3-stimulated LSG1 GTPase activity. Thus, VAPA spatially recruits or sequesters LSG1 but is not required for its established ribosome-maturation reaction. A proposed stress-regulated role involving phosphorylation of LSG1 T320 remains hypothetical. (sutjita2024theribosomeassembly pages 5-8, sutjita2024theribosomeassembly pages 1-2)

## 5. Interaction network and specificity

Proteomic studies report **more than 250 proteins** interacting with VAPA and/or VAPB, with approximately **50% shared** between the two paralogs. This breadth is consistent with VAPA being a modular interaction hub, but proximity-labeling and affinity-purification datasets differ substantially—only seven proteins were common to three summarized interactome studies—so individual high-throughput hits require orthogonal validation. (james2021theinteractomeof pages 7-9, james2021theinteractomeof pages 6-7)

Representative interaction classes include:

- CERT/STARD11: ER-to-Golgi ceramide transfer;
- OSBP and ORPs: sterol, PS, and phosphoinositide exchange;
- Nir/PITPNM proteins: phosphatidylinositol/phosphatidylcholine transfer and phosphoinositide control;
- ORP1L and STARD3: endosomal cholesterol handling;
- FIP200 and ULK1: autophagosome biogenesis; and
- LSG1: ER recruitment of a ribosome-assembly factor. (james2021theinteractomeof pages 7-9, sutjita2024theribosomeassembly pages 1-2, peretti2008coordinatedlipidtransfer pages 1-2, eden2016annexina1tethers pages 1-4)

ACBD5-mediated ER–peroxisome tethering and PTPIP51-mediated ER–mitochondria calcium signaling are often described as VAP functions, but the strongest retrieved evidence is specifically **VAPB-associated**. These should not be asserted as proven primary VAPA functions without direct VAPA substitution or selective-loss experiments. (james2021theinteractomeof pages 7-9, kodama2025beyondstatictethering pages 22-24)

The following evidence map summarizes both mechanism and attribution.

| Functional module | VAPA molecular role | Representative partner/contact site | Strongest evidence and quantitative result | Attribution/confidence |
|---|---|---|---|---|
| Identity and architecture | Non-catalytic, tail-anchored ER receptor/scaffold; cytosolic MSP β-sandwich recognizes FFAT-family motifs; coiled-coil and transmembrane regions support oligomerization | FFAT-bearing cytosolic proteins at the ER surface | Human VAPA is explicitly mapped to UniProt Q9P0L0 and historical hVAP-33; architecture comprises MSP residues approximately 14–131, disordered linkers, coiled-coil residues approximately 169–205, and a C-terminal transmembrane helix near residues 224–247 | **VAPA-specific; high confidence** |
| ER–Golgi lipid transfer | Recruits lipid-transfer proteins to the ER; VAPA is a docking/tethering component, not the lipid transporter | CERT, OSBP, Nir2, ORP9–ORP11; ER–trans-Golgi contacts | Combined VAPA/VAPB depletion reduced both paralogs by approximately 80%, lowered Golgi PI4P, DAG, and sphingomyelin, and reduced CARTS-dependent secretion by more than 50%. ORP9–ORP11 directly exchanges PS toward Golgi for PI4P toward ER, but its 2024 reconstitution used VAPB | **VAPA/VAPB redundant for cellular phenotype; VAPB-only reconstitution cannot establish VAPA-specific transport** |
| ER–PM contacts and focal adhesions | Stabilizes ventral ER–PM contacts near focal adhesions, maintains plasma-membrane phosphoinositides, and promotes microtubule-dependent adhesion disassembly | Candidate effectors Nir2 and ORP3; ER–PM–focal-adhesion interface | In migrating Caco2 cells, 75% of central focal adhesions were near an ER–PM-contact focus in controls versus 30% after VAPA knockout. Approximately 50% of nearest signal peaks were 50–150 nm apart; 71.4% of contact arrivals preceded adhesion disassembly and persisted about 6 min | **VAPA-specific; high confidence for localization/dynamics, moderate for proposed lipid-transfer effectors** |
| ER–endosome cholesterol and EGFR regulation | Provides the ER docking site for an endosomal sterol-transfer complex that supports intraluminal-vesicle formation and spatial termination of EGFR signaling | ORP1L–VAPA at Rab7/EGFR-positive multivesicular endosomes; annexin A1–S100A11 auxiliary tether | VAPA–ORP1L interaction was required for ER-derived cholesterol delivery to cholesterol-poor endosomes and for intraluminal-vesicle formation; contact-site membranes are apposed by less than 30 nm | **VAPA-specific interaction and functional requirement; high confidence** |
| Neuronal mitochondria and synaptic plasticity | Contributes to ER/actin-associated stabilization of mitochondrial compartments that provide local energetic support for dendritic plasticity | Dendritic and axonal mitochondria; ER–actin–mitochondria interface | Combined Vapa/Vapb depletion shortened and destabilized mitochondria and prevented sustained spine plasticity. VAP-dependent mitochondrial compartments supported an approximately 30-µm dendritic segment for about 60 min; control versus knockout differences yielded p values of 8.77×10⁻⁴ and 3.36×10⁻⁴ over successive time intervals | **VAPA/VAPB redundant perturbation; VAPA localization is broader, but a VAPA-only causal effect was not established** |
| Autophagy, proteostasis, and LSG1 | Recruits regulatory proteins to the ER and can spatially sequester clients without necessarily changing their catalytic activity | FIP200/ULK1; CFTR quality-control machinery; LSG1–VAPA at ER | VAPA/VAPB bind FIP200 and ULK1 in autophagosome biogenesis. VAP-family MSP domains modulate ΔF508-CFTR degradation. In 2024, VAPA bound LSG1 through residues 254–324 and localized a pool to ER, but disrupting binding did not impair NMD3 recycling or alter LSG1 GTPase activity | **Mixed: autophagy and CFTR evidence largely VAPA/VAPB family-level; LSG1 binding is VAPA-specific but dispensable for known LSG1 activity** |
| Translational relevance | Host-cell interaction hub whose contact-site machinery can be co-opted or disrupted in disease models; currently a mechanistic target rather than a validated clinical target | Pathogen vacuoles, CFTR proteostasis, cancer-cell migration, neuronal energy organization | More than 250 proteins have been reported to interact with VAPA and/or VAPB, with approximately 50% shared. Experimental relevance spans pathogen lipid acquisition, cystic-fibrosis proteostasis, epithelial migration, and synaptic plasticity, but no selective VAPA-directed approved therapy or validated clinical biomarker is established | **Biological relevance high; clinical actionability currently low to exploratory; avoid assigning VAPB-specific ALS mechanisms directly to VAPA** |


*Table: A compact evidence map distinguishing VAPA-specific functions from redundant VAPA/VAPB biology and findings attributable only to VAPB. It emphasizes VAPA’s primary role as an ER docking scaffold rather than a lipid transporter or enzyme.*

## 6. Recent developments, applications, and real-world relevance

### 6.1 Major 2023–2024 advances

The strongest VAPA-specific 2024 advance is the demonstration that ER–PM contacts are dynamically anchored to focal adhesions and participate in migration-associated phosphoinositide regulation and adhesion turnover. This moves VAPA beyond a generic lipid-transfer scaffold and identifies spatially restricted contact-site behavior in living human epithelial cells. Published March 2024: https://doi.org/10.7554/eLife.85962. (siegfried2024theertether pages 9-11, siegfried2024theertether pages 11-12, siegfried2024theertether pages 1-2)

A second advance is the identification of VAPA as an ER receptor for LSG1 through a noncanonical FFAT-like element, illustrating that the VAPA interactome extends beyond classical lipid-transfer proteins. Published August 2024: https://doi.org/10.1080/10985549.2024.2384600. (sutjita2024theribosomeassembly pages 5-8, sutjita2024theribosomeassembly pages 1-2)

The neuronal study published in January 2024 established VAP-dependent mitochondrial stabilization as a local organizer of synaptic plasticity over approximately 30 µm and 60 min, although VAPA-specific causality remains unresolved. https://doi.org/10.1038/s41467-023-44233-8. (bapat2024vapspatiallystabilizes pages 8-10, bapat2024vapspatiallystabilizes pages 1-2)

The ORP9–ORP11 lipidomics and reconstitution study, posted in 2023 and published as a version of record in August 2024, linked ER–Golgi PS/PI4P exchange to sphingomyelin synthesis. Its direct VAP reconstitution used VAPB, making it mechanistically relevant to VAPA but not VAPA-specific. https://doi.org/10.7554/eLife.91345. (cabukusta2024theorp9orp11dimer pages 1-2, cabukusta2024theorp9orp11dimer pages 9-11)

### 6.2 Experimental and translational applications

VAPA is currently most useful as:

1. **A membrane-contact-site marker and manipulation node.** Fluorescent VAPA constructs, FFAT-binding mutants, knockout cells, proximity labeling, TIRF/SIM, and reconstituted membrane systems are used to map ER contacts and separate physical tethering from lipid-transfer activity. (siegfried2024theertether pages 9-11, james2021theinteractomeof pages 6-7, cabukusta2024theorp9orp11dimer pages 9-11)
2. **A model for lipid-transfer-platform biology.** Perturbing VAPA/VAPB helps dissect ceramide–sphingomyelin metabolism, cholesterol/PI4P exchange, Golgi carrier biogenesis, and phosphoinositide-dependent adhesion dynamics. (wakana2015cartsbiogenesisrequires pages 1-4, peretti2008coordinatedlipidtransfer pages 1-2)
3. **A host factor in disease-relevant cell biology.** VAP machinery influences CFTR proteostasis, EGFR downregulation, epithelial migration, neuronal mitochondrial organization, and pathogen access to host membranes. These findings identify possible intervention points but do not yet establish VAPA as a clinically validated drug target. (bapat2024vapspatiallystabilizes pages 8-10, ernst2016vampassociatedproteins(vap) pages 1-2, eden2016annexina1tethers pages 1-4)

There is presently no retrieved evidence of an approved VAPA-selective drug, validated VAPA clinical biomarker, or VAPA-directed therapeutic trial. Directly inhibiting VAPA could also be difficult because it is ubiquitous, interacts with hundreds of proteins, and overlaps functionally with VAPB. A more selective translational strategy may be to target an individual VAPA–partner interface or disease-specific contact-site complex rather than globally suppressing VAPA.

## 7. Expert assessment and annotation confidence

Authoritative reviews characterize VAP proteins as ubiquitous ER “signposts”: partner proteins recognize VAP to target themselves to the ER, and proteins on other organelles convert that recruitment into membrane-contact-site bridges. This is the most coherent primary annotation for VAPA. (levine2025updateonvap pages 2-4, levine2025updateonvap pages 1-2)

**High-confidence annotation:** human Q9P0L0 is VAPA/VAP-A/hVAP-33; it is a cytoplasm-facing, tail-anchored ER membrane protein with an MSP/Ig-like FFAT-binding domain, flexible linker/coiled-coil region, and C-terminal transmembrane anchor. Its primary role is non-catalytic recruitment and organization of proteins at ER contact sites. (james2021theinteractomeof pages 1-2, kodama2025beyondstatictethering pages 4-6, kodama2025beyondstatictethering pages 1-2)

**High-to-moderate confidence:** VAPA organizes ER–Golgi and ER–endosome lipid-transfer pathways, ER–PM phosphoinositide signaling, membrane trafficking, and adhesion dynamics. Confidence is highest where VAPA alone was knocked out or directly shown to bind the partner; it is lower where both VAPA and VAPB were depleted. (siegfried2024theertether pages 9-11, wakana2015cartsbiogenesisrequires pages 1-4, peretti2008coordinatedlipidtransfer pages 1-2, eden2016annexina1tethers pages 1-4)

**Important limitation:** VAPA and VAPB are highly homologous and share about half of reported interactors. Many studies use antibodies, knockdowns, or constructs that address both proteins. VAPB-specific ALS, PTPIP51, or ACBD5 findings should not be transferred uncritically to VAPA. Conversely, unchanged Golgi/endosomal PI4P after VAPA-only loss suggests that VAPB can compensate in some compartments. (james2021theinteractomeof pages 7-9, levine2025updateonvap pages 1-2, siegfried2024theertether pages 11-12)

## Conclusion

Human VAPA is best annotated as a **ubiquitous ER-resident membrane-contact-site receptor and scaffold**. Its cytosolic MSP domain recognizes FFAT-family motifs; its flexible and oligomerizing architecture recruits lipid-transfer, signaling, trafficking, autophagy, and regulatory proteins and positions them between the ER and other membranes. VAPA does not itself catalyze lipid conversion or transport a defined substrate. Rather, it organizes effectors that transfer ceramide, cholesterol, PS, PI4P, and related lipids or regulate local calcium and phosphoinositide signals. The strongest recent VAPA-specific evidence concerns focal-adhesion-associated ER–PM contacts and LSG1 recruitment, while ER–Golgi lipid metabolism and neuronal mitochondrial stabilization remain partly VAPA/VAPB-redundant. This distinction is essential for accurate functional annotation and therapeutic interpretation.

References

1. (kodama2025beyondstatictethering pages 4-6): Takashi S. Kodama, Kyoko Furuita, and Chojiro Kojima. Beyond static tethering at membrane contact sites: structural dynamics and functional implications of vap proteins. Mar 2025. URL: https://doi.org/10.3390/molecules30061220, doi:10.3390/molecules30061220. This article has 5 citations.

2. (kodama2025beyondstatictethering pages 1-2): Takashi S. Kodama, Kyoko Furuita, and Chojiro Kojima. Beyond static tethering at membrane contact sites: structural dynamics and functional implications of vap proteins. Mar 2025. URL: https://doi.org/10.3390/molecules30061220, doi:10.3390/molecules30061220. This article has 5 citations.

3. (levine2025updateonvap pages 1-2): Tim P. Levine. Update on vap, a ubiquitous signpost for the er. Biological Chemistry, 406(10-12):487-504, Nov 2025. URL: https://doi.org/10.1515/hsz-2025-0199, doi:10.1515/hsz-2025-0199. This article has 7 citations and is from a peer-reviewed journal.

4. (james2021theinteractomeof pages 1-2): Christina James and Ralph H. Kehlenbach. The interactome of the vap family of proteins: an overview. Jul 2021. URL: https://doi.org/10.3390/cells10071780, doi:10.3390/cells10071780. This article has 78 citations.

5. (james2021theinteractomeof pages 7-9): Christina James and Ralph H. Kehlenbach. The interactome of the vap family of proteins: an overview. Jul 2021. URL: https://doi.org/10.3390/cells10071780, doi:10.3390/cells10071780. This article has 78 citations.

6. (siegfried2024theertether pages 9-11): Hugo Siegfried, Georges Farkouh, Rémi Le Borgne, Catherine Pioche-Durieu, Thaïs De Azevedo Laplace, Agathe Verraes, Lucien Daunas, Jean-Marc Verbavatz, and Mélina L Heuzé. The er tether vapa is required for proper cell motility and anchors er-pm contact sites to focal adhesions. Mar 2024. URL: https://doi.org/10.7554/elife.85962, doi:10.7554/elife.85962. This article has 19 citations and is from a domain leading peer-reviewed journal.

7. (bapat2024vapspatiallystabilizes pages 8-10): Ojasee Bapat, Tejas Purimetla, Sarah Kruessel, Monil Shah, Ruolin Fan, Christina Thum, Fiona Rupprecht, Julian D. Langer, and Vidhya Rangaraju. Vap spatially stabilizes dendritic mitochondria to locally support synaptic plasticity. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44233-8, doi:10.1038/s41467-023-44233-8. This article has 56 citations and is from a highest quality peer-reviewed journal.

8. (sutjita2024theribosomeassembly pages 5-8): Putri Sutjita, Sharmishtha Musalgaonkar, Jeffrey Recchia-Rife, Lisa Huang, Blerta Xhemalce, and Arlen W. Johnson. The ribosome assembly factor lsg1 interacts with vesicle-associated membrane protein-associated proteins (vaps). Molecular and Cellular Biology, 44:345-357, Aug 2024. URL: https://doi.org/10.1080/10985549.2024.2384600, doi:10.1080/10985549.2024.2384600. This article has 4 citations and is from a domain leading peer-reviewed journal.

9. (peretti2008coordinatedlipidtransfer pages 1-2): Diego Peretti, Nili Dahan, Eyal Shimoni, Koret Hirschberg, and Sima Lev. Coordinated lipid transfer between the endoplasmic reticulum and the golgi complex requires the vap proteins and is essential for golgi-mediated transport. Molecular biology of the cell, 19 9:3871-84, Sep 2008. URL: https://doi.org/10.1091/mbc.e08-05-0498, doi:10.1091/mbc.e08-05-0498. This article has 398 citations and is from a domain leading peer-reviewed journal.

10. (eden2016annexina1tethers pages 1-4): Emily R. Eden, Elena Sanchez-Heras, Anna Tsapara, Andrzej Sobota, Tim P. Levine, and Clare E. Futter. Annexin a1 tethers membrane contact sites that mediate er to endosome cholesterol transport. Developmental Cell, 37:473-483, Jun 2016. URL: https://doi.org/10.1016/j.devcel.2016.05.005, doi:10.1016/j.devcel.2016.05.005. This article has 191 citations and is from a highest quality peer-reviewed journal.

11. (levine2025updateonvap pages 2-4): Tim P. Levine. Update on vap, a ubiquitous signpost for the er. Biological Chemistry, 406(10-12):487-504, Nov 2025. URL: https://doi.org/10.1515/hsz-2025-0199, doi:10.1515/hsz-2025-0199. This article has 7 citations and is from a peer-reviewed journal.

12. (kodama2025beyondstatictethering pages 20-22): Takashi S. Kodama, Kyoko Furuita, and Chojiro Kojima. Beyond static tethering at membrane contact sites: structural dynamics and functional implications of vap proteins. Mar 2025. URL: https://doi.org/10.3390/molecules30061220, doi:10.3390/molecules30061220. This article has 5 citations.

13. (kodama2025beyondstatictethering pages 19-20): Takashi S. Kodama, Kyoko Furuita, and Chojiro Kojima. Beyond static tethering at membrane contact sites: structural dynamics and functional implications of vap proteins. Mar 2025. URL: https://doi.org/10.3390/molecules30061220, doi:10.3390/molecules30061220. This article has 5 citations.

14. (wakana2015cartsbiogenesisrequires pages 1-4): Yuichi Wakana, Richika Kotake, Nanako Oyama, Motohide Murate, Toshihide Kobayashi, Kohei Arasaki, Hiroki Inoue, and Mitsuo Tagaya. Carts biogenesis requires vap–lipid transfer protein complexes functioning at the endoplasmic reticulum–golgi interface. Molecular Biology of the Cell, 26:4686-4699, Dec 2015. URL: https://doi.org/10.1091/mbc.e15-08-0599, doi:10.1091/mbc.e15-08-0599. This article has 72 citations and is from a domain leading peer-reviewed journal.

15. (kodama2025beyondstatictethering pages 12-14): Takashi S. Kodama, Kyoko Furuita, and Chojiro Kojima. Beyond static tethering at membrane contact sites: structural dynamics and functional implications of vap proteins. Mar 2025. URL: https://doi.org/10.3390/molecules30061220, doi:10.3390/molecules30061220. This article has 5 citations.

16. (kodama2025beyondstatictethering pages 2-4): Takashi S. Kodama, Kyoko Furuita, and Chojiro Kojima. Beyond static tethering at membrane contact sites: structural dynamics and functional implications of vap proteins. Mar 2025. URL: https://doi.org/10.3390/molecules30061220, doi:10.3390/molecules30061220. This article has 5 citations.

17. (cabukusta2024theorp9orp11dimer pages 1-2): Birol Cabukusta, Shalom Borst Pauwels, Jimmy J.L.L. Akkermans, Niek Blomberg, Aat A. Mulder, Roman I. Koning, Martin Giera, and Jacques Neefjes. The orp9-orp11 dimer promotes sphingomyelin synthesis. Jul 2024. URL: https://doi.org/10.7554/elife.91345.2, doi:10.7554/elife.91345.2. This article has 18 citations and is from a domain leading peer-reviewed journal.

18. (cabukusta2024theorp9orp11dimer pages 9-11): Birol Cabukusta, Shalom Borst Pauwels, Jimmy J.L.L. Akkermans, Niek Blomberg, Aat A. Mulder, Roman I. Koning, Martin Giera, and Jacques Neefjes. The orp9-orp11 dimer promotes sphingomyelin synthesis. Jul 2024. URL: https://doi.org/10.7554/elife.91345.2, doi:10.7554/elife.91345.2. This article has 18 citations and is from a domain leading peer-reviewed journal.

19. (siegfried2024theertether pages 11-12): Hugo Siegfried, Georges Farkouh, Rémi Le Borgne, Catherine Pioche-Durieu, Thaïs De Azevedo Laplace, Agathe Verraes, Lucien Daunas, Jean-Marc Verbavatz, and Mélina L Heuzé. The er tether vapa is required for proper cell motility and anchors er-pm contact sites to focal adhesions. Mar 2024. URL: https://doi.org/10.7554/elife.85962, doi:10.7554/elife.85962. This article has 19 citations and is from a domain leading peer-reviewed journal.

20. (siegfried2024theertether pages 1-2): Hugo Siegfried, Georges Farkouh, Rémi Le Borgne, Catherine Pioche-Durieu, Thaïs De Azevedo Laplace, Agathe Verraes, Lucien Daunas, Jean-Marc Verbavatz, and Mélina L Heuzé. The er tether vapa is required for proper cell motility and anchors er-pm contact sites to focal adhesions. Mar 2024. URL: https://doi.org/10.7554/elife.85962, doi:10.7554/elife.85962. This article has 19 citations and is from a domain leading peer-reviewed journal.

21. (siegfried2024theertether pages 12-13): Hugo Siegfried, Georges Farkouh, Rémi Le Borgne, Catherine Pioche-Durieu, Thaïs De Azevedo Laplace, Agathe Verraes, Lucien Daunas, Jean-Marc Verbavatz, and Mélina L Heuzé. The er tether vapa is required for proper cell motility and anchors er-pm contact sites to focal adhesions. Mar 2024. URL: https://doi.org/10.7554/elife.85962, doi:10.7554/elife.85962. This article has 19 citations and is from a domain leading peer-reviewed journal.

22. (bapat2024vapspatiallystabilizes pages 1-2): Ojasee Bapat, Tejas Purimetla, Sarah Kruessel, Monil Shah, Ruolin Fan, Christina Thum, Fiona Rupprecht, Julian D. Langer, and Vidhya Rangaraju. Vap spatially stabilizes dendritic mitochondria to locally support synaptic plasticity. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44233-8, doi:10.1038/s41467-023-44233-8. This article has 56 citations and is from a highest quality peer-reviewed journal.

23. (ernst2016vampassociatedproteins(vap) pages 1-2): Wayne L. Ernst, Kuntala Shome, Christine C. Wu, Xiaoyan Gong, Raymond A. Frizzell, and Meir Aridor. Vamp-associated proteins (vap) as receptors that couple cystic fibrosis transmembrane conductance regulator (cftr) proteostasis with lipid homeostasis. Mar 2016. URL: https://doi.org/10.1074/jbc.m115.692749, doi:10.1074/jbc.m115.692749. This article has 43 citations and is from a domain leading peer-reviewed journal.

24. (sutjita2024theribosomeassembly pages 1-2): Putri Sutjita, Sharmishtha Musalgaonkar, Jeffrey Recchia-Rife, Lisa Huang, Blerta Xhemalce, and Arlen W. Johnson. The ribosome assembly factor lsg1 interacts with vesicle-associated membrane protein-associated proteins (vaps). Molecular and Cellular Biology, 44:345-357, Aug 2024. URL: https://doi.org/10.1080/10985549.2024.2384600, doi:10.1080/10985549.2024.2384600. This article has 4 citations and is from a domain leading peer-reviewed journal.

25. (james2021theinteractomeof pages 6-7): Christina James and Ralph H. Kehlenbach. The interactome of the vap family of proteins: an overview. Jul 2021. URL: https://doi.org/10.3390/cells10071780, doi:10.3390/cells10071780. This article has 78 citations.

26. (kodama2025beyondstatictethering pages 22-24): Takashi S. Kodama, Kyoko Furuita, and Chojiro Kojima. Beyond static tethering at membrane contact sites: structural dynamics and functional implications of vap proteins. Mar 2025. URL: https://doi.org/10.3390/molecules30061220, doi:10.3390/molecules30061220. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](VAPA-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. james2021theinteractomeof pages 7-9
2. kodama2025beyondstatictethering pages 4-6
3. kodama2025beyondstatictethering pages 1-2
4. levine2025updateonvap pages 1-2
5. james2021theinteractomeof pages 1-2
6. siegfried2024theertether pages 9-11
7. bapat2024vapspatiallystabilizes pages 8-10
8. sutjita2024theribosomeassembly pages 5-8
9. peretti2008coordinatedlipidtransfer pages 1-2
10. levine2025updateonvap pages 2-4
11. kodama2025beyondstatictethering pages 20-22
12. kodama2025beyondstatictethering pages 19-20
13. wakana2015cartsbiogenesisrequires pages 1-4
14. kodama2025beyondstatictethering pages 12-14
15. kodama2025beyondstatictethering pages 2-4
16. siegfried2024theertether pages 11-12
17. siegfried2024theertether pages 1-2
18. siegfried2024theertether pages 12-13
19. bapat2024vapspatiallystabilizes pages 1-2
20. sutjita2024theribosomeassembly pages 1-2
21. james2021theinteractomeof pages 6-7
22. kodama2025beyondstatictethering pages 22-24
23. https://doi.org/10.7554/eLife.85962.
24. https://doi.org/10.1080/10985549.2024.2384600.
25. https://doi.org/10.1038/s41467-023-44233-8.
26. https://doi.org/10.7554/eLife.91345.
27. https://doi.org/10.3390/molecules30061220,
28. https://doi.org/10.1515/hsz-2025-0199,
29. https://doi.org/10.3390/cells10071780,
30. https://doi.org/10.7554/elife.85962,
31. https://doi.org/10.1038/s41467-023-44233-8,
32. https://doi.org/10.1080/10985549.2024.2384600,
33. https://doi.org/10.1091/mbc.e08-05-0498,
34. https://doi.org/10.1016/j.devcel.2016.05.005,
35. https://doi.org/10.1091/mbc.e15-08-0599,
36. https://doi.org/10.7554/elife.91345.2,
37. https://doi.org/10.1074/jbc.m115.692749,