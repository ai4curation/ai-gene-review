---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-31T20:00:04.308768'
end_time: '2025-12-31T20:02:24.612190'
duration_seconds: 140.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: RTT109
  gene_symbol: RTT109
  uniprot_accession: Q07794
  protein_description: 'RecName: Full=Histone acetyltransferase RTT109; EC=2.3.1.48
    {ECO:0000269|PubMed:17272722, ECO:0000269|PubMed:17369253, ECO:0000269|PubMed:17690098,
    ECO:0000269|PubMed:18707894, ECO:0000269|PubMed:21256037, ECO:0000269|PubMed:29300933,
    ECO:0000269|PubMed:31194870}; AltName: Full=Regulator of Ty1 transposition protein
    109;'
  gene_info: Name=RTT109 {ECO:0000303|PubMed:17046836}; Synonyms=KAT11 {ECO:0000303|PubMed:18568037},
    KIM2, REM50; OrderedLocusNames=YLL002W; ORFNames=L1377;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the RTT109 family. .
  protein_domains: HAT_RTT109-like. (IPR051236); Histone_AcTrfase_Rtt109/CBP. (IPR013178);
    Rtt109. (IPR016849); HAT_KAT11 (PF08214)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 41
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q07794
- **Protein Description:** RecName: Full=Histone acetyltransferase RTT109; EC=2.3.1.48 {ECO:0000269|PubMed:17272722, ECO:0000269|PubMed:17369253, ECO:0000269|PubMed:17690098, ECO:0000269|PubMed:18707894, ECO:0000269|PubMed:21256037, ECO:0000269|PubMed:29300933, ECO:0000269|PubMed:31194870}; AltName: Full=Regulator of Ty1 transposition protein 109;
- **Gene Information:** Name=RTT109 {ECO:0000303|PubMed:17046836}; Synonyms=KAT11 {ECO:0000303|PubMed:18568037}, KIM2, REM50; OrderedLocusNames=YLL002W; ORFNames=L1377;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the RTT109 family. .
- **Key Domains:** HAT_RTT109-like. (IPR051236); Histone_AcTrfase_Rtt109/CBP. (IPR013178); Rtt109. (IPR016849); HAT_KAT11 (PF08214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RTT109" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RTT109' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RTT109** (gene ID: RTT109, UniProt: Q07794) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze this query carefully. The user is asking me to write a comprehensive research report on the gene RTT109 from Saccharomyces cerevisiae (UniProt Q07794). The user has provided verification steps and context about gene/protein identity.

Let me first verify:
1. Gene symbol: RTT109 (Regulator of Ty1 transposition protein 109) - also known as KAT11 (Histone acetyltransferase 11)
2. Organism: Saccharomyces cerevisiae (Baker's yeast)
3. EC number: 2.3.1.48 (acetyltransferase activity)
4. Protein family: RTT109 family, HAT (Histone Acetyltransferase)

From the search results provided, I can see extensive literature on RTT109 from S. cerevisiae. The search results discuss:
- Substrate specificity (H3K56, H3K9, H3K27 acetylation)
- Interaction with histone chaperones (Vps75, Asf1)
- Role in replication-coupled nucleosome assembly
- Role in DNA damage response
- Structural features and catalytic mechanism
- Functions in R-loop homeostasis
- Pathogenicity implications (Candida)

I have enough information to write a comprehensive 10,000+ word report on RTT109.

My plan:
1. Introduction and overview of RTT109
2. Enzymatic function and substrate specificity
3. Histone chaperone interactions and activation mechanisms
4. Cellular localization and nuclear import
5. Role in replication-coupled nucleosome assembly
6. Function in DNA damage response and genome stability
7. Role in R-loop homeostasis and DNA-RNA hybrid regulation
8. Transcriptional regulation and gene expression
9. Structural insights and catalytic mechanism
10. Cell cycle regulation and deacetylation


11. Evolutionary conservation and fungal-specific roles
12. Pathogenicity and therapeutic implications
13. Conclusion and future perspectives

I'll structure this into major sections and write a comprehensive narrative report following all the formatting guidelines.
</think>

# Histone Acetyltransferase Rtt109: Molecular Structure, Biochemical Function, and Cellular Roles in Saccharomyces cerevisiae

## Summary of Key Findings

Rtt109 (Regulator of Ty1 transposition protein 109), also designated KAT11 (histone acetyltransferase 11), is a fungal-specific histone acetyltransferase that catalyzes the acetylation of multiple lysine residues on histone H3, primarily targeting lysines 56, 9, and 27.[1][12] This enzyme functions as a critical regulator of DNA replication and genome stability through its unique dependence on histone chaperone cofactors, either Vps75 or Asf1, which activate its catalytic activity approximately 100-fold.[1][12] Rtt109 catalyzes the acetylation of newly synthesized histone H3 prior to its incorporation into chromatin, marking nascent DNA and facilitating nucleosome assembly while simultaneously stabilizing replication forks and promoting DNA damage recovery.[3][7][10] The enzyme exhibits a sophisticated activation mechanism wherein Vps75 and Asf1 function through distinct molecular pathways to direct substrate specificity, with Rtt109-Asf1 complexes specifically acetylating H3K56 while Rtt109-Vps75 complexes primarily acetylate H3K9 and H3K27.[1][3] Beyond its canonical role in nucleosome assembly, Rtt109 prevents DNA-RNA hybrid accumulation by acetylating H3K14 and H3K23, thereby maintaining genome stability in the face of R-loop formation.[2] The protein undergoes essential autoacetylation at lysine 290, which stabilizes the interaction between its protein acetyltransferase domain and activation domain, establishing a regulatory mechanism that links cellular acetyl-CoA availability to catalytic activity.[31] Given its critical importance for fungal pathogenesis and its divergence from metazoan acetyltransferases, Rtt109 represents both a fascinating model for understanding histone modifications in replication and an attractive therapeutic target for antifungal intervention.

## Molecular Identity and Structural Architecture of Rtt109

Rtt109 represents a fungal-specific histone acetyltransferase that operates as an independent enzyme within the broader family of histone-modifying enzymes.[37] Originally identified through genetic screening for regulators of Ty1 transposition in Saccharomyces cerevisiae, this protein has attracted considerable research attention due to its unique structural features and functional requirements.[54] The enzyme exhibits a distinctive bipartite architecture comprising a protein acetyltransferase (PAT) domain and an internal activation domain connected by flexible linker regions.[31] The PAT domain adopts a structure substantially similar to the catalytic domain of the metazoan p300/CBP acetyltransferase, despite the absence of overall sequence conservation, indicating potential functional convergence among distantly related acetyltransferases.[31][33] This structural homology to p300/CBP is particularly notable given that both enzymes regulate histone acetylation at lysine 56 of histone H3, suggesting an evolutionary relationship between fungal and metazoan pathways of H3K56 acetylation despite their temporal separation and divergent protein sequences.[33][43]

The protein acetyltransferase domain of Rtt109 measures approximately 60 Å × 40 Å × 40 Å and comprises a central, nearly flat, extensive β-sheet constructed of eight β-strands forming a rectangular plate surrounded by eight α-helices and five extensive surface loops.[31] This domain architecture creates the catalytic center of the enzyme, where acetyl-CoA binds within a binding site positioned such that both ends of the cofactor remain exposed from the PAT domain.[31] The acetyl head group of acetyl-CoA is located at the base of an approximately 7-Å-deep water-filled hydrophobic tunnel that terminates in a small circular opening on the enzyme surface.[31] This tunnel appears critical for substrate positioning and catalysis, as evidenced by mutagenesis studies revealing that alterations to residues lining this tunnel substantially impair acetyl transfer rates.[31] The activation domain of Rtt109 comprises approximately 45 residues that fold into three α-helices arranged as a small α-helical bundle, creating a structure that remains tethered to the core PAT domain through 19-residue and 8-residue connector segments.[31]

A particularly striking feature of the Rtt109 structure involves the presence of an acetylated lysine residue at position 290 (K290) located within the activation domain, positioned at the center of a hydrophobic cage formed by surfaces of both the PAT and activation domains.[31] This autoacetylated lysine serves a regulatory rather than catalytic function, maintaining the tight association between the activation domain and the PAT domain.[31] The attachment of the activation domain through autoacetylation at K290 represents a unique regulatory mechanism, as in most other acetyltransferases the interaction interface between catalytic and regulatory domains is composed exclusively of hydrophobic residues, whereas in Rtt109 this interface critically incorporates the acetylated lysine residue.[31] This structural innovation suggests that Rtt109 exists in at least two functional states: an inactive state in which the activation domain remains disengaged from the PAT domain, and an active state in which autoacetylation at K290 facilitates engagement of the activation domain with the PAT domain core.[31]

## Enzymatic Function and Substrate Specificity

Rtt109 functions as a histone lysine acetyltransferase catalyzing the transfer of an acetyl moiety from acetyl-CoA to the ε-amino group of specific lysine residues on histone H3.[1][12] The enzyme exhibits multisite substrate recognition, with distinct acetylation targets dependent on the histone chaperone cofactor directing the catalytic activity.[1][12][37] Historically, Rtt109 was identified primarily as an acetyltransferase specific for histone H3 lysine 56 (H3K56), but subsequent biochemical and genetic studies have established that H3K9 and H3K27 represent bona fide Rtt109 substrates, with more recent evidence identifying H3K14 and H3K23 as additional acetylation targets under specific cellular conditions.[1][2][12][37] The residues K9 and K27, located within the disordered tail region of histone H3, are acetylated by multiple acetyltransferases including both Rtt109 and Gcn5 (KAT2), which initially obscured the Rtt109-dependent acetylation of these residues.[1][37] However, comprehensive analysis using both western blotting and mass spectrometry techniques has definitively established Rtt109 as responsible for a significant fraction of K9 and K27 acetylation, particularly in the replication-coupled nucleosome assembly pathway.[1][37] By contrast, H3K56 is positioned within the histone-fold domain of H3, and Rtt109 functions as the sole enzymatic source of H3K56 acetylation on newly synthesized histones in budding yeast.[1][6][27]

The specificity of Rtt109 for distinct lysine residues depends critically on which histone chaperone cofactor activates the enzyme.[1][3][12] When associated with the histone chaperone Asf1, Rtt109 specifically acetylates H3K56 in the context of H3-H4 histone pairs, with K56 acetylation being the predominant modification under these conditions.[1][3][12] In contrast, when Rtt109 associates with the histone chaperone Vps75, the acetyltransferase complex preferentially acetylates the N-terminal tail residues of histone H3, with H3K9 acetylation occurring with 100% efficiency under steady-state conditions, H3K23 acetylation at approximately 82% efficiency, H3K27 acetylation at approximately 31% efficiency, and H3K56 acetylation at 100% efficiency when free H3 or H3-H4 dimer substrates are employed.[29][37] This differential substrate utilization reflects distinct molecular mechanisms of Rtt109 activation employed by each chaperone. Experimental deletion of Asf1 abolishes H3K56 acetylation, slightly reduces H3K9 acetylation, and maintains H3K27 acetylation, whereas deletion of Vps75 maintains H3K56 acetylation but substantially reduces both H3K9 and H3K27 acetylation.[1][12][37] These phenotypes indicate a complex division of labor between the two chaperones in directing Rtt109 substrate selectivity.

An important constraint on Rtt109 substrate specificity involves the accessibility of histone lysine residues within nucleosomal contexts. Notably, Rtt109 cannot acetylate H3K56 on histone H3 that is already incorporated as a constituent of nucleosomes, as K56 remains buried within the histone-fold domain when positioned within the nucleosomal structure.[1][37] This restriction establishes that Rtt109 functions exclusively on newly synthesized, non-nucleosomal histone H3, either as free protein or as part of H3-H4 dimers or tetramers in association with chaperone proteins.[1][37] This nucleosome-independence represents a critical feature distinguishing Rtt109 from many other histone acetyltransferases and ensures that the enzyme specifically marks newly replicated DNA through H3K56 acetylation of nascent histones prior to nucleosome assembly.

## Histone Chaperone Cofactors and Activation Mechanisms

Among all characterized histone acetyltransferases, Rtt109 occupies a unique position in requiring histone chaperone cofactors for efficient catalytic activity, a property shared with only Hat1 among yeast acetyltransferases and with human p300/CBP complexes that associate with histone chaperones in some contexts.[1][3][21] Rtt109 purifies from yeast cells in physical complex with two distinct histone chaperones—Vps75 and Asf1—which independently stimulate the acetyltransferase activity of Rtt109 by approximately 100-fold or greater.[1][3][9][12] Despite their shared ability to activate Rtt109, Vps75 and Asf1 represent structurally unrelated proteins that function through distinct molecular mechanisms to enhance catalysis. Vps75 belongs to the nucleosome assembly protein (NAP) family of histone chaperones and forms a characteristic "headphone" architecture with homodimeric organization featuring extended helical dimerization domains and earmuff domains at opposite ends.[9] In contrast, Asf1 represents a distinct histone chaperone family with a fundamentally different fold that nonetheless shares the ability to bind and present histone H3-H4 to acetyltransferases.[1][9]

The interaction between Rtt109 and Vps75 characteristically involves a tight, high-affinity complex formation with dissociation constants in the nanomolar range, whereas the interaction between Rtt109 and Asf1 remains substantially more transient and lower affinity.[1][21][52] This distinction is particularly notable in that Vps75 co-purifies with Rtt109 from yeast and bacteria, and biochemical studies utilizing varying Vps75 concentrations demonstrate saturation of Rtt109 catalytic efficiency at approximately equimolar concentrations of the complex.[1][21][52] Conversely, Asf1 interacts transiently with Rtt109, likely facilitating substrate presentation rather than forming a stable complex.[1][12][21] The structural basis for Rtt109-Vps75 interaction involves multiple contact surfaces on the earmuff domain of Vps75, with a stoichiometry that remains somewhat uncertain, ranging from either one Rtt109 molecule per Vps75 homodimer or one Rtt109 molecule per Vps75 monomer depending on the specific structural determination.[1][20][27][37]

The mechanism by which Vps75 stimulates Rtt109 catalytic activity has been extensively characterized through steady-state kinetic analyses using hydrogen-labeled substrates and purified recombinant proteins.[3][29] These analyses reveal that Vps75 activation of Rtt109 operates through enhanced acetyl transfer rates (increased kcat) rather than through altered substrate binding affinity (no significant change in Km).[3][29] This enhancement of catalytic turnover occurs through stabilization of the active enzyme conformation, whereby the bound Vps75 chaperone induces critical structural rearrangements in Rtt109 that position catalytic residues and substrate for optimal reaction progression.[3][29] Within the structure of the Rtt109-Vps75 complex, specific electrostatic contact surfaces have been identified as critical for catalytic activation, with residues R173 and K177 from the Vps75 earmuff domain predicted to interact with E374 and E378 on helix α9 of Rtt109 and with E299, E300, and D301 on helix α6.[3] Mutagenesis studies targeting these electrostatic interfaces reveal that disruption of these contacts specifically impairs Vps75-dependent acetylation without affecting Asf1-dependent H3K56 acetylation, demonstrating that the two chaperones contact Rtt109 through distinct surfaces and mechanisms.[3][29]

By contrast, Asf1 stimulates Rtt109 through a fundamentally different mechanism that remains incompletely understood but appears to involve direct stabilization of Rtt109 in its active conformational state.[1][12][20] Crystal structure determination of the Rtt109-Asf1-H3-H4-CoA complex has revealed that Asf1-dependent H3K56 acetylation requires unwinding of the histone H3 α-helix in the region where K56 is normally located, combined with stabilization of the very C-terminal β strand of histone H4 by Asf1.[20] Unexpectedly, this crystallographic analysis also revealed that an interaction between Rtt109 and the central helix of histone H3 is required for H3K56 acetylation, suggesting multiprotein, multisite substrate recognition that extends beyond simple substrate presentation.[20] The structural evidence supports a model wherein Asf1 facilitates proper positioning of nascent histone H3-H4 dimers while Rtt109 catalyzes acetylation, and this coordination between chaperone and acetyltransferase ensures substrate specificity for K56 within the context of nucleosomal histone processing.

A critical feature of the Rtt109-chaperone interaction involves the role of Vps75 in nuclear import and stabilization of Rtt109. The Vps75 protein possesses a nuclear localization sequence that functions in directing Rtt109 into the nucleus, and biochemical and cellular evidence demonstrates that Vps75 critically stabilizes Rtt109 in vivo.[1][16][28][37] Deletion of VPS75 results in dramatic reductions in cellular Rtt109 protein levels, whereas deletion of ASF1 leaves Rtt109 levels largely unchanged, indicating that the two chaperones serve distinct roles beyond simple catalytic stimulation.[1][16][28][52] Furthermore, evidence indicates that Rtt109-Vps75 acetyltransferase activity operates in the cytoplasm, consistent with nascent histone H3 being the substrate, and this cytoplasmic activity represents a critical aspect of the replication-coupled nucleosome assembly pathway wherein newly synthesized histones are acetylated prior to nuclear import as part of Asf1-histone complexes.[1][25][28]

## Cellular Localization and Nuclear Import Mechanisms

Rtt109 functions primarily within the nucleus, where it encounters its histone H3 substrates and coordinates with replication and DNA repair machinery.[1][16][28] However, the pathway by which Rtt109 achieves nuclear localization involves the Vps75 histone chaperone, which possesses a canonical nuclear localization sequence (NLS) critical for directing both Vps75 and associated Rtt109 into the nucleus.[1][25][28] This relationship between Vps75 and Rtt109 nuclear import distinguishes it from many other histone acetyltransferases that possess intrinsic nuclear localization signals. The evidence supporting Vps75-mediated nuclear import of Rtt109 derives from multiple experimental approaches including deletion analysis identifying the Vps75 NLS and biochemical demonstration that Vps75 and Rtt109 physically associate prior to nuclear entry.[1][25] Additionally, cellular fractionation studies and microscopy-based approaches have revealed Rtt109-Vps75 acetyltransferase activity in the cytoplasm, indicating that a portion of H3-H4 acetylation occurs prior to nuclear import.[1][25]

The evidence for cytoplasmic Rtt109-Vps75 acetyltransferase activity aligns with the known biology of histone biogenesis, wherein newly synthesized histone H3 associates with Asf1 chaperone in the cytoplasm before nuclear import.[1][25][27] However, the precise coordination between Rtt109-Vps75 catalytic activity in the cytoplasm and the subsequent Asf1-mediated presentation of H3-H4 for acetylation remains incompletely characterized. It appears that both Rtt109-Vps75 and Rtt109-Asf1 acetylation of nascent H3 may occur, with the Rtt109-Vps75 complex potentially acetylating cytoplasmic histone H3 and the Rtt109-Asf1 complex continuing acetylation in the nucleus or facilitating additional modifications necessary for proper nucleosome assembly. This dual-site acetylation model would explain the redundancy observed between Vps75 and Asf1 in certain cellular contexts while also accounting for their distinct substrate specificities and cellular roles.

## Role in Replication-Coupled Nucleosome Assembly

The paramount function of Rtt109 occurs within the context of DNA replication-coupled nucleosome assembly (RCNA), a fundamental process essential for maintaining genome integrity and propagating epigenetic information.[7][27][32][49] During DNA replication, nucleosomes positioned ahead of replication forks must be disassembled to permit access of replication machinery, and following replication, these nucleosomes must be reassembled onto the newly synthesized DNA strands using combinations of parental and newly synthesized histones.[7][27] By one estimate, cells must generate approximately 30 million nucleosomes per complete genome replication, necessitating a highly orchestrated assembly process coordinated with replication fork progression.[7] Rtt109 plays a seminal role in this process through H3K56 acetylation of newly synthesized histone H3 prior to incorporation into chromatin, thereby marking nascent DNA and facilitating proper nucleosome assembly.

The acetylation of H3K56 on newly synthesized histone H3 represents one of the first post-translational modifications applied to nascent histones, occurring within the cytoplasm as part of histone H3-H4 dimer complexes bound to the Asf1 chaperone.[7][27] This early acetylation enhancement substantially increases the binding affinity of H3K56-acetylated histones for the downstream histone chaperones Rtt106 and chromatin assembly factor 1 (CAF1), thereby facilitating the transfer of H3-H4 dimers from Asf1 to these nucleosome assembly factors.[32][35] CAF1 functions to deposit H3-H4 dimers at the replication fork through a direct interaction with proliferating cell nuclear antigen (PCNA), the processivity factor of DNA polymerase, thereby ensuring that newly replicated DNA is rapidly assembled into nucleosomes.[32][35] The requirement for H3K56 acetylation in this transfer process has been demonstrated through multiple experimental approaches including genetic and biochemical studies showing that defects in H3K56 acetylation substantially impair nucleosome deposition on replicated DNA, resulting in accumulation of recombinogenic DNA damage.

Beyond its role in facilitating nucleosome deposition through enhanced chaperone interactions, H3K56 acetylation appears to alter the physical properties of chromatin structure in ways that promote nucleosome assembly. The chromatin assembled with acetylated H3K56 exhibits a relaxed conformation relative to chromatin with unacetylated H3K56, as evidenced by supercoiling density measurements of circular DNA templates acetylated in vitro and in vivo.[27][38][56] This relaxed chromatin structure may reduce the energetic barriers to nucleosome assembly by minimizing the superhelical tension that would otherwise accumulate as DNA wraps around histones. Furthermore, nucleosomes assembled with acetylated H3K56 demonstrate enhanced stability during replication fork progression, suggesting that H3K56 acetylation may strengthen nucleosome-DNA interactions under the specific conditions of active DNA replication when helical tension accumulates ahead of replication forks.[7][32][49]

Rtt109 and its associated histone chaperones also contribute to nucleosome dynamics specifically at the replication fork. Recent high-resolution studies examining nucleosome occupancy during replication have revealed that Rtt109 executes a dual function: it stabilizes nucleosomes behind the replication fork through H3K56 acetylation, while simultaneously promoting histone H3 replacement ahead of the replication fork through acetylation of N-terminal lysine residues including H3K9.[10] This dual function reflects the actions of the two distinct Rtt109 complexes—Rtt109-Asf1 stabilizing replicated nucleosomes through H3K56 acetylation and Rtt109-Vps75 promoting nucleosome replacement ahead of the fork through H3K9 acetylation.[10] The replacement of nucleosomes ahead of the replication fork appears necessary to overcome the accumulated helical tension that accumulates during fork progression, and acetylation of H3K9 by the Rtt109-Vps75 complex may facilitate this replacement either by promoting nucleosome disassembly or by directing the incorporation of acetylated histones that form more dynamic nucleosomes.[10]

## Participation in DNA Damage Response and Genome Stability

Rtt109 functions as a critical component of the cellular response to DNA damage, particularly S-phase replication-associated lesions that threaten genome integrity.[15][32] Yeast cells deleted for RTT109 display profound hypersensitivity to DNA-damaging agents including methyl methanesulfonate (MMS), a DNA alkylating agent, hydroxyurea (HU), which depletes nucleotide pools and stalls replication forks, and camptothecin (CPT), a topoisomerase poison that generates double-strand breaks.[15][32] The hypersensitivity of rtt109Δ cells specifically manifests during S-phase, as these cells remain relatively resistant to acute ionizing radiation that induces double-strand breaks in G2-phase cells, suggesting that Rtt109 functions specifically in replication-associated DNA damage tolerance rather than general double-strand break repair.[15] This S-phase specific function aligns with the known cell-cycle regulation of Rtt109 expression, with Rtt109 mRNA and protein levels peaking during S-phase coincident with the maximal expression of replication machinery and the elevated H3K56 acetylation that marks nascent DNA.[15][27]

The molecular mechanism by which Rtt109 promotes genome stability during replication involves several distinct pathways. First, H3K56 acetylation facilitates proper nucleosome assembly on newly replicated DNA, and defects in this assembly leave single-stranded DNA regions exposed to damage-causing agents including reactive oxygen species generated during normal cellular metabolism and ionizing radiation.[8][32] Second, H3K56-acetylated nucleosomes assembled through the CAF1-Rtt106 pathway provide enhanced replication fork stability, as the absence of H3K56 acetylation or simultaneous deletion of CAF1 and Rtt106 results in increased homologous recombination events reflecting replication fork collapse.[32] Third, Rtt109-dependent acetylation of histone H3 at multiple residues appears to promote replicative DNA damage repair and tolerance through mechanisms independent of nucleosome assembly factors, likely involving recruitment of specialized DNA repair or checkpoint control proteins to acetylated chromatin regions.[2][32]

This pleiotropic role of Rtt109 in genome stability has been demonstrated through multiple experimental approaches. Cells lacking Rtt109 display spontaneous DNA damage as evidenced by elevated Rad52-YFP foci, a marker of double-strand breaks, occurring at frequencies approximately 3-4 fold higher than wild-type cells, with the majority of these lesions arising during S-phase.[15][58] Moreover, rtt109Δ cells display a high proportion of cells arrested in G2-M phase of the cell cycle due to chronic activation of the DNA damage checkpoint, as evidenced by persistent phosphorylation of the Rad53 checkpoint kinase.[15][58] The spontaneous DNA damage burden in rtt109Δ cells translates to dramatically elevated rates of gross chromosomal rearrangements, approximately 9-fold higher than wild-type, and increased hyper-recombination between tandem direct repeats reflecting the accumulation of recombinogenic DNA damage.[15][58] These cellular phenotypes collectively indicate that Rtt109 and H3K56 acetylation are absolutely essential for maintaining genome stability during DNA replication.

Rtt109 additionally participates in DNA damage repair following the formation of exogenous lesions. Cells lacking H3K56 acetylation exhibit severely compromised chromatin reassembly at sites of double-strand break repair induced by HO endonuclease cleavage, and this defect can be rescued by using acetylation-mimetic H3K56Q mutations.[8][32] This requirement for H3K56 acetylation in break-induced chromatin reassembly indicates that the histone modification functions analogously in both replication-coupled and replication-independent nucleosome assembly contexts, reflecting the fundamental role of this modification in nucleosome reconstitution processes.

## Function in R-Loop Homeostasis and Prevention of DNA-RNA Hybridization

Beyond its canonical role in nucleosome assembly during DNA replication, Rtt109 functions to maintain genomic stability by preventing accumulation of DNA-RNA hybrids and R-loops, which represent DNA double-stranded to single-stranded regions containing RNA-DNA hybrids that form during transcription.[2][5] R-loops occur when nascent RNA transcripts remain hybridized to the template DNA strand rather than fully dissociating, and excessive R-loop accumulation can impede replication fork progression, leading to fork stalling, double-strand break formation, and genome instability.[2][5] Through screening of chromatin modifiers in yeast, researchers identified Rtt109 as a critical component of R-loop homeostasis, with rtt109Δ cells displaying substantially elevated cellular levels of DNA-RNA hybrids at multiple tested loci including PDC1, SPF1, and PDR5.[2]

The mechanism by which Rtt109 prevents DNA-RNA hybridization involves acetylation of histone H3 at lysine residues 14 and 23, distinct from the K56 acetylation associated with nucleosome assembly during replication.[2] Evidence supporting this mechanism derives from genetic and biochemical studies demonstrating that H3K14A and H3K23A mutations phenocopy rtt109Δ in terms of increased DNA-RNA hybrid accumulation, whereas H3K14Q and H3K23Q acetyl-mimetic mutations suppress this accumulation.[2] These findings indicate that a proper acetylation state at H3K14 and H3K23 is maintained by Rtt109-dependent acetylation and is essential for preventing pathological R-loop formation. The proposed mechanism involves altered chromatin structure at acetylated residues that renders chromatin configuration less permissive for R-loop formation or more prone to R-loop resolution, though the precise molecular details remain to be elucidated.

Additionally, Rtt109 functions in the repair of replication-born DNA breaks that arise from R-loop-induced replication fork stalling through a mechanism dependent on H3K14 and H3K56 acetylation.[2] This dual role of Rtt109 in both preventing R-loop formation and facilitating repair of R-loop-associated DNA damage positions it as a central regulator of genomic stability in the context of both transcription-associated and replication-associated processes. This expanded understanding of Rtt109 function reveals that the enzyme coordinates chromatin states to suppress transcription-associated DNA-RNA hybridization while simultaneously preparing chromatin for efficient DNA damage repair when replication forks collide with R-loops.

## Transcriptional Regulation and Gene Expression Control

Beyond its primary role in replication-coupled nucleosome assembly, Rtt109 participates in transcriptional regulation through mechanisms that extend beyond simple histone acetylation-mediated chromatin opening.[14][19][55] Analysis of gene expression changes in rtt109Δ cells reveals complex effects on promoter activity and transcription initiation that involve distinct mechanisms for different gene classes. At the extensively studied ARG1 gene, which encodes an enzyme in the arginine biosynthetic pathway, Rtt109 and its chaperone cofactor Asf1 display context-dependent effects on promoter activity that differ markedly from effects observed at other genes.[14][19][55] Under arginine-replete conditions when ARG1 should be repressed, deletion of RTT109 causes substantial de-repression of ARG1 expression, whereas under inducing conditions when ARG1 should be activated, deletion of RTT109 causes only partial impairment of expression.[14][19][55]

This complex regulation reflects an unprecedented mechanism of transcriptional control involving Rtt109 inhibition of transcriptional activation by Asf1, a mechanism referred to as ANKYR (Asf1 not H3Kac yes Rtt109) that operates independently of Rtt109 acetylation of H3K56.[14][19][55] Chromatin immunoprecipitation and genetic interaction studies support a model wherein promoter-targeted Rtt109 represses ARG1 by silencing a pathway of transcriptional activation that depends on Asf1, suggesting that Rtt109 and Asf1 have dual roles in ARG1 regulation that control transcription intensity at both activated and repressed set points through different mechanisms of functional interplay.[14][19][55] This transcriptional regulatory role of Rtt109 operates independently of cell cycle progression, as G2/M-arrested rtt109Δ cells display higher ARG1 transcription than arrested wild-type cells, indicating that Rtt109 repression of ARG1 involves mechanisms that regulate the transcription process prior to elongation and do not depend on cyclin-dependent kinase activity or S-phase-specific events.

The role of Rtt109 in transcriptional regulation extends to cryptic unstable transcripts (CUTs), a class of noncoding RNAs that are rapidly degraded by the nuclear RNA exosome.[45] Loss of Rtt109 and the associated H3K56 acetylation partially suppress the transcriptional changes observed in cells lacking the exosome subunit Rrp6, with the majority of CUTs showing reduced expression in rtt109Δ rrp6Δ double mutants compared to rrp6Δ single mutants.[45] These findings suggest that Rtt109 contributes to CUT expression through mechanisms that likely involve chromatin state changes at the promoters of these noncoding RNAs, though the precise molecular details remain incompletely understood.

## Autoacetylation and Autoregulation of Rtt109

A distinctive feature of Rtt109 catalytic regulation involves autoacetylation at lysine 290 (K290), an acetylation that functions to regulate the enzymatic activity of Rtt109 itself rather than serving as a mark of the enzyme's catalytic target.[23][26][31] The K290 residue is located within the activation domain of Rtt109, in the center of a hydrophobic cage formed by interactions with the PAT domain, and represents an intra-molecular acetylation target distinct from the histone substrates.[23][26][31] Mutagenesis studies substituting K290 with alanine (K290A), arginine (K290R), glutamate (K290E), or tryptophan (K290W) result in complete loss of DNA damage resistance in vivo and abolish Rtt109 catalytic activity both in vitro and in vivo, demonstrating that K290 autoacetylation is absolutely essential for Rtt109 function.[31]

The essential role of K290 autoacetylation appears to derive from its requirement for stabilizing the interaction between the activation domain and the PAT domain, thereby maintaining the proper three-dimensional architecture required for acetyl-CoA binding and substrate positioning.[31] In contrast to many other acetyltransferases wherein the interface between catalytic and regulatory domains comprises exclusively hydrophobic residues, Rtt109 uniquely requires the acetylated lysine residue at K290 to maintain this critical interface.[31] This design suggests that Rtt109 autoacetylation and catalytic activity may be coupled to cellular acetyl-CoA concentration, as the availability of acetyl-CoA would determine the extent of K290 autoacetylation and thus the proportion of enzymatically active Rtt109 molecules within the cell. This regulatory mechanism provides an elegant linkage between cellular metabolic state and the capacity of cells to acetylate histone H3 during replication, ensuring that nucleosome assembly acetylation marks are applied only when the cell possesses sufficient metabolic resources to support replication.

Importantly, K290 autoacetylation occurs intra-molecularly and is not influenced by the presence of Vps75 chaperone, indicating that Rtt109 catalytic activation occurs through a two-step mechanism: first, autoacetylation at K290 generates the active enzyme conformation independent of chaperone presence, and second, the chaperone-bound form of active Rtt109 exhibits further enhanced catalytic rates through mechanisms involving proper substrate positioning and presentation.[1][23][31] This sequential activation model indicates that Vps75 is involved in histone H3 presentation to Rtt109 rather than in generating the active conformational state of the acetyltransferase itself, reinforcing that Vps75 functions by enhancing the rate of acetyl transfer through substrate-positioning mechanisms rather than by stabilizing enzyme conformation.

## Cell Cycle Regulation and Deacetylation of H3K56

The acetylation of H3K56 by Rtt109 represents a dynamic modification that undergoes sophisticated cell-cycle regulation, with acetylation peaking during S-phase and being removed during G2/M phase through the action of the NAD+-dependent histone deacetylases Hst3 and Hst4.[38][41][56][59] This temporal regulation ensures that H3K56 acetylation marks specifically on newly synthesized, nascent histones that undergo assembly during active DNA replication, and that these acetyl groups are removed after nucleosome assembly is complete and DNA replication concludes.[38][41][56] The precise coordination of acetylation and deacetylation appears critical for proper genome function, as both hypoacetylation of H3K56 (as in rtt109Δ cells) and hyperacetylation (as in hst3Δ hst4Δ cells) result in elevated rates of trinucleotide repeat contractions, indicating that a proper balance of H3K56 acetylation is essential for genome stability.[8][38][41][56]

The deacetylation of H3K56 at the end of S-phase appears to facilitate the transition of cells from a replication-active state to a replication-quiescent state. Hst3 and Hst4 represent sirtuins, NAD+-dependent histone deacetylases also known as silent information regulators, and their expression peaks during G2/M phase in a cell-cycle dependent manner.[38][41][56] The removal of H3K56 acetylation by these deacetylases likely serves to restore nucleosomes to a more condensed, stable chromatin state characteristic of replicated DNA during G2/M phase when active DNA replication has concluded. Furthermore, the deacetylation of H3K56 appears necessary for maintenance of silent chromatin at telomeric and mating-type silent loci, as deletion of both HST3 and HST4 results in hyperacetylation of H3K56 at silent loci and loss of silencing despite continued presence of the Sir repressive complex proteins.[38][41][56] These findings indicate that the H3K56 acetylation/deacetylation cycle serves distinct functions in both replication-coupled nucleosome assembly and in the maintenance of heterochromatic gene silencing.

## Role of Rtt109 in Telomere Positioning and Subnuclear Organization

A specialized function of Rtt109 and H3K56 acetylation involves the proper subnuclear positioning of telomeres at the nuclear periphery, a process essential for maintaining yeast telomeric silencing and telomere stability.[13] Rtt109 and its chaperone cofactors Asf1 and Vps75 are required for correct perinuclear localization of telomeres during both G1 and S phases of the cell cycle, as demonstrated through chromosome immunostaining and chromosome dot visualization assays.[13] Deletion of RTT109 results in loss of perinuclear telomere localization with telomeres distributing randomly throughout the nuclear space, and this telomere localization defect correlates with defects in telomeric heterochromatin silencing and proper telomere function.[13]

The role of H3K56 acetylation itself in telomere positioning appears specific, as neither the simple presence of acetylated H3K56 nor the presence of unacetylated H3K56 fully explains the positioning effect; rather, the acetylation/deacetylation cycle at H3K56 appears necessary.[13] This conclusion derives from observations that both H3K56Q (acetyl-mimetic) and H3K56R (non-acetylatable) mutations result in telomere localization defects, indicating that the dynamic cycling of acetylation and deacetylation at this residue represents an essential aspect of telomere positioning regulation.[13] The molecular mechanism by which H3K56 acetylation influences telomere subnuclear localization remains incompletely understood but likely involves recruitment of positioning factors or alter chromatin interactions that facilitate anchoring of telomeres at the nuclear envelope through interactions with nuclear pore complexes and associated proteins.

## Structural Evolutionary Relationships with Metazoan Acetyltransferases

The discovery of substantial structural homology between Rtt109 and the metazoan p300/CBP acetyltransferase family despite profound sequence divergence has provided important insights into the conservation of histone acetyltransferase mechanisms across eukaryotic kingdoms.[31][33][43][46] Both Rtt109 and p300/CBP catalyze acetylation of H3K56, an observation particularly noteworthy given the temporal and evolutionary distance separating fungi and higher animals and the divergence of protein sequences encoding these enzymes.[33][43] The structural conservation of the catalytic domain architecture suggests functional convergence, wherein different protein sequences evolved to achieve similar active site geometries and catalytic mechanisms.[33][43] However, Rtt109 exhibits important functional divergence from p300/CBP, most notably its requirement for histone chaperone cofactors for efficient catalysis and its fungal-specific nature without direct orthologues in higher eukaryotes.[1][6][37][43]

The evolutionary history of Rtt109-like proteins appears restricted to fungal organisms, with the enzyme absent from higher eukaryotes that instead rely on p300/CBP complexes for H3K56 acetylation.[18][44] This fungal specificity has prompted investigation of Rtt109 as a potential therapeutic target for antifungal intervention, particularly given the organism-restricted distribution and the demonstrated importance for fungal pathogenesis. In the pathogenic fungus Candida albicans, Rtt109 is required for efficient pathogenesis in mice, with rtt109−/− mutant cells displaying severely reduced virulence and substantially diminished capability to survive in the immune system of infected hosts.[18][44] This therapeutic potential reflects both the essential nature of Rtt109 for fungal survival and the divergence of the fungal enzyme from metazoan acetyltransferases, suggesting that selective inhibition of Rtt109 might be achievable without disrupting human histone acetylation pathways.

## Pathogenic Functions and Therapeutic Implications

Investigation of Rtt109 function in the pathogenic fungus Candida albicans has revealed critical roles for this acetyltransferase in fungal virulence and survival within mammalian hosts.[18][44] Candida albicans rtt109−/− mutant cells display constitutively elevated DNA repair gene expression and increased H2A serine 129 phosphorylation, indicators of endogenous DNA damage burden, and manifest hypersensitivity to genotoxic stress agents including MMS and CPT.[18][44] Most significantly, rtt109−/− mutant C. albicans strains are substantially less pathogenic in mouse infection models and display markedly increased susceptibility to killing by macrophages in vitro compared to wild-type cells.[18][44]

The reduced pathogenicity of rtt109−/− mutant cells appears attributable to heightened sensitivity to reactive oxygen species (ROS) generated within macrophage phagosomes.[18][44] Wild-type C. albicans cells can survive the ROS-mediated DNA damage that occurs within the phagocytic environment through efficient DNA repair processes dependent on Rtt109 and H3K56 acetylation.[18][44] In contrast, rtt109−/− mutant cells display enhanced susceptibility to macrophage-generated ROS, as evidenced by experiments wherein pharmacological inhibition of the NADPH oxidase enzyme responsible for ROS generation restores rtt109−/− cell survival to wild-type levels.[18][44] This finding indicates that the primary mechanism by which Rtt109 contributes to C. albicans pathogenesis involves enabling survival of the genotoxic stress encountered within the infected host.

Given the essential role of Rtt109 for fungal survival in hostile host environments and the fungal specificity of this acetyltransferase, Rtt109 has been proposed as an attractive candidate for therapeutic antifungal intervention.[18][44] Selective inhibition of Rtt109 would target fungal pathogen growth without directly affecting human histone acetylation, as humans lack Rtt109 orthologues and instead utilize structurally distinct p300/CBP complexes for H3K56 acetylation.[18][44] This selective targeting potential contrasts with many current antifungal strategies that target cellular processes conserved between fungi and humans, thereby creating substantial risk of human toxicity.[18][44] The development of specific Rtt109 inhibitors represents a promising avenue for future antifungal drug development.

## Regulation of Gene Expression During DNA Replication

A particularly well-characterized aspect of Rtt109 function involves its role in buffering gene expression during DNA replication to maintain expression homeostasis despite doubling of genomic DNA content.[59] In cells lacking Rtt109 or unable to acetylate H3K56, mRNA synthesis of early-replicating genes increases to the same extent as the increase in their DNA content, indicating loss of transcriptional buffering.[59] In contrast, wild-type cells exhibit disproportionately lower increase in mRNA levels compared to DNA content increase, suggesting active suppression of transcription at newly replicated loci through Rtt109-dependent H3K56 acetylation.[59] This buffering function appears specific to S-phase, reflecting the temporal window during which H3K56 acetylation is most prominent on the genome. The molecular mechanism appears to involve Rtt109-dependent H3K56 acetylation recruiting specific assembly factors that promote nucleosome formation on newly replicated DNA, thereby creating a more closed chromatin structure that suppresses transcription initiation.[59]

This role in transcriptional buffering during replication provides an important additional function for Rtt109 beyond its canonical role in nucleosome assembly itself, highlighting the multiple layers of biological process coordination achieved through H3K56 acetylation.[59] By suppressing transcription from newly replicated DNA during S-phase and then restoring transcription after deacetylation by Hst3/Hst4 at the conclusion of S-phase, cells maintain relatively constant expression levels throughout the cell cycle despite the dramatic changes in DNA content and chromatin state that accompany DNA replication.[59]

## Molecular Basis for Catalysis and Active Site Architecture

The catalytic mechanism of Rtt109 involves transfer of the acetyl group from acetyl-CoA to the ε-amino group of the target lysine residue on histone H3, a reaction catalyzed through an active site positioned within the PAT domain at the terminus of the approximately 7-Å-deep hydrophobic tunnel described earlier.[31] The precise identity of the catalytic base residue that accepts a proton from the histone lysine side chain during acetyl transfer has been debated, with evidence supporting roles for either aspartate 287 (D287) or aspartate 288 (D288) based on structural positioning and mutagenesis studies.[31] Both residues are positioned within proximity to the acetyl-CoA binding site and the predicted substrate binding pocket, and their precise roles in catalysis await further structural and biochemical characterization.

Steady-state kinetic analyses of Rtt109 and Rtt109-Vps75 complexes have identified the rate-limiting step of catalysis as the chemical step of acetyl transfer, with both unactivated Rtt109 and Rtt109-Vps75 displaying linear accumulation of acetylated product over time without detectable lag or burst phases characteristic of some other acetyltransferases.[29] This observation indicates that neither pre-steady-state product release nor enzyme-substrate complex formation contributes significantly to rate limitation, and instead the chemistry of acetyl transfer represents the slowest step of the overall catalytic cycle.[29] The enhanced rates observed for Rtt109-Vps75 complexes compared to Rtt109 alone reflect specifically enhanced rates of acetyl transfer chemistry, consistent with Vps75-induced stabilization of a conformational state of Rtt109 optimally positioned for catalysis.

## Interactions with Other DNA Repair and Chromatin-Associated Proteins

Beyond its direct interactions with histone chaperones, Rtt109 functions within a broader network of proteins involved in DNA repair, nucleosome assembly, and chromatin-based regulation. The histone chaperone Rtt106 represents an important interaction partner of Rtt109-acetylated H3K56, with Rtt106 displaying H3K56ac-specific binding and functioning to deliver H3K56ac histones to sites of DNA synthesis during replication.[32][35] Rtt106 contains two rigid pleckstrin homology (PH) domains that mediate H3K56ac binding and also facilitate interactions with CAF1 and with Sir4 of the silent information regulator complex, indicating that Rtt106 serves as a linking factor connecting replication-coupled nucleosome assembly to transcriptional silencing through H3K56ac recognition.[32][35] The interaction of Rtt106 with Asf1 and with Rtt109 itself suggests that Rtt109-Asf1-H3K56ac complexes transfer histones to Rtt106 for subsequent deposition by CAF1 or for delivery to silent loci for silencing establishment.

Rtt109 additionally interacts with DNA damage checkpoint proteins, including the Rad53 kinase, which phosphorylates Rtt109 and modulates its activity in response to genotoxic stress.[57] The interaction between Rad53 and the histone chaperone Asf1 increases upon DNA damage and appears important for proper DNA damage recovery, with rtt109Δ mutants displaying impaired recovery from DNA damage checkpoint activation even after DNA repair has been completed.[57] These findings suggest that Rtt109 contributes to DNA damage recovery through checkpoint inactivation mechanisms that involve Asf1 interaction and Rad53 dephosphorylation.

## Comparative Analysis with Other Histone Acetyltransferases

Rtt109 represents one of a relatively small number of histone acetyltransferases in budding yeast that catalyze distinct sets of histone acetylation events. In contrast to the broadly active Gcn5 (KAT2) and Esa1 (KAT5) acetyltransferases that acetylate multiple histone lysines at numerous genes, Rtt109 exhibits specialized substrate and temporal specificity, functioning primarily on newly synthesized, non-nucleosomal histones during S-phase.[1][39][42] The division of labor among yeast HATs appears designed to segregate different acetylation events into distinct enzymatic pathways, with Rtt109 controlling replication-associated histone acetylation through its unique dependence on histone chaperones and its S-phase restricted expression.[1][39][42] This functional compartmentalization represents a sophisticated regulatory strategy enabling cells to coordinate multiple distinct acetylation-dependent processes including transcription, DNA repair, and nucleosome assembly through specialized enzymatic machinery.

Unlike the SAGA and NuA4 HAT complexes that function in transcriptional regulation at genes throughout the genome, Rtt109 operates in a replication-synchronized manner, with expression and activity peaking during S-phase. This temporal regulation ensures that the primary function of Rtt109 in marking newly replicated DNA through H3K56 acetylation occurs specifically during the period when DNA replication is occurring and nascent histones are being incorporated into chromatin. Furthermore, the dependence of Rtt109 on histone chaperone cofactors for activation contrasts with many other HATs that function more autonomously, and this chaperone requirement ensures that Rtt109 catalytic activity is coupled to proper histone presentation and substrate availability through the chaperone binding partners.

## Conclusions and Perspectives on Rtt109 Biology

Rtt109 has emerged as a central regulatory enzyme controlling histone acetylation during DNA replication and DNA damage response, with functions extending beyond nucleosome assembly into transcriptional regulation, R-loop homeostasis, and checkpoint control.[1][2][7][27] The sophisticated chaperone-dependent activation mechanism, the essential autoacetylation regulatory system, and the dynamic cell-cycle controlled substrate acetylation and deacetylation reflect the critical importance of proper histone acetylation regulation during the energy-intensive and genome-threatening process of DNA replication. The fungal specificity of Rtt109, combined with its essential role in DNA damage resistance and pathogen survival within host immune systems, positions this acetyltransferase as a promising target for antifungal therapeutic development. Future research should focus on detailed structural characterization of Rtt109 complexes with various substrates and regulatory proteins, investigation of the precise mechanisms by which H3K56 acetylation recruits downstream chromatin-associated proteins, and development of selective inhibitors of Rtt109 catalytic activity suitable for therapeutic use against fungal pathogens. Additionally, further investigation into the relationship between Rtt109 and the metazoan p300/CBP acetyltransferases may reveal conserved mechanistic principles of H3K56 acetylation in eukaryotic cells spanning from simple fungi to complex multicellular organisms.

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC3232334/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC9434296/
3. https://www.pnas.org/doi/10.1073/pnas.1009860107
4. https://www.yeastgenome.org/locus/S000003925
5. https://academic.oup.com/genetics/article-abstract/222/1/iyac108/6648348
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC2574607/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC4415165/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC2847066/
9. https://www.pnas.org/doi/10.1073/pnas.0802393105
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC9248883/
11. https://pubmed.ncbi.nlm.nih.gov/17272723/
12. https://rupress.org/jcb/article/183/4/641/45671/Histone-H3-lysine-56-acetylation-by-Rtt109-is
13. https://www.pnas.org/doi/10.1073/pnas.1111501108
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC3334813/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC3115401/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC4016993/
17. https://www.pnas.org/doi/10.1073/pnas.0912427107
18. https://www.rcsb.org/structure/5zba
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC2680711/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC10219144/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC2527895/
22. https://pubs.acs.org/doi/abs/10.1021/bi100381y
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC3137045/
24. https://onlinelibrary.wiley.com/doi/10.1111/j.1600-0854.2011.01202.x
25. https://pubmed.ncbi.nlm.nih.gov/22023828/
26. https://www.pnas.org/doi/10.1073/pnas.0805813105
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC3213180/
28. https://www.pnas.org/doi/full/10.1073/pnas.1119095109
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC2575165/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC2447148/
31. https://www.molbiolcell.org/doi/10.1091/mbc.e08-05-0524
32. https://journals.asm.org/doi/10.1128/ec.00097-10
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC2824404/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC4662874/
35. https://pubmed.ncbi.nlm.nih.gov/18568037/
36. https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1365-2958.2011.07754.x
37. https://genesdev.cshlp.org/content/early/2021/12/14/gad.348923.121.full.pdf
38. https://academic.oup.com/nar/article/46/5/2279/4781507
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC4888841/
40. https://www.tandfonline.com/doi/full/10.1080/19491034.2016.1216743
41. https://genesdev.cshlp.org/content/22/14/1906.abstract