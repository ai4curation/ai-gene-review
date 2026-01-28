---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T18:29:47.590493'
end_time: '2026-01-23T18:44:54.157220'
duration_seconds: 906.57
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RAD18
  gene_symbol: RAD18
  uniprot_accession: Q9NS91
  protein_description: 'RecName: Full=E3 ubiquitin-protein ligase RAD18; EC=2.3.2.27;
    AltName: Full=Postreplication repair protein RAD18; Short=hHR18; Short=hRAD18;
    AltName: Full=RING finger protein 73; AltName: Full=RING-type E3 ubiquitin transferase
    RAD18 {ECO:0000305};'
  gene_info: Name=RAD18; Synonyms=RNF73;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the RAD18 family. .
  protein_domains: Rad18. (IPR039577); Rad18_UBZ4. (IPR006642); SAP_dom. (IPR003034);
    SAP_dom_sf. (IPR036361); Znf_RING. (IPR001841)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9NS91
- **Protein Description:** RecName: Full=E3 ubiquitin-protein ligase RAD18; EC=2.3.2.27; AltName: Full=Postreplication repair protein RAD18; Short=hHR18; Short=hRAD18; AltName: Full=RING finger protein 73; AltName: Full=RING-type E3 ubiquitin transferase RAD18 {ECO:0000305};
- **Gene Information:** Name=RAD18; Synonyms=RNF73;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the RAD18 family. .
- **Key Domains:** Rad18. (IPR039577); Rad18_UBZ4. (IPR006642); SAP_dom. (IPR003034); SAP_dom_sf. (IPR036361); Znf_RING. (IPR001841)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RAD18" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RAD18' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RAD18** (gene ID: RAD18, UniProt: Q9NS91) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RAD18: E3 Ubiquitin-Protein Ligase in DNA Damage Tolerance

## Introduction

RAD18 (also known as RNF73, RING finger protein 73) is an E3 ubiquitin-protein ligase that plays a central role in the cellular response to DNA damage, particularly in the DNA damage tolerance (DDT) pathway that allows cells to complete replication despite the presence of DNA lesions [hedglin-2015-regulation-abstract]. The human RAD18 gene was first identified as a homolog of the yeast RAD18, mapping to chromosome 3p24-25, a region frequently deleted in various cancers including lung, breast, ovary, and testis malignancies [tateishi-2000-dysfunction-abstract]. RAD18 functions primarily by catalyzing the monoubiquitination of proliferating cell nuclear antigen (PCNA) at lysine 164, a modification that serves as a molecular switch to recruit specialized translesion synthesis (TLS) polymerases capable of bypassing DNA lesions that would otherwise stall replicative polymerases [watanabe-2004-poleta-abstract].

The protein operates as part of an E2-E3 complex with the ubiquitin-conjugating enzyme RAD6 (also called UBE2A/UBE2B or hHR6), and this partnership is essential for its function in postreplication repair [tateishi-2000-dysfunction-abstract]. Beyond its canonical role in TLS, RAD18 has been implicated in additional DNA repair processes including homologous recombination, double-strand break repair, and the Fanconi anemia pathway, establishing it as a multifunctional coordinator of genome maintenance [huang-2009-hrrrepair-abstract; geng-2010-fanconianemia-abstract]. The enzymatic activity of RAD18 (EC 2.3.2.27) classifies it as a RING-type E3 ubiquitin transferase, and the protein belongs to the RAD18 family of ubiquitin ligases that is conserved across eukaryotes.

## Enzymatic Activity and Substrate Specificity

RAD18 functions as an E3 ubiquitin-protein ligase that catalyzes the transfer of ubiquitin from an E2 ubiquitin-conjugating enzyme to specific substrate proteins. The primary and best-characterized substrate of RAD18 is PCNA, specifically at lysine 164 [watanabe-2004-poleta-abstract]. This monoubiquitination event is critical for initiating translesion DNA synthesis in response to replication fork stalling at DNA lesions.

A key mechanistic insight into RAD18 function was provided by structural and biochemical studies demonstrating that the RAD6/RAD18 complex specifically promotes monoubiquitination rather than polyubiquitin chain formation [hibbert-2011-monoubiquitination-abstract]. The E2 enzyme RAD6, when functioning alone, possesses an intrinsic capability for ubiquitin chain synthesis through a noncovalent interaction between ubiquitin and a "backside" binding site on RAD6. However, when RAD6 associates with RAD18, the C-terminal RAD6-binding domain (R6BD) of RAD18 competitively occupies this backside binding site, thereby preventing ubiquitin from binding there and blocking chain formation [hibbert-2011-monoubiquitination-abstract]. This elegant mechanism ensures that PCNA receives only a single ubiquitin moiety, which is the specific signal for TLS polymerase recruitment.

The substrate specificity of RAD18 extends beyond PCNA. Studies have identified 53BP1 as an additional direct substrate of RAD18-mediated ubiquitination [watanabe-2009-53bp1-abstract]. RAD18 monoubiquitinates the kinetochore-binding domain of 53BP1 at lysine 1268, and this modification enhances the chromatin retention of 53BP1 at sites of DNA double-strand breaks during G1 phase. RFC2, a subunit of the replication factor C complex, has also been reported as a RAD18 substrate [hedglin-2015-regulation-abstract]. The identification of multiple substrates indicates that RAD18 coordinates several aspects of the DNA damage response through its ubiquitination activity.

The complex stoichiometry of functional RAD18 has been elucidated through detailed structural analysis. The active complex consists of one RAD6 molecule bound to a RAD18 homodimer, forming a RAD6A-(RAD18)₂ ternary complex [masuda-2012-asymmetric-abstract]. Interestingly, only one of the two RAD6-binding domains in the RAD18 dimer is necessary for complex formation and ligase activity, revealing an asymmetric functional architecture. Similarly, while inactivating mutations in the RING or SAP domains of both RAD18 subunits strongly reduces activity, inactivation in only one subunit has no effect, further supporting the asymmetric model.

## Role in Translesion Synthesis and DNA Damage Tolerance

Translesion synthesis represents one of the two major DNA damage tolerance pathways that allow cells to complete DNA replication despite the presence of template lesions. When replicative polymerases encounter DNA damage, they stall, leading to uncoupling between the replicative helicase and polymerase activities. This uncoupling generates extended stretches of single-stranded DNA (ssDNA) that become coated with replication protein A (RPA) [hedglin-2015-regulation-abstract]. The RPA-ssDNA complex serves as the primary signal for RAD18 recruitment to stalled replication forks.

Upon recruitment, RAD18 together with RAD6 catalyzes the monoubiquitination of PCNA at K164. This modified form of PCNA (monoUb-PCNA) has substantially increased affinity for Y-family TLS polymerases, particularly DNA polymerase eta (Polη), compared to unmodified PCNA [watanabe-2004-poleta-abstract]. The enhanced affinity facilitates polymerase exchange at the stalled fork, allowing TLS polymerases to incorporate nucleotides opposite damaged template bases. Although TLS polymerases can replicate past lesions, they lack the proofreading activity of replicative polymerases and are often error-prone, which explains why TLS is associated with damage-induced mutagenesis.

RAD18 participates in TLS polymerase recruitment through two complementary mechanisms [watanabe-2004-poleta-abstract]. First, monoubiquitinated PCNA provides a binding platform for Polη through the polymerase's ubiquitin-binding zinc finger (UBZ) domain. Second, RAD18 directly interacts with Polη through physical protein-protein contact, providing an additional layer of polymerase recruitment that is independent of PCNA modification. Cells lacking RAD18 fail to form Polη nuclear foci following UV irradiation, demonstrating the essential nature of this E3 ligase for TLS initiation.

The regulation of RAD18-dependent TLS is tightly integrated with cell cycle progression through phosphorylation-dependent mechanisms [day-2010-phosphorylation-abstract]. The kinase Cdc7/DDK (Dbf4/Drf1-dependent Cdc7 kinase) phosphorylates RAD18 at a serine-rich "S box" region within its C-terminal domain, with S434 identified as a primary target. This phosphorylation is essential for efficient RAD18-Polη association and the subsequent formation of Polη foci at sites of replication fork stalling. The Cdc7-RAD18 regulatory axis provides a mechanism for coordinating DNA replication progression with postreplication repair.

Beyond TLS, DNA damage tolerance also operates through template switching (TS), an error-free pathway that uses the undamaged sister chromatid as a template for bypass synthesis. While RAD18-dependent PCNA monoubiquitination initiates TLS, this modification can be extended to K63-linked polyubiquitin chains by the Ubc13-Mms2/RAD5 (HLTF and SHPRH in humans) complex, which routes DDT toward the template switching pathway [hedglin-2015-regulation-abstract]. Thus, RAD18 functions at a critical decision point in choosing between error-prone and error-free damage tolerance mechanisms.

It is important to note that while Polη is the most extensively studied TLS polymerase in the context of RAD18, monoubiquitinated PCNA also recruits other Y-family polymerases including Polκ, Polι, and Rev1. Each TLS polymerase exhibits preference for bypass of specific types of DNA damage; for example, Polη is specialized for bypass of UV-induced cyclobutane pyrimidine dimers (CPDs), while Polκ preferentially bypasses benzo[a]pyrene adducts. These polymerases contain ubiquitin-binding domains—UBZ domains in Polη and Polκ, and UBM domains in Polι and Rev1—that mediate their interaction with monoubiquitinated PCNA [yang-2018-tumorigenesis-abstract].

Intriguingly, Polη plays a unique non-catalytic role in promoting PCNA monoubiquitination itself [durando-2013-noncatalytic-abstract]. Polη physically bridges RAD18 and PCNA through its C-terminal domain, facilitating their interaction independently of polymerase catalytic activity. Catalytically inactive Polη mutants can still stimulate PCNA monoubiquitination to levels comparable to wild-type protein. This scaffolding function is specific to Polη among Y-family polymerases, as Polκ and Polι lack this capability. This non-catalytic role has important implications for understanding why xeroderma pigmentosum variant (XPV) patients, who carry mutations in Polη, experience increased mutagenesis—catalytically inactive Polη can still promote recruitment of alternative, more error-prone TLS polymerases.

## Domain Structure and Function

RAD18 is a 495 amino acid protein (in humans) containing several functionally distinct domains that coordinate its various activities in DNA damage response. The domain architecture includes an N-terminal RING finger domain, a ubiquitin-binding zinc finger (UBZ4) domain, a SAP (SAF-A/B, Acinus and PIAS) domain, and a C-terminal RAD6-binding domain (R6BD).

The RING finger domain (IPR001841) located at the N-terminus is the catalytic domain responsible for E3 ubiquitin ligase activity. This domain mediates the interaction with the E2 ubiquitin-conjugating enzyme RAD6 and facilitates ubiquitin transfer to substrates [notenboom-2007-domains-abstract]. Structural studies have determined the crystal structure of the homodimeric RAD18 RING domain (PDB: 2Y43), revealing a classical RING-RING dimer that dimerizes through helices adjacent to the RING domains. The RING domain can theoretically recruit two RAD6 molecules, but the full-length RAD18 homodimer binds only a single RAD6 molecule due to constraints imposed by other domains.

The UBZ4 domain (IPR006642) is a C2HC-type zinc finger that functions as a ubiquitin-binding module rather than a DNA-binding domain as initially proposed [notenboom-2007-domains-abstract]. NMR structural studies have determined the structure of the RAD18-UBZ domain both alone (PDB: 2MRF) and in complex with ubiquitin (PDB: 2MRE), revealing that it adopts a β1-β2-α fold and binds ubiquitin with micromolar affinity (Kd approximately 42 μM) [rizzo-2014-ubzstructure-abstract]. The RAD18-UBZ4 interacts with ubiquitin through both its α-helix and β1 strand, distinguishing it from the Polη-UBZ3 domain that uses only the α-helix for binding. This ubiquitin-binding activity is critical for RAD18 accumulation at DNA damage sites, particularly through recognition of RNF8-generated ubiquitin chains at double-strand breaks [huang-2009-hrrrepair-abstract].

The SAP domain (IPR003034) provides DNA-binding activity, with preferential affinity for single-stranded DNA over double-stranded DNA (affinity approximately 1 μM for ssDNA) [notenboom-2007-domains-abstract]. Despite its DNA-binding capability, the SAP domain is not absolutely required for RAD18 accumulation at damage sites but appears crucial for PCNA ubiquitination and Polη focus formation [nakajima-2006-replication-dependent-abstract]. The SAP domain may function by positioning the RAD18 complex appropriately at stalled replication forks where ssDNA is exposed.

The C-terminal RAD6-binding domain (R6BD) provides a second interaction interface with RAD6, distinct from the RING domain interaction [notenboom-2007-domains-abstract]. Importantly, this domain competes with ubiquitin for the backside binding site on RAD6, thereby suppressing polyubiquitin chain formation and ensuring monoubiquitination specificity [hibbert-2011-monoubiquitination-abstract].

## Cellular Localization

RAD18 is predominantly a nuclear protein that displays dynamic localization patterns depending on cell cycle phase and DNA damage status. Under normal conditions, RAD18 shows diffuse nuclear distribution, but upon DNA damage, it rapidly accumulates at sites of DNA lesions, forming distinct nuclear foci [nakajima-2006-replication-dependent-abstract].

Following UV irradiation, RAD18 forms numerous nuclear foci (typically >80 per cell) that colocalize extensively with PCNA, consistent with its role at stalled replication forks [nakajima-2006-replication-dependent-abstract]. This UV-induced pattern is replication-dependent and relies on the SAP domain of RAD18. The colocalization with PCNA reflects RAD18's function in monoubiquitinating this replication clamp to initiate translesion synthesis.

In contrast, ionizing radiation (IR) induces a distinct pattern of RAD18 localization. X-ray-induced RAD18 foci are fewer in number (approximately 50 per cell) but larger than UV-induced foci, and they colocalize with γ-H2AX rather than PCNA [nakajima-2006-replication-dependent-abstract]. This pattern reflects RAD18's replication-independent role in double-strand break repair. The IR-induced recruitment depends on the zinc finger domain and occurs through recognition of ubiquitin chains generated by the RNF8/UBC13 system at break sites [huang-2009-hrrrepair-abstract].

The mechanism of RAD18 recruitment differs between these two types of DNA damage. At stalled replication forks, RPA-coated single-stranded DNA serves as the recruitment signal, while at double-strand breaks, RAD18 is recruited through a signaling cascade involving H2AX phosphorylation, MDC1, RNF8, and ubiquitin chain formation. RAD18 colocalizes with chromatin-associated conjugated ubiquitin and ubiquitylated H2A throughout the cell cycle and following irradiation, indicating constitutive association with ubiquitin-modified chromatin.

Cell cycle-specific patterns have also been observed. RAD18 shows distinct localization during G1 phase when it participates in 53BP1-dependent DSB repair, and during S phase when it functions in replication-coupled DNA damage tolerance [watanabe-2009-53bp1-abstract]. Accumulation of RAD18 in nucleoli has been observed in late G2, dependent on its zinc finger domain.

## Regulatory Mechanisms

The activity and localization of RAD18 are tightly controlled through multiple regulatory mechanisms including post-translational modifications, protein-protein interactions, and transcriptional regulation.

Phosphorylation represents a key regulatory mechanism for RAD18 function. Cdc7/DDK kinase phosphorylates RAD18 at serine residues within the S box region, with S434 being a major target [day-2010-phosphorylation-abstract]. This phosphorylation enhances RAD18's interaction with Polη and is essential for efficient Polη recruitment to stalled replication forks. The phosphorylation occurs both during normal S phase and is enhanced following UV damage through a Chk1-dependent pathway, integrating RAD18 function with DNA damage checkpoint signaling. Additionally, SLF1 recognizes RAD18 phosphorylated at S442 and S444 through its tandem BRCT domain, facilitating RAD18 accumulation at DNA breaks in post-replicative chromatin.

More recently, O-GlcNAcylation has emerged as another important modification regulating RAD18 function. This modification promotes both translesion DNA synthesis and homologous recombination repair. Importantly, abrogation of RAD18 O-GlcNAcylation limits Cdc7-dependent RAD18 phosphorylation at S434, establishing crosstalk between these two modifications. Reduced O-GlcNAcylation significantly decreases damage-induced PCNA monoubiquitination, impairs Polη focus formation, and enhances UV sensitivity.

RAD18 is also subject to autoubiquitination at multiple lysine residues (K161, K261, K309, K318 in mouse RAD18), which regulates its stability and activity [notenboom-2007-domains-abstract]. Auto-ubiquitination mediated by RAD6 inhibits RAD18 recruitment to DNA breaks, providing a negative feedback mechanism.

Several accessory proteins regulate RAD18 activity at damaged sites. SIVA1 functions as a critical adaptor protein that constitutively interacts with PCNA and directs RAD18 to its substrate [han-2014-siva1-abstract]. SIVA1 binds RAD18 through domains separate from those used to bind PCNA, creating a bridging complex. Cells lacking SIVA1 phenocopy RAD18 deficiency with compromised PCNA monoubiquitination, defective Polη recruitment, increased UV sensitivity, and elevated mutation frequencies.

Other proteins that regulate RAD18 function include NBS1 (mutated in Nijmegen breakage syndrome), which recruits RAD18 to sites of DNA damage through direct binding; Claspin and CHK1, which participate in checkpoint-dependent RAD18 regulation; and chromatin remodeling complexes including Ino80, RSC, and NuRD that modulate chromatin accessibility at damage sites [hedglin-2015-regulation-abstract].

## Roles Beyond Translesion Synthesis

While RAD18 is best characterized for its function in translesion synthesis, accumulating evidence demonstrates its participation in additional DNA repair pathways, establishing it as a multifunctional coordinator of genome maintenance.

In double-strand break (DSB) repair, RAD18 plays distinct roles depending on cell cycle phase. During G1, RAD18 promotes DSB repair through a 53BP1-dependent mechanism [watanabe-2009-53bp1-abstract]. RAD18 directly associates with 53BP1 via its zinc finger domain and monoubiquitinates 53BP1 at K1268, enhancing 53BP1 chromatin retention at break sites. Rad18-null cells exhibit impaired DSB repair efficiency and reduced post-irradiation viability. This function appears to promote non-homologous end joining (NHEJ) repair.

During S and G2 phases, RAD18 participates in homologous recombination (HR) repair through a mechanism that involves direct interaction with RAD51C [huang-2009-hrrrepair-abstract]. Importantly, this HR function is independent of RAD18's E3 ligase activity and depends solely on its recruitment to damage sites. RAD18 localizes to DSBs through its zinc finger domain, which binds ubiquitin chains created by the RNF8/UBC13 complex, while the RING domain mediates RAD51C interaction. This reveals how RAD18 functions as a molecular bridge connecting DNA damage checkpoint signaling with repair processes.

RAD18 also plays a significant role in the Fanconi anemia (FA) pathway, which is essential for interstrand crosslink (ICL) repair [geng-2010-fanconianemia-abstract]. RAD18-mediated PCNA ubiquitination recruits FANCL, the E3 ligase of the FA core complex, to chromatin. Monoubiquitinated PCNA then stimulates FANCL-catalyzed monoubiquitination of the FANCI-FANCD2 complex, which is the critical activation step for ICL repair. This establishes PCNA as a regulatory hub coordinating TLS and FA pathway responses to DNA damage.

Beyond these pathway connections, RAD18 directly interacts with FANCD2 independently of the FA core complex and is required for efficient FANCD2 and FANCI chromatin loading [williams-2011-fancd2-abstract]. The E3 ligase activity of RAD18 is necessary for FANCD2 chromatin loading through a mechanism that appears independent of PCNA modification, suggesting additional direct roles for RAD18 in FA pathway regulation. RAD18-deficient cells show increased sensitivity to DNA crosslinking agents including mitomycin C and cisplatin.

Recent work has also implicated RAD18 in suppressing R-loop-mediated genome instability by promoting FANCD2 recruitment to difficult-to-replicate and R-loop-prone genomic sites. This function helps prevent transcription-replication conflicts, expanding RAD18's role as a guardian of genome stability.

## Evolutionary Conservation

The RAD6-RAD18 pathway for PCNA modification represents an evolutionarily ancient DNA damage tolerance mechanism that is highly conserved across eukaryotes. The human RAD18 gene was identified through its homology to the Saccharomyces cerevisiae RAD18 gene, and the yeast pathway has served as a foundational model for understanding mammalian DNA damage tolerance [tateishi-2000-dysfunction-abstract].

Human RAD18 encodes a 495-amino acid protein that shares 20% sequence identity and 42% similarity with yeast Rad18, with particularly strong conservation in the functional domains including the RING finger and zinc finger motifs. The mouse ortholog (mRAD18Sc) is 509 amino acids and shows strong conservation with both yeast and human homologs, demonstrating preserved domain architecture across mammals [vanderlaan-2000-mrad18-abstract]. The conservation of the RING-zinc-finger structure and the interaction with RAD6 homologs indicates that the core biochemical mechanism of PCNA monoubiquitination has been maintained throughout eukaryotic evolution.

Functionally orthologous genes have been identified in diverse fungi including Neurospora crassa (uvs-2) and Aspergillus nidulans (nuvA), all sharing the characteristic zinc finger motifs and involvement in DNA repair. Notably, the Schizosaccharomyces pombe rad18 gene is not a true ortholog of S. cerevisiae RAD18 but instead belongs to the SMC family of proteins (the true ortholog is RHC18), illustrating the importance of functional rather than nomenclature-based comparisons.

The conservation of the RAD6-RAD18 pathway extends to the downstream signaling as well. PCNA monoubiquitination at K164, the recruitment of Y-family TLS polymerases, and the extension to K63-linked polyubiquitin chains for template switching are all conserved from yeast to humans, underscoring the fundamental importance of this pathway in maintaining genome stability across evolution.

## Clinical Relevance and Role in Cancer

RAD18 has emerged as a significant factor in cancer biology through multiple mechanisms, reflecting its dual nature as both a genome maintenance factor and a potential contributor to mutagenesis [yang-2018-tumorigenesis-abstract]. The human RAD18 gene maps to chromosome 3p24-25, a region frequently deleted in lung, breast, ovarian, and testicular cancers, initially suggesting a tumor suppressor role [tateishi-2000-dysfunction-abstract].

However, the relationship between RAD18 and cancer is complex. RAD18 and the downstream Y-family TLS polymerases confer DNA damage tolerance at the expense of DNA replication fidelity, making them attractive candidate mediators of mutagenesis and carcinogenesis. Consistent with this, RAD18 is pathologically overexpressed in many cancer types including colorectal cancer, triple-negative breast cancer, and lung adenocarcinoma [yang-2018-tumorigenesis-abstract]. One mechanism of RAD18 overexpression involves increased protein stability through binding to MAGE-A4, a cancer/testis antigen that is normally absent in somatic cells but is aberrantly expressed in tumors.

Studies of RAD18 in colorectal cancer (CRC) have demonstrated that high RAD18 expression correlates with lymph node metastasis and poor prognosis. RAD18 overexpression increases the metastatic potential of CRC cells through activation of the epithelial-mesenchymal transition (EMT) pathway. In triple-negative breast cancer (TNBC), RAD18 is highly expressed and inversely related to patient prognosis, promoting cancer stem cell characteristics through the Hippo/YAP signaling pathway.

In vivo studies using mouse models have provided mechanistic insights into RAD18's role in shaping mutational landscapes [lou-2021-mutational-signatures-abstract]. Analysis of carcinogen-induced tumors revealed that Rad18-proficient tumors predominantly display COSMIC mutational signature 22, while Rad18-deficient tumors show features associated with homologous recombination defects (signature 3). Analysis of The Cancer Genome Atlas (TCGA) data demonstrates that RAD18 expression is strongly associated with high single nucleotide variant burdens across multiple human cancer types, suggesting RAD18 promotes mutagenesis in human cancers.

The role of RAD18 in drug resistance has also been documented. In osteosarcoma, RAD18 was identified as a determinant of doxorubicin sensitivity through genome-wide CRISPR screening. Rad18 knockout increased sensitivity to doxorubicin, while overexpression led to resistance, highlighting RAD18 as a potential therapeutic target for overcoming chemoresistance.

Paradoxically, RAD18 can also act as a tumor suppressor in specific contexts. In carcinogen-induced oral cancer models, Rad18 deficiency accelerated tumor onset, with Rad18-null tumors showing increased genomic instability and characteristic mutational patterns. This context-dependent activity reflects the balance between RAD18's role in maintaining genome stability through proper TLS and its contribution to mutagenesis through error-prone polymerase activity.

## Open Questions

Despite substantial progress in understanding RAD18 function, several important questions remain:

1. **Substrate specificity determinants**: While PCNA, 53BP1, and RFC2 have been identified as RAD18 substrates, the full spectrum of RAD18 targets remains incompletely characterized. Understanding how RAD18 achieves substrate selectivity in different cellular contexts requires further investigation.

2. **Coordination between pathways**: RAD18 participates in TLS, HR, NHEJ, and FA pathways. How the cell coordinates these different activities of RAD18 and directs it toward specific pathways depending on damage type and cell cycle phase remains unclear.

3. **Regulatory integration**: Multiple modifications regulate RAD18 (phosphorylation, O-GlcNAcylation, auto-ubiquitination), but how these modifications are integrated to produce context-appropriate responses is not fully understood.

4. **Tissue-specific functions**: The observation that RAD18 maps to a region frequently deleted in various cancers raises questions about potential tissue-specific roles that may be relevant to tumor suppression.

5. **Structure of full-length complex**: While structures of individual domains are available, a complete structural understanding of the RAD6-(RAD18)₂-PCNA complex and how it achieves substrate monoubiquitination is lacking.

6. **Template switching coordination**: How RAD18-dependent monoubiquitination is extended to polyubiquitin chains that promote template switching, and how the choice between TLS and TS is made, requires further mechanistic characterization.

7. **Alternative E3 ligases**: CRL4-Cdt2 can also monoubiquitinate PCNA independently of RAD18 in proliferating cells. The relative contributions and coordination of these alternative pathways in different contexts remains to be determined.

## References

* [tateishi-2000-dysfunction-abstract] Tateishi S, Sakuraba Y, Masuyama S, Inoue H, Yamaizumi M. Dysfunction of human Rad18 results in defective postreplication repair and hypersensitivity to multiple mutagens. Proc Natl Acad Sci USA. 2000;97(14):7927-7932. PMID: 10884424. DOI: 10.1073/pnas.97.14.7927

* [watanabe-2004-poleta-abstract] Watanabe K, Tateishi S, Kawasuji M, Tsurimoto T, Inoue H, Yamaizumi M. Rad18 guides poleta to replication stalling sites through physical interaction and PCNA monoubiquitination. EMBO J. 2004;23(19):3886-3896. PMID: 15359278. DOI: 10.1038/sj.emboj.7600383

* [nakajima-2006-replication-dependent-abstract] Nakajima S, Lan L, Kanno S, Usami N, Kobayashi K, Mori M, Shiomi T, Yasui A. Replication-dependent and -independent responses of RAD18 to DNA damage in human cells. J Biol Chem. 2006;281(45):34687-34695. PMID: 16980296. DOI: 10.1074/jbc.M605545200

* [notenboom-2007-domains-abstract] Notenboom V, Hibbert RG, van Rossum-Fikkert SE, Olsen JV, Mann M, Sixma TK. Functional characterization of Rad18 domains for Rad6, ubiquitin, DNA binding and PCNA modification. Nucleic Acids Res. 2007;35(17):5819-5830. PMID: 17720710. DOI: 10.1093/nar/gkm615

* [watanabe-2009-53bp1-abstract] Watanabe K, Iwabuchi K, Sun J, Tsuji Y, Tani T, Tokunaga K, Date T, Hashimoto M, Yamaizumi M, Tateishi S. RAD18 promotes DNA double-strand break repair during G1 phase through chromatin retention of 53BP1. Nucleic Acids Res. 2009;37(7):2176-2193. PMID: 19228710. DOI: 10.1093/nar/gkp082

* [huang-2009-hrrrepair-abstract] Huang J, Huen MSY, Kim H, Leung CCY, Glover JNM, Yu X, Chen J. RAD18 transmits DNA damage signaling to elicit homologous recombination repair. Nat Cell Biol. 2009;11(5):592-603. PMID: 19396164. DOI: 10.1038/ncb1865

* [geng-2010-fanconianemia-abstract] Geng L, Huntoon CJ, Karnitz LM. RAD18-mediated ubiquitination of PCNA activates the Fanconi anemia DNA repair network. J Cell Biol. 2010;191(2):249-257. PMID: 20937699. DOI: 10.1083/jcb.201005101

* [day-2010-phosphorylation-abstract] Day TA, Palle K, Barkley LR, Kakusho N, Zou Y, Tateishi S, Verreault A, Masai H, Vaziri C. Phosphorylated Rad18 directs DNA Polymerase η to sites of stalled replication. J Cell Biol. 2010;191(5):953-966. PMID: 21098111. DOI: 10.1083/jcb.201006043

* [hibbert-2011-monoubiquitination-abstract] Hibbert RG, Huang A, Boelens R, Sixma TK. E3 ligase Rad18 promotes monoubiquitination rather than ubiquitin chain formation by E2 enzyme Rad6. Proc Natl Acad Sci USA. 2011;108(14):5590-5595. PMID: 21422291. DOI: 10.1073/pnas.1017516108

* [williams-2011-fancd2-abstract] Williams SA, Longerich S, Sung P, Vaziri C, Kupfer GM. The E3 ubiquitin ligase RAD18 regulates ubiquitylation and chromatin loading of FANCD2 and FANCI. Blood. 2011;117(19):5078-5087. PMID: 21355096. DOI: 10.1182/blood-2010-10-311761

* [masuda-2012-asymmetric-abstract] Masuda Y, Suzuki M, Kawai H, Suzuki F, Kamiya K. Asymmetric nature of two subunits of RAD18, a RING-type ubiquitin ligase E3, in the human RAD6A-RAD18 ternary complex. Nucleic Acids Res. 2012;40(3):1065-1076. PMID: 21967848. DOI: 10.1093/nar/gkr805

* [rizzo-2014-ubzstructure-abstract] Rizzo AA, Salerno PE, Bezsonova I, Korzhnev DM. NMR structure of the human Rad18 zinc finger in complex with ubiquitin defines a class of UBZ domains in proteins linked to the DNA damage response. Biochemistry. 2014;53(37):5895-5906. PMID: 25162118. DOI: 10.1021/bi500823h

* [han-2014-siva1-abstract] Han J, Liu T, Huen MSY, Hu L, Chen Z, Huang J. SIVA1 directs the E3 ubiquitin ligase RAD18 for PCNA monoubiquitination. J Cell Biol. 2014;205(6):811-827. PMID: 24958773. DOI: 10.1083/jcb.201311007

* [hedglin-2015-regulation-abstract] Hedglin M, Benkovic SJ. Regulation of Rad6/Rad18 Activity During DNA Damage Tolerance. Annu Rev Biophys. 2015;44:207-228. PMID: 26098514. DOI: 10.1146/annurev-biophys-060414-033841

* [vanderlaan-2000-mrad18-abstract] van der Laan R, Roest HP, Hoogerbrugge JW, Smit EM, Slater R, Baarends WM, Hoeijmakers JH, Grootegoed JA. Characterization of mRAD18Sc, a mouse homolog of the yeast postreplication repair gene RAD18. Genomics. 2000;69(1):86-94. PMID: 11013078. DOI: 10.1006/geno.2000.6220

* [durando-2013-noncatalytic-abstract] Durando M, Tateishi S, Vaziri C. A non-catalytic role of DNA polymerase η in recruiting Rad18 and promoting PCNA monoubiquitination at stalled replication forks. Nucleic Acids Res. 2013;41(5):3079-3093. PMID: 23345618. DOI: 10.1093/nar/gkt016

* [yang-2018-tumorigenesis-abstract] Yang Y, Gao Y, Zlatanou A, Tateishi S, Yurchenko V, Rogozin IB, Vaziri C. Diverse roles of RAD18 and Y-family DNA polymerases in tumorigenesis. Cell Cycle. 2018;17(7):833-843. PMID: 29683380. DOI: 10.1080/15384101.2018.1456296

* [lou-2021-mutational-signatures-abstract] Lou J, Yang Y, Gu Q, Price BA, Qiu Y, Fedoriw Y, Desai S, Mose LE, Chen B, Tateishi S, Parker JS, Vaziri C, Wu D. Rad18 mediates specific mutational signatures and shapes the genomic landscape of carcinogen-induced tumors in vivo. NAR Cancer. 2021;3(1):zcaa037. PMID: 33447826. DOI: 10.1093/narcan/zcaa037


## Citations

1. day-2010-phosphorylation-abstract.md
2. durando-2013-noncatalytic-abstract.md
3. geng-2010-fanconianemia-abstract.md
4. han-2014-siva1-abstract.md
5. hedglin-2015-regulation-abstract.md
6. hibbert-2011-monoubiquitination-abstract.md
7. huang-2009-hrrrepair-abstract.md
8. lou-2021-mutational-signatures-abstract.md
9. masuda-2012-asymmetric-abstract.md
10. nakajima-2006-replication-dependent-abstract.md
11. notenboom-2007-domains-abstract.md
12. rizzo-2014-ubzstructure-abstract.md
13. tateishi-2000-dysfunction-abstract.md
14. vanderlaan-2000-mrad18-abstract.md
15. watanabe-2004-poleta-abstract.md
16. watanabe-2009-53bp1-abstract.md
17. williams-2011-fancd2-abstract.md
18. yang-2018-tumorigenesis-abstract.md