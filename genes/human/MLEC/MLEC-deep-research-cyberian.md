---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T06:50:12.784750'
end_time: '2026-01-23T07:17:58.348197'
duration_seconds: 1665.56
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: MLEC
  gene_symbol: MLEC
  uniprot_accession: Q14165
  protein_description: 'RecName: Full=Malectin {ECO:0000305}; Flags: Precursor;'
  gene_info: Name=MLEC {ECO:0000312|HGNC:HGNC:28973}; Synonyms=KIAA0152;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the malectin family. .
  protein_domains: Malectin_dom. (IPR021720); MLEC. (IPR039155); Malectin (PF11721)
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
- **UniProt Accession:** Q14165
- **Protein Description:** RecName: Full=Malectin {ECO:0000305}; Flags: Precursor;
- **Gene Information:** Name=MLEC {ECO:0000312|HGNC:HGNC:28973}; Synonyms=KIAA0152;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the malectin family. .
- **Key Domains:** Malectin_dom. (IPR021720); MLEC. (IPR039155); Malectin (PF11721)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MLEC" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MLEC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MLEC** (gene ID: MLEC, UniProt: Q14165) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Malectin (MLEC): A Comprehensive Research Report

## Introduction and Summary

Malectin is an endoplasmic reticulum (ER)-resident type I membrane protein that functions as a carbohydrate-binding lectin with remarkable specificity for diglucosylated high-mannose N-glycans. First identified in *Xenopus laevis* and subsequently characterized in humans (where it corresponds to the previously uncharacterized gene KIAA0152), malectin represents a critical component of the ER glycoprotein quality control machinery [schallus-2008-malectin-fulltext]. The human protein, encoded by the MLEC gene (UniProt Q14165), comprises 292 amino acids including an N-terminal signal peptide (residues 1-26), a conserved lectin-like carbohydrate-binding domain (residues 27-213), and a C-terminal transmembrane anchor (residues 255-274) that tethers the protein to the ER membrane with its functional domain oriented toward the ER lumen [schallus-2008-malectin-fulltext][yang-2021-malectin-review-abstract].

The primary molecular function of malectin centers on its highly selective recognition of the Glc2Man9GlcNAc2 (G2M9) N-glycan intermediate, a transient structure generated during the early processing of N-linked oligosaccharides. This specificity positions malectin as an early checkpoint in the glycoprotein folding pathway, functioning upstream of and in parallel to the well-characterized calnexin/calreticulin chaperone system [galli-2011-backup-qc-fulltext][chen-2011-qc-alpha1at-abstract]. Rather than serving as a classical chaperone itself, malectin operates as a surveillance factor that preferentially associates with misfolded glycoproteins and facilitates their retention in the ER and subsequent degradation via the ER-associated degradation (ERAD) pathway.

## Molecular Structure and Carbohydrate Recognition

### Domain Architecture

The three-dimensional structure of the malectin carbohydrate-binding domain was determined by nuclear magnetic resonance (NMR) spectroscopy, revealing a compact globular fold consisting of two elongated beta-sheets packed against each other, flanked by three alpha-helices [schallus-2008-malectin-fulltext]. This architecture represents a novel type of carbohydrate recognition domain that shares structural similarity with prokaryotic carbohydrate-binding modules found in polysaccharide hydrolases, despite limited sequence conservation. The atomic coordinates have been deposited in the Protein Data Bank as entries 2JWP (free protein) and 2K46 (malectin-nigerose complex) [schallus-2008-malectin-fulltext].

The carbohydrate-binding site is located at one face of the domain and is characterized by a distinctive aromatic cage formed by four residues: tyrosines Y67, Y89, and Y116, along with phenylalanine F117 [schallus-2008-malectin-fulltext]. This aromatic sandwich mechanism, in which glucose residues stack against the aromatic side chains through CH-pi interactions, is a common strategy employed by carbohydrate-binding proteins. An additional hydrogen bond from aspartate D186 provides further ligand stabilization.

### Substrate Specificity

Carbohydrate microarray analyses using 335 diverse oligosaccharide probes demonstrated extraordinarily selective binding of malectin specifically to glucose-terminating oligosaccharides, with by far the strongest interaction observed with the diglucosylated Glc2-N-glycan probe [schallus-2008-malectin-fulltext]. Quantitative binding studies established dissociation constants of 26.3 micromolar for nigerose (glucose-alpha-1,3-glucose), 50 micromolar for maltose (glucose-alpha-1,4-glucose), and 210 micromolar for kojibiose (glucose-alpha-1,2-glucose), while glucose monomers showed insufficient affinity for reliable determination [schallus-2008-malectin-fulltext]. The preference for nigerose is significant because the alpha-1,3-linked diglucose motif (Glc-alpha-1,3-Glc) corresponds to the innermost two glucose residues of the Glc3Man9GlcNAc2 oligosaccharide precursor that remains after cleavage of the terminal alpha-1,2-linked glucose by glucosidase I.

Human malectin binds specifically to the physiologically relevant G2M9 N-glycan with an association constant (Ka) of 1.97 x 10^5 M^-1, while binding to Glc1Man9GlcNAc2 (G1M9), Glc3Man9GlcNAc2 (G3M9), and other N-glycan structures is barely detectable [chen-2011-qc-alpha1at-abstract]. The structural basis for this selectivity has been elucidated: the axial orientation of the C-2 hydroxyl group in mannose (versus the equatorial position in glucose) would sterically clash with Y116 and F117, thereby excluding monoglucosylated structures. Similarly, the terminal glucose of the triglucosylated precursor would sterically prevent the middle glucose from properly occupying the binding pocket [schallus-2008-malectin-fulltext].

## Subcellular Localization and Membrane Topology

Malectin is an integral membrane protein of the endoplasmic reticulum, as established through immunofluorescence colocalization studies showing strong overlap with the canonical ER marker calnexin [schallus-2008-malectin-fulltext][galli-2011-backup-qc-fulltext]. The protein adopts a type I membrane topology, with its N-terminal signal peptide directing cotranslational insertion into the ER membrane and a single C-terminal transmembrane helix anchoring it in place while the large luminal domain protrudes into the ER lumen where it can access nascent glycoproteins [galli-2011-backup-qc-fulltext].

Deletion of the N-terminal signal peptide (residues 1-26) results in cytoplasmic localization of malectin, confirming the essential role of this sequence in ER targeting [schallus-2008-malectin-fulltext]. The short cytoplasmic tail lacks any recognized ER retention signals, suggesting that retention may be mediated through interactions with other ER-resident proteins, particularly the oligosaccharyltransferase (OST) complex via ribophorin I [qin-2012-ribophorin-abstract].

## Tissue Expression and Mouse Phenotypes

### Expression Pattern

According to the Human Protein Atlas, MLEC is broadly expressed across human tissues, including expression in the mucosa of the sigmoid colon, corpus epididymis, pancreatic ductal cells, and over 218 other cell types or tissues [human-protein-atlas]. The gene shows particularly high expression in peripheral blood mononuclear cells. This widespread expression pattern is consistent with malectin's fundamental role in ER glycoprotein quality control, a process essential in all secretory cells. The original discovery studies in *Xenopus laevis* similarly documented broad expression across adult tissues including liver, pancreas, and multiple other organs [schallus-2008-malectin-fulltext].

### Mouse Knockout Phenotypes

The International Mouse Phenotyping Consortium (IMPC) has characterized Mlec knockout mice, revealing that loss of malectin is not embryonic lethal but does result in measurable phenotypes affecting three physiological systems: homeostasis/metabolism, growth/size/body region, and skeleton [impc-mlec]. Out of 24 physiological systems evaluated, 17 were tested, with 3 showing significant phenotypic impacts and 14 showing no significant changes. These relatively mild phenotypes suggest that while malectin contributes to glycoprotein quality control, compensatory mechanisms (possibly through the calnexin/calreticulin system) can partially substitute for its loss under normal physiological conditions. The phenotypes observed may reflect situations where the quality control burden exceeds the capacity of backup systems, or tissues with particularly high secretory loads.

## Role in N-Glycoprotein Quality Control

### The N-Glycan Processing Pathway

Protein N-glycosylation begins in the ER when the oligosaccharyltransferase (OST) complex transfers a preassembled 14-sugar glycan composed of three glucoses, nine mannoses, and two N-acetylglucosamines (Glc3Man9GlcNAc2) to asparagine residues within the Asn-X-Ser/Thr consensus sequence of nascent polypeptides [schallus-2008-malectin-fulltext]. Following transfer, the glycan undergoes sequential processing by ER-resident glucosidases. Glucosidase I removes the terminal alpha-1,2-linked glucose to generate the G2M9 intermediate, which is then the substrate for malectin. Glucosidase II subsequently cleaves the two remaining alpha-1,3-linked glucose residues in a sequential manner, first generating the G1M9 intermediate and ultimately the Man9GlcNAc2 product [schallus-2008-malectin-fulltext][chen-2011-qc-alpha1at-abstract].

### Malectin as a Quality Control Factor

Malectin functions as an ER stress-responsive backup quality control mechanism that operates parallel to, rather than within, the classical calnexin/calreticulin chaperone cycle [galli-2011-backup-qc-fulltext]. Several lines of evidence support this model. First, malectin expression is upregulated approximately two-fold upon induction of ER stress by agents such as thapsigargin, alongside other established ER stress markers [galli-2011-backup-qc-fulltext]. Second, while calnexin binds nascent glycoproteins early in their biosynthesis (engaging with monoglucosylated G1M9 structures), malectin shows delayed binding kinetics and preferentially associates with misfolded conformers [galli-2011-backup-qc-fulltext].

Studies using influenza hemagglutinin (HA), an obligate calnexin client protein, demonstrated that malectin associates approximately 20 minutes after synthesis initiation, substantially later than calnexin engagement [galli-2011-backup-qc-fulltext]. Importantly, malectin preferentially associated with disulfide-bonded aggregates and misfolded HA conformers rather than properly folding intermediates. This selectivity for misfolded substrates was further confirmed using alpha-1-antitrypsin variants, where human malectin stably interacted with the misfolded ATNHK variant (carrying the Null Hong Kong mutation) but not with wild-type alpha-1-antitrypsin, and this interaction occurred via G2M9 glycans [chen-2011-qc-alpha1at-abstract].

### Mechanism of Misfolded Protein Recognition

A central question in understanding malectin function concerns how it distinguishes misfolded from properly folded glycoproteins when both carry G2M9 glycans early in their biosynthesis. The answer lies in the formation of a functional complex between malectin and ribophorin I (RPN1), a subunit of the oligosaccharyltransferase complex [qin-2012-ribophorin-abstract]. Proteomic analyses identified ribophorin I as a stable binding partner of malectin, with the interaction occurring independently of malectin's glycan-binding activity. The interaction is mediated through the transmembrane domain and/or cytoplasmic tail of malectin, as truncated malectin lacking these regions fails to co-precipitate with ribophorin I [qin-2012-ribophorin-abstract].

Ribophorin I contributes chaperone-like function to the complex, preferentially binding misfolded or scrambled proteins through recognition of exposed hydrophobic patches [qin-2012-ribophorin-abstract]. Co-expression of malectin and ribophorin I significantly enhanced the association between malectin and the misfolded ATNHK variant while having no effect on properly folded proteins. This dual recognition mechanism, combining malectin's glycan-binding specificity with ribophorin I's ability to recognize aberrant protein conformations, provides the selectivity necessary for effective quality control [qin-2012-ribophorin-abstract].

### Coordination with Glucosidase II

The relationship between malectin and glucosidase II represents a critical regulatory node in the N-glycan processing pathway. Glucosidase II is a heterodimeric enzyme consisting of a catalytic alpha subunit (GIIα) and a regulatory beta subunit (GIIβ) that contains a mannose-6-phosphate receptor homology (MRH) domain. This enzyme catalyzes the sequential removal of the two inner alpha-1,3-linked glucose residues from G2M9, first generating G1M9 and then Man9GlcNAc2 [schallus-2008-malectin-fulltext]. Current models suggest that malectin and glucosidase II may coordinately select misfolded proteins at an early stage of glycoprotein biosynthesis. When properly folding glycoproteins are released from malectin, the G2M9 glycan becomes accessible to glucosidase II, allowing efficient glucose trimming and progression to the calnexin/calreticulin cycle. However, on misfolded glycoproteins, inefficient trimming by glucosidase II may maintain the G2M9 structure, prolonging association with malectin and facilitating eventual targeting to ERAD [chen-2011-qc-alpha1at-abstract].

### Integration with ERAD

The interaction of misfolded glycoproteins with malectin results in their enhanced degradation through the ER-associated degradation (ERAD) pathway and prevents their secretion [chen-2011-qc-alpha1at-abstract]. Overexpression of malectin dramatically inhibited the secretion of ATNHK, and this inhibitory effect was abolished by treatment with the proteasome inhibitor MG132, indicating that malectin guides misfolded substrates toward proteasome-mediated degradation [chen-2011-qc-alpha1at-abstract]. Interestingly, malectin itself has been identified as an ERAD substrate of the SEL1L-HRD1 complex, suggesting that its own levels are subject to quality control regulation.

## Association with the Oligosaccharyltransferase Complex

Cryo-electron microscopy structural studies of human OST complexes have revealed that malectin is a substoichiometric component that associates with both OST-A (containing STT3A, coupled to cotranslational glycosylation) and OST-B (containing STT3B, mediating posttranslational glycosylation) [ramirez-2019-ost-cryoem-abstract]. Strong density consistent with a transmembrane helix and a short luminal stretch of malectin was observed in proximity to TMEM258 and the luminal domain of ribophorin I, confirming direct physical association [ramirez-2019-ost-cryoem-abstract]. This positioning places malectin in an optimal location to encounter newly synthesized glycoproteins immediately after they receive their oligosaccharide modification.

The tight linkage between malectin and the OST complex is functionally significant. By associating with ribophorin I at the site of glycan transfer, malectin can perform early surveillance of glycoprotein folding status. This proximity may also explain the original proposal that malectin might recruit glucosidase II to G2M9 substrates, potentially regulating the rate of glucose trimming and thereby controlling entry into the calnexin/calreticulin cycle [schallus-2008-malectin-fulltext].

## Evolutionary Conservation

Database searches have identified malectin homologues across animal species, with generally one copy per proteome [schallus-2008-malectin-fulltext]. The aligned animal proteins display colinear modular architecture, including the conserved hydrophobic N- and C-terminal segments [schallus-2008-malectin-fulltext]. PSI-BLAST analyses revealed highly divergent malectin-homologous domains in plant receptor-like kinases and in certain ciliates and apicomplexan parasites, though these occur in different modular contexts [schallus-2008-malectin-fulltext][yang-2021-malectin-review-abstract].

Notably, malectin is absent from most fungi and many plants despite their utilization of N-glycosylation pathways similar to animals [schallus-2008-malectin-fulltext]. Plants have evolved an expanded repertoire of malectin-like (ML) domain proteins, with over 3,400 ML domains identified across 121 plant species (averaging approximately 60 per species) [yang-2021-malectin-review-abstract]. These plant ML domain proteins function in different contexts, often as receptor-like kinases involved in cell wall sensing, stress responses, and developmental signaling rather than ER quality control.

## Disease Associations and Pathophysiological Relevance

### Hepatocellular Carcinoma

Recent research has demonstrated aberrant upregulation of malectin in human hepatocellular carcinoma (HCC) tissues and cell lines compared to matched normal controls [dong-2025-hcc-abstract]. CRISPR-Cas9-mediated knockout of malectin in HCC cell lines (HepG2 and QGY-7703) significantly suppressed colony formation, migration, and invasion without affecting basic cell proliferation rates. Tumor growth was notably reduced in nude mice implanted with malectin-deficient cells, suggesting an oncogenic role for this protein in HCC development [dong-2025-hcc-abstract]. The mechanistic basis for this tumor-promoting function likely relates to the increased burden of misfolded glycoproteins in rapidly proliferating cancer cells and the general upregulation of ER quality control pathways under conditions of chronic ER stress characteristic of tumor microenvironments.

### Viral Infection

Malectin has emerged as a host factor that promotes coronavirus replication [davies-2024-coronavirus-abstract]. Quantitative proteomics and functional genetic screening identified malectin as a conserved interactor of coronavirus nonstructural proteins nsp2 and nsp4. Knockdown of malectin significantly reduced infectious titers of murine hepatitis virus (MHV), with effects surpassing those observed for receptor knockout [davies-2024-coronavirus-abstract]. Mechanistically, malectin promotes early replicase protein production; its depletion specifically impairs nonstructural protein synthesis, which subsequently reduces viral genome replication and structural protein production.

The pro-viral function of malectin operates through its canonical role in the N-linked glycosylation pathway. Treatment with NGI-1, an OST complex inhibitor, showed no additive effect when combined with malectin knockdown, confirming that malectin acts through the glycoprotein quality control mechanism [davies-2024-coronavirus-abstract]. Beyond MHV, malectin knockdown suppressed SARS-CoV-2 replication to 41-43% of wild-type levels for both Delta and Omicron variants, establishing malectin as a potential target for pan-coronavirus antivirals [davies-2024-coronavirus-abstract].

## Summary of Biochemical Pathway

The primary biochemical function of malectin can be summarized as follows:

1. **N-glycan attachment**: OST transfers Glc3Man9GlcNAc2 to nascent polypeptides
2. **Initial processing**: Glucosidase I removes terminal glucose to generate G2M9
3. **Malectin engagement**: Malectin, in complex with ribophorin I at the OST, binds G2M9-bearing glycoproteins
4. **Quality assessment**: Ribophorin I assesses protein folding status via hydrophobic patch recognition
5. **Fate determination**:
   - Properly folding proteins proceed to glucosidase II cleavage and the calnexin/calreticulin cycle
   - Misfolded proteins are retained by malectin-ribophorin I complex and directed to ERAD

Under normal conditions, malectin binding is transient as proteins rapidly progress through the folding pathway. Under ER stress, malectin expression increases and the lectin more persistently associates with accumulating misfolded substrates, serving as a backup retention system to prevent secretion of aberrant glycoproteins.

## Open Questions

Several important questions remain regarding malectin biology:

1. **Regulation of glucosidase II activity**: While the original discovery paper proposed that malectin might recruit glucosidase II to G2M9 substrates, the molecular details of this potential interaction remain unclear. Whether malectin actively promotes or inhibits the second glucose trimming step, and how this might be regulated, warrants further investigation.

2. **Mechanisms of ER retention**: Malectin lacks canonical ER retention signals. Whether its retention depends entirely on interactions with ribophorin I and the OST complex, or whether additional mechanisms contribute, is not fully established.

3. **Tissue-specific functions**: While malectin is broadly expressed and IMPC knockout mice show phenotypes in homeostasis, growth, and skeletal systems, the specific molecular mechanisms underlying these phenotypes remain unclear. Conditional deletion studies in specific tissues would help determine where malectin function is most critical and whether phenotypes reflect direct quality control defects or secondary metabolic consequences.

4. **Therapeutic targeting**: Given malectin's role in promoting coronavirus replication and potentially tumor progression, it may represent a therapeutic target. However, the consequences of inhibiting this quality control pathway for normal cellular physiology need careful evaluation.

5. **Interaction with other quality control factors**: How malectin coordinates with other ER lectins (EDEM1, OS-9, XTP3-B) and the timing of substrate handoff to downstream ERAD components requires further mechanistic characterization.

6. **Structural basis of ribophorin I interaction**: While the malectin transmembrane domain and cytoplasmic tail are implicated in ribophorin I binding, high-resolution structures of the complete complex would illuminate the molecular details of this interaction.

## References

- [schallus-2008-malectin-fulltext] Schallus T, Jaeckh C, Fehér K, Palma AS, Liu Y, Simpson JC, Mackeen M, Stier G, Gibson TJ, Feizi T, Pieler T, Muhle-Goll C. Malectin: a novel carbohydrate-binding protein of the endoplasmic reticulum and a candidate player in the early steps of protein N-glycosylation. Mol Biol Cell. 2008 Aug;19(8):3404-14. doi: 10.1091/mbc.e08-04-0354. PMID: 18524852; PMCID: PMC2488313. https://pmc.ncbi.nlm.nih.gov/articles/PMC2488313/

- [galli-2011-backup-qc-fulltext] Galli C, Bernasconi R, Soldà T, Calber V, Molinari M. Malectin participates in a backup glycoprotein quality control pathway in the mammalian ER. PLoS One. 2011 Jan 20;6(1):e16304. doi: 10.1371/journal.pone.0016304. PMID: 21283690; PMCID: PMC3027649. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0016304

- [chen-2011-qc-alpha1at-abstract] Chen Y, Hu D, Yabe R, Tateno H, Qin SY, Matsumoto N, Hirabayashi J, Yamamoto K. Role of malectin in Glc(2)Man(9)GlcNAc(2)-dependent quality control of α1-antitrypsin. Mol Biol Cell. 2011 Oct;22(19):3559-70. doi: 10.1091/mbc.E11-03-0201. PMID: 21813736; PMCID: PMC3183012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3183012/

- [qin-2012-ribophorin-abstract] Qin SY, Hu D, Matsumoto K, Takeda K, Matsumoto N, Yamaguchi Y, Yamamoto K. Malectin forms a complex with ribophorin I for enhanced association with misfolded glycoproteins. J Biol Chem. 2012 Nov 2;287(45):38080-9. doi: 10.1074/jbc.M112.394288. PMID: 22988243; PMCID: PMC3488078. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3488078/

- [ramirez-2019-ost-cryoem-abstract] Ramírez AS, Kowal J, Locher KP. Cryo-electron microscopy structures of human oligosaccharyltransferase complexes OST-A and OST-B. Science. 2019 Dec 13;366(6471):1372-1375. doi: 10.1126/science.aaz3505. PMID: 31831667. https://www.science.org/doi/10.1126/science.aaz3505

- [yang-2021-malectin-review-abstract] Yang H, Cheung AY. Malectin/Malectin-like domain-containing proteins: A repertoire of cell surface molecules with broad functional potential. Cell Surf. 2021 Jun 24;7:100056. doi: 10.1016/j.tcsw.2021.100056. PMID: 34258419; PMCID: PMC8287233. https://pmc.ncbi.nlm.nih.gov/articles/PMC8287233/

- [dong-2025-hcc-abstract] Dong Y, Fu MF, Liu SM, Yu HY, Ge XX, Zhang L, Hu D, Qin SY. Malectin, an endoplasmic reticulum-resident lectin, promotes malignant behavior of human hepatocellular carcinoma. Glycobiology. 2025;35(4):cwaf007. doi: 10.1093/glycob/cwaf007. PMID: 39987555. https://academic.oup.com/glycob/advance-article-abstract/doi/10.1093/glycob/cwaf007/8030605

- [davies-2024-coronavirus-abstract] Davies JP, Plate L. The glycoprotein quality control factor Malectin promotes coronavirus replication and viral protein biogenesis. bioRxiv. 2024 Jun 3;2024.06.02.597051. doi: 10.1101/2024.06.02.597051. PMID: 38895409. https://elifesciences.org/reviewed-preprints/100834

- [human-protein-atlas] Human Protein Atlas. MLEC - Tissue expression summary. ENSG00000110917. https://www.proteinatlas.org/ENSG00000110917-MLEC/tissue

- [impc-mlec] International Mouse Phenotyping Consortium. Mlec - malectin mouse gene. MGI:1924015. https://www.mousephenotype.org/data/genes/MGI:1924015


## Citations

1. chen-2011-qc-alpha1at-abstract.md
2. chen-2011-qc-alpha1at-summary.md
3. davies-2024-coronavirus-abstract.md
4. dong-2025-hcc-abstract.md
5. galli-2011-backup-qc-fulltext.md
6. galli-2011-backup-qc-summary.md
7. human-protein-atlas-mlec.md
8. impc-mlec-phenotypes.md
9. qin-2012-ribophorin-abstract.md
10. qin-2012-ribophorin-summary.md
11. ramirez-2019-ost-cryoem-abstract.md
12. schallus-2008-malectin-fulltext.md
13. schallus-2008-malectin-summary.md
14. yang-2021-malectin-review-abstract.md