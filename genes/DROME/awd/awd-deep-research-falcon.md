---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T18:29:00.565351'
end_time: '2026-09-08T18:37:01.218344'
duration_seconds: 480.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: awd
  gene_symbol: awd
  uniprot_accession: A0A0B4LHX6
  protein_description: 'RecName: Full=Nucleoside diphosphate kinase {ECO:0000256|RuleBase:RU004013};
    EC=2.7.4.6 {ECO:0000256|RuleBase:RU004013};'
  gene_info: Name=awd {ECO:0000313|EMBL:AHN57624.1, ECO:0000313|FlyBase:FBgn0000150};
    Synonyms=1084/08 {ECO:0000313|EMBL:AHN57624.1}, anon-EST:Liang-2.27 {ECO:0000313|EMBL:AHN57624.1},
    anon-EST:Liang-2.28 {ECO:0000313|EMBL:AHN57624.1}, anon-WO0172774.80 {ECO:0000313|EMBL:AHN57624.1},
    anon-WO0172774.82 {ECO:0000313|EMBL:AHN57624.1}, AWD {ECO:0000313|EMBL:AHN57624.1},
    Awd {ECO:0000313|EMBL:AHN57624.1}, BcDNA:GM19775 {ECO:0000313|EMBL:AHN57624.1},
    BcDNA:RH27794 {ECO:0000313|EMBL:AHN57624.1}, clone 2.27 {ECO:0000313|EMBL:AHN57624.1},
    clone 2.28 {ECO:0000313|EMBL:AHN57624.1}, Dmel\CG2210 {ECO:0000313|EMBL:AHN57624.1},
    e(shi)A {ECO:0000313|EMBL:AHN57624.1}, eshiA {ECO:0000313|EMBL:AHN57624.1}, K-pn
    {ECO:0000313|EMBL:AHN57624.1}, Kpn {ECO:0000313|EMBL:AHN57624.1}, l(3)j2A4 {ECO:0000313|EMBL:AHN57624.1},
    l(3)L8700 {ECO:0000313|EMBL:AHN57624.1}, NDKB {ECO:0000313|EMBL:AHN57624.1}, NDPK
    {ECO:0000313|EMBL:AHN57624.1}, Nm23 {ECO:0000313|EMBL:AHN57624.1}, Nm23/awd {ECO:0000313|EMBL:AHN57624.1};
    ORFNames=CG2210 {ECO:0000313|EMBL:AHN57624.1, ECO:0000313|FlyBase:FBgn0000150},
    Dmel_CG2210 {ECO:0000313|EMBL:AHN57624.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the NDK family. {ECO:0000256|ARBA:ARBA00008142,
  protein_domains: NDK-like_dom. (IPR034907); NDK-like_dom_sf. (IPR036850); Nucleoside_diP_kinase.
    (IPR001564); Nucleoside_diP_kinase_AS. (IPR023005); NDK (PF00334)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: awd-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** A0A0B4LHX6
- **Protein Description:** RecName: Full=Nucleoside diphosphate kinase {ECO:0000256|RuleBase:RU004013}; EC=2.7.4.6 {ECO:0000256|RuleBase:RU004013};
- **Gene Information:** Name=awd {ECO:0000313|EMBL:AHN57624.1, ECO:0000313|FlyBase:FBgn0000150}; Synonyms=1084/08 {ECO:0000313|EMBL:AHN57624.1}, anon-EST:Liang-2.27 {ECO:0000313|EMBL:AHN57624.1}, anon-EST:Liang-2.28 {ECO:0000313|EMBL:AHN57624.1}, anon-WO0172774.80 {ECO:0000313|EMBL:AHN57624.1}, anon-WO0172774.82 {ECO:0000313|EMBL:AHN57624.1}, AWD {ECO:0000313|EMBL:AHN57624.1}, Awd {ECO:0000313|EMBL:AHN57624.1}, BcDNA:GM19775 {ECO:0000313|EMBL:AHN57624.1}, BcDNA:RH27794 {ECO:0000313|EMBL:AHN57624.1}, clone 2.27 {ECO:0000313|EMBL:AHN57624.1}, clone 2.28 {ECO:0000313|EMBL:AHN57624.1}, Dmel\CG2210 {ECO:0000313|EMBL:AHN57624.1}, e(shi)A {ECO:0000313|EMBL:AHN57624.1}, eshiA {ECO:0000313|EMBL:AHN57624.1}, K-pn {ECO:0000313|EMBL:AHN57624.1}, Kpn {ECO:0000313|EMBL:AHN57624.1}, l(3)j2A4 {ECO:0000313|EMBL:AHN57624.1}, l(3)L8700 {ECO:0000313|EMBL:AHN57624.1}, NDKB {ECO:0000313|EMBL:AHN57624.1}, NDPK {ECO:0000313|EMBL:AHN57624.1}, Nm23 {ECO:0000313|EMBL:AHN57624.1}, Nm23/awd {ECO:0000313|EMBL:AHN57624.1}; ORFNames=CG2210 {ECO:0000313|EMBL:AHN57624.1, ECO:0000313|FlyBase:FBgn0000150}, Dmel_CG2210 {ECO:0000313|EMBL:AHN57624.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the NDK family. {ECO:0000256|ARBA:ARBA00008142,
- **Key Domains:** NDK-like_dom. (IPR034907); NDK-like_dom_sf. (IPR036850); Nucleoside_diP_kinase. (IPR001564); Nucleoside_diP_kinase_AS. (IPR023005); NDK (PF00334)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "awd" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'awd' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **awd** (gene ID: awd, UniProt: A0A0B4LHX6) in DROME.

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
- **UniProt Accession:** A0A0B4LHX6
- **Protein Description:** RecName: Full=Nucleoside diphosphate kinase {ECO:0000256|RuleBase:RU004013}; EC=2.7.4.6 {ECO:0000256|RuleBase:RU004013};
- **Gene Information:** Name=awd {ECO:0000313|EMBL:AHN57624.1, ECO:0000313|FlyBase:FBgn0000150}; Synonyms=1084/08 {ECO:0000313|EMBL:AHN57624.1}, anon-EST:Liang-2.27 {ECO:0000313|EMBL:AHN57624.1}, anon-EST:Liang-2.28 {ECO:0000313|EMBL:AHN57624.1}, anon-WO0172774.80 {ECO:0000313|EMBL:AHN57624.1}, anon-WO0172774.82 {ECO:0000313|EMBL:AHN57624.1}, AWD {ECO:0000313|EMBL:AHN57624.1}, Awd {ECO:0000313|EMBL:AHN57624.1}, BcDNA:GM19775 {ECO:0000313|EMBL:AHN57624.1}, BcDNA:RH27794 {ECO:0000313|EMBL:AHN57624.1}, clone 2.27 {ECO:0000313|EMBL:AHN57624.1}, clone 2.28 {ECO:0000313|EMBL:AHN57624.1}, Dmel\CG2210 {ECO:0000313|EMBL:AHN57624.1}, e(shi)A {ECO:0000313|EMBL:AHN57624.1}, eshiA {ECO:0000313|EMBL:AHN57624.1}, K-pn {ECO:0000313|EMBL:AHN57624.1}, Kpn {ECO:0000313|EMBL:AHN57624.1}, l(3)j2A4 {ECO:0000313|EMBL:AHN57624.1}, l(3)L8700 {ECO:0000313|EMBL:AHN57624.1}, NDKB {ECO:0000313|EMBL:AHN57624.1}, NDPK {ECO:0000313|EMBL:AHN57624.1}, Nm23 {ECO:0000313|EMBL:AHN57624.1}, Nm23/awd {ECO:0000313|EMBL:AHN57624.1}; ORFNames=CG2210 {ECO:0000313|EMBL:AHN57624.1, ECO:0000313|FlyBase:FBgn0000150}, Dmel_CG2210 {ECO:0000313|EMBL:AHN57624.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the NDK family. {ECO:0000256|ARBA:ARBA00008142,
- **Key Domains:** NDK-like_dom. (IPR034907); NDK-like_dom_sf. (IPR036850); Nucleoside_diP_kinase. (IPR001564); Nucleoside_diP_kinase_AS. (IPR023005); NDK (PF00334)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "awd" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'awd' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **awd** (gene ID: awd, UniProt: A0A0B4LHX6) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster awd* (UniProt A0A0B4LHX6)

## Executive summary

The supplied identity is internally consistent and matches the experimental literature. **awd** (*abnormal wing discs*; **CG2210**, FlyBase FBgn0000150) in *Drosophila melanogaster* encodes a soluble, approximately 17–18-kDa NME/Nm23-family **nucleoside diphosphate kinase** (NDPK; EC 2.7.4.6). Awd is about 78% identical to human NME1/NME2, forms an approximately 100-kDa homo-oligomer consistent with a hexamer, and contains the conserved NDK catalytic residue His119. These findings agree with the supplied UniProt NDK, NDK-like, and nucleoside-diphosphate-kinase domain annotations. No literature concerning a different gene called *awd* was used. (ignesti2017uncoveringtherelationship pages 44-47, woolworth2009thedrosophilametastasis pages 1-2, timmons2000roleofawdnucleoside pages 1-2)

Awd’s **primary molecular function** is reversible transfer of the terminal phosphate between nucleoside triphosphates and diphosphates through a phosphohistidine intermediate. Its best-established **cellular function** is to support endocytic membrane trafficking—especially dynamin-associated internalization and Rab5-associated early-endosome maturation. This controls the abundance or itinerary of specific cargos, including the Breathless FGF receptor, adherens-junction proteins, Notch, and probably components governing Wingless distribution. The frequently invoked model that Awd supplies GTP locally to dynamin or Rab GTPases is biochemically plausible, but has not been demonstrated directly in vivo. (woolworth2009thedrosophilametastasis pages 9-11, nallamothu2009developmentalfunctionof pages 4-5, ignesti2014notchsignalingduring pages 12-14)

No directly Awd-focused publication from 2023–2024 was identified in the retrieved literature. The most recent direct mechanistic study retrieved was published in 2020; thus, current annotation still rests substantially on foundational biochemical and genetic studies from 2000–2014. This absence should not be confused with absence of evidence for function—the older experimental evidence is unusually specific and internally coherent.

## 1. Identity verification

### Gene, organism, and family

The literature explicitly equates *D. melanogaster awd*/*abnormal wing discs* with an NME/Nm23-family NDPK. The cloned product is approximately 17 kDa, reacts with antibodies against mammalian NDPK/NM23, and purified recombinant Awd has NDPK activity. Human NME1/NM23-H1 and NME2/NM23-H2 transgenes are enzymatically active in flies and partially rescue *awd* mutants; the homologous fly transgene provides fuller rescue, suggesting that conserved catalysis is necessary but species-specific interactions also matter. (timmons2000roleofawdnucleoside pages 1-2, timmons2000roleofawdnucleoside pages 2-4)

The protein is reported to form a roughly 100-kDa complex and more specifically a homohexamer, consistent with canonical group-I NME/NDK architecture. Awd reportedly supplies more than 98% of total NDPK activity in larval extracts. These biochemical and structural observations align with UniProt’s NDK-family assignment and the listed InterPro/Pfam NDK domains. (ignesti2017uncoveringtherelationship pages 44-47, timmons2000roleofawdnucleoside pages 1-2)

**Identity conclusion:** A0A0B4LHX6 can be annotated confidently as the *D. melanogaster* Awd/CG2210 NME-family NDPK described in the cited fly literature. The symbol is not functionally ambiguous in this organismal context.

## 2. Primary biochemical function

### Catalyzed reaction

Awd catalyzes the canonical NDPK reaction:

**NTP₁ + NDP₂ ⇌ NDP₁ + NTP₂**

ATP commonly serves as phosphate donor and GDP as acceptor, yielding ADP and GTP, but NDPKs are generally nucleotide-pool-balancing enzymes rather than ATP- or GDP-specific kinases. The available Awd literature describes transfer from ATP to an NDP such as GDP and production of non-ATP NTPs, especially GTP; it does **not** provide a comprehensive Awd-specific kinetic panel establishing a strict physiological preference among GDP, UDP, CDP, or other NDPs. Therefore, the defensible annotation is **broad nucleoside-diphosphate phosphotransfer**, not “GDP kinase” alone. (woolworth2009thedrosophilametastasis pages 9-11, nallamothu2009developmentalfunctionof pages 4-5, woolworth2009thedrosophilametastasis pages 1-2)

### Catalytic mechanism

The reaction follows a ping-pong mechanism in which the donor NTP first phosphorylates Awd’s active-site **His119**; the phosphohistidine then transfers phosphate to an acceptor NDP. Recombinant Awd incubated with dCTP formed progressively more acidic phosphorylated species, and addition of an NDP reversed the modification, supporting formation and discharge of a catalytic phosphoenzyme. Seven principal isoelectric species were interpreted as hexamers carrying zero through six phosphorylated subunits. (timmons2000roleofawdnucleoside pages 5-7)

The strongest causal evidence is the H119A substitution: it abolished detectable NDPK activity despite normal protein accumulation and failed to rescue the *awd* mutant phenotype. Thus, His119-dependent catalytic activity—not merely the presence of Awd as a scaffold—is essential for viability and development. (ignesti2017uncoveringtherelationship pages 47-50, timmons2000roleofawdnucleoside pages 1-2)

The dominant *Killer of prune*/*K-pn* allele encodes P97S. It retains conventional NDPK catalytic efficiency but alters flexibility near the substrate-binding region and has been proposed to change protein interactions or substrate recognition. Reports that this allele loses histidine-dependent “protein-kinase” activity should be interpreted cautiously: atypical protein phosphorylation by NME proteins has been debated, whereas canonical NDPK activity is firmly established. (ignesti2017uncoveringtherelationship pages 47-50, nallamothu2009developmentalfunctionof pages 4-5)

## 3. Cellular localization

Awd is principally described as a **soluble intracellular protein**, rather than an integral membrane protein. Expression occurs throughout development and is prominent in imaginal discs, brain, lymph glands, ovaries, and fat body. Antibody staining has also associated Awd/NDPK with microtubules, although this does not establish a permanent microtubule-bound pool. (timmons2000roleofawdnucleoside pages 1-2, timmons2000roleofawdnucleoside pages 2-4)

Localization is tissue- and stage-dependent. In ovarian follicle cells, Awd is initially cytoplasmic with apical/lateral representation, begins shifting toward the basal region after stage 5, is predominantly basal around stage 6, and becomes firmly or exclusively basal by stages 8–10. This polarized localization is consistent with its role in spatially controlled retrieval and turnover of membrane and junctional proteins. (ignesti2017uncoveringtherelationship pages 47-50)

A doctoral study additionally detected Awd in larval hemolymph and S2-cell microvesicles and found that dominant-negative Shibire reduced intracellular Awd in 80.6% of adipocytes examined (n=62), while increasing hemolymph Awd under restrictive conditions. These observations suggest extracellular release and dynamin-dependent reuptake, but this proposed extracellular cycle is less firmly established than Awd’s intracellular NDPK and endocytic functions and should not be made the principal localization annotation. (ignesti2017uncoveringtherelationship pages 98-101)

## 4. Endocytosis as the central cellular function

### Shibire/dynamin-associated internalization

Awd was linked genetically to endocytosis through screens involving **shibire (shi)**, the fly dynamin. Temperature-sensitive *shi* animals are paralyzed at 29°C because synaptic-vesicle recycling fails; three mutations that enhanced paralysis at 25°C proved to be *awd* alleles, and established *awd* alleles reproduced the interaction. These results place Awd in synaptic-vesicle recycling or a closely connected endocytic process. (nallamothu2009developmentalfunctionof pages 4-5)

No stable physical Awd–Shibire interaction was detected in the reported work. One model proposes that NDPK activity generates GTP locally for dynamin’s membrane-fission cycle. This is attractive because His119-dependent catalysis is essential and dynamin is a GTPase, but the fly experiments demonstrate genetic and functional cooperation—not direct nucleotide channeling. Awd may also influence trafficking through Rab5 abundance, endosome maturation, membrane-associated protein interactions, or a combination of these mechanisms. (ignesti2017uncoveringtherelationship pages 47-50, timmons2000roleofawdnucleoside pages 2-4, ignesti2014notchsignalingduring pages 12-14)

### Breathless/FGFR and tracheal guidance

During embryonic tracheal development, Awd restrains signaling by the Breathless FGF receptor (Btl/FGFR). *awd* loss or Awd RNAi causes massive receptor accumulation, consistent with defective internalization, and produces ectopic tracheal-cell migration; severe mutants exhibit epithelial detachment resembling an EMT-like disruption. *awd–shi* double mutants strongly exacerbate the tracheal phenotype, supporting a shared endocytic mechanism. (nallamothu2009developmentalfunctionof pages 4-5)

The precise interpretation is that Awd is not primarily an FGF-pathway enzyme or transcription factor. Rather, it limits the amount and duration of signaling-competent Btl at the cell surface or within its endocytic itinerary. Failure to clear the receptor makes migratory tracheal cells excessively responsive to guidance cues, explaining ectopic migration and branching abnormalities. This is among the clearest links between Awd’s trafficking activity and a defined developmental pathway.

## 5. Rab5, adherens junctions, and epithelial integrity

In ovarian follicle epithelium, Awd positively regulates the early-endosomal GTPase **Rab5**. *awd*-null cells show reduced Rab5 and accumulation/spreading of DE-cadherin, Armadillo/β-catenin, and α-spectrin. The resulting defects include breaks in the epithelial sheet and adenoma-like cell piling. Conversely, Awd overexpression reduces junctional components and promotes spindle- or mesenchymal-like morphology, indicating that both insufficient and excessive junction turnover can compromise tissue organization. (woolworth2009thedrosophilametastasis pages 9-11, woolworth2009thedrosophilametastasis pages 1-2)

The evidence supports a model in which Awd promotes Rab5-dependent internalization or turnover of uncomplexed adherens-junction components, thereby maintaining appropriate junction composition and epithelial architecture. It does not show that Awd is itself a structural adherens-junction protein. Nor does the phenotype amount to spontaneous metastatic behavior: most mutant follicle cells remain associated with the epithelium. Detachment and ectopic movement become especially prominent in cell populations with an intrinsic migratory program, such as tracheal cells. (ignesti2017uncoveringtherelationship pages 47-50, woolworth2009thedrosophilametastasis pages 9-11)

## 6. Notch trafficking and signaling

Awd is required for productive Notch signaling in ovarian follicle cells and larval wing discs. In complete-loss clones, Notch can enter cells but accumulates near the apical surface and in enlarged Avalanche/Rab5-positive early endosomes; it progresses poorly into Rab7-positive late-endosomal compartments. Notch remains trapped for at least an hour after internalization, while lysosomal abundance measured by LysoTracker is not detectably changed. These observations localize the principal defect to **early-endosome maturation or onward trafficking**, rather than a global absence of endocytosis or lysosomes. (ignesti2014notchsignalingduring pages 4-6, ignesti2014notchsignalingduring pages 1-2, ignesti2014notchsignalingduring pages 9-10)

Genetic epistasis refines this placement. Constitutively active Rab5 produces enlarged early endosomes but does not restore Notch signaling in *awd* mutant cells, indicating that Awd is needed for Rab5 function or for a subsequent maturation step. In mutant follicle cells expressing Rab5CA, 87.1% of Notch vesicles colocalized with Rab5CA but only 31.45% with the multivesicular-body marker Hrs (n=124). (ignesti2014notchsignalingduring pages 12-14, ignesti2014notchsignalingduring pages 10-12)

Expression of nuclear Notch intracellular domain (NICD) restored the target Hindsight in 60.5% of mutant cells (199/329), whereas membrane-bound NEXT—which still requires intracellular processing—failed to rescue. Presenilin abundance was unchanged. Together, these findings place Awd upstream of productive NICD release, at trafficking required for γ-secretase/S3 processing rather than at transcription downstream of NICD. Wing clones lacking Awd lose Notch-responsive reporters and Wg expression; 72% of adult mosaics examined (18/25) had notched margins or thickened veins. (ignesti2014notchsignalingduring pages 4-6, ignesti2014notchsignalingduring pages 6-9, ignesti2014notchsignalingduring pages 2-4)

## 7. Wingless/Wg signaling and dosage effects

Awd dosage produces distinct effects on Notch and Wg. Complete *awd* loss blocks Notch signaling and therefore eliminates Notch-dependent Wg expression at the wing dorsoventral boundary. Partial RNAi depletion, however, leaves Notch reporters and the Wg-producing domain largely intact while altering Wg intracellular distribution and signaling range. Short-range Sens expression is lost adjacent to Wg-producing cells, while Wg puncta and ectopic distal Sens indicate that some longer-range movement persists. The authors proposed defective recycling of the Wg chaperone Evi/Wls, but did not directly establish Evi as an Awd cargo. (serafini2020theimpactof pages 7-9, serafini2020theimpactof pages 1-3)

Recent quantitative data from that study illustrate the dose dependence: 23.48% of posterior-compartment knockdown animals survived to adults (n=132); 64.9% of larvae with ubiquitous RNAi reached pupation (n=111); all *awdJ2A4* null larvae died before pupariation (n=120). Partial depletion also causes chromosomal instability and JNK-dependent, p53-independent death, which may contribute indirectly to wing phenotypes and cautions against assigning every RNAi phenotype solely to altered Wg transport. (serafini2020theimpactof pages 7-9, serafini2020theimpactof pages 1-3)

## 8. Integrated pathway model

The best-supported functional sequence is:

1. Awd uses His119-dependent NDPK chemistry to maintain or spatially supply non-ATP nucleoside triphosphates, prominently GTP.
2. Awd supports dynamin-dependent membrane internalization and Rab5-associated early-endosomal function.
3. Cargo-specific effects follow: surface Btl/FGFR is restrained; adherens-junction components undergo controlled turnover; internalized Notch proceeds beyond early endosomes for productive cleavage; and Wg distribution is maintained.
4. These trafficking effects tune cell migration, epithelial cohesion, morphogenesis, and signaling output.

Steps 2–4 are strongly supported by genetics, cell biology, cargo localization, and epistasis. The direct mechanistic bridge between step 1 and step 2 remains unresolved. In particular, no cited experiment directly measured a local Awd-generated GTP pool at dynamin-coated pits or Rab5 endosomes. It is therefore most accurate to annotate Awd with both **NDPK activity** and **positive regulation of endocytic trafficking**, while describing local GTP channeling as a leading hypothesis rather than an established molecular mechanism.

## 9. Evidence matrix

| Functional claim | Direct evidence | Biological context / localization | Confidence and interpretive caveat | Key paper |
|---|---|---|---|---|
| **Identity and primary enzyme function:** *D. melanogaster* **awd/CG2210** encodes an NME/Nm23-family nucleoside diphosphate kinase (NDPK; EC 2.7.4.6). | Recombinant Awd has NDPK activity; the soluble ~17-kDa subunit assembles into an approximately 100-kDa complex consistent with a homohexamer. Awd is ~78% identical to human NME1/NME2 and contributes >98% of total larval NDPK activity. It transfers a terminal phosphate from an NTP, commonly ATP, to an NDP through a phosphoenzyme intermediate. (ignesti2017uncoveringtherelationship pages 44-47, timmons2000roleofawdnucleoside pages 1-2, timmons2000roleofawdnucleoside pages 5-7) | Soluble intracellular protein expressed throughout development, with enrichment reported in imaginal discs, brain, lymph glands, ovaries, and fat body. | **High confidence.** Identity, enzyme activity, and oligomeric organization are supported experimentally and agree with the supplied UniProt NDK-family/domain annotations. Detailed Awd-specific kinetic constants across all nucleotide substrates were not provided. | Timmons & Shearn (2000), [https://doi.org/10.1023/A:1005545214937](https://doi.org/10.1023/A:1005545214937) |
| **Catalytic His119 is biologically essential.** | His119→Ala abolishes detectable NDPK activity despite normal protein accumulation and fails to rescue *awd* mutants. Incubation with dCTP generates phosphorylated Awd species, and addition of an NDP reverses phosphorylation, supporting a ping-pong phosphohistidine mechanism. (timmons2000roleofawdnucleoside pages 1-2, timmons2000roleofawdnucleoside pages 5-7) | Catalysis occurs on the soluble homohexamer; each subunit can form the phosphorylated intermediate. | **High confidence** for the necessity of His119-dependent NDPK catalysis. The physiological identity and concentrations of nucleotide donor–acceptor pairs in particular compartments remain unresolved. | Timmons & Shearn (2000), [https://doi.org/10.1023/A:1005545214937](https://doi.org/10.1023/A:1005545214937) |
| **Awd supports Shibire/dynamin-dependent endocytosis and Breathless/FGFR down-regulation.** | Multiple *awd* alleles enhance temperature-sensitive *shibire* paralysis; *awd–shi* double mutants strongly exacerbate tracheal defects. Loss or RNAi depletion of Awd causes marked Breathless/FGFR accumulation and ectopic tracheal-cell migration, consistent with failed receptor internalization. (nallamothu2009developmentalfunctionof pages 4-5) | Synaptic-vesicle recycling and embryonic tracheal epithelium; relevant activity is associated functionally with the plasma-membrane endocytic machinery. | **High confidence** for genetic cooperation and receptor-trafficking control. A direct stable Awd–dynamin physical interaction was not detected. The proposal that Awd supplies GTP locally to dynamin is plausible but **hypothesized, not directly demonstrated** in these experiments. (ignesti2017uncoveringtherelationship pages 47-50, timmons2000roleofawdnucleoside pages 2-4, ignesti2014notchsignalingduring pages 12-14) | Dammai et al. (2003), [https://doi.org/10.1101/gad.1096903](https://doi.org/10.1101/gad.1096903) |
| **Awd promotes Rab5-associated adherens-junction turnover and epithelial integrity.** | In *awd*-null follicle cells, Rab5 is reduced while DE-cadherin, Armadillo/β-catenin, and α-spectrin accumulate and spread; epithelial sheets break and cells pile up. Awd overexpression reduces junctional components and induces spindle-like morphology. (woolworth2009thedrosophilametastasis pages 9-11, woolworth2009thedrosophilametastasis pages 1-2) | Ovarian follicular epithelium. Awd shifts from cytoplasmic/apical-lateral distribution early in oogenesis toward the basal domain after stage 6 and is exclusively basal by stage 10. (ignesti2017uncoveringtherelationship pages 47-50) | **High confidence** that Awd dosage regulates Rab5 abundance/function and junction-component trafficking. Whether nucleotide channeling directly activates Rab5 remains unproven; the data establish functional dependence rather than direct GTP transfer to Rab5. | Woolworth et al. (2009), [https://doi.org/10.1128/MCB.00297-09](https://doi.org/10.1128/MCB.00297-09) |
| **Awd is required for Notch progression through early endosomes and productive signaling.** | In *awd*-null follicle and wing-disc cells, internalized Notch accumulates in enlarged Avl/Rab5-positive early endosomes and fails to progress efficiently to Rab7-positive late compartments. Constitutively active Rab5 does not rescue signaling; NICD restores Hnt in 60.5% of mutant cells (199/329), whereas membrane-bound NEXT does not. In Rab5CA-expressing mutant follicle cells, 87.1% of Notch vesicles colocalize with Rab5CA versus 31.45% with Hrs (n=124). (ignesti2014notchsignalingduring pages 10-12, ignesti2014notchsignalingduring pages 4-6, ignesti2014notchsignalingduring pages 6-9, ignesti2014notchsignalingduring pages 9-10) | Ovarian follicle cells and larval wing imaginal discs; the critical site is the early-endosomal maturation/progression step upstream of productive NICD release. | **High confidence.** Epistasis places the principal defect after internalization and before or at trafficking needed for γ-secretase/S3 processing. Presenilin abundance is unchanged, favoring a trafficking defect over loss of γ-secretase itself. | Ignesti et al. (2014), [https://doi.org/10.1186/1741-7007-12-12](https://doi.org/10.1186/1741-7007-12-12) |
| **Awd dosage differentially affects Wingless/Wg and Notch signaling.** | Complete *awd* loss blocks Notch outputs, including Wg expression. Partial RNAi depletion leaves Notch reporters active and Wg in its normal dorsoventral source domain, but alters Wg distribution, eliminates nearby Sens expression, and permits ectopic distal Sens. Only 23.48% of posterior-compartment knockdown animals reached adulthood (n=132); 64.9% of ubiquitous-knockdown larvae pupated (n=111), whereas all null larvae died before pupariation (n=120). (serafini2020theimpactof pages 7-9, serafini2020theimpactof pages 1-3) | Larval wing-disc epithelium; interpreted in the context of Wg secretion/distribution and endocytic recycling, potentially involving Evi/Wls. | **Moderate confidence** for a dose-dependent requirement in Wg distribution. Altered Evi/Wls recycling is a mechanistic proposal rather than a directly established Awd cargo relationship in this study; chromosomal instability and JNK-dependent death may contribute indirectly. | Serafini et al. (2020), [https://doi.org/10.3390/ijms21197257](https://doi.org/10.3390/ijms21197257) |


*Table: Experimental evidence linking Awd’s NDPK chemistry to endocytic trafficking and developmental signaling in Drosophila. The matrix separates demonstrated catalytic and trafficking functions from the unproven model that Awd locally supplies GTP to dynamin or Rab proteins.*

## 10. Current applications and translational relevance

Awd is chiefly a **research model**, not a therapeutic product or clinical biomarker. Its major real-world use is experimental: *Drosophila* mosaics, RNAi, temperature-sensitive *shi* genetics, live cargo-trafficking assays, and tissue-specific developmental models allow researchers to dissect how NME-family proteins couple nucleotide metabolism to receptor trafficking, epithelial organization, and migration. The fly system is especially informative for interpreting human NME1/NME2 metastasis-suppressor biology because human NME proteins can partially rescue *awd* defects and because endocytic regulation is conserved. Nevertheless, human cancer conclusions should not be inferred automatically from fly phenotypes; NME effects are dose-, cargo-, tissue-, and localization-dependent. (woolworth2009thedrosophilametastasis pages 1-2, timmons2000roleofawdnucleoside pages 2-4, serafini2020theimpactof pages 7-9)

## 11. Evidence gaps and priorities

The principal unresolved questions are:

- **Substrate specificity:** purified-Awd kinetic constants across physiologically relevant NDP/NTP pairs are not available in the retrieved evidence.
- **Catalysis-to-trafficking coupling:** direct imaging or biosensor measurements are needed to test whether Awd creates local GTP microdomains for dynamin, Rab5, or other GTPases.
- **Physical partners:** genetic cooperation with Shibire and Rab5 is strong, but stable direct binding and its structural basis remain uncertain.
- **Subcellular pools:** the relative roles of cytosolic, cortical, endosomal, microtubule-associated, and possible extracellular Awd require modern endogenous tagging and quantitative imaging.
- **Recent research:** no Awd-specific 2023–2024 study was found in the searched corpus, so claims of a newer revised mechanism would presently be unsupported.

## Key cited publications

- Timmons L, Shearn A. **Role of AWD/Nucleoside Diphosphate Kinase in Drosophila Development.** *Journal of Bioenergetics and Biomembranes*. Published June 2000. https://doi.org/10.1023/A:1005545214937 (timmons2000roleofawdnucleoside pages 1-2, timmons2000roleofawdnucleoside pages 5-7)
- Dammai V, Adryan B, Lavenburg KR, Hsu T. **Drosophila awd, the homolog of human nm23, regulates FGF receptor levels and functions synergistically with shi/dynamin during tracheal development.** *Genes & Development*. Published November 2003. https://doi.org/10.1101/gad.1096903 (nallamothu2009developmentalfunctionof pages 4-5)
- Nallamothu G, Dammai V, Hsu T. **Developmental function of Nm23/awd: a mediator of endocytosis.** *Molecular and Cellular Biochemistry*. Published April 2009. https://doi.org/10.1007/s11010-009-0112-7 (nallamothu2009developmentalfunctionof pages 4-5)
- Woolworth JA, Nallamothu G, Hsu T. **The Drosophila metastasis suppressor gene Nm23 homolog, awd, regulates epithelial integrity during oogenesis.** *Molecular and Cellular Biology*. Published September 2009. https://doi.org/10.1128/MCB.00297-09 (woolworth2009thedrosophilametastasis pages 9-11, woolworth2009thedrosophilametastasis pages 1-2)
- Ignesti M et al. **Notch signaling during development requires the function of awd, the Drosophila homolog of human metastasis suppressor gene Nm23.** *BMC Biology*. Published February 2014. https://doi.org/10.1186/1741-7007-12-12 (ignesti2014notchsignalingduring pages 12-14, ignesti2014notchsignalingduring pages 6-9)
- Serafini G et al. **The Impact of Drosophila Awd/NME1/2 Levels on Notch and Wg Signaling Pathways.** *International Journal of Molecular Sciences*. Published October 2020. https://doi.org/10.3390/ijms21197257 (serafini2020theimpactof pages 7-9, serafini2020theimpactof pages 1-3)

References

1. (ignesti2017uncoveringtherelationship pages 44-47): Marilena Ignesti. Uncovering the relationship between endocytosis and awd, the drosophila homolog of nme metastasis suppressor proteins. ArXiv, Apr 2017. URL: https://doi.org/10.6092/unibo/amsdottorato/7850, doi:10.6092/unibo/amsdottorato/7850. This article has 0 citations.

2. (woolworth2009thedrosophilametastasis pages 1-2): Julie A. Woolworth, Gouthami Nallamothu, and Tien Hsu. The <i>drosophila</i> metastasis suppressor gene <i>nm23</i> homolog, <i>awd</i>, regulates epithelial integrity during oogenesis. Sep 2009. URL: https://doi.org/10.1128/mcb.00297-09, doi:10.1128/mcb.00297-09. This article has 51 citations and is from a domain leading peer-reviewed journal.

3. (timmons2000roleofawdnucleoside pages 1-2): Lisa Timmons and Allen Shearn. Role of awd/nucleoside diphosphate kinase in drosophila development. Journal of Bioenergetics and Biomembranes, 32:293-300, Jun 2000. URL: https://doi.org/10.1023/a:1005545214937, doi:10.1023/a:1005545214937. This article has 54 citations and is from a peer-reviewed journal.

4. (woolworth2009thedrosophilametastasis pages 9-11): Julie A. Woolworth, Gouthami Nallamothu, and Tien Hsu. The <i>drosophila</i> metastasis suppressor gene <i>nm23</i> homolog, <i>awd</i>, regulates epithelial integrity during oogenesis. Sep 2009. URL: https://doi.org/10.1128/mcb.00297-09, doi:10.1128/mcb.00297-09. This article has 51 citations and is from a domain leading peer-reviewed journal.

5. (nallamothu2009developmentalfunctionof pages 4-5): Gouthami Nallamothu, Vincent Dammai, and Tien Hsu. Developmental function of nm23/awd: a mediator of endocytosis. Molecular and Cellular Biochemistry, 329:35-44, Apr 2009. URL: https://doi.org/10.1007/s11010-009-0112-7, doi:10.1007/s11010-009-0112-7. This article has 28 citations and is from a peer-reviewed journal.

6. (ignesti2014notchsignalingduring pages 12-14): Marilena Ignesti, Marilena Barraco, Gouthami Nallamothu, Julie A Woolworth, Serena Duchi, Giuseppe Gargiulo, Valeria Cavaliere, and Tien Hsu. Notch signaling during development requires the function of awd, the drosophila homolog of human metastasis suppressor gene nm23. BMC Biology, 12:12-12, Feb 2014. URL: https://doi.org/10.1186/1741-7007-12-12, doi:10.1186/1741-7007-12-12. This article has 29 citations and is from a domain leading peer-reviewed journal.

7. (timmons2000roleofawdnucleoside pages 2-4): Lisa Timmons and Allen Shearn. Role of awd/nucleoside diphosphate kinase in drosophila development. Journal of Bioenergetics and Biomembranes, 32:293-300, Jun 2000. URL: https://doi.org/10.1023/a:1005545214937, doi:10.1023/a:1005545214937. This article has 54 citations and is from a peer-reviewed journal.

8. (timmons2000roleofawdnucleoside pages 5-7): Lisa Timmons and Allen Shearn. Role of awd/nucleoside diphosphate kinase in drosophila development. Journal of Bioenergetics and Biomembranes, 32:293-300, Jun 2000. URL: https://doi.org/10.1023/a:1005545214937, doi:10.1023/a:1005545214937. This article has 54 citations and is from a peer-reviewed journal.

9. (ignesti2017uncoveringtherelationship pages 47-50): Marilena Ignesti. Uncovering the relationship between endocytosis and awd, the drosophila homolog of nme metastasis suppressor proteins. ArXiv, Apr 2017. URL: https://doi.org/10.6092/unibo/amsdottorato/7850, doi:10.6092/unibo/amsdottorato/7850. This article has 0 citations.

10. (ignesti2017uncoveringtherelationship pages 98-101): Marilena Ignesti. Uncovering the relationship between endocytosis and awd, the drosophila homolog of nme metastasis suppressor proteins. ArXiv, Apr 2017. URL: https://doi.org/10.6092/unibo/amsdottorato/7850, doi:10.6092/unibo/amsdottorato/7850. This article has 0 citations.

11. (ignesti2014notchsignalingduring pages 4-6): Marilena Ignesti, Marilena Barraco, Gouthami Nallamothu, Julie A Woolworth, Serena Duchi, Giuseppe Gargiulo, Valeria Cavaliere, and Tien Hsu. Notch signaling during development requires the function of awd, the drosophila homolog of human metastasis suppressor gene nm23. BMC Biology, 12:12-12, Feb 2014. URL: https://doi.org/10.1186/1741-7007-12-12, doi:10.1186/1741-7007-12-12. This article has 29 citations and is from a domain leading peer-reviewed journal.

12. (ignesti2014notchsignalingduring pages 1-2): Marilena Ignesti, Marilena Barraco, Gouthami Nallamothu, Julie A Woolworth, Serena Duchi, Giuseppe Gargiulo, Valeria Cavaliere, and Tien Hsu. Notch signaling during development requires the function of awd, the drosophila homolog of human metastasis suppressor gene nm23. BMC Biology, 12:12-12, Feb 2014. URL: https://doi.org/10.1186/1741-7007-12-12, doi:10.1186/1741-7007-12-12. This article has 29 citations and is from a domain leading peer-reviewed journal.

13. (ignesti2014notchsignalingduring pages 9-10): Marilena Ignesti, Marilena Barraco, Gouthami Nallamothu, Julie A Woolworth, Serena Duchi, Giuseppe Gargiulo, Valeria Cavaliere, and Tien Hsu. Notch signaling during development requires the function of awd, the drosophila homolog of human metastasis suppressor gene nm23. BMC Biology, 12:12-12, Feb 2014. URL: https://doi.org/10.1186/1741-7007-12-12, doi:10.1186/1741-7007-12-12. This article has 29 citations and is from a domain leading peer-reviewed journal.

14. (ignesti2014notchsignalingduring pages 10-12): Marilena Ignesti, Marilena Barraco, Gouthami Nallamothu, Julie A Woolworth, Serena Duchi, Giuseppe Gargiulo, Valeria Cavaliere, and Tien Hsu. Notch signaling during development requires the function of awd, the drosophila homolog of human metastasis suppressor gene nm23. BMC Biology, 12:12-12, Feb 2014. URL: https://doi.org/10.1186/1741-7007-12-12, doi:10.1186/1741-7007-12-12. This article has 29 citations and is from a domain leading peer-reviewed journal.

15. (ignesti2014notchsignalingduring pages 6-9): Marilena Ignesti, Marilena Barraco, Gouthami Nallamothu, Julie A Woolworth, Serena Duchi, Giuseppe Gargiulo, Valeria Cavaliere, and Tien Hsu. Notch signaling during development requires the function of awd, the drosophila homolog of human metastasis suppressor gene nm23. BMC Biology, 12:12-12, Feb 2014. URL: https://doi.org/10.1186/1741-7007-12-12, doi:10.1186/1741-7007-12-12. This article has 29 citations and is from a domain leading peer-reviewed journal.

16. (ignesti2014notchsignalingduring pages 2-4): Marilena Ignesti, Marilena Barraco, Gouthami Nallamothu, Julie A Woolworth, Serena Duchi, Giuseppe Gargiulo, Valeria Cavaliere, and Tien Hsu. Notch signaling during development requires the function of awd, the drosophila homolog of human metastasis suppressor gene nm23. BMC Biology, 12:12-12, Feb 2014. URL: https://doi.org/10.1186/1741-7007-12-12, doi:10.1186/1741-7007-12-12. This article has 29 citations and is from a domain leading peer-reviewed journal.

17. (serafini2020theimpactof pages 7-9): Giulia Serafini, Giorgia Giordani, Luca Grillini, Davide Andrenacci, Giuseppe Gargiulo, and Valeria Cavaliere. The impact of drosophila awd/nme1/2 levels on notch and wg signaling pathways. International Journal of Molecular Sciences, 21:7257, Oct 2020. URL: https://doi.org/10.3390/ijms21197257, doi:10.3390/ijms21197257. This article has 2 citations.

18. (serafini2020theimpactof pages 1-3): Giulia Serafini, Giorgia Giordani, Luca Grillini, Davide Andrenacci, Giuseppe Gargiulo, and Valeria Cavaliere. The impact of drosophila awd/nme1/2 levels on notch and wg signaling pathways. International Journal of Molecular Sciences, 21:7257, Oct 2020. URL: https://doi.org/10.3390/ijms21197257, doi:10.3390/ijms21197257. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](awd-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. timmons2000roleofawdnucleoside pages 5-7
2. ignesti2017uncoveringtherelationship pages 47-50
3. ignesti2017uncoveringtherelationship pages 98-101
4. nallamothu2009developmentalfunctionof pages 4-5
5. ignesti2017uncoveringtherelationship pages 44-47
6. woolworth2009thedrosophilametastasis pages 1-2
7. timmons2000roleofawdnucleoside pages 1-2
8. woolworth2009thedrosophilametastasis pages 9-11
9. ignesti2014notchsignalingduring pages 12-14
10. timmons2000roleofawdnucleoside pages 2-4
11. ignesti2014notchsignalingduring pages 4-6
12. ignesti2014notchsignalingduring pages 1-2
13. ignesti2014notchsignalingduring pages 9-10
14. ignesti2014notchsignalingduring pages 10-12
15. ignesti2014notchsignalingduring pages 6-9
16. ignesti2014notchsignalingduring pages 2-4
17. serafini2020theimpactof pages 7-9
18. serafini2020theimpactof pages 1-3
19. https://doi.org/10.1023/A:1005545214937
20. https://doi.org/10.1101/gad.1096903
21. https://doi.org/10.1128/MCB.00297-09
22. https://doi.org/10.1186/1741-7007-12-12
23. https://doi.org/10.3390/ijms21197257
24. https://doi.org/10.1023/A:1005545214937](https://doi.org/10.1023/A:1005545214937
25. https://doi.org/10.1101/gad.1096903](https://doi.org/10.1101/gad.1096903
26. https://doi.org/10.1128/MCB.00297-09](https://doi.org/10.1128/MCB.00297-09
27. https://doi.org/10.1186/1741-7007-12-12](https://doi.org/10.1186/1741-7007-12-12
28. https://doi.org/10.3390/ijms21197257](https://doi.org/10.3390/ijms21197257
29. https://doi.org/10.1007/s11010-009-0112-7
30. https://doi.org/10.6092/unibo/amsdottorato/7850,
31. https://doi.org/10.1128/mcb.00297-09,
32. https://doi.org/10.1023/a:1005545214937,
33. https://doi.org/10.1007/s11010-009-0112-7,
34. https://doi.org/10.1186/1741-7007-12-12,
35. https://doi.org/10.3390/ijms21197257,