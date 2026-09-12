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

- Gene symbol: CLV3
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: Q9XF04
Entry Name: CLV3_ARATH
Gene Name: CLV3
Locus Tag: At2g27250 {ECO:0000312|Araport:AT2G27250}
Protein Name: Protein CLAVATA 3
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702
Function: [MCLV3]: The secreted peptide MCLV3 activates a signal transduction cascade to restrict WUSCHEL (WUS) expression, inducing shoot and root meristem consumption as cells differentiated into other organs.
Subcellular Location: Secreted, extracellular space
Subunit: Interacts with the extracellular leucine-rich repeat region of CLV1 (PubMed:18202283, PubMed:19525968). Interacts with CLV2 (PubMed:20626648). CLV3-derived CLE peptides interacts with a tetrameric complex made of two CLV2/CRN heterodimers (PubMed:20697738).
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


## Gene Research Report for GO Annotation Review: **CLV3** (*Arabidopsis thaliana*)

**Target**: CLV3 (At2g27250)  
**UniProt**: Q9XF04 (CLV3_ARATH)  
**Gene product class**: secreted CLE-family signaling peptide precursor, processed to mature peptide ligand(s).  

### 1. Executive summary

CLAVATA3 (CLV3) encodes a small, secreted preproprotein that is proteolytically processed into short mature CLE peptide ligand(s) that act in the **apoplast/extracellular space** to activate the CLAVATA receptor signaling network and thereby **restrict WUSCHEL (WUS) expression**, maintaining stem cell homeostasis in the shoot (and floral) apical meristem. This CLV3–WUS negative feedback loop is one of the best-supported intercellular signaling circuits in plant development, with strong loss- and gain-of-function phenotypes, direct evidence for extracellular localization, and mass spectrometry identification of the mature peptide forms. Core GO annotations should focus on **extracellular signaling ligand activity**, **meristem/stem cell population regulation**, and **extracellular region (apoplast)** localization; annotations implying intracellular (cytosolic/nuclear) site of action or animal-only pathways (apoptosis/pyroptosis/inflammation/neuronal functions) are not supported. (jun2008theclefamily pages 4-5, rojo2002clv3islocalized pages 1-3, xu2013thesequenceflanking pages 1-2, demesaarevalo2024intercellularcommunicationin pages 3-4)

Key recent syntheses (2023–2024) additionally emphasize that CLV3 perception likely involves multiple receptor modules (CLV1; CLV2–CRN; BAMs; RPK2) and co-receptors such as CIK kinases, with downstream RLCKs/phosphatases and MAPK signaling proposed/partly supported as intermediates linking receptor activation to WUS repression. (demesaarevalo2024intercellularcommunicationin pages 15-17, nakagami2024clepeptidesignaling pages 1-2)

### 2. Molecular function

#### 2.1 Core biochemical activity and specificity

**Best-supported molecular function:** CLV3 functions as a **signaling receptor ligand** (a peptide hormone-like ligand) rather than an enzyme. Its activity is mediated by **short mature peptides** derived from the C-terminal CLE motif of the precursor and recognized by LRR receptor complexes at the plasma membrane. (jun2008theclefamily pages 4-5)

**Mature peptide forms (sequence/length and PTMs):**

* A **12-amino-acid** mature peptide was identified in planta by in situ MALDI-TOF MS; the reported sequence is **RTVPhSGPhDPLHH**, where the notation includes modified residues (e.g., “h” consistent with hydroxyproline). (jun2008theclefamily pages 4-5)
* Mass spectrometry-based work also supports **12-aa hydroxylated** and **13-aa arabinosylated** mature forms, with proline hydroxylation and arabinosylation among the key PTMs. (xu2013thesequenceflanking pages 1-2, nakagami2024clepeptidesignaling pages 1-2)

**PTM specificity and functional consequences:**

* Hydroxyproline (Hyp) formation is a prerequisite for subsequent O-arabinosylation in CLE peptides, and CLV3 arabinosylation occurs on the **seventh proline/hydroxyproline** in the mature peptide region. Arabinosylated CLV3 is reported to have **enhanced affinity for CLV1** and higher bioactivity in meristem termination assays compared with non-arabinosylated forms. (betsuyaku2011thefunctionof pages 5-6, fedoreyeva2023molecularmechanismsof pages 4-6)
* Recent synthesis reviews attribute tri-arabinosylation to **Golgi-localized hydroxyproline O-arabinosyltransferases (HPATs)**, consistent with secretory-pathway maturation prior to apoplastic function. (nakagami2024clepeptidesignaling pages 1-2)

**Receptor engagement / binding:**

* CLV3 signaling is **CLV1-dependent** in multiple assays; direct interaction between a CLV3-derived peptide (CLV3p12) and CLV1 has been reported (heterologous system), and CLV3 peptide activity on SAM size is absent in the clv1 mutant background. (xu2013thesequenceflanking pages 1-2)
* Current (2024) models place CLV3 perception in **multiple receptor modules**, including CLV1-type LRR-RLKs and a CLV2–CRN module with co-receptor kinases such as **CIKs**; CLV3 mature forms are summarized as binding CLV1 ectodomain. (nakagami2024clepeptidesignaling pages 1-2)

#### 2.2 Activation/maturation mechanism (processing)

CLV3 is synthesized as a **96-aa secreted precursor** containing an N-terminal signal peptide (∼18 aa), and **proteolytic processing** is required to generate active mature CLE peptides from near the C-terminus. (jun2008theclefamily pages 4-5)

A mass spectrometry-based in vitro cleavage assay identified two precursor cleavage sites: one **before Arg70** (previously reported) and a second **before Met39**. Importantly, residues flanking the N-terminus of the mature peptide influence cleavage and biological activity: a non-conserved 5-aa motif and **Leu69** are critical, and Leu69→Ala substitutions reduce cleavage and reduce meristem regulatory activity. (xu2013thesequenceflanking pages 1-2)

The responsible endogenous proteases are not fully resolved; extracellular subtilisin-like proteases have been proposed as candidate processors for peptide hormone precursors in general, but specific CLV3-processing protease(s) remain incompletely identified. (xu2013thesequenceflanking pages 1-2, betsuyaku2011thefunctionof pages 5-6)

### 3. Biological process roles

#### 3.1 Core processes (highest confidence for GO)

**Shoot apical meristem stem cell homeostasis (CLV–WUS feedback loop):**

Loss-of-function clv3 mutants exhibit **excess stem cell accumulation** and **enlarged, fasciated** shoot apical meristems (SAMs), producing extra flowers and floral organs; CLV3 acts non-cell-autonomously to restrict the stem cell pool. (jun2008theclefamily pages 4-5, rojo2002clv3islocalized pages 1-3)

CLV3 restricts stem cell fate by repressing **WUSCHEL (WUS)** expression in the organizing center. Overexpression of CLV3 leads to **complete repression of WUS** (a strong indicator of pathway directionality and a direct GO-appropriate “negative regulation of WUS expression” process statement, while recognizing CLV3 is not a transcription factor). (jun2008theclefamily pages 4-5, zhang2023maintenanceofstem pages 2-4)

**Floral meristem size/determinacy and floral organ number:**

CLV pathway mutants (including clv3) have enlarged floral meristems that manifest as increased organ numbers across whorls; a concrete phenotype highlighted in 2024 synthesis is formation of **more than two carpels**, sometimes producing **three or more fused carpels** and malformed club-shaped siliques. (demesaarevalo2024intercellularcommunicationin pages 3-4)

Conversely, CLV3 overexpression can cause **premature meristem termination** (e.g., “terminal leaf”), showing that elevated CLV3 signaling pushes meristems toward determinacy/differentiation. (rojo2002clv3islocalized pages 1-3)

#### 3.2 Root phenotypes and other contexts (moderate confidence; often assay-dependent)

CLV3 peptides can inhibit root growth and promote meristem differentiation/consumption when supplied exogenously. In one experimental assay, heterologously produced CLV3 fusion peptide (TH-ProCLV3) applied at **1 µM for 8 days** reduced SAM size in clv3-2 but not in clv1-1 (CLV1 dependence), and also strongly inhibited root growth in Ler. (xu2013thesequenceflanking pages 1-2)

Because these effects can reflect non-physiological dosing and ectopic exposure, **root meristem consumption** is best treated as a context-specific bioassay outcome rather than the most conservative “core endogenous function” annotation for CLV3, compared with the SAM/floral meristem roles. (xu2013thesequenceflanking pages 1-2, meng2010cle(clavata3esrlike)peptides pages 94-97)

#### 3.3 Exclusion of apoptosis/developmental cell death and animal-only processes

Across the primary and recent review literature examined here, CLV3 phenotypes are explained by **stem cell fate regulation and meristem size control**, not by apoptosis, pyroptosis, inflammatory signaling, synaptic remodeling, or neuronal functions. Thus, these process domains should be treated as **unsupported for CLV3** in Arabidopsis GO review. (jun2008theclefamily pages 4-5, rojo2002clv3islocalized pages 1-3, demesaarevalo2024intercellularcommunicationin pages 3-4)

### 4. Cellular localization and complexes

#### 4.1 Best-supported subcellular localization

CLV3 is localized to the **extracellular space/apoplast**. In Rojo et al. (2002), CLV3-GFP signal is observed **between cells**, and immunogold electron microscopy detects CLV3 in the **cell wall/extracellular space**, supporting an apoplastic site of ligand action. (rojo2002clv3islocalized pages 1-3, rojo2002clv3islocalized media 3bc47db1)

The **signal peptide is required** for functional secretion: removal of the signal peptide retains CLV3 in the cytoplasm and disrupts its functional delivery. (rojo2002clv3islocalized pages 1-3)

#### 4.2 Receptor complexes and perception modules (current understanding)

A conservative GO framing is that CLV3 acts extracellularly and is perceived at the **plasma membrane** by receptor complexes including:

* **CLV1** (LRR receptor-like kinase) as a primary receptor module with direct ligand binding evidence and strong genetic dependency. (xu2013thesequenceflanking pages 1-2, nakagami2024clepeptidesignaling pages 1-2)
* A **CLV2–CRN** module (CLV2 is an LRR receptor-like protein lacking a kinase domain; CRN is a membrane pseudokinase/RLK component), proposed to operate as a receptor complex and converging with CLV1 signaling to regulate WUS. (wang2010clepeptidesignaling pages 5-7, nakagami2024clepeptidesignaling pages 1-2)
* **Co-receptors (CIKs)** are emphasized in 2024 synthesis as components of CLE perception, including in CLV-type receptor complexes. (nakagami2024clepeptidesignaling pages 1-2)
* Additional/auxiliary receptor nodes (BAM-family RLKs; RPK2) are emphasized in recent syntheses as supplementary receptors for CLV3-like signaling in the SAM. (demesaarevalo2024intercellularcommunicationin pages 15-17, nakagami2024clepeptidesignaling pages 1-2)

Downstream, recent authoritative syntheses describe intracellular intermediates that likely connect receptor activation to transcriptional outputs: RLCKs (PBS1-like kinases/PBLs), phosphatases POL/PLL1, heterotrimeric G proteins, and MAPKs (including MPK3/MPK6) are discussed as pathway components. (nakagami2024clepeptidesignaling pages 1-2, demesaarevalo2024intercellularcommunicationin pages 15-17)

### 5. Annotation-risk assessment (GO review guidance)

A structured evidence table is provided below to map key claims to evidence and flag over-extension risks.

| GO aspect | Proposed GO term phrasing | Core claim | Key experimental evidence (methods) | Key citations with year / DOI / URL | Annotation notes (core vs context-specific; caveats) |
|---|---|---|---|---|---|
| MF | signaling receptor ligand activity | CLV3 is a secreted CLE-family peptide ligand that acts non-cell-autonomously to activate CLAVATA signaling in meristems. | Genetic rescue/overexpression; extracellular targeting requirement; mature peptide identification by in situ MALDI-TOF MS; receptor-dependent bioactivity in clv backgrounds (jun2008theclefamily pages 4-5, rojo2002clv3islocalized pages 1-3, xu2013thesequenceflanking pages 1-2) | Rojo et al. 2002, 10.1105/tpc.002196, https://doi.org/10.1105/tpc.002196; Jun et al. 2008, 10.1007/s00018-007-7411-5, https://doi.org/10.1007/s00018-007-7411-5; Xu et al. 2013, 10.1186/1471-2229-13-225, https://doi.org/10.1186/1471-2229-13-225 (rojo2002clv3islocalized pages 1-3, jun2008theclefamily pages 4-5, xu2013thesequenceflanking pages 1-2) | **Core.** Best GO-MF framing is ligand/signaling activity, not enzymatic catalysis. Avoid assigning kinase activity or generic “protein binding” as CLV3’s primary function. |
| MF | CLV1 receptor binding / receptor complex engagement | Mature CLV3 binds the extracellular domain of CLV1; perception likely also involves CLV2-CRN and co-receptors in vivo. | Direct ligand-receptor interaction reported for CLV1 ectodomain; receptor genetics; peptide response lost in clv1 backgrounds; reviews summarize CLV2-CRN and CIK participation (xu2013thesequenceflanking pages 1-2, nakagami2024clepeptidesignaling pages 1-2, wang2010clepeptidesignaling pages 5-7, czyzewicz2013messageina pages 7-8) | Xu et al. 2013, 10.1186/1471-2229-13-225, https://doi.org/10.1186/1471-2229-13-225; Wang & Fiers 2010, 10.1007/s00709-009-0095-y, https://doi.org/10.1007/s00709-009-0095-y; Nakagami et al. 2024, 10.3389/fpls.2024.1481650, https://doi.org/10.3389/fpls.2024.1481650 (xu2013thesequenceflanking pages 1-2, wang2010clepeptidesignaling pages 5-7, nakagami2024clepeptidesignaling pages 1-2, czyzewicz2013messageina pages 7-8) | **Core with caveat.** CLV1 binding is strongest/most direct. CLV2-CRN and CIKs are well-supported for pathway perception, but exact stoichiometry and whether all modules directly bind CLV3 under native conditions remain more model-based than CLV1 binding alone. |
| MF | mature peptide hormone / modified peptide form | Bioactive CLV3 exists as short mature peptides rather than the 96-aa precursor. The main reported forms are a 12-aa hydroxylated peptide and a 13-aa arabinosylated peptide. | In situ MALDI-TOF MS and LC-MS detection of mature peptides; sequence assignment near C-terminus of precursor (jun2008theclefamily pages 4-5, xu2013thesequenceflanking pages 1-2, lu2024currentadvancesin pages 9-10, lu2024smallpeptidesorchestrators pages 7-9) | Jun et al. 2008, 10.1007/s00018-007-7411-5, https://doi.org/10.1007/s00018-007-7411-5; Xu et al. 2013, 10.1186/1471-2229-13-225, https://doi.org/10.1186/1471-2229-13-225; Lu & Xiao 2024, 10.3390/ijms25147627, https://doi.org/10.3390/ijms25147627 (jun2008theclefamily pages 4-5, xu2013thesequenceflanking pages 1-2, lu2024currentadvancesin pages 9-10, lu2024smallpeptidesorchestrators pages 7-9) | **Core.** Useful for annotation review because the precursor itself is not the active signaling species. |
| BP | protein maturation by proteolytic processing | CLV3 precursor requires proteolytic processing to generate the active peptide; cleavage near Arg70 is experimentally supported, with additional upstream cleavage evidence. | MS-based in vitro cleavage assay; identification of cleavage before Arg70 and before Met39; mutational analysis of flanking residues affecting cleavage and activity (xu2013thesequenceflanking pages 1-2) | Xu et al. 2013, 10.1186/1471-2229-13-225, https://doi.org/10.1186/1471-2229-13-225 (xu2013thesequenceflanking pages 1-2) | **Core but limited specificity.** Strong evidence that processing is required; weak evidence for the exact endogenous protease(s). Avoid annotating CLV3 itself with peptidase activity. |
| BP | post-translational protein modification required for signaling peptide activity | Hydroxylation and hydroxyproline arabinosylation increase CLV3 bioactivity; tri-arabinosylated Hyp7 is associated with stronger CLV1 affinity. | MS detection of modified forms; biochemical/genetic literature summarized in reviews; activity/affinity comparisons of modified peptides (betsuyaku2011thefunctionof pages 5-6, fedoreyeva2023molecularmechanismsof pages 4-6, nakagami2024clepeptidesignaling pages 1-2) | Betsuyaku et al. 2011, 10.1199/tab.0149, https://doi.org/10.1199/tab.0149; Nakagami et al. 2024, 10.3389/fpls.2024.1481650, https://doi.org/10.3389/fpls.2024.1481650 (betsuyaku2011thefunctionof pages 5-6, fedoreyeva2023molecularmechanismsof pages 4-6, nakagami2024clepeptidesignaling pages 1-2) | **Core pathway chemistry, but enzyme attribution belongs elsewhere.** HPATs catalyze arabinosylation; do not annotate CLV3 with transferase activity. |
| BP | shoot apical meristem maintenance / regulation of stem cell population maintenance | CLV3 restricts stem cell accumulation in the SAM through the canonical CLV–WUS negative feedback loop. | Loss-of-function phenotypes (enlarged/fasciated SAM); WUS repression after CLV3 overexpression; expression/domain analyses; peptide application phenotypes (jun2008theclefamily pages 4-5, wang2010clepeptidesignaling pages 1-2, zhang2023maintenanceofstem pages 2-4, demesaarevalo2024intercellularcommunicationin pages 3-4) | Jun et al. 2008, 10.1007/s00018-007-7411-5, https://doi.org/10.1007/s00018-007-7411-5; Wang & Fiers 2010, 10.1007/s00709-009-0095-y, https://doi.org/10.1007/s00709-009-0095-y; Demesa-Arevalo et al. 2024, 10.1146/annurev-arplant-070523-035342, https://doi.org/10.1146/annurev-arplant-070523-035342 (jun2008theclefamily pages 4-5, wang2010clepeptidesignaling pages 1-2, zhang2023maintenanceofstem pages 2-4, demesaarevalo2024intercellularcommunicationin pages 3-4) | **Core.** This is the safest and strongest BP annotation for Arabidopsis CLV3. |
| BP | negative regulation of WUSCHEL expression / stem cell fate | CLV3 signaling represses WUS expression in the organizing center, thereby limiting stem cell fate. | Overexpression causing complete WUS repression; feedback-loop studies; time-course induction summarized in reviews (jun2008theclefamily pages 4-5, zhang2023maintenanceofstem pages 2-4, betsuyaku2011thefunctionof pages 5-6) | Jun et al. 2008, 10.1007/s00018-007-7411-5, https://doi.org/10.1007/s00018-007-7411-5; Zhang et al. 2023, 10.3389/fpls.2023.1302046, https://doi.org/10.3389/fpls.2023.1302046; Betsuyaku et al. 2011, 10.1199/tab.0149, https://doi.org/10.1199/tab.0149 (jun2008theclefamily pages 4-5, zhang2023maintenanceofstem pages 2-4, betsuyaku2011thefunctionof pages 5-6) | **Core.** Appropriate as a pathway-level process; do not overstate as direct transcriptional repression by CLV3 itself. |
| BP | floral meristem maintenance / regulation of floral organ number | Loss of CLV3 leads to enlarged floral meristems and increased floral organ/carpel numbers; strong CLV signaling promotes determinacy/termination. | Floral phenotyping in clv mutants; extra carpels and malformed siliques; overexpression causing premature meristem termination in some lines (rojo2002clv3islocalized pages 1-3, demesaarevalo2024intercellularcommunicationin pages 3-4) | Rojo et al. 2002, 10.1105/tpc.002196, https://doi.org/10.1105/tpc.002196; Demesa-Arevalo et al. 2024, 10.1146/annurev-arplant-070523-035342, https://doi.org/10.1146/annurev-arplant-070523-035342 (rojo2002clv3islocalized pages 1-3, demesaarevalo2024intercellularcommunicationin pages 3-4) | **Core developmental consequence.** Strongly supported in floral meristems; phrase as meristem/floral organ number control rather than broad “flower development.” |
| BP | root meristem consumption / inhibition of root growth after exogenous peptide treatment | Exogenous mature CLV3 peptides can inhibit root growth and promote root meristem differentiation/consumption. | Synthetic peptide treatment; heterologous peptide application; genotype dependence involving CLV-pathway receptors (xu2013thesequenceflanking pages 1-2, meng2010cle(clavata3esrlike)peptides pages 94-97, fedoreyeva2023molecularmechanismsof pages 17-18) | Xu et al. 2013, 10.1186/1471-2229-13-225, https://doi.org/10.1186/1471-2229-13-225; Fedoreyeva 2023, 10.3390/plants12061320, https://doi.org/10.3390/plants12061320 (xu2013thesequenceflanking pages 1-2, meng2010cle(clavata3esrlike)peptides pages 94-97, fedoreyeva2023molecularmechanismsof pages 17-18) | **Context-specific / caution.** Strong for exogenous peptide bioassays; weaker as evidence for endogenous core CLV3 function in Arabidopsis roots than for SAM roles. |
| CC | extracellular region / apoplast | CLV3 is secreted via the secretory pathway and accumulates in the extracellular space/apoplast, where signaling occurs. | Signal peptide dependence; GFP/GUS localization between cells; immunogold EM in cell walls/apoplast; secretory-pathway manipulations (rojo2002clv3islocalized pages 1-3, rojo2002clv3islocalized media 3bc47db1) | Rojo et al. 2002, 10.1105/tpc.002196, https://doi.org/10.1105/tpc.002196 (rojo2002clv3islocalized pages 1-3, rojo2002clv3islocalized media 3bc47db1) | **Core.** Strongest CC annotation for the active ligand. Avoid cytosol/nucleus localization for functional CLV3. |
| CC | cell surface receptor complex (target site of action) | CLV3 functions at the cell surface by engaging plasma-membrane receptor modules in underlying cells. | Extracellular localization plus receptor genetics/biochemistry; modern reviews synthesize CLV1, CLV2-CRN, CIK, BAM, and RPK2 modules (lu2024currentadvancesin pages 9-10, demesaarevalo2024intercellularcommunicationin pages 15-17, nakagami2024clepeptidesignaling pages 1-2, czyzewicz2013messageina pages 7-8) | Demesa-Arevalo et al. 2024, 10.1146/annurev-arplant-070523-035342, https://doi.org/10.1146/annurev-arplant-070523-035342; Nakagami et al. 2024, 10.3389/fpls.2024.1481650, https://doi.org/10.3389/fpls.2024.1481650 (lu2024currentadvancesin pages 9-10, demesaarevalo2024intercellularcommunicationin pages 15-17, nakagami2024clepeptidesignaling pages 1-2, czyzewicz2013messageina pages 7-8) | **Useful contextual CC note, but receptor-complex membership is more appropriate for receptors than for CLV3 itself.** |
| BP | receptor-mediated signaling pathway downstream of CLV3 perception | CLV3 perception feeds into intracellular signaling involving PBL/RLCKs, POL/PLL1 phosphatases, and MAPKs such as MPK3/MPK6 to regulate WUS and meristem homeostasis. | Recent reviews synthesize genetic/biochemical evidence for RLCK, phosphatase, G-protein, and MAPK nodes downstream of CLV receptors (lu2024currentadvancesin pages 9-10, demesaarevalo2024intercellularcommunicationin pages 15-17, nakagami2024clepeptidesignaling pages 1-2, jun2008theclefamily pages 4-5) | Nakagami et al. 2024, 10.3389/fpls.2024.1481650, https://doi.org/10.3389/fpls.2024.1481650; Demesa-Arevalo et al. 2024, 10.1146/annurev-arplant-070523-035342, https://doi.org/10.1146/annurev-arplant-070523-035342; Jun et al. 2008, 10.1007/s00018-007-7411-5, https://doi.org/10.1007/s00018-007-7411-5 (lu2024currentadvancesin pages 9-10, demesaarevalo2024intercellularcommunicationin pages 15-17, nakagami2024clepeptidesignaling pages 1-2, jun2008theclefamily pages 4-5) | **Pathway-level, not direct CLV3 activity.** Appropriate as BP context, but avoid annotating CLV3 to kinase cascade components unless evidence is specifically for the ligand’s role in that pathway. |
| Annotation risk | avoid apoptosis / cell death / neuronal / inflammatory / pyroptosis terms | No evidence from Arabidopsis CLV3 literature supports apoptosis, pyroptosis, inflammatory signaling, synaptic remodeling, or neuronal roles. Meristem termination reflects developmental fate control, not animal-type cell death programs. | Negative assessment based on scope of plant developmental literature reviewed; reported phenotypes are meristem size, stem cell fate, and organ number changes (jun2008theclefamily pages 4-5, rojo2002clv3islocalized pages 1-3, wang2010clepeptidesignaling pages 1-2, demesaarevalo2024intercellularcommunicationin pages 3-4) | Jun et al. 2008, 10.1007/s00018-007-7411-5, https://doi.org/10.1007/s00018-007-7411-5; Rojo et al. 2002, 10.1105/tpc.002196, https://doi.org/10.1105/tpc.002196; Demesa-Arevalo et al. 2024, 10.1146/annurev-arplant-070523-035342, https://doi.org/10.1146/annurev-arplant-070523-035342 (jun2008theclefamily pages 4-5, rojo2002clv3islocalized pages 1-3, wang2010clepeptidesignaling pages 1-2, demesaarevalo2024intercellularcommunicationin pages 3-4) | **High-confidence exclusion.** Also avoid cytoplasm/cytosol/nucleus annotations for active CLV3 unless tied only to transient precursor trafficking, not functional localization. |


*Table: This table organizes GO-relevant evidence for Arabidopsis CLV3 across molecular function, biological process, and cellular component, emphasizing experimentally supported core annotations and flagging context-specific or risky extensions.*

**High-confidence, core annotations (recommended):**

* **Extracellular/apoplastic peptide ligand** (cell–cell signaling) (rojo2002clv3islocalized pages 1-3, jun2008theclefamily pages 4-5)
* **Regulation of shoot apical meristem stem cell population / stem cell homeostasis** via the CLV–WUS feedback loop (jun2008theclefamily pages 4-5, demesaarevalo2024intercellularcommunicationin pages 3-4)
* **Negative regulation of WUS expression** (process-level, not direct transcription factor activity) (jun2008theclefamily pages 4-5, zhang2023maintenanceofstem pages 2-4)

**Moderate-confidence / context-specific annotations (use caution):**

* **Root meristem consumption / inhibition of root growth** based primarily on exogenous peptide assays; may not reflect the dominant endogenous role of CLV3 compared to CLE40 and other CLEs in roots. (xu2013thesequenceflanking pages 1-2, meng2010cle(clavata3esrlike)peptides pages 94-97)

**Likely incorrect / over-extended annotations (avoid):**

* **Cytosolic/nuclear localization** as a functional site of action (precursor may transit secretory pathway, but functional ligand acts extracellularly). (rojo2002clv3islocalized pages 1-3)
* **Apoptosis, developmental cell death programs, inflammatory signaling, neuronal roles, synaptic remodeling, pyroptosis**—no supporting evidence in the CLV3 meristem literature reviewed here. (jun2008theclefamily pages 4-5, rojo2002clv3islocalized pages 1-3, demesaarevalo2024intercellularcommunicationin pages 3-4)

### 6. Key literature (with publication dates and URLs)

**Primary experimental anchors**

1. Rojo E, Sharma VK, Kovaleva V, Raikhel NV, Fletcher JC. *CLV3 is localized to the extracellular space, where it activates the Arabidopsis CLAVATA stem cell signaling pathway.* **The Plant Cell** (May 2002). https://doi.org/10.1105/tpc.002196 (rojo2002clv3islocalized pages 1-3, rojo2002clv3islocalized media 3bc47db1)
2. Jun JH, Fiume E, Fletcher JC. *The CLE family of plant polypeptide signaling molecules.* **Cellular and Molecular Life Sciences** (Mar 2008). https://doi.org/10.1007/s00018-007-7411-5 (jun2008theclefamily pages 4-5)
3. Xu TT, Song XF, Ren SC, Liu CM. *The sequence flanking the N-terminus of the CLV3 peptide is critical for its cleavage and activity in stem cell regulation in Arabidopsis.* **BMC Plant Biology** (Dec 2013). https://doi.org/10.1186/1471-2229-13-225 (xu2013thesequenceflanking pages 1-2)

**Recent (2023–2024) priority sources (authoritative syntheses)**

4. Demesa-Arevalo E, Narasimhan M, Simon R. *Intercellular communication in shoot meristems.* **Annual Review of Plant Biology** (Jul 2024). https://doi.org/10.1146/annurev-arplant-070523-035342 (demesaarevalo2024intercellularcommunicationin pages 15-17, demesaarevalo2024intercellularcommunicationin pages 3-4)
5. Nakagami S, Kajiwara T, Tsuda K, Sawa S. *CLE peptide signaling in plant-microbe interactions.* **Frontiers in Plant Science** (Oct 2024). https://doi.org/10.3389/fpls.2024.1481650 (nakagami2024clepeptidesignaling pages 1-2)
6. Zhang H, Mu Y, Zhang H, Yu C. *Maintenance of stem cell activity in plant development and stress responses.* **Frontiers in Plant Science** (Dec 2023). https://doi.org/10.3389/fpls.2023.1302046 (zhang2023maintenanceofstem pages 2-4)

**Additional curated background sources (processing/PTMs and pathway framing)**

7. Betsuyaku S, Sawa S, Yamada M. *The function of the CLE peptides in plant development and plant-microbe interactions.* **The Arabidopsis Book** (Sep 2011). https://doi.org/10.1199/tab.0149 (betsuyaku2011thefunctionof pages 5-6)
8. Wang G, Fiers M. *CLE peptide signaling during plant development.* **Protoplasma** (Dec 2010). https://doi.org/10.1007/s00709-009-0095-y (wang2010clepeptidesignaling pages 1-2, wang2010clepeptidesignaling pages 5-7)

### Notes on requested statistics/data

Quantitative data explicitly extractable from the examined primary excerpts include a **peptide-treatment regimen (1 µM, 8 days)** producing CLV1-dependent SAM size reduction and root growth inhibition in the Xu et al. (2013) assay. (xu2013thesequenceflanking pages 1-2) Other widely cited quantitative measures (e.g., binding constants for arabinosylated vs non-arabinosylated CLV3 to CLV1) are referenced in review syntheses but were not present as explicit numeric values in the retrieved text passages; thus, they are not reported here to avoid over-claiming. (betsuyaku2011thefunctionof pages 5-6, nakagami2024clepeptidesignaling pages 1-2)


References

1. (jun2008theclefamily pages 4-5): Ji Hyung Jun, Ji Hyung Jun, Elisa Fiume, Elisa Fiume, Jennifer C. Fletcher, and Jennifer C. Fletcher. The cle family of plant polypeptide signaling molecules. Cellular and Molecular Life Sciences, 65:743-755, Mar 2008. URL: https://doi.org/10.1007/s00018-007-7411-5, doi:10.1007/s00018-007-7411-5. This article has 133 citations and is from a domain leading peer-reviewed journal.

2. (rojo2002clv3islocalized pages 1-3): Enrique Rojo, Vijay K. Sharma, Valentina Kovaleva, Natasha V. Raikhel, and Jennifer C. Fletcher. Clv3 is localized to the extracellular space, where it activates the arabidopsis clavata stem cell signaling pathway article, publication date, and citation information can be found at www.plantcell.org/cgi/doi/10.1105/tpc.002196. The Plant Cell Online, 14:969-977, May 2002. URL: https://doi.org/10.1105/tpc.002196, doi:10.1105/tpc.002196. This article has 434 citations.

3. (xu2013thesequenceflanking pages 1-2): Ting-Ting Xu, Xiu-Fen Song, Shi-Chao Ren, and Chun-Ming Liu. The sequence flanking the n-terminus of the clv3 peptide is critical for its cleavage and activity in stem cell regulation in arabidopsis. BMC Plant Biology, 13:225-225, Dec 2013. URL: https://doi.org/10.1186/1471-2229-13-225, doi:10.1186/1471-2229-13-225. This article has 27 citations and is from a peer-reviewed journal.

4. (demesaarevalo2024intercellularcommunicationin pages 3-4): Edgar Demesa-Arevalo, Madhumitha Narasimhan, and Rüdiger Simon. Intercellular communication in shoot meristems. Jul 2024. URL: https://doi.org/10.1146/annurev-arplant-070523-035342, doi:10.1146/annurev-arplant-070523-035342. This article has 21 citations and is from a domain leading peer-reviewed journal.

5. (demesaarevalo2024intercellularcommunicationin pages 15-17): Edgar Demesa-Arevalo, Madhumitha Narasimhan, and Rüdiger Simon. Intercellular communication in shoot meristems. Jul 2024. URL: https://doi.org/10.1146/annurev-arplant-070523-035342, doi:10.1146/annurev-arplant-070523-035342. This article has 21 citations and is from a domain leading peer-reviewed journal.

6. (nakagami2024clepeptidesignaling pages 1-2): Satoru Nakagami, Taiki Kajiwara, Kenichi Tsuda, and Shinichiro Sawa. Cle peptide signaling in plant-microbe interactions. Frontiers in Plant Science, Oct 2024. URL: https://doi.org/10.3389/fpls.2024.1481650, doi:10.3389/fpls.2024.1481650. This article has 20 citations.

7. (betsuyaku2011thefunctionof pages 5-6): Shigeyuki Betsuyaku, Shinichiro Sawa, and Masashi Yamada. The function of the cle peptides in plant development and plant-microbe interactions. The Arabidopsis Book, 2011:e0149, Sep 2011. URL: https://doi.org/10.1199/tab.0149, doi:10.1199/tab.0149. This article has 127 citations and is from a peer-reviewed journal.

8. (fedoreyeva2023molecularmechanismsof pages 4-6): Larisa I. Fedoreyeva. Molecular mechanisms of regulation of root development by plant peptides. Plants, 12:1320, Mar 2023. URL: https://doi.org/10.3390/plants12061320, doi:10.3390/plants12061320. This article has 21 citations.

9. (zhang2023maintenanceofstem pages 2-4): Huankai Zhang, Yangwei Mu, Hui Zhang, and Caiyu Yu. Maintenance of stem cell activity in plant development and stress responses. Frontiers in Plant Science, Dec 2023. URL: https://doi.org/10.3389/fpls.2023.1302046, doi:10.3389/fpls.2023.1302046. This article has 22 citations.

10. (meng2010cle(clavata3esrlike)peptides pages 94-97): L Meng. Cle (clavata3/esr-like) peptides: roles in cell signaling and stem cell homeostasis in arabidopsis. Unknown journal, 2010.

11. (rojo2002clv3islocalized media 3bc47db1): Enrique Rojo, Vijay K. Sharma, Valentina Kovaleva, Natasha V. Raikhel, and Jennifer C. Fletcher. Clv3 is localized to the extracellular space, where it activates the arabidopsis clavata stem cell signaling pathway article, publication date, and citation information can be found at www.plantcell.org/cgi/doi/10.1105/tpc.002196. The Plant Cell Online, 14:969-977, May 2002. URL: https://doi.org/10.1105/tpc.002196, doi:10.1105/tpc.002196. This article has 434 citations.

12. (wang2010clepeptidesignaling pages 5-7): Guodong Wang and Martijn Fiers. Cle peptide signaling during plant development. Protoplasma, 240:33-43, Dec 2010. URL: https://doi.org/10.1007/s00709-009-0095-y, doi:10.1007/s00709-009-0095-y. This article has 130 citations and is from a peer-reviewed journal.

13. (czyzewicz2013messageina pages 7-8): Nathan Czyzewicz, Kun Yue, Tom Beeckman, and Ive De Smet. Message in a bottle: small signalling peptide outputs during growth and development. Journal of experimental botany, 64 17:5281-96, Dec 2013. URL: https://doi.org/10.1093/jxb/ert283, doi:10.1093/jxb/ert283. This article has 152 citations and is from a domain leading peer-reviewed journal.

14. (lu2024currentadvancesin pages 9-10): Shuaiqi Lu and Fei Xiao. Current advances in small peptides during plant growth and development. Unknown journal, Jun 2024. URL: https://doi.org/10.20944/preprints202406.0156.v1, doi:10.20944/preprints202406.0156.v1.

15. (lu2024smallpeptidesorchestrators pages 7-9): Shuaiqi Lu and Fei Xiao. Small peptides: orchestrators of plant growth and developmental processes. International Journal of Molecular Sciences, 25:7627, Jul 2024. URL: https://doi.org/10.3390/ijms25147627, doi:10.3390/ijms25147627. This article has 36 citations.

16. (wang2010clepeptidesignaling pages 1-2): Guodong Wang and Martijn Fiers. Cle peptide signaling during plant development. Protoplasma, 240:33-43, Dec 2010. URL: https://doi.org/10.1007/s00709-009-0095-y, doi:10.1007/s00709-009-0095-y. This article has 130 citations and is from a peer-reviewed journal.

17. (fedoreyeva2023molecularmechanismsof pages 17-18): Larisa I. Fedoreyeva. Molecular mechanisms of regulation of root development by plant peptides. Plants, 12:1320, Mar 2023. URL: https://doi.org/10.3390/plants12061320, doi:10.3390/plants12061320. This article has 21 citations.