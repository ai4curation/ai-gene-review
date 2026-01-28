---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T01:33:52.717362'
end_time: '2026-01-24T01:47:29.751214'
duration_seconds: 817.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: BCCIP
  gene_symbol: BCCIP
  uniprot_accession: Q9P287
  protein_description: 'RecName: Full=BRCA2 and CDKN1A-interacting protein; AltName:
    Full=P21- and CDK-associated protein 1; AltName: Full=Protein TOK-1;'
  gene_info: Name=BCCIP; Synonyms=TOK1;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the BCP1 family. .
  protein_domains: BCP1_family. (IPR025602); BCCIP (PF13862)
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
- **UniProt Accession:** Q9P287
- **Protein Description:** RecName: Full=BRCA2 and CDKN1A-interacting protein; AltName: Full=P21- and CDK-associated protein 1; AltName: Full=Protein TOK-1;
- **Gene Information:** Name=BCCIP; Synonyms=TOK1;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the BCP1 family. .
- **Key Domains:** BCP1_family. (IPR025602); BCCIP (PF13862)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "BCCIP" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'BCCIP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **BCCIP** (gene ID: BCCIP, UniProt: Q9P287) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# BCCIP: BRCA2 and CDKN1A-Interacting Protein - A Comprehensive Functional Review

## Introduction

BCCIP (BRCA2 and CDKN1A-interacting protein) is an evolutionarily conserved nuclear protein that plays essential roles in DNA damage repair via homologous recombination, cell cycle regulation, replication fork stability, and ribosome biogenesis. Originally identified in 2001 through a yeast two-hybrid screen for proteins interacting with the C-terminal conserved region of the tumor suppressor BRCA2 [liu-2001-bccip-discovery-abstract], BCCIP has since emerged as a multifunctional protein whose partial loss promotes tumorigenesis while complete loss is lethal. The human BCCIP gene is located at chromosome 10q25.3-26.2, a region frequently altered in brain and other cancers [liu-2001-bccip-discovery-abstract]. The protein belongs to the BCP1 family (InterPro: IPR025602) and contains the characteristic BCCIP/PF13862 domain. BCCIP is expressed in two major isoforms in humans—BCCIPα (322 amino acids) and BCCIPβ (314 amino acids)—which arise through alternative splicing of the 3'-terminal exons [meng-2003-bccip-genomic-structure-abstract]. Both isoforms share an N-terminal acidic domain and a central internal conserved domain (ICD) but differ in their C-terminal variable domains, conferring partially distinct functions.

## Protein Structure and Domain Organization

The BCCIP protein contains three functionally distinct domains: an N-terminus acidic domain (NAD) comprising approximately 30-60 amino acids, an internal conserved domain (ICD) of 180-220 amino acids, and a C-terminus variable domain (CVD) of 30-60 amino acids [liu-2001-bccip-discovery-abstract]. The ICD is the most highly conserved region and mediates interactions with both BRCA2 and p21/CDKN1A. Specifically, the BRCA2 interaction domain maps to amino acids 59-167, while the p21 interaction domain encompasses amino acids 168-258 [lu-2007-bccip-hr-domains-abstract]. The N-terminal half of the ICD shares moderate homology with regions of calmodulin and M-calpain, suggesting that BCCIP may possess calcium-binding properties, though this has not been experimentally confirmed [liu-2001-bccip-discovery-abstract].

A major advance in understanding BCCIP came with the determination of crystal structures of human BCCIPβ (residues 61-314) by Choi et al. [choi-2021-bccip-structure-abstract]. Remarkably, despite lacking sequence similarity to proteins of known structures, BCCIP adopts a fold structurally similar to GCN5-related acetyltransferases (GNATs). However, both the acetyl-CoA and substrate-binding grooves are altered compared to canonical GNATs. The structure reveals a 19-residue flap over the putative CoA binding site that can adopt either open or closed conformations. The substrate binding groove is significantly reduced in size and carries a positive charge despite BCCIP's overall acidic isoelectric point [choi-2021-bccip-structure-abstract]. These structural features suggest BCCIP may have potential binding sites for partner proteins and possibly enzymatic activity, though no acetyltransferase activity has been demonstrated.

## Role in Homologous Recombination Repair

The most extensively characterized function of BCCIP is its essential role in homologous recombination (HR) repair of DNA double-strand breaks (DSBs). BCCIP was initially noted to interact with a highly conserved C-terminal domain of BRCA2 that includes three RPA-like ssDNA binding domains [lu-2007-bccip-hr-domains-abstract]. This interaction positions BCCIP at the nexus of the HR machinery. Both BCCIPα and BCCIPβ isoforms interact with BRCA2 through their shared internal conserved domain [lu-2005-bccip-rad51-brca2-foci-abstract].

Functional studies have demonstrated that BCCIP is critical for BRCA2- and RAD51-dependent responses to DNA damage. Chromatin-bound BRCA2 colocalizes with BCCIP nuclear foci, and upon ionizing radiation, most radiation-induced RAD51 foci colocalize with BCCIP [lu-2005-bccip-rad51-brca2-foci-abstract]. RNA interference-mediated knockdown of BCCIPα by 90% or BCCIPβ by 50% markedly reduces RAD51 and BRCA2 focus formation and reduces HR repair of DSBs by 20- to 100-fold [lu-2005-bccip-rad51-brca2-foci-abstract]. This dramatic effect on HR is notably stronger than that observed with BRCA2 truncations that eliminate the BCCIP binding domain, which typically cause only 2- to 12-fold reductions in HR [lu-2007-bccip-hr-domains-abstract]. This disparity suggests that BCCIP regulates HR through mechanisms beyond its interaction with BRCA2 alone.

The biochemical mechanism by which BCCIP promotes HR was elucidated by Kelso et al., who demonstrated that BCCIPβ directly binds DNA and physically and functionally interacts with RAD51 to stimulate homologous DNA pairing activity [kelso-2017-bccipbeta-rad51-abstract]. Importantly, this stimulation is not achieved through RAD51 nucleoprotein filament stabilization. Rather, BCCIPβ induces a conformational change within the RAD51 filament that promotes the release of ADP, thereby helping to maintain an active presynaptic filament [kelso-2017-bccipbeta-rad51-abstract]. This finding establishes BCCIPβ as a RAD51 accessory factor that promotes the ATP-bound active state of the recombinase.

Notably, BCCIP appears to function specifically in HR and not in non-homologous end joining (NHEJ). Transient BCCIP down-regulation significantly inhibits homology-directed gene targeting but does not affect random (non-homologous) integration of transfected DNA [lu-2007-bccip-hr-domains-abstract]. Both the BRCA2-interacting domain (aa 59-167) and the p21-interacting domain (aa 168-258) exert dominant negative effects on HR when expressed as fragments, indicating that BCCIP regulates HR through at least two distinct mechanisms [lu-2007-bccip-hr-domains-abstract].

## Role in Replication Fork Stability and Stress Response

Beyond its role in DSB repair, BCCIP plays a critical function in protecting stalled replication forks and maintaining genome stability during DNA replication. Cells with constitutive BCCIP knockdown display increased levels of spontaneous single-stranded DNA (ssDNA) and DSBs, even in the absence of exogenous DNA damage [lu-2007-bccip-hr-domains-abstract]. This accumulation of spontaneous DNA damage likely reflects defective restart of stalled replication forks and/or failure to properly resolve replication intermediates.

Singh et al. demonstrated that BCCIP is recruited to stalled replication forks and prevents MRE11 nuclease-mediated degradation of nascent DNA strands [singh-2022-bccip-replication-stress-abstract]. In the presence of replication stress, BCCIP deficiency increases replication fork stalling and results in DNA double-strand break formation [singh-2022-bccip-replication-stress-abstract]. This fork protection function parallels the repair-independent functions of BRCA2 and RAD51, which are crucial for protecting nascent DNA from nucleolytic degradation. Thus, BCCIP functions alongside BRCA2 and RAD51 not only in HR repair but also in the preservation of stalled replication fork integrity.

Studies in mouse embryonic fibroblasts (MEFs) deficient for BCCIP revealed significant spontaneous chromosome structural alterations associated with replication stress, including a 3.5-fold induction of chromatid breaks [lu-2011-bccip-embryonic-development-abstract]. A particularly striking finding was a ~20-fold increase in sister chromatid union (SCU), a unique type of chromatid aberration that may give rise to chromatin bridges between daughter nuclei during anaphase [lu-2011-bccip-embryonic-development-abstract]. The modest 1.5-fold increase in sister chromatid exchanges (SCE) contrasts with the dramatic SCU phenotype, suggesting a specific defect in resolving replication-associated DNA structures rather than a general increase in recombination.

## Cell Cycle Regulation via p21/CDKN1A

BCCIP was originally identified not only as a BRCA2-interacting protein but also as a p21/CDKN1A-interacting protein [liu-2001-bccip-discovery-abstract]. The interaction with p21 provides BCCIP with a direct role in cell cycle regulation, particularly at the G1/S transition. Overexpression of BCCIPβ delays G1 to S progression and results in elevated p21 expression [meng-2004-bccip-g1s-cell-cycle-abstract]. The growth inhibition mediated by BCCIPβ can be partially abrogated in p21-deficient cells, confirming the functional importance of the BCCIP-p21 interaction [meng-2004-bccip-g1s-cell-cycle-abstract].

BCCIP regulates p21 through multiple mechanisms. First, BCCIP enhances p21's inhibitory activity toward CDK2 [meng-2004-bccip-g1s-cell-cycle-abstract]. Second, BCCIP knockdown reduces p21 levels by abrogating p53 transcriptional activity, demonstrating that BCCIP functions upstream of p53 to regulate p21 expression [meng-2004-bccip-p53-p21-abstract]. Third, BCCIP is required for the nuclear localization of p21, which is essential for p21's CDK-inhibitory function [fan-2009-bccip-p21-localization-abstract]. Downregulation of BCCIP reduces nuclear p21 and increases cytoplasmic p21, and this redistribution is independent of Thr-145 phosphorylation status [fan-2009-bccip-p21-localization-abstract]. The BCCIP-p21 interaction is enhanced in response to DNA damage, as demonstrated by Fluorescence Resonance Energy Transfer (FRET) experiments [fan-2009-bccip-p21-localization-abstract].

Consistent with these cell cycle regulatory functions, partial BCCIP knockdown impairs G1/S checkpoint activation in response to ionizing radiation [meng-2004-bccip-p53-p21-abstract]. This checkpoint defect, combined with defective HR repair, likely contributes to the genomic instability and tumor susceptibility observed with BCCIP deficiency.

## Subcellular Localization

BCCIP is predominantly a nuclear protein, consistent with its functions in DNA repair and cell cycle regulation [liu-2001-bccip-discovery-abstract]. Immunofluorescence studies show that the majority of total BCCIP protein is distributed throughout the nucleus, while Triton X-100-resistant BCCIP mainly resides in the nucleolus [ye-2020-bccip-ribosome-biogenesis-abstract]. Notably, only the BCCIPβ isoform, and not BCCIPα, is detectable in the nucleolus after detergent extraction [ye-2020-bccip-ribosome-biogenesis-abstract]. Within the nucleolus, BCCIP colocalizes completely with nucleolin and partially with RPA194 (a fibrillar center marker), fibrillarin (a dense fibrillar component marker), and B23 (a granular component marker), suggesting BCCIP associates with the fibrillar center and dense fibrillar component where rRNA transcription, processing, and early pre-ribosome assembly occur [ye-2020-bccip-ribosome-biogenesis-abstract].

The nucleolar retention of BCCIP is dependent on both RNA and DNA, as treatment with RNase A completely abolishes BCCIP signals in the nucleolus, and DNase I treatment also dramatically alters the nuclear BCCIP staining pattern [ye-2020-bccip-ribosome-biogenesis-abstract].

## Role in Ribosome Biogenesis

A novel and important function of BCCIP in ribosome biogenesis has been established. The yeast homologue of mammalian BCCIP, Bcp1, was computationally predicted to be required for ribosomal biogenesis, and temperature-sensitive Bcp1 mutants exhibit deficits in 60S biogenesis [ye-2020-bccip-ribosome-biogenesis-abstract]. In mammalian cells, BCCIP is required for the nucleolar recruitment of eIF6 (eukaryotic translation initiation factor 6) and for the production of 12S pre-rRNA, a precursor to the 5.8S rRNA component of 60S ribosomal subunits [ye-2020-bccip-ribosome-biogenesis-abstract].

The mechanistic basis of BCCIP's role in ribosome biogenesis involves its interaction with ribosomal protein RPL23/uL14 and the pre-60S trans-acting factor eIF6. Wyler et al. demonstrated that BCCIPβ, but not BCCIPα, forms a ternary complex with RPL23 and eIF6, and this complex formation depends on the intact C-terminal domain of BCCIPβ [wyler-2014-bccipbeta-rpl23-abstract]. Depletion of BCCIPβ reduces the pool of free RPL23 and decreases eIF6 levels in nucleoli [wyler-2014-bccipbeta-rpl23-abstract]. Overexpression of BCCIPβ leads to nucleoplasmic accumulation of extra-ribosomal RPL23 and stabilizes overexpressed RPL23, suggesting that BCCIPβ functions as a nuclear chaperone for RPL23 [wyler-2014-bccipbeta-rpl23-abstract].

Both abrogation of BCCIP nucleolar localization and impaired BCCIP-eIF6 interaction compromise eIF6 recruitment to the nucleolus and 60S ribosome biogenesis [ye-2020-bccip-ribosome-biogenesis-abstract]. However, heterozygous Bccip loss is insufficient to impair 60S biogenesis in mouse embryo fibroblasts; a profound reduction of BCCIP is required to abrogate its function in 60S biogenesis [ye-2020-bccip-ribosome-biogenesis-abstract]. This dosage sensitivity may explain the different phenotypic consequences of partial versus complete BCCIP loss.

## Role in Mitotic Spindle Integrity and Cytokinesis

Beyond its functions in DNA repair and ribosome biogenesis, BCCIP plays an essential role in the maintenance of mitotic spindle integrity and successful cytokinesis. Meng et al. demonstrated that downregulation of BCCIP in HT1080 cells leads to chromosomal polyploidization, centrosome amplification, and abnormal mitotic spindle formation [meng-2007-bccip-cytokinesis-abstract]. BCCIP-knockdown cells can enter mitosis and retain the spindle checkpoint, but fail to complete cytokinesis, resulting in cells with multiple nuclei and abnormal chromosome content. These findings established that BCCIP is essential for the maintenance of genomic integrity through proper cell division.

The mechanistic basis for BCCIP's role in mitosis was further elucidated by Huhn et al., who identified BCCIP, particularly the BCCIPα isoform, as a previously unrecognized component of the mitotic spindle pole and the centrosome [huhn-2017-bccip-spindle-mitosis-abstract]. BCCIP localizes proximal to the mother centriole where it participates in microtubule organization, and subsequently redistributes to the spindle pole to ensure faithful spindle architecture during cell division. Depletion of BCCIP leads to morphological defects, disoriented mitotic spindles, chromosome congression defects, and delayed mitotic progression [huhn-2017-bccip-spindle-mitosis-abstract]. The spindle orientation function of BCCIP is particularly significant because spindle orientation is a major determinant of cell fate during tissue regeneration, linking BCCIP function to both tumor suppression and developmental processes.

This mitotic function of BCCIP provides an additional mechanism for its tumor suppressor activity: defective spindle integrity leads not only to chromosome instability but also to defective asymmetric cell division, which can disrupt tissue architecture and stem cell homeostasis.

## Essential Role in Development and Tumorigenesis

BCCIP exhibits a remarkable dose-dependent effect on cell viability and tumorigenesis. Partial BCCIP deficiency is sufficient to trigger genomic instability and tumorigenesis, while complete loss of BCCIP is lethal. Conditional BCCIP knockdown transgenic mice generated using Cre-LoxP mediated RNA interference demonstrate that BCCIP knockdown embryos display impaired cellular proliferation and apoptosis as early as embryonic day E7.5, with lethality occurring before E11.5 [lu-2011-bccip-embryonic-development-abstract]. The developmental defects are associated with spontaneous DNA damage and subsequent cell death in proliferative cell populations during embryogenesis. Deletion of the p53 gene cannot rescue the embryonic lethality due to BCCIP deficiency, though it partially rescues the growth delay of mouse embryonic fibroblasts in vitro [lu-2011-bccip-embryonic-development-abstract].

BCCIP is particularly critical for neural development. Using a conditional BCCIP knockdown mouse model, Huang et al. showed that BCCIP deficiency impairs both embryonic and postnatal neural development, causing severe ataxia, cerebral and cerebellar defects, and microcephaly [huang-2012-bccip-neural-development-abstract]. These developmental defects are associated with spontaneous DNA damage and subsequent cell death in the proliferative cell populations of the neural system during embryogenesis. In vitro neural spheroid cultures revealed that BCCIP deficiency impairs neural progenitor self-renewal capability and spontaneously activates p53 [huang-2012-bccip-neural-development-abstract]. The particular sensitivity of neural progenitors to BCCIP loss reflects the high proliferative demand and the critical importance of homologous recombination in resolving stalled replication forks during neural development.

The relationship between BCCIP and cancer is unexpectedly complex. Huang et al. described BCCIP as a "suppressor for initiation but requisite for progression" (SIRP) tumor suppressor, representing a distinct class from classical tumor suppressors that are permanently inactivated during tumorigenesis [huang-2013-bccip-sirp-abstract]. In a p53-null background, conditional BCCIP knockdown caused rapid development of medulloblastomas bearing alterations in the Sonic Hedgehog (Shh) pathway. Surprisingly, the progressed tumors spontaneously lost the transgenic BCCIP knockdown cassette and restored BCCIP expression [huang-2013-bccip-sirp-abstract]. This indicates that transient BCCIP downregulation, rather than permanent mutation, is sufficient to initiate tumorigenesis; however, once malignant transformation is established, BCCIP expression becomes necessary for tumor progression. This "hit-and-run" mechanism has major implications for understanding how transient or non-mutagenic regulation of essential caretaker genes contributes to cancer development.

BCCIP expression is downregulated in multiple human cancer types, including ovarian cancer (74% of cases), renal cell carcinoma (89%), and colorectal cancer (75%) [liu-2013-bccip-cancer-expression, cited in search results]. Reduced BCCIP expression in breast cancer is associated with 53BP1 loss, particularly in triple-negative breast cancer. In mouse models, partial BCCIP deficiency causes benign mammary nodules resembling epidermal inclusion cysts, but only ~10% evolve into malignant tumors after long latency, with progression associated with loss of 53BP1 and p16 expression [droz-rosario-2017-bccip-mammary, cited in search results].

The essential functions of BCCIP in ribosome biogenesis, DNA repair, and cell division together explain why complete BCCIP depletion is lethal: without adequate ribosome production, replication fork protection, and successful cytokinesis, cells cannot sustain the proliferation required for viability [ye-2020-bccip-ribosome-biogenesis-abstract].

## Summary of Molecular Functions

BCCIP serves as a multifunctional adaptor protein with the following primary functions:

1. **Homologous recombination repair**: BCCIP promotes HR by facilitating BRCA2 and RAD51 focus formation and by directly stimulating RAD51 activity through promoting ADP release from the presynaptic filament.

2. **Replication fork protection**: BCCIP is recruited to stalled replication forks and prevents MRE11-mediated degradation of nascent DNA, functioning alongside BRCA2 and RAD51 in fork protection.

3. **Cell cycle regulation**: BCCIP regulates the G1/S transition by enhancing p21 inhibitory activity toward CDK2, regulating p21 expression via p53, and controlling p21 nuclear localization.

4. **60S ribosome biogenesis**: BCCIPβ functions as a chaperone for RPL23 and is required for nucleolar recruitment of eIF6 and production of 12S pre-rRNA.

5. **Mitotic spindle integrity and cytokinesis**: BCCIPα localizes to the centrosome and spindle pole where it participates in microtubule organization, ensuring proper spindle architecture and successful completion of cytokinesis.

## Open Questions

Several important questions remain regarding BCCIP function:

1. **Enzymatic activity**: The structural similarity of BCCIP to GCN5-related acetyltransferases raises the question of whether BCCIP possesses any acetyltransferase or other enzymatic activity. The altered substrate-binding groove suggests any such activity would differ from canonical GNATs.

2. **Isoform-specific functions**: While BCCIPβ has been specifically implicated in ribosome biogenesis and RAD51 stimulation, the specific functions of BCCIPα beyond its shared roles with BCCIPβ in HR and cell cycle regulation remain unclear.

3. **Calcium binding**: The homology of the BCCIP ICD with calmodulin and M-calpain calcium-binding regions has not been experimentally validated. Whether BCCIP binds calcium and whether this affects its function warrants investigation.

4. **Coordination of functions**: How BCCIP coordinates its multiple functions in DNA repair, replication fork protection, cell cycle regulation, and ribosome biogenesis is not well understood. Are these functions independent, or do they intersect in specific cellular contexts?

5. **Therapeutic implications**: Given that BCCIP deficiency sensitizes cells to DNA damaging agents and that BCCIP is downregulated in many cancers, whether BCCIP status could serve as a biomarker for therapy response or as a therapeutic target remains to be explored.

6. **Regulation of BCCIP**: The mechanisms regulating BCCIP expression, stability, and activity are incompletely understood. Post-translational modifications and interactions beyond BRCA2, p21, RAD51, RPL23, and eIF6 likely exist.

## References

- **[liu-2001-bccip-discovery-abstract]** Liu J, Yuan Y, Huan J, Shen Z. Inhibition of breast and brain cancer cell growth by BCCIPalpha, an evolutionarily conserved nuclear protein that interacts with BRCA2. Oncogene. 2001;20(3):336-45. DOI: [10.1038/sj.onc.1204098](https://doi.org/10.1038/sj.onc.1204098). PMID: 11313963.

- **[meng-2003-bccip-genomic-structure-abstract]** Meng X, Liu J, Shen Z. Genomic structure of the human BCCIP gene and its expression in cancer. Gene. 2003;302(1-2):139-46. DOI: [10.1016/s0378-1119(02)01098-3](https://doi.org/10.1016/s0378-1119(02)01098-3). PMID: 12527204.

- **[lu-2005-bccip-rad51-brca2-foci-abstract]** Lu H, Guo X, Meng X, Liu J, Allen C, Wray J, Nickoloff JA, Shen Z. The BRCA2-interacting protein BCCIP functions in RAD51 and BRCA2 focus formation and homologous recombinational repair. Mol Cell Biol. 2005;25(5):1949-57. DOI: [10.1128/MCB.25.5.1949-1957.2005](https://doi.org/10.1128/MCB.25.5.1949-1957.2005). PMID: 15713648. PMCID: PMC549367.

- **[lu-2007-bccip-hr-domains-abstract]** Lu H, Yue J, Meng X, Nickoloff JA, Shen Z. BCCIP regulates homologous recombination by distinct domains and suppresses spontaneous DNA damage. Nucleic Acids Res. 2007;35(21):7160-70. DOI: [10.1093/nar/gkm732](https://doi.org/10.1093/nar/gkm732). PMID: 17947333. PMCID: PMC2175368.

- **[meng-2004-bccip-g1s-cell-cycle-abstract]** Meng X, Liu J, Shen Z. Inhibition of G1 to S cell cycle progression by BCCIP beta. Cell Cycle. 2004;3(3):343-8. PMID: 14726710.

- **[meng-2004-bccip-p53-p21-abstract]** Meng X, Lu H, Shen Z. BCCIP functions through p53 to regulate the expression of p21Waf1/Cip1. Cell Cycle. 2004;3(11):1457-62. DOI: [10.4161/cc.3.11.1213](https://doi.org/10.4161/cc.3.11.1213). PMID: 15539944.

- **[fan-2009-bccip-p21-localization-abstract]** Fan J, Wray J, Meng X, Shen Z. BCCIP is required for the nuclear localization of the p21 protein. Cell Cycle. 2009;8(18):3019-24. PMID: 19713748. PMCID: PMC3862257.

- **[lu-2011-bccip-embryonic-development-abstract]** Lu H, Huang YY, Mehrotra S, Droz-Rosario R, Liu J, Bhaumik M, White E, Shen Z. Essential roles of BCCIP in mouse embryonic development and structural stability of chromosomes. PLoS Genet. 2011;7(9):e1002291. DOI: [10.1371/journal.pgen.1002291](https://doi.org/10.1371/journal.pgen.1002291). PMID: 21966279. PMCID: PMC3178617.

- **[wyler-2014-bccipbeta-rpl23-abstract]** Wyler E, Wandrey F, Badertscher L, Montellese C, Alper D, Kutay U. The beta-isoform of the BRCA2 and CDKN1A(p21)-interacting protein (BCCIP) stabilizes nuclear RPL23/uL14. FEBS Lett. 2014;588(20):3685-91. DOI: [10.1016/j.febslet.2014.08.013](https://doi.org/10.1016/j.febslet.2014.08.013). PMID: 25150171.

- **[kelso-2017-bccipbeta-rad51-abstract]** Kelso AA, Goodson SD, Watts LE, Ledford LL, Waldvogel SM, Diehl JN, Shah SB, Say AF, White JD, Sehorn MG. The β-isoform of BCCIP promotes ADP release from the RAD51 presynaptic filament and enhances homologous DNA pairing. Nucleic Acids Res. 2017;45(2):711-725. DOI: [10.1093/nar/gkw877](https://doi.org/10.1093/nar/gkw877). PMID: 27694622. PMCID: PMC5314795.

- **[ye-2020-bccip-ribosome-biogenesis-abstract]** Ye C, Liu B, Lu H, Liu J, Rabson AB, Jacinto E, Pestov DG, Shen Z. BCCIP is required for nucleolar recruitment of eIF6 and 12S pre-rRNA production during 60S ribosome biogenesis. Nucleic Acids Res. 2020;48(22):12817-12832. DOI: [10.1093/nar/gkaa1114](https://doi.org/10.1093/nar/gkaa1114). PMID: 33245766. PMCID: PMC7736804.

- **[choi-2021-bccip-structure-abstract]** Choi WS, Liu B, Shen Z, Yang W. Structure of human BCCIP and implications for binding and modification of partner proteins. Protein Sci. 2021;30(3):693-699. DOI: [10.1002/pro.4026](https://doi.org/10.1002/pro.4026). PMID: 33452718.

- **[singh-2022-bccip-replication-stress-abstract]** Singh B, Roy Chowdhury S, Mansuri MS, Pillai SJ, Mehrotra S. The BRCA2 and CDKN1A-interacting protein (BCCIP) stabilizes stalled replication forks and prevents degradation of nascent DNA. FEBS Lett. 2022;596(16):2041-2055. DOI: [10.1002/1873-3468.14406](https://doi.org/10.1002/1873-3468.14406). PMID: 35592921.

- **[meng-2007-bccip-cytokinesis-abstract]** Meng X, Fan J, Shen Z. Roles of BCCIP in chromosome stability and cytokinesis. Oncogene. 2007;26(43):6253-60. DOI: [10.1038/sj.onc.1210460](https://doi.org/10.1038/sj.onc.1210460). PMID: 17452982. PMCID: PMC2667889.

- **[huhn-2017-bccip-spindle-mitosis-abstract]** Huhn SC, Liu J, Ye C, Lu H, Jiang X, Feng X, Ganesan S, White E, Shen Z. Regulation of spindle integrity and mitotic fidelity by BCCIP. Oncogene. 2017;36(33):4750-4766. DOI: [10.1038/onc.2017.92](https://doi.org/10.1038/onc.2017.92). PMID: 28394342. PMCID: PMC5561484.

- **[huang-2012-bccip-neural-development-abstract]** Huang YY, Lu H, Liu S, Droz-Rosario R, Shen Z. Requirement of mouse BCCIP for neural development and progenitor proliferation. PLoS One. 2012;7(1):e30638. DOI: [10.1371/journal.pone.0030638](https://doi.org/10.1371/journal.pone.0030638). PMID: 22292003. PMCID: PMC3265516.

- **[huang-2013-bccip-sirp-abstract]** Huang YY, Dai L, Gaines D, Droz-Rosario R, Lu H, Liu J, Shen Z. BCCIP suppresses tumor initiation but is required for tumor progression. Cancer Res. 2013;73(23):7122-33. DOI: [10.1158/0008-5472.CAN-13-1766](https://doi.org/10.1158/0008-5472.CAN-13-1766). PMID: 24145349. PMCID: PMC3918420.


## Citations

1. choi-2021-bccip-structure-abstract.md
2. fan-2009-bccip-p21-localization-abstract.md
3. huang-2012-bccip-neural-development-abstract.md
4. huang-2013-bccip-sirp-abstract.md
5. huhn-2017-bccip-spindle-mitosis-abstract.md
6. kelso-2017-bccipbeta-rad51-abstract.md
7. liu-2001-bccip-discovery-abstract.md
8. lu-2005-bccip-rad51-brca2-foci-abstract.md
9. lu-2007-bccip-hr-domains-abstract.md
10. lu-2011-bccip-embryonic-development-abstract.md
11. meng-2003-bccip-genomic-structure-abstract.md
12. meng-2004-bccip-g1s-cell-cycle-abstract.md
13. meng-2004-bccip-p53-p21-abstract.md
14. meng-2007-bccip-cytokinesis-abstract.md
15. singh-2022-bccip-replication-stress-abstract.md
16. wyler-2014-bccipbeta-rpl23-abstract.md
17. ye-2020-bccip-ribosome-biogenesis-abstract.md