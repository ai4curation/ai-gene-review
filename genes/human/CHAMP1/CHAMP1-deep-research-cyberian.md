---
provider: cyberian
model: deep-research
cached: false
start_time: '2025-12-03T19:40:05.627565'
end_time: '2025-12-03T19:56:40.583489'
duration_seconds: 994.96
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CHAMP1
  gene_symbol: CHAMP1
  uniprot_accession: Q96JM3
  protein_description: 'RecName: Full=Chromosome alignment-maintaining phosphoprotein
    1; AltName: Full=Zinc finger protein 828;'
  gene_info: Name=CHAMP1; Synonyms=C13orf8, CAMP, CHAMP, KIAA1802, ZNF828;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: CAMP. (IPR039330); Znf_C2H2_sf. (IPR036236); Znf_C2H2_type. (IPR013087)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q96JM3
- **Protein Description:** RecName: Full=Chromosome alignment-maintaining phosphoprotein 1; AltName: Full=Zinc finger protein 828;
- **Gene Information:** Name=CHAMP1; Synonyms=C13orf8, CAMP, CHAMP, KIAA1802, ZNF828;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CAMP. (IPR039330); Znf_C2H2_sf. (IPR036236); Znf_C2H2_type. (IPR013087)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CHAMP1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CHAMP1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CHAMP1** (gene ID: CHAMP1, UniProt: Q96JM3) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CHAMP1 (Chromosome Alignment-Maintaining Phosphoprotein 1): A Comprehensive Functional Review

## 1. Introduction and Summary

CHAMP1 (Chromosome Alignment-Maintaining Phosphoprotein 1), also known as C13orf8, CAMP, or ZNF828, is a vertebrate-specific zinc finger protein that plays essential roles in mitotic chromosome segregation, DNA repair, and neuronal development. The gene is located on chromosome 13q34 and encodes an 812 amino acid protein containing multiple functional domains including five C2H2-type zinc finger motifs and characteristic WK, SPE, and FPE repeat sequences [itoh-2011-kinetochore-abstract].

The protein was first characterized in 2010-2011 by Itoh and colleagues at Tohoku University, who identified it as a novel regulator of kinetochore-microtubule attachment essential for proper chromosome alignment during mitosis [itoh-2011-kinetochore-abstract]. Subsequent research has revealed that CHAMP1 possesses at least three core functions: (1) regulation of kinetochore-microtubule attachment during cell division; (2) promotion of homologous recombination repair of DNA double-strand breaks; and (3) participation in heterochromatin assembly and neuronal development. The clinical importance of CHAMP1 was established in 2015 when de novo mutations were shown to cause an intellectual disability syndrome with severe speech impairment [hempel-2015-intellectual-disability-abstract].

## 2. Protein Structure and Domain Architecture

CHAMP1 is an 812 amino acid zinc finger protein that exhibits a modular domain architecture critical for its multiple functions. The protein contains five C2H2-type zinc finger domains, with some located at the N-terminus and others at the C-terminus [itoh-2011-kinetochore-abstract]. These zinc finger motifs are characteristic of DNA-binding proteins, though in CHAMP1 they also mediate protein-protein interactions and provide regulatory functions.

Three characteristic repeat motifs define the central region of CHAMP1 and are essential for its mitotic functions. The SPE motif (consensus sequence PxxSPExxK) contains multiple serine residues that undergo CDK1-dependent phosphorylation during mitosis [itoh-2011-kinetochore-abstract]. The WK motif (consensus SPxxWKxxP) mediates the critical interaction with MAD2L2/REV7, enabling both mitotic checkpoint signaling and DNA repair pathway regulation [itoh-2011-kinetochore-abstract][li-2022-rev7-abstract]. The FPE motif (consensus FPExxK) is responsible for spindle and kinetochore localization and is essential for CHAMP1's function in chromosome alignment [itoh-2011-kinetochore-abstract].

The protein also contains intrinsically disordered regions that may facilitate its multiple protein-protein interactions. Importantly, the C-terminal zinc finger domains exert a negative regulatory effect on the FPE region's function, an inhibition that is relieved by mitotic phosphorylation [itoh-2011-kinetochore-abstract]. This phosphorylation-dependent regulation ensures that CHAMP1's chromosome alignment function is properly restricted to the mitotic phase of the cell cycle.

CHAMP1 is evolutionarily conserved exclusively among vertebrates, with no identifiable homologs in yeast, worms, or flies, suggesting a role in fine-tuning mitotic regulation that arose specifically in the vertebrate lineage [itoh-2011-kinetochore-abstract]. According to the Human Protein Atlas, CHAMP1 exhibits low tissue specificity (tau score 0.23), with expression detected across all human tissues examined. The highest RNA expression levels are observed in lymphoid tissues (tonsil, thymus, lymph node) and metabolic organs (pancreas, liver). At the protein level, CHAMP1 shows general nuclear expression with enhanced localization to the nucleoplasm and nuclear bodies. During brain development, single-cell transcriptomic analyses have revealed that CHAMP1 is highly enriched in apical radial glia (aRG) and other early proliferative cell types, consistent with its role in cell division and its association with neurodevelopmental disorders when mutated [vancaugherty-2024-thesis].

## 3. Role in Kinetochore-Microtubule Attachment and Chromosome Segregation

The primary cellular function of CHAMP1 is the regulation of kinetochore-microtubule attachment during mitosis, ensuring proper chromosome alignment on the metaphase plate. This function was elucidated through comprehensive studies using siRNA depletion, live-cell imaging, and biochemical analyses [itoh-2011-kinetochore-abstract].

During interphase, CHAMP1 localizes to the nucleus. Upon entry into mitosis, the protein associates with chromosomes throughout their length and subsequently concentrates at spindle fibers and kinetochores from prometaphase through anaphase [itoh-2011-kinetochore-abstract]. This dynamic localization pattern is controlled by the FPE region, which independently localizes to spindle and kinetochore structures, while the C-terminal region contributes to chromosome association.

Depletion of CHAMP1 results in severe chromosome misalignment in approximately 50% of cells [itoh-2011-kinetochore-abstract]. Time-lapse microscopy revealed that CHAMP1-depleted cells experience delayed chromosome congression and an unstable metaphase plate, with chromosomes frequently failing to maintain alignment. These cells typically remain arrested in mitosis with an active spindle assembly checkpoint, indicating that the chromosome segregation defects are sufficient to trigger checkpoint-mediated cell cycle arrest.

The mechanistic basis for CHAMP1's function involves the stabilization of kinetochore fibers (K-fibers), the specialized bundles of microtubules that connect kinetochores to spindle poles. In CHAMP1-depleted cells, K-fibers cannot maintain bi-orientation, meaning sister kinetochores fail to achieve stable attachments to microtubules from opposite spindle poles [itoh-2011-kinetochore-abstract]. This manifests as reduced inter-kinetochore distances, indicating insufficient tension across sister kinetochore pairs. Cold-stability assays, which assess the resistance of K-fibers to depolymerization, demonstrated that microtubule attachments at kinetochores are dramatically reduced following CHAMP1 depletion.

CHAMP1 regulates the kinetochore localization of two downstream effectors: CENP-E and CENP-F. These large coiled-coil proteins are components of the fibrous corona at the outer kinetochore and are essential for stable kinetochore-microtubule attachments. CHAMP1 depletion reduces the kinetochore levels of both proteins, and importantly, depletion of CENP-E or CENP-F produces phenotypes similar to CHAMP1 depletion without additive effects, indicating that CENP-E and CENP-F function downstream of CHAMP1 in the same pathway [itoh-2011-kinetochore-abstract]. The regulation appears to be indirect, as no direct physical interaction between CHAMP1 and CENP-E or CENP-F has been detected.

## 4. Function in DNA Repair: Promotion of Homologous Recombination

Beyond its role in mitosis, CHAMP1 has emerged as a critical regulator of DNA double-strand break (DSB) repair through the homologous recombination (HR) pathway. This function was discovered through studies of the HORMA domain protein REV7 (also known as MAD2L2 or FANCV) at the Dana-Farber Cancer Institute [li-2022-rev7-abstract].

REV7 is a versatile adaptor protein that binds different partners through its C-terminal "seatbelt" domain to direct distinct cellular outcomes. When REV7 binds to REV3, it activates translesion DNA synthesis. When bound to SHLD3, a component of the Shieldin complex, REV7 promotes non-homologous end joining (NHEJ). The Li et al. study demonstrated that CHAMP1 is a third REV7 seatbelt-binding partner, and that CHAMP1 binding activates HR repair [li-2022-rev7-abstract].

The interaction between CHAMP1 and REV7 is mediated by the WKPAKPAPS motif in CHAMP1, which corresponds to the consensus REV7 seatbelt-binding sequence. Site-directed mutagenesis creating a CHAMP1-W334A/K335A double mutant (designated CHAMP1-2A) abolished REV7 binding [li-2022-rev7-abstract]. Importantly, this mutant failed to rescue the PARP inhibitor sensitivity of CHAMP1 knockout cells, demonstrating that REV7 binding is essential for CHAMP1's DNA repair function.

DNA damage with ionizing radiation activates the CHAMP1-REV7 interaction, stimulating the colocalization of both proteins in nuclear foci that peak within one hour post-irradiation [li-2022-rev7-abstract]. Mechanistically, CHAMP1 binding to REV7 promotes HR through two related effects: reducing the level of the Shieldin complex (thereby decreasing NHEJ activity) and enhancing DSB end resection. End resection is a critical early step in HR that generates single-stranded DNA substrates for RAD51 loading. CHAMP1 knockout cells exhibited reduced DSB end resection as measured by SMART assays and reduced RAD51 foci assembly following DNA damage [li-2022-rev7-abstract].

Using DR-GFP reporter assays, which directly measure HR efficiency, CHAMP1 knockout reduced HR activity by approximately 60% [li-2022-rev7-abstract]. This functional defect renders cells sensitive to PARP inhibitors, which are synthetic lethal with HR deficiency. Importantly, CHAMP1 operates together with POGZ in a heterochromatin complex that also includes HP1alpha, LEDGF, and HDGFRP2. Genetic epistasis experiments demonstrated that POGZ and CHAMP1 function in the same HR pathway [li-2022-rev7-abstract].

The 2024 study by Yoshizaki et al. extended these findings to patient-derived cells, demonstrating that premature termination codon (PTC) mutations found in individuals with CHAMP1-related intellectual disability cause HR defects through haploinsufficiency [yoshizaki-2024-haploinsufficiency-abstract]. Truncated CHAMP1 proteins of expected sizes were detected in Epstein-Barr virus-transformed lymphoblastoid cells and fibroblasts from affected individuals. When DSBs were induced, these patient fibroblasts showed defective HR. Heterozygous CHAMP1 depletion in DLD-1 cells similarly resulted in HR defects, confirming haploinsufficiency as the mechanism [yoshizaki-2024-haploinsufficiency-abstract]. Interestingly, CHAMP1 missense mutations did not affect HR function, suggesting that the DNA repair defects may not contribute to disease in all CHAMP1 mutation types.

## 5. The CHAMP1 Complex: Heterochromatin Assembly and Function

CHAMP1 functions as part of a larger protein complex that promotes heterochromatin assembly and maintenance. This complex, sometimes referred to as the CHAMP1 complex, includes POGZ (Pogo transposable element with ZNF domain) and HP1alpha (Heterochromatin Protein 1), both of which are implicated in chromatin organization and, notably, are also associated with neurodevelopmental disorders when mutated [li-2025-heterochromatin-abstract]. De novo heterozygous mutations in POGZ cause White-Sutton syndrome, a rare neurodevelopmental disorder with significant clinical overlap with CHAMP1 syndrome.

The architecture of the CHAMP1 complex has been recently elucidated: the N-terminal region of CHAMP1 binds to the C-terminus of POGZ, while both proteins independently interact with HP1alpha and the H3K9me3 histone mark [li-2025-heterochromatin-abstract]. The zinc finger domain of CHAMP1 mediates binding to both HP1 and POGZ. Additionally, the POGZ subunit binds and recruits the methyltransferase SETDB1 to heterochromatin regions, establishing a positive feedback mechanism that reinforces heterochromatin formation [li-2025-heterochromatin-abstract].

The hierarchical recruitment of CHAMP1 to pericentromeric heterochromatin has been further clarified through studies of CDYL2 (Chromodomain on Y-like 2). Siouda et al. (2023) demonstrated that CDYL2 functions as an adaptor protein that reads pericentromeric H3K9me3 via its chromodomain and recruits CHAMP1 and POGZ through its non-conserved central linker region [siouda-2023-cdyl2-abstract]. This hierarchical organization ensures that CHAMP1 is properly positioned at heterochromatin during cell division. CDYL2 depletion causes loss of CHAMP1 localization at pericentromeres, leading to nuclear abnormalities, mitotic defects, and genome instability [siouda-2023-cdyl2-abstract].

The CHAMP1 complex promotes heterochromatin assembly at multiple chromosomal sites, including centromeres and telomeres. CRISPR knockout of either CHAMP1 or POGZ in U2OS cells resulted in significant reduction of H3K9me3 and HP1alpha foci at both centromeres and telomeres [li-2025-heterochromatin-abstract]. The complex is also essential for heterochromatin maintenance in specialized contexts, particularly in ALT (Alternative Lengthening of Telomeres) positive tumor cells, where it is required for both heterochromatin structure and DNA repair at telomeres. This heterochromatin function is intimately linked to the HR repair activity, as heterochromatin regions require specialized repair mechanisms, and the CHAMP1 complex promotes homology-directed repair of DNA double-strand breaks occurring in these regions.

Critically, a 2025 study demonstrated that peripheral blood lymphocytes from individuals with CHAMP1 syndrome exhibit defective heterochromatin clustering and impaired repair of DNA double-strand breaks [li-2025-heterochromatin-abstract]. This finding provides direct evidence from patient cells that heterochromatin and DNA repair defects contribute to CHAMP1 syndrome pathogenesis, offering mechanistic insight into how mutations in a mitotic regulator lead to neurodevelopmental consequences.

## 6. Role in Cell Survival and Mcl-1 Regulation

An additional function of CHAMP1 in cell survival was characterized by Hino et al. (2021), who demonstrated that CHAMP1 depletion accelerates mitotic cell death and suppresses mitotic slippage in cancer cells [hino-2021-mcl1-abstract]. Notably, this cell survival function is independent of CHAMP1's role in kinetochore-microtubule attachment, as accelerated mitotic cell death was observed even in the presence of high-dose nocodazole, which eliminates kinetochore-microtubule attachments entirely.

The mechanism involves regulation of Mcl-1, an antiapoptotic member of the Bcl-2 family. CHAMP1 maintains Mcl-1 expression at both protein and mRNA levels [hino-2021-mcl1-abstract]. At the protein level, CHAMP1 suppresses proteasome-dependent degradation of Mcl-1, stabilizing the protein. At the mRNA level, CHAMP1 depletion reduces Mcl-1 mRNA production rather than increasing its degradation, though the precise mechanism does not appear to involve direct transcriptional control. Immunoprecipitation experiments found no direct binding between CHAMP1 and Mcl-1, indicating that the regulation is indirect [hino-2021-mcl1-abstract].

The functional consequence of this regulation is that CHAMP1 depletion reduces cell viability and exhibits synergistic effects with antimitotic drugs including nocodazole, taxol, and vincristine. In xenograft mouse models, CHAMP1 depletion suppressed tumor growth [hino-2021-mcl1-abstract]. These findings suggest that CHAMP1 could be a therapeutic target to overcome resistance to antimitotic chemotherapy by shifting cells toward apoptosis.

## 7. CHAMP1-Related Neurodevelopmental Disorder

In 2015, Hempel and colleagues identified de novo mutations in CHAMP1 as a cause of intellectual disability with severe speech impairment [hempel-2015-intellectual-disability-abstract]. The disorder is now recognized as CHAMP1-related neurodevelopmental disorder (CHAMP1-NDD), an ultra-rare condition with fewer than 250 individuals identified worldwide as of 2025.

The disorder is autosomal dominant, with nearly all cases arising from de novo mutations. The majority of pathogenic variants are premature termination codon mutations (frameshift or nonsense) that are predicted to disrupt the C-terminal zinc finger domains essential for proper chromosome alignment and chromatin localization [hempel-2015-intellectual-disability-abstract]. The gene is expressed from the terminal exon, so resultant mRNAs may escape nonsense-mediated decay, potentially allowing expression of truncated proteins.

Clinical features include intellectual disability ranging from mild to severe, pronounced speech and language impairment (with expressive deficits typically more severe than receptive), motor developmental delay with walking typically achieved between 18 and 48 months, and muscular hypotonia particularly affecting the trunk and orofacial regions [hempel-2015-intellectual-disability-abstract][abiraad-2023-clinical-review-abstract]. Characteristic dysmorphic features include a short philtrum, tented upper lip, everted lower lip, hypertelorism, and upslanted palpebral fissures. Microcephaly is observed in approximately half of cases. A notable behavioral feature is a friendly, amicable disposition observed consistently across affected individuals.

Additional features may include seizures, ophthalmologic abnormalities (hyperopia, strabismus), gastrointestinal problems (constipation, gastroesophageal reflux), stereotypical movements, and decreased pain sensation [abiraad-2023-clinical-review-abstract]. Recent studies have also documented autism spectrum disorder (in approximately 33% of patients), attention-deficit/hyperactivity disorder (in approximately 60%), and other behavioral symptoms including repetitive behaviors and sensory-seeking.

A 2023 case report documented the first patient with CHAMP1-related disorder showing all features of metabolic syndrome, including abdominal obesity, hypertension, hypertriglyceridemia, low HDL cholesterol, impaired fasting glucose, elevated uric acid, and polycystic ovary syndrome [abiraad-2023-clinical-review-abstract]. Whether this represents a previously unrecognized aspect of the phenotype or a coincidental finding requires further investigation.

## 8. Mouse Models and Neuronal Development

The first characterization of CHAMP1 knockout mice by Nagai et al. (2022) provided important insights into the developmental functions of this gene [nagai-2022-knockout-mouse-abstract]. Homozygous knockout mice (CHAMP1-/-) on a pure C57BL/6J background were neonatally lethal, dying within two days of birth despite having grossly normal brain structure. On mixed genetic backgrounds, homozygous knockouts could survive to adulthood but exhibited skeletal abnormalities.

Heterozygous knockout mice (CHAMP1+/-) were healthy and fertile, enabling behavioral and cognitive testing [nagai-2022-knockout-mouse-abstract]. Adult heterozygous mice exhibited mild working memory impairment in T-maze forced alternation tasks, cued fear memory deficits in remote memory testing, increased social interaction in home-cage monitoring, and depression-like behaviors in the Porsolt forced swim test. These phenotypes resemble some aspects of the human disorder, supporting the relevance of the mouse model.

Developmental studies revealed that CHAMP1 is critical for proper neuronal differentiation and migration. Homozygous knockout embryos showed increased mitotic cells in the cerebral cortex at embryonic day 14.5 (E14.5), suggesting prolonged or abnormal cell division [nagai-2022-knockout-mouse-abstract]. In vitro, CHAMP1-deficient neural stem cells exhibited delayed differentiation into neurons and astrocytes, though proliferation rates were normal. In utero electroporation with CHAMP1 siRNA demonstrated delayed cortical migration, with transfected cells failing to reach the cortical plate by E16.5.

Transcriptomic analysis of E14.5 embryonic brains identified 178 differentially expressed genes, with 111 downregulated and 67 upregulated [nagai-2022-knockout-mouse-abstract]. Downregulated genes were enriched for neurotransmitter transport pathways, and gene set enrichment analysis revealed significant downregulation of 94 neurodevelopmental disorder-associated genes. Of particular note was downregulation of Slc6a1, which encodes a GABA transporter associated with intellectual disability in humans.

## 9. Cancer Implications and Therapeutic Potential

The multiple functions of CHAMP1 have important implications for cancer biology and therapy. The finding that high CHAMP1 expression promotes homologous recombination has significant consequences for PARP inhibitor therapy, which targets HR-deficient tumors [li-2022-rev7-abstract].

Analysis of The Cancer Genome Atlas (TCGA) datasets revealed that in BRCA1-mutant tumors, high CHAMP1 expression correlates with worse overall survival [li-2022-rev7-abstract]. This correlation is particularly strong in tumors with high REV7 expression. A PARP inhibitor-resistant BRCA1-deficient cell clone showed elevated CHAMP1 levels, and knockdown of CHAMP1 in these cells restored PARP inhibitor sensitivity. CHAMP1 amplification occurs frequently in breast and ovarian cancers.

CHAMP1 expression also correlates strongly with cyclin E (CCNE1) mRNA levels. Cells experiencing replication stress from cyclin E amplification appear dependent on CHAMP1-mediated HR for survival, representing a potential synthetic lethal relationship [li-2022-rev7-abstract].

The work by Hino et al. on Mcl-1 regulation provides an additional therapeutic angle [hino-2021-mcl1-abstract]. CHAMP1 depletion sensitizes cells to antimitotic drugs and suppresses tumor growth in xenograft models. The synergy between CHAMP1 depletion and antimitotic agents suggests that CHAMP1 inhibition could overcome resistance to microtubule-targeting chemotherapies.

## Open Questions

Several important questions remain regarding CHAMP1 biology, though recent advances have begun to address some of these:

1. **Mechanistic link to neurodevelopment**: While CHAMP1 deficiency impairs neuronal differentiation and migration, and the 2025 study demonstrated heterochromatin and DNA repair defects in patient lymphocytes, the precise molecular mechanisms connecting these defects to neurodevelopmental consequences remain unclear. The expression of CHAMP1 in apical radial glia and its role in proper cell division suggest that dividing neural progenitors may be particularly vulnerable to CHAMP1 dysfunction, but this requires further investigation.

2. **Genotype-phenotype correlations in disease**: Recent work confirms that premature termination codon mutations cause HR defects through haploinsufficiency, while missense mutations do not affect HR [yoshizaki-2024-haploinsufficiency-abstract]. Whether this explains clinical differences between mutation types, and whether other CHAMP1 functions (mitotic, heterochromatin) are differentially affected, requires systematic comparison.

3. **Regulation of CENP-E/F localization**: CHAMP1 is required for proper kinetochore localization of CENP-E and CENP-F, but no direct physical interaction has been detected. The mechanism by which CHAMP1 regulates these downstream effectors remains to be elucidated.

4. **Mcl-1 regulatory pathway**: CHAMP1 maintains Mcl-1 expression at both mRNA and protein levels without direct binding. The signaling pathway(s) connecting CHAMP1 to Mcl-1 regulation are unknown.

5. **CHAMP1 complex regulation**: While the CHAMP1-POGZ-HP1 complex architecture has been clarified, including SETDB1 recruitment and the CDYL2-mediated hierarchical recruitment to H3K9me3-marked chromatin [li-2025-heterochromatin-abstract][siouda-2023-cdyl2-abstract], the dynamic regulation of this complex during the cell cycle and in response to DNA damage requires further characterization.

6. **Potential therapeutic applications**: Whether CHAMP1 inhibition would be therapeutically tractable (given potential toxicity from disrupting essential mitotic and repair functions) and in which cancer contexts it might be beneficial requires preclinical investigation. The relationship between CHAMP1 and PARP inhibitor resistance identifies potential therapeutic strategies.

7. **Metabolic phenotypes**: The observation of metabolic syndrome in a CHAMP1-related disorder patient raises the question of whether CHAMP1 has additional, undiscovered functions in metabolic regulation.

8. **CHAMP1 in ALT-positive tumors**: The finding that CHAMP1 is required for heterochromatin maintenance and DNA repair at telomeres in ALT-positive cancer cells [li-2025-heterochromatin-abstract] raises the question of whether CHAMP1 could be a therapeutic vulnerability in this subset of cancers.

## References

1. **itoh-2011-kinetochore**: Itoh G, Kanno S, Uchida KSK, Chiba S, Sugino S, Watanabe K, Mizuno K, Yasui A, Hirota T, Tanaka K. CAMP (C13orf8, ZNF828) is a novel regulator of kinetochore-microtubule attachment. *EMBO J*. 2011;30(1):130-144. doi:10.1038/emboj.2010.276. PMID: 21063390; PMCID: PMC3020106.

2. **li-2022-rev7**: Li F, Sarangi P, Iyer DR, Feng H, Moreau L, Nguyen H, Clairmont C, D'Andrea AD. CHAMP1 binds to REV7/FANCV and promotes homologous recombination repair. *Cell Reports*. 2022;40(9):111297. doi:10.1016/j.celrep.2022.111297. PMID: 36044844; PMCID: PMC9472291.

3. **hempel-2015-intellectual-disability**: Hempel M, Cremer K, Ockeloen CW, et al. De Novo Mutations in CHAMP1 Cause Intellectual Disability with Severe Speech Impairment. *Am J Hum Genet*. 2015;97(3):493-500. doi:10.1016/j.ajhg.2015.08.003. PMID: 26340335; PMCID: PMC4564986.

4. **nagai-2022-knockout-mouse**: Nagai M, Iemura K, Kikkawa T, Naher S, Hattori S, Hagihara H, Nagata K, Anzawa H, Kugisaki R, Wanibuchi H, Abe T, Inoue K, Kinoshita K, Miyakawa T, Osumi N, Tanaka K. Deficiency of CHAMP1, a gene related to intellectual disability, causes impaired neuronal development and a mild behavioural phenotype. *Brain Commun*. 2022;4(5):fcac220. doi:10.1093/braincomms/fcac220. PMID: 36106092; PMCID: PMC9465530.

5. **hino-2021-mcl1**: Hino M, Iemura K, Ikeda M, Itoh G, Tanaka K. Chromosome alignment-maintaining phosphoprotein CHAMP1 plays a role in cell survival through regulating Mcl-1 expression. *Cancer Sci*. 2021;112(9):3711-3721. doi:10.1111/cas.15018. PMID: 34107118; PMCID: PMC8409433.

6. **abiraad-2023-clinical-review**: Abi Raad S, Yazbeck Karam V, Chouery E, Mehawej C, Megarbane A. CHAMP1-Related Disorder: Sharing 20 Years of thorough Clinical Follow-Up and Review of the Literature. *Genes (Basel)*. 2023;14(8):1546. doi:10.3390/genes14081546. PMID: 37628598; PMCID: PMC10454041.

7. **yoshizaki-2024-haploinsufficiency**: Yoshizaki Y, Ouchi Y, Kurniawan D, et al. CHAMP1 premature termination codon mutations found in individuals with intellectual disability cause a homologous recombination defect through haploinsufficiency. *Sci Rep*. 2024;14:31251. doi:10.1038/s41598-024-83435-y. PMID: 39738383.

8. **siouda-2023-cdyl2**: Siouda M, Dujardin AD, Dekeyzer B, Schaeffer L, Mulligan P. Chromodomain on Y-like 2 (CDYL2) implicated in mitosis and genome stability regulation via interaction with CHAMP1 and POGZ. *Cell Mol Life Sci*. 2023;80(2):47. doi:10.1007/s00018-022-04659-7. PMID: 36658409; PMCID: PMC11072993.

9. **li-2025-heterochromatin**: Li F, et al. CHAMP1 complex directs heterochromatin assembly and promotes homology-directed DNA repair. *Nat Commun*. 2025;16(1):1714. doi:10.1038/s41467-025-56834-6. PMID: 39962076; PMCID: PMC11832927.

10. **vancaugherty-2024-thesis**: Van Caugherty ZM. The Genomics of CHAMP1: Insights into their Cell-Type Specificity and Developmental Trajectories. Master's thesis, Medical University of South Carolina, 2024. https://medica-musc.researchcommons.org/theses/892/


## Citations

1. abiraad-2023-clinical-review-abstract.md
2. abiraad-2023-clinical-review-summary.md
3. hempel-2015-intellectual-disability-abstract.md
4. hempel-2015-intellectual-disability-summary.md
5. hino-2021-mcl1-abstract.md
6. hino-2021-mcl1-summary.md
7. itoh-2011-kinetochore-abstract.md
8. itoh-2011-kinetochore-summary.md
9. li-2022-rev7-abstract.md
10. li-2022-rev7-summary.md
11. li-2025-heterochromatin-abstract.md
12. li-2025-heterochromatin-summary.md
13. nagai-2022-knockout-mouse-abstract.md
14. nagai-2022-knockout-mouse-summary.md
15. siouda-2023-cdyl2-abstract.md
16. siouda-2023-cdyl2-summary.md
17. yoshizaki-2024-haploinsufficiency-abstract.md
18. yoshizaki-2024-haploinsufficiency-summary.md