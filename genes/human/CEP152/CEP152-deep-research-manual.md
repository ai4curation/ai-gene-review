# Manual deep research: human CEP152 (O94986)

Date: 2026-07-18

Automated deep-research providers were attempted before this manual synthesis. Falcon/Edison returned HTTP 402 and the Perplexity-lite fallback returned HTTP 401, so this file records a source-grounded manual synthesis rather than masquerading as provider output.

## Executive summary

CEP152 is a non-enzymatic, coiled-coil scaffold of the pericentriolar material and proximal parent-centriole region. Together with CEP63 it builds a higher-order cylindrical assembly. Its N-terminal PLK4-binding region recruits and positions the master centriole-biogenesis kinase PLK4, while another region engages CPAP/CENPJ. This spatial adaptor function is required for procentriole initiation and normal centrosome duplication. The direct evidence is unusually convergent: depletion phenotypes, rescue/mutant analysis, interaction mapping, super-resolution localization, biochemistry, and structural reconstitution all support the same mechanism.

CEP152 is reused in specialized centriole-amplification contexts. Mouse multiciliated-cell work places Cep152 at DEUP1-positive deuterosomes and shows that DEUP1 assemblies concentrate Cep152 and Plk4. This supports the transferred human annotations as plausible, specialized biology, while leaving direct human tissue evidence as a gap.

A separate 2022 study identifies CEP152 as both an APC/C interaction partner and substrate at centrosomes/spindle poles. Timed CEP152 ubiquitylation dismantles an inhibitory CEP152-CEP63-CEP57 complex, freeing CEP57 to recruit pericentrin and support microtubule nucleation and spindle assembly. This is a direct, annotation-worthy mitotic role, but it does not make CEP152 a ubiquitin ligase or a microtubule nucleator.

## Molecular architecture and centriole duplication

The initial human functional studies defined CEP152 as a scaffold rather than an enzyme. Drosophila Asterless and human CEP152 use separated regions to bind PLK4 and Sas-4/CPAP [PMID:20852615 "Here we show that the centriolar protein Asterless (Asl; human orthologue CEP152) provides a conserved molecular platform, the amino terminus of which interacts with the cryptic Polo box of Plk4 whereas the carboxy terminus interacts with the centriolar protein Sas-4 (CPAP in humans)."] Human depletion blocks duplication [PMID:20852615 "Depletion of Asl or CEP152 caused failure of centrosome duplication;"]

Independent work directly mapped human CEP152 binding to the PLK4 cryptic Polo-box and showed that CEP152 loss prevents PLK4 recruitment and centriole duplication [PMID:21059844 "In this study, we show that the pericentriolar material protein, Cep152, interacts with the distinctive cryptic Polo-box of Plk4 via its N-terminal domain and is required for Plk4-induced centriole overduplication."] [PMID:21059844 "Our results suggest that Cep152 recruits Plk4 and CPAP to the centrosome to ensure a faithful centrosome duplication process."] A companion human/Xenopus study similarly found that depletion prevents normal and PLK4-driven centriole formation [PMID:21059850 "Depletion of Cep152 prevents both normal centriole duplication and Plk4-induced centriole amplification and results in a failure to localize Sas6 to the centriole, an early step in duplication."] and mapped the interaction to the N-terminal 217 residues [PMID:21059850 "The interaction requires the N-terminal 217 residues of Cep152 and the crypto Polo-box of Plk4."]

Super-resolution work refined this into a scaffold-switch model: PLK4 moves from an inner CEP192 ring to an outer CEP152 ring as the daughter centriole matures [PMID:24997597 "We show that Plk4 relocalizes from the inner Cep192 ring to the outer Cep152 ring as newly recruited Cep152 assembles around the Cep192-encircled daughter centriole."] A CEP152 mutation that weakens PLK4 binding impairs procentriole formation and chromosome segregation [PMID:24997597 "A cancer-associated Cep152 mutation impairing the Plk4 interaction induced defects in procentriole assembly and chromosome segregation."]

Biochemical and structural studies then showed that CEP63 and CEP152 form a heterotetrameric coiled-coil building block and self-assemble into a PLK4-recruiting cylinder [PMID:30858376 "Here we show that two human pericentriolar material scaffolds, Cep63 and Cep152, cooperatively generate a heterotetrameric α-helical bundle that functions in conjunction with its neighboring hydrophobic motifs to self-assemble into a higher-order cylindrical architecture capable of recruiting downstream components, including Plk4, a key regulator for centriole duplication."] Disrupting the assembly blocks PLK4-mediated duplication [PMID:30858376 "Mutations disrupting the self-assembly abrogate Plk4-mediated centriole duplication."] A later analysis directly resolved the stepwise assembly [PMID:37433832 "we showed that two long coiled-coil proteins, Cep63 and Cep152, form a heterotetrameric building block that undergoes a stepwise formation into higher molecular weight complexes, ultimately generating a cylindrical architecture around a centriole."] and linked assembly-defective mutants to abnormal CEP152 organization, PLK4 positioning, and duplication [PMID:37433832 "Mutants defective in Cep63•Cep152 heterotetramer formation displayed crippled pericentriolar Cep152 organization, polo-like kinase 4 (Plk4) relocalization to the procentriole assembly site, and Plk4-mediated centriole duplication."]

## Centrosomal network and location

CEP152 participates in a centrosomal microcephaly-protein hierarchy with CDK5RAP2, WDR62, and CEP63 [PMID:26297806 "Primary microcephaly (MCPH) associated proteins CDK5RAP2, CEP152, WDR62 and CEP63 colocalize at the centrosome."] The proteins interact and are interdependent for centrosomal localization [PMID:26297806 "We found that they interact to promote centriole duplication and form a hierarchy in which each is required to localize another to the centrosome"] This network provides biological context for the CEP131 interaction but does not convert every physical contact into a distinct molecular activity.

Multiple microscopy and proteomics studies independently support centrosome, centriole, procentriole, and pericentriolar-material localization. The PMID:22020124 cached abstract foregrounds STIL and CPAP and does not describe the CEP152 assay; because the full text was not locally available, the associated experimental centriole annotation was retained in deference to curator access and because the location is strongly corroborated by independent direct studies.

## Multiciliated cells and deuterosomes

In a mouse oviduct multiciliated-cell model, DEUP1 assemblies spatially concentrate Cep152 and Plk4 [PMID:33658185 "Using an optogenetic approach, we demonstrated that self-assembly and the C-terminal half of Deup1 were sufficient to spatially compartmentalize centrosomal protein 152 (Cep152) and polo like kinase 4 (Plk4), master components for centriole biogenesis, in the cytoplasm."] Mouse tracheal epithelial cells show Cep152 at both parent centrioles and deuterosomes [PMID:33627667 "Cep152 decorated parental centrioles (arrows), deuterosomes (arrowheads indicating typical ones), and, in stages V–VI, a spot at the proximal side of the nascent centrioles or basal bodies in mTECs8."] This supports the orthology-based human deuterosome and multiciliated epithelial differentiation annotations as non-core/context-specific. The evidence does not establish that every human CEP152 isoform or every multiciliated cell uses an identical route.

## Mitotic spindle assembly

APC/C is recruited to spindle poles through CEP152, which is both an interaction partner and substrate [PMID:34878135 "Recruitment of the APC/C to spindle poles requires the centrosomal protein Cep152, and we identified Cep152 as both an APC/C interaction partner and an APC/C substrate."] Timed ubiquitylation of CEP152 releases CEP57 from an inhibitory CEP152-CEP63-CEP57 complex, permitting CEP57-pericentrin interaction and microtubule nucleation [PMID:34878135 "The APC/C-mediated ubiquitylation of Cep152 at the centrosome releases Cep57 from this inhibitory complex and enables its interaction with pericentrin, a critical step in promoting microtubule nucleation."] This supports `mitotic spindle assembly` as a new biological-process annotation. The mechanistic direction is temporal and complex-dependent, so a simple positive-regulation-of-microtubule-nucleation annotation could obscure the initial inhibitory sequestration and was not proposed.

## Disease and isoforms

Pathogenic biallelic CEP152 variants cause primary microcephaly and Seckel syndrome. A premature-termination allele prevented centrosome localization in transfected cells [PMID:20598275 "The third affected child was compound heterozygous for the missense mutation plus a second, premature-termination mutation truncating a third of the protein and preventing its localization to centrosomes in transfected cells."] The disease association supports the physiological importance of centrosomal localization but does not itself identify a separate molecular function.

UniProt lists four alternative products. None of the reviewed studies supplied sufficiently clear isoform-resolved functional comparisons to justify functional-isoform classes or isoform-specific GO decisions.

## PAINT assessment

The local PANTHER PAINT table (`interpro/panther/PTHR10337/PTHR10337-paint.tsv`) assigns centrosome and centriole-replication functions at node `PTN000818649`, with human CEP152 and mouse Cep152 among the evidence sources. This node is specific to the CEP152 lineage even though the broader family contains unrelated SHC subfamilies. The two IBA annotations are therefore accepted: their propagation scope is coherent, and the functions are independently established experimentally in human CEP152. Because O94986 is itself a PAINT seed, the IBA records are corroborative rather than independent evidence.

## Curation conclusions

- Core molecular function: `protein-macromolecule adaptor activity` (GO:0030674).
- Core process: `centriole replication` (GO:0007099), with centrosome duplication as the broader process.
- Defining locations/complex: pericentriolar material, procentriole, centrosome/centriole, and procentriole replication complex.
- Specialized non-core context: deuterosome and de novo centriole assembly during multiciliated epithelial differentiation.
- New direct process: `mitotic spindle assembly` (GO:0090307).
- Generic `protein binding` should not be retained as the final functional representation. PLK4 records can be made specific as `protein kinase binding`; the CENPJ record is best represented by adaptor activity; other interaction-only records remain biologically plausible but are over-annotated as GO molecular functions.
