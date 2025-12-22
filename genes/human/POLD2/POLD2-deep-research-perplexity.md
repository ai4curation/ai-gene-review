---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-12T07:11:19.200165'
end_time: '2025-12-12T07:13:38.083979'
duration_seconds: 138.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: POLD2
  gene_symbol: POLD2
  uniprot_accession: P49005
  protein_description: 'RecName: Full=DNA polymerase delta subunit 2; AltName: Full=DNA
    polymerase delta subunit p50;'
  gene_info: Name=POLD2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the DNA polymerase delta/II small subunit
  protein_domains: DNA_pol_a/d/e_bsu. (IPR007185); DNA_pol_D_N. (IPR040663); DNA_pol_delta/II_ssu.
    (IPR024826); PolD2_C. (IPR041863); DNA_pol_D_N (PF18018)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 54
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P49005
- **Protein Description:** RecName: Full=DNA polymerase delta subunit 2; AltName: Full=DNA polymerase delta subunit p50;
- **Gene Information:** Name=POLD2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the DNA polymerase delta/II small subunit
- **Key Domains:** DNA_pol_a/d/e_bsu. (IPR007185); DNA_pol_D_N. (IPR040663); DNA_pol_delta/II_ssu. (IPR024826); PolD2_C. (IPR041863); DNA_pol_D_N (PF18018)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "POLD2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'POLD2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **POLD2** (gene ID: POLD2, UniProt: P49005) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze the search results to understand the query and verify the gene/protein identity before proceeding.

## VERIFICATION STEPS:

1. **Check gene symbol "POLD2" against UniProt description:**
   - UniProt Accession: P49005
   - Protein Description: DNA polymerase delta subunit 2; AltName: DNA polymerase delta subunit p50
   - Gene: POLD2
   - Organism: Homo sapiens (Human)
   - This matches! The gene POLD2 encodes a protein also known as p50, which is the second subunit of DNA polymerase delta.

2. **Verify organism is correct:** Homo sapiens (Human) ✓

3. **Check if protein family/domains align:**
   - Domains listed: DNA_pol_a/d/e_bsu (IPR007185); DNA_pol_D_N (IPR040663); DNA_pol_delta/II_ssu (IPR024826); PolD2_C (IPR041863); DNA_pol_D_N (PF18018)
   - From search results, I can see extensive literature on POLD2 as a subunit of DNA polymerase delta complex ✓

4. **Check for ambiguity or different genes with same symbol:**
   - Search results consistently refer to POLD2 as the p50 subunit of human DNA polymerase delta
   - All sources are discussing human POLD2 (Homo sapiens)
   - No evidence of ambiguity or different genes with same symbol

The gene is correctly identified. Now I'll organize my research into a comprehensive report structure.

## PLANNING THE REPORT:

Based on the search results, I need to cover:

1. **Gene/Protein Identity and Basic Properties**
   - POLD2 encodes the p50 subunit of human DNA polymerase delta
   - Part of DNA polymerase delta complex (pol δ)
   - Alternatively designated as DNA polymerase delta 2, an accessory subunit within the enzymatic complex

2. **DNA Polymerase Delta Complex Structure and Function**
   - Intricate holoenzyme composed of 4-5 critical subunits
   - POLD2/p50 plays a specialized role in maintaining complex stability
   - Facilitates precise interactions between different subunit components

3. **Molecular Functions**
   - Enables precise DNA synthesis mechanisms
   - Supports critical 3'→5' exonuclease proofreading capabilities
   - Mediates interactions with PCNA through specialized binding domains
   - Manages multiple protein interaction interfaces

4. **Biological Processes**
   - Crucial involvement in DNA replication, particularly lagging strand synthesis
   - Participates in fundamental genomic maintenance mechanisms including DNA repair pathways like base excision repair (BER), nucleotide excision repair (NER), and mismatch repair (MMR)
   - Supports translesion synthesis during challenging replication scenarios
   - Manages Okazaki fragment processing with high precision
   - Assists in parental histone transfer during chromosomal replication

5. **Subcellular Localization**
   - Predominantly localized within nuclear compartments
   - Demonstrates strong chromatin association capabilities

6. **Biochemical and Structural Properties**
   - Subject to complex post-translational modifications including acetylation, phosphorylation, and ubiquitination
   - Engages in sophisticated protein-protein interaction networks
   - Possesses specialized structural domains enabling functional versatility

7. **Clinical Significance**
   - Demonstrates significant associations with cancer development
   - Genetic mutations can trigger critical cellular dysfunction
   - Potential target for therapeutic interventions

8. **Regulation and Degradation**
   - Integral component of cellular DNA damage response mechanisms
   - Involves regulated degradation of p12 subunit
   - Undergoes intricate post-translational regulatory processes
</think>

# POLD2: DNA Polymerase Delta Subunit 2 - A Comprehensive Molecular and Functional Analysis

The **POLD2** gene encodes DNA polymerase delta subunit 2, commonly referred to as the p50 subunit, which serves as a critical accessory component of the mammalian DNA polymerase delta (Pol δ) holoenzyme[1][2]. This comprehensive report examines the structure, biochemical functions, biological roles, regulation, and clinical significance of POLD2 in human cells, with particular emphasis on its essential contributions to genomic DNA replication, DNA repair pathways, and the maintenance of genetic stability. POLD2 functions as a molecular scaffold that coordinates the assembly and activity of the DNA polymerase delta complex, facilitating high-fidelity DNA synthesis during lagging strand replication while simultaneously participating in multiple specialized DNA repair mechanisms including nucleotide excision repair, base excision repair, and translesion synthesis. Beyond its catalytic roles, POLD2 demonstrates emerging functions in epigenetic inheritance through its involvement in parental histone transfer during DNA replication, and dysregulation of POLD2 expression has been associated with multiple cancer types and potential immunotherapy resistance, positioning this protein as both a fundamental replication factor and a potential therapeutic biomarker.

## Structural Architecture and Composition of DNA Polymerase Delta

### The Holoenzyme Complex Organization

The human DNA polymerase delta holoenzyme represents a highly organized macromolecular complex consisting of four catalytic and accessory subunits that work in concert to achieve accurate and processive DNA synthesis[2][3][35]. The holoenzyme traditionally comprises four subunits: p125 (encoded by POLD1, the catalytic subunit), p50 (encoded by POLD2, the second subunit), p68 (encoded by POLD3, the third subunit), and p12 (encoded by POLD4, the smallest subunit)[3][31]. Recent evidence demonstrates that the p12 subunit exists as a dimer in solution and within the holoenzyme, suggesting that the functional human Pol δ complex may exist as a pentameric structure with dimeric p12[32]. This pentameric architecture represents an important refinement in our understanding of Pol δ organization, as earlier studies that characterized the tetrameric form may have underestimated the stoichiometry of the smallest subunit.

The catalytic subunit p125 harbors both the polymerase active site and the 3'→5' exonuclease activity critical for proofreading during DNA synthesis[26][31]. The p125 subunit contains a distinctive "right hand" shaped architecture common to DNA polymerases, with domains that create a cleft between the exonuclease and N-terminal domains that accommodates single-stranded DNA template[31]. The C-terminal domain (CTD) of p125 coordinates a 4Fe-4S cluster through invariant cysteines of the CysB motif, a cofactor that appears critical for maintaining proper enzyme fidelity and function[50][53].

POLD2, encoding the p50 subunit, serves a fundamentally important structural and regulatory role that extends far beyond simple scaffolding[32][33]. The p50 subunit possesses distinct functional domains including a phosphodiesterase-like (PDE) domain at its center, an oligonucleotide binding (OB) fold domain, and regulatory regions that facilitate protein-protein interactions[49][52]. The crystal structure of the p50•p66N complex reveals that these domains create an extended "cashew-shaped" molecule with overall dimensions of approximately 100 × 60 × 50 Ångströms[49][52]. The PDE domain in p50, while structurally reminiscent of phosphodiesterase enzymes, does not appear to possess catalytic activity itself but rather serves as a critical platform for mediating interactions between p50, p125, p68, and p12[49][52].

### POLD2 as a Molecular Scaffold

POLD2 occupies a central organizational role within the Pol δ holoenzyme through its simultaneous interaction with all three other subunits of the complex[32][33]. The p50 subunit serves as a receptor that directly interacts with the catalytic p125 subunit, the regulatory p68 subunit, and the small p12 subunit, essentially functioning as the organizational hub around which the entire complex is assembled[33]. This scaffolding function has been demonstrated through multiple experimental approaches including yeast two-hybrid analysis, co-immunoprecipitation studies, and biochemical reconstitution of Pol δ from recombinant subunits[32][33].

POLD2 depletion results in dramatic destabilization of the entire Pol δ holoenzyme, leading to degradation of both the catalytic p125 subunit and the regulatory p68 subunit[36]. This observation underscores the essential role of POLD2 in maintaining holoenzyme integrity. When POLD2 is depleted through RNA interference or genetic manipulation, the remaining subunits of the complex become susceptible to proteasomal degradation, demonstrating that POLD2 acts as a stabilizing factor essential for the assembly and maintenance of the functional complex[36]. This dependency relationship suggests that POLD2 likely underwent evolutionary selection as a critical checkpoint for ensuring that Pol δ activity is only present when the complete, functional holoenzyme can be assembled.

## Biochemical Functions and Catalytic Properties

### DNA Synthesis Activity and Processivity

DNA polymerase delta catalyzes the synthesis of the vast majority of the eukaryotic genome, specifically mediating lagging strand synthesis during chromosomal DNA replication[31]. The pol δ holoenzyme, with POLD2 as an integral component, exhibits remarkable processivity—the ability to synthesize approximately 200–300 nucleotides without dissociating from the DNA template—a property that is dramatically enhanced by interaction with the processivity factor proliferating cell nuclear antigen (PCNA)[31][35]. This high processivity is essential for the efficiency of lagging strand synthesis, as the polymerase must traverse the length of individual Okazaki fragments, which typically span 1,000–2,000 nucleotides in eukaryotes.

The processivity of Pol δ is mediated through multiple PCNA-interacting protein (PIP) box motifs distributed across the Pol δ subunits[11][14][35]. POLD2/p50 contains one of these critical PIP-box motifs with the sequence \(^{58}\text{LIQMRPFL}^{65}\)[11][14], which binds to the inter-domain-connecting loop (IDCL) of PCNA with relatively modest affinity compared to other PIP-box motifs within the complex[11]. However, the presence of multiple PIP-box motifs across the p125, p50, p68, and p12 subunits creates a multivalent interaction network that collectively stabilizes the Pol δ-PCNA association, with the p125 PIP-box making the most substantial contribution to processivity followed by the p12 PIP-box[35].

Recent cryo-EM structures have revealed that the catalytic p125 subunit binds atop the PCNA ring in an open configuration, with POLD2 and other regulatory subunits positioned laterally[6][35]. This arrangement allows PCNA to thread and stabilize the duplex DNA exiting from the catalytic cleft, with the regulatory subunits projecting away from the DNA synthesis axis. The flexibility of this arrangement appears functionally important, as alternative holoenzyme conformations captured in cryo-EM reconstructions suggest that dynamic interactions between PCNA loops and both the thumb and C-terminal domain of p125 maintain PCNA in a position competent for DNA polymerization[6].

### Exonuclease and Proofreading Functions

The 3'→5' exonuclease activity that imparts proofreading capability to Pol δ resides within the catalytic p125 subunit, not within POLD2 itself[12][31]. However, POLD2 plays an important regulatory role in modulating the efficiency and fidelity of this proofreading activity through its structural organization of the holoenzyme[31]. The exonuclease domain of p125 can remove incorrectly incorporated nucleotides from the 3' end of the growing DNA strand, and this activity is particularly important when Pol δ encounters template damage or when incorrect nucleotides have been incorporated opposite undamaged template bases.

The balance between polymerase and exonuclease activities is critical for maintaining replication fidelity, and recent kinetic analyses demonstrate that removal of the p12 subunit (converting the Pol δ tetramer to a trimer, Pol δ3) dramatically alters this balance[44]. Specifically, deletion of p12 causes approximately a five-fold decrease in the polymerase elongation rate constant (k_pol) and an approximately eight-fold increase in the exonuclease activity constant (k_pol-exo), resulting in roughly a 40-fold increase in the ratio of editing to extension[44]. This suggests that while POLD2 itself does not directly catalyze exonuclease activity, the presence of the complete holoenzyme, including POLD2's interaction with all other subunits, modulates the propensity of the catalytic subunit to engage in proofreading versus continuing DNA synthesis.

### Post-translational Modifications and Enhanced Catalytic Properties

Recent studies have revealed that the p125 catalytic subunit undergoes acetylation at specific lysine residues including K16, K897, and K998 on the PolD1 catalytic subunit, as well as K15 and K25 on the p12 subunit, though acetylation of POLD2 itself has not been definitively demonstrated[3][26]. Notably, acetylation of the Pol δ holoenzyme significantly enhances its catalytic properties[3]. The acetylated form of human Pol δ displays higher polymerization activity compared to the unmodified form of the enzyme, and acetylation enhances the ability of the polymerase to resolve complex secondary structures such as G-quadruplexes that might be present on the template strand[3].

Furthermore, acetylation enhances the strand displacement activity of Pol δ, allowing it to more efficiently displace downstream DNA fragments during processes such as Okazaki fragment maturation[3]. These findings suggest that post-translational modifications of the Pol δ complex, while not directly involving POLD2, may regulate the activity of the holoenzyme in response to cellular conditions or requirements. The acetylation appears to support higher-fidelity DNA replication and enhanced processivity, suggesting that cells may employ histone acetyltransferases or other acetyltransferases to modify Pol δ during specific stages of the cell cycle or in response to replication stress.

## Cellular Localization and DNA Replication Fork Dynamics

### Nuclear Localization and Replication Fork Association

POLD2, as an integral component of the Pol δ holoenzyme, localizes to the nucleus where it participates in DNA replication at replication forks[31][32]. The nuclear localization of Pol δ is critical for its access to chromosomal DNA during S phase of the cell cycle, when the majority of genomic DNA replication occurs. Dynamic imaging studies employing single-molecule tracking (SMT) have revealed that individual Pol δ molecules show highly dynamic binding to nuclear chromatin, with repeated cycles of recruitment, synthesis, and dissociation[58].

Real-time tracking experiments demonstrate that Pol δ molecules arrive at PCNA-loaded replication forks and establish productive complexes through PCNA-mediated interactions[58]. The order of arrival appears important, with approximately 79% of SNAP-tagged Pol δ molecules arriving after PCNA loading at genomic sites[58]. Once bound, Pol δ and PCNA typically colocalize for a median time of approximately 4 seconds before Pol δ dissociates, while PCNA often remains on chromatin for an additional 1–30 seconds[58]. This temporal dynamics suggests that Pol δ exhibits transient productive engagement with PCNA at replication forks before dissociating and being recycled to other replication fork sites.

The loading order of Pol δ and PCNA appears to influence complex stability, with pathways where PCNA loads first showing approximately 1.5–2 fold longer colocalization times compared to pathways where Pol δ precedes PCNA loading[58]. This observation suggests that PCNA loading creates a more favorable conformational context for Pol δ binding and productive DNA synthesis, possibly by virtue of the circular topology of the PCNA clamp properly positioning the DNA duplex for efficient polymerase engagement.

### Dynamics of Pol δ Dissociation and PCNA Recycling

An important finding from dynamic studies is that replication factor C (RFC), the PCNA loader, remains transiently bound to DNA near the loaded PCNA clamp after completion of loading[58]. This proximity allows RFC to re-engage and unload PCNA from the template if Pol δ does not complex with PCNA within an appropriate timeframe[58]. This PCNA recycling mechanism ensures efficient distribution of the limited pool of PCNA sliding clamps across multiple replication fork sites in the genome, as replication must proceed efficiently at multiple loci simultaneously during S phase.

Interestingly, the catalytic activity of Pol δ affects the chromatin binding dynamics of both Pol δ and PCNA[58]. Overexpression of catalytically dead Pol δ leads to increased chromatin residence time of both the inactive polymerase and PCNA during long binding events, suggesting that productive DNA polymerization actively triggers dissociation of the Pol δ-PCNA complex from chromatin[58]. This behavior provides an elegant mechanism for ensuring temporal coupling of polymerase activity: when the polymerase successfully extends the DNA through synthesis, the catalytic activity itself promotes dissociation, allowing the next replication fork site to be addressed.

## DNA Replication and Okazaki Fragment Processing

### Lagging Strand Synthesis and Primase-Polymerase Switching

During lagging strand DNA synthesis, DNA primase (the catalytic subunit of Pol α-primase complex) synthesizes short RNA primers approximately 10 nucleotides in length, which are then extended by DNA polymerase α to approximately 20–22 nucleotides[3]. At this point, a polymerase switching event occurs that is critical for lagging strand synthesis efficiency. Replication factor C recognizes the primer terminus and loads PCNA onto the primed template[3]. This PCNA loading event simultaneously displaces Pol α and recruits Pol δ to continue synthesis.

POLD2, as a component of the Pol δ holoenzyme, participates directly in this polymerase switching by virtue of its role in stabilizing the Pol δ complex and organizing its interaction with PCNA. The p50 subunit's multiple protein-protein interaction surfaces facilitate the proper positioning of the catalytic p125 subunit onto the PCNA clamp, ensuring efficient transfer of synthesis from the departing Pol α to the arriving Pol δ. Once Pol δ takes over, it synthesizes approximately 200–300 nucleotides (the length of an Okazaki fragment) with high processivity and fidelity until it encounters the RNA primer of the previously synthesized Okazaki fragment.

### Strand Displacement and Nick Translation

When the synthesizing Pol δ encounters the 5' end of the downstream Okazaki fragment, an important transition occurs. Pol δ possesses intrinsic strand displacement activity that allows it to synthesize through the downstream double-stranded DNA, displacing the RNA-DNA primer synthesized by Pol α-primase in the process[19][22]. However, this strand displacement is carefully modulated by replication protein A (RPA) and flap endonuclease 1 (FEN1) to prevent the generation of excessively long displaced flaps.

POLD2 contributes to this process indirectly through its role in organizing the Pol δ holoenzyme into its optimal configuration for these specialized synthesis modes. The p50 subunit's interactions with p125 and p68 help establish the structural context in which the polymerase and exonuclease activities are balanced appropriately for flap processing. Pol δ exhibits a unique property termed "idling"—repetitive extension and removal of one nucleotide at a time when pausing at a nick[22]. This idling activity produces small oligonucleotide flaps that can be efficiently cleaved by FEN1, generating ligatable nicks for subsequent sealing by DNA ligase I[22].

### Fidelity Mechanism and Mismatch Detection

The integrated action of Pol δ's polymerase and exonuclease activities, combined with the mismatch repair system, results in remarkably high fidelity DNA replication. The concerted actions of Pol δ on the lagging strand, Pol ε on the leading strand, associated replicative factors, and mismatch repair (MMR) proteins result in a mutation rate of less than one misincorporation per genome per replication cycle[31][37]. This extraordinarily high fidelity protects against genetic defects during development and prevents the initiation of malignancies in somatic cells.

POLD2, through its role in assembling and stabilizing the Pol δ holoenzyme, contributes to this fidelity maintenance. The complete holoenzyme architecture appears to provide a selectivity context that helps the polymerase discriminate between correct and incorrect nucleotides. The p50 subunit's interaction with the OB fold and PDE domains creates structural features that may detect certain types of DNA distortions due to damage or mismatch, potentially facilitating switching of the polymerase from processive replication to specialized activities required for DNA repair.

## DNA Repair Pathways and Damage Tolerance

### Nucleotide Excision Repair (NER)

Nucleotide excision repair represents a primary defense mechanism against bulky DNA lesions that distort the helical structure of the DNA double helix, such as those induced by ultraviolet light or polycyclic aromatic hydrocarbons[24]. The NER pathway divides into two sub-pathways: global genome NER (GG-NER) that scans the entire genome for lesions, and transcription-coupled NER (TC-NER) that specifically addresses lesions encountered by RNA polymerase during transcription[24]. Both pathways employ similar core repair machinery but differ in how damage is recognized and the timing of their activity.

Following recognition of a DNA lesion and unwinding of the double helix around the lesion by the TFIIH complex (creating an open bubble of approximately 25–30 nucleotides), the XPF-ERCC1 complex and XPG endonuclease make coordinated nicks on the 5' and 3' sides of the lesion respectively[24]. This excision removes a fragment typically 24–32 nucleotides in length, leaving a gap in the damaged strand[24]. The final resynthesis step of NER employs DNA polymerase δ, and specifically involves POLD2 as an essential component of the Pol δ holoenzyme[24]. DNA polymerase δ uses the template provided by the single strand to resynthesize the DNA, filling the gap with the correct sequence, after which DNA ligase seals the final nick in the DNA backbone[24].

Studies indicate that DNA polymerase δ carries out approximately half of the nucleotide excision repair synthesis following UV irradiation, sharing this function with DNA polymerase κ[42]. This demonstrates a specialized function of POLD2-containing Pol δ in responding to environmental DNA damage. The requirement for a complete, functional holoenzyme containing POLD2 during NER underscores the importance of high-fidelity synthesis in repair contexts, as errors introduced during repair could fix additional mutations into the genome.

### Base Excision Repair (BER)

Base excision repair corrects those forms of oxidative, deamination, alkylation, and abasic single base damage that do not constitute major distortions to the DNA helix[45]. In the nucleus, this repair process is mainly active in the G1 phase of the cell cycle[45]. Following recognition and excision of a damaged base by a DNA glycosylase, an AP (apurinic/apyrimidinic) endonuclease creates a 3'-OH end at the site of the lesion, generating a gap in the DNA[45].

During long-patch BER, the repair gap left behind from a bifunctional glycosylase is tailored, and DNA polymerase δ or ε synthesize DNA in a strand-displacement manner, which is then followed by flap removal by FEN1 and ligation by DNA ligase I[45]. POLD2, as a component of the replicative Pol δ holoenzyme, participates in this gap-filling synthesis. The ability of Pol δ to perform strand displacement synthesis makes it particularly suited for long-patch BER, as the polymerase can efficiently displace the downstream DNA fragments created during the BER process while synthesizing the corrected sequence.

### Translesion Synthesis and Polymerase Switching

When DNA replication encounters modified bases that block normal DNA synthesis, specialized translesion synthesis (TLS) polymerases can bypass these lesions and allow replication to continue, albeit sometimes at the cost of reduced fidelity[20][23]. The Y-family TLS polymerases (including Pol η, Pol κ, and Pol ι) and the B-family Pol ζ function as inserter and extender polymerases respectively, typically working in sequential pairs to bypass DNA lesions[20][23].

POLD2 plays a crucial role in facilitating the transition between replicative synthesis by Pol δ and TLS by these specialized polymerases. POLD2 interacts with DNA polymerase-interacting protein 2 (PolDIP2, also known as PDIP38), which serves as a processivity factor and coordination protein for TLS polymerases[7]. PolDIP2 can increase the processivity of TLS polymerases Pol λ and Pol η during the bypass of common DNA lesions such as 8-oxo-guanine, abasic sites, and cyclobutane thymine dimers[7]. The p50 subunit of Pol δ appears to coordinate with PolDIP2 to facilitate the switch between replicative and TLS polymerases, enabling error-free TLS in many cases through the sequential action of these polymerases.

Recent evidence indicates that translesion synthesis predominantly occurs behind restarted replication forks in a post-replicational manner, rather than causing immediate stalling and bypass at the lesion site[20]. Following PrimPol-mediated restart of a stalled fork downstream of a DNA adduct, TLS polymerases are recruited to fill single-stranded DNA gaps created by this restart process[20]. This mechanism allows cells to separate the timing of lesion bypass from initial fork stalling, providing an opportunity for more careful regulation of TLS polymerase activity through POLD2-containing Pol δ and its associated factors.

### DNA Polymerase Zeta Complex Assembly

POLD2 serves an additional critical function as a component of the DNA polymerase zeta complex, a specialized translesion synthesis polymerase composed of Rev3L (REV3), Rev7 (REV7), POLD2, and POLD3[42][43]. In this context, POLD2 acts as a regulatory factor that dramatically enhances the activity of the minimal Rev3L-Rev7 two-subunit Pol ζ complex. The four-subunit Pol ζ complex containing POLD2 and POLD3 shows dramatically higher efficiency and processivity in DNA synthesis compared to the minimal two-subunit complex, suggesting that POLD2 acts as a processivity or activity factor for Pol ζ[42][43].

POLD2 in the Pol ζ context likely performs a similar structural and organizational function as it does in Pol δ, potentially helping to coordinate the assembly of the complex and optimize its interaction with PCNA or other replication accessories. The fact that POLD2 functions in both Pol δ and Pol ζ complexes suggests that this p50 subunit has evolved as a general factor for organizing replication and repair polymerase complexes, with the specific functions of each complex determined by the catalytic subunit partner (p125 in Pol δ versus Rev3L in Pol ζ).

## Parental Histone Transfer and Epigenetic Inheritance

### Coupling of DNA Replication to Chromatin Recycling

Beyond its classical roles in DNA synthesis and repair, POLD2 has been identified as playing a critical role in the transfer of parental histones from the parental DNA strand to the newly synthesized lagging strand during DNA replication[13][30]. This function represents an emerging understanding of how DNA polymerases couple replication to the maintenance of epigenetic information. The transfer of parental histones H3-H4 to newly replicated DNA is essential for faithful epigenetic inheritance, as histone posttranslational modifications (PTMs) such as H3K27me3 and H3K4me3 carry gene expression information that must be perpetuated to daughter cells[13][30].

The p12 subunit (POLD4) of the Pol δ complex, which is directly associated with POLD2, has been identified as a histone chaperone that facilitates this transfer[13][30]. However, the broader Pol δ complex, including POLD2, appears necessary for proper epigenetic information maintenance during replication. Specifically, the PCNA-Pol δ complex couples lagging strand DNA synthesis to parental H3-H4 transfer, suggesting that the organization and localization of Pol δ at replication forks creates a favorable context for histone recycling[55].

### POLD2 Mutations and Epigenetic Dysregulation

Mutations in POLD2 result in altered patterns of histone modifications including changes in H3K27me3 and H3K4me3[40]. These chromatin modifications regulate gene expression through a mechanism termed the DNA replication-related transcriptional gene silencing (DRR-TGS) pathway[40]. The pold2-1 mutant in Arabidopsis exhibits sensitivity to DNA damage, delayed cell cycle progression, increased homologous recombination, and reduced telomere length, phenotypes that extend beyond simple DNA replication defects to encompass chromatin stability and epigenetic inheritance[40].

The altered histone modification patterns in POLD2 mutant cells correlate with changes in expression of specific genes[40]. These findings suggest that POLD2 is required for maintaining genome integrity while properly establishing the epigenetic markers during DNA replication to modulate gene expression. The integration of DNA replication fidelity with epigenetic inheritance through POLD2 represents an important aspect of how cells maintain both genetic and epigenetic information across cell divisions.

## Post-Translational Modifications and Protein-Protein Interactions

### Acetylation and Enhanced Catalytic Activity

While acetylation has been primarily documented for the p125 catalytic subunit and p12 subunit of Pol δ, the modifications of these subunits occur within the context of the complete holoenzyme containing POLD2[3][26]. Recent mass spectrometric analysis revealed that the human Pol δ is acetylated on subunits p125 (PolD1), p68 (PolD3), and p12 (PolD4), though direct acetylation of POLD2/p50 was not detected in these studies[3][26]. However, given the intimate structural associations between p50 and other subunits, acetylation-induced conformational changes in partner subunits could indirectly modulate POLD2 function.

### Phosphorylation and Regulatory Modifications

Phosphorylation of the p68 subunit (PolD3) has been shown to regulate its interaction with PCNA[3]. Similarly, the p125 catalytic subunit undergoes phosphorylation modifications that affect its function[3][26]. These phosphorylation events may influence the overall conformation of the holoenzyme and modulate POLD2's effectiveness in organizing the complex. The regulatory role of phosphorylation in DNA polymerase function appears to be a mechanism by which cells respond to cellular signaling and stress conditions by adjusting the activity of the replication and repair machinery.

### POLD2 Interactions with Non-Catalytic Proteins

Beyond its role within the Pol δ holoenzyme itself, POLD2 interacts with several non-catalytic proteins that regulate DNA metabolism[54]. These include PIAS2 (protein inhibitor of activated STAT 2), P21 (cyclin-dependent kinase inhibitor), PDIP1 (polymerase δ-interaction protein 1), PDIP38 (also known as PolDIP2), PDIP46, and WRN (Werner syndrome protein)[54]. These protein-protein interactions suggest that POLD2 serves as a nexus for coordinating replication and repair activities with broader cellular regulatory pathways.

The interaction with PolDIP2/PDIP38 is particularly significant in the context of translesion synthesis coordination, as PolDIP2 functions as a processivity factor for multiple TLS polymerases and bridges between the replicative Pol δ complex and the TLS apparatus[7]. The interaction with Werner syndrome helicase (WRN) may coordinate Pol δ with specialized helicases that process unusual DNA structures or facilitate break-induced replication during double-strand break repair.

### SUMOylation and Chromatin Localization

POLD2 has been identified as interacting with PIAS2, a SUMO E3 ligase family member[51]. This suggests that POLD2 may undergo SUMOylation, a post-translational modification involving the covalent attachment of small ubiquitin-like modifier (SUMO) proteins[41]. SUMOylation is a reversible modification that typically does not target proteins for degradation (in contrast to polyubiquitination) but rather modulates protein-protein interactions, alters protein localization, and affects enzyme activity[41]. The potential SUMOylation of POLD2 could represent a mechanism for regulating its assembly into the Pol δ holoenzyme or its interactions with other proteins regulating DNA replication.

## DNA Damage Response and Regulation in Response to Genotoxic Stress

### Degradation of the p12 Subunit in Response to DNA Damage

A key regulatory mechanism involves the degradation of the p12 subunit (POLD4) of Pol δ in response to DNA damage, particularly following UV irradiation[44][45]. UV-induced DNA damage triggers rapid degradation of p12, converting the Pol δ holoenzyme from its normal tetrameric or pentameric form to the Pol δ3 trimer lacking p12[44]. This conversion appears to be mediated by the CRL4^Cdt2^ E3 ubiquitin ligase complex, which recognizes a PIP-degron motif in p12 following DNA damage or replication stress[44].

The conversion from Pol δ4 (or Pol δ5 with dimeric p12) to Pol δ3 has functional consequences for the polymerase properties. As noted earlier, deletion of p12 causes approximately a five-fold decrease in the polymerase elongation rate constant and an approximately eight-fold increase in exonuclease activity, dramatically shifting the balance toward proofreading and away from processive synthesis[44]. This may enhance the ability of Pol δ to discriminate against damaged bases and mismatched primers, enhancing replication fidelity on damaged templates during TLS.

POLD2, as the structural scaffold that connects all Pol δ subunits, experiences dramatic functional reorganization during this p12 degradation event. While POLD2 remains in place through the p12 degradation process, the loss of its interaction with dimeric p12 modifies the overall architecture of the complex. Spatiotemporal analysis reveals that Pol δ4 is initially recruited to sites of UV-induced DNA damage, followed by the appearance of Pol δ3 upon loss of p12[44]. This temporal transition suggests that cells employ a two-step mechanism for responding to DNA damage: initial recruitment of the fully assembled Pol δ4, followed by conversion to the more proofreading-active Pol δ3 to handle synthesis on damaged templates.

### POLD2 Depletion and Complex Stability

POLD2 depletion results in marked destabilization of the Pol δ holoenzyme, leading to nearly complete loss of both POLD1 (p125) and POLD3 (p68) subunits through proteasomal degradation[36]. This observation demonstrates that POLD2 acts as a stabilizing factor essential for maintaining the assembly of the complete complex. Unlike degradation of p12 which occurs in response to DNA damage, degradation of p125 and p68 following POLD2 depletion suggests a constitutive requirement for POLD2 in maintaining holoenzyme integrity. The strong coupling between POLD2 levels and the stability of other subunits provides a checkpoint mechanism ensuring that Pol δ catalytic activity is only present in the context of the complete, functional holoenzyme.

## Clinical Significance and Cancer Association

### POLD2 Expression in Cancer Tissues

Comprehensive pan-cancer analysis has revealed that POLD2 is significantly overexpressed in most tumor types compared to normal tissues[18][54]. High POLD2 expression is significantly associated with advanced tumor stage, shorter overall survival (OS), and reduced progression-free survival (PFS) in multiple cancer types[18]. The correlation between POLD2 expression and tumor stage suggests that POLD2 upregulation may be selected for during tumor progression, potentially providing a growth advantage to malignant cells.

In multiple specific cancer types, POLD2 expression has been shown to correlate with poor prognosis[15][18]. In bladder urothelial carcinoma, high POLD2 expression was associated with poor overall survival (p = 0.019) and was significantly correlated with CAD (carbamoyl-phosphate synthetase II, aspartate transcarbamoylase, dihydroorotase) expression[15]. High expression of both CAD and POLD2 was associated with worse survival than patients with only one elevated marker[15]. Similarly, in glioblastoma, POLD2 expression correlates with poor patient survival, and POLD2 knockdown sensitizes glioblastoma cells to chemotherapy and radiation-induced cell death[21][33].

### POLD2 and Chemotherapy Resistance

The association between POLD2 expression and poor chemotherapy response appears mechanistically related to enhanced DNA repair capacity. POLD2 has been specifically implicated in cellular resistance to cisplatin, due to its ability to dramatically increase the efficiency and processivity of DNA synthesis via interaction with Pol ζ to bypass 1,2-intrastrand d(GpG)-cisplatin cross-links[15]. This function allows tumor cells to repair platinum-induced DNA damage more efficiently, reducing the effectiveness of platinum-based chemotherapy.

In glioblastoma cells, POLD2 inhibition significantly increased temozolomide-induced cell death from approximately 20% to 45%, and increased γ-radiation-induced cell death from approximately 19% to 31%[21][33]. These findings demonstrate that POLD2 functions to protect cells from chemo/radiation-induced DNA damage and apoptosis. EGFR pathway activation induced POLD2 expression in a time-dependent manner, and gene expression analysis of clinical specimens revealed a positive correlation between POLD2 and EGFR in glioblastoma specimens[21]. This suggests that signaling pathways active in cancer promote POLD2 expression, potentially contributing to chemoresistance through enhanced DNA repair capacity.

### POLD2 as a Tumor Suppressor in Specific Contexts

Interestingly, while high POLD2 expression is generally associated with poor cancer prognosis, there is evidence suggesting context-dependent functions. The relationship between POLD2 and tumor development appears complex, potentially involving both tumor-promoting and tumor-suppressive functions depending on the specific cancer type and genetic background. In the context of colorectal cancer, heterozygous mutations affecting POLD1 have been associated with increased cancer risk, yet the mechanisms by which POLD2 mutations or expression changes influence cancer development remain incompletely understood[42].

### POLD2 and Immune Checkpoint Interactions

Recent integrative analysis has revealed that POLD2 expression correlates strongly with immunomodulatory genes and shows significant negative correlation with immune checkpoints including PD-L1, CTLA4, TIM3, and CD28[18]. Furthermore, high POLD2 expression inhibits infiltration of CD8+ T cells and CD4+ memory T cells in the tumor microenvironment[18]. These findings suggest that POLD2 may promote tumor immune escape through suppression of anti-tumor immune responses. Pathway enrichment analysis demonstrates that low POLD2 expression promotes immune regulation-related pathways, while high POLD2 expression promotes metabolic and DNA repair-related pathways[18]. These observations suggest that POLD2 may serve as a potential target for immunotherapy assessment and that POLD2 expression could serve as a prognostic biomarker for both chemotherapy and immunotherapy response.

### POLD2 in Genetic Disorders and Developmental Defects

Germline biallelic mutations in POLD1 or POLD2 have been identified as the underlying etiology of a previously unknown autosomal-recessive syndrome combining replicative stress, neurodevelopmental abnormalities, and immunodeficiency[39]. The POLD2^Asp293Asn^ mutation lies in the phosphodiesterase (PDE) domain and is absent from public genetic databases[39]. This mutation reduces the stability of the p50 subunit, resulting in defective assembly or function of the Pol δ complex[39]. Patients with biallelic POLD2 mutations present with developmental defects and immunodeficiency, highlighting the critical importance of intact Pol δ function for normal human development and immune system establishment.

Heterozygous mutations affecting the polymerase and CysB domains of POLD1 have been found to cause autosomal-dominant mandibular hypoplasia, deafness, and progeroid features (MDP) syndrome[39]. These findings underscore the importance of Pol δ for normal development and the severe consequences of polymerase dysfunction. The involvement of POLD2 in maintaining genetic stability during development explains why even subtle mutations affecting POLD2 stability or function can result in significant developmental and immunological abnormalities.

## Regulation of Translocations and Genome Rearrangements

### POLD2 Promotion of Chromosomal Translocations

Recent evidence demonstrates that POLD2 promotes chromosomal translocations in multiple human cell types[36]. POLD2 depletion markedly reduces the frequency of translocations with sequence modifications but does not affect the frequency of translocations with exact joins[36]. This selective effect suggests that POLD2 specifically affects the accuracy of DNA processing during translocation formation.

Using separation-of-function mutants, studies have shown that both the DNA synthesis and exonuclease activities of the POLD1 catalytic subunit contribute to translocations[36]. When POLD2 is depleted, leading to degradation of POLD1 and POLD3, translocation frequency is severely reduced[36]. This can be rescued by expressing siRNA-resistant POLD2, confirming the specific role of POLD2 in translocation formation. The DNA polymerase δ complex appears to orchestrate translocations through alternative non-homologous end joining (Alt-NHEJ), a process that can result in complex rearrangements when dysregulated[36].

## Conclusion and Future Perspectives

POLD2 represents a multifunctional regulatory subunit of the DNA polymerase delta holoenzyme that extends far beyond simple scaffolding to encompass critical roles in DNA replication fidelity, DNA repair, epigenetic inheritance, and the regulation of genome stability[31][32][33][37]. The p50 subunit encoded by POLD2 serves as the organizational hub that maintains the assembly and optimal functioning of the complete Pol δ complex, facilitating its remarkably high processivity on undamaged DNA, its accurate synthesis on damaged templates, and its participation in multiple specialized DNA repair pathways[31][35].

Recent discoveries have expanded our understanding of POLD2 function beyond the realm of replication and repair to encompass previously unappreciated roles in chromatin dynamics and the transfer of parental histones during DNA replication[13][30]. This finding reveals an exquisite coupling of DNA synthesis to epigenetic inheritance, ensuring that both genetic and epigenetic information are faithfully transmitted to daughter cells. The dysregulation of POLD2 in cancer tissues and its association with chemotherapy resistance identify this protein as a potential therapeutic target for enhancing cancer treatment efficacy[15][21][33][36].

Future research directions include elucidating the precise structural mechanisms by which POLD2 organizes the holoenzyme, identifying all post-translational modifications that regulate POLD2 function, and developing therapeutic strategies to selectively inhibit POLD2-mediated DNA repair in cancer cells while preserving normal replication fidelity in non-tumor tissues. The emerging recognition of POLD2's role as an immune checkpoint factor suggests that modulation of POLD2 expression or activity could enhance immunotherapy effectiveness in multiple cancer types[18][54]. Understanding how POLD2 coordinates replication with epigenetic inheritance may also provide insights into developmental abnormalities and strategies for preventing errors in epigenetic programming during critical developmental windows.

## Citations

1. https://en.wikipedia.org/wiki/POLD2
2. https://www.uniprot.org/uniprotkb/A0A087WWF6/entry
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC10137900/
4. https://www.uniprot.org/uniprotkb/P49005/entry
5. https://predictomes.org/hp?pid=11575
6. https://www.nature.com/articles/s41467-020-14898-6
7. https://www.pnas.org/doi/10.1073/pnas.1308760110
8. https://www.pnas.org/doi/10.1073/pnas.2017637117
9. https://www.nature.com/articles/s41467-023-44125-x
10. https://www.ncbi.nlm.nih.gov/gene/5425
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC7189476/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC2685094/
13. https://www.pnas.org/doi/10.1073/pnas.2400610121
14. https://portlandpress.com/bioscirep/article/40/4/BSR20200602/222728/Identification-of-PCNA-interacting-protein-motifs
15. https://www.oncotarget.com/article/25701/text/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC4902588/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC7048817/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC9447486/
19. https://www.pnas.org/doi/10.1073/pnas.251193198
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC12051500/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC7198369/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC528896/
23. https://academic.oup.com/narcancer/article/5/1/zcad005/7028011
24. https://geneglobe.qiagen.com/us/knowledge/pathways/nucleotide-excision-repair-pathway
25. https://geneglobe.qiagen.com/us/knowledge/gene/ENSG00000106628
26. https://elifesciences.org/reviewed-preprints/107582
27. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=5425
28. https://academic.oup.com/nar/article/28/2/620/1039516
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC11098083/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC3694620/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC6424025/
32. https://www.pnas.org/doi/10.1073/pnas.2014176117
33. https://www.nature.com/articles/s41467-023-35795-8
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC6763221/
35. https://academic.oup.com/plphys/article/171/2/1192/6114933
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC5843405/
37. https://www.genecards.org/cgi-bin/carddisp.pl?gene=POLD2
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC6895278/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC5541323/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC5474181/
41. https://www.pnas.org/doi/10.1073/pnas.2511136122
42. https://www.uniprot.org/uniprot/P49004
43. https://www.uab.edu/medicine/biochem/images/Biochemistry/Vassylyev/PDF/X-ray%20structure%20of%20the%20complex%20of%20regulatory%20subunits%20of%20human%20DNA%20polymerase%20delta.pdf
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC6613617/
45. https://pubmed.ncbi.nlm.nih.gov/22824807/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC2605013/
47. https://pubmed.ncbi.nlm.nih.gov/31278166/
48. https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.877468/full
49. https://www.science.org/doi/10.1126/sciadv.adn5175
50. https://pubmed.ncbi.nlm.nih.gov/17410126/
51. https://www.pnas.org/doi/10.1073/pnas.0914857107
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC7597369/
53. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0213383
54. https://pmc.ncbi.nlm.nih.gov/articles/PMC3552135/