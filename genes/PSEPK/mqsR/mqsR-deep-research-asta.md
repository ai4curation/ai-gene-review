---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-07-10T16:02:57.604080'
end_time: '2026-07-10T16:03:03.068553'
duration_seconds: 5.46
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mqsR
  gene_symbol: mqsR
  uniprot_accession: Q88F93
  protein_description: 'SubName: Full=mRNA interferase MqsR of the MqsA-MqsR antitoxin/toxin
    complex and DNA-binding transcriptional repressor {ECO:0000313|EMBL:AAN69786.1};
    EC=3.1.-.- {ECO:0000313|EMBL:AAN69786.1};'
  gene_info: Name=mqsR {ECO:0000313|EMBL:AAN69786.1}; OrderedLocusNames=PP_4205 {ECO:0000313|EMBL:AAN69786.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: MqsR_sf. (IPR038493); MqsR_toxin. (IPR031451); MqsR_toxin (PF15723)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    query_char_limit: 500
    paper_limit: 50
    snippet_limit: 20
    snippet_paper_limit: 50
    restrict_snippets_to_papers: false
    paper_fields: title,abstract,authors,year,url,venue,journal,tldr,publicationDate,citationCount,influentialCitationCount,externalIds
    publication_date_range: ''
    venues: ''
    inserted_before: ''
citation_count: 13
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88F93
- **Protein Description:** SubName: Full=mRNA interferase MqsR of the MqsA-MqsR antitoxin/toxin complex and DNA-binding transcriptional repressor {ECO:0000313|EMBL:AAN69786.1}; EC=3.1.-.- {ECO:0000313|EMBL:AAN69786.1};
- **Gene Information:** Name=mqsR {ECO:0000313|EMBL:AAN69786.1}; OrderedLocusNames=PP_4205 {ECO:0000313|EMBL:AAN69786.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** MqsR_sf. (IPR038493); MqsR_toxin. (IPR031451); MqsR_toxin (PF15723)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mqsR" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mqsR' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mqsR** (gene ID: mqsR, UniProt: Q88F93) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Asta Literature Retrieval: Gene Research for Functional Annotation ⚠️ CRITICAL: Gene/Protein Identification Context BEFORE YOU BEGIN RESEARCH: Y...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 13
- Snippets retrieved: 20

## Relevant Papers

### [1] Substrate specificity of bacterial endoribonuclease toxins
- Authors: Yoontak Han, Eun-Jin Lee
- Year: 2020
- Venue: BMB Reports
- URL: https://www.semanticscholar.org/paper/c8fba26817ac67e890b44fbe9acd42764898eb15
- DOI: 10.5483/BMBRep.2020.53.12.203
- PMID: 33148377
- PMCID: 7781912
- Citations: 13
- Influential citations: 2
- Summary: The biology, structure, and substrate specificity of the updated bacterial endoribonuclease toxins are summarized and determined by its structure and the composition of active site residues.
- Evidence snippets:
  - Snippet 1 (score: 0.880)
    > PemK toxin inhibits protein synthesis by cleaving mRNAs while PemI antitoxin neutralizes PemK to resume protein synthesis (60). PemK toxin is yet another sequence-specific endoribonuclease that cleaves mRNA at the 5' or 3' side of the A nucleotide in the UAH recognition sequences where H could be one of C, A, or U nucleotides (60). MqsR-MqsA: The mqsR-mqsA (ygiU-ygiT) operon encodes MqsR toxin and MqsA antitoxin protein. The organization of the mqsR-mqsA (ygiU-ygiT) operon is non-canonical in a sense that the mqsR toxin gene precedes the mqsA antitoxin gene (61, 62). In addition to an MqsA-autorepressible promoter upstream of the mqsR toxin gene, the mqsA antitoxin gene has two additional constitutive promoters in the coding region of the mqsR toxin gene, allowing to uncouple transcription of the mqsR and mqsA genes (63). The MqsR toxin was originally identified as a motility quorum-sensing regulator because an mqsR insertional mutant exhibited a decreased autoinducer 2-mediated biofilm formation and reduced motility (64), both of which were controversial (63). In addition to motility and quorum sensing, the biological function of MqsR toxin was also suggested to be involved in persister cell formation (65).
    > MqsR toxin turned out to be a ribosome-independent endoribonuclease in E. coli (62). It cleaves mRNA preferentially at the 5' or 3' side of G nucleotide in GCU recognition sequences both in vivo and in vitro (8,62).
  - Snippet 2 (score: 0.755)
    > Here we summarized the bacterial toxins with endoribonuclease activity. The toxin components are organized in pairs with its cognate antitoxin components. For example, type II toxin-antitoxin systems consist of toxins and its cognate antitoxin proteins that are organized as bicistronic operons. The expression of the bicistronic operon is mostly repressed by the antitoxin protein, which has a DNA-binding domain for auto-repressor activity and a toxin-binding domain for neutralizing the toxin's activity. Stress conditions including amino acid starvation promote the differential degradation of the labile antitoxins by Lon or ClpAP proteases (78), and the removal of antitoxins results in an increase in the expression of the toxin-antitoxin operon (Fig. 1). The molecular ratio between toxin and anti-toxin proteins appears to be tightly regulated because most of the antitoxin and toxin genes are bicistronic and translationally coupled. Generally, the antitoxin gene precedes the toxin gene, which is also likely to ensure an appropriate molecular ratio between toxin and antitoxin proteins. However, the hicAB, higBA, and mqsRA operons have a reverse arrangement, whereby the toxin genes (hicA, higB, and mqsR) precede its cognate antitoxin genes (hicB, higA, and mqsA) (7,62,79). Moreover, the mqsRA operon has an additional promoter within the mqsR gene uncoupling transcription of the mqsR and mqsA genes (63). However, the biological significance of the reverse arrangement or transcriptional uncoupling is currently unclear. Similarly to most type II toxin-antitoxin systems, type III toxin-antitoxin systems are transcribed as single transcripts and then antitoxin RNAs are processed as mature sRNAs (34-36 nt) by the type III ribonuclease toxin.

### [2] Regulating Toxin-Antitoxin Expression: Controlled Detonation of Intracellular Molecular Timebombs
- Authors: Finbarr Hayes, B. Kedzierska
- Year: 2014
- Venue: Toxins
- URL: https://www.semanticscholar.org/paper/8696cca8682182bc588454346364063c1e6d4dbd
- DOI: 10.3390/toxins6010337
- PMID: 24434949
- PMCID: 3920265
- Citations: 95
- Influential citations: 2
- Summary: Interference with TA gene transcriptional autoregulation holds considerable promise as a novel antibacterial strategy: artificial release of the toxin factor using designer drugs is a potential approach to induce bacterial suicide from within.
- Evidence snippets:
  - Snippet 1 (score: 0.832)
    > The mqsRA module encoded by E. coli displays many features that differ from canonical type II TA systems. First, the gene for the mqsR toxin precedes the mqsA antitoxin gene, whereas the standard organization comprises an antitoxin gene followed by a toxin gene (Figure 1). This unusual genetic organization has been observed only rarely in other TA systems characterized to date, including the higBA [105] and hicAB modules [106]. Second, the MqsA antitoxin is well-ordered throughout its entire length and requires zinc ions to maintain its structural stability, properties that are unique among known antitoxins (Figure 2D) [48].
    > Autoregulation of the mqsRA module also is distinctive. The antitoxin repressor, MqsA, undergoes extensive domain rearrangements upon DNA binding and is the only antitoxin known to interact with DNA via its C-terminal domain [48,107]. However, the MqsA N-terminal domain, which binds the MqsR toxin, also makes direct interactions with DNA. It twists and collapses over the DNA and this rotation clamps the DNA thereby enhancing binding [107]. Interestingly, the MqsR toxin does not function as a transcriptional corepressor as in many other TA systems. Instead, MqsR destabilizes the MqsA-DNA complex. This reflects that the binding sites of DNA and MqsR on MqsA partially overlap rendering simultaneous binding of both by MqsA impossible. Thus, MqsR is a transcriptional activator of mqsRA expression, not a transcriptional repressor [85].
    > Distinct from other type II TA systems, the MqsR-MqsA complex also regulates other genomic promoter regions. Specifically, the MqsA antitoxin and the MqsR-MqsA complex regulate the promoters of genes that are important for E. coli metabolism, including the mcbR, spy and cspD loci [48,108]. The mcbR gene encodes a colanic acid regulator, Spy is a periplasmic chaperone of proteins, and CspD is a stress-induced cold shock protein that is a DNA replication inhibitor.

### [3] The Escherichia coli Toxin MqsR Destabilizes the Transcriptional Repression Complex Formed between the Antitoxin MqsA and the mqsRA Operon Promoter*
- Authors: Breann L Brown, D. Lord, Simina Grigoriu, W. Peti, R. Page
- Year: 2012
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/c7d314c4583ac3d5f64c54bbb571597a3eeea8aa
- DOI: 10.1074/jbc.M112.421008
- PMID: 23172222
- Citations: 85
- Influential citations: 8
- Summary: This is the first TA system in which the toxin does not function as a transcriptional co-repressor, but instead functions to destabilize the antitoxin-operator complex under all conditions, and thus defines another unique feature of the mqsRA TA module.
- Evidence snippets:
  - Snippet 1 (score: 0.819)
    > Background: MqsR, an endoribonuclease, and MqsA, a transcriptional regulator, form a unique toxin-antitoxin (TA) pair. Results: The high affinity, stable MqsR-MqsA complex is unable to bind DNA. Conclusion: MqsR is the only toxin shown to disrupt the antitoxin-DNA complex, which would promote transcription. Significance: The MqsR toxin may promote multidrug tolerance in E. coli by disrupting MqsA-mediated transcriptional repression of several genes related to persistence. Bacterial biofilms are complex communities of cells containing an increased prevalence of dormant cells known as persisters, which are characterized by an up-regulation of genes known as toxin-antitoxin (TA) modules. The association of toxins with their cognate antitoxins neutralizes toxin activity, allowing for normal cell growth. Additionally, protein antitoxins bind their own promoters and repress transcription, whereas the toxins serve as co-repressors. Recently, TA pairs have been shown to regulate their own transcription through a phenomenon known as conditional cooperativity, where the TA complexes bind operator DNA and repress transcription only when present in the proper stoichiometric amounts. The most differentially up-regulated gene in persister cells is mqsR, a gene that, with the antitoxin mqsA, constitutes a TA module. Here, we reveal that, unlike other TA systems, MqsR is not a transcription co-repressor but instead functions to destabilize the MqsA-DNA complex. We further show that DNA binding is not regulated by conditional cooperativity. Finally, using biophysical studies, we show that complex formation between MqsR and MqsA results in an exceptionally stable interaction, resulting in a subnanomolar dissociation constant that is similar to that observed between MqsA and DNA. In combination with crystallographic studies, this work reveals that MqsA binding to DNA and MqsR is mutually exclusive. To our knowledge, this is the first TA system in which the toxin does not function as a transcriptional co-repressor, but instead functions to destabilize the antitoxin-operator complex under all conditions, and thus defines another unique feature of
  - Snippet 2 (score: 0.730)
    > Thus, unlike most toxins, MqsR does not act as a transcriptional co-repressor but instead a transcriptional derepressor. Critically, this newly identified function of MqsR may also explain previous results which showed that overexpression of MqsR led to an increase in the transcription of genes known to be regulated by MqsA, including cspD, rpoS, and mqsA itself (28). Therefore, both in vitro (these studies) and in vivo experiments (28) show that MqsR also functions as a transcriptional derepressor.
    > We previously determined that the mqsRA toxin-antitoxin module is unique among E. coli TA modules based upon the novel features of the MqsA antitoxin. However, it is now becoming evident that the MqsR toxin also displays unusual toxin characteristics which, together with the unique features of the MqsA antitoxin, may also lead to differences in transcriptional regulation of the mqsRA operon. We report that the MqsR-MqsA complex does not bind its own operon promoter, which would lead to transcriptional repression, as is common for several other TA systems. Instead, in all instances, the MqsR toxin serves solely to disrupt the MqsA-DNA complex in vitro and thus results in transcriptional activation. In addition, we show that MqsR is capable of cleaving mRNA corresponding not only to mqsA, but to mqsR as well. This suggests that MqsR may autoregulate its own activity, which could allow for rapid exit from the persister state upon removal of environmental stress. Expression of MqsR was previously shown to play a role in persistence as well as biofilm formation through positively regulating the expression of various genes including the toxin cspD and the two-component motility regulatory system qseBC (27,28). Because MqsA regulates multiple genes that play a vital role in E. coli physiology, including activation of the general stress response (21), the function of MqsR in alleviating MqsAmediated repression would further elucidate the mechanism by which MqsR exerts some of its cellular effects.
  - Snippet 3 (score: 0.719)
    > However, under conditions of environmen-tal stress, such as nutrient starvation, oxidative stress, or antibiotic challenge, the antitoxins are rapidly degraded by cellular proteases, mainly Lon or ClpXP (20 -23), and the toxins are free to exert their cellular effects.
    > Previously, gene expression profiling revealed that the gene most highly up-regulated in Escherichia coli persister cells is the toxin mqsR (9). The mqsR gene encodes a small 98-amino acid protein that functions as a sequence-specific mRNA endoribonuclease belonging to the RelE family of bacterial toxins (24 -26). Its cognate antitoxin mqsA, which is located immediately downstream of mqsR in the same operon, encodes a 131-amino acid protein that functions to neutralize MqsR toxicity. There is a growing body of evidence that the mqsRA TA system plays a significant role in multiple cellular processes in E. coli. For instance, MqsR has been shown to facilitate biofilm formation by affecting cellular motility as a result of autoinducer-2 signaling (27). Also, deletion of mqsR and the mqsRA operon leads to decreased persister cell formation, the only type II TA system known to do so, whereas overexpression of MqsR increases persister cell formation (10). Finally, the antitoxin MqsA has been shown to serve as a transcriptional regulator not only of the mqsRA operon, but also of several other E. coli genes, including mcbR, cspD, and the general stress response regulator rpoS (21,24,28).
    > We showed previously that the antitoxin MqsA is unique among all antitoxins studied to date. First, MqsA is completely structured throughout its entire sequence both in the free and DNA-or toxin-bound states (24,29), whereas other antitoxins are either partially or completely unstructured in the free state (30 -34).
  - Snippet 4 (score: 0.691)
    > We believe that MqsR cannot utilize either mechanism to serve as a transcriptional co-repressor for two reasons. First, there is no evidence for multiple binding interfaces between MqsR and MqsA. Our analysis of the MqsR-MqsA complex in solution has not revealed the presence of any oligomeric species larger than the MqsR-MqsA 2 -MqsR heterotetramer, as determined using size exclusion chromatography (Fig. 1A). Second, MqsR exists as a monomer in solution and has not been demonstrated to dimerize, which we also showed using size exclusion chromatography (Fig. 1A). Therefore, MqsR cannot serve as a co-repressor either alone (mechanism 1) or as a dimer (mechanism 2). Instead, and in contrast to all other characterized TA systems, even subequimolar quantities of MqsR toxin serve to destabilize the MqsA-DNA interaction (Fig. 4). In fact, at a 1:1 ratio of MqsR toxin to MqsA antitoxin, DNA binding by MqsA is essentially ablated. This behavior is unique to mqsRA because in all other TA systems, transcriptional derepression occurs only when toxin concentrations exceed their normal stoichiometric levels.
    > A detailed analysis of the x-ray crystal structures of the various states of MqsR and MqsA provides insight as to why MqsR destabilizes the interaction between MqsA and the mqsRA promoter. A model of the hypothetical MqsR-MqsA-DNA ternary complex based on our crystal structures of MqsA bound to DNA (Protein Data Bank (PDB) ID code 3O9X) and MqsR bound to the N-terminal domain of MqsA (PDB ID code 3HI2) revealed the potential for clashes between the DNA and MqsR when both are bound to MqsA (Fig. 5A). Moreover, the binding sites on MqsA for both MqsR and DNA partially overlap as MqsA Arg-61 forms interactions with both binding partners in the respective crystal structures (Fig. 5, B and C).

### [4] MqsR/MqsA Toxin/Antitoxin System Regulates Persistence and Biofilm Formation in Pseudomonas putida KT2440
- Authors: Chenglong Sun, Yunxue Guo, K. Tang, Zhongling Wen, Baiyuan Li et al.
- Year: 2017
- Venue: Frontiers in Microbiology
- URL: https://www.semanticscholar.org/paper/6c4b78f65bbb7964332e329c0758f28c7a7a38ac
- DOI: 10.3389/fmicb.2017.00840
- PMID: 28536573
- PMCID: 5422877
- Citations: 60
- Influential citations: 2
- Summary: An important regulatory role of MqsR/MqsA in persistence and biofilm formation in P. putida KT2440 is revealed and an type II TA system in a soil bacterium Pseudomonas putidaKT2440 belongs to the MqS/MqA family is identified.
- Evidence snippets:
  - Snippet 1 (score: 0.783)
    > Bacterial toxin/antitoxin (TA) systems have received increasing attention due to their prevalence, diverse structures, and important physiological functions. In this study, we identified and characterized a type II TA system in a soil bacterium Pseudomonas putida KT2440. This TA system belongs to the MqsR/MqsA family. We found that PP_4205 (MqsR) greatly inhibits cell growth in P. putida KT2440 and Escherichia coli, the antitoxin PP_4204 (MqsA) neutralizes the toxicity of the toxin MqsR, and the two genes encoding them are co-transcribed. MqsR and MqsA interact with each other directly in vivo and MqsA is a negative regulator of the TA operon through binding to the promoter. Consistent with the MqsR/MqsA pair in E. coli, the binding of the toxin MqsR to MqsA inhibits the DNA binding ability of MqsA in P. putida KT2440. Disruption of the mqsA gene which induces mqsR expression increases persister cell formation 53-fold, while overexpressing mqsA which represses mqsR expression reduces persister cell formation 220-fold, suggesting an important role of MqsR in persistence in P. putida KT2440. Furthermore, both MqsR and MqsA promote biofilm formation. As a DNA binding protein, MqsA can also negatively regulate an ECF sigma factor AlgU and a universal stress protein PP_3288. Thus, we revealed an important regulatory role of MqsR/MqsA in persistence and biofilm formation in P. putida KT2440.
  - Snippet 2 (score: 0.759)
    > The two genes encoding MqsR homolog and MqsA homolog are co-transcribed and both encode small proteins. MqsR and MqsA interact with each other directly in vivo and MqsA is a negative regulator of the TA operon through binding to the promoter. Consistent with the MqsR/MqsA pair in E. coli, the MqsR inhibits the binding of MqsA to its promoter in P. putida KT2440. Disruption of the mqsA gene which induces mqsR expression increases persister cell formation while overexpressing mqsA which represses mqsR expression reduces persister cell formation, suggesting an important role of MqsR in persistence in P. putida KT2440. However, different from E. coli, both MqsR and MqsA promote biofilm formation in P. putida KT2440. As a DNA binding protein, MqsA in E. coli also regulates the stationary phase sigma factor RpoS and CsgD. In contrast, we found that MqsA negatively regulates the ECF sigma factor AlgU and a universal stress protein PP_3288 in P. putida KT2440, suggesting a different role of MqsR/MqsA in P. putida KT2440.

### [5] Escherichia coli toxin/antitoxin pair MqsR/MqsA regulate toxin CspD
- Authors: Younghoon Kim, Xiaoxue Wang, Xue-Song Zhang, Simina Grigoriu, R. Page et al.
- Year: 2010
- Venue: Environmental microbiology
- URL: https://www.semanticscholar.org/paper/c80a41dacb26d80cbb67433eee406eba7b42b354
- DOI: 10.1111/j.1462-2920.2009.02147.x
- PMID: 20105222
- PMCID: 3980499
- Citations: 172
- Influential citations: 13
- Summary: It is demonstrated that the MqsR/MqsA TA system controls cell physiology via its own toxicity as well as through its regulation of another toxin, CspD, through proteases Lon and ClpXP.
- Evidence snippets:
  - Snippet 1 (score: 0.750)
    > Summary Previously we identified that the Escherichia coli protein MqsR (YgiU) functions as a toxin and that it is involved in the regulation of motility by quorum sensing signal autoinducer-2 (AI-2). Furthermore, MqsR is directly associated with biofilm development and is linked to the development of persister cells. Here we show that MqsR and MqsA (YgiT) are a toxin/antitoxin (TA) pair, which, in significant difference to other TA pairs, regulates additional loci besides its own. We have recently identified that MqsR functions as an RNase. However, using three sets of whole-transcriptome studies and two nickel-enrichment DNA binding microarrays coupled with cell survival studies in which MqsR was overproduced in isogenic mutants, we identified eight genes (cspD, clpX, clpP, lon, yfjZ, relB, relE and hokA) that are involved in a mode of MqsR toxicity in addition to its RNase activity. Quantitative real-time reverse transcription polymerase chain reaction (qRT-PCR) showed that (i) the MqsR/MqsA complex (and MqsA alone) represses the toxin gene cspD, (ii) MqsR overproduction induces cspD, (iii) stress induces cspD, and (iv) stress fails to induce cspD when MqsR/MqsA are overproduced or when mqsRA is deleted. Electrophoretic mobility shift assays show that the MqsA/MqsR complex binds the promoter of cspD. In addition, proteases Lon and ClpXP are necessary for MqsR toxicity. Together, these results indicate the MqsR/MqsA complex represses cspD which may be derepressed by titrating MqsA with MqsR or by degrading MqsA via stress conditions through proteases Lon and ClpXP. Hence, we demonstrate that the MqsR/MqsA TA system controls cell physiology via its own toxicity as well as through its regulation of another toxin, CspD.

### [6] Three Dimensional Structure of the MqsR:MqsA Complex: A Novel TA Pair Comprised of a Toxin Homologous to RelE and an Antitoxin with Unique Properties
- Authors: Breann L Brown, Simina Grigoriu, Younghoon Kim, J. M. Arruda, Andrew M. Davenport et al.
- Year: 2009
- Venue: PLoS Pathogens
- URL: https://www.semanticscholar.org/paper/4762d1b8181e2d25190402a4f115b51310b3c47a
- DOI: 10.1371/journal.ppat.1000706
- PMID: 20041169
- PMCID: 2791442
- Citations: 191
- Influential citations: 16
- Summary: It is revealed that MqsR:MqsA form a novel toxin:antitoxin (TA) pair and that TA systems, especially the antitoxins, are significantly more diverse than previously recognized and provide new insights into the role of toxins in maintaining the persister state.
- Evidence snippets:
  - Snippet 1 (score: 0.745)
    > Because the sequence of MqsR is not similar to that of any other known toxin, its molecular function is unknown.
    > Deletion of mqsA (ygiT/b3021), the second gene in the two-gene mqsRA operon, is lethal [6,36]. This led to the postulation that mqsRA constitutes a novel TA module [6,15], with MqsR as the toxin and MqsA as its cognate antitoxin. However, mqsRA has many characteristics that differ from canonical TA systems. First, in the mqsRA operon, mqsR precedes, instead of follows, mqsA. This unusual genetic organization has only been observed in two other recently characterized TA systems, that of higBA [37] and hicAB [32]. Second, their isoelectric points are nearly identical (8.8, MqsR; 9.1, MqsA) rather than being basic and acidic for the toxin and antitoxin, respectively. Third, the MqsA protein is larger, instead of smaller, than MqsR; the only other TA system with an antitoxin larger than its cognate toxin is that of hicAB [32]. Finally, their sequences are not homologous to any member of a recognized TA system.
    > In this paper, we employed a combination of biochemical and structural studies to show that MqsR, along with MqsA, are a bona fide TA pair that, because of the unique features of MqsA, define a novel family of TA modules. We show that MqsR is toxic and forms a tight complex with its antitoxin, MqsA, an interaction that mitigates MqsR toxicity. MqsA and the MqsR:MqsA complex also bind the promoters of the mqsRA operon and, unexpectedly, genes critical for E. coli physiology, including mcbR and spy. To the best of our knowledge, this is the first time a TA pair has been shown to bind and regulate promoters other than its own. The structure of MqsR reveals that it is a member of the RelE/YoeB family of bacterial RNase toxins.
  - Snippet 2 (score: 0.732)
    > (B) Western blots showing soluble expression of MqsR mutants K56A, Q68A, Y81A and K96A from the cultures used to generate the growth curves in (A) (WT MqsR arrests cell growth so rapidly that free MqsR is not detectable by Western Blot). All MqsR constructs include an N-terminal his 6 -tag and protein expression was detected using a polyhistidine polyclonal antibody. Like WT, expressed protein for MqsR mutants Y55A, M58A and R72A was not detected. doi:10.1371/journal.ppat.1000706.g006 predicted to bind DNA via its C-and not N-terminal domain is HicB [32,50]. MqsA is also the first antitoxin described that requires a metal, zinc, for structural stability. Moreover, unlike most other TA inhibition mechanisms, MqsA (like its RelB homolog [28]) does not occlude the toxin active site. Finally, in addition to binding its own promoter, MqsA and the MqsR:MqsA 2 :MqsR complex also bind and regulate the promoters of genes that play roles in E. coli physiology, including mcbR and spy. To the best of our knowledge, this is the first time a TA system has been shown to bind the promoters of genes other than its own. The MqsR:MqsA 2 :MqsR complex is oligomeric, and forms a dimer of dimers (MqsR:MqsA 2 :MqsR). Since the structure of the MqsA-N is invariant among all structures determined (MqsA-F; MqsA-N and the MqsR:MqsA-N complex), we used the MqsA-F and MqsR:MqsA-N structures to generate an accurate model of the full MqsR:MqsA 2 :MqsR complex.
  - Snippet 3 (score: 0.716)
    > Our biochemical and structural analysis of the E. coli MqsA antitoxin and the MqsR:MqsA-N complex provide a detailed 3dimensional structural view of the free antitoxin and the TA complex. These structures combined with our biochemical data unequivocally demonstrate that MqsR, a protein previously shown to be critical for biofilm formation [34,35] and the most highly upregulated gene in persister cells [6] in E. coli, and MqsA form a novel bacterial TA system. Our data show that, as expected for a TA system, the expression of the MqsR toxin leads to growth arrest, while co-expression with its antitoxin, MqsA, rescues the growth arrest phenotype. In addition, MqsR associates with MqsA to form a tight, non-toxic complex and both MqsA alone and the MqsR:MqsA 2 :MqsR complex bind and regulate the mqsR promoter. Finally, the structure of MqsR reveals that it is a member of the RelE/YoeB family of bacterial RNases, which are structurally and functionally characterized bacterial toxins.
    > Comparison of the microbial RNase active sites between MqsR, RelE, YoeB and RNase Sa demonstrates that MqsR is most similar to RelE (Fig. 8A). In microbial RNases, such as RNase Sa, RNA binding is mediated by polar (Q38) and aromatic (Y86) residues while RNA cleavage is catalyzed by a histidine (H85) and glutamic acid (E54) residue [47,48]. While the catalytic histidine and glutamic acid are conserved in YoeB (H83, E46), which has intrinsic endoribonuclease activity [33], they are not found in RelE, which functions as a ribosome-dependent RNase [23,45]. These catalytic residues are also not present at the MqsR functional site (Figs. 7C, 8B, 8C).

### [7] Toxins of Prokaryotic Toxin-Antitoxin Systems with Sequence-Specific Endoribonuclease Activity
- Authors: H. Masuda, M. Inouye
- Year: 2017
- Venue: Toxins
- URL: https://www.semanticscholar.org/paper/1e5086124d4cd5473bee417c858d7815f2f44e0b
- DOI: 10.3390/toxins9040140
- PMID: 28420090
- PMCID: 5408214
- Citations: 59
- Summary: In this review, a variety of tools utilized to study the nuclease activities of toxins over the past 15 years will be reviewed and a recent adaptation of an RNA-seq-based technique to analyze entire sets of cellular RNA will be introduced with an emphasis on its strength in identifying novel targets and redefining recognition sequences.
- Evidence snippets:
  - Snippet 1 (score: 0.738)
    > Cleavage occurs at the 5 and/or 3 end of the G-residue. Despite exhibiting sequence-specific ribonuclease activity independently of a ribosome, MqsR belongs to the same protein family as RelE and YoeB, which are the ribosome-dependent ribonucleases [39].
    > MqsA, an antitoxin of MqsR, also belongs to a distinctive protein family from MazE [39,75]. There are many differences between MqsA and MazE, with regard to the structure and the mechanism of inhibiting the toxin's activity. MqsA consists of a novel fold containing a zinc ion, although it merely serves structural role and not a catalytic role [39]. Unlike MazE, whose unstructured C-terminal tail is crucial for binding with the toxin to inhibit its activity, the structure of MqsA is not flexible [39,76]. Furthermore, MqsA does not directly bind to the active site of the toxin to block catalysis. Binding with MqsA induces a substantial conformational change in MqsR so that it loses its activity. Additionally, when bound to its antitoxin, the active sites in two MqsR proteins face one another, making them inaccessible to the target mRNA.
    > Despite its distinct phylogenetic origin and mechanism of toxin sequestration, MqsRA autoregulates its own transcription in a similar manner as other Type II TA systems [49,76,77]. The antitoxin or TA complex binds with DNA at the palindromic sequence and suppresses its own expression. MqsRA also regulates the expression of other genes as a global transcriptional regulator, which will be further discussed in the later sections.

### [8] Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes
- Authors: Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al.
- Year: 2021
- Venue: mSystems
- URL: https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
- DOI: 10.1128/mSystems.00673-21
- PMID: 34726489
- PMCID: 8562490
- Citations: 15
- Summary: This work systematically updates the functional genome annotation of Mycobacterium tuberculosis virulent type strain H37Rv and identifies hundreds of high-confidence candidates for mechanisms of antibiotic resistance, virulence factors, and basic metabolism and other functions key in clinical and basic tuberculosis research.
- Evidence snippets:
  - Snippet 1 (score: 0.738)
    > 3. Fig. S2B -match/mismatch colours mixed up? (I think match should be teal and mismatch -red?) 4. Line 162-163: Rv1430 is in UniProt (EC 3.1.1.-) and has been present in Uniprot since version 45 of the gene record: https://www.uniprot.org/uniprot/L7N697. I presume you had conducted your literature analysis before the UniProt entry was updated to include the EC code, so maybe you can add the dates when the data was retrieved from UniProt and other databases you used in the Materials and Methods section? 5. Supplementary text, p. 9, first paragraph. I believe that an unrelated fragment of text was copy-pasted into the second sentence of the paragraph ("Many mutations that altered bacterial clearance...") 6. Supplementary text, p. 12, final paragraph. It should be Rv1191, not Rv1191c. Could you also add a short explanation why you believe it should be classified as a cathepsin (what protein did you transfer this annotation from)?
    > Reviewer #3 (Comments for the Author):
    > In this manuscript, Modlin et al., attempt to tackle the problem of assigning functions to ~1700 hypothetical and/or underannotated genes in the Mycobacterium tuberculosis H37Rv (Mtb) genome. Rapid and accurate annotation of microbial genomes is indeed a very critical and under appreciated part of microbial ecophysiology. This step is especially crucial for pathogenic organisms such as Mtb where accurate functional annotation of these hypothetical proteins could unravel mechanisms which could act as drug targets. The authors employed a two-pronged strategy to define a set of these unannotated or under-annotated genes and to then provide possible functions for many of these genes. First, they undertook a large-scale manual curation of literature to assign functions (including EC numbers for enzymatic functions) to ~575 genes.

### [9] Keeping the Wolves at Bay: Antitoxins of Prokaryotic Type II Toxin-Antitoxin Systems
- Authors: W. Chan, M. Espinosa, C. Yeo
- Year: 2016
- Venue: Frontiers in Molecular Biosciences
- URL: https://www.semanticscholar.org/paper/3f550bf6b186a2a89d348d5159da25909e53896e
- DOI: 10.3389/fmolb.2016.00009
- PMID: 27047942
- PMCID: 4803016
- Citations: 141
- Influential citations: 6
- Summary: Type II TA antitoxins, as DNA-binding proteins, play an essential role in modulating the prokaryotic lifestyle whilst at the same time preventing the lethal action of the toxins under normal growth conditions, i.e., keeping the proverbial wolves at bay.
- Evidence snippets:
  - Snippet 1 (score: 0.729)
    > The MqsRA locus of E. coli K-12 is an unusual TA locus that differs from most canonical TA systems. The MqsR (motility quorum sensing regulator) toxin was initially identified as a regulator of motility and quorum sensing, influencing the development of biofilms by mediating the cellular response to autoinducer-2 (Ren et al., 2004;González Barrios et al., 2006). The mqsR gene was also significantly upregulated in persister cells and, along with its downstream gene, mqsA, were shown to be a type II TA system (Brown et al., 2009;Yamaguchi et al., 2009;Christensen-Dalsgaard et al., 2010;Kasari et al., 2010). MqsR is a ribosome-independent endoribonuclease that specifically cleaves mRNA at 5 ′ -GCU-3 ′ and, to a lesser extent, 5 ′ -GCA-3 ′ sequences (Yamaguchi et al., 2009;Christensen-Dalsgaard et al., 2010).
    > The MqsRA system is unique in several aspects. The mqsR toxin gene precedes the mqsA antitoxin gene, an arrangement that so far has been observed only in a few type II TA loci, namely higBA (Tian et al., 1996), hicAB (Jørgensen et al., 2009), and rnlAB (Koga et al., 2011). The MqsA antitoxin is larger than MqsR toxin (14.7 kDa and 11.2 kDa, respectively) whereas in canonical TA systems, the toxin is larger than the antitoxin, with the exception of HicB (Jørgensen et al., 2009). Both MqsA and MqsR are also basic proteins whereas usually, the toxin is basic while the antitoxin is acidic (Kasari et al., 2010).
    > Elucidation of the MqsRA crystal structure also revealed a few surprises.

### [10] Avian Immunome DB: an example of a user-friendly interface for extracting genetic information
- Authors: Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al.
- Year: 2020
- Venue: BMC Bioinformatics
- URL: https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
- DOI: 10.1186/s12859-020-03764-3
- PMID: 33176685
- PMCID: 7661159
- Citations: 6
- Summary: The Avian Immunome DB (Avimm) for easy gene property extraction as exemplified by avian immune genes is presented and described, which contains 1170 distinct avian immune genes with canonical gene symbols and 612 synonyms across 363 bird species.
- Evidence snippets:
  - Snippet 1 (score: 0.719)
    > Ever since the advent of commercial next-generation sequencing platforms in the early 2000s with its associated decrease in sequencing costs [1], the number of DNA sequences increased considerably [2]. Generally, these data become publicly accessible in databases provided by projects focussing on different aspects of biological sequence information [3,4]. Ensembl [5] and NCBI [6] for instance, have a strong focus on genome annotation with the help of RNA transcript information while UniProt has a pronounced emphasis on protein-coding genes and biological function of proteins. UniProt's records are either based on manually annotated, non-redundant protein sequences (SwissProt) or on highquality computationally analysed records, which are enriched with automatic annotation (TrEMBL) [7]. Relying on accurate genome annotations and protein descriptions, Gene Ontology (GO) [8,9] categorises gene products and fits them into a computational model of biological systems. Their assignment deploys a controlled vocabulary, so-called GO terms, to link genes and gene products to biological processes, cellular components, or molecular functions.
    > However, genome annotation is not standardised, and each service provider uses their own custom-built annotation pipelines. As a consequence, this often leads to ambiguity in gene names during genome annotation with different gene symbols being given to the same gene or the same gene symbol being given to different, but similar genes. Additionally, since the pre-existing wealth of sequencing information relies on model organisms like human and mouse, there is a strong bias in gene symbols towards those chosen for these species. Particularly for model species, this issue has been partially addressed, for example by the Human Genome Organisation (HUGO) Gene Nomenclature Committee (HGNC) [10], the Vertebrate Gene Nomenclature Committee (VGNC) [11], or the Chicken Gene Nomenclature Consortium [12]. However, this neither guarantees that gene names are harmonised among these consortia, nor does it keep researchers from assigning alternative gene symbols in their annotations, especially when working with non-model species.

### [11] Intracellular Localization of the Proteins Encoded by Some Type II Toxin-Antitoxin Systems in Escherichia coli
- Authors: Alexander Mager, Tommy Safran, H. Engelberg-Kulka
- Year: 2021
- Venue: mBio
- URL: https://www.semanticscholar.org/paper/3400981ba961c43f50e703afa6b9a869aeefbb69
- DOI: 10.1128/mBio.01417-21
- PMID: 34340547
- PMCID: 8406201
- Citations: 1
- Summary: This study is the first to clarify the intracellular localization of the proteins specified for some type II TA systems, and shows that, with the exception of the chpBIK module, each toxin-antitoxin complex was localized in a different part of the cell than the toxin itself.
- Evidence snippets:
  - Snippet 1 (score: 0.699)
    > Having found that the protein products of the mazEF and chpBIK TA modules had different intracellular localization patterns, we asked if other type II TA modules might each have unique intracellular localization patterns. First, we considered the mqsRA toxin-antitoxin module, generating mCherry fusions of the toxin MqsR and the antitoxin MqsA as we did for the mazEF and chpBIK modules. The primers used for cloning are listed in the supplemental material, and the constructed fusions are illustrated schematically in Fig. S2 in the supplemental material.
    > Figure 6A demonstrates the intracellular localization of the toxin MqsR fused with mCherry in the E. coli MC4100 relA 1 strain. As shown, two main intracellular localization patterns of MqsR were observed. First, in one subpopulation of the cells, MqsR-mCherry was located at the middle of the cell (indicated by yellow arrows). In another subpopulation of the cells, the toxin MqsR was localized between the pole and the middle of the cell (indicated by white arrows).
    > Figure 6B represents the intracellular localization of the antitoxin MqsA fused with mCherry. In contrast to the toxin MqsR, MqsA-mCherry was dispersed homogenously in the cells.
    > Unlike the mazEF and chpBIK TA modules, in which the gene for the antitoxin precedes the gene for the toxin, in the mqsRA TA module, the mqsR toxin gene precedes the mqsA antitoxin gene. To recreate the conditions under which the toxin is fused with mCherry and is expressed in the presence of the overproduced antitoxin, we needed to use a different approach than the one described above for the mazEF and chpBIK modules. We cloned the mqsA antitoxin gene to pBAD33 and transformed this newly constructed plasmid into E. coli MC4100 relA 1 cells harboring the pBAD-18-mqsR-mcherry plasmids. The cloning protocol is described in details in Materials and Methods.

### [12] Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir
- Authors: Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al.
- Year: 2025
- Venue: Molecular ecology
- URL: https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
- DOI: 10.1111/mec.70012
- PMID: 40613337
- PMCID: 12288799
- Citations: 3
- Summary: It is hypothesized that the combination of down‐ and up‐regulated immune gene expression may prevent overstimulation of the immune response, acting as an adaptation in grey seals to resist IAV‐associated mortality.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > Top hits were required to have a percent query coverage (QC) ≥ 80 to be used for annotating transcripts. A subsequent blastx search against the Swiss-Prot database (downloaded from NCBI 07/02/2021) for transcripts without a sufficient hit was conducted using the parameters max_target_seqs 2, max_hsps 1, e-value 0.001 and qcov_hsp_perc 80. Genes without a published gene symbol (named 'LOC' + Gene ID in NCBI's database) were assigned a UniProt gene symbol based on the protein annotation listed in the RefSeq entries, when possible. Ultimately, a list of transcript identifiers and gene symbols were compiled into a transcript-to-gene map for subsequent analyses.
    > To further facilitate analyses of gene functions, additional steps were taken to identify the putative function of genes annotated with a symbol that began with 'LOC'. First 'LOC' genes with a protein-coding gene description in NCBI's database were manually assigned the appropriate gene symbol. Transcript sequences of remaining 'LOC' genes were queried through a blastn search against NCBI's nucleotide database (parameters: max target seq = 2, max hsps = 1, evalue = 0.01, perc identity = 90). Results from the blastn search were filtered to exclude hits with query coverage < 90 and hits that included vague terms (e.g., 'uncharacterized', 'genome assembly' and 'chromosome'). Gene symbols were extracted from the first hit for each transcript and assigned as the identity of that gene for genes with only a single transcript with hits or with consistent hits across transcripts. For genes with multiple transcripts that matched different gene symbols, the annotation was manually determined based on the number of transcripts for each gene symbol hit and query coverage/% identity values. For any 'LOC' genes that were identified as a gene already present in the dataset, gene counts were concatenated for further analysis.

### [13] Characterization of the Deep-Sea Streptomyces sp. SCSIO 02999 Derived VapC/VapB Toxin-Antitoxin System in Escherichia coli
- Authors: Yunxue Guo, Jianyun Yao, Chenglong Sun, Zhongling Wen, Xiaoxue Wang
- Year: 2016
- Venue: Toxins
- URL: https://www.semanticscholar.org/paper/ba38f6ce608d862163fee287c086e7c988bb9d45
- DOI: 10.3390/toxins8070195
- PMID: 27376329
- PMCID: 4963828
- Citations: 19
- Influential citations: 1
- Summary: A new deep sea TA system is identified and characterized in the deep sea Streptomyces sp.
- Evidence snippets:
  - Snippet 1 (score: 0.688)
    > New approaches are in needed to purify the toxin for in vitro characterization of the cellular targets of the toxin.
    > Studies on cross-activation among TA systems or other toxins mainly focus on type II TA system in which the toxin components are endoribonucleases. The well-studied type II TA MqsR/MqsA induces or represses various toxin genes in E. coli. For example, titrating antitoxin MqsA with MqsR or degrading MqsA through proteases Lon and ClpXP represses the expression of small toxic gene cspD [65]. In contrast, the deletion of toxin gene mqsR represses small toxic polypeptides encoding genes hokA and hokE [65]. In addition, MqsR overproduction induced expression of the relBEF operon and relF encodes a hok-like toxin targeting the inner membrane [65,66]. Furthermore, MqsR degrades ghoS mRNA and enriches toxin ghoT mRNA of the GhoT/GhoS type V TA pair during stress conditions [40]. In turn, HipA toxin activates the mqsR/mqsA operon [22], and RelE toxin induces the transcription of several TA operons including mqsR/mqsA [66,67]. Expression of VapC from Salmonella and Shigella activates toxin gene yoeB expression in E. coli, and the activation depends on Lon protease [41]. However, cross-activation among TAs in E. coli can also occur in protease deficient strains such as in lon, ppk, clpP, and hslV deficient strains [66]. Collectively, these results suggest that cross-talk among TAs is rather complex, and the exact mechanism remains to be elucidated.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Citations

1. Yoontak Han, Eun-Jin Lee (2020). Substrate specificity of bacterial endoribonuclease toxins. BMB Reports. https://www.semanticscholar.org/paper/c8fba26817ac67e890b44fbe9acd42764898eb15
2. Finbarr Hayes, B. Kedzierska (2014). Regulating Toxin-Antitoxin Expression: Controlled Detonation of Intracellular Molecular Timebombs. Toxins. https://www.semanticscholar.org/paper/8696cca8682182bc588454346364063c1e6d4dbd
3. Breann L Brown, D. Lord, Simina Grigoriu, W. Peti, R. Page (2012). The Escherichia coli Toxin MqsR Destabilizes the Transcriptional Repression Complex Formed between the Antitoxin MqsA and the mqsRA Operon Promoter*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/c7d314c4583ac3d5f64c54bbb571597a3eeea8aa
4. Chenglong Sun, Yunxue Guo, K. Tang, Zhongling Wen, Baiyuan Li et al. (2017). MqsR/MqsA Toxin/Antitoxin System Regulates Persistence and Biofilm Formation in Pseudomonas putida KT2440. Frontiers in Microbiology. https://www.semanticscholar.org/paper/6c4b78f65bbb7964332e329c0758f28c7a7a38ac
5. Younghoon Kim, Xiaoxue Wang, Xue-Song Zhang, Simina Grigoriu, R. Page et al. (2010). Escherichia coli toxin/antitoxin pair MqsR/MqsA regulate toxin CspD. Environmental microbiology. https://www.semanticscholar.org/paper/c80a41dacb26d80cbb67433eee406eba7b42b354
6. Breann L Brown, Simina Grigoriu, Younghoon Kim, J. M. Arruda, Andrew M. Davenport et al. (2009). Three Dimensional Structure of the MqsR:MqsA Complex: A Novel TA Pair Comprised of a Toxin Homologous to RelE and an Antitoxin with Unique Properties. PLoS Pathogens. https://www.semanticscholar.org/paper/4762d1b8181e2d25190402a4f115b51310b3c47a
7. H. Masuda, M. Inouye (2017). Toxins of Prokaryotic Toxin-Antitoxin Systems with Sequence-Specific Endoribonuclease Activity. Toxins. https://www.semanticscholar.org/paper/1e5086124d4cd5473bee417c858d7815f2f44e0b
8. Samuel J. Modlin, A. Elghraoui, Deepika Gunasekaran, Alyssa M Zlotnicki, N. Dillon et al. (2021). Structure-Aware Mycobacterium tuberculosis Functional Annotation Uncloaks Resistance, Metabolic, and Virulence Genes. mSystems. https://www.semanticscholar.org/paper/76ff9a62b36b32cc10e46e71ffd4dd90344e4706
9. W. Chan, M. Espinosa, C. Yeo (2016). Keeping the Wolves at Bay: Antitoxins of Prokaryotic Type II Toxin-Antitoxin Systems. Frontiers in Molecular Biosciences. https://www.semanticscholar.org/paper/3f550bf6b186a2a89d348d5159da25909e53896e
10. Ralf C. Mueller, Nicolai Mallig, Jacqueline Smith, Lél Eöry, Richard I. Kuo et al. (2020). Avian Immunome DB: an example of a user-friendly interface for extracting genetic information. BMC Bioinformatics. https://www.semanticscholar.org/paper/b894d9ca8ea2d653bf1711a0c67dab71d054487c
11. Alexander Mager, Tommy Safran, H. Engelberg-Kulka (2021). Intracellular Localization of the Proteins Encoded by Some Type II Toxin-Antitoxin Systems in Escherichia coli. mBio. https://www.semanticscholar.org/paper/3400981ba961c43f50e703afa6b9a869aeefbb69
12. Christina M McCosker, E. Unal, Alayna K Gigliotti, Wendy B Puryear, Jonathan A. Runstadler et al. (2025). Molecular mechanisms underlying response to influenza in grey seals (Halichoerus grypus), a potential wild reservoir. Molecular ecology. https://www.semanticscholar.org/paper/bebb135aae1c1182d098fce839c9a3df0cfb2b21
13. Yunxue Guo, Jianyun Yao, Chenglong Sun, Zhongling Wen, Xiaoxue Wang (2016). Characterization of the Deep-Sea Streptomyces sp. SCSIO 02999 Derived VapC/VapB Toxin-Antitoxin System in Escherichia coli. Toxins. https://www.semanticscholar.org/paper/ba38f6ce608d862163fee287c086e7c988bb9d45