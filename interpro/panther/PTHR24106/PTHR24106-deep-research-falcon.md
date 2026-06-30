---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:15:52.766474'
end_time: '2026-06-28T21:39:48.385892'
duration_seconds: 1435.62
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24106
  interpro_name: NOD-like receptor (NLR)
  interpro_short_name: NLR
  interpro_type: family
  interpro_integrated: IPR051261
  member_databases: Not specified
  n_proteins: '35463'
  n_taxa: '2720'
  n_subfamilies: '12'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The NOD-like receptor (NLR) family is involved in the innate
    immune response, acting as pattern recognition receptors (PRRs) that detect pathogen-associated
    molecular patterns (PAMPs) and danger signals. Members of the family participate
    in various signaling pathways, including NF-kappa-B, MAP kinases, and type I/II
    interferon pathways, contributing to the transcriptional activation of genes involved
    in immune response. They play roles in gastrointestinal immunity, antiviral defense,
    autophagy, and inflammation regulation. Some NLRs detect specific bacterial peptidoglycan
    fragments, while others negatively regulate immune responses to prevent excessive
    inflammation. Additionally, they are implicated in metabolic regulation, appetite
    control, and cellular stress responses.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR24106-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR24106-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR24106
- **Name:** NOD-like receptor (NLR)
- **Short name:** NLR
- **Entry type:** family
- **Integrated into / parent:** IPR051261
- **Member database signatures:** Not specified
- **Scale:** 35463 proteins across 2720 taxa, 12 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The NOD-like receptor (NLR) family is involved in the innate immune response, acting as pattern recognition receptors (PRRs) that detect pathogen-associated molecular patterns (PAMPs) and danger signals. Members of the family participate in various signaling pathways, including NF-kappa-B, MAP kinases, and type I/II interferon pathways, contributing to the transcriptional activation of genes involved in immune response. They play roles in gastrointestinal immunity, antiviral defense, autophagy, and inflammation regulation. Some NLRs detect specific bacterial peptidoglycan fragments, while others negatively regulate immune responses to prevent excessive inflammation. Additionally, they are implicated in metabolic regulation, appetite control, and cellular stress responses.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24106 (NOD-like receptor (NLR))**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


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

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR24106
- **Name:** NOD-like receptor (NLR)
- **Short name:** NLR
- **Entry type:** family
- **Integrated into / parent:** IPR051261
- **Member database signatures:** Not specified
- **Scale:** 35463 proteins across 2720 taxa, 12 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The NOD-like receptor (NLR) family is involved in the innate immune response, acting as pattern recognition receptors (PRRs) that detect pathogen-associated molecular patterns (PAMPs) and danger signals. Members of the family participate in various signaling pathways, including NF-kappa-B, MAP kinases, and type I/II interferon pathways, contributing to the transcriptional activation of genes involved in immune response. They play roles in gastrointestinal immunity, antiviral defense, autophagy, and inflammation regulation. Some NLRs detect specific bacterial peptidoglycan fragments, while others negatively regulate immune responses to prevent excessive inflammation. Additionally, they are implicated in metabolic regulation, appetite control, and cellular stress responses.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24106 (NOD-like receptor (NLR))**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


# InterPro Family Research Report: PTHR24106 — NOD-like Receptor (NLR) Family

## 1. Family Definition and Biochemistry

### Domain Architecture and Structural Fold

The NOD-like receptor (NLR) family comprises multidomain intracellular proteins typically ~1,000 amino acids (~120 kDa) in size, organized around a conserved tripartite domain architecture (hochheiser2023structuralaspectsof pages 1-4, ohto2022activationandregulation pages 1-2). The three core structural elements are:

1. **N-terminal effector domain**: Variable across subfamilies — may be a pyrin domain (PYD), caspase activation and recruitment domain (CARD), baculoviral inhibitor of apoptosis repeat (BIR), acidic transactivation domain (AD), or an atypical domain. This domain mediates protein–protein interactions for downstream signaling (hochheiser2023structuralaspectsof pages 4-6, zhou2023nodlikereceptorsignaling pages 2-4).

2. **Central NACHT domain**: The defining feature of the family. The NACHT domain is a nucleoside-triphosphatase (NTPase) module belonging to the STAND (signal transduction ATPases with numerous domains) subgroup of P-loop ATPases, related to the AAA+ superfamily (chou2023thenlrgene pages 12-13, hochheiser2023structuralaspectsof pages 1-4). The NACHT domain comprises four conserved subdomains: the nucleotide-binding domain (NBD, ~155 aa, three-layered αβα sandwich containing Walker A and Walker B motifs for ATP/ADP coordination), helical domain 1 (HD1, ~60 aa four-helix bundle), winged helix domain (WHD, ~107 aa), and helical domain 2 (HD2) (hochheiser2023structuralaspectsof pages 4-6, ohto2022activationandregulation pages 1-2). An additional N-terminal FISNA subdomain forms a lid over the nucleotide-binding site (hochheiser2023structuralaspectsof pages 4-6). The core NOD module averages 322 residues across human NLRs (hochheiser2023structuralaspectsof pages 4-6).

3. **C-terminal leucine-rich repeat (LRR) domain**: Composed of tandem repeats of ~20–30 amino acids forming a curved solenoid structure, serving as the ligand-sensing and auto-inhibitory module (swain2025nodlikereceptorsin pages 8-9, zhou2023nodlikereceptorsignaling pages 2-4).

NLR proteins function as molecular switches regulated by nucleotide binding. In the autoinhibited state, ADP binding creates a compact closed conformation stabilized by interactions between HD2, LRR, and NACHT subdomains (chou2023thenlrgene pages 12-13). Upon activation, ATP binding induces conformational changes enabling oligomerization and assembly of signaling platforms, including inflammasomes (ohto2022activationandregulation pages 1-2, hochheiser2023structuralaspectsof pages 1-4).

### Conserved Catalytic and Binding Residues

The Walker A motif (GxxGxGK[T/S]) within the NBD coordinates nucleotide phosphate binding, while the Walker B motif provides the catalytic residue for NTPase activity (hochheiser2023structuralaspectsof pages 1-4). Cryo-EM structures of NLRP3 have shown that the sulfonylurea group of the inhibitor CRID3/MCC950 interacts directly with the Walker A motif and is sandwiched between two arginine residues from opposing sites within the NACHT domain, explaining specificity (hochheiser2023structuralaspectsof pages 1-4). In the NACHT domains of NLRPs, a conserved acidic amino acid (Asp) contributes to nucleotide coordination (hochheiser2023structuralaspectsof pages 4-6).

### Key Structural Distinction: Animal NACHT vs. Plant NB-ARC

Critically, animal NLRs possess the **NACHT domain** subclass (named for NAIP, CIITA, HET-E, and TP1), while plant NLRs possess the **NB-ARC domain** subclass (named for APAF-1, R proteins, and CED-4) (maruta2022structuralbasisof pages 1-2). Both belong to the STAND family but have been proposed to have independent evolutionary origins — representing convergent evolution rather than shared ancestry (maruta2022structuralbasisof pages 1-2). A key structural difference is that the plant NB-ARC module lacks the HD2 domain present in animal NACHT domains (chou2023thenlrgene pages 1-3).

---

## 2. InterPro2GO Mapping Appropriateness

The PTHR24106 entry currently has **no InterPro2GO terms mapped**. This section evaluates whether this absence is appropriate by analyzing candidate GO terms against the family's functional diversity.

The following table provides a systematic assessment of candidate GO terms that might be considered for family-wide mapping:

| Candidate GO term | Family-wide applicability to PTHR24106 | Why it is or is not appropriate for all matched proteins | Recommendation |
|---|---|---|---|
| ATP binding (GO:0005524) | **Possibly broad structural property, but not safely universal as an experimentally justified family-wide function** | Many animal NLRs share a conserved NACHT P-loop NTPase core with Walker motifs and ATP/ADP-dependent conformational switching, but the family represented by this InterPro/PANTHER entry is functionally heterogeneous and may include divergent members where ATP binding is inferred from fold rather than demonstrated; mapping this generic term would add little biological specificity and risks over-generalization across highly diverged taxa and subfamilies (hochheiser2023structuralaspectsof pages 1-4, chou2023thenlrgene pages 12-13, sundaram2024thenlrfamily pages 4-6) | **REJECT** |
| innate immune response (GO:0045087) | **No; only a subset** | Many metazoan NLRs do function in innate immunity, but others act mainly in MHC transcriptional control (CIITA, NLRC5), reproduction/embryogenesis (multiple NLRPs), metabolism, hematopoiesis, or fungal allorecognition/self-nonself pathways rather than canonical innate immune response. Taxonomic spread beyond animals also makes this process term unsafe at family level (almeidadasilva2023theroleof pages 3-5, sundaram2024thenlrfamily pages 6-7, sundaram2024thenlrfamily pages 11-12, daskalov2023emergenceofthe pages 4-6, sundaram2024thenlrfamily pages 48-49, chou2023thenlrgene pages 11-12) | **REJECT** |
| defense response (GO:0006952) | **No; too broad and not true for all members** | Some NLRs mediate host defense, but others negatively regulate inflammation, control antigen-presentation genes, or function in oocyte/embryo biology. In fungi, NLRs are heavily involved in allorecognition and regulated cell death, not necessarily defense response in the GO sense for every member. This term would over-annotate many regulatory and developmental NLRs (chou2023thenlrgene pages 18-18, daskalov2023emergenceofthe pages 4-6, wojciechowski2022exploringadiverse pages 1-2, chou2023thenlrgene pages 18-19, chou2023thenlrgene pages 4-6) | **REJECT** |
| inflammatory response (GO:0006954) | **No; only some subfamilies/members** | Inflammasome-forming NLRs such as NLRP1, NLRP3, and NLRC4 strongly promote inflammatory cytokine maturation, but several NLRs instead suppress NF-κB, IFN, or inflammasome pathways (NLRC3, NLRX1, NLRP12, NLRP4), and others are primarily reproductive or transcriptional regulators. Opposite-direction regulation within the family makes this inappropriate family-wide (sundaram2024thenlrfamily pages 6-7, chou2023thenlrgene pages 10-11, zhou2023nodlikereceptorsignaling pages 19-20, sundaram2024thenlrfamily pages 11-12, chou2023thenlrgene pages 9-10) | **REJECT** |
| inflammasome complex (GO:0061702) | **No; restricted to specific inflammasome-forming NLRs** | This cellular component/process association is valid only for specific members such as NAIP/NLRC4 and selected NLRPs (for example NLRP1, NLRP3, NLRP6, NLRP9, context-dependent NLRP12/NLRP10). CIITA, NLRC5, NOD1/2, NLRC3, NLRX1, and many reproductive NLRPs do not have this as a core universal property (almeidadasilva2023theroleof pages 3-5, zhou2023nodlikereceptorsignaling pages 2-4, sundaram2024thenlrfamily pages 4-6, sundaram2024thenlrfamily pages 11-12, sundaram2024thenlrfamily pages 7-9) | **REJECT** |
| cytoplasm (GO:0005737) | **No; too generic and not universal** | Many NLRs are cytosolic, but some have specialized localization or trafficking behavior; for example NLRX1 is mitochondrial, and transcriptional regulators such as CIITA and NLRC5 shuttle to or function in the nucleus in MHC gene regulation contexts. The term is also too generic to be very informative (zhou2023nodlikereceptorsignaling pages 2-4, sundaram2024thenlrfamily pages 11-12, sundaram2024thenlrfamily pages 7-9, chou2023thenlrgene pages 18-18) | **REJECT** |
| protein binding (GO:0005515) | **Essentially yes in a trivial sense, but not useful** | NLRs act through extensive homotypic and heterotypic protein interactions via CARD, PYD, BIR, NACHT, or LRR-mediated assemblies, but "protein binding" is an extremely generic GO term that contributes little functional specificity and is generally unsuitable as a core family-wide InterPro2GO mapping (hochheiser2023structuralaspectsof pages 4-6, ohto2022activationandregulation pages 1-2, zhou2023nodlikereceptorsignaling pages 2-4, chou2023thenlrgene pages 12-13) | **REJECT** |
| cysteine-type endopeptidase activity (GO:0004197) | **No; false for the family** | NLRs are receptors/scaffolds/regulators, not the caspase proteases themselves. Some NLRs recruit or activate caspase-1 in inflammasomes, but they do not generally possess cysteine-type endopeptidase catalytic activity. Assigning this would be a categorical error (hochheiser2023structuralaspectsof pages 1-4, zhou2023nodlikereceptorsignaling pages 2-4, sundaram2024thenlrfamily pages 6-7, sundaram2024thenlrfamily pages 4-6) | **REJECT** |


*Table: This table evaluates common candidate GO terms for the PTHR24106 NLR family and shows why none are appropriate as blanket family-wide InterPro2GO mappings. It is useful for demonstrating that the family is too functionally diverse and taxonomically broad for safe propagation of these GO annotations.*

**Assessment Summary**: The absence of InterPro2GO mappings for PTHR24106 is scientifically well-justified. The NLR family is extraordinarily functionally heterogeneous. Within humans alone, the 22 NLR proteins span at least five distinct functional categories: inflammasome-forming pattern recognition receptors, MHC transcriptional regulators, negative regulators of inflammatory signaling, reproductive/developmental regulators, and metabolic regulators (almeidadasilva2023theroleof pages 3-5, zhou2023nodlikereceptorsignaling pages 2-4, sundaram2024thenlrfamily pages 11-12). When taxonomic breadth is considered (35,463 proteins across 2,720 taxa including animals, fungi, and potentially plants and bacteria), no single GO term — whether molecular function, biological process, or cellular component — can be safely applied to all matched proteins without systematically over-annotating a substantial fraction.

Even the most conserved structural feature (ATP/nucleotide binding via the NACHT domain) is insufficiently specific as a GO annotation, and whether all matched members retain functional ATPase activity has not been universally demonstrated (sundaram2024thenlrfamily pages 4-6, hochheiser2023structuralaspectsof pages 1-4).

---

## 3. Functional Divergence Across the Family

The NLR family exhibits extreme functional divergence, with subfamilies performing fundamentally different — and sometimes opposite — biological roles.

| Subfamily | N-terminal Domain | Key Members | Primary Function | Inflammasome Formation | Notable Roles |
|---|---|---|---|---|---|
| NLRA | Acidic transactivation domain (AD) | CIITA | Transcriptional co-activator; non-inflammasome regulator of adaptive immunity genes | No | Master regulator of MHC class II expression; links innate sensing architecture to antigen-presentation control, showing that not all NLRs are PRR signaling activators (almeidadasilva2023theroleof pages 3-5, zhou2023nodlikereceptorsignaling pages 2-4, sundaram2024thenlrfamily pages 6-7, sundaram2024thenlrfamily pages 4-6) |
| NLRB | BIR (baculoviral inhibitor of apoptosis repeat) | NAIPs | Sensor of bacterial ligands; activates downstream NLRC4 rather than acting alone | Indirect: NAIPs nucleate the NAIP-NLRC4 inflammasome | Detects flagellin and type III secretion system components; exemplifies ligand-specific upstream activation module rather than a generic NLR function (almeidadasilva2023theroleof pages 3-5, zhou2023nodlikereceptorsignaling pages 2-4, sundaram2024thenlrfamily pages 6-7) |
| NLRC | CARD | NOD1, NOD2, NLRC3, NLRC4, NLRC5 | Mixed functions: peptidoglycan sensing and NF-κB/MAPK activation (NOD1/2); negative regulation of NF-κB, IFN, STING, and mTOR pathways (NLRC3); inflammasome scaffold (NLRC4); transcriptional regulation of MHC class I (NLRC5) | Mixed: NLRC4 yes; NOD1/2, NLRC3, NLRC5 generally no | Includes both positive and negative immune regulators plus MHC-I transactivator; disease links include Crohn disease/Blau syndrome (NOD2), infection defense, inflammatory disease, and cancer-related signaling control (almeidadasilva2023theroleof pages 3-5, zhou2023nodlikereceptorsignaling pages 2-4, sundaram2024thenlrfamily pages 6-7, sundaram2024thenlrfamily pages 7-9, chou2023thenlrgene pages 10-11, zhou2023nodlikereceptorsignaling pages 19-20) |
| NLRP | PYD (with exceptions such as NLRP1 also carrying FIIND and CARD; NLRP10 lacking LRR) | NLRP1, NLRP3, NLRP6, NLRP9, NLRP10, NLRP12, NLRP2, NLRP4, NLRP5, NLRP7, NLRP14 | Highly heterogeneous: canonical inflammasome sensors; negative regulators of NF-κB/IFN; reproductive and embryonic regulators | Mixed: many yes (NLRP1, NLRP3, NLRP6, NLRP9, NLRP10, sometimes NLRP12); others no or context-dependent | Covers pyroptosis/cytokine maturation, intestinal homeostasis, suppression of inflammation, oocyte/ovary expression, embryogenesis, fertility, imprinting disorders, hydatidiform mole susceptibility, metabolic disease, cancer, and neuroinflammation; strongest evidence that family-wide GO terms would over-annotate (almeidadasilva2023theroleof pages 3-5, almeidadasilva2023theroleof pages 5-6, sundaram2024thenlrfamily pages 11-12, sundaram2024thenlrfamily pages 7-9, chou2023thenlrgene pages 8-9, chou2023thenlrgene pages 9-10, sundaram2024thenlrfamily pages 48-49, chou2023thenlrgene pages 18-19, chou2023thenlrgene pages 4-6, chou2023thenlrgene pages 11-12, chou2023thenlrgene pages 10-11) |
| NLRX | Atypical/other N-terminal domain; mitochondrial-targeted | NLRX1 | Non-inflammasome regulatory NLR; predominantly negative regulator of antiviral and inflammatory signaling, with autophagy/mitophagy functions | No established canonical inflammasome role as core function | Mitochondrial localization; dampens RIG-I-MAVS, TRAF6-NF-κB, and type I IFN pathways; regulates ROS, autophagy, and mitophagy, illustrating strong subfamily specialization away from classical PRR signaling (sundaram2024thenlrfamily pages 11-12, chou2023thenlrgene pages 10-11, chou2023thenlrgene pages 18-18, chou2023thenlrgene pages 9-10) |


*Table: This table summarizes the five major NLR subfamilies by domain architecture, representative members, and core functions. It highlights the marked functional divergence within the NLR family, supporting the conclusion that blanket GO annotation at the family level would be over-broad.*

### Major Functional Categories

**A. Inflammasome-Forming NLRs (Positive Immune Activation)**
NLRP1 (the first NLR shown to assemble an inflammasome), NLRP3 (the most extensively studied), and NLRC4 (activated by NAIP sensor proteins) form canonical inflammasomes that recruit and activate caspase-1, leading to processing of pro-IL-1β and pro-IL-18, and induction of pyroptotic cell death (zhou2023nodlikereceptorsignaling pages 2-4, sundaram2024thenlrfamily pages 4-6, sundaram2024thenlrfamily pages 7-9). Additional NLRPs including NLRP6, NLRP9, NLRP10, and context-dependently NLRP12 also form inflammasomes (sundaram2024thenlrfamily pages 11-12).

**B. MHC Transcriptional Regulators**
CIITA (NLRA subfamily) is a master transcriptional co-activator of MHC class II genes, while NLRC5 controls MHC class I expression (zhou2023nodlikereceptorsignaling pages 2-4, sundaram2024thenlrfamily pages 6-7, sundaram2024thenlrfamily pages 7-9). These NLRs function as nuclear-shuttling transcriptional regulators, a role fundamentally distinct from cytoplasmic pattern recognition.

**C. Negative Regulators of Immune Signaling (Anti-Inflammatory)**
Multiple NLR family members actively suppress immune activation, performing the **opposite** function to inflammasome-forming members. NLRC3 negatively regulates NF-κB signaling, type I interferon responses, STING-mediated signaling, and PI3K-mTOR pathways (chou2023thenlrgene pages 10-11, chou2023thenlrgene pages 18-18, sundaram2024thenlrfamily pages 6-7, zhou2023nodlikereceptorsignaling pages 2-4). NLRX1 attenuates RIG-I-MAVS, TRAF6-NF-κB, and type I IFN signaling from its unique mitochondrial localization (chou2023thenlrgene pages 18-18, sundaram2024thenlrfamily pages 11-12, chou2023thenlrgene pages 9-10). NLRP12 suppresses both canonical and non-canonical NF-κB signaling (chou2023thenlrgene pages 18-18, chou2023thenlrgene pages 9-10). NLRP4 negatively regulates NF-κB and type I IFN signaling (chou2023thenlrgene pages 10-11, sundaram2024thenlrfamily pages 11-12). This opposing functionality within the same family is a critical reason that process-level GO terms (whether "positive regulation" or "negative regulation" of inflammation) cannot be applied family-wide.

**D. Reproductive and Developmental Regulators**
A large cluster of NLRP genes (NLRP2, NLRP4, NLRP5, NLRP7, NLRP8, NLRP9, NLRP11, NLRP13, NLRP14) are highly expressed in oocytes and ovaries with roles in embryogenesis, pre-implantation development, and fertility (sundaram2024thenlrfamily pages 48-49, chou2023thenlrgene pages 11-12, chou2023thenlrgene pages 10-11). NLRP5 mediates mitochondrial function in oocytes and is critical for the subcortical maternal complex (SCMC) (chou2023thenlrgene pages 11-12). NLRP7 (primate-specific) mutations cause recurrent hydatidiform moles (chou2023thenlrgene pages 18-19, chou2023thenlrgene pages 4-6). NLRP14 regulates spermatogenesis and primordial germ cell differentiation (chou2023thenlrgene pages 10-11).

**E. Metabolic and Other Regulators**
NLRP3 is broadly implicated in metabolic disorders including obesity, diabetes, atherosclerosis, and gout (sundaram2024thenlrfamily pages 48-49). NLRC3 has been identified as protective against colorectal cancer via PI3K-mTOR suppression (sundaram2024thenlrfamily pages 6-7, chou2023thenlrgene pages 10-11). NLRX1 regulates autophagy and mitophagy (sundaram2024thenlrfamily pages 11-12). Nlrc3 has also been shown to regulate hematopoietic stem cell emergence via Notch signaling in vertebrates, a function entirely outside canonical innate immunity.

### Fungal NLR Neo-Functionalization
Fungal NLRs represent a dramatic case of functional divergence. In fungi such as *Podospora anserina*, NLRs primarily control **allorecognition** (self/non-self discrimination between conspecific individuals) through vegetative incompatibility — triggering regulated cell death when genetically incompatible hyphae fuse (daskalov2023emergenceofthe pages 4-6, daskalov2023emergenceofthe pages 2-4, wojciechowski2022exploringadiverse pages 2-3). Fungal NLRs employ at least 14 different N-terminal effector domain types, many with enzymatic activities, and some utilize unique amyloid-based signaling through prion-like fold transfer (wojciechowski2022exploringadiverse pages 1-2, daskalov2023emergenceofthe pages 7-9, wojciechowski2022exploringadiverse pages 3-5). Only a small fraction of fungal NLRs function in allorecognition; the broader repertoire likely mediates xenorecognition (immune defense against foreign organisms) (daskalov2023emergenceofthe pages 9-11). Fungal NLR gene numbers are highly variable (median 41, up to 602 in some species) (daskalov2023emergenceofthe pages 7-9).

---

## 4. Taxonomic Scope

### Distribution Across Kingdoms of Life

NLR genes are distributed across all three domains of life — bacteria, archaea, and eukarya (including algae, fungi, plants, and animals) (sundaram2024thenlrfamily pages 41-45). Specific bacterial examples include *Streptomyces coelicolor* and *Rickettsia conorii*, and prokaryotic antiviral STAND (Avs) proteins have been recently described (sundaram2024thenlrfamily pages 41-45, chou2023thenlrgene pages 1-3).

**In animals**, NLR diversity includes representatives from sponges (Porifera) through vertebrates. The demosponge *Dysidea avara* contains 126 *bona fide* NLR genes (NACHT+LRR containing), including NLRC, NLRD, and NLRX categories, indicating early emergence in metazoan evolution (sundaram2024thenlrfamily pages 41-45). Invertebrates from sponge to amphioxus possess NLRC and/or NLRD forms (sundaram2024thenlrfamily pages 41-45). In mammals, 22 NLR genes are identified in humans and more (e.g., 19 NLRPs) in mice (ohto2022activationandregulation pages 1-2, sundaram2024thenlrfamily pages 7-9). Notably, NLRs are absent from *Drosophila melanogaster* and *Caenorhabditis elegans* genomes, indicating lineage-specific losses (sundaram2024thenlrfamily pages 41-45).

**In plants**, NLRs (NBS-LRR proteins) represent the largest class of disease resistance proteins and are subdivided into CC-NLRs (CNLs), TIR-NLRs (TNLs), and RPW8-NLRs (RNLs) (maruta2022structuralbasisof pages 1-2, sundaram2024thenlrfamily pages 4-6, chou2023thenlrgene pages 1-3). Plant genomes can harbor hundreds of NLR genes (over 80,000 sequences in NLRscape database). However, plant NLRs use the NB-ARC domain rather than the NACHT domain, and plant and animal NLRs have been proposed to have **independent evolutionary origins** (maruta2022structuralbasisof pages 1-2).

**In fungi**, NLR-like proteins with NACHT/NOD domains and diverse effector domains are widespread, particularly in ascomycetes and basidiomycetes (wojciechowski2022exploringadiverse pages 1-2, daskalov2023emergenceofthe pages 7-9, amentvelasquez2025nodlikereceptorgenes pages 30-35). Fungal NLRs with HIC (high internal conservation) repeats have been found across Dikarya, and similar elements occur in animals, plants, and bacteria (amentvelasquez2025nodlikereceptorgenes pages 30-35).

### Implications for GO Annotation

The vast taxonomic spread means that any GO biological process term related to vertebrate-specific pathways (e.g., "inflammasome-mediated signaling pathway," "adaptive immune response regulation," "MHC class II biosynthetic process") would be inapplicable to the majority of matched proteins from non-vertebrate taxa. Fungal NLRs function primarily in allorecognition and regulated cell death rather than canonical innate immune pathways (daskalov2023emergenceofthe pages 4-6, daskalov2023emergenceofthe pages 2-4). The independent evolutionary origins of plant and animal NLRs further complicate any attempt at unified functional annotation.

---

## 5. Over-Annotation Verdict

### Summary Assessment

The PTHR24106 entry (NOD-like receptor family) currently has **no InterPro2GO terms mapped**. Based on the comprehensive evidence gathered, this absence is **scientifically appropriate and should be maintained**. The NLR family as defined by PTHR24106 is one of the most functionally heterogeneous protein families in biology, with members performing:

- **Opposite regulatory functions** within the same pathway (pro-inflammatory inflammasome sensors vs. anti-inflammatory negative regulators of NF-κB and IFN) (chou2023thenlrgene pages 10-11, chou2023thenlrgene pages 18-18, chou2023thenlrgene pages 9-10)
- **Fundamentally different biological processes** (innate immune sensing, MHC transcriptional regulation, oocyte/embryo development, hematopoiesis, metabolic regulation, autophagy) (sundaram2024thenlrfamily pages 48-49, chou2023thenlrgene pages 11-12, zhou2023nodlikereceptorsignaling pages 2-4)
- **Kingdom-specific functions** (animal pattern recognition, plant effector-triggered immunity, fungal allorecognition) with proposed convergent rather than homologous evolutionary origins for plant vs. animal members (maruta2022structuralbasisof pages 1-2, daskalov2023emergenceofthe pages 4-6)
- **Lineage-specific expansions and losses**, with gene numbers varying from 0 (in *Drosophila*) to >600 (in some fungi) (sundaram2024thenlrfamily pages 41-45, daskalov2023emergenceofthe pages 7-9)

### Recommended GO Action Pattern

| Action | Recommendation |
|---|---|
| **Current status (no InterPro2GO mappings)** | **ACCEPT** — The absence of mappings is correct |
| **Adding any biological process term** | **NOT RECOMMENDED** — No process is universal to all 35,463 proteins |
| **Adding "ATP binding" (GO:0005524)** | **NOT RECOMMENDED** — Too generic, and not experimentally verified for all members |
| **Adding "innate immune response" (GO:0045087)** | **NOT RECOMMENDED** — False for reproductive NLRPs, MHC regulators, fungal allorecognition NLRs |
| **GO annotations for subfamilies** | **STRONGLY RECOMMENDED** — GO terms should be assigned at the subfamily/child entry level (e.g., NLRP3-specific inflammasome terms, CIITA-specific MHC-II regulation terms, NLRC3-specific negative regulation terms) |

### Recommendation for InterPro

The current approach of having no InterPro2GO mappings at the PTHR24106 family level is the correct decision. The 12 subfamilies noted for this entry should each be evaluated independently for appropriate GO term mappings. Specific recommendations:

1. **Inflammasome-forming subfamilies** (e.g., NLRP3, NLRP1, NLRC4): Could receive GO terms for "inflammasome complex" (GO:0061702), "positive regulation of inflammatory response," and "caspase-1 activation."
2. **MHC regulatory subfamilies** (CIITA, NLRC5): Should receive GO terms for "positive regulation of MHC class II biosynthetic process" or "MHC class I biosynthetic process" respectively.
3. **Negative regulatory subfamilies** (NLRC3, NLRX1): Could receive "negative regulation of NF-kappaB transcription factor activity" or "negative regulation of type I interferon production."
4. **Reproductive NLRPs** (NLRP2, NLRP5, NLRP7): Could receive appropriate developmental/reproductive GO terms at the subfamily level.

The family-level entry should remain GO-term-free, as any mapping would constitute systematic over-annotation across the majority of matched proteins. This represents a textbook case where functional annotation should be **pushed down to child/subfamily entries** rather than applied at the parent family level.

**Final Verdict: ACCEPT (current absence of InterPro2GO mappings is sound)** — with a strong recommendation to ensure appropriate GO terms are assigned at subfamily-level entries rather than at this functionally heterogeneous family level.

References

1. (hochheiser2023structuralaspectsof pages 1-4): Inga V. Hochheiser and Matthias Geyer. Structural aspects of inflammasomes forming NOD-like receptors, pages 215-233. Elsevier, Jan 2023. URL: https://doi.org/10.1016/b978-0-323-91802-2.00022-0, doi:10.1016/b978-0-323-91802-2.00022-0. This article has 2 citations.

2. (ohto2022activationandregulation pages 1-2): Umeharu Ohto. Activation and regulation mechanisms of nod-like receptors based on structural biology. Frontiers in Immunology, Sep 2022. URL: https://doi.org/10.3389/fimmu.2022.953530, doi:10.3389/fimmu.2022.953530. This article has 71 citations and is from a peer-reviewed journal.

3. (hochheiser2023structuralaspectsof pages 4-6): Inga V. Hochheiser and Matthias Geyer. Structural aspects of inflammasomes forming NOD-like receptors, pages 215-233. Elsevier, Jan 2023. URL: https://doi.org/10.1016/b978-0-323-91802-2.00022-0, doi:10.1016/b978-0-323-91802-2.00022-0. This article has 2 citations.

4. (zhou2023nodlikereceptorsignaling pages 2-4): Yujie Zhou, Songyan Yu, and Wenyong Zhang. Nod-like receptor signaling pathway in gastrointestinal inflammatory diseases and cancers. International Journal of Molecular Sciences, 24:14511, Sep 2023. URL: https://doi.org/10.3390/ijms241914511, doi:10.3390/ijms241914511. This article has 69 citations.

5. (chou2023thenlrgene pages 12-13): Wei-Chun Chou, Sushmita Jha, Michael W. Linhoff, and Jenny P.-Y. Ting. The nlr gene family: from discovery to present day. Nature Reviews Immunology, 23:635-654, Mar 2023. URL: https://doi.org/10.1038/s41577-023-00849-x, doi:10.1038/s41577-023-00849-x. This article has 221 citations and is from a highest quality peer-reviewed journal.

6. (swain2025nodlikereceptorsin pages 8-9): Banikalyan Swain and Kavi R. Miryala. Nod-like receptors in fish: evolution, structure, immune signaling, and targeting for aquaculture vaccine adjuvants. Frontiers in Immunology, Sep 2025. URL: https://doi.org/10.3389/fimmu.2025.1665071, doi:10.3389/fimmu.2025.1665071. This article has 9 citations and is from a peer-reviewed journal.

7. (maruta2022structuralbasisof pages 1-2): Natsumi Maruta, Hayden Burdett, Bryan Y. J. Lim, Xiahao Hu, Sneha Desa, Mohammad Kawsar Manik, and Bostjan Kobe. Structural basis of nlr activation and innate immune signalling in plants. Immunogenetics, 74:5-26, Jan 2022. URL: https://doi.org/10.1007/s00251-021-01242-5, doi:10.1007/s00251-021-01242-5. This article has 130 citations and is from a peer-reviewed journal.

8. (chou2023thenlrgene pages 1-3): Wei-Chun Chou, Sushmita Jha, Michael W. Linhoff, and Jenny P.-Y. Ting. The nlr gene family: from discovery to present day. Nature Reviews Immunology, 23:635-654, Mar 2023. URL: https://doi.org/10.1038/s41577-023-00849-x, doi:10.1038/s41577-023-00849-x. This article has 221 citations and is from a highest quality peer-reviewed journal.

9. (sundaram2024thenlrfamily pages 4-6): Balamurugan Sundaram, Rebecca E. Tweedell, Sivakumar Prasanth Kumar, and Thirumala-Devi Kanneganti. The nlr family of innate immune and cell death sensors. Immunity, 57 4:674-699, Apr 2024. URL: https://doi.org/10.1016/j.immuni.2024.03.012, doi:10.1016/j.immuni.2024.03.012. This article has 197 citations and is from a highest quality peer-reviewed journal.

10. (almeidadasilva2023theroleof pages 3-5): Cássio Luiz Coutinho Almeida-da-Silva, Luiz Eduardo Baggio Savio, Robson Coutinho-Silva, and David M. Ojcius. The role of nod-like receptors in innate immunity. Frontiers in Immunology, Mar 2023. URL: https://doi.org/10.3389/fimmu.2023.1122586, doi:10.3389/fimmu.2023.1122586. This article has 187 citations and is from a peer-reviewed journal.

11. (sundaram2024thenlrfamily pages 6-7): Balamurugan Sundaram, Rebecca E. Tweedell, Sivakumar Prasanth Kumar, and Thirumala-Devi Kanneganti. The nlr family of innate immune and cell death sensors. Immunity, 57 4:674-699, Apr 2024. URL: https://doi.org/10.1016/j.immuni.2024.03.012, doi:10.1016/j.immuni.2024.03.012. This article has 197 citations and is from a highest quality peer-reviewed journal.

12. (sundaram2024thenlrfamily pages 11-12): Balamurugan Sundaram, Rebecca E. Tweedell, Sivakumar Prasanth Kumar, and Thirumala-Devi Kanneganti. The nlr family of innate immune and cell death sensors. Immunity, 57 4:674-699, Apr 2024. URL: https://doi.org/10.1016/j.immuni.2024.03.012, doi:10.1016/j.immuni.2024.03.012. This article has 197 citations and is from a highest quality peer-reviewed journal.

13. (daskalov2023emergenceofthe pages 4-6): Asen Daskalov. Emergence of the fungal immune system. iScience, 26:106793, Jun 2023. URL: https://doi.org/10.1016/j.isci.2023.106793, doi:10.1016/j.isci.2023.106793. This article has 39 citations and is from a peer-reviewed journal.

14. (sundaram2024thenlrfamily pages 48-49): Balamurugan Sundaram, Rebecca E. Tweedell, Sivakumar Prasanth Kumar, and Thirumala-Devi Kanneganti. The nlr family of innate immune and cell death sensors. Immunity, 57 4:674-699, Apr 2024. URL: https://doi.org/10.1016/j.immuni.2024.03.012, doi:10.1016/j.immuni.2024.03.012. This article has 197 citations and is from a highest quality peer-reviewed journal.

15. (chou2023thenlrgene pages 11-12): Wei-Chun Chou, Sushmita Jha, Michael W. Linhoff, and Jenny P.-Y. Ting. The nlr gene family: from discovery to present day. Nature Reviews Immunology, 23:635-654, Mar 2023. URL: https://doi.org/10.1038/s41577-023-00849-x, doi:10.1038/s41577-023-00849-x. This article has 221 citations and is from a highest quality peer-reviewed journal.

16. (chou2023thenlrgene pages 18-18): Wei-Chun Chou, Sushmita Jha, Michael W. Linhoff, and Jenny P.-Y. Ting. The nlr gene family: from discovery to present day. Nature Reviews Immunology, 23:635-654, Mar 2023. URL: https://doi.org/10.1038/s41577-023-00849-x, doi:10.1038/s41577-023-00849-x. This article has 221 citations and is from a highest quality peer-reviewed journal.

17. (wojciechowski2022exploringadiverse pages 1-2): Jakub W. Wojciechowski, Emirhan Tekoglu, Marlena Gąsior-Głogowska, Virginie Coustou, Natalia Szulc, Monika Szefczyk, Marta Kopaczyńska, Sven J. Saupe, and Witold Dyrka. Exploring a diverse world of effector domains and amyloid signaling motifs in fungal nlr proteins. PLOS Computational Biology, 18:e1010787, Dec 2022. URL: https://doi.org/10.1371/journal.pcbi.1010787, doi:10.1371/journal.pcbi.1010787. This article has 20 citations and is from a highest quality peer-reviewed journal.

18. (chou2023thenlrgene pages 18-19): Wei-Chun Chou, Sushmita Jha, Michael W. Linhoff, and Jenny P.-Y. Ting. The nlr gene family: from discovery to present day. Nature Reviews Immunology, 23:635-654, Mar 2023. URL: https://doi.org/10.1038/s41577-023-00849-x, doi:10.1038/s41577-023-00849-x. This article has 221 citations and is from a highest quality peer-reviewed journal.

19. (chou2023thenlrgene pages 4-6): Wei-Chun Chou, Sushmita Jha, Michael W. Linhoff, and Jenny P.-Y. Ting. The nlr gene family: from discovery to present day. Nature Reviews Immunology, 23:635-654, Mar 2023. URL: https://doi.org/10.1038/s41577-023-00849-x, doi:10.1038/s41577-023-00849-x. This article has 221 citations and is from a highest quality peer-reviewed journal.

20. (chou2023thenlrgene pages 10-11): Wei-Chun Chou, Sushmita Jha, Michael W. Linhoff, and Jenny P.-Y. Ting. The nlr gene family: from discovery to present day. Nature Reviews Immunology, 23:635-654, Mar 2023. URL: https://doi.org/10.1038/s41577-023-00849-x, doi:10.1038/s41577-023-00849-x. This article has 221 citations and is from a highest quality peer-reviewed journal.

21. (zhou2023nodlikereceptorsignaling pages 19-20): Yujie Zhou, Songyan Yu, and Wenyong Zhang. Nod-like receptor signaling pathway in gastrointestinal inflammatory diseases and cancers. International Journal of Molecular Sciences, 24:14511, Sep 2023. URL: https://doi.org/10.3390/ijms241914511, doi:10.3390/ijms241914511. This article has 69 citations.

22. (chou2023thenlrgene pages 9-10): Wei-Chun Chou, Sushmita Jha, Michael W. Linhoff, and Jenny P.-Y. Ting. The nlr gene family: from discovery to present day. Nature Reviews Immunology, 23:635-654, Mar 2023. URL: https://doi.org/10.1038/s41577-023-00849-x, doi:10.1038/s41577-023-00849-x. This article has 221 citations and is from a highest quality peer-reviewed journal.

23. (sundaram2024thenlrfamily pages 7-9): Balamurugan Sundaram, Rebecca E. Tweedell, Sivakumar Prasanth Kumar, and Thirumala-Devi Kanneganti. The nlr family of innate immune and cell death sensors. Immunity, 57 4:674-699, Apr 2024. URL: https://doi.org/10.1016/j.immuni.2024.03.012, doi:10.1016/j.immuni.2024.03.012. This article has 197 citations and is from a highest quality peer-reviewed journal.

24. (almeidadasilva2023theroleof pages 5-6): Cássio Luiz Coutinho Almeida-da-Silva, Luiz Eduardo Baggio Savio, Robson Coutinho-Silva, and David M. Ojcius. The role of nod-like receptors in innate immunity. Frontiers in Immunology, Mar 2023. URL: https://doi.org/10.3389/fimmu.2023.1122586, doi:10.3389/fimmu.2023.1122586. This article has 187 citations and is from a peer-reviewed journal.

25. (chou2023thenlrgene pages 8-9): Wei-Chun Chou, Sushmita Jha, Michael W. Linhoff, and Jenny P.-Y. Ting. The nlr gene family: from discovery to present day. Nature Reviews Immunology, 23:635-654, Mar 2023. URL: https://doi.org/10.1038/s41577-023-00849-x, doi:10.1038/s41577-023-00849-x. This article has 221 citations and is from a highest quality peer-reviewed journal.

26. (daskalov2023emergenceofthe pages 2-4): Asen Daskalov. Emergence of the fungal immune system. iScience, 26:106793, Jun 2023. URL: https://doi.org/10.1016/j.isci.2023.106793, doi:10.1016/j.isci.2023.106793. This article has 39 citations and is from a peer-reviewed journal.

27. (wojciechowski2022exploringadiverse pages 2-3): Jakub W. Wojciechowski, Emirhan Tekoglu, Marlena Gąsior-Głogowska, Virginie Coustou, Natalia Szulc, Monika Szefczyk, Marta Kopaczyńska, Sven J. Saupe, and Witold Dyrka. Exploring a diverse world of effector domains and amyloid signaling motifs in fungal nlr proteins. PLOS Computational Biology, 18:e1010787, Dec 2022. URL: https://doi.org/10.1371/journal.pcbi.1010787, doi:10.1371/journal.pcbi.1010787. This article has 20 citations and is from a highest quality peer-reviewed journal.

28. (daskalov2023emergenceofthe pages 7-9): Asen Daskalov. Emergence of the fungal immune system. iScience, 26:106793, Jun 2023. URL: https://doi.org/10.1016/j.isci.2023.106793, doi:10.1016/j.isci.2023.106793. This article has 39 citations and is from a peer-reviewed journal.

29. (wojciechowski2022exploringadiverse pages 3-5): Jakub W. Wojciechowski, Emirhan Tekoglu, Marlena Gąsior-Głogowska, Virginie Coustou, Natalia Szulc, Monika Szefczyk, Marta Kopaczyńska, Sven J. Saupe, and Witold Dyrka. Exploring a diverse world of effector domains and amyloid signaling motifs in fungal nlr proteins. PLOS Computational Biology, 18:e1010787, Dec 2022. URL: https://doi.org/10.1371/journal.pcbi.1010787, doi:10.1371/journal.pcbi.1010787. This article has 20 citations and is from a highest quality peer-reviewed journal.

30. (daskalov2023emergenceofthe pages 9-11): Asen Daskalov. Emergence of the fungal immune system. iScience, 26:106793, Jun 2023. URL: https://doi.org/10.1016/j.isci.2023.106793, doi:10.1016/j.isci.2023.106793. This article has 39 citations and is from a peer-reviewed journal.

31. (sundaram2024thenlrfamily pages 41-45): Balamurugan Sundaram, Rebecca E. Tweedell, Sivakumar Prasanth Kumar, and Thirumala-Devi Kanneganti. The nlr family of innate immune and cell death sensors. Immunity, 57 4:674-699, Apr 2024. URL: https://doi.org/10.1016/j.immuni.2024.03.012, doi:10.1016/j.immuni.2024.03.012. This article has 197 citations and is from a highest quality peer-reviewed journal.

32. (amentvelasquez2025nodlikereceptorgenes pages 30-35): S. Lorena Ament-Velásquez and Sven J. Saupe. Nod-like receptor genes evolve under diversity-enhancing mechanisms in a fungal species complex. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.29.679196, doi:10.1101/2025.09.29.679196. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR24106-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR24106-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. hochheiser2023structuralaspectsof pages 4-6
2. chou2023thenlrgene pages 12-13
3. hochheiser2023structuralaspectsof pages 1-4
4. maruta2022structuralbasisof pages 1-2
5. chou2023thenlrgene pages 1-3
6. sundaram2024thenlrfamily pages 11-12
7. chou2023thenlrgene pages 11-12
8. chou2023thenlrgene pages 10-11
9. sundaram2024thenlrfamily pages 48-49
10. daskalov2023emergenceofthe pages 9-11
11. daskalov2023emergenceofthe pages 7-9
12. sundaram2024thenlrfamily pages 41-45
13. amentvelasquez2025nodlikereceptorgenes pages 30-35
14. ohto2022activationandregulation pages 1-2
15. zhou2023nodlikereceptorsignaling pages 2-4
16. swain2025nodlikereceptorsin pages 8-9
17. sundaram2024thenlrfamily pages 4-6
18. almeidadasilva2023theroleof pages 3-5
19. sundaram2024thenlrfamily pages 6-7
20. daskalov2023emergenceofthe pages 4-6
21. chou2023thenlrgene pages 18-18
22. wojciechowski2022exploringadiverse pages 1-2
23. chou2023thenlrgene pages 18-19
24. chou2023thenlrgene pages 4-6
25. zhou2023nodlikereceptorsignaling pages 19-20
26. chou2023thenlrgene pages 9-10
27. sundaram2024thenlrfamily pages 7-9
28. almeidadasilva2023theroleof pages 5-6
29. chou2023thenlrgene pages 8-9
30. daskalov2023emergenceofthe pages 2-4
31. wojciechowski2022exploringadiverse pages 2-3
32. wojciechowski2022exploringadiverse pages 3-5
33. T/S
34. https://doi.org/10.1016/b978-0-323-91802-2.00022-0,
35. https://doi.org/10.3389/fimmu.2022.953530,
36. https://doi.org/10.3390/ijms241914511,
37. https://doi.org/10.1038/s41577-023-00849-x,
38. https://doi.org/10.3389/fimmu.2025.1665071,
39. https://doi.org/10.1007/s00251-021-01242-5,
40. https://doi.org/10.1016/j.immuni.2024.03.012,
41. https://doi.org/10.3389/fimmu.2023.1122586,
42. https://doi.org/10.1016/j.isci.2023.106793,
43. https://doi.org/10.1371/journal.pcbi.1010787,
44. https://doi.org/10.1101/2025.09.29.679196,