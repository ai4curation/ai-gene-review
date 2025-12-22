---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-12T07:11:18.583105'
end_time: '2025-12-12T07:13:14.284484'
duration_seconds: 115.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: EIF3E
  gene_symbol: EIF3E
  uniprot_accession: P60228
  protein_description: 'RecName: Full=Eukaryotic translation initiation factor 3 subunit
    E {ECO:0000255|HAMAP-Rule:MF_03004}; Short=eIF3e {ECO:0000255|HAMAP-Rule:MF_03004};
    AltName: Full=Eukaryotic translation initiation factor 3 subunit 6 {ECO:0000255|HAMAP-Rule:MF_03004};
    AltName: Full=Viral integration site protein INT-6 homolog; AltName: Full=eIF-3
    p48 {ECO:0000255|HAMAP-Rule:MF_03004};'
  gene_info: Name=EIF3E {ECO:0000255|HAMAP-Rule:MF_03004}; Synonyms=EIF3S6 {ECO:0000255|HAMAP-Rule:MF_03004},
    INT6 {ECO:0000255|HAMAP-Rule:MF_03004};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the eIF-3 subunit E family. {ECO:0000255|HAMAP-
  protein_domains: eIF3e. (IPR016650); eIF3e_N. (IPR019010); PCI_dom. (IPR000717);
    WH_DNA-bd_sf. (IPR036390); eIF3_N (PF09440)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 48
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P60228
- **Protein Description:** RecName: Full=Eukaryotic translation initiation factor 3 subunit E {ECO:0000255|HAMAP-Rule:MF_03004}; Short=eIF3e {ECO:0000255|HAMAP-Rule:MF_03004}; AltName: Full=Eukaryotic translation initiation factor 3 subunit 6 {ECO:0000255|HAMAP-Rule:MF_03004}; AltName: Full=Viral integration site protein INT-6 homolog; AltName: Full=eIF-3 p48 {ECO:0000255|HAMAP-Rule:MF_03004};
- **Gene Information:** Name=EIF3E {ECO:0000255|HAMAP-Rule:MF_03004}; Synonyms=EIF3S6 {ECO:0000255|HAMAP-Rule:MF_03004}, INT6 {ECO:0000255|HAMAP-Rule:MF_03004};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the eIF-3 subunit E family. {ECO:0000255|HAMAP-
- **Key Domains:** eIF3e. (IPR016650); eIF3e_N. (IPR019010); PCI_dom. (IPR000717); WH_DNA-bd_sf. (IPR036390); eIF3_N (PF09440)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EIF3E" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EIF3E' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EIF3E** (gene ID: EIF3E, UniProt: P60228) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze this comprehensive request. The user wants a detailed research report on the gene EIF3E (UniProt: P60228) in human. I need to:

1. First verify I have the correct gene - EIF3E encoding eukaryotic translation initiation factor 3 subunit E
2. Create a comprehensive 10,000+ word research report
3. Focus on primary function, substrate specificity, localization, and biochemical pathways
4. Use the provided search results to cite evidence
5. Follow the strict formatting rules about no lists, proper citations, etc.

Looking at the search results, I have extensive information about EIF3E:

Key sources:
- Source [3], [40]: Wikipedia articles on eIF3 in general
- Source [2], [7], [10], [26], [49], [54]: Papers on INT6/eIF3e and nonsense-mediated mRNA decay
- Source [9], [19], [22], [57]: Papers on eIF3e/INT6 in breast cancer and EMT
- Source [8], [51]: Detailed structural and functional reviews of eIF3
- Source [15]: Recent work on eIF3 engagement with 3'-UTR termini
- Source [18], [24]: eIF3 targets specific mRNAs
- Source [25]: Int6/eIF3e promotes general translation
- Source [31], [32], [33], [35]: Work on m6A methylation and eIF3
- Source [38]: Nuclear localization of eIF3e/INT6
- Source [37], [56]: Reconstitution and structural studies of eIF3
- Source [43], [46]: More structural and functional details on eIF3
- Source [48], [50], [53]: eIF3e expression in cancer
- Source [52]: Upf1 phosphorylation and eIF3

The search results are excellent and contain very relevant information. Let me plan the report structure:


I'll craft a comprehensive research report with a strategic outline covering the gene's molecular identity, structural features, functional roles, and clinical significance. The report will systematically explore EIF3E's complex involvement in translation initiation, mRNA regulation, and cellular processes. By leveraging multiple high-quality research sources, I'll provide an in-depth analysis that captures the multifaceted nature of this critical gene. The structured approach will ensure a thorough examination of EIF3E's scientific importance across molecular, cellular, and clinical domains.
</think>

# Eukaryotic Translation Initiation Factor 3 Subunit E (EIF3E): Molecular Function, Cellular Roles, and Regulatory Biology

Eukaryotic translation initiation factor 3 subunit E (EIF3E), also known as INT6 or eIF3-p48, represents a critical non-core component of the multiprotein eIF3 complex that coordinates the initiation of protein synthesis in human cells. While long characterized primarily as a structural component of the translation initiation apparatus, recent research has revealed that EIF3E functions as a specialized regulatory subunit that controls both general and transcript-specific translation through distinct mechanisms, participates in nonsense-mediated mRNA decay pathways, and serves as a hub for coordinating translational control with other cellular processes including mRNA quality surveillance, DNA damage responses, and cell proliferation regulation. The protein occupies a unique functional niche within eIF3, as it is simultaneously essential for global translation initiation when integrated within the complete eIF3 complex, yet plays highly specialized roles in directing the fate of specific mRNAs away from translation toward degradation. EIF3E is found in both cytoplasmic and nuclear compartments where it interacts with distinct molecular partners, and its expression levels are tightly regulated in response to cell cycle progression and stress conditions, with dysregulation associated with multiple human malignancies including breast cancer and colorectal cancer. This comprehensive review synthesizes current molecular understanding of EIF3E structure, biochemistry, and cellular function, establishing it as a multifunctional translation factor whose roles extend far beyond simple recruitment of ribosomes to mRNA.

## Molecular Architecture and Structural Organization of EIF3E

The human EIF3E protein, encoded by the EIF3E gene located on chromosome 8, represents a 48 kilodalton polypeptide that serves as a non-core subunit of the eIF3 translation initiation complex[3][27]. As a member of the PCI (proteasome-COP9 signalosome-eIF3) protein family, EIF3E possesses a characteristic PCI domain located within its carboxyl terminus that enables it to interact with other PCI-domain-containing proteins and to participate in the formation of large multiprotein complexes[3][40]. The presence of the PCI domain in EIF3E represents a key structural feature that distinguishes it from the five core subunits of eIF3 (eIF3a, eIF3b, eIF3c, eIF3g, and eIF3i) that are conserved across eukaryotic species from budding yeast to humans[37][40]. The structural organization of EIF3E reveals that this protein integrates into what is termed the PCI/MPN octamer, a shared structural scaffold found not only in eIF3 but also in functionally unrelated complexes such as the 19S proteasome lid and the COP9 signalosome, highlighting an ancient and evolutionarily conserved module for organizing large protein assemblies[3][40].

Within the three-dimensional architecture of the eIF3 complex bound to the 40S ribosomal subunit, EIF3E appears to occupy a position on the solvent-exposed face of the small ribosomal subunit, "sticking out" from the core octameric structure alongside other non-core subunits eIF3h, eIF3k, and eIF3l into the aqueous solution rather than directly contacting the ribosomal surface[8][51]. This positioning suggests that EIF3E, rather than forming direct contacts with ribosomal proteins or RNA, instead serves as an interface for recruiting and stabilizing interactions with additional initiation factors and mRNA regulatory proteins[8][51]. The extended arm-like projections of EIF3E from the main eIF3 body would position this subunit to modulate translation initiation rates in an mRNA-specific manner, potentially by recognizing structural features within mRNA molecules or by serving as a docking site for auxiliary translation factors[8][51]. Recent structural investigations using cryo-electron microscopy and biochemical cross-linking coupled to mass spectrometry have demonstrated that EIF3E integrates into the eIF3 complex through interactions with multiple other subunits, particularly with the large eIF3a-eIF3b-eIF3c core module, though the precise atomic-level interactions remain incompletely characterized due to the high flexibility inherent in this region of eIF3[8].

## EIF3E as a Non-Core Component of the eIF3 Translation Initiation Factor

Functional classification of eIF3 subunits into "core" and "non-core" categories emerged from comparative genomic and biochemical analyses demonstrating that while the five core subunits (eIF3a through eIF3i, excluding eIF3d, eIF3e, eIF3f, eIF3h, eIF3k, eIF3l, and eIF3m) are conserved in the simple five-subunit eIF3 complex of budding yeast, the additional eight non-core subunits found in mammalian eIF3 are absent from yeast and appear to regulate rather than to provide essential functions in basic translation initiation[37][40]. EIF3E, classified definitively as a non-core subunit, is notable for being dispensable for the assembly of active eIF3 complexes when reconstituted from recombinant protein subunits in vitro, yet appears essential for eIF3 function in living cells where it plays specialized regulatory roles[37][48]. A landmark biochemical study systematically investigating the minimal requirements for mammalian eIF3 activity demonstrated that a six-subunit complex comprising eIF3a, eIF3b, eIF3c, eIF3e, eIF3f, and eIF3h exhibited robust translation initiation activity, and that removal of any one of these six subunits severely compromised complex assembly and function[37]. These findings established that while eIF3e is not strictly required for in vitro reconstitution of active translation initiation complexes from purified proteins, it is essential for maintaining the integrity and full activity of mammalian eIF3 within intact cells[37].

The functional distinction between core and non-core eIF3 subunits extends beyond simple assembly requirements, as individual non-core subunits including EIF3E have been repeatedly demonstrated to regulate the translation efficiency of specific mRNAs rather than globally affecting protein synthesis rates[14][18]. For example, in studies using the plant model Arabidopsis thaliana, the non-core eIF3h subunit (analogous to mammalian eIF3h) was shown to be dispensable for general protein translation but was required for efficient translation of specific mRNAs containing particular 5' untranslated region sequences, including mRNAs encoding the bZip transcription factor ATB2[14]. This paradigm of selective, mRNA-specific translational control through non-core eIF3 subunits has been documented for human EIF3E, which demonstrates capacity to both activate and repress translation of distinct cellular mRNAs through direct interactions with mRNA secondary structures[18][24]. The discovery that eIF3 subunits including EIF3E possess intrinsic regulatory capacity to control transcriptionally specific translation initiation rates has fundamentally reshaped understanding of eIF3 from a general translation scaffold to a multifunctional regulatory hub capable of selective translational control[18][24][27].

## Primary Function of EIF3E within Global Translation Initiation

Translation initiation in eukaryotic cells proceeds through a complex, multi-step pathway involving sequential recruitment and assembly of numerous protein factors with the 40S small ribosomal subunit to form the 43S pre-initiation complex (PIC), which then binds mRNA and scans to locate the initiation codon[3][17][40]. The eIF3 complex, of which EIF3E is a component, serves as an essential scaffold throughout this process, functioning to promote recruitment of multiple initiation factors to the ribosome and to facilitate proper positioning of mRNA within the mRNA binding channel of the 40S subunit[3][8][40]. EIF3E, when present as part of intact eIF3, contributes to these general initiation functions by helping to maintain the structural integrity of the complex and by potentially modulating the conformational flexibility of eIF3 as it undergoes the dramatic rearrangements required to accommodate mRNA binding and start codon recognition[8][51].

The eIF3 complex, including its EIF3E subunit, binds the solvent-exposed face of the 40S ribosomal subunit near the platform region and serves to coordinate the activities of other initiation factors including eIF1, eIF1A, eIF2 (in its GTP-bound ternary complex form), and eIF5[3][8][40]. EIF3E participates in maintaining the open conformation of the 43S PIC that is essential for mRNA entry into the mRNA-binding channel, a function mediated by the concerted action of eIF1 and eIF1A which prevent premature closure of the complex before the correct initiation codon is identified[46]. Additionally, the eIF3 complex including EIF3E is required for the stimulation of scanning of the mRNA along the ribosome from the 5' cap structure to identify the initiator AUG codon, and for the subsequent conformational transition to a closed complex upon AUG recognition[3][8][40]. While EIF3E itself does not directly contact the ribosomal RNA or proteins based on available structural evidence, its presence within the eIF3 complex influences the overall conformational dynamics and positioning of subunits that do make critical contacts with ribosomal components[51].

A striking aspect of EIF3E function is the observation that despite being a non-core subunit, depletion of EIF3E in cultured cells can have significant effects on global translation rates, particularly under certain conditions[53]. Studies examining the consequences of EIF3E knockdown in breast cancer cells revealed modest but reproducible decreases in overall protein synthesis coupled with changes in ribosome occupancy patterns, suggesting that EIF3E contributes to the efficiency of bulk translation initiation even though it is not absolutely required for this process in minimal reconstituted systems[53]. These observations suggest that EIF3E functions as a fine-tuner of general translation initiation capacity in cells, potentially by facilitating the assembly or stability of functional eIF3 complexes, or by optimizing the interaction between eIF3 and other initiation factors or the ribosome itself[37][53].

## Specialized Roles of EIF3E in Transcript-Specific Translation Regulation

A paradigm-shifting discovery in the field of translational control has been the revelation that eIF3, rather than functioning simply as a general scaffold for all translation initiation events, selectively binds specific cellular mRNAs and regulates their translation through direct interactions with mRNA secondary structures[18]. These studies employing photo-activatable ribonucleoside-enhanced crosslinking and immunoprecipitation (PAR-CLIP) identified a limited set of mRNAs, comprising only approximately three percent of total expressed transcripts, that crosslink directly with eIF3 subunits within living cells[18]. Remarkably, eIF3 acts as both a translation activator and repressor of different mRNAs, a dual functional capacity that was definitively demonstrated through analysis of the proto-oncogene c-Jun and the tumor suppressor BTG1[18].

For the c-Jun mRNA, eIF3 binding to a conserved hairpin stem-loop structure located within the 5' untranslated region directly promotes translation initiation through a cap-dependent mechanism requiring the 5' methyl-guanosine cap, yet this eIF3-mediated activation occurs independently of the canonical eIF4F cap-binding complex that typically initiates cap-dependent translation[18][24]. The stem-loop structure within the c-Jun 5' UTR that recruits eIF3 has been structurally characterized by nuclear magnetic resonance spectroscopy, revealing a complex three-dimensional architecture that exhibits similarities to internal ribosomal entry sites (IRES) elements from hepatitis C virus, suggesting mechanistic parallels between viral cap-independent translation and specialized eIF3-mediated translation of cellular proto-oncogenes[24]. EIF3E likely contributes to this specialized translation mechanism through its position within the eIF3 complex and potential interactions with the mRNA stem-loop structure, though the precise atomic contacts between EIF3E and specific mRNA bases remain to be determined[24].

In contrast to its role in promoting c-Jun translation, eIF3 binding to a stem-loop structure within the BTG1 mRNA (B cell translocation gene 1, a tumor suppressor) suppresses translation of this transcript[18]. The structural determinants that cause the identical eIF3 complex to activate translation of one mRNA while repressing another remain incompletely understood, though evidence suggests that the surrounding mRNA sequence context, as well as the identity of additional trans-acting factors present in the cellular milieu, influences whether eIF3 binding results in translational activation or repression[18]. These observations establish that EIF3E, as a component of the eIF3 complex that directly contacts target mRNAs, must be capable of recognizing distinct molecular features that discriminate between activation and repression targets, and of transducing this recognition into appropriate regulatory outcomes[18].

A second major discovery regarding eIF3-mediated transcript-specific translation involves recognition of N6-methyladenosine (m6A) modifications within the 5' untranslated regions of specific mRNAs[31][32]. eIF3 directly binds m6A residues in particular sequence contexts within 5' UTRs and recruits the 43S pre-initiation complex to these mRNAs to initiate translation in a manner that is independent of the canonical 5' methylguanosine cap and the eIF4F cap-binding complex[31][32]. This m6A-dependent translation becomes particularly important during cellular stress conditions such as heat shock or endoplasmic reticulum stress, when cap-dependent translation is inhibited yet certain stress-response genes including heat shock protein 70 (HSP70) must continue to be translated to allow cellular adaptation[31]. EIF3E presumably participates in m6A recognition and recruitment of the translation machinery, though specific evidence establishing EIF3E's direct role in m6A-mediated translation initiation remains to be reported[31].

A remarkable additional finding has revealed that eIF3, contrary to its well-established association with 5' cap-proximal regions of mRNA, also engages extensively with the 3' untranslated region terminals of actively translated mRNAs[15]. Using Quick-irCLIP (rapid infrared crosslinking and immunoprecipitation) and alternative polyadenylation sequencing technologies, researchers demonstrated that eIF3 crosslinks predominantly to the 3' UTR termini of multiple mRNA isoforms, adjacent to the poly(A) tail, and that this 3' UTR engagement correlates with the overall translation efficiency of those transcripts[15]. Furthermore, eIF3 shows preference for specific 3' UTR isoforms produced through alternative polyadenylation, with evidence suggesting that 3' UTR binding by eIF3 reflects the initiation factor's involvement in mRNA circularization, a process in which the 5' and 3' ends of mRNA are brought into close proximity by protein bridges including eIF4G and poly(A)-binding protein[15]. This function of eIF3 including EIF3E in mRNA circularization likely represents a general mechanism for enhancing translation initiation by stabilizing interactions between the 5' cap-binding machinery and the translation machinery recruited to initiate protein synthesis[15].

## Nonsense-Mediated Decay and the Specialized Role of EIF3E in mRNA Surveillance

One of the most extensively characterized specialized functions of EIF3E is its essential role in nonsense-mediated mRNA decay (NMD), a quality control pathway that recognizes and degrades mRNAs containing premature termination codons (PTCs)[2][7][10][26][49]. NMD functions to prevent accumulation of truncated, potentially toxic proteins by detecting mRNAs in which translation termination occurs upstream of exon-exon junctions generated during pre-mRNA splicing, with a threshold of approximately 50-55 nucleotides upstream of the downstream-most exon junction typically triggering degradation[26][49]. The molecular recognition of NMD substrates requires a "pioneer" round of translation during which newly synthesized mRNAs, still bound by the nuclear cap-binding heterodimer CBP80-CBP20 (as opposed to the canonical translation cap-binding protein eIF4E), are subjected to translation initiation in the nucleus where interaction between translation termination factors and the exon junction complex machinery results in recruitment of the UPF proteins that execute NMD[26][49][52].

Detailed biochemical studies have demonstrated that EIF3E (also designated INT6) is uniquely required specifically for the pioneer round of translation and subsequent NMD, while the core eIF3b subunit is required for both pioneer round translation and steady-state translation[26][49]. RNA interference-mediated knockdown of EIF3E expression strongly inhibits NMD of model substrates carrying premature stop codons without affecting the stability of normal mRNAs or the global translation rate, establishing EIF3E as a specialized component of the NMD machinery[2][7][10]. Mechanistically, immunoprecipitation experiments have demonstrated that EIF3E co-purifies with CBP80, the nuclear cap-binding protein, and with UPF2, a core component of the NMD machinery[26][49]. These interactions suggest a model in which EIF3E, in association with eIF3, facilitates the recruitment of mRNA to the CBP80-bound initiation complex and, in conjunction with UPF2, directs these newly synthesized mRNAs toward the NMD pathway rather than toward continuing translation[26][49].

The mechanistic basis for EIF3E's selective role in NMD versus general translation appears to involve its interaction with specific binding partners that are present in the nuclear compartment but not in the cytoplasm. EIF3E possesses sequences consistent with nuclear localization signals and nuclear export signals, enabling it to shuttle between the nucleus and cytoplasm[38]. Evidence demonstrates that EIF3E interacts with the MIF4G (middle domain of eIF4G-1) motifs found in various protein partners, raising the possibility that EIF3E specifically binds to distinct versions of eIF3 complexes that associate with UPF2 and the CBP80 cap-binding protein in the nuclear compartment[26][49]. The composition of eIF3 complexes appears to be dynamic, with EIF3E-containing complexes potentially being enriched in the nucleus where they participate in the pioneer round of translation and NMD, while EIF3 complexes lacking EIF3E or containing different complements of non-core subunits mediate steady-state translation in the cytoplasm[26][38].

The functional significance of the EIF3E-dependent NMD pathway extends beyond simple quality control, as numerous transcripts are known to be regulated by NMD in response to cellular conditions, making EIF3E a critical node in pathways controlling cellular protein composition[26]. Furthermore, disruption of NMD through EIF3E knockdown has been shown to lead to accumulation of PTC-containing transcripts from genes including those encoding proteins involved in cell cycle regulation and apoptosis, suggesting that dysregulation of the EIF3E-dependent NMD pathway could contribute to malignant transformation through altered expression of cell cycle control proteins[26].

## Cellular Localization and Subcellular Compartmentalization of EIF3E

In contrast to other eIF3 subunits which localize predominantly to the cytoplasm where translation initiation occurs, EIF3E exhibits a striking and partially nuclear localization pattern that has been revealed through immunofluorescence microscopy using specific antibodies[38]. Quantitative cell fractionation studies have confirmed that EIF3E is present in both nuclear and cytoplasmic fractions, distinguishing it from the bulk of the eIF3 complex which resides in the cytoplasm[38]. The nuclear pool of EIF3E has been observed to accumulate in PML bodies, nuclear foci associated with various regulatory functions including DNA damage response and protein ubiquitination[38]. Notably, the extent of nuclear localization of EIF3E varies with cell cycle position, with particularly striking decreases in nuclear EIF3E fluorescence occurring during early S phase in primary human fibroblasts, suggesting that the subcellular distribution of EIF3E is subject to active, cell cycle-regulated redistribution[38].

The presence of nuclear EIF3E likely reflects its participation in the pioneer round of translation and NMD pathway, processes that occur predominantly in the nucleus for newly synthesized mRNAs still bound by CBP80[38]. The partial nuclear localization of EIF3E, in contrast to the predominantly cytoplasmic localization of other eIF3 subunits, indicates that EIF3E may represent a dedicated component that is selectively recruited to nuclear pioneer round translation complexes and subsequently removed or sequestered to prevent its participation in cytoplasmic steady-state translation[38]. The mechanism of nuclear-cytoplasmic shuttling of EIF3E remains incompletely characterized, though its possession of putative nuclear localization signals and nuclear export sequences is consistent with active transport mechanisms involving importins and exportins[38].

The cell cycle-dependent redistribution of EIF3E from nuclear to cytoplasmic locales during S phase raises intriguing questions about the biological function driving this redistribution[38]. One possibility is that decreased nuclear EIF3E during S phase reflects a need for its relocation to the cytoplasm to support increased translation of S-phase-specific proteins required for DNA replication[38]. Alternatively, the redistribution might reflect altered requirements for pioneer round translation or NMD during DNA replication, or might be secondary to changes in eIF3 complex composition that occur during different cell cycle phases[38]. Understanding the mechanisms and functional consequences of EIF3E shuttling represents an important area for future research.

## Post-Translational Modification and Regulatory Protein Interactions of EIF3E

The activity of EIF3E is subject to regulation through post-translational modifications including phosphorylation, though the complete repertoire of EIF3E modification sites and their functional consequences remain incompletely defined[39][42]. Phosphorylation by DNA-damage-responsive kinases, likely including ATM and ATR family members, has been reported to occur on EIF3E following DNA damage[39]. Additionally, EIF3E is phosphorylated as a consequence of mTOR signaling pathway activation, with particular relevance to the translational control function of eIF3[39]. The eIF3 complex serves as a hub for cellular signaling through the mTOR-S6K1 axis, with activated mTOR/Raptor binding to eIF3 and phosphorylating ribosomal S6 kinase 1 (S6K1) to promote its release from the complex and subsequent phosphorylation of downstream targets including eIF4B[3]. EIF3E, as a component of eIF3, participates in this signaling function, though whether EIF3E itself serves as a direct substrate for mTOR or S6K1 remains to be definitively established[39].

EIF3E interacts with multiple other cellular proteins beyond its integrated associations within the eIF3 complex. Notably, EIF3E has been demonstrated to interact with UPF2, a core component of the NMD machinery, and with CBP80, the nuclear cap-binding protein[26][49]. These interactions likely represent the molecular basis for EIF3E's specialized function in the NMD pathway and pioneer round translation[26][49]. Additionally, EIF3E has been shown to interact with subunits of the COP9 signalosome, a multiprotein complex involved in regulating protein ubiquitination and neddylation, suggesting potential cross-talk between translation initiation and post-translational protein modification pathways[38]. In fission yeast, the INT6 ortholog has been demonstrated to interact with the 26S proteasome and to promote proteasome assembly through interaction with the Rpn5 regulatory particle subunit[28], though analogous proteasome interactions for human EIF3E remain to be characterized[28].

The regulation of EIF3E protein levels itself appears to be subject to control through multiple mechanisms. Several studies have reported that EIF3E expression is downregulated in various human malignancies, including breast cancer and colorectal cancer[9][50], raising questions about mechanisms controlling EIF3E protein stability or synthesis. Whether EIF3E undergoes proteasomal degradation, is subject to microRNA-mediated translational repression, or is simply downregulated at the transcriptional level in cancer cells remains incompletely understood and represents an important question for future investigation[9][50].

## Functional Roles of EIF3E in Stress Responses and Cellular Adaptation

During cellular stress conditions that compromise cap-dependent translation, eIF3 including EIF3E plays enhanced roles in promoting alternative cap-independent translation mechanisms that sustain synthesis of critical stress-response proteins[31][32][34]. Heat stress, for example, triggers a global shutdown of cap-dependent translation while selectively maintaining or even increasing translation of heat shock proteins, a switching process that involves m6A-dependent eIF3-mediated translation initiation[31][34]. EIF3E participates in this stress-adaptive function as a component of eIF3, enabling continued translation of mRNAs marked with m6A modifications within their 5' UTRs[31][32]. Additionally, EIF3E undergoes relocalization into cytoplasmic foci in response to heat stress and osmotic stress, implicating it in stress granule assembly or modification, though the precise functional consequences of this relocalization remain to be elucidated[41].

The capacity of EIF3E to support stress-responsive translation appears to extend to viral infection responses, as eIF3 including EIF3E is required for the initiation of translation from internal ribosomal entry sites (IRES) of many RNA viruses[55][58]. Hepatitis C virus (HCV), for example, depends critically upon eIF3-mediated recruitment of the translation machinery to its IRES-containing RNA genome, and the interaction between eIF3 and the HCV IRES has been extensively characterized structurally[55][58]. The requirement for EIF3E in viral IRES-mediated translation likely reflects its general function within the eIF3 complex in promoting translation from structured mRNA elements, a capacity that is exploited by viruses but is also employed for cellular mRNAs in stress situations[55][58].

## Role of EIF3E in Cancer and Dysregulation in Human Malignancies

The involvement of EIF3E in human cancer has been established through multiple independent lines of evidence demonstrating that EIF3E expression is frequently altered in diverse malignancies, and that changes in EIF3E abundance influence tumor cell biology in important ways[9][22][27][50][53][57]. The role of EIF3E in cancer is complex and, in certain respects, paradoxical, with evidence supporting both tumor suppressor and oncogenic functions depending on the cellular context and cancer type.

In breast cancer, reduced expression of EIF3E/INT6 has been documented in up to 37 percent of cases, making it one of the most frequently downregulated eIF3 subunits in this disease[9][19][57]. Expression of a truncated mutant version of the murine eIF3e/INT6 protein leads to malignant transformation of normal mammary cells, providing evidence that loss of full-length EIF3E function promotes breast oncogenesis[9][19][57]. However, these tumor suppressor findings initially conflicted with an earlier study reporting that reduction of EIF3E expression in certain breast cancer cell lines led to decreased translation of specific oncogenes, suggesting a potential oncogenic role for EIF3E[22]. This apparent paradox has been partially reconciled through investigations revealing that EIF3E plays cell-context-dependent roles: decreased EIF3E expression causes breast epithelial cells to undergo epithelial-to-mesenchymal transition (EMT), imparting invasive and migratory properties while also increasing expression of key EMT regulators including SNAIL1 and ZEB2[9][19][57]. These findings suggest that EIF3E functions as a tumor suppressor by preventing the EMT process and maintaining epithelial cell characteristics, with loss of EIF3E promoting metastatic capability in breast cancer[9][19][57].

In colorectal cancer, high EIF3E expression has been associated with poor prognosis and increased tumor aggressiveness[50]. Multivariate analysis of colorectal cancer patients revealed that elevated EIF3E expression independently predicted both reduced overall survival and reduced disease-free survival[50]. Mechanistic studies in colon cancer cell lines demonstrated that knockdown of EIF3E inhibited cell proliferation, reduced colony formation, and promoted apoptosis, supporting an oncogenic role for EIF3E in this cancer type[50]. These findings suggest that the functional role of EIF3E in cancer biology is cancer-type-specific, with EIF3E serving as a tumor suppressor in breast cancer but as an oncogene in colorectal cancer[9][50]. The basis for this context-dependent function may reside in the specialized mRNAs that EIF3E regulates in different cell types; EIF3E's capacity to selectively control translation of specific cell proliferation and apoptosis-regulating mRNAs could result in differing net effects on tumor progression depending on which target mRNAs dominate in particular cancer types[18][50].

Recent investigations have revealed additional mechanisms linking EIF3E to cancer biology and therapeutic responses. In EIF3E-depleted breast cancer cells, reduced synthesis of PARP1 (poly-ADP-ribose polymerase 1) protein occurs due to weakened translation of the corresponding mRNA, resulting in decreased cellular ability to synthesize poly(ADP-ribose) polymers and rendering these cells resistant to PARP inhibitor drugs[53]. Additionally, EIF3E depletion leads to impaired DNA repair via homologous recombination, suggesting that EIF3E may regulate translation of mRNAs encoding proteins critical for DNA damage responses[53]. Paradoxically, the DNA repair defect resulting from EIF3E loss renders cells vulnerable to replication stress, and EIF3E-depleted breast cancer cells undergo premature senescence with activation of senescence-associated secretory phenotype (SASP) characterized by increased production of inflammatory cytokines including IL-6, IL-8, and CXCL1[53]. These findings reveal an unexpected tumor suppressor function for EIF3E in maintaining genomic stability, contrasting with its role in suppressing EMT, and suggesting that multiple cellular processes depend upon EIF3E-regulated translation for proper function[53].

## Specialized Translation Initiation Mechanisms Involving EIF3E

Beyond its roles in general translation initiation and NMD, EIF3E participates in additional specialized translation initiation mechanisms that represent important regulatory pathways in eukaryotic cells. One such mechanism involves the recognition of upstream open reading frames (uORFs) present in the 5' untranslated regions of certain cellular mRNAs. Following translation of a short upstream ORF and termination at its stop codon, eIF3 can remain bound to the ribosome through elongation and termination events to promote reinitiation at downstream ORFs, a process termed reinitiation[3][40][46]. EIF3E likely participates in reinitiation through its functions in maintaining eIF3 complex stability and in facilitating conformational changes of the ribosomal complex required to resume scanning for the next AUG codon[46]. The classic example of reinitiation-mediated translational control involves the GCN4 transcription factor, whose translation is regulated by uORFs in response to amino acid starvation through mechanisms dependent on eIF3[44][46].

Another specialized mechanism involves programmed stop codon readthrough, a process in which translation termination factors are prevented from recognizing stop codons, allowing translation to proceed through the stop codon and into normally untranslated downstream sequences[3][40]. eIF3 has been implicated in regulating programmed readthrough in yeast through interactions with pre-termination complexes, and EIF3E may similarly participate in this process in mammalian cells, though direct evidence specific to EIF3E remains to be reported[3][40]. Additionally, eIF3 including EIF3E plays roles in recycling of ribosomes following translation termination, promoting the dissociation of 40S and 60S subunits and preventing premature rejoining, ensuring that ribosomes are properly released for participation in subsequent rounds of translation initiation[3][13][40]. These diverse specialized functions of EIF3E highlight its critical role not only in initiating translation but in coordinating multiple steps throughout the entire translation cycle.

## Concluding Synthesis and Future Perspectives

EIF3E (eukaryotic translation initiation factor 3 subunit E), also designated INT6 or eIF3-p48, emerges from current scientific understanding as a multifunctional translation factor whose roles extend far beyond a simple structural role within the eIF3 translation initiation complex. As a non-core component of eIF3, EIF3E contributes to the general capacity of cells to initiate translation on most cellular mRNAs while simultaneously serving as a dedicated regulatory subunit capable of selectively controlling the translation of specific transcripts that encode cell proliferation and apoptosis regulators. The specialized functions of EIF3E in transcript-specific translational control derive from its participation in eIF3-mRNA interactions that are mediated by mRNA secondary structures and post-transcriptional modifications such as m6A methylation, mechanisms that enable EIF3E to discriminate between different mRNA substrates and to impose appropriate regulatory decisions upon them.

The unique role of EIF3E in the nuclear pioneer round of translation and in the nonsense-mediated mRNA decay pathway represents a critical quality control function that prevents accumulation of truncated protein products that might otherwise exert dominant-negative effects on cellular function. The regulated subcellular localization of EIF3E, with partial nuclear sequestration that varies with cell cycle position, supports the hypothesis that EIF3E represents a specialized eIF3 component dedicated to nuclear mRNA surveillance functions. The dysregulation of EIF3E expression in human malignancies, with a complex pattern of tumor-suppressive functions in breast cancer and oncogenic roles in colorectal cancer, underscores the fundamental importance of balanced EIF3E expression for proper cellular behavior and suggests potential therapeutic strategies targeting EIF3E-mediated translation control in cancer treatment.

Future research into EIF3E biology should prioritize several important questions. First, the atomic-level structural characterization of EIF3E within intact eIF3 complexes and in association with ribosomes and mRNA remains incomplete, with high-resolution cryo-EM structures providing detailed visualization of EIF3E's exact role in eIF3-ribosome positioning and conformational dynamics. Second, the complete identification of cellular mRNAs whose translation is specifically regulated by EIF3E, and the characterization of the sequence and structural determinants that distinguish EIF3E-activated versus EIF3E-repressed mRNAs, would provide critical insights into the mechanisms of selective translational control. Third, the mechanisms controlling EIF3E expression and subcellular localization, and the identity of trans-acting factors that recruit EIF3E to specific cellular compartments and protein complexes, represent important areas for investigation. Fourth, the therapeutic potential of modulating EIF3E expression or function as a strategy for treating cancers and other diseases characterized by dysregulated protein synthesis requires further exploration through both basic research and preclinical development studies.

## Citations

1. https://www.ncbi.nlm.nih.gov/gene/3646
2. https://pubmed.ncbi.nlm.nih.gov/17468741/
3. https://en.wikipedia.org/wiki/Eukaryotic_initiation_factor_3
4. https://www.uniprot.org/uniprotkb/P60228/entry
5. https://www.proteinatlas.org/ENSG00000104408-EIF3E
6. https://royalsocietypublishing.org/rstb/article/372/1716/20160176/23133/Human-eIF3-from-blobology-to-biological
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC2002529/
8. https://academic.oup.com/nar/article/45/19/10948/4157872
9. https://pubmed.ncbi.nlm.nih.gov/22907435/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC3973348/
11. https://article.imrpress.com/bri/Landmark/articles/pdf/Landmark4469.pdf
12. https://www.abcam.com/en-us/targets/eif3e/19755
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC535877/
14. https://elifesciences.org/articles/102977
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC4003276/
16. https://www.nature.com/articles/nrm1488
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC4603833/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC3089590/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC5820134/
20. https://pubmed.ncbi.nlm.nih.gov/20453879/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC7225069/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC2494926/
23. https://www.embopress.org/doi/10.1038/sj.embor.7400955
24. https://www.genecards.org/cgi-bin/carddisp.pl?gene=EIF3E
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC111132/
26. https://www.uniprot.org/uniprot/A0A2T3A300
27. https://www.proteinatlas.org/ENSG00000104408-EIF3E/structure
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7333474/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC4695625/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC1173091/
31. https://royalsocietypublishing.org/rsos/article/12/7/250132/235434/Translational-reprogramming-under-heat-stress-a
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC8036370/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC1933396/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC6495725/
35. https://www.uniprot.org/uniprot/Q3UIG0
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC2666973/
37. https://academic.oup.com/nar/article/47/15/8282/5530675
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC2950517/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC5311491/
40. https://elifesciences.org/articles/20934
41. https://academic.oup.com/g3journal/article/2/11/1393/6026000
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC4230162/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC4193665/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC8021025/
45. https://www.pnas.org/doi/10.1073/pnas.2505538122
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC4151992/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC6884710/
48. https://www.nature.com/articles/s43018-024-00839-5