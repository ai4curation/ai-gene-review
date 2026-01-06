---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-31T19:52:01.417640'
end_time: '2025-12-31T19:53:54.633404'
duration_seconds: 113.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: SPT16
  gene_symbol: SPT16
  uniprot_accession: P32558
  protein_description: 'RecName: Full=FACT complex subunit SPT16; AltName: Full=Cell
    division control protein 68; AltName: Full=Facilitates chromatin transcription
    complex subunit SPT16; AltName: Full=Suppressor of Ty protein 16;'
  gene_info: Name=SPT16; Synonyms=CDC68, SSF1; OrderedLocusNames=YGL207W;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the peptidase M24 family. SPT16 subfamily.
  protein_domains: Creatin/AminoP/Spt16_N. (IPR029149); Creatinase/aminopeptidase-like.
    (IPR036005); FACT-SPT16_Nlobe. (IPR029148); Fact-SPT16_PH. (IPR056595); FACT_SPT16_C.
    (IPR048969)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 47
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P32558
- **Protein Description:** RecName: Full=FACT complex subunit SPT16; AltName: Full=Cell division control protein 68; AltName: Full=Facilitates chromatin transcription complex subunit SPT16; AltName: Full=Suppressor of Ty protein 16;
- **Gene Information:** Name=SPT16; Synonyms=CDC68, SSF1; OrderedLocusNames=YGL207W;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the peptidase M24 family. SPT16 subfamily.
- **Key Domains:** Creatin/AminoP/Spt16_N. (IPR029149); Creatinase/aminopeptidase-like. (IPR036005); FACT-SPT16_Nlobe. (IPR029148); Fact-SPT16_PH. (IPR056595); FACT_SPT16_C. (IPR048969)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SPT16" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SPT16' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SPT16** (gene ID: SPT16, UniProt: P32558) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze this request carefully. The user is asking for a comprehensive research report on SPT16 (UniProt P32558) from Saccharomyces cerevisiae. 

First, I need to verify this is the correct gene by checking against the search results provided:

From the search results:
- Source 1 shows SPT16 from yeastgenome.org with information about FACT complex
- Source 2 mentions "The CDC68 gene (also called SPT16) encodes a transcription factor" - this confirms SPT16 is also known as CDC68
- Source 3 discusses "Structure of the Spt16 Middle Domain" - clearly about the same protein
- Multiple sources discuss FACT complex with Spt16 as a major subunit

The UniProt description says:
- RecName: FACT complex subunit SPT16
- AltName: Cell division control protein 68
- AltName: Suppressor of Ty protein 16
- Gene: SPT16; Synonyms: CDC68, SSF1
- Organism: Saccharomyces cerevisiae
- Family: Peptidase M24 family, SPT16 subfamily

This matches perfectly with what I found in the search results. SPT16 is indeed the large subunit of the FACT complex, also known as Cdc68 or Spt16p in yeast.

Now I need to structure a comprehensive 10,000+ word report covering:
1. Title and summary
2. Main sections covering:
   - Overview and structural organization
   - Molecular composition and protein domains
   - Role in transcription/chromatin dynamics
   - Role in DNA replication
   - Role in DNA repair
   - Protein-protein interactions
   - Regulation and post-translational modifications
   - Evolutionary conservation
3. Conclusion

Let me plan this carefully to ensure I create a comprehensive, well-cited report that follows all formatting rules.
</think>

# Comprehensive Functional Analysis of SPT16: A Critical Histone Chaperone in Saccharomyces cerevisiae

The SPT16 gene encodes a large subunit of the **FACT complex** (Facilitates Chromatin Transcription), a highly conserved heterodimeric histone chaperone that serves as a central orchestrator of chromatin dynamics across multiple DNA-dependent biological processes[2][11]. The protein, also known as CDC68 or Cdc68p, represents one of the most multifunctional chromatin regulators in eukaryotic cells, functioning not merely as a passive facilitator of transcription but as a dynamic manager of nucleosome integrity that operates across transcription, DNA replication, and DNA repair pathways. With a molecular weight of approximately 120.6 kilodaltons and a length of 1,035 amino acids, Spt16p exhibits a sophisticated domain architecture that enables complex interactions with nucleosomal histones and DNA, positioning it as an essential component of the cell's chromatin homeostasis machinery[5][10]. The critical importance of SPT16 is underscored by its essential function in budding yeast, where loss of FACT complex activity compromises cellular viability, yet paradoxically, the dependence on FACT varies dramatically across eukaryotic cell types, suggesting highly specialized roles in different biological contexts.

## Structural Organization and Domain Architecture of Spt16p

The Spt16 protein exhibits a tripartite domain organization that reflects its multifaceted functional capabilities within the FACT complex and in chromatin transactions[46]. The protein comprises three major structural domains: an N-terminal domain (Spt16-NTD or Spt16-N), a middle domain (Spt16-MD or Spt16-M), and a C-terminal domain (Spt16-CTD or Spt16-C), each contributing distinct molecular functions to the overall activity of the complex[15][18]. The N-terminal domain, spanning approximately 450 residues, demonstrates homology to the catalytic domain of aminopeptidases, exhibiting the characteristic "peptidase-like" or "pita-fold" structure typical of the M24 peptidase family[15][18][25]. However, detailed structural and biochemical characterization has revealed that this domain has lost enzymatic activity through evolution and has been repurposed as a histone-binding module with specialized interactions to histone H3 and H4 tails and globular domains[15]. The Spt16-NTD achieves high-affinity binding to H3-H4 cores through interactions with their globular domains and N-terminal tails, with distinct binding surfaces recognizing the H3 tail separately from the H4 tail, suggesting a sophisticated molecular recognition mechanism[15].

The middle domain of Spt16 adopts a distinctive double pleckstrin homology architecture that shares remarkable structural similarity to the middle domain of the Pob3 protein (the yeast partner of Spt16) and to the histone chaperone Rtt106[3][24]. This double PH domain structure comprises two tandem pleckstrin homology motifs arranged in an unusual rigid configuration, and biochemical and genetic studies have demonstrated that this domain interacts directly with histone H3-H4 tetramers with low micromolar affinity[3][24][31]. The functional significance of the Spt16-M domain is particularly well-established through extensive genetic studies, as many mutations affecting FACT function map to this domain, and several of these mutations can be suppressed by mutations in histone H3 that destabilize the H3-H4 interface, indicating a critical functional link between Spt16-M and histone tetramer stability[3][24][31]. Furthermore, genetic studies have demonstrated that mutations affecting the Spt16-M domain that cause derepression of the SER3 locus can be suppressed by mutations in Spt16-M itself, supporting a role for this domain in reassembly of nucleosomes following passage of RNA polymerase[3][24].

The C-terminal domain of Spt16, designated as Spt16-CTD or Spt16-C, comprises an acidic region rich in aspartate and glutamate residues that is essential for protein viability and cellular function[40][56]. This domain exhibits inherent structural disorder and serves as the primary interface for histone H2A-H2B dimer binding, with multiple studies establishing that the acidic C-terminus is required for interaction with H2A-H2B dimers both in biochemical assays and in the context of intact nucleosomes[7][15][40]. The interaction of Spt16-CTD with H2A-H2B dimers represents a critical functional module, as it enables FACT to tether and stabilize the H2A-H2B dimer during complex nucleosome reorganization events[7][16]. In addition to its histone-binding functions, the Spt16-CTD has recently been shown to contain an intrinsically disordered region (IDR) that plays a regulatory role in chromatin dynamics and transcription initiation[27][37]. This IDR facilitates eviction of H2A-H2B dimers from inducible promoters upon transcription induction, thereby stimulating pre-initiation complex formation and transcription initiation, while also regulating chromatin reassembly at coding sequences in the wake of elongating RNA polymerase II[27][37].

## Role of Spt16p in Transcription Elongation and Chromatin Dynamics

The most well-established function of Spt16p resides in its role during RNA polymerase II-dependent transcription, where it operates as a critical regulator of chromatin structure and nucleosome dynamics during both transcriptional initiation and elongation[9][10][17]. The FACT complex, with Spt16p as its large subunit, was originally identified and characterized through its ability to stimulate transcription of chromatin templates in vitro, demonstrating that FACT directly facilitates RNA polymerase passage through nucleosomal barriers[10][53]. In yeast cells, FACT specifically associates with active RNA polymerase II genes in a manner dependent on the TFIIH transcription factor, and travels across genes with elongating Pol II in a coordinated fashion[9][35]. Chromatin immunoprecipitation studies have shown that Spt16p localizes to transcriptionally active genes, with a distribution pattern that corresponds to the trajectory of elongating RNA polymerase II, entering the gene at or near the promoter and proceeding toward the 3′ end of the gene during active transcription[9].

The detailed mechanism by which Spt16p and the FACT complex facilitate transcription elongation involves a sophisticated choreography of nucleosome disassembly and reassembly events that occur in coordination with polymerase progression. Recent structural studies using cryo-EM have elucidated the structure of FACT bound to partially disassembled nucleosomes in the context of an elongation complex, revealing that the Spt16 middle domain interacts with the H3-H4 tetramer and the proximal H2A-H2B dimer, becoming integrated with the histone hexamer unit[13]. The Spt16-MD interacts with the exposed basic surface of the H3-H4 through highly acidic regions, particularly through an HA1 helix and its flanking loop that directly bind the exposed H3 α1 helix and H4 N-terminal tail, while the Spt16 linker helix extends along the H2A α2 helix and can interact with nucleosomal acidic patch residues[13]. These interactions allow Spt16 to disrupt the important interaction between H2A-H2B and H3-H4 mediated by the H2A-docking domain while simultaneously stabilizing the subnucleosomal structure through multiple contact points[13]. This mechanism ensures that FACT prevents the loss of the proximal H2A-H2B dimer, maintaining histone octamer integrity during the passage of the elongation complex.

A critical and unexpected function of FACT and Spt16p has emerged through studies examining the role of these proteins in preventing aberrant transcriptional initiation from cryptic promoters located within gene bodies. Conditional inactivation of Spt16p in yeast results in increased RNA polymerase II density, transcription, and TATA-binding protein occupancy in the 3′ portions of certain coding regions, indicating that FACT suppresses inappropriate initiation from cryptic promoters within mRNA coding regions[9][35]. This function operates through maintenance of proper chromatin structure, as nucleosomes normally occlude these cryptic promoters, and when FACT function is compromised, these sites become exposed to transcriptional machinery, leading to fortuitous internal initiation events[9][35]. In plant cells, FACT is similarly found to associate with elongating Arabidopsis RNA polymerase II as part of the transcript elongation complex and functions as a repressor of aberrant intragenic transcriptional initiation[10]. This role in transcriptional fidelity appears to be fundamental to FACT's function across eukaryotes, suggesting that a key role of the complex is to maintain chromatin integrity in the wake of polymerase passage, preserving both histone modification patterns and nucleosome positioning that normally restrict transcription to designated promoters.

## The Multidomain Architecture of Spt16 in Nucleosome Reorganization

The ability of Spt16p and the FACT complex to facilitate nucleosome dynamics depends critically on the coordinated action of multiple histone-binding domains that can sequentially engage different nucleosomal components during reorganization and reassembly cycles. Human FACT subunits, while not the direct research focus here, have been shown through functional studies to coordinate in a manner that appears conserved with yeast FACT, with the SSRP1 HMGB domain functioning to displace DNA from nucleosomes while the SPT16 middle domain and C-terminal domain work to stabilize and tether disrupted histone-DNA interactions[16]. Isolated SSRP1 HMGB domains promote rapid octamer dissociation but cannot support nucleosome reformation, whereas isolated SPT16 middle domains weakly stabilize strong site-DNA interactions, and only the combination of both subunits with the SPT16 C-terminal tethering domain enables full catalytic activity in both nucleosome disassembly and reassembly[16]. This demonstrates that FACT functions as a true catalyst, with the two key domains plus the tethering ability of the SPT16 C-terminal domain working together to lower the energy barrier to nucleosome reorganization[16].

The mechanism by which FACT-mediated nucleosome disassembly and reassembly occur appears to involve specific recognition of partially unfolded nucleosome states that arise during transcription. Biochemical studies have established that FACT binds with higher affinity to nucleosomes that have already undergone partial disruption than to intact, fully wrapped nucleosomes, and importantly, FACT does not bind significantly to naked DNA[50][56]. This specificity for disrupted nucleosomes suggests that FACT functions to stabilize and manage partially unwrapped nucleosomal states that naturally arise during polymerase passage, rather than actively unwinding intact nucleosomes de novo[50][56]. The observation that a single FACT molecule may be recycled from one nucleosome to the next as RNA polymerase II progresses along genes further supports this model, wherein FACT is continuously reused to manage the series of transient nucleosome disruptions that occur during elongation[41][56]. Recent evidence suggests that the chromatin remodeler Chd1 plays a critical role in facilitating this recycling process, with Chd1's ATPase activity appearing essential for determining FACT distribution on genes without affecting its initial recruitment[41][56].

## Role of Spt16p in Histone Chaperone Activities and Nucleosome Assembly

Beyond its functions in transcription, Spt16p operates as a bona fide histone chaperone capable of facilitating both nucleosome disassembly and assembly, functions that are essential for multiple DNA-dependent processes. The histone chaperone activity of FACT has been demonstrated through purified component reconstitution experiments showing that FACT can mediate the sequential assembly of nucleosomes through tethering and deposition of histone components[7]. In these in vitro assays, FACT interacts with H2A-H2B dimers and forms a ternary complex with (H3-H4)₂ tetramers and DNA, and through competition between free DNA and histone-DNA interactions, FACT promotes both hexasome and nucleosome formation[7]. Specifically, FACT is shown to facilitate H2A-H2B deposition onto tetrasomes through a mechanism wherein free DNA extending from the tetrasome competes FACT off the H2A-H2B dimer, effectively resulting in H2A-H2B deposition onto (H3-H4)₂ tetrasomes to form hexasomes and ultimately complete nucleosomes[7]. This mechanism reveals how the multiple histone-binding domains of Spt16p enable a sophisticated tethering activity that first captures and stabilizes histone components during disruption, then guides their deposition during reassembly through DNA-histone competition dynamics.

The role of Spt16p in promoting nucleosome reassembly appears to be particularly important for maintaining chromatin structure and suppressing aberrant gene expression in the wake of transcribing polymerase. Genetic evidence indicates that several features of Spt16 mutations that affect nucleosome reassembly map specifically to the middle domain, and that disruption of FACT activity results in activation of cryptic transcription initiation sites within coding regions due to nucleosome loss and failure of proper nucleosome reformation[23]. This suggests that Spt16p and FACT function to monitor and restore nucleosome integrity as a system of quality control, ensuring that the genome maintains proper chromatin structure even after perturbation by transcriptional machinery[50]. The distinction between Spt16p's roles in nucleosome disruption during transcription elongation versus its roles in nucleosome restoration appears important, as mutations affecting these functions can be separated genetically through different histone mutations that suppress distinct FACT defects[50]. For example, some mutations in Spt16 cause derepression of normally repressed genes through disruption of chromatin assembly, while other mutations affect proper Spt16 localization and its association with chromatin during transcription, indicating that promoting and resolving changes in nucleosome structure represent at least partially separable functions[50].

## Spt16p Function in DNA Replication and Parental Histone Recycling

The FACT complex, with Spt16p as its large subunit, plays critical roles in DNA replication that extend well beyond its transcriptional functions, particularly in the disassembly of nucleosomes ahead of replication forks and the preservation of parental histones during chromatin replication. FACT is known to associate directly with replication complex components, including the replicative MCM2-7 helicase and DNA polymerase α, interactions that appear essential for maintaining normal DNA replication fork progression rates[14][44][47]. In cells depleted of the SSRP1 subunit of FACT, DNA replication fork progression is significantly slowed, with the tracking length of newly synthesized DNA substantially reduced compared to wild-type cells, while DNA replication initiation rates appear normal, indicating that FACT's primary replication role is in fork elongation rather than initiation[47]. Furthermore, nucleosome reassembly on daughter strands does not appear to be significantly affected by SSRP1 depletion, suggesting that FACT's critical replication function relates to its ability to maintain normal replication fork rates by disassembling prereplicative nucleosomes ahead of the fork rather than in de novo nucleosome assembly[47].

A particularly important and recently characterized function of Spt16p involves the recycling and transfer of parental histones to newly replicated DNA strands during DNA replication, a process essential for maintaining epigenetic information and histone modification patterns across cell divisions[21][44][55]. The N-terminal domain of Spt16 (Spt16-N), which was previously thought to be largely dispensable for nucleosome binding based on in vitro studies, has been revealed to function as a critical protein-protein interaction module that enables FACT to serve as a shuttle chaperone in collaboration with the replicative MCM2-7 helicase and other replisome components[21][44][55]. Specifically, the Spt16-N domain interacts directly with the MCM2-7 complex and is essential for the formation of a ternary complex involving FACT, histone H3/H4, and the Mcm2 histone binding domain, which is critical for efficient recycling and transfer of parental histones to lagging strands[21][44][55]. Depletion of Spt16 or mutations in the middle domain that impair histone binding compromise parental histone recycling on both leading and lagging strands, though the Spt16-N domain deletion produces more pronounced defects specifically on the lagging strand[21][44][55]. This lagging strand-specific defect aligns with the observation that Spt16-N domain interactions with replisome components including the fork protection complex subunits (Mrc1-Tof1-Csm3) and DNA polymerase α are critical for positioning FACT properly at replication forks[21][44][55].

The mechanism by which Spt16p facilitates parental histone recycling during replication involves coordinated interactions with multiple replisome components and histones. Recent evidence suggests that while Dpb3 and Dpb4 subunits of DNA polymerase ε facilitate transfer of parental histones to the leading strand, the Mcm2-Ctf4-DNA polymerase α axis aids in transfer to the lagging strand[21][44]. The Spt16-N domain's interaction with the MCM2-7 complex and the fork protection complex positions FACT at the replication fork in coordination with these polymerase-associated pathways, enabling efficient local transfer of parental histones[21][44]. The tethering activities mediated by Spt16's middle and C-terminal domains likely function to stabilize partially dissociated histones and facilitate their transfer to daughter strands, analogous to their roles during transcription, thereby preserving epigenetic memory across replication[21][44][50]. This function of Spt16p appears especially important for maintaining heterochromatic states and ensuring proper epigenetic transmission through cell divisions.

## Spt16p in DNA Repair and Base Excision Repair

Beyond its established roles in transcription and replication, Spt16p participates in DNA repair processes, particularly in base excision repair (BER), through a mechanism that involves switching from transcription-associated protein complexes to DNA repair protein complexes. Upon induction of oxidative DNA damage, FACT is recruited rapidly to sites of damage coincident with glycosylase enzymes, demonstrating active participation in the repair response[26]. FACT has been shown to facilitate removal of damaged bases by uracil-DNA glycosylase (UDG) from nucleosomal DNA through a novel mechanism involving boosting of the activity of ATP-dependent chromatin remodelers such as RSC[26]. Specifically, FACT greatly facilitates UDG removal of uracil from nucleosomal DNA by cooperating with the RSC chromatin remodeler to generate remodeled nucleosome-like structures with enhanced DNA accessibility[26]. This co-remodeling activity, wherein FACT strongly enhances the remodeling capacity of chromatin remodelers at DNA damage sites, suggests a mechanistic principle wherein Spt16p's histone-binding and nucleosome-reorganizing capabilities are deployed in the context of DNA repair pathways to temporarily expose damaged DNA sites for repair enzyme access while maintaining overall chromatin integrity[26].

The recruitment of FACT to DNA damage sites appears to involve recognition of partially disrupted nucleosomal states by Spt16p and SSRP1, likely through mechanisms similar to those operating during transcription, wherein partially unfolded nucleosomes are preferentially recognized and stabilized by FACT[26]. The HMG domain of SSRP1 may contribute to recognizing the deformed DNA at damaged sites, while Spt16p's multiple histone-binding domains enable tethering and management of histone components during the repair process[26]. This role of Spt16p in DNA repair, while less extensively characterized than its transcriptional functions, underscores the principle that FACT operates as a general manager of chromatin dynamics during any process that perturbs nucleosome structure.

## Regulation of Spt16p and the FACT Complex Through Protein Stability Mechanisms

The levels of Spt16p and its partner SSRP1 in the cell are subject to sophisticated regulatory mechanisms that depend on the presence of their mRNAs and their association within the FACT complex, establishing an unusual form of post-transcriptional control with important implications for cellular differentiation and function[38][54]. Notably, the FACT complex is highly expressed in undifferentiated cells including germ cells, stem cells, and progenitor cells, but shows dramatically reduced expression in most differentiated cells of higher organisms, and is frequently upregulated in cancer cells, particularly in poorly differentiated, aggressive tumors[38][54]. This differential expression pattern prompted investigations into the mechanisms controlling FACT levels, which revealed that the stability of SSRP1 and SPT16 proteins depends critically on the presence of SSRP1 and SPT16 mRNAs[38][54]. When SSRP1 mRNA levels drop, the FACT complex quickly degrades, and importantly, in the absence of FACT complex, both SSRP1 and SPT16 mRNAs become unstable and are inefficiently translated, making reactivation of FACT function unlikely in normal cells following its downregulation[38][54].

This mutual stabilization mechanism creates an intricate regulatory circuit wherein SSRP1 mRNA acts as the key driver of FACT complex stability and levels, exerting a notably stronger effect on SPT16 protein stability than SPT16 exerts on SSRP1[38][54]. The presence of SSRP1 and SPT16 mRNAs bound to the FACT complex stabilizes the proteins themselves, while the FACT proteins enhance the stability and translation efficiency of their own mRNAs, creating a self-reinforcing cycle[38][54]. This unusual mode of regulation appears advantageous because it maintains an extremely stable FACT complex when sufficient mRNA is present, minimizing energy consumption for continuous protein synthesis, while simultaneously allowing rapid and effective reduction of FACT levels simply by reducing mRNA transcription[38][54]. Upon induction of differentiation or senescence in cultured cells, both SSRP1 and SPT16 protein levels decline rapidly and effectively, accompanied by reduced expression of their mRNAs, suggesting that this regulatory system enables cells to precisely control FACT availability in response to developmental cues.

Spt16p is further regulated through post-translational modifications that modulate its biochemical activity and interactions with histones. In mammalian cells, SPT16 undergoes ubiquitylation and proteasomal degradation to regulate transcription and control cell cycle progression, with impairment of proteasomal degradation leading to upregulation of SPT16 and enhancement of cell cycle progression genes while suppressing cell differentiation genes[30][51]. The proteasomal regulation of SPT16 has been found to be impaired in cancer cells, contributing to the elevated SPT16 levels observed in tumor cells, suggesting that targeting this degradation pathway could represent a potential anti-cancer strategy[30][51]. In plant cells, phosphorylation of SPT16 catalyzed by protein kinase CK2 modulates histone interactions, with a non-phosphorylatable version of SPT16 showing reduced histone binding and reduced ability to complement growth and developmental phenotypes of spt16 mutant plants[60]. Importantly, phosphorylation of SPT16 by CK2 increases its interaction with nucleosomal histones, suggesting that this post-translational modification functions to enhance the histone chaperone activity of Spt16p[60].

## Protein-Protein Interactions and Partnership with SSRP1

The function of Spt16p in virtually all its known biological roles depends critically on its association with SSRP1 (termed Pob3 in yeast), which comprises the second subunit of the FACT complex. The Spt16-SSRP1 heterodimeric complex exhibits extraordinary conservation across eukaryotes, with homologous proteins identified in organisms ranging from yeast to humans and plants, reflecting the fundamental importance of this complex for chromatin regulation[1][4][10]. The dimerization between Spt16 and SSRP1 is mediated through the middle domain of Spt16 (containing two pleckstrin homology motifs) and the N-terminal/dimerization domain of SSRP1, with recent structural studies revealing that this interaction is mutually exclusive with SSRP1 homodimerization[43]. Specifically, substitutions in the SSRP1 pleckstrin homology domain that disrupt SPT16 binding also disrupt SSRP1 homodimerization, and evidence suggests that SSRP1 homo- and heterodimerization compete for the same SSRP1 surface[43]. This raises the intriguing possibility that SSRP1 may exist in multiple oligomeric states with different functional consequences, potentially enabling SPT16-independent functions of SSRP1 under certain cellular conditions[43].

Beyond its obligate partnership with SSRP1, Spt16p interacts with an extensive network of other proteins involved in transcription, replication, and repair. Chromatin immunoprecipitation and co-immunoprecipitation experiments have identified associations between Spt16p and numerous elongation factors, including Spt4/5, Spt6, and components of the TREX complex, consistent with its role in transcriptional elongation[9]. The interaction of Spt16p with the replicative helicase MCM2-7 through its N-terminal domain has been noted above as critical for replication functions[21][44][55]. Additional interactions include those with histone H3 and H4 through the N-terminal and middle domains, H2A-H2B through the C-terminal domain, and DNA through multiple regions of the protein[15][18][24][31][56]. More recent discoveries have identified interactions between Spt16p and kinetochore proteins including CENP-A and components of the constitutive centromere-associated network (CCAN), suggesting roles for Spt16p in centromere establishment and chromosome segregation[45]. These multifaceted interactions underscore the position of Spt16p as a central hub protein within the chromatin regulatory machinery, engaging with numerous partners to coordinate diverse aspects of chromatin dynamics.

## Molecular Mechanism of Spt16p Function: A Unicycle Model

Recent structural and biochemical advances have generated detailed models for the molecular mechanism by which Spt16p orchestrates nucleosome dynamics. A particularly illuminating model describes FACT as resembling a unicycle structure, with Spt16p and SSRP1 forming the "saddle" and "fork" respectively that is engaged in extensive interactions with nucleosomal DNA and histones[10][56]. In this model, the middle domains of both Spt16p and SSRP1 reach down on both sides, interacting with DNA at the dyad axis (the center of the nucleosome), the H3-H4 tetramer beneath, and extending down to the H2A-H2B dimer "pedals," thereby forming both forks of the unicycle structure[56]. The positioning of both middle domains with H3 and H4 histones would clash with the trajectory of DNA in a fully wrapped nucleosome, explaining why destabilization of histone-DNA interactions stimulates FACT binding and why FACT preferentially engages with partially unwrapped or disrupted nucleosomes[56]. The C-terminal domains of both Spt16p and SSRP1 contribute to this architecture, with the SPT16-CTD serving the critical function of binding to and helping tether H2A-H2B dimers as DNA is displaced[16].

In the context of transcription elongation by RNA polymerase II, recent cryo-EM structures show that Spt16p becomes engaged with the polymerase as part of a large elongation complex that includes additional factors such as Spt4/5 and Spt6. The Spt16 middle domain makes extensive contacts with multiple components of the RNA polymerase II elongation complex, including the Spt6 YqgF and Spt5 KOW1 domains, while simultaneously maintaining interactions with the downstream nucleosome that is being disrupted[13]. This arrangement allows FACT to manage a transitional nucleosome state as the polymerase advances, tethering nucleosome components together while exposing DNA for polymerase passage and preventing loss of histone components[13]. As the polymerase proceeds further along the gene, the upstream DNA rewraps around the histone octamer behind the polymerase, and FACT dissociates once nucleosome reassembly is complete[13]. This cyclic process may be repeated multiple times as the polymerase traverses a long gene, with FACT molecules being recycled from the upstream newly reassembled nucleosome to the downstream disrupted nucleosome through the action of chromatin remodelers like Chd1[13][41][56].

## Evolutionary Conservation and Functional Specialization of Spt16p Across Eukaryotes

The high degree of evolutionary conservation of Spt16p and the FACT complex across eukaryotic organisms, from unicellular yeasts to plants and animals, indicates the fundamental importance of this complex for eukaryotic chromatin regulation[10][17][20]. However, the dependence of eukaryotic cells on FACT function varies considerably, with budding yeast requiring FACT for viability, some mammalian cell types being able to proliferate in the absence of FACT, while other specialized cell types exhibit absolute dependence on FACT[14][17][20]. In C. elegans, two genes encode SSRP1 proteins (hmg-3 and hmg-4), which exhibit functional redundancy for maternally-provided embryonic functions but are each uniquely required zygotically for germline development, demonstrating how FACT gene duplications can lead to specialized functions in multicellular organisms[20]. In plants, primarily the role of FACT in RNA polymerase II transcription has been examined, with Arabidopsis plants depleted in FACT subunits exhibiting various defects in vegetative and reproductive development[10].

The existence of SSRP1-independent functions of FACT has been suggested through cellular and genomic studies, particularly in mammalian cells where SSRP1 homodimerization may enable SPT16-independent functions[43]. SSRP1 knockdown and SPT16 knockdown experiments in human nonsmall cell lung carcinoma cells revealed overlapping but distinct sets of genes regulated by the two proteins, suggesting that SSRP1 may regulate transcription independently of SPT16 under certain conditions[43]. The conditions under which SSRP1 homodimerization occurs and its functional consequences remain to be fully elucidated, but the concentration-dependent nature of SSRP1 oligomerization suggests that SSRP1 levels, regulated through the mRNA-dependent mechanism described above, may control the balance between FACT heterodimer formation and SSRP1 homodimer formation, thereby tuning the spectrum of FACT-dependent and SSRP1-independent functions[43].

## Role of Spt16p in Controlling Gene Expression and Chromatin Repression

Beyond its direct effects on nucleosome dynamics during transcription elongation, Spt16p and FACT play important roles in controlling which genes are expressed and which remain repressed, through maintenance of proper chromatin structure that prevents aberrant transcription initiation. FACT has been demonstrated to have a global role in maintaining chromatin in a form that blocks inappropriate transcription initiation, as inactivation of FACT results in derepression of transposon-associated promoters and aberrant transcription from cryptic promoters within gene bodies[9][32][35]. Particularly intriguing is the discovery that in embryonic stem cells, FACT represses retrotransposon MERVL and endogenous retroviruses through a mechanism involving cooperation with the deubiquitinase Usp7, which deubiquitinates H2B ubiquitination (H2Bub) at affected loci, thereby repressing expression of retrotransposon-fused genes and preventing inappropriate activation of the 2-cell-like fate[32]. This suggests that FACT works in concert with epigenetic regulators to maintain proper chromatin states and prevent unwanted transcriptional activation from normally silenced loci.

The role of Spt16p in transcriptional repression appears to extend to its participation in maintaining heterochromatic states and suppressing expression from subtelomeric regions and other normally silent loci[50]. This protective chromatin function of Spt16p is thought to operate through its ability to ensure proper nucleosome occupancy and positioning, thereby physically occluding access to cryptic promoters and maintaining heterochromatic structures[50]. Experimental evidence shows that disruption of FACT function compromises nucleosome occupancy over extended regions, allowing improper transcriptional initiation from sites that are normally nucleosome-covered[50]. The massive loss of nucleosomes upon FACT inactivation suggests that Spt16p's histone chaperone activity in promoting nucleosome reassembly and stabilization may be more fundamental to its function than its role in nucleosome disruption, supporting a model wherein the primary function of Spt16p is to serve as a guardian of chromatin integrity[17][41].

## Conclusion and Perspectives on Spt16p Function

The SPT16 gene encodes a multifunctional histone chaperone protein that occupies a central position in eukaryotic chromatin biology, orchestrating nucleosome dynamics across transcription, DNA replication, DNA repair, and gene silencing processes[1][2][4][10][11][14][17][50]. Through its tripartite domain architecture comprising the N-terminal histone-binding module, the middle domain's double pleckstrin homology structure, and the C-terminal acidic region, Spt16p achieves remarkable functional versatility in engaging with nucleosomal histones and DNA[3][15][18][24][31][40][56]. The protein's essential function in budding yeast is underscored by the profound effects observed upon its inactivation, including collapse of chromatin structure, aberrant transcription initiation, and replication defects[14][17][50]. Yet paradoxically, the dependence on FACT varies dramatically across eukaryotic cell types, with differentiated mammalian cells able to survive without FACT while pluripotent stem cells and cancer cells show elevated FACT expression, suggesting highly specialized roles for the complex in controlling cell identity and proliferation[38][51][54].

Recent discoveries have substantially refined understanding of Spt16p's mechanisms of action, moving beyond the original model of FACT as simply a factor that disrupts nucleosomes to facilitate polymerase passage. The sophisticated roles of Spt16p in chromatin reassembly, maintenance of histone modification patterns, suppression of cryptic transcription initiation, recycling of parental histones during replication, and cooperation with DNA repair machinery reveal a protein that functions as a comprehensive guardian and manager of chromatin integrity across diverse cellular processes[13][14][17][21][26][27][50][56]. The identification of post-translational modifications regulating Spt16p activity, the characterization of sophisticated protein-protein interactions linking Spt16p to numerous chromatin regulatory complexes, and the emerging evidence for context-dependent and cell-type-specific functions of Spt16p point toward an even more nuanced understanding of FACT biology in the future[30][38][43][51][60].

The ability of Spt16p to be regulated at multiple levels—through mRNA-dependent protein stability, proteasomal degradation, phosphorylation by kinases, and cooperation with distinct partner proteins—enables cells to precisely tune FACT activity in response to developmental cues and cellular stress conditions. The emerging link between FACT dysfunction and cancer, wherein FACT levels are frequently elevated and its proteasomal degradation is impaired, suggests that targeting FACT regulation could represent a promising avenue for cancer therapy[30][38][51]. Furthermore, the conservation of Spt16p function from yeast to humans indicates that mechanistic insights gained from studies in budding yeast remain highly relevant to understanding human chromatin biology and disease processes. The continued investigation of Spt16p function through structural, biochemical, genetic, and cell biological approaches promises to reveal additional layers of regulation and specialization, further illuminating how cells control access to their genetic information and maintain proper gene expression patterns across diverse biological contexts.

## Citations

1. https://www.yeastgenome.org/locus/S000003175
2. https://pubmed.ncbi.nlm.nih.gov/8246972/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC3624403/
4. https://www.uniprot.org/uniprotkb/P32558/entry
5. https://www.yeastgenome.org/locus/S000003175/protein
6. https://onlinelibrary.wiley.com/doi/full/10.1107/S2053230X15024565
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC6238592/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC125512/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC262413/
10. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2020.00085/full
11. http://flybase.org/reports/FBgg0000282.htm
12. https://www.science.org/doi/10.1126/science.abp9466
13. https://academic.oup.com/nar/article/48/21/11929/5940495
14. https://www.pnas.org/doi/10.1073/pnas.0712293105
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC9807050/
16. https://www.tandfonline.com/doi/full/10.1080/21541264.2022.2069995
17. https://pubmed.ncbi.nlm.nih.gov/18579787/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC2013732/
19. https://pubmed.ncbi.nlm.nih.gov/30336114/
20. https://academic.oup.com/nar/article/51/21/11549/7321068
21. https://academic.oup.com/g3journal/article/3/6/929/6026130
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC1636840/
23. https://www.ebi.ac.uk/interpro/entry/IPR033825
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC4965029/
25. https://www.tandfonline.com/doi/full/10.1080/10985549.2025.2501630
26. https://www.uniprot.org/uniprotkb/Q920B9/entry
27. https://pubmed.ncbi.nlm.nih.gov/34847380/
28. https://pubmed.ncbi.nlm.nih.gov/33526453/
29. https://academic.oup.com/nar/article/48/18/10211/5902438
30. https://www.tandfonline.com/doi/full/10.1080/15592294.2022.2121073
31. https://academic.oup.com/g3journal/article/2/5/555/5986896
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC9665134/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC3841321/
34. https://pubs.acs.org/doi/10.1021/cr500350x
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC3362939/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC4375056/
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC6028955/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC11912937/
39. https://academic.oup.com/nar/article/32/19/5894/1244327
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC3162410/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC4911930/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC8088127/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC3099653/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC4914445/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC6486547/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC2099615/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC9122599/