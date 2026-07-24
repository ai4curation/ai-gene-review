---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/RAD51C
affinage_run_date: 2026-06-10T06:43:36
uniprot_accession: O43502
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 42
citation_count: 42
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for RAD51C (human)

## Current model (mechanistic narrative)

RAD51C is a central RAD51 paralog that organizes homologous recombination (HR) by serving as the shared, catalytic hub of two distinct paralog complexes—BCDX2 (RAD51B–RAD51C–RAD51D–XRCC2) and CX3 (RAD51C–XRCC3)—and is required for assembly of both [PMID:11744692, PMID:11842113, PMID:11912211]. RAD51C contributes ssDNA-binding, DNA-stimulated ATPase, and homologous-pairing/strand-annealing activities to these complexes, and acts as a recombination mediator that relieves RPA inhibition to promote RAD51 loading [PMID:11331762, PMID:11751636, PMID:15141025]. Cryo-EM and X-ray structures show that within BCDX2 the RAD51C–RAD51D–XRCC2 module mimics three RAD51 protomers to nucleate and extend RAD51 filaments on ssDNA in a manner dependent on the coupled ATPase activities of RAD51B and RAD51C, while CX3 binds ATP like RAD51 and contributes a polymerization/5′-capping motif governing replication fork protection, restart, and reversal [PMID:37344587, PMID:37488098]. Functionally, RAD51C is required for DNA-damage-induced RAD51 focus formation, Holliday-junction branch migration and resolution, and BRCA2-independent nuclear import of RAD51, and it also acts upstream in damage signaling by enabling ATM/NBS1/RPA-dependent recruitment and CHK2-dependent checkpoint activation [PMID:12000837, PMID:14716019, PMID:19451272, PMID:19783859]. Beyond canonical HR it joins a PALB2–BRCA2 complex, localizes to mitochondrial nucleoids with XRCC3 to support mtDNA maintenance, and stimulates ALKBH3-mediated demethylation repair [PMID:24141787, PMID:29158291, PMID:31642493]. RAD51C is a tumor suppressor: biallelic mutation causes a Fanconi anemia–like disorder (FANCO) and monoallelic loss-of-function confers breast and ovarian cancer susceptibility with PARP-inhibitor sensitivity, while reversion mutations and loss of promoter methylation drive PARPi resistance [PMID:20400963, PMID:28588062, PMID:34321239].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0003677 DNA binding, GO:0140657 ATP-dependent activity, GO:0140097 catalytic activity, acting on DNA, GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome, GO:0005739 mitochondrion, GO:0005829 cytosol, GO:0005815 microtubule organizing center
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-1643685 Disease, R-HSA-1640170 Cell Cycle, R-HSA-1474165 Reproduction, R-HSA-69306 DNA Replication
- **partners:** XRCC3, RAD51B, RAD51D, XRCC2, RAD51, PALB2, BRCA2, ALKBH3
- **complexes:** BCDX2 (RAD51B-RAD51C-RAD51D-XRCC2), CX3 (RAD51C-XRCC3), PALB2-RAD51C-BRCA2 complex, mitochondrial nucleoid

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | Medium | RAD51C was identified as a member of the RAD51 protein family encoding a 376 aa protein. Yeast two-hybrid experiments showed RAD51C binds XRCC3 and RAD51B but not itself, suggesting a mediator/accessory role analogous to yeast Rad55/Rad57. | PMID:9469824 | Nucleic acids research |
| 2001 | High | RAD51C and XRCC3 copurify as a stable complex from baculovirus-infected insect cells and from HeLa cell endogenous extracts. The purified RAD51C–XRCC3 complex binds single-stranded DNA (but not duplex DNA) to form protein–DNA networks visualized by electron microscopy. | PMID:11459987 | Proceedings of the National Academy of Sciences of the United States of America |
| 2001 | High | The purified XRCC3–RAD51C complex catalyzes homologous pairing in vitro; RAD51C alone also shows homologous pairing activity (though reduced), indicating RAD51C is the catalytic subunit. XRCC3 enhances DNA binding of the complex. Both proteins form filamentous structures with ssDNA as observed by electron microscopy. | PMID:11331762 | Proceedings of the National Academy of Sciences of the United States of America |
| 2001 | High | RAD51B and RAD51C form a stable heterodimeric complex with ssDNA-binding and ssDNA-stimulated ATPase activities. The RAD51B–RAD51C complex acts as a recombination mediator by partially alleviating RPA competition with RAD51 for ssDNA substrate binding, thereby facilitating RAD51-catalyzed DNA strand exchange. | PMID:11751636 | Genes & development |
| 2001 | High | RAD51B and RAD51C form an endogenous heterocomplex in human cells (HeLa, MCF10A, MCF7). Co-immunoprecipitation showed RAD51C is central to a larger complex containing RAD51B, RAD51D, XRCC2, and XRCC3, but RAD51 was not found in these complexes. | PMID:11744692 | The Journal of biological chemistry |
| 2002 | High | RAD51C participates in two distinct in vivo protein complexes: RAD51B–RAD51C–RAD51D–XRCC2 (BCDX2) and RAD51C–XRCC3 (CX3). XRCC2 and RAD51D co-precipitate with RAD51C but not XRCC3; conversely, XRCC3 pulls down with RAD51C but not XRCC2/RAD51D. RAD51 co-precipitates with XRCC3 (not XRCC2 or RAD51D), suggesting a RAD51–RAD51C–XRCC3 complex. | PMID:11842113 | Nucleic acids research |
| 2002 | High | XRCC3 and RAD51C interact directly in human cells. RAD51C (but not XRCC3) interacts with RAD51B, RAD51D, and XRCC2, confirming two paralog complexes. Overexpression of XRCC3 elevates endogenous RAD51C levels, suggesting dimerization stabilizes RAD51C. | PMID:11842112 | Nucleic acids research |
| 2002 | High | Mammalian RAD51C deficiency (CL-V4B hamster cell mutant with exon 5 deletion) causes hypersensitivity to interstrand crosslinking agents (MMC, cisplatin), alkylating agents, and camptothecin; impaired RAD51 focus formation after DNA damage; increased chromosomal aberrations; reduced sister chromatid exchanges; and a reduced level of sister chromatid cohesion. | PMID:12000837 | Nucleic acids research |
| 2002 | High | RAD51C (RAD51L2) deficiency in hamster irs3 cells causes reduced sister chromatid exchange, increased isochromatid breaks, and decreased RAD51 focus formation after DNA damage. Complementation was specific to RAD51L2; other RAD51-like genes or RAD51 itself did not rescue. RAD51L2 is required for formation of both RAD51 paralog complexes; neither complex forms in irs3 cells. | PMID:11912211 | The Journal of biological chemistry |
| 2002 | High | Purified RAD51B and RAD51C proteins bind both single- and double-stranded DNA with preference for 3'-tailed duplexes; both exhibit DNA-stimulated ATPase activity. RAD51C displays ATP-independent DNA duplex destabilization activity (reported as apparent strand exchange). RAD51B–RAD51C heterodimer interacts weakly with RAD51. | PMID:12427746 | The Journal of biological chemistry |
| 2003 | High | Non-conservative mutation of the putative ATP-binding domain of RAD51C (RAD51L2) severely reduces its function, while a conservative mutation causes partial loss. The C-terminal domain functions as a nuclear localization signal. RAD51L2-deficient cells show significantly reduced homology-directed repair (gene conversion) of a chromosomal DSB, partially restored by ectopic RAD51L2 expression. | PMID:12966089 | The Journal of biological chemistry |
| 2003 | Medium | Drosophila spn-D encodes a RAD51C ortholog required exclusively during meiosis. Single and double spn-B/spn-D mutants showed no sensitization to DSB-inducing agents (X-rays, MMS) in mitotic cells, indicating meiosis-specific (not somatic) function of this RAD51C ortholog in Drosophila. | PMID:14504227 | Genetics |
| 2004 | High | Extracts from cells with RAD51C or XRCC3 mutations have reduced Holliday junction (HJ) resolvase activity. Depletion of RAD51C from fractionated human extracts abolished branch migration and HJ resolution activity, both of which were restored by complementation with RAD51 paralog complexes containing RAD51C. RAD51C is thus required for HJ processing in human cells. | PMID:14716019 | Science (New York, N.Y.) |
| 2004 | High | RNAi-mediated depletion of RAD51C in human cells reduces homologous recombination frequency and causes XRCC3 protein instability (XRCC3 levels drop sharply upon RAD51C depletion), indicating XRCC3 stability depends on heterodimerization with RAD51C. RAD51C-depleted cells are hypersensitive to MMC and ionizing radiation specifically in S and G2/M phases. | PMID:15292210 | The Journal of biological chemistry |
| 2004 | High | The RAD51B–RAD51C–RAD51D–XRCC2 (BCDX2) complex preferentially binds branched DNA structures (Y-shaped DNA and synthetic Holliday junctions) over linear or nicked DNA. The BCDX2 complex also catalyzes strand-annealing between complementary ssDNA molecules. | PMID:15141025 | Nucleic acids research |
| 2004 | Medium | Residues 14–25 of RAD51C define a protein interaction hotspot used in both XRCC3–RAD51C and RAD51B–RAD51C interactions. Point mutations in this region altered interactions with both XRCC3 and RAD51B in two-hybrid assays. A synthetic peptide from this region fused to a membrane transduction domain inhibited subnuclear RAD51 assembly and sensitized cells to cisplatin. | PMID:15126333 | Cancer research |
| 2005 | Medium | RAD51C depletion in human cells leads to reduced steady-state nuclear RAD51 levels and diminished DNA damage-induced increase in nuclear RAD51. RAD51C contains a functional nuclear localization signal and undergoes damage-induced increase in nuclear accumulation. RAD51C plays a role in regulating RAD51 nuclear entry and ubiquitin-mediated proteasome degradation of RAD51 during recombinational repair. | PMID:16215984 | Journal of cellular biochemistry |
| 2006 | High | HJ resolvase activity co-elutes with the ~80 kDa RAD51C–XRCC3 complex by gel filtration, indicating CX3 is the active complex. RAD51C localizes to mouse meiotic chromosomes at pachytene/diplotene, co-localizing with MLH1 at crossover sites, implicating RAD51C–XRCC3 in resolution of meiotic recombination intermediates. | PMID:17114795 | The Journal of biological chemistry |
| 2006 | High | RAD51C controls the choice between short-tract and long-tract gene conversion in sister chromatid recombination. Rad51C-deficient CL-V4B cells show biased long-tract gene conversions (bimodal distribution <1 kb or >3.2 kb) that are restored to normal short-tract bias upon Rad51C re-expression, indicating RAD51C suppresses long-tract and gene amplification events. | PMID:16954385 | Molecular and cellular biology |
| 2007 | High | RAD51C is essential for murine viability (null mice die in early embryogenesis). Hypomorphic Rad51c mice display sexually dimorphic meiotic defects: spermatocytes arrest in early meiotic prophase I (consistent with a role in early RAD51-mediated recombination), while oocytes progress to metaphase I but exhibit precocious sister chromatid separation, aneuploidy, and broken chromosomes at metaphase II. Rad51c-null MEFs show markedly reduced HJ resolution activity. | PMID:17312021 | The Journal of cell biology |
| 2007 | Medium | RAD51C deficiency in CL-V4B cells increases the number of centrosomes in mitosis, leading to aberrant mitotic spindles, suggesting a role for RAD51C in maintaining correct centrosome numbers. | PMID:17268176 | Cytogenetic and genome research |
| 2009 | High | RAD51C is required for activation of checkpoint kinase CHK2 and cell cycle arrest in response to DNA damage. RAD51C accumulates at damage sites concomitantly with RAD51 and is retained after RAD51 disassembly (consistent with early and late function). RAD51C recruitment depends on ATM, NBS1, and RPA, placing it after DNA end resection but before RAD51 assembly. | PMID:19451272 | The Journal of cell biology |
| 2009 | High | Rad51c deficiency leads to embryonic lethality, which is partially rescued on a Trp53-null background. Double-heterozygous cis mice (simultaneous LOH of both Rad51c and Trp53) develop tumors of specialized sebaceous glands (distinct from Trp53-only tumors), establishing direct tumor suppressor function for Rad51c and epistatic interaction with Trp53. | PMID:19155299 | Cancer research |
| 2009 | High | RAD51C undergoes damage-induced translocation from cytoplasm to nucleus; RAD51C contains a functional nuclear localization signal. Subcellular fractionation showed that RNAi depletion of RAD51C in HeLa and Capan-1 cells results in lower steady-state nuclear RAD51 levels and diminished damage-induced nuclear RAD51 increase, demonstrating a BRCA2-independent mechanism for RAD51 nuclear entry dependent on RAD51C. | PMID:19783859 | The Journal of biological chemistry |
| 2009 | Medium | RAD51C deficiency in HCT116 cells leads to centrosome aberrations in an ATR–CHK1-dependent manner and increased aneuploidy. Treatment with caffeine, ATR siRNA, or CHK1 inhibitor/siRNA reduced centrosome aberrations, showing the ATR–CHK1 pathway mediates centrosome amplification in Rad51C-deficient cells. | PMID:19403737 | Nucleic acids research |
| 2011 | High | RAD51C deficiency causes ICL sensitivity, chromatid-type errors, and G2/M accumulation consistent with Fanconi anemia phenotype. RAD51C is dispensable for ICL unhooking and FANCD2 monoubiquitination but essential for HR, confirming its downstream role in ICL repair. RAD51C also controls intra-S-phase checkpoint through CHK2 activation. Pathological FA and cancer-associated RAD51C mutants show distinct defects in HR versus DNA damage signaling. | PMID:22167183 | The Journal of biological chemistry |
| 2013 | High | RAD51C is part of a novel protein complex containing PALB2 and BRCA2. The PALB2 WD40 domain directly and independently binds both RAD51C and BRCA2. Breast cancer–associated PALB2 WD40 missense mutants partially disrupt PALB2–RAD51C–BRCA2 complex formation and decrease HR capacity. Cancer-associated RAD51C mutants also show decreased PALB2 complex formation. | PMID:24141787 | Oncogene |
| 2018 | Medium | RAD51C/XRCC3 localizes to mitochondria as a component of the mitochondrial nucleoid, with nucleus-independent roles in mtDNA maintenance. RAD51C/XRCC3 localizes to the mtDNA D-loop regulatory region along with mitochondrial polymerase POLG, and this recruitment depends on Twinkle helicase. RAD51C/XRCC3-deficient cells exhibit reduced mtDNA synthesis, increased mtDNA lesions, and destabilized POLG on mtDNA. | PMID:29158291 | Molecular and cellular biology |
| 2019 | Medium | RAD51C directly interacts with the ALKBH3 DNA demethylase. The RAD51C–ALKBH3 interaction stimulates ALKBH3-mediated repair of methyl-adducts in 3'-tailed DNA substrates (which serve as RAD51 recombinase substrates). Loss of this interaction impairs ALKBH3 function both in vitro and in vivo. | PMID:31642493 | Nucleic acids research |
| 2023 | High | Cryo-EM structure of the BCDX2 complex (RAD51B–RAD51C–RAD51D–XRCC2) reveals RAD51C–RAD51D–XRCC2 mimics three RAD51 protomers aligned within a nucleoprotein filament, while RAD51B is highly dynamic. Biochemical and single-molecule analyses show BCDX2 stimulates nucleation and extension of RAD51 filaments on ssDNA in reactions dependent on the coupled ATPase activities of RAD51B and RAD51C. BCDX2 orchestrates RAD51 assembly for replication fork protection and DSB repair. | PMID:37344587 | Nature |
| 2023 | High | X-ray co-crystal structure of RAD51C–XRCC3 (CX3) with bound ATP analog reveals ATP binding matching RAD51 recombinase, distinct CX3 interfaces, and an unappreciated polymerization motif. Structural analysis combined with CRISPR/Cas9-edited human cells established separable RAD51C functions in DNA replication fork protection, restart, and reversal through discrete CX3 regions for DNA binding and implied 5' RAD51 filament capping. | PMID:37488098 | Nature communications |
| 2022 | High | A cluster of RAD51C missense mutations in and around the Walker A (ATP-binding) box disrupts HR, interactions with multiple RAD51 paralogs (RAD51B, RAD51D, XRCC2), ssDNA binding, and ATP hydrolysis. Structural modeling predicts ATP binding at the interface of RAD51C with other RAD51 paralogs, explaining how Walker A mutations simultaneously disrupt multiple paralog interactions. | PMID:36099300 | Proceedings of the National Academy of Sciences of the United States of America |
| 2024 | High | Saturation genome editing (SGE) functionally assessed 9,188 unique RAD51C variants (>99.5% of all possible coding sequence SNVs). 3,094 variants were classified as disruptive based on cell fitness changes. Cell fitness was the primary readout. Specific missense variants showed distinct depletion kinetics suggesting hypomorphic alleles. Critical residues mapped onto the RAD51C structure; SGE-depleted variants associated with cancer diagnoses in UK Biobank. | PMID:39299233 | Cell |
| 2003 | Medium | XRCC3 residues Tyr139 and Phe249 are essential for RAD51C binding. The Rad51C-binding region of XRCC3 spans amino acids 63–346. The XRCC3(63-346)–RAD51C complex retains ssDNA and dsDNA binding activities comparable to the full-length complex. | PMID:12853621 | Nucleic acids research |
| 2004 | High | XRCC3 ATPase activity (Walker A box) is required for homologous recombination complementation and for normal XRCC3–RAD51C complex dynamics. Wild-type and K113A mutant XRCC3 form stable complexes with RAD51C; K113R mutant does not (predominantly insoluble). Addition of ATP (but not ADP) abolishes complex formation, suggesting ATP binding/hydrolysis by XRCC3 regulates CX3 complex assembly/disassembly. | PMID:15037616 | The Journal of biological chemistry |
| 2005 | Medium | The ATPase motif of RAD51D (Walker A K113) is required for resistance to DNA interstrand crosslinks; K113R and K113A mutations caused 96% and 83% reduction in repair capacity. Walker A mutations in RAD51D reduced interaction with RAD51C ~8-fold in yeast two-hybrid assays while XRCC2 interaction was retained, demonstrating the RAD51D ATPase is required for its interaction with RAD51C. | PMID:16236763 | Mutagenesis |
| 2010 | High | Biallelic RAD51C missense mutation in a consanguineous family caused loss of RAD51 focus formation in response to DNA damage and increased cellular sensitivity to MMC and camptothecin, establishing RAD51C as a Fanconi anemia–like disorder gene (FANCO). | PMID:20400963 | Nature genetics |
| 2017 | High | Secondary somatic mutations in RAD51C that restore the open reading frame confer resistance to PARP inhibitor rucaparib in ovarian carcinoma. In vitro complementation assays confirmed that secondary RAD51C mutations restore HR function and drive PARPi resistance. Molecular modeling predicted functional restoration of RAD51C protein by secondary mutations. | PMID:28588062 | Cancer discovery |
| 2021 | High | RAD51C promoter methylation (homozygous) silences RAD51C expression, causes homologous recombination deficiency, and confers PARP inhibitor sensitivity. Loss of a single unmethylated RAD51C gene copy is sufficient to drive PARPi resistance; loss of RAD51C promoter methylation under PARPi treatment pressure was confirmed as a resistance mechanism in PDX models. | PMID:34321239 | Cancer research |
| 2016 | Medium | Estrogen transcriptionally upregulates RAD51C expression in an ERα-dependent manner in ERα-positive breast cancer cells. Estrogen also induces RAD51C assembly into nuclear foci at DSBs, which precedes RAD51 complex recruitment. Anti-estrogens or ERα siRNA prevent estrogen-induced RAD51C upregulation. | PMID:27753535 | Cell cycle (Georgetown, Tex.) |
| 2014 | Medium | RAD51C-deficient cells treated with PARP inhibitor show enhanced non-homologous end joining (NHEJ) protein recruitment to chromatin, increased error-prone NHEJ activity, and synthetic lethality. Inhibition of DNA-PKcs or depletion of KU70 or Ligase IV rescues cell death, demonstrating that PARPi-induced synthetic lethality in RAD51C-deficient cells is mediated by hyperactivated NHEJ. | PMID:25292178 | Carcinogenesis |
| 2023 | High | Combining hypomorphic Brca2/Fancd1 and Rad51c/Fanco mutations in mice phenocopies human Fanconi anemia (bone marrow failure, rapid cancer death, drug hypersensitivity, severe replication instability), while single-gene mutations produce unremarkable phenotypes. This demonstrates unexpected synergism between FANC mutations (polygenic replication stress concept) and places RAD51C/FANCO in an epistatic relationship with BRCA2/FANCD1 in replication stress response. | PMID:36906610 | Nature communications |

## Citations

- PMID:11331762
- PMID:11459987
- PMID:11744692
- PMID:11751636
- PMID:11842112
- PMID:11842113
- PMID:11912211
- PMID:12000837
- PMID:12427746
- PMID:12853621
- PMID:12966089
- PMID:14504227
- PMID:14716019
- PMID:15037616
- PMID:15126333
- PMID:15141025
- PMID:15292210
- PMID:16215984
- PMID:16236763
- PMID:16954385
- PMID:17114795
- PMID:17268176
- PMID:17312021
- PMID:19155299
- PMID:19403737
- PMID:19451272
- PMID:19783859
- PMID:20400963
- PMID:22167183
- PMID:24141787
- PMID:25292178
- PMID:27753535
- PMID:28588062
- PMID:29158291
- PMID:31642493
- PMID:34321239
- PMID:36099300
- PMID:36906610
- PMID:37344587
- PMID:37488098
- PMID:39299233
- PMID:9469824
