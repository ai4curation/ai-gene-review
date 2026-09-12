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

- Gene symbol: MGAT1
- Organism: Homo sapiens

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: P26572
Entry Name: MGAT1_HUMAN
Gene Name: MGAT1
Protein Name: Alpha-1,3-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase
EC Number: 2.4.1.101
Organism: Homo sapiens (Human)
NCBI Taxonomy ID: 9606
Function: Initiates complex N-linked carbohydrate formation. Essential for the conversion of high-mannose to hybrid and complex N-glycans.
Subcellular Location: Golgi apparatus membrane
Subunit: Interacts with MGAT4D. Interacts with BRI3 (isoforms 1 and 2); the interaction with isoform 2 is weaker than with isoform 1 (PubMed:30983867).
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


# Comprehensive Literature-Backed Research Report for GO Annotation Review of MGAT1

**Gene:** MGAT1 (Alpha-1,3-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase)  
**Organism:** Homo sapiens  
**UniProt ID:** P26572  
**EC Number:** 2.4.1.101

---

## 1. EXECUTIVE SUMMARY

MGAT1 (also known as GnT-I, GlcNAc-transferase I) encodes the glycosyltransferase that catalyzes the first committed step in the conversion of oligomannose N-glycans to hybrid and complex N-glycans (kizuka2024regulationofintracellular pages 1-2, abdelbary2023nlinkedglycansan pages 1-2). The enzyme transfers N-acetylglucosamine (GlcNAc) from UDP-GlcNAc to the α-1,3-mannose arm of Man5GlcNAc2, forming a β-1,2-glycosidic linkage that is essential for all downstream hybrid and complex N-glycan biosynthesis (liu2026iterativebumpandholeengineering pages 1-4, thoma2024determinationexpressionand pages 1-2). MGAT1 is a type II transmembrane protein localized to the medial-Golgi apparatus membrane, where it participates in multi-enzyme complexes with other glycosyltransferases and nucleotide sugar transporters (kizuka2024regulationofintracellular pages 1-2, huang2015gnt1iplspecificallyinhibits pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2).

The core function of MGAT1 is highly conserved and well-defined: protein N-glycosylation in the Golgi. Loss-of-function studies in mice demonstrate that Mgat1 deletion is embryonically lethal (E9.5-E10.5) due to neural tube maldevelopment, establishing MGAT1 as essential for early mammalian development (liu2026iterativebumpandholeengineering pages 1-4, hall2023reductioninnacetylglucosaminyltransferasei pages 1-2). MGAT1-dependent N-glycan maturation also plays critical roles in T-cell development, including β-selection, regulatory T-cell generation, and γδ T-cell lineage determination (abdelbary2023nlinkedglycansan pages 1-2, vicente2023mannosylatedglycansimpair pages 1-2).

Recent studies (2023-2025) have expanded understanding of MGAT1's context-specific roles in immune regulation, cancer progression, and metabolic processes, but these represent indirect, substrate-mediated effects rather than direct MGAT1 functions (chi2025mgat1guidedcomplexnglycans pages 1-2, zhou2024lactatesupportstreg pages 1-2, blomberg2025mgat1knockoutin pages 1-2). A key annotation risk is conflating the pleiotropic consequences of altered N-glycan structures on substrate glycoproteins with direct MGAT1 molecular activities.

---

## 2. MOLECULAR FUNCTION

### 2.1 Core Biochemical Activity

| Aspect | MGAT1 finding | Evidence / notes |
|---|---|---|
| Enzyme name | Alpha-1,3-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase; also GnT-I / GlcNAc-transferase I | Identified as the key branching enzyme that initiates hybrid and complex N-glycan synthesis (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, thoma2024determinationexpressionand pages 1-2) |
| Enzyme class | Glycosyltransferase; UDP-GlcNAc:α-1,3-D-mannoside β-1,2-N-acetylglucosaminyltransferase I | Explicitly described as transferring GlcNAc from UDP-GlcNAc to an α1,3-linked mannose acceptor (thoma2024determinationexpressionand pages 1-2, huang2015gnt1iplspecificallyinhibits pages 1-2) |
| EC number | EC 2.4.1.101 | Reported for GnT-I/MGAT1 in biochemical characterization and standard nomenclature (thoma2024determinationexpressionand pages 1-2) |
| Core biochemical activity | Catalyzes the first committed GlcNAc-branching step that converts high-mannose/oligomannose N-glycans into substrates for hybrid and complex N-glycan biosynthesis | MGAT1 is described as necessary to start elaboration of all hybrid and complex N-glycans and to initiate conversion from Man5 structures (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, abdelbary2023nlinkedglycansan pages 1-2, hall2023reductioninnacetylglucosaminyltransferasei pages 1-2) |
| Catalytic reaction | Transfers N-acetylglucosamine (GlcNAc) from UDP-GlcNAc to the α1,3-Man arm of Man5GlcNAc2, creating a β1,2 linkage | Described as formation of a β-1,2-glycosidic bond between GlcNAc and a mannose on the α-1,3 arm of Man5GlcNAc2-Asn / Man5GlcNAc2 (liu2026iterativebumpandholeengineering pages 1-4, thoma2024determinationexpressionand pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Donor substrate | UDP-N-acetylglucosamine (UDP-GlcNAc) | Explicit donor substrate in MGAT1/GnT-I reactions (liu2026iterativebumpandholeengineering pages 1-4, thoma2024determinationexpressionand pages 1-2, huang2015gnt1iplspecificallyinhibits pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Acceptor substrate | Primarily Man5GlcNAc2 on N-glycoproteins; specifically the α1,3 mannose arm in the N-glycan core | Multiple sources define Man5GlcNAc2 as the physiologic substrate and the α1,3-Man arm as the acceptor site (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, thoma2024determinationexpressionand pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Product | GlcNAcβ1-2Manα1-3-containing intermediate that becomes substrate for MAN2A1/MAN2A2 and then MGAT2, enabling hybrid/complex N-glycan formation | Product is the entry point to downstream elaboration by α-mannosidase II and additional transferases (kizuka2024regulationofintracellular pages 1-2, abdelbary2023nlinkedglycansan pages 1-2, thoma2024determinationexpressionand pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Biosynthetic position | Acts after Golgi mannose trimming to a Man5 structure and before MAN2A1/MAN2A2 and MGAT2 | Reviews and pathway diagrams place MGAT1 immediately before α-mannosidase II and MGAT2 in medial-Golgi N-glycan maturation (kizuka2024regulationofintracellular pages 1-2, abdelbary2023nlinkedglycansan pages 1-2, liu2024abioorthogonalprecision pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Functional consequence of reaction | Produces the obligatory substrate pool for downstream branching, extension, galactosylation, fucosylation, and terminal maturation of complex N-glycans | Loss of MGAT1 abolishes hybrid/complex N-glycan synthesis and leaves oligomannose-rich glycans (abdelbary2023nlinkedglycansan pages 1-2, blomberg2025mgat1knockoutin pages 1-2, hall2023reductioninnacetylglucosaminyltransferasei pages 1-2, huang2015gnt1iplspecificallyinhibits pages 1-2) |
| Cofactor requirement | Divalent metal ions are required; Mn2+ is the key activating cofactor for GnT-I activity | Biochemical characterization of GnT-I orthologs shows divalent cations are indispensable, with highest activity at 40 mM Mn2+ and loss of activity with EDTA; reviews note Golgi glycosyltransferases commonly require Mn2+ (thoma2024determinationexpressionand pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Inhibitory metal/chelating conditions | EDTA abolishes activity; Cu2+ abolishes activity in ortholog biochemical assays | Supports metal dependence of GnT-I catalysis and risk of inferring activity in metal-poor conditions (thoma2024determinationexpressionand pages 1-2) |
| pH / temperature preference | Ortholog biochemical data: highest activity at pH 7.0 and 30°C using Man5 substrate | Direct human enzymology is not provided in retrieved texts, but the ortholog assay supports conserved catalytic preferences (thoma2024determinationexpressionand pages 1-2) |
| Donor specificity | Physiologic donor is UDP-GlcNAc; engineered studies show WT related MGAT enzymes can display some analog tolerance, but native MGAT1 function is defined by UDP-GlcNAc use | Recent bioorthogonal engineering work frames MGAT1 as a UDP-GlcNAc-dependent transferase and seeks variants that lose native donor use while accepting analogs, underscoring native donor specificity (liu2026iterativebumpandholeengineering pages 1-4, liu2024abioorthogonalprecision pages 1-2) |
| Acceptor specificity | Strong preference for the trimmed pentamannosyl N-glycan precursor rather than later complex products; recognizes a defined N-glycan arm rather than generic mannose residues | MGAT1 is repeatedly described as acting on Man5GlcNAc2 and specifically on the α1,3 arm, indicating narrow pathway position and acceptor selectivity (liu2026iterativebumpandholeengineering pages 1-4, thoma2024determinationexpressionand pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Site specificity within glycan | Adds GlcNAc to C-2 of the α1,3-linked core mannose | Explicitly stated in pathway descriptions of MGAT1 action (khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Substrate context | Acceptors are N-glycans attached to glycoproteins traversing the secretory pathway; the reaction occurs on luminal glycan chains rather than free cytosolic glycans | MGAT1 catalytic activity is described in the Golgi lumen on glycoprotein N-glycans (liu2026iterativebumpandholeengineering pages 1-4, huang2015gnt1iplspecificallyinhibits pages 1-2) |
| Consequence of loss of function | Abolishes synthesis of hybrid and complex N-glycans and enriches oligomannose/high-mannose structures | Demonstrated in knockout/knockdown systems in dendritic cells, thymocytes, and zebrafish (vicente2023mannosylatedglycansimpair pages 1-2, blomberg2025mgat1knockoutin pages 1-2, hall2023reductioninnacetylglucosaminyltransferasei pages 1-2) |
| Protein type | Type II transmembrane Golgi glycoprotein | Multiple reviews and studies describe MGAT1/Golgi glycosyltransferases as type II membrane proteins (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, thoma2024determinationexpressionand pages 1-2, huang2015gnt1iplspecificallyinhibits pages 1-2) |
| Domain organization | Short N-terminal cytosolic tail, single transmembrane domain, stem region, and large C-terminal luminal catalytic domain | Canonical architecture for MGAT1 and other Golgi glycosyltransferases is explicitly described (kizuka2024regulationofintracellular pages 1-2, huang2015gnt1iplspecificallyinhibits pages 1-2) |
| Membrane topology | N-terminus faces cytosol; catalytic ectodomain faces the Golgi lumen | Follows type II membrane topology and is necessary for luminal access to UDP-GlcNAc and glycoprotein acceptors (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Subcellular localization relevant to function | Golgi apparatus membrane, especially cis/medial-Golgi or medial-Golgi during early branching steps | MGAT1 is consistently placed in the Golgi, particularly where Man5 glycans are processed into hybrid/complex forms (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, huang2015gnt1iplspecificallyinhibits pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |
| Structural/catalytic architecture | Active-site-containing luminal catalytic domain plus additional glycan-recognition determinants/exosites inferred from GnT family structural studies; substrate recognition is highly pathway-ordered | Review literature notes crystal structures of rabbit GnT-I and exosite-based substrate recognition principles for N-glycan branching enzymes, supporting modular recognition beyond the catalytic center alone (biswas2020promiscuityandspecificity pages 1-2, liu2024abioorthogonalprecision pages 1-2) |
| Complexes influencing function | Can participate in Golgi multi-enzyme / multi-transporter assemblies with MAN2A2 and other MGATs, and with the UDP-GlcNAc transporter SLC35A3; can be inhibited by MGAT4D/GnT1IP-L in the Golgi | These interactions are relevant to efficient substrate channeling/regulation but do not alter the core catalytic definition of MGAT1 (huang2015gnt1iplspecificallyinhibits pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2) |


*Table: This table summarizes MGAT1’s core enzymatic function, donor and acceptor specificity, cofactor dependence, and structural organization for GO annotation review. It focuses on direct biochemical evidence and distinguishes core catalytic properties from regulatory interaction context.*

MGAT1 functions as a UDP-N-acetylglucosamine:α-1,3-D-mannoside β-1,2-N-acetylglucosaminyltransferase (EC 2.4.1.101) (thoma2024determinationexpressionand pages 1-2). The enzyme catalyzes the transfer of N-acetylglucosamine from the donor substrate UDP-GlcNAc to the C-2 position of the α-1,3-linked mannose residue in the acceptor substrate Man5GlcNAc2 (liu2026iterativebumpandholeengineering pages 1-4, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2). This reaction produces the first branch point that distinguishes oligomannose from hybrid/complex N-glycans and creates the obligatory intermediate for all subsequent branching by MGAT2, MGAT4, and MGAT5 (kizuka2024regulationofintracellular pages 1-2, abdelbary2023nlinkedglycansan pages 1-2).

Recent bioorthogonal engineering studies confirm that while MGAT1 can display some promiscuity toward modified UDP-GlcNAc analogs, the native physiological donor is strictly UDP-GlcNAc (liu2026iterativebumpandholeengineering pages 1-4, liu2024abioorthogonalprecision pages 1-2). The acceptor specificity is highly pathway-ordered: MGAT1 efficiently acts on the pentamannosyl precursor (Man5GlcNAc2) following prior trimming by Golgi mannosidases, but shows minimal activity toward later complex products or other mannose-containing structures (biswas2020promiscuityandspecificity pages 1-2, thoma2024determinationexpressionand pages 1-2).

### 2.2 Cofactor Requirements and Catalytic Mechanism

MGAT1 requires divalent metal ions for catalytic activity, with Mn²⁺ serving as the principal cofactor (thoma2024determinationexpressionand pages 1-2). Biochemical characterization of GnT-I orthologs demonstrates that enzyme activity is completely abolished by EDTA chelation or Cu²⁺ addition, while optimal activity occurs at approximately 40 mM Mn²⁺ concentration (thoma2024determinationexpressionand pages 1-2). The pH optimum is near physiological conditions (pH 7.0), consistent with Golgi luminal function (thoma2024determinationexpressionand pages 1-2).

Crystal structure analyses of rabbit GnT-I and related family members reveal a modular catalytic architecture with distinct donor and acceptor binding sites, including exosites that recognize specific N-glycan structural motifs beyond the immediate reaction center (biswas2020promiscuityandspecificity pages 1-2, liu2024abioorthogonalprecision pages 1-2). The catalytic domain adopts a GT-A fold typical of many glycosyltransferases and uses metal coordination to stabilize the UDP-GlcNAc donor during nucleophilic attack (kizuka2024regulationofintracellular pages 1-2).

### 2.3 Substrate Specificity

The strict substrate specificity of MGAT1 is central to its role as a biosynthetic gatekeeper. The enzyme recognizes Man5GlcNAc2 attached to asparagine residues within glycoproteins trafficking through the secretory pathway (liu2026iterativebumpandholeengineering pages 1-4, thoma2024determinationexpressionand pages 1-2). Importantly, MGAT1 does not act on free oligosaccharides or cytosolic substrates; the reaction occurs exclusively on luminal glycan chains of Golgi-resident or transiting glycoproteins (kizuka2024regulationofintracellular pages 1-2, huang2015gnt1iplspecificallyinhibits pages 1-2).

Structural and mutational studies indicate that MGAT1 makes specific contacts with the trimannosyl core and the α-1,3-mannose arm, positioning it to selectively modify this arm while excluding the α-1,6-mannose arm (which becomes a substrate for MGAT2 only after MGAT1 action and subsequent mannosidase II trimming) (biswas2020promiscuityandspecificity pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2). This ordered specificity ensures proper N-glycan maturation along the biosynthetic pathway.

---

## 3. BIOLOGICAL PROCESS ROLES

### 3.1 Core Biological Process: Protein N-Glycosylation

The primary and universally conserved biological process annotation for MGAT1 is **protein N-linked glycosylation**, specifically the conversion of oligomannose to hybrid and complex N-glycans (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, abdelbary2023nlinkedglycansan pages 1-2). MGAT1 initiates the biosynthesis of all complex-type and hybrid-type N-glycans by adding the first GlcNAc branch to the pentamannosyl core (kizuka2024regulationofintracellular pages 1-2). This function is absolutely required for complex N-glycan formation, as demonstrated by MGAT1 knockout systems that accumulate only oligomannose structures and completely lack hybrid/complex glycans (vicente2023mannosylatedglycansimpair pages 1-2, blomberg2025mgat1knockoutin pages 1-2, hall2023reductioninnacetylglucosaminyltransferasei pages 1-2).

### 3.2 Well-Supported Developmental and Physiological Processes

**Embryonic Development and Neural Tube Formation:**  
Loss of Mgat1 in mice causes embryonic lethality between E9.5 and E10.5, with severe neural tube maldevelopment being the primary cause of death (liu2026iterativebumpandholeengineering pages 1-4, hall2023reductioninnacetylglucosaminyltransferasei pages 1-2). This phenotype reflects the essential requirement for complex N-glycan structures on multiple developmental glycoproteins rather than a specific developmental signaling function of MGAT1 itself. In zebrafish models, reduced Mgat1 activity decreases survivability, delays brain anlagen formation, impairs skeletal muscle development, and disrupts cardiac activity onset (hall2023reductioninnacetylglucosaminyltransferasei pages 1-2).

**T-Cell Development and Immune Cell Maturation:**  
Conditional deletion of Mgat1 in mouse thymocytes, which restricts N-glycosylation to high-mannose structures, causes profound defects in β-selection at the DN3-to-DN4 transition, impaired regulatory T-cell (Treg) generation, and altered γδ T-cell development (vicente2023mannosylatedglycansimpair pages 1-2). These phenotypes are associated with increased susceptibility to colon and kidney inflammation, demonstrating that MGAT1-dependent N-glycan maturation is critical for establishing proper immune homeostasis (vicente2023mannosylatedglycansimpair pages 1-2). However, these effects are mediated through altered glycosylation of T-cell receptors and coreceptors, not through direct participation of MGAT1 in TCR signaling or inflammation pathways.

Similarly, MGAT1 knockout in human dendritic cells enhances their capacity to activate CD8⁺ T cells by altering surface densities of costimulatory molecules and MHC complexes (blomberg2025mgat1knockoutin pages 1-2). This finding supports annotation to immune cell development and maturation processes, but emphasizes that MGAT1 acts indirectly by modulating the glycosylation state of immune receptors.

**Spermatogenesis:**  
MGAT1 regulatory partner MGAT4D (GnT1IP) is highly expressed in spermatocytes and spermatids, and conditional deletion of Mgat2 in mouse germ cells blocks spermatogenesis, indicating overlapping requirements for N-glycan branching in male fertility (huang2015gnt1iplspecificallyinhibits pages 1-2). While direct human MGAT1-specific spermatogenesis evidence is limited in the retrieved literature, orthologous mammalian data support a conserved role in germ cell glycoprotein maturation.

### 3.3 Context-Specific and Substrate-Mediated Processes

Recent studies (2023-2025) have identified several MGAT1-associated processes that reflect context-specific, substrate-dependent phenomena rather than core MGAT1 functions:

**Cancer Progression and Immune Evasion:**  
In triple-negative breast cancer (TNBC), MGAT1 overexpression drives complex N-glycosylation of CD73, promoting its membrane translocation via VAMP3-mediated fusion and enabling adenosine-dependent suppression of CD8⁺ T cell function (chi2025mgat1guidedcomplexnglycans pages 1-2). This represents a substrate-specific mechanism where MGAT1 indirectly promotes immune evasion by modifying a particular immunosuppressive ectoenzyme. Similar substrate-specific effects have been reported for other glycoproteins in various cancers (chi2025mgat1guidedcomplexnglycans pages 1-2, tang2023transcriptomicandglycomic pages 1-2). These findings should **not** lead to direct GO annotations of MGAT1 to "immune evasion" or "cancer progression," as the enzyme itself does not possess intrinsic oncogenic or immunosuppressive activity—it is the altered glycosylation of specific substrates in specific cellular contexts that drives these phenotypes.

**Metabolic Regulation in Regulatory T Cells:**  
A notable 2024 study reports that lactate treatment of human Tregs increases MGAT1 expression and proposes that MGAT1 translocates to mitochondria, where it modulates oxidative phosphorylation through N-glycosylation of mitochondrial proteins such as progranulin (GRN) and HYOU1 (zhou2024lactatesupportstreg pages 1-2). This finding is mechanistically provocative but represents an emerging, context-specific observation that contrasts sharply with the well-established Golgi-resident model of MGAT1 (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, huang2015gnt1iplspecificallyinhibits pages 1-2). Independent validation is needed before this mitochondrial role is incorporated into core GO annotations.

**Neuronal Function and Alzheimer's Disease:**  
Transcriptomic analysis of Alzheimer's disease (AD) brain tissue shows upregulation of MGAT1 and corresponding increases in complex N-glycan abundance (tang2023transcriptomicandglycomic pages 1-2). While this implicates MGAT1-dependent glycosylation in AD pathophysiology, it does not establish MGAT1 as a direct mediator of neurodegeneration or apoptosis. Previous literature cited in AD studies mentions associations between MGAT1 defects and neuronal apoptosis (tang2023transcriptomicandglycomic pages 1-2), but these are secondary consequences of failed glycoprotein maturation rather than evidence for direct apoptotic functions.

**Inflammatory Responses:**  
Mgat1-deficient thymocytes show increased susceptibility to inflammatory conditions in mouse models (vicente2023mannosylatedglycansimpair pages 1-2). However, this phenotype arises from defective T-cell development and altered immune receptor glycosylation, not from direct MGAT1 participation in inflammatory signaling cascades. Annotation to broad inflammatory response terms should be avoided unless there is evidence of direct MGAT1 involvement beyond its glycosyltransferase activity.

---

## 4. CELLULAR LOCALIZATION AND COMPLEXES

### 4.1 Subcellular Localization

MGAT1 is a **type II transmembrane protein** localized to the **Golgi apparatus membrane**, specifically the **medial-Golgi** compartment where early N-glycan branching occurs (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, huang2015gnt1iplspecificallyinhibits pages 1-2). The protein has a short N-terminal cytosolic tail, a single-pass transmembrane domain, a stem region, and a large C-terminal catalytic domain that faces the Golgi lumen (kizuka2024regulationofintracellular pages 1-2, thoma2024determinationexpressionand pages 1-2). This topology allows MGAT1 to access both the UDP-GlcNAc donor (delivered by luminal nucleotide sugar transporters) and the glycoprotein acceptors traversing the secretory pathway (huang2015gnt1iplspecificallyinhibits pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2).

MGAT1 retention in the Golgi is mediated by multiple factors, including transmembrane domain length, stem region interactions, and oligomerization with other Golgi-resident enzymes (kizuka2024regulationofintracellular pages 1-2, khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2). The enzyme does not constitutively localize to the cytoplasm, cytosol, or nucleus under normal physiological conditions (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4).

**Annotation Risk - Mitochondrial Localization:**  
A recent study proposes lactate-induced translocation of MGAT1 to mitochondria in activated human Tregs (zhou2024lactatesupportstreg pages 1-2). This claim, if validated, would represent a novel and context-specific localization. However, it contrasts with decades of established Golgi-resident literature and requires independent confirmation before being incorporated into core cellular component annotations. Current GO annotation should prioritize the canonical Golgi membrane localization.

### 4.2 Protein Complexes and Interactions

MGAT1 participates in several functionally relevant protein complexes within the Golgi membrane:

**Multi-Enzyme Assemblies:**  
High-throughput FRET and BiFC interaction screens demonstrate that MGAT1 forms homomeric and heteromeric assemblies with other N-glycan processing enzymes, including MGAT2, MGAT3, MGAT4B, and the mannosidase MAN2A2 (khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2). MAN2A2 acts as a central hub in these complexes, consistent with its sequential action immediately downstream of MGAT1 (khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2). These multi-enzyme complexes likely facilitate efficient substrate channeling and coordinated N-glycan maturation.

**Nucleotide Sugar Transporter Interactions:**  
MGAT1 associates with nucleotide sugar transporters, particularly SLC35A3 (the UDP-GlcNAc transporter), forming multi-enzyme/multi-transporter assemblies in Golgi membranes (khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2). These interactions ensure efficient delivery of UDP-GlcNAc to the catalytic site and may contribute to Golgi retention (khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2).

**Inhibitory Interaction with MGAT4D (GnT1IP-L):**  
MGAT1 interacts specifically with MGAT4D/GnT1IP-L in the Golgi, where GnT1IP-L inhibits MGAT1 activity via its luminal domain (huang2015gnt1iplspecificallyinhibits pages 1-2). This regulatory interaction is predominantly observed in spermatogenic cells and provides a physiological mechanism for modulating MGAT1 activity in specific developmental contexts (huang2015gnt1iplspecificallyinhibits pages 1-2). Importantly, GnT1IP-L does not interact with other medial-Golgi GlcNAc transferases (MGAT2, MGAT3, MGAT4B, MGAT5), demonstrating specificity for MGAT1 (huang2015gnt1iplspecificallyinhibits pages 1-2).

**Interaction with BRI3:**  
UniProt metadata indicates MGAT1 interacts with BRI3 isoforms, with stronger interaction with isoform 1 than isoform 2 (UniProt entry). This interaction may contribute to Golgi organization or enzyme regulation, though detailed functional studies are not present in the retrieved literature set.

---

## 5. ANNOTATION-RISK ASSESSMENT

### 5.1 Core Function vs. Pleiotropic Effects

The central annotation risk for MGAT1 is the conflation of **direct enzymatic function** with **indirect, substrate-mediated phenotypes**. MGAT1 is fundamentally a glycosyltransferase that modifies N-glycans on hundreds of glycoproteins. The biological consequences of MGAT1 activity are thus highly pleiotropic, reflecting the diverse functions of its glycoprotein substrates rather than intrinsic properties of MGAT1 itself.

**High-Confidence Core Annotations:**
- Molecular Function: N-acetylglucosaminyltransferase activity (EC 2.4.1.101)
- Biological Process: Protein N-linked glycosylation; complex N-glycan biosynthetic process
- Cellular Component: Golgi apparatus membrane; medial-Golgi

**Well-Supported Physiological Process Annotations:**
- Embryonic development (essential for viability and neural tube formation)
- T-cell development and differentiation
- Immune system development

**Context-Specific Annotations Requiring Caution:**
- Cancer progression, metastasis, immune evasion: These are **substrate-specific** effects mediated by MGAT1 modification of particular glycoproteins (e.g., CD73, integrins) in specific cellular contexts (chi2025mgat1guidedcomplexnglycans pages 1-2). Direct annotation of MGAT1 to "negative regulation of immune response" or "positive regulation of cell migration" would be misleading.
- Inflammatory response: Observed phenotypes in Mgat1-deficient models reflect altered immune cell development and receptor glycosylation, not direct MGAT1 participation in inflammatory signaling (vicente2023mannosylatedglycansimpair pages 1-2).
- Apoptosis and neuronal cell death: Associations with neurological phenotypes and cell death are secondary to failed glycoprotein maturation, not evidence of direct apoptotic functions (tang2023transcriptomicandglycomic pages 1-2).
- Mitochondrial localization and metabolic regulation: Emerging data from specialized Treg contexts (zhou2024lactatesupportstreg pages 1-2) require validation and should not replace canonical Golgi annotations without strong confirmatory evidence.

### 5.2 Distinguishing Direct vs. Indirect Roles

A useful principle for MGAT1 annotation is to ask: **Does this process or localization reflect the direct biochemical activity of MGAT1 as a Golgi-resident glycosyltransferase, or does it reflect consequences of altered glycosylation on specific substrate proteins?**

For example:
- "Protein N-glycosylation" ✓ Direct
- "Complex N-glycan biosynthetic process" ✓ Direct
- "Embryonic neural tube formation" ✓ Well-supported (essential gene)
- "T-cell receptor signaling pathway" ✗ Indirect (MGAT1 modifies TCR glycans; it does not transduce TCR signals)
- "Negative regulation of T-cell activation" ✗ Indirect (context-dependent effect via substrate glycoproteins)
- "Immune evasion" ✗ Highly context-specific (substrate-mediated in cancer)
- "Apoptosis" ✗ Indirect (consequence of failed glycoprotein function, not direct apoptotic activity)

### 5.3 Over-Extension Risks

Several specific annotation risks merit attention:

1. **Avoid cytoplasmic/cytosolic/nuclear localization annotations** unless strong direct evidence emerges. Current data overwhelmingly support Golgi membrane residence (kizuka2024regulationofintracellular pages 1-2, liu2026iterativebumpandholeengineering pages 1-4, huang2015gnt1iplspecificallyinhibits pages 1-2).

2. **Mitochondrial annotations require caution.** The 2024 lactate/Treg study (zhou2024lactatesupportstreg pages 1-2) is provocative but represents a single, context-specific report. Until independently validated, mitochondrial localization should be noted as emerging/provisional rather than replacing core Golgi annotations.

3. **Signaling complex annotations are generally inappropriate.** MGAT1 does not participate in canonical signal transduction complexes. It forms functional complexes with other Golgi glycosylation enzymes and transporters (khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2), which is appropriate for cellular component annotation, but these should not be conflated with signaling scaffolds.

4. **Disease-association does not equal direct function.** Altered MGAT1 expression correlates with cancer, neurodegeneration, and immune disorders (chi2025mgat1guidedcomplexnglycans pages 1-2, tang2023transcriptomicandglycomic pages 1-2), but these are phenotypic associations rather than evidence for direct MGAT1 roles in oncogenesis or neurodegeneration.

---

## 6. KEY LITERATURE

| Category | Reference | Journal | DOI / URL | Contribution to MGAT1 GO annotation review |
|---|---|---|---|---|
| Recent high-quality study | Zhou et al., 2024 | *Journal of Clinical Investigation* | https://doi.org/10.1172/JCI175897 | Reports a novel, context-specific claim that lactate increases MGAT1 expression and promotes apparent mitochondrial localization/translocation in human Tregs, linking MGAT1 to Treg OXPHOS. Useful mainly as an annotation-risk paper because it challenges the canonical Golgi-only view and likely requires independent validation before broad GO transfer (zhou2024lactatesupportstreg pages 1-2). |
| Recent high-quality study | Kizuka, 2024 | *Journal of Biological Chemistry* | https://doi.org/10.1016/j.jbc.2024.107471 | Authoritative recent review of mammalian N-glycan branching enzymes. Clearly places MGAT1 as the enzyme that transfers GlcNAc to Man5 structures to initiate complex-type N-glycan biosynthesis, and summarizes Golgi-resident type II membrane protein architecture and regulatory principles relevant to GO MF/BP/CC terms (kizuka2024regulationofintracellular pages 1-2). |
| Recent high-quality study | Hall et al., 2023 | *Current Issues in Molecular Biology* | https://doi.org/10.3390/cimb45110575 | Zebrafish study showing reduced Mgat1 activity increases oligomannose glycans, decreases complex glycans, and impairs survival, brain anlagen formation, muscle development, sensory responses, and cardiac onset. Useful for conserved developmental-process support, but should be interpreted as downstream consequences of defective N-glycan maturation (hall2023reductioninnacetylglucosaminyltransferasei pages 1-2). |
| Recent high-quality study | Vicente et al., 2023 | *Cellular & Molecular Immunology* | https://doi.org/10.1038/s41423-023-01052-7 | Conditional mouse thymocyte study showing Mgat1-dependent restriction of high-mannose glycans is required for normal β-selection, γδ T-cell development, and Treg generation. Strong evidence for immune-development phenotypes mediated by MGAT1-dependent N-glycan maturation (vicente2023mannosylatedglycansimpair pages 1-2). |
| Recent high-quality study | Tang et al., 2023 | *Scientific Reports* | https://doi.org/10.1038/s41598-023-34787-4 | Human AD transcriptomic/glycomic study showing MGAT1 upregulation correlates with increased complex N-glycan features in brain. Useful as disease-context evidence of expression change, but not strong support for direct GO process annotation beyond N-glycosylation pathway involvement (tang2023transcriptomicandglycomic pages 1-2). |
| Foundational biochemical / pathway paper | Huang et al., 2015 | *eLife* | https://doi.org/10.7554/eLife.08916 | Defines MGAT1 as the GlcNAc-transferase that transfers GlcNAc from UDP-GlcNAc to Man5GlcNAc2Asn in the medial Golgi to initiate hybrid/complex N-glycan synthesis. Also provides evidence for specific Golgi inhibition by GnT1IP-L/MGAT4D, relevant to regulation and interaction annotations (huang2015gnt1iplspecificallyinhibits pages 1-2). |
| Foundational biochemical / pathway paper | Khoder-Agha et al., 2019 | *Cellular and Molecular Life Sciences* | https://doi.org/10.1007/s00018-019-03032-5 | Demonstrates that MGAT1 forms Golgi membrane assemblies with MGAT2, MGAT3, MGAT4B, MAN2A2, and nucleotide sugar transporters including SLC35A3. Important for refined cellular-component and complex-context review, while still supporting canonical Golgi localization (khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2). |
| Foundational biochemical / pathway paper | Thoma et al., 2024 | *Glycoconjugate Journal* | https://doi.org/10.1007/s10719-024-10148-9 | Biochemical characterization of GnT-I ortholog showing the canonical reaction: transfer of GlcNAc from UDP-GlcNAc to the α1,3-Man arm of Man5GlcNAc2; also shows Mn2+ dependence and EDTA sensitivity. Valuable for catalytic specificity and cofactor expectations when direct human enzymology is sparse in the retrieved set (thoma2024determinationexpressionand pages 1-2). |
| Foundational structural / mechanistic review | Nagae et al., 2020 | *International Journal of Molecular Sciences* | https://doi.org/10.3390/ijms21020437 | Review summarizing structural and mechanistic knowledge of N-glycan maturation enzymes, including rabbit GnT-I crystal structure and exosite concepts. Useful for framing MGAT1 substrate recognition and catalytic architecture in GO molecular-function review (kizuka2024regulationofintracellular pages 1-2). |
| Foundational conceptual review | Abdelbary & Nolz, 2023 | *Immunometabolism* | http://dx.doi.org/10.1097/IN9.0000000000000035 | Immune-focused review that clearly explains MGAT1 as the critical step after mannose trimming that enables hybrid and then complex N-glycan formation. Useful for concise pathway description and for linking MGAT1 to T-cell developmental biology without overstating direct signaling roles (abdelbary2023nlinkedglycansan pages 1-2). |
| Key developmental / physiological study | Hall et al., 2023 | *Current Issues in Molecular Biology* | https://doi.org/10.3390/cimb45110575 | Supports developmental and organismal viability roles of MGAT1 through glycan maturation defects, especially in nervous-system and muscle-related phenotypes in zebrafish (hall2023reductioninnacetylglucosaminyltransferasei pages 1-2). |
| Key developmental / physiological study | Vicente et al., 2023 | *Cellular & Molecular Immunology* | https://doi.org/10.1038/s41423-023-01052-7 | Supports a physiological requirement for MGAT1 in thymocyte maturation and immune homeostasis, with inflammation susceptibility arising secondarily from altered thymocyte glycosylation (vicente2023mannosylatedglycansimpair pages 1-2). |
| Annotation-risk assessment | Chi et al., 2025 | *Nature Communications* | https://doi.org/10.1038/s41467-025-58524-9 | Shows MGAT1-dependent glycosylation of CD73 in triple-negative breast cancer can drive membrane trafficking and immune evasion. Important as a cautionary example: such cancer-specific substrate effects should not be generalized into core MGAT1 GO annotations like 'immune evasion' or broad signaling-complex localization (chi2025mgat1guidedcomplexnglycans pages 1-2). |
| Annotation-risk assessment | Blomberg et al., 2025 | *Frontiers in Immunology* | https://doi.org/10.3389/fimmu.2025.1588795 | MGAT1 KO in human dendritic cells abolishes hybrid/complex N-glycans and enhances CD8 T-cell activation. Useful to show that immune phenotypes can be robust yet indirect consequences of global N-glycan remodeling, arguing for caution in assigning direct inflammatory or activation-process terms to MGAT1 (blomberg2025mgat1knockoutin pages 1-2). |
| Annotation-risk assessment | Zhou et al., 2024 | *Journal of Clinical Investigation* | https://doi.org/10.1172/JCI175897 | Especially relevant for reviewing proposed noncanonical mitochondrial localization and metabolic roles. Strong direct experimental claim in a specialized cell context, but because it diverges from longstanding Golgi-resident consensus, it should be treated as emerging rather than replacing core MGAT1 CC annotations (zhou2024lactatesupportstreg pages 1-2, kizuka2024regulationofintracellular pages 1-2). |
| Annotation-risk assessment | Tang et al., 2023 | *Scientific Reports* | https://doi.org/10.1038/s41598-023-34787-4 | Disease-association paper that links altered MGAT1 expression with AD-related glycomic changes; useful to distinguish expression correlation and pathology context from direct causal GO process annotation such as apoptosis or neurodegeneration (tang2023transcriptomicandglycomic pages 1-2). |


*Table: This table compiles the most relevant literature for MGAT1 GO annotation review, separating core biochemical and developmental evidence from context-specific studies that pose annotation-risk. It is designed to help distinguish canonical MGAT1 function and localization from indirect disease- or cell-type-specific effects.*

---

## SUMMARY RECOMMENDATIONS FOR GO ANNOTATION

Based on comprehensive literature review, the following annotation framework is recommended:

**Molecular Function (High Confidence):**
- N-acetylglucosaminyltransferase activity (EC 2.4.1.101)
- UDP-N-acetylglucosamine:α-1,3-D-mannoside β-1,2-N-acetylglucosaminyltransferase activity
- Metal ion binding (Mn²⁺)

**Biological Process (High Confidence):**
- Protein N-linked glycosylation
- Complex N-glycan biosynthetic process
- Asparagine-linked glycosylation

**Biological Process (Well-Supported, Organism-Level):**
- Embryonic development
- Neural tube formation
- T-cell differentiation
- Immune system development

**Cellular Component (High Confidence):**
- Golgi apparatus membrane
- Medial-Golgi
- Integral component of membrane

**Avoid or Use with Extreme Caution:**
- Direct annotation to apoptosis, immune evasion, inflammatory response, cancer progression (these are indirect, substrate-mediated)
- Cytoplasm, cytosol, nucleus (not supported by current evidence)
- Mitochondrion (emerging claim requiring validation)
- Generic "signaling complex" terms (not applicable to glycosyltransferase complexes)

**Interaction Annotations (Moderate Confidence):**
- Physical interaction with MGAT2, MGAT3, MGAT4B, MAN2A2, SLC35A3, MGAT4D, BRI3
- Participation in Golgi multi-enzyme assemblies

This framework distinguishes the well-established core function of MGAT1 as a Golgi-resident glycosyltransferase from context-specific, substrate-mediated phenotypes that arise from altered N-glycan structures on diverse glycoprotein substrates. Proper annotation should reflect this distinction to avoid over-extending MGAT1's functional repertoire beyond its direct biochemical role.

---

**References:** Citations are embedded throughout the report using context IDs () corresponding to specific literature sources detailed in the Key Literature table (artifact-02).

References

1. (kizuka2024regulationofintracellular pages 1-2): Yasuhiko Kizuka. Regulation of intracellular activity of n-glycan branching enzymes in mammals. Jul 2024. URL: https://doi.org/10.1016/j.jbc.2024.107471, doi:10.1016/j.jbc.2024.107471. This article has 28 citations and is from a domain leading peer-reviewed journal.

2. (abdelbary2023nlinkedglycansan pages 1-2): Mahmoud Abdelbary and Jeffrey C. Nolz. N-linked glycans: an underappreciated key determinant of t cell development, activation, and function. Immunometabolism (Cobham, Surrey), 5:e00035-e00035, Oct 2023. URL: https://doi.org/10.1097/in9.0000000000000035, doi:10.1097/in9.0000000000000035. This article has 9 citations.

3. (liu2026iterativebumpandholeengineering pages 1-4): Yu Liu, Saskia Pieters, Ganka Bineva-Todd, Mert Sagiroglugil, Sean A. Burnap, Freya Hoddle, Anna Cioce, Andre Ohara, Kevin Bruemmer, Carolyn R. Bertozzi, Karen Polizzi, Weston B. Struwe, Carme Rovira, and Benjamin Schumann. Iterative bump-and-hole engineering creates a bioorthogonal reporter for <i>n</i> -acetylglucosaminyltransferase i. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.16.699845, doi:10.64898/2026.01.16.699845. This article has 0 citations.

4. (thoma2024determinationexpressionand pages 1-2): Julia Thoma, Reingard Grabherr, and Erika Staudacher. Determination, expression and characterization of an udp-n-acetylglucosamine:α-1,3-d-mannoside β-1,2-n-acetylglucosaminyltransferase i (gnt-i) from the pacific oyster, crassostrea gigas. Glycoconjugate Journal, 41:151-162, Apr 2024. URL: https://doi.org/10.1007/s10719-024-10148-9, doi:10.1007/s10719-024-10148-9. This article has 3 citations and is from a peer-reviewed journal.

5. (huang2015gnt1iplspecificallyinhibits pages 1-2): Hung-Hsiang Huang, Antti Hassinen, Subha Sundaram, Andrej-Nikolai Spiess, Sakari Kellokumpu, and Pamela Stanley. Gnt1ip-l specifically inhibits mgat1 in the golgi via its luminal domain. eLife, Sep 2015. URL: https://doi.org/10.7554/elife.08916, doi:10.7554/elife.08916. This article has 30 citations and is from a domain leading peer-reviewed journal.

6. (khoderagha2019nacetylglucosaminyltransferasesandnucleotide pages 1-2): Fawzi Khoder-Agha, Paulina Sosicka, Maria Escriva Conde, Antti Hassinen, Tuomo Glumoff, Mariusz Olczak, and Sakari Kellokumpu. N-acetylglucosaminyltransferases and nucleotide sugar transporters form multi-enzyme–multi-transporter assemblies in golgi membranes in vivo. Cellular and Molecular Life Sciences: CMLS, 76:1821-1832, Feb 2019. URL: https://doi.org/10.1007/s00018-019-03032-5, doi:10.1007/s00018-019-03032-5. This article has 57 citations.

7. (hall2023reductioninnacetylglucosaminyltransferasei pages 1-2): M. Kristen Hall, Cody J. Hatchett, Sergei Shalygin, Parastoo Azadi, and Ruth A. Schwalbe. Reduction in n-acetylglucosaminyltransferase-i activity decreases survivability and delays development of zebrafish. Current Issues in Molecular Biology, 45:9165-9180, Nov 2023. URL: https://doi.org/10.3390/cimb45110575, doi:10.3390/cimb45110575. This article has 7 citations.

8. (vicente2023mannosylatedglycansimpair pages 1-2): Manuel M. Vicente, Inês Alves, Ângela Fernandes, Ana M. Dias, Beatriz Santos-Pereira, Elena Pérez-Anton, Sofia Santos, Tao Yang, Alexandra Correia, Anja Münster-Kühnel, Afonso R. M. Almeida, Sarina Ravens, Gabriel A. Rabinovich, Manuel Vilanova, Ana E. Sousa, and Salomé S. Pinho. Mannosylated glycans impair normal t-cell development by reprogramming commitment and repertoire diversity. Cellular and Molecular Immunology, 20:955-968, Jun 2023. URL: https://doi.org/10.1038/s41423-023-01052-7, doi:10.1038/s41423-023-01052-7. This article has 41 citations and is from a peer-reviewed journal.

9. (chi2025mgat1guidedcomplexnglycans pages 1-2): Junlong Jack Chi, Ping Xie, Mary Hongying Cheng, Yueming Zhu, Xin Cui, Joshua Watson, Lidan Zeng, Amad Uddin, Hoang Nguyen, Lei Li, Kelley Moremen, April Reedy, Megan Wyatt, Adam Marcus, Mingji Dai, Chrystal M. Paulos, Massimo Cristofanilli, William J. Gradishar, Shaying Zhao, Kevin Kalinsky, Mine-Chie Hung, Ivet Bahar, Bin Zhang, and Yong Wan. Mgat1-guided complex n-glycans on cd73 regulate immune evasion in triple-negative breast cancer. Nature Communications, Apr 2025. URL: https://doi.org/10.1038/s41467-025-58524-9, doi:10.1038/s41467-025-58524-9. This article has 15 citations and is from a highest quality peer-reviewed journal.

10. (zhou2024lactatesupportstreg pages 1-2): Jinren Zhou, Jian Gu, Qufei Qian, Yigang Zhang, Tianning Huang, Xiangyu Li, Zhuoqun Liu, Qing Shao, Yuan Liang, Lei Qiao, Xiaozhang Xu, Qiuyang Chen, Zibo Xu, Yu Li, Ji Gao, Yufeng Pan, Yiming Wang, Roderick O’Connor, Keli L. Hippen, Ling Lu, and Bruce R. Blazar. Lactate supports treg function and immune balance via mgat1 effects on n-glycosylation in the mitochondria. Journal of Clinical Investigation, Sep 2024. URL: https://doi.org/10.1172/jci175897, doi:10.1172/jci175897. This article has 55 citations and is from a highest quality peer-reviewed journal.

11. (blomberg2025mgat1knockoutin pages 1-2): Anne Louise Blomberg, Betina Lyngfeldt Henriksen, Weihua Tian, Kerstin Skovgaard, Sarah Line Skovbakke, and Steffen Goletz. Mgat1 knockout in human dendritic cells enhance cd8+ t cell activation. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1588795, doi:10.3389/fimmu.2025.1588795. This article has 0 citations and is from a peer-reviewed journal.

12. (liu2024abioorthogonalprecision pages 1-2): Yu Liu, Ganka Bineva-Todd, Richard W. Meek, Laura Mazo, Beatriz Piniello, Olga Moroz, Sean A. Burnap, Nadima Begum, André Ohara, Chloe Roustan, Sara Tomita, Svend Kjaer, Karen Polizzi, Weston B. Struwe, Carme Rovira, Gideon J. Davies, and Benjamin Schumann. A bioorthogonal precision tool for human n-acetylglucosaminyltransferase v. Journal of the American Chemical Society, 146:26707-26718, Sep 2024. URL: https://doi.org/10.1021/jacs.4c05955, doi:10.1021/jacs.4c05955. This article has 10 citations and is from a highest quality peer-reviewed journal.

13. (biswas2020promiscuityandspecificity pages 1-2): Ansuman Biswas and Mukund Thattai. Promiscuity and specificity of eukaryotic glycosyltransferases. Biochemical Society Transactions, 48:891-900, Jun 2020. URL: https://doi.org/10.1042/bst20190651, doi:10.1042/bst20190651. This article has 62 citations and is from a peer-reviewed journal.

14. (tang2023transcriptomicandglycomic pages 1-2): Xinyu Tang, Jennyfer Tena, Jacopo Di Lucente, Izumi Maezawa, Danielle J. Harvey, Lee-Way Jin, Carlito B. Lebrilla, and Angela M. Zivkovic. Transcriptomic and glycomic analyses highlight pathway-specific glycosylation alterations unique to alzheimer’s disease. Scientific Reports, May 2023. URL: https://doi.org/10.1038/s41598-023-34787-4, doi:10.1038/s41598-023-34787-4. This article has 45 citations and is from a peer-reviewed journal.