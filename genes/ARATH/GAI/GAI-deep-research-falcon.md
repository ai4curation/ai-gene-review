Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for GO Annotation Review

## Target

- Gene symbol: GAI
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: Q9LQT8
Entry Name: GAI_ARATH
Gene Name: GAI
Locus Tag: At1g14920 {ECO:0000312|Araport:AT1G14920}
Gene Synonyms: RGA2 {ECO:0000303|PubMed:9237632}
Protein Name: DELLA protein GAI
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702
Function: Transcriptional regulator that acts as a repressor of the gibberellin (GA) signaling pathway. Transcription coactivator of the zinc finger transcription factors GAF1/IDD2 and ENY/IDD1 in regulation of gibberellin homeostasis and signaling (PubMed:25035403). No effect of the BOI proteins on its stability. Probably acts by participating in large multiprotein complexes that repress transcription of GA-inducible genes. Positively regulates XERICO expression. In contrast to RGA, it is less sensitive to GA. Its activity is probably regulated by other phytohormones such as auxin and ethylene. Involved in the regulation of seed dormancy and germination, including glucose-induced delay of seed germination (PubMed:24989044). Involved in the process leading to microtubules (MTs) dissociation in response to gibberellic acid (GA) probably by mediating the translocation of the prefoldin co-chaperone complex from the cytoplasm to the nucleus (PubMed:23583555).
Subcellular Location: Nucleus
Subunit: Interacts directly with the GID2/SLY1 component of the SCF(GID2) complex. Interacts (via N-terminus) with GID1A, GID1B and GID1B (via N-terminus). Interacts with the BOI proteins BOI, BRG1, BRG2, BRG3 and NUP58 (PubMed:15155881, PubMed:15161962, PubMed:15173565, PubMed:16709201, PubMed:19037309, PubMed:23482857, PubMed:23840761). Interacts with TOPP4 (PubMed:15155881, PubMed:15161962, PubMed:15173565, PubMed:16709201, PubMed:19037309, PubMed:23482857, PubMed:23840761, PubMed:25010794). Interacts with TCP14 and TCP15 (PubMed:25655823). Interacts with FLZ5 (Ref.27). Binds to and coactivates GAF1/IDD2 and ENY/IDD1 at the promoter of GA20OX2 gene (PubMed:25035403). Binds to PDF2 and ATML1 (PubMed:24989044). Interacts with the prefoldin alpha subunits PFD3 and PFD5 in the nucleus (PubMed:23583555).
======================

## Research Objective

Prepare a comprehensive literature-backed research report for GO annotation review of the target gene.

Focus on:

1. The core biochemical activity of the gene product and any substrate specificity.
2. The activation or maturation mechanism of the protein, including proteolytic processing if relevant.
3. The best-supported subcellular localization and complexes where the active protein functions.
4. The strongest experimentally supported biological processes in the target organism, or in very close orthologs when transfer is justified.
5. Which annotations appear to reflect core function versus context-specific, pleiotropic, or over-extended roles.
6. Any evidence bearing on apoptosis, developmental cell death, neuronal roles, inflammatory signaling, pyroptosis, synaptic remodeling, protein processing, and localization to cytoplasm, cytosol, nucleus, or signaling complexes.

## Output Requirements

Structure the report as:

1. Executive summary
2. Molecular function
3. Biological process roles
4. Cellular localization and complexes
5. Annotation-risk assessment
6. Key literature

Use citations for all substantive claims.


# Gene research report for GO annotation review: **GAI** (Arabidopsis thaliana; At1g14920; UniProt Q9LQT8)

## 1. Executive summary

**GAI encodes a DELLA-family nuclear transcriptional regulator that represses gibberellin (GA) responses.** GA signaling is primarily mediated by GA binding to the soluble receptor GID1, which enables formation of a GA–GID1–DELLA complex that is recognized by SCF-type E3 ubiquitin ligases containing the F-box protein SLY1 (Arabidopsis) / GID2 (rice), resulting in polyubiquitination and 26S proteasome-dependent DELLA degradation. This pathway is well supported by genetic, biochemical, and structural evidence, including classic gai-1 DELLA-motif deletion alleles that block GA-induced degradation and yield constitutive GA repression. (shani2024highlightsingibberellin pages 7-8, park2013dellaproteinsand pages 1-2)

**Core molecular function (GO-MF):** DELLA proteins lack canonical DNA-binding domains, but act as **transcription co-regulators** (coactivators and/or corepressors) through extensive protein–protein interactions and chromatin association. Evidence includes large-scale interaction screens and promoter association by ChIP/ChIP-seq. (shani2024highlightsingibberellin pages 8-10, zentella2007globalanalysisof pages 1-2)

**GAI-specific mechanistic complexes:** 
- **GAF1/IDD1–GAI–TPR4 transcriptional complexes**: GAI physically associates with the IDD-family transcription factor GAF1 (and related IDD1/ENHYDROUS) and TOPLESS-related corepressor TPR4, binds GA homeostasis/signaling promoters (notably **GA20ox2**), and can activate promoters of **GA20ox2**, **GA3ox1**, and **GID1b** in protoplast reporter assays; GA-driven DELLA degradation switches complex output toward repression. (fukazawa2014dellasfunctionas pages 13-15)
- **Prefoldin (PFD3/PFD5) interaction**: GAI binds prefoldin subunits (PFD5, PFD3) and drives GA-dependent nuclear/cytosolic relocalization of PFD5; under GA-deficient conditions (PAC), PFD5-GFP accumulates in nuclei, and **cytosolic localization is restored ~3 h after GA4** application, linking DELLA abundance to cortical microtubule organization and anisotropic growth. (locascio2013dynamicregulationof pages 1-2, locascio2013dynamicregulationof media 5b391f96)

**Recent developments (2023–2024 prioritized):** A 2024 Plant Physiology synthesis (Shani, Hedden & Sun) consolidates the mechanistic model and provides quantitative summary statistics relevant for GO scoping (e.g., **370 candidate DELLA interactors; >40 validated**, and RGA ChIP-seq association with **421 genes in seedlings and 2,327 genes in inflorescences**), emphasizing that DELLA output is mediated by combinatorial interactions and chromatin association rather than direct DNA binding. (shani2024highlightsingibberellin pages 8-10, shani2024highlightsingibberellin pages 7-8)

**Annotation safety:** No evidence in retrieved plant literature supports annotation of GAI to animal-specific pathways (neuronal/synaptic remodeling, inflammatory signaling, pyroptosis) or to apoptosis; “programmed cell death” appears only as a generic context in one GA-signaling component study and is not linked mechanistically to GAI. (balouri2024gibberellinsignalingthrough pages 1-2)

## 2. Molecular function (GO-MF)

### 2.1 Key concepts and definitions (current understanding)

**DELLA proteins are GRAS-family transcription regulators that function through protein–protein interactions rather than DNA binding.** In Arabidopsis, the DELLA family comprises five genes (RGA, GAI, RGL1, RGL2, RGL3). DELLAs are **nucleus-localized transcription regulators** and do not contain canonical DNA-binding motifs; they regulate transcription by interacting with many transcription factors/regulators and chromatin-associated proteins. (shani2024highlightsingibberellin pages 7-8, zentella2007globalanalysisof pages 1-2)

**Three modes of DELLA transcriptional control** are emphasized in recent synthesis: (i) repression by sequestering/blocking DNA-binding of activators (e.g., PIF3/4), (ii) activation by recruiting/partnering with transcription factors (e.g., ABI3/ABI5, ARRs, IDDs), and (iii) activation by sequestering transcription repressors (e.g., JAZs, SCL3). (shani2024highlightsingibberellin pages 8-10)

### 2.2 Best-supported molecular activities for GAI

**(A) Transcription co-regulator activity (broad, core):** 
- Evidence that DELLAs act as transcriptional regulators and associate with promoters is supported by ChIP experiments identifying promoter association for DELLA targets and by genome-wide binding data (presented for the paralog RGA as a representative DELLA). (zentella2007globalanalysisof pages 1-2, shani2024highlightsingibberellin pages 7-8)

**(B) GAI as a DELLA coactivator with GAF1/IDD factors (GA homeostasis module; relatively direct for GAI):** Fukazawa et al. experimentally identify GAF1 as a DELLA-binding transcription factor (“GAI-associated factor”), show physical association between **GAI and GAF1**, and demonstrate that **GAI and TOPLESS-related corepressors (TPR4)** can assemble into a promoter-associated complex that regulates GA feedback targets including **GA20ox2**, and reporter assays show activation of **GA3ox1** and **GID1b** promoters by the GAF1/GAI complex. (fukazawa2014dellasfunctionas pages 13-15, fukazawa2014dellasfunctionas pages 11-12)

**Important GO implication:** These data support annotation to “transcription co-regulator activity” and to “regulation of GA biosynthetic process / GA homeostasis” as a direct, mechanistically grounded function (rather than only phenotype-level growth repression). (fukazawa2014dellasfunctionas pages 13-15, zentella2007globalanalysisof pages 1-2)

### 2.3 Substrate specificity / biochemical activity

GAI is not an enzyme and no catalytic substrate specificity is supported. Instead, its “activity” is best captured as **protein binding** and **transcriptional co-regulation** within the nucleus and chromatin-associated complexes. (shani2024highlightsingibberellin pages 8-10, zentella2007globalanalysisof pages 1-2)

## 3. Biological process roles (GO-BP)

### 3.1 Core processes strongly supported

**(1) Negative regulation of GA responses and GA-activated signaling**
- DELLA proteins repress GA responses; GID1 and SLY1 activate GA responses by binding and ubiquitinating DELLAs, leading to DELLA degradation. This is central to GA-dependent control of growth and developmental transitions. (park2013dellaproteinsand pages 1-2, shani2024highlightsingibberellin pages 7-8)

**(2) GA homeostasis feedback regulation (direct transcriptional targets)**
- Zentella et al. identify **14 early GA-responsive genes that are also early DELLA-responsive**; for eight, ChIP supports promoter association. The work concludes that DELLAs help establish GA homeostasis by direct feedback on GA biosynthetic and GA receptor gene expression, and that one target, **XERICO**, promotes ABA accumulation antagonizing GA. (zentella2007globalanalysisof pages 1-2)
- Fukazawa et al. provide a GAI-specific mechanism wherein the **GAF1–GAI** complex activates GA homeostasis/signaling promoters (GA20ox2, GA3ox1, GID1b) under GA-deficient conditions, and GA-induced DELLA degradation changes complex behavior. (fukazawa2014dellasfunctionas pages 13-15)

### 3.2 Context-specific / mechanistic process links (supported but narrower)

**(A) Microtubule organization and anisotropic cell expansion via prefoldin sequestration**
- Locascio et al. demonstrate that GAI binds prefoldin subunits (PFD5/PFD3) and that GA availability controls prefoldin subcellular localization: GA deficiency (PAC) leads to nuclear PFD5-GFP accumulation, and **GA4 restores cytosolic localization within ~3 hours**, consistent with a mechanism in which high DELLA levels sequester prefoldin in nuclei, compromising tubulin heterodimer availability and microtubule organization during hypocotyl growth. (locascio2013dynamicregulationof pages 1-2, locascio2013dynamicregulationof media 5b391f96)

**(B) Promoter-bound repression with BOI family proteins affecting GA responses**
- Park et al. identify BOI/BRG RING domain proteins that interact with DELLAs, are targeted with DELLAs to promoters of GA-responsive genes, and repress their expression. Genetic analysis indicates that GAI requires BOIs to inhibit a subset of GA responses; boiQ mutants show higher seed germination frequency under PAC, and accelerated developmental transitions consistent with enhanced GA signaling. (park2013dellaproteinsand pages 1-2)

### 3.3 Recent developments and expert synthesis (2024 emphasis)

A major 2024 Plant Physiology synthesis provides a consolidated, current model that DELLA proteins (including GAI) are master regulators integrating internal/environmental cues through extensive interaction networks and chromatin recruitment. It reports: 
- **Three GID1 paralogs** in Arabidopsis (GID1A/B/C), with cytoplasm+nucleus localization for GID1. (shani2024highlightsingibberellin pages 8-10)
- Interaction network breadth: **370 candidate DELLA interactors**, with **>40 verified** by co-IP and/or genetics. (shani2024highlightsingibberellin pages 8-10)
- Genome-wide chromatin association via the DELLA paralog RGA: **421 associated genes in seedlings** and **2,327 in inflorescences** (as an indicator of the scale of direct chromatin engagement by DELLA proteins). (shani2024highlightsingibberellin pages 7-8)

These statistics support a conservative GO approach: annotate GAI to core GA-signaling repression and transcription co-regulation, and treat many distal developmental outputs as pleiotropic unless GAI-specific mechanistic evidence exists. (shani2024highlightsingibberellin pages 8-10, shani2024highlightsingibberellin pages 7-8)

## 4. Cellular localization and complexes (GO-CC)

### 4.1 Subcellular localization

**Nucleus is the best-supported location for functional GAI/DELLA action.** DELLA proteins are described as nucleus-localized transcription regulators; DELLA-GFP fusions are nuclear in transgenic studies, and GAI-dependent BiFC signals with interactors can be nuclear. (zentella2007globalanalysisof pages 1-2, locascio2013dynamicregulationof pages 1-2)

**GID1 is nucleocytoplasmic**, consistent with GA perception enabling receptor–DELLA complex formation across compartments, followed by nuclear transcriptional control. (shani2024highlightsingibberellin pages 8-10)

### 4.2 Complexes and interaction partners relevant for GO curation

**GAI–GAF1/IDD1–TPR4 promoter-associated complex (GA homeostasis/signaling):** Supported by Y2H domain mapping, co-IP, BiFC, ChIP at GA20ox2, and protoplast promoter-reporter assays for GA20ox2/GA3ox1/GID1b. (fukazawa2014dellasfunctionas pages 13-15, fukazawa2014dellasfunctionas pages 11-12)

**GAI–prefoldin (PFD3/PFD5) interaction module:** Supported by Y2H, co-IP, BiFC nuclear signal, and Arabidopsis microscopy showing GA-dependent PFD5 relocalization (PAC-induced nuclear, GA4 reversal at ~3 h). (locascio2013dynamicregulationof pages 1-2, locascio2013dynamicregulationof media 5b391f96)

**DELLA–BOI promoter repression module:** Supported by genetic and promoter-targeting evidence for DELLAs with BOI family proteins repressing subsets of GA-responsive genes. (park2013dellaproteinsand pages 1-2)

## 5. Annotation-risk assessment (core vs over-extended)

### 5.1 Likely “core function” annotations (low risk)

**Recommended core emphasis for GAI:**
- GA signaling repression / negative regulation of GA responses (core biological role of DELLA family, including GAI). (shani2024highlightsingibberellin pages 7-8, park2013dellaproteinsand pages 1-2)
- GA-dependent ubiquitin–proteasome pathway-mediated DELLA turnover (via GA–GID1–DELLA and SCF^SLY1). (shani2024highlightsingibberellin pages 7-8, park2013dellaproteinsand pages 1-2)
- Nuclear transcription co-regulator activity (chromatin-associated, protein–protein interaction mediated). (shani2024highlightsingibberellin pages 8-10, zentella2007globalanalysisof pages 1-2)
- Direct participation in GA homeostasis feedback via GAF1-associated promoter regulation (GA20ox2/GA3ox1/GID1b). (fukazawa2014dellasfunctionas pages 13-15)

### 5.2 Context-specific / pleiotropic annotations (higher risk; consider qualifiers)

- **Microtubule organization / cytoskeleton-related processes:** Supported mechanistically through prefoldin sequestration by GAI, but likely condition- and tissue-specific (hypocotyl growth, GA/PAC regimes). This should be treated as a mechanistic extension rather than the primary molecular function. (locascio2013dynamicregulationof pages 1-2, locascio2013dynamicregulationof media 5b391f96)
- **Flowering time, fertility, stress responses:** Frequently downstream of GA–DELLA integration; unless backed by GAI-specific mechanistic assays, direct annotation may over-extend beyond core function. (shani2024highlightsingibberellin pages 8-10)

### 5.3 Explicit evaluation of apoptosis, developmental cell death, neuronal, inflammatory, pyroptosis terms

No evidence in the retrieved Arabidopsis GAI/DELLA literature supports annotation of GAI to apoptosis, pyroptosis, inflammatory signaling, neuronal roles, synaptic remodeling, or other animal-specific pathways. A recent GA-signaling/chromatin paper (Balouri et al. 2024) does not implicate these processes, and no mechanistic links to programmed cell death are provided for GAI. (balouri2024gibberellinsignalingthrough pages 1-2)

## 6. Evidence mapping table (for GO review traceability)

| GO aspect (MF/BP/CC) | Proposed GO term wording (plain English) | Core vs context-specific | Evidence type | Key finding | Primary citation with year/month and URL | PaperQA context citation id |
|---|---|---|---|---|---|---|
| BP | negative regulation of gibberellin-activated signaling pathway | core | Genetics, mutant phenotype, review synthesis | GAI is one of five Arabidopsis DELLA repressors of GA responses; the gai-1 allele carries a 17-aa deletion in the DELLA motif that converts GAI into a constitutive GA-signaling repressor and causes GA-unresponsive dwarfism (shani2024highlightsingibberellin pages 7-8, alabadi2025greenrevolutiondella pages 3-4). | Shani E, Hedden P, Sun T-p. 2024 Jan. *Plant Physiology* 195:111-134. https://doi.org/10.1093/plphys/kiae044 | (shani2024highlightsingibberellin pages 7-8) |
| BP | gibberellin-dependent protein catabolic process via ubiquitin-proteasome system | core | Y2H, pull-down, genetics, structural/biochemical synthesis | GA-bound GID1 promotes DELLA binding and conformational change enabling SCF^SLY1/GID2 recognition, polyubiquitination, and 26S proteasome degradation; the DELLA/LEXLE/VHYNP motifs are required, and deletion of the DELLA motif abolishes GA-induced degradation (shani2024highlightsingibberellin pages 7-8, park2013dellaproteinsand pages 1-2). | Shani E, Hedden P, Sun T-p. 2024 Jan. *Plant Physiology* 195:111-134. https://doi.org/10.1093/plphys/kiae044 | (shani2024highlightsingibberellin pages 7-8) |
| CC | nucleus | core | GFP fusion/confocal microscopy, BiFC, ChIP-associated localization evidence | DELLA proteins including GAI are nuclear-localized transcription regulators; GAI-dependent BiFC signals with partners are nuclear, and DELLA-GFP fusions/localization studies place active function in nuclei (zentella2007globalanalysisof pages 1-2, locascio2013dynamicregulationof pages 1-2). | Zentella R et al. 2007 Oct. *The Plant Cell* 19:3037-3057. https://doi.org/10.1105/tpc.107.054999 | (zentella2007globalanalysisof pages 1-2) |
| MF | transcription co-regulator activity | core | Transcriptomics, ChIP-qPCR/ChIP-seq, interaction-network synthesis | DELLAs lack canonical DNA-binding motifs but regulate transcription through protein-protein interactions and chromatin association; Arabidopsis DELLA interactome includes 370 candidates with >40 validated, and RGA ChIP-seq identified 421 associated genes in seedlings and 2,327 in inflorescences (shani2024highlightsingibberellin pages 8-10, shani2024highlightsingibberellin pages 7-8). | Shani E, Hedden P, Sun T-p. 2024 Jan. *Plant Physiology* 195:111-134. https://doi.org/10.1093/plphys/kiae044 | (shani2024highlightsingibberellin pages 8-10, shani2024highlightsingibberellin pages 7-8) |
| MF/BP | transcriptional co-activation with GAF1/IDD1 and switching with TPR4 to regulate GA homeostasis genes | core | Y2H, co-IP, BiFC, ChIP, protoplast reporter assay | GAI physically interacts with GAF1/IDD-family factors and TPR4; GAF1–GAI activates GA20ox2, GA3ox1, and GID1b promoters, whereas GA-triggered DELLA degradation converts the complex toward repression, with ChIP showing GAF1, GAI, and TPR4 at the GA20ox2 promoter (fukazawa2014dellasfunctionas pages 7-9, fukazawa2014dellasfunctionas pages 13-15, fukazawa2014dellasfunctionas pages 11-12, fukazawa2014dellasfunctionas pages 12-13). | Fukazawa J et al. 2014 Jul. *The Plant Cell* 26:2920-2938. https://doi.org/10.1105/tpc.114.125690 | (fukazawa2014dellasfunctionas pages 13-15) |
| BP | regulation of gibberellin homeostasis and positive regulation of XERICO expression | core | Microarray, qRT-PCR, ChIP | DELLA proteins directly upregulate early GA-responsive targets including GA biosynthetic/receptor genes and XERICO; 14 early DELLA-responsive genes were defined, with ChIP support for promoter association of 8, supporting direct feedback control of GA homeostasis and ABA-antagonistic output via XERICO (zentella2007globalanalysisof pages 1-2). | Zentella R et al. 2007 Oct. *The Plant Cell* 19:3037-3057. https://doi.org/10.1105/tpc.107.054999 | (zentella2007globalanalysisof pages 1-2) |
| CC/BP | nuclear prefoldin sequestration affecting cortical microtubule organization | context | Y2H, co-IP, BiFC, live-cell microscopy | GAI binds prefoldin subunits PFD5 and PFD3; YFP-PFD5 is cytosolic alone but relocalizes to nuclei with RFP-GAI, PAC induces nuclear PFD5-GFP accumulation in hypocotyl cells, and GA4 restores cytosolic localization within 3 h, linking DELLA abundance to microtubule organization and anisotropic growth (locascio2013dynamicregulationof pages 1-2, locascio2013dynamicregulationof media 5b391f96). | Locascio A, Blázquez MA, Alabadí D. 2013 May. *Current Biology* 23:804-809. https://doi.org/10.1016/j.cub.2013.03.053 | (locascio2013dynamicregulationof pages 1-2, locascio2013dynamicregulationof media 5b391f96) |
| MF/BP | promoter-bound repression complex with BOI family proteins on GA-responsive genes | context | Protein interaction assays, promoter occupancy assays, genetics | BOI/BRG proteins interact with DELLA proteins and co-occupy promoters of a subset of GA-responsive genes; boi quadruple mutants show higher seed germination on paclobutrazol, precocious phase transition, and early flowering, while BOIs do not substantially alter DELLA stability, indicating promoter-level repression rather than degradation control (park2013dellaproteinsand pages 1-2). | Park J et al. 2013 Mar. *The Plant Cell* 25:927-943. https://doi.org/10.1105/tpc.112.108951 | (park2013dellaproteinsand pages 1-2) |


*Table: This table maps key GO-annotation-relevant claims for Arabidopsis GAI to the strongest supporting experimental evidence and recent synthesis literature. It separates core functions from more context-specific roles to aid conservative, evidence-based GO review.*

## 7. Key literature (URLs + publication dates)

### 2023–2024 priority sources

1) **Shani E, Hedden P, Sun T-p.** “Highlights in gibberellin research: A tale of the dwarf and the slender.” *Plant Physiology*. **2024-01**. https://doi.org/10.1093/plphys/kiae044  
Supports core GA–GID1–DELLA–SCF^SLY1 mechanism, nuclear localization, DELLA transcriptional co-regulation modes, interaction-network statistics (shani2024highlightsingibberellin pages 8-10, shani2024highlightsingibberellin pages 7-8).

2) **Huang X et al.** “Phosphorylation activates master growth regulator DELLA by promoting histone H2A binding at chromatin in Arabidopsis.” *Nature Communications*. **2024-09**. https://doi.org/10.1038/s41467-024-52033-x  
Mechanistic and methods evidence for DELLA chromatin/histone association (paralog RGA), relevant for interpreting DELLA transcription-regulatory GO terms (huang2024phosphorylationactivatesmaster pages 10-11).

3) **Balouri C et al.** “Gibberellin Signaling through RGA Suppresses GCN5 Effects on Arabidopsis Developmental Stages.” *International Journal of Molecular Sciences*. **2024-06**. https://doi.org/10.3390/ijms25126757  
Shows GA signaling interface with chromatin regulation; no support for apoptosis/animal-specific processes (balouri2024gibberellinsignalingthrough pages 1-2).

### GAI-specific and foundational mechanistic sources

4) **Fukazawa J et al.** “DELLAs Function as Coactivators of GAI-ASSOCIATED FACTOR1 in Regulation of Gibberellin Homeostasis and Signaling in Arabidopsis.” *The Plant Cell*. **2014-07**. https://doi.org/10.1105/tpc.114.125690  
GAI–GAF1/IDD1–TPR4 interactions; promoter occupancy (ChIP) at GA20ox2; promoter activation of GA3ox1/GID1b; complex switching via GA-induced DELLA degradation (fukazawa2014dellasfunctionas pages 13-15, fukazawa2014dellasfunctionas pages 11-12).

5) **Locascio A, Blázquez MA, Alabadí D.** “Dynamic Regulation of Cortical Microtubule Organization through Prefoldin-DELLA Interaction.” *Current Biology*. **2013-05**. https://doi.org/10.1016/j.cub.2013.03.053  
GAI binds PFD5/PFD3; GAI-driven nuclear prefoldin relocalization under PAC; GA4 restores cytosolic PFD5 at ~3 h; links to microtubules (locascio2013dynamicregulationof pages 1-2, locascio2013dynamicregulationof media 5b391f96).

6) **Park J et al.** “DELLA Proteins and Their Interacting RING Finger Proteins Repress Gibberellin Responses by Binding to the Promoters of a Subset of Gibberellin-Responsive Genes in Arabidopsis.” *The Plant Cell*. **2013-03**. https://doi.org/10.1105/tpc.112.108951  
BOI/BRG–DELLA promoter co-occupancy; boiQ phenotypes; requirement of GAI for subset repression; mechanism not via DELLA stability changes (park2013dellaproteinsand pages 1-2).

7) **Zentella R et al.** “Global Analysis of DELLA Direct Targets in Early Gibberellin Signaling in Arabidopsis.” *The Plant Cell*. **2007-10**. https://doi.org/10.1105/tpc.107.054999  
Defines early DELLA-responsive targets (14 genes); ChIP evidence for promoter association (8 genes); establishes GA homeostasis and XERICO/ABA antagonism module (zentella2007globalanalysisof pages 1-2).

## 8. Notes on real-world implementations/applications

While Arabidopsis GAI itself is a research model gene, DELLA proteins are described as “Green Revolution” regulators across crops; the canonical mechanism (GA–GID1–DELLA degradation controlling growth) underlies dwarfing traits used to optimize lodging resistance and yield in cereals, and current research emphasizes tuning DELLA interactions/PTMs to modulate growth–stress trade-offs. (shani2024highlightsingibberellin pages 7-8)


References

1. (shani2024highlightsingibberellin pages 7-8): Eilon Shani, Peter Hedden, and Tai-ping Sun. Highlights in gibberellin research: a tale of the dwarf and the slender. Plant Physiology, 195:111-134, Jan 2024. URL: https://doi.org/10.1093/plphys/kiae044, doi:10.1093/plphys/kiae044. This article has 95 citations and is from a highest quality peer-reviewed journal.

2. (park2013dellaproteinsand pages 1-2): Jeongmoo Park, Khoa Thi Nguyen, Eunae Park, Jong-Seong Jeon, and Giltsu Choi. Della proteins and their interacting ring finger proteins repress gibberellin responses by binding to the promoters of a subset of gibberellin-responsive genes in<i>arabidopsis</i>. The Plant Cell, 25:927-943, Mar 2013. URL: https://doi.org/10.1105/tpc.112.108951, doi:10.1105/tpc.112.108951. This article has 194 citations.

3. (shani2024highlightsingibberellin pages 8-10): Eilon Shani, Peter Hedden, and Tai-ping Sun. Highlights in gibberellin research: a tale of the dwarf and the slender. Plant Physiology, 195:111-134, Jan 2024. URL: https://doi.org/10.1093/plphys/kiae044, doi:10.1093/plphys/kiae044. This article has 95 citations and is from a highest quality peer-reviewed journal.

4. (zentella2007globalanalysisof pages 1-2): Rodolfo Zentella, Zhong-Lin Zhang, Mehea Park, Stephen G. Thomas, Akira Endo, Kohji Murase, Christine M. Fleet, Yusuke Jikumaru, Eiji Nambara, Yuji Kamiya, and Tai-ping Sun. Global analysis of della direct targets in early gibberellin signaling in <i>arabidopsis</i>. The Plant Cell, 19(10):3037-3057, Oct 2007. URL: https://doi.org/10.1105/tpc.107.054999, doi:10.1105/tpc.107.054999. This article has 822 citations.

5. (fukazawa2014dellasfunctionas pages 13-15): Jutarou Fukazawa, Hiroshi Teramura, Satoru Murakoshi, Kei Nasuno, Naotaka Nishida, Takeshi Ito, Michiteru Yoshida, Yuji Kamiya, Shinjiro Yamaguchi, and Yohsuke Takahashi. Dellas function as coactivators of gai-associated factor1 in regulation of gibberellin homeostasis and signaling in<i>arabidopsis</i>. The Plant Cell, 26:2920-2938, Jul 2014. URL: https://doi.org/10.1105/tpc.114.125690, doi:10.1105/tpc.114.125690. This article has 254 citations.

6. (locascio2013dynamicregulationof pages 1-2): Antonella Locascio, Miguel A. Blázquez, and David Alabadí. Dynamic regulation of cortical microtubule organization through prefoldin-della interaction. Current Biology, 23:804-809, May 2013. URL: https://doi.org/10.1016/j.cub.2013.03.053, doi:10.1016/j.cub.2013.03.053. This article has 174 citations and is from a highest quality peer-reviewed journal.

7. (locascio2013dynamicregulationof media 5b391f96): Antonella Locascio, Miguel A. Blázquez, and David Alabadí. Dynamic regulation of cortical microtubule organization through prefoldin-della interaction. Current Biology, 23:804-809, May 2013. URL: https://doi.org/10.1016/j.cub.2013.03.053, doi:10.1016/j.cub.2013.03.053. This article has 174 citations and is from a highest quality peer-reviewed journal.

8. (balouri2024gibberellinsignalingthrough pages 1-2): Christina Balouri, Stylianos Poulios, Dimitra Tsompani, Zoe Spyropoulou, Maria-Christina Ketikoglou, Athanasios Kaldis, John H. Doonan, and Konstantinos E. Vlachonasios. Gibberellin signaling through rga suppresses gcn5 effects on arabidopsis developmental stages. International Journal of Molecular Sciences, 25:6757, Jun 2024. URL: https://doi.org/10.3390/ijms25126757, doi:10.3390/ijms25126757. This article has 7 citations.

9. (fukazawa2014dellasfunctionas pages 11-12): Jutarou Fukazawa, Hiroshi Teramura, Satoru Murakoshi, Kei Nasuno, Naotaka Nishida, Takeshi Ito, Michiteru Yoshida, Yuji Kamiya, Shinjiro Yamaguchi, and Yohsuke Takahashi. Dellas function as coactivators of gai-associated factor1 in regulation of gibberellin homeostasis and signaling in<i>arabidopsis</i>. The Plant Cell, 26:2920-2938, Jul 2014. URL: https://doi.org/10.1105/tpc.114.125690, doi:10.1105/tpc.114.125690. This article has 254 citations.

10. (alabadi2025greenrevolutiondella pages 3-4): David Alabadí and Tai-ping Sun. Green revolution della proteins: functional analysis and regulatory mechanisms. Annual review of plant biology, Dec 2025. URL: https://doi.org/10.1146/annurev-arplant-053124-050732, doi:10.1146/annurev-arplant-053124-050732. This article has 24 citations and is from a domain leading peer-reviewed journal.

11. (fukazawa2014dellasfunctionas pages 7-9): Jutarou Fukazawa, Hiroshi Teramura, Satoru Murakoshi, Kei Nasuno, Naotaka Nishida, Takeshi Ito, Michiteru Yoshida, Yuji Kamiya, Shinjiro Yamaguchi, and Yohsuke Takahashi. Dellas function as coactivators of gai-associated factor1 in regulation of gibberellin homeostasis and signaling in<i>arabidopsis</i>. The Plant Cell, 26:2920-2938, Jul 2014. URL: https://doi.org/10.1105/tpc.114.125690, doi:10.1105/tpc.114.125690. This article has 254 citations.

12. (fukazawa2014dellasfunctionas pages 12-13): Jutarou Fukazawa, Hiroshi Teramura, Satoru Murakoshi, Kei Nasuno, Naotaka Nishida, Takeshi Ito, Michiteru Yoshida, Yuji Kamiya, Shinjiro Yamaguchi, and Yohsuke Takahashi. Dellas function as coactivators of gai-associated factor1 in regulation of gibberellin homeostasis and signaling in<i>arabidopsis</i>. The Plant Cell, 26:2920-2938, Jul 2014. URL: https://doi.org/10.1105/tpc.114.125690, doi:10.1105/tpc.114.125690. This article has 254 citations.

13. (huang2024phosphorylationactivatesmaster pages 10-11): Xu Huang, Rodolfo Zentella, Jeongmoo Park, Larry Reser, Dina L. Bai, Mark M. Ross, Jeffrey Shabanowitz, Donald F. Hunt, and Tai-ping Sun. Phosphorylation activates master growth regulator della by promoting histone h2a binding at chromatin in arabidopsis. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52033-x, doi:10.1038/s41467-024-52033-x. This article has 11 citations and is from a highest quality peer-reviewed journal.