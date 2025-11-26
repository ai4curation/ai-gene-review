---
provider: cyberian
model: deep-research
cached: false
start_time: '2025-11-24T17:52:59.730088'
end_time: '2025-11-24T18:11:23.710998'
duration_seconds: 1103.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: pombe
  gene_id: cps1
  gene_symbol: cps1
  uniprot_accession: O13968
  protein_description: 'RecName: Full=Uncharacterized carboxypeptidase C24C9.08; EC=3.4.17.-;'
  gene_info: ORFNames=SPAC24C9.08;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the peptidase M20A family. .
  protein_domains: Bact_exopeptidase_dim_dom. (IPR036264); Pept_M20_carboxypep. (IPR017141);
    Pept_M20A. (IPR047177); Peptidase_M20. (IPR002933); Peptidase_M20_dimer. (IPR011650)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 12
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O13968
- **Protein Description:** RecName: Full=Uncharacterized carboxypeptidase C24C9.08; EC=3.4.17.-;
- **Gene Information:** ORFNames=SPAC24C9.08;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the peptidase M20A family. .
- **Key Domains:** Bact_exopeptidase_dim_dom. (IPR036264); Pept_M20_carboxypep. (IPR017141); Pept_M20A. (IPR047177); Peptidase_M20. (IPR002933); Peptidase_M20_dimer. (IPR011650)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cps1" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cps1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cps1** (gene ID: cps1, UniProt: O13968) in pombe.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Vacuolar Carboxypeptidase S (cps1/SPAC24C9.08) in Schizosaccharomyces pombe

## Introduction and Summary

The *Schizosaccharomyces pombe* gene SPAC24C9.08, also known as *cps1*, encodes a vacuolar carboxypeptidase S (SpCPS), a zinc-dependent metallopeptidase belonging to the M20A family of peptidases [PomBase-SPAC24C9.08-database]. This enzyme functions as a carboxypeptidase in the vacuolar lumen, where it participates in the terminal degradation of proteins and peptides by cleaving amino acids from the C-terminus of polypeptide substrates. The protein is synthesized as a type II transmembrane precursor that transits through the secretory pathway and is delivered to the vacuole via the multivesicular body (MVB) sorting pathway, where it is processed to its mature, soluble form [hecht-2014-vacuole-abstract].

**Critical Note on Gene Symbol Ambiguity:** The gene symbol "cps1" in *S. pombe* literature can be confusing, as it is also used as an alias for *bgs1* (SPBC19G7.05c), which encodes the 1,3-β-glucan synthase catalytic subunit involved in cell wall synthesis and cytokinesis. The protein described in this report—the vacuolar carboxypeptidase S encoded by SPAC24C9.08—is a fundamentally different enzyme from the glucan synthase [PomBase-SPAC24C9.08-database].

Carboxypeptidase S was first identified in *S. cerevisiae* by Wolf and Weiser in 1977 using a carboxypeptidase Y-deficient mutant (prc1-1) [wolf-1977-cpsy-abstract]. They observed that a double mutant lacking carboxypeptidase Y but auxotrophic for leucine could still grow on the dipeptide benzyloxycarbonylglycylleucine (Cbz-Gly-Leu) as a sole nitrogen source, indicating the existence of a second carboxypeptidase. Using a new peptidase test, they biochemically confirmed this second enzyme and named it carboxypeptidase S (yscS). Subsequent genetic studies characterized CPS-deficient mutants and demonstrated that the absence of both carboxypeptidases Y and S does not affect mitotic growth, but prevents cells from utilizing certain exogenous peptides as nitrogen sources [wolf-1981-cps-mutants-abstract].

## Protein Structure and Domain Architecture

SpCPS belongs to the M20A subfamily of metallopeptidases, which is part of the larger M20 family within clan MH [MEROPS-M20-database]. The protein contains several characteristic domains including the peptidase M20 catalytic domain (IPR002933), the peptidase M20 dimer domain (IPR011650), the bacterial exopeptidase dimerization domain (IPR036264), and the M20A-specific domain (IPR047177) [PomBase-SPAC24C9.08-database].

The structural architecture of M20 family members is well characterized. Each monomer consists of a catalytic domain with an αβα sandwich fold that harbors a bimetallic active site center, and an oligomerization domain (also called the satellite or lid domain) that covers the active site and mediates homodimerization [MEROPS-M20-database]. The oligomerization domain contributes an invariant arginine residue that interacts with the alpha-carboxylate of the amino acid substrate at the S1' site, helping to orient substrates in the active site. The structure adopts a homodimeric configuration where hydrogen bonds between helices in the lid domain form the dimer interface.

The M20 family employs a "co-catalytic" mechanism involving two zinc ions per monomer at the active site center [MEROPS-M20-database]. In the *S. cerevisiae* ortholog, the enzyme is synthesized as a ~64 kDa precursor containing a transmembrane sequence spanning amino acids 20-40 that anchors it to the ER membrane [hecht-2014-vacuole-abstract]. Following glycosylation, mature forms of 74 or 77 kDa are produced, differing by one carbohydrate residue [spormann-1992-biogenesis-abstract].

SpCPS has four lysine residues (K16, K19, K32, and K33) in its putative N-terminal cytoplasmic domain, which are potential sites for ubiquitination required for MVB sorting [iwaki-2007-escrt-abstract]. This is consistent with findings in *S. cerevisiae* where K8 of the N-terminal cytoplasmic domain is ubiquitinated.

## Catalytic Activity and Substrate Specificity

As a zinc-dependent metallocarboxypeptidase, SpCPS depends on Zn²⁺ ions for catalytic function [hecht-2014-vacuole-abstract]. The enzyme hydrolyzes terminal or penultimate peptide bonds at the carboxy termini of peptides, releasing single amino acid residues [SGD-CPS1-database]. Based on studies of the *S. cerevisiae* ortholog CPS1 (YJL172W), the enzyme exhibits partially overlapping substrate specificity with carboxypeptidase Y (CPY) and demonstrates preference for glycine and leucine residues at the P1 site [hecht-2014-vacuole-abstract]. CPS contributes approximately 60% of vacuolar activity for hydrolyzing specific synthetic dipeptides.

The catalytic mechanism employed by M20 family members involves the following steps: (1) before substrate binding, a bridging water molecule is positioned between two Zn²⁺ ions and spatially close to the carboxylate group of the catalytic glutamate; (2) upon substrate binding, the enzyme undergoes a conformational change; (3) the catalytic glutamate acts as a general base, promoting nucleophilic attack of the metal-bound water on the substrate carbonyl carbon; (4) the carbonyl oxygen binds in an "oxyanion binding hole" formed by Zn1 and an imidazole group of histidine, polarizing the carbonyl group; (5) this leads to a tetrahedral intermediate that subsequently decays to products after proton transfer [MEROPS-M20-database]. The transition from an open to a closed enzyme conformation may be associated with formation of the catalytically competent active site.

## Subcellular Localization

SpCPS is localized to the vacuolar lumen, the primary degradative compartment of yeast cells [SGD-CPS1-database][hecht-2014-vacuole-abstract]. The yeast vacuole is analogous to the mammalian lysosome and performs multiple functions including metabolite storage, pH and ion homeostasis, and protein degradation. The vacuole harbors at least seven distinct proteases in *S. cerevisiae*, including two carboxypeptidases and two aminopeptidases [hecht-2014-vacuole-abstract].

## Trafficking Pathway: From Biosynthesis to Vacuolar Delivery

The intracellular trafficking of SpCPS represents one of the best-characterized biosynthetic cargo pathways through the endosomal system and multivesicular body (MVB) pathway. Unlike soluble vacuolar hydrolases such as carboxypeptidase Y (Cpy1), which require the Vps10 receptor for sorting from the trans-Golgi network (TGN) to the prevacuolar endosome (PVE), Cps1 is a transmembrane protein that reaches the PVE in a Vps10-independent manner [yanguas-2019-gga-abstract][iwaki-2006-vps10-abstract].

The trafficking of Cps1 from the TGN to the vacuole involves several key steps and molecular players. Carboxypeptidases Y and S, along with the Vps10 receptor and the vacuolar ATPase subunit Vph1, follow the carboxypeptidase Y (CPY) pathway from the TGN to the PVE [yanguas-2019-gga-abstract]. Using *S. pombe* quantitative live-cell imaging, biochemical, and genetic analyses, Yanguas and colleagues demonstrated that collaboration between the GGA (Golgi-localized, Gamma-ear-containing, ARF-binding) adaptors Gga22 and Gga21, and between Gga22 and the endosomal epsin Ent3, is required for efficient Cps1 exit from the TGN and its sorting in the PVE en route to the vacuole [yanguas-2019-gga-abstract]. These monomeric clathrin adaptors facilitate trafficking events of Cps1 in different organelles.

## MVB Sorting and Ubiquitin-Dependent Regulation

A critical aspect of CPS trafficking is its sorting into the intralumenal vesicles of multivesicular bodies, which is required for delivery to the vacuolar lumen rather than the limiting membrane. The MVB sorting pathway provides a mechanism for delivering transmembrane proteins into the lumen of the lysosome/vacuole [katzmann-2004-rsp5-abstract]. For CPS and other biosynthetic cargoes, MVB sorting is controlled by protein ubiquitination.

The ubiquitin ligase Rsp5 (a HECT-domain E3 ligase) appends K63-linked polyubiquitin chains on protein cargo, which promotes MVB trafficking [katzmann-2004-rsp5-abstract]. Katzmann and colleagues identified that a point mutation in Rsp5 (rsp5-326) specifically impairs ubiquitin modification of precursor carboxypeptidase S (pCPS) while preserving normal ubiquitination of other substrates. This established that ubiquitin modification acts *in cis* as a signal for the sorting of cargoes into the MVB pathway. Multiple Rsp5 domains participate in cargo modification: the C2 domain aids membrane recruitment, WW domains facilitate protein-protein interactions, and the HECT domain catalyzes ubiquitin transfer to target substrates [katzmann-2004-rsp5-abstract].

The ubiquitinated cargo is then recognized by the endosomal sorting complexes required for transport (ESCRT). ESCRT-0 (the Vps27p/Hse1p complex) recognizes ubiquitinated cargo via three UIM (ubiquitin-interacting motif) domains and subsequently recruits ESCRT-I, ESCRT-II, and ESCRT-III [iwaki-2007-escrt-abstract]. Together, these ESCRT complexes drive cargo incorporation into and formation of intralumenal vesicles within MVBs.

## ESCRT Machinery and Class E Vps Proteins in S. pombe

The class E vps genes are largely conserved between *S. cerevisiae*, *S. pombe*, and mammals [iwaki-2007-escrt-abstract]. In *S. pombe*, Iwaki and colleagues demonstrated that the sst4/vps27 and sst6 genes are essential for proper vacuolar sorting of carboxypeptidase Y and the MVB marker Ub-GFP-CPS [iwaki-2007-escrt-abstract]. Disruption of various other class E vps homologues also resulted in defects in sorting of CPY and Ub-GFP-CPS. This study was the first to demonstrate that the MVB pathway functions in *S. pombe* and that the roles of class E Vps proteins in MVB sorting are conserved.

The *S. pombe* Sst4/Vps27 protein contains VHS, FYVE, and UIM domains, similar to its *S. cerevisiae* counterpart [iwaki-2007-escrt-abstract]. Additionally, *S. pombe* possesses a mammalian AMSH homologue (Sst2) that functions as a class E Vps protein. Sst4p (Vps27 homolog) is required for efficient transport of the fluorescent dye FM4-64 and Ub-GFP-CPS fusion protein to the vacuole, confirming its role in both endocytic membrane trafficking and anterograde sorting of biosynthesized proteins into MVBs.

## Vacuolar Processing and Maturation

Once delivered to the vacuole, the precursor form of CPS (pCPS) must be processed to generate the mature, soluble enzyme (mCPS). In *S. cerevisiae*, the carboxypeptidase yscS precursor molecules are delivered to the vacuole in a membrane-bound form via the secretory pathway [spormann-1992-biogenesis-abstract]. After assembly into the vacuolar membrane, proteinase yscB (Prb1) cleaves the precursor molecules to release soluble carboxypeptidase yscS forms into the lumen of the vacuole. Similarly, in *S. pombe*, CPS is processed by proteinase B and released into the vacuolar lumen [hecht-2014-vacuole-abstract].

Mature carboxypeptidase S appears soluble in the vacuolar lumen, while precursor proteins accumulate at the vacuolar membrane [spormann-1992-biogenesis-abstract]. An N-terminal hydrophobic domain mediates membrane binding in the precursor form. The enzyme is synthesized as two active high molecular mass precursor forms which are converted to the mature forms with a half-time of approximately 20 minutes.

## Biological Role and Cellular Functions

As a vacuolar hydrolase, SpCPS participates in the terminal degradation of proteins and peptides within the vacuolar lumen. The vacuole serves as the major degradative organelle of yeast cells, breaking down substrates delivered by autophagy, endocytosis, and biosynthetic pathways [hecht-2014-vacuole-abstract]. The proteolytically produced amino acids are recycled for maintenance of cellular functions, particularly during nutrient starvation conditions.

Studies in *S. cerevisiae* have revealed several phenotypes associated with CPS1 deletion: decreased growth rate, leucine auxotrophy, elevated nicotinamide sensitivity, increased heat sensitivity, reduced filamentous growth, and decreased competitive fitness [SGD-CPS1-database]. Expression of CPS1 is induced under low-nitrogen conditions, suggesting a role in amino acid recycling during nutrient limitation. Overexpression results in a slow growth phenotype.

The *S. cerevisiae* CPS1 gene is involved in 97 total interactions: 42 physical interactions (primarily identified through affinity capture-MS) and 55 genetic interactions (predominantly negative genetic interactions) [SGD-CPS1-database]. These extensive interaction networks suggest that CPS integrates with multiple cellular processes.

## Relationship to Other Vacuolar Proteases

The yeast vacuole contains at least two carboxypeptidases with partially overlapping substrate specificities [hecht-2014-vacuole-abstract]. While carboxypeptidase Y (CPY/Prc1) is a serine protease, carboxypeptidase S (CPS/Cps1) is a zinc metallopeptidase belonging to a distinct protein family. Both enzymes contribute to the hydrolysis of C-terminal amino acids from peptide substrates in the vacuolar lumen, but they differ in their catalytic mechanisms, structural organization, and trafficking requirements.

In *S. pombe*, the vacuolar protease network includes Isp6, a starvation-specific serine protease that is essential for autophagy-dependent protein degradation during nitrogen starvation [nakashima-2006-isp6-abstract]. Studies have shown that *isp6* disruption mutants grow normally under standard conditions but are defective in large-scale protein degradation during nitrogen starvation and exhibit infertility under nutrient-poor conditions. Isp6 and its paralog Psp3 are required for processing autophagy-delivered cargo in the vacuole. SpCPS likely works in concert with these endopeptidases, with Isp6 and Psp3 providing initial cleavages and carboxypeptidases like SpCPS and Cpy1 completing the breakdown of peptide products to free amino acids. This coordinated action is critical for amino acid recycling during nutrient starvation and for supporting nitrogen-dependent developmental processes such as mating and sporulation in fission yeast.

## Open Questions

Several aspects of SpCPS biology remain incompletely understood:

1. **Precise substrate specificity:** While the *S. cerevisiae* ortholog shows preference for Gly and Leu at the P1 site, the full substrate specificity profile of SpCPS has not been systematically characterized. Understanding whether SpCPS has similar or distinct preferences would clarify its functional role.

2. **Regulation of expression and activity:** CPS1 expression is induced under low-nitrogen conditions in *S. cerevisiae*, but the transcriptional and post-translational regulatory mechanisms controlling SpCPS expression and activity in *S. pombe* are not well characterized.

3. **Functional redundancy with other vacuolar peptidases:** The extent to which SpCPS function overlaps with or complements other vacuolar proteases, particularly during autophagy and nitrogen starvation, remains to be fully elucidated.

4. **Role in specific physiological processes:** While *cps1* null mutants in *S. cerevisiae* show phenotypes related to sporulation and stress responses, the specific physiological roles of SpCPS in *S. pombe* sporulation, mating, and stress adaptation have not been directly investigated.

5. **Three-dimensional structure:** No experimental structure of SpCPS or the *S. cerevisiae* ortholog CPS1 is currently available. Structural determination would provide insights into substrate specificity determinants and catalytic mechanism.

6. **Ubiquitination sites and regulation:** While four lysine residues (K16, K19, K32, K33) in the N-terminal cytoplasmic domain are potential ubiquitination sites, the specific residue(s) modified and the regulatory consequences of this modification in *S. pombe* remain to be determined.

7. **Evolution and functional conservation:** While SpCPS is clearly a homolog of *S. cerevisiae* CPS1, detailed evolutionary analysis of the M20A peptidase subfamily across fungi and the degree of functional conservation would be valuable.

## References

- [hecht-2014-vacuole-abstract] Hecht KA, O'Donnell AF, Brodsky JL. The proteolytic landscape of the yeast vacuole. Cell Logist. 2014;4:e28023. PMID: 24843828. PMCID: PMC4022603. DOI: 10.4161/cl.28023. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4022603/

- [iwaki-2007-escrt-abstract] Iwaki T, Onishi M, Ikeuchi M, Kita A, Sugiura R, Giga-Hama Y, Fukui Y, Takegawa K. Essential roles of class E Vps proteins for sorting into multivesicular bodies in Schizosaccharomyces pombe. Microbiology (Reading). 2007;153(Pt 8):2753-2764. PMID: 17660439. PMCID: PMC2885615. DOI: 10.1099/mic.0.2007/006072-0. URL: https://pubmed.ncbi.nlm.nih.gov/17660439/

- [iwaki-2006-vps10-abstract] Iwaki T, Hosomi A, Tokudomi S, Kusunoki Y, Fujita Y, Giga-Hama Y, Tanaka N, Takegawa K. Vacuolar protein sorting receptor in Schizosaccharomyces pombe. Microbiology (Reading). 2006;152(Pt 5):1523-1532. PMID: 16622069. DOI: 10.1099/mic.0.28627-0. URL: https://pubmed.ncbi.nlm.nih.gov/16622069/

- [katzmann-2004-rsp5-abstract] Katzmann DJ, Sarkar S, Chu T, Audhya A, Emr SD. Multivesicular body sorting: ubiquitin ligase Rsp5 is required for the modification and sorting of carboxypeptidase S. Mol Biol Cell. 2004;15(2):468-480. PMID: 14657247. PMCID: PMC329214. DOI: 10.1091/mbc.E03-07-0473. URL: https://pubmed.ncbi.nlm.nih.gov/14657247/

- [nakashima-2006-isp6-abstract] Nakashima A, Hasegawa T, Mori S, Ueno M, Tanaka S, Ushimaru T, Sato S, Uritani M. A starvation-specific serine protease gene, isp6+, is involved in both autophagy and sexual development in Schizosaccharomyces pombe. Curr Genet. 2006;49(6):403-413. PMID: 16550352. DOI: 10.1007/s00294-006-0067-0. URL: https://pubmed.ncbi.nlm.nih.gov/16550352/

- [spormann-1992-biogenesis-abstract] Spormann DO, Heim J, Wolf DH. Biogenesis of the yeast vacuole (lysosome). The precursor forms of the soluble hydrolase carboxypeptidase yscS are associated with the vacuolar membrane. J Biol Chem. 1992;267(12):8021-8029. PMID: 1569061. URL: https://pubmed.ncbi.nlm.nih.gov/1569061/

- [wolf-1977-cpsy-abstract] Wolf DH, Weiser U. Studies on a carboxypeptidase Y mutant of yeast and evidence for a second carboxypeptidase Activity. Eur J Biochem. 1977;73(2):553-556. DOI: 10.1111/j.1432-1033.1977.tb11350.x. URL: https://febs.onlinelibrary.wiley.com/doi/10.1111/j.1432-1033.1977.tb11350.x

- [wolf-1981-cps-mutants-abstract] Zubenko GS, Mitchell AP, Jones EW. Carboxypeptidase S- and carboxypeptidase Y-deficient mutants of Saccharomyces cerevisiae. J Bacteriol. 1981;147(2):461-468. PMID: 7021530. PMCID: PMC216060. URL: https://pubmed.ncbi.nlm.nih.gov/7021530/

- [yanguas-2019-gga-abstract] Yanguas F, Moscoso-Romero E, Valdivieso MH. Ent3 and GGA adaptors facilitate diverse anterograde and retrograde trafficking events to and from the prevacuolar endosome. Sci Rep. 2019;9(1):10747. PMID: 31341193. PMCID: PMC6656748. DOI: 10.1038/s41598-019-47035-5. URL: https://www.nature.com/articles/s41598-019-47035-5

- [MEROPS-M20-database] MEROPS - the Peptidase Database. M20 family summary. EMBL-EBI. URL: https://www.ebi.ac.uk/merops/cgi-bin/famsum?family=M20

- [SGD-CPS1-database] Saccharomyces Genome Database. CPS1/YJL172W. URL: https://www.yeastgenome.org/locus/S000003708

- [PomBase-SPAC24C9.08-database] PomBase. SPAC24C9.08/cps1. URL: https://www.pombase.org/gene/SPAC24C9.08


## Citations

1. MEROPS-M20-database.md
2. PomBase-SPAC24C9.08-database.md
3. SGD-CPS1-database.md
4. hecht-2014-vacuole-abstract.md
5. iwaki-2006-vps10-abstract.md
6. iwaki-2007-escrt-abstract.md
7. katzmann-2004-rsp5-abstract.md
8. nakashima-2006-isp6-abstract.md
9. spormann-1992-biogenesis-abstract.md
10. wolf-1977-cpsy-abstract.md
11. wolf-1981-cps-mutants-abstract.md
12. yanguas-2019-gga-abstract.md