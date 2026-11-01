---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:51:02.327191'
end_time: '2026-10-26T00:58:58.028456'
duration_seconds: 475.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: RASGEF1A
  gene_symbol: RASGEF1A
  uniprot_accession: A0A9L0J8J4
  protein_description: 'SubName: Full=RasGEF domain family member 1A {ECO:0000313|Ensembl:ENSEASP00005049616.1};'
  gene_info: Name=RASGEF1A {ECO:0000313|Ensembl:ENSEASP00005049616.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Not specified in UniProt
  protein_domains: Ras-like_GEF. (IPR008937); Ras-like_Gua-exchang_fac_N. (IPR000651);
    Ras_GEF_dom_sf. (IPR023578); RASGEF_cat_dom. (IPR001895); RASGEF_cat_dom_sf. (IPR036964)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3303
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 47
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0J8J4
- **Protein Description:** SubName: Full=RasGEF domain family member 1A {ECO:0000313|Ensembl:ENSEASP00005049616.1};
- **Gene Information:** Name=RASGEF1A {ECO:0000313|Ensembl:ENSEASP00005049616.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ras-like_GEF. (IPR008937); Ras-like_Gua-exchang_fac_N. (IPR000651); Ras_GEF_dom_sf. (IPR023578); RASGEF_cat_dom. (IPR001895); RASGEF_cat_dom_sf. (IPR036964)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RASGEF1A" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RASGEF1A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RASGEF1A** (gene ID: RASGEF1A, UniProt: A0A9L0J8J4) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RASGEF1A (Ras-GEF domain-containing family member 1A) in *Equus asinus* (UniProt A0A9L0J8J4): A Functional Annotation Review

## 1. Introduction and Summary

UniProt A0A9L0J8J4 is an unreviewed, computationally predicted donkey protein of 516 amino acids. Ensembl annotation names it RASGEF1A (gene ENSEASG00005006902 on donkey chromosome 2), and the protein carries an N-terminal Ras-GEF (RasGEF_N/REM) domain at residues 76–205 and a CDC25-homology Ras-GEF catalytic domain at residues 249–496 [uniprot-A0A9L0J8J4-record]. The sequence comes from the donkey reference genome project [wang-2020-donkey-genome-abstract]. No experimental study of the donkey protein exists, so its function has to be inferred from its orthologue in human (Q8N9B8) and other mammals. That inference is strong. The gene symbol is unambiguous: it is not RASSF1A, which literature searches often return. The donkey and human proteins are 96% identical, and the catalytic domain is essentially invariant (see Section 2).

The best biochemical evidence says that RASGEF1A is a guanine nucleotide exchange factor (GEF) with high selectivity for the small GTPase Rap2. With purified proteins, Yaman and colleagues showed that RasGEF1A and its paralog RasGEF1B catalyse GDP/GTP exchange on Rap2 but not on Rap1 or on Ras-subfamily GTPases. They traced this selectivity to Phe39 in the switch I region of Rap2 [yaman-2009-rasgef1-rap2-abstract]. An earlier study from a cancer-genomics group reported exchange activity toward K-, H- and N-Ras in vitro. That study also linked RASGEF1A overexpression to proliferation and motility of intrahepatic cholangiocarcinoma cells and to migration of COS7 cells [ura-2006-rasgef1a-cholangiocarcinoma-abstract]. UniProt's curated human entry records both findings, describing RASGEF1A as a GEF "with specificity for RAP2A, KRAS, HRAS, and NRAS (in vitro)" that "plays a role in cell migration" [uniprot-Q8N9B8-record]. The most parsimonious model is that RASGEF1A turns on Rap2 signalling. Through Rap2, it could feed into pathways that control the actin cytoskeleton, cell adhesion and migration, neurite and synapse remodelling, and Hippo/YAP mechanotransduction [meng-2018-rap2-hippo-abstract; zhu-2005-rap2-jnk-ampar-abstract; kawabe-2010-nedd4-rap2a-tnik-abstract].

Direct evidence on where RASGEF1A acts in the cell is sparse. Database annotations place it at the plasma membrane (phylogenetic inference) and in the cytosol (Reactome) [uniprot-Q8N9B8-record]. The paralog RasGEF1b localizes to early endosomes [andrade-2010-rasgef1b-endosome-abstract]. Human expression data point mainly to the central nervous system (brain and spinal cord), with additional expression in some leukocytes and tumours [uniprot-Q8N9B8-record; celesnik-2024-rasgef1a-pbmc-isoform-fulltext].

## 2. Identity, Orthology and Domain Architecture

The donkey entry was checked against the human reference protein before any literature was used. A global Needleman–Wunsch alignment (BLOSUM62) of A0A9L0J8J4 against human Q8N9B8 (481 aa) gave 462 identical positions, 96% of the human length (`alignment_donkey_vs_human.txt`). The main difference is a 36-residue N-terminal extension in the donkey model (MFLEPQTRGF…). This is most likely an alternative or mispredicted upstream start codon in the automated Ensembl gene model, because the human protein begins at the equivalent of donkey Met37 (MPQTSVVFSS…). Over the C-terminal half, which spans the CDC25-homology catalytic domain, the alignment shows almost uninterrupted identity. The donkey domain coordinates are therefore those of human RASGEF1A shifted by 36 residues. The UniProt cross-references support this assignment: PANTHER subfamily PTHR23113:SF172 ("RAS-GEF DOMAIN-CONTAINING FAMILY MEMBER 1A"), Pfam RasGEF_N (PF00618) and RasGEF (PF00617), SMART SM00229/SM00147, and PROSITE PS50212/PS50009 [uniprot-A0A9L0J8J4-record]. The organism and symbol therefore agree, and the human and rodent literature on RASGEF1A applies to this protein.

RASGEF1A belongs to the small RasGEF1 family (RasGEF1A, RasGEF1B, RasGEF1C). These are compact proteins built from just the two core modules of the CDC25/SOS-type exchange factors: the N-terminal REM-like RasGEF_N domain and the catalytic CDC25-homology domain. They lack the extra regulatory modules (DH/PH, PDZ, cyclic-nucleotide-binding, Ras-association domains) that most Ras/Rap GEFs carry [yaman-2009-rasgef1-rap2-abstract; bos-2007-gefs-gaps-review-abstract]. The family is conserved from nematodes to vertebrates [epting-2007-rasgef1b-zebrafish-abstract]. A eukaryote-wide phylogenetic classification of Ras regulators puts its origin earlier still. Díez and colleagues define a RASGEF1 subfamily with one gene in the choanoflagellate *Monosiga*, Ciona, sea urchin, insects and nematodes, two in fish and *Xenopus*, and three in birds/reptiles and mammals. They find none in fungi or slime moulds [diez-2011-ras-switch-evolution-fulltext]. RASGEF1 is therefore an ancient holozoan GEF lineage that expanded into three paralogs (RASGEF1A, -1B, -1C) during vertebrate evolution. The donkey gene is the RASGEF1A member of this triplet. Because the family stayed so compact over that long period, its core GEF function was probably fixed early, while the paralogs may since have diverged in regulation and expression.

## 3. Catalytic Mechanism of the CDC25-Homology Domain

The CDC25-homology domain is a well-understood catalytic module. The crystal structure of H-Ras bound to the Sos catalytic region showed how this domain works. A helical hairpin from the GEF inserts into the GTPase and displaces switch I, which opens the nucleotide-binding pocket. Side chains from that helix, together with a distorted switch II, then destabilize binding of the phosphates and the Mg2+ ion. The guanine base and ribose binding sites stay intact, so the nucleotide can leave and be replaced by the more abundant cellular GTP [boriacksjodin-1998-ras-sos-structure-abstract]. GEFs thus speed up nucleotide release rather than "loading" GTP directly. Because cytosolic GTP greatly exceeds GDP, the net result is activation of the GTPase [bos-2007-gefs-gaps-review-abstract].

A CDC25-homology GEF picks its substrate largely through how its helical hairpin and nearby surfaces contact the switch I region of the GTPase. The structure of the Ral-specific Cdc25 domain from RalGPS1a illustrates this. Its bowl-shaped fold matches those of SOS and RasGRF1, but the conformation of the hairpin and the electrostatics of the switch I interface differ, which explains its Ral selectivity [peng-2011-ralgps1a-cdc25-structure-abstract]. The RasGEF1 family fits this principle. The specificity of RasGEF1A/B for Rap2 over Rap1 depends on one switch I residue, Phe39 in Rap2 (Ser39 in Rap1). An S39F mutation in Rap1 was enough to make it a RasGEF1B substrate [yaman-2009-rasgef1-rap2-abstract]. The catalytic domain is conserved almost perfectly between donkey and human, so the donkey protein almost certainly keeps this Rap2-selective catalytic surface.

## 4. Substrate Specificity: Rap2 versus Classical Ras

The two primary biochemical studies of RASGEF1A disagree in part. Ura et al. found RASGEF1A while profiling genes that are commonly overexpressed in intrahepatic cholangiocarcinoma. They reported that RASGEF1A protein had exchange activity toward K-RAS, H-RAS and N-RAS in vitro and that exogenous expression raised cellular Ras activity [ura-2006-rasgef1a-cholangiocarcinoma-abstract]. Yaman et al., working in Alfred Wittinghofer's laboratory, later tested purified RasGEF1A and RasGEF1B systematically against Ras-family proteins. They found the two GEFs to be "very specific exchange factors for Rap2". They did not act on Rap1 or on other members of the Ras subfamily [yaman-2009-rasgef1-rap2-abstract]. The authors noted that this made RasGEF1A/B the first GEFs specific for Rap2, a GTPase already implicated in cell adhesion, cell morphology and synapse modulation [yaman-2009-rasgef1-rap2-abstract].

The Yaman study used purified components, tested a wide panel of GTPases, and confirmed its result mechanistically by reciprocal mutagenesis. Its conclusion of Rap2 selectivity is therefore the stronger one. The Ras activity reported by Ura et al. might reflect weaker, non-selective activity under their assay conditions, or indirect effects in cells. Overexpressed GEFs can activate Ras by cross-talk, for example through Rap2 effectors that feed into MAPK or cytoskeletal pathways. Curated resources record both claims. UniProt lists RAP2A, KRAS, HRAS and NRAS as in-vitro substrates, and GO has an IDA annotation to "guanyl-nucleotide exchange factor activity" from both papers [uniprot-Q8N9B8-record]. For functional annotation of the donkey orthologue, the most defensible statements are "guanyl-nucleotide exchange factor activity" and, more specifically, Rap2-directed exchange. Ras-subfamily activity should be treated as possible but contested. RasGEF1b, the paralog, has also been reported to associate with and activate Ras in cells [andrade-2010-rasgef1b-endosome-abstract]. This shows that cell-based assays in this family can give Ras activation even where purified-protein assays point to Rap2. The most recent cell-based study makes this tension sharper. In hepatocytes co-overexpressing the TAF2 coactivator and MYC, RASGEF1A was the most strongly induced MYC-bound target gene. Cellular Ras-GTP, measured by Raf-RBD pull-down, was elevated, and siRNA knockdown of RASGEF1A lowered active Ras, MEK/ERK phosphorylation and cell viability. The authors note explicitly that this contrasts with the in vitro Rap2 specificity, and suggest that RASGEF1A "might promote Ras activation as well" [raha-2026-taf2-myc-hcc-fulltext]. That study did not assay Rap2-GTP and did not test whether the Ras effect is direct. Two genetic loss-of-function studies, Ura et al. and Raha et al., now agree that RASGEF1A supports Ras–ERK output in transformed epithelial cells. Whether that reflects direct but weak Ras exchange, which overexpression amplifies, or indirect coupling through Rap2 is still unresolved.

## 5. Signalling Pathways Downstream of RASGEF1A–Rap2

RASGEF1A appears to have no catalytic or scaffolding function apart from GEF activity. Its pathway roles are therefore those of active, GTP-bound Rap2. The most direct cell-based evidence linking the RasGEF1 family to a defined Rap2 effector comes from endothelial cells. Pannekoek and colleagues showed that Rap1 and Rap2 control endothelial barrier resistance in opposite directions: Rap1 tightens junctions and Rap2 loosens them. siRNA depletion of the RasGEF1 GEFs (RasGEF1A, RasGEF1B and RasGEF1C were each targeted) mimicked Rap2 depletion and increased barrier resistance, as did depletion of the Ste20-family kinase MAP4K4 but not TNIK or MINK. They concluded that "the RasGEF1 family and MAP4K4 therefore form a Rap2 specific signalling route" [pannekoek-2013-rap1-rap2-endothelial-barrier-fulltext]. In HUVECs the effect came mainly from RasGEF1C, so RASGEF1A contributed less there, consistent with paralog specialization by tissue. This RasGEF1→Rap2→MAP4K4 axis is the best-supported pathway template for RASGEF1A. It agrees with the three broader Rap2 output pathways described below, none of which has yet been shown to depend on RASGEF1A specifically.

The first is Hippo-pathway mechanotransduction. Meng et al. showed that RAP2 is activated when extracellular matrix stiffness is low. GTP-bound RAP2 then binds and stimulates MAP4K4, MAP4K6, MAP4K7 and the RhoGAP ARHGAP29. This activates LATS1/2 and inhibits the transcriptional co-activators YAP and TAZ. In that study the upstream GEFs were PDZGEF1/2 (RAPGEF2/6), which respond to PLCγ1-controlled lipid signals [meng-2018-rap2-hippo-abstract]. RASGEF1A could be another way to feed GTP-loaded Rap2 into this module.

The second is neuronal morphogenesis and synaptic plasticity. In hippocampal neurons, Rap2 activated by NR2A-containing NMDA receptors depresses AMPA-receptor transmission through JNK and drives synaptic removal of AMPA receptors during depotentiation [zhu-2005-rap2-jnk-ampar-abstract]. Rap2A also forms a complex with the ubiquitin ligase Nedd4-1 and the kinase TNIK. Rap2A signals through TNIK-family kinases (TNIK, MINK1) to restrain dendrite growth, and Nedd4-1-mediated ubiquitination of Rap2A relieves this restraint [kawabe-2010-nedd4-rap2a-tnik-abstract]. Human RASGEF1A is expressed in brain and spinal cord [uniprot-Q8N9B8-record], and mice lacking the paralog RasGEF1b show behavioural and neurochemical changes [fernandes-2024-rasgef1b-mice-abstract]. Together these make neuronal Rap2 regulation an attractive candidate physiological role for RASGEF1A.

The third is cell migration and adhesion. Ectopic RASGEF1A increased COS7 cell motility in Transwell and wound-healing assays, and its knockdown slowed cholangiocarcinoma cell growth [ura-2006-rasgef1a-cholangiocarcinoma-abstract]. This is the basis for the GO annotation "cell migration" [uniprot-Q8N9B8-record]. It fits the established roles of Rap2 in cell adhesion and morphology [yaman-2009-rasgef1-rap2-abstract]. The GO annotation "positive regulation of Ras protein signal transduction", contributed by FlyBase from the Ura study [uniprot-Q8N9B8-record], should be read in light of the specificity question discussed in Section 4.

More broadly, RASGEF1A sits in the regulatory layer of the Ras superfamily. In this layer, GEFs and GAPs are controlled in time and space and set the activation state of their GTPases [bos-2007-gefs-gaps-review-abstract]. Deregulated GEF expression is a recurring way that small GTPase signalling is perturbed in cancer [vigil-2010-gefs-gaps-cancer-abstract].

## 6. Subcellular Localization and Tissue Expression

No study has determined where endogenous RASGEF1A is located in the cell. The donkey entry inherits a "plasma membrane" GO term from PANTHER phylogenetic inference [uniprot-A0A9L0J8J4-record]. The human entry also carries "cytosol" from Reactome curation and the same IBA-derived "plasma membrane" term [uniprot-Q8N9B8-record]. The protein has no predicted transmembrane segment, lipidation motif or membrane-targeting domain. Any membrane association is therefore probably indirect, through binding to membrane-anchored Rap2, which is prenylated, or to unidentified partners. The closest paralog gives a useful precedent: ectopic RasGEF1b fractionated with heavy membranes and colocalized with early endosome markers in HEK293T cells [andrade-2010-rasgef1b-endosome-abstract]. RASGEF1A might likewise be a cytosolic protein that cycles onto endomembranes or the plasma membrane wherever its Rap2 substrate sits. This is still a hypothesis.

At the tissue level, UniProt reports that human RASGEF1A is detected in brain and spinal cord and is highly expressed in many intrahepatic cholangiocarcinoma biopsies [uniprot-Q8N9B8-record; ura-2006-rasgef1a-cholangiocarcinoma-abstract]. Single-cell data cited by Čelešnik et al. detect RASGEF1A mRNA in T cells, NK cells and macrophages. In circulating mononuclear leukocytes the predominant Rap2 isoform is Rap2C, a possible partner [celesnik-2024-rasgef1a-pbmc-isoform-fulltext]. No expression data exist for the donkey. Given the high conservation, a similar neural-enriched pattern is expected.

## 7. Genetic and Disease Associations (Context Only)

RASGEF1A lies on chromosome 10q11.21 in humans, immediately downstream of RET. Hirschsprung disease GWAS consistently find a top signal in the RET–CSGALNACT2–RASGEF1A interval. A Korean GWAS replicated this region at genome-wide significance and noted that CSGALNACT2 and RASGEF1A are differentially expressed between colon and small intestine "although the functions of these genes have not been adequately characterized" [kim-2014-hirschsprung-gwas-fulltext]. The association is widely attributed to RET enhancer variation, so it does not show that RASGEF1A itself is involved in enteric nervous system development. In oncology, high RASGEF1A expression predicts poor survival in cytogenetically normal AML, and promoter hypermethylation predicts favourable outcome [he-2023-rasgef1a-aml-abstract]. Reduced levels of one RASGEF1A transcript isoform in PBMCs are associated with breast cancer, ctDNA levels and Ki-67 [celesnik-2024-rasgef1a-pbmc-isoform-abstract]. These are correlative biomarker studies. They say little about molecular mechanism, but they do show that RASGEF1A expression is variable and epigenetically regulated. One transcriptional input has been mapped directly. MYC occupies the RASGEF1A promoter, and that occupancy rises sharply when TAF2 is co-expressed. Rasgef1a is also induced in mouse liver tumours driven by TAF2 plus MYC [raha-2026-taf2-myc-hcc-fulltext]. The main regulation of this compact GEF may therefore be at the level of its expression. None of these associations has been studied in equids.

## 8. Synthesis for Functional Annotation of the Donkey Protein

Taking the evidence together, A0A9L0J8J4 is best annotated as the donkey orthologue of RASGEF1A. It is a cytosolic, peripherally membrane-associated guanine nucleotide exchange factor of the CDC25/SOS family. Its main molecular function is to catalyse GDP release from the small GTPase Rap2 (Rap2A/B/C), and so to promote formation of Rap2-GTP. Substrate selection depends on Rap2 switch I residue Phe39. Classical Ras isoforms are possible secondary substrates, but the evidence there is contested. Functionally, RASGEF1A operates in Rap2-dependent signalling, which controls cytoskeletal organization, cell adhesion and migration, neuronal dendrite and synapse remodelling (via TNIK/MINK and JNK), and Hippo/YAP mechanoresponses (via MAP4Ks and LATS1/2). The best experimentally supported cellular roles are cell migration, support of Ras–MEK–ERK output in transformed epithelial cells, and, together with its paralogs, a Rap2–MAP4K4 route that controls endothelial junctions. The evidence for the donkey protein is entirely inferred, from sequence orthology (96% identity), domain conservation and a phylogenetic placement within the vertebrate RASGEF1 paralog triplet, but these are strong grounds. The experimental support comes from one purified-protein biochemical study [yaman-2009-rasgef1-rap2-abstract], two cell-based gain- and loss-of-function studies in human cancer cells [ura-2006-rasgef1a-cholangiocarcinoma-abstract; raha-2026-taf2-myc-hcc-fulltext] and one family-level siRNA study in endothelial cells [pannekoek-2013-rap1-rap2-endothelial-barrier-fulltext], with paralog and pathway-level data adding context.

## Open Questions

Several important questions remain open. The most basic is the true substrate profile of RASGEF1A in cells. The purified-protein data (Rap2-specific) and the earlier data (K/H/N-Ras) have never been reconciled, and a side-by-side kinetic analysis with full-length protein plus cellular Rap2-GTP and Ras-GTP pull-down assays would settle the question. Nobody has identified the upstream signals that regulate RASGEF1A, whether receptor pathways, second messengers, phosphorylation or binding partners. Its compact two-domain architecture makes it unclear whether it is constitutively active and controlled mainly at the level of expression or localization. No structure exists of RASGEF1A, alone or with Rap2. The AlphaFold model (AlphaFoldDB A0A9L0J8J4) could be used to model the Rap2 interface around Phe39, and to see whether the RasGEF_N domain has an allosteric role analogous to the REM domain of SOS. Endogenous subcellular localization has not been determined. Testing whether RASGEF1A, like RasGEF1b, targets endosomes would be informative. In vivo loss-of-function data are lacking for RASGEF1A in any mammal. A knockout mouse phenotyped for neural, enteric-nervous-system and immune traits would show whether it contributes to the neuronal Rap2–TNIK/JNK pathways or to Hippo mechanotransduction. The donkey gene model itself needs checking: the 36-residue N-terminal extension relative to human should be validated against equine RNA-seq or transcript evidence to establish the correct start codon. Finally, it is unknown whether RASGEF1A is functionally redundant with RASGEF1B and RASGEF1C, which also activate Rap2, and how the three paralogs divide their tissue expression. The endothelial study, in which RasGEF1C dominated, suggests they are not simply redundant [pannekoek-2013-rap1-rap2-endothelial-barrier-fulltext]. A further useful experiment would measure Rap2-GTP alongside Ras-GTP after RASGEF1A knockdown in the MYC/TAF2 hepatocyte model [raha-2026-taf2-myc-hcc-fulltext]. That would show directly whether the reported ERK dependence runs through Rap2.

## References

- **[uniprot-A0A9L0J8J4-record]** UniProt Consortium. UniProtKB entry A0A9L0J8J4 (A0A9L0J8J4_EQUAS), RasGEF domain family member 1A, *Equus asinus*; unreviewed (TrEMBL), entry version 15. https://rest.uniprot.org/uniprotkb/A0A9L0J8J4.txt
- **[uniprot-Q8N9B8-record]** UniProt Consortium. UniProtKB/Swiss-Prot entry Q8N9B8, Ras-GEF domain-containing family member 1A, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q8N9B8.txt
- **[yaman-2009-rasgef1-rap2]** Yaman E, Gasper R, Koerner C, Wittinghofer A, Tazebay UH. RasGEF1A and RasGEF1B are guanine nucleotide exchange factors that discriminate between Rap GTP-binding proteins and mediate Rap2-specific nucleotide exchange. *FEBS J.* 2009;276(16):4607–4616. PMID: 19645719. DOI: 10.1111/j.1742-4658.2009.07166.x
- **[ura-2006-rasgef1a-cholangiocarcinoma]** Ura K, Obama K, Satoh S, Sakai Y, Nakamura Y, Furukawa Y. Enhanced RASGEF1A expression is involved in the growth and migration of intrahepatic cholangiocarcinoma. *Clin Cancer Res.* 2006;12(22):6611–6616. PMID: 17121879. DOI: 10.1158/1078-0432.CCR-06-0783
- **[wang-2020-donkey-genome]** Wang C, Li H, Guo Y, et al. Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun.* 2020;11(1):6014. PMID: 33293529. PMCID: PMC7723042. DOI: 10.1038/s41467-020-19813-7
- **[boriacksjodin-1998-ras-sos-structure]** Boriack-Sjodin PA, Margarit SM, Bar-Sagi D, Kuriyan J. The structural basis of the activation of Ras by Sos. *Nature.* 1998;394(6691):337–343. PMID: 9690470. DOI: 10.1038/28548
- **[peng-2011-ralgps1a-cdc25-structure]** Peng W, Xu J, Guan X, Sun Y, Zhang XC, Li X, Rao Z. Structural study of the Cdc25 domain from Ral-specific guanine-nucleotide exchange factor RalGPS1a. *Protein Cell.* 2011;2(4):308–319. PMID: 21494904. PMCID: PMC4875206. DOI: 10.1007/s13238-011-1036-z
- **[bos-2007-gefs-gaps-review]** Bos JL, Rehmann H, Wittinghofer A. GEFs and GAPs: critical elements in the control of small G proteins. *Cell.* 2007;129(5):865–877. PMID: 17540168. DOI: 10.1016/j.cell.2007.05.018
- **[vigil-2010-gefs-gaps-cancer]** Vigil D, Cherfils J, Rossman KL, Der CJ. Ras superfamily GEFs and GAPs: validated and tractable targets for cancer therapy? *Nat Rev Cancer.* 2010;10(12):842–857. PMID: 21102635. PMCID: PMC3124093. DOI: 10.1038/nrc2960
- **[andrade-2010-rasgef1b-endosome]** Andrade WA, Silva AM, Alves VS, et al. Early endosome localization and activity of RasGEF1b, a toll-like receptor-inducible Ras guanine-nucleotide exchange factor. *Genes Immun.* 2010;11(6):447–457. PMID: 20090772. DOI: 10.1038/gene.2009.107
- **[epting-2007-rasgef1b-zebrafish]** Epting D, Vorwerk S, Hageman A, Meyer D. Expression of rasgef1b in zebrafish. *Gene Expr Patterns.* 2007;7(4):389–395. PMID: 17239665. DOI: 10.1016/j.modgep.2006.11.010
- **[fernandes-2024-rasgef1b-mice]** Fernandes HB, Oliveira BDS, Machado CA, et al. Behavioral, neurochemical and neuroimmune features of RasGEF1b deficient mice. *Prog Neuropsychopharmacol Biol Psychiatry.* 2024;129:110908. PMID: 38048936. DOI: 10.1016/j.pnpbp.2023.110908
- **[meng-2018-rap2-hippo]** Meng Z, Qiu Y, Lin KC, et al. RAP2 mediates mechanoresponses of the Hippo pathway. *Nature.* 2018;560(7720):655–660. PMID: 30135582. PMCID: PMC6128698. DOI: 10.1038/s41586-018-0444-0
- **[zhu-2005-rap2-jnk-ampar]** Zhu Y, Pak D, Qin Y, et al. Rap2-JNK removes synaptic AMPA receptors during depotentiation. *Neuron.* 2005;46(6):905–916. PMID: 15953419. DOI: 10.1016/j.neuron.2005.04.037
- **[kawabe-2010-nedd4-rap2a-tnik]** Kawabe H, Neeb A, Dimova K, et al. Regulation of Rap2A by the ubiquitin ligase Nedd4-1 controls neurite development. *Neuron.* 2010;65(3):358–372. PMID: 20159449. PMCID: PMC2825371. DOI: 10.1016/j.neuron.2010.01.007
- **[kim-2014-hirschsprung-gwas]** Kim JH, Cheong HS, Sul JH, et al. A genome-wide association study identifies potential susceptibility loci for Hirschsprung disease. *PLoS One.* 2014;9(10):e110292. PMID: 25310821. PMCID: PMC4195606. DOI: 10.1371/journal.pone.0110292
- **[pannekoek-2013-rap1-rap2-endothelial-barrier]** Pannekoek WJ, Linnemann JR, Brouwer PM, Bos JL, Rehmann H. Rap1 and Rap2 antagonistically control endothelial barrier resistance. *PLoS One.* 2013;8(2):e57903. PMID: 23469100. PMCID: PMC3585282. DOI: 10.1371/journal.pone.0057903
- **[diez-2011-ras-switch-evolution]** Díez D, Sánchez-Jiménez F, Ranea JA. Evolutionary expansion of the Ras switch regulatory module in eukaryotes. *Nucleic Acids Res.* 2011;39(13):5526–5537. PMID: 21447561. PMCID: PMC3141262. DOI: 10.1093/nar/gkr154
- **[raha-2026-taf2-myc-hcc]** Raha S, Zhang Q, Farrar D, et al. Molecular mechanism of augmentation of oncogenic activity of MYC by TAF2 in HCC. *J Biol Chem.* 2026;302(11):113581. PMID: 42759661. PMCID: PMC13682000. DOI: 10.1016/j.jbc.2026.113581
- **[he-2023-rasgef1a-aml]** He X, Zhang W, Fu W, et al. The prognostic value of RASGEF1A RNA expression and DNA methylation in cytogenetically normal acute myeloid leukemia. *Cancer Biomark.* 2023;36(2):103–116. PMID: 36404533. PMCID: PMC12412801. DOI: 10.3233/CBM-210407
- **[celesnik-2024-rasgef1a-pbmc-isoform]** Čelešnik H, Gorenjak M, Krušič M, et al. Isoform-Level Transcriptome Analysis of Peripheral Blood Mononuclear Cells from Breast Cancer Patients Identifies a Disease-Associated RASGEF1A Isoform. *Cancers (Basel).* 2024;16(18):3171. PMID: 39335143. PMCID: PMC11429621. DOI: 10.3390/cancers16183171


## Citations

1. andrade-2010-rasgef1b-endosome-abstract.md
2. andrade-2010-rasgef1b-endosome-summary.md
3. boriacksjodin-1998-ras-sos-structure-abstract.md
4. boriacksjodin-1998-ras-sos-structure-summary.md
5. bos-2007-gefs-gaps-review-abstract.md
6. bos-2007-gefs-gaps-review-summary.md
7. celesnik-2024-rasgef1a-pbmc-isoform-abstract.md
8. celesnik-2024-rasgef1a-pbmc-isoform-fulltext.txt
9. celesnik-2024-rasgef1a-pbmc-isoform-summary.md
10. diez-2011-ras-switch-evolution-abstract.md
11. diez-2011-ras-switch-evolution-fulltext.txt
12. diez-2011-ras-switch-evolution-summary.md
13. epting-2007-rasgef1b-zebrafish-abstract.md
14. epting-2007-rasgef1b-zebrafish-summary.md
15. fernandes-2024-rasgef1b-mice-abstract.md
16. fernandes-2024-rasgef1b-mice-summary.md
17. he-2023-rasgef1a-aml-abstract.md
18. he-2023-rasgef1a-aml-summary.md
19. kawabe-2010-nedd4-rap2a-tnik-abstract.md
20. kawabe-2010-nedd4-rap2a-tnik-summary.md
21. kim-2014-hirschsprung-gwas-abstract.md
22. kim-2014-hirschsprung-gwas-fulltext.txt
23. kim-2014-hirschsprung-gwas-summary.md
24. meng-2018-rap2-hippo-abstract.md
25. meng-2018-rap2-hippo-summary.md
26. pannekoek-2013-rap1-rap2-endothelial-barrier-abstract.md
27. pannekoek-2013-rap1-rap2-endothelial-barrier-fulltext.txt
28. pannekoek-2013-rap1-rap2-endothelial-barrier-summary.md
29. peng-2011-ralgps1a-cdc25-structure-abstract.md
30. peng-2011-ralgps1a-cdc25-structure-summary.md
31. raha-2026-taf2-myc-hcc-abstract.md
32. raha-2026-taf2-myc-hcc-fulltext.txt
33. raha-2026-taf2-myc-hcc-summary.md
34. uniprot-A0A9L0J8J4-record.fasta
35. uniprot-A0A9L0J8J4-record.txt
36. uniprot-Q8N9B8-record.fasta
37. uniprot-Q8N9B8-record.txt
38. ura-2006-rasgef1a-cholangiocarcinoma-abstract.md
39. ura-2006-rasgef1a-cholangiocarcinoma-summary.md
40. vigil-2010-gefs-gaps-cancer-abstract.md
41. vigil-2010-gefs-gaps-cancer-summary.md
42. wang-2020-donkey-genome-abstract.md
43. wang-2020-donkey-genome-summary.md
44. yaman-2009-rasgef1-rap2-abstract.md
45. yaman-2009-rasgef1-rap2-summary.md
46. zhu-2005-rap2-jnk-ampar-abstract.md
47. zhu-2005-rap2-jnk-ampar-summary.md