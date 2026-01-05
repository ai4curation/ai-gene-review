---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-31T19:53:59.814443'
end_time: '2025-12-31T19:55:59.588259'
duration_seconds: 119.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: POB3
  gene_symbol: POB3
  uniprot_accession: Q04636
  protein_description: 'RecName: Full=FACT complex subunit POB3; AltName: Full=Facilitates
    chromatin transcription complex subunit POB3;'
  gene_info: Name=POB3; OrderedLocusNames=YML069W;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the SSRP1 family. .
  protein_domains: PH-like_dom_sf. (IPR011993); RTT106/SPT16-like_middle_dom. (IPR013719);
    RTT106/SSRP1_HistChap/FACT. (IPR050454); SSRP1-like_PH1. (IPR048993); SSRP1/POB3.
    (IPR000969)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 53
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q04636
- **Protein Description:** RecName: Full=FACT complex subunit POB3; AltName: Full=Facilitates chromatin transcription complex subunit POB3;
- **Gene Information:** Name=POB3; OrderedLocusNames=YML069W;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the SSRP1 family. .
- **Key Domains:** PH-like_dom_sf. (IPR011993); RTT106/SPT16-like_middle_dom. (IPR013719); RTT106/SSRP1_HistChap/FACT. (IPR050454); SSRP1-like_PH1. (IPR048993); SSRP1/POB3. (IPR000969)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "POB3" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'POB3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **POB3** (gene ID: POB3, UniProt: Q04636) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
The user is asking me to research the gene POB3 (UniProt Q04636) from Saccharomyces cerevisiae and provide a comprehensive research report. Let me review the search results provided to understand what information I have.

Looking at the search results, I can see extensive information about POB3 and the FACT complex (Facilitates Chromatin Transactions). The search results include:

1. Gene database entries (SGD, Ensembl)
2. Protein structure and function studies
3. Research on FACT complex interactions with histones
4. Roles in transcription, replication, and DNA repair
5. Studies on nucleosome reorganization
6. Information about histone chaperone activity
7. Evolutionary conservation

Key findings from the search results:
- POB3 is the small subunit of the heterodimeric FACT complex (along with Spt16/SPT16)
- It's a histone chaperone involved in nucleosome disassembly and reassembly
- It plays roles in transcription elongation, DNA replication, and DNA repair
- It contains pleckstrin homology (PH) domains
- It lacks the HMG box domain that mammalian SSRP1 has
- In yeast, the HMG box function is provided by Nhp6 proteins
- It binds to H2A-H2B dimers primarily through its C-terminal acidic domain
- It also binds H3-H4
- It's essential for cell viability
- It localizes to the nucleus and associates with chromatin

Now I need to structure this into a comprehensive 10,000+ word research report following the format guidelines. Let me plan the structure:

1. Title and introductory summary
2. Main body sections covering:
   - Overview and evolutionary conservation of POB3
   - Structural organization and domains
   - Role in nucleosome reorganization and histone chaperone activity
   - Function in transcription and elongation
   - Function in DNA replication
   - Function in DNA repair
   - Cellular localization and chromatin association
   - Interactions with other proteins
   - Post-translational modifications and regulation
3. Conclusion with synthesis of findings

I'll expand the research report to explore additional dimensions of POB3's biological significance. The comprehensive analysis will delve into its molecular mechanisms, structural characteristics, and critical cellular functions. By examining its role in various genomic processes, I'll provide a holistic understanding of this essential yeast protein's contributions to cellular maintenance and genetic stability.
</think>

# POB3: A Critical Histone Chaperone Subunit of the FACT Complex in Saccharomyces cerevisiae

The **POB3** gene in *Saccharomyces cerevisiae* encodes a small subunit of the **FACT complex** (Facilitates Chromatin Transcription), which represents one of the most essential and conserved histone chaperone complexes across eukaryotes[2][8][12]. POB3 forms a stable heterodimer with Spt16 (also known as CDC68), and together these proteins function as the catalytic core of FACT, playing indispensable roles in processes requiring nucleosome reorganization, including transcription elongation, DNA replication, and DNA damage repair[2][35][52]. Unlike its mammalian homolog SSRP1, which possesses an intrinsic high-mobility-group box (HMG) DNA-binding domain, yeast POB3 achieves similar functional outcomes through a bipartite architecture involving cooperation with the small HMG-box proteins Nhp6a and Nhp6b[1][26][29]. The protein has been shown to be absolutely essential for cell viability in budding yeast, and its loss results in rapid cell death due to defects in multiple essential cellular processes[2][35]. Through its histone chaperone activity, POB3 facilitates the dynamic reorganization of nucleosomes that would otherwise present insurmountable barriers to RNA polymerase and DNA polymerase progression along chromatin templates. This comprehensive review examines the structural features, biochemical mechanisms, and biological functions of POB3 based on recent molecular and genetic studies.

## Structural Organization and Protein Domain Architecture

The POB3 protein possesses a modular architecture comprising several functionally distinct domains that work cooperatively to execute the multifaceted roles of the FACT complex[25][28][38]. The protein begins with an N-terminal domain that contains a pleckstrin homology (PH) fold and functions in heterodimerization with Spt16[27][28]. This N-terminal domain forms the essential interface between POB3 and the larger Spt16 subunit, stabilizing the heterodimeric complex that represents the functional form of FACT in cells[37][50]. Following the N-terminal region, POB3 contains a middle domain (Pob3-M) that comprises two tandem pleckstrin homology folds arranged in an unusual double-PH domain architecture[25][28][38]. This middle domain adopts a remarkable structural arrangement in which two PH domains are rigidly fixed relative to one another, creating a distinctive structural platform for protein-protein interactions[28][38]. The Pob3 middle domain exhibits significant structural similarity to the middle domains found in other histone chaperones such as Rtt106, suggesting a conserved mechanism for histone recognition and binding across this family of proteins[28][38][41].

Biochemical and structural studies have revealed that the Pob3 middle domain engages in direct interactions with core histones, particularly the H3-H4 tetramer, though with more modest affinity compared to the full heterodimeric FACT complex[28][38]. The middle domain contributes to the overall histone-binding capacity of FACT by providing one of multiple interaction surfaces for histone engagement[7][13]. Genetic evidence indicates that the Pob3-middle domain contains surfaces important for both histone binding and potentially other protein-protein interactions critical to FACT function[28][38]. Beyond the middle domain, POB3 contains a highly acidic C-terminal region (approximately 80-100 residues) that constitutes the primary binding site for H2A-H2B dimers[19][22]. This acidic C-terminus utilizes a combination of charge-based interactions and specific aromatic residues—particularly a conserved phenylalanine residue (F512 in yeast POB3)—to achieve high-affinity binding to H2A-H2B dimers with a dissociation constant of approximately 0.3 μM[19]. The remarkable discovery that a single aromatic residue contributes more to H2A-H2B binding than the collective effect of numerous acidic residues suggests a sophisticated molecular recognition mechanism involving both electrostatic interactions and hydrophobic contacts[19].

Notably, yeast POB3 lacks the HMG-box domain that characterizes the mammalian SSRP1 protein and defines the SSRP1 family of proteins[1][8][26]. Instead, the DNA-binding function provided by the HMG box in higher eukaryotes is delegated in yeast to the separate small HMG-box proteins Nhp6a and Nhp6b, which associate with the Spt16-POB3 complex in a regulated manner[26][29][40]. This functional organization, in which histone-binding and DNA-binding activities are distributed across multiple subunits rather than integrated into a single polypeptide, may reflect an evolutionary divergence in how the FACT complex assembled its functional capabilities. Recent evidence demonstrates that the domain architecture of POB3 is highly conserved among fungal species, with structural homology extending to plant and other eukaryotic SSRP1 orthologs[8]. This conservation indicates that the multi-domain organization of POB3 represents a fundamental feature of the FACT complex architecture that has been maintained through hundreds of millions of years of evolution.

## Role as a Histone Chaperone: Nucleosome Disassembly and Reassembly

The primary biological function of POB3 centers on its activity as a histone chaperone, a role that constitutes the biochemical foundation for virtually all of FACT's roles in chromatin-dependent processes[7][8][19][42][56]. Histone chaperones are specialized proteins that facilitate the transfer of histones between different cellular locations and contexts, and critically, they mediate the reversible disassembly and reassembly of nucleosomes without hydrolyzing ATP[59]. The FACT complex, and specifically the interaction between POB3 and its partner Spt16, accomplishes nucleosome reorganization through a multi-step mechanism that begins with binding to nucleosomes that have been partially disrupted or destabilized by the mechanical force exerted by transcribing or replicating polymerases[10][42][56].

The initial step in FACT-mediated nucleosome reorganization involves the recognition and binding of the Spt16-POB3 heterodimer to nucleosomes, likely nucleosomes that have begun to unwind or "fray" due to polymerase passage[39][42][56]. The high-resolution cryo-electron microscopy structures of transcription complexes have provided remarkable visual evidence for how FACT engages with nucleosomes during active transcription[39]. These structures reveal that the middle domain of Spt16 (Spt16-M) interacts extensively with the H3-H4 tetramer within the nucleosome, making contacts with both the histone fold domains and the N-terminal tails of histones H3 and H4[39][7][13]. Simultaneously, the C-terminal acidic regions of both Spt16 and POB3 engage with H2A-H2B dimers, establishing a network of interactions that destabilize the normal nucleosomal structure[7][13][19]. The combined effect of these interactions is to create a partially reorganized nucleosome in which the normal interactions between histones and DNA are weakened, and in particular, the stability of H2A-H2B dimer association with the (H3-H4)₂ tetramer is compromised[7][39].

This reorganization activity proceeds through a remarkable mechanism in which FACT does not catalyze ATP-dependent nucleosome remodeling in the classical sense, but rather facilitates energetically favorable conformational transitions that are driven by the mechanical force exerted by transcribing or replicating polymerases[10][59]. When RNA polymerase II encounters a nucleosome during transcription, the forward motion of the polymerase itself provides the mechanical energy that drives partial nucleosome unwrapping[39]. The FACT complex, through its multiple histone-binding domains, stabilizes this unwrapped, reorganized state of the nucleosome, preventing the nucleosome from snapping back into its canonical form despite the intrinsic energetic preference for this conformation[39][42][56]. This stabilization of partial nucleosome structures appears to involve the formation of defined intermediates comprising FACT, histone hexamers (H3-H4-H2A-H2B), and DNA, with the missing H2A-H2B dimer being held in complex with FACT itself[42][56].

The reassembly function of FACT proves equally important to its disassembly activity[7][42][56]. After RNA polymerase has traversed a nucleosome during transcription elongation, the nucleosome must be rapidly reassembled behind the polymerase to restore chromatin structure and maintain epigenetic information[39][42][56]. Recent cryo-EM structures have revealed how FACT catalyzes this reassembly process through a series of sequential steps[39]. The FACT complex, still holding H2A-H2B dimers, is positioned upstream of the transcribing polymerase. As the polymerase continues its forward motion and exits the nucleosomal DNA, free DNA emerges from the polymerase, and this free DNA can compete with FACT for binding to the histone octamer[42][56][59]. The fundamental insight emerging from these studies is that free DNA possesses higher affinity for histones than FACT does, and therefore as continuous DNA becomes available, it preferentially displaces FACT from H2A-H2B, promoting histone deposition and completing nucleosome reassembly[42][59]. This elegant mechanism ensures that nucleosomes are efficiently reconstructed behind transcribing polymerases, maintaining chromatin integrity and preventing permanent loss of nucleosomes from transcribed regions.

Optical tweezers and atomic force microscopy studies of FACT-nucleosome interactions have provided quantitative evidence for how FACT mechanically stabilizes partial nucleosome structures[42]. These experiments demonstrate that FACT binding to nucleosomes disrupts the outer wrapping of DNA, reducing the mechanical force required to further unwind nucleosomal DNA[42]. Remarkably, intact FACT exhibits dramatic chaperone activity, enabling nucleosomes to be disrupted and reformed through multiple cycles of force disruption and release, with some nucleosomes undergoing over thirty such cycles before losing the ability to fully reassemble[42]. This extraordinary capacity for repeated disassembly and reassembly cycles likely reflects FACT's role in protecting cells during ongoing transcription and replication, when nucleosomes may be subjected to repeated mechanical stress and require continuous dynamic adjustment.

## Function in Transcription: Elongation and Initiation

The transcription-related functions of POB3 have been extensively characterized through both genetic and biochemical approaches, establishing FACT as an essential cofactor for productive mRNA synthesis in eukaryotic cells[8][9][20][23][54]. POB3, as part of the FACT heterodimer, travels with elongating RNA polymerase II across transcribed genes, and this physical association with the transcription machinery appears essential for efficient transcript elongation through nucleosomes[23]. Chromatin immunoprecipitation studies have provided direct evidence that Spt16 and POB3 associate with actively transcribed genes at levels that correlate strongly with RNA polymerase II occupancy, and moreover, the enrichment of FACT at different positions along genes corresponds closely to the position of the actively transcribing polymerase, indicating that FACT tracks with the transcription machinery as it moves along genes[23].

The elongation-promoting function of FACT operates at a mechanistic level by removing the substantial barrier that nucleosomes present to polymerase progression[7][8][20][39][56]. The nucleosome represents one of the most significant impediments to transcript elongation, as the tight wrapping of DNA around the histone octamer must be mechanically disrupted to allow polymerase access to the template strand. Without FACT, nucleosomes on transcribed regions cause substantial polymerase pausing and stalling, dramatically reducing the overall rate of transcript synthesis[39][54]. The presence of FACT, traveling with polymerase II, ensures that nucleosomes are dynamically reorganized as the polymerase approaches them, minimizing polymerase pausing and allowing for productive, continuous elongation[39]. Biochemical experiments employing purified transcription systems have demonstrated that FACT increases the rate of RNA polymerase II-mediated RNA synthesis on chromatin templates containing nucleosomes, and moreover, FACT specifically enhances the ability of polymerase to enter nucleosomes from promoter regions and to exit nucleosomes at termination sites[39][56].

Beyond its role in elongation, evidence has accumulated indicating that FACT also participates in transcription initiation, a perhaps surprising discovery given FACT's prominent characterization as an elongation factor[23]. Chromatin immunoprecipitation studies examining the formation of preinitiation complexes at promoter regions revealed that inactivation of Spt16 causes a substantial reduction in the formation of new preinitiation complexes at transcription start sites, suggesting that FACT facilitates the stable assembly of preinitiation complexes on chromatin[23]. Furthermore, FACT inactivation results in inappropriate initiation of transcription from cryptic promoters within gene bodies, indicating that FACT also suppresses spurious transcription initiation events[23]. This finding suggests that FACT contributes to transcriptional fidelity by linking the processes of initiation and elongation, perhaps by establishing a chromatin state that is refractory to transcription initiation at locations other than bona fide promoters.

The specific interactions between FACT components and transcription initiation factors have begun to be elucidated through biochemical studies[23]. FACT exhibits strong genetic interactions with the transcription factor TFIIH, and the association of FACT at promoters appears dependent on the kinase activity of TFIIH, suggesting direct functional coupling between these two essential transcription factors[23]. Spt16 and POB3 also genetically interact with basal transcription factors including TFIID and TFIIB, further supporting the model that FACT participates in the formation and/or stabilization of preinitiation complexes. The molecular basis for these interactions remains incompletely understood, but likely involves direct protein-protein contacts that position FACT appropriately to facilitate both transcription initiation and the subsequent transition to productive elongation.

## Function in DNA Replication and Replication Fork Progression

The involvement of POB3 and the FACT complex in DNA replication was among the earliest functions attributed to these proteins, predating recognition of their critical roles in transcription[45][52]. The discovery that POB3 physically associates with the catalytic subunit of DNA polymerase α, the polymerase responsible for initiating DNA synthesis at replication origins and during Okazaki fragment synthesis, provided the initial evidence for FACT's participation in replication[45][52]. Subsequent genetic and biochemical analyses have established that FACT plays essential roles in multiple aspects of DNA replication, including origin firing, replication fork progression, and the replication-coupled assembly of chromatin behind the advancing replication fork[14][17][49][52].

At the level of replication fork progression, FACT functions analogously to its role in transcription, facilitating polymerase passage through nucleosomal DNA by mediating dynamic nucleosome reorganization[10][49][52][59]. The chromatin template presents a significant barrier to replication fork progression, and nucleosomes must be partially disassembled ahead of the advancing polymerase and then reassembled behind the fork to maintain chromatin structure[49][59]. FACT accomplishes these nucleosome dynamics through the same fundamental mechanisms it employs during transcription elongation, binding to and stabilizing partially disrupted nucleosomes while facilitating H2A-H2B dissociation and subsequently promoting histone reassembly[17][42][56][59]. The replication fork-associated functions of FACT are distinguished from its transcription-related roles by the involvement of additional components of the replication machinery, including the proliferating cell nuclear antigen (PCNA) sliding clamp and various histone chaperones, which coordinate with FACT to ensure comprehensive nucleosome dynamics during replication[17].

The replication-coupled nucleosome assembly process, which couples the deposition of newly synthesized histones with ongoing DNA synthesis, depends critically on FACT function[17][42][49][59]. As the replication fork advances and newly synthesized DNA emerges from the polymerase, histone proteins must be rapidly deposited onto this nascent DNA to maintain chromatin structure and enable proper epigenetic regulation[17][49]. FACT contributes to this process not only through its direct H2A-H2B chaperone activity but also through its cooperation with other histone chaperones such as CAF-1 and ASF1, which are responsible for depositing newly synthesized H3-H4 dimers[17][49][59]. Studies employing chromatin immunoprecipitation have demonstrated that both Spt16 and POB3 associate with replication forks, and their enrichment correlates with the position of active DNA synthesis, much as their enrichment correlates with transcribing polymerase position during transcription[49][52][59].

The ubiquitylation of Spt16 by the cullin-based E3 ubiquitin ligase Rtt101 provides a mechanism for regulating FACT localization to replication origins and may serve to coordinate FACT function with the initiation of DNA replication[49][52]. Cells expressing ubiquitylation-defective mutants of Spt16 show altered localization of FACT to replication origins and display sensitivity to DNA-damaging agents, indicating that post-translational modification of FACT represents an important regulatory mechanism controlling its replication-specific functions. This ubiquitylation likely does not target FACT for degradation but rather serves as a localization signal that directs FACT to sites of active DNA replication where its nucleosome reorganization activity is required. The existence of such regulatory mechanisms highlights the sophisticated control of FACT localization and activity that has evolved to couple FACT function with the specific requirements of different cellular processes.

## Function in DNA Repair and Chromatin Remodeling During Damage Response

DNA damage creates particular challenges for cells, as lesions in DNA must be detected and removed through specialized repair pathways, but the lesions frequently reside within nucleosomes where they are occluded from direct access by repair proteins[21]. Nucleotide excision repair (NER), the primary pathway for removing bulky DNA adducts such as those induced by ultraviolet radiation or chemical mutagens, must therefore engage in sophisticated chromatin remodeling to expose damaged DNA to repair proteins[21][24]. FACT has emerged as a critical participant in this chromatin remodeling response to DNA damage, contributing to both the "access" phase in which nucleosomes are disrupted to expose lesions and the "restore" phase in which nucleosomes are reassembled after successful repair[21][24].

The molecular mechanisms by which FACT participates in NER appear to leverage the same nucleosome reorganization activities that FACT employs during transcription and replication[21]. Upon recognition of a DNA lesion, either by the global genomic NER pathway or by transcription-coupled NER mechanisms, the repair machinery must gain access to the damaged DNA[21][24]. FACT can promote both the eviction and subsequent reinsertion of H2A-H2B dimers from nucleosomes, activities that would allow repair proteins to access lesions within nucleosomal DNA and subsequently permit reassembly of chromatin after repair completion[21]. The mechanism by which FACT is recruited to DNA damage sites remains incompletely characterized, but likely involves direct recognition of lesions or activation through histone modifications associated with DNA damage response pathways[21]. Notably, the rapid recruitment of FACT to damage sites may be facilitated through interactions with DNA damage sensors such as the histone variants H2AX, which become phosphorylated upon DNA damage and may serve as recognition signals for chromatin-reorganizing factors[21].

## Nucleosomal Context and Histone Variant Specificity

Beyond its general role in nucleosome dynamics, POB3 as part of the FACT complex exhibits specific interactions with histone variants that distinguish it from canonical histones and indicate a regulatory role in histone variant incorporation and exclusion[43][46]. The histone variant H2A.Z, which is incorporated into chromatin primarily at promoter regions through the action of the SWR-C chromatin remodeling complex, is actively excluded from gene body regions through the combined action of FACT and another histone chaperone, Spt6[43]. Biochemical evidence demonstrates that while FACT and Spt6 efficiently remove H2A.Z-containing nucleosomes during transcription elongation, they cannot efficiently reincorporate H2A.Z back into nucleosomes, instead preferentially redepositing canonical H2A[43]. This selectivity in histone variant handling appears critical for maintaining the appropriate genomic distribution of H2A.Z, preventing its inappropriate incorporation into transcribed regions where it would be detrimental to normal gene expression.

Similarly, POB3 and FACT have been implicated in chromatin dynamics involving the centromeric histone variant CENP-A, which must be specifically excluded from euchromatic regions despite the abundance of CENP-A-loading machinery throughout the nucleus[43][34]. The mechanisms by which FACT participates in centromeric histone dynamics remain incompletely understood, but appear to involve both the selective removal of CENP-A-containing nucleosomes during transcription and the prevention of new CENP-A incorporation into non-centromeric regions[43][34][57]. These findings suggest that histone chaperones of the FACT family function not merely as general nucleosome dynamics factors but as sophisticated regulators of histone variant distribution, ensuring that specific histone variants occupy appropriate genomic regions.

## Biochemical Characterization of Histone Binding

The biochemical basis for POB3's histone-binding activities has been elucidated through a combination of biochemical, genetic, and structural approaches that have identified the specific domains and residues critical for binding to different histone species[7][11][13][19][28]. As discussed previously, the C-terminal acidic region of POB3 contains the primary binding site for H2A-H2B dimers, with a dissociation constant of approximately 0.3 μM under physiological salt conditions[19]. This binding is mediated by both the distributed acidic charges characteristic of histone chaperone acidic domains and a critical aromatic residue (phenylalanine 512 in yeast POB3) that makes the single largest individual contribution to binding affinity[19]. Mutation of this phenylalanine to alanine reduces H2A-H2B binding affinity by approximately 6-fold, a substantial effect for a single amino acid substitution and indicative of the prominent role of hydrophobic interactions in histone binding[19]. The Spt16 subunit of FACT possesses an analogous H2A-H2B binding site within its own C-terminal acidic region, and evidence suggests that Spt16 and POB3 bind competitively to overlapping sites on the H2A-H2B dimer surface[19].

The binding of POB3 to H3-H4 histones proceeds through a distinctly different mechanism involving the middle domain (Pob3-M) and proceeds with lower affinity compared to H2A-H2B binding[28][38][41]. The middle domain of POB3, with its characteristic double-PH domain architecture, directly engages with the H3-H4 tetramer, making contacts with both the histone fold domains and the N-terminal tail regions of these histones[28][38]. Importantly, unlike the histone chaperone Rtt106, which specifically recognizes H3 acetylated at lysine 56 (H3K56ac), POB3 binds to H3-H4 regardless of the acetylation state of H3K56[41]. This modification-independent binding of POB3 reflects its likely role in recycling parental histones during replication and transcription, as these histones would typically have been deacetylated at H3K56 by histone deacetylases following chromatin deposition[41].

The N-terminal domain of Spt16 (Spt16-N), with its characteristic pita-fold structure resembling peptide-binding domains of aminopeptidases, also contributes to histone binding by engaging with H3-H4 through recognition of histone N-terminal tails[7][13]. The binding of Spt16-N to H3-H4 tails shows high affinity (low nanomolar Kd values) and occurs through specific interaction surfaces within the N-terminal domain[7]. Mutations within conserved surface pockets of Spt16-N that disrupt H3-H4 tail binding cause significant phenotypic defects in cells, attesting to the biological importance of this interaction[7]. The cumulative effect of multiple histone-binding domains within the Spt16-POB3 heterodimer is to create a multivalent interaction platform that engages histones at multiple sites simultaneously, thereby achieving high avidity and specificity despite individual binding domains having modest intrinsic affinities[7][28][38].

## Cooperation with DNA-Binding Proteins and the Role of Nhp6

As noted previously, yeast POB3 lacks the intrinsic DNA-binding HMG-box domain possessed by mammalian SSRP1, instead relying on cooperation with separate small HMG-box proteins (Nhp6a and Nhp6b) to achieve DNA-binding capability[1][26][29][40]. The bipartite organization of this DNA-binding function raises important questions about how the separate DNA-binding and histone-binding components of the yeast FACT complex are coordinated. Biochemical experiments employing purified components have provided insights into this coordination[40]. Nhp6 proteins alone can bind to nucleosomes and linear DNA, and this binding induces marked changes in the electrophoretic mobility of nucleosomes[40]. Importantly, Spt16-POB3 alone does not substantially alter the electrophoretic mobility of DNA or nucleosomes[40]. However, when all three components (Spt16, POB3, and Nhp6) are combined with nucleosomes, a complex SPN-nucleosome structure forms with enhanced electrophoretic mobility and altered nuclease sensitivity distinct from Nhp6-nucleosomes alone[40].

These observations establish that while Nhp6 can initiate binding to nucleosomes independently, Spt16-POB3 specifically recognizes Nhp6-bound nucleosomes rather than binding to Nhp6 or nucleosomes independently[40]. This specificity ensures that FACT is recruited to chromatin through its association with DNA-binding proteins rather than through direct DNA contacts, a mechanism that may provide regulated access to specific chromatin regions. The functional consequences of this architecture include the ability to use Nhp6 as a modular DNA-binding platform that can be deployed to different chromosomal regions through regulated expression or localization of Nhp6 proteins. Quantitative analysis of the stoichiometry of SPN-nucleosome complexes indicates that each nucleosome is associated with approximately one heterodimer of Spt16-POB3, suggesting that FACT functions as a monomeric species on individual nucleosomes rather than as higher-order oligomers[40].

The evolutionary relationship between the bipartite yeast system (POB3 + Nhp6) and the monopartite mammalian system (SSRP1 with integrated HMG box) remains incompletely resolved. Fusing an HMG-box domain to the C-terminus of POB3 produces a fusion protein possessing DNA-binding activity, yet even this modified version shows residual dependence on Nhp6 for efficient nucleosome reorganization[8]. This finding suggests that the HMG-box domain alone is insufficient to fully replace Nhp6 function, possibly because Nhp6 proteins contribute functions beyond simple DNA binding, such as inducing specific nucleosome conformational changes that prime the nucleosome for FACT binding[8][26]. Alternatively, or in addition, Nhp6 proteins may enhance the accessibility or activity of the histone-binding domains of Spt16-POB3 through allosteric mechanisms.

## Genetic Interactions and Regulation

The essential nature of POB3 is underscored by the lethality of *pob3* null mutations in budding yeast[35][53]. However, comprehensive genetic screens have identified numerous alleles of *POB3* that cause conditional growth defects, providing tools for investigating FACT function. Many *pob3* mutations display synthetic defects with mutations in genes encoding other chromatin-associated proteins, histone acetyltransferases, and histone deacetylases, suggesting that FACT function is intimately coupled with chromatin modification and remodeling pathways[35][47][53]. The *pob3-Q308K* allele, extensively studied in recent years, causes a gain-of-function phenotype in which FACT retains enhanced nucleosome reorganization activity in vitro yet displays complex and sometimes counterintuitive growth phenotypes in vivo[36][47]. Analysis of this allele and its interactions with histone mutations has revealed that FACT function depends critically on proper coordination between histone-binding activities and the mechanical steps of nucleosome disassembly and reassembly[36][47].

Genetic evidence indicates that POB3 genetically interacts with histone H3, particularly mutations affecting histone H3 lysine 56, which is an important site for acetylation by the Rtt109 acetyltransferase during DNA replication[36][47]. The genetic interactions between *pob3* mutants and H3K56 mutations suggest direct functional coupling between FACT and the acetylation status of newly synthesized histones during replication-coupled nucleosome assembly[36][47]. Additionally, POB3 displays genetic interactions with genes encoding transcription factors and chromatin remodeling complexes, indicating that FACT functions within a broader network of chromatin-modifying activities[35][53]. The strength and nature of these genetic interactions provide clues to the cellular functions disrupted by different *pob3* mutations, allowing functional dissection of FACT's diverse roles.

Post-translational modifications of POB3 and Spt16 have begun to be characterized and appear to provide additional regulatory mechanisms controlling FACT activity[15][49][52]. The ubiquitylation of Spt16 by the Rtt101 ubiquitin ligase has been discussed previously in the context of replication regulation[49][52]. Additionally, the nuclear import of POB3 involves a C-terminal nuclear localization sequence that interacts with importin-α proteins[15]. Importantly, the importin-α interaction with POB3's nuclear localization sequence interferes with H2A-H2B binding, suggesting a regulatory mechanism in which nuclear import and histone chaperone activity are functionally linked[15]. This finding implies that newly synthesized or reimported POB3 molecules may be temporarily sequestered from histone binding during nuclear import and subsequently activated upon dissociation from import machinery, providing a potential checkpoint in FACT activation.

## Subcellular Localization and Chromatin Association

POB3, as part of the FACT complex, localizes to the nucleus where it associates with chromatin at sites of active gene expression and DNA replication[23][35][40][49][52][59]. Biochemical fractionation and microscopy studies have established that a substantial fraction of cellular FACT exists in free, nucleoplasmic pools in addition to the chromatin-associated population[35][40][49][52][59]. The dynamic equilibrium between these pools allows FACT to be recruited to different chromosomal regions as needed for transcription, replication, and repair. The recruitment of FACT to specific chromosomal locations appears mediated through multiple mechanisms, including direct interaction with transcribing RNA polymerase II and with DNA polymerase α at replication forks, as well as through interactions with DNA-binding proteins such as Nhp6[23][40][49].

Chromatin immunoprecipitation experiments employing epitope-tagged POB3 or Spt16 have mapped the genomic distribution of FACT and revealed that FACT enrichment correlates strongly with active gene transcription[9][23][46]. On actively transcribed genes, FACT shows particularly high enrichment at the promoter regions and 5' ends of genes, consistent with roles in both transcription initiation and early elongation[23][46]. Throughout gene bodies, FACT levels correlate with RNA polymerase II occupancy, indicating that FACT travels with the transcribing polymerase[23][39]. At the 3' ends of genes, FACT shows reduced enrichment, and particularly at polymerase III-transcribed genes, FACT exhibits preferential accumulation at the 3' ends, suggesting specific roles in transcription termination for this polymerase[9][46].

The association of FACT with replication forks can be inferred from its enrichment in replicating chromatin and its physical association with DNA replication machinery, though direct visualization of FACT at individual replication forks at the genome-wide level remains technically challenging[49][52][59]. Cell cycle analyses have provided evidence that FACT association with chromatin varies across the cell cycle, with some reports indicating increased FACT chromatin association during S phase when replication is occurring[49][52]. This cell cycle-dependent localization may reflect the distinct requirements for FACT activity at different stages of the cell cycle and provides another layer of regulatory control over FACT function.

## Evolution and Conservation Across Eukaryotic Species

POB3 and its orthologs represent a highly conserved family of proteins found throughout eukaryotic evolution, from fungi to plants to animals, indicating the fundamental importance of FACT-mediated chromatin dynamics for eukaryotic gene expression and DNA replication[1][2][8][26][27]. The evolutionary history of the FACT complex appears to involve an ancestral single-subunit FACT protein (similar to mammalian SSRP1) that underwent divergent evolution in different eukaryotic lineages. In fungi, this divergence resulted in the separation of histone-binding and DNA-binding functions into distinct protein subunits—the histone-binding POB3 and the DNA-binding Nhp6 partners. In mammals and plants, the ancestral protein maintained its integrated structure with both functions residing in the single SSRP1 polypeptide[1][8][26][27]. The existence of these alternative solutions to achieving FACT function indicates that the fundamental requirement is for a molecular platform capable of simultaneously binding histones and DNA in a manner that permits nucleosome reorganization, and that this requirement can be met through either monopartite or multipartite protein complexes.

The conservation of specific amino acid sequences within POB3 and SSRP1 family members extends beyond the overall domain architecture, with particular conservation evident in the C-terminal acidic regions responsible for H2A-H2B binding and the middle domain pleckstrin homology folds[25][27][28][38]. The critical aromatic residue (phenylalanine 512 in yeast POB3) that makes the largest contribution to H2A-H2B binding is conserved across all characterized SSRP1 family members, highlighting the fundamental importance of this specific residue for FACT function[19]. Similarly, the N-terminal regions mediating heterodimerization with Spt16 are highly conserved, indicating that the Spt16-POB3 partnership has been maintained throughout eukaryotic evolution[25][27][37][40].

## Conclusions and Remaining Questions

POB3 emerges from extensive molecular and genetic research as a critical histone chaperone subunit of the essential FACT complex, fulfilling indispensable roles in nucleosome dynamics during transcription elongation, DNA replication, and DNA repair. The protein's activity as a histone chaperone—facilitating the reversible disassembly and reassembly of nucleosomes without ATP hydrolysis—provides a molecular foundation for understanding how cells navigate the substantial physical barrier that chromatin presents to polymerase progression. The distinctive modular architecture of POB3, featuring pleckstrin homology domains and an acidic C-terminal histone-binding region, has been precisely sculpted by evolution to enable multiple simultaneous histone interactions through distinct domains, achieving the high specificity and avidity required for productive nucleosome dynamics.

The uncovering of POB3's roles in multiple essential cellular processes—transcription initiation, transcription elongation, DNA replication, and DNA repair—demonstrates the remarkable functional versatility of this single protein, accomplished through utilization of identical nucleosome-reorganizing biochemical mechanisms in diverse cellular contexts. The evolutionary conservation of POB3 and its orthologs across eukaryotes, from simple fungal cells to complex multicellular organisms, underscores the fundamental requirement for FACT-mediated chromatin dynamics in eukaryotic genome function. The sophisticated regulation of POB3 and FACT activity through post-translational modifications, protein-protein interactions, and cell cycle-dependent localization suggests that the finely tuned control of FACT function represents an important regulatory layer in eukaryotic gene expression and DNA replication.

Despite the substantial progress in understanding POB3 function achieved in recent years, significant questions remain regarding the precise molecular mechanisms by which POB3 and FACT mediate the diverse cellular functions attributed to them. The structural basis for how POB3's multiple histone-binding domains cooperate to coordinate binding to H3-H4 and H2A-H2B simultaneously warrants further investigation through structural studies. The mechanisms by which different histone modifications influence POB3 binding and activity, particularly whether POB3 recognizes specific histone acetylation patterns or other post-translational modifications beyond H3K56ac, remain incompletely characterized. The relative contributions of different POB3 domains to specific biological outcomes—particularly the roles of the N-terminal heterodimerization domain and the middle pleckstrin homology domain in organismal physiology—require further genetic and biochemical analysis.

Additionally, the coordination of FACT with other chromatin-associated proteins and remodeling complexes in establishing and maintaining appropriate chromatin states during transcription and replication demands continued investigation. How FACT activity is regulated in response to different cellular signals and stresses, and whether POB3 undergoes cell cycle-dependent modifications that alter its activity or localization, remain incompletely understood. The potential involvement of POB3 and FACT in developmental and differentiation processes, particularly in higher eukaryotes, represents an area of active investigation with important implications for understanding how chromatin dynamics contribute to developmental gene expression programs. These remaining questions ensure that POB3 and the FACT complex will continue to be subjects of intensive investigation, with the expectation that continued research will reveal additional layers of sophistication in how this essential histone chaperone complex maintains the dynamic chromatin architecture required for eukaryotic genome function.

## Citations

1. https://www.yeastgenome.org/locus/S000004534
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC165710/
3. https://www.ensembl.org/id/YML069W
4. https://www.uniprot.org/uniprotkb/Q04636/publications
5. https://www.uniprot.org/uniprotkb/O94529/entry
6. https://www.uniprot.org/uniprotkb/Q04636/entry
7. https://www.pnas.org/doi/10.1073/pnas.0712293105
8. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2020.00085/full
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC7901838/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC3229669/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC3761294/
12. https://www.yeastgenome.org/complex/CPX-3215
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC3627427/
14. https://pubmed.ncbi.nlm.nih.gov/26414936/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC5912460/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC7066812/
17. https://pubs.acs.org/doi/abs/10.1021/acschembio.5b00493
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC4620744/
19. https://genesdev.cshlp.org/content/18/20/2437.full
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC3497329/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC262413/
22. https://en.wikipedia.org/wiki/Nucleotide_excision_repair
23. https://www.vandemark.pitt.edu/publications/2008spt16p.pdf
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC125512/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC6028955/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC3624403/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC100271/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC4685450/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC7617577/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC8860598/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC5224485/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC3687001/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC1461200/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC6404263/
35. https://pubmed.ncbi.nlm.nih.gov/10413469/
36. https://www.science.org/doi/10.1126/science.abp9466
37. https://www.pnas.org/doi/full/10.1073/pnas.1119095109
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC9807050/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC4475440/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC232271/
41. https://academic.oup.com/nar/article/39/10/4023/1293592
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC3142300/
43. https://genesdev.cshlp.org/content/21/18/2288.full.html
44. https://thebiogrid.org/102491/publication/ubiquitylation-of-fact-by-the-cullin-e3-ligase-rtt101-connects-fact-to-dna-replication.html
45. https://pubs.acs.org/doi/abs/10.1021/bi982851d
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC10250246/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC2904938/
48. https://www.pnas.org/doi/10.1073/pnas.1904324116
49. https://academic.oup.com/nar/article/44/19/9142/2468379
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC6238592/
51. https://pmc.ncbi.nlm.nih.gov/articles/PMC7612134/
52. https://portlandpress.com/essaysbiochem/article/63/1/29/174/The-histone-chaperoning-pathway-from-ribosome-to
53. https://thebiogrid.org/35097/summary/saccharomyces-cerevisiae/pob3.html