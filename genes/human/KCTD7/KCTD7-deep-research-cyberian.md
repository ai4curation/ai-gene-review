---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T20:54:54.401878'
end_time: '2026-01-22T21:08:54.376483'
duration_seconds: 839.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KCTD7
  gene_symbol: KCTD7
  uniprot_accession: Q96MP8
  protein_description: 'RecName: Full=BTB/POZ domain-containing protein KCTD7;'
  gene_info: Name=KCTD7;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: BTB/POZ_dom. (IPR000210); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB.
    (IPR003131); BTB_2 (PF02214)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q96MP8
- **Protein Description:** RecName: Full=BTB/POZ domain-containing protein KCTD7;
- **Gene Information:** Name=KCTD7;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** BTB/POZ_dom. (IPR000210); SKP1/BTB/POZ_sf. (IPR011333); T1-type_BTB. (IPR003131); BTB_2 (PF02214)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KCTD7" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KCTD7' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KCTD7** (gene ID: KCTD7, UniProt: Q96MP8) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KCTD7: A BTB/POZ Domain Protein Linking Protein Degradation to Neuronal Excitability and Lysosomal Function

## Introduction

KCTD7 (Potassium Channel Tetramerization Domain-containing protein 7) is a human gene located on chromosome 7q11.21 that encodes a 289 amino acid cytoplasmic protein containing an N-terminal BTB/POZ (bric-à-brac, tramtrack, broad complex/poxvirus and zinc finger) domain [vanbogaert-2007-kctd7-pme-abstract]. Despite its name suggesting involvement in potassium channel tetramerization, KCTD7 does not possess transmembrane domains or function directly as an ion channel. Instead, accumulated evidence demonstrates that KCTD7 functions primarily as a substrate adapter protein for Cullin-3 (CUL3)-based E3 ubiquitin ligase complexes, thereby regulating protein degradation through the ubiquitin-proteasome system [staropoli-2012-kctd7-cln14-abstract][wang-2022-kctd7-cln5-abstract].

The protein was first linked to human disease in 2007 when Van Bogaert and colleagues identified a homozygous nonsense mutation (R99X) in KCTD7 as the cause of a severe form of progressive myoclonic epilepsy (now designated EPM3) in a consanguineous Moroccan family [vanbogaert-2007-kctd7-pme-abstract]. Subsequent research has revealed that KCTD7 mutations can also cause a form of neuronal ceroid lipofuscinosis (CLN14), highlighting its essential role in lysosomal function and autophagy [staropoli-2012-kctd7-cln14-abstract][metz-2018-kctd7-autophagy-abstract]. Current understanding positions KCTD7 at the intersection of protein homeostasis, neuronal excitability, and lysosomal enzyme trafficking, with its dysfunction leading to devastating pediatric neurodegenerative disease.

## Structural Organization and Domain Architecture

KCTD7 belongs to the human KCTD (potassium channel tetramerization domain) protein family, which comprises 26 members that share sequence similarity with the cytoplasmic T1 domain of voltage-gated K+ channels [skoblov-2013-kctd-family-abstract]. Based on phylogenetic analysis of BTB domain sequences, the family is divided into seven groups, with KCTD7 classified in the C-group alongside its closest homolog KCTD14 [skoblov-2013-kctd-family-abstract]. This family arose through gene duplication from a common ancestral gene followed by divergence, leading to functional diversification across the animal kingdom. Despite the family name suggesting tetrameric assembly (as in Kv channels), crystallographic and cryo-electron microscopy studies have demonstrated that most KCTD family proteins, including KCTD7, assemble as pentamers [jiang-2023-kctd-structure-abstract].

The cryo-EM structure of mouse KCTD7 in complex with human Cullin-3 N-terminal domain (PDB: 8I79) was determined at 2.80 Å resolution and reveals a heterodecameric complex with C5 symmetry, comprising five KCTD7 subunits and five CUL3 molecules [jiang-2023-kctd-structure-abstract]. The pentameric BTB domain ring sits at the central fivefold axis, with five CUL3 molecules extending outward like arms from this core. Each CUL3 molecule contacts two adjacent BTB subunits through a primary binding interface (~732 Å² buried surface area) and a secondary binding interface (~247 Å²), creating a stable interaction network [jiang-2023-kctd-structure-abstract].

The C-terminal region of KCTD7 (residues 139-289) serves as the substrate-binding domain, responsible for recruiting specific proteins for ubiquitination. Bioinformatic analyses indicate that KCTD7 is structurally similar to KCTD5, another well-characterized family member, and both proteins form pentameric assemblies that engage substrates through their C-terminal domains while recruiting CUL3 through their BTB domains [jiang-2023-kctd-structure-abstract].

## Primary Molecular Function: Substrate Adapter for CUL3 E3 Ubiquitin Ligase

The primary biochemical function of KCTD7 is to serve as a substrate adapter protein within Cullin-RING E3 ubiquitin ligase complexes (CRL3-KCTD7) [wang-2022-kctd7-cln5-abstract][staropoli-2012-kctd7-cln14-abstract]. In these complexes, CUL3 provides the central scaffold that recruits the RING domain protein Rbx1 (which in turn binds ubiquitin-conjugating E2 enzymes), while KCTD7 serves as the substrate receptor that determines which proteins are targeted for ubiquitination and subsequent proteasomal degradation.

A critical substrate of the CRL3-KCTD7 complex is CLN5, a soluble lysosomal protein whose mutations cause another form of neuronal ceroid lipofuscinosis (CLN5 disease) [wang-2022-kctd7-cln5-abstract]. Wang et al. (2022) demonstrated that KCTD7 promotes K48-linked polyubiquitination of CLN5, marking it for proteasomal degradation. Under normal conditions, this ubiquitination maintains CLN5 at appropriate steady-state levels. When KCTD7 is deficient or mutated, CLN5 escapes degradation and accumulates to pathological levels in the endoplasmic reticulum [wang-2022-kctd7-cln5-abstract].

The functional consequences of CLN5 accumulation are profound. CLN5 normally interacts with the CLN6-CLN8 complex (the "EGRESS complex"), which recruits newly synthesized lysosomal enzymes at the ER for transport to the Golgi apparatus and eventual delivery to lysosomes [wang-2022-kctd7-cln5-abstract]. When CLN5 accumulates excessively due to KCTD7 deficiency, it paradoxically disrupts this EGRESS complex-mediated enzyme trafficking, leading to impaired lysosomal enzyme delivery and lysosomal dysfunction. This mechanism elegantly explains how KCTD7 mutations can phenocopy other NCL subtypes caused by direct mutations in CLN5, CLN6, or CLN8 genes [wang-2022-kctd7-cln5-abstract].

## Role in Neuronal Potassium Homeostasis and Excitability

Despite not functioning as a channel itself, KCTD7 exerts significant effects on neuronal membrane potential and excitability. Azizieh et al. (2011) demonstrated using patch-clamp electrophysiology that overexpression of KCTD7 in neurons hyperpolarizes the cell membrane and reduces neuronal excitability [azizieh-2011-kctd7-potassium-abstract]. This hyperpolarizing effect is potassium-dependent, as confirmed by studies in Xenopus oocyte expression systems [moen-2016-kctd7-glutamine-abstract].

The mechanism by which KCTD7 influences potassium conductance remains incompletely understood, but the interaction with CUL3 appears essential. One hypothesis suggests that the CRL3-KCTD7 complex may regulate the expression levels of potassium channel subunits or their regulatory proteins through ubiquitin-mediated degradation [azizieh-2011-kctd7-potassium-abstract]. By modulating the turnover of negative regulators of potassium channels, KCTD7 could indirectly enhance potassium conductance and promote membrane hyperpolarization.

Importantly, Moen et al. (2016) discovered that KCTD7 also regulates the activity of SAT2 (Slc38a2), a sodium-coupled neutral amino acid transporter that mediates glutamine uptake into neurons [moen-2016-kctd7-glutamine-abstract]. SAT2 is predominantly expressed in glutamatergic neurons, where it concentrates glutamine in dendritic compartments. This glutamine pool serves as a precursor for glutamate synthesis, the brain's primary excitatory neurotransmitter. Wild-type KCTD7 expression enhances SAT2-mediated glutamine transport, while pathogenic KCTD7 variants impair this function [moen-2016-kctd7-glutamine-abstract]. The disruption of glutamine transport may lead to inadequate glutamate synthesis in excitatory neurons, potentially contributing to the seizure phenotype through dysregulation of the glutamate-glutamine cycle.

## Subcellular Localization

KCTD7 displays primarily cytoplasmic localization with additional association at the plasma membrane [azizieh-2011-kctd7-potassium-abstract]. The protein's hydropathy profile and primary sequence are consistent with a soluble, intracytoplasmic protein lacking transmembrane domains. Studies in heterologously transfected HeLa and COS-1 cells showed diffuse cytosolic localization without significant colocalization with markers for endosomes, endoplasmic reticulum, Golgi apparatus, lysosomes, or cytoskeleton [azizieh-2011-kctd7-potassium-abstract].

In neurons, KCTD7 localization extends beyond the cell soma to include neuritic varicosities along developing neuronal extensions and neurite growth cones [azizieh-2011-kctd7-potassium-abstract]. Laser scanning microscopy has also detected KCTD7 signal at the plasma membrane, consistent with its functional effects on membrane potential. Wild-type KCTD7 shows broad cytoplasmic distribution with distinct plasma membrane signal, while certain pathogenic variants (such as R184C) display more diffuse cytoplasmic distribution with diminished membrane association and formation of cytoplasmic aggregates [staropoli-2012-kctd7-cln14-abstract].

Within the mouse brain, KCTD7 expression is widespread in neurons, including cortical neurons, pyramidal and granular cell layers of the hippocampus, and cerebellar Purkinje cells [azizieh-2011-kctd7-potassium-abstract]. Importantly, not all neurons express KCTD7, and expression is absent from astrocytes and microglial cells. The expression pattern in hippocampus and cerebellum correlates well with the clinical phenotype of KCTD7-related disease, which prominently features seizures and progressive ataxia.

## Role in Autophagy and Lysosomal Function

Beyond its role in CLN5 regulation, KCTD7 has broader functions in maintaining autophagy-lysosome pathway integrity. Metz et al. (2018) conducted comprehensive studies of patient-derived fibroblasts and a yeast model (deletion of WHI2, the KCTD7 homolog) to characterize the cellular consequences of KCTD7 deficiency [metz-2018-kctd7-autophagy-abstract].

Electron microscopy of brain biopsies and cultured fibroblasts from KCTD7-deficient patients revealed characteristic ultrastructural abnormalities: abnormal phagolysosomes with accumulated lipid droplets, supernumerary lipid droplets in proximity to mitochondria, and mitochondrial cristae malformations [metz-2018-kctd7-autophagy-abstract]. Lipofuscin accumulation was observed, although it lacked the classical characteristics of neuronal ceroid lipofuscinosis storage material, suggesting a distinct pathological entity.

Functional assays demonstrated impaired autophagy flux in KCTD7-deficient cells. Patient fibroblasts showed reduced LC3-II accumulation following chloroquine treatment (which blocks autophagosome-lysosome fusion), indicating defective autophagosome formation or processing [metz-2018-kctd7-autophagy-abstract]. Immunofluorescence analysis revealed increased numbers of p62, ubiquitin, and LC3B puncta in KCTD7-deficient cells, consistent with autophagic substrate accumulation. The mCherry-GFP-LC3B reporter assay confirmed increased formation of both autophagosomes and autolysosomes, suggesting a defect in autophagic degradation rather than initiation [metz-2018-kctd7-autophagy-abstract].

Additional studies using KCTD7-deficient cells revealed lysosomal acidification defects, altered lysosomal enzymatic composition and activity, drastic lipidomic changes, mTORC1 inactivation, unfolded protein response (UPR) activation with upregulation of ATF4 and CHOP, and increased susceptibility to spermine-induced lysosome-dependent cell death [metz-2018-kctd7-autophagy-abstract]. The UPR activation suggests persistent ER stress, a common feature of many neurodegenerative disorders characterized by misfolded protein accumulation.

Strikingly, the autophagy defect is evolutionarily conserved. Yeast lacking the KCTD7 homolog WHI2 displayed profound defects in autophagy induction and flux during amino acid starvation, with impaired conversion of the LC3 homolog Atg8 [metz-2018-kctd7-autophagy-abstract]. This conservation across more than a billion years of evolution underscores the fundamental importance of KCTD7-like proteins in cellular homeostasis.

## Disease Associations: Progressive Myoclonic Epilepsy and Neuronal Ceroid Lipofuscinosis

Biallelic pathogenic variants in KCTD7 cause a severe pediatric neurodegenerative disorder with two overlapping clinical presentations: progressive myoclonic epilepsy type 3 (EPM3, OMIM 611726) and neuronal ceroid lipofuscinosis type 14 (CLN14) [vanbogaert-2007-kctd7-pme-abstract][staropoli-2012-kctd7-cln14-abstract]. Whether these represent distinct entities or a phenotypic spectrum remains debated, but the underlying molecular pathology appears unified.

The disease typically manifests in infancy or early childhood after a period of normal or mildly delayed psychomotor development. The average age of onset is approximately 17 months (range 5-39 months), distinguishing KCTD7-related disease from other progressive myoclonic epilepsies which typically present later [metz-2018-kctd7-autophagy-abstract][jain-2022-kctd7-indian-abstract]. In 60-70% of cases, seizures are the presenting symptom, while other patients first develop movement disorders or developmental regression before seizure onset [metz-2018-kctd7-autophagy-abstract].

Myoclonic seizures are the hallmark, occurring in over 84% of patients, but other seizure types including generalized tonic-clonic, atonic, atypical absence, and focal seizures also occur [jain-2022-kctd7-indian-abstract]. The epilepsy is frequently pharmacoresistant, and neurological deterioration parallels seizure refractoriness [vanbogaert-2007-kctd7-pme-abstract]. Progressive features include cognitive decline with eventual severe dementia, speech deterioration (100% of patients), ataxia (63%), and motor handicap leading to wheelchair dependence. Many patients become non-verbal within years of onset [jain-2022-kctd7-indian-abstract].

Brain MRI is typically normal early in the disease course but may show progressive cerebral and cerebellar atrophy. EEG demonstrates slow dysrhythmia with multifocal and occasionally generalized epileptiform discharges, and photosensitivity is common [vanbogaert-2007-kctd7-pme-abstract]. Notably, retinal degeneration—a characteristic feature of several NCL subtypes—is typically absent or mild in KCTD7-related disease, providing a clinical distinguishing feature from CLN1 disease [metz-2018-kctd7-autophagy-abstract].

To date, over 40 unique pathogenic KCTD7 variants have been identified in more than 60 patients worldwide [jain-2022-kctd7-indian-abstract]. These include missense mutations, small insertions/deletions, splice site variants, and large exonic deletions. Mutations cluster in functionally critical regions: BTB domain mutations typically impair CUL3 binding, while mutations in the C-terminal region (residues 139-289) disrupt substrate (CLN5) interaction [wang-2022-kctd7-cln5-abstract]. Both mutation classes ablate the capacity of KCTD7 to mediate CLN5 degradation, converging on a common pathogenic mechanism.

## Mouse Model Evidence and Neurovascular Involvement

The generation of Kctd7 knockout mouse models has provided critical insights into KCTD7 function in vivo and validated its role in neurological disease. Liang et al. (2022) demonstrated that Kctd7-deficient mice develop myoclonic seizures and locomotor defects that closely mirror the human disease phenotype [liang-2022-kctd7-mouse-abstract]. Importantly, these mice exhibit substantial loss of cerebellar Purkinje cells, providing a cellular basis for the progressive ataxia observed in human patients. The cerebellar pathology is accompanied by region-specific defects in brain microvasculature, suggesting that KCTD7 plays a role in neurovascular interactions [liang-2022-kctd7-mouse-abstract].

The connection between KCTD7 and vascular development was initially discovered in the retina, a tractable model system for studying neurovascular interactions. Alevy et al. (2019) identified Kctd7 through a high-throughput screen as a regulator of vascular patterning and subsequently demonstrated that Kctd7 deletion causes defective patterning of the retinal vascular network, including increased branching, vessel length, and lacunarity [alevy-2019-kctd7-retina-abstract]. These alterations reflect early developmental defects, as emergence of both the superficial and deep vascular layers was delayed in Kctd7-null mice. Notably, KCTD7 is expressed in inner retinal neurons (particularly bipolar cells) but is absent from blood vessels themselves, indicating that the vascular phenotype arises from non-cell-autonomous effects of neuronal KCTD7 dysfunction [alevy-2019-kctd7-retina-abstract]. Loss of Kctd7 resulted in increased numbers of bipolar cells during development, suggesting that KCTD7 normally restrains neuronal proliferation or survival in specific contexts.

These mouse model studies collectively establish that KCTD7 is required for proper neuronal survival, excitability, and neurovascular coupling. The finding that Kctd7 deficiency affects both neurons and their associated vasculature suggests that the pathophysiology of KCTD7-related disease may extend beyond cell-autonomous neuronal dysfunction to include aberrant neurovascular interactions that could exacerbate neurodegeneration.

## Open Questions

Several important questions regarding KCTD7 function and dysfunction remain unresolved:

1. **Complete substrate repertoire**: While CLN5 has been identified as a key substrate of CRL3-KCTD7, the full complement of proteins targeted for ubiquitination by this complex remains unknown. Identifying additional substrates could reveal other pathways disrupted in KCTD7 deficiency and potential therapeutic targets.

2. **Mechanism of K+ conductance regulation**: The precise mechanism by which cytoplasmic KCTD7 influences plasma membrane potassium conductance remains unclear. Whether KCTD7 directly or indirectly regulates specific potassium channel subunits, and which channels are affected, requires further investigation.

3. **SAT2 regulation mechanism**: How KCTD7 modulates SAT2-mediated glutamine transport is not well understood. It is unclear whether this involves direct protein-protein interaction, post-translational modification of SAT2, or effects on SAT2 trafficking and membrane localization.

4. **Phenotypic variability**: Despite all patients having loss-of-function KCTD7 mutations, there is clinical heterogeneity in disease severity and progression. The genetic or environmental modifiers responsible for this variability are unknown.

5. **Therapeutic approaches**: Currently, there are no disease-modifying treatments for KCTD7-related disorders. Understanding whether gene therapy, substrate reduction therapy (reducing CLN5 by other means), or enhancing autophagy could ameliorate disease progression is an important area for future research.

6. **Tissue-specific effects**: Why neurons are particularly vulnerable to KCTD7 deficiency despite its broad expression pattern is not fully explained. Understanding the unique requirements of neurons for KCTD7 function could provide insights into neuroprotective strategies.

7. **Relationship to other NCL genes**: KCTD7 dysfunction leads to accumulation of CLN5, which disrupts the CLN6-CLN8 EGRESS complex. How this pathway intersects with other NCL gene products (CLN1, CLN2, CLN3, etc.) and whether there are common therapeutic targets across NCL subtypes warrants investigation.

## References

- **vanbogaert-2007-kctd7-pme-abstract**: Van Bogaert P, Azizieh R, Désir J, Aeby A, De Meirleir L, Laes JF, Christiaens F, Abramowicz MJ. Mutation of a potassium channel-related gene in progressive myoclonic epilepsy. *Annals of Neurology* 2007; 61(6):579-586. PMID: 17455289. DOI: 10.1002/ana.21121

- **azizieh-2011-kctd7-potassium-abstract**: Azizieh R, Orduz D, Van Bogaert P, Bouschet T, Rodriguez W, Schiffmann SN, Bharat I, Bharat MJ. Progressive myoclonic epilepsy-associated gene KCTD7 is a regulator of potassium conductance in neurons. *Molecular Neurobiology* 2011; 44(1):111-121. PMID: 21710140. DOI: 10.1007/s12035-011-8194-0

- **kousi-2012-kctd7-mutations-abstract**: Kousi M, Anttila V, Schulz A, Calafato S, Jakkula E, Riesch E, Myllykangas L, Kalimo H, Topçu M, Gökben S, Alehan F, Lemke JR, Alber M, Palotie A, Kopra O, Lehesjoki AE. Novel mutations consolidate KCTD7 as a progressive myoclonus epilepsy gene. *Journal of Medical Genetics* 2012; 49(6):391-399. PMID: 22693283. DOI: 10.1136/jmedgenet-2012-100859

- **staropoli-2012-kctd7-cln14-abstract**: Staropoli JF, Karaa A, Lim ET, Kirby A, Elbalalesy N, Romansky SG, Leydiker KB, Coppel SH, Barone R, Xin W, MacDonald ME, Abdenur JE, Daly MJ, Sims KB, Cotman SL. A homozygous mutation in KCTD7 links neuronal ceroid lipofuscinosis to the ubiquitin-proteasome system. *American Journal of Human Genetics* 2012; 91(1):59-71. PMID: 22748208. DOI: 10.1016/j.ajhg.2012.05.023

- **moen-2016-kctd7-glutamine-abstract**: Moen MN, Fjær R, Hamdani EH, Laerdahl JK, Menchini RJ, Vigeland MD, Sheng Y, Undlien DE, Hassel B, Salih MA, El Khashab HY, Selmer KK, Chaudhry FA. Pathogenic variants in KCTD7 perturb neuronal K+ fluxes and glutamine transport. *Brain* 2016; 139(12):3109-3120. PMID: 27742667. DOI: 10.1093/brain/aww244

- **metz-2018-kctd7-autophagy-abstract**: Metz KA, Teng X, et al. KCTD7 deficiency defines a distinct neurodegenerative disorder with a conserved autophagy-lysosome defect. *Annals of Neurology* 2018; 84(5):766-780. PMID: 30295347. DOI: 10.1002/ana.25351

- **wang-2022-kctd7-cln5-abstract**: Wang Y, Cao X, Liu P, Zeng W, Peng R, Shi Q, Feng K, Zhang P, Sun H, Wang C, Wang H. KCTD7 mutations impair the trafficking of lysosomal enzymes through CLN5 accumulation to cause neuronal ceroid lipofuscinoses. *Science Advances* 2022; 8(31):eabm5578. PMID: 35921411. PMCID: PMC9348797. DOI: 10.1126/sciadv.abm5578

- **jiang-2023-kctd-structure-abstract**: Jiang C, Wang R, Kong Z, Zheng D. Structural basis for the ubiquitination of G protein βγ subunits by KCTD5/Cullin3 E3 ligase. *Science Advances* 2023; 9(29):eadg8369. PMID: 37450587. PMCID: PMC10348674. DOI: 10.1126/sciadv.adg8369. PDB: 8I79

- **jain-2022-kctd7-indian-abstract**: Jain P, Sharma S, Das B, et al. KCTD7-related progressive myoclonic epilepsy: report of three Indian families and review of literature. *Child's Nervous System* 2022; 38(5):1009-1020. PMID: 34866617. PMCID: PMC8918358. DOI: 10.1007/s00381-021-05422-4

- **alevy-2019-kctd7-retina-abstract**: Alevy J, Burger CA, Albrecht NE, Jiang D, Samuel MA. Progressive myoclonic epilepsy-associated gene Kctd7 regulates retinal neurovascular patterning and function. *Neurochemistry International* 2019; 129:104486. PMID: 31175897. DOI: 10.1016/j.neuint.2019.104486

- **liang-2022-kctd7-mouse-abstract**: Liang JH, Alevy J, Akhanov V, Seo R, Massey CA, Jiang D, Zhou J, Sillitoe RV, Noebels JL, Samuel MA. Kctd7 deficiency induces myoclonic seizures associated with Purkinje cell death and microvascular defects. *Disease Models & Mechanisms* 2022; 15(9):dmm049642. PMID: 35972048. DOI: 10.1242/dmm.049642

- **skoblov-2013-kctd-family-abstract**: Skoblov M, et al. Protein partners of KCTD proteins provide insights about their functional roles in cell differentiation and vertebrate development. *Cell & Bioscience* 2013; 3:45. PMID: 24268103. PMCID: PMC3882106. DOI: 10.1186/2045-3701-3-45

- **GeneReviews**: Metz KA, Bhalerao A, Bhalerao S. KCTD7-Related Progressive Myoclonic Epilepsy. In: Adam MP, et al., editors. *GeneReviews*. Seattle (WA): University of Washington, Seattle; 2023. https://www.ncbi.nlm.nih.gov/books/NBK619245/

- **OMIM 611725**: POTASSIUM CHANNEL TETRAMERIZATION DOMAIN-CONTAINING PROTEIN 7; KCTD7. https://www.omim.org/entry/611725

- **OMIM 611726**: EPILEPSY, PROGRESSIVE MYOCLONIC, 3, WITH OR WITHOUT INTRACELLULAR INCLUSIONS; EPM3. https://omim.org/entry/611726

- **UniProt Q96MP8**: BTB/POZ domain-containing protein KCTD7. https://www.uniprot.org/uniprotkb/Q96MP8/entry


## Citations

1. alevy-2019-kctd7-retina-abstract.md
2. azizieh-2011-kctd7-potassium-abstract.md
3. jain-2022-kctd7-indian-abstract.md
4. jiang-2023-kctd-structure-abstract.md
5. kousi-2012-kctd7-mutations-abstract.md
6. liang-2022-kctd7-mouse-abstract.md
7. metz-2018-kctd7-autophagy-abstract.md
8. metz-2018-kctd7-autophagy-summary.md
9. moen-2016-kctd7-glutamine-abstract.md
10. skoblov-2013-kctd-family-abstract.md
11. staropoli-2012-kctd7-cln14-abstract.md
12. vanbogaert-2007-kctd7-pme-abstract.md
13. vanbogaert-2007-kctd7-pme-summary.md
14. wang-2022-kctd7-cln5-abstract.md
15. wang-2022-kctd7-cln5-summary.md