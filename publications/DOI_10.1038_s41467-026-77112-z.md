---
reference_id: DOI:10.1038/s41467-026-77112-z
title: The predicted interactome of the human mitochondrial proteome
authors:
- Abhinav B. Swaminathan
- Mohammad Zulkifli
- Rachel M. Guerra
- Sofia M. Calabrese
- Dimitris T. Kalafatis
- David J. Pagliarini
- Vishal M. Gohil
journal: Nature Communications
year: '2026'
doi: 10.1038/s41467-026-77112-z
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41467-026-77112-z_reference.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s41467-026-77112-z.pdf
---

# The predicted interactome of the human mitochondrial proteome
**Authors:** Abhinav B. Swaminathan, Mohammad Zulkifli, Rachel M. Guerra, Sofia M. Calabrese, Dimitris T. Kalafatis, David J. Pagliarini, Vishal M. Gohil
**Journal:** Nature Communications (2026)
**DOI:** [10.1038/s41467-026-77112-z](https://doi.org/10.1038/s41467-026-77112-z)

## Content

Abstract

                    Despite the fundamental importance of mitochondria in cellular metabolism, the molecular function(s) of many mitochondrial proteins remain unknown. Since protein function can be inferred from their interacting partners, we repurpose the protein structure prediction algorithm AlphaFold Multimer (AFM) as a classification model to predict protein-protein interactions of the entire human mitochondrial proteome. By screening 630,003 protein pairs, we create a compendium of 2,895 previously known and newly observed interactions, which include the interacting partner(s) of 85 uncharacterized mitochondrial proteins, thereby linking them to a known biochemical pathway. Extending the AFM-based analysis to 11 diverse eukaryotes identifies evolutionarily conserved interactions among human hits, including regulators of core bioenergetic pathways. Our experiments, guided by these predictions, nominate protein interactions that form the coenzyme Q metabolon and define the mitochondrial copper delivery pathway to cytochrome
                    c
                    oxidase. Our compendium represents a powerful resource for the systematic, structure-based functionalization of the human mitochondrial proteome.

Article | Article in Press https://doi.org/10.1038/s41467-026-77112-z
The predicted interactome of the human
mitochondrial proteome
Abhinav B. Swaminathan 1 , Mohammad Zulkiﬂi 1,R a c h e lM .G u e r r a2,
Soﬁa M. Calabrese1, Dimitris T. Kalafatis1,D a v i dJ .P a g l i a r i n i2,3,4,5 &
Vishal M. Gohil 1
Despite the fundamental importance of mitochondria in cellular metabolism,
the molecular function of many mitochondrial proteins remains unknown.
Since protein function can be inferred from their interacting partners, we
repurpose the protein structure prediction algorithm AlphaFold Multimer
(AFM) as a classiﬁer model to predict protein-protein interactions of the entire
human mitochondrial proteome. By screening 630,003 protein pairs, we
create a compendium of 2,895 previously known and newly observed inter-
actions, which include the interacting partner(s) of 85 uncharacterized mito-
chondrial proteins, thereby linkingthem to a known biochemical pathway.
Extending the AFM-based analysisto 11 diverse eukaryotes identiﬁes evolu-
tionarily conserved interactions among human hits, including regulators of
core bioenergetic pathways. Our experiments, guided by these predictions,
nominate protein interactions thatform the coenzyme Q metabolon and
deﬁne the mitochondrial copper delivery pathway to cytochromec oxidase.
Our compendium represents a powerful resource for the systematic,
structure-based functionalizationof the human mitochondrial proteome.
Mitochondria house core metabolic pathways for cellular energy
generation and biosynthesis of cofactors essential for cellular and
organismal health
1. Pathogenic mutations have been identi ﬁed in
almost 30% of the ~1100 mitochondrial proteins that result in common
human diseases, as well as rare inborn errors of metabolism2–4.D e s p i t e
their critical roles in cellular functions and human disease, approxi-
mately 10% of the human mitochondrial proteome remains orphan
without an associated pathway annotation or biochemical function
5.
Consequently, regulators and components of some of the core mito-
chondrial metabolic pathways remain to be discovered.
The availability of a well-deﬁned inventory of mitochondrial pro-
teins called MitoCarta
5,6 has spurred many targeted and high-
throughput loss-of-function studies to determine the function of
these poorly characterized proteins
7–15. Complementary approaches,
such as yeast two-hybrid and co-immunoprecipitation-based protein-
protein interaction studies, and more recently, complexome proﬁling,
have been used to elucidate the function of uncharacterized proteins
through the guilt-by-association principle
16–18. However, these
approaches are laborious, time-consuming, and often contaminated
with false positives 19,20, which limits their application in annotating
protein functions in a high-throughput manner. Thus, there is a need
for orthogonal approaches to systematically determine the function of
uncharacterized mitochondrial proteins.
AlphaFold-Multimer (AFM) is a neural network model trained to
predict the structures of multimeric protein complexes of known
stoichiometry and composition
21. Recent studies applying AFM to
small datasets have uncovered its potential to identify interacting
partners of a query protein
22–24. However, the utility of AFM for a large-
scale, ab initio identiﬁcation of protein–protein interactions remains
to be systematically evaluated. In this study, we demonstrate that AFM
Received: 5 November 2025
Accepted: 17 August 2026
Check for updates
1Department of Biochemistry and Biophysics, Texas A&M University, College Station, TX, USA.2Department of Cell Biology and Physiology, Washington
University School of Medicine, St. Louis, MO, USA. 3Department of Biochemistry and Molecular Biophysics, Washington University School of Medicine, St.
Louis, MO, USA. 4Department of Genetics, Washington University School of Medicine, St. Louis, MO, USA.5Howard Hughes Medical Institute, Washington
University School of Medicine, St. Louis, MO, USA. e-mail: abhinav22@tamu.edu; vgohil@tamu.edu
Nature Communications Article in Press
1234567890():,;
1234567890():,;

can be repurposed as a discovery tool that can predict binary protein-
protein interactions in the mitochondrial proteome with 85% preci-
sion. Our dataset, which we have named MitoMatch (mitomatch.web.
app), consists of 2895 interactions and includes at least one interacting
partner for 85% of orphan mitochondrial proteins. We demonstrated
the utility of this resource through experimental validation of our
predictions by nominating direct protein-protein interactions that
form the coenzyme Q metabolon, and by placing poorly characterized
human mitochondrial protein, COA4, at a speci ﬁc step in the mito-
chondrial copper delivery pathway. MitoMatch is a powerful resource
of organelle-wide direct protein-protein interactions to link mito-
chondrial protein(s) to known pathways and help assign their role in
mitochondrial functions.
Results
MitoMatch: human mitochondrial protein interactome
We ﬁrst asked if AFM21 can be repurposed as a classiﬁcation model that
predicts whether two proteins can interact based on the interface
predicted template modeling (ipTM) score (Fig.1a). The ipTM score is
ac o nﬁdence metric that was originally designed to assess the accuracy
of predicted multimeric structures. We asked if we could repurpose
this metric as a classi ﬁer cutoff score to distinguish interacting from
non-interacting protein pairs. In this case, a score of 0 would indicate
no interaction, whereas a score of 1 would indicate a high-conﬁdence
interaction. To accomplish this, we compiled a non-redundant list of
1338 binary interacting pairs and 15,005 non-interacting pairs from
recently deposited PDB structures that were not used for training AFM
(Supplementary Notes). We ran all ﬁve multimer models of AFM with
one random seed, producing ﬁve predictions in total for each inter-
action. We found that the interacting protein pairs have a bimodal
distribution with one prominent peak at ipTM >0.8 and another peak
at an ipTM <0.2, whereas the non-interacting protein pairs have a
single peak at ipTM <0.2 (Fig. 1b). The choice of using either the
maximum ipTM score or the average of all ﬁve ipTM scores did not
markedly affect the distribution of the interacting pairs; however, the
right-sided shoulder of the non-interacting peak was more restricted
when using the mean ipTM score as compared to using just the max-
imum score (Fig. 1b). This suggests that for a high-throughput appli-
cation of AFM, the mean ipTM score will be more informative in
eliminating false positives than simply considering the best model with
the maximum score. This is also reﬂected in the precision-recall curve,
where using the mean ipTM as a classi ﬁer metric yielded ~40% of all
true positives at 90% precision whereas the best ipTM score yielded
only 30% of the true hits at the same precision (Fig. 1c). We analyzed
the key parameters that could in ﬂuence ipTM scores and found that
the primary determinant of AFM success is the multiple sequence
alignment (MSA) depth, where interacting pairs with more than 25
diverse sequences perform well, with median ipTM scores of more
than 0.6, which steadily increases with increasing MSA depth (Sup-
plementary Fig. 1a, b and Supplementary Notes). Our analysis further
revealed that a total number of interface residues of greater than 20
and lower global stoichiometry, de ﬁned as the total number of sub-
units in the protein complex, also increased the ipTM score (Supple-
mentary Fig. 1c–f and Supplementary Notes).
Given that AFM predicts protein-protein interactions with higher
precision when the above-mentioned parameters are met, we asked if
it can be applied to the human mitochondrial proteome. To this end,
we ﬁrst determined the MSA depth of human mitochondrial protein
pairs and found that more than 97% of protein pairs have an MSA
depth of at least 25 sequences (Supplementary Fig. 2a). Next, we set
out to determine the ipTM cut-off score to separate true interactors
from non-interacting protein pairs. To this end, we curated a small test
dataset of mitochondrial protein-protein interactions that have been
experimentally validated (Supplementary Table 1) and compared their
mean and max ipTM score distribution in the background of non-
interacting pairs of mitochondrial proteins. Consistent with our pre-
vious observation (Fig.1b), we ﬁnd that using the mean ipTM score is
better at separating interacting from non-interacting pairs (Supple-
mentary Fig. 2b). The ﬁrst false positive appears around a mean ipTM
score of about 0.5 (Supplementary Fig. 2b, bottom panel), therefore,
we decided to use 0.5 as a cutoff to separate interacting from non-
interacting pairs, which gives 67% recall at a false discovery rate of
about 15% (Supplementary Fig. 2b, c).
MitoCarta3.0, the most well-curated inventory of the human
mitochondria, lists 1136 mitochondrial proteins
5.O ft h e s e ,1 0 1p r o t e i n s
are completely uncharacterized without any pathway annotation. Even
in cases where proteins have a pathway annotation, there are many
instances where their molecular function or their precise position in
the pathway remain obscure. To functionalize the mitochondrial pro-
teome, we applied AFM to predict the interactome of the human
mitochondrial proteins. We ﬁrst parsed the MitoCarta3.0 dataset by
excluding the proteins that have non-canonical amino acids and pro-
teins with more than 2000 amino acids to overcome AFM and com-
putational limitations, respectively, and generated a curated list of 1123
proteins (~99% of mitochondrial proteins) for further analysis (Sup-
plementary Methods). We applied AFM to predict interacting partners
for each of these 1123 proteins by pairing each protein with every other
protein from this list to generate 630,003 protein pairs (see Zenodo
deposition 21232148). AFM predicted most protein pairs to be non-
interacting, with 541,758 protein pairs (86%) having an ipTM score of
less than 0.2 (Supplementary Fig. 2d). Based on our cutoff of 0.5 mean
ipTM score, we predict 2895 interactions (0.46%) involving 1004
proteins at an apparent FDR of 15% (Fig.1d and Supplementary Data 1).
The median number of interacting partners for these 1004 proteins is
4.0 (Supplementary Fig. 2e).
Next, we asked if our mitochondrial interactome predictions
recapitulate known interactions from existing protein-protein interac-
tion databases. Mapping our dataset against STRING, BioGRID, IntAct,
BioPlex, HuRI, and PDB recovered 43% of interactions predicted by
MitoMatch; the remaining 57% were not present in these databases and
thus represent putative previously unreported interactions (Fig.1ea n d
Supplementary Data 2). We also completely recapitulated 56% of indi-
vidual mitochondrial complexes reported in the recently released
‘complex portal’ dataset
25, with an average coverage of 77% proteins per
complex (Supplementary Fig. 3). This includes large mitochondrial
protein complexes, including the mitochondrial ribosomes and oxida-
tive phosphorylation (OxPhos) com plexes for which experimentally
resolved structures exist (Supplementary Fig. 3). Importantly, Mito-
Match provides structures for interactions for which none exists. For
example, MitoMatch predicts the structures of the mitochondrial pro-
cessing peptidase complex (Fig.1f and Supplementary Fig. 4a), gluta-
myl-t-RNA(Gln) amidotransferase complex (Fig.1g and Supplementary
Fig. 4b, c), interaction between Fe-S cluster biogenesis factors BOLA3
and GLRX5 (Fig. 1h and Supplementary Fig. 4d), and the interaction
between mitochondrial OxPhos protein COX2 with its assembly factor
COX20 (Fig. 1i and Supplementary Fig. 4e). In addition to recovering
these known protein-protein interactions, we identi ﬁed at least one
interacting partner for 85 uncharacterized proteins that were dis-
tributed across multiple mitochondrial pathways (Fig.1j). Among these,
we recapitulated interactions reported in two recent studies that linked
the uncharacterized protein TCAIM to OGDH regulation
26 (Fig. 1k, l and
Supplementary Fig. 4f, g) and C16ORF91 to MT-CYB assembly27 (Fig.1m,
n and Supplementary Fig. 4h, i), cross validating these new discoveries.
Evolutionarily conserved interactions
To investigate what fraction of the predicted human mitochondrial
protein interactions are conserved we mapped our 2895 high-
conﬁdence interactions to 11 other evolutionarily distant eukaryotic
organisms—Chimpanzee (P. troglodytes), Mouse (M. musculus), Rat (R.
norvegicus), Frog (X. laevis), Fish (D. rerio), Fly (D. melanogaster), Worm
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

(C. elegans), Slime Mold ( D. discoidium), Plant ( A. thaliana), Fission
yeast ( S. pombe ), and Baker ’sy e a s t(S. cerevisiae, henceforth called
yeast) (Supplementary Table 2). To do this, we ﬁrst identiﬁed homo-
logs of each of 1123 human mitochondrial proteins in these organisms
using the reciprocal best-hit search (Supplementary Fig. 5a and
Supplementary Methods). We then mapped each protein in 2895
human protein pairs to the proteome of these 11 organisms resulting in
2787, 2768, and 383 protein pairs in chimpanzee, mouse, and yeast,
respectively (Supplementary Fig. 5b). We ﬁnd a strong correlation
between ipTM scores of the human hits and higher eukaryotes, and
COX20
COX2
GATB
GATA
GATC
ab
d eg
hi
OGDH
TCAIM
MT-CYB
C16ORF91
(UQCC4)
j k m
n
GLRX5BOLA3
PMPCA
PMPCB
Metabolism
Mitochondrial central dogma
OXPHOS
Mitochondrial dynamics and surveillance
Protein import, sorting and homeostasisSignaling
Small molecule transport
Unknown
c
UQCC1
C16ORF91
(UQCC4)
f
Loss-of-function
characterizationCo-IP In vitro 
biochemistry
ipTM Score
AlphaFold
Multimer
Experimental
Validation
MitoMatch
HSPA9
TCAIM
l
Fig. 1 | Using AlphaFold-Multimer as a classiﬁcation model to predict mito-
chondrial protein-protein interactions. aA schematic showing the application of
AlphaFold-Multimer as a classiﬁer model to predict protein-protein interactions
based on its output: the interface predicted template modeling (ipTM) score and
follow-up experimental validation. Parts of this image were created in BioRender.
Swaminathan, A. (2026) https://BioRender.com/lkvpwscand Swaminathan, A.
(2026) https://BioRender.com/l0d23t7. b A plot of the number of protein-protein
interactions that fall into different ipTM bins for the recent PDB dataset. Solid line
represents the mean ipTM score, and dotted line represents the best ipTM score
from ﬁve different predicted models of interactions. The interacting and non-
interacting groups have sample sizes of 1338 and 15,005 protein pairs, respectively.
c Precision-recall curve ofb at a 1:100 ratio of true:false pairs. The shaded part of
the curve indicates a conﬁdence interval of 95%.d Interaction network of predicted
mitochondrial protein-protein interactions. Proteins are represented as circles, and
the interactions are represented as gray lines. The thickness of lines is proportional
to the mean ipTM scores. Blue dots represent proteins with a MitoCarta pathway
annotation, and black dots represent uncharacterized proteins.e A pie chart of the
predicted mitochondrial interactions mapped to known databases. Predicted
structures of the f mitochondrial processing peptidase complex (PMPCB-PMPCA),
g glutamyl-t-RNA(Gln) amidotransferase complex (GATA-GATB-GATC),
h interaction between Fe-S cluster biogenesis factors (BOLA3-GLRX5), and
i cytochrome c oxidase assembly intermediate (COX2-COX20).j A heat map
depicting the predicted interactions for uncharacterized mitochondrial proteins
across different MitoCarta Pathways. Predicted structures ofk TCAIM-OGDH,
l TCAIM-HSPA9,m C16ORF91-UQCC1, andn C16ORF91-MT-CYB interactions.
Source data are provided as a Source Data ﬁle. Co-IP co-immunoprecipitation.
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

that decreases with more distant homologs (Fig. 2a, Supplementary
Fig. 6 and Supplementary Data 3). Speci ﬁcally, AFM predicts about
93%, 87%, and 44% of the homologous hits to be interacting in chim-
panzee, mouse, and yeast, respectively (Fig. 2b). In addition, we also
devised two metrics to prioritize interactions for downstream experi-
mental follow-up. First, we provide a species score, which is calculated
as the sum of ipTM scores across all species containing homologs of
both proteins in the query pair. Second, we provide a conservation
score which represents the fraction of homologous pairs identiﬁed as
hits in the screen (ipTM ≥0.5). Higher scores in both these metrics
indicate greater conﬁdence in the predicted interaction across species
(Supplementary Data 2).
Next, to determine if these evolutionarily conserved protein-
protein interactions were enriched in certain mitochondrial processes
and pathways, we analyzed all 149 pathways listed in MitoCarta3.0
5.A
distinct high ipTM score pattern emerges at the diagonal, which indi-
cates that interactions between proteins in the same pathway are more
highly conserved than others (Fig. 2c and Supplementary Fig. 7). We
also observed heatmap signatures where interactions of proteins
belonging to two different pathways were conserved across eukar-
yotes, which is more apparent in the yeast heatmap (Fig. 2c). These
were predominantly interactions between proteins belonging to
OxPhos subunits and their corresponding assembly factors, and with
metal cofactors such as copper, Fe-S clusters, and heme pathway
proteins (depicted as green arrows in Fig. 2c).
Using MitoMatch to deﬁne the molecular interactions of the
coenzyme Q complex
To demonstrate the utility of MitoMatch, we focused on the biosyn-
thetic pathway of coenzyme Q (C oQ, ubiquinone), a quinone-
isoprenoid mobile electron carrier that transfers electrons from
OxPhos complexes I/II to III. The biosynthesis of CoQ requires the
concerted action of multiple evolutionarily conserved Coq proteins28.
PDSS1/2 (named Coq1 in S. cerevisiae) synthesizes the polyprenyl pyr-
ophosphate tail, which gets attached to the CoQ head-group precursor
4-hydroxybenzoic acid by Coq2 (Fig.3a). Coq3-7 modify this precursor
D. rerioM. musculus S. cerevisiae
ab
c
Fig. 2 | Evolutionary conserved interactions across different mitochondrial
pathways. a A heatmap of ipTM scores of 2895 interactions between human
mitochondrial protein pairs mapped to 11 other organisms. The color bar repre-
sents the ipTM scores and the lack of color indicates the absence of a homologous
protein pair in that species. b A bar chart depicting the number of homologous
pairs predicted to be interacting or not in the indicated species. c Heatmap
depicting the median ipTM scores of interactions between proteins of each mito-
chondrial pathways in the indicated organisms. The boxes highlighted by green
arrows in the ‘Yeast’ heatmap show clusters of interactions between pathways that
are highly conserved from humans to yeast as explained in the text. Source data are
provided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

Coq6
Coq3
Coq3
Coq5
Coq7
Coq4
Coq9
Coq7
a
k
Matrix
IMM
Complex Q
1 2
3 4 7 9
5 6 8
3
5 9
4
7
......
......
bc
de f
-5 0 5 10 15
0
1
2
3
4
Protein log2 fold-change (Coq11-GFP/WT)
-log10(p-value)
All proteins
FDR < 0.05
CoQ-related
Coq11
Coq3
Coq7
Coq5
Coq9
Coq6
Coq4
-5 0 5 10 15
0
2
4
6
8
Protein log2 fold-change (Coq9-GFP/WT)
-log10(p-value)
Coq6
Coq7
Coq5
Coq9
Coq11
Coq4
Yah1
Coq3
Coq21
All proteins
FDR < 0.05
CoQ-related
-5 0 5 10
0
1
2
3
4
5
Protein log2 fold-change (Coq6-GFP/WT)
-log10(p-value)
Coq6
Coq7
Coq3
Coq5Coq11
Coq9
Coq21
Yah1
Coq4
All proteins
FDR < 0.05
CoQ-related
-5 0 5 10
0
2
4
6
8
Protein log2 fold-change (Coq4-GFP/WT)
-log10(p-value)
Coq6
Coq7
Coq4
Coq3
Coq9
Coq21
Yah1
Coq5Coq11Hfd1
All proteins
FDR < 0.05
CoQ-related
-5 0 5 10
0
1
2
3
4
5
Protein log2 fold-change (Coq5-GFP/WT)
-log10(p-value)
All proteins
FDR < 0.05
CoQ-related
Coq3
Coq5
Coq7
Coq9
Coq4
Coq11Coq6
Coq1
h i
-5 0 5 10
0
2
4
6
Protein log2 fold-change (Coq3-GFP/WT)
-log10(p-value)
Coq3Coq5
Coq6
Coq4
Coq21
Coq9
Coq7
Coq11
Coq1
All proteins
FDR < 0.05
CoQ-related
g
lm n
COQ7
COQ9j
Fig. 3 | Predicting binary interactions of proteins in mitochondrial complex Q.
a A schematic representation of mitochondrial coenzyme Q biosynthetic pathway
involving Coq1–Coq9 proteins. b–g Volcano plot obtained from immunoprecipi-
tation of the indicated GFP-tagged Coq protein followed by mass spectrometry
analysis (n = 3 biological replicates). The data were normalized to immunopreci-
pitation performed in WT mitochondria. Statistical analysis was performed using a
two-sided Student’s t test. h Heatmap depicting ipTM scores of pairwise
interactions of yeast proteins involved in CoQ biosynthesis.i An interaction net-
work of yeast CoQ proteins based on the ipTM scores from (h). j Superposition of
experimentally resolved human COQ7-COQ9 interaction with the predicted COQ7-
COQ9 structure. k–n Predicted structures of the binary interactions of the indi-
cated yeast Coq proteins. Source data are provided as a Source Data ﬁle. ipTM
interface predicted template modeling score.
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

head-group via a series of reactions further aided by Coq8, 9, and 11, to
produce the mature CoQ molecule 28 (Fig. 3a). These head-group
modifying proteins are thought to form a dynamic metabolon com-
plex at the matrix-facing side of the IMM, called complex Q (also called
the CoQ-synthome)
28.
To identify all the components of the CoQ metabolon, we per-
formed co-IP of endogenously tagged Coq1-6, Coq8-9, and Coq11
proteins from chemically cross-linked yeast mitochondria (Fig. 3b–g
and Supplementary Fig. 8). Coq1 and Coq2 did not co-
immunoprecipitate with any other Coq proteins, consistent with the
idea that only proteins related to head-group modi ﬁcation form the
metabolon (Supplementary Fig. 8a, b). Coq3-6, Coq9, and Coq11 con-
sistently co-immunoprecipitated Coq3-7, Coq9, and Coq11, suggesting
that these proteins form a core complex amongst themselves
(Fig. 3b–g). We observed additional known auxiliary factors involved in
CoQ biosynthesis, such as Yah1 and Coq21, in some of our co-IP
experiments (Fig. 3c, e, f). Coq8, an ATPase that supports CoQ bio-
synthesis, only captured Coq3 and itself (Supplementary Fig. 8c). This
is also consistent with prior studies demonstrating that Coq8 activity is
required for metabolon formation and activity
29, but likely only exhi-
bits transient interactions with metabolon proteins.
Although crosslinking mass spectrometry helped identify pro-
teins forming a complex Q metabolon, this approach cannot de ﬁne
direct binary interactions. To delineate direct interactors from indirect
association, we applied AFM to predict binary interactions amongst
known Coq pathway proteins in yeast (Fig. 3h, i). Since our experi-
mental conditions above may preclude select interactions, we inclu-
ded the full set of Coq1-11 in our AFM-based analyses to identify binary
interactors (Fig. 3h). This identiﬁed nine high-conﬁdence interactions
among Coq proteins consistent with our co-IP data. Importantly, many
of these interactions were also identiﬁed in their human counterparts
from our MitoMatch compendium (Supplementary Fig. 9a, b). To date,
only one structure of a complex Q interaction has been solved —the
complex between COQ7 and its auxiliary factor COQ9
30. Encoura-
gingly, our analyses accurately predict the individual human structures
of these proteins and their experimentally de ﬁned binding interface
(Fig. 3j and Supplementary Fig. 10a) and reveal a highly similar com-
plex for the yeast proteins (Fig. 3k and Supplementary Fig. 10b). Our
second top prediction was between Coq3 and Coq6 (Fig. 3h, l and
Supplementary Fig. 10c), which was also reported in a recently avail-
able preprint
31. Given that Coq3 and Coq6 function sequentially in the
CoQ biosynthesis pathway, this interaction is biochemically
meaningful
28. Beyond these, we reveal strong predictions for binary
interactions between head group-modifying enzymes Coq3-Coq5 and
Coq4-Coq7 (Fig. 3m, n and Supplementary Fig. 10d, e), and between
enzymes and auxiliary factors, including Coq6-8, Coq5-9, and Coq7-8
(Supplementary Fig. 11a–c). These predictions may help explain recent
observations regarding the ability of Coq8 to augment the Coq6-
mediated reaction using ancestrally reconstructed versions of the Coq
proteins
32. Finally, our work predicts a robust interaction between
Coq6 and Coq10 (Supplementary Fig. 11d), the latter being a CoQ-
binding protein whose current function is poorly understood, thereby
motivating functional hypotheses.
While this general approach can be extended to predict larger
oligomeric complexes, recent analyses suggest that the complex Q
metabolon is most likely a “statistical complex” with multiple con-
formations rooted in a smaller number of robust binary interactions
31.
Collectively, our work here serves to de ﬁne the complex Q member-
ship and to nominate select interactions as the anchoring interactions
within the metabolon.
Using MitoMatch to deﬁne the mitochondrial copper delivery
pathway
Next, we applied predictions from MitoMatch to elucidate the struc-
tural basis of the mitochondrial copper delivery pathway to the
OxPhos complex IV, also known as cytochromec oxidase (CcO). CcO is
the copper-containing enzyme of the mitochondrial electron transport
chain that uses ~90% of all oxygen consumed by the cell to drive
mitochondrial ATP synthesis
33. The core subunits of CcO, COX1 and
COX2 contain three copper ions that are essential for its catalytic
activity and stability. The delivery and insertion of copper into CcO
subunits is a complex process that requires copper-metallochaperones
and accessory proteins
34. These proteins are localized to the mito-
chondrial intermembrane space (IMS) and the inner mitochondrial
membrane (IMM) and together constitute the mitochondrial copper
delivery pathway (Fig.4a). Despite decades of work, this pathway is not
fully understood with many other poorly characterized, evolutionarily
conserved CcO assembly factors such as COX23, CMC2, PET191, and
COA4 implicated in copper delivery, though their precise position in
the pathway remains unresolved
35–38.T od eﬁne this pathway, we used
AFM to analyze the interactions between all known proteins of the
human copper delivery pathway, along with these four uncharacter-
ized proteins. AFM successfully predicted 8 of the 12 known interac-
tions in the pathway (Fig. 4b), most of which were conserved in yeast
(Fig. 4c). Importantly, the predicted models provide a structural basis
for many steps in the pathway that have evaded structural studies.
These include key steps in copper delivery to the COX2 subunit
involving metallochaperones, COX17, and SCO1, and accessory pro-
teins SCO2, COA6, and COX16 (Supplementary Figs. 12 and 13).
Given that AFM-predicted structural models are consistent with
the molecular function of experimentally characterized proteins, we
wanted to extend the utility of AFM in placing uncharacterized pro-
teins in the copper delivery pathway. We focused on IMS-localized CcO
assembly factors, COX23, CMC2, PET191, and COA4, whose roles in
CcO assembly are not known. AFM predicted evolutionarily conserved
interactions between COX23 and COX1, CMC2 with COX2, and COA4
with COX11 (Fig. 4b, c). Since copper metallochaperone COX11 is the
core member of the mitochondrial copper delivery pathway, we
focused on the COA4-COX11 interaction. The predicted structure of
this interaction is consistent with the localization and topology of
these proteins, where IMS-localized COA4 interacts with the IMS-
facing domain of COX11 (Fig. 4d and Supplementary Fig. 13f). We
experimentally validated our prediction by performing co-
immunoprecipitation (Co-IP) of yeast Coa4-V5 from chemically
cross-linked mitochondria, followed by mass spectrometric analysis,
which identiﬁed Cox11 as its interacting partner (Fig. 4e). In addition,
we also ﬁnd other proteins enriched in our Co-IP-MS data, including
the IMS-localized Ptc5 phosphatase, which suggests a role for this
protein in regulating copper delivery to CcO through reversible
phosphorylation of Coa4 in yeast. To validate this interaction in
humans, we also performed co-IP in mitochondria isolated from 293 T
cells transfected with COA4-V5 and COX11-FLAG constructs. Co-IP of
COX11-FLAG using Anti-FLAG beads recovered COA4-V5 as an inter-
acting partner, validating our prediction (Fig. 4f). We also recovered
COX1 as an interacting partner of COX11 (Fig. 4f), which serves as a
positive control because COX11 is a known metallochaperone of COX1.
A recent study has shown that COX1 and COX2 assembly processes are
highly coordinated, with COX11 also interacting with newly synthe-
sized COX2
39. This is also consistent with our MitoMatch dataset,
which predicts an interaction of COX11 with COX2 (Fig. 4b). Impor-
tantly, we also recover COX2 as an interactor of COX11 in our co-IP
(Fig. 4f), validating both our prediction and reproducing prior results
from others
39. In a reciprocal IP experiment using Anti-V5 beads, we
identiﬁed COX11-FLAG as an interacting partner of COA4 (Fig. 4g),
again validating MitoMatch prediction. Notably, unlike with COX11-IP,
we did not recover COX1 and COX2 proteins in our COA4-V5-IP, which
is in line with our MitoMatch prediction that does not predict direct
interaction between COA4 and either COX1 or COX2.
To understand the biological signiﬁcance of this interaction, we
next set out to determine if the human COA4 plays a role in copper
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

delivery to CcO. To this end, we generated a CRISPR-Cas9-based
knockout of COA4 in a human ﬁbroblast cell line, which showed a
complete absence of COA4 in two independent COA4-KO clones
(Fig. 4h). Consistent with the evidence of direct interaction between
COA4 and COX11, we ﬁnd that the loss of COA4 results in a striking
reduction in COX11 abundance (Fig. 4i). Loss of COA4 also results in
reduced mitochondrial copper content without impacting the levels of
other transition metals (Fig. 4j and Supplementary Fig. 14). Since our
AFM prediction implicates COA4 in copper delivery to COX1 through
its interaction with COX11, we argued that COA4-KO cells would
be sensitive to copper limitation. Indeed, we ﬁnd that the treatment
with increasing concentrations of the copper chelator, bath-
ocuproinedisulfonic acid (BCS), results in a more pronounced reduc-
tion in COX1 abundance in COA4-KO cells as compared to the wild-
type (WT) cells (Fig. 4k). Failure of copper delivery to COX1 is known
to reduce its abundance. To assess if COA4-KO cells exhibit
reduced abundance of COX1-containing complexes, we performed BN-
PAGE followed by western blotting and found a drastic and speci ﬁc
reduction in the levels of complex IV-containing supercomplexes in
COA4-KO mitochondria (Fig. 4l). This decreased abundance of com-
plex IV expectedly resulted in reduced respiration in COA4-KO cells
(Fig. 4m). Taken together, our AFM prediction not only provided the
structural basis of known aspects of the mitochondrial copper delivery
pathway but also guided experiments that placed the uncharacterized
human COA4 protein in the COX11-mediated copper delivery path-
way to CcO.
Matrix
IMS
IMM
COX11
COA4
d
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

Discussion
In an era of arti ﬁcial intelligence where millions of protein structures
are now available through machine learning algorithms such as
AlphaFold2 and ESMFold, de ﬁning their functions is now a grand
challenge in biology
40,41. Even for one of the best studied organelles,
such as the mitochondria, almost 100 resident proteins remain com-
pletely uncharacterized without an associated pathway annotation or
biochemical function
5. Here, we applied the machine learning algo-
rithm AFM to generate a high-con ﬁdence compendium of protein-
protein interactions for the entire human mitochondrial proteome.
This work recapitulated 77% of proteins of the known mitochondrial
protein complexes and predicted previously unreported interactions
for 85% of uncharacterized mitochondrial proteins. Guided by these
predictions, we deﬁned binary interactions and membership amongst
the CoQ metabolon proteins and assigned human COA4 to a speci ﬁc
step in copper delivery to cytochrome c oxidase. Thus, MitoMatch
provides a resource for annotating uncharacterized mitochondrial
proteins by identifying the proteins they interact with. A predicted
interaction with a characterized protein serves as a starting point for
hypothesis generation—the orphan protein may function as a subunit
of the same pathway, a regulatory factor, a chaperone, or an assembly
factor.
One of the strengths of AFM-based protein-protein interaction
predictions is that they solely rely on evolutionary signals found
within and between proteins to predict interaction interfaces in
protein pairs from residue coevolution and are agnostic to biologi-
cal or thermodynamic constraints. As a result, a limitation of this
approach is that it cannot provide binding af ﬁnities of the interac-
tion pair. Further, we note that many of our predicted interactions
could happen in the cell in the context of a larger complex and may
not exist as true heterodimers. Thus, our predictions indicate whe-
ther a given protein pair can interact, but not the biological condi-
tions, stoichiometry, or the complex composition in which that
interaction takes place.
Although AFM was originally developed to predict the structure of
multimeric protein complexes of known stoichiometry, a few recent
studies have explored the potential of AFM to identify new protein-
protein interactions
22–24,42. For example, a recent study utilized AFM
to predict the interacting partners of a protein called DONSON
that was previously implicated in DNA replication
24. This in-silico
screen targeted against ~70 core replication factors identi ﬁed other
replication initiation proteins as interacting partners of DONSON.
However, extending this approach to an unbiased screening against
the entire human proteome was not successful
24. In our study, we
adopt two simple approaches to enable the successful application of
AFM to the entire mitochondrial proteome. First, since cognate
interacting partners should be co-localized, we restricted our search
grid to ~1100 mitochondrial proteins instead of the entire human
proteome, achieving ~20-fold enrichment in true interactions to
begin with. Second, we increased the stringency of our cutoff by
considering a consensus among allﬁve multimer models by taking an
average of the ipTM scores, thereby reducing false positives (Fig. 1c).
Similarly, a recent study developed a scoring algorithm to increase the
accuracy of human AFM predictions by integrating biological infor-
mation about the protein pairs, such as their co-localization, co-
expression, and co-dependency from the DEPMAP dataset
43.Am o r e
recent approach utilized deeper MSAs and a ﬁnetuned version of
RoseTTAFold as a classiﬁer to predict protein-protein interactions for
the human proteome, which recovered 8-22% of true positives 44.
Compared to these approaches that are currently only applicable to
the human proteome, our pipeline is broadly applicable and can be
extended to any organismal proteome, thereby providing a simple and
generalized framework that improves the accuracy of AFM-based
predictions.
Consistent with a previous study
45, which showed that genes
belonging to cofactor and energy metabolism in yeast are replaceable
with their human counterpart, we ﬁnd that evolutionarily conserved
interactions were also highly enriched in these pathways (Fig. 2c).
Building on this ﬁnding, we provide two experimental vignettes that
exemplify the utility of MitoMatch. In theﬁrst example, we focused on
deﬁning the molecular interactions that underpin the complex Q
metabolon. This problem is two-fold—ﬁrst requiring the identiﬁcation
of the components of complex Q, followed by identifying direct
interactions amongst these proteins. We partly address this problem
through cross-linking co-immunoprecipitation mass spectrometry
experiments that identiﬁed the Coq proteins that are a part of the
complex Q metabolon (Fig. 3b–g). However, this experimental data,
just like every other co-immunoprecipitation dataset, does not dis-
tinguish direct interactions from indirect associations. To address this,
we leveraged AFM to predict binary interactions amongst the yeast
Coq proteins, identifying nine high-conﬁdence protein-protein inter-
actions amongst Coq3-10 proteins (Fig. 3h, i). Many of these interac-
tions are also conserved from yeast to humans (Supplementary Fig. 9).
Importantly, AFM accurately reproduces an experimentally resolved
structure of COQ7-COQ9 interaction, while also predicting a similar
structure for the yeast counterpart (Fig. 3j, k). This experimental
structure of COQ7-COQ9 was released after the training cutoff date for
AFM
21,30, and therefore serves as an unbiased validation, highlighting
the robustness with which this approach can be applied to discover
protein-protein interactions. Together, we nominate several binary
interactions that could serve as anchor points for the formation of the
coenzyme Q metabolon. For our second application, we focused on
Fig. 4 | Placing COA4 in the mitochondrial copper delivery pathway to cyto-
chrome c oxidase through the identiﬁcation of its physical interactor. a A
schematic representation of the mitochondrial copper delivery pathway to cyto-
chrome c oxidase (CcO). Copper delivery to COX1 and COX2 subunits of CcO
requires metallochaperones—COX17, SCO1, and COX11—that bind and transfer
copper to their target proteins, and accessory factors such as COX16, COX19, SCO2,
and COA6 that enable this transfer. Intermembrane space (IMS) localized CcO
assembly factors depicted in yellow circles are hypothesized to play a role in copper
delivery.b A heatmap of ipTM scores of the indicated human andc yeast protein
pairs that are either a part of the mitochondrial copper delivery pathway or are
implicated in the copper delivery process. The color bar represents the ipTM score.
d Predicted structure of COA4-COX11 interaction.e A volcano plot of the relative
abundance of proteins immunoprecipitated from V5-tagged Coa4 yeast mitochon-
dria compared to untagged mitochondria versus statistical signiﬁcance (n = 3 bio-
logical replicates). Statistical analysis was performed using a two-sided Student’s t
test.f Co-immunoprecipitation of COX11-FLAG (n =3 )a n dg COA4-V5 from digitonin
solubilized mitochondria of 293 T cellstransfected with COA4-V5 and COX11-FLAG
followed by western blotting (n =3 ) .h SDS-PAGE/western blot analysis of COA4
from WT and COA4-KO MCH58 cell lines. ATP5A is used as a loading control (n =2 ) .
i SDS-PAGE/western blot analysis of COX11 in solubilized mitochondria isolated
from WT and COA4-KO-6 MCH58 cells (n =3 ) .j Mitochondrial Cu levels measured in
WT and COA4-KO-6 mitochondria using inductively coupled plasma–mass spec-
trometry (n = 3). Data are presented as mean ± SD. Statistical analyses were per-
formed using an unpaired two-tailed Student’s t test. k SDS-PAGE/western blot
analysis of COX1 from WT and COA4-KO-6 cells treated with different concentra-
tions of the copper chelator BCS (n =3 ) .l BN-PAGE/western blot analysis of WT and
COA4-KO-6 mitochondria isolated from cells grown with and without BCS (n =2 ) .
m Oxygen consumption rate measurements of WT and COA4-KO-6 MCH58 cells
following treatment with ATP synthase inhibitor (Oligomycin), uncoupler (CCCP),
and electron transport inhibitor (Antimycin A) (n = 3). Data are presented as
mean ± SEM. Statistical analyses were performed using ordinary one-way ANOVA. All
sample sizes in this ﬁgure represent biological replicates from independent
experiments. Statistical signiﬁcance levels: **p
< 0.01; ****p < 0.0001. Western blots
are representative of the indicated numberof independent biological replicates.
Source data are provided as a Source Dataﬁle. OMM outer mitochondrial mem-
brane, IMM inner mitochondrial membrane.
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

assigning a protein to a speci ﬁc step in the mitochondrial copper
delivery pathway to CcO. AFM predicted an evolutionarily conserved
interaction between the mitochondrial protein COA4 and COX11, the
copper metallochaperone for CcO
46 (Fig. 4b–d). Co-IP conﬁrmed this
interaction (Fig. 4e–g) and provided a biochemical basis for a prior
observation showing rescue of the respiratory growth defect of yeast
coa4Δ by Cox11 overexpression
38. Together, these results placed COA4
in a COX11-dependent step of copper delivery to CcO. Based on these
experimental vignettes, we antici pate that MitoMatch will greatly
accelerate the functionalization of the human mitochondrial
proteome.
Methods
AlphaFold Multimer pipeline for high-throughput protein-pro-
tein interaction prediction
We used AlphaFold Multimer algorithm to generate multiple
sequence alignments (MSA) of input protein sequences. Since MSA
generation for a protein is independent of what protein it is paired
with, we split the AlphaFold Multimer pipeline into MSA generation
and prediction steps, thereby eliminating the time-consuming
steps of repeated MSA generation for each prediction. In the MSA
generation step, we compute alignments using the default Multimer
pipeline, identify templates with a max cut-off date of 2018-04-30,
generate features, and store the features as a pickle ﬁle. In the pre-
diction step, we read these pickle ﬁl e st om a k eu s eo ft h e s ep r e -
computed alignment features for all input proteins, and the default
prediction pipeline is followed including MSA pairing and structure
prediction.
Curating a recent PDB dataset for using AlphaFold Multimer as a
classiﬁer model
Our recent PDB dataset consists of dimers, binary pairs from oligo-
meric complexes, and non-interacting protein pairs from the PDB.
Since AlphaFold-Multimer v2.2 was trained on structures deposited
before 2018-04-30, we only considered structures deposited after this
date for the recent PDB dataset. We downloaded the PDB mmcif ﬁles
and PDB bioassembly ﬁles on 2022-12-18, our “recent” PDB data con-
sisted of protein structures deposited between these two dates. We
only considered bioassemblies that had a global stoichiometry
between 2–100 chains, discarding monomers. For bioassemblies that
had more than 2 chains, we decomposed them into binary pairs by
pairing each protein chain with every other protein chain in that
assembly and categorizing them into interacting and non-interacting
protein pairs. We consider a protein pair, say ‘A-B’, as interacting if at
least one heavy (non-hydrogen) atom of protein ‘A’ is within 4 Å of
another heavy atom of protein ‘B’. We enforced the following criteria
f o ra n yp r o t e i np a i rt ob ei n c l u d e df u r t h e r-b o t hp r o t e i n ss h o u l db ea n
L-polypeptide containing only 20 canonical amino acids, each should
have a length of at least 50 amino acids and a total length of less than
2000 amino acids, and the pair should be heteromers and from the
same species. These were then furtherﬁltered with a strategy similar to
what DeepMind used to validate their Multimer model
29.B r i eﬂy, we
performed sequence alignment using MMseqs2 against sequences of
the training dataset (structures deposited before 2018-04-30) and
removed any protein pair, even if only one of the proteins has more
than 40% sequence identity to the training dataset. For the dimer
dataset, we simplyﬁltered protein pairs whose global stoichiometry is
2 subunits. For binary protein pairs from oligomers, we only con-
sidered core interactions in the complex that are both minimalistic and
essential to build the oligomeric complex (refer Supplementary
Methods). For the non-interacting dataset, we selected protein pairs
that are not interacting.
For each of these datasets, we clustered the proteins at 40%
sequence identity using MMseqs2 and gave each cluster an identiﬁer.
We then mapped the protein pair to a cluster pair, which is simply the
union of the cluster identiﬁers of its individual proteins. We grouped
all protein pairs that belong to a cluster pair and randomly selected
one representative interaction from each cluster. This resulted in 110
binary pairs from dimers and 1228 binary pairs from oligomers. For the
non-interacting dataset, after mapping a protein pair to a cluster pair,
we only selected those clusters where all protein pairs in that cluster
were non-interacting and randomly selected a representative protein
pair from each cluster pair, resulting in 15,509 pairs. Finally, we map-
ped these pairs to the entire PDB regardless of the release date and
removed any pair whose proteins share sequence homology with
another interacting pair in any structure, resulting in 15,005 non-
interacting protein pairs.
Mitochondrial test dataset
We manually curated a list of 12 interactions that were experimentally
validated in the copper delivery pathway to the mitochondrial cyto-
chrome c oxidase (Supplementary Table 1). Apart from COX1-COX11
interaction, all other interactions were previously validated using
puriﬁed proteins. Many of these interactions are thought to be of a
transient nature, and most of them do not have an experimentally
solved structure. These 12 interactions constitute the interacting
dataset. To generate a non-interacting dataset, we reasoned that pro-
teins involved in copper delivery to CcO will not interact with proteins
of OxPhos complex I, II, III, and V because only complex IV contains
copper. Therefore, we paired 7 proteins in MitoCarta3.0 that were
annotated as “Metabolism > Metals and cofactors > Copper metabo-
lism” with 115 proteins annotated as OXPHOS complex I, II, III, and V
subunits or their assembly factors, resulting in 805 non-
interacting pairs.
Calculation of total interface residues
The total interface residues of an interacting protein pair A-B are
deﬁned as the sum of interacting residues in both proteins A and B. An
interacting residue of protein A is deﬁned as any residue in protein A
whose heavy atoms are within 4 Å to any heavy atom in protein B, and
vice versa. We implemented a Python script using the NeighborSearch
function of BioPython for this calculation (Supplementary Methods).
Calculation of median per-residue effective (Neff) multiple
sequence alignment (MSA) depth
The default setting of AFM involves pairing MSA of both query proteins
from the same species while block-diagonalizing the rest. Since the
paired MSA part is rich in coevolutionary information between two
proteins, we calculated the MSA depth of the paired MSA part only. We
ﬁrst ﬁltered the paired MSA from the total MSA. For each residue in the
query protein, we only consider those sequences that have a non-gap
residue at that position in the MSA. We then cluster these sequences at
80% sequence identity and count the number of clusters, which gives
us the effective number of sequences or the effective MSA depth at
that position. We do this for each residue of the query sequence, and
the median of all the effective MSA depths at each position is referred
to as the median per-residue N
eff MSA depth. Details of the calculation,
along with the code, are provided in supplementary methods.
Human mitochondrial interaction prediction
We obtained the list of 1136 human genes encoding mitochondrial
proteins from the MitoCarta3.0 repository. We updated the genes
whose UniProt IDs were missing or outdated in MitoCarta3.0 and
removed unreviewed entries that could not be mapped to reviewed
ones. We then removed proteins that were more than 2000 amino
acids long and those that contained non-canonical amino acids. This
resulted in 1123 proteins. Heteromeric combinations of these proteins
resulted in 630,003 binary protein pairs that were used for our mito-
chondrial protein-protein interaction prediction.
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

Identifying homologs of human mitochondrial proteins in other
eukaryotic organisms
The human proteome and proteomes of the 11 other eukaryotic
organisms were downloaded from UniProt. We performed a ‘recipro-
cal best hit’ search to identify the homologs of human mitochondrial
proteins. Brieﬂy, we performed a sequence alignment of each human
mitochondrial “query” p r o t e i na g a i n s tt h ep r o t e o m eo ft h et a r g e t
eukaryotic organism using Mmseqs2 and retrieved the best hit (lowest
e-value). This best hit is considered the homolog of the query protein if
a sequence alignment of this best hit against the human proteome
retrieves the query protein as the best hit. Since we already begin with
a human mitochondrial interaction dataset that is enriched in true
interactions, we relaxed our criteria for identifying evolutionary hits by
considering an interaction in the homologous pairs to be true if at least
one predicted model has an ipTM score above our threshold of 0.5.
Yeast culturing
YPD media was prepared with 1% yeast extract, 2% peptone, and 2%
glucose, while YPGE media was prepared with 1% yeast extract, 2%
peptone, 3% Glycerol, and 1% ethanol. The media pH was adjusted to
5.5. Yeast primary cultures were grown in YPD media overnight at
30 °C. Secondary cultures were inoculated at 0.1 OD
600nm and were
grown in YPGE media at 30 °C till the mid-log phase, and cells were
harvested.
Yeast transformation
Yeast transformation was performed as described before 47.B r i eﬂy,
cells were grown in YPD overnight at 30 °C and were washed and
r e s u s p e n d e di no n e - s t e pb u f f e r( 0 .2 N Lithium acetate, 40% PEG 3350,
and 100 mM dithiothreitol (DTT)) along with 1µgo fp l a s m i dD N Aa n d
50 µg of salmon sperm DNA. The mixture was incubated at room
temperature for 25 min, 42 °C for 20 min, followed by incubation on
ice for 5 min. Cells were then pelleted, washed, and plated on appro-
priate selection plates and incubated at 30 °C for about 2 –3d a y s t o
obtain colonies.
Mammalian cell culture
The human MCH58 cells were cultured in high-glucose Gibco Dul-
becco’sM o d iﬁed Eagle Medium (DMEM, Thermo #11995065) media
supplemented with 10% fetal bovine serum (FBS) (Sigma #F2442). Cells
were cultured in 5% CO
2 at 37 °C. Growth in galactose media was
performed by adding 10 mM galactose and 1 mM pyruvate in glucose-
free media (DMEM, Thermo# 11966025).
Mammalian CRISPR-Cas9-based gene knockout
We used lentiCRISPRv2 plasmid (Addgene #52961) to construct
CRISPR/Cas9-based COA4 knockout in human MCH58 cell line. The
guide RNA sequences targeting COA4 gene are: sgCOA4_1For:CAC
CGACGGGTGAAGAAAGACGATG sgCOA4_1Rev:AAACCATCGTCTTTC
TTCACCCGTC sgCOA4_2For:CACCGAGGCCATACCTGGACCCAAC sg
COA4_2Rev:AAACGTTGGGTCCAGGTATGGCCTC
sgCOA4_3For:CACCGCAGGTGCAGGCGTTCAAGGA
sgCOA4_3Rev: AAACTCCTTGAACGCCTGCACCTGC
LentiCRISPRv2 plasmid vector backbone was digested using
BsmBI restriction enzyme followed by T4 ligation of the digested
vector with the phosphorylated and annealed oligo pairs. The ligated
constructs were ampli ﬁed in the Stbl3 Escherichia coli strain and
sequence veriﬁed. Lentiviral particles were prepared using standard
protocols. Transduction using the lentivirus was performed in MCH58
WT cells using 8 μg/mL polybrene (EMD Millipore). After 24-h incu-
bation, the virus-containing medium was removed, and a fresh culture
medium containing puromycin/blasticidin was added and selected for
72 h. Cells were then trypsinized, diluted, and plated at a density of 1
cell per well in 96-well plates. A clonal population was established in
the selection medium containing 2.5 µg/ml puromycin. Disruption of
the COA4 was conﬁrmed by western blotting.
Mitochondrial isolation
Crude mitochondria from yeast cells were isolated as described
previously48.Y e a s tc e l l sw e r eg r o w ni n1 0 0–500 mL of YPGE media and
were harvested at mid-log phase. The cell pellet (2–10 g) was incubated
in DTT buffer (100 mM Tris-HCl, pH 9.4, 10 mM DTT, at 2 mL/g of cells)
for 20 min at 30 °C. Cells were then pelleted, washed in zymolyase
buffer (1.2 M sorbitol, 20 mM potassium phosphate, pH 7.4 at 7 mL/g
of cells), and resuspended in zymolyase buffer containing 3 mg
zymolyase (US Biological Life Sciences) per gram of cell pellet. The cell
suspension was incubated at 30 °C for 45 min. The ef ﬁciency of
digestion was checked spectrophotometrically by diluting zymolyase-
treated cells in water and measuring optical density at 600 nm.
Spheroplasts, thus obtained, were pelleted at 3000 × g for 5 min and
were homogenized in homogenization buffer (0.6 M sorbitol, 10 mM
Tris-HCl, pH 7.4, 1 mM EDTA, 1 mM PMSF, 0.2% (w/v) BSA (essentially
fatty acid-free, Sigma-Aldrich) at 6.5 mL/g of cells) with 15 strokes using
ag l a s sT eﬂon homogenizer with pestle B. The homogenate was then
diluted in an equal volume of homogenization buffer and centrifuged
at 1500 × g for 5 min at 4 °C. The supernatant was centrifuged again at
4000 × g for 5 min at 4 °C, and theﬁnal supernatant was centrifuged at
12,000 ×g at 4 °C for 15 min to pellet mitochondria. Mitochondria were
resuspended in SEM buffer (250 mM sucrose, 1 mM EDTA, 10 mM
MOPS-KOH, pH 7.2, containing 1× EDTA-free protease-inhibitor cock-
tail from Roche).
Crude mitochondria from mammalian cells were isolated using
the Abcam mitochondrial isolation kit for cultured cells (ab110170) by
following the manufacturer ’s instructions. Protease inhibitor was
added to all the buffers used (1× EDTA-free protease-inhibitor cocktail
from Roche). Brie ﬂy, cells harvested from 2 –4 15-cm plates were
incubated in buffer A for 10 min and homogenized with 30 strokes.
The solution was centrifuged at 1000 × g for 10 min and the super-
natant (SN1) was collected while the pellet was resuspended in buffer B
and homogenized with 30 strokes. The supernatant (SN2) was col-
lected by pelleting the solution at 1000 × g for 10 min. The super-
natants SN1 and SN2 were combined and pelleted at 12,000 × g for
15 min to obtain the crude mitochondrial pellet. The pellet was resus-
pended in buffer C and was ﬂash-frozen in liquid nitrogen and stored
at −80 °C.
Co-immunoprecipitation experiments
For the yeast co-immunoprecipitation (co-IP) experiments, mito-
chondria isolated from yeast cells expressing GFP-tagged or V5-tagged
target proteins wereﬁrst cross-linked with the 0.5 mM DSSO (Thermo
#A33545) crosslinker for 1 h at room temperature. The crosslinking was
quenched with 100 mM Tris (pH 8.0) buffer.
For co-IP experiments in human cell line, 293 T cells (ATCC CRL-
3216) were transfected with COA4-V5-pcDNA3.1-Blast and COX11-
FLAG-pcDNA3.1-Neo using PEIMAX (Polysciences # 24765-100). Brieﬂy,
15 million 293 T cells cultured in 15 cm plates were transfected using
15 µg of each plasmid and 90µlo fP E I M A X ( 1µg/µl) for 48 h and the cells
were harvested by scraping. Mitochondria (~2 mg) isolated from these
cells were used for each co-IP experiment.
Mitochondria were solubilized with digitonin and incubated with
magnetic beads conjugated with anti-V5 or anti-GFP or anti-FLAG
antibodies. The antibody-conjugated beads were pulled down with a
magnet. The beads were washed, and the proteins were analyzed using
mass spectrometry or western blotting. All Co-IP experiments were
performed with n = 3 biological replicates. Statistical analysis was
performed using a two-sided Student’s t test.
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

Crosslinking afﬁnity enrichment mass spectrometry
Crude mitochondria were isolated from yeast (expressing GFP-tagged
or V5-tagged target proteins) as described above and subjected to
chemical crosslinking (1 mg mitochondria, 0.5 mM DSSO (Thermo,
catalog no. A33433), 1 h, room temperature [r.t.]). Crosslinking was
quenched with 100 mM Tris pH 8.0 followed by centrifugation
(15,000 ×g, 5 min, 4 °C). Mitochondria were then solubilized with
50 mM imidazole, 500 mM 6-hexaminocaproic acid, 1 mM EDTA and
1 g/g digitonin. The bait protein and crosslinked interactors were then
enriched by anti-GFP or anti-V5 immunoprecipitation (IP) using mag-
netic GFP-Trap or V5-Trap agarose beads (Chromotek, catalog no.
gtma or v5ta), respectively, washed and subjected to on-bead tryptic
digest. The on-bead crosslinked proteins were denatured with 2 M urea
i n 2 0 0m M T r i sp H 8 . 0 , t h e n r e d u c e d w i t h 5m MD T T ( 3 0m i n , 5 6° C )
and alkylated with 15 mM iodoacetamide (30 min, r.t., in the dark). The
proteins on-bead were digested (overnight, 37 °C) with 1 μgt r y p s i n
(Promega, catalog no. V5113). The digested supernatant was acidiﬁed
with 10% Tri ﬂuoroacetic acid (TFA) to a pH of 2 and desalted with
10 mg StrataX solid phase extraction columns (Phenomenex), then
dried under vacuum using a SpeedVac (Thermo Scientiﬁc) and stored
at −80 °C until MS analysis.
Samples were resuspended in 0.2% formic acid and subjected to
LC–MS analysis. LC separation was performed using the Thermo Ulti-
mate 3000 RSLCnano system. A 15 cm EASY-Spray PepMap RSLC C18
column (150 mm × 75μm, 3 μm) was used at 300 nL/minﬂow rate with
a 90 min gradient using mobile phase A consisting of 0.1% formic acid
in H
2O, and mobile phase B consisting of 0.1% formic acid in acetoni-
trile (ACN)/H2O (80/20, v/v). An EASY-Spray source was used at 35 °C.
Each sample run was held at 4.0% B for 5 min and increased to 50% B
over 65 min, followed by 8 min at 95% B and back to 4% B for equili-
bration for 10 min. An Acclaim PepMap C18 HPLC trap column
(20 mm × 75μm, 3 μm) was used for sample loading. MS detection was
performed with a Thermo Exploris 240 Orbitrap mass spectrometer in
positive mode. The source voltage was set to 1.8 kV, ion transfer tube
temperature was set to 275 °C, RF lens was at 70%. Full MS spectra were
acquired from m/z 350 to 1400 at the Orbitrap resolution of 60,000,
with the normalized automatic gain control target of 300% (3 × 10
6).
Data-dependent acquisition (DDA) was performed for the top 20
precursor ions with the charge state of 2–6 and an isolated width of 2.
Intensity threshold was 5 × 103. Dynamic exclusion was 30 s with the
exclusion of isotopes. Other settings for DDA include Orbitrap reso-
lution of 15,000 and high-energy collision-induced dissociation
energy of 30%.
Raw ﬁles were analyzed by SequestHT search engine incorporated
in Proteome Discoverer v.2.5.0.400 software against yeast databases
downloaded from Uniprot. Label-free quanti ﬁcation was enabled in
the searches. The resulting data were analyzed by Perseus
v.1.6.15.0 software
49.
Inductively coupled plasma–mass spectrometry
Metals (Cu, Fe, Zn, Mn) levels were quantiﬁed by inductively coupled
plasma mass spectrometry (ICP-MS) using a NexION 300D instrument
(PerkinElmer). Brieﬂy, 60–100 mg of mitochondria were collected and
washed twice with 1 mL of 300 mM mannitol containing 100μME D T A
prepared in ultrapure, metal-free water (Trace SELECT; Sigma), fol-
lowed by two additional washes with 300 mM mannitol to remove
residual EDTA. After washing, pellets were weighed and digested in
40% (w/v) nitric acid (Trace SELECT; Sigma) at 90 °C for 18 h. This was
followed by an additional 4 h digestion with 0.75% H ₂O₂ (Sigma
Supelco). The digested samples were then diluted to aﬁnal volume of
5 mL with ultrapure water prior to ICP-MS analysis.
Oxygen consumption rate measurements
Oxygen consumption rate (OCR) measurements were carried out in
intact cells using Seahorse XFe24 extracellular ﬂux analyzer (Agilent
Technologies). Brieﬂy, cells were seeded in XF24-well cell culture
microplates (Agilent Technologies) at 20,000 cells/well in 250 µlo f
growth media in high glucose DMEM growth media supplemented
with 10% FBS and incubated at 37 °C in a 5% CO
2 incubator for ∼20 h.
Before measurements, 525µl of the pre-warmed growth medium was
added to each well, and cells were further incubated at 37 °C for 30 min
in a non-CO
2 incubator. Mix, wait, and measure timings were set to 2, 2,
and 2 min, respectively. For the mitochondrial stress test, oligomycin,
carbonyl cyanide 3-cholorophenylhydrazone (CCCP), and antimycin A
were sequentially injected to achieve ﬁnal concentrations of 0.5, 20,
and 1 µM, respectively.
SDS-PAGE, BN-PAGE, and western blotting
Protein concentrations in cellular or mitochondrial lysates were mea-
sured using Pierce BCA Protein Assay Kit (Thermo Fisher Scienti ﬁc).
The samples for sodium dodecyl sulfate-polyacrylamide gel electro-
phoresis (SDS-PAGE) wereﬁrst denatured by the addition of LDS buffer
and reducing agent followed by heating at 70 °C for 10 min. A total of
20 µg of the denatured protein extracts were then separated using
NuPAGE 12% Bis-Tris gels (Thermo Fisher Scientiﬁc) and blotted onto a
polyvinylidene diﬂuoride (PVDF) membrane.
Blue native-polyacrylamide gel electrophoresis (BN-PAGE) sam-
ples were prepared by solubilizing crude mitochondria in 1% digitonin,
followed by incubation on ice for 30 min and centrifugation at
20,000 ×g for 30 min. The supernatant was collected, and G-250
sample additive was added to it. The solubilized mitochondrial pro-
teins (20 µg) were separated using 3 –12% Bis-Tris NativePAGE gel
(Thermo Fisher Scientiﬁc) and were transferred onto a PVDF mem-
brane for western blotting.
All PVDF membranes were blocked for 1 h in 5% (w/v) nonfat milk
dissolved in Tris-buffered saline with 0.1% (w/v) Tween 20 (TBST-milk),
followed by overnight incubation with a primary antibody in TBST-
milk at 4 °C. Primary antibodies were used at the following dilutions.
COA4, 1:500 (ab105678; Abcam); Anti-V5, 1:1000 (R96025; Invitrogen);
COX11, 1:500 (11498-1-AP; ProteinTech); PDH1A, 1:1000 (ab168379;
Abcam); NDUFB8, 1:1000 (ab110242; Abcam) SDHB, 1:1000 (ab14714;
Abcam); UQCRFS1, 1:1000 (ab14746; Abcam); COX1, 1:1000 (ab14705;
Abcam); COX2, 1:1000 (ab198286; Abcam); ATP5A, 1:20,000 (ab14748;
Abcam); ACO2, 1:500 (MA535527; Thermo Fisher Scienti ﬁc). After
incubation with the primary anti body, the membranes were washed
ﬁve times with TBST containing (0.1% TWEEN 20) buffer for 5 min each
and incubated at room temperature with (1:5000) horseradish
peroxidase-conjugated secondary antibody (anti-rabbit, Cat. No.
32460, Thermo Fisher Scienti ﬁc or anti-mouse, Cat. No. 95017-332,
VWR) prepared in 5% TBST-milk. After 60 min, the secondary antibody
was discarded, and the membranes were washedﬁve times with TBST
buffer for 5 min each. Secondary antibodies (GE healthcare) were used
at 1:5000 dilution in TBST-milk for 1 h at room temperature. Mem-
branes were developed using Clarity Western ECL substrate (Bio-Rad,
#1705060), or Clarity Max Western ECL substrate (Bio-Rad, #1705062).
Uncropped blots can be found in the Source Data ﬁle.
Statistical analysis
GraphPad Prism v11.0 software was used to plot graphs and bar
charts. Statistical analyses were performed using unpaired two-tailed
Student’s t test and the level of signi ﬁcance was indicated as
stars representing p values in the ﬁgures. The bar height and error
bars in bar graphs of experimental data represent mean and
standard deviation, respectively, from 3 biological replicates. Co-
variates such as cell line passage number were accounted for by using
similar passages for control and knockout lines. Effect sizes are
reported as the log ₂ fold change ( x-axis) in the volcano plots of
immunoprecipitation–mass spectrometry experiments (Figs. 3b–g
and 4e). For other quantitative comparisons, effect sizes correspond to
the difference in group means, which can be derived from the mean
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

and standard deviation values provided in the source data. Addition-
ally, the number of biological replicates for eachﬁgure are provided in
the ﬁgure legends.
Figure generation
The data from our computational work were plotted andﬁgures were
generated using matplotlib v3.10.5 and seaborn v0.12.2 modules in
Python. The protein-protein interaction network was created using
Cytoscape v10.3 ( https://cytoscape.org/). Protein structures were
visualized using UCSF ChimeraX v1.8 ( https://www.cgl.ucsf.edu/
chimerax/). Graphs related to experimental data were plotted using
GraphPad Prism v11.0.
Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Data availability
The computational data generated in this study have been deposited in
the Zenodo database under accession code21232148. This includes the
predicted structures, conﬁdence metrics such as pLDDT and predicted
aligned error data. The structures and the conﬁdence metrics can also
be downloaded from the MitoMatch website [mitomatch.web.app].
The Mass Spectrometry data relevant to the Co-IP experiments have
been deposited in the MassIVE database under accession code
MSV000102370 [ https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?
task=ed4f2a9140d44b61ade526149edaf3d8]. Source data for the ﬁg-
ures in this manuscript are also provided as a Source Data ﬁle.
Reagents generated in this study are available upon request. Source
data are provided with this paper.
Code availability
All original code has been provided in the Supplementary Methods or
in Zenodo (https://doi.org/10.5281/zenodo.21232148).
References
1. Suomalainen, A. & Nunnari, J. Mitochondria at the crossroads of
health and disease. Cell 187,2 6 0 1– 2627 (2024).
2. Vafai, S. B. & Mootha, V. K. Mitochondrial disorders as windows into
an ancient organelle.Nature 491,3 7 4– 383 (2012).
3. Koopman, W. J., Willems, P. H. & Smeitink, J. A. Monogenic mito-
chondrial disorders.N. Engl. J. Med. 366, 1132– 1141 (2012).
4 . G o r m a n ,G .S .e ta l .M i t o c h o n d r i a ld i s e a s e s .Nat. Rev. Dis. Prim. 2,
16080 (2016).
5. Rath, S. et al. MitoCarta3.0: an updated mitochondrial proteome
now with sub-organelle localization and pathway annotations.
Nucleic Acids Res. 49,D 1 5 4 1– D1547 (2021).
6. Pagliarini, D. J. et al. A mitochond rial protein compendium eluci-
dates complex I disease biology.Cell 134, 112– 123 (2008).
7. Vukotic, M. et al. Rcf1 mediates cytochrome oxidase assembly and
respirasome formation, revealing heterogeneity of the enzyme
complex. Cell Metab. 15,3 3 6– 347 (2012).
8. Van Vranken, J. G. et al. SDHAF4 promotes mitochondrial succinate
dehydrogenase activity and prevents neurodegeneration.Cell
Metab. 20,2 4 1– 252 (2014).
9. Ghosh, A. et al. Copper supplementation restores cytochrome c
oxidase assembly defect in a mitochondrial disease model of COA6
deﬁciency. Hum. Mol. Genet. 23,3 5 9 6– 3606 (2014).
10. Zulki ﬂi, M. et al. Yeast homologs of human MCUR1 regulate
mitochondrial proline metabolism.Nat. Commun. 11, 4866
(2020).
11. Baughman, J. M. et al. Integrative genomics identi ﬁes MCU as an
essential component of the mitochondrial calcium uniporter.Nat-
ure 476,3 4 1– 345 (2011).
12. Perocchi, F. et al. MICU1 encodes a mitochondrial EF hand protein
required for Ca(2+) uptake.Nature 467,2 9 1– 296 (2010).
13. Arroyo, J. D. et al. A genome-wide CRISPR death screen identi ﬁes
genes essential for oxidative phosphorylation.Cell Metab. 24,
875– 885 (2016).
14. Rensvold, J. W. et al. De ﬁning mitochondrial protein functions
through deep multiomic proﬁling. Nature 606,3 8 2– 388
(2022).
15. Stefely, J. A. et al. Mitochondrial protein functions elucidated by
multi-omic mass spectrometry proﬁling. Nat. Biotechnol.34,
1191– 1197 (2016).
16. Luck, K. et al. A reference map of the human binary protein inter-
actome. Nature 580,4 0 2– 408 (2020).
17. Huttlin, E. L. et al. Dual proteome-scale networks reveal cell-speciﬁc
remodeling of the human interactome.Cell 184,
3022– 3040.e3028 (2021).
18. Schulte, U. et al. Mitochondrial complexome reveals quality-control
pathways of protein import.Nature 614,1 5 3– 159 (2023).
19. Kuchaiev, O., Rasajski, M., Higham, D. J. & Przulj, N. Geometric de-
noising of protein-protein interaction networks.PLoS Comput. Biol.
5,e 1 0 0 0 4 5 4( 2 0 0 9 ) .
2 0 . M a c k a y ,J .P . ,S u n d e ,M . ,L o w r y ,J .A . ,C r o s s l e y ,M .&M a t t h e w s ,J .M .
Protein interactions: is seeing believing?Trends Biochem. Sci. 32,
530– 531 (2007).
21. Evans, R. et al. Protein complex prediction with AlphaFold-
Multimer. bioRxiv https://doi.org/10.1101/2021.10.04.
463034 (2022).
22. Burke, D. F. et al. Towards a structurally resolved human protein
interaction network.Nat. Struct. Mol. Biol. 30,2 1 6– 225 (2023).
23. Homma, F., Huang, J. & van der Hoorn, R. A. L. AlphaFold-Multimer
predicts cross-kingdom interactions at the plant-pathogen inter-
face. Nat. Commun. 14,6 0 4 0( 2 0 2 3 ) .
24. Lim, Y. et al. In silico protein interaction screening uncovers DON-
SON’s role in replication initiation.Science 381, eadi3448 (2023).
25. Balu, S. et al. Complex portal 2025: predicted human complexes
and enhanced visualisation tools for the comparison of orthologous
and paralogous complexes.Nucleic Acids Res. 53,
D644– D650 (2025).
26. Jiahui, W. et al. The mitochondrial DNAJC co-chaperone TCAIM
reduces alpha-ketoglutarate dehydrogenase protein levels to reg-
ulate metabolism.Mol. Cell 85,6 3 8–
651.e639 (2025).
27. Liang, C. et al. Mitochondrial microproteins link metabolic cues to
respiratory chain biogenesis.Cell Rep. 40, 111204 (2022).
28. Guerra, R. M. & Pagliarini, D. J. Coenzyme Q biochemistry and bio-
synthesis.Trends Biochem. Sci. 48, 463– 476 (2023).
29. Subramanian, K. et al. Coenzyme Q biosynthetic proteins assemble
in a substrate-dependent manner into domains at ER-mitochondria
contacts. J. Cell Biol. 218,1 3 5 3– 1369 (2019).
30. Manicki, M. et al. Structure and functionality of a multimeric human
COQ7:COQ9 complex.Mol. Cell 82,4 3 0 7– 4323.e4310 (2022).
31. Wang, D. et al. Complete enzyme clustering enhances coenzyme Q
biosynthesis via substrate channeling.bioRxiv https://doi.org/10.
1101/2025.05.24.655883(2025).
32. Nicoll, C. R. et al. In vitro construction of the COQ metabolon
unveils the molecular determinants of coenzyme Q biosynthesis.
Nat. Catal. 7,1 4 8– 160 (2024).
33. Tsukihara, T. et al. Structures of metal sites of oxidized bovine heart
cytochrome c oxidase at 2.8 A. Science 269,1 0 6 9– 1074 (1995).
34. Timon-Gomez, A. et al. Mitochondrial cytochrome c oxidase bio-
genesis: recent developments.Semin. Cell Dev. Biol. 76,
163– 178 (2018).
35. Barros, M. H., Johnson, A. & Tzagoloff, A. COX23, a homologue of
COX17, is required for cytochrome oxidase assembly.J. Biol. Chem.
279,3 1 9 4 3– 31947 (2004).
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press

36. Horn, D. et al. The conserved mitochondrial twin Cx9C protein
Cmc2 Is a Cmc1 homologue essential for cytochrome c oxidase
biogenesis.J. Biol. Chem. 285,1 5 0 8 8– 15099 (2010).
37. Khalimonchuk, O. et al. Pet191 is a cytochrome c oxidase assembly
factor in Saccharomyces cerevisiae.Eukaryot. Cell 7,
1427– 1431 (2008).
38. Swaminathan, A. B. et al. A yeast suppressor screen links Coa4 to
the mitochondrial copper deliverypathway for cytochrome c oxi-
dase. Genetics 221, (2022).
39. Nývltová, E., Dietz, J. V., Seravalli, J., Khalimonchuk, O. & Barrientos,
A. Coordination of metal center biogenesis in human cytochrome c
oxidase. Nat. Commun. 13, 3615 (2022).
40. Jumper, J. et al. Highly accurate protein structure prediction with
AlphaFold.Nature 596,5 8 3– 589 (2021).
41. Lin, Z. et al. Evolutionary-scale prediction of atomic-level protein
structure with a language model.Science 379, 1123– 1130 (2023).
42. Yu, J. et al. A replisome-associated histone H3-H4 chaperone
required for epigenetic inheritance.Cell 187,
5010– 5028.e5024 (2024).
43. Schmid, E. W. & Walter, J. C. Predictomes, a classi ﬁer-curated
database of AlphaFold-modeled protein-protein interactions.Mol.
Cell 85,1 2 1 6– 1232.e1215 (2025).
44. Zhang, J. et al. Predicting protein-protein interactions in the human
proteome. Science 390, eadt1630 (2025).
45. Kachroo, A. H. et al. Evolution. Systematic humanization of yeast
genes reveals conserved functions and genetic modularity.Science
348,9 2 1– 925 (2015).
46. Hiser, L., Di Valentin, M., Hamer, A. G. & Hosler, J. P. Cox11p is
required for stable formation of the Cu(B) and magnesium centers
of cytochrome c oxidase. J. Biol. Chem. 275,6 1 9– 623 (2000).
47. Chen, D. C., Yang, B. C. & Kuo, T. T. One-step transformation of yeast
in stationary phase. Curr. Genet. 21,8 3– 84 (1992).
48. Meisinger, C., Pfanner, N. & Truscott, K. N. Isolation of yeast mito-
chondria. Methods Mol. Biol. 313,3 3– 39 (2006).
49. Tyanova, S. et al. The Perseus computational platform for com-
prehensive analysis of (prote)omics data.Nat. Methods 13,
731–
740 (2016).
Acknowledgements
Parts of this research were conducted with the advanced computing
resources provided by the Texas A&M High Performance Research
Computing (TAMU-HPRC) facility. This work also used the FASTER
cluster at TAMU-HPRC through alloca t i o n# B I O 2 4 0 1 3 8t oA . B . S .f r o mt h e
Advanced Cyberinfrastructure Coordination Ecosystem: Services &
Support (ACCESS) program, which is supported by U.S. National Sci-
ence Foundation grants #2138259, #2138286, #2138307, #2137603, and
#2138296.
Author contributions
A.B.S. and V.M.G. conceptualized the project; A.B.S. performed all the
computational predictions; A.B.S. and D.T.K. developed computational
tools for data analysis; A.B.S., M.Z., R.M.G., and S.M.C. performed
experiments and analyzed the data along with D.J.P. and V.M.G.; D.J.P.
and V.M.G. were responsible for theresources and funding acquisition;
A.B.S. and V.M.G. wrote the manuscript with input from others.
Funding
The research reported in this publication was supported by the National
Institute of General Medical Sciences of the NIH awards R35GM152102
(V.M.G.) and R35GM131795 (D.J.P.). This work was also supported by the
Robert A. Welch grants A-1810 and A-2280-20260402 (V.M.G.) and
funds from the BJC Investigator Program (D.J.P.). D.J.P. is an investigator
of the Howard Hughes Medical Institute. The content is solely the
responsibility of the authors and does not necessarily represent the
ofﬁcial views of the NIH.
Competing interests
The authors declare no competing interests.
Additional information
Supplementary informationThe online version contains
supplementary material available at
https://doi.org/10.1038/s41467-026-77112-z
.
Correspondenceand requests for materials should be addressed to
Abhinav B. Swaminathan or Vishal M. Gohil.
Peer review informationNature Communicationsthanks Qian Cong and
the other, anonymous, reviewer(s) for their contribution to the peer
review of this work. A peer review ﬁle is available.
Reprints and permissions informationis available at
http://www.nature.com/reprints
Publisher’s note Springer Nature remains neutral with regard to jur-
isdictional claims in published maps and institutional afﬁliations.
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if
changes were made. The images or other third party material in this
article are included in the article's Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article's CreativeCommons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visithttp://creativecommons.org/
licenses/by/4.0/
.
© The Author(s) 2026
This Article in Press is shared early to give you faster access to new
research. It is citable and carries a permanent DOI. The ﬁnal edited
version will replace it automatically.
Article https://doi.org/10.1038/s41467-026-77112-z
Nature Communications Article in Press