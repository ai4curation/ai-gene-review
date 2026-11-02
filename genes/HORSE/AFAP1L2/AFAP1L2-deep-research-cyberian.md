---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:15:56.923342'
end_time: '2026-10-26T01:24:55.230793'
duration_seconds: 538.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: AFAP1L2
  gene_symbol: AFAP1L2
  uniprot_accession: A0A9L0RQI4
  protein_description: 'RecName: Full=Actin filament-associated protein 1-like 2 {ECO:0000256|ARBA:ARBA00072612};'
  gene_info: Name=AFAP1L2 {ECO:0000313|Ensembl:ENSECAP00000066139.1};
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: AFAP. (IPR030113); AFAP_C. (IPR063177); AFAP_N. (IPR063153); PH-like_dom_sf.
    (IPR011993); PH_domain. (IPR001849)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3302
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 70
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0RQI4
- **Protein Description:** RecName: Full=Actin filament-associated protein 1-like 2 {ECO:0000256|ARBA:ARBA00072612};
- **Gene Information:** Name=AFAP1L2 {ECO:0000313|Ensembl:ENSECAP00000066139.1};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AFAP. (IPR030113); AFAP_C. (IPR063177); AFAP_N. (IPR063153); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "AFAP1L2" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'AFAP1L2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **AFAP1L2** (gene ID: AFAP1L2, UniProt: A0A9L0RQI4) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# AFAP1L2 (XB130) in the Horse (*Equus caballus*; UniProt A0A9L0RQI4): A Src/PI3K-Coupling Adaptor That Organizes Cortical Actin in Epithelia

## 1. Introduction and Summary

The horse gene *AFAP1L2* encodes actin filament-associated protein 1-like 2, an 850-residue predicted protein (UniProt A0A9L0RQI4, Ensembl ENSECAP00000066139.1, equine chromosome 1). The entry is unreviewed, has protein-existence level 4 ("predicted"), and comes from the Thoroughbred reference genome [uniprot-A0A9L0RQI4-entry; wade-2009-horse-genome-abstract]. Its function, subunit and localization fields are automatic ARBA annotations. These state that the protein may enhance SRC kinase activity, contributes to SRC-regulated transcription, interacts with SRC and with LCK, and is cytoplasmic [uniprot-A0A9L0RQI4-entry]. All of them are inherited from the reviewed human entry (Q8N4X5), whose evidence is two experimental papers [uniprot-Q8N4X5-entry; xu-2007-xb130-adaptor-abstract; emaduddin-2008-odin-src-target-abstract].

**Identity check.** The gene symbol, protein name, domain composition and organism all match. A PubMed search for AFAP1L2 or XB130 together with horse, equine or *Equus* returned no records (search performed 2026-10-26). There is therefore **no horse-specific experimental literature**. Everything below about function is inferred from orthologs: mainly human XB130, mouse and rat PI3KAP/XB130, and work in human, mouse and rat cell lines. I aligned the horse protein with the human canonical isoform (818 aa). Across the human sequence the two are 88.6% identical. The PH domains are 98% identical, and every experimentally mapped functional residue I checked is conserved (Section 2; `analysis/identity_analysis.txt`). This makes transfer of function from the ortholog well supported. No literature on a different gene with the same symbol turned up.

**Main conclusion.** AFAP1L2/XB130 is a non-catalytic adaptor (scaffold) protein. It has no enzymatic activity and no transport substrate. It works in two connected ways. First, it is a tyrosine-kinase substrate that couples upstream kinases to class I PI3K. These kinases are c-Src, RET (including the oncogenic RET/PTC fusion), and Src-family kinases downstream of TSH/cAMP. Once phosphorylated on an N-terminal YxxM motif (human Tyr54), XB130 recruits the p85α regulatory subunit and activates Akt. Akt in turn phosphorylates a selected set of substrates that control G1–S progression and survival [lodyga-2009-xb130-retptc-pi3k-abstract; yamanaka-2012-pi3kap-igf-abstract; shiozaki-2012-xb130-akt-downstream-abstract]. Second, XB130 is an actin-binding, multimerizing scaffold. It cross-links F-actin in vitro [yamanaka-2016-pi3kap-actin-crosslink-abstract], is recruited to Rac-driven lamellipodial branched actin [lodyga-2010-xb130-lamellipodia-abstract], and in thyroid follicular cells sits at the apical membrane, where it links the actin cortex to microtubules [wang-2021-xb130-ko-hypothyroidism-abstract; wang-2022-xb130-folliculogenesis-abstract]. Mice lacking XB130 have congenital hypothyroidism with disorganized apical thyrocyte membranes [wang-2021-xb130-ko-hypothyroidism-abstract]. They also have impaired airway epithelial repair [toba-2015-xb130-airway-repair-abstract; zhao-2014-xb130-tracheal-repair-abstract]. The protein is therefore best described as a cytoplasmic and cortical/apical signaling scaffold in epithelial cells, especially thyrocytes, with additional roles in oligodendrocyte differentiation [tanga-2019-ptprz-afap1l2-oligodendrocyte-abstract].

## 2. Gene, Protein Architecture and Conservation in the Horse

Human XB130 was cloned serendipitously while searching for human AFAP1 (AFAP-110). It sits on chromosome 10q25.3 and encodes an 818-residue protein that migrates at about 130 kDa [xu-2007-xb130-adaptor-abstract; bai-2014-xb130-review-fulltext]. It is also called AFAP1L2, KIAA1914 and, in rodents, PI3K-associated protein (PI3KAP) [bai-2014-xb130-review-fulltext; yamanaka-2012-pi3kap-igf-abstract]. The human gene has 19 exons and several splice variants, and orthologs exist throughout vertebrates [bai-2014-xb130-review-fulltext].

The protein is built from distinct modules [xu-2007-xb130-adaptor-abstract; bai-2014-xb130-review-fulltext]. Its N-terminal region carries a proline-rich SH3-binding motif and three SH2-binding tyrosine motifs, one of which is the YxxM site that docks p85; AFAP1 and AFAP1L1 each have only one SH2-binding motif. The center of the protein holds two pleckstrin homology (PH) domains, which are thought to bind phosphoinositides or membranes. The C-terminal region contains a coiled coil and a short, conserved segment that binds actin directly.

XB130 belongs to the three-member AFAP family with AFAP1 and AFAP1L1. It shares about 40% homology with AFAP1. Unlike AFAP1 and AFAP1L1, it lacks their classical leucine zipper and actin-binding domain [bai-2014-xb130-review-fulltext; snyder-2011-afap1l1-cortactin-abstract]. The InterPro and Pfam signatures in the horse entry match this layout: AFAP family (IPR030113, PANTHER PTHR14338:SF4), AFAP_N, AFAP_C and two PH domains (PS50003 at residues 186–282 and 364–458) [uniprot-A0A9L0RQI4-entry]. The human PH domains are at 175–271 and 353–447, and the coiled coil at 652–749 [uniprot-Q8N4X5-entry]. A structural genomics consortium solved the second human PH domain by NMR (PDB 2COF, residues 354–447; deposited 2005), confirming that this region adopts a PH-domain fold [pdb-2cof-entry; uniprot-Q8N4X5-entry]. Horse and human are 98% identical across this domain, so the structure should apply directly to the horse protein.

My pairwise alignment (Needleman–Wunsch, BLOSUM62; `analysis/residue_mapping.py`) shows three length differences between the horse and human proteins. First, the horse model has an 11-residue N-terminal offset, because its predicted first exon (MRSTMWVLLANTATSN…) replaces human isoform 1's MERYKAL… start. Second, there is a short insertion in the coiled-coil region. Third, the PH domains shift by +11 to positions that match the horse annotation exactly. Every experimentally defined human motif maps onto a conserved horse residue. Human Tyr54, the p85-binding tyrosine of the YxxM motif, corresponds to horse Tyr65 within an identical DEEYIYM sequence. The PPPxxxP SH3-binding motif that binds Tks5 (human Pro101, Pro103 and Pro107) corresponds to horse Pro112, Pro114 and Pro118 in the stretch PDLPPPKIIPERK. The additional SH2-binding motifs at human Tyr124 and Tyr161/Pro164 correspond to horse Tyr135 and Tyr172/Pro175. All three phosphosites annotated in the human entry (Ser408, Tyr413 and Ser484) are also retained.

The C-terminal actin-binding stretch is almost invariant: the last 30 residues differ from human at only two positions (`analysis/identity_analysis.txt`). This agrees with the strong vertebrate conservation of the actin-binding segment reported by Yamanaka and colleagues [yamanaka-2016-pi3kap-actin-crosslink-fulltext].

Yamanaka and colleagues also observed something that bears directly on the horse model. Human isoform 1 has an N-terminal K/RYKXL sequence that was proposed to help target XB130 to lamellipodia. Mouse variant 1 lacks this sequence because it uses a different first exon, and a splice variant that skips exon 2 restores it [yamanaka-2016-pi3kap-actin-crosslink-fulltext]. The horse Ensembl model starts with an alternative first exon and also lacks RYKAL. It therefore resembles mouse variant 1 more than human isoform 1. Whether horses express additional N-terminal isoforms is unknown.

## 3. Primary Molecular Function: Tyrosine-Phosphorylated Adaptor Coupling Kinases to PI3K

The founding study showed that endogenous XB130 binds c-Src. Co-expressing the two in COS-7 cells activated Src and raised tyrosine phosphorylation of many proteins, including XB130 itself. XB130 also enhanced Src-driven serum response element and AP-1 transcription, and deleting its N-terminus (which removes the SH3-binding motif and several SH2-binding sites) weakened this effect [xu-2007-xb130-adaptor-abstract]. In human lung epithelial cells, siRNA against XB130 lowered c-Src activity, IL-8 production and EGF-induced phosphorylation of Akt and GSK3β, and disturbed the cell cycle [xu-2007-xb130-adaptor-abstract]. These findings are the source of the "enhances SRC kinase activity" annotation on the human and horse entries [uniprot-Q8N4X5-entry; uniprot-A0A9L0RQI4-entry].

The mechanism was clarified in thyroid cells. Lodyga and colleagues found XB130 mostly in the thyroid. The constitutively active RET/PTC kinase phosphorylated it mainly at Tyr54, which lies in a YxxM motif and is the critical binding site for the SH2 domains of PI3K p85α [lodyga-2009-xb130-retptc-pi3k-abstract; bai-2014-xb130-review-fulltext]. In TPC1 papillary thyroid cancer cells, knocking down XB130 strongly reduced Akt activity but left ERK1/2 phosphorylation unchanged. This shows that XB130 couples the kinase specifically to PI3K rather than to the MAPK branch [lodyga-2009-xb130-retptc-pi3k-abstract].

A separate line of work reached the same conclusion in normal thyroid cells. Rat FRTL-5 thyrocytes were pretreated with TSH or cAMP, which potentiates IGF-I-driven DNA synthesis. Under these conditions a 125-kDa tyrosine-phosphorylated p85 partner appeared, and mass spectrometry identified it as the rat XB130 ortholog, named PI3KAP [yamanaka-2012-pi3kap-igf-abstract]. cAMP raised PI3KAP mRNA, protein, Src-dependent tyrosine phosphorylation, p85 binding and associated PI3K activity. Src-family inhibitors (PP1, PP2) abolished the phosphorylation and the p85 binding. Knocking down PI3KAP weakened cAMP potentiation of IGF-I mitogenesis. A Y72F mutant, the rat equivalent of the p85-docking tyrosine, could not bind p85 or enhance IGF-I-induced DNA synthesis in NIH3T3 cells [yamanaka-2012-pi3kap-igf-abstract]. Together these studies place XB130 at a node where TSH/cAMP signaling, Src-family kinases and growth-factor PI3K signaling meet. The horse protein keeps the corresponding tyrosine (Tyr65) in an intact YxxM context.

XB130 is a substrate of several tyrosine kinases. Lck-SH2 affinity purification of tyrosine-phosphorylated proteins from colorectal cancer cells pulled down AFAP1L2/XB130 together with established Src-family substrates [emaduddin-2008-odin-src-target-abstract]. This is the basis for the "interacts with LCK when tyrosine phosphorylated" annotation [uniprot-Q8N4X5-entry]. XB130 is also phosphorylated by multiple other tyrosine kinases [shiozaki-2012-xb130-akt-downstream-abstract].

Phosphorylation is opposed by a dedicated phosphatase. In oligodendrocyte precursor-like cells, AFAP1L2 was the substrate of receptor protein tyrosine phosphatase PTPRZ that responded most strongly when pleiotrophin inactivated the phosphatase. PTPRZ dephosphorylated AFAP1L2 directly, both in vitro and in cells [tanga-2019-ptprz-afap1l2-oligodendrocyte-abstract]. XB130's output therefore depends on the balance between tyrosine kinases and PTPRZ-type phosphatases.

A second scaffold partner, Tks5 (SH3PXD2A), came out of a yeast two-hybrid screen as the most frequently recovered XB130 interactor. Endogenous XB130, Tks5 and Src form a complex. The fifth SH3 domain of Tks5 binds the N-terminal PPPxxxP motif of XB130, with Pro101 and Tyr161 contributing [moodley-2015-xb130-tks5-src-fulltext]. Knocking down either protein reduced serum- and growth factor-induced Src activation and the downstream phosphorylation of PI3K and Akt. It also caused G1 arrest and caspase-3-dependent apoptosis. Disrupting the XB130–Tks5 interface with mutants had similar effects [moodley-2015-xb130-tks5-src-abstract]. The horse protein conserves all of these contact residues.

## 4. Downstream Signaling: Selective Akt Outputs, Cell Cycle, Survival and Gene Expression

Downstream of PI3K, XB130 regulates only part of Akt's output. In thyroid (WRO) and lung (A549) cancer cells, knocking down XB130 reduced phosphorylation of p21Cip1/WAF1, p27Kip1, FOXO3a and GSK3β, raised p21 protein levels and increased cleavage of caspase-8 and caspase-9. Phosphorylation of FOXO1 and p53 protein levels did not change [shiozaki-2012-xb130-akt-downstream-abstract]. The resulting cell-level effects were a block in G1–S progression, spontaneous apoptosis and greater sensitivity to intrinsic and extrinsic death stimuli [shiozaki-2011-xb130-thyroid-tumor-abstract; shiozaki-2012-xb130-akt-downstream-abstract]. The A549 cells lack RET/PTC, so this function does not depend on the oncogenic kinase [shiozaki-2012-xb130-akt-downstream-abstract].

Changes in gene expression appear to follow from this signaling rather than reflect a direct role in transcription. XB130 knockdown in WRO cells altered 246 transcripts, many of them proliferation-related transcriptional regulators [shiozaki-2011-xb130-thyroid-tumor-abstract]. XB130 also suppresses tumor-suppressive microRNAs (miR-33a, miR-149, miR-193a-3p) that target MYC, FOSL1 and SLC7A5 [takeshita-2013-xb130-mirna-abstract]. The early observation that XB130 boosts Src-dependent SRE/AP-1 reporter activity [xu-2007-xb130-adaptor-abstract] fits the same picture of a signaling adaptor upstream of transcription. In human hepatocellular carcinoma, AFAP1L2 was also reported to act through SRC to phosphorylate the mitophagy receptor FUNDC1. This reduces LC3B recruitment to mitochondria and suppresses mitophagy [ma-2024-afap1l2-src-fundc1-abstract]. That finding comes from a drug-resistance study and still needs independent mechanistic confirmation.

## 5. Cytoskeletal Function and Subcellular Localization

Despite the name, XB130 differs from AFAP1 in its basic localization. In resting BEAS-2B lung epithelial cells it is cytoplasmic, punctate and perinuclear, and it does not decorate stress fibers as AFAP1 does [bai-2014-xb130-review-fulltext; moodley-2015-xb130-tks5-src-fulltext]. This is consistent with the "Cytoplasm" annotation in UniProt [uniprot-Q8N4X5-entry]. Several stimuli move it to the cell periphery and the lamellipodial F-actin meshwork: EGF, wounding, PMA, the tobacco carcinogen NNK and constitutively active Rac1 (but not active RhoA) [lodyga-2010-xb130-lamellipodia-abstract; wu-2015-xb130-nnk-migration-abstract; bai-2014-xb130-review-fulltext]. Genetic and pharmacological experiments indicate that the formation of branched F-actin itself triggers this recruitment. The N-terminal 167 and C-terminal 63 residues are required, whereas the PH domains and the Src-targeted tyrosines are not [lodyga-2010-xb130-lamellipodia-abstract]. In airway epithelial cells XB130 co-distributes with WAVE2 and binds Rac1. It promotes lateral, lamellipodia-driven migration, while Tks5 promotes Cdc42-dependent, podosome-type invasive migration, and separation of the two scaffolds favors motility [moodley-2016-xb130-tks5-migration-abstract]. XB130 also helps move MT1-MMP (MMP-14) to motility structures after NNK exposure [wu-2015-xb130-nnk-migration-abstract]. Knocking down XB130 slowed wound closure, Matrigel invasion, lamellipodial persistence and spreading [lodyga-2010-xb130-lamellipodia-abstract].

XB130 can also act directly as an actin cross-linker. Using mouse PI3KAP/XB130, Yamanaka and colleagues found that a C-terminal segment (residues 830–840) is necessary and sufficient for co-sedimentation with F-actin. This segment is conserved across vertebrates and differs from the actin-binding domains of AFAP1 and AFAP1L1. They also showed that the N-terminal 40 residues mediate multimerization into 250–1200 kDa assemblies, and that full-length protein cross-links actin filaments in vitro. Mutants lacking either region could not cross-link actin, and overexpression enhanced fluid-phase endocytosis in an actin-binding-dependent way [yamanaka-2016-pi3kap-actin-crosslink-abstract; yamanaka-2016-pi3kap-actin-crosslink-fulltext]. This partly contradicts earlier statements that XB130 lacks an actin-binding domain [bai-2014-xb130-review-fulltext; moodley-2015-xb130-tks5-src-fulltext]. The two positions can be reconciled: XB130 lacks the classical AFAP-type actin-binding domain but has a short, non-canonical actin-binding motif. The horse sequence conserves this C-terminal motif.

In tissues, XB130 is concentrated at the apical side of polarized epithelia. In human trachea it lies in the apical cytoplasm of ciliated cells beneath the microvilli and is absent from basal cells [zhao-2014-xb130-tracheal-repair-fulltext]. In mouse thyroid follicles it is found mainly on the apical (luminal) membrane of thyrocytes [wang-2021-xb130-ko-hypothyroidism-abstract]. In three-dimensional thyrocyte cultures it lines up with actin filaments at the site where the apical membrane and lumen form. Without it, microtubule-associated proteins are recruited less efficiently and acetylated microtubules beneath the apical membrane are disorganized. This led the authors to propose that XB130 links the actin cortex to the microtubule network to establish polarity [wang-2022-xb130-folliculogenesis-abstract]. XB130 is also expressed in alveolar type I and type II cells [toba-2016-xb130-lps-lung-injury-abstract]. It has been reported in the nucleus of some cancer cells [bai-2014-xb130-review-fulltext], but the significance of this is not established.

Taken together, the evidence supports the following localization for horse AFAP1L2: cytoplasm (resting state), the cell cortex and lamellipodia (stimulated state), and the apical cortex and apical plasma membrane of polarized epithelial cells.

## 6. Physiological Roles from Knockout Models: Thyroid Hormone Synthesis and Epithelial Repair

The thyroid shows the clearest physiological role, consistent with the gene's high thyroid expression [lodyga-2009-xb130-retptc-pi3k-abstract; uniprot-Q8N4X5-entry]. *Xb130*-/- mice have transient postnatal growth retardation caused by congenital hypothyroidism. Thyroglobulin iodination and thyroid hormone release are reduced both before and after birth, and exogenous thyroxine rescues growth. The knockout thyroids have disorganized apical membranes, delayed folliculogenesis and abnormal lumen formation [wang-2021-xb130-ko-hypothyroidism-abstract]. Hormone synthesis (thyroglobulin iodination by thyroperoxidase and H₂O₂) happens at the apical membrane–colloid interface. A structural defect there therefore explains the hormonal phenotype more directly than a signaling defect does.

In aged knockout mice, cytoskeletal and adhesion-molecule organization is disturbed, iodide organification falls, thyroperoxidase becomes less responsive to H₂O₂, and severe multinodular goiter develops [cho-2022-xb130-goiter-abstract]. Thyroid transcriptomes from knockouts show early loss of metabolic gene programs, followed by matrix, angiogenic, proliferative and inflammatory programs [sugihara-2022-xb130-ko-thyroid-transcriptome-abstract]. These later changes are probably adaptive responses rather than direct XB130 targets. In normal thyrocytes the TSH/cAMP→Src→PI3KAP/XB130→PI3K axis (Section 3) also supports mitogenesis [yamanaka-2012-pi3kap-igf-abstract]. XB130 therefore contributes to both the structure and the growth control of the follicular epithelium.

In the airways, *Xb130*-null mice are grossly normal but have a thicker tracheal epithelium. After tracheal transplantation injury they accumulate excess proliferative and basal cells, which suggests altered epithelial differentiation [zhao-2014-xb130-tracheal-repair-abstract]. After naphthalene injury, repair of the small airways is delayed, with fewer Club cells, no expansion of bronchioalveolar stem cells, and reduced p85α, Akt and GSK-3β phosphorylation in the epithelium [toba-2015-xb130-airway-repair-abstract]. Loss of XB130 also worsens LPS-induced sepsis and acute lung injury, with more apoptosis, less proliferation and greater permeability [toba-2016-xb130-lps-lung-injury-abstract]. In the central nervous system, pleiotrophin-mediated inhibition of PTPRZ increases AFAP1L2 tyrosine phosphorylation and PI3K–AKT–mTOR signaling, which drives oligodendrocyte precursor differentiation. Mice with catalytically inactive PTPRZ show higher AFAP1L2 phosphorylation and faster myelination and remyelination [tanga-2019-ptprz-afap1l2-oligodendrocyte-abstract].

## 7. Disease Associations and Relevance to the Horse

In humans, XB130 has mainly been studied in cancer. Its RET/PTC substrate role and its support of thyroid tumor growth [lodyga-2009-xb130-retptc-pi3k-abstract; shiozaki-2011-xb130-thyroid-tumor-abstract] are complemented by the discovery of an *AFAP1L2/RET* fusion oncogene in a pediatric papillary thyroid carcinoma. That fusion transforms cells through MAPK activation [iyama-2017-afap1l2-ret-fusion-abstract]. Many expression-association studies in other carcinomas (listed in the review by Bai and colleagues [bai-2014-xb130-review-fulltext]) are correlative and add little to the molecular picture, so they are not detailed here.

For the horse, no variants, expression data or phenotypes linked to *AFAP1L2* were found in the literature. Given how conserved the protein is and how consistent the mouse knockout phenotypes are, a reasonable expectation is that equine AFAP1L2 works mainly in thyroid follicular epithelium, airway epithelium and oligodendrocyte-lineage cells. In those cells it would act as a tyrosine-phosphorylated PI3K-recruiting adaptor and as an apical/cortical actin scaffold. This remains a hypothesis based on ortholog data and should not be treated as established fact for the horse.

For Gene Ontology-style annotation of A0A9L0RQI4, the evidence supports several inferences by orthology or sequence similarity. At the level of molecular function, the protein can be described as a signaling adaptor. It binds protein kinases (SRC, RET), binds the PI3K regulatory subunit p85α through its phosphorylated YxxM motif, binds actin filaments, and forms homo-oligomers. In terms of biological process, it positively regulates PI3K/Akt signal transduction and Src kinase activity, takes part in actin filament cross-linking and lamellipodium-dependent cell migration, contributes to epithelial cell polarity and thyroid follicle development, and promotes the G1/S transition and cell survival. Its cellular components are the cytoplasm, lamellipodium, cell cortex and apical plasma membrane.

## Open Questions

Several gaps limit what can be said with confidence about horse AFAP1L2. The most basic concerns the horse gene model itself. The predicted horse protein starts with an alternative first exon and has a short insertion in the coiled-coil region. Equine transcript data, from RNA-seq or long-read sequencing, are needed to confirm the N-terminus. They would also show whether horses, like mice, express an isoform that carries the N-terminal K/RYKXL actin-targeting motif [yamanaka-2016-pi3kap-actin-crosslink-fulltext]. Mapping expression across equine tissues, especially thyroid, airway and brain, would then test whether the thyroid-dominant pattern seen in humans and mice holds in the horse.

Several mechanistic questions remain open even in the well-studied species. It is not known which lipids, if any, the two PH domains bind; Lodyga and colleagues found these domains dispensable for lamellipodial targeting [lodyga-2010-xb130-lamellipodia-abstract]. It is also unclear how the PI3K-recruiting and actin-cross-linking functions are coordinated. For example, tyrosine phosphorylation might regulate multimerization or actin binding. The proteins that connect XB130 to microtubules at the thyrocyte apical membrane have not been identified [wang-2022-xb130-folliculogenesis-abstract]. The mouse finding that a C-terminal motif binds actin also needs to be reconciled with the human finding that both termini are needed for lamellipodial targeting [yamanaka-2016-pi3kap-actin-crosslink-fulltext; lodyga-2010-xb130-lamellipodia-abstract].

The only experimental structure is an NMR solution structure of the isolated second PH domain of the human protein (PDB 2COF, residues 354–447) [pdb-2cof-entry; uniprot-Q8N4X5-entry]. No full-length or multimeric structure exists. Structural work could start from the AlphaFold model listed in the horse entry [uniprot-A0A9L0RQI4-entry] to define how the N-terminal multimerization region and the coiled coil assemble, and whether the PH domains have the basic pockets typical of phosphoinositide-binding PH domains. The mouse knockout phenotypes [wang-2021-xb130-ko-hypothyroidism-abstract; cho-2022-xb130-goiter-abstract] suggest that equine thyroid physiology and disease would be the most informative setting for testing whether *AFAP1L2* variation matters in horses; this suggestion rests on mouse data alone. Finally, the reported AFAP1L2–SRC–FUNDC1 link to mitophagy comes from a single study of drug-resistant hepatocellular carcinoma [ma-2024-afap1l2-src-fundc1-abstract] and should be validated independently, including in non-cancer cells.

## References

* **uniprot-A0A9L0RQI4**: UniProtKB/TrEMBL entry A0A9L0RQI4_HORSE, Actin filament-associated protein 1-like 2 (*Equus caballus*), entry version 14 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0RQI4.txt
* **pdb-2cof-entry**: Li H, Saito K, Koshiba S, et al. Solution structure of the C-terminal PH domain of hypothetical protein KIAA1914 from human. RCSB Protein Data Bank entry 2COF (solution NMR; released 2005-11-17). https://www.rcsb.org/structure/2COF
* **uniprot-Q8N4X5**: UniProtKB/Swiss-Prot entry Q8N4X5 (AF1L2_HUMAN), Actin filament-associated protein 1-like 2 (*Homo sapiens*). https://rest.uniprot.org/uniprotkb/Q8N4X5.txt
* **wade-2009-horse-genome**: Wade CM, Giulotto E, Sigurdsson S, et al. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 326:865-7. PMID: 19892987; DOI: 10.1126/science.1178158; PMCID: PMC3785132. https://pubmed.ncbi.nlm.nih.gov/19892987/
* **xu-2007-xb130-adaptor**: Xu J, Bai XH, Lodyga M, et al. (2007). XB130, a novel adaptor protein for signal transduction. *J Biol Chem* 282:16401-12. PMID: 17412687; DOI: 10.1074/jbc.M701684200. https://pubmed.ncbi.nlm.nih.gov/17412687/
* **lodyga-2009-xb130-retptc-pi3k**: Lodyga M, De Falco V, Bai XH, et al. (2009). XB130, a tissue-specific adaptor protein that couples the RET/PTC oncogenic kinase to PI 3-kinase pathway. *Oncogene* 28:937-49. PMID: 19060924; DOI: 10.1038/onc.2008.447. https://pubmed.ncbi.nlm.nih.gov/19060924/
* **lodyga-2010-xb130-lamellipodia**: Lodyga M, Bai XH, Kapus A, et al. (2010). Adaptor protein XB130 is a Rac-controlled component of lamellipodia that regulates cell motility and invasion. *J Cell Sci* 123:4156-69. PMID: 21084565; DOI: 10.1242/jcs.071050. https://pubmed.ncbi.nlm.nih.gov/21084565/
* **shiozaki-2011-xb130-thyroid-tumor**: Shiozaki A, Lodyga M, Bai XH, et al. (2011). XB130, a novel adaptor protein, promotes thyroid tumor growth. *Am J Pathol* 178:391-401. PMID: 21224076; DOI: 10.1016/j.ajpath.2010.11.024; PMCID: PMC3070596. https://pubmed.ncbi.nlm.nih.gov/21224076/
* **shiozaki-2012-xb130-akt-downstream**: Shiozaki A, Shen-Tu G, Bai X, et al. (2012). XB130 mediates cancer cell proliferation and survival through multiple signaling events downstream of Akt. *PLoS One* 7:e43646. PMID: 22928011; DOI: 10.1371/journal.pone.0043646; PMCID: PMC3426539. https://pubmed.ncbi.nlm.nih.gov/22928011/
* **yamanaka-2012-pi3kap-igf**: Yamanaka D, Akama T, Fukushima T, et al. (2012). Phosphatidylinositol 3-kinase-binding protein, PI3KAP/XB130, is required for cAMP-induced amplification of IGF mitogenic activity in FRTL-5 thyroid cells. *Mol Endocrinol* 26:1043-55. PMID: 22496359; DOI: 10.1210/me.2011-1349; PMCID: PMC5416991. https://pubmed.ncbi.nlm.nih.gov/22496359/
* **yamanaka-2016-pi3kap-actin-crosslink**: Yamanaka D, Akama T, Chida K, et al. (2016). Phosphatidylinositol 3-Kinase-Associated Protein (PI3KAP)/XB130 Crosslinks Actin Filaments through Its Actin Binding and Multimerization Properties In Vitro and Enhances Endocytosis in HEK293 Cells. *Front Endocrinol (Lausanne)* 7:89. PMID: 27462298; DOI: 10.3389/fendo.2016.00089; PMCID: PMC4939424. https://pubmed.ncbi.nlm.nih.gov/27462298/
* **moodley-2015-xb130-tks5-src**: Moodley S, Hui Bai X, Kapus A, et al. (2015). XB130/Tks5 scaffold protein interaction regulates Src-mediated cell proliferation and survival. *Mol Biol Cell* 26:4492-502. PMID: 26446840; DOI: 10.1091/mbc.E15-07-0483; PMCID: PMC4666142. https://pubmed.ncbi.nlm.nih.gov/26446840/
* **moodley-2016-xb130-tks5-migration**: Moodley S, Derouet M, Bai XH, et al. (2016). Stimulus-dependent dissociation between XB130 and Tks5 scaffold proteins promotes airway epithelial cell migration. *Oncotarget* 7:76437-76452. PMID: 27835612; DOI: 10.18632/oncotarget.13261; PMCID: PMC5363521. https://pubmed.ncbi.nlm.nih.gov/27835612/
* **bai-2014-xb130-review**: Bai XH, Cho HR, Moodley S, et al. (2014). XB130-A Novel Adaptor Protein: Gene, Function, and Roles in Tumorigenesis. *Scientifica (Cairo)* 2014:903014. PMID: 24995146; DOI: 10.1155/2014/903014; PMCID: PMC4068053. https://pubmed.ncbi.nlm.nih.gov/24995146/
* **wang-2021-xb130-ko-hypothyroidism**: Wang Y, Shimizu H, Xiang YY, et al. (2021). XB130 Deficiency Causes Congenital Hypothyroidism in Mice due to Disorganized Apical Membrane Structure and Function of Thyrocytes. *Thyroid* 31:1650-1661. PMID: 34470464; DOI: 10.1089/thy.2021.0195; PMCID: PMC8917886. https://pubmed.ncbi.nlm.nih.gov/34470464/
* **wang-2022-xb130-folliculogenesis**: Wang Y, Xiang YY, Sugihara J, et al. (2022). XB130 Plays an Essential Role in Folliculogenesis Through Mediating Interactions Between Microfilament and Microtubule Systems in Thyrocytes. *Thyroid* 32:128-137. PMID: 34652970; DOI: 10.1089/thy.2021.0461; PMCID: PMC8861928. https://pubmed.ncbi.nlm.nih.gov/34652970/
* **cho-2022-xb130-goiter**: Cho HR, Sugihara J, Shimizu H, et al. (2022). Pathogenesis of Multinodular Goiter in Elderly XB130-Deficient Mice: Alteration of Thyroperoxidase Affinity with Iodide and Hydrogen Peroxide. *Thyroid* 32:385-396. PMID: 34915750; DOI: 10.1089/thy.2021.0458; PMCID: PMC9048175. https://pubmed.ncbi.nlm.nih.gov/34915750/
* **sugihara-2022-xb130-ko-thyroid-transcriptome**: Sugihara J, Wong A, Shimizu H, et al. (2022). Thyroidal Transcriptomic Profiles of Pathoadaptive Responses to Congenital Hypothyroidism in XB130 Knockout Mice. *Cells* 11. PMID: 35326426; DOI: 10.3390/cells11060975; PMCID: PMC8947158. https://pubmed.ncbi.nlm.nih.gov/35326426/
* **tanga-2019-ptprz-afap1l2-oligodendrocyte**: Tanga N, Kuboyama K, Kishimoto A, et al. (2019). The PTN-PTPRZ signal activates the AFAP1L2-dependent PI3K-AKT pathway for oligodendrocyte differentiation: Targeted inactivation of PTPRZ activity in mice. *Glia* 67:967-984. PMID: 30667096; DOI: 10.1002/glia.23583. https://pubmed.ncbi.nlm.nih.gov/30667096/
* **toba-2015-xb130-airway-repair**: Toba H, Wang Y, Bai X, et al. (2015). XB130 promotes bronchioalveolar stem cell and Club cell proliferation in airway epithelial repair and regeneration. *Oncotarget* 6:30803-17. PMID: 26360608; DOI: 10.18632/oncotarget.5062; PMCID: PMC4741569. https://pubmed.ncbi.nlm.nih.gov/26360608/
* **toba-2016-xb130-lps-lung-injury**: Toba H, Tomankova T, Wang Y, et al. (2016). XB130 deficiency enhances lipopolysaccharide-induced septic response and acute lung injury. *Oncotarget* 7:25420-31. PMID: 27029000; DOI: 10.18632/oncotarget.8326; PMCID: PMC5041914. https://pubmed.ncbi.nlm.nih.gov/27029000/
* **zhao-2014-xb130-tracheal-repair**: Zhao J, Wang Y, Wakeham A, et al. (2014). XB130 deficiency affects tracheal epithelial differentiation during airway repair. *PLoS One* 9:e108952. PMID: 25272040; DOI: 10.1371/journal.pone.0108952; PMCID: PMC4182764. https://pubmed.ncbi.nlm.nih.gov/25272040/
* **wu-2015-xb130-nnk-migration**: Wu Q, Nadesalingam J, Moodley S, et al. (2015). XB130 translocation to microfilamentous structures mediates NNK-induced migration of human bronchial epithelial cells. *Oncotarget* 6:18050-65. PMID: 25980441; DOI: 10.18632/oncotarget.3777; PMCID: PMC4627235. https://pubmed.ncbi.nlm.nih.gov/25980441/
* **ma-2024-afap1l2-src-fundc1**: Ma Z, Chen W, Liu Y, et al. (2024). Artesunate Sensitizes human hepatocellular carcinoma to sorafenib via exacerbating AFAP1L2-SRC-FUNDC1 axis-dependent mitophagy. *Autophagy* 20:541-556. PMID: 37733919; DOI: 10.1080/15548627.2023.2261758; PMCID: PMC10936616. https://pubmed.ncbi.nlm.nih.gov/37733919/
* **iyama-2017-afap1l2-ret-fusion**: Iyama K, Matsuse M, Mitsutake N, et al. (2017). Identification of Three Novel Fusion Oncogenes, SQSTM1/NTRK3, AFAP1L2/RET, and PPFIBP2/RET, in Thyroid Cancers of Young Patients in Fukushima. *Thyroid* 27:811-818. PMID: 28351223; DOI: 10.1089/thy.2016.0673. https://pubmed.ncbi.nlm.nih.gov/28351223/
* **emaduddin-2008-odin-src-target**: Emaduddin M, Edelmann MJ, Kessler BM, et al. (2008). Odin (ANKS1A) is a Src family kinase target in colorectal cancer cells. *Cell Commun Signal* 6:7. PMID: 18844995; DOI: 10.1186/1478-811X-6-7; PMCID: PMC2584000. https://pubmed.ncbi.nlm.nih.gov/18844995/
* **snyder-2011-afap1l1-cortactin**: Snyder BN, Cho Y, Qian Y, et al. (2011). AFAP1L1 is a novel adaptor protein of the AFAP family that interacts with cortactin and localizes to invadosomes. *Eur J Cell Biol* 90:376-89. PMID: 21333378; DOI: 10.1016/j.ejcb.2010.11.016; PMCID: PMC3085893. https://pubmed.ncbi.nlm.nih.gov/21333378/
* **takeshita-2013-xb130-mirna**: Takeshita H, Shiozaki A, Bai XH, et al. (2013). XB130, a new adaptor protein, regulates expression of tumor suppressive microRNAs in cancer cells. *PLoS One* 8:e59057. PMID: 23527086; DOI: 10.1371/journal.pone.0059057; PMCID: PMC3602428. https://pubmed.ncbi.nlm.nih.gov/23527086/


## Citations

1. _metadata.json
2. bai-2014-xb130-review-abstract.md
3. bai-2014-xb130-review-fulltext.txt
4. bai-2014-xb130-review-summary.md
5. cho-2022-xb130-goiter-abstract.md
6. cho-2022-xb130-goiter-summary.md
7. emaduddin-2008-odin-src-target-abstract.md
8. emaduddin-2008-odin-src-target-fulltext.txt
9. emaduddin-2008-odin-src-target-summary.md
10. iyama-2017-afap1l2-ret-fusion-abstract.md
11. iyama-2017-afap1l2-ret-fusion-summary.md
12. lodyga-2009-xb130-retptc-pi3k-abstract.md
13. lodyga-2009-xb130-retptc-pi3k-summary.md
14. lodyga-2010-xb130-lamellipodia-abstract.md
15. lodyga-2010-xb130-lamellipodia-summary.md
16. ma-2024-afap1l2-src-fundc1-abstract.md
17. ma-2024-afap1l2-src-fundc1-summary.md
18. moodley-2015-xb130-tks5-src-abstract.md
19. moodley-2015-xb130-tks5-src-fulltext.txt
20. moodley-2015-xb130-tks5-src-summary.md
21. moodley-2016-xb130-tks5-migration-abstract.md
22. moodley-2016-xb130-tks5-migration-fulltext.txt
23. moodley-2016-xb130-tks5-migration-summary.md
24. pdb-2cof-entry.json
25. pdb-2cof-summary.md
26. shiozaki-2011-xb130-thyroid-tumor-abstract.md
27. shiozaki-2011-xb130-thyroid-tumor-summary.md
28. shiozaki-2012-xb130-akt-downstream-abstract.md
29. shiozaki-2012-xb130-akt-downstream-fulltext.txt
30. shiozaki-2012-xb130-akt-downstream-summary.md
31. snyder-2011-afap1l1-cortactin-abstract.md
32. snyder-2011-afap1l1-cortactin-fulltext.txt
33. snyder-2011-afap1l1-cortactin-summary.md
34. sugihara-2022-xb130-ko-thyroid-transcriptome-abstract.md
35. sugihara-2022-xb130-ko-thyroid-transcriptome-fulltext.txt
36. sugihara-2022-xb130-ko-thyroid-transcriptome-summary.md
37. takeshita-2013-xb130-mirna-abstract.md
38. takeshita-2013-xb130-mirna-fulltext.txt
39. takeshita-2013-xb130-mirna-summary.md
40. tanga-2019-ptprz-afap1l2-oligodendrocyte-abstract.md
41. tanga-2019-ptprz-afap1l2-oligodendrocyte-summary.md
42. toba-2015-xb130-airway-repair-abstract.md
43. toba-2015-xb130-airway-repair-fulltext.txt
44. toba-2015-xb130-airway-repair-summary.md
45. toba-2016-xb130-lps-lung-injury-abstract.md
46. toba-2016-xb130-lps-lung-injury-fulltext.txt
47. toba-2016-xb130-lps-lung-injury-summary.md
48. uniprot-A0A9L0RQI4-entry.txt
49. uniprot-A0A9L0RQI4-summary.md
50. uniprot-Q8N4X5-entry.txt
51. uniprot-Q8N4X5-summary.md
52. wade-2009-horse-genome-abstract.md
53. wade-2009-horse-genome-summary.md
54. wang-2021-xb130-ko-hypothyroidism-abstract.md
55. wang-2021-xb130-ko-hypothyroidism-summary.md
56. wang-2022-xb130-folliculogenesis-abstract.md
57. wang-2022-xb130-folliculogenesis-summary.md
58. wu-2015-xb130-nnk-migration-abstract.md
59. wu-2015-xb130-nnk-migration-fulltext.txt
60. wu-2015-xb130-nnk-migration-summary.md
61. xu-2007-xb130-adaptor-abstract.md
62. xu-2007-xb130-adaptor-summary.md
63. yamanaka-2012-pi3kap-igf-abstract.md
64. yamanaka-2012-pi3kap-igf-summary.md
65. yamanaka-2016-pi3kap-actin-crosslink-abstract.md
66. yamanaka-2016-pi3kap-actin-crosslink-fulltext.txt
67. yamanaka-2016-pi3kap-actin-crosslink-summary.md
68. zhao-2014-xb130-tracheal-repair-abstract.md
69. zhao-2014-xb130-tracheal-repair-fulltext.txt
70. zhao-2014-xb130-tracheal-repair-summary.md