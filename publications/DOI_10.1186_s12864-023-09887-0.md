---
reference_id: DOI:10.1186/s12864-023-09887-0
title: mosGILT controls innate immunity and germ cell development in Anopheles gambiae
authors:
- Gunjan Arora
- Xiaotian Tang
- Yingjun Cui
- Jing Yang
- Yu-Min Chuang
- Jayadev Joshi
- Andaleeb Sajid
- Yuemei Dong
- Peter Cresswell
- George Dimopoulos
- Erol Fikrig
journal: BMC Genomics
year: '2024'
doi: 10.1186/s12864-023-09887-0
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://bmcgenomics.biomedcentral.com/counter/pdf/10.1186/s12864-023-09887-0"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1186_s12864-023-09887-0.pdf
---

# mosGILT controls innate immunity and germ cell development in Anopheles gambiae
**Authors:** Gunjan Arora, Xiaotian Tang, Yingjun Cui, Jing Yang, Yu-Min Chuang, Jayadev Joshi, Andaleeb Sajid, Yuemei Dong, Peter Cresswell, George Dimopoulos, Erol Fikrig
**Journal:** BMC Genomics (2024)
**DOI:** [10.1186/s12864-023-09887-0](https://doi.org/10.1186/s12864-023-09887-0)

## Content

AbstractGene-edited mosquitoes lacking a gamma-interferon-inducible lysosomal thiol reductase-like protein, namely (mosGILTnull) have lower Plasmodium infection, which is linked to impaired ovarian development and immune activation. The transcriptome of mosGILTnull Anopheles gambiae was therefore compared to wild type (WT) mosquitoes by RNA-sequencing to delineate mosGILT-dependent pathways. Compared to WT mosquitoes, mosGILTnull A. gambiae demonstrated altered expression of genes related to oogenesis, 20-hydroxyecdysone synthesis, as well as immune-related genes. Serendipitously, the zero population growth gene, zpg, an essential regulator of germ cell development was found to be one of the most downregulated genes in mosGILTnull mosquitoes. These results provide a crucial missing link between two previous studies on the role of zpg and mosGILT in ovarian development. This study further demonstrates that mosGILT has the potential to serve as a target for the biological control of mosquito vectors and to influence the Plasmodium life cycle within the vector.

Arora et al. BMC Genomics           (2024) 25:42  
https://doi.org/10.1186/s12864-023-09887-0
RESEARCH Open Access
© The Author(s) 2024. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which 
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory 
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this 
licence, visit http://creativecommons.org/licenses/by/4.0/. The Creative Commons Public Domain Dedication waiver (http://creativecom‑
mons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.
BMC Genomics
mosGILT controls innate immunity and germ 
cell development in Anopheles gambiae
Gunjan Arora1*†, Xiaotian Tang1†, Yingjun Cui1, Jing Yang1,5, Yu‑Min Chuang1, Jayadev Joshi2, Andaleeb Sajid1, 
Yuemei Dong3, Peter Cresswell4, George Dimopoulos3 and Erol Fikrig1* 
Abstract 
Gene‑edited mosquitoes lacking a gamma‑interferon‑inducible lysosomal thiol reductase‑like protein, namely 
(mosGILTnull) have lower Plasmodium infection, which is linked to impaired ovarian development and immune activa‑
tion. The transcriptome of mosGILTnull Anopheles gambiae was therefore compared to wild type (WT) mosquitoes 
by RNA‑sequencing to delineate mosGILT‑dependent pathways. Compared to WT mosquitoes, mosGILTnull A. gambiae 
demonstrated altered expression of genes related to oogenesis, 20‑hydroxyecdysone synthesis, as well as immune‑
related genes. Serendipitously, the zero population growth gene, zpg, an essential regulator of germ cell development 
was found to be one of the most downregulated genes in mosGILTnull mosquitoes. These results provide a crucial 
missing link between two previous studies on the role of zpg and mosGILT in ovarian development. This study further 
demonstrates that mosGILT has the potential to serve as a target for the biological control of mosquito vectors 
and to influence the Plasmodium life cycle within the vector.
Keywords Anopheles, Mosquito, Immunity, Metabolism, Genomics, Ovarian Development, mosGILT, GILT, ZPG, 
Mosuito Immunity, Mosquito Reproduction, Fat body, Malaria, 20‑Hydroxyecdysone
Introduction
Malaria remains one of the deadliest vector-borne dis -
eases, with over 247 million cases and approximately 
619 thousand deaths reported globally in 2021 [1]. It is 
caused by apicomplexan protozoa of the genus Plasmo -
dium and transmitted by female Anopheles mosquitoes. 
During its journey through the vector, Plasmodium is 
profoundly influenced by mosquito factors that either 
facilitate or suppress parasite development [2–5]. In 
the mosquito midgut, Plasmodium  development begins 
with the differentiation of gametocytes into gametes, fol -
lowed by the formation of zygotes, ookinetes, and then 
oocysts. Parasite numbers suffer great losses, especially 
during traversal of the midgut epithelium [6, 7]. This 
midgut bottleneck of the Plasmodium  life cycle is, there -
fore, an optimal target for blocking malaria transmission 
[8–13]. Considering the increase of insecticide resistance 
in Anopheles [5, 14–16], a better knowledge of how mos -
quito-derived factors influence midgut-stage parasites 
†Gunjan Arora and Xiaotian Tang contributed equally to this work.
*Correspondence:
Gunjan Arora
arorag1983@gmail.com
Erol Fikrig
erol.fikrig@yale.edu
1 Section of Infectious Diseases, Department of Internal Medicine, Yale 
School of Medicine, New Haven, Connecticut 06520, USA
2 Genomic Medicine Institute, Cleveland Clinic, Cleveland, Ohio 44195, 
USA
3 W. Harry Feinstone Department of Molecular Microbiology 
and Immunology, Bloomberg School of Public Health, Johns Hopkins 
University, Baltimore, Maryland 21205, USA
4 Department of Immunobiology, Yale School of Medicine, New Haven, 
Connecticut 06510, USA
5 Current Affiliation: Cuiying Biomedical Research Center, Lanzhou 
University Second Hospital, Lanzhou, Gansu 730030, China

Page 2 of 12Arora et al. BMC Genomics           (2024) 25:42 
is important for developing novel strategies for malaria 
intervention.
Blood-feeding is important for the female mosquito to 
obtain the nutrients required for egg development. Stud -
ies suggest that Plasmodium  maturation in the midgut 
is influenced by concurrent mosquito reproductive pro -
cesses, yet the underlying mechanisms remain poorly 
understood [17, 18]. Through CRISPR/Cas9 gene editing, 
our group demonstrated that disruption of a mos quito 
gamma-interferon-inducible lysosomal thiol reductase-
like protein—mosGILT—caused underdeveloped ovaries 
with a reduction in egg development and the production 
of ecdysteroid hormone 20-hydroxyecdysone (20E), and 
vitellogenin (Vg) [19]. Interestingly, mosGILT-deficient 
(mosGILTnull) Anopheles gambiae also showed signifi -
cant suppression of both Plasmodium berghei and Plas-
modium falciparum  infection, as measured by reduced 
oocyst intensity and prevalence [19]. In parallel, another 
study showed that Anopheles mosquitoes with a dis -
rupted zero-population growth—zpg—gene also exhib -
ited underdeveloped ovaries that produced low amounts 
of 20E and were less permissive to P. falciparum infec -
tion [20]. Though both mosGILTnull and zpgnull mosqui -
toes exhibited somewhat similar phenotypes, it is unclear 
whether their mechanisms of action are similar or dis -
tinct. In this study, we elucidate the mosGILT-depend -
ent global transcriptional responses in A. gambiae. The 
information here may provide novel insights into the A. 
gambiae reproductive system network, as well as innate 
responses associated with Plasmodium infection.
Results
Transcriptome analysis of mosGIL Tnull A. gambiae
To examine whether the molecular responses to a blood 
meal were altered in mosGILT null A. gambiae, RNA 
sequencing (RNA-seq) was performed. mosGILT null and 
Wild type (WT, control) mosquitoes were fed on naïve 
mice and then separated into cardboard containers. The 
whole body, ovaries, and fat bodies were collected from 
blood-fed mosquitoes 24 h after completion of the meal. 
RNA-seq was carried out with total RNA extracted from 
the whole body, ovaries, or fat bodies from A. gambiae  
using Illumina sequencing technology. A total of 16  
samples (from control and mosGILTnull A. gambiae) were 
sequenced (Supplementary Fig. 1). After sequencing, each 
library generated around 10–28 million reads and approxi-
mately 78.0–99.7% of the reads in each library mapped to 
the A. gambiae genome (Supplementary Figs.  2, 3, and 4).
Principal component analysis of mosquito libraries  
examined the clustering of data/samples after a blood meal. 
All biological replicates of control and mosGILTnull samples  
were distributed into two distinct groups (Fig.  1A).  
Volcano plots indicated that there were differentially 
expressed genes (DEGs) in all three groups (Fig. 1B), with 
whole-body samples having the maximum number of 
DEGs (n = 5749), followed by the ovaries and fat bodies. In 
all the three samples analyzed, 108 DEGs were common to 
all three groups (Fig. 2A). Of particular interest were 4991 
DEGs in the ovaries of mosGILTnull mosquitoes which are 
potentially helpful to elucidate the role of mosGILT in  
A. gambiae development and Plasmodium infection.
Fig. 1 A Principal component analysis of the RNA‑Seq data. The whole body (WB), fat body (FB) and ovary (OV) samples were collected at 24 h 
from blood‑fed (BF) wild‑type (WT) and  mosGILTnull Anopheles gambiae. B Volcano plot analysis of differentially expressed genes (DEGs) of whole 
body (WB), fat body (FB) and ovary (OV) between wild type (control) and mosGILTnull Anopheles gambiae. DEGs with False Discovery Rate (FDR) 
p‑values of < 0.05 and  log2 fold changes > 1 are presented

Page 3 of 12
Arora et al. BMC Genomics           (2024) 25:42 
 
DEG analysis reveals that mosGILT has a role 
in nucleocytoplasmic transport
Since female mosGILT null mosquitoes display defects in 
ovarian development and show refractoriness to Plas -
modium, we first focused on the nature of genes that 
showed differential expression patterns in the ovarian 
tissue. Among the 4991 DEGs, 117 genes had a more 
than a 100-fold increase in mRNA abundance compared 
to the WT controls, and 97 genes showed at least a 100-
fold lower mRNA abundance. Several groups of genes 
showed altered expression patterns in oxidative phos -
phorylation and nucleocytoplasmic transport based on 
Gene Ontology (GO) annotation (Figs.  2B, and 3 A, B, 
C, D). Nucleocytoplasmic transport (75 genes, p -value 
2.60E-13) is a process crucial for cell function (Supple -
mentary Table  1 and Supplementary Fig.  5). Depletion 
Fig. 2 A Venn diagrams showing the number of differentially expressed genes (DEGs) between whole body (WB), fat body (FB) and ovary (OV) 
tissues of blood‑fed Anopheles gambiae. The numbers in the overlapping areas indicate genes that were common to both or to all three different 
time points. The number of DEGs was highest between the whole body and ovary samples. B Bubble chart and circle graph showing enriched 
pathways in the whole body, fat body, and ovary of mosGILTnull mosquitoes by KEGG (Kyoto Encyclopedia of Genes and Genomes) analysis. Gene 
ontology annotation and pathway enrichment analysis of the top differentially expressed genes (DEGs) in the whole body, fat body, and ovary are 
shown. Enriched functional ontology terms are shown on the left. The whole body, fat body, and ovary are represented by blue, red, and orange 
colors respectively. The  Log10 (p‑value) is shown on the X‑axis
Fig. 3 A, B and C Bubble chart showing enrichment of Gene Ontology (GO) terms of the differentially expressed genes in the whole body, fat 
body, and ovary of mosGILTnull mosquitoes. The biological processes, cellular components, and molecular functions are shown in blue, magenta 
and orange respectively. The –Log10 (p‑value) for each process is shown on the X‑axis. D The figure presents the Manhattan plot showcasing 
enrichment analysis of differentially expressed genes in the ovary of mosGILTnull mosquitoes performed using g:Profiler. The x‑axis represents 
functional GO terms grouped and color‑coded based on data sources. The y‑axis displays adjusted enrichment p‑values on a negative log10 scale

Page 4 of 12Arora et al. BMC Genomics           (2024) 25:42 
of mammalian GILT (IFI30) in immune cells can inhibit 
cytokine production and the release of high mobility 
group box  1 (HMGB1), a nonhistone nuclear protein. 
The cytosolic translocation of the nuclear HMGB1 
protein is then activated and associated with increased 
autophagy in GILT-depleted fibroblasts [21, 22]. These 
findings suggest that mammalian GILT is involved in 
the homeostatic regulation of oxidative stress. In the 
absence of mosGILT, nucleocytoplasmic transport path -
ways are upregulated which can influence diverse cel -
lular responses, such as autophagy (Fig.  2B). Indeed, 
autophagy negatively regulates Vg production in gono -
trophic cycles in Aedes  mosquitoes, which is consist -
ent with the changes in Vg production as shown by our 
group previously [23].
Whole body analysis of A. gambiae confirms the role 
of mosGILT in development and metabolism
Our previous studies demonstrated that mosGILT is 
implicated in embryonic and ovarian development and 
shows refractoriness to Plasmodium  infection [19]. To 
fully understand how female mosGILT null mosquitoes 
show resistance to Plasmodium , we also examined the 
genes that showed differential expression patterns in 
the whole body. Among the 5749 DEGs, 76 genes had a 
more than a 100-fold decrease in expression compared 
to the WT control, and 7 genes showed at least 100-
fold upregulation. Similar to the ovaries, nucleocy -
toplasmic transport pathways were affected in the 
whole body of mosGILT null mosquitoes. The most 
downregulated proteins included AGAP007823 (mei -
osis arrest female protein 1, fold change: -1000000, 
p-value < 0.0001) and AGAP008738 (eukaryotic trans -
lation initiation factor 4E transporter, fold change 
-14625, p-value 0.0001) which is involved in protein 
translation and oogenesis (Fig. 4 A).
The most overexpressed genes included AGAP010658 
(fold change 169, p-value < 0.00001) which encodes 
a homolog of the hexameric 2 beta protein or larval 
serum protein 1 which serves as a major storage pro -
tein. AGAP010658 antagonizes Plasmodium berghei 
oocyst development and silencing of this gene by RNAi 
results in a significant increase in oocyst infection inten -
sities and melanization of ookinetes [24]. Other highly 
expressed genes were AGAP000046 (a sugar transporter, 
fold change 160, p-value < 00001) and AGAP002518 
(delta l-pyrroline-5-carboxylate synthetase, fold 
change 102, p-value < 0.00001). While transcripts of 
AGAP004203 were decreased (fold change -343), another 
Vg-like protein was overexpressed (AGAP008369 fold 
change 102, p-value < 0.00001). Among the major down -
regulated genes were AGAP002134 (vitelline membrane 
Fig. 4 Heat Map analysis of key differentially expressed genes in the ovary (A), and fat body (B) of mosGILTnull mosquitoes. C Heat map analysis 
of key differentially expressed genes that are related to germ cell development in mosGILTnull mosquitoes. D STRING functional gene analysis 
of zpg‑related genes: Each node represents a protein product of an investigated gene. Lines denote protein–protein interactions, with each edge 
representing an interaction including either physical or functional associations

Page 5 of 12
Arora et al. BMC Genomics           (2024) 25:42 
 
component which is required for the proper assembly 
of the eggshell) AGAP003545 (maternal effect protein 
oskar), and AGAP007767 (mosquito-specific bZIP1 tran -
scription factor) (Fig.  4A). Indeed, silencing of bZIP1 
in the embryos of Aedes aegypti resulted in embryonic 
death [25]. These findings indicate that mosGILT is 
involved in both development and metabolism.
Effect of mosGILT on metabolic responses in the  
A. gambiae fat body
Our previous study showed that mosGILT is expressed 
in the ovaries and fat body [19]. In insects, the fat body 
plays a central role in energy metabolism. After a blood 
meal, the fat body, which is the mosquito fat storage 
organ, initiates Vg synthesis. The fat body releases Vg 
into the hemolymph, and it is then taken up by devel -
oping oocytes via receptor-mediated endocytosis. Since 
mosGILTnull mosquitoes showed lower Vg mRNA levels, 
we examined the transcriptional response in the fat body. 
Our analysis shows that in the fat body, gene transcripts 
of metabolic pathways (gene count: 93, p-value 6.30E-
14) and pathways related to carbohydrate metabolism 
(pentose and glucuronate interconversions, fructose and 
mannose metabolism, galactose metabolism, biosynthe -
sis of nucleotide sugars, glycolysis/gluconeogenesis and 
starch, and sucrose metabolism) demonstrated major 
changes in the mosGILTnull mosquitoes. Among the most 
altered DEGs, AGAP029067 (lipid-binding protein) tran -
scripts were enriched by a 194-fold while transcripts of 
AGAP008547, a gene with a predicted function in car -
bohydrate metabolism showed nearly 160-fold enrich -
ment in the fat body of mosGILTnull mosquitoes (Fig. 4A). 
Blood-meal ingestion, therefore, not only induces the 
expression of genes related to egg development but also 
increased the expression of genes related to oxidative stress.
In mammals, GILT is expressed in lysosomes and is 
required for optimal activity of cysteine proteases, such 
as cathepsin in macrophages [26, 27]. In mosquitoes, the 
fat body plays a central role in metabolism and nutrient 
storage, mirroring the functions of the liver in vertebrates. 
In response to blood-feeding, the Aedes  fat body secretes 
a cathepsin-b-like thiol protease [28]. Interestingly, in 
our analysis of mosGILT null A. gambiae, the most down -
regulated genes include proteases such as AGAP004534 
(cathepsin B -like serine protease, fold change -18, p-value 
0.0001), and AGAP004700 (trypsin-like serine protease, 
fold change -20, p-value 0.0003) (Fig. 4B).
mosGILT regulates germ cell maintenance by controlling 
the expression of zero population growth (zpg)
A. gambiae females express  zero population growth  (zpg, 
AGAP006241), an essential gene for germ cell development. 
Genetic ablation of zpg in mosquitoes leads to severely 
underdeveloped ovaries and impaired egg production 
after a blood meal [20, 29, 30] similar to the mosGILTnull  
mosquitoes. zpg and mosGILT are important for Plasmo -
dium infection since mosquitoes lacking either gene show 
fewer oocysts after feeding on P. falciparum-infected 
blood compared to sibling controls. In the ovaries of 
mosGILTnull A. gambiae, zpg was strongly downregu -
lated (fold change -8130, p -value 0.0001) which suggests  
mosGILT acts upstream of zpg or influences the molecular 
pathway that regulates zpg expression (Fig.  4C). We fur -
ther performed protein network analysis (Fig. 4D, Supple-
mentary Fig.  6) to determine whether mosGILT affected 
the expression of other genes that are associated with zpg. 
STRING analysis showed the genes that are in the zpg 
network may be involved in germ cell development. Lack 
of mosGILT affected the expression of AGAP000427 (fold 
change -26814, p-value > 0.00001), which is in the zpg  
network and is a putative Vg receptor. In the ovaries of 
mosGILTnull mosquitoes, another zpg-related protein, oskar 
(AGAP003545) was strongly downregulated (fold change 
-8162, p-value > 0.00001) (Fig.  4C). Oskar is required 
for the formation of the germplasm in Drosophila [ 31]. 
Germplasm promotes the formation and specification of 
the primordial germ cells, the first cell lineage to form 
in the fertilized embryo [32]. Our genetic analyses of  
mosGILTnull mosquitoes reveal underdeveloped ovaries 
and a decrease in 20E production. Here, we have ana -
lyzed genes involved in insect hormone biosynthesis 
and found that five genes (AGAP001038, AGAP001039, 
AGAP004665, AGAP005992, AGAP000284) involved in 20E  
biosynthesis were downregulated in mosGILTnull mosqui -
toes (Fig. 5). Signaling of 20E is initiated by binding of 20E 
to the heterodimer ecdysone receptor (EcR)/ultraspiracle 
(USP) complex, which triggers a transcriptional response 
that promotes egg development. Our results show that  
mosGILTnull also decreases the expression of ultraspira -
cle (USP , AGAP002095, fold change -4, p-value < 0.00001) 
(Fig. 4C). The complex formed after 20E binding to EcR/USP  
upregulates the expression of an array of 20E-regulated 
genes which in turn controls the Vg transcriptional pro -
gram [33]. These results show that mosGILT regulates 20E 
levels, as well as the downstream transcriptional response.
Immune pathway alteration in mosGIL Tnull mosquitoes
GILT was first identified as an IFNγ-inducible, lysoso -
mal thiol reductase in mammals [37]. GILT is also key 
to antigen processing in mammals but in other organ -
isms it is part of the innate immune response [38]. 
Thioester-containing protein 1 (TEP1) is an important 
component of the A. gambiae innate immune system and 
plays a major role against Plasmodium  parasites [39, 40]. 
TEP is an antimicrobial protein family that acts like the 
human complement protein C3 and can damage the cell 

Page 6 of 12Arora et al. BMC Genomics           (2024) 25:42 
membranes of pathogens. In our study, we observed an 
increase in TEP1 activity in mosGILTnull mosquitoes [19]. 
We also showed that strong refractoriness to Plasmo -
dium infection in mosGILTnull mosquitoes was related to 
increased TEP1 activity. Therefore, we examined immune 
genes that are differentially expressed in mosGILTnull 
mosquitoes to better understand how TEP1 activity is 
influenced.
In our analysis, we found that AGAP028725 (SPCLIP1) 
was upregulated in the ovary (fold change 73, p-value 
0.0001) and whole body (fold change 12, p-value 0.0001) 
of mosGILTnull mosquitoes (Fig.  6). Clip domain ser -
ine proteases (CLIPs) play an important role in innate 
immunity in mosquitoes. These proteases are present in 
hemolymph and are involved in Plasmodium  immunity, 
antimicrobial peptide synthesis and melanization. Pre -
viously it was shown that complement C3-like protein 
TEP1 mediated killing of Plasmodium  is dependent on 
the CLIP-domain serine protease homolog SPCLIP1 [41, 
42]. SPCLIP1 is required for the accumulation of TEP1 
on microbial surfaces, a reaction that leads to lysis of 
malaria parasites [41, 42].
In this study, we also found that mosGILT null mos -
quitoes have increased expression of three TEP pro -
teins—TEP15, TEP14, and TEP2. TEP15 (AGAP008364) 
expression was increased in the ovary (fold change 230, 
p-value < 0.0001) and whole body (fold change 12, p-value 
0.0001) (Fig.  6). TEP14 (AGAP008368, fold change 10, 
p-value 0.0017) and TEP2 (AGAP008366, fold change 9, 
p-value 0.0001) expression was increased in the whole 
body. These TEP  genes were upregulated significantly 
upon P. falciparum infection in the midgut of A. gambiae 
mosquitoes [42].
mosGILT disruption also increased the expression of 
another innate immune gene, peptidoglycan recogni -
tion protein, PGRPLD (AGAP005552) in the ovary (fold 
change 125, p-value < 0.0001), whole body (fold change 
8, p-value < 0.0001) and fat body (fold change 7, p-value 
0.0001). Peptidoglycan recognition proteins (PGRPs) are 
a family of immune regulators, conserved from insects 
to mammals. PGRPLD is important for anti-Plasmo -
dium immunity and in PGRPLD -silenced mosquitoes, 
Plasmodium infection increased significantly [43]. 
Additional immune-related genes, including 2 serpins, 
SRPN6 (AGAP009212) and SRPN9 (AGAP003139) was 
also overexpressed in the ovary (fold change 11, p-value 
0.0002, fold change 8, p-value < 0.0001 respectively) and 
whole body (fold change 3, p-value 0.0135, fold change 
3, p-value 0.0002 respectively) and fat body (SRPN9, fold 
change 5, p-value 0.0007) (Fig.  6). SRPN6 is a compo -
nent of the midgut epithelial immune-response system 
which is increased during Plasmodium  infection and 
Fig. 5 Insect hormone biosynthesis pathway in Anopheles gambiae based on KEGG pathway analysis. Enzymes are indicated in green highlight. 
The DEGs genes in mosGILT.null mosquitoes are shown in orange (overexpression) and blue (downregulation) are indicated by the gene ids. KEGG 
Pathway entry aga00981 framework is used (https:// www. genome. jp/ entry/ pathw ay+ aga00 981) [34–36]

Page 7 of 12
Arora et al. BMC Genomics           (2024) 25:42 
 
knockdown of this gene increased parasite numbers in  
A. stephensi [44].
In addition, we also observed increase in defensin 
transcripts, an anti-microbial peptide (AGAP011294, 
DEF1). Def1 expression was upregulated in the ovary 
(fold change 255, p-value 0.0001) and whole body (fold 
change 3, p-value 0.0029) of mosGILT null mosquitoes 
(Fig.  6). Transcripts of another anti-microbial peptide 
gene, cercopin 1 (AGAP000693) was also increased in the 
ovary (fold change 300, p-value 0.0004) and whole body 
of the mosGILT null mosquitoes (fold change 2, p-value 
0.0235), and cercopin 3 (AGAP000694) expression was 
upregulated in the whole body (fold change 3, p-value 
0.0016). Toll-like receptors (TLRs) are evolutionarily 
conserved pattern recognition receptor proteins with 
diverse biological functions. In Drosophila melanogaster, 
Toll plays an important role in pattern formation dur -
ing embryogenesis and in immunity. In this study we 
observed that TLR9 expression in the mosGILTnull mos -
quito was upregulated in the whole body (AGAP006974, 
fold change 2, p-value 0.0095) Though there is not much 
information on this gene in A. gambiae, in the silk moth, 
Bombyx mori, TLR9 is involved in innate immunity and 
functions as a pattern recognition receptor that binds 
lipopolysaccharide.
Discussion
To further understand Plasmodium  infection of the 
vector, and develop new mosquito and malaria con -
trol strategies, it is important to decipher the molecu -
lar mechanisms related to mosquito reproduction and 
immunity. Recently our lab uncovered a critical role for 
mosGILT in A. gambiae ovary development and  Plas-
modium  infection [19]. The mosGILT null mosquitoes 
displayed underdeveloped ovaries and reproductive 
defects including impaired production of 20E and Vg 
while showing an increased TEP1-mediated immune 
response against Plasmodium  ookinetes [19]. However, 
there is a lack of knowledge regarding how mosGILT 
functions in A. gambiae, its interacting partners, and 
the implicated signaling pathways. Here we character -
ize the transcriptional response in mosGILT null mosqui -
toes, including the ovaries, whole body, and fat body, and 
delineate how mosGILT is regulating reproduction and 
immune responses.
GILT is a thioredoxin-related oxidoreductase which 
is the only known lysosomal thiol reductase [27]. Mam -
malian GILT is related to the thioredoxin family of oxi -
doreductases, characterized by a CXXC motif in the 
active site and an enzymatic mechanism in which the 
pair of active site cysteine residues cooperate to reduce 
substrate disulfide bonds [45–48]. In Anopheles mosqui -
toes and other insect genera, the active motif is CXXS, 
where the second cysteine is replaced with serine (Fig. 7A 
and B). This change in the active site of mosGILT hinders 
the thioredoxin reaction of the mixed intermolecular 
disulfide. The CXXS containing thioredoxins can inter -
act with their substrate proteins in a more stable manner 
since there is a covalent complex formed between thiore-
doxins and their target. However, some studies report 
that at least some CXXS-containing forms of thiore -
doxin-fold proteins retain catalytic activity albeit at a 
Fig. 6 Heat map analysis of key differentially expressed genes related to immune pathways in the whole body (WB), fat body (FB) and ovary (OV) 
of mosGILTnull mosquitoes

Page 8 of 12Arora et al. BMC Genomics           (2024) 25:42 
lower level [49, 50]. It is therefore possible that mosGILT 
has partial thioredoxin activity that is critical to the tran -
scriptional response that leads to oogenesis and ovarian 
development.
Vector reproduction is closely associtaed with immune 
defense pathways, as these two processes are simulta -
neously initiated after a blood meal [51–53]. Identi -
fication of mosquito proteins that regulate cross-talk 
between reproduction and immunity could serve as tar -
gets for vector-control strategies. Our previous study 
demonstrated that mosGILT plays an essential role in 
the reproduction of A. gambiae [19]. In this study we 
show that mosGILT influences complement activity and 
upregulates defense-related genes, which are associated 
with anti-Plasmodium  responses. In addition, mosGILT 
regulates TEP1 activity by altering SPCLIP1 expression, 
which can influence Plasmodium survival in mosquitoes. 
mosGILTnull mosquito refractoriness to microbes was 
also suggested by the increase in genes encoding antimi -
crobial peptides and innate immune molecules. mosGILT 
may therefore be a potential target for new malaria con -
trol strategies, such as gene drive -propelled transgenes 
targeting mosGILT, that would induce mosquito sterility 
and also reduce the overall malaria parasite burden.
Development and immunity are highly demanding pro-
cesses and, thus, a balance must be maintained between 
the two [54]. Previously it was suggested that there is a 
trade-off between reproductive fitness and immune 
defense in mosquitoes including A. gambiae and acti -
vation of immune pathways can cause a reduction in 
fecundity by inducing the resorption of ovarian follicles 
during oocyte development [55–58]. In another exam -
ple, activation of immune signaling leads to decreased 
in reproductive capacity of D. melanogaster [59]. These 
observations suggest that in the absence of mosGILT 
and a reduction in ovary development, there may be an 
increase in the immune response. This is also supported 
by a recent study where it was shown that 20E binding 
to the ecdysone receptor (EcR) directly induces a Pirk-
like inhibitor, affecting the immune deficiency (IMD) 
pathway in Aedes mosquitoes [57]. Pirk downregulates 
the IMD pathway by inhibitng the nuclear translocation 
of the NF-κB transcriptional factor Rel2 and this down -
regulation of the immune response is vital for maintain -
ing mosquito fertility. We hypothesize that the effects 
of downregulating ecdysone on mosquito immunity can 
be complex. We acknowledge that in some studies 20E 
is shown to have immunomodulatory effects, and it can 
enhance the mosquitoes immune response [52, 60–62]. 
Our results with mosGILT null mosquitoes show that the 
influence of 20E on immunity may be part of a broader 
regulatory network. Overall our results suggest that mos -
GILT may be important for resource allocation in respect 
to both development and immunity. In the absence of 
Fig. 7 Structural and sequence analysis of mosGILT (A) The mosGILT structural model is created by Alpha Fold. Structural alignment of mosGILT 
homologs from Anopheles, Aedes, Drosophila and human GILT. The active site motif is shown in the yellow in the inset. B Sequence alignment 
of Anopheles, Aedes, Drosophila and Ixodes GILT. Protein sequence of mosGILT homologs from Anopheles gambiae (AGAP004551), Aedes aegypti 
(XP_021707151.1 GILT‑like protein 1), Drosophila melanogaster (NP_650287.3 Gamma‑interferon‑inducible lysosomal thiol reductase 1), Ixodes 
scapularis (XP_029851151.3 GILT‑like protein 1). Active site residues are shown in the inset box

Page 9 of 12
Arora et al. BMC Genomics           (2024) 25:42 
 
mosGILT, resources are moved to immune pahways and 
there is reduction in reproductive capacity. Overall, our 
results suggest tha mosquito immunity is multilayered 
and hierarchical, where downregulation of the mosGILT 
in Anopheles mosquitoes is sufficient to activate the 
immune system even in the absence of 20E.
mosGILT mutants have underdeveloped ovaries that 
produced low amounts of 20E, and were significantly less 
permissive to P. falciparum infection [19]. This is some -
what similar to Plasmodium  infection in zpg mutant 
mosquitoes, a gene that is essential for germ cell develop-
ment [20, 30]. Though both mutant mosquitoes provide 
an association between 20E signaling and intensity of 
Plasmodium infection, it is not known if they act together 
or independently. Our studies now suggest that mos -
GILT may affect several genes that are associated with 
zpg. Since zpg and other germ cell development genes 
are considered a prime target for gene drive[63–65], our 
results suggest mosGILT may be more attractive target 
for gene drive of A. gambiae.
mosGILT plays an important role in reproduction and 
host defenses in A. gambiae. The elucidation of mos -
GILT as a regulator of zpg and involvement in cross-talk 
between reproduction and immunity could provide new 
targets for the development of disease-control strategies 
(Fig.  8). These findings can potentially lead to new pre -
ventive strategies for malaria based on Anopheles mos -
GILT and also potentially suggest a role for arthropod 
GILT-like proteins for other vector-borne diseases.
Materials and methods
Mosquito rearing
All the A. gambiae mosquito lines were derived from the G3 
strain, including the docking line X1 [66], vasa2-Cas9 [67], 
mosGILT-gRNA3 [ 19], mosGILT  mutant and sibling mos-
quitoes. They were raised at 27 °C, 80% humidity, under a 
12/12  h light/dark cycle and maintained with 10% sucrose. 
Swiss Webster mice (8-week-old females) were purchased 
from Charles River Laboratories.
Generation of transgenic mosGIL T mutant mosaic 
Anopheles mosquitoes
CRISPR/Cas9 mediated A. gambiae mosGILT somatic 
KO mutants were generated using the  A. gambiae dock -
ing line X1 as described in Yang et al., 2020 [19]. In brief, 
the mosGILT-gRNA female mosquitoes were crossed 
with the homozygous  male Vasa Cas9  transgenic strain 
(vasa2-Cas9; with green/yellow fluorescence in the eyes;) 
[67, 68]. The progeny of this cross was screened at the 
larvae stage with both RFP (red fluorescence marker) 
and YFP (appeared as green fluorescence through GFP-
channel under the fluorescence microscope) signals 
was  gRNA/Cas9  trans-heterozygous. Molecular screen -
ing of these trans-heterozygotes by PCR and sequencing 
was done as described to confirm the mosGILTnull [19].
RNA isolation
Total RNA was extracted from the whole body, ovaries, or 
fat bodies from mosquitoes. Trizol was added to the tissues 
and RNA was isolated using a using a combination method 
which utilizes TRIzol (Thermo Fisher Scientific) and 
RNeasy Mini Kit (QIAGEN) as described before [69].
RNA‑seq
RNA was submitted for library preparation using TruSeq 
(Illumina, San Diego, CA, USA) and sequenced using 
Illumina HiSeq 2500 by paired-end sequencing at the 
Yale Center for Genome Analysis (YCGA).
Fig. 8 Diagrammatic representation of mosGILT’s role in immunity and development

Page 10 of 12Arora et al. BMC Genomics           (2024) 25:42 
Differential gene expression analysis
All the RNA-seq analyses including alignment, quanti -
tation, normalization, and differential gene expression 
analyses were performed using Partek Genomics Flow 
software (St. Louis, MO, USA). Specifically, RNA-seq 
data were trimmed and aligned to the Anopheles PEST 
genome, version P4.14. with associated annotation file 
using STAR (v2.7.3a) [70]. The aligned reads were quan -
tified using the Partek E/M algorithm [71] and the sub -
sequent steps were performed on gene-level annotation 
followed by total count normalization. The gene-level 
data were normalized by dividing the gene counts by the 
total number of reads followed by the addition of a small 
offset (0.0001).
Principal components analysis
Principal components analysis (PCA) was performed 
using default parameters for the determination of the 
component number, with all components contributing 
equally in Partek Flow. Volcano plot Hierarchal cluster -
ing was performed on the genes that were differentially 
expressed across the conditions (P < 0.05, fold change ≥ 2 
for each comparison).
Pathway enrichment analysis
Pathway enrichment was also conducted in Partek Flow 
and the functional annotation tool DAVID (https:// david. 
ncifc rf. gov/ tools. jsp). The selected genes expression heat-
map was further plotted by ggplot2 (R sutdio) and Prism 
v8 (Graphpad). The selected immune pathways were 
further plotted on a bubble diagram by ggplot2 (version 
3.3.5) in R Statistical Software (v4.1.2) as described pre -
viously[72, 73]. The network analysis was performed in 
String database [74, 75].
PPI network and Cluster analysis
PPI network was generated by STRING online database 
and visualized by Cytoscape software [75, 76]. K means 
clustering with 10 clusters was selected to generate cluster 
with edges.
Homology modeling and sequence analysis
The mosGILT structural model was created using Alpha -
Fold [77]. The structural model of mosGILT was ana -
lyzed as detailed previously [78]. Structural alignment of 
mosGILT homologs from Anopheles, Aedes, Drosophila 
and human GILT. (B) Sequence alignment of Anopheles, 
Aedes, Drosophila and Ixodes GILT was performed using 
Clustal Omega (Version 1.2.4) [79]. Protein sequence 
of mosGILT homologs from Anopheles gambiae  
(AGAP004551), Aedes aegypti (XP_021707151.1 GILT-
like protein 1), Drosophila melanogaster (NP_650287.3 
Gamma-interferon-inducible lysosomal thiol reductase 1), 
Ixodes scapularis (XP_029851151.3 GILT-like protein 1) 
were analyzed.
Statistical analysis
All data analysis, graphing, and statistics were performed 
in Prism (v8.0, GraphPad Software) and R Statistical Soft-
ware (v4.1.2) (https:// www.r- proje ct. org/).
Supplementary Information
The online version contains supplementary material available at https:// doi. 
org/ 10. 1186/ s12864‑ 023‑ 09887‑0.
Additional file 1: Supplementary Figure 1. Distribution of Raw counts 
in all Anopheles samples. Supplementary Figure 2. Key statistics of 
Ovary samples. Supplementary Figure 3. Key statistics of whole‑body 
samples. Supplementary Figure 4. Key statistics of Fatbody samples. 
Supplementary Figure 5. Pathway enrichment analysis using the 
g:Profiler online tool. Table provides comprehensive information related 
to the selected term, including the data source, term ID, term name, and 
corresponding p‑value. Abbreviations: GO:BP (Gene Ontology: Biological 
Process); GO:CC (GO: Cellular Component); GO:MF (GO: Molecular Func‑
tion). Supplementary Figure 6. Protein‑Protein Interaction (PPI) network: 
The interaction Network of DEGs in the Ovary of mosGILTnull mosquitoes 
was created using the STRING database and imported into Cytoscape. The 
k clustering method was used to identify clusters and key nodes in this 
network.
Additional file 2: Supplementary Table 1. Fold change data and raw 
statistics showing the role of mosGILT in Anopheles mosquitoes.
Acknowledgements
We thank the Yale Center for Genome Analysis (YCGA) for conducting RNA 
sequencing. We thank the JHMRI insectary core facility for maintaining  
A. gambiae mosquitoes.
Authors’ contributions
Conceived and designed the experiments: GA, XT, EF. Performed the experi‑
ments: GA, XT, YC, JY, YMC, AS, YD. Analyzed the data: GA, XT, JJ, EF. Contrib‑
uted reagents/materials/analysis tools: JY, JJ, YD, PC, GD, EF. Wrote the main 
manuscript text: GA, XT, EF. All authors reviewed the manuscript.
Funding
This work is supported in part by the Howard Hughes Medical Institute 
Emerging Pathogens Initiative and NIH grants (AI142708, and AI58615), and 
the Bloomberg Philanthropies.
Availability of data and materials
RNAseq data are deposited in a public database (Sequence Read Archive (SRA) 
data. The RNA‑seq data are available in the Gene Expression Omnibus (GEO) 
repository at the National Center for Biotechnology Information under the 
accession number: GSE239600 (https:// www. ncbi. nlm. nih. gov/ geo/ query/ acc. 
cgi? acc= GSE23 9600).
Declarations
Ethics approval and consent to participate
Mice used in the study were housed at the Yale Animal Resource Center of 
Yale University. Mice were handled in accordance with the Guide for the Care 
and Use of Laboratory Animals of the National Institutes of Health, USA. The 
Institutional Animal Care and Use Committee of Yale University approved the 
animal experimental protocol (protocol permit no. 2017–07941) and followed 
the ARRIVE Guidelines (https:// arriv eguid elines. org/).
Consent for publication
Not applicable.

Page 11 of 12
Arora et al. BMC Genomics           (2024) 25:42 
 
Competing interests
The authors declare no competing interests.
Received: 5 September 2023   Accepted: 9 December 2023
References
 1. World Health Organization. World Malaria report. 2022. https:// www. who. 
int/ teams/ global‑ malar iapro gramme/ repor ts/ world‑ malar ia‑ report‑ 2022.
 2. Arora G, Chuang YM, Sinnis P , Dimopoulos G, Fikrig E. Malaria: influence 
of Anopheles mosquito saliva on Plasmodium infection. Trends Immunol. 
2023;44(4):256–65.
 3. Dong S, Dong Y, Simoes ML, Dimopoulos G. Mosquito transgenesis for 
malaria control. Trends Parasitol. 2022;38(1):54–66.
 4. Waterhouse RM, Kriventseva EV, Meister S, Xi Z, Alvarez KS, Bartholomay 
LC, et al. Evolutionary dynamics of immune‑related genes and pathways 
in disease‑vector mosquitoes. Science. 2007;316(5832):1738–43.
 5. Shaw WR, Catteruccia F. Vector biology meets disease control: using basic 
research to fight vector‑borne diseases. Nat Microbiol. 2019;4(1):20–34.
 6. Volohonsky G, Paul‑Gilloteaux P , Stafkova J, Soichot J, Salamero J, 
Levashina EA. Kinetics of Plasmodium midgut invasion in Anopheles 
mosquitoes. PLoS Pathog. 2020;16(9):e1008739.
 7. Baton LA, Ranford‑Cartwright LC. How do malaria ookinetes cross the 
mosquito midgut wall? Trends Parasitol. 2005;21(1):22–8.
 8. Wang S, Jacobs‑Lorena M. Genetic approaches to interfere with malaria 
transmission by vector mosquitoes. Trends Biotechnol. 2013;31(3):185–93.
 9. Smith RC, Vega‑Rodriguez J, Jacobs‑Lorena M. The Plasmodium bottle‑
neck: malaria parasite losses in the mosquito vector. Mem Inst Oswaldo 
Cruz. 2014;109(5):644–61.
 10. Blandin SA, Marois E, Levashina EA. Antimalarial responses in Anopheles 
gambiae: from a complement‑like protein to a complement‑like path‑
way. Cell Host Microbe. 2008;3(6):364–74.
 11. Vijay S, Rawal R, Kadian K, Singh J, Adak T, Sharma A. Proteome‑wide 
analysis of Anopheles culicifacies mosquito midgut: new insights into the 
mechanism of refractoriness. BMC Genomics. 2018;19(1):337.
 12. Bennink S, Kiesow MJ, Pradel G. The development of malaria parasites in 
the mosquito midgut. Cell Microbiol. 2016;18(7):905–18.
 13. Whitten MM, Shiao SH, Levashina EA. Mosquito midguts and malaria: 
cell biology, compartmentalization and immunology. Parasite Immunol. 
2006;28(4):121–30.
 14. Hemingway J, Ranson H, Magill A, Kolaczinski J, Fornadel C, Gimnig J, 
et al. Averting a malaria disaster: will insecticide resistance derail malaria 
control? Lancet. 2016;387(10029):1785–8.
 15. Ranson H, Lissenden N. Insecticide resistance in African Anopheles 
mosquitoes: a worsening situation that needs urgent action to maintain 
malaria control. Trends Parasitol. 2016;32(3):187–96.
 16. Benelli G, Beier JC. Current vector control challenges in the fight against 
malaria. Acta Trop. 2017;174:91–6.
 17. Costa G, Gildenhard M, Eldering M, Lindquist RL, Hauser AE, Sauer‑
wein R, et al. Non‑competitive resource exploitation within mosquito 
shapes within‑host malaria infectivity and virulence. Nat Commun. 
2018;9(1):3474.
 18. Marcenac P , Shaw WR, Kakani EG, Mitchell SN, South A, Werling K, et al. 
A mating‑induced reproductive gene promotes Anopheles tolerance to 
Plasmodium falciparum infection. PLoS Pathog. 2020;16(12):e1008908.
 19. Yang J, Schleicher TR, Dong Y, Park HB, Lan J, Cresswell P , et al. Disruption 
of mosGILT in Anopheles gambiae impairs ovarian development and 
Plasmodium infection. J Exp Med. 2020;217(1):e20190682.
 20. Werling K, Shaw WR, Itoe MA, Westervelt KA, Marcenac P , Paton DG, et al. 
Steroid hormone function controls non‑competitive plasmodium devel‑
opment in anopheles. Cell. 2019;177(2):315–25.
 21. Chen R, Kang R, Tang D. The mechanism of HMGB1 secretion and release. 
Exp Mol Med. 2022;54(2):91–102.
 22. Chiang HS, Maric M. Lysosomal thiol reductase negatively regulates 
autophagy by altering glutathione synthesis and oxidation. Free Radic 
Biol Med. 2011;51(3):688–99.
 23. Bryant B, Raikhel AS. Programmed autophagy in the fat body of Aedes 
aegypti is required to maintain egg maturation cycles. PLoS One. 
2011;6(11):e25502.
 24. Lombardo F, Christophides GK. Novel factors of Anopheles gambiae 
haemocyte immune response to Plasmodium berghei infection. Parasit 
Vectors. 2016;9:78.
 25. Criscione F. A mosquito‑specific bZIP transcription factor and the influ‑
ence of a Y‑specific gene on sex determination in Anopheles stephensi. 
Virginia Polytechnic Institute and State University. 2013. https:// vtech 
works. lib. vt. edu/ server/ api/ core/ bitst reams/ 9a507 e7f‑ fd95‑ 47b2‑ 97f4‑ 
77343 5537f 71/ conte nt.
 26. Ewanchuk BW, Arnold CR, Balce DR, Premnath P , Orsetti TL, Warren 
AL, et al. A non‑immunological role for gamma‑interferon‑inducible 
lysosomal thiol reductase (GILT) in osteoclastic bone resorption. Sci Adv. 
2021;7(17):eabd3684.
 27. Balce DR, Allan ERO, McKenna N, Yates RM. gamma‑Interferon‑
inducible lysosomal thiol reductase (GILT) maintains phagosomal 
proteolysis in alternatively activated macrophages. J Biol Chem. 
2014;289(46):31891–904.
 28. Cho WL, Tsao SM, Hays AR, Walter R, Chen JS, Snigirevskaya ES, et al. 
Mosquito cathepsin B‑like protease involved in embryonic degradation 
of vitellin is produced as a latent extraovarian precursor. J Biol Chem. 
1999;274(19):13311–21.
 29. Magnusson K, Mendes AM, Windbichler N, Papathanos PA, Nolan T, 
Dottorini T, et al. Transcription regulation of sex‑biased genes dur‑
ing ontogeny in the malaria vector Anopheles gambiae. PLoS One. 
2011;6(6):e21572.
 30. Tazuke SI, Schulz C, Gilboa L, Fogarty M, Mahowald AP , Guichet A, et al. A 
germline‑specific gap junction protein required for survival of differenti‑
ating early germ cells. Development. 2002;129(10):2529–39.
 31. Ephrussi A, Dickinson LK, Lehmann R. Oskar organizes the germ plasm 
and directs localization of the posterior determinant nanos. Cell. 
1991;66(1):37–50.
 32. Kistler KE, Trcek T, Hurd TR, Chen R, Liang FX, Sall J, et al. Phase transi‑
tioned nuclear Oskar promotes cell division of Drosophila primordial 
germ cells. Elife. 2018;7:e37949.
 33. Ferracchiato S, Catteruccia F, Peirce MJ. 20E‑dependent tyros‑
ine phosphorylation of phospholipase C gamma underpins egg 
development in the malaria vector Anopheles gambiae. bioRxiv. 
2022:2022.09.01.506175. https:// www. biorx iv. org/ conte nt/ 10. 1101/ 2022. 
09. 01. 50617 5v1.
 34. Kanehisa M, Furumichi M, Sato Y, Kawashima M, Ishiguro‑Watanabe M. 
KEGG for taxonomy‑based analysis of pathways and genomes. Nucleic 
Acids Res. 2023;51(D1):D587–92.
 35. Kanehisa M. Toward understanding the origin and evolution of cellular 
organisms. Protein Sci. 2019;28(11):1947–51.
 36. Kanehisa M, Goto S. KEGG: kyoto encyclopedia of genes and genomes. 
Nucleic Acids Res. 2000;28(1):27–30.
 37. Arunachalam B, Pan M, Cresswell P . Intracellular formation and cell 
surface expression of a complex of an intact lysosomal protein and MHC 
class II molecules. J Immunol. 1998;160(12):5797–806.
 38. Liu M, Liu H, Guan X, Ai H, Wu H, Liu P , et al. Characterization and expres‑
sion of gamma‑interferon‑inducible lysosomal thiol reductase (GILT) 
gene in rainbow trout (Oncorhynchus mykiss) with implications for GILT 
in innate immune response. Immunogenetics. 2013;65(12):873–82.
 39. Blandin S, Shiao SH, Moita LF, Janse CJ, Waters AP , Kafatos FC, et al. 
Complement‑like protein TEP1 is a determinant of vectorial capacity in 
the malaria vector Anopheles gambiae. Cell. 2004;116(5):661–70.
 40. Levashina EA, Moita LF, Blandin S, Vriend G, Lagueux M, Kafatos FC. 
Conserved role of a complement‑like protein in phagocytosis revealed by 
dsRNA knockout in cultured cells of the mosquito. Anopheles gambiae 
Cell. 2001;104(5):709–18.
 41. Povelones M, Bhagavatula L, Yassine H, Tan LA, Upton LM, Osta MA, et al. 
The CLIP‑domain serine protease homolog SPCLIP1 regulates comple‑
ment recruitment to microbial surfaces in the malaria mosquito Anoph‑
eles gambiae. PLoS Pathog. 2013;9(9):e1003623.
 42. Dong Y, Aguilar R, Xi Z, Warr E, Mongin E, Dimopoulos G. Anopheles 
gambiae immune responses to human and rodent Plasmodium parasite 
species. PLoS Pathog. 2006;2(6):e52.

Page 12 of 12Arora et al. BMC Genomics           (2024) 25:42 
•
 
fast, convenient online submission
 •
  
thorough peer review by experienced researchers in your ﬁeld
• 
 
rapid publication on acceptance
• 
 
support for research data, including large and complex data types
•
  
gold Open Access which fosters wider collaboration and increased citations 
 
maximum visibility for your research: over 100M website views per year •
  At BMC, research is always in progress.
Learn more biomedcentral.com/submissions
Ready to submit y our researc hReady to submit y our researc h  ?  Choose BMC and benefit fr om: ?  Choose BMC and benefit fr om: 
 43. Gendrin M, Turlure F, Rodgers FH, Cohuet A, Morlais I, Christophides GK. 
The peptidoglycan recognition proteins PGRPLA and PGRPLB regulate 
anopheles immunity to bacteria and affect infection by plasmodium. J 
Innate Immun. 2017;9(4):333–42.
 44. Abraham EG, Pinto SB, Ghosh A, Vanlandingham DL, Budd A, Higgs 
S, et al. An immune‑responsive serpin, SRPN6, mediates mos‑
quito defense against malaria parasites. Proc Natl Acad Sci U S A. 
2005;102(45):16327–32.
 45. Kongton K, McCall K, Phongdara A. Identification of gamma‑interferon‑
inducible lysosomal thiol reductase (GILT) homologues in the fruit fly 
Drosophila melanogaster. Dev Comp Immunol. 2014;44(2):389–96.
 46. Fomenko DE, Gladyshev VN. CxxS: fold‑independent redox motif revealed 
by genome‑wide searches for thiol/disulfide oxidoreductase function. 
Protein Sci. 2002;11(10):2285–96.
 47. Hastings KT, Cresswell P . Disulfide reduction in the endocytic pathway: 
immunological functions of gamma‑interferon‑inducible lysosomal thiol 
reductase. Antioxid Redox Signal. 2011;15(3):657–68.
 48. Schleicher TR, Yang J, Freudzon M, Rembisz A, Craft S, Hamilton M, et al. A 
mosquito salivary gland protein partially inhibits Plasmodium sporozoite 
cell traversal and transmission. Nat Commun. 2018;9(1):2908.
 49. Anelli T, Alessio M, Mezghrani A, Simmen T, Talamo F, Bachi A, et al. ERp44, 
a novel endoplasmic reticulum folding assistant of the thioredoxin family. 
EMBO J. 2002;21(4):835–44.
 50. Norgaard P , Winther JR. Mutation of yeast Eug1p CXXS active sites to 
CXXC results in a dramatic increase in protein disulphide isomerase activ‑
ity. Biochem J. 2001;358(Pt 1):269–74.
 51. Clayton AM, Dong Y, Dimopoulos G. The Anopheles innate immune 
system in the defense against malaria infection. J Innate Immun. 
2014;6(2):169–81.
 52. Reynolds RA, Kwon H, Smith RC. 20‑Hydroxyecdysone primes innate 
immune responses that limit bacterial and malarial parasite survival in 
Anopheles gambiae. mSphere. 2020;5(2):e00983‑19.
 53. Upton LM, Povelones M, Christophides GK. Anopheles gambiae blood 
feeding initiates an anticipatory defense response to Plasmodium 
berghei. J Innate Immun. 2015;7(1):74–86.
 54. Schwenke RA, Lazzaro BP , Wolfner MF. Reproduction‑immunity trade‑offs 
in insects. Annu Rev Entomol. 2016;61:239–56.
 55. Critchlow JT, Prakash A, Zhong KY, Tate AT. Mapping the functional form 
of the trade‑off between infection resistance and reproductive fitness 
under dysregulated immune signaling. bioRxiv. 2023. https:// www. biorx 
iv. org/ conte nt/ 10. 1101/ 2023. 08. 10. 55281 5v1. https:// pubmed. ncbi. nlm. 
nih. gov/ 37645 726/.
 56. Ahmed AM, Hurd H. Immune stimulation and malaria infection impose 
reproductive costs in Anopheles gambiae via follicular apoptosis. 
Microbes Infect. 2006;8(2):308–15.
 57. Wang M, Wang Y, Chang M, Wang X, Shi Z, Raikhel AS, et al. Ecdysone 
signaling mediates the trade‑off between immunity and reproduction 
via suppression of amyloids in the mosquito Aedes aegypti. PLoS Pathog. 
2022;18(9):e1010837.
 58. Shaw WR, Marcenac P , Catteruccia F. Plasmodium development in 
Anopheles: a tale of shared resources. Trends Parasitol. 2022;38(2):124–35.
 59. Nystrand M, Dowling DK. Dose‑dependent effects of an immune chal‑
lenge at both ultimate and proximate levels in Drosophila melanogaster. 
J Evol Biol. 2014;27(5):876–88.
 60. Reynolds RA, Kwon H, Alves ESTL, Olivas J, Vega‑Rodriguez J, Smith RC. 
The 20‑hydroxyecdysone agonist, halofenozide, promotes anti‑Plasmo‑
dium immunity in Anopheles gambiae via the ecdysone receptor. Sci 
Rep. 2020;10(1):21084.
 61. Keith SA. Steroid hormone regulation of innate immunity in Drosophila 
melanogaster. PLoS Genet. 2023;19(6):e1010782.
 62. Rus F, Flatt T, Tong M, Aggarwal K, Okuda K, Kleino A, et al. Ecdysone trig‑
gered PGRP‑LC expression controls Drosophila innate immunity. EMBO J. 
2013;32(11):1626–38.
 63. Terradas G, Hermann A, James AA, McGinnis W, Bier E. High‑resolution 
in situ analysis of Cas9 germline transcript distributions in gene‑drive 
Anopheles mosquitoes. G3 (Bethesda). 2022;12(1):jkab369.
 64. Hammond A, Karlsson X, Morianou I, Kyrou K, Beaghton A, Gribble 
M, et al. Regulating the expression of gene drives is key to increasing 
their invasive potential and the mitigation of resistance. PLoS Genet. 
2021;17(1):e1009321.
 65. Kyrou K, Hammond AM, Galizi R, Kranjc N, Burt A, Beaghton AK, et al. A 
CRISPR‑Cas9 gene drive targeting doublesex causes complete popula‑
tion suppression in caged Anopheles gambiae mosquitoes. Nat Biotech‑
nol. 2018;36(11):1062–6.
 66. Volohonsky G, Terenzi O, Soichot J, Naujoks DA, Nolan T, Windbichler 
N, et al. Tools for Anopheles gambiae Transgenesis. G3 (Bethesda). 
2015;5(6):1151–63.
 67. Hammond A, Galizi R, Kyrou K, Simoni A, Siniscalchi C, Katsanos D, 
et al. A CRISPR‑Cas9 gene drive system targeting female reproduction 
in the malaria mosquito vector Anopheles gambiae. Nat Biotechnol. 
2016;34(1):78–83.
 68. Dong Y, Simoes ML, Marois E, Dimopoulos G. CRISPR/Cas9 ‑mediated 
gene knockout of Anopheles gambiae FREP1 suppresses malaria parasite 
infection. PLoS Pathog. 2018;14(3):e1006898.
 69. Untergasser. RNAprep: Trizol combined with columns. 2008.
 70. Dobin A, Davis CA, Schlesinger F, Drenkow J, Zaleski C, Jha S, et al. STAR: 
ultrafast universal RNA‑seq aligner. Bioinformatics. 2013;29(1):15–21.
 71. Xing Y, Yu T, Wu YN, Roy M, Kim J, Lee C. An expectation‑maximization 
algorithm for probabilistic reconstructions of full‑length isoforms from 
splice graphs. Nucleic Acids Res. 2006;34(10):3150–60.
 72. Wickham H. ggplot2. WIREs Comput Stat. 2011;3(2):180–5.
 73. Arora G, Lynn GE, Tang X, Rosen CE, Hoornstra D, Sajid A, et al. CD55 
facilitates immune evasion by Borrelia crocidurae, an agent of relapsing 
fever. mBio. 2022;13(5):6122.
 74. Szklarczyk D, Kirsch R, Koutrouli M, Nastou K, Mehryary F, Hachilif R, et al. 
The STRING database in 2023: protein‑protein association networks and 
functional enrichment analyses for any sequenced genome of interest. 
Nucleic Acids Res. 2023;51(D1):D638–46.
 75. Snel B, Lehmann G, Bork P , Huynen MA. STRING: a web‑server to retrieve 
and display the repeatedly occurring neighbourhood of a gene. Nucleic 
Acids Res. 2000;28(18):3442–4.
 76. Shannon P , Markiel A, Ozier O, Baliga NS, Wang JT, Ramage D, et al. 
Cytoscape: a software environment for integrated models of biomolecu‑
lar interaction networks. Genome Res. 2003;13(11):2498–504.
 77. Jumper J, Evans R, Pritzel A, Green T, Figurnov M, Ronneberger O, et al. 
Highly accurate protein structure prediction with AlphaFold. Nature. 
2021;596(7873):583–9.
 78. Arora G, Sajid A, Singhal A, Joshi J, Virmani R, Gupta M, et al. Identification 
of Ser/Thr kinase and forkhead associated domains in Mycobacterium 
ulcerans: characterization of novel association between protein kinase Q 
and MupFHA. PLoS Negl Trop Dis. 2014;8(11):e3315.
 79. Sievers F, Wilm A, Dineen D, Gibson TJ, Karplus K, Li W, et al. Fast, scalable 
generation of high‑quality protein multiple sequence alignments using 
Clustal Omega. Mol Syst Biol. 2011;7:539.
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub‑
lished maps and institutional affiliations.