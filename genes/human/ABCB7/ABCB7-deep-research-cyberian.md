---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T12:50:38.651983'
end_time: '2026-01-15T13:07:39.928392'
duration_seconds: 1021.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ABCB7
  gene_symbol: ABCB7
  uniprot_accession: O75027
  protein_description: 'RecName: Full=Iron-sulfur clusters transporter ABCB7, mitochondrial
    {ECO:0000305}; AltName: Full=ATP-binding cassette sub-family B member 7, mitochondrial
    {ECO:0000305}; AltName: Full=ATP-binding cassette transporter 7; Short=ABC transporter
    7 protein; Flags: Precursor;'
  gene_info: Name=ABCB7 {ECO:0000312|HGNC:HGNC:48}; Synonyms=ABC7;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the ABC transporter superfamily. ABCB family.
  protein_domains: AAA+_ATPase. (IPR003593); ABC1_TM_dom. (IPR011527); ABC1_TM_sf.
    (IPR036640); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS.
    (IPR017871)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 17
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O75027
- **Protein Description:** RecName: Full=Iron-sulfur clusters transporter ABCB7, mitochondrial {ECO:0000305}; AltName: Full=ATP-binding cassette sub-family B member 7, mitochondrial {ECO:0000305}; AltName: Full=ATP-binding cassette transporter 7; Short=ABC transporter 7 protein; Flags: Precursor;
- **Gene Information:** Name=ABCB7 {ECO:0000312|HGNC:HGNC:48}; Synonyms=ABC7;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the ABC transporter superfamily. ABCB family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC1_TM_dom. (IPR011527); ABC1_TM_sf. (IPR036640); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ABCB7" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ABCB7' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ABCB7** (gene ID: ABCB7, UniProt: O75027) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ABCB7: The Mitochondrial Iron-Sulfur Cluster Exporter

## Introduction

ABCB7 (ATP-binding cassette sub-family B member 7) is a mitochondrial transporter protein that plays an essential role in cellular iron-sulfur (Fe-S) cluster biogenesis. This 752-amino acid protein belongs to the ABC transporter superfamily and functions as a homodimeric half-transporter localized to the inner mitochondrial membrane [shimada-1998-habc7-cloning-abstract]. The primary function of ABCB7 is to export a sulfur-containing compound from the mitochondrial matrix to the cytosol, which is essential for the maturation of cytosolic and nuclear Fe-S proteins [kispal-1999-atm1-nfs1-abstract]. ABCB7 is the human ortholog of the yeast Saccharomyces cerevisiae protein Atm1 (ABC transporter of mitochondria 1), and the two proteins share approximately 49% sequence identity [shimada-1998-habc7-cloning-abstract]. Mutations in ABCB7 cause X-linked sideroblastic anemia with cerebellar ataxia (XLSA/A), a rare hereditary disorder characterized by mitochondrial iron accumulation, defective heme synthesis, and neurological dysfunction [allikmets-1999-abc7-xlsa-abstract].

The biogenesis of cellular Fe-S proteins represents what is now understood to be the essential and minimal function of mitochondria in eukaryotic cells [lill-freibert-2020-mitochondrial-fes-review-abstract]. Iron-sulfur clusters are ancient cofactors essential for the activity of numerous enzymes involved in DNA replication and repair, protein translation, cellular respiration, and many other fundamental processes [braymer-lill-2017-fes-trafficking-abstract]. ABCB7 occupies a critical position in this pathway, serving as the bridge between the mitochondrial iron-sulfur cluster assembly (ISC) machinery and the cytosolic iron-sulfur protein assembly (CIA) machinery.

## Protein Structure and Domain Organization

ABCB7 is classified as a half-transporter, meaning it contains a single transmembrane domain (TMD) with six membrane-spanning alpha-helices followed by a nucleotide-binding domain (NBD) containing the characteristic Walker A and Walker B motifs, as well as the ABC signature sequence [shimada-1998-habc7-cloning-abstract]. To form a functional transporter, two ABCB7 monomers must dimerize, creating a homodimeric complex with two TMDs and two NBDs. The protein contains an N-terminal mitochondrial targeting sequence that is unusually long compared to typical mitochondrial proteins, directing the nascent polypeptide to the inner mitochondrial membrane where the mature protein is inserted with the NBDs facing the mitochondrial matrix [yan-2022-human-abcb7-cryoem-abstract].

Recent cryo-electron microscopy studies have provided detailed structural information about ABCB7. The structure of AMP-PNP-bound human ABCB7 reveals an inverted V-shaped homodimeric architecture with an inward-facing open conformation [yan-2022-human-abcb7-cryoem-abstract]. In this state, one AMP-PNP molecule and Mg2+ ion are bound in each nucleotide-binding domain. Complementary structural studies of CtAtm1, a fungal ortholog of human ABCB7, determined by cryo-EM at resolutions between 2.8-3.2 Å, have captured multiple conformational states during the transport cycle [li-2022-ctatm1-cryoem-abstract]. These structures reveal that the inward-open configuration represents the resting state, in which the transporter exposes a highly electropositive cleft to the inside of the mitochondrial matrix, ready to accept negatively charged substrate molecules.

Crystal structures of yeast Atm1 determined at 3.06-3.38 Å resolution in both nucleotide-free and glutathione-bound states have provided additional mechanistic insights [srinivasan-2014-atm1-crystal-abstract]. The glutathione binding site is located near the inner membrane surface within a large cavity and includes a residue (corresponding to human E433) that is mutated in XLSA/A patients. The two ATP binding domains in the dimer are held together by strong interaction of the C-terminal helices, a stabilization mechanism that may be common to all ABC exporters.

## Substrate Specificity and Transport Mechanism

The precise nature of the substrate transported by ABCB7 has been the subject of intensive investigation and some debate. The prevailing model, supported by substantial biochemical and structural evidence, holds that ABCB7 exports glutathione-coordinated [2Fe-2S] clusters from the mitochondrial matrix to the cytosol [qi-2014-gsh-fes-model-abstract][li-2015-gsh-fes-viable-substrate-abstract]. In this model, mitochondrial glutathione abstracts a [2Fe-2S] cluster core from the mitochondrial ISC machinery (likely from the scaffold protein ISU/ISCU), forming a [2Fe-2S](GS)4 complex. This negatively charged complex is then transported through the inner mitochondrial membrane by ABCB7 in an ATP-dependent manner, and the exported cluster is subsequently delivered to the cytosolic CIA machinery for insertion into target apoproteins.

The evidence supporting this model comes from multiple lines of investigation. Biochemical studies demonstrated that glutathione-bound [2Fe-2S] clusters substantially increase the ATPase activity of ABCB7-type transporters, with a dissociation constant (KD) of approximately 68 μM [qi-2014-gsh-fes-model-abstract]. Transport assays using proteoliposome-reconstituted protein confirmed that glutathione-coordinated [2Fe-2S] clusters can serve as viable physiological substrates [li-2015-gsh-fes-viable-substrate-abstract]. Structural modeling identified a potential substrate-binding site composed of a conserved arginine-rich region (Arg313, Arg315, Arg317, Arg319 in human ABCB7) that forms a positively-charged pocket capable of binding the negatively charged cluster complex [qi-2014-gsh-fes-model-abstract].

An alternative hypothesis proposes that ABCB7 exports glutathione polysulfides rather than intact Fe-S clusters [schaedler-2014-gsh-polysulfide-abstract]. Studies using a transportomics approach with mass spectrometry identified glutathione trisulfide (GS-S-SG) as a transported substrate, and demonstrated that the plant homolog ATM3 and yeast Atm1 selectively transport glutathione disulfide (GSSG) but not reduced glutathione. According to this model, the exported glutathione polysulfides contain persulfide (sulfane sulfur) that serves as the sulfur source for both Fe-S cluster and molybdenum cofactor (Moco) biosynthesis in the cytosol. This hypothesis accounts for the observation that ABCB7-type transporters are required not only for cytosolic Fe-S protein maturation but also for Moco synthesis.

The transport mechanism follows the classical alternating access model for ABC transporters. In the resting inward-open state, the transporter exposes a highly electropositive cleft to the mitochondrial matrix, allowing negatively charged substrates to associate [li-2022-ctatm1-cryoem-abstract]. Substrate binding triggers conformational changes that progress through partially occluded and fully occluded states, coupled to ATP binding and hydrolysis. The binding region becomes internalized and partially divided during the transport cycle, ultimately releasing the substrate to the intermembrane space side of the membrane.

## Cellular Localization and Pathway Context

ABCB7 is localized to the inner mitochondrial membrane with its nucleotide-binding domains facing the mitochondrial matrix [shimada-1998-habc7-cloning-abstract][yan-2022-human-abcb7-cryoem-abstract]. This topology is consistent with its proposed function as an exporter, moving substrates from the matrix to the intermembrane space/cytosol. The protein is expressed ubiquitously across human tissues, with particularly high levels in heart, duodenum, and other metabolically active tissues.

ABCB7 functions as a critical link between two major cellular pathways for Fe-S protein maturation. The mitochondrial ISC (iron-sulfur cluster) machinery synthesizes Fe-S clusters de novo using iron, sulfur derived from cysteine via the cysteine desulfurase NFS1, and electrons from a dedicated electron transfer chain [lill-freibert-2020-mitochondrial-fes-review-abstract]. The initial [2Fe-2S] clusters are assembled on scaffold proteins (ISCU in humans) and can be directly inserted into mitochondrial target proteins or converted to [4Fe-4S] clusters for insertion into other mitochondrial recipients. However, the cytosol and nucleus also contain numerous essential Fe-S proteins, and these require a different maturation pathway.

The cytosolic iron-sulfur protein assembly (CIA) machinery consists of approximately eight proteins that assemble Fe-S clusters outside the mitochondria [braymer-lill-2017-fes-trafficking-abstract]. The CIA machinery depends on a sulfur-containing compound exported from mitochondria via ABCB7, often referred to as "X-S" because its precise identity remained uncertain for many years. The Reactome pathway database describes this process as occurring on a heterotetrameric scaffold composed of NUBP1 and NUBP2 subunits, with subsequent transfer of [4Fe-4S] clusters to target proteins like XPD and POLD1 via the CIA targeting complex (composed of NARFL, CIAO1, FAM96B, and MMS19).

Importantly, ABCB7 is not only required for cytosolic Fe-S protein maturation but also for proper iron homeostasis. Depletion of Atm1/ABCB7 leads to iron accumulation in mitochondria, deficiency of cytosolic Fe-S proteins, and dysregulation of cellular iron uptake [kispal-1999-atm1-nfs1-abstract]. This phenotype is related to the iron regulatory protein system: IRP1 (iron regulatory protein 1) can function either as cytosolic aconitase when bound to a [4Fe-4S] cluster, or as an RNA-binding protein that regulates iron metabolism genes when the cluster is absent. Loss of ABCB7 function impairs cytosolic Fe-S cluster assembly, causing IRP1 to shift toward its RNA-binding form and alter the expression of iron metabolism genes [pondarre-2006-abcb7-essential-abstract].

## Cytosolic Iron-Sulfur Target Proteins and DNA Metabolism

The cytosol and nucleus contain numerous essential Fe-S proteins whose maturation depends on ABCB7-mediated export. These target proteins play critical roles in DNA replication, repair, and genome maintenance, explaining why ABCB7 deficiency has profound effects on rapidly dividing cells. Among the most important cytosolic Fe-S proteins is IRP1 (iron regulatory protein 1), which functions as cytosolic aconitase when bound to a [4Fe-4S] cluster but switches to its RNA-binding form when the cluster is absent, thereby regulating iron metabolism genes. Loss of ABCB7 function causes IRP1 to adopt its RNA-binding form, leading to dysregulated expression of iron metabolism genes including transferrin receptor (increased) and ferritin (decreased).

DNA replication and repair enzymes represent another critical category of cytosolic Fe-S proteins affected by ABCB7 deficiency. The DNA polymerase delta catalytic subunit POLD1 contains a [4Fe-4S] cluster that is essential for its function and is inserted by the CIA targeting complex containing MMS19. Similarly, the DNA helicase XPD (xeroderma pigmentosum group D protein) requires a [4Fe-4S] cluster for its role in nucleotide excision repair and transcription. The Fe-S cluster in XPD is positioned in the core helicase domain and facilitates DNA damage recognition and repair. Other Fe-S cluster-containing DNA metabolism enzymes include the DNA2 nuclease/helicase, primase, and various DNA glycosylases involved in base excision repair.

The importance of ABCB7 for DNA replication has been directly demonstrated in studies of B cell development. Conditional deletion of Abcb7 in mice causes a severe block in bone marrow B cell development at the pro-B cell stage, where cells undergo rapid proliferation [lehrke-2021-abcb7-bcell-abstract]. ABCB7-deficient pro-B cells accumulate intracellular iron but do not undergo ferroptosis or apoptosis. Instead, they exhibit replication-induced DNA damage and slowed DNA replication, independent of VDJ recombination. Stimulated ABCB7-deficient splenic B cells also show marked proliferation defects and impaired class switch recombination, further linking Fe-S cluster availability to DNA metabolism and cell division.

## Role in Heme Biosynthesis and Erythropoiesis

Beyond its general role in Fe-S cluster export, ABCB7 has a particularly critical function in erythroid cells where it participates in a multiprotein complex required for heme biosynthesis [maio-2019-fech-abcb7-abcb10-complex-abstract]. Studies using chemical crosslinking and mass spectrometry identified a 480 kDa hexameric complex in which dimeric ferrochelatase physically bridges ABCB7 and ABCB10 homodimers in a 2:2:2 stoichiometry. Ferrochelatase is the terminal enzyme of heme biosynthesis, catalyzing the insertion of iron into protoporphyrin IX, and it is itself an Fe-S protein requiring [2Fe-2S] clusters for its activity and stability.

Two critical sequences in the C-terminus of ABCB7 (residues V450-L463 and G527-D538) mediate its interaction with ferrochelatase, while residues 90-115 of ferrochelatase engage the nucleotide-binding domain of ABCB7 [maio-2019-fech-abcb7-abcb10-complex-abstract]. Loss of ABCB7 function disrupts this complex and leads to ferrochelatase instability, contributing to the heme synthesis defect observed in XLSA/A patients. Interestingly, knockdown of ABCB7 causes loss of mitochondrial Fe-S proteins before affecting cytosolic Fe-S enzymes, and results in a profound hemoglobinization defect in erythroid cells through both translational repression of ALAS2 (the erythroid-specific isoform of aminolevulinic acid synthase, the first enzyme of heme synthesis) and ferrochelatase destabilization.

Studies in mice have demonstrated that Abcb7 is essential not only for erythropoiesis but for hematopoiesis in general [pondarre-2007-hematopoiesis-abstract]. Complete deletion of Abcb7 results in severe pancytopenia and death within approximately 16 days. The partial loss-of-function mutations that cause XLSA/A in humans inhibit heme biosynthesis by altering iron availability needed to synthesize heme from protoporphyrin IX. Mouse models carrying the E433K mutation, corresponding to the most severe human variant, develop siderocytes (iron-containing red blood cells) in peripheral blood and show abnormal mitochondria in reticulocytes with increased zinc protoporphyrin levels.

## Disease Associations: X-Linked Sideroblastic Anemia with Ataxia

Mutations in ABCB7 cause X-linked sideroblastic anemia with cerebellar ataxia (XLSA/A; OMIM 301310), a rare hereditary disorder first linked to this gene in 1999 [allikmets-1999-abc7-xlsa-abstract]. XLSA/A is characterized by moderate hypochromic microcytic anemia, elevated zinc protoporphyrin levels, the presence of ring sideroblasts in bone marrow (erythroblasts with iron-laden mitochondria surrounding the nucleus), and early-onset spinocerebellar ataxia [allikmets-1999-abc7-xlsa-abstract]. The neurological features include delayed walking, ataxia evident in early childhood, dysmetria, dysdiadochokinesis, and mild to moderately severe dysarthria. The ataxia is generally described as non-progressive or slowly progressive.

To date, five different missense mutations in ABCB7 have been identified in XLSA/A patients: E208D, I400M, V411L, E433K, and G682S [pearson-cowan-2020-e433k-mutation-abstract]. The first four mutations result in sideroblastic anemia with cerebellar ataxia, while the fifth mutation (G682S) causes ataxia without anemia, suggesting some degree of genotype-phenotype correlation. Structural mapping of these mutations reveals that they cluster in functionally important regions: E208D is located in the long TM2 helix on the matrix side, I400M is positioned between TM5 and TM6, V411L is in TM6, and E433K is in the substrate-binding pocket [pearson-cowan-2020-e433k-mutation-abstract].

The E433K mutation produces the most severe clinical phenotype and has been extensively characterized biochemically. Studies showed that this mutation reduces transport activity to just 3.5% of wild-type levels and abolishes ATPase stimulation by both glutathione and Fe-S cluster substrates [pearson-cowan-2020-e433k-mutation-abstract]. The carboxylate-bearing amino acid at position 433 is critical for coupling substrate binding in the TMD to conformational changes in the NBD required for ATP hydrolysis and transport. Introduction of the corresponding mutation into yeast Atm1 resulted in partial loss of function, demonstrating evolutionary conservation of this critical residue [allikmets-1999-abc7-xlsa-abstract].

The pathogenic mechanism in XLSA/A involves a buildup of iron in mitochondria (forming ring sideroblasts) coupled with deficiency of cytosolic Fe-S proteins [allikmets-1999-abc7-xlsa-abstract]. The mitochondrial iron accumulation likely results from dysregulated iron import when Fe-S cluster export is impaired, while the cytosolic Fe-S protein deficiency affects numerous essential enzymes. The particular sensitivity of erythroid cells may reflect their high demand for both Fe-S clusters (for ferrochelatase activity) and iron (for heme synthesis), while the cerebellar involvement likely relates to high ABCB7 expression in this tissue and the sensitivity of neurons to Fe-S protein deficiency.

## Evolutionary Conservation and Homologs

ABCB7 belongs to a highly conserved family of mitochondrial ABC transporters found throughout eukaryotes. The yeast ortholog Atm1 was first identified and characterized in the laboratory of Roland Lill, who demonstrated its essential role in cytosolic Fe-S protein biogenesis [kispal-1999-atm1-nfs1-abstract]. The human ABCB7 gene can complement yeast cells defective in Atm1, confirming functional conservation across this evolutionary distance [allikmets-1999-abc7-xlsa-abstract]. In plants, the ortholog is called ATM3 (in Arabidopsis thaliana), and it similarly functions in Fe-S cluster export and is additionally required for molybdenum cofactor synthesis.

The conservation extends to the substrate binding site and transport mechanism. Structural studies comparing yeast Atm1, fungal CtAtm1, and human ABCB7 reveal remarkable conservation of the glutathione binding pocket and the positively-charged substrate binding cavity [srinivasan-2014-atm1-crystal-abstract][li-2022-ctatm1-cryoem-abstract][yan-2022-human-abcb7-cryoem-abstract]. The arginine-rich motif involved in substrate binding is conserved from yeast to humans, as are the residues mutated in XLSA/A, emphasizing the critical importance of this region for transporter function.

## Open Questions

Despite significant advances in understanding ABCB7 function, several important questions remain unresolved:

1. **Precise substrate identity**: While substantial evidence supports glutathione-coordinated [2Fe-2S] clusters as the transported substrate, the alternative hypothesis proposing glutathione polysulfides has not been definitively excluded. The two models are not necessarily mutually exclusive, and it remains possible that ABCB7 can transport multiple related substrates. High-resolution structural studies capturing substrate-bound states of human ABCB7 would help resolve this question.

2. **Mechanism of substrate transfer**: How the exported cluster or sulfur compound is handed off from ABCB7 to the CIA machinery in the cytosol remains unclear. The identity of the immediate acceptor on the cytosolic side and the mechanistic details of this transfer process require further investigation.

3. **Tissue-specific requirements**: Why liver cells can survive Abcb7 deletion while most other tissues cannot [pondarre-2006-abcb7-essential-abstract] is not fully understood. This tissue specificity may reflect differences in Fe-S protein requirements, alternative pathways, or compensatory mechanisms.

4. **Neurological pathogenesis**: The mechanism underlying cerebellar ataxia in XLSA/A patients is incompletely understood. While ABCB7 is highly expressed in the cerebellum, the specific neuronal Fe-S proteins affected and the pathway leading to ataxia require further characterization.

5. **Regulatory mechanisms**: How ABCB7 expression and activity are regulated in response to cellular iron status and Fe-S cluster demand is not well characterized. Understanding this regulation could provide therapeutic targets for XLSA/A and related disorders.

6. **Interaction with other mitochondrial factors**: The ISC export machinery includes not only Atm1/ABCB7 but also the sulfhydryl oxidase Erv1 (human ALR) and glutathione. How these components cooperate in the export process and whether additional factors are involved remains to be fully elucidated.

## References

1. **[kispal-1999-atm1-nfs1-abstract]**: Kispal G, Csere P, Prohl C, Lill R. The mitochondrial proteins Atm1p and Nfs1p are essential for biogenesis of cytosolic Fe/S proteins. EMBO J. 1999 Jul 15;18(14):3981-9. PMID: 10406803; PMCID: PMC1171474; DOI: 10.1093/emboj/18.14.3981. https://pubmed.ncbi.nlm.nih.gov/10406803/

2. **[allikmets-1999-abc7-xlsa-abstract]**: Allikmets R, Raskind WH, Hutchinson A, Schueck ND, Dean M, Koeller DM. Mutation of a putative mitochondrial iron transporter gene (ABC7) in X-linked sideroblastic anemia and ataxia (XLSA/A). Hum Mol Genet. 1999 May;8(5):743-9. PMID: 10196363; DOI: 10.1093/hmg/8.5.743. https://pubmed.ncbi.nlm.nih.gov/10196363/

3. **[shimada-1998-habc7-cloning-abstract]**: Shimada Y, et al. Cloning and chromosomal mapping of a novel ABC transporter gene (hABC7), a candidate for X-linked sideroblastic anemia with spinocerebellar ataxia. J Hum Genet. 1998;43(2):115-22. PMID: 9621516; DOI: 10.1007/s100380050051. https://pubmed.ncbi.nlm.nih.gov/9621516/

4. **[pondarre-2006-abcb7-essential-abstract]**: Pondarré C, et al. The mitochondrial ATP-binding cassette transporter Abcb7 is essential in mice and participates in cytosolic iron-sulfur cluster biogenesis. Hum Mol Genet. 2006 Mar 15;15(6):953-64. PMID: 16467350; DOI: 10.1093/hmg/ddl012. https://pubmed.ncbi.nlm.nih.gov/16467350/

5. **[pondarre-2007-hematopoiesis-abstract]**: Pondarré C, et al. Abcb7, the gene responsible for X-linked sideroblastic anemia with ataxia, is essential for hematopoiesis. Blood. 2007 Apr 15;109(8):3567-9. PMID: 17192398; PMCID: PMC1852240; DOI: 10.1182/blood-2006-04-015768. https://pubmed.ncbi.nlm.nih.gov/17192398/

6. **[srinivasan-2014-atm1-crystal-abstract]**: Srinivasan V, Pierik AJ, Lill R. Crystal structures of nucleotide-free and glutathione-bound mitochondrial ABC transporter Atm1. Science. 2014 Mar 7;343(6175):1137-40. PMID: 24604199; DOI: 10.1126/science.1246729. https://pubmed.ncbi.nlm.nih.gov/24604199/

7. **[qi-2014-gsh-fes-model-abstract]**: Qi W, Li J, Cowan JA. A structural model for glutathione-complexed iron-sulfur cluster as a substrate for ABCB7-type transporters. Chem Commun (Camb). 2014 Apr 14;50(29):3795-8. PMID: 24584132; PMCID: PMC4052440; DOI: 10.1039/c3cc48239a. https://pubmed.ncbi.nlm.nih.gov/24584132/

8. **[li-2015-gsh-fes-viable-substrate-abstract]**: Li J, Cowan JA. Glutathione-coordinated [2Fe-2S] cluster: a viable physiological substrate for mitochondrial ABCB7 transport. Chem Commun (Camb). 2015 Feb 11;51(12):2253-5. PMID: 25556595; PMCID: PMC4522903; DOI: 10.1039/c4cc09175b. https://pubmed.ncbi.nlm.nih.gov/25556595/

9. **[schaedler-2014-gsh-polysulfide-abstract]**: Schaedler TA, et al. A conserved mitochondrial ATP-binding cassette transporter exports glutathione polysulfide for cytosolic metal cofactor assembly. J Biol Chem. 2014 Aug 22;289(34):23264-74. PMID: 25006243; PMCID: PMC4156053; DOI: 10.1074/jbc.M114.553438. https://pubmed.ncbi.nlm.nih.gov/25006243/

10. **[li-2022-ctatm1-cryoem-abstract]**: Li P, et al. Structures of Atm1 provide insight into [2Fe-2S] cluster export from mitochondria. Nat Commun. 2022 Jul 27;13(1):4339. PMID: 35896548; PMCID: PMC9329353; DOI: 10.1038/s41467-022-32006-8. https://pubmed.ncbi.nlm.nih.gov/35896548/

11. **[yan-2022-human-abcb7-cryoem-abstract]**: Yan Q, Shen Y, Yang X. Cryo-EM structure of AMP-PNP-bound human mitochondrial ATP-binding cassette transporter ABCB7. J Struct Biol. 2022 Mar;214(1):107832. PMID: 35041979; DOI: 10.1016/j.jsb.2022.107832. https://pubmed.ncbi.nlm.nih.gov/35041979/

12. **[pearson-cowan-2020-e433k-mutation-abstract]**: Pearson SA, Cowan JA. Evolution of the human mitochondrial ABCB7 [2Fe-2S](GS)4 cluster exporter and the molecular mechanism of an E433K disease-causing mutation. Arch Biochem Biophys. 2021 Jan 15;697:108661. PMID: 33157103; PMCID: PMC7785629; DOI: 10.1016/j.abb.2020.108661. https://pubmed.ncbi.nlm.nih.gov/33157103/

13. **[maio-2019-fech-abcb7-abcb10-complex-abstract]**: Maio N, et al. Dimeric ferrochelatase bridges ABCB7 and ABCB10 homodimers in an architecturally defined molecular complex required for heme biosynthesis. Haematologica. 2019 Sep;104(9):1756-1767. PMID: 30819913; PMCID: PMC6717594; DOI: 10.3324/haematol.2018.214320. https://haematologica.org/article/view/9042

14. **[lill-freibert-2020-mitochondrial-fes-review-abstract]**: Lill R, Freibert SA. Mechanisms of Mitochondrial Iron-Sulfur Protein Biogenesis. Annu Rev Biochem. 2020 Jun 20;89:471-499. PMID: 31935115; DOI: 10.1146/annurev-biochem-013118-111540. https://pubmed.ncbi.nlm.nih.gov/31935115/

15. **[braymer-lill-2017-fes-trafficking-abstract]**: Braymer JJ, Lill R. Iron-sulfur cluster biogenesis and trafficking in mitochondria. J Biol Chem. 2017 Aug 4;292(31):12754-12763. PMID: 28615445; PMCID: PMC5546016; DOI: 10.1074/jbc.R117.787101. https://pubmed.ncbi.nlm.nih.gov/28615445/

16. **[lehrke-2021-abcb7-bcell-abstract]**: Lehrke MJ, Shapiro MJ, Rajcula MJ, Kennedy MM, McCue SA, Medina KL, Shapiro VS. The mitochondrial iron transporter ABCB7 is required for B cell development, proliferation, and class switch recombination in mice. eLife. 2021 Nov 11;10:e69621. PMID: 34762046; PMCID: PMC8585479; DOI: 10.7554/eLife.69621. https://elifesciences.org/articles/69621


## Citations

1. allikmets-1999-abc7-xlsa-abstract.md
2. braymer-lill-2017-fes-trafficking-abstract.md
3. kispal-1999-atm1-nfs1-abstract.md
4. lehrke-2021-abcb7-bcell-abstract.md
5. li-2015-gsh-fes-viable-substrate-abstract.md
6. li-2022-ctatm1-cryoem-abstract.md
7. lill-freibert-2020-mitochondrial-fes-review-abstract.md
8. maio-2019-fech-abcb7-abcb10-complex-abstract.md
9. pearson-cowan-2020-e433k-mutation-abstract.md
10. pondarre-2006-abcb7-essential-abstract.md
11. pondarre-2007-hematopoiesis-abstract.md
12. qi-2014-gsh-fes-model-abstract.md
13. rouault-tong-2008-fes-disease-review-abstract.md
14. schaedler-2014-gsh-polysulfide-abstract.md
15. shimada-1998-habc7-cloning-abstract.md
16. srinivasan-2014-atm1-crystal-abstract.md
17. yan-2022-human-abcb7-cryoem-abstract.md