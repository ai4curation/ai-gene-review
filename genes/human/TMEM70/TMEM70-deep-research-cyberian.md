---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-23T23:50:32.008890'
end_time: '2026-01-24T00:03:14.465001'
duration_seconds: 762.46
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: TMEM70
  gene_symbol: TMEM70
  uniprot_accession: Q9BUB7
  protein_description: 'RecName: Full=Transmembrane protein 70, mitochondrial {ECO:0000305};
    Flags: Precursor;'
  gene_info: Name=TMEM70 {ECO:0000312|HGNC:HGNC:26050};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the TMEM70 family. .
  protein_domains: TMEM70. (IPR009724); TMEM70/TMEM186/TMEM223. (IPR045325); TMEM70
    (PF06979)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 21
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9BUB7
- **Protein Description:** RecName: Full=Transmembrane protein 70, mitochondrial {ECO:0000305}; Flags: Precursor;
- **Gene Information:** Name=TMEM70 {ECO:0000312|HGNC:HGNC:26050};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the TMEM70 family. .
- **Key Domains:** TMEM70. (IPR009724); TMEM70/TMEM186/TMEM223. (IPR045325); TMEM70 (PF06979)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TMEM70" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TMEM70' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TMEM70** (gene ID: TMEM70, UniProt: Q9BUB7) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TMEM70: A Critical Assembly Factor for Mitochondrial ATP Synthase

## Introduction and Summary

TMEM70 (Transmembrane protein 70, mitochondrial; UniProt: Q9BUB7) is a nuclear-encoded protein of approximately 21-30 kDa that functions as an essential assembly factor for the mitochondrial F1Fo-ATP synthase (Complex V) [cizkova-2008-discovery-abstract]. This protein was first identified in 2008 through whole-genome homozygosity mapping in patients with isolated mitochondrial ATP synthase deficiency presenting as neonatal encephalocardiomyopathy [cizkova-2008-discovery-abstract]. TMEM70 is localized in the inner mitochondrial membrane, specifically within the cristae membranes, where it plays a pivotal role in facilitating the assembly of the c-ring component of the Fo proton channel [bahri-2020-scaffold-abstract]. Mutations in TMEM70 represent the most common nuclear genetic cause of isolated ATP synthase deficiency, with the disease manifesting primarily as severe neonatal lactic acidosis, hypertrophic cardiomyopathy, and encephalopathy [tauchmannova-2024-review-abstract].

The primary molecular function of TMEM70 is to serve as an oligomeric scaffold that promotes the stepwise assembly of subunit c into the c-ring, the essential rotor component of the ATP synthase proton translocation domain [kovalcikova-2019-subunitc-abstract]. Without functional TMEM70, cells accumulate the F1 catalytic domain and peripheral stalk but fail to properly incorporate the Fo membrane domain, resulting in severely impaired ATP synthesis capacity. Recent evidence also suggests that TMEM70 may have a role in Complex I assembly, indicating a broader function in oxidative phosphorylation system biogenesis [sanchez-caballero-2020-complexI-abstract].

## Molecular Function: ATP Synthase Assembly

### Role in c-Ring Assembly

The mitochondrial F1Fo-ATP synthase is a remarkable molecular machine that harnesses the proton gradient across the inner mitochondrial membrane to synthesize ATP from ADP and inorganic phosphate. The enzyme consists of two major domains: the membrane-extrinsic F1 catalytic domain (containing the α, β, γ, δ, and ε subunits) and the membrane-embedded Fo proton channel (containing subunits a, c, and accessory subunits). The Fo domain includes the c-ring, composed of 8 identical copies of the highly hydrophobic subunit c, which rotates as protons flow through the channel to drive ATP synthesis [bahri-2020-scaffold-abstract].

Studies using TMEM70 conditional knockout mice have definitively established that TMEM70 functions at an early stage of ATP synthase biogenesis by promoting the incorporation of subunit c into the rotor structure [kovalcikova-2019-subunitc-abstract]. In the absence of TMEM70, cells form an incomplete enzyme complex consisting of the F1 domain and peripheral stalk but lacking the Fo proton channel. This results in an 80% decrease in fully assembled ATP synthase and a marked accumulation of F1 complexes [vrbacky-2016-knockout-abstract]. Critically, direct interaction between TMEM70 and subunit c has been demonstrated through immunoprecipitation and pulse-chase experiments, with TMEM70-subunit c complexes containing progressively increasing amounts of subunit c detected, suggesting a role for TMEM70 oligomers in the gradual assembly of the c-ring [bahri-2020-scaffold-abstract].

The biological significance of TMEM70 lies in its ability to increase the low efficacy of spontaneous subunit c oligomer assembly, which represents the key rate-limiting step of ATP synthase biogenesis [kovalcikova-2019-subunitc-abstract]. Overexpression of subunit c can partially rescue the TMEM70 defect in cultured cells, further supporting this model [kovalcikova-2019-subunitc-abstract].

### High Molecular Weight Complexes

TMEM70 forms large oligomeric complexes that function as scaffolds for c-ring assembly. On Blue-Native PAGE, TMEM70 is detected in multiple forms including dimers, and these complexes display partial overlap with assembled ATP synthase [kratochvilova-2014-topology-abstract]. Studies in HeLa cells have shown that mutant TMEM70 associates in high molecular weight complexes of 470-550 kDa [torraco-2012-hotspot-abstract]. Interestingly, immunoprecipitation and immunogold electron microscopy studies indicate that while TMEM70 molecules interact with each other, there is no direct stable interaction with fully assembled ATP synthase subunits, suggesting that TMEM70's function is transient and specific to the assembly process [kratochvilova-2014-topology-abstract].

### Partnership with TMEM242

A significant mechanistic advance came from the discovery that TMEM70 works in partnership with another mitochondrial transmembrane protein, TMEM242 [carroll-2021-tmem242-abstract]. Both proteins interact with subunit c and contribute to c-ring assembly, though with distinct but overlapping functions. Deletion of either TMEM70 or TMEM242 individually reduces but does not completely eliminate ATP synthase assembly. However, simultaneous deletion of both proteins completely prevents ATP synthase assembly, demonstrating their essential and partially redundant roles in c-ring formation [carroll-2021-tmem242-abstract]. Interestingly, TMEM242 (but not TMEM70) also affects the introduction of subunits ATP6, ATP8, j, and k into the enzyme, indicating that TMEM242 has additional functions in later stages of ATP synthase assembly [carroll-2021-tmem242-abstract].

### Dual Role in Complexes I and V

Beyond its established role in ATP synthase assembly, recent evidence from BioID proximity labeling, complexome profiling, and coevolution analyses has revealed that TMEM70 also functions in the assembly of respiratory chain Complex I (NADH:ubiquinone oxidoreductase) [sanchez-caballero-2020-complexI-abstract]. Loss of TMEM70 results in the accumulation of an assembly intermediate followed by a reduction of the next assembly intermediate for both complexes I and V, indicating that TMEM70 has a role in the stability of membrane-bound subassemblies or in the membrane recruitment of subunits into forming complexes [sanchez-caballero-2020-complexI-abstract]. This dual function provides an explanation for the observation that some TMEM70 patient tissues show deficiencies in multiple OXPHOS complexes rather than isolated Complex V defects [diodato-2014-italian-abstract].

Importantly, both TMEM70 and TMEM242 interact with the mitochondrial complex I assembly (MCIA) complex, which supports assembly of the membrane arm of Complex I [carroll-2021-tmem242-abstract]. The double deletion of TMEM70 and TMEM242 enhances the impact on Complex I assembly beyond that seen with single deletions [carroll-2021-tmem242-abstract]. These interactions provide a molecular explanation for the coordinate regulation of Complex I and Complex V assembly and suggest that TMEM70 and TMEM242 may serve as a hub for OXPHOS membrane complex biogenesis.

## Subcellular Localization and Membrane Topology

### Inner Mitochondrial Membrane Localization

TMEM70 is localized to the inner mitochondrial membrane, a finding confirmed through multiple approaches including immunogold labeling experiments and comparative genomics analysis [jonckheere-2011-topology-abstract]. More specifically, expansion super-resolution microscopy has demonstrated that TMEM70 localizes specifically at the inner cristae membrane, distinct from the MICOS component MIC60 which marks cristae junctions [bahri-2020-scaffold-abstract]. This cristae localization is significant because ATP synthase is known to be enriched at the edges of cristae where it plays a key role in cristae structure and stability [bahri-2020-scaffold-abstract].

### Membrane Topology

Topological studies using tagged forms of TMEM70 have established that the protein adopts a hairpin structure with both the N- and C-termini oriented towards the mitochondrial matrix [kratochvilova-2014-topology-abstract]. This topology positions TMEM70 to interact with newly synthesized subunit c and facilitate its incorporation into the growing c-ring within the inner membrane.

## Gene Ontology Annotation Summary

The functional annotations for TMEM70 (Q9BUB7) in the Gene Ontology database, derived from experimental evidence, provide a concise summary of its characterized functions:

**Molecular Function:** TMEM70 has been annotated with protein binding activity (GO:0005515) based on physical interaction evidence from multiple studies [kovalcikova-2019-subunitc-abstract][bahri-2020-scaffold-abstract][carroll-2021-tmem242-abstract]. It also functions as a protein-macromolecule adaptor (GO:0030674), mediating interactions between subunit c and the growing c-ring complex [sanchez-caballero-2020-complexI-abstract]. Additionally, TMEM70 has been shown to bind to the mitochondrial proton-transporting ATP synthase complex (GO:0140260) [sanchez-caballero-2020-complexI-abstract].

**Biological Process:** TMEM70 participates in mitochondrial proton-transporting ATP synthase complex assembly (GO:0033615), supported by extensive mutant phenotype evidence from both human patients and knockout mice [cizkova-2008-discovery-abstract][kovalcikova-2019-subunitc-abstract][vrbacky-2016-knockout-abstract]. It also contributes to mitochondrial respiratory chain complex I assembly (GO:0032981) [sanchez-caballero-2020-complexI-abstract]. TMEM70 itself undergoes protein complex oligomerization (GO:0051259) and protein homooligomerization (GO:0051260), forming the scaffolds essential for its assembly function [kratochvilova-2014-topology-abstract][bahri-2020-scaffold-abstract].

**Cellular Component:** TMEM70 is localized to the mitochondrial inner membrane (GO:0005743) and more specifically to the mitochondrial crista (GO:0030061), as confirmed by immunogold labeling and super-resolution microscopy [kratochvilova-2014-topology-abstract][bahri-2020-scaffold-abstract].

## Evolutionary Conservation and Protein Family

TMEM70 belongs to the TMEM70/TMEM186/TMEM223 protein family, with all three members being mitochondrial in humans [sanchez-caballero-2020-complexI-abstract]. Evolutionary analyses demonstrate that this protein family only occurs in species with oxidative phosphorylation complexes, providing independent evidence for a role in OXPHOS assembly [sanchez-caballero-2020-complexI-abstract]. While initial phylogenetic analyses suggested that TMEM70 was specific for higher eukaryotes [houstek-2009-ancillary-abstract], subsequent comparative genomics studies have revealed that the gene is not restricted to higher multicellular eukaryotes and is also found in simpler organisms [jonckheere-2011-topology-abstract].

## Consequences of TMEM70 Deficiency

### Effects on Mitochondrial Structure

Loss of TMEM70 function has profound effects on mitochondrial morphology. Patient fibroblasts exhibit a fragmented mitochondrial network with swollen and irregularly shaped mitochondria showing partial to complete loss of cristae [jonckheere-2011-topology-abstract]. Complementation with wild-type TMEM70 can completely restore normal mitochondrial morphology [jonckheere-2011-topology-abstract]. In TMEM70 knockout mouse embryos, mitochondria display concentric or irregular cristae structures [vrbacky-2016-knockout-abstract]. Studies using immunogold electron microscopy and tomography have shown that mitochondrial DNA nucleoid clusters are disrupted in abnormal mitochondria from TMEM70-deficient patients, with both nucleoids and respiratory chain complexes confined to the outer rings of the cristae whorls [cameron-2010-nucleoid-abstract]. This observation may explain the differential effects on complex V expression and assembly in different tissues.

### Metabolic Consequences

TMEM70 deficiency results in severely impaired mitochondrial ATP production. In patient fibroblasts, there is an 82-89% decrease in ATP synthase content [havlickova-2012-compensation-abstract]. This leads to decreased ADP-stimulated State 3 respiration, reduced respiratory control ratio, and lower ATP/ADP ratios [vrbacky-2016-knockout-abstract]. Interestingly, cells respond to ATP synthase deficiency with compensatory upregulation of other respiratory chain complexes: a 50-162% increase in Complex IV and a 22-53% increase in Complex III [havlickova-2012-compensation-abstract]. This compensation occurs through posttranscriptional mechanisms rather than changes in mRNA levels [havlickova-2012-compensation-abstract]. Additionally, diminished ATP synthase results in elevated mitochondrial membrane potential and increased reactive oxygen species (ROS) production [havlickova-2012-compensation-abstract].

### Mouse Knockout Studies

Generation of Tmem70 knockout mice has provided critical insights into the essential nature of this protein. Homozygous Tmem70-/- knockouts exhibit profound growth retardation and embryonic lethality at approximately embryonic day 9.5 [vrbacky-2016-knockout-abstract]. Blue-Native electrophoresis demonstrates an 80% decrease in fully assembled ATP synthase and marked accumulation of F1 complexes, indicating that biogenesis is stalled following F1 oligomer formation [vrbacky-2016-knockout-abstract]. Heterozygous Tmem70+/- mice are fully viable and display normal postnatal growth, but they present with mild deterioration of heart function [vrbacky-2016-knockout-abstract]. Transgenic rescue experiments using rats have shown that restoration of TMEM70 to 16-49% of normal levels is sufficient for full biochemical complementation in liver and partial complementation in heart [markovic-2022-transgenic-abstract].

## Clinical Manifestations of TMEM70 Mutations

### Disease Phenotype

Mutations in TMEM70 cause a distinctive clinical syndrome characterized by neonatal mitochondrial encephalocardiomyopathy (OMIM 604273). The largest cohort study to date examined 48 patients and found neonatal onset in 85% of cases [magner-2015-longterm-abstract]. The most frequent presenting features include severe muscular hypotonia (92-95% of patients), apneic spells (92%), hypertrophic cardiomyopathy (76-89%), and profound lactic acidosis with lactate levels of 5-36 mmol/L (92%) [honzik-2010-natural-history-abstract][magner-2015-longterm-abstract]. Hyperammonemia (100-520 μmol/L) is present in 86% of cases and 3-methylglutaconic aciduria is a consistent finding [honzik-2010-natural-history-abstract]. Additional features include developmental delay (98%), faltering growth (94%), short stature (89%), microcephaly (71%), and facial dysmorphism (66%) [magner-2015-longterm-abstract]. Male patients frequently present with hypospadias (50-54%) and cryptorchidism (67%) [honzik-2010-natural-history-abstract]. Persistent pulmonary hypertension of the newborn has been identified as a life-threatening complication in 22% of patients [catteruccia-2014-pphn-abstract][magner-2015-longterm-abstract]. Notably, the cardiomyopathy is typically non-progressive and may even resolve in some children [honzik-2010-natural-history-abstract].

### Genetic Basis

The most common mutation is a homozygous splice site mutation c.317-2A>G, which is particularly prevalent in the Roma population [cizkova-2008-discovery-abstract][magner-2015-longterm-abstract]. However, TMEM70 deficiency is a panethnic disease, and numerous other mutations have been identified in patients of various ethnic backgrounds including Arab Muslim and Turkish populations [magner-2015-longterm-abstract]. These include missense, frameshift, and other splice site mutations throughout the gene [spiegel-2011-commonmutations-abstract].

### Metabolic Biomarkers and Classification

A hallmark metabolic feature of TMEM70 deficiency is elevated urinary 3-methylglutaconic acid (3-MGA), which places this disorder in the category of "secondary 3-methylglutaconic acidurias" [wortmann-2013-3mga-abstract]. Unlike primary 3-MGA-uria caused by defects in leucine catabolism (AUH deficiency), the 3-MGA elevation in TMEM70 deficiency arises from compromised mitochondrial membrane function. TMEM70 deficiency is classified alongside other mitochondrial membrane-associated disorders that present with 3-MGA-uria, including Costeff syndrome (OPA3 defect) and DCMA syndrome (DNAJC19 defect) [wortmann-2013-3mga-abstract]. This metabolic signature provides a useful diagnostic clue, as consistent and significant 3-MGA elevation in a neonate with encephalocardiomyopathy should prompt consideration of TMEM70 deficiency [wortmann-2013-3mga-abstract].

### Prognosis and Management

The prognosis for TMEM70 deficiency is variable but serious. Ten-year survival is approximately 63%, with most deaths occurring in the neonatal period; importantly, no deaths have been reported after the age of five years in surviving patients [magner-2015-longterm-abstract]. Acute metabolic crises with life-threatening hyperammonemia can occur during childhood, often triggered by acute gastroenteritis and prolonged fasting [honzik-2010-natural-history-abstract]. These episodes respond to treatment with intravenous glucose and lipid infusion, ammonia scavengers, or hemodialfiltration [magner-2015-longterm-abstract]. Importantly, adequate management of hyperammonemic crises in the neonatal period and early childhood is critical for long-term outcomes [magner-2015-longterm-abstract].

## Open Questions

Despite significant advances in understanding TMEM70 function, several important questions remain:

1. **Precise molecular mechanism**: While TMEM70 has been established as a scaffold for c-ring assembly, the exact molecular mechanism by which TMEM70 oligomers promote subunit c oligomerization remains unclear. Does TMEM70 actively catalyze c-ring formation or simply provide a permissive environment?

2. **Coordination with other assembly factors**: How does TMEM70 coordinate with other ATP synthase assembly factors such as the INA complex (Ina17/Ina22), which facilitates peripheral stalk assembly? What is the temporal sequence of these interactions during holoenzyme biogenesis?

3. **Complex I involvement**: The dual role of TMEM70 in both Complex I and Complex V assembly requires further elucidation. Does TMEM70 perform similar functions for both complexes, or are the mechanisms distinct?

4. **TMEM186 and TMEM223 functions**: The roles of the related family members TMEM186 and TMEM223 in mitochondrial biogenesis remain largely unexplored. Do these proteins have redundant or distinct functions?

5. **Tissue-specific effects**: Why do some tissues show more severe consequences of TMEM70 deficiency than others? The observation of differential effects on cristae structure and nucleoid organization across tissues deserves further investigation.

6. **Therapeutic approaches**: Can gene therapy or other interventions effectively treat TMEM70 deficiency? The transgenic rescue experiments in rats are encouraging but translation to clinical applications remains to be developed.

7. **Structural biology**: High-resolution structural information on TMEM70, particularly in complex with subunit c intermediates, would greatly enhance understanding of its molecular function.

## References

1. **cizkova-2008-discovery**: Cízkova A, Stránecký V, Mayr JA, et al. TMEM70 mutations cause isolated ATP synthase deficiency and neonatal mitochondrial encephalocardiomyopathy. *Nature Genetics*. 2008;40(11):1288-90. PMID: 18953340. DOI: [10.1038/ng.246](https://doi.org/10.1038/ng.246)

2. **bahri-2020-scaffold**: Bahri H, Buratto J, Rojo M, et al. TMEM70 forms oligomeric scaffolds within mitochondrial cristae promoting in situ assembly of mammalian ATP synthase proton channel. *Biochimica et Biophysica Acta - Molecular Cell Research*. 2020;1868(4):118942. PMID: 33359711. DOI: [10.1016/j.bbamcr.2020.118942](https://doi.org/10.1016/j.bbamcr.2020.118942)

3. **kovalcikova-2019-subunitc**: Kovalčíková J, Vrbacký M, Pecina P, et al. TMEM70 facilitates biogenesis of mammalian ATP synthase by promoting subunit c incorporation into the rotor structure of the enzyme. *FASEB Journal*. 2019;33(12):14103-14117. PMID: 31652072. DOI: [10.1096/fj.201900685RR](https://doi.org/10.1096/fj.201900685RR)

4. **sanchez-caballero-2020-complexI**: Sánchez-Caballero L, Elurbe DM, Baertling F, et al. TMEM70 functions in the assembly of complexes I and V. *Biochimica et Biophysica Acta - Bioenergetics*. 2020;1861(8):148202. PMID: 32275929. DOI: [10.1016/j.bbabio.2020.148202](https://doi.org/10.1016/j.bbabio.2020.148202)

5. **houstek-2009-ancillary**: Houstek J, Kmoch S, Zeman J. TMEM70 protein - a novel ancillary factor of mammalian ATP synthase. *Biochimica et Biophysica Acta - Bioenergetics*. 2009;1787(5):529-32. PMID: 19103153. DOI: [10.1016/j.bbabio.2008.11.013](https://doi.org/10.1016/j.bbabio.2008.11.013)

6. **jonckheere-2011-topology**: Jonckheere AI, Huigsloot M, Lammens M, et al. Restoration of complex V deficiency caused by a novel deletion in the human TMEM70 gene normalizes mitochondrial morphology. *Mitochondrion*. 2011;11(6):954-63. PMID: 21945727. DOI: [10.1016/j.mito.2011.08.012](https://doi.org/10.1016/j.mito.2011.08.012)

7. **kratochvilova-2014-topology**: Kratochvílová H, Hejzlarová K, Vrbacký M, et al. Mitochondrial membrane assembly of TMEM70 protein. *Mitochondrion*. 2014;15:1-9. PMID: 24576557. DOI: [10.1016/j.mito.2014.02.010](https://doi.org/10.1016/j.mito.2014.02.010)

8. **vrbacky-2016-knockout**: Vrbacký M, Kovalčíková J, Chawengsaksophak K, et al. Knockout of Tmem70 alters biogenesis of ATP synthase and leads to embryonal lethality in mice. *Human Molecular Genetics*. 2016;25(21):4674-4685. PMID: 28173120. DOI: [10.1093/hmg/ddw295](https://doi.org/10.1093/hmg/ddw295)

9. **honzik-2010-natural-history**: Honzík T, Tesarová M, Mayr JA, et al. Mitochondrial encephalocardio-myopathy with early neonatal onset due to TMEM70 mutation. *Archives of Disease in Childhood*. 2010;95(4):296-301. PMID: 20335238. DOI: [10.1136/adc.2009.168096](https://doi.org/10.1136/adc.2009.168096)

10. **magner-2015-longterm**: Magner M, Dvorakova V, Tesarova M, et al. TMEM70 deficiency: long-term outcome of 48 patients. *Journal of Inherited Metabolic Disease*. 2015;38(3):417-26. PMID: 25326274. DOI: [10.1007/s10545-014-9774-8](https://doi.org/10.1007/s10545-014-9774-8)

11. **torraco-2012-hotspot**: Torraco A, Verrigni D, Rizza T, et al. TMEM70: a mutational hot spot in nuclear ATP synthase deficiency with a pivotal role in complex V biogenesis. *Neurogenetics*. 2012;13(4):375-86. PMID: 22986587. DOI: [10.1007/s10048-012-0343-8](https://doi.org/10.1007/s10048-012-0343-8)

12. **cameron-2010-nucleoid**: Cameron JM, Levandovskiy V, Mackay N, et al. Complex V TMEM70 deficiency results in mitochondrial nucleoid disorganization. *Mitochondrion*. 2010;11(1):191-9. PMID: 20920610. DOI: [10.1016/j.mito.2010.09.008](https://doi.org/10.1016/j.mito.2010.09.008)

13. **havlickova-2012-compensation**: Havlíčková Karbanová V, Cížková Vrbacká A, Hejzlarová K, et al. Compensatory upregulation of respiratory chain complexes III and IV in isolated deficiency of ATP synthase due to TMEM70 mutation. *Biochimica et Biophysica Acta - Bioenergetics*. 2012;1817(7):1037-43. PMID: 22433607. DOI: [10.1016/j.bbabio.2012.03.004](https://doi.org/10.1016/j.bbabio.2012.03.004)

14. **tauchmannova-2024-review**: Tauchmannová K, Pecinová A, Houštěk J, Mráček T. Variability of Clinical Phenotypes Caused by Isolated Defects of Mitochondrial ATP Synthase. *Physiological Research*. 2024;73(Suppl 1):S243-S278. PMID: 39016153. PMCID: PMC11412354. DOI: [10.33549/physiolres.935407](https://doi.org/10.33549/physiolres.935407)

15. **spiegel-2011-commonmutations**: Spiegel R, Khayat M, Shalev SA, et al. TMEM70 mutations are a common cause of nuclear encoded ATP synthase assembly defect: further delineation of a new syndrome. *Journal of Medical Genetics*. 2011;48(3):177-82. PMID: 21147908. DOI: [10.1136/jmg.2010.084608](https://doi.org/10.1136/jmg.2010.084608)

16. **catteruccia-2014-pphn**: Catteruccia M, Verrigni D, Martinelli D, et al. Persistent pulmonary arterial hypertension in the newborn (PPHN): a frequent manifestation of TMEM70 defective patients. *Molecular Genetics and Metabolism*. 2014;111(3):353-359. PMID: 24485043. DOI: [10.1016/j.ymgme.2014.01.001](https://doi.org/10.1016/j.ymgme.2014.01.001)

17. **markovic-2022-transgenic**: Marković A, Tauchmannová K, Šimáková M, et al. Genetic Complementation of ATP Synthase Deficiency Due to Dysfunction of TMEM70 Assembly Factor in Rat. *Biomedicines*. 2022;10(2):276. PMID: 35203486. PMCID: PMC8869460. DOI: [10.3390/biomedicines10020276](https://doi.org/10.3390/biomedicines10020276)

18. **diodato-2014-italian**: Diodato D, Invernizzi F, Lamantea E, et al. Common and Novel TMEM70 Mutations in a Cohort of Italian Patients with Mitochondrial Encephalocardiomyopathy. *JIMD Reports*. 2014;15:71-8. PMID: 24740313. PMCID: PMC4270871. DOI: [10.1007/8904_2014_300](https://doi.org/10.1007/8904_2014_300)

19. **el-hattab-2016-cardiomyopathy**: El-Hattab AW, Scaglia F. Mitochondrial Cardiomyopathies. *Frontiers in Cardiovascular Medicine*. 2016;3:25. PMID: 27504452. PMCID: PMC4958622. DOI: [10.3389/fcvm.2016.00025](https://doi.org/10.3389/fcvm.2016.00025)

20. **carroll-2021-tmem242**: Carroll J, He J, Ding S, Fearnley IM, Walker JE. TMEM70 and TMEM242 help to assemble the rotor ring of human ATP synthase and interact with assembly factors for complex I. *Proceedings of the National Academy of Sciences USA*. 2021;118(13):e2100558118. PMID: 33753518. PMCID: PMC8020751. DOI: [10.1073/pnas.2100558118](https://doi.org/10.1073/pnas.2100558118)

21. **wortmann-2013-3mga**: Wortmann SB, Duran M, Anikster Y, et al. Inborn errors of metabolism with 3-methylglutaconic aciduria as discriminative feature: proper classification and nomenclature. *Journal of Inherited Metabolic Disease*. 2013;36(6):923-8. PMID: 23296368. DOI: [10.1007/s10545-012-9580-0](https://doi.org/10.1007/s10545-012-9580-0)

22. **zhou-2021-atpaf1**: Zhou Z, Zhang K, Liu Z, et al. ATPAF1 deficiency impairs ATP synthase assembly and mitochondrial respiration. *Mitochondrion*. 2021;60:129-141. PMID: 34375736. PMCID: PMC9201681. DOI: [10.1016/j.mito.2021.08.005](https://doi.org/10.1016/j.mito.2021.08.005)


## Citations

1. bahri-2020-scaffold-abstract.md
2. cameron-2010-nucleoid-abstract.md
3. carroll-2021-tmem242-abstract.md
4. catteruccia-2014-pphn-abstract.md
5. cizkova-2008-discovery-abstract.md
6. diodato-2014-italian-abstract.md
7. havlickova-2012-compensation-abstract.md
8. honzik-2010-natural-history-abstract.md
9. houstek-2009-ancillary-abstract.md
10. jonckheere-2011-topology-abstract.md
11. kovalcikova-2019-subunitc-abstract.md
12. kratochvilova-2014-topology-abstract.md
13. magner-2015-longterm-abstract.md
14. markovic-2022-transgenic-abstract.md
15. sanchez-caballero-2020-complexI-abstract.md
16. spiegel-2011-commonmutations-abstract.md
17. tauchmannova-2024-review-abstract.md
18. torraco-2012-hotspot-abstract.md
19. vrbacky-2016-knockout-abstract.md
20. wortmann-2013-3mga-abstract.md
21. zhou-2021-atpaf1-abstract.md