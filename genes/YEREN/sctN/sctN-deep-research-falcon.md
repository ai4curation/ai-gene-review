---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T16:50:14.609340'
end_time: '2026-09-27T16:59:22.604833'
duration_seconds: 548.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: YEREN
  gene_id: sctN
  gene_symbol: sctN
  uniprot_accession: P40290
  protein_description: 'RecName: Full=Type 3 secretion system ATPase {ECO:0000305};
    Short=T3SS ATPase {ECO:0000305}; EC=7.4.2.8 {ECO:0000305|PubMed:16672607, ECO:0000305|PubMed:8132449};
    AltName: Full=Type III secretion ATPase {ECO:0000303|PubMed:17050689}; AltName:
    Full=Yop proteins secretion ATPase; AltName: Full=Ysc ATPase {ECO:0000303|PubMed:8132449};'
  gene_info: Name=sctN {ECO:0000303|PubMed:25591178, ECO:0000303|PubMed:9618447};
    Synonyms=yscN {ECO:0000303|PubMed:8132449};
  organism_full: Yersinia enterocolitica.
  protein_family: Belongs to the ATPase alpha/beta chains family. T3SS ATPase
  protein_domains: AAA+_ATPase. (IPR003593); ATPase_a/bsu_AS. (IPR020003); ATPase_alpha/beta_chains.
    (IPR050053); ATPase_F1/V1/A1_a/bsu_N. (IPR004100); ATPase_F1/V1/A1_a/bsu_nucl-bd.
    (IPR000194)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: sctN-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P40290
- **Protein Description:** RecName: Full=Type 3 secretion system ATPase {ECO:0000305}; Short=T3SS ATPase {ECO:0000305}; EC=7.4.2.8 {ECO:0000305|PubMed:16672607, ECO:0000305|PubMed:8132449}; AltName: Full=Type III secretion ATPase {ECO:0000303|PubMed:17050689}; AltName: Full=Yop proteins secretion ATPase; AltName: Full=Ysc ATPase {ECO:0000303|PubMed:8132449};
- **Gene Information:** Name=sctN {ECO:0000303|PubMed:25591178, ECO:0000303|PubMed:9618447}; Synonyms=yscN {ECO:0000303|PubMed:8132449};
- **Organism (full):** Yersinia enterocolitica.
- **Protein Family:** Belongs to the ATPase alpha/beta chains family. T3SS ATPase
- **Key Domains:** AAA+_ATPase. (IPR003593); ATPase_a/bsu_AS. (IPR020003); ATPase_alpha/beta_chains. (IPR050053); ATPase_F1/V1/A1_a/bsu_N. (IPR004100); ATPase_F1/V1/A1_a/bsu_nucl-bd. (IPR000194)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sctN" matches the protein description above**
2. **Verify the organism is correct:** Yersinia enterocolitica.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sctN' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sctN** (gene ID: sctN, UniProt: P40290) in YEREN.

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
- **UniProt Accession:** P40290
- **Protein Description:** RecName: Full=Type 3 secretion system ATPase {ECO:0000305}; Short=T3SS ATPase {ECO:0000305}; EC=7.4.2.8 {ECO:0000305|PubMed:16672607, ECO:0000305|PubMed:8132449}; AltName: Full=Type III secretion ATPase {ECO:0000303|PubMed:17050689}; AltName: Full=Yop proteins secretion ATPase; AltName: Full=Ysc ATPase {ECO:0000303|PubMed:8132449};
- **Gene Information:** Name=sctN {ECO:0000303|PubMed:25591178, ECO:0000303|PubMed:9618447}; Synonyms=yscN {ECO:0000303|PubMed:8132449};
- **Organism (full):** Yersinia enterocolitica.
- **Protein Family:** Belongs to the ATPase alpha/beta chains family. T3SS ATPase
- **Key Domains:** AAA+_ATPase. (IPR003593); ATPase_a/bsu_AS. (IPR020003); ATPase_alpha/beta_chains. (IPR050053); ATPase_F1/V1/A1_a/bsu_N. (IPR004100); ATPase_F1/V1/A1_a/bsu_nucl-bd. (IPR000194)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sctN" matches the protein description above**
2. **Verify the organism is correct:** Yersinia enterocolitica.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sctN' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sctN** (gene ID: sctN, UniProt: P40290) in YEREN.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Yersinia enterocolitica* **sctN/yscN** (UniProt P40290)

## Executive conclusion

P40290 is the **Ysc–Yop type III secretion-system ATPase** of *Yersinia enterocolitica*, historically called **YscN** and now standardized as **SctN**. It is a cytoplasmic, peripheral component of the injectisome—not an integral membrane transporter—and occupies the center of the cytosolic sorting platform beneath the inner-membrane export gate. Its primary biochemical function is ATP hydrolysis, conventionally represented as **ATP + H₂O → ADP + Pi**, coupled to preparation and delivery of secretion substrates to the export apparatus. Direct *Y. enterocolitica* genetics show that **yscN is required for Yop secretion**. Current evidence supports roles in sorting-platform organization and ATP-dependent remodeling of chaperone–substrate complexes, but does **not** establish P40290 as the sole motor for passage through the secretion channel; proton motive force and the membrane export apparatus also contribute.

The strongest recent advance is a January 2024 live-cell study showing that SctN participates in dynamic cytosolic sorting-platform complexes, while SctQ and SctL make the most evident contacts with effector–chaperone cargo. Secretion activation increased estimated injectisome abundance from **5.1 ± 1.7 to 17.9 ± 5.4 per bacterium**, approximately 3.5-fold. (wimmi2024cytosolicsortingplatform pages 1-2, wimmi2024cytosolicsortingplatform pages 3-4)

## 1. Mandatory identity verification

### Correct gene and organism

The target is the *Y. enterocolitica* **Ysc–Yop-system ATPase** described in the supplied UniProt record as P40290, gene **sctN**, synonym **yscN**. The legacy name YscN is used in most older experimental papers; SctN is the unified nomenclature for the homologous ATPase across injectisome T3SSs. Organism-specific studies identify YscN/SctN as part of the Ysc apparatus responsible for exporting Yersinia outer proteins, or Yops. An *Y. enterocolitica yscN* mutant failed to secrete the tested YopE–DHFR substrates, directly linking this gene to Ysc–Yop export. (feldman2002syceallowssecretion pages 5-6)

### Critical ambiguity resolved: SctN/YscN is not YsaN

*Y. enterocolitica* also possesses a distinct T3SS ATPase named **YsaN**, belonging to the chromosomal Ysa–Ysp system. YsaN studies report a Mg²⁺-dependent ATPase, dodecameric preparations and inhibition by YsaL, but those measurements are **not measurements of P40290** and should not be used as direct annotations for SctN/YscN. For example, YsaL inhibited YsaN by 73%, had a reported binding Kd of 35 nM, and showed maximal inhibition at a 2:1 ratio; these results are informative only as same-species homolog evidence. (chatterjee2013identificationandmolecular pages 6-8, chatterjee2013identificationandmolecular pages 8-10)

### Family and domain consistency

The supplied InterPro assignments—AAA+-like ATPase, ATPase alpha/beta-chain family, and F1/V1/A1 ATPase-related nucleotide-binding domains—are consistent with the accepted evolutionary and structural interpretation of SctN proteins as secretion ATPases related to rotary ATPases. The architecture supports nucleotide binding, oligomerization and ATP-coupled conformational cycling. The retrieved literature did not independently map exact InterPro boundaries on P40290, so domain-boundary details remain database-derived rather than newly verified experimentally.

The evidence-weighted annotation is summarized below.

| Annotation dimension | Best-supported conclusion | Evidence type | Key quantitative result | Important caveat |
|---|---|---|---|---|
| Identity and nomenclature | UniProt P40290 is the *Yersinia enterocolitica* Ysc–Yop-system ATPase historically named **YscN** and standardized as **SctN**. It is distinct from **YsaN**, the ATPase of the separate chromosomal Ysa–Ysp T3SS. | Supplied UniProt identity aligned with organism-specific YscN studies and modern Sct nomenclature (wimmi2024cytosolicsortingplatform pages 1-2, feldman2002syceallowssecretion pages 5-6) | Not applicable. | The retrieved literature did not independently map P40290 to a particular strain or locus; the accession mapping rests on the supplied UniProt record. |
| Catalytic reaction | SctN/YscN is an ATP-hydrolyzing secretion ATPase catalyzing ATP + H₂O → ADP + phosphate. ATP is the established substrate; broader NTP specificity is not adequately defined. | Direct ATPase classification supported by homolog biochemistry. Mg²⁺ dependence was measured for *Y. enterocolitica* YsaN, not P40290 (swietnicki2011identificationofsmallmolecule pages 1-2, chatterjee2013identificationandmolecular pages 8-10) | No reliable P40290-specific kinetic constants were recovered. | YsaN kinetic and oligomerization measurements must not be transferred directly to P40290 because YsaN belongs to a different T3SS. |
| Substrate and cargo recognition | SctN helps prepare Yop substrates for export, probably by promoting remodeling or dissociation of chaperone–cargo complexes. Live-cell evidence indicates that initial effector capture is mediated principally by SctQ and SctL rather than a stable direct SctN–effector interaction (wimmi2024cytosolicsortingplatform pages 3-4, wimmi2024cytosolicsortingplatform pages 2-3) | Live-cell tracking, immunoprecipitation and proximity labeling in *Y. enterocolitica*, interpreted using conserved T3SS ATPase mechanisms. | YopO–SycO strongly changed SctQ and SctL mobility but had essentially no effect on SctN: Σ(Δ²) values were 0.415, 0.413 and 0.003, respectively (wimmi2024cytosolicsortingplatform pages 1-2, pintor2024thepathand pages 37-38) | Direct P40290 binding to every exported Yop has not been demonstrated; chaperone removal should not be treated as the sole cargo-recognition step. |
| Localization and complex architecture | SctN is a cytoplasmic component positioned beneath the inner-membrane export gate. It forms the central ATPase assembly connected through SctL to SctQ-containing sorting-platform pods and also occurs in mobile cytosolic complexes (wimmi2024cytosolicsortingplatform pages 7-8, wimmi2024cytosolicsortingplatform pages 2-3) | Fluorescence localization and single-particle tracking in live *Y. enterocolitica*, integrated with conserved injectisome architecture. | Proposed single-pod composition is 1 SctK, 4 SctQ, 2 SctL and 1 SctN; approximately 24 SctQ molecules occur per injectisome (pintor2024thepathand pages 146-149, wimmi2024cytosolicsortingplatform pages 7-8) | The proposed stoichiometry is an integrated model, not an atomic structure of native P40290 within the *Y. enterocolitica* injectisome. |
| Requirement for secretion | YscN/SctN is required for Ysc–Yop type III export: an *Y. enterocolitica yscN* mutant failed to secrete the tested YopE–DHFR substrates (feldman2002syceallowssecretion pages 5-6) | Direct organism-specific genetic loss-of-function and secretion assays. | No secretion of the tested YopE–DHFR hybrids was detected in the *yscN* mutant (feldman2002syceallowssecretion pages 5-6) | Necessity for secretion does not mean ATP hydrolysis is the only energy source; proton motive force also contributes to T3SS transport. |
| Folding and unfolding of cargo | The Ysc system favors destabilized or readily unfolded substrates, although some cargo can reach a folded, ligand-binding state before secretion. SctN is best viewed as part of a substrate-preparation pathway rather than a proven stand-alone universal unfoldase (feldman2002syceallowssecretion pages 5-6, wilharm2004yersiniaenterocoliticatype pages 6-7) | Direct YopE–DHFR secretion, ligand-binding, stability and channel-jamming experiments in *Y. enterocolitica*. | Secreted destabilized DHFR had an approximately 12–15 min half-life; a severely truncated form had a half-life below 5 min and was secreted efficiently. Some folded fusions jammed the apparatus (feldman2002syceallowssecretion pages 5-6) | These experiments indicate conformational remodeling but do not directly measure mechanical unfolding by purified P40290. |
| 2024 live-cell findings | Mobile sorting-platform complexes capture effectors in the cytosol and shuttle them to membrane-bound injectisomes. SctN occurs in the larger complexes but behaves differently from the cargo-responsive SctQ and SctL components (wimmi2024cytosolicsortingplatform pages 1-2, wimmi2024cytosolicsortingplatform pages 3-4) | 2024 *Nature Microbiology* study using PALM, sptPALM, proximity labeling, interaction assays and quantitative microscopy in live *Y. enterocolitica*. | Secretion activation increased injectisomes from 5.1 ± 1.7 to 17.9 ± 5.4 per bacterium, approximately 3.5-fold; SctQ exchanged at about 0.51 molecules per second per injectisome with a 68.2 s recovery half-time (wimmi2024cytosolicsortingplatform pages 3-4, wimmi2024cytosolicsortingplatform pages 7-8) | The increase reflects injectisome assembly and remodeling, not the catalytic turnover of individual SctN molecules. |
| Inhibitor and application evidence | T3SS ATPases are plausible antivirulence targets because inhibition can block effector secretion without directly targeting essential bacterial growth. YscN inhibition has proof of concept in *Y. pestis*, but no P40290-selective inhibitor or clinical implementation is established (swietnicki2011identificationofsmallmolecule pages 1-2) | **Homolog evidence only:** biochemical inhibition, secretion assays and mouse virulence studies using *Y. pestis* YscN. | Reported inhibitors had in-vitro IC₅₀ values below 20 μM; catalytic-domain deletion attenuated *Y. pestis* by more than three million-fold in a mouse bubonic-plague model (swietnicki2011identificationofsmallmolecule pages 1-2) | These results cannot be assigned directly to *Y. enterocolitica* P40290; potency, selectivity, permeability and efficacy require organism-specific validation. |
| Same-species YsaN homolog evidence | *Y. enterocolitica* YsaN illustrates conserved regulation of a T3SS ATPase by an inhibitory partner, but it is not P40290. YsaN is Mg²⁺ dependent, forms active higher-order oligomers and is inhibited by YsaL (chatterjee2013identificationandmolecular pages 6-8, chatterjee2013identificationandmolecular pages 8-10) | **Homolog evidence only:** purified-protein biochemistry, size-exclusion chromatography, dynamic light scattering, crosslinking and surface plasmon resonance. | YsaL reduced YsaN activity by 73%, bound with a reported Kd of 35 nM and showed maximal inhibition at a 2:1 YsaL:YsaN ratio; an approximately 603 kDa YsaN dodecamer was reported (chatterjee2013identificationandmolecular pages 6-8, chatterjee2013identificationandmolecular pages 8-10) | These values are not P40290 measurements and do not establish that native SctN is dodecameric; current injectisome models favor a central SctN hexamer. |


*Table: Evidence-weighted annotation of *Yersinia enterocolitica* SctN/YscN, explicitly separating direct P40290-relevant findings from homolog evidence involving *Y. pestis* YscN or the distinct *Y. enterocolitica* YsaN ATPase.*

## 2. Primary biochemical function

### Catalyzed reaction and substrate

SctN is an **ATP phosphohydrolase** associated with type III protein export:

**ATP + H₂O → ADP + orthophosphate.**

ATP is therefore its primary small-molecule substrate. Mg²⁺ dependence is typical of this ATPase family and has been demonstrated for the distinct *Y. enterocolitica* YsaN homolog, but a P40290-specific metal-dependence curve or reliable kinetic constants were not recovered in the accessible evidence. Broader substrate specificity—such as meaningful turnover of GTP, CTP or other NTPs—should be regarded as unestablished for P40290 rather than assumed.

Functionally, its macromolecular “substrates” are not transported metabolites but components of the T3SS export pathway: sorting-platform proteins and secretion cargo presented as free substrates or chaperone–substrate complexes. Related Yersinia work describes ATP hydrolysis as facilitating chaperone removal and secretion of Yops. (swietnicki2011identificationofsmallmolecule pages 1-2)

### What ATP hydrolysis accomplishes

The best-supported mechanistic interpretation is that SctN uses ATP-dependent conformational cycling to **prepare secretion substrates for entry into the export apparatus**, including remodeling or dissociating cognate secretion chaperones. It is less secure to state that SctN alone mechanically pushes substrates through the needle. In current models, ATPase-mediated substrate preparation and sorting act together with the inner-membrane export gate and proton motive force.

Direct *Y. enterocolitica* evidence establishes necessity: a **yscN mutant secreted none of the tested YopE–DHFR hybrids**. This is strong evidence that YscN is indispensable for productive Ysc export, although the experiment does not by itself partition energetic contributions between ATP hydrolysis and proton motive force. (feldman2002syceallowssecretion pages 5-6)

## 3. Cellular localization and structural role

SctN is located on the **cytoplasmic side of the bacterial inner membrane**, beneath the membrane-embedded export apparatus. It is not secreted and is not expected to enter the periplasm, extracellular medium or host-cell cytoplasm. At assembled injectisomes, SctN forms the central ATPase assembly below the export gate. SctL dimers connect the SctN center to SctQ-containing sorting-platform pods, while SctK links the platform to the membrane-associated basal body. (wimmi2024cytosolicsortingplatform pages 2-3)

Localization is dynamic rather than exclusively injectisome-bound. Live-cell tracking indicates that SctN and other sorting-platform proteins partition between **soluble cytosolic complexes** and **injectisome-associated assemblies**. Larger mobile complexes contain SctK, SctQ, SctL and SctN, consistent with preassembly or cargo-delivery intermediates. (wimmi2024cytosolicsortingplatform pages 1-2, wimmi2024cytosolicsortingplatform pages 7-8)

The working architectural model assigns a central SctN hexamer connecting six sorting-platform pods. One proposed pod contains one SctK, four SctQ, two SctL and one SctN-equivalent connection; approximately 24 SctQ molecules are estimated per injectisome. This is an integrated stoichiometric model rather than an atomic structure of native P40290 in situ. (pintor2024thepathand pages 146-149, wimmi2024cytosolicsortingplatform pages 7-8)

## 4. Biological pathway and mechanism

### Ysc–Yop injectisome pathway

The Ysc–Yop T3SS transfers Yop proteins from the bacterial cytoplasm across both bacterial membranes and, after host-cell contact and translocon formation, into the eukaryotic target cell. Within this pathway, SctN acts at the cytoplasmic entrance to the machinery:

1. Yop effectors are synthesized in the bacterial cytoplasm, often bound by cognate Syc chaperones.
2. SctQ- and SctL-containing mobile sorting-platform complexes capture or associate with cargo.
3. Cargo-loaded complexes shuttle to membrane-bound injectisomes.
4. SctN and associated components prepare cargo for engagement with the export gate, including ATP-dependent chaperone release or conformational remodeling.
5. The export apparatus then translocates substrates through the narrow secretion channel, with proton motive force contributing to transport.

This assignment is more precise than describing SctN simply as an “energizer”: the ATPase is simultaneously a catalytic enzyme and an organizational hub of the substrate-sorting machinery.

### Cargo recognition is distributed across the platform

The 2024 data refine earlier models that placed direct cargo recognition primarily at the ATPase. YopO–SycO expression markedly altered diffusion of SctQ and SctL but produced almost no corresponding change for SctN: reported distribution-difference values were **0.415 for SctQ, 0.413 for SctL and 0.003 for SctN**. SctN was detected in SctQ-associated complexes, but less strongly than SctL. Thus, SctN belongs to cargo-handling complexes, while the clearest initial effector contacts occur through SctQ and SctL. (wimmi2024cytosolicsortingplatform pages 1-2, wimmi2024cytosolicsortingplatform pages 3-4, pintor2024thepathand pages 37-38)

Effectors were estimated to bind SctQ at roughly one effector per SctQ in proposed soluble complexes. SctQ exchange at injectisomes had a fluorescence-recovery half-time of **68.2 seconds**, corresponding to approximately **0.51 SctQ molecules per second per injectisome**. These measurements support a shuttle-and-exchange model rather than a permanently fixed cytoplasmic platform. (wimmi2024cytosolicsortingplatform pages 7-8)

## 5. Substrate folding, chaperones and the proposed unfoldase role

YopE–DHFR fusion experiments demonstrate that substrate conformation strongly affects secretion. Destabilized DHFR cargo with a half-life of approximately **12–15 minutes**, and especially a severely truncated form with a half-life under **5 minutes**, was secreted more readily than stable wild-type DHFR. Some stable fusions were secretion-defective and jammed the apparatus. SycE enabled secretion of certain otherwise problematic YopE–DHFR constructs, indicating that chaperones help maintain or deliver secretion-competent cargo. (feldman2002syceallowssecretion pages 5-6, feldman2002syceallowssecretion pages 1-2)

Other experiments showed that YopE–DHFR cargo could bind methotrexate before secretion, demonstrating that at least its DHFR moiety had reached a folded, ligand-binding state. Pre-existing fusion protein could still be secreted after translation was inhibited. Conversely, other folded fusion architectures plugged the machinery. The apparatus can therefore process some cargo that folds before export, but not all stable folds. (wilharm2004yersiniaenterocoliticatype pages 6-7, wilharm2004yersiniaenterocoliticatype pages 2-4)

These findings are compatible with active unfolding or remodeling at the cytoplasmic entrance, potentially involving SctN, but they do not directly visualize purified P40290 mechanically unfolding a protein. The conservative annotation is therefore: **SctN participates in ATP-dependent substrate preparation and chaperone release and may assist unfolding, but P40290 has not been shown to be a universal stand-alone unfoldase.**

## 6. Recent development: dynamic effector shuttling in live cells

The most important recent organism-specific advance is Wimmi et al., published in *Nature Microbiology* in **January 2024**: [https://doi.org/10.1038/s41564-023-01545-1](https://doi.org/10.1038/s41564-023-01545-1). Using photoactivated localization microscopy, single-particle tracking, proximity labeling and interaction assays, the authors showed that sorting-platform proteins form mobile cytosolic cargo-delivery assemblies as well as injectisome-bound pods. SctN occurs within larger assemblies containing SctK, SctQ and SctL, but cargo-dependent mobility changes are strongest for SctQ and SctL. (wimmi2024cytosolicsortingplatform pages 1-2, wimmi2024cytosolicsortingplatform pages 3-4)

Upon secretion activation, estimated injectisome abundance increased from **5.1 ± 1.7 to 17.9 ± 5.4 per cell**. This approximately 3.5-fold rise reveals substantial remodeling of secretion capacity and shows that SctN operates in a system whose copy number and organization respond dynamically to secretion state. (wimmi2024cytosolicsortingplatform pages 3-4)

Expert interpretation from these data is that mobile sorting-platform “pods” capture effectors in the cytoplasm and deliver them to membrane-bound machines. SctN should consequently be understood as the central ATPase of a dynamic logistics and substrate-preparation system, not merely a static basal-body component. (wimmi2024cytosolicsortingplatform pages 1-2, wimmi2024cytosolicsortingplatform pages 7-8)

## 7. Applications and translational relevance

### Antivirulence target

SctN-family ATPases are attractive antivirulence targets because blocking them can disable effector secretion without necessarily inhibiting core bacterial metabolism. Proof of concept exists for the close *Y. pestis* YscN homolog: deletion of its catalytic domain attenuated the organism by more than **three million-fold** in a mouse bubonic-plague model, and small molecules with in-vitro **IC50 values below 20 μM** inhibited ATPase activity and YopE secretion. Publication: May 2011, [https://doi.org/10.1371/journal.pone.0019716](https://doi.org/10.1371/journal.pone.0019716). (swietnicki2011identificationofsmallmolecule pages 1-2)

This is compelling family-level validation, but it is not evidence of a clinically deployable P40290 inhibitor. No P40290-selective drug, approved therapy or clinical implementation was identified. Future compounds must demonstrate inhibition of purified *Y. enterocolitica* SctN, intracellular access, selectivity over host ATPases and bacterial housekeeping enzymes, blockade of Yop secretion, and efficacy in relevant infection models.

### Experimental and biotechnology applications

SctN is useful as:

- a genetic switch for constructing secretion-deficient controls;
- a mechanistic probe of cargo recognition, chaperone release and sorting-platform assembly;
- a reporter target in single-molecule studies of injectisome dynamics;
- a candidate node for engineering T3SS-based protein-delivery systems.

These are primarily research applications. There is no evidence that P40290 itself currently has an industrial or clinical real-world implementation.

## 8. Evidence limitations and confidence assessment

**High-confidence annotations** are the protein’s identity as YscN/SctN, its assignment to the Ysc–Yop T3SS, its cytoplasmic/injectisome-associated localization, ATPase function, central sorting-platform position and requirement for Yop secretion. The *yscN* loss-of-function secretion phenotype and 2024 live-cell localization data are particularly strong. (wimmi2024cytosolicsortingplatform pages 1-2, feldman2002syceallowssecretion pages 5-6)

**Moderate-confidence mechanistic annotations** are ATP-driven chaperone dissociation and substrate remodeling. These are strongly supported across the SctN family and consistent with *Y. enterocolitica* cargo-folding experiments, but the retrieved evidence did not provide a complete purified-P40290 kinetic and single-turnover analysis.

**Insufficiently established for P40290** are exact Km, kcat, metal dependence, non-ATP nucleotide specificity, a native high-resolution P40290 structure, direct mechanical-unfolding rates and a selective inhibitor profile. Quantitative results from *Y. enterocolitica* YsaN or *Y. pestis* YscN should be labeled explicitly as homolog evidence rather than transferred as accession-specific facts.

## Overall functional annotation

**SctN/YscN (P40290) is the cytoplasmic ATPase and central sorting-platform component of the *Y. enterocolitica* Ysc–Yop type III secretion injectisome. It hydrolyzes ATP to coordinate substrate preparation—probably including chaperone release and conformational remodeling—and delivery to the inner-membrane export gate. It functions beneath the inner membrane in both soluble cytosolic sorting-platform complexes and injectisome-bound assemblies. Loss of YscN abolishes tested Yop secretion, establishing it as essential for this virulence-export pathway. Current evidence indicates that SctQ/SctL perform prominent initial cargo-capture functions, while SctN supplies ATP-dependent processing and organizational activity; subsequent translocation also depends on the membrane export machinery and proton motive force.**

References

1. (wimmi2024cytosolicsortingplatform pages 1-2): Stephan Wimmi, Alexander Balinovic, Corentin Brianceau, Katherine Pintor, Jan Vielhauer, Bartosz Turkowyd, Carlos Helbig, Moritz Fleck, Katja Langenfeld, Jörg Kahnt, Timo Glatter, Ulrike Endesfelder, and Andreas Diepold. Cytosolic sorting platform complexes shuttle type iii secretion system effectors to the injectisome in yersinia enterocolitica. Nature Microbiology, 9:185-199, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01545-1, doi:10.1038/s41564-023-01545-1. This article has 25 citations and is from a highest quality peer-reviewed journal.

2. (wimmi2024cytosolicsortingplatform pages 3-4): Stephan Wimmi, Alexander Balinovic, Corentin Brianceau, Katherine Pintor, Jan Vielhauer, Bartosz Turkowyd, Carlos Helbig, Moritz Fleck, Katja Langenfeld, Jörg Kahnt, Timo Glatter, Ulrike Endesfelder, and Andreas Diepold. Cytosolic sorting platform complexes shuttle type iii secretion system effectors to the injectisome in yersinia enterocolitica. Nature Microbiology, 9:185-199, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01545-1, doi:10.1038/s41564-023-01545-1. This article has 25 citations and is from a highest quality peer-reviewed journal.

3. (feldman2002syceallowssecretion pages 5-6): Mario F. Feldman, Simone Müller, Esther Wüest, and Guy R. Cornelis. Syce allows secretion of yope–dhfr hybrids by the yersinia enterocolitica type iii ysc system. Molecular Microbiology, 46:1183-1197, Nov 2002. URL: https://doi.org/10.1046/j.1365-2958.2002.03241.x, doi:10.1046/j.1365-2958.2002.03241.x. This article has 137 citations and is from a domain leading peer-reviewed journal.

4. (chatterjee2013identificationandmolecular pages 6-8): Rakesh Chatterjee, Pranab Kumar Halder, and Saumen Datta. Identification and molecular characterization of ysal (ye3555): a novel negative regulator of ysan atpase in type three secretion system of enteropathogenic bacteria yersinia enterocolitica. PLoS ONE, 8:e75028, Oct 2013. URL: https://doi.org/10.1371/journal.pone.0075028, doi:10.1371/journal.pone.0075028. This article has 17 citations and is from a peer-reviewed journal.

5. (chatterjee2013identificationandmolecular pages 8-10): Rakesh Chatterjee, Pranab Kumar Halder, and Saumen Datta. Identification and molecular characterization of ysal (ye3555): a novel negative regulator of ysan atpase in type three secretion system of enteropathogenic bacteria yersinia enterocolitica. PLoS ONE, 8:e75028, Oct 2013. URL: https://doi.org/10.1371/journal.pone.0075028, doi:10.1371/journal.pone.0075028. This article has 17 citations and is from a peer-reviewed journal.

6. (swietnicki2011identificationofsmallmolecule pages 1-2): Wieslaw Swietnicki, Daniel Carmany, Michael Retford, Mark Guelta, Russell Dorsey, Joel Bozue, Michael S. Lee, and Mark A. Olson. Identification of small-molecule inhibitors of yersinia pestis type iii secretion system yscn atpase. PLoS ONE, 6:e19716, May 2011. URL: https://doi.org/10.1371/journal.pone.0019716, doi:10.1371/journal.pone.0019716. This article has 95 citations and is from a peer-reviewed journal.

7. (wimmi2024cytosolicsortingplatform pages 2-3): Stephan Wimmi, Alexander Balinovic, Corentin Brianceau, Katherine Pintor, Jan Vielhauer, Bartosz Turkowyd, Carlos Helbig, Moritz Fleck, Katja Langenfeld, Jörg Kahnt, Timo Glatter, Ulrike Endesfelder, and Andreas Diepold. Cytosolic sorting platform complexes shuttle type iii secretion system effectors to the injectisome in yersinia enterocolitica. Nature Microbiology, 9:185-199, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01545-1, doi:10.1038/s41564-023-01545-1. This article has 25 citations and is from a highest quality peer-reviewed journal.

8. (pintor2024thepathand pages 37-38): K Pintor. The path and regulation of the type iii secretion effector export. Unknown journal, 2024.

9. (wimmi2024cytosolicsortingplatform pages 7-8): Stephan Wimmi, Alexander Balinovic, Corentin Brianceau, Katherine Pintor, Jan Vielhauer, Bartosz Turkowyd, Carlos Helbig, Moritz Fleck, Katja Langenfeld, Jörg Kahnt, Timo Glatter, Ulrike Endesfelder, and Andreas Diepold. Cytosolic sorting platform complexes shuttle type iii secretion system effectors to the injectisome in yersinia enterocolitica. Nature Microbiology, 9:185-199, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01545-1, doi:10.1038/s41564-023-01545-1. This article has 25 citations and is from a highest quality peer-reviewed journal.

10. (pintor2024thepathand pages 146-149): K Pintor. The path and regulation of the type iii secretion effector export. Unknown journal, 2024.

11. (wilharm2004yersiniaenterocoliticatype pages 6-7): Gottfried Wilharm, Verena Lehmann, Wibke Neumayer, Janja Trček, and Jürgen Heesemann. Yersinia enterocolitica type iii secretion: evidence for the ability to transport proteins that are folded prior to secretion. BMC Microbiology, 4:27-27, Jul 2004. URL: https://doi.org/10.1186/1471-2180-4-27, doi:10.1186/1471-2180-4-27. This article has 34 citations and is from a peer-reviewed journal.

12. (feldman2002syceallowssecretion pages 1-2): Mario F. Feldman, Simone Müller, Esther Wüest, and Guy R. Cornelis. Syce allows secretion of yope–dhfr hybrids by the yersinia enterocolitica type iii ysc system. Molecular Microbiology, 46:1183-1197, Nov 2002. URL: https://doi.org/10.1046/j.1365-2958.2002.03241.x, doi:10.1046/j.1365-2958.2002.03241.x. This article has 137 citations and is from a domain leading peer-reviewed journal.

13. (wilharm2004yersiniaenterocoliticatype pages 2-4): Gottfried Wilharm, Verena Lehmann, Wibke Neumayer, Janja Trček, and Jürgen Heesemann. Yersinia enterocolitica type iii secretion: evidence for the ability to transport proteins that are folded prior to secretion. BMC Microbiology, 4:27-27, Jul 2004. URL: https://doi.org/10.1186/1471-2180-4-27, doi:10.1186/1471-2180-4-27. This article has 34 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](sctN-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. feldman2002syceallowssecretion pages 5-6
2. swietnicki2011identificationofsmallmolecule pages 1-2
3. wimmi2024cytosolicsortingplatform pages 2-3
4. wimmi2024cytosolicsortingplatform pages 7-8
5. wimmi2024cytosolicsortingplatform pages 3-4
6. wimmi2024cytosolicsortingplatform pages 1-2
7. chatterjee2013identificationandmolecular pages 6-8
8. chatterjee2013identificationandmolecular pages 8-10
9. pintor2024thepathand pages 37-38
10. pintor2024thepathand pages 146-149
11. wilharm2004yersiniaenterocoliticatype pages 6-7
12. feldman2002syceallowssecretion pages 1-2
13. wilharm2004yersiniaenterocoliticatype pages 2-4
14. https://doi.org/10.1038/s41564-023-01545-1
15. https://doi.org/10.1371/journal.pone.0019716
16. https://doi.org/10.1038/s41564-023-01545-1](https://doi.org/10.1038/s41564-023-01545-1
17. https://doi.org/10.1371/journal.pone.0019716](https://doi.org/10.1371/journal.pone.0019716
18. https://doi.org/10.1038/s41564-023-01545-1,
19. https://doi.org/10.1046/j.1365-2958.2002.03241.x,
20. https://doi.org/10.1371/journal.pone.0075028,
21. https://doi.org/10.1371/journal.pone.0019716,
22. https://doi.org/10.1186/1471-2180-4-27,