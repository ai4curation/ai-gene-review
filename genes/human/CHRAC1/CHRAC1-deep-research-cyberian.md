---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-21T21:34:18.269897'
end_time: '2026-01-21T21:48:41.409586'
duration_seconds: 863.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CHRAC1
  gene_symbol: CHRAC1
  uniprot_accession: Q9NRG0
  protein_description: 'RecName: Full=Chromatin accessibility complex protein 1; Short=CHRAC-1;
    AltName: Full=Chromatin accessibility complex 15 kDa protein; Short=CHRAC-15;
    Short=HuCHRAC15; AltName: Full=DNA polymerase epsilon subunit p15;'
  gene_info: Name=CHRAC1; Synonyms=CHRAC15;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: CBFA_NFYB_domain. (IPR003958); Histone-fold. (IPR009072); Transcr_DNA_Rep_Reg.
    (IPR050568); CBFD_NFYB_HMF (PF00808)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9NRG0
- **Protein Description:** RecName: Full=Chromatin accessibility complex protein 1; Short=CHRAC-1; AltName: Full=Chromatin accessibility complex 15 kDa protein; Short=CHRAC-15; Short=HuCHRAC15; AltName: Full=DNA polymerase epsilon subunit p15;
- **Gene Information:** Name=CHRAC1; Synonyms=CHRAC15;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CBFA_NFYB_domain. (IPR003958); Histone-fold. (IPR009072); Transcr_DNA_Rep_Reg. (IPR050568); CBFD_NFYB_HMF (PF00808)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CHRAC1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CHRAC1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CHRAC1** (gene ID: CHRAC1, UniProt: Q9NRG0) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CHRAC1 (Chromatin Accessibility Complex Protein 1): A Comprehensive Review

## Introduction

CHRAC1 (Chromatin Accessibility Complex Subunit 1), also known as CHRAC-15, HuCHRAC15, or YCL1, is a small histone-fold protein that functions as an essential component of the chromatin accessibility complex (CHRAC) in humans. Encoded by the CHRAC1 gene (gene ID: 54108) located on chromosome 8q24.3, this 131 amino acid protein (UniProt: Q9NRG0) plays a critical role in ATP-dependent chromatin remodeling by facilitating nucleosome sliding and assembly. CHRAC1 forms a stable heterodimer with POLE3 (CHRAC-17/p17) that binds DNA in a sequence-independent manner and integrates into larger chromatin remodeling complexes. Through its interactions with the ISWI-family ATPase SMARCA5/SNF2H and the regulatory subunit BAZ1A/ACF1, CHRAC1 participates in fundamental nuclear processes including DNA replication, transcriptional regulation, and chromatin organization [poot-2000-huchrac-abstract][kukimoto-2004-chrac15-17-sliding-abstract].

The identification of CHRAC1 emerged from studies of chromatin remodeling complexes in Drosophila melanogaster, where the chromatin accessibility complex was first discovered as an ATP-dependent machine capable of increasing DNA accessibility within chromatin [vargaweisz-1997-chrac-nature-abstract]. Subsequent work by Poot and colleagues in 2000 characterized the human homolog, HuCHRAC, and identified two novel histone-fold proteins, p15 (CHRAC1) and p17 (POLE3), as conserved subunits [poot-2000-huchrac-abstract]. This evolutionary conservation from insects to humans underscores the fundamental importance of CHRAC1 in chromatin biology.

## Protein Structure and Domain Architecture

CHRAC1 is a relatively small protein consisting of 131 amino acids with an apparent molecular mass of approximately 15 kDa as determined by SDS-PAGE analysis [poot-2000-huchrac-abstract]. The protein contains a central histone-fold domain (HFD) of approximately 65 amino acids, flanked by short N-terminal and C-terminal regions that are enriched in acidic and lysine residues [bolognese-2000-ybl1-ycl1-abstract]. The histone-fold domain of CHRAC1 is classified as an H2A-type fold, showing significant similarity to the HFD found in NFYC (NF-YC, CBFC), a subunit of the CCAAT-binding transcription factor NF-Y [corona-2000-chrac14-16-abstract][gnesutta-2013-hfd-proteins-abstract].

The crystal structure of the Drosophila CHRAC14-CHRAC16 heterodimer (homologs of human POLE3 and CHRAC1, respectively) was determined at 2.4-Angstrom resolution by Hartlepp and colleagues in 2005 (PDB: 2BYM) [hartlepp-2005-structure-mechanism-abstract]. This structure revealed that the two proteins dimerize via a variant histone fold in a characteristic "handshake" configuration, directly analogous to the H2A-H2B histone pair within the nucleosome. The heterodimer contains unstructured N- and C-terminal tail domains that protrude from the handshake structure, reminiscent of histone tails. Importantly, deletion of the negatively charged C-terminus of CHRAC-16 (the fly homolog of CHRAC1) enhances DNA binding 25-fold but paradoxically inhibits nucleosome sliding, suggesting that these terminal regions play crucial regulatory roles in balancing DNA binding affinity with functional activity [hartlepp-2005-structure-mechanism-abstract].

Despite sharing only 15-18% sequence identity with core histones H2A and H2B, CHRAC1 and related histone-fold domain proteins share highly conserved tertiary structures [gnesutta-2013-hfd-proteins-abstract]. The CHRAC1 HFD shows 25-35% sequence identity with other H2A-type HFD proteins including NC2alpha, NF-YC, and CHRAC-16, which is considerably higher than the identity with canonical histones. This structural conservation enables the CHRAC1-POLE3 heterodimer to function in a manner analogous to DNA chaperones, providing transient acceptor sites for DNA during the nucleosome remodeling process.

## Molecular Function: Facilitation of Nucleosome Sliding and Assembly

The primary molecular function of CHRAC1 is to facilitate ATP-dependent nucleosome sliding and chromatin assembly as a component of the CHRAC complex. This function was definitively established through biochemical studies by Kukimoto and colleagues in 2004, who demonstrated that the CHRAC-15/17 (CHRAC1/POLE3) heterodimer enhances nucleosome sliding mediated by the ACF complex (ACF1-ISWI) [kukimoto-2004-chrac15-17-sliding-abstract]. The direct interaction between CHRAC-15/17 and ACF1 is essential for this enhancement, and notably, CHRAC-15 (CHRAC1) specifically is required for the interaction with ACF and the resulting enhancement of nucleosome sliding activity.

The mechanism by which CHRAC1 facilitates nucleosome sliding involves low-affinity, sequence-independent DNA binding. The CHRAC1-POLE3 heterodimer binds naked DNA with submicromolar affinity but does not bind to nucleosomes directly [poot-2000-huchrac-abstract]. This DNA binding activity is thought to provide a transient acceptor site for DNA that is being displaced from the histone surface during the sliding reaction [hartlepp-2005-structure-mechanism-abstract]. Analysis of the DNA binding properties suggests that CHRAC1-POLE3 functions analogously to the DNA chaperone HMGB1 in facilitating nucleosome remodeling, where dynamic, low-affinity DNA interactions improve the efficiency of nucleosome mobilization [hartlepp-2005-structure-mechanism-abstract].

Mechanistically, CHRAC induces movements of intact histone octamers to neighboring DNA segments without disrupting the octamer or displacing histones to competing DNA in trans [langst-1999-nucleosome-movement-abstract]. This nucleosome sliding activity is ATP-dependent and requires the catalytic activity of the ISWI ATPase (SMARCA5/SNF2H in humans). Importantly, the directionality of nucleosome sliding differs between CHRAC and ISWI alone, indicating that the accessory subunits including CHRAC1 modulate the activity of the ATPase motor [langst-1999-nucleosome-movement-abstract].

Beyond nucleosome sliding, CHRAC1 also participates in chromatin assembly reactions. The CHRAC-15/17 complex facilitates ACF-mediated chromatin assembly, converting irregular chromatin into regular arrays of nucleosomes with even spacing [vargaweisz-1997-chrac-nature-abstract][kukimoto-2004-chrac15-17-sliding-abstract]. Interestingly, this chromatin assembly activity occurs through a mechanism distinct from nucleosome sliding enhancement, suggesting that CHRAC1 has multiple functional modes in chromatin dynamics.

## The CHRAC Complex: Composition and Organization

The complete human CHRAC (HuCHRAC) complex consists of four core subunits: SMARCA5/SNF2H (the ISWI ATPase), BAZ1A/ACF1 (the regulatory subunit), CHRAC1/CHRAC-15 (p15), and POLE3/CHRAC-17 (p17) [poot-2000-huchrac-abstract]. SMARCA5 provides the ATP-dependent motor activity that drives nucleosome sliding, while ACF1 contains multiple functional domains including WAC, DDT, WAKZ, PHD finger, and bromodomain motifs that regulate nucleosome interactions and targeting [fyodorov-2004-acf1-chromatin-abstract]. The CHRAC1-POLE3 heterodimer binds DNA and enhances the efficiency of the remodeling reaction.

The evolutionary conservation of this complex is remarkable. In Drosophila, CHRAC contains ISWI, Acf1, CHRAC-14 (homolog of POLE3), and CHRAC-16 (homolog of CHRAC1) [corona-2000-chrac14-16-abstract]. Notably, Drosophila CHRAC also contains topoisomerase II as a fifth subunit, which was not found in human CHRAC [vargaweisz-1997-chrac-nature-abstract][poot-2000-huchrac-abstract]. This compositional difference may reflect species-specific functional requirements.

CHRAC is closely related to but distinct from the ACF complex, which contains only SMARCA5 and ACF1 without the histone-fold subunits [fyodorov-2004-acf1-chromatin-abstract]. The presence of CHRAC1 and POLE3 in CHRAC distinguishes it from ACF and confers enhanced nucleosome sliding activity. Both complexes participate in chromatin assembly and remodeling, but CHRAC appears to be particularly important for efficient nucleosome mobilization under conditions of limiting enzyme concentrations [hartlepp-2005-structure-mechanism-abstract].

## Dual Identity: CHRAC Subunit and DNA Polymerase Epsilon Component

A remarkable feature of the CHRAC histone-fold subunits is their dual localization in distinct macromolecular complexes. POLE3 (CHRAC-17/p17) was independently identified as a subunit of human DNA polymerase epsilon [li-2000-pole3-pole4-abstract]. Within the polymerase epsilon complex, POLE3 forms a heterodimer with POLE4 (p12), and this heterodimer is required for interaction with the catalytic subunit POLE1 (p261) and the accessory subunit POLE2 (p59) [li-2000-pole3-pole4-abstract]. This dual residence of POLE3 in both chromatin remodeling (with CHRAC1) and DNA replication (with POLE4) machineries suggests functional coordination between these processes.

CHRAC1 also interacts with POLE3 in the context of the DNA polymerase epsilon complex pathway, though its role there is less well characterized than in CHRAC [bolognese-2000-ybl1-ycl1-abstract]. The ability of these histone-fold proteins to participate in multiple complexes reflects the modular nature of chromatin-associated machinery and suggests that CHRAC1 may coordinate chromatin remodeling with DNA replication at a molecular level.

## Subcellular Localization

CHRAC1 localizes to the nucleus, consistent with its function in chromatin remodeling. According to the Human Protein Atlas, the protein is specifically localized to the nucleoplasm. Based on ortholog data and functional studies, CHRAC1 is also found at pericentromeric heterochromatin regions [fyodorov-2004-acf1-chromatin-abstract]. This heterochromatic localization is functionally significant, as the ACF1-containing complexes (including CHRAC) have been implicated in heterochromatin formation and maintenance.

The targeting of CHRAC to specific chromatin regions appears to be mediated primarily through the ACF1 subunit, which contains multiple chromatin-reading domains including a PHD finger and bromodomain. ACF1 specifically targets heterochromatin through its N-terminal region, and the CHRAC1-containing complex accumulates at sites of pericentromeric heterochromatin replication during S phase.

## Biological Processes and Pathways

### DNA Replication

CHRAC participates in DNA replication by facilitating access of the replication machinery to chromatin-covered origins and by promoting replication through condensed chromatin regions. The pioneering study by Alexiadis and colleagues demonstrated that CHRAC could facilitate initiation of SV40 DNA replication from a nucleosomal origin by enabling T-antigen access to chromatin-covered sequences [alexiadis-1998-sv40-replication-abstract]. This finding established a direct role for chromatin remodeling in DNA replication initiation.

In Drosophila, loss of ACF1 (which disrupts both ACF and CHRAC complexes) results in accelerated progression through S phase, consistent with reduced chromatin-mediated repression of DNA replication [fyodorov-2004-acf1-chromatin-abstract]. The ACF1-SMARCA5 complex is specifically enriched in replicating pericentromeric heterochromatin, and depletion of ACF1 by RNA interference specifically impairs heterochromatin replication. These findings indicate that CHRAC1, as part of the CHRAC complex, facilitates the replication of heterochromatic regions that would otherwise present a barrier to the replication fork.

### Chromatin Organization and Gene Silencing

CHRAC1 participates in establishing and maintaining organized chromatin structure. The ACF/CHRAC complexes promote the formation of repressive chromatin by generating regularly spaced nucleosome arrays from irregular chromatin [vargaweisz-1997-chrac-nature-abstract][fyodorov-2004-acf1-chromatin-abstract]. Loss of ACF1 in Drosophila results in decreased periodicity of nucleosome arrays and shorter nucleosomal repeat length in bulk chromatin, demonstrating the importance of these complexes in chromatin organization.

Genetically, ACF1 (and by extension CHRAC) contributes to transcriptional silencing in pericentromeric heterochromatin and in regions regulated by Polycomb group proteins [fyodorov-2004-acf1-chromatin-abstract]. The CHRAC/ACF complexes have been described as contributing to the "repressive ground state of chromatin," establishing an inactive baseline from which gene expression must be activated.

### DNA Repair

Components of the CHRAC complex, particularly SMARCA5/SNF2H and ACF1, have been implicated in DNA repair pathways. Recent studies have elucidated the mechanism by which the ACF complex is recruited to sites of DNA damage. ADP-ribosylation signaling, which marks sites of DNA lesions, orchestrates the recruitment of various repair factors and chromatin remodeling complexes during the early stages of the DNA damage response. The ACF complex accumulates at DNA lesions in an ADP-ribosylation-dependent manner, though interestingly, each subunit (SMARCA5 and ACF1) accumulates independently from its partner. The recruitment of these proteins is not due to direct binding to ADP-ribose moieties but rather results from facilitated DNA binding at relaxed, ADP-ribosylated chromatin. ACF1 and SMARCA5 facilitate both nucleotide excision repair and transcription-coupled nucleotide excision repair (TC-NER) following UV irradiation. While the specific contribution of CHRAC1 to DNA repair has not been extensively characterized, its role in enhancing the nucleosome sliding activity of the CHRAC complex suggests participation in repair-associated chromatin remodeling that facilitates access of repair machinery to damaged DNA.

## Expression Pattern

Northern blot analysis revealed that CHRAC1 is expressed ubiquitously across human tissues, producing a 2.4-kb transcript [poot-2000-huchrac-abstract]. The expression pattern of CHRAC1 parallels that of its heterodimer partner POLE3 (CHRAC-17), suggesting coordinated regulation of these functionally linked genes. According to the Human Protein Atlas, CHRAC1 shows low tissue specificity, with expression detected in virtually all major tissue types.

The highest expression levels are observed in bone marrow (26.4 nTPM), skeletal muscle (26.1 nTPM), tonsil (24.5 nTPM), and blood vessel (22.3 nTPM). In the brain, white matter shows the highest regional expression (32.2 nTPM). At the single-cell level, early primary spermatocytes show exceptionally high CHRAC1 expression (91.8 nCPM), potentially reflecting the intense chromatin remodeling activity required during meiosis. This is consistent with the recently described essential role of SMARCA5 in male meiosis and fertility.

## Evolutionary Conservation

CHRAC1 is highly conserved across metazoan species, reflecting the fundamental importance of the CHRAC complex in chromatin biology. The Drosophila homolog CHRAC-16 shows significant sequence conservation with human CHRAC1, particularly within the histone-fold domain. Both proteins share the H2A-type HFD structure and the ability to heterodimerize with their POLE3/CHRAC-14 partners [corona-2000-chrac14-16-abstract].

The conservation extends beyond the histone-fold motif to include the N- and C-terminal regions, suggesting functional importance for these apparently unstructured domains [bolognese-2000-ybl1-ycl1-abstract]. The yeast ISW2 chromatin remodeling complex also contains a pair of histone-fold proteins, indicating that this organization of chromatin remodeling complexes predates the divergence of fungi and animals.

## Disease Associations and Therapeutic Implications

Recent studies have revealed significant associations between CHRAC1 and cancer progression, particularly through its interaction with the Hippo pathway effector YAP. Wang and colleagues in 2022 demonstrated that CHRAC1 is highly expressed in lung cancer tissues, and this elevated expression correlates with poor prognosis in lung cancer patients [wang-2022-chrac1-lung-cancer-abstract]. Their functional studies showed that CHRAC1 overexpression promotes lung cancer cell proliferation and migration both in vitro and in vivo using a genetically engineered KrasG12D.LSL lung adenocarcinoma mouse model. Conversely, CHRAC1 silencing inhibited cell proliferation, migration, and tumor growth in xenograft models. Mechanistically, CHRAC1 binds to YAP and enhances the transcription of downstream oncogenic targets in the Hippo pathway, thereby promoting tumor growth [wang-2022-chrac1-lung-cancer-abstract].

These findings were extended by Li and colleagues in 2024, who demonstrated that CHRAC1 promotes tumor growth in breast and cervical cancer through the same YAP-mediated mechanism [li-2024-chrac1-cancer-abstract]. CHRAC1 depletion suppressed cancer cell proliferation and tumor growth, while elevated CHRAC1 expression correlated with worse patient outcomes, advanced disease stages, and metastasis. The interaction between CHRAC1 and YAP appears to be indirect and may be mediated by other components of the CHRAC complex, such as ACF1 or SMARCA5, consistent with the relatively small size of CHRAC1 (15 kDa).

Analysis of The Cancer Genome Atlas (TCGA) data has revealed that CHRAC1, along with its complex partners BAZ1A and POLE3, is simultaneously upregulated in multiple tumor types including esophageal carcinoma, liver hepatocellular carcinoma, stomach adenocarcinoma, and breast invasive carcinoma [zhou-2021-iswi-cancer-review-summary]. The CHRAC1 gene is located on chromosome 8q24.3, a region frequently amplified in cancer, and has been identified as a driver gene promoting proliferation and clonal survival of breast cancer cells.

More broadly, the ISWI chromatin remodeling complexes including CHRAC have been implicated in various cancers. SMARCA5, the catalytic subunit of CHRAC, is upregulated in acute myeloid leukemia and has been linked to breast, lung, and gastric cancers [zhou-2021-iswi-cancer-review-summary]. The emerging understanding of CHRAC1's role in cancer, particularly its function as a YAP coactivator, suggests it may represent a potential therapeutic target, though further research is needed to fully characterize its contribution to oncogenesis and determine whether its chromatin remodeling function can be specifically targeted.

## Open Questions

Despite significant advances in understanding CHRAC1 function, several important questions remain:

1. **Specificity of CHRAC1 versus POLE4 interactions with POLE3:** Both CHRAC1 and POLE4 form heterodimers with POLE3, but the factors determining which complex assembles in different cellular contexts are not fully understood. How is the partitioning of POLE3 between chromatin remodeling and DNA replication functions regulated?

2. **Direct contribution to DNA repair:** While the SMARCA5-ACF1 complex is clearly implicated in DNA repair, the specific contribution of CHRAC1 to repair pathways has not been definitively established. Does CHRAC1 have distinct functions in repair versus replication-associated chromatin remodeling?

3. **Tissue-specific functions:** Despite ubiquitous expression, CHRAC1 may have tissue-specific roles, particularly in contexts requiring intensive chromatin remodeling such as spermatogenesis. What are the consequences of CHRAC1 deficiency in specific cell types?

4. **Mechanistic details of YAP interaction:** The recently discovered interaction between CHRAC1 and YAP in cancer contexts raises questions about whether this represents a normal physiological function or a pathological gain-of-function. Does CHRAC1 regulate Hippo pathway targets in normal cells?

5. **Post-translational modifications:** The role of post-translational modifications of CHRAC1 in regulating its function, localization, and protein interactions remains largely unexplored.

6. **Relationship to other histone-fold proteins:** CHRAC1 shares structural features with NF-YC and NC2alpha, which function in transcription. Whether CHRAC1 has any direct roles in transcriptional regulation beyond chromatin remodeling merits investigation.

## References

- [vargaweisz-1997-chrac-nature-abstract] Varga-Weisz PD, Wilm M, Bonte E, Dumas K, Mann M, Becker PB. Chromatin-remodelling factor CHRAC contains the ATPases ISWI and topoisomerase II. Nature. 1997 Aug 7;388(6642):598-602. DOI: 10.1038/41587. PMID: 9252192.

- [poot-2000-huchrac-abstract] Poot RA, Dellaire G, Hülsmann BB, Grimaldi MA, Corona DF, Becker PB, Bickmore WA, Varga-Weisz PD. HuCHRAC, a human ISWI chromatin remodelling complex contains hACF1 and two novel histone-fold proteins. EMBO J. 2000 Jul 3;19(13):3377-87. DOI: 10.1093/emboj/19.13.3377. PMID: 10880450.

- [corona-2000-chrac14-16-abstract] Corona DF, Eberharter A, Budde A, Deuring R, Ferrari S, Varga-Weisz P, Wilm M, Tamkun J, Becker PB. Two histone fold proteins, CHRAC-14 and CHRAC-16, are developmentally regulated subunits of chromatin accessibility complex (CHRAC). EMBO J. 2000 Jun 15;19(12):3049-59. DOI: 10.1093/emboj/19.12.3049. PMID: 10856248.

- [bolognese-2000-ybl1-ycl1-abstract] Bolognese F, Imbriano C, Caretti G, Mantovani R. Cloning and characterization of the histone-fold proteins YBL1 and YCL1. Nucleic Acids Res. 2000 Oct 1;28(19):3830-8. DOI: 10.1093/nar/28.19.3830. PMID: 11000277.

- [li-2000-pole3-pole4-abstract] Li Y, Pursell ZF, Linn S. Identification and cloning of two histone fold motif-containing subunits of HeLa DNA polymerase epsilon. J Biol Chem. 2000 Jul 28;275(30):23247-52. DOI: 10.1074/jbc.M002548200. PMID: 10801849.

- [langst-1999-nucleosome-movement-abstract] Längst G, Bonte EJ, Corona DF, Becker PB. Nucleosome movement by CHRAC and ISWI without disruption or trans-displacement of the histone octamer. Cell. 1999 Jun 25;97(7):843-52. DOI: 10.1016/s0092-8674(00)80797-7. PMID: 10399913.

- [alexiadis-1998-sv40-replication-abstract] Alexiadis V, Varga-Weisz PD, Bonte E, Becker PB, Gruss C. In vitro chromatin remodelling by chromatin accessibility complex (CHRAC) at the SV40 origin of DNA replication. EMBO J. 1998 Jun 15;17(12):3428-38. DOI: 10.1093/emboj/17.12.3428. PMID: 9628878.

- [kukimoto-2004-chrac15-17-sliding-abstract] Kukimoto I, Elderkin S, Grimaldi M, Oelgeschläger T, Varga-Weisz PD. The histone-fold protein complex CHRAC-15/17 enhances nucleosome sliding and assembly mediated by ACF. Mol Cell. 2004 Jan 30;13(2):265-77. DOI: 10.1016/s1097-2765(03)00523-9. PMID: 14759371.

- [fyodorov-2004-acf1-chromatin-abstract] Fyodorov DV, Blower MD, Karpen GH, Kadonaga JT. Acf1 confers unique activities to ACF/CHRAC and promotes the formation rather than disruption of chromatin in vivo. Genes Dev. 2004 Jan 15;18(2):170-83. DOI: 10.1101/gad.1139604. PMID: 14752009.

- [hartlepp-2005-structure-mechanism-abstract] Hartlepp KF, Fernández-Tornero C, Eberharter A, Grüne T, Müller CW, Becker PB. The histone fold subunits of Drosophila CHRAC facilitate nucleosome sliding through dynamic DNA interactions. Mol Cell Biol. 2005 Nov;25(22):9886-96. DOI: 10.1128/MCB.25.22.9886-9896.2005. PMID: 16260604.

- [gnesutta-2013-hfd-proteins-abstract] Gnesutta N, Nardini M, Mantovani R. The H2A/H2B-like histone-fold domain proteins at the crossroad between chromatin and different DNA metabolisms. Transcription. 2013 May 16;4(3):114-119. DOI: 10.4161/trns.25002. PMID: 23695160.

- [wang-2022-chrac1-lung-cancer-abstract] Wang M, Li S, Guo W, Wang L, Huang J, Zhuo J, Lai B, Liao C, Ge T, Nie Y, Jin S, Wang M, Zhang Y, Liu Y, Li X, Zhang H. CHRAC1 promotes human lung cancer growth through regulating YAP transcriptional activity. Carcinogenesis. 2022 Apr 25;43(3):264-276. DOI: 10.1093/carcin/bgab103. PMID: 34718437.

- [li-2024-chrac1-cancer-abstract] Li S, Wang L, Shi J, Chen Y, Xiao A, Huo B, Tian W, Zhang S, Yang G, Gong W, Zhang H. Chromatin accessibility complex subunit 1 enhances tumor growth by regulating the oncogenic transcription of YAP in breast and cervical cancer. PeerJ. 2024 Jan 10;12:e16752. DOI: 10.7717/peerj.16752. PMID: 38223760.

- [zhou-2021-iswi-cancer-review-summary] Zhou M, Yuan J, Deng Y, Fan X, Shen J. The emerging role of ISWI chromatin remodeling complexes in cancer. J Exp Clin Cancer Res. 2021 Nov 12;40(1):346. DOI: 10.1186/s13046-021-02151-x. PMID: 34772431.


## Citations

1. alexiadis-1998-sv40-replication-abstract.md
2. bolognese-2000-ybl1-ycl1-abstract.md
3. corona-2000-chrac14-16-abstract.md
4. fyodorov-2004-acf1-chromatin-abstract.md
5. gnesutta-2013-hfd-proteins-abstract.md
6. hartlepp-2005-structure-mechanism-abstract.md
7. kukimoto-2004-chrac15-17-sliding-abstract.md
8. langst-1999-nucleosome-movement-abstract.md
9. li-2000-pole3-pole4-abstract.md
10. li-2024-chrac1-cancer-abstract.md
11. poot-2000-huchrac-abstract.md
12. vargaweisz-1997-chrac-nature-abstract.md
13. wang-2022-chrac1-lung-cancer-abstract.md
14. zhou-2021-iswi-cancer-review-summary.md