---
reference_id: url:https://backend.orbit.dtu.dk/ws/files/406857921/PhD_Thesis_-_Garret_William_O_Connell.pdf
extractor_version: 1
url_source_version: 2
title: "https://backend.orbit.dtu.dk/ws/files/406857921/PhD_Thesis_-_Garret_William_O_Connell.pdf"
content_type: full_text_pdf
full_text_url: "https://backend.orbit.dtu.dk/ws/files/406857921/PhD_Thesis_-_Garret_William_O_Connell.pdf"
---

# https://backend.orbit.dtu.dk/ws/files/406857921/PhD_Thesis_-_Garret_William_O_Connell.pdf

## Content

 
 
General rights 
Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright 
owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights. 
 
 Users may download and print one copy of any publication from the public portal for the purpose of private study or research. 
 You may not further distribute the material or use it for any profit-making activity or commercial gain 
 You may freely distribute the URL identifying the publication in the public portal 
 
If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately 
and investigate your claim. 
  
 
   
 
 
Downloaded from orbit.dtu.dk on: Oct 26, 2026
Refactoring native metabolism in Pseudomonas putida towards production and
incorporation of novel fluorinated building blocks
O’Connell, Garret William
Publication date:
2024
Document Version
Publisher's PDF, also known as Version of record
Link back to DTU Orbit
Citation (APA):
O’Connell, G. W. (2024). Refactoring native metabolism in Pseudomonas putida towards production and
incorporation of novel fluorinated building blocks. Technical University of Denmark.

 
 
 
Refactoring native metabolism in Pseudomonas 
putida towards production and incorporation of 
novel fluorinated building blocks 
 
PhD Thesis 
Garret William O’Connell  


 
ii 
 
 
 
 
 
 
 
Refactoring native metabolism in 
Pseudomonas putida towards production 
and incorporation of novel fluorinated 
building blocks 
 
 
PhD Thesis 
 
 
Garret William O’Connell 
 
 
Novo Nordisk Center for Biosustainability 
Technical University of Denmark 
 
August 2024  

 
iii 
 
 
 
 
 
 
 
 
 
 
 
You’re only given one little spark of madness. 
You mustn’t lose it. 
-Robin Williams 
 
  

 
iv 
 
Preface 
This thesis is written in partial fulfillment of the requirements to obtain a PhD degree at the Technical 
University of Denmark. The work presented in this thesis was carried out between September 1 st, 2021 
and August 31 st 2024 at the Novo Nordisk Foundation Center for Biosustainability at the Technical 
University of Denmark, Kongens Lyngby, where it was supervised by Full Professor Dr. Pablo Ivan Nikel 
and the co-supervision of Senior Researcher Morten H. H. Nørholm. Funding was provided by the Novo 
Nordisk Foundation Copenhagen Bioscience PhD program. 
  

 
v 
 
 
 
 
 
 
 
 
 
 
 
 
 
This thesis is dedicated to my grandfather, William Thomas O’Connell, who 
taught me to always support those in need; to my grandfather Joseph Leeroy 
McGinn, who taught me to bring loved ones together; to my grandmother 
Marie Deliska Chiasson O’Connell, who taught me to be proud of my Acadian 
heritage; to my grandmother Georgia Frances Reid McGinn, who taught me 
to capture moments and connections with loved one; to my father, 
Christopher John O’Connell who taught me patience and prudence; to my 
mother, Veronica Susan McGinn, who taught me to be best I can and wish for 
the best in others and to my brother Keenan Leeroy and Ethan Christopher 
O’Connell who taught me that for family, you support without question. 
  

 
vi 
 
Dansk resmué 
At bryde grænser inden for kemi er i sin kerne den måde, hvorpå vi som samfund når højere højder i syntesen af 
nye forbindelser og materialer for at forbedre livet for de mennesker, vi lever sammen med. Udviklingen af 
polychlortrifluorethylen i slutningen af 1930'erne fødte Teflon, tetrafluorethylen, som blev brugt omfattende under 
Manhattan-projektet til uranberigelse under Anden Verdenskrig. Tilsvarende repræsenterer de kemiske grænser 
for bakteriel metabolisme en afgørende barriere for at udvide vores anvendelse af cellefabrikker, som har vundet 
fart og popularitet som et alternativ til traditionel kemi i de sidste to årtier. For at bryde disse grænser skal forskere 
udnytte enzymers promiskenhed og alsidigheden i kemisk syntese. 
I denne afhandling belyser jeg først den promiskuøse natur af sulfonatmetabolisme i Pseudomonas putida og 
udvikler værktøjer til dens tilpasning. Ved at bruge den viden, der er genereret fra Escherichia coli, vælger jeg 
forstyrrelsesmål, der tillader maksimal belysning af denne uudforskede metabolisme. Yderligere omics 
karakterisering kaster lys over de regulerende mekanismer for den samlede svovlmetabolisme. Derefter 
undersøger jeg opgraderinger til det alsi dige og billige Chi.Bio reaktorsystem til automatiseret adaptiv 
laboratorieevolution (ALE) med P. putida i tankerne. Kernen i denne afhandling syntetiserer jeg udforskningen af 
svovlmetabolisme med fremskridt til automatiseret ALE i et forsøg på at bygge en platformstamme af P. putida, 
der kan bryde grænserne for konventionel biokemi. Den attraktive promiskuøse natur af sulfonatmetabolisme 
balanceres af det lave behov for svovlmolekyler. Derefter forsøger jeg at bygge en biosyntetisk shunt for 
mellemkædede fedtsyrer med PFAS-indgang som en ledende princip til sekundær metabolisme. Kernen i denne 
afhandling er et forsøg på at udvide det metaboliske landskab i Pseudomonas putida med samtidig belysning af 
uudforskede metabolismer. Ved at gøre det fandt vi, at svovlmetabolisme for det meste følger en lignende model 
som E. coli, og der kræves meget få modifikationer for at muliggøre fedtsyreshunting. 
Samlet set lægger resultaterne i denne afhandling grundlaget for at etablere en platform for opdagelse af ny kemi. 
Derudover giver de en vej til bioremediering af PFAS, verdens fremtrædende miljøforurener. Hvis 
nøglemetaboliske forhindringer overvindes, vil de etablerede stammer og arbejde her-i sætte scenen for produktion 
af molekyler, som i deres kerne er nye for naturen. 
 
 
  

 
vii 
 
Abstract 
Breaking boundaries within chemistry is at it’s core the way we, as a society, reach further heights in synthesis a 
novel compounds and materials to better the lives of the people we live with. Development of 
polychlorotrifluorethylene in the late 1930s birthed Teflon, tetrafluoroethylene, which was extensively used during 
Manhattan project  for uranium enrichment during World War II.  Similarly, the chemical bounds of bacterial 
metabolism represent a crucial barrier to expanding our utilization of cell facto ries, factories which have been 
gaining speed and popularity as alternative for traditional chemistry  in the past two decades. In order to break 
these bounds, researchers need to take advantage of the promiscuity of enzymes and the versatility of chemical 
synthesis. 
In this thesis I first elucidate the promiscuous nature of sulfonate metabolism in Pseudomonas putida and develop 
tools for its adaptation. By using the knowledge generated from Escherichia coli, I choose disruption targets which 
allow for maximum elucidation of this underexplored metabolism. Further omics characterization shed light on the 
regulational mechanisms of total sulfur metabolism. Next, I explore upgrades to the versatile and cheap Chi .Bio 
reactor system for automated adaptive laboratory evolution (ALE) with P. putida in mind. At the core of this thesis, 
I synthesize the sulfur metabolism exploration with advances to automated ALE in an attempt to build a platform 
strain of P. putida capable of breaking the bounds of conventional biochemistry. The attractive promiscuous nature 
of sulfonate metabolism is balanced by the low demand for sulfur molecules. Then, I attempt to build a biosynthetic 
shunt for medium chain fatty acids, with PFAS entry as guiding principal to secondary metabolism in mind. The 
core of this thesis is an attempt at the expansion of the metabolic landscape in Pseudomonas putida with the 
concomitant elucidation of underexplored metabolisms . In doing so, we found that, fo r the most part, sulfur 
metabolism follows a similar model as E. coli and very few modifications are required to enable fatty acid shunting. 
Overall, the results in this thesis set the foundation for establishing a platform for novel chemistry discovery. 
Additionally, they provide an avenue for bioremediation of PFAS, the worlds pre-eminent environmental pollutant. 
If key metabolic hurdles are overcome, the strains and work established here-in would set the stage for production 
of molecules which, at their core, are New-to-Nature.  

 
viii 
 
Acknowledgements 
Without a doubt this thesis would not have been possible without the help of those who supported me through this 
process. While this list could easily take up an entire thesis of its own, I will try to acknowledge as many people as 
I possibly can. The appe arance of each person in this list no way conveys any degree of acknowledgement, I 
couldn’t have done it without everyone below. 
Without a doubt, Pablo deserves an acknowledgement for inspiring, better than anyone, the drive to learn new 
and exciting science. Whether it be #CoolPapers at midnight on a Saturday or meetings where new ideas are 
generated for the craziest metabolic construction – you did it all! 
When not Science-ing, I’m a huge fan of Magic the Gathering and I couldn’t have gotten through the lows without 
this outlet! My dear friends Jimmy Caroli, Khalil Bahlawan and Arash Davoodi made my time playing Magic a 
time worth having (and much needed). 
What a guy… The words for this man are difficult to describe but if I had to choose three: Italian +, supportive and 
enriching. Alberto de Maria, you are, at your core, without any doubt, an extra Italian man. Everyday you seek 
enriching experience between people and were always ready to support me, with whatever it may be. Not being 
afraid to challenge me enriched my growth more than you can possible know. 
Not asking but demanding daily doses of hugs is a hallmark of Maria Victoria Gracia Alvan Vargas  (yes, the 
whole name!). As grumpy as I may seem on the outside, these made my days that much better and with your 
constant support on and off the battlefield of science, I say a heartfelt thank you. 
Coming from New Brunswick, Canada, I am French speaking and to my delight, I arrived to the SEM group to two 
French lab mates Antonin and Justin. Despite not getting too many chances to converse in French, having the 
opportunity to do so made me feel at home. 
Stoic would be a word that some could described Maneul Nieto but to me, I knew him as supportive and caring, 
not something he would readily admit. Manu, your presence in and out of the lab made my day-to-day experience 
that much better. Be it the subtle nods when getting coffee to calling me out for being silly – thank you. 
The saying goes, keep your friends close and your enemies closer but I take this one step further, keep those that 
infuriate you closest. Oscar Puiggene Gonzalez and I are like two rams butting heads constantly and it always 
kept me on my toes and, moist importantly, humble. Thank you for that 
To the trio of Nico’s, Nico Krink your constant readiness to ‘talk shop’ gave me plenty of inspiration towards my 
many ongoing projects and I always appreciated a good bit of gossip; Nico Wirth, you are one of the most capable 
scientist I have evet met and discussion were always fruitful; Nico Gurdo, without a doubt you were one of the 
most supportive lab mates I have had the pleasure of working with and I look forward to our next asada together! 

 
ix 
 
By far my favorite Austrian (not German!) lab mate, Robert Haas. You were constantly excited to hear about my 
scientific progress and each time you did, you gave me that much more excitement to pursue the next goal. For 
that I thank you for driving me in the direction you did! 
The beauty of Automation quickly caught my attention early on in my PhD. Without the added interest of Stefano 
Donati and Lachlan Munro, I would not have been able to delve into the world of automated bioreactors. Thank 
you for inspiring me to put my feet up and let a machine do the heavy lifting for me! 
‘2024 is the year of love’ – Garret O’Connell – Javier Hernandez Sancho. Javier, your one-liners are surgical in 
their comedic relief and your everyday presence made the atmosphere in our office and lab that much more 
positive. As I quoted, and you love to re-quote, ‘2024 is the year of love’ but 2025 is your year. It will be up to you 
to decide what kind of year it is. 
Alexandre Perrin, you were my first supervised student, and I couldn’t have asked for a better student. As you 
start your own doctoral journey, I can only hope that your experience with me will help shape a successful PhD as 
your support helped shape mine! Thank you! 
Overflowing with excitement and anticipation for every day, Sofia de Francisco, you brought only the to quality 
mischief, laughs and passion. Without your energy, the days leading to the start of my PhD thesis writing would 
have been that much duller. Thank you for brining the Spanish sun and brightening each day just a little bit more. 
My passion for 3D printing ignited with my realization that CfB had a top -of-the-line 3D printing facility. I couldn’t 
have pursued this passion in my everyday science without the gleeful help from Kasper and August. Thank you 
for indulging my curiosity and allowing me to explore new possibilities! 
Finally, I’d like to acknowledge the ‘kids’ of the SEM group, all of the Special Project, Master’s students and visiting 
students/Phd’s alike. You all enriched the SEM group with activities, energy and aspirations to do the coolest 
science possible! 
Thank you to everyone who made my PhD a wholly positive experience – without you, it would have been that 
much harder to reach the level I did. 
  

 
x 
 
Table of Contents 
Preface iv 
Dansk resmué vi 
Abstract vii 
Acknowledgements viii 
Table of Contents x 
Thesis Outline 
 
xii 
Chapter 1: Unravelling the physiological structure of sulfur metabolism in P. putida 
KT2440 
 
Figure 1: Putative metabolic and expressional map of P. putida KT2440 sulfur 
metabolism. 
Figure 2: Investigating preferential sulfur trophism in P. putida KT2440. 
Figure 3: Combinatorial proteomics characterization of P. putida KT2440 under 
sulfate, cysteine and ethanesulfonate. 
Figure 4: Fitness heat map of wild-type P. putida and sulfur enzyme disrupted 
variants under select sulfur conditions. 
Figure 5: Investigating of 6:2 FTSA media preparation. 
1 
 
 
20 
 
21 
22 
 
24 
 
26 
 
Chapter 2 : Upgrading the Chi.Bio system for automated cultivation, quantitative 
physiology analysis and adaptive laboratory evolution of biotechnologically -relevant 
bacteria 
 
Graphical Abstract 
Figure 1: Agitation-dependent growth rate of Pseudomonas putida KT2440 and 
Escherichia coli MG1655 in Chi.Bio reactors. 
Figure 2: Cultivation of Pseudomonas putida rG1 and Cupravidus necator in 
ambient and enriched CO2 atmospheres. 
Figure 3: Growth rate optimization adaptive laboratory evolution of Pseudomonas 
putida SEM10 on ribose.  
Figure 4: Growth rate optimization adaptive laboratory evolution of Pseudomonas 
putida rG1 in enriched CO2 atmosphere.  
Figure 5: Tolerance adaptive laboratory evolution of Escherichia coli MG1655 to 
increasing concentrations of butanol. 
Figure 6: Multi-omics characterization of Pseudomonas putida KT2440 and 
Escherichia coli MG1655. 
 
31 
 
 
 
58 
59 
 
60 
 
61 
 
62 
 
64 
 
66 
 
Chapter 3: Tuning the sulfonate consumption capacity of Pseudomonas putida  for 
artificial overconsumption 
 
Figure 1: Engineering of Pseudomonas putida ST8 and adaptive laboratory 
evolution towards increased sulfonate consumption.  
Figure 2: Further engineering of Pseudomonas putida ST8 and carbon limiting 
adaptive laboratory evolution towards increased sulfonate uptake.  
Figure 3: Optimizing taurine to amino acid and nitrogen metabolism towards 
nitrogen-oriented adaptive laboratory evolution of Pseudomonas putida ST8. 
 
 
67 
 
 
89 
 
90 
 
91 
Chapter 4: Hidden in plain sight: Potential in upcycling PFAS 92 

 
xi 
 
 
Chapter 5: Direct and lossless delivery of exogenous fatty acids to fatty acid synthesis 
for incorporation of fluorinated fatty acyl compounds 
 
Figure 1: Simplified metabolic map of fatty acid metabolism in Pseudomonas putida.  
Figure 2: Fatty acid degradation (β-oxidation) inhibition in Pseudomonas putida.  
Figure 3: Direct-to-ACP ligation in Pseudomonas putida. 
103 
 
 
112 
113 
114 
 
Chapter 6: Concluding Remarks 
 
122 
 
Appendix I to Chapter 1 
 
126 
 
Appendix II to Chapter 2 
 
166 
 
Appendix V to Chapter 5 
 
188 
 
  

 
xii 
 
Thesis outline 
Grand feats of architecture are seen across the world from the red sandstone-lined Taj Mahal in Agra to 
the white marbled Parthenon in Athens. Concrete, a novel mixture of volcanic ash, lime and seawater in 
72 AD , allowed the Roman’s to build the Colosseum. A structure which still stands today. The Eiffel 
tower’s construction was made possible by the advancements to steel production and now stands as a 
cultural centerpiece to modern day Paris whereas more recently, the Burj Khalifa, made of both reinforced 
concrete and modern steels, stands as the tallest man -made structure at 828 meters. The true limit to 
human ingenuity is not creativity, rather, access to novel raw materials. In this work, we attempt to ignite 
the metabolic revolution in cell factories by  trying to establish a catch and release mechanism  of novel 
metabolites through sulfur metabolism and, provide new raw materials to realize the boundless creativity 
of metabolic engineers.  
This thesis is divided into two major sections: Chapter 1-3 which investigates the metabolic systems and 
tools needed to engineering sulfur metabolism in Pseudomonas putida and, in Chapter 3, we attempt to 
use this knowledge to engineer Pseudomonas putida as a platform strain for sulfonate overconsumption. 
Chapter 4-5 tackles the challenges of incorporating fluorinated sulfonates into fatty acid metabolism. 
Chapter 1 explores the metabolic structure of sulfur metabolism in Pseudomonas putida with a particular 
emphasis on mapping the known sulfur metabolism of Escherichia coli onto that of Pseudomonas putida. 
This chapter serves as an explorative work where the scope of sulfate and sulfur metabolism are 
elucidated through genomic disruption s and proteomics  characterization. Sulfur-containing per and 
polfluoroakyl substance utilization is briefly explored. 
Chapter 2 is a manuscript in preparation focusing on utilizing the Chi.Bio automated bioreactor system 
for adaptive laboratory evolution and omics characterization. This chapter serves as a tool development 
chapter used to adapt metabolic constructs generated in Chapter 3. 
The work in  Chapter 3 attempts to generate selection strains for increased sulfonate consumption in 
Pseudomonas putida. This chapter uses the  sulfur-metabolism knowledge generated in Chapter 1 and 
the Chi.Bio tool generated in Chapter 2 to achieve this goal. 
Chapter 4 is a manuscript in preparation outlining the problems of PFAS in an environmental context and 
the milestones needed to achieve PFAS utilization upcycling in a cell factory. This chapter sets the stage 
for reader to understand the works of Chapter 5 and why metabolic targets were chosen as such. 

 
xiii 
 
Chapter 5  explores the fatty acid metabolic engineering  needed to allow for PFAS utilization and 
upcycling by Pseudomonas putida. In it, we engineer fatty acid synthesis and degradation with the goal 
of inhibiting β-oxidation and enable Direct-to-ACP ligation of medium chain fatty acids. 
Chapter 6 serves as a conclusion for the works presented here-in and a perspective on works to come. 
Chapters 1 and 4 are manuscripts in preparation to be published after submission of the PhD thesis. 
Supplementary information is provided  in the Appendix at the end of this thesis. For consistency, the 
appendix number will correspond to the chapter with the same number. For example, supporting 
documentation for Chapter 1 can be found in Appendix I and documentation for Chapter 3 can be found 
in Appendix III. 

 
1 
 
Chapter 1: Unravelling the physiological structure of sulfur 
metabolism in P. putida KT2440 
Garret W. O'Connell1, Alexandre Perrin2, Pablo Ivan Nikel1 
1Novo Nordisk Center for Biosustainability, Systems Environmental Microbiology group 
2Ecole Polytechnique, Centre de mathématiques appliquées 
   
Sulfur is core to the elemental make -up of life itself. In  the model organism  Escherichia coli, sulfur 
metabolism is predicted to be tri-trophic with cysteine being at the top of the preference hierarchy, sulfate 
following closely behind and organic sulfur last. Sulfur metabolism, in particular sulfonate uptake, has the 
potential to be address two potential questions: what avenues exists for New -to-Nature metabolite 
production and, how can per- and polyfluoroakyl substances (PFAS) be selectively imported into a cell? 
The ssu operon shows potential for both delivery of non-natural metabolites and PFAS uptake. Much of 
what is expected from sulfur metabolism in non -E. coli organisms is modeled from that of E. coli. To 
answer the above questions in a more ideal chassis , we explored two major sulfur aspects of sulfur 
metabolism in Pseudomonas putida. First, we explored sulfur source preference with sequential sulfur 
consumption and proteomics. Sequential sulfur consumption was unsuccessful due to the unstable 
nature of cysteine, but proteomics revealed that P. putida will upregulate enzymes of the sulfur starvation 
response when sulfate is the sole sulfur source and upregulate enzymes of the extended sulfur starvation 
response when ethanesulfonate is the sole sulfur source. Contrary to the predicted structure in E. coli, 
cysteine did not have the same repressive effect on proteins of the sulfur starvation and extended sulfur 
starvation response as sulfate did on the extended sulfur starvation response. Next, we tested the sulfur 
capacity of the total sulfur metabolism in P. putida with disruptions to key sulfur acquisition enzymes and 
regulator. Like E. coli, the assimilatory sulfate reduction pathway in P. putida is the sole pathway for 
sulfate utilization and a single master regulator (CysB) controls the totality of sulfur acquisition and de 
novo cysteine production. Sulfonate utilization capacity was broad with cyclic, halogenated and vinyl 
sulfonates utilized as sole sulfur source. Concerningly, PFAS sulfonate uptake could not be confirmed. 
Assimilatory sulfate reduction disrupted P. putida were not able to grow on 6:2 FTSA as sole sulfur source 
shedding doubt on the potential PFAS upcycling by P. putida. These results dispel any doubt regarding 
prediction of sulfur metabolism in P. putida  from E. coli  and, to our knowledge, this is the first 
combinatorial sulfur source proteomic data set available for P. putida. It is our hope that the data sets 
here-in will fuel hypothesis regarding sulfur acquisition regulation and sulfonate delivery for New -to-
Nature molecule production. Further exploration of the sulfonate uptake and degradation is required to 
achieve PFAS delivery.  

 
2 
 
Introduction 
Sulfur is one of the six core elements with which life builds from. Often forgotten as the sixth, and final, element of 
the CHNOPS acronym learned in secondary school and university courses, and sulfur plays an essential role for 
various biological functions and represents a core building block for life. Of note, sulfur is important to amino acid 
synthesis and structure (Takagi and Ohtsu 2016 and Bechtel and Weerapana 2017), synthesis of cofactors (Du et 
al. 2011), nitrogen fixation (Marino and Howarth, 2014) and quorum sensing (Israel et al. 2023). In Pseudomonas 
species, sulfur in the form of hydrogen sulfide, is required for cysteine and methionine production (Vermeij and 
Kertesz 1999). Further, sulfur containing 2-(2-carboxy-4-methylazol-5-yl) ethyl phosphate is a predicted precursor 
to Vitamin B1 and S-adenosyl-L-methionine predicted to be required for biotin biosynthesis, both of which are key 
to fatty acid, gluconeogenesis and glycolysis metabolism (Jurgenson et al. 2009 and Lin et al. 2010). 
The structure of sulfur metabolism in P. putida is putative, that is, predicted based on the sulfur metabolism of E. 
coli. In E. coli, sulfur metabolism is tri -trophic in nature. When environmental sulfur is available in the form of 
cysteine, no enzymes are upregulated for de novo cysteine production. However, in the absence of cysteine, E. 
coli will express enzymes of the cys regulon, a regulon of ~20 genes involved in de novo cysteine production (van 
der Ploeg et al. 1997, Lochowska et al. 2001 and Jagura -Burdzy and Hulanicka 1981). The primary function of 
these enzymes is sulfate uptake and reduction through a process know as assimilator sulfate reduction (ASR – 
Leyh et al. 1988). In the absence of sulfate, E. coli will upregulate enzymes of the extended sulfur starvation 
response; a response involved in uptake of organic sulfur sources, typically in the form of sulfonates such as 
ethanesulfonate or taurine (Eichhorn et al. 1999 and Nishikawa et al. 2018). These enzymes are typically classified 
into two major groups: ssuEADCB variants involved in broad range sulfonate uptake or tauABCD enzymes which 
primarily uptake and degrade taurine (Eichhorn et al. 2000). 
Regulation of sulfur metabolism is crucial as cysteine, a sulfhydryl containing amino acid is highly reactive and can 
have detrimental metabolic effects if in excess (Korshunov et al. 2019). In E. coli master regulation of the cys 
regulon is performed by CysB, a LysR-type transcriptional regulator (van der Ploag et al, 1997). Under low cysteine 
conditions, N -acetyl serine levels increase and ‘activate’ CysB by binding to the transcriptional regulator and 
allowing binding upstream of cys regulon genes (Jaguar-Burdzy and Hulanicka 1981). When cysteine is abundant, 
N-acetyl serine levels are low due to the inhibition of the serine acetyltransferase; a process which inhibits O-acetyl 
serine, and consequently N-acetyl serine, production (Hindson 2003). Furthermore, in the inactive state, CysB will 
bind upstream of it’s own encoding site and act as a transcriptional repressor (Jovanovic et al. 2003). One protein 
produced from the sulfur starvation response is Cbl (CysB -like), a secondary regulator and activator of the 
extended sulfur starvation response responsible for the expression of ssu and tau enzymes (van der Ploeg et al. 
1999). Cbl is regulated by the presence of adenosine -phosphosulfate (APS) and phosphoadenosine -
phosphosulfate (PAPS); during ASR, sulfate reduction is processed via first transformation to APS then PAPS 
before sulfite (Bykowsk et al. 2002). This metabolic arrangement ensures sulfonate metabolism is repressed if 
sulfate is present as a more suitable sulfur source. 

 
3 
 
Sulfonate metabolism has garnered some interest as of late as its board specificity may be used as a vector system 
for delivery of cargo molecules directly to metabolism (Rodriguez -Robles et al. 2024). Rodriguez -Robles et al. 
2024 and colleagues demonstrated the use of the ssu system in E. coli as a delivery system for non canonical 
amino acids lending space for the potential discovery of New-to-Nature metabolism. Furthermore, degradation of 
key bottleneck PFAS (Zhang et al. 2016) molecules such as 6:2 FTSA has been found to likely enter host cells via 
ssu enzymes (Bottos et al. 2020 and Mendez et al. 2023). Bottos et al. 2020 and Mendez et al. 2023 reported 
upregulation of ssu enzymes by Gordonia NB4-1Y and Dietzia aurantiaca J3 when fed 6:2 FTSA as a sole sulfur 
source when compared to control sulfur sources. These would suggest the ssu enzymes may be a likely candidate 
for 6:2 FTSA uptake and degradation. 
P. putida is an emerging chassis for biotechnological production due to it’s suite of stress tolerating phenotypes 
(Reva et al. 2006, Calero et al. 2018, Ankenbaur et al. 2020, Nikel et al. 2021), established genetic engineering 
toolbox (Cook et al. 2018, Volke et al. 2021, Batianis et al. 2020 and Weimer et al. 2020) and it’s close relation to 
known PFAS degrading pure cultures (Bernhau et al. 2023). Here, we set out to explore two functions, sulfur 
metabolism structure and sulfonate uptake capacity in Pseudomonas putida  with a focus on halogenated 
sulfonates. PFAS are of global concern (Gulge et al. 2020) and it is our hope the study here -in will establish a 
starting point to merge P. putida engineering with PFAS upcycling and New-to-Nature molecule production. 
  

 
4 
 
Results and Discussion 
Understanding sulfur trophism in P. putida  through sulfur source preference and proteomics 
characterization. 
Sulfur is crucial for amino acid metabolism and co -factor synthesis leading it to be the 6 th essential element for 
growth. In P. putida and Escherichia coli  sulfur metabolism can be divided into three major categories: 
environmental cysteine acquisition, assimilatory sulfate reduction (ASR) and sulfonate acquisition and degradation. 
The later two categories make up the sulfur starvation and extended sulfur starvation response (Fig. 1). In brief, if 
cysteine is environmentally available, from proteolytic degradation or extracellular import, de novo cysteine 
synthesis is predicted to be repressed by CysB (PP_2327) autoregulation of itself (Kredich, 1992). High intracellular 
concentrations of cysteine inhibit the serine acetyltransferase which is responsible for O -acetyl serine, and 
consequently N-acetyl-serine, production, both of which are activators of CysB (Denk and Bock 1987 and Kredich, 
1992). In the absence of cysteine, the sulfur starvation response is predicted to express enzymes involved in 
sulfate (SO 4) uptake (e.g. cysAWU → PP_5168-5170), activation to sulfite (SO 3, cysDNC → PP_1303-4) and 
reduction to sulfide (H 2S, cysI → PP_2371; van der Ploeg and Leisinger 2001). Cysteine is predicted to be 
produced from the condensation of O-acetyl-serine and H2S to produce cysteine de novo (Becker et al. 1969). In 
the absence of both cysteine and sulfate, an extended sulfur response is predicted to upregulate expression of 
sulfonate uptake and degradation enzymes through an unknown, likely CysB-like, regulator (Bykowski et al. 2002). 
Briefly, sulfonates are actively up taken by putative sulfonate and taurine transporters (ssuACB and tauABC) and 
sulfite released via mono or dioxygenase activity producing one molecule of corresponding aldehyde (Fig. 1).  
While sulfur is an essential element, the available literature on the trophic structure of sulfur metabolism in Gram-
negative bacteria is limited primarily to E. coli (Kertezs 2000, van der Ploeg and Leisinger 2001). Hypotheses 
regarding sulfur trophism structure in P. putida have been primarily based on literature with E. coli as subject. To 
remedy this, sulfur source preference was explored by feeding limiting (~50 µM) amounts of L -cysteine, sulfate 
and ethanesulfonate and aliquots collected every hour fo r 12 hours; L -cysteine concentrations were measured 
using Ellman’s reagent (DTNB), sulfate concentrations using barium sulfate precipitation and ethanesulfonate 
concentrations using targeted metabolomics ( Fig 2. A). Over the course of 12 hours, no detectable levels of L -
cysteine could be seen using DTNB, sulfate could not be quantified with the method described here -in but 
ethanesulfoante concentrations steadily decreased from 58.9 uM to undetectable 0 to 8 hour s of incubation (Fig 
2. B). 
Unequivocally, the sulfur trophism experiments here-in were inconclusive. Cystine and sulfate consumption could 
not be quantified with DTNB or barium sulfate precipitation. One possible explanation for the lack of detectability 
of L-cysteine in culture supernatant can be found in the nature of the reaction between DTNB and L -cysteine. To 
cleave the disulfuide bond within DTNB, DTNB must interact with a reduced thiol (Ellman 1959). This would require 
L-cysteine to be in the reduced form and not protonated. When L-cysteine solutions are prepared in slightly acidic 
conditions, DTNB will not react with it and no molecules of TNB2- produced (Ellman, 1959). It could be hypothesized 

 
5 
 
that the lack of absorbance in samples lag phase samples (Fig 1., B, ~1 - 4 hours) is likely due to the protonation 
of L-cysteine during sample concentration or media acidification from gluconate production during exponential and 
stationary phases (Volke et al . 2021). Furthermore, barium sulfate precipitation was attempted using an 
Spectroquant sulfate test kit designed for Prove series spectrophotometer (Supelco 101812 and 173016). 
Adaptation of this kit for microtiter plate reader required scale down reac tion conditions 20 -fold. When barium 
chloride is exposed, in solution, to sulfate -containing media or solution, a pronounced white precipitate (barium 
sulfate) forms which is measured via turbidity quickly before collapsing (Abs > 700 nm). Scaling down of the barium 
sulfate precipitation reaction likely compromised the integrity of the precipitate such that an accurate measurement 
could not be taken. 
While sulfur source preference could not be fully confirmed by sequential consumption, a proteomics approach 
was taken to shed light on the regulation of sulfur metabolism. To answer whether P. putida preferentially 
metabolizes certain sulfur source categories, cysteine, sulfate and ethanesulfonate were individually and 
combinatorially challenged to P. putida, in excess, to generate the following sulfur conditions: L-cysteine, sulfate, 
ethanesulfonate, sulfate + L -cysteine, sulfate + ethanesulfonate and L -cysteine + ethanesulfonate ( Fig 3., A). 
Strains were grown to mid exponential phase, harvested and proteome assessed. A full list of differentially 
produced proteins and proteome binning by gene ontology can be found in the supplementary material. 
Relative abundance of sulfur starvation and extended sulfur starvation response enzymes were first compared 
between conditions (Fig 3., B) to assess apparent regulational patterns. At a glance, all identified enzymes of the 
extended sulfur starvation response ( ssuEADB and tauAD) were less abundant in conditions containing sulfate 
and L-cysteine (Fig 3., B, row 1-6; column 1, 3 - 6). Only when ethanesulfonate is provided as sole sulfur source 
are the extended sulfur starvation response enzymes upregulated. F urthermore, when L-cysteine is provided as 
sulfur source, are not downregulated to the same extent as seen in the extended sulfur response ( Fig 3., B, row 
7-11; column 3-5). 
To assess proteome wide changes between sulfur conditions, proteomes of single sulfur source conditions were 
compared to one another and multi sulfur source conditions compared to single sources where sulfur sources were 
common. Volcano plots of select conditions are reported in Fig. 2, C. 
First, proteomes of cysteine grown P. putida were compared to proteomes of sulfate, ethanesulfonate, cysteine 
and sulfate and cysteine and ethanesulfonate grown proteomes (Fig 3., C, E, F, G). When the proteome of cysteine 
grown P. putida was compared to that sulfate of sulfate grown P. putida, 132 proteins were upregulated and none 
downregulated (Table S2.) whereas in comparison to ethanesulfonate, 15 were upregulated and 132 
downregulated (Table S6.). To verify if additional sulfur sources had an impact on total proteome, the proteome of 
cysteine grown P. putida was compared to the proteome of cysteine and sulfate and ethanesulfonate grown 
proteomes (Fig 2., F, G). When sulfate is added, P. putida downregulated 9 proteins (Table S15.) as opposed to 
an upregulation of 2 proteins and downregulation of 3 (Table S17.) when ethanesulfonate is added. 

 
6 
 
Next, to confirm upregulation the enzymes of the extended sulfur response and assess the ability of cysteine to 
repress the sulfur starvation and extended sulfur starvation response, proteomes of sulfate grown P. putida were 
compared to the proteomes of ethanesulfonate, sulfate and cysteine and sulfate and ethanesulfonate grown 
proteomes (Fig 3., D, H, I). When compared to ethanesulfonate, 34 proteins are upregulated and 56 downregulated 
(Table S4.). In the additional presence of cysteine, 15 proteins were downregulated and 8 upregulated (Table S10.) 
whereas in the additional presence of ethanesulfonate, 13 proteins were downregulated and 11 upregulated when 
compared to the sulfate grown proteome (Table S8). 
Finally, understand if sulfate or cysteine can repress the extended sulfur response, the proteome of 
ethanesulfonate grown P. putida were compared to the proteomes of ethanesulfonate and cysteine and sulfate 
grown proteomes (Fig 3., J, K). With the addition of cysteine, 10 proteins were downregulated and 1 upregulated 
(Table S14.) wherease the addition of sulfate saw 26 proteins downregulated and 56 proteins upregulated (Table 
S11.). 
As described above, sulfur metabolism is expected to be tri -trophic in nature with cysteine repressing the sulfur 
starvation response and extended sulfur starvation response. Proteome differences between cysteine and sulfate 
and ethanesulfonate grown P. putida proteomes reflected that expectation with upregulation of enzymes of the 
sulfate assimilation and sulfur compound metabolic process (GO:0000103, 0006790; Table S3.) under sulfate 
conditions and alkanesulfonate catabolic process (GO:0046306, Table S7) under ethanesulfonate conditions (Fig 
3., B-C, E; Fig. S2, 4). Furthermore, upregulation of sulfonate degradation -specific enzymes such as SsuD and 
TauD (Table S5.) was observed when comparing the proteomes of sulfate and ethanesulfonate grown proteomes 
of P. putida (Fig 3., B, D; Fig S3.). Coincidentally, the above conditions were three of the four conditions with the 
most differences (20+ up or downregulated proteins). 
While the metabolic machinery predicted to be employed by P. putida to metabolism various sulfur sources is in 
fact produced ( cys, ssu and tau enzymes), the trophic nature of sulfur metabolism remains somewhat cryptic. 
When proteomes of cysteine grown P. putida were compared to proteomes of cysteine and sulfate or 
ethanesulfonate, little to no differences were observed and further no binning of differentially produced proteins 
were observed (Table S15 – 16). This is expected given cysteine’s predicted role in master regulation of the cys 
regulon (van der Ploeg and Leisinger 2001) however, this trend is not seen when comparing sulfate or 
ethanesulfonate grown proteomes to those of cysteine and sulfate and cysteine and ethanesulfonate respectively 
(Table S10-14). Downregulation Cys and Ssu enzymes given the putative metabolic structure is expected. Sulfate, 
on the other hand seemed to have a repressive effect on enzymes of the extended sulfur starvation response 
since, when sulfate grown proteomes were compared to sulfate and ethanesulfonate grown proteomes, only SsuD 
was upregulated ( Fig 3., B; Table S9). When the comparison was made with ethanesulfonate and sulfate and 
ethanesulfonate, ssu related enzymes were dramatically upregulated and binning of upregulated proteins returned 
sulfonate specific gene ontology terms such as alkanesulfonate metabolic process ( Fig 3., B, K; Table S13, Fig 
S5).  

 
7 
 
At high intracellular concentrations, cysteine is toxic due to it’s tendency to form disulfide bonds, disrupt isoleucine 
biosynthesis and promote reactive oxygen species production (Korshunov et al. 2019). In E. coli, environmental 
cysteine is quickly transformed to cystine (a disulfide dimer of cysteine) and exported to reduce toxicity (Korshunov 
et al. 2019). Should this mechanism be conserved in P. putida, the concentrations of free cysteine may in fact not 
be high enough to cause the accumulate of O-actyle serine and strict repression of the cys regulon. Alternatively, 
with predicted low intracellular cysteine concentrations and several steps removed from direct CysB inhibition, it 
can be hypothesized that enzymes of the sulfur starvation response are leaky, when compared to the extended 
sulfur starvation response. While cysteine itself may not have a strong regulational impact on sulfur and sulfonate 
uptake and metabolism, sulfate itself is a strong repressor of sulfonate uptake and metabolism enzymes. Whether 
this mechanism is the same in P. putida as in E. coli is yet to be determined as the regulator responsible for ssu 
and tau expression has yet to be identified in P. putida. 
Exploring the metabolic bounds of sulfur metabolism in P. putida.  
Under laboratory conditions, sulfur is abundantly provided in the form of sulfate (Elbing and Brent, 2002) however, 
in the environment, readily available sulfur is contingent upon amino acid availability and sulfate concentrations. 
Environmental sulfate concentrations can vary wildly from 2700 mg/L in seawater to 30 mg/L in freshwater and 
~1600 mg/kg in soil (Hitchcock, 1975, Katz, 1977, and Sacklette and Boerngen, 1984). To that end, organisms 
such as P. putida can inhabit environments where sulfur is scarce and scavenging sulfur from organic sources 
(e.g. sulfonates) is needed. To ensure sulfur requirements are met in sulfate starved environments, P. putida will 
produce enzymes involved in sulfonate uptake and degradation (Fig 3; Vermeij and Kertesz 1999). These enzymes 
must have a broad import and catalytic capacity todeBon ensure optimal survival in diverse environments.  
To gauge the metabolic capacity of sulfur metabolism in P. putida, genes involved in sulfur acquisition regulation 
(cysB), sulfate reduction ( cysDNCH) and sulfonate uptake and degradation ( ssuEADCB and tauDABC) were 
disrupted with the pSNW2 suicide vector ( Table 1.) resulting in 13 strains with altered sulfur metabolism ( Table 
2.). These 13 strains and wild -type P. putida were challenged with 20 select sulfur conditions divided into three 
categories: control, catalytic capacity and import capacity sulfur source (Fig S2-4). In total, 840 growth curves were 
produced across 14 strains and 20 conditions, analyzed with the QurvE software (Wirth et al. 2023) and growth 
parameters (lag time, growth rate and max growth yield) assessed with the fitness calculator written here-in. Growth 
parameter weights were chosen to highlight growth rate and max growth yield to account for toxicity and 
morphology changing effects of sulfur conditions and ‘ghost’ growth rates generated from few, biologically relevant 
data points. Resulting fitness scores (Fscore) are reported in Fig 4; an Fscore > ~0.5 is considered wild-type growth; 
Fscore matrix of all sulfur and genetic conditions can be found in the supplemental material. 
While any sulfur-containing molecules could be chosen as a sulfur source, sulfur sources were chosen based on 
availability, price and accessibility of sulfur. The Sigma-Aldrich catalog of chemicals was exhaustively searched on 
January 8th, 2024 and candidate sulfur sources purchased (Fig S6-8.). Control sulfur sources were chosen as know 
sulfuonate metabolites of P. putida, catalytic capacity sulfur sources chosen to explore the catalytic capacity of 

 
8 
 
putative sulfonate degradation enzymes (SsuD and TauD) and import capacity sulfonates chosen to test the bound 
of sulfonate uptake by sulfonate uptake enzymes (SsuACB and TauABC). 
When the putative master regulator of sulfur metabolism, cysB, is disrupted, P. putida is completely inhibited from 
growing on all sulfur conditions ( Fig 4., Fscore 0.04 - 0.07) except for on L -cysteine (Fig 4., Fscore 0.54). Further, 
when enzymes of the ASR pathway, cysD, cysNC, and cysH, are disrupted, P. putida is uniquely inhibited from 
growing of sulfate (Fig 4., Fscore 0.04 for all strains) and interestingly, diphenylamine-4 sulfonate and 6:2 FTSA (Fig 
4., F score 0.04 for both conditions). Further gro wth inhibitions include 3F -EtSO3, Br -EtSO3, 3 -(1-pyridino)-1-
propanesulfonic acid and (1s)-(+)-10-camphorsulfonic acid were not unique to ASR affected strains (Fig. 4.; row 2 
– 4, column 6 – 7, 12 – 13). 
To assess the complementary scope of each system when faced with varying sulfonate sources, ssu and tau 
enzymes were individually disrupted and, to confirm the potential presence of cryptic sulfonate uptake and 
degradation systems, ssu and tau enzymes were conjointly disrupted. When the ssu and tau operon were disrupted 
individually, P. putida was uniquely inhibited from growing on ethanesulfonate, 3 -sulfopropyl acrylate, HEPES, 
MOPS, 6:2 FTSA and 3 -chloro-2-hydroxy-1-propanesulfonate (Fig 4., F score 0.04, 0.04, 0.09 and 0.04 in Δssu 
compared to 0.49, 0.65, 0.49 and 0.71 in Δtau respectively) only when ssu was disrupted. Common growth 
inhibitions to both include trifluoroethanesulfonate, bromoethanesulfnate and (1s) -(+)-10-camphorsulfonic acid 
(Fig 4., Fscore 0.04 and 0.04 in Δssu compared to 0.17 and 0.09 in Δtau respectively). Similar patterns of growth 
inhibition are seen when both ssu and tau are disrupted as compared to when ssu was uniquely disrupted with the 
notable exception of growth inhibition of taurine (Fig 4., Fscore 0.04 fitness scores in Δssu tau compared to 0.5 and 
0.64 in Δssu and Δtau respectively). 
The ssu and tau operons area divided into two major components: carbon -sulfur bond breaking enzymes ( ssuD 
and tauD) and transmembrane sulfonate uptake (ssuACB and tauABC). To evaluate if the individual components 
of each system function in trans (e.g. TauD can complement SsuACB), six strains were generated. Four strains 
with individual deletions of carbon -sulfur bond breaking enzymes ( ΔssuD and ΔtauD) and transmembrane 
sulfonate uptake ( ΔssuBC and ΔtauABC) and two strains with combinatorial trans deletion b etween systems 
(ΔssuD tauABC and ΔtauD ssuBC). Due to the genetic placement of the ssuACB enzymes (Fig S5.), only ssuCB 
(permease and cytoplasmic ATPase) were disrupted. 
Selective sulfonate degradation and uptake systems resulted in a more nuanced effect on P. putida fitness scores. 
Notably, when ssuD was disrupted, growth on ethanesulfonate, bromoethanesulfonate, chloroethanesulfonate, 
trimethylsilipropanesulfonate, 3 -(1-pyridino)-1-propanesulfonate, HEPES, MOPS and 3 -chloro-2-hydroxy-1-
propanesulfonate was negatively affected (Fig 4., Fscore 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04 and 0.04 in ΔssuD 
and 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.07, 0.04 in ΔssuD tauABC compared to 0.62, 0.14, 0.43, 0.13, 0.22, 0.49, 
0.61 and 0.59 in ΔtauD, 0.67, 0.36, 0.1, 0.35, 0.48, 0.37, 0.45, 0.56 and 0.62 ΔtauABC and 0.61, 0.15, 0.36, 0.08, 
0.04, 0.04, 0.24 and 0.7 ΔtauD ΔssuCB respectively). Further, disruption of ssuCB impacted fitness on 3 -(1-

 
9 
 
pyridino)-1-propanesulfonate and HEPES (Fig 4., Fscore 0.04 in both conditions). Disruption of the tau enzymes did 
not have a major impact on sulfonate uptake fitness scores. 
The ssu and tau systems have been studied primarily in E. coli since their initial characterization in the late 90s 
and early 2000s (Eichhorn et al. 1999 and 2000). Eichhorn et al. 1999 and colleagues reported on the broad 
catalytic capacity of ssuD and this was furthered in the works of Eichhorn et al. 2000 where combinatorial deletions 
ssu and tau enzymes in E. coli revealed the broader range of substrate to the ssu system over the tau system. 
Here we report on the same trend observed by Eichhorn et al. 2000; when ssuEADCB, ssuD or ssuCB were 
disrupted, sulfonate utilization was uniquely impacted when compared to the tau-affected variants. Interestingly, 
the only condition where growth was inhibited on taurine was whole disruption of the ssu and tau operons 
suggesting that, while the tau system plays a role in taurine metabolism, the ssu system likely has enough overlap 
to also uptake and degrade taurine. 
The SsuD enzyme is a flavin-dependent alkanesulfonate monooxygenase (Eichhorn et al. 1999). Reduced flavin 
mononucleotide (FMNH2) produced by the oxidoreductase SsuE is co-ordinated into the active side of SsuD where 
a peroxyflavin intermediate is produced (Dayal et al . 2015). This intermediate will undergo a Baeyer -Viliger 
rearrangement producing sulfite and the corresponding aldehyde (Ellis, 2011). When challenged with sulfonates 
chosen to test the catalytic capacity of SsuD, only 3-chloro-2-hydrox-1-pronanesulfonate definitively demonstrated 
metabolism by the ssu system. Fitness scores for aminomethanesulfonic acid and diphenylamine -4 sulfonate 
indicate contamination of non -cysteine sulfur sources or sulfate with growth under all conditions in non -cysB 
disrupted variants and selective inhibition with ASR disruption. 
Little literature is available on the limits of the SsuACB  and TauABC transmembrane transporter. In this study, 
sulfonate chosen to test these limits revealed that cyclic, aliphatic sulfonates could be used as sole sulfur sources 
in the case of HEPES and MOPS and some steric and functional flexibility exists in the case of 
chloroethanesulfonate and 3 -sulfopropyl acrylate but larger cyclic monoterpenes such as (1s) -(+)-10-
camphorsulfonic acid are likely not up taken by either transport system. Fitness scores of halogenated sulfonates 
reveled a less consistent trend across sulfonate sources. When challenged with trifluoro and 
bromoethanesulfonate, strains were considerably inhibited but not when challenged with fluoro and 
chloroethanesulfonate and 3 -chloro-2-hydroxy-1-propanesulfonate. These results seem contradictory to one 
another; however, fluorine functional groups can have a considerable electronic impact on their cognate molecule 
(Pursur et al. 2007 and Chandra et al. 2023). It could be hypothesized that the presence of a trifluoro group on 
ethanesulfonate inhibits SsuD-mediate carbon-sulfur bond cleavage by changing the electronic properties of the 
sulfur center and the increased size difference between bromo and chloro and fluoro (ratomic = ~1.93, 1.74 and 1.35 
Ǻ respectively) functional groups leads to decreased or inhibited uptake of bromoethanesulfonate by SsuACB. 
Extended investigation 6:2 FTSA metabolism in P. putida as sole sulfur source. 
Alarmingly, of the strains and conditions tested in Fig 4., all strains with intact ASR or cysB were able to grow on 
6:2 FTSA as sole sulfur source. This leads to two conclusions; P. putida can utilize 6:2 FTSA as sole sulfur source 

 
10 
 
or 6:2 FTSA conditions are contaminated with sulfate. In an attempt to rule out the latter, 6:2 FTSA media 
preparations were tested to confirm the presence of 6:2 FTSA in the final media and the ability of ASR intact ( P. 
putida KT2440) and disrupted ( P. putida ΔcysH) to grow on 6:2 FTSA media. This was confirmed by assessing 
three potential bottlenecks in 6:2 FTSA preparation: 6:2 FTSA solubility, absorption to Teflon -based syringe filter 
membrane and sulfate contamination in the final media preparation (Fig 5., A). 
First, the assess best solubility conditions, 6:2 FTSA was suspended to a final concentration of 10 mM in 100, 50 
and 0% v/v ethanol and incubated for 10 minutes ( Fig 5., B). In absolute ethanol, 6:2 FTSA was visibly insoluble 
and in water, 10 mM was partially soluble. In 50% v/v ethanol, however, no visible suspension could be seen after 
10 minutes of incubation. Going forward, 6:2 FTSA was prepared in 50% v/v ethanol. 
Laboratory syringe filters for media preparation are made of Teflon (polytetrafluoroethylene), a perfluorinated 
polymer which is unreactive to most conditions. While suitable for routine lab experiments, preparation of 6:2 FTSA 
containing media may lend be  problematic due to potential PFAS absorption to the filter. In order to qualitatively 
test this, four medias were prepared: filtered 6:2 FTSA -containing media, unfiltered 6:2 FTSA -containing media, 
filtered octanesulfonate containing media and filtered no sulfur containing media. These media were transferred to 
a glass bottle and a foam test performed by vigorously shaking the bottles for 15 seconds. After one minute 
incubation, foam could be seen in both the filtered and unfiltered 6:2 FTSA containing med ia suggesting the 
presence of a surfactant (likely 6:2 FTSA) in the solution (Fig 5., C). 
Finally, to test if the final media preparation of 6:2 FTSA contained contaminating sulfate, ASR intact ( P. putida 
KT2440) and disrupted (ΔcysH) were challenged with filtered and unfiltered 6:2 FTSA media. In both filtered and 
unfiltered 6:2 FTSA media, P. putida KT2440 was able to grow where del cysH demonstrated similar growth curves 
to no culture added controls (Fig 5., D). While 6:2 FTSA may not be used as a sole sulfur source, 6:2 FTSA may 
be able to rescue growth deficiencies at lower sulfur concentrations. To test this, ASR intact and disrupted strains 
were grown on decreasing concentrations ethanesulfonate from 2 mM to 0.047 mM while concentrations of 6:2 
FTSA were maintained at 0.5 mM. Resulting growth rates from 2 mM to 0.047 mM for all strains and  conditions 
remained consistent ( Fig 5., E) until ~0.165 mM, where growth rates for P. putida KT2440, ΔcysH without 6:2 
FTSA and P. putida KT2440 with 6:2 FTSA saw decreasing growth rates from 1.04 to 0.85, 1.15 to 1.03 and 1.12 
to 0.76 h-1 respectively between ethanesulfonate concentrations of 0.109 – 0.047 mM. Growth rates for P. putida 
ΔcysH increased slightly from 0.77 to 0.88 h-1 between concentrations 0.109 – 0.047 mM. 
The carbon-fluorine bond is one of the strongest bonds in organic chemistry with bond length and size similar to 
that of the carbon-hydrogen bond (O’ Hagan 2008; ~ lbond = 1.35 Ǻ and rcov = 0.57 Ǻ compared to lbond = 1.09 Ǻ and 
rcov = 0.53 Ǻ). Together, these would suggest that 6:2 FTSA is structurally similar in size to octanesulfonate, a 
known non-fluorinated substrate of the ssu system. While it is evident here that media preparations of 6:2 FTSA 
contain contaminating sulfate, the reason as to why ASR di srupted strains couldn’t utilize 6:2 FTSA as a sulfur 
source remains cryptic. Successful growth of undisrupted ASR strains indicates that the presence of 6:2 FTSA in 

 
11 
 
the media does not have growth impacting characteristics by presence of the 6:2 FTSA, but, rather import or 
carbon-sulfur bond cleavage is impacted.  
While use of 6:2 FTSA as a sole sulfur source is not likely by P. putida, use as a co-sulfonate may yet be possible. 
The results here-in lack the resolution of lower sulfonate concentrations to demonstrate beyond a reasonable doubt 
that the presence of 6:2 FTSA can rescue a sulfur deficiency. Furthermore, inconsistent growth r ates make 
definitive claims impossible. The sulfur concentrations starting point were chosen for consistency with other 
experiments in this study and, the sulfur concentration added to M9 media being 2 mM (Elbing and Brent, 2002). 
Furthermore, the range of concentrations were chosen based on the availability of wells in a singular 96-well plate. 
Expanding the resolution of the ethanesulfonate titration in Fig 5., E to 10 µM or lower would shed light on the 
exact sulfur impact 6:2 FTSA may have on P. putida. Alternatively, beginning the ethanesulfonate titration from 
500 uM would lead to a final concentration of 11.8 µM if 10, serial 66% dilutions are performed. 
So, if 6:2 cannot be used a sole sulfur source, how can 6:2 FTSA uptake and degradation capabilities be endowed 
to P. putida. Bottos et al. 2020 and colleagues reported Gordonia NB4-1Y upregulated several ssu-like uptake and 
carbon-sulfur bond cleaving enzymes. These are furthered by the results from Mendez et al. 2022 where Dietzia 
sp. J3 also upregulated ssu-like enzymes when challenged with 6:2 FTSA as a sole sulfur source. The first step to 
enabling 6:2 FTSA utilization in P. putida would be the heterologous expression of Gordonia NB4-1Y and Dietzia 
sp. J3 ssu-like enzymes.  

 
12 
 
Conclusion 
Like with many putative metabolic structures, sulfur metabolism in Pseudomonas putida is predicted to map onto 
the metabolic structure of E. coli. One draw back to this approach when designing engineering experiments is the 
potential for cryptic function, pseudo genes or unidentified homologs. With sulfur metabolism appearing as a 
promising candidate for new-to-nature molecules delivery (Rodriguez-Robles et al. 2024) and the appeal of using 
P. putida as a cell factory due to its resistance to a wide variety of solvents and stressors (Weimer et al. 2020), we 
set out to map what is known in E. coli to P. putida to gain a better understanding of the key forces underpinning 
sulfur metabolism in P. putida. 
Sulfur metabolism in P. putida is predicted to be dynamic metabolism as it must respond to ever changing 
environmental sulfur availability. To confirm the dynamic nature of sulfur metabolism, P. putida was challenged 
with starvation levels of three sulfur sources to assess if sequential or parallel consumption of sulfur sources occur. 
The resulting data set unfortunately led to inconclusive results regarding which sulfur source is preferred due to 
limitations of the DTNB assay and the lack of sensitivity of the barium sulfate assay. 
Instead of monitoring decreasing sulfur concentrations, proteomic profiles of cysteine, sulfate, ethanesulfonate and 
combinations there-of were generated exploring the nearly full range of sulfur source combinations possible. The 
hypothesis being that preferential sulfur sources (e.g. sulfate prefered over ethanesulfonate) would downregulate 
enzymes of the more distant extended sulfur starvation response. Differential expression was predominantly 
observed where unique sulfur sources were compared to other u nique sulfur sources. Expectedly, when only 
sulfate is available, enzymes of the cys regulaon (e.g. cysDNC) are upregulated and when only ethanesulfonate 
is available, ssu and tau proteins (ssuEADCB and tauABCD) were upregulated. Changes comparing sulfur source 
combinations were murkier; cysteine did not have the expect repressive effect on sulfur starvation and extended 
sulfur starvation response as predict but sulfate strongly repressed enzymes of the exte nded sulfur starvation 
response. Cysteine can have detrimental impacts on amino acid metabolism and intracellular homeostasis which 
suggests that P. putida likely modulates intracellular cysteine concentrations tightly (Korshunov et al. 2019). Since 
CysB regulates the cys regulon through interaction N -acetyl serine concentrations and not cysteine (Kredich, 
1992), one could hypothesize that cysteine mediated control of the cys regulon is leaky due to the steps removed 
from direct regulation. Sulfate repression of the extended sulfur starvation response are in line with E. coli sulfur 
metabolism structure but the activator of said response remains elusive in P. putida. 
Sulfonate uptake has garnered some attention as a potential direct delivery system for metabolites (Rodriguez -
Robles et al. 2024). To understand the scope of sulfur metabolism in P. putida, strains with disrupted regulation, 
assimilatory sulfate reduction (ASR) and sulfonate uptake and degradation were challenged with 20 sulfur 
conditions. Regulation of total sulfur metabolism was quickly identified to be contingent upon cysB and 
contaminating sulfate in diphenylamine-4 sulfonate and 6:2 FTSA quickly identi fied. ASR genes cysDNCH were 
identified as the only mechanism allowing growth on sulfate indicating P. putida does not have a secondary ASR 
system. Scope of sulfonate degradation in P. putida was revealed to be quite broad with ssu allowing growth on 

 
13 
 
halogenated (chloroethanesulfonate, 3 -chloro-2-hydrox-1-propanesulfonate), vinyl and silicon containing (3 -
sulfopropyl acrylate and trimethylsililpropanesulfonate) and partially cyclic (HEPES, MOPS and 3 -(1-pyridino)-1-
propaonesulfonate) sulfonates. To the  best of our knowledge, this data set is the first broad spectrum sulfonate 
consumption data set in P. putida. 
Broad spectrum degradation of 6:2 FTSA, an important industrial PFAS (Gluge et al 2020), in ASR intact strains 
signaled a worrying conclusion: 6:2 FTSA preparation contain sulfate. To that end, a brief characterization of 6:2 
FTSA media was performed. Media preparations were found to likely contain 6:2 FTSA but as feared, 6:2 FTSA 
could not be used as a sole sulfur source. Attempt to resolve the co -sulfonate capabilities of 6:2 FTSA were 
unsuccessful. Structurally, 6:2 FTSA is similar to octanesulfoante due to the steric similarity of the carbon-hydrogen 
and carbon-fluorine bond (O’Hagan, 2008). While the latter is a known ssuABC metabolite (Eichhorn and Leisinger, 
2000), the former should therefore also be a substrate. Further purification and characterization of SsuD may shed 
light on the bottleneck of 6:2 FTSA degradation. 
  

 
14 
 
Materials and Methods 
Reagents and media. All chemicals in this study were purchased from Sigma -Aldrich (St. Louis, MI, USA) with 
the exception of potassium 3,3,4,4,5,5,6,6,7,7,8,8 -tridecafluoroocantesulfonate which was purchased from 
Biosynth (Staad, Switzerland) and trifluoroethanesulfonic acid an trimethylsilipropanesulfonic acid which was 
purchased from ChemSpace (Riga, Latvia). Lysogeny (LB) broth composed of 5g/L NaCl, 10 g/L tryptone and 5g/L 
yeast extract and agar plates prepared with the addition of 15 g/L agar. In this study, a modified d eBont was 
prepared (deBont Cl) containing the following: 3.88 g/L K 2HPO4, 1.63 g/L NaH 2PO4, 4 g/L NH 4Cl, 10 mg/L 
ethylenediaminetetraacetic acid (EDTA), 100 mg/L MgCl2·6H2O, 2 mg/L ZnCl2, 1 mg/L CaCl2·2H2O, 5 mg/L FeCl2, 
0.2 mg/L Na2MoO4·2H2O, 0.2 mg/L CuCl2·5H2O, 0.4 mg/L CoCl2·6H2O and 1 mg/L MnCl2·2H2O. Carbon sources 
were added separately as described in the text. Kanamycin and gentamicin were added to 50 - and 10 µg/L, 
respectively, when needed. 
Media preparation. For the purposes of sulfur-sensitive experiments, established deBont (Hartmans et al. 1989) 
was modified to generate deBont Cl; all instances of sulfur -containing minerals were replaced with sulfur -free 
minerals. Departure from established deBont recipe are as follows: ammonium sulfate ((NH 4)2SO4) was replaced 
with ammonium chloride (NH 4Cl) and trace elements copper sulfate (CuSO 4), iron (II) sulfate (FeSO 4) and zinc 
sulfate (ZnSO4) were replaced with copper (II) chloride (CuCl2), iron (II) chloride (FeCl2) and zinc chloride (ZnCl2). 
Concentrations maintained to reflect core deBont concentrations. Unless otherwise noted, deBontCl was prepared 
with the addition of sulfur sources to a final concentration of 2 mM. 
Bacterial strains, plasmids and oligonucleotides. All strains, plasmids and oligonucleotides are listed in tables 
S1-3. Oligonucleotides were purchased from Integrated DNA technologies (Coralville, IA, USA). Genomic DNA 
extractions were performed using DNeasy blood and tissue DNA extraction kits (Qiagen, Hilden, Germany), 
plasmid extractions performed with Nucleospin ® Plasmid kit (Macherny-Nagel, Düren, Germany), gel extractions 
and PCR clean -up with NucleoSpin ® Gel and PCR clean -up kit (Macherny -Nagel, Düren, Germany ), 
oligonucleotides designed using the Benchling primer wizard function (San Francisco, CA, USA) and AMUSER 
web-tool (Genee et al. 2015). Polymerase chain reactions (PCR) were carried out with PhusionU (ThermoFisher, 
Waltham, MA, USA) or OneTaq (New England Biolabs, Ipswich, MA, USA) polymerase. 
Plasmid construction, and homologous recombination -mediated genome engineering of pseudomonas 
putida. Unless otherwise noted, plasmids were constructed with established USER cloning techniques (Nour-Eldin 
et al. 2006). In brief, primers were designed using the AMUSER web - tool (Genee et al. 2015) uracil-containing 
primers were purchased from Invitrogen (Waltham, MA, USA) and PCR performed with PhusionU (ThermoFisher, 
Waltham, MA, USA). Cleaned PCR fragments were pooled to equimolar concentrations and ligated with USER™ 
enzyme (New England Biolabs, Ipswich, MA, USA). Contaminating methylated DNA was digested using DpnI (New 
England Biolabs, Ipswich, MA, USA). 

 
15 
 
Genetic manipulation was performed using pSWN2 assisted homologous recombination (Volke et al. 2021). In 
brief, genetic constructs destined for chromosomal deletion or integration were designed with two homology arms, 
~500 bp upstream and downstream a target region of interest. For deletion, the homology arms flanking a gene of 
interest were ligated together. To integrate constructed pSNW2 plasmids, P. putida strains were washed with 1 
mL of 300 mM sucrose 2 -3 times and washed strains placed in a Gene Pulse r® cuvette (Bio-Rad, Hercules, CA, 
USA) electroporation cuvette with 100-500 ng of purified plasmid and electroporated at 2.5 kV with a MicroPulser™ 
electroporator (Bio-Rad, Hercules, CA, USA). The cell mixture was recovered in 1 mL LB broth for one hour before 
plating on LB agar with kanamycin. 
Resulting colonies with green fluorescence and kanamycin resistance were considered single integrants. Single 
integrants were inoculated in LB with kanamycin, washed the following day 2 -3 times with 300 mM sucrose and 
electroporated with pQure-6-strong. The cell mixture was immediately suspended in 5 mL LB broth with gentamicin 
and 5 mM 3-methyl benzoate and incubated at 30°C overnight to promote a secondary recombination event. The 
following day, the curing broth was plated on LB agar with gentamicin and colonies with red fluorescence, absence 
of green fluorescence, sensitivity to kanamycin and genetic background of interest were inoculated in LB media 
with no antibiotics to cure the pQure -6-strong plasmid. Next, the cell mixture was plate on LB with no ant ibiotics 
and colonies screen for sensitivity to gentamicin. Successful genetic manipulations were screen by PCR and final 
strains stored at -80°C 
P. putida growth analysis. Growth curves of P. putida strains were prepared by first pre -culturing the chosen 
strain in lysogen broth. The resulting biomass collected the following day and washed twice in ddH 2O before 
normalizing OD to ~2.5. Washed, OD normalized strains were inoculated 1:100 in 24 - or 96-well plates (Greiner 
Bio-One, Kremsmünster, Austria) to an effective starting OD of ~0.025. Plates were incubated in Epoch2 microtiter 
plate reader (Agilent, Santa Clara, CA, USA), SynergyH1 microtiter plate reader (Agilent, Santa Clara, CA, USA) 
or ELx808 microtiter plate reader (BioTek, Winoosky VA, USA)) and absorbance monitored at 600 or 630 nm. 
Resulting absorbances, when necessary, were converted to OD600 via transformation with a calibration curve 
The resulting growth curves were analyzed using the QurvE (Wirth et al. 2023) software with default settings unless 
otherwise mentioned. Fitness scores were determined using a fitness calculator 
(https://github.com/Garret721/fitness-calculator). In brief, a fitness score is weighted summary of normalized 
growth parameters. Fitness scores are determined by first normalizing growth parameters (Max OD, Growth Rate 
and Lag Time) across a data set and summarizing each per curve growth with user defined weights. 
Sulfate determination and quantification.  Sulfate (SO 42-) was quantified using the Spectroquant sulfate test 
(Merckmillipore, Burlington, MA, USA). In brief, acidified sulfate-containing samples are mixed with barium chloride 
and incubated for two minutes. Resulting precipitation is the formation of barium sulfate which is measured on an 
Epoch 2 (Agilent Technologies, Santa Clara, CA, USA) microplate reader at 600 nm. Samples were quantified with 
reference to a calibration curve. 

 
16 
 
Sulfonate determination and quantification. Ethanesulfonate was quantified with targeted metabolomics at the 
Novo Nordisk, Center for Biosustainability analytics department. Samples destined for ethanesulfonate 
quantification were first clarified via centrifugation at 13, 000 g’s for one to five m inutes followed by transfer to a 
microcentrifuge tube. Samples were diluted 1:1000 in ddH 2O in a short -thread 32 x 11.6 mm clear glass vial 
(Mirkolab Aarhus, Aarhus, Denmark) and capped with a silicone/PTFE screw -cap lid (Mikrolab Aarhus, Aarhus, 
Denmark). Samples were analyzed by ultra -high performance liquid chromatography (Nexera X2, Shimaduzu, 
Kyoto, Japan) coupled to tandem mass spectrometry (SCIEX QTRAP 5500, SCIEX Framingham, MA, USA) using 
electrospray ionization in negative ion mode. Selected reaction monitoring was used to quantify ethanesulfonate 
and declustering potential, entrance potential and collision energy and collision cell exit potential values were 
optimizied for each ion transition ( m/z109 > 80 and m/z 109 > 64). Ion source, curtain and collisionally activated 
dissociation gas was generated by an Infitinty 1031 nitrogen generator (Peak Scientific Instruments Ltd, Inchinnan, 
Scotland, UK). Samples were separated using a XSelect® HSS T3 Column (2.1 mm x 50 mm, particle size 2.5 um) 
(WatersTM, Milford, MA, USA) with 10 mM tributalamine, 20 mM acetic acid in 5% (v/v) methanol 2% (v/v) 
isopropanol as eluent A and isopropanol as eluent B. Total run time was 23 minutes. A detailed description of the 
method can be found in the supplementary materials. Injection volumes for each sample was 10 µL and column 
oven temperature 40°C. Data was acquired using the SCIEX Analyst ® software (version 1.7.3) and processed 
using the SCIEX OS software (version 3.0.0.3399). 
Cysteine and free thiol determination and quantification. L-cysteine and free thiols were quantified using 5,5-
dithio-bis-(2-nitrobenzoic acid) (DTNB) established methods (Reiner et al. 2002). In short, DTNB was prepared to 
50 mM concentration in 22.27 mM K 2HPO4 13.59 mM NaH 2PO4 pH ~7.0. Solutions containing free thiols were 
mixed with excess DTNB and incubated at room temperature for five to ten minutes. When in the presence of free 
thiols, DTNB reacts equimolarly with thiols generating an equivalent of 5 -thio-2-nitrobenzoate (TNB 2-). TNB2 - 
produces a strong yellow color and absorbance was measured at 412 nm in an Epoch 2 (Agilent Technologies, 
Santa Clara, CA, USA) microplate reader. Free thiol concentration was calculated with reference to a calibration 
curve. 
Proteomics sample preparation and analysis. Proteomics analysis was performed by the Novo Nordisk, Center 
for Biosustainability analytics department. Samples were prepared as described previously by Kozaeva et al. 2021.  
In brief, P. putida KT2440 was grown overnight in 5 mL of LB brother and the following day, pelleted and washed 
twice with ddH2O. The resulting pellet was resuspended in 2 mL of ddH2O and inoculated in 50 mL deBontCl with 
10 mM glucose to a final OD600 of 0.025-0.05. Sulfur sources were added as described to 2 mM where needed. 
Cultures were incubated in baffled shake flask, OD monitored until strains achieved ~OD 0.5 and a total of 1 OD 
collected for proteomics analysis. 
Proteomics analysis and preparation were performed by the Novo Nordisk, Center for Biosustainability analytics 
department. Briefly, cell pellets were lysed in 6M guanidine HCl, 5 mM tris(2 -carboxyethyl) phosphine, 10 mM 
chloroacetamide and 100 mM Tris HCl (pH = 8.5) disrupted mechanically and heated to 99C. Cell debris were 

 
17 
 
centrifuged and cell free lysate diluted with 50 mM ammonium bicarbonate. Protein content was estimated with 
BCA assay to estimate protein content and 20 ug protein was treated with Trypsin and LysC digestion mix 
(Promega, Madison WI, USA) and incubated fo r 8 hours. Digestions was halted with trifluoroacetic acid and 
samples desalted with a C18 resin (3M, Saint Paul MN, USA) prior to HPLC-MS analysis. 
HPLC-MS analysis was performed on an Orbitrap Exploris 480 (Thermo Fisher, Waltham, MA, USA) preceded by 
an EASY-nLC 1200 HPLC system (Thermo Fisher, Waltham, MA, USA). Peptides were captured on a 2 -cm C18 
trap column (Thermo Fisher, Waltham, MA, USA) and separated with a 60 minute gradient of 8 -48% (v/v) 
acetonitrile in 0.1% (v/v) formic acid on a 15 cm C18 EasySpray ES904 reverse-phase analytical column (Thermo 
Fisher, Waltham, MA, USA) at a flow rate of 250 nL/min. Mass spectrometer was operated with a DD-MS2 method. 
Full MS1 spectra were collected at a resolution of 120,000 and scan range of 400 -1,200 m/z, maximum injection 
time set to auto, intensity threshold of 5.0 and dynamic exclusion at 45 seconds. MS2 spectra were obtained at a 
resolution of 30,000, an isolation window of 1.6 m/z, HCD collision energy set to 28% and maximum injection time 
set to auto. 
Sequence identification was performed using a protein database consisting of the P. putida reference proteome 
retrieved from UniProt on 20 -04-2021. The raw files from the DDA method were analyzed using the Proteome 
Discoverer v2.4 (Thermo Fisher, Waltham, MA, USA) with the following settings: carbamidomethylation of cysteine 
residues and oxidation of methionine residues as dynamic modifications, precursors mass tolerance set to 10 ppm, 
fragment mass tolerance at 0.02 DA, trypsin (full) as digestion enzyme, maximum missed cleavage sites set to 2, 
peptide length set to a minimum of 6 and maximum of 144, and false discovery rate (FDR) set to 1%. Only peptides 
unique to one protein were used in further analysis and normalisation between samples was based on total peptide 
amounts. 
 
 
 
 
 
 
 
 
 
 

 
18 
 
Table 1. Plasmids used and generated in this study 
Plasmid name Description Source 
pSNW2 P14g(BCD2) -> msfGFP; KmR Volke et al. 2020 
pSNW2-ΔcysDNC pSNW2 variant for cysDNC deletion 
(PP_1303-1304) 
This study 
pSNW2-ΔcysNC pSNW2 variant for cysNC deletion (PP_1304) This study 
pSNW2-ΔcysH pSNW2 variant for cysH deletion (PP_2328) This study 
pSNW2-ΔcysB pSNW2 variant for cysDNC deletion 
(PP_2327) 
This study 
pSNW2-Δssu pSNW2 variant for ssuEADCB deletion 
(PP_0236-0240) 
This study 
pSNW2-Δtau pSNW2 variant for tauDABC deletion 
(PP_0230-0233) 
This study 
pSNW2-ΔssuD pSNW2 variant for ssuD deletion (PP_0238) This study 
pSNW2-ΔssuBC pSNW2 variant for ssuBC deletion (PP_0239-
0240) 
This study 
pSNW2-ΔtauD pSNW2 variant for tauD deletion (PP_0230) This study 
pSNW2-ΔtauABC pSNW2 variant for tauABC deletion 
(PP_0230-0232) 
This study 
pQure-6-Strong Xyl/Pm -> I-SceI; P14g(BCD2) -> mRFP; GmR Volke et al. 2020 
 
Table 2. Strains used and generated in this study. 
Strain name Description Source 
P. putida KT2440 ΔcysDNC Bagdasarian et al. 1981 
P. putida KT2440 ΔcysNC This study 
P. putida KT2440 ΔcysH This study 
P. putida KT2440 ΔcysB This study 
P. putida KT2440 Δssu This study 
P. putida KT2440 Δssu tau This study 
P. putida KT2440 Δtau This study 
P. putida KT2440 ΔssuD This study 
P. putida KT2440 ΔssuBC This study 

 
19 
 
P. putida KT2440 ΔtauD This study 
P. putida KT2440 ΔtauABC This study 
P. putida KT2440 ΔssuD tauABC This study 
P. putida KT2440 ΔtauD ssuCB This study 
Escherichia coli DH5α λpir Cloning host, DH5α variant with 
λpir lysogen 
Platt et al. 2000 
  

 
20 
 
 
 
 
Figure 1. Putative metabolic and expressional map of P. putida KT2440 sulfur metabolism. Metabolic reactions 
are given by solid arrows, cell membrane is denoted by solid line, dashed line indicate possible interactions and 
light blue boxes indicate genetic elements. Gene names correspond to P. putida PP numbers as follows: cysA – 
PP_5168, cysU – PP_5170, cysZ – PP_0785, spb-I – PP_4305, spb-II – PP_5171, cysD – PP_1303, cysNC – 
PP_1304, cysH – PP_2328, cysI – PP_2371, cysJ – PP_1703, ssuEADCB - PP_0236_0240, tauDCBA - PP_0230-
0233. Metabolite accronyms are given as follows: APS – adenosine phosphosulfate, PAPS – phosphoadenosine 
phosphosulfate and R -SO3 – aliphatic sulfonates, NAD + - nicotinamide adenine dinucleotide, NADH – reduced 
nicotinamide adenine dinucleotide, FMN – flavin mononucleotide, FMNH2 – reduced flavin mononucleotide, ATP 
– adenosine triphosphate, ADP – adenosine diphosphate, Pi – inorganic phosphate, α-KG – alpha ketoglutarate, 
OAA – oxaloacetate, Met – methionine and Cys - cysteine. 
 
 
 
 
 


 
21 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 2. Investigating preferential sulfur trophism in P. putida KT2440. A) Workflow for sulfur source identification 
and quantification; cultivation media contained 50 uM cysteine, sulfate and ethanesulfonate. Cysteine was detected 
using Ellman’s reagent (5,5′ -dithiobis-(2-nitrobenzoic acid)), sulfate detected using the barium chloride and 
ethanesulfonate detected with targeted metabolomic.  


 
22 
  


 
23 
 
Figure 3.  Combinatorial proteomics characterization of P. putida KT2440 under sulfate, cysteine and 
ethanesulfonate. A) Proteomics workflow and comparison network. Double headed arrows indicate comparisons 
made. B) Heat map of Log 2 transformed relative abundance of select sulfur metabolism enzymes under diverse 
sulfur conditions. C-K) Volcano plots of select pairwise comparison between sulfur conditions. A full list of pairwise 
differentially produced proteins is listed in the supplementary information. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
24 
 
 


 
25 
 
Figure 4.  Fitness heat map of wild -type P. putida and sulfur enzyme disrupted variants under select sulfur 
conditions. Denoted strains are wild-type P. putida (KT2440) or modified strains with deletions to sulfur metabolism 
related genes (e.g. ΔcysDNC). Fitness scores were calculated with a growth parameter weight of 0.05, 0.55 and 
0.4 for lag time, growth rate and growth yield respectively. Sulfur source choice categories and growth parameter 
matrices are listed in the supplementary material. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
26 
 
 
 
Figure 5. Investigating of 6:2 FTSA media preparation. A) Possible reasons for improper 6:2 FTSA media preparation: I) 6:2 FTSA is incompletely dissolved; II) 
Polytetrafluoroethylene (PTFE) media filters absorb passing 6:2 FTSA; and III) final 6:2 FTSA contains contaminating sulfate. B) Solubility test of 10 mM 6:2 FTSA 
in 100% v/v ethanol (left), 50 % v/v ethanol (middle) and 0% v/v ethanol (right) to dissolve 6:2 FTSA. C) Foam test of unfiltered 6:2 FTSA containing media (I), 
filtered 6:2 FTSA containing media (II), filtered octanesulfonate containing media (III) and filtered media with no sulfur source (IV). D) Growth assay of P. putida 
KT2440, ΔcysH and no culture to grow on filtered and unfiltered on deBont medium containing 6:2 FTSA as sole sulfur source E) Dose response curve of P. putida 
KT2440 and del cysH on decreasing concentration of ethanesulfonate with (blue and orange respectively) and without (purple and brown respectively) 6:2 FTSA 
as an additional sulfur source. 

 
27 
 
References 
Ankenbauer, A., Schäfer, R., Viegas, S. C., Pobre, V., Björn Voß, Arraiano, C. M., & Ralf Takors. (2020). 
Pseudomonas putida  KT2440 is naturally endowed to withstand industrial ‐scale stress conditions. Microbial 
Biotechnology, 13(4), 1145–1161.  
Batianis, C., Kozaeva, E., Damalas, S. G., Martín ‐Pascual, M., Volke, D. C., Nikel, P. I., & Martins dos 
Santos, V. A. P. (2020). An expanded CRISPRi toolbox for tunable control of gene expression in Pseudomonas 
putida. Microbial Biotechnology, 13(2), 368–385.  
Bechtel, T. J., & Weerapana, E. (2017). From structure to redox: The diverse functional roles of disulfides 
and implications in disease. PROTEOMICS, 17(6), 1600391.  
Becker, M. A., Kredich, N. M., & Tomkins, G. M. (1969). The purification and characterization of O -
acetylserine sulfhydrylase-A from Salmonella typhimurium. The Journal of Biological Chemistry , 244(9), 2418–
2427.  
Bykowski, T., Ploeg, J. R. van der, Iwanicka -Nowicka, R., & Hryniewicz, M. M. (2002). The switch from 
inorganic to organic sulphur assimilation in Escherichia coli: adenosine 5′-phosphosulphate (APS) as a signalling 
molecule for sulphate excess. Molecular Microbiology, 43(5), 1347–1358. 
Calero, P., Sheila Ingemann Jensen, Bojanovič, K., Lennen, R. M., Koza, A., & Alex Toftgaard Nielsen. 
(2017). Genome‐wide identification of tolerance mechanisms toward p‐coumaric acid in Pseudomonas putida. 
Biotechnology and Bioengineering, 115(3), 762–774.  
Chandra, G., Durg Vijay Singh, Gopal Kumar Mahato, & Patel, S. (2023). Fluorine -a small magic bullet 
atom in the drug development: perspective to FDA approved and COVID-19 recommended drugs. Fluorine-a Small 
Magic Bullet Atom in the Drug Development: Perspective to FDA Approved and COVID-19 Recommended Drugs.  
Cook, T. B., Rand, J. M., Nurani, W., Courtney, D. K., Liu, S. A., & Pfleger, B. F. (2018). Genetic tools for 
reliable gene expression and recombineering in Pseudomonas putida. Journal of Industrial Microbiology & 
Biotechnology, 45(7), 517–527. 
DENK, D., & BOCK, A. (1987). L -Cysteine Biosynthesis in Escherichia coli: Nucleotide Sequence and 
Expression of the Serine Acetyltransferase (cysE) Gene from the Wild -type and a Cysteine -excreting Mutant. 
Microbiology, 133(3), 515–525.  
Douwe, J., Roksana Iwanicka -Nowicka, Bykowski, T., Hryniewicz, M. M., & Leisinger, T. (1999). The 
Escherichia coli ssuEADCB Gene Cluster Is Required for the Utilization of Sulfur from Aliphatic Sulfonates and Is 
Regulated by the Transcriptional Activator Cbl. Journal of Biological Chemistry, 274(41), 29358–29365.  

 
28 
 
Douwe, J., Roksana Iwanicka -Nowicka, Kertesz, M. A., Leisinger, T., & Hryniewicz, M. M. (1997). 
Involvement of CysB and Cbl regulatory proteins in expression of the tauABCD operon and other sulfate starvation-
inducible genes in Escherichia coli. Journal of Bacteriology, 179(24), 7671–7678.  
Drinking Water Advisory: Consumer Acceptability Advice and Health Effects Analysis on Sulfate. (2003). 
https://www.epa.gov/sites/default/files/2014-09/documents/support_cc1_sulfate_healtheffects.pdf 
Du, Q., Wang, H., & Xie, J. (2011). Thiamin (Vitamin B1) Biosynthesis and Regulation: A Rich Source of 
Antimicrobial Drug Targets? International Journal of Biological Sciences, 7(1), 41–52.  
Eichhorn, E., van der Ploeg, J. R., & Leisinger, T. (1999). Characterization of a Two -component 
Alkanesulfonate Monooxygenase from Escherichia coli. Journal of Biological Chemistry, 274(38), 26639–26646.  
Eichhorn, E., van der Ploeg, J. R., & Leisinger, T. (2000). Deletion Analysis of the Escherichia coli Taurine 
and Alkanesulfonate Transport Systems. Journal of Bacteriology, 182(10), 2687–2695.  
Elbing, K., & Brent, R. (2002). Media Preparation and Bacteriological Tools. Current Protocols in 
Molecular Biology, 59(1).  
Ellis, H. R. (2011). Mechanism for sulfur acquisition by the alkanesulfonate monooxygenase system. 
Bioorganic Chemistry, 39(5-6), 178–184.  
Ellman, G. L. (1959). Tissue sulfhydryl groups. Archives of Biochemistry and Biophysics, 82(1), 70–77.  
Glüge, J., Scheringer, M., Cousins, I. T., DeWitt, J. C., Goldenman, G., Herzke, D., Lohmann, R., Ng, C. 
A., Trier, X., & Wang, Z. (2020). An overview of the uses of per - and polyfluoroalkyl substances (PFAS). 
Environmental Science: Processes & Impacts, 22(12), 2345–2373.  
Hartmans, S., Smits, J. P., van der Werf, M. J., Volkering, F., & de Bont, J. A. (1989). Metabolism of 
Styrene Oxide and 2 -Phenylethanol in the Styrene -Degrading Xanthobacter Strain 124X. Applied and 
Environmental Microbiology, 55(11), 2850–2855.  
HINDSON, V. J. (2003). Serine acetyltransferase of Escherichia coli: substrate specificity and feedback 
control by cysteine. Biochemical Journal, 375(3), 745–752.  
Israel, E., Ramganesh Selvarajan, King, L., & Chioma Blaise Chikere. (2023). Quorum Sensing: 
Unravelling the Intricacies of Microbial Communication for Biofilm Formation, Biogeochemical Cycling, and 
Biotechnological Applications. Journal of Marine Science and Engineering, 11(8), 1586–1586.  
Jeong, H., Kim, H. J., & Lee, S. J. (2015). Complete Genome Sequence of Escherichia coli Strain BL21. 
Genome Announcements, 3(2).  
Jovanovic, M., Lilic, M., Savic, D. J., & Jovanovic, G. (2003). The LysR-type transcriptional regulator CysB 
controls the repression of hslJ transcription in Escherichia coli. Microbiology, 149(12), 3449–3459.  

 
29 
 
Jurgenson, C. T., Begley, T. P., & Ealick, S. E. (2009). The Structural and Biochemical Foundations of 
Thiamin Biosynthesis. Annual Review of Biochemistry, 78(1), 569–603.  
Kertesz, M. A. (2000). Riding the sulfur cycle – metabolism of sulfonates and sulfate esters in Gram -
negative bacteria. FEMS Microbiology Reviews, 24(2), 135–175.  
Korshunov, S., Imlay, K. R. C., & Imlay, J. A. (2019). Cystine import is a valuable but risky process whose 
hazardsEscherichia coliminimizes by inducing a cysteine exporter. Molecular Microbiology, 113(1), 22–39.  
Kredich, N. M. (1992). The molecular basis for positive regulation of cys promoters in Salmonella 
typhimurium and Escherichia coli. Molecular Microbiology, 6(19), 2747–2753.  
Leyh. (2015). The sulfate activation locus of Escherichia coli K12: cloning, genetic, and enzymatic 
characterization. The Journal of Biological Chemistry, 263(5).  
Lochowska, A., Iwanicka-Nowicka, R., Plochocka, D., & Hryniewicz, M. M. (2001). Functional Dissection 
of the LysR-type CysB Transcriptional Regulator. Journal of Biological Chemistry, 276(3), 2098–2107.  
Marino, R. W., & Howarth, R. (2014). Nitrogen Fixation in Freshwater and Saline Waters ☆. Reference 
Module in Earth Systems and Environmental Sciences.  
Nikel, P. I., Fuhrer, T., Chavarría, M., Sánchez -Pascuala, A., Sauer, U., & de Lorenzo, V. (2021). 
Reconfiguration of metabolic fluxes in Pseudomonas putida as a response to sub-lethal oxidative stress. The ISME 
Journal, 15(6), 1751–1766. 
Nishikawa, M., Shen, L., & Ogawa, K. (2018). Taurine dioxygenase (tauD) -independent taurine 
assimilation in Escherichia coli. Microbiology, 164(11), 1446–1456. 
Nour-Eldin, H. H., Hansen, B. G., Nørholm, M. H. H., Jensen, J. K., & Halkier, B. A. (2006). Advancing 
uracil-excision based cloning towards an ideal technique for cloning PCR fragments. Nucleic Acids Research , 
34(18), e122–e122.  
O’Hagan, D. (2008). Understanding organofluorine chemistry. An introduction to the C –F bond. Chem. 
Soc. Rev., 37(2), 308–319. 
Purser, S., Moore, P. R., Swallow, S., & Gouverneur, V. (2008). Fluorine in medicinal chemistry. Chem. 
Soc. Rev., 37(2), 320–330.  
Reva, O. N., Weinel, C., Weinel, M., Bo ̈hmK., Stjepandic, D., HoheiselJ. D., & Tu ̈mmlerB. (2006). 
Functional Genomics of Stress Response in Pseudomonas putida KT2440. Journal of Bacteriology , 188(11), 
4079–4092.  
Riener, C. K., Kada, G., & Gruber, H. J. (2002). Quick measurement of protein sulfhydryls with Ellman’s 
reagent and with 4,4′-dithiodipyridine. Analytical and Bioanalytical Chemistry, 373(4-5), 266–276. 

 
30 
 
Rodríguez-Robles, E., Müller, D., Tilmann Künzl, Nemat, S. J., Martin Peter Edelmann, Srivastava, P., 
Louis, D., Elisabetta Groaz, Konrad Tiefenbacher, Tania Michelle Roberts, Piet Herdewijn, Philippe Marlière, & 
Panke, S. (2024). Rational design of a bacterial import system for new-to-nature molecules. Metabolic Engineering, 
85, 26–34. 
Takagi, H., & Ohtsu, I. (2016). l -Cysteine Metabolism and Fermentation in Microorganisms. Amino Acid 
Fermentation, 129–151. 
van der Ploeg, J., Eichhorn, E., & Leisinger, T. (2001). Sulfonate -sulfur metabolism and its regulation in 
Escherichia coli. Archives of Microbiology, 176(1-2), 1–8. 
Vermeij, P., & Kertesz, M. A. (1999). Pathways of Assimilative Sulfur Metabolism in Pseudomonas putida. 
Journal of Bacteriology, 181(18), 5833–5837. 
Volke, D. C., Olavarría, K., & Nikel, P. I. (2021). Cofactor Specificity of Glucose -6-Phosphate 
Dehydrogenase Isozymes in Pseudomonas putida Reveals a General Principle Underlying Glycolytic Strategies 
in Bacteria. MSystems, 6(2), e00014-21.  
Volke, D. C., Wirth, N. T., & Nikel, P. (2021). Rapid Genome Engineering of Pseudomonas Assisted by 
Fluorescent Markers and Tractable Curing of Plasmids. BIO-PROTOCOL, 11(4).  
Weimer, A., Kohlstedt, M., Volke, D. C., Nikel, P. I., & Wittmann, C. (2020). Industrial biotechnology of 
Pseudomonas putida: advances and prospects. Applied Microbiology and Biotechnology, 104(18), 7745–7766.  
Wirth, N. T., Funk, J., Donati, S., & Nikel, P. I. (2023). QurvE: user -friendly software for the analysis of 
biological growth and fluorescence data. Nature Protocols, 18(8), 2401–2403. https://doi.org/10.1038/s41596-023-
00850-7 
Zhang, S., Lu, X., Wang, N., & Buck, R. C. (2016). Biotransformation potential of 6:2 fluorotelomer 
sulfonate (6:2 FTSA) in aerobic and anaerobic sediment. Chemosphere, 154, 224–230.  
  

 
31 
 
Chapter 2: Upgrading the Chi.Bio system for automated 
cultivation, quantitative physiology analysis and adaptive 
laboratory evolution of biotechnologically-relevant bacteria 
Garret W. O'Connell1, Stefano Donati1, Filippo Federici1, Maria Victoria Gracia Alvan-Vargas1,  
Aina Sendra-Ortiz1, Lachlan J. Munro1, Lars K. Nielsen2 & Pablo I. Nikel1* 
1Novo Nordisk Center for Biosustainability, Systems Environmental Microbiology group 
2Novo Nordisk Center for Biosustainability, Automation group 
3University of Queensland 
 
Cell factories are the foundation to a growing bio -economy and, development of cell factories often 
require deployment of laborious techniques such as adaptive laboratory evolution or multi -omics 
characterization. These techniques are central to the Test a nd Learn aspects of the Design -Build-Test-
Learn cycle but, are often time consuming or inconvenient. To that end, bioreactors represent an ideal 
technology to automate passaging of strains or maintaining strains in a static metabolic state. Here we 
attempt to demonstrate the power of the commercially available Chi.Bio system as effective tool for gas-
enriched cultivation, adaptive laboratory evolution and omics sampling. Chi.Bio system reactors allowed 
for a growth of Pseudomonas putida rG1 and a 1.6-fold growth yield of Cupriavidus necator when CO2 
was sparged. Where adaptive laboratory evolution is concerned, simple modifications to the Chi.Bio 
system code base allowed for the growth rate optimization of Pseudomonas putida SEM10 and rG1 with 
resulting isolates having 1.2-1.8- and 1.15-1.2-fold increases in growth rate respectively. With custom 
code implemented, Escherichia coli  was successfully underwent a tolerance adaptive laboratory 
evolution and with modified Chi.Bio lids, omics sampling of Escherichia coli and Pseudomonas putida 
was possible. With some minor modifications to the out-of-the-box Chi.Bio codebase and lids, the Chi.Bio 
system can be used to cultivate bacteria in gas -enriched environments, adapt bacteria through two 
different kinds of adapti ve laboratory evolution and maintain bacteria in a static exponential state. 
Together, these make the Chi.Bio system an affordable piece of laboratory equipment for cell factory 
optimization and characterization and, with further analysis, a real contender  for every-day laboratory 
equipment. 
  

 
32 
 
INTRODUCTION 
 
Laboratory evolution and multi -omics analysis are cornerstones to the development of cell factories. 
Adaptive laboratory evolution (ALE) is a technique which allows for selection natural or synthetic 
phenotypes through repeated propagation of cells whereas multi-omics analysis, such as proteomics and 
metabolomics, allow insight into the physiological state of a developed strain. ALE can be divided into 
two major categories growth rate optimization and tolerance ALE (GRO- and T-ALE). Through GRO-ALE, 
cells can be evolved to more effectively utilize substrates, have an increased growth rate and through T-
ALE, tolerance to toxic or stressor compounds can be propagated across a population (Sandberg et al. 
2019). Multi-omics characterization involves the integration of omics experiments such as proteomics 
and metabolomics to gleam useful information regarding the genetic regulation and metabolism of a cell 
factory (Amer and Baidoo, 2021). Multi -omics characterization is key component to the Learn step of 
Design-Build-Test-Learn cycle, and efficient methods to perform multi-omics experiments are becoming 
increasingly important as data sources for AI and machine learning systems (Opegenorth et al. 2019). 
 
Traditionally, ALE and multi -omics experiments involve serial batch cultivation (e.g. re -inoculating a 
culture every day) to effectuate evolution or keep a desired culture in a steady metabolic state. This 
practice is, unfortunately, incompatible with a Monday to Friday, 9-5 work week due to a variety of issues 
such as long lag phases or slow growth rates, heterogeneous growth rates among strains or populations 
and sampling at inconvenient times. While automated systems to perform ALE are available, they ar e 
generally built on either expensive existing liquid handling systems. To that end, automated bioreactor, 
such as turbidostats, with in -line growth measurements allow a user to automate their evolution 
experiment or keep strains and populations in a static steady state for convenient sampling. 
 
Several bioreactors exist on the market today. On the higher end, the AMBR system (Sartorius, 
Göttingen, Germany) is an effective, disposable, bioreactor which can cost in the hundreds of thousands 
of USD. Reactors like these often have high monetary and skillset barriers of entry and are spacious and 
laborious to use. Alternatively, a number of automated DIY bioreactors have been described to date such 
as eVOLVER (Wang et al. 2018) and many more (Pen et al. 2021, Hoffman et al. 2017 and, Takahashi 
et al. 2015). However, among DIY reactors, only the Chi.Bio ( https://chi.bio/) and, recently, Pioreactor 
(https://pioreactor.com/) systems are commercially available.  
 

 
33 
 
The most promising DIY system to date is the Chi.Bio system. Steele et al. [1] succinctly demonstrated 
the ability of the Chi.Bio system to cultivate and automated growth rate measurements of Escherichia 
coli, follow multiple induced fluorescent outputs and develop novel programs with the system. 
Furthermore, the Chi.Bio system has been used to study population dynamics with manual and 
automated sampling (Joshi et al . 2022 and Berteaux et al . 2022), adapt an SOS gene circuit in 
Escherichia coli (Chen et al . 2021)  and implement synthetic formatotrophy Escherichia coli over the 
course of 150 days (Wenk et al. 2022). With the exception of the work done by Steele et al. 2020, each 
study tailored the Chi.Bio system out -of-the box to their specific goal. Steele et al. 2020 noted that the 
possible applications of the Chi.Bio systems are broad. Here, we set out to improve the out -of-the box 
Chi.Bio system for cultivation of biotechnologically relevant microorganisms, cultivation in gas enriched 
environments, GRO-ALE in non-gas and gas enriched environments, T -ALE and multi-omics sampling 
of biotechnologically relevant microorganisms and provide a road map for others to follow. 
 
  

 
34 
 
RESULTS AND DISCUSSION 
 
Benchmarking batch cultures of Pseudomonas putida KT2440 and Escherichia coli MG1655 in 
Chi.Bio reactors 
The original setup of the Chi.Bio system calls for the use of 40 -mL vials covered with lids bearing a 3.5-
cm outlet. This combination effectively allows for a 20-24 mL working volume in a 40-mL vial — thus, with 
a mere 16 -20 mL of headspace, a concern is o xygen transfer and availability. In the case of obligate 
aerobes relying on an oxidative metabolism (such as P. putida), this cultivation setup could lead to 
restrictions in microbial growth; whereas for facultative anaerobes (such as E. coli), oxygen-limitation 
would mediate a shift to fermentative metabolism — likewise limiting cell densities. To test the extent of 
these technical concerns, we picked a model bacterium falling within each of these categories and we 
established batch cultivations in the Chi .Bio system, where the oxygen transfer was modified by 
increasing stirring rates in the reactors. The Gram -negative bacteria P. putida KT2440 and  E. coli 
MG1655 were adopted as examples of an obligate aerobe and a facultative anaerobe, respectively. 
These strains were cultivated at 0.25, 0.5, 0.75 and 1.00 spinning speed setups in the Chi.Bio system 
(translating to 1,125; 2,250; 3,375; and 4,500 rpm) either on a complex medium (LB medium) or a mineral 
medium [de Bont minimal (DBM) medium or M9 medium, for P. putida and E. coli, respectively] containing 
20 mM glucose as the sole carbon substrate. In all cases, the optical density was recorded online during 
the entire cultivation, and the QurvE software was used to calculate the specific growth rates (m). 
 
P. putida KT2440 cultures had increasing m values with higher spinning speeds, from m = 0.128 ± 0.031 
h-1 up to 0.751 ± 0.046 h -1 in LB medium and m = 0.116 ± 0.033 h -1 up to 0.573 ± 0.015 h -1 in DBM 
medium with 20 mM glucose ( Fig. 1). These results line up with reported maximal growth rates of P. 
putida KT2440 grown on LB medium (La Rosa et al. 2015) and on DBM with glucose (Wang et al. 2019) 
in larger scale cultivation setups. Conversely, E. coli had an increase in m values with faster agitation 
only in cultivations on LB medium (from m = 0.378 ± 0.012 h-1 to 0.867 ± 0.041 h-1). In M9 medium with 
glucose, however, m showed no clear increasing or decreasing patterns with respect to agitation sp eed 
(Fig. 1), and the calculated growth rates for these cultivations spanned values between m = 0.619 ± 
0.068 h-1 at 1,125 rpm to 0.520 ± 0.061 h-1 at 4,500 rpm. Although no clear trend was observed in these 
cultures, growth rates between 0.5-0.65 h-1 have been reported for E. coli MG1655 growing on a mineral 
medium with glucose as the carbon source (Smirniva and Oktyabrysky, 2017 and Rugbjerg et al. 2018), 
consistent with our calculated m values. On LB medium, E. coli has been reported to grow in bioreactors 
with rates above 1.0 h -1 when oxygen is not limited (Baev et al. 2006 and Smirniva and Oktyabrysky, 

 
35 
 
2017). The disparity between the kinetic parameters of E. coli grown on LB and M9 with glucose is likely 
caused by the limited amount of fermentable sugars and amino acids available in LB medium (Zhou et 
al. 2022, Sezonov et al. 2018). At the same time, under these conditions, optimal growth of E. coli was 
achieved in minimal medium even at the lowest agitation rate (1,125 rpm). Expectedly, P. putida was 
more sensitive to this parameter. Taken together, these results show that we were able to achieve near 
reported optimal growth rates for both bacterial species in the Chi.Bio system, allowing for precise 
determinations of the growth rates. 
 
Gas-enriched cultivation of engineered formatotrophic P. putida and Cupriavidus necator 
With growing interest in utilizing C1 feedstocks in cell factories, the use of bioreactors capable of handling 
engineered and natural bacteria that can grow in enriched CO 2 environments has become ever more 
demanding. However, small -scale fermentors that can be run in parallel are scarce. To bridge this 
technical gap, we developed an adapted Chi.Bio lid with secondary inlet spout that dips below the media 
during cultivation and, when connected to a gas mixer, can deliver continuous sparging gases. As proof 
of principle, P. putida rG1 (a formatotrophic strain previously engineered in our laboratory) and 
Cupriavidus necator (a native C1-trophic bacterium,) were incubated in the upgraded Chi.Bio system with 
continuous sparging of 10% (v/v) CO2 at a rate of 33 mL min-1 (Fig. 2). 
 
P. putida rG1 is an engineered formatotrophic strain derivative of reduced -genome P. putida EM42 that 
requires excess CO2 to drive the glycine cleavage system (GCS) in the reverse direction and effectively 
incorporate CO2 into biomass (Fig. 2A). This strain uses formate as carbon substrate and, to a lesser 
extent, for energy regeneration (through the activity of formate dehydrogenases). Acetate can be fed to 
support ATP formation, enhancing bacterial growth by leaving more formate available for biomass build-
up. When cultivated on formate and acetate as carbon and energy source, respectively, P. putida rG1 
has been reported to have a doubling time of ~31 h. We tested if the upgraded Chi.Bio system could 
support the CO2-dependent growth of this formatotrophic strain, and we cultivated P. putida rG1 in DBM 
medium containing formate and acetate as reported previously. In a set of experiments, adopted as 
control conditions, no CO2 sparging was provided (other than the CO2 present in the ambient), whereas 
in the remaining cultivations, CO2 was sparged at a continuous rate of 33 mL min-1. As expected, P. putida 
rG1 could not grow in the absence of CO 2 since there is no metabolic push to support formate 
assimilation; with gas sparging, however, this formatotrophic strain could grow with a growth rate of 0.045 
± 0.001 h-1 (Fig. 2C). This value is within the range of doubling times reported by Turlin et al. 2022, where 
the authors cultivated P. putida rG1 in microtiter plate readers. The maximum OD 600 reached in these 
cultures was 0.59 ± 0.08, with a slight drop by the end of the cultivation (90 h). Under control conditions, 

 
36 
 
the biomass remained at the same level as in the inoculum used to start the bioreactor cultivations, 
indicating no net carbon assimilation but also no cell death. These results indicated that the cultivation 
setup has a strong influence in the growth param eters of engineered bacteria and validated the use of 
our adapted Chi.Bio system to support formatotrophic growth of the engineered P. putida strain rG1.  
 
C. necator is a natural CO2-fixing lithotrophic and autotrophic bacterium, which converts CO2 into biomass 
through the Calvin-Benson-Bassham cycle (Fig. 2B). When cultivated in the upgraded Chi.Bio system in 
M9 minimal medium with formate (in this case, added as an energy source), C. necator H16 was able to 
grow with or without CO2 sparging, with a growth rate of 0.08 ± 0.05 h-1 and 0.18 ± 0.04 h-1, respectively 
(Fig. 2D). The maximum OD600 values by the end of the cultivation were 0.48 ± 0.02 and 0.078 ± 0.003, 
respectively. Growth rates between 0.04 h -1 and 0.18 h -1 have been reported in the lite rature for C. 
necator H16 growing on formate as sole carbon source (Grunwald et al 2015, Yu et al 2018 and Calvey 
et al. 2023). While growth rate variations do exist due to culture set-up, CO2 availability has a substantial 
impact on the growth rate and biomass yield of C. necator, with sparging nearly doubling the growth rate 
and mediating a 1.6-fold increase in the final OD600. Taken together, these results show that our updated 
Chi.Bio setup, equipped with modified lids and air sparging devices, can deliver an enriched CO 2 
environment to the cultivation milieu to grow both native and engineered C1-trophic bacteria. 
 
Adaptation of Pseudomonas putida SEM10 for effective utilization of ribose as sole carbon source 
Adaptive laboratory evolution is a key tool that can complement metabolic engineering approaches 
towards obtaining a desired phenotype. To that end, we explored the applicability of the Chi.Bio system 
as a tool for enhancing growth rate optimization adapti ve laboratory evolotuion (GRO-ALE) to enhance 
microbial growth rates (i.e., acceleration). We tested if P. putida could be adapted to grow on a non -
preferred sugar substrate in this platform. Ribose is a pentose that, upon transport into the cell, is 
processed through the upper catabolism via phosphorylation to ribose 5 -phosphate ( Fig. 3A ). This 
phosphorylated sugar is then assimilated through the EDEMP cycle to yield triose phosphate 
intermediates, ultimately leading to biomass building blocks. Owing to the ATP demand for 
phosphorylation and, probably, limited fluxes through the lower cat abolism, ribose is considered to be a 
poor substrate for P. putida and supports low growth rates and limited biomass yields. 
 
To evaluate the use of the Chi.Bio platform for ALE, we selected a genome -reduced P. putida strain, P. 
putida SEM10, for long -term evolution on pentoses. Specifically, strain SEM 10 was grown in de Bont 
medium in the presence of 10 mM ribose for 260 h, and a serial passage into fresh medium, containing 
the same amount of ribose, was prompted every time that the OD600 ~0.75 (Fig. 3B). This sequence was 

 
37 
 
automated by modifying the built -in ‘dither’ function to the Chi.Bio software. In brief, the Chi.Bio system 
has a ‘dither’ function which oscillates the target OD set in the Chi.Bio dashboard by a defined value. 
This oscillation allows for automated calcul ation of growth rate in the dashboard. By changing the 
oscillation value from 0.05 to 0.5, the oscillation occurs across a total amplitude of 1 OD Chi.Bio instead of 
0.1, an approximate difference OD 600 0.5 instead of 0.05 (Supplementary Material). Over the  course of 
the ALE experiment, a clear increase in growth rate was observed as seen by the decrease in the time 
between phases (Fig. 3B). Phases are defined as the OD values between positive and negative inflection 
points over the ALE experiment (valley to peak). Inflection points were automatically calculated with the 
QurveX program. The OD 600 data was used to calculate growth rates during the evolution process; 
between 50 and 200 h of incubation in the Chi.Bio reactors, the growth rate of the bacterial po pulation 
nearly tripled, from 0.0221 to 0.0489 h -1 (Fig. 3C). Following the end of the ALE experiment, reactor 
populations were streaked on LB plates and resulting colonies screened for increased growth rate on 
ribose as sole carbon source. Three isolates (termed RA2, RA3, and RA6) were chosen based on their 
reduced duplication times, in all cases <  80% of that of the parental strain (21.4  ± 0.5 h; Fig. 3D), and 
their genome sequenced.  
 
Several mutations were identified in the chromosome of these isolates as compared to the parental strain 
(summarized in Table S1 in the Supplementary Information). Out of these mutations,  all three isolates 
RA2, RA3, and RA6 shared a silencing mutation in the pykA gene (PP_1362, encoding pyruvate kinase 
A). Gene silencings are given in Table S3; in summary, RA2 contained an C → A transversion likely 
affecting enzyme active site, RA3 contained an CC insertion near the N-terminus of the enzyme leading 
to a frameshift and RA6 contained an G → C transition leading to a premature stop codon. Given the 
role of PykA in the lower catabolism of P. putida, we speculated that these mutations found in the cognate 
gene may be involved in improved ribose metabolism. To explore the  possibility that the growth rate 
increase is associated to pykA silencing, we deleted the gene via allelic exchange in the parental, 
unadapted SEM10 strain (Volke et al., 2020, 2021). When cultivated with 10 mM ribose as sole carbon 
source in 96-well microtiter plates, strains with the pykA deletion showed significant growth rates 1.8 -
fold higher than the parental strain and, interestingly, a significant 1.2 -fold higher growth rate over the 
adapted strains (Fig. 3D and 3E). While an increased growth rate was observed on ribose when pykA 
was disrupted, the exact underlying mechanism for this phenotype remains unclear. In E. coli , for 
instance, deletion of both pyruvate kinase-encoding genes is known to increase the flux via the pentose 
phosphate pathway under some conditions (Emmerling et al., 2002; Meza et al., 2012; Ponce et al., 
1998). E. coli PykA is allosterically activated by phosphorylated sugars from the pentose phosphate 
pathway, including ribose 5-phosphate (Meza et al., 2012; Mort & Sanwal, 1978; Waygood et al., 1975). 

 
38 
 
Assuming that this regulatory mechanism is similar in P. putida, it could be hypothesized that feeding 
ribose to strain SEM10 leads to an accumulation of ribose 5 -phosphate and other phosphorylated 
pentoses, and, therefore, an overactivation of PykA leading to excessive depletion of upstream 
metabolites such as phosph oenol pyruvate, 2 -phosphoglycerate, 3 -phosphoglycerate and glycerol -3-
phosphate. Interestingly, no mutations in the pykA gene were found in ALE experiments to improve the 
growth of engineered s trains of P. putida on xylose, despite the structural similarity of the two sugars 
(Elmore et al., 2020; Espeso et al., 2020; Lim et al., 2021). 
 
Adaptation of the formatotrophic P. putida strain rG1 in a CO2-enriched environment 
The results in the previous section exposed the value of the upgraded Chi.Bio system for ALE of P. 
putida. Based on these experiments, we decided to explore the capacity of the Chi.Bio reactors for 
conducting ALE under a controlled atmosphere, namely, with CO 2 enrichment (Fig. 4 ). As explained 
above, formatotrophic P. putida strains are characterized by a low growth rate when incubated in the 
presence of formate as the only carbon source. Hence, we optimized the growth of P. putida rG1 on 
formate in the pre sence of CO 2. In de Bont medium with 20 mM acetate and 80 mM formate, we were 
able to continuously and stably cultivate strain  rG1 for 400 h (Fig. 4B) with continuous sparging of 10% 
CO2 at ~ 33 mL/min. Growth rate evolution was monitored over approximately the same number of 
phases as the previous experiment ( Fig. 3B). The change in the growth features over the phases (i.e., 
acceleration) was more subtle than what was observed during the ALE on ribose, with the growth rate 
increasing from 0.03 h -1 to 0.05 h-1 from phase 3 to 10 ( Fig. 4C). At the end of the ALE, isolates were 
streaked on LB agar and picked for further screening based on their growth parameters. In this case, LB 
was chosen for isolation due to the very slow growth of P. putida rG1 on de Bont medium with acetate 
and formate. Out of the isolates screened, P. putida rG1-E1 and rG1-E2 outperformed the parental rG1 
strain with a 1.145- and 1.38-fold reduced lag phase (Fig. 4D and Fig S3.) and displaying growth rates 
1.15- and 1.2-fold higher, respectively, than the non-evolved strain (Fig. 4E). 
 
Following the same scheme as discussed for the ALE on ribose, we performed whole -genome 
sequencing on the evolved isolates (Table S4). This analysis did not reveal an immediately clear pattern 
of shared mutations between strains rG1-E1 and rG1-E2 that could explain the increased growth rate of 
either isolate ( Table S5 -7). Nevertheless, both P. putida rG1-E1 and rG1 -E2 shared three allelic 
variations, a GCC insertion between PP_4887 (a hypothetical protein) and PP_4888 (encoding a methyl-
accepting chemotaxis  transducer), as well as two substitutions between sbcD (PP_2025, encoding 
exonuclease subunit SbcD) and PP_5497 (a Rhs repeat -associated core domain -containing protein) 
(Table S6). Both strains did, however, have unique single nucleotide polymorphisms (SNPs) in nadA 

 
39 
 
(PP_1231) (Table S5). NadA is a quinolate synthase which converts 2 -iminosuccinate and glycerone 
phosphate to quinilate (pyridine-2,3-dicarboxylate), phosphate and water (Saunders and Booker, 2008). 
NAD+ is required in the serine branch of the glycine cleavage system to produce 5,10 -methylene-
tetrahydrofolate (Turlin et al. 2022). Should the SNPs found in the evolved rG1 -E1 and rG1-E2 clones 
increase the NAD+ pool, it could lead to increased fluxes through the serine branch of the glycine cleavage 
system. 
 
Interestingly, we identified a C→T transition in BCD10, a translational coupler upstream of the gcvH-I 
gene in isolate rG1 -E1 ( Table S7 ). The GcvH-I protein is one of two carrier proteins of the glycine 
cleavage system and is encoded in an operon together with gcvP-I, tdcG-II, and gcvT-I (Turlin et al. 
2022). These proteins are involved in glycine generation and pyruvate synthesis in the formatotrophic 
rG1 strain (Turlin et al . 2022). BCD motifs are synthetic regulatory elements that modulate protein 
production without modifying the promoter sequence (Claasen et al. 2019). It can be hypothesized that 
the C→T transition in the BCD10 element upstream of gcvH-I increases the availability of enzymes 
needed for the conversion of formate to glycine or stabilizes protein and enzyme levels within the cell. 
The rG1-E2 isolate, in contrast, did not contain any modification within the BCD10 element upstream of 
gcvH-I. Rather, this evolved clone had a T→G transversion in the 257 -bp long intergenic region 
downstream of ppc (PP_1505) and upstream adk (PP_1506) (Table S7). Ppc is a phosphoenolpyruvate 
carboxylase that converts oxaloacetate to phosphoenolpyruvate (Matsuoka and Shimizu, 2013), while 
Adk is an adenylate kinase which mediates the transformation of AMP and ATP to two molecules of ADP 
(Brune et al . 1985). Modulation of the ppc expression or activity could potentially lead to a higher 
anaplerotic flux towards oxaloacetate formation from phosphoenolpyruvate, which, in turn, could support 
increased growth rates (Turlin et al. 2022). Given that the transversion was found downstream ppc, it is 
more plausible that this mutation influences the expression of adk. Adk is involved in energy homeostasis 
(Rodionova et al. 2017), with an important role in maintaining ATP/ADP ratios in acetate -grown E. coli 
(Lu et al. 1996). Since we adapted the engineered P. putida rG1 to use acetate as the only energy source, 
modulating Adk levels could have a positive impact in energy allocation, affecting both growth rates and 
cell density under formatotrophic growth conditions.  
 
In future work, reverse -engineering the identified mutations and allelic variants will shed light on the 
underlying mechanism used by clones rG1 -E1 and -E2 for increased growth rate and OD 600 on formate 
and acetate and carbon and energy sources. The use of the upgraded Chi.Bio system enabled us to 
isolate clones with enhanced growth characteristics, which exposes the value of this platform to execute 

 
40 
 
ALE programs under carefully controlled environmental conditions, such as a gas atmosphere enriched 
in CO2. 
 
Adaptation of wild-type E. coli MG1655 to improve tolerance to butanol 
As illustrated in the examples above, ALE is a powerful tool to optimize growth parameters, and microbial 
tolerance to specific stressors can also be improved by means of tolerance adaptive laboratory evolution 
(T-ALE) (Sandberg et al. 2019). On this background, we explored if the Chi.Bio platform could be adapted 
to run T -ALE experiments to improve the tolerance of biotechnologically -relevant bacterial species to 
alcohols. To this end, we modified the open-source Chi.Bio software to introduce a function that steadily 
increases the concentration of a given toxic stressor while holding the cells in an exponential growth 
phase (Fig. 5). The modified script is available at https://github.com/ljm176/Chi.Bio. In brief, the modified 
Chi.Bio script provides a new ALE functionality in the Chi.Bio platform. When engaged, the Chi.Bio 
software will operate in 10 phase cycles upon which at the tenth, the ratio between media A (starting 
media) and media B (stress med ia) is changed by 5%. Under these conditions, the ratio of starting to 
stressor media should change in favor of increasing stressor. 
 
To demonstrate the utility of this novel functionality, we adapted the wild -type E. coli strain MG1655 to 
increasing butanol concentrations. Butanol is an alcohol that has attracted significant interest as a biofuel, 
and several studies have attempted to produce butanol in engineered E. coli (Nawab et al. 2020). A major 
ongoing barrier to butanol production by engineered microbial hosts, however, is the toxic effects of the 
alcohol above a relatively low threshold concentration. Some promising strategies have been 
implemented to improve butanol tolerance in E. coli including, for instance, efflux protein engineering 
(Fischer et al. 2013) and overexpression of stress response genes (Xu et al. 2020). 
  
In our setup, E. coli was incubated in M9 minimal medium containing 2% w/v glucose as the main carbon 
substrate, and the butanol concentration was increased stepwise. We successfully utilized the 
customized T-ALE function in the upgraded Chi.Bio system to reach butanol concent rations of 1.2% v/v 
over 150 h (Fig. 5A). In a stepwise fashion, the modified Chi.Bio script increased the stressor to relaxing 
media ratio by 0.05 every 10 phases leading to an effective butanol concentration increase of 0.15% v/v 
each step. These eight steps were 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05 and 1.2 % v/v butanol. 
 
During the adaptation experiment, we observed the inverse cell density trajectories as in the other ALE 
examples (Fig. 5B), where the cells recovered after each ratio change (i.e., an increase in the butanol 
concentration) but growth rate decreased with successive phases ( Fig. 5C ). The T -ALE experiment 

 
41 
 
ended after ~130 h due to the abrupt decrease in OD 600 values, likely indicating cell death, which 
highlights the upper limit of butanol tolerance under these conditions ( Fig. 5B). We observed a steady 
decrease in the growth rate over the course of the T -ALE experiment (µ specific = 0.899 h -1 to 0.443 h -1, 
Fig. 5C). We isolated clones from the end-point population on LB agar and, out of the isolates identified 
from the T-ALE experiment, two isolates (termed 3_3 and 3_5) showed an increase in the growth rate 
when cultivated in batch cultures with M9 medium containing 2% w/v glucose and 1.2% v/v butanol (Fig. 
5D). E. coli MG1655, the parental strain, grew with  = 0.224 ± 0.018 h-1, whereas the adapted isolates 
3_3 and 3_5 had a  = to 0.271 ± 0.030 h-1 and 0.293 ± 0.054  h-1, respectively (Fig. 5E). Further, lag 
times between parental and adapted strains decreased from 2.715 ± 0.248 h to 2.185 ± 0.355 h and 
2.125 ± 0.515 h respectively ( Fig S4.). While growth rates increase and lag time decrease do indicate 
an adaptation to butanol as a stressor, the lack of statistical significance between data sets does shed 
doubt on an underlying physiological difference. That said, the script her e-in can be used recursively to 
achieve significant adaptation, given appropriate sampling. 
 
While the genetic basis for the improved phenotypes in these adapted E. coli clones is yet to be explored, 
several candidate genes have been demonstrated to play a central role in enhanced alcohol tolerance. 
Engineered E. coli strains adapted to high butanol levels, for instance, have been shown to accumulate 
mutations in secB, encoding a protein involved in protein export, folding, and the general stress response 
(Xu et al. 2019). SecB maintains newly synthesized secretory pre-proteins in their unfolded, translocation-
competent state, and delivers them to the membrane-embedded Sec translocon. SecB also functions as 
a general chaperone, assisting in the folding of cytosolic proteins. Other proteins, either enzymes or 
regulators, have also been associated with tolerance against alcohols and similar stressor molecules. 
Taken together, the results in this section underscore the value of the upgraded Chi.Bio system for T -
ALE experiments. 
 
Multi-omic sampling using the upgraded Chi.Bio platform 
The examples above demonstrated that, with appropriate modifications, the Chi.Bio reactors can be 
utilized for various applications such as GRO-ALE and T-ALE, as well as for prolonged cultivation under 
tightly controlled environmental conditions. Next, we investigated whether the upgraded system could 
also be employed to explore microbial physiology and metabolism through multi -omic analysis. Multi -
omic data has become a cornerstone for studying and rationally engineering microbial metabolism. Due 
to the re latively limited accessibility of chemostats for exploring cell physiology and metabolism under 
constant growth rates, most laboratories rely on simpler batch cultivations using shaken flasks or 

 
42 
 
microtiter plates. Despite their simplicity, such cultivation setups have drawbacks, including cultures not 
reaching metabolic steady -state and, in the case of slow -growing strains, impractical sampling without 
an online growth readout. The Chi.Bio system represents an affordable and accessible platform for 
performing reproducible, continuous cultivation and convenient sampling. 
 
To facilitate the sampling process, we further modified the Chi.Bio lids to include a sampling port ( Fig. 
S1) that could enable fast withdrawal of aliquots from the culture using a common laboratory syringe. To 
test if samples obtained from the Chi.Bio system could be used to capture reproducible and meaningful 
metabolic states, we cultivated P. putida KT2440 and E. coli MG1655 in de Bont and M9 minimal media 
with glucose in both batch and turbidostatic cultivations. We sampled the moment the reactors reach ed 
OD600 of 1.0 – 1.2 for P. putida and E. coli as an approximate for exponential phase (T0; Fig. 6A and 6B, 
respectively), whereupon we began holding the culture in a dynamic steady-state using the Chi.Bio ‘hold 
OD’ function. During the batch phase, P. putida grew with a growth rate µ = 0.788 ± 0.03 h-1 and lag time 
= 0.88 ± 0.03 h whereas E. coli grew with a µ = 0.367 ± 0.04 h-1 and lag time = 1.91 ± 0.24 h. The OD600 
was held by the automated dilution, rendering the reactors turbidostatic by oscillating the reac tor OD600 
across a narrow range (<0.05 OD600) of the target OD600 and we sampled again 1 h (T1) after initiating 
the ‘hold OD’ function (Fig. 6A and 6B). Targeted metabolomics samples were processed by separating 
supernatant from biomass via vacuum filtration and biomass disrupted with quenching solution whereas 
proteomics samples were prepared by collecting a biomass and processed with our partners at the DTU 
Bioengineering department.  
 
High ATP to ADP/AMP ratios is a hallmark of growing cells (Rados et al. 2022). Concentrations of ATP, 
ADP and AMP were measured in samples from T0 and T1 using targeted metabolomics to confirm that 
strains are in fact growing in batch and turbidostatic conditions. When quantified, we found 120.75 ± 15.3 
µM ATP, 8.5 ± 1.6 µM ADP, 6.9 µM ± 1.4 µM AMP for P. putida at T0 and 109.2 ± 11.5 µM ATP, 6.4 ± 
1.3 µM ADP, 6.8 ± 2.5 µM AMP at T1; we also found 120.3 ± 15.6 µM ATP, 8.0 ± 0.33 µM ADP, 7.4 
µM ± 1.0 µM AMP for E. coli at T0 and 143.0 ± 13.1 µM ATP, 10.2 ± 0.36 µM ADP, 11.2 ± 0.53 µM 
AMP at T1 ( Table S12. ) under our sampling conditions. While ATP, ADP and AMP absolute 
concentrations may vary slightly between samples, high energy -charge ratios (ECR > 0.85 in all 
conditions, Fig. 6C) indicate strains are growing and sampling procedures did not lead to excessive ATP 
degradation within the cell, a typical challenge in metabolomics setups (Rados et al. 2022). Here we 
report ATP:ADP ratios between 12.2-19.0:1 among all sampling conditions (Table S12.). 
 

 
43 
 
Proteome changes are indicative of cell -wide adaptations to their environment. To assess proteome 
modulations, and consequently confirm if strains are in a static metabolic state, proteomes of P. putida 
and E. coli were compared at T0 and T1. Proteomes at T0 and T1 showed little to no differences between 
batch and turbidostatic growth modes with only a handful of proteins differentially expressed between 
conditions in P. putida and E. coli (Fig. 7D and 7E, respectively). Only 40 of the 2,143 identified proteins 
were differentially produced between T0 and T1 for P. putida, 25 of which were downregulated whereas 
15 were upregulated. In E. coli, 8 of 1,824 identified proteins were differentially expressed between T0 
and T1, all downregulated. 
 
In P. putida , downregulated genes were involved in glycogen synthesis (PP_4050), amino acid 
degradation (PP_3446 and PP_1412), ion transport (PP_0118) and polysaccharide transport (PP_3126) 
whereas upregulated genes were involved in amino acid synthesis (PP_3788) and organic cyclic 
compound catabolism (PP_3713 and PP_3166). In E. coli, downregulated genes were involved in valine 
and isoleucine biosynthesis (b4488), glucan biosynthesis and transport (b3538 and b0679), fatty acid 
degradation (b0221) and stres s (b1375). A full list of differentially expressed proteins can be found in 
Tables S8-11. and Fig S5-6. of the supplementary information. 
 
During exponential growth, enzymes involved in aerobic respiration and DNA, RNA and protein synthesis 
are all upregulated while during stationary phase, genes involved in protein degradation, stress response 
and synthesis of secondary metabolites (e.g. ant ibiotics) are upregulated whereas genes involved in 
protein synthesis and aerobic fermentation are downregulated (Llorens et al. 2010). While no major, 
proteome wide change were observed between T0 and T1, P. putida downregulated genes involved in 
amino ac id degradation and polysaccharide transport likely due to the lack of amino acids and 
polysaccharides in the rector media. Upregulation of amino acid synthesis enzymes is likely to meet the 
amino acid demand of exponentially growing cells. In E. coli, downregulation of glucan biosynthesis and 
fatty acid degradation is unsurprising due to the overabundance of glucose in the media. Hexose 
synthesis would be detrimental in a glucose -rich environment as valuable hexose precursors would be 
bled to contribute to a hexose rich environment and acetyl-CoA produced from fatty acid degradation can 
be supplied readily from glycolysis. Puzzling, glucan transport downregulation seems to be counter -
intuitive under these reactor conditions but, b3538 and b0769 are involved in cellulose modification and 
glucosamine transport and not glucose synthesis or transport (Anderson et al. 2020 and Postma et al. 
1993). 
 

 
44 
 
Overall, the modifications to the Chi.Bio lid and the setup for turbidostatic cultivation enabled effective 
and rapid sampling of microbial cultures grown under different modes. Importantly, cultures exhibited little 
to no differences at the metabolomic and proteomic levels when cultivated in either batch or turbidostatic 
modes. While these results indicate that the protocols established herein can be effectively used to carry 
out multi -omic analysis of microbial cultures, expanding the timeframe and sampli ng points in future 
experiments will be crucial to determining the precise moment where proteome and total metabolome 
stability occurs. 
 
  

 
45 
 
CONCLUSION 
 
The DBTL cycle lies at the core of the development of cell factories, with ALE and multi -omic analysis 
characterization as components with both the test and learn phases (Opgenorth et al. 2019). However, 
methods to perform these studies remain inconvenient  or incongruent with the standard workday and 
week. To address this, miniaturized bioreactors capable of functioning as turbidostats emerge as 
convenient tools to automate ALE and maintain cells in a steady-state metabolic condition. We aimed at 
expanding the capabilities of the commercially available Chi.Bio system (Steele et al. 2020) to cultivate 
and adapt biotechnologically -relevant bacteria, while serving as a versatile platform for multi -omic 
characterization. In our goal to demonstrate the relevance of this system, we chose to characterize both 
wild-type and engineered C. necator , P. putida , and E. coli , highly relevant biotechnological hosts 
(Theisen and Liao, 2016 and Weimer et al. 2020).  
 
When cultivated in LB and minimal media, both P. putida and E. coli exhibited growth rates consistent 
with those reported in the literature. To test whether the delivery of an enriched CO 2 environment within 
a Chi.Bio reactor was feasible, we designed modified Chi.Bio reactor lids with an outlet spout capable of 
dipping below the medium during prolonged cultivation. When CO 2 was sparged through this outlet, we 
found that the engineered P. putida strain rG1 was able to grow under formatotrophic conditions, whereas 
C. necator exhibited increased growth rates and optical density than previously reported. These results 
position the Chi.Bio system as a suitable cultivation platform for all three bacterial species. 
 
Next, we wanted to test the ability of the Chi.Bio system to serve as an automated ALE and TALE 
platform. To achieve this, we chose three different ALE modes: optimizing the growth rate of P. putida 
SEM10 on ribose as the sole carbon source, optimizing the growth rate of P. putida rG1 with formate as 
carbon source and CO2 sparging, and increasing the butanol tolerance of E. coli. In all cases, we found 
isolates that adapted to poor carbon and energy sources or exhibited increased tolerance towards toxic 
compounds. We conclude that, with minor modifications to the Chi.Bio codebase and custom reactor lids, 
this reactor system can be an effective tool for GRO-ALE and T-ALE. 
 
Finally, to demonstrate the ability of the Chi.Bio system to maintain cells in a stable metabolic static state, 
we cultivated and sampled P. putida and E. coli in minimal medium while holding the reactor OD 600 
constant in a turbidostatic mode. We observed little variations in the energy charge in our samples, 
suggesting growing cultures and the sampling procedure was fast enough to prevent ATP degradation in 

 
46 
 
the samples. Very little variations in the protein abundance could be detected between T0 and T1. For 
multi-omics sampling, the Chi.Bio system appears to be an effective, low -cost tool when implemented 
with our custom lids. 
 
With only a handful of modifications to the out -of-the-box Chi.Bio system, we were able to cultivate 
relevant biotechnological bacteria, deliver an enriched CO 2 environment within a reactor, achieve two 
variations of ALE, and demonstrate the capacity for multi-omics characterization. As suggested by Steele 
et al. 2020, the range of applications for this system is sparsely investigated. It is our hope that the results 
provided here will lay the foundation for laboratories, regardless of size, to jump -start t heir efforts to 
develop new cell factories. 
  

 
47 
 
MATERIALS AND METHODS 
 
Reagents and media. All the chemicals used in this study were purchased from Sigma-Aldrich Co. (St. 
Louis, Missouri, USA) unless otherwise noted. Lysogeny broth (LB) was composed of 5 g/L NaCl, 10 g/L 
tryptone and 5 g/L yeast extract; LB plates further contained 15 g/L agar. Two minimal media were used 
in this study, de Bont and M9 minimal media. In particular, de Bont minimal medium was composed of 
3.88 g/L K2HPO4, 1.63 g/L NaH2PO4, 2 g/L (NH4)2SO4, 10 mg/L ethylenediaminetetraacetic acid (EDTA), 
100 mg/L MgCl2·6H2O, 2 mg/L ZnSO4, 1 mg/L CaCl 2·2H2O, 5 mg/L FeSO 4, 0.2 mg/L Na 2MoO4·2H2O, 
0.2 mg/L CuSO 4·5H2O, 0.4 mg/L CoCl 2·6H2O and 1 mg/L MnCl 2·2H2O. M9 minimal medium contained 
6.8 g/L Na2HPO4, 3 g/L KH2PO4, 0.5 g/L NaCl, 1 g/L NH4Cl, 50 mg/L EDTA, 8.3 mg/L FeCl3·6H2O, 0.84 
mg/L ZnCl2, 0.19 mg/L CuSO 4·5H2O, 0.1 mg/L CoCl 2·6H2O, 0.1 mg/L H 3BO3, 0.016 mg/L MnCl 2·4H2O, 
240 mg/L MgSO 4 and 12 mg/L CaCl 2. Carbon sources were added separately whenever needed as 
described in the text. Kanamycin and gentamicin were added to the culture media at 50 mg/L and 10 
mg/L, respectively, whenever relevant. 
 
Bacterial strains, plasmids and oligonucleotides.  A full list of bacterial strains used in this study are 
listed in Tables 1. The pSNW2 ΔpykA (variant of the pSNW2 plasmid)  and pQure-6-strong (Volke et al. 
2020) were used to delete the pykA gene (PP_1362) in Pseudomonas putida SEM10. The pET28a 
plasmid (Rosenberg et al . 1987) was used to confer kanamycin resistance. Oligonucleotides were 
purchased from Integrated DNA technologies (Coralville, IA, USA). Genomic DNA extractions were 
performed using a DNeasy blood and tissue DNA extraction kit, plasmid extractions performed with a 
NucleoSpin® Plasmid kit (Macherny -Nagel, Düren, Germany ) and gel extractions performed with a 
NucleoSpin® Gel and PCR Clean -up kit (Macherny -Nagel, Düren, Germany ). Oligonucleotides were 
designed using the primer wizard function on Benchling (San Francisco, CA, USA) and uracil-containing 
primers designed with the AMUSER web-tool (Genee et al. 2015). 
 
Plasmid construction and homologous recombination -mediated genome engineering of 
Pseudomonas putida. Plasmids were constructed using USER cloning (Nour-Eldin et al. 2006). In brief, 
oligonucleotids containing deoxy uracil were designed to amplify two fragments ~500 base pairs (bp) up 
and downstream of a gene of interest. The two fragments were assembled via a USER reaction into the 
pSNW2 plasmid and cloned into E. coli DH5a. Plasmid sequence were confirmed via Sanger sequencing 
at EuroFins Genomic (Ebersber g, Germany). In order to delete genes in Pseudomonas putida , the 
protocol outlined by Wirth et al. [2] was employed. In brief, 100 -500 ng of pSNW2 vector designed to 

 
48 
 
delete a target gene was transformed into the appropriate strain and plated on kanamycin-containing LB 
agar. Green fluorescent colonies were picked, inoculated in LB containing kanamycin. The following day, 
the dense culture was washed 2-3 times with 300 mM sucrose and transformed with pQure-6-Strong and 
directly inoculated in LB containing gentamicin and 5 mM 3-methylbenzoate. The following day, the dense 
culture was streaked on LB agar plates containing gentamicin. Red fluorescent colonies were screen with 
primers designed to confirm target gene deletion and the pQure plasmid cured via incubation in LB broth 
without antibiotics. 
 
Modeling and 3D printer materials. All 3D models developed in this study are depicted in Figures S1 -
2 and are available at https://www.thingiverse.com/garret721/designs. Models were developed via enhancing 
the Chi.Bio lids available at https://chi.bio/hardware/ with Blender ( https://www.blender.org/). Models were 
printed in a Form 3 (Formlabs, Somerville, MA, USA) 3D printer with high temp resin or BioMed clear 
resin (Formlabs, Somerville, MA, USA). 
 
Cultivation of P. putida , E. coli  and C. necator in Chi.Bio reactors.  A detailed description of the 
Chi.Bio system set-up is given in the supplementary material. In brief, Chi.Bio reactors were kept inside 
laminar flow hoods for the duration, media bottles were capped with DWK Life Science DURAN TM 
(Fischer Scientific, Waltham, MA, USA) HPLC screw caps. For the purposes of this study, 40 mL clear 
Fisher Scientific (Waltham, MA, USA) glass vials (Product code: 11593532) placed inside the Chi.Bio 
reactor jackets along with a 10 cm stir bar (Fisher Sci entific, Waltham, MA, USA, product number: 
11858922). Prior to an experiment, the inlet and outlet pumps were flushed with 70% v/v EtOH for 30 to 
60 seconds. Media was flushed through the inlet to purge any remaining EtOH. 
 
On the Chi.Bio system dashboard, reactors destined to cultivate Pseudomonas putida and Cupriavideus 
necator were set to 30°C and reactors destined to cultivate Escherichia coli  were set to 37°C. 
Pseudomonas putida was cultivated in de Bont media and Escherichia coli and Cupriavideus necator 
cultivated in M9 media. Unless otherwise note, spinning speed was set to 0.75-1.00. When required, CO2 
was mixed with air using a GmixTM gas mixer (HiTec Zang GmbH, Herzogenrath, Germany) and sparged 
into each reactor at  a rate of approximately 33 mL/min. Gas output was split with a homemade (Figure 
S3) flowmeter. 
 
Chi.Bio adaptive laboratory evolution of Pseudomonas putida SEM10 in the presence of ribose 
as sole carbon source and screening for growth adapted isolates.  Adaptation experiments were 
performed using a modified ‘dither’ function available on the Chi.Bio system. In brief, the script allowed 

 
49 
 
the collected optical density to reach a desired value above the target optical density before diluting to 
the same desired value below the target optical density; details given in the supplementary information. 
Growth rate optimization adaptations were performed for approximately 250 hours before termination.  
 
Following the end of the adaptation, samples were taken for -80°C storage via the sampling port and 
stored in 25% glycerol. To identify and characterized single isolates, samples taken from the end of 
adaptation experiments were streaked on de Bont solid media with 10 mM ribose as sole carbon source. 
Candidate colonies were pre-cultured in 5 - 10 mL of de Bont media with 10 mM ribose for approximately 
48 hours. Candidate cultures were inoculated to an OD 600 of 0.05 in 1 mL of de Bont media containing 
10 mM of Ribose and incubated for 96 hours at 30°C in Synergy H1 (BioTek, Winooski, VT, USA) plate 
reader with measurements taken every 15 minutes. Wells were overlayed with 1 mL of filter sterilized 
mineral oil to minimize evaporation. 
 
Chi.Bio adaptive laboratory evolution of Pseudomonas putida rG1 in 10% v/v CO 2 and 
characterization of adapted isolates.  Pseudomonas putida rG1 was routinely cultivated in de Bont 
media with 20 mM glucose or acetate and 80 mM sodium formate in 10% CO 2 atmosphere. For the 
purpose of screening adapted isolates, Pseudomonas putida rG1 isolates were assayed in 20 mM sodium 
acetate and 80 mM sodium formate in a Synergy H1 (BioTek, Winooski, VT, USA) plate reader equipped 
with a CO2/O2 Gas regulator (BioTek, Winooski, VT, USA) set to 10% CO2. Wells were filled with 150 µL 
of media and overlayed with 50 µL of mineral oil. Isolates were inoculated to a starting OD600 of 0.05 and 
readings were taken every 10 minutes. 
 
Chi.Bio adaptive laboratory evolution of Escherichia coli MG1665 in increasing concentrations of 
butanol and screening of butanol adapted strains. All Escherichia coli cultivations were performed in 
M9 media with 2% w/v glucose. Escherichia coli adaptation was performed in M9 media with 2% w/v 
glucose and challenged with the same media supplemented with 3% v/v butanol. Adaptation was 
performed continuously for approximately 150 hours utilizing a custom function incorporated into the 
Chi.Bio code. When this function is engaged, when a target OD value is reached the culture is diluted by 
30% in the starting media and allowed to grow back to the target OD. When the target OD has been 
reached 10 times, the dilution is performed in 95 % starting media and 5 % stress media. Following 10 
dilutions in this media, dilution is then performed in 90 % starting media and 10 % stress media. This 
process continues until the experiment is ended or the dilution has progressed to be in 100 % stress 
media. The function is fully provided in the supplementary methods and the updated Chi.Bio code can 
be found at https://github.com/ljm176/Chi.Bio. 

 
50 
 
 
Growth under this program was continued for 150 hours in two reactors running in parallel, resulting in a 
final butanol concentration in the culture media of 1.2 %. Colonies were isolated from these evolved 
strains and growth was evaluated in M9 supplemented with 1.2 % butanol using the Growth Profiler 960 
(Enzyscreen, NL, Heemstede), which uses camera -based measurements to estimate growth rates. 
Methodology was essentially the same as that described in Radi et al. [3]. Briefly, CR1496c Enzyscreen 
polystyrene plates (Heemstede, Netherlands) were loaded with 297 µL of the appropriate M9 media with 
butanol combination and inoculated with 3 µL of pre -culture of the isolated strain. The Growth Profiler 
960 was set to 37 °C with 225 rpm shaking, the recommended settings for Escherichia coli, with pictures 
taken every 20 minutes. G -values were obtained from the plate images using the manufacturer’s 
software. G-values were converted to OD600 values using the formula: 
 
OD600=a∗(Gvalue−GBlank)b 
 
With the predetermined values  a = 0.0158 and  b = 0.9854, which were found by measurement of a 
standard curve in accordance with the instructions of the manufacturer. 
 
QurvE and QurvE_X utilization for growth rate estimation during growth rate enhancement 
adaptive laboratory evolution.  Growth rate estimation was performed using the QurvE 
(https://github.com/NicWir/QurvE) and QurvE_X ( https://github.com/NicWir/QurvE-X) packages for plate 
reader and Chi.Bio data respectively [4]. Unless otherwise noted, default settings were used. For 
QurvE_X, one phase is described as two points in time between which growth rate was calculated. One 
phase effectively translates to the ‘batch-like’ growth rate of a single dilution. 
 
Multi-omics sampling and processing of P. putida and E. coli in Chi.Bio reactors. In order to use 
the Chi.Bio system as multi -omics sampling platform, the same conditions were used to prepare the 
reactors for a routine cultivation. Specifically, cultures destined for a multi -omics study were cultured in 
the same media used for the study. Reactors were inoculated at a starting OD 600 of ~0.05 and grown to 
an OD600 ~1.0 after which the reactor was set to ‘hold OD’ on the dashboard. Sampling was performed 
using the sampling port (Figure 1B.) and a 10 cm needle and syringe. Samples were taken at hour zero 
(T0), the moment the ’hold OD’ function was enabled, and one hour after the ‘hold OD’ function was 
enabled (T1).  
 

 
51 
 
For metabolomics, 800 µL of culture was filtered on a 0.22 µm cellulose acetate filter. The filter was 
quickly placed in 2 mL of 40% methanol, 40% acetonitrile and 20% water quenching solution and 
incubated at -80°C for at least 30 minutes. The supernatant was then transferred to an Eppendorf vial 
and centrifuged at 4°C for 30 minutes at 13000 rpm. Supernatants were then transferred to HPLC vials 
and stored at –80°C until analyzed. Samples were analyzed as previously described (Donati et al. 2023).   
 
For proteomics, 800 µL of culture were centrifuged at 13000 rpm for 2 minutes at 4 °C, the supernatant 
discarded, and the pellet stored at -20°C until ready for analysis. Proteomics samples were processed 
and analyzed at the Denmark Technical University department of Bioengineering proteomics facility as 
described elsewhere [6].  
 
Genome sequencing  and single nucleotide polymorphisms and variation characterization of 
adapted strains. Adapted strains in this study contained a number of single nucleotide polymorphisms 
(SNPs) and varitations such as insertions, deletions and duplications. In order to identify SNPs and 
variations in adapted strains, candidate strains were cultured, and th eir genomic DNA extracted using a 
DNeasy Blood & Tissue kit (Qiagen, Hilden Germany) following the protocol for bacterial genomic DNA 
purification. Puri fied genomic DNA products was sent to NovoGene Europe (Cambridge, United 
Kingdom). Analysis of sequencing results were completed using the Geneious Prime software 
(https://www.geneious.com) and SNPs and variations identified following the protocol outlined on 
https://www.geneious.com/tutorials/map-to-reference/. SNPs and variations unique to the adapted strains and 
above 50% in frequency were considered for further investigation. 
  

 
52 
 
Table 1. Strains used in this study 
Strain name Description Source 
Pseudomonas putida KT2440 Wild-type strain Bagdasarian et al . 
1981 
Pseudomonas putida SEM10 Genome reduced variant of Pseudomonas 
putida KT2440 
Volke et al. 2020 
Pseudomonas putida ΔpykA Variant of Pseudomonas putida KT2440 
carrying deletion of pykA (PP_1362) 
This Study 
Pseudomonas putida RA2 Adapted isolate of Pseudomonas SEM10 This Study 
Pseudomonas putida RA3 Adapted isolate of Pseudomonas SEM10 This study 
Pseudomonas putida RA6 Adapted isolate of Pseudomonas SEM10 This study 
Pseudomonas putida rG1 ΔthiO Engineered formatotrophic strain of 
Pseudomonas putida EM42 
Turlin et al. 2022 
Pseudomonas putida rG1-E1 Adapted isolates of Pseudomonas putida 
rG1 ΔthiO 
This study 
Pseudomonas putida rG1-E2 Adaptred isolates of Pseudomonas putida 
rG1 ΔthiO 
This study 
Escherichia coli MG1655 Wild-type strain Blattner et al. 1997 
Escherichia coli DH5α λpir Cloning host, DH5 α variant with λpir 
lysogen  
Platt et al. 200 
Cupriavidus necator Wild-type strain Little et al. 2019 
 
  

 
53 
 
REFERENCES 
 
Amer, B., & Baidoo, E. E. K. (2021). Omics -Driven Biotechnology for Industrial Applications. 
Frontiers in Bioengineering and Biotechnology, 9, 613307.  
Anderson, A. C., Burnett, A. J. N., Hiscock, L., Maly, K. E., & Weadge, J. T. (2020). The 
Escherichia coli cellulose synthase subunit G (BcsG) is a Zn2+ -dependent phosphoethanolamine 
transferase. Journal of Biological Chemistry, 295(18), 6225–6235. 
Baev, M. V., Baev, D., Radek, A. J., & Campbell, J. W. (2006a). Growth of Escherichia coli 
MG1655 on LB medium: Determining metabolic strategy with transcriptional microarrays. Applied 
Microbiology and Biotechnology, 71(3), 323–328.  
Baev, M. V., Baev, D., Radek, A. J., & Campbell, J. W. (2006b). Growth of Escherichia coli 
MG1655 on LB medium: Monitoring utilization of sugars, alcohols, and organic acids with transcriptional 
microarrays. Applied Microbiology and Biotechnology, 71(3), 310–316.  
Bagdasarian, M., Lurz, R., Rückert, B., Franklin, F. C. H., Bagdasarian, M. M., Frey, J., & Timmis, 
K. N. (1981). Specific -purpose plasmid cloning vectors II. Broad host range, high copy number, RSF 
1010-derived vectors, and a host-vector system for gene cloning in Pseudomonas. Gene, 16(1–3), 237–
247.  
Bertaux, F., Sosa -Carrillo, S., Gross, V., Fraisse, A., Aditya, C., Furstenheim, M., & Batt, G. 
(2022). Enhancing bioreactor arrays for automated measurements and reactive control with ReacSight. 
Nature Communications, 13(1), 3363. 
Blattner, F. R., Iii, G. P., Bloch, C. A., Perna, N. T., Burland, V., Riley, M., Collado -Vides, J., 
Glasner, J. D., Rode, C. K., Mayhew, G. F., Gregor, J., Davis, N. W., Kirkpatrick, H. A., Goeden, M. A., 
Rose, D. J., Mau, B., & Shao, Y. (1997). The Complete Genome Sequence of Escherichia coli K-12. 277. 
Brune, M., Schumann, R., & Wittinghofer, F. ( 1985). Cloning and sequencing of the adenylate 
kinase gene (adk) of Escherchia coil. Nucleic Acids Research. 
Chen, J. X., Lim, B., Steel, H., Song, Y., Ji, M., & Huang, W. E. (2021). Redesign of ultrasensitive 
and robust RecA gene circuit to sense DNA damage. Microbial Biotechnology, 14(6), 2481–2496.  
Donati, S., Mattanovich, M., Hjort, P., Jacobsen, S. A. B., Blomquist, S. D., Mangaard, D., Gurdo, 
N., Pastor, F. P., Maury, J., Hanke, R., Herrgård, M. J., Wulff, T., Jakočiūnas, T., Nielsen, L. K., & 
McCloskey, D. (2023). An automated workflow for multi -omics screening of microbial model organisms. 
Npj Systems Biology and Applications, 9(1), 14.  
Elmore, J. R., Dexter, G. N., Salvachúa, D., O’Brien, M., Klingeman, D. M., Gorday, K., Michener, 
J. K., Peterson, D. J., Beckham, G. T., & Guss, A. M. (2020). Engineered Pseudomonas putida 

 
54 
 
simultaneously catabolizes five major components of corn stover lignocellulose: Glucose, xylose, 
arabinose, p-coumaric acid, and acetic acid. Metabolic Engineering, 62, 62–71. 
Emmerling, M., Dauner, M., Ponti, A., Fiaux, J., Hochuli, M., Szyperski, T., Wüthrich, K., Bailey, 
J. E., & Sauer, U. (2002). Metabolic Flux Responses to Pyruvate Kinase Knockout in Escherichia coli. 
Journal of Bacteriology, 184(1), 152–164. 
Espeso, D. R., Dvořák, P., Aparicio, T., & Lorenzo, V. (2021). An automated DIY framework for 
experimental evolution of Pseudomonas putida. Microbial Biotechnology, 14(6), 2679–2685.  
Fisher, M. A., Boyarskiy, S., Yamada, M. R., Kong, N., Bauer, S., & Tullman -Ercek, D. (2014). 
Enhancing Tolerance to Short-Chain Alcohols by Engineering the Escherichia coli AcrB E ﬄux Pump to 
Secrete the Non-native Substrate n-Butanol. ACS Synthetic Biology. 
Genee, H. J., Bonde, M. T., Bagger, F. O., Jespersen, J. B., Sommer, M. O. A., Wernersson, R., 
& Olsen, L. R. (2015). Software-Supported USER Cloning Strategies for Site-Directed Mutagenesis and 
DNA Assembly. ACS Synthetic Biology, 4(3), 342–349.  
Grunwald, S., Mottet, A., Grousseau, E., Plassmeier, J. K., Popović, M. K., Uribelarrea, J. -L., 
Gorret, N., Guillouet, S. E., & Sinskey, A. (2015). Kinetic and stoichiometric characterization of 
organoautotrophic growth of R alstonia eutropha on formic acid in fed -batch and continuous cultures: 
Organoautotrophic growth of Ralstonia eutropha. Microbial Biotechnology, 8(1), 155–163.  
Heins, Z. J., Mancuso, C. P., Kiriakov, S., Wong, B. G., Bashor, C. J., & Khalil, A. S. (2019). 
Designing Automated, High-throughput, Continuous Cell Growth Experiments Using eVOLVER. Journal 
of Visualized Experiments, 147, 59652.  
Hoffmann, S. A., Wohltat, C., Müller, K. M., & Arndt, K. M. (2017). A user -friendly, low -cost 
turbidostat with versatile growth rate estimation based on an extended Kalman filter. PLOS ONE, 12(7), 
e0181923.  
Jahn, M., Crang, N., Janasch, M., Hober, A., Forsström, B., Kimler, K., Mattausch, A., Chen, Q., 
Asplund-Samuelsson, J., & Hudson, E. P. (2021). Protein allocation and utilization in the versatile 
chemolithoautotroph Cupriavidus necator. eLife, 10, e69019. 
Joshi, S. H. -N., Yong, C., & Gyorgy, A. (2022). Inducible plasmid copy number control for 
synthetic biology in commonly used E. coli strains. Nature Communications, 13(1), 6691. 
La Rosa, R., Behrends, V., Williams, H. D., Bundy, J. G., & Rojo, F. (2016). Influence of the Crc 
regulator on the hierarchical use of carbon sources from a complete medium in P seudomonas: Crc and 
the hierarchy of substrate consumption. Environmental Microbiology, 18(3), 807–818. 
Lim, H. G., Eng, T., Banerjee, D., Alarcon, G., Lau, A. K., Park, M.-R., Simmons, B. A., Palsson, 
B. O., Singer, S. W., Mukhopadhyay, A., & Feist, A. M. (2021). Generation of Pseudomonas putida  

 
55 
 
KT2440 Strains with Efficient Utilization of Xylose and Galactose via Adaptive Laboratory Evolution. ACS 
Sustainable Chemistry & Engineering, 9(34), 11512–11523. 
Little, G. T., Ehsaan, M., Arenas -López, C., Jawed, K., Winzer, K., Kovacs, K., & Minton, N. P. 
(2019). Complete Genome Sequence of Cupriavidus necator H16 (DSM 428). Microbiology Resource 
Announcements, 8(37), e00814-19. 
Losen, M., Frolich, B., Pohl, M., & Buchs, J. (2004). Effect of Oxygen Limitation and Medium 
Composition on Escherichia coli Fermentation in Shake -Flask Cultures. Biotechnology Progress, 20(4), 
1062–1068.  
Matsuoka, Y., & Shimizu, K. (2012). IMPORTANCE OF UNDERSTANDING THE MAIN 
METABOLIC REGULATION IN RESPONSE TO THE SPECIFIC PATHWAY MUTATION FOR 
METABOLIC ENGINEERING OF ESCHERICHIA COLI. Computational and Structural Biotechnology 
Journal, 3(4), e201210018. 
Meza, E., Becker, J., Bolivar, F., Gosset, G., & Wittmann, C. (2012). Consequences of 
phosphoenolpyruvate:sugar phosphotranferase system and pyruvate kinase isozymes inactivation in 
central carbon metabolism flux distribution in Escherichia coli. Microbial Cell Factories, 11(1), 127.  
Mort, J. S., & Sanwal, B. D. (1978). The control of pyruvate kinases of Escherichia coli: Further 
studies of the enzyme activated by ribose -5-phosphate. Canadian Journal of Biochemistry, 56(6), 647–
653.  
Navarro Llorens, J. M., Tormo, A., & Martínez -García, E. (2010). Stationary phase in gram -
negative bacteria. FEMS Microbiology Reviews, 34(4), 476–495.  
Nour-Eldin, H. H., Hansen, B. G., Nørholm, M. H. H., Jensen, J. K., & Halkier, B. A. (2006). 
Advancing uracil-excision based cloning towards an ideal technique for cloning PCR fragments. Nucleic 
Acids Research, 34(18), e122–e122.  
Opgenorth, P., Costello, Z., Okada, T., Goyal, G., Chen, Y., Gin, J., Benites, V., De Raad, M., 
Northen, T. R., Deng, K., Deutsch, S., Baidoo, E. E. K., Petzold, C. J., Hillson, N. J., Garcia Martin, H., & 
Beller, H. R. (2019). Lessons from Two Design –Build–Test–Learn Cycles of Dodecanol Production in 
Escherichia coli Aided by Machine Learning. ACS Synthetic Biology, 8(6), 1337–1351.  
Pedersen, B. H., Gurdo, N., Johansen, H. K., Molin, S., Nikel, P. I., & La Rosa, R. (2021). High‐
throughput dilution ‐based growth method enables time ‐resolved exo ‐metabolomics of Pseudomonas 
putida and Pseudomonas aeruginosa. Microbial Biotechnology, 14(5), 2214–2226. 
Pen, U. -Y., Nunn, C. J., & Goyal, S. (2021). An Automated Tabletop Continuous Culturing 
System with Multicolor Fluorescence Monitoring for Microbial Gene Expression and Long -Term 
Population Dynamics. ACS Synthetic Biology, 10(4), 766–777.  

 
56 
 
Platt, R., Drescher, C., Park, S. -K., & Phillips, G. J. (2000). Genetic System for Reversible 
Integration of DNA Constructs and lacZ Gene Fusions into the Escherichia coli Chromosome. Plasmid, 
43(1), 12–23.  
Ponce, E., Martínez, A., Bolívar, F., & Valle, F. (1998). Stimulation of glucose catabolism through 
the pentose pathway by the absence of the two pyruvate kinase isoenzymes inEscherichia coli. 
Biotechnology and Bioengineering, 58(2–3), 292–295. 
Postma, P. W., Lengeler, J. W., & Jacobson, G. R. (1993). Phosphoenolpyruvate:carbohydrate 
phosphotransferase systems of bacteria. Microbiological Reviews, 57(3), 543–594.  
Radi, M. S., Munro, L. J., Salcedo-Sora, J. E., Kim, S. H., Feist, A. M., & Kell, D. B. (2022). Understanding 
Functional Redundancy and Promiscuity of Multidrug Transporters in E. coli under Lipophilic Cation 
Stress. Membranes, 12(12), 1264. 
Radoš, D., Donati, S., Lempp, M., Rapp, J., & Link, H. (2022). Homeostasis of the biosynthetic 
E. coli metabolome. iScience, 25(7), 104503. 
Reitzer, L. (2005). Catabolism of Amino Acids and Related Compounds. EcoSal Plus , 1(2), 
ecosalplus.3.4.7.  
Rodionova, I. A., Zhang, Z., Mehla, J., Goodacre, N., Babu, M., Emili, A., Uetz, P., & Saier, M. 
H. (2017). The phosphocarrier protein HPr of the bacterial phosphotransferase system globally regulates 
energy metabolism by directly interacting with multiple enzymes in Escherichia coli. Journal of Biological 
Chemistry, 292(34), 14250–14257. 
Rosenberg, A. H., Lade, B. N., Dao -shan, C., Lin, S. -W., Dunn, J. J., & Studier, F. W. (1987). 
Vectors for selective expression of cloned DNAs by T7 RNA polymerase. Gene, 56(1), 125–135.  
Rugbjerg, P., Feist, A. M., & Sommer, M. O. A. (2018). Enhanced Metabolite Productivity of 
Escherichia coli Adapted to Glucose M9 Minimal Medium. Frontiers in Bioengineering and Biotechnology, 
6, 166.  
Sandberg, T. E., Salazar, M. J., Weng, L. L., Palsson, B. O., & Feist, A. M. (2019). The 
emergence of adaptive laboratory evolution as an efficient tool for biological discovery and industrial 
biotechnology. Metabolic Engineering, 56, 1–16. 
Saunders, A. H., & Booker, S. J. (2008). Regulation of the Activity of Escherichia coli Quinolinate 
Synthase by Reversible Disulfide-Bond Formation. Biochemistry, 47(33), 8467–8469.  
Sezonov, G., Joseleau-Petit, D., & D’Ari, R. (2007). Escherichia coli Physiology in Luria-Bertani 
Broth. Journal of Bacteriology, 189(23), 8746–8749.  
Smirnova, G. V., & Oktyabrsky, O. N. (n.d.). Relationship between Escherichia coli growth rate 
and bacterial susceptibility to ciprofloxacin. 

 
57 
 
Steel, H., Habgood, R., Kelly, C. L., & Papachristodoulou, A. (2020). In situ characterisation and 
manipulation of biological systems with Chi.Bio. PLOS Biology, 18(7), e3000794.  
Takahashi, C. N., Miller, A. W., Ekness, F., Dunham, M. J., & Klavins, E. (2015). A Low Cost, 
Customizable Turbidostat for Use in Synthetic Circuit Characterization. ACS Synthetic Biology, 4(1), 32–
38.  
Theisen, M., & Liao, J. C. (2016). Industrial Biotechnology: Escherichia coli as a Host. In C. 
Wittmann & J. C. Liao (Eds.), Industrial Biotechnology (pp. 149–181). Wiley-VCH Verlag GmbH & Co. 
KGaA.  
Volke, D. C., Friis, L., Wirth, N. T., Turlin, J., & Nikel, P. I. (2020). Synthetic control of plasmid 
replication enables target- and self-curing of vectors and expedites genome engineering of Pseudomonas 
putida. Metabolic Engineering Communications, 10, e00126. 
Volke, D. C., Olavarría, K., & Nikel, P. I. (2021). Cofactor Speciﬁcity of Glucose -6-Phosphate 
Dehydrogenase Isozymes in Pseudomonas putida Reveals a General Principle Underlying Glycolytic 
Strategies in Bacteria. 6(2). 
Wang, Y., Horlamus, F., Henkel, M., Kovacic, F., Schläfle, S., Hausmann, R., Wittgens, A., & 
Rosenau, F. (2019). Growth of engineered Pseudomonas putida  KT2440 on glucose, xylose, and 
arabinose: Hemicellulose hydrolysates and their major sugars as sustainable carbon sources. GCB 
Bioenergy, 11(1), 249–259.  
Waygood, E. B., Rayman, M. K., & Sanwal, B. D. (1975). The Control of Pyruvate Kinases of 
Escherichia coli. II. Effectors and Regulatory Properties of the Enzyme Activated by Ribose 5-Phosphate. 
Canadian Journal of Biochemistry, 53(4), 444–454. 
Weimer, A., Kohlstedt, M., Volke, D. C., Nikel, P. I., & Wittmann, C. (2020). Industrial 
biotechnology of Pseudomonas putida: Advances and prospects. Applied Microbiology and 
Biotechnology, 104(18), 7745–7766. 
Wirth, N. T., Kozaeva, E., & Nikel, P. I. (2020). Accelerated genome engineering of 
Pseudomonas putida  by I ‐ Sce I―mediated recombination and CRISPR ‐Cas9 counterselection. 
Microbial Biotechnology, 13(1), 233–249.  
Wong, B. G., Mancuso, C. P., Kiriakov, S., Bashor, C. J., & Khalil, A. S. (2018). Precise, 
automated control of conditions for high-throughput growth of yeast and bacteria with eVOLVER. Nature 
Biotechnology, 36(7), 614–623.  
Xu, G., Xiao, L., Wu, A., Han, R., & Ni, Y. (2021). Enhancing n-Butanol Tolerance of Escherichia 
coli by Overexpressing of Stress -Responsive Molecular Chaperones. Applied Biochemistry and 
Biotechnology, 193(1), 257–270. 
  

 
58 
 
   
 
 
 
 
 
 
 
Graphical Abstract 
 
 
 
 
 
 
 
 
 


 
59 
 
Figure 1. Agitation-dependent growth rate of Pseudomonas putida KT2440 and Escherichia coli MG1655 
in Chi.Bio reactors.  Agitation (0.0 – 1.0) refers to the percentage of the maximum rotation per minute 
(RPM) of the case fan integrated in the Chi.Bio system. The case fan with mounted magnets provided in 
the Chi.Bio system have a 4500 RPM maximum (Steel et al, 2020, supplementary). Growth rates were 
calculated with the QurvE default settings. Error bars represent standard deviation (n=3). 
 
 
 
 
 
 
 
 
 
 


 
60 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 2. Cultivation of Pseudomonas putida rG1 and Cupravidus necator in ambient and enriched CO2 
atmospheres. A-B, Metabolic maps of Pseudomonas putida rG1 and Curpriavideus Necator depicting 
the effects of CO 2 on cellular fitness and biomass output. C-D Quantitive physiological effects of CO 2 
sparging on Pseudomonas putida rG1 and Cupriavideus necator in the Chi.Bio system. Pseudomonas 
putida rG1 was cultivated in de Bont media with 20 mM sodium acetate, 80 mM sodium formate. 
Cupriavideus necator was cultivated in M9 media, 80 mM format. Artifacts in data acquisition were 
removed from the curves of Cupriavidus necator cultivated in enriched CO 2; raw data is given in the 
supplementary information. Student’s T -test was p erformed using Graphpad Prism; n.s. indicate no 
significance, one asterixis indicates p -values ≤ 0.05, two asterixis indicate p -values ≤ 0.01, three 
indicates p-values less than ≤ 0.001 and four indicate less than ≤ 0.0001. 
 


 
61 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 3.  Growth rate optimization adaptive laboratory evolution of Pseudomonas putida SEM10 on 
ribose. A, Metabolic map of ribose metabolism in the framework of central carbon metabolism as 
described by Volke et al 2021. Red gene names indicate genes which were disrupted or deleted in this 
study. B, Raw growth data obtained during the course of the ribose GRO -ALE experiment. C, Evolution 
of growth rate per phase as calculated by QurvE_X. D-E, Growth curves and corresponding growth rate 
of select adapted and un-adapted Pseudomonas putida SEM10. Lag time is reported within D and given 
in hours.  Growth rates were calculated with QurvE default settings. One way ANOVA analysis was 
performed using Graphpad Prism; n.s. indicates no significance, one asterixis indicates p-values ≤ 0.05, 
two asterixis indicate p-values ≤ 0.01, three indicates p -values less than ≤ 0.001 and four indicate less 
than ≤ 0.0001. 


 
62 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 4. Growth rate optimization adaptive laboratory evolution of Pseudomonas putida rG1 in enriched 
CO2 atmosphere. A, Metabolic map of formate assimilation in Pseudomonas putida rG1 as described by 
Turlin et al. 2022. Red enzyme names indicate enzymes deleted or inhibited and green gene names 
indicate genes affected by one or more SNP or variation potentially leading to enhanced growth rate on 
formate. B, Raw growth data obtained during adaptive laboratory evolution experiment. C, Evolution of 
growth rate per phase, as calculated by QurvE_X over the course of the ALE experiment. Growth rates 
were calculated with a sliding window of 1000 and phases with growth rates which could not be calculated 
were omitted. D-E, Growth curve and corresponding growth rates of select adapted and un -adapted 
Pseudomonas putida rG1 strains; growth rates calculated using QurvE default settings. Error bars 
represent standard deviation (n=3). One way ANOVA analysis was performed using Graphpad Prism; 


 
63 
 
n.s. indicates no significance, one asterixis indicates p -values ≤ 0.05, two asterixis indicate p -values ≤ 
0.01, three indicates p-values less than ≤ 0.001 and four indicate less than ≤ 0.0001. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
64 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 5.  Tolerance adaptive laboratory evolution of Escherichia coli  MG1655 to increasing 
concentrations of butanol. A, Predicted set vs real stressor concentration of the custom ALE function, 
one dilution is equivalent to one phase. B, Raw growth data obtained during the course of the Escherichia 
coli MG1655 T-ALE experiment with 3% v/v butanol as stressor media. Red bars indicate set butanol 
stressor concentrations. C, Evolution of growth rate per phase, as calculated by QurvE_X. Growth rates 
were calculated with default settings. Panel D-E, Growth curves and associated g rowth rates of select 


 
65 
 
adapted and un -adapted Escherichia coli MG1655 isolates challenged with M9 media with 2% w/v 
glucose and 1.2% butanol; n.s. indicate no significance. Growth rates calculations were performed with 
QurvE default settings with the exception that a sliding window of 30 was used to produce the data i n C 
and a sliding window of 20 for E. Error bars represent standard deviation (n=3). OD ChiBio represents a 
relative OD calculated by manually setting the starting OD, subsequent OD values were calculated by 
the Chi.Bio system (Steele et al. 2020). One way ANOVA analysis was performed using Graphpad Prism; 
n.s. indicates no significance, one asterixis indicates p -values ≤ 0.05, two asterixis indicate p -values ≤ 
0.01, three indicates p-values less than ≤ 0.001 and four indicate less than ≤ 0.0001. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
66 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 6. Multi-omics characterization of Pseudomonas putida KT2440 and Escherichia coli MG1655.  
A-B, Real time OD 600 of Pseudomonas putida and Escherichia coli  grown on de Bont and M9 
supplemented with glucose respectively. Red data points with arrows indicate sampling points for each 
cultivation. Growth rates were calculated with QurvE with the following restriction: ( A) consideration of 
timepoints between 2 and 5 h, sliding window of 15 and R 2 of 0.9, (B), consideration of timepoints after 
5 h, sliding window of 15 and R 2 of 0.9. C, Calculated energy charge ratio of Pseudomonas putida and 
Escherichia coli at time T0 and T1, error bars represent standard deviation (n=3). D-E, Volcano plots 
depicting proteomics profiles of Pseudomonas putida and Escherichia coli at T0 versus T1. Horizontal 
dashed lines represent the threshold for p -value significance and vertical dashed lines represent fold 
changes greater than 2. Red data points indicate proteins differentially produced by 2 -fold with p-values 
below 0.05. A full list of differentially produced enzymes are given in the supplementary material. 
  


 
67 
 
Chapter 3: Tuning the sulfonate consumption capacity of 
Pseudomonas putida for artificial overconsumption 
Garret William O’Connell1 and Pablo Ivan Nikel1 
Novo Nordisk Center for Biosustainability1 
Platform technologies exist as tools for scientists to systematically, and with user-defined input, explore a particular 
research question. In metabolic engineering, platform strains manifest as strains which delivery a particular 
metabolite or can utilize  a novel substrate. The alkanesulfonate degradation system ( ssu) is a promiscuous 
sulfonate import and degradation system and to fully realize the potential of this system in a resistant chassis like 
Pseudomonas putida , three selection strains were devised  to enhance the sulfonate uptake and degradation 
capacity of the ssu enzymes. In the first selection scheme, sulfate import and activation were inhibited leading to 
the formation of a sulfonate auxotroph. Next, sulfite oxidases and exporters were expressed to previously 
generated strains to reduce perceived levels of intra cellular sulfur, and, in a final schema, taurine -specific 
(tauABCD) importers were disrupted to establish a connection between sulfur and nitrogen metabolism. Each 
selection strain was adapted in three distinct adaptive laboratory evolution (ALE) procedures. Sulfate activation 
was successfully inactivated by disruption of cysDNC enzymes but following seven disruptions to putative sulfate 
transporters, total sulfate uptake could not be inhibited. Furthermore, expression of sulfite oxidases and exporters 
could not increase strain fitness when growth yield is used as estimate. Ethanolamine, however, could be used as 
a nitrogen source indicating that aminoacetaldehyde generate from taurine degradation could be used as nitrogen 
source. Every attempt to adapt engineered strains towards increased sulfonate consumption were met with 
challenges. Growth yield could not be used as an indicator for increased fitness and ethanesulfonate nor taurine 
quantification could clearly identify adapted strains. The major limitation or the methods employed to adapt P. 
putida towards increased sulfonate consumption is the effective operational range of sulfur metabolism. Requiring 
several orders of magnitude less tha n carbon or nitrogen metabolism, establishing an effective selection strain 
presents a massive challenge. Disrupting of aminoaceladehyde deamination could lead to selection strains with 
operational selection ranges within the reach of sulfur metabolism limits.   
  

 
68 
 
Introduction 
Renowned astronomer and physicist Sir Isaac Newton once wrote “If I see further, it’s because I sit on the shoulders 
of giants”. This quote signifies the great discoveries and progress made by him were made possible by the 
cumulative knowledge of his prede cessor. These leaps and bounds can be akin to platform technologies. Key 
examples of technologies which have served as runways for new advances include the Internet which arose in the 
late 1960s and gave rise to social media, shared data archives and all p opular digital content streaming (e.g. 
Netflix) and the polymerase chain reaction (PCR) developed by Kary Mullis in 1985 which revolutionized molecular 
biology and is one of the founding pillars of most of the methods in this chapter. 
The definition of a platform technology can vary from source to source, but, as per the Federal Food, Drug and 
Cosmetic act, a platform technology is a well understood and reproducible technology which serves as a base for 
or incorporated into a drug or biological product or facilitates the production or manufacturing of a drug or biological 
product (21 st Century Cures Act, Section 3060(a)). In essence, a platform technology can be identified as a 
technology which allows user-input modifications to be the driver of discovery. 
In Biotechnology, platform technologies are tools, vectors or strains which allow user -defined input to explore a 
particular scientific question, research line or area. For example, the pET system (Studier et al 1986) is used as a 
versatile plasmid vector used in protein biochemistry to drive production of user-encoded genes. N- and C- terminal 
tags can be encoded in the vector to produce chimeric proteins with enhance solubility (MBP, GST and SUMO 
tags; Duan et al. 2001 and Kapust and Waugh et al. 1999, Harper and Speicher et al. 2011 and Butt et al. 2005) 
or targeted purification (Hengen, 1995). The alkanesulfonate monooxygenase system (SsuDE) was purified with 
the pET system allowing researchers to characterize Bayer -Villiger mechanism of FMNH 2-dependent sulfolytic 
cleavage sulfite from sulfonates and protein-protein interaction between system subunits (Gao and Ellis, 2007 and 
Dayal et al. 2015). Other systems include the pSNW2/pQure system used for genetic engineering of Pseudomonas 
putida; with user-define construction of the pSNW2 vector, users can target homologous recombination for whole 
gene disruption, gene insertion or replacement (Volke et al. 2021 and 2022). Wirth et al. 2022 were successful in 
disrupting the numerous acetyl -CoA generating enzymes in P. putida using the pSNW2 generating an acetate 
auxotroph. In a similar vein, platform strains like the Standardized Genome Architecture (SEGA; Bayer et al. 2021) 
are the bread and butter of metabolic engineering. By standardizing genome engineering and genetic part, in E. 
coli Bayer et al. 2021 established a two-part methodology where user-defined DNA or genes can be targeted for 
replacement, disruption and genomic expression.  
Metabolic engineering can be divided into two core pillars: a metabolic pathway of interest and a background 
providing the machinery for said pathway. A problem -drive approach to metabolic engineering is identifying a 
pathway that produces one or more value added compounds and moulding a chassis for production through that 
pathway. An example of this is the enhancement of the chorismate node in E. coli for the production of value added 
salicylate (Noda et al. 2016). Chorismate is an important pre -cursor to several value-added products such as 
aspirin and lamivudine (Noda et al. 2016 and Hubrich et al. 2021). Biosynthesis of chorismate is the end product 

 
69 
 
of the shikimate pathway in bacteria and Noda et al. 2016 increased chorismate titers for salicylate biosynthesis 
by disrupting phosphoenol pyruvate consuming reactions in E. coli. 
While the chorismate node is a stepping stone to an open -ended exploration, researchers focused on enhancing 
a chassis with the end goal of the pathway in mind. Flipping the script on this paradigm presents an opportunity 
for open-ended discovery. Instead of focusing genetic engineering to establish a chassis for a particular pathway, 
engineering a particular pathway for to establish a novel chassis sets the foundation for systematic exploration of 
a particular metabolism and, at its core, is the founding principle of a platform strain. 
In this work, we chose to focus on the alkanesulfonate uptake and degradation system (ssu) due to it’s promiscuity 
(Eichhorn et al. 2000) and potential to deliver sulfonate degradation by-products. Sulfonates are diverse in structure 
and elemental composition (e.g. bromoethanesulfonate, trimethylsilipropanesulfonate and 6:2 fluorotelomer 
sulfonate) and can be delivered in a catch-and-release mechanism. To that end, we attempt to engineer P. putida 
to over-consume sulfonates through the generation of selection strains in an attempt to establish a platform strain 
capable of delivering sulfonate degradation by-products for systematic novel chemistry discovery. Pseudomonas 
putida was chosen as chassis due to its resilient nature (Martinez -Garcia and de Lorenzo, 2024) to chemical 
stressors, presence of ssu enzymes (Kertesz, 2000) and promiscuous nature of sulfonate utilization (Chapter 1). 
  

 
70 
 
Results & Discussion 
Goals & rational for enhancing sulfonate consumption in P. putida 
At the advent of the work performed in this chapter and that of Chapter 2, Pseudomonas putida was hypothesized 
to be a suitable host for the delivery of sulfonates with non-natural elements (e.g. silicone, fluorine or bromine) due 
to its involvement in PFAS degradation (Liu et al. 2007, Kim et al. 2012 and 2014) resistance to a wide range of 
chemical stressors (Martinez-Garcia and de Lorenzo, 2024 and Craig et al. 2021) and growing tool-box for genetic 
manipulation (Volke et al. 2020 and 2021). Sulfonates are an alternative, organic source of sulfur (Kertez, 2000) 
which can support metabolism in Gram -negative and -positive bacteria (Shaw et al. 2019, Bottos et al., 2020, 
Eichhorn et al.,1999), and, due to the promiscuous nature of sulfonate import (Eichhorn et al., 2000), sulfonates 
could be used as a catch and release delivery system for non-natural element containing sulfonates. 
It was further hypothesized that the total sulfur demand in P. putida is low in comparison to carbon, or nitrogen 
demand due to the limited, but crucial, involvement of sulfur in cellular metabolism (Takagi and Ohtsu 2016 and 
Bechtel and Weerapana 2017). To establish a platform strain capable of delivering sufficient non -natural 
metabolites, increasing sulfonate delivery is an essential first step. To that end, three selection schemas were 
developed to enhance sulfonate uptake: generation of a sulfonate auxotrophy, sulfur desensitization through sulfite 
oxidation and connection of sulfur to nitrogen demand. 
Generation of a sulfonate auxotroph P. putida and adaptation through carbon demand 
In E. coli , sulfonates are transported and degraded through the activity of two systems: the ssuEADCB and 
tauABCD systems (Eichhorn et al. 2000), P. putida harbors homologs of both (PP_0236 -0240, PP_0230-0233). 
Each system performs the active uptake of organic sulfonates and subsequent release sulfite (SO32-). Sulfite then 
enters sulfur metabolism through the assimilator sulfate reduction pathway (ASR; Leyh et al . 1988). Crucially, 
degradation of sulfonates releases sulfite, and a cognate aldehyde as by-product, allowing sulfur to by-pass initial 
sulfate reduction and CysDNC activity (Leyh et al. 1988; Fig 1., A). To render P. putida completely dependent on 
exogenous sulfonates when grown in minimal media, the first step of ASR (Fig 1., A; SO42- → SO32-) was inhibited 
via the disruption of cysDNC and additional deletion of all known and putative sulfate transports ( Fig 1., A). P. 
putida harbors the known active sulfate (SO 42-) transport system ( cysAWU, sbp-I/II; Sirko et al. 1995), sulfate 
transport system (cysZ; Zhang et al. 2014) and four putative sulfate transporters (PP_5168-5171 and _4305). 
Disruption of cysDNC has previously been demonstrated to inhibit growth on sulfate as a sole sulfur source in 
Chapter 2, however, disruption of all known and putative sulfate transporters in strain ST7 (see Table 2) did not 
lead to a sulfonate auxotrophy (Fig 2., B). When all known and putative sulfate transporters were disrupted, relative 
growth rates of P. putida KT2440 and ST7 were not statistically different from one another above 100 µM of sulfate 
(Fig 2., B; dashed line). Fortunately, disruption of these transporters did lead to a growth rate impact on sulfate 
concentrations below 100 µM with P. putida KT2440 having a relative growth rate of 0.681 - 0.685 h-1 between 27 
– 62 µM sulfate whereas ST7 had relative growth rates between 0.08 - 0.362 h-1 between 27 – 62 µM sulfate 

 
71 
 
concentrations. Reduced growth rates indicate that, while sulfate can still enter P. putida ST7, sulfate transport is 
partially impacted. 
To enhance the utilization of sulfonates, we combined disruption of sulfate transporters and activators to generate 
P. putida ST8 and adapted it in limiting carbon and excess sulfonate (Fig 1., C). When sulfonates are degraded to 
release sulfite, a cognate aldehyde is released (Eichhorn et al. 1999). Release of aldehyde by -product presents 
an opportunity to restrict carbon (e.g. acetate if the sulfonate is ethanesulfonate) and select for increased activity 
of sulfonate uptake and degradation by monitoring b iomass production. It is expected that cytoplasmic 
acetaldehydes, the aldehyde release from ethanesulfonate degradation, would be readily oxidized to the 
corresponding aldehyde and enter carbon metabolism ( Fig 1., A; Riveros -Rosas et al. 2019). To that end, ST8 
was serial passaged for 25 passages in 15 mM acetate and 15 mM ethanesulfonate (~1 month; Fig 1. , C). 
Ethanesulfonate was chosen as sulfur source to mirror carbon entry of acetate (ethanesulfonate → acetaldehyde 
→ acetyl-CoA) 
To streamline screening of potentially adapted stains, two growth assays were tested: microtiter and shake flask 
growth assays. In a perfect world, un-adapted strains would generate less biomass than adapted strains capable 
of over-consuming sulfonates whe n limiting carbon and excess sulfonate carbon is provided. To test this, two 
adapted strains (n1n16 and n3n14) and un -adapted ST8 were screened in microtiter plate with decreasing 
concentrations of acetate (7.5 – 40 mM), excess ethanesulfonate (15 mM) and growth yield estimated by 
absorbance at 600 nm (Fig 1., D). Immediately the results were suspicious. While certainly indicative of increased 
sulfonate consumption, and as a result increased intracellular acetaldehyde, growth yields of n1n16 and n3n14 
were higher than growth yields of ST8 at acetate concentrat ions of 11.5 – 40 mM. At 7.5 mM of acetate, growth 
yields of ST8 (Abs 600 = 0.343) were higher than that of n3n14 (Abs 600 = 0.180) but not n1n16 (Abs 600 = 0.427). If 
the excess ethanesulfonate were to have an impact on growth, it is expected that growth yields of ST8 would be 
affected across all acetate concentrations and, furthermore, increasing acetate concentrations should correlate 
with a linear increase in growth yield. Something not observed in this experiment. In an attempt to salvage growth 
yield as a measure of increased sulfonate consumption, growth yields were measured by shake flask assay. Here, 
n3n14 and ST8 were grown in 30 mM acetate and 15 mM ethanesulfonate (excess) and OD600 monitored for nine 
hours; ST8 performed marginally poorer than n3n14 with maximum OD600 0.731 and 0.793 respectively. 
Microtiter growth assays are a powerful tool when characterizing cell factories as they allow for testing multiple, 
combinatorial, conditions simultaneously. But these types of experiments are not without their drawback. Due to 
the reduced scale of the exp erimental conditions (e.g. lower volumes), microtiter growth assays are particularly 
vulnerable to micro-environmental changes, inoculation changes and oxygen transfer. In this work, the outer wells 
were deliberately left cell -free and filled with water to  mitigate the edge effect (Mansoury et al . 2021) and 
standardizing inoculation techniques proved effective in other chapters. While oxygenation could be a problem for 
P. putida due to its obligate aerobe status, microtiter growth assays were performed without lid and, further, P. 
putida has been characterized ad nauseam in microtiter plate readers (Turlin et al. 2020, Volke et al. 2020 and 

 
72 
 
Wirth et al. 2022). The only parameter which was not controlled throughout these experiments is colony age; aged 
or dying colonies used may have impacted the metabolic state of inoculum cultures leading to the odd and 
inconsistent results observed. Repeating the microtiter experiment with fresh colonies would shed light on the true 
nature of the observed results. 
While the root cause for the null observations requires further investigation, shake flask growth experiments painted 
a clear picture: no adaptation to increased sulfur consumption. Sulfur is an element needed in ‘homeopathic’ 
quantities, that is, very little. As demonstrated, P. putida KT2440 can grow to maximum growth rates with as little 
as 50 µM of sulfate. Likely a two- to ten-fold increase in sulfur concentrations would not been quantified in microtiter 
and shake flask growth assay due to the substant ially larger demand for carbon compared to sulfur. Instead, 
monitoring ethanesulfonate consumption may prove more accurate. 
De-sensitization of intracellular sulfite concentrations and concomitant enhanced sulfonate uptake 
In previous chapters we investigated the nature of assimilatory sulfate reduction (ASR) in P. putida. Briefly, we 
found that the ASR pathway in P. putida mirrored that of E. coli in the where sulfate is first ‘activated’ with ligation 
to adenosine via CysD generating adenosine phosphosulfate (APS), subsequent phosphorylation to 
phosphoadenosine phosphosulfate (PAPS) via CysNC and finally release of sulfite (SO32-) via CysH (Krone et al. 
1991). Ligation of sulfate to adenosine is irreversible and therefore, once the reaction takes place, the sulfur 
molecules is committed to the ASR pathway (Leyh et al. 1988 and Liu et al. 1994). 
While APS and PAPS are not directly measured in this or previous chapters nor in the literature, sulfate activation 
was demonstrated to proceed solely via the ASR pathways enzymes (CysDNCH) and therefor disruption of one of 
more of these enzymes would lead to the complete inhibition of growth on sulfate. To take advantage of this and 
increase sulfonate uptake and degradation, two sulfite oxidases and a sulfite exporter were heterologously 
expressed in ST8 strains. When sulfur enters in the form of sulfonate, the immediate by-product is SsuDE activity 
is sulfite and a cognate aldehyde (Eichhorn et al. 1999). In the ST8 strain, if sulfite release from a sulfonate is 
oxidized to sulfate, that molecule of sulfur will be unable to re -enter total sulfur metabolism requiring further 
sulfonate uptake and degradation (Fig 2., A). Furthermore, expression of a sulfite exporter (TauE) would effectively 
perform the same function by reducing the apparent sulfur concentration within the cytoplasm (Fig 2., A). 
Sulfite oxidation is a common reaction performed by sulfite oxidases in the mitochondria of eukaryotic cells and 
plays a crucial role in sulfur compound metabolism, a process if defective in humans can cause seizures and 
neurodevelopmental disorders in ear ly infants (Tan et al . 2005 and Cohen et al . 1972). Sulfite oxidases are 
characterized by their ability to catalyze the oxidation of sulfite to sulfate with molybdopterin and heme as co -
factors; the Arabadopsis thaliana SUOX (sulfite oxidase) has been extensively characterized (Eiler et al. 2001 and 
Schrader et al. 2003). While found in eukaryotic cells, sulfite oxidases have also been reported in bacteria such as 
the draSO gene from Deinococcus radiodurans (D’Errico et al. 2006) and sorA from Starkeya novella (Kapplet and 
Bailey, 2005). 

 
73 
 
To ensure sulfite oxidation activity, two sulfite oxidases were chosen for heterologous expression in ST8 strains: 
SUOX and SorA. It was expected that sulfite oxidases were to be soluble (and functional) when expressed in P. 
putida since characterization of eukaryotic and prokaryotic sulfite oxidases were performed by first expression from 
E. coli BL21 (Scrader et al. 2003, D’errico et al. 2006, Kapplet and Bailey, 2005 and Di Salle et al. 2006) and P. 
putida has the capacity to synthesize molybdopterin cofactor (Xia et al. 2018 and Turlin et al. 2023). Additionally, 
the sulfite exporter tauE expressed during taurine consumption under nitrogen limiting conditions by Cupriavidus 
necator H16 was also expressed (Weinitschke et al. 2007). 
Sulfite oxidase(s) and exporter were expressed in individual, constitutive operons in previously identified landing 
pad (Wirth et al 2020). Resulting strains were termed 351 for ST8 expressing SUOX and tauE and 352 for ST8 
expressing SorA and tauE. No adequate experiment could be devised to confirm the activity of TauE but, the sulfite 
oxidation could be characterized with whole -cell lysate assay. It was hypothesized that endougenous 
molybdopterin in P. putida whole cell lysate could feed the sulfite oxidation activity of SUOX or SorA and therefore, 
sulfite oxidation was monitored with DTNB as in previous chapters. Assays were started with 500 µM of sulfite and 
over the course of the sulfite oxidation assay, all readings were ≥ 500 µM ( Fig 2., B). T o our knowledge, no 
component in the oxidation assay should interact with DTNB in such a way as to increase the apparent sulfite 
concentration. The likely explanation for this inconsistency is precipitation of lysate components during HCl reaction 
inactivation leading to artificial absorbance increase – acidic precipitation of proteins is possible (Zellner et al. 
2005). Similar to the previous section, microtiter growth yield did not reveal consistent results across decreasing 
acetate concentrations ( Fig 2., C). As highlighted previously, inoculum colony age was not controlled and the 
discrepancies between ST8, 351 and 352 could be accounted for due to this lack of control. 
Despite unconfirmed sulfite oxidation activity and still inconclusive microtiter growth yield assay, it was assessed 
that TauE may yet be active and adaptive laboratory evolution could be attempted on engineered strains 351 and 
352. In a best-case scenario, 351 and 352 harbored active SUOX and SorA respectively and ALE would enhance 
the sulfonate consuming phenotype and, in a worse case scenario, both sulfite oxidase and exporter are inactive, 
and engineered strains would be adapted with a distinct ALE protocol compared to the previous section. 
In the hopes of enhancing sulfonate uptake, ALE was performed in increasing ethanesulfonate and decreasing 
acetate concentrations (Fig 2., D); specifically, 5:25, 10:20, 15:17.5, and 10:22.5 mM of acetate:ethanesulfonate. 
ALE was performed in Chi.Bio reactors as described in Chapter 3 and media regiments were swapped (e.g. 
swapped ethanesulfonate and acetate concentrations) once reactor culture had consumed 1 litre of media (Fig 2., 
D). From the results obtained during the generation of the sulfonate auxotr ophy in the previous section, growth 
yield may not be a suitable measure for screening adapted strains. Instead, ethanesulfonate consumption in media 
was monitored by targeted metabolomics. Several adapted 351 and 352 isolates were chosen and ethanesulfoante 
concentrations monitored following a 24-hour cultivation. In the end, 351 strains returned between 441 to 520 of 
500 µM added ethanesulfonate and 352 strains returned between 416 to 543 of 500 µM added ethanesulfonate. 
When no cells were added, the remaining ethanesulfonate concentrations were 650 +/- 45 µM. 

 
74 
 
The sulfite oxidases expressed in this chapter are molybopterin -dependent sulfite oxidase which contain a 
molybdopterin co-factor required for enzyme activity (D’errico et al. 2006, Kisker et al. 1998). When deciding to 
express SUOX and SorA, consideration was given to in vivo activity as it is expected that P. putida can synthesize 
the molybdopterin co-factor (Xia et al. 2018 and Turlin et al. 2023). Consideration was not, however, given to the 
necessary in vitro concentrations. D’Errico et al. 2006 did not have to supplement synthesized molybdopterin co-
factor when characterizing sulfite oxidases, however, did have to use a production strain high intracellular 
molybdenum achieve effective in vitro activity. Unsuccessful sulfite oxidation activity from cell lysate could have 
arisen due to limited molybdenum available for molybdopterin synthesis in vivo . While deBont media trace 
elements already contain sodium molybdate as molybdenum source, additional supplementation may resolve lack 
of activity issues. 
We don’t expect any component of our sulfite oxidation assay to generate apparent sulfite concentrations beyond 
500 µM. Addition of concentrated HCl during reaction killing led to the inconsistent precipitation of protein across 
wells and interfered with a ppropriate absorbance measurement. To improve the process, we would first need to 
confirm the if HCl killing of reactions is needed for accurate measurement. This could be achieved with real -time 
monitoring of absorbance at 412 nm of DTNB-reacted lysate reactions. Stable absorbance readings would indicate 
sufficient DTNB-mediated reaction killing. 
ALE is a powerful tool for the selection of phenotypes advantageous under controlled environments (Dragosits and 
Mattanovich, 2013). In this section, we hoped the expression of sulfite oxidases and exporters generates a 
metabolic environment where apparent  sulfur concentrations are decreased by decreasing the availability of 
sulfonate-generated sulfite. In an acetate diminishing environment, we hoped strains capable of metabolizing more 
sulfonates would have a greater fitness over those not able to where et hanesulfoante is abundant and acetate 
limiting.  
Why no isolates could be identified which could metabolize more sulfonates could be explained from a metabolic 
and process perspective. Much of what is known about sulfur metabolism in Gram-negative bacteria was inferred 
from E. coli. Regulationally, ssu enzymes are controlled at two levels, with cysB and with cbl (van der Ploeg et al. 
1999); this regulation is expected in P. putida but no discrete homolog to cbl has been identified. Furthermore, 
there is lack of knowledge surrounding negative regulation of  the ssu enzymes in E. coli or P. putida. One could 
hypothesize that abundant SsuD and SsuE may require increased NADH pools to support the activity of SsuE 
(Robbins and Ellis, 2012) and consequently sulfonate degradation. Rodriguez-Robles et al. 2024 and colleagues 
used the ssuEADCB operon to uptake sulfobutanoate amides with cargo molecules attached for intracellular 
release with a gamma-glutamyl transferase. The ssu operon was split placed under the regulation of Ptet and PBAD 
regulators, were only able to deliver 100 µM of sulfonate. Finally, when preparing samples for ethanesulfonate 
quantifications, samples are dilute 1:1000 in ddH2O, a step which is particularly sensitive to micro changes in 
pipetting. Using a liquid handler for sample preparation could streamline sample preparation and minimize pipetting 
error. 

 
75 
 
Linking sulfur and nitrogen metabolism for greater resolution increased sulfonate uptake 
When constructing a selection strain, great consideration needs to be given to the operational range of the pathway 
you are trying to enhance. That is, if your output will be growth, you must consider how effective your pathway will 
be to supporting the growth demands of you selection strain and, if the pathway is active, will baseline or enhanced 
activity be seen through the lens of growth. In the previous two sections, selection strains were made designed to 
deliver acetaldehyde from degraded sulfonates w hich, in turn, would be oxidized to acetate and feed carbon 
demand.  
Alternatively, taurine is a common sulfonate derived from variety of sources (Machlin et al. 1954, McCusker et al. 
2014, Sass and Martin et al . 1972 and Sumizu 1962) who’s degradation leads to the formation of 
aminoacetalehyde, an oxidation away from glycine (van der Ploeg et al. 1996). We hypothesized that, instead of 
developing a selection strain directed at carbon metabolism, directing efforts towards nitrogen metabolism may be 
fruitful. In E. coli, carbon to nitrogen ratios vary between 8 -10:1 (Rios-Lozano et al. 2016). If these ratios are 
anything similar in P. putida, feed nitrogen through sulfonate uptake and delivery could be less stringent a selection 
route and offer greater adaptation resolution (Fig 3., A).  
To that end, taurine was used a delivery mechanism for nitrogen. First, we assessed the ability of P. putida to 
oxidize aminoacetaldehyde to glycine. Aminoacetaldehyde is unstable at room temperature and not commercially 
available. Instead, aminoethanol (EtNH3OH) was used as a replacement. It’s expected that the metabolic product 
of EtNH3OH will follow the same degradation route as ethanol by first being oxidized to an intermediate aldehyde 
(aminoacetaldehyde) before terminal oxidation to an acid. P. putida can utilize ethanol as carbon source, and it is 
therefore predicted to harbor an alcohol dehydrogenase with potential activity towards EtNH3OH (Thompson et al. 
2020). To assess the ability of P. putida to utilize aminoacetaldehyde as nitrogen source, two strains were tested 
for their ability to grow EtNH3OH KT2440 and ΔserA, a glycine auxotroph provided by colleague Oscar Puiggene. 
When tested for their ability to grow on 10 and 20 mM EtNH 3OH in nitrogen free, no sulfur added deBont media 
(deBont(Cl-N)), only KT2440 could grow on 10 mM EtNH3OH (Fig 3., B). 
The inability of ΔserA to grow on EtNH 3OH and as sole nitrogen source indicates that degradation products of 
EtNH3OH does not produce sufficient or any aminoaceladehyde to support the glycine auxotrophy inherent to the 
strain. However, the growth of KT2440 on 10 mM of EtNH3OH does indicate that nitrogen, in some form, is released 
from aminoethanol and is capable of rescuing nitrogen limitation. Our initial hypothesis was the ammonia (NH3) is 
release from EtNH3OH or aminoacetaldehyde before aminoacetaldehyde can be oxidized to glycine. After a brief 
literature review, we found that E. coli will, in fact, degrade via release of NH3 from aminoethaneol (de Gouveia et 
al. 2023 and Jallet et al. 2024). This presented an opportunity to pivot away from connecting sulfur metabolism 
and glycine demand to sulfur and nitrogen metabolism. 
To adapt ST8 strains on taurine as both nitrogen and sulfur source, we first had to identify a critical nitrogen 
limitation point. By titrating NH 4Cl in deBont Cl(-N) media, we found that P. putida began to demonstrate growth 
inhibition on ~ 3 mM NH4Cl (Fig 3., C). With a selection condition identified, we next had to ensure any adaptation 

 
76 
 
occurred through the more promiscuous ssuEADCB operon and therefore the taurine specific tauABCD operon 
was disrupted (Eichhorn et al. 2000). 
Next, returning to the Chi.Bio reactors, an alternative ALE scheme was used. Instead of changing feed medias 
periodically, a baseline, stressful media of deBontCl(-N) was initially prepared containing 3 mM NH4Cl then reduced 
to 1 mM. The reactor was set to turbidostatic mode and the strains were initially supplemented with relaxing 
concentrations of NH4Cl the nitrogen content to deBontCl levels. The philosophy behind this scheme was to provide 
a set of conditions where cells can proliferate in relaxing conditions and, as the cells grow and the media replaced, 
stressing conditions where advantageous adaptations can arise. A cyclical moveme nt between allows for 
advantageous adaptations to arise in stressful conditions and for those adaptations to proliferate under relaxing 
conditions (Fig 3., D). Real time ALE ODChi.Bio values are reported in the supplementary material. 
After ~1 month of ALE, the final reactor culture was collected and the resulting strains isolated on LB media and 
characterized. Learning from the results of previous sections, strains were immediately screen for their ability to 
consume taurine. Taking advantage of established amino acid quantification methods, 15 strains and un-adapted 
ST8 Δtau were screen for their ability to consume taurine by quantifying taurine disappearance (Fig 3., E). Of the 
15 adapted strains tested, four returned taurine concentr ations statistically different from ST8 Δtau: TuA38 (2.68 
+/- 0.44 mM), TuA31 (2.64 +/- 0 mM), TuA18 (2.49 +/- 0.28 mM) and TuA12 (2.39 +/- 0.21 mM) (Fig 3., E). 
While at a glance, one could argue that TuA38, 31, 18 and 12 are ready for further characterization, taurine 
consumption characterization requires further testing. First, taurine loss to biomass absorption and processing 
needs to be assessed with the addit ion of a no -cells control similar previous sections. Substrate absorption to 
biomass may artificially obfuscate actual substrate consumption (Gupta et al 2020). Finally, tested strains need to 
be re-tested in a randomized fashion to clarify potential sample processing chronology effects. When samples are 
delivered to the HPLC instrument, they are first placed in a chilled autosampler. Chronological effects of total 
sample may have arisen due to first samples being warmer due to having spent less time in the chilled autosampler 
compared to later samples. Alternatively, guard column wear could explain the chronological effect. As more 
particulates and impurities build up in the guard column, the greater chance derivatized taurine could be 
sequestered by bound impurities. 
Should the above precautions demonstrate that the TuA strains are in fact not adapted, a new metabolic scheme 
needs to be implemented to connect sulfur and nitrogen metabolism. To that end, re-focusing on the original goal 
of this chapter may prove more su ccessful. With the added knowledge that E. coli can metabolize aminoethanol 
via deamination, disruption of P. putida homologs (PP_0542-0544) may pave the way for a novel glycine-auxotroph 
which could be rescued with taurine. Furthermore, the operational range of a glycine auxotrophy is narrower than 
that of carbon and nitrogen auxotroph leading to, hopefully, a biomass-dependent screening method.  
 
  

 
77 
 
Conclusion 
Platform technologies are versatile base technologies which allow for user -defined systemic exploration of a 
particular question. To establish an open-ended platform strain for new chemistry discovery, we tried to co-opt the 
ssu operon in P. putida to act as a catch-and-release mechanism for novel metabolites. Metabolic engineering of 
sulfur metabolism was successful as generation of a sulfonate auxotroph was made possible with disruption to the 
cysDNC enzymes and sulfate uptake hindered with en masse disruption of sulfate importers. ALE, however, failed 
to produce strains capable of over consuming sulfonates under three distinct selection schema and the reason 
likely lies in the operational range of sulfur metabolism. Due to the low levels of sulfur required for growth, we were 
left ‘blind’ to any sulfonate overconsuming phenotypes when growth yield was used fitness measure. With a 
potential upper limit ~100 µM sulfonate consumed; any selection strain designed for ALE would have to translate 
increased fitness within the 50 -100 µM range to use growth as a selectable marker. Total carbon and nitrogen 
metabolism are unsuitable as targets for in this range. Instead, connecting sulfonate metabolism to a narrower 
demand such as glycine demand may allow the use of g rowth yield as fitness measure. A process which could 
accelerate identification of strain capable of over-consuming sulfonates and screening selection strains. A crucial 
limitation to sulfur metabolism not yet explored is the upper bounds of sulfur consumption. If ssu and tau enzymes 
are constitutively expressed, what are the kinetic limitations to constant sulfonate uptake and degradation; will 
NADH or FMN become a limiting factor? Also, is there a protein -mediated degradation of sulfonate degrading 
enzymes preventing excessive accumulation of ssu and tau enzymes? Increasing available pools of NADH and 
heterologously expressing non-P. putida ssu and tau enzymes would shed light on these questions. It is our hope 
that these results will set the stage for fut ure development of sulfonate overconsuming P. putida strains and the 
systematic discovery of novel chemistries in vivo. 
  

 
78 
 
Materials & Methods 
Reagents and media. Chemicals in this study were purchased from Sigma-Aldrich (St. Louis, MI, USA) with the 
exception of potassium 3,3,4,4,5,5,6,6,7,7,8,8-tridecafluoroocantesulfonate (6:2 FTSA) which was purchased from 
Biosynth (Staad, Switzerland). Lysogeny broth (LB) composed of 5g/L NaCl, 10 g/L tryptone and 5g/L yeast extract. 
For solid LB agar, a further 15 g/L agar was added. Two minimal medias were prepared in this study: deBontCl and 
deBontCl(-N). DeBontCl is a modified deBont media with all instances of sulfate (SO 42-) replaced with chloride (Cl ) 
variants. In total, deBont Cl consists of 3.88 g/L K 2HPO4, 1.63 g/L NaH 2PO4, 4 g/L NH 4Cl, 10 mg/L 
ethylenediaminetetraacetic acid (EDTA), 100 mg/L MgCl2·6H2O, 2 mg/L ZnCl2, 1 mg/L CaCl2·2H2O, 5 mg/L FeCl2, 
0.2 mg/L Na2MoO4·2H2O, 0.2 mg/L CuCl2·5H2O, 0.4 mg/L CoCl2·6H2O and 1 mg/L MnCl 2·2H2O. For deBontCl(-N), 
NH4Cl was omitted, and media supplemented with defined quantities of NH4Cl or otherwise noted nitrogen source. 
Unless otherwise noted, sulfur sources were added to a final concentration of 2 mM, carbon sources added 
separately and kanamycin and gentamicin added to 50- and 10 µg/mL respectively, when needed. 
Bacterial strains, plasmids and oligonucleotides. All strains and plasmids are listed in tables Table 1 -2. 
Oligonucleotides were purchased from Integrated DNA technologies (Coralville, IA, USA), genomic DNA 
extractions performed with a DNeasy blood and tissue DNA extraction kit (Qiagen, Hilden, Germany) and plasmid 
extraction, PCR clean up and gel extractions done with a NucleoSpin® Gel and PCR clean-up kit (Macherny-Nagel, 
Düren, Germany). Oligonucleotides were designed with the Benchling primer wizard fun ction (Benchling, San 
Fransico CA, USA) or AMUSER web -tool (gene). Polymerase chain reactions (PCR) were performed with 
PhusionU (Thermo Fisher Scientific, Waltham MA, USA) or OneTaq polymerase (New England BioLabs, Ipswich 
MA, USA). 
Plasmid construction and homologous recombination -mediated genome engineering of Pseudomonas 
putida. Unless otherwise noted, plasmids were constructed with established USER cloning techniques (Nour-Eldin 
et al. 2006). In brief, primers were designed using the AMUSER web - tool (Genee et al. 2015) uracil-containing 
primers were purchased from Invitrogen (Waltham, MA, USA) and PCR performed with PhusionU (ThermoFisher, 
Waltham, MA, USA). Cleaned PCR fragments were pooled to equimolar concentrations and ligated with USER™ 
enzyme (New England Biolabs, Ipswich, MA, USA). Contaminating methylated DNA was digested using DpnI (New 
England Biolabs, Ipswich, MA, USA). 
Genetic manipulation was performed using pSWN2 assisted homologous recombination (Volke et al. 2021). In 
brief, genetic constructs destined for chromosomal deletion or integration were designed with two homology arms, 
~500 bp upstream and downstream a target region of interest. For deletion, the homology arms flanking a gene or 
region of interest were ligated together whereas, for insertion, homology arms flank an insertion of interest. To 
integrate constructed pSNW2 plasmids, Pseudomonas putida strains were washed with 1 mL of 300 mM sucrose 
2-3 times and washed strains placed in a Gene Pulser ® cuvette (Bio-Rad, Hercules, CA, USA) electroporation 
cuvette with 100-500 ng of purified plasmid and electroporated at 2.5 kV with a MicroPulser™ electroporator (Bio-

 
79 
 
Rad, Hercules, CA, USA). The cell mixture was recovered in 1 mL LB broth for one hour before plating on LB agar 
with kanamycin. 
Resulting colonies with green fluorescence and kanamycin resistance were considered single integrants. Single 
integrants were inoculated in LB with kanamycin, washed the following day 2 -3 times with 300 mM sucrose and 
electroporated with pQure-6-strong. The cell mixture was immediately suspended in 5 mL LB broth with gentamicin 
and 5 mM 3-methyl benzoate and incubated at 30°C overnight to promote a secondary recombination event. The 
following day, the curing broth was plated on LB agar with gentamicin and colonies with red fluorescence, absence 
of green fluorescence, sensitivity to kanamycin and genetic background of interest were inoculated in LB media 
with no antibiotics to cure the pQure -6-strong plasmid. Next, the cell mixture was plate on LB with no ant ibiotics 
and colonies screen for sensitivity to gentamicin. Successful genetic manipulations were screen by PCR and final 
strains stored at -80°C. 
Microtiter and shake flask growth assay. Growth characterization in this study was performed using two 
methods, microtiter growth assay’s and shake flask assays. For both assays, strains to be characterized were first 
grown overnight in 5 mL of LB broth and the following day, the turbid culture c ollected and washed twice with 
ddH2O. The resulting pellet was further resuspended and 1-3 mL of ddH2O and normalized to OD600 2.5-5 before 
moving to microtiter or shake flask set-ups. 
Microtiter growth assays were performed in 96-well plates on an Epoch 2 Mictrotiter Spectrophotometer (Winnoski, 
VA, USA) with agitation set to low, absorbance monitoring set to 600 nm and temperature set to 30C for optimal 
P. putida growth. To prepare a microtiter growth assays 96-well plate, the outer columns and rows of the chosen 
96-well plate were filled with 250 µL ddH2O to help minimize central well evaporation throughout the assay leaving 
60 effective wells. Next, washed strains were inoculated as n eeded in each well at a 1:100 ratio (starting OD600 
~ 0.025 - 0.05). Raw absorbance data were recorded in the Gen5 (Santa Clara, CA, USA) software and absorbance 
data at 600 nm were converted to OD600 when necessary, with comparison to a standard curve. 
Shake flask experiments were performed using 250 mL baffled shake flasks (Fisher Scientific, Waltham, MA, USA) 
in a shaking incubator. To begin a shake flask experiments, 50 mL of select media were transferred to each flask 
and inoculated with washed, conc entrated select strain to a starting OD 600 of 0.025-0.05. Growth was monitored 
with OD 600 measurements using an Jenway 6705 UV-Vis Spectrophotometer (Cole-Palmer, Chicago, IL, USA). 
Where necessary, growth parameters were calculated using the QurvE (Wirth et al. 2023) software with default 
settings unless otherwise specified. 
Adaptive Laboratory Evolution procedures. In this chapter, three adaptive laboratory evolution (ALE) protocols 
were followed: manual ALE, Chi.Bio -assisted relaxer decreasing ALE and relaxer spiking ALE. Manual ALE 
procedures were performed by manually passaging cultures in a 24-well deep well plate in a fixed media condition.  
Chi-Bio assisted ALE procedures were followed using the set-up described in Chapter 3. In brief, Chi.Bio reactors 
were set-up in turbidostatic function with modified code to allow for an approximate 0.5 ODChi.Bio oscillation across 

 
80 
 
a target OD. A relaxer decreasing ALE involved the steady decrease of a relaxer concentration (e.g Acetate) via 
multiple feed-media replacements. Relaxer spiking ALE involved the fixing a stringent media regiment (e.g limiting 
nitrogen) and periodically sp iking the reactor with concentrated relaxer (e.g. NH 4Cl) when real -time OD Chi.Bio 
measurements no longer initiate media replacement. 
Sulfite and free -thiol determination. Sulfite and free -thiol concentrations were determined using established 
free-thiol fluorometric assays (Ellman, 1959 and Reiner et al. 2002). In brief, 5,5′ -dithiobis-(2-nitrobenzoic acid) 
(DTNB) is a di -sulfide containing aromatic compound which, when mixed with free -thiol containing solution (e.g. 
sulfite, cysteine), said bond will break generating equimolar concentrations of a 2 -nitro-5-thiobenzoate (TNB 2-) 
bound molecule and free TNB 2-. TNB2- produces as strong yellow color with spectrophotometric maxima at 412 
nm. Spectrophotometric readings at 412 nm were taken in an Epoch 2 Microtiter Spectrophotometer (Agilent, Santa 
Clara, CA, USA) or an Jenway 6705 UV -Vis Spectrophotometer (Cole -Palmer, Chicago, IL, USA) . Free -thiol 
concentrations are expected to be equimolar to TNB2- concentrations; effective concentrations of free-thiol are then 
estimated with the molar extinction coefficient of TNB2- (14150 M-1 cm-1) or with reference to a standard curve. 
Sulfite oxidation by cell lysate assay. Sulfite oxidation was monitored by quantifying sulfite concentrations over 
time when exposed to various whole cell lysates. To start, strains with lysate destined for assessment of sulfite 
oxidation were grown in 50 mL LB media overnight. The following day , the resulting cultures were harvested by 
centrifugation at 4000 g’s for 15 minutes and the resulting supernatant discarded. Cell pellets were washed twice 
with ddH2O following the pelleting conditions before being suspended in 5 mL of Tris-HCl pH 7.0. Cells were lysed 
by sonication with a Vibra -Cell VCX130 (Sonics, Newton, CT, USA) sonicator equipped with a 2 mm sonicator 
probe. Cells were sonicated on ice with 50% amplitude setting for 30 seconds with a 30 second r est following. 
Sonication cycle was repeated three times or until a visible change in lysate color was observed. 
Intact cells and cell debris were separated from whole cell lysate by centrifugation at 14000 g’s for 30 minutes. The 
resulting supernatant was filtered with a 0.22 -0.45 µm filter and total protein content was estimated using the 
Bradford method (Kielkopf et al . 2020). In brief, protein -containing solution was mixed 1:1 with Coomassie 
InstantBlue protein staining solution (Abcam, Manchester, United Kingdom) and absorbance at 595 recorded on 
an Epoch 2 Microtiter plate reader (Agilent, Santa Clara, CA, USA) or Jenway 6705 UV-Vis Spectrophotometer 
(Cole-Palmer, Chicago, IL, USA) Spectrophotometer. Protein content was estimated by standard curve generated 
with defined bovine serum albumin (BSA) concentrations. 
To monitor sulfite oxidation by cell lysate, a 96-well plate containing the desired number of time points was prepared 
containing 50 mM Tris-HCl pH 7.0 and 500 µM sodium sulfite and, to a final volume of 100 µL, 50 µg of cell lysate 
was added. Reactions were stopped with the addition of HCl to a final concentration of 50 mM and reducing thiols 
quantified with DTNB.  
Taurine & Ethanesulfonate consumption assay. To estimate taurine and ethanesulfonate consumption by 
engineered and adapted strains, HPLC and targeted metabolomics were performed at the Novo Nordisk Center 
for Biosustainability analytics department. In brief, strains destined for Taurine or Ethanesulf onate consumption 

 
81 
 
quantification were prepared by pre-culturing to late stationary phase chosen strains in 1 mL of test media in 24 -
well deep well plates overnight at 30C. The following day, 10 µL of overnight, stationary culture was transferred to 
a fresh 1 mL of test medi a and incubated at 30C for 8 -12 hours. Next, cells were harvested by centrifugating the 
deep well plates at 4000 g’s for 10 -30 minutes. Supernatant were aspirated before proceeding for “Taurine 
determination and quantification” or “Ethanesulfonate determination and quantification”. 
Taurine determination and quantification was performed following established amino acid derivatization 
protocols (Dietmair et al. 2010). In brief, samples destined for amino acid derivatization were first diluted 1:10 in 
ddH2O and further diluted 1:1 with internal standard (sarcosine and aminobutyric acid). Prepared samples were 
transferred to a 32 x 11.6 mm clear glass vial (Mirkolab Aarhus, Aarhus, Denmark) and capped with a 
silicone/PTFE screw-cap lid (Mikrolab Aarhus, Aarhus, Denmark) and analyzed on an Dionex Ultimate 3000 HPLC 
system (Thermo Fisher, Waltham, MA, USA) equipped with a Dionex Ultimate 3000 WPS -3000 autosampler. 
Samples were separated on a Gemini C18 column (Phenomex, Torrance, CA, USA) column with a SecurityGuard 
C18 guard column (Phenome x, Torrance, CA, USA). Samples were derivatized as per Dietmair et al. 2010 and 
derivatization automated with the Ultimate 3000 WPS -3000 autosampler. Full chromatographic method can be 
found in the supplementary materials. Derivatized amino-containing compounds were monitored with 340 and 266 
nm excitation wavelengths and 450 and 305 nm emission wavelengths respectively. Peak areas were analyzed 
with the (Thermo Fisher, Waltham, MA, USA) and taurine peak areas normalized to internal standard peak area. 
Where relevant, peak areas were converted to concentration with reference to a standard curve of known taurine 
concentrations. 
Ethanesulfonate determination and quantification was performed using a targeted metabolimcs method 
established in Chapter 2. In brief, clarified samples were diluted 1:1000 and analyzed on a ultra-high performance 
liquid chromatography (Nexera X2, Shimaduzu, Kyoto, Japan) coupled to tandem mass spectrome try (SCIEX 
QTRAP 5500, SCIEX Framingham, MA, USA) and samples were separated using a XSelect® HSS T3 Column (2.1 
mm x 50 mm, particle size 2.5 um) (WatersTM, Milford, MA, USA) with 10 mM tributalamine, 20 mM acetic acid in 
5% (v/v) methanol 2% (v/v) isopropanol as eluent A and isopropanol as eluent B. Full chromatographic method 
can be found in the supplementary materials. Data was acquired using the SCIEX Analyst® software (version 1.7.3) 
and processed using the SCIEX OS software (version 3.0.0.3399). 
  

 
82 
 
Table 1. Plasmids used and generated in this Chapter. 
Plasmid name Description Source 
pSNW2 P14g(BCD2) -> msfGFP; KmR Volke et al. 2020 
pQure-6-Strong Xyl/Pm -> I-SceI; P14g(BCD2) -> 
mRFP; GmR 
Volke et al. 2020 
pSNW2ΔcysDNC Suicide vector for cysDNC 
disruption 
This study 
pSNW2ΔcysAWU_sbp-II Suicide vector for cysAWU and 
sbp-II disruption 
This study 
pSNW2Δsbp-I Suicide vector for sbp-I 
disruption 
This study 
pSNW2ΔcysZ Suicide vector for cysZ 
disruption 
This study 
pSNW2ΔPP_4112 Suicide vector for PP_4112  
disruption 
This study 
pSNW2ΔPP_1407 Suicide vector for PP_1407  
disruption 
This study 
pSNW2ΔPP_0718 Suicide vector for PP_0718  
disruption 
This study 
pSNW2ΔPP_0101 Suicide vector for PP_0101  
disruption 
This study 
pSNW2_LPpEM7::SUOX_tauE Suicide vector for SUOX and 
tauE integration 
This study 
pSNW2_LPpEM7::SorA_tauE Suicide vector for draSO and 
tauE integration 
This study 
pSNW2Δtau Suicide vector for tauABCD 
disruption 
This study 
 
 
 
 
 

 
83 
 
Table 2. Strains used and generated in this Chapter. 
Strain name1-2 Description Source 
Pseudomonas putida   
KT2440 Wild-type strain Bagdasarian et al. 1981 
ST7 KT2440; deletion of cysAWU, 
sbp-I/II, PP_4112, 1407, 0718 
and 0101 
This study 
ST8 ST7; ΔcysDNC This study 
ST8 Δtau ST8; deletion of tauABC  This study 
ΔserA Deletion of serA Turlin et al. 2022 
351 ST8; pEM7 -> SUOX, p14 G -> 
tauE 
This study 
352 ST8; pEM7 -> sorA, p14 G -> 
tauE 
This study 
Eschericha coli   
DH5α λpir Cloning host, DH5α variant with 
λpir lysogen 
Platt et al. 2000 
1 All strains generated in this study were generated from Pseudomonas putida KT2440 except for ΔserA which 
was generated from EM42. 
2 Adapted strains not listed.   

 
84 
 
References 
Bayer, C. N., Rennig, M., Ehrmann, A. K., & Nørholm, M. H. H. (2021). A standardized genome 
architecture for bacterial synthetic biology (SEGA). Nature Communications, 12(1).  
Bechtel, T. J., & Weerapana, E. (2017). From structure to redox: The diverse functional roles of disulfides 
and implications in disease. PROTEOMICS, 17(6), 1600391.  
Bottos, E. M., AL-shabib, E. Y., Shaw, D. M. J., McAmmond, B. M., Sharma, A., Suchan, D. M., Cameron, 
A. D. S., & Van Hamme, J. D. (2020). Transcriptomic response of Gordonia sp. strain NB4-1Y when provided with 
6:2 fluorotelomer sulfonamidoalkyl betaine o r 6:2 fluorotelomer sulfonate as sole sulfur source. Biodegradation, 
31(4-6), 407–422.  
Butt, T. R., Edavettal, S. C., Hall, J. P., & Mattern, M. R. (2005). SUMO fusion technology for difficult-to-
express proteins. Protein Expression and Purification, 43(1), 1–9.  
Cohen, H. (1972). Hepatic Sulfite Oxidase. The Journal of Biological Chemistry, 247(23). 
Craig, K., Johnson, B. R., & Grunden, A. (2021). Leveraging Pseudomonas Stress Response 
Mechanisms for Industrial Applications. Frontiers in Microbiology, 12.  
Dayal, P. V., Singh, H., Busenlehner, L. S., & Ellis, H. R. (2015). Exposing the Alkanesulfonate 
Monooxygenase Protein-Protein Interaction Sites. Biochemistry, 54(51), 7531–7538.  
Di Salle, A., D’Errico, G., La Cara, F., Cannio, R., & Rossi, M. (2006). A novel thermostable sulfite oxidase 
from Thermus thermophilus: characterization of the enzyme, gene cloning and expression in Escherichia coli. 
Extremophiles : Life under Extreme Conditions, 10(6), 587–598.  
Dietmair, S., Timmins, N. E., Gray, P. P., Nielsen, L. K., & Krömer, J. O. (2010). Towards quantitative 
metabolomics of mammalian cells: Development of a metabolite extraction protocol. Analytical Biochemistry , 
404(2), 155–164.  
Douwe, J., Weiss, M. A., Saller, E., H Nashimoto, Saito, N., Kertesz, M. A., & Leisinger, T. (1996). 
Identification of sulfate starvation-regulated genes in Escherichia coli: a gene cluster involved in the utilization of 
taurine as a sulfur source. Journal of Bacteriology, 178(18), 5438–5446.  
Dragosits, M., & Mattanovich, D. (2013). Adaptive laboratory evolution – principles and applications for 
biotechnology. Microbial Cell Factories, 12(1), 64.  
Duan, X., Hall, J. A., Nikaido, H., & Quiocho, F. A. (2001). Crystal structures of the maltodextrin/maltose-
binding protein complexed with reduced oligosaccharides: flexibility of tertiary structure and ligand binding. Journal 
of Molecular Biology, 306(5), 1115–1126.  

 
85 
 
Eichhorn, E., van der Ploeg, J. R., & Leisinger, T. (1999). Characterization of a Two -component 
Alkanesulfonate Monooxygenase from Escherichia coli. Journal of Biological Chemistry, 274(38), 26639–26646.  
Eichhorn, E., van der Ploeg, J. R., & Leisinger, T. (2000). Deletion Analysis of the Escherichia coli Taurine 
and Alkanesulfonate Transport Systems. Journal of Bacteriology, 182(10), 2687–2695.  
Eilers, T., Schwarz, G., Brinkmann, H., Witt, C., Richter, T., Nieder, J., Koch, B., Hille, R., Hänsch, R., & 
Mendel, R. R. (2001). Identification and Biochemical Characterization ofArabidopsis thaliana Sulfite Oxidase. 
Journal of Biological Chemistry, 276(50), 46989–46994.  
Ellman, G. L. (1959). Tissue sulfhydryl groups. Archives of Biochemistry and Biophysics, 82(1), 70–77.  
Gao, B., & Ellis, H. R. (2007). Mechanism of flavin reduction in the alkanesulfonate monooxygenase 
system. Biochimica et Biophysica Acta (BBA) - Proteins and Proteomics, 1774(3), 359–367.  
Genee, H. J., Bonde, M. T., Bagger, F. O., Jespersen, J. B., Sommer, M. O. A., Wernersson, R., & Olsen, 
L. R. (2014). Software -Supported USER Cloning Strategies for Site -Directed Mutagenesis and DNA Assembly. 
ACS Synthetic Biology, 4(3), 342–349.  
Gupta, P., Gupta, S., & Pruthi, V. (2020). Techniques for Detection and Extraction of Metabolites. 
Engineering of Microbial Biosynthetic Pathways, 33–51.  
Harper, S., & Speicher, D. W. (2010). Purification of Proteins Fused to Glutathione S -Transferase. 
Methods in Molecular Biology, 681, 259–280.  
Hengen, P. N. (1995). Purification of His-Tag fusion proteins from Escherichia coli. Trends in Biochemical 
Sciences, 20(7), 285–286.  
Hubrich, F., Müller, M., & Andexer, J. N. (2021). Chorismate - and isochorismate converting enzymes: 
versatile catalysts acting on an important metabolic node. Chemical Communications, 57(20), 2441–2463.  
Kappler, U., & Bailey, S. M. (2005). Molecular Basis of Intramolecular Electron Transfer in Sulfite-oxidizing 
Enzymes Is Revealed by High Resolution Structure of a Heterodimeric Complex of the Catalytic Molybdopterin 
Subunit and a c-Type Cytochrome Subunit. Journal of Biological Chemistry, 280(26), 24999–25007.  
Kapust, R. B., & Waugh, D. S. (1999). Escherichia colimaltose -binding protein is uncommonly effective 
at promoting the solubility of polypeptides to which it is fused. Protein Science, 8(8), 1668–1674.  
Kertesz, M. A. (2000). Riding the sulfur cycle – metabolism of sulfonates and sulfate esters in Gram -
negative bacteria. FEMS Microbiology Reviews, 24(2), 135–175. 
Kielkopf, C. L., Bauer, W., & Urbatsch, I. L. (2020). Bradford Assay for Determining Protein Concentration. 
Cold Spring Harbor Protocols, 2020(4). 

 
86 
 
Kim, M. H., Wang, N., & Chu, K. H. (2013). 6:2 Fluorotelomer alcohol (6:2 FTOH) biodegradation by 
multiple microbial species under different physiological conditions. Applied Microbiology and Biotechnology, 98(4), 
1831–1840.  
Kisker, C., Schindelin, H., Baas, D., Rétey, J., Meckenstock, R. U., & Kroneck, P. M. H. (1998). A 
structural comparison of molybdenum cofactor-containing enzymes. FEMS Microbiology Reviews, 22(5), 503–521.  
Krone, F. A., Westphal, G., & Schwenn, J. D. (1991). Characterisation of the gene cysH and of its product 
phospho-adenylylsulphate reductase from Escherichia coli. Molecular & General Genetics : MGG , 225(2), 314–
319.  
Leyh. (2015). The sulfate activation locus of Escherichia coli K12: cloning, genetic, and enzymatic 
characterization. The Journal of Biological Chemistry, 263(5).  
Liu, C., Suo, Y., & Leyh, T. S. (1994). The energetic linkage of GTP hydrolysis and the synthesis of 
activated sulfate. Biochemistry, 33(23), 7309–7314. 
Liu, J., Lee, L. S., Nies, L. F., Nakatsu, C. H., & Turco, R. F. (2007). Biotransformation of 8:2 Fluorotelomer 
Alcohol in Soil and by Soil Bacteria Isolates. Environmental Science & Technology, 41(23), 8024–8030.  
Machlin, L. J., Pearson, P. B., & Denton, C. A. (1954). The Ultilization of sulfate sulfur for the synthesis of 
taurine in the developing chick embryo. Journal of Biological Chemistry, 212(1), 469–475. 
Mansoury, M., Hamed, M., Karmustaji, R., Al Hannan, F., & Safrany, S. T. (2021). The edge effect: A 
global problem. The trouble with culturing cells in 96-well plates. Biochemistry and Biophysics Reports, 26, 100987.  
Martínez-García, E., & de Lorenzo, V. (2024). Pseudomonas putida as a synthetic biology chassis and a 
metabolic engineering platform. Current Opinion in Biotechnology, 85, 103025.  
McCusker, S., Buff, P. R., Yu, Z., & Fascetti, A. J. (2014). Amino acid content of selected plant, algae and 
insect species: a search for alternative protein sources for use in pet foods. Journal of Nutritional Science, 3. 
Mohamed, E. T., Mundhada, H., Landberg, J., Cann, I., Mackie, R. I., Nielsen, A. T., Herrgård, M. J., & 
Feist, A. M. (2019). Generation of an E. coli platform strain for improved sucrose utilization using adaptive 
laboratory evolution. Microbial Cell Factories, 18(1). 
Moreira de Gouveia, M. I., Daniel, J., Garrivier, A., Bernalier-Donadille, A., & Jubelin, G. (2022). Diversity 
of ethanolamine utilization by human commensal Escherichia coli. Research in Microbiology, 174(1-2), 103989.  
Nour-Eldin, H. H., Hansen, B. G., Nørholm, M. H. H., Jensen, J. K., & Halkier, B. A. (2006). Advancing 
uracil-excision based cloning towards an ideal technique for cloning PCR fragments. Nucleic Acids Research , 
34(18), e122–e122.  

 
87 
 
Platt, R., Drescher, C., Park, S.-K., & Phillips, G. J. (2000). Genetic System for Reversible Integration of 
DNA Constructs and lacZ Gene Fusions into the Escherichia coli Chromosome. Plasmid, 43(1), 12–23.  
Riener, C. K., Kada, G., & Gruber, H. J. (2002). Quick measurement of protein sulfhydryls with Ellman’s 
reagent and with 4,4′-dithiodipyridine. Analytical and Bioanalytical Chemistry, 373(4-5), 266–276.  
Rios-Lozano, M., Guerrero -Torres, V., Badillo -Corona, A., Chairez, I., & Garibay -Orijel, C. (2016). 
Characterization of nitrogen substrate limitation on Escherichia coli’s growth by parameter identification tools. 
Bioprocess and Biosystems Engineering, 39(7), 1151–1161.  
Riveros-Rosas, H., Julián-Sánchez, A., Moreno-Hagelsieb, G., & Muñoz-Clares, R. A. (2019). Aldehyde 
dehydrogenase diversity in bacteria of the Pseudomonas genus. Chemico-Biological Interactions, 304, 83–87.  
Robbins, J. M., & Ellis, H. R. (2012). Identification of Critical Steps Governing the Two -Component 
Alkanesulfonate Monooxygenase Catalytic Mechanism. Biochemistry, 51(32), 6378–6387. 
Rodríguez-Robles, E., Müller, D., Tilmann Künzl, Nemat, S. J., Martin Peter Edelmann, Srivastava, P., 
Louis, D., Elisabetta Groaz, Konrad Tiefenbacher, Tania Michelle Roberts, Piet Herdewijn, Philippe Marlière, & 
Panke, S. (2024). Rational design of a bacterial import system for new-to-nature molecules. Metabolic Engineering, 
85, 26–34. 
Sass, N. L., & Martin, W. G. (1972). The Synthesis of Taurine from Sulfate III. Further Evidence for the 
Enzymatic Pathway in Chick Liver. Experimental Biology and Medicine, 139(3), 755–761. 
Schrader, N., Fischer, K., Theis, K., Mendel, R. R., Schwarz, G., & Kisker, C. (2003). The Crystal Structure 
of Plant Sulfite Oxidase Provides Insights into Sulfite Oxidation in Plants and Animals. Structure, 11(10), 1251–
1263.  
Shaw, D. M. J., Munoz, G., Bottos, E. M., Duy, S. V., Sauvé, S., Liu, J., & Van Hamme, J. D. (2019). 
Degradation and defluorination of 6:2 fluorotelomer sulfonamidoalkyl betaine and 6:2 fluorotelomer sulfonate by 
Gordonia sp. strain NB4-1Y under sulfur-limiting conditions. Science of the Total Environment, 647, 690–698.  
Studier, F. William., & Moffatt, B. A. (1986). Use of bacteriophage T7 RNA polymerase to direct selective 
high-level expression of cloned genes. Journal of Molecular Biology, 189(1), 113–130.  
Sumizu, K. (1962). Oxidation of hypotaurine in rat liver. Biochimica et Biophysica Acta, 63(1), 210–212.  
Takagi, H., & Ohtsu, I. (2016). l -Cysteine Metabolism and Fermentation in Microorganisms. Amino Acid 
Fermentation, 129–151.  
Tan, W. -H. . (2005). Isolated Sulfite Oxidase Deficiency: A Case Report With a Novel Mutation and 
Review of the Literature. PEDIATRICS, 116(3), 757–766.  

 
88 
 
Thompson, M. G., Incha, M. R., Pearson, A. W., Schmidt, M., Sharpless, W. A., Eiben, C. B., Cruz -
Morales, P., Blake-Hedges, J. M., Liu, Y., Adams, C. A., Haushalter, R. C., Krishna, R. N., Lichtner, P., Blank, L. 
M., Mukhopadhyay, A., Deutschbauer, A. M., Shih, P. M., & Keasling, J. D. (2020). Fatty Acid and Alcohol 
Metabolism in Pseudomonas putida: Functional Analysis Using Random Barcode Transposon Sequencing. 
Applied Environmental Microbiology, 86(21). 
Turlin, J., Dronsella, B., De Maria, A., Lindner, S. N., & Nikel, P. I. (2022). Integrated rational and 
evolutionary engineering of genome -reduced Pseudomonas putida strains promotes synthetic formate 
assimilation. Metabolic Engineering, 74, 191–205.  
Turlin, J., Òscar Puiggené, Donati, S., Wirth, N. T., & Nikel, P. I. (2023). Core and auxiliary functions of 
one-carbon metabolism in Pseudomonas putida  exposed by a systems -level analysis of transcriptional and 
physiological responses. MSystems. 
Volke, D. C., Friis, L., Wirth, N. T., Turlin, J., & Nikel, P. I. (2020). Synthetic control of plasmid replication 
enables target- and self-curing of vectors and expedites genome engineering of Pseudomonas putida. Metabolic 
Engineering Communications, 10, e00126.  
Volke, D. C., Wirth, N. T., & Nikel, P. (2021). Rapid Genome Engineering of Pseudomonas Assisted by 
Fluorescent Markers and Tractable Curing of Plasmids. BIO-PROTOCOL, 11(4).  
Weinitschke, S., Denger, K., Cook, A. M., & Smits, T. H. M. (2007). The DUF81 protein TauE in 
Cupriavidus necator H16, a sulfite exporter in the metabolism of C2 sulfonates. Microbiology, 153(9), 3055–3060.  
Wirth, N. T., Gurdo, N., Krink, N., Vidal-Verdú, À., Donati, S., Férnandez-Cabezón, L., Wulff, T., & Nikel, 
P. I. (2022). A synthetic C2 auxotroph of Pseudomonas putida for evolutionary engineering of alternative sugar 
catabolic routes. Metabolic Engineering, 74, 83–97.  
Wirth, N. T., Kozaeva, E., & Nikel, P. I. (2020). Accelerated genome engineering of Pseudomonas putida 
by I‐ Sce I―mediated recombination and CRISPR ‐Cas9 counterselection. Microbial Biotechnology, 13(1), 233–
249.  
Xia, Z., Lei, L., Zhang, H.-Y., & Wei, H.-L. (2018). Characterization of the ModABC Molybdate Transport 
System of Pseudomonas putida in Nicotine Degradation. Frontiers in Microbiology, 9.  
Zellner, M., Winkler, W., Hayden, H., Diestinger, M., Maja Munk Eliasen, Bernd Gesslbauer, Miller, I., 
Chang, M., Kungl, A. J., Roth, E., & Oehler, R. (2005). Quantitative validation of different protein precipitation 
methods in proteome analysis of blood platelets. Electrophoresis, 26(12), 2481–2489.  
Zhang, L., Jiang, W., Nan, J., Almqvist, J., & Huang, Y. (2014). The Escherichia coli CysZ is a pH dependent 
sulfate transporter that can be inhibited by sulfite. Biochimica et Biophysica Acta (BBA) - Biomembranes, 1838(7), 
1809–1816.  

 
89 
 
 
 
 
 
Figure 1. Engineering of Pseudomonas putida ST8 and adaptive laboratory evolution towards increased sulfonate consumption. A) Metabolic 
map of sulfur metabolism in Pseudomonas putida ST8 with designed modifications. Arrowed reactions indicate putative reactions, and red 
crosses indicate intended inhibitions with genetic modifications. B) Sulfate-response curve of Pseudomonas putida ST8. Dashed line 
corresponds to 100 µM of sulfate. C) Adaptive laboratory evolution strategy for Pseudomonas putida ST8; P. putida ST8 was serial passaged 
in 15 mM EtSO3 and 15 mM AcE for 25 passages, isolates collected, and fitness monitored via shake flask growth characterization. D) Acetate 
titration in excess sulfonate of ST8 and adapted strains. E) Shake flask characterization of select, adapted Pseudomonas putida ST8 strains in 
deBont media with 30 mM Acetate and 15 mM EtSO3. Error bars indicate standard deviations (n=3). 

 
90 
 
 
Figure 2. Further engineering of Pseudomonas putida ST8 and carbon limiting adaptive laboratory evolution towards increased sulfonate uptake. A) Metabolic map of sulfur 
metabolism in Pseudomonas putida ST8_SorA and ST8_SUOX. Arrowed reactions indicate putative reactions, and red crosses indicate intended inhibitions with genetic 
modification. B) Sulfite oxidation by Pseudomonas putida ST8_SorA and ST8_SUOX whole cell lysate. C) Adaptive laboratory evolution strategy for Pseudomonas putida 
ST8_SorA and ST8_SUOX; P. putida ST8_SorA and ST8_SUOX were cultivated in Chi.Bio reactors under turbidostatic conditions in EtSO3 and AcE media with sequential 
ratio increase, isolates were collected and characterized. D) Acetate titration under excess sulfonate of ST8, ST8_SorA and ST8_SUOX E) Ethanesulfonate consumption of 
ST8, ST8_SorA and ST8_SUOX. Error bars represent standard deviations (n=3). 
 

 
91 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
Figure 3. Optimizing taurine to amino acid and nitrogen metabolism towards nitrogen-oriented adaptive laboratory evolution of Pseudomonas putida ST8. A) 
Metabolic map of sulfur metabolism in Pseudomonas putida ST8Δtau. Arrowed reactions indicate putative reactions and red crosses indicate intended inhibitions 
with genetic modification. B) Ethanolamine consumption characterization of Pseudomonas putida ST8Δtau, rG1ΔserA. C) NH4Cl titration of ST8, Titration 1 from 
30.5 mM to 0.71 mM and Titration 2 from 3.05 mM to 0.07 mM. D) Adaptive laboratory evolution strategy for Pseudomonas putida ST8Δtau; P. putida ST8Δtau 
was cultivated in nitrogen starved conditions under pseudo-turbidostatic conditions and spiked with concentrated NH4Cl when growth stopped, isolates were 
collected and characterized. E) Taurine consumption of Pseudomonas putida ST8Δtau and select adapted variants. Error bars represent standard deviations (n=3). 

 
92 
 
Chapter 4: Hidden in plain sight: Potential in upcycling PFAS 
Garret William O’Connell1 & Pablo Ivan Nikel1 
1The Novo Nordisk Center for Biosustainability, Technical University of Denmark 
 
After at least three decades of research, the field of per - and polyfluorinated substances (PFAS) biodegradation 
remains as timely as ever. To date, PFAS biodegradation studies can be classified into two major categories: 
substrate disappearing and metabolite identifying. Of the latter, two major studies have reported on the 
biodegradative capacity of bacteria and reported on the potential mechanisms involved. This, in combination with 
recent advances into New -to-Nature molecule delivery via sulfonate metabolism, may shorten the gap between 
degradation and upcycling. In this opinion article, we discuss the latest developments in the domain of 
biodegradation of PFAS, and we expose the key role of synthetic biology and metabolic engineering to bring new 
(biosynthesis) degradation chemistries into living cells. 
  

 
93 
 
Per and Polyfluoroalkyl substances: definitions and categories 
 
Per and polyfluoroalkyl substances (PFAS) are a broad category of typically aliphatic, heavily fluorinated molecules 
that are considered emergent pollutants due to their bioaccumulation, resistance to physical and chemical 
degradation and ubiquitous usage (Gluge et al. 2020 and Brun at al. 2023). The carbon-fluorine bond is on of the 
strongest in organic chemistry, contributing to high thermal and chemical stability of PFAS (O’Hagan 2008). This 
makes them incredibly resistant to both environmental and metabolic degradation earning them the  nickname 
“forever chemicals”. The persistence of PFAS in the environment poses significant challenges for remediation and 
has led to widespread contamination of water supplies (McMahon et al. 2022, Gobelius et al. 2018 and Murakami 
et al. 2009). Exposure to PFAS has been linked to various health issues, including cancer, and immune system 
disruption (Sunderland et al. 2019, Barry et al. 2013, Grandjean et al. 2012). 
Well known PFAS include perfluorooctanoate (PFOA, C8) and perfluorooctanesulfonate (PFOS). These 
substances are used in a variety of non-stick cookware, water-repellent fabrics and firefighting foams (Gluge et al. 
2020). Within the category of PFAS, two major groups emerge: polymers and non -polymers (Buck et al. 2011). 
The former group contains well -known materials such as Teflon and perfluoropolyether (Buck et al. 2011), while 
the later is further divided into two families: perfluorinated and polyfluorinat ed. Perfluorinated substances are 
aliphatic molecules with all carbon-hydrogen bonds replaced with carbon-fluorine bonds, such as PFOA and PFOS 
whereas polyfluorinated substances contain one ore more carbon -hydrogen bonds, such as 
3,3,4,4,5,5,6,6,7,7,8,8,8-tridecafluoro-1-octanesulfonic acid (6:2 FTSA) or 3,3,4,4,5,5,6,6,7,7,8,8,8 -tridecafluoro-
1-sulfonamidoalkyl betaine (6:2 FTAB). Perfluorinated substances are typically less complex than polyfluorinated 
substances, more resistant to degradation and considered environmental end-point products (Cousins et al. 2020). 
 
Bacterial degradation of PFAS 
 
Understanding the biological mechanisms behind PFAS degradation has been an ongoing effort for the past 30 
years. Studies have attempted to elucidate the mechanisms of PFAS degradation primarily through two ‘types’ of 
studies: PFAS disappearance (and fluoride appearance) studies (Yi et al. 2016 and Kwon et al. 2014) or metabolite 
identification studies. In the former, PFAS disappearance is typically monitored in conjunction with fluoride 
increase. Examplβes include the works of Kwon et al. 2014 that, not withstanding rebuttal (Avendano et al. 2015), 
monitored PFOS disappearance in culture media enriched with Pseudomonas aeruginosa HJ4 and attempted 
fluoride monitoring. Unfortunately, these studies do not shed light on the potential underlying mechanism of PFAS 
degradation will not be included here. 
The later category of study involves identification of PFAS degradation metabolites and hypothesized degradation 
routes. Examples include the works of Wang et al. 2009 and Zhang et al. 2016 where polyfluorinated alcohols and 
sulfonates degradation products were identified from batch microbial community experiments. In most cases 
Pseudomonas species have been attributed to as the main degraders of polyfluorinated substances (Key et al. 

 
94 
 
1998, Liu et al. 2007 and Kim et al. 2012). More recently, Gordonia NB4-1Y and Dietzia aurantiaca have been 
reported to degrade sulfonated PFAS such as 6:2 FTSA and upstream products such as 3,3,4,4,5,5,6,6,7,7,8,8,8-
tridecafluoro-1-sulfonamidoalkyl betaine (6:2 FTAB) (Shaw et al. 2019 and Mendez et al. 2022). 
While aerobic and anaerobic degradation of PFAS bear similarities, anaerobic degradation is limited in upstream 
metabolites (Zhang et al. 2016). While, in aerobic degradation, upstream PFAS metabolites (non -carboxylates) 
are hypothesized to be transformed via oxidation to carboxylate of corresponding length (Bernhau et al. 2023). 
Once transformed to polyfluorinated carboxylates, there is a hypothesized oxidation of the beta and gamme 
carbons, leading to the formation of an enoyl carboxylate (Bernhau et al. 2023). From here, two parthways are 
hypothesized: a one-carbon oxidation and a β -oxidation pathway (Bernhau et al. 2023). In the former, a fluoride 
is predicted to be released, generating an X:3 unsaturated carboxylate followed successive oxidation to a 
perfluorinated molecule or a saturated polyfluorinated carboxylate. In the latter case, the unsaturated carboxylate 
is first oxidized to a ketone, followed by reduction to a hydroxyl and eventual oxidation to perfluorinated molecules 
(Bernhau et al. 2023). 
While discrete mechanisms of PFAS biodegradation have not been fully reported and no PFAS -CoA molecules 
have been identified, the presence of enoyl, ketone, hydroxyl groups bear a striking resemblance to non -CoA 
molecules of β-oxidation (Pavoncello et al. 2022).  
Few studies have reported expressional changes to pure cultures when exposed to PFAS except for the works of 
Bottos et al. 2020 and Mendez et al. 2022. In the former case, Gordonia NB4-1Y differentially expressed enzymes 
involved in the alkanesulfonate degradation pathway ( ssu), taurine degradation pathway (tau) and general sulfur 
starvation response (van der Ploeg et al. 2001 and Tralau et al. 2007). Bottos et al. 2020 also noted an increased 
abundance of differentially expressed low -sulfur content amino acids, a response noted in Pseudomonas 
aeruginosa (Tralau et al. 2007). These results are mirrored in the works of Mendez et al. 2022 where a strain of 
Dietzia aurantiaca could degrade 6:2 FTSA as sole sulfur source and proteomics analysis revealed differential 
production of ssu and ssu-related enzymes.  
 
Cell factory development for PFAS upcycling 
 
Synthetic biology tools for genetic engineering have expanded for what were once model organisms (Martin -
Pascual et al. 2021). With it, the tangibility of bridging PFAS remediation and cell factory development has become 
a reality. To harness the biosynthetic potential of PFAS, four key milestones must be met: PFAS import, tolerance 
to PFAS, fluoride resistance and direct-to-ACP ligation. 
 
PFAS Import 
 
Key to upcycling PFAS is the delivery of PFAS to the metabolism of the chosen cell factory. To achieve this, the 
chosen PFAS must have some property that allows for active transport into the cell. Sulfonated PFAS, such as 6:2 

 
95 
 
FTSA represent the best entry point due their structural similarity to aliphatic sulfonates and usage as delivery 
mechanism for New-to-Nature molecules (Rodriguez-Robles et al. 2024). Furthermore, harnessing 6:2 FTSA is 
advantageous following industrial usage (Poulson et al. 2005 and Gluge et al. 2020) is advantageous as these 
PFAS variants are not degraded in anaerobic environments (Zhang et al. 2016) 
Sulfonate metabolism has been well studied in Pseudomonas putida and Escherichia coli as part of the global 
sulfur starvation response (Tralau et al. 2007, van der Ploeg et al. 2001). Two major operons mediating import and 
degradation: the broad range ssu operon and tau operon (Eichhorn et al. 1999, van der Ploag et al. 1997). These 
operons involve the periplasmic binding and ATP -dependent import of sulfonates (ssuACB and tauABC) and 
mono- or -dioxygenase mediated enzymatic desulfonation (ssuED and tauD) (Eichhorn et al. 1999, van der Ploeg 
et al. 2001). The ssu system is reported to have a broader substrate specificity in both import and enzymatic 
desulfonation (Eichhorn et al. 2000). 
Reports of sulfur metabolism gene upregulation in the presence of sulfonated PFAS as sole sulfur source (Bottos 
et al. 2020 and Mendez et al. 2022) indicated that cell factories with native sulfonate uptake operons may already 
harbor the capacity for sulfonated PFAS uptake. Should this not be the case, heterogous expression of Gordonia 
NB4-1Y or Dietzia aurantiaca ssu enzymes may prove key to establishing uptake.  
 
PFAS Resistance 
 
Next, PFAS resistance needs to be address. PFAS are known for their chemical and physical resistance as well 
as their hydro and oleophobic properties (Brun et al . 2023 and Kissa 2001). As such, PFAS, particularly 
polyfluorinated sulfonates exhibit amphiphilic properties and behave like surfactants (Kissa 2001). Surfactants 
interact with the cell wall of bacteria by inserting themselves within the lipid bilayer and disrupt cell integrity leading 
to cytoplasm leakage (Sharma et al. 2022). To develop a cell fa ctory for PFAS upcycling, a choice of cell factory 
must be chosen that can withstand these harsh conditions. One such choice is Pseudomonas putida due to its 
abundance of genetic engineering tools, resistance to solvents and biodegradative capacity (Martin-Pascual et al. 
2021). Further, of the 12 pure bacterial cultures reported on by Berhanu et al. 2023 capable of transforming PFAS, 
10 are Pseudomonas (Yi et al. 2016, Kwon et al. 2014, Chetverikov et al. 2017, Kim et al. 2014, Yu et al. 2022, 
Liu et al . 20 07, Kim et al . 2012, Qiao et al . 2021,). Of these, Kim et al. 2012 reported on two species of 
Pseudomonas (oleovorans and butanovora ) capable of partial degradation and defluorination of fluorotelomer 
alcohols. Pseudomonas oleovorans was first isolated from water -oil emulsion (Lee & Chandler, 1949) and 
subsequent strain isolations have been predominantly found in surfactant associated milieu (Nandy et al. 2021, Ali 
et al. 2024). Pseudomonas oleovorans has been reported to modulate its lipid membrane profile in response to 
stressors such as antibiotics (Ali et al . 2024) and identifying the lipid membrane modulating mechanisms of 
Pseudomonas oleovorans may be key to transferring a biotechnologically relevant phenotype to a chosen cell 
factory. While other surfactant-responding phenotypes exist, such as biofilm formation, they may not be suitable 
for cell factory development. 

 
96 
 
 
Fluoride toxicity & PFAS degradation 
 
Of the numerous PFAS degradation studies where metabolites were identified, many report on the formation of a 
polyfluorinated unsaturated acid (PFUCA), the result of polyfluorinated PFAS degradation pathways (Hamid et al. 
2020 and Li et al. 2018). The formation of PFUCA implies the release of fluoride ions (Berhanu et al. 2023). Where 
PFAS upcycling is concerned, this is a problem since fluoride is cytotoxic to microbial biochemical functions 
inhibiting enzymes in the central carbon metabolism (Ma et al. 2014, Qin et al. 2006, Samygina et al. 2007 and 
Calero et al . 2022) and further degradation products of PFUCA are shorter perfluorinated carboxylates. 
Perfluorinated carboxylates are considered inert, endpoint metabolites.  To effectively upcycle PFAS, fluoride 
toxicity and PFAS degradation need to be addressed. As noted by Berhanu et al . 2023, the prevalence of 
Pseudomonas species identified as PFAS degrading organisms is likely due to their innate resistance to fluoride. 
Bacteria employ fluoride resistance t hrough fluoride export (Stockbridge & Wackett 2024) and heterologous 
expression of these antiporters, such as crcB from Pseudomonas putida (Calero et al. 2022), may prove critical. 
Alternatively, a Pseudomonas-based cell factory, such as Pseudomonas putida , could be chosen.  Next, 
preservation of non-fluorinated portion of PFAS is crucial to capturing their biosynthetic potential. While the specific 
mechanisms of PFAS degradation have yet to be elucidated through biochemical studies, the presence of FTUCA, 
sFTOH, polyfluorinated ketones (Hamid et al. 2020, Li et al. 2018 and Shaw et al. 2019) and overall PFAS chain 
shortening indicate β -oxidation is the likely mechanism leading to polyfluorinated chain shortening. FadE enzymes 
are involved in the dehydrogenation of aliphatic fatty acid during β-oxidation (Pavoncello et al. 2022 and Campbell 
and Cronan Jr 2002) and inhibition or deletion of these enzymes in the chosen cell factory background would likely 
prevent the formation of FTUCA, thereby also preventing fluoride release, and preserving the biochemically 
accessible portion of PFAS. Alternatively, inhibition of longer chain specific FadD enzymes could provide 
operational control over β-oxidation based on chain length (Thompson et al. 2020). 
 
Direct-to-ACP ligation 
 
Bacterial aliphatic fatty acid metabolism is marked by two, independent systems: fatty acid synthesis and β-
oxidation (Thompson et al. 2020, McNaught et al. 2023, Yao and Rock et al. 2018). In the former, fatty acids are 
synthesized de novo  from the condensation of one molecule of acetyl -CoA and Malonyl -CoA generating 
acetoacetyl-acyl carrier protein (ACP) (McNaught et al. 2023). Nascent fatty acids are extended, while attached to 
ACP, two carbon units at a time via transformation through β-ketoacyl-ACP, β-hydroxyl-ACP and enoyl -ACP 
(McNaught et al . 2023). On the other hand, β-oxidation is the reverse process whereby free fatty acids are 
degraded two carbon units at a time while bound to CoA (Acyl -CoA → enoyl-CoA → β-hydroxyacyl-CoA → β-
ketoacyl-CoA) (Tompson et al. 2020). 

 
97 
 
Separation of fatty acid synthesis and β-oxidation represents a roadblock for biosynthesis in cell factories. PFAS 
metabolism, regardless of starting product, converge on polyfluorinated aliphatic carboxylates (Bernhau et al . 
2023). For exogenous PFAS to be used as biosynthetic substrate, ligation to ACP is crucial to allow entry into 
secondary metabolic pathways such as polyhydroxyalkanoate or rhamnolipid production (Vicente et al . 2023, 
Chong and Li, 2017). To that end, direct-to-ACP ligation is required. Two possible routes for direct-to-ACP ligation 
include heterologous expression of mycolic acid producing enzymes such as fabD10 (Liu et al . 2013) or 
heterologous expression of the Pseudomonas aeruginosa long chain β-acetoacetyl-ACP synthase (Yuan et al. 
2012). The former, however, would require implementation of a disparate fatty acid synthesis system as fabD10 
acylates a disparate ACP (Liu et al. 2013). The latter retains some de novo fatty acid initiation (Yuan et al. 2012) 
and would make generating a fully fatty acid auxotrophic strain difficult. While not perfect, these systems allow for 
the entry of free or CoA attached fatty acids into fatty acid synthesis via ligation to ACP.  
 
Counter argument 
 
While we believe the opinions in this article are scientifically sound, there exists counter arguments from 
philosophical and logical perspectives. First, a strong argument can be made against the biosynthetic potential of 
PFAS. In simple terms, the arguments laid out here do not affect the perfluorinated parts to polyfluorinated 
sulfonates. One could argue that this, while innovative from a biochemical standpoint, is not a sustainable solution 
to global PFAS contamination as whatever metabolite produced fr om these PFAS would maintain their 
environmental pollutant properties if released to the environment. While we sympathize with these arguments, the 
first step to bridging synthetic biology and biodegradation is the import and transformation of the desired pollutant. 
One could envision a cell factory converted cell ‘sponge’ where PFAS are biomagnified and stored in recoverable 
molecules such as polyhydroxyalkanoate granules. From a biological perspective, incorporation of PFAS into fatty 
acids may be untenab le without separation of phospholipid and produced metabolite metabolisms. It is possible 
that, should direct -to-ACP ligation be achieved and PFAS exposed to fatty acid synthesis, heavily fluorinated 
phospholipid could be produced and enter membrane of a chosen cell factory. This could easily lead to a 
membrane destabilizing effect like surfactants and hamper cell factory developme nt. While possible, identifying 
and implementing membrane modulating systems or properties of bacteria such as Pseudomonas oleovorans may 
prove crucial to establishing stability. 
 
Conclusion 
 
To summarize, PFAS degradation has been studied for close to three decades. In that time, we’ve understood that 
perfluorinated molecules are poorly transformed. Structurally similar polyfluorinated substances, have, however, 
been subject to a significant body of degradation studies. Resulting studies have identified metabolites that bare a 
striking resemblance to microbial β-oxidation and enzymes involved in sulfonate degradation in Gordonia NB4-1Y 

 
98 
 
and Dietzia aurantiaca are upregulated fed polyfluorinated sulfonate as sole sulfur source. It is in the opinion of the 
authors here that PFAS, particularly polyfluorinated sulfonates can interact with bacterial metabolism through 
sulfonate uptake and fatty acid degradation. If the metabolic potential of these systems is harnessed in combination 
with direct-to-ACP ligation of fatty acids achieved, PFAS could be upcycled into New-to-Nature molecules and set 
the stage for new chemistries within cell factories. 
 
Call to action 
 
There exists a font of knowledge on known PFAS degraders such as Pseudomonas oleovorans, Pseudomonas 
butanovorans and Gordonia NB4-1Y and Dietzia aurantiaca. If this knowledge is interwoven with modern synthetic 
biology capacities, the global PFAS problem could be tackled with model organisms such as Pseudomonas putida 
and Escherichia coli. 
 
Highlights 
 
-PFAS are a broad category of polymer and non-polymer, heavily fluorinated molecules 
-Perfluorinated PFAS degradation are poorly investigated, polyfluorinated PFAS degradation has been extensively 
-PFAS upcycling requires active import, likely through ssu enzymes 
-Pseudomonas species may be innately suited to handle PFAS-based biosynthesis 
-Implementation of direct-to-ACP ligation is crucial for PFAS upcycling 
 
References 
 
Ali, M. L., Ferrieres, L., Jass, J., & Hyötyläinen, T. (2024). Metabolic Changes in Pseudomonas 
oleovorans Isolated from Contaminated Construction Material Exposed to Varied Biocide Treatments. Metabolites, 
14(6), 326. 
Barry, V., Winquist, A., & Steenland, K. (2013). Perfluorooctanoic Acid (PFOA) Exposures and Incident 
Cancers among Adults Living Near a Chemical Plant. Environmental Health Perspectives , 121(11–12), 1313–
1318.  
Berhanu, A. (2023). A review of microbial degradation of per - and polyfluoroalkyl substances (PFAS): 
Biotransformation routes and enzymes. Science of the Total Environment. 
Bottos, E. M., AL-shabib, E. Y., Shaw, D. M. J., McAmmond, B. M., Sharma, A., Suchan, D. M., Cameron, 
A. D. S., & Van Hamme, J. D. (2020). Transcriptomic response of Gordonia sp. Strain NB4-1Y when provided with 
6:2 fluorotelomer sulfonamidoalkyl betaine o r 6:2 fluorotelomer sulfonate as sole sulfur source. Biodegradation, 
31(4–6), 407–422.  

 
99 
 
Brunn, H., Arnold, G., Körner, W., Rippen, G., Steinhäuser, K. G., & Valentin, I. (2023). PFAS: Forever 
chemicals—persistent, bioaccumulative and mobile. Reviewing the status and the need for their phase out and 
remediation of contaminated sites. Environmental Sciences Europe, 35(1), 20.  
Buck, R. C., Franklin, J., Berger, U., Conder, J. M., Cousins, I. T., De Voogt, P., Jensen, A. A., Kannan, 
K., Mabury, S. A., & Van Leeuwen, S. P. (2011). Perfluoroalkyl and polyfluoroalkyl substances in the environment: 
Terminology, classification, and origins. Integrated Environmental Assessment and Management, 7(4), 513–541.  
Calero, P., Gurdo, N., & Nikel, P. I. (2022). Role of the CRCB transporter of Pseudomonas putida in the 
multi‐level stress response elicited by mineral fluoride. Environmental Microbiology, 24(11), 5082–5104.  
Campbell, J. W., & Cronan, J. E. (2002). The Enigmatic Escherichia coli fadE Gene Is yafH. Journal of 
Bacteriology, 184(13), 3759–3764.  
Chetverikov, S. P., Sharipov, D. A., Korshunova, T. Yu., & Loginov, O. N. (2017). Degradation of 
perfluorooctanyl sulfonate by strain Pseudomonas plecoglossicida 2.4-D. Applied Biochemistry and Microbiology, 
53(5), 533–538.  
Chong, H., & Li, Q. (2017). Microbial production of rhamnolipids: Opportunities, challenges and strategies. 
Microbial Cell Factories, 16(1), 137.  
Cousins, I. T., DeWitt, J. C., Glüge, J., Goldenman, G., Herzke, D., Lohmann, R., Ng, C. A., Scheringer, 
M., & Wang, Z. (2020). The high persistence of PFAS is sufficient for their management as a chemical class. 
Environmental Science: Processes & Impacts, 22(12), 2307–2312.  
Eichhorn, E., Van Der Ploeg, J. R., & Leisinger, T. (1999). Characterization of a Two -component 
Alkanesulfonate Monooxygenase from Escherichia coli. Journal of Biological Chemistry, 274(38), 26639–26646.  
Eichhorn, E., Van Der Ploeg, J. R., & Leisinger, T. (2000). Deletion Analysis of the Escherichia coli Taurine 
and Alkanesulfonate Transport Systems. Journal of Bacteriology, 182(10), 2687–2695.  
Falk, N. A. (2019). Surfactants as Antimicrobials: A Brief Overview of Microbial Interfacial Chemistry and 
Surfactant Antimicrobial Activity. Journal of Surfactants and Detergents, 22(5), 1119–1127.  
Glüge, J. (2020). An overview of the uses of per- and polyfluoroalkyl substances (PFAS). Environmental 
Science. 
Gobelius, L., Hedlund, J., Dürig, W., Tröger, R., Lilja, K., Wiberg, K., & Ahrens, L. (2018). Per - and 
Polyfluoroalkyl Substances in Swedish Groundwater and Surface Water: Implications for Environmental Quality 
Standards and Drinking Water Guidelines. Environmental Science & Technology, 52(7), 4340–4349.  
Hamid, H., Li, L. Y., & Grace, J. R. (2020). Aerobic biotransformation of fluorotelomer compounds in 
landfill leachate-sediment. Science of The Total Environment, 713, 136547.  

 
100 
 
Huang, S., & Jaffé, P. R. (2019). Defluorination of Perfluorooctanoic Acid (PFOA) and Perfluorooctane 
Sulfonate (PFOS) by Acidimicrobium sp. Strain A6. Environmental Science & Technology, 53(19), 11410–11419.  
Key, B. D., Howell, R. D., & Criddle, C. S. (1998). Defluorination of Organofluorine Sulfur Compounds by 
Pseudomonas Sp. Strain D2. Environmental Science & Technology, 32(15), 2283–2287.  
Kim, M. H., Wang, N., McDonald, T., & Chu, K. -H. (2012). Biodefluorination and biotransformation of 
fluorotelomer alcohols by two alkane ‐degrading Pseudomonas strains. Biotechnology and Bioengineering , 
109(12). 
Kwon, B. G., Lim, H. -J., Na, S. -H., Choi, B. -I., Shin, D. -S., & Chung, S. -Y. (2014). Biodegradation of 
perfluorooctanesulfonate (PFOS) as an emerging contaminant. Chemosphere, 109, 221–225.  
Li, F., Su, Q., Zhou, Z., Liao, X., Zou, J., Yuan, B., & Sun, W. (2018). Anaerobic biodegradation of 8:2 
fluorotelomer alcohol in anaerobic activated sludge: Metabolic products and pathways. Chemosphere, 200, 124–
132.  
Liu, J., Lee, L. S., Nies, L. F., Nakatsu, C. H., & Turco, R. F. (2007). Biotransformation of 8:2 Fluorotelomer 
Alcohol in Soil and by Soil Bacteria Isolates. Environmental Science & Technology, 41(23), 8024–8030.  
Liu, Z., Ioerger, T. R., Wang, F., & Sacchettini, J. C. (2013). Structures of Mycobacterium tuberculosis 
FadD10 Protein Reveal a New Type of Adenylate -forming Enzyme. Journal of Biological Chemistry , 288(25), 
18473–18483.  
Ma, H., Wu, X., Yang, M., Wang, J., Wang, J., & Wang, J. (2014). Effects of fluoride on bacterial growth 
and its gene/protein expression. Chemosphere, 100, 190–193.  
Martin-Pascual, M., Batianis, C., Bruinsma, L., Asin-Garcia, E., Garcia-Morales, L., Weusthuis, R. A., Van 
Kranenburg, R., & Martins Dos Santos, V. A. P. (2021). A navigation guide of synthetic biology tools for 
Pseudomonas putida. Biotechnology Advances, 49, 107732.  
McMahon, P. B., Tokranov, A. K., Bexfield, L. M., Lindsey, B. D., Johnson, T. D., Lombard, M. A., & 
Watson, E. (2022). Perfluoroalkyl and Polyfluoroalkyl Substances in Groundwater Used as a Source of Drinking 
Water in the Eastern United States. Environmental Science & Technology, 56(4), 2279–2288.  
McNaught, K. J., Kuatsjah, E., Zahn, M., Prates, É. T., Shao, H., Bentley, G. J., Pickford, A. R., Gruber, 
J. N., Hestmark, K. V., Jacobson, D. A., Poirier, B. C., Ling, C., San Marchi, M., Michener, W. E., Nicora, C. D., 
Sanders, J. N., Szostkiewicz, C. J ., Veličković, D., Zhou, M.  Beckham, G. T. (2023). Initiation of fatty acid 
biosynthesis in Pseudomonas putida KT2440. Metabolic Engineering, 76, 193–203.  
Mejia Avendaño, S., Zhong, G., & Liu, J. (2015). Comment on “Biodegradation of 
perfluorooctanesulfonate (PFOS) as an emerging contaminant”. Chemosphere, 138, 1037–1038.  

 
101 
 
Méndez, V., Holland, S., Bhardwaj, S., McDonald, J., Khan, S., O’Carroll, D., Pickford, R., Richards, S., 
O’Farrell, C., Coleman, N., Lee, M., & Manefield, M. J. (2022). Aerobic biotransformation of 6:2 fluorotelomer 
sulfonate by Dietzia aurantiaca J3 under sulfur-limiting conditions. Science of The Total Environment, 829, 154587.  
Murakami, M., Kuroda, K., Sato, N., Fukushi, T., Takizawa, S., & Takada, H. (2009). Groundwater 
Pollution by Perfluorinated Surfactants in Tokyo. Environmental Science & Technology, 43(10), 3480–3486.  
Nandy, S., Arora, U., Tarar, P., Viggor, S., Jõesaar, M., Kivisaar, M., & Kapley, A. (2021). Monitoring the 
growth, survival and phenol utilization of the fluorescent -tagged Pseudomonas oleovorans immobilized and free 
cells. Bioresource Technology, 338, 125568.  
Pavoncello, V., Barras, F., & Bouveret, E. (2022). Degradation of Exogenous Fatty Acids in Escherichia 
coli. Biomolecules, 12(8), 1019.  
Poulsen, P. B., Jensen, A. A., & Wallström, E. (n.d.). More environmentally friendly alternatives to PFOS-
compounds and PFOA. 
Qin, J., Chai, G., Brewer, J. M., Lovelace, L. L., & Lebioda, L. (2006). Fluoride Inhibition of Enolase: 
Crystal Structure and Thermodynamics ,. Biochemistry, 45(3), 793–800.  
Rodríguez-Robles, E., Müller, D., Künzl, T., Nemat, S. J., Edelmann, M. P., Srivastava, P., Louis, D., 
Groaz, E., Tiefenbacher, K., Roberts, T. M., Herdewijn, P., Marlière, P., & Panke, S. (2024). Rational design of a 
bacterial import system for new-to-nature molecules. Metabolic Engineering, S1096717624000715.  
Samygina, V. R., Moiseev, V. M., Rodina, E. V., Vorobyeva, N. N., Popov, A. N., Kurilova, S. A., Nazarova, 
T. I., Avaeva, S. M., & Bartunik, H. D. (2007). Reversible Inhibition of Escherichia coli Inorganic Pyrophosphatase 
by Fluoride: Trapped Catalytic Intermediates in Cryo-crystallographic Studies. Journal of Molecular Biology, 366(4), 
1305–1317.  
Sharma, P., Vaiwala, R., Parthasarathi, S., Patil, N., Verma, A., Waskar, M., Raut, J. S., Basu, J. K., & 
Ayappa, K. G. (2022). Interactions of Surfactants with the Bacterial Cell Wall and Inner Membrane: Revealing the 
Link between Aggregation and Antimicrobial Activity. Langmuir, 38(50), 15714–15728.  
Shaw, D. M. J., Munoz, G., Bottos, E. M., Duy, S. V., Sauvé, S., Liu, J., & Van Hamme, J. D. (2019). 
Degradation and defluorination of 6:2 fluorotelomer sulfonamidoalkyl betaine and 6:2 fluorotelomer sulfonate by 
Gordonia sp. Strain NB4-1Y under sulfur-limiting conditions. Science of The Total Environment, 647, 690–698.  
Stockbridge, R. B., & Wackett, L. P. (2024). The link between ancient microbial fluoride resistance 
mechanisms and bioengineering organofluorine degradation or synthesis. Nature Communications, 15(1), 4593.  
Sunderland, E. M., Hu, X. C., Dassuncao, C., Tokranov, A. K., Wagner, C. C., & Allen, J. G. (2019). A 
review of the pathways of human exposure to poly - and perfluoroalkyl substances (PFASs) and present 
understanding of health effects. Journal of Exposure Science & Environmental Epidemiology, 29(2), 131–147.  

 
102 
 
Thompson, M. G., Incha, M. R., Pearson, A. N., Schmidt, M., Sharpless, W. A., Eiben, C. B., Cruz -
Morales, P., Blake-Hedges, J. M., Liu, Y., Adams, C. A., Haushalter, R. W., Krishna, R. N., Lichtner, P., Blank, L. 
M., Mukhopadhyay, A., Deutschbauer, A. M., Shih, P. M., & Keasling, J. D. (2020). Fatty Acid and Alcohol 
Metabolism in Pseudomonas putida: Functional Analysis Using Random Barcode Transposon Sequencing. 
Applied and Environmental Microbiology, 86(21), e01665-20.  
Tralau, T., Vuilleumier, S., Thibault, C., Campbell, B. J., Hart, C. A., & Kertesz, M. A. (2007). 
Transcriptomic Analysis of the Sulfate Starvation Response of Pseudomonas aeruginosa. Journal of Bacteriology, 
189(19), 6743–6750.  
Van Der Ploeg, J., Eichhorn, E., & Leisinger, T. (2001). Sulfonate-sulfur metabolism and its regulation in 
Escherichia coli. Archives of Microbiology, 176(1–2), 1–8.  
Van Der Ploeg, J. R., Iwanicka -Nowicka, R., Kertesz, M. A., Leisinger, T., & Hryniewicz, M. M. (1997). 
Involvement of CysB and Cbl regulatory proteins in expression of the tauABCD operon and other sulfate starvation-
inducible genes in Escherichia coli. Journal of Bacteriology, 179(24), 7671–7678.  
Vicente, D., Proença, D. N., & Morais, P. V. (2023). The Role of Bacterial Polyhydroalkanoate (PHA) in a 
Sustainable Future: A Review on the Biological Diversity. International Journal of Environmental Research and 
Public Health, 20(4), 2959.  
Yao, J., & Rock, C. O. (2017). Exogenous fatty acid metabolism in bacteria. Biochimie, 141, 30–39.  
Yi, L. B., Chai, L. Y., Xie, Y., Peng, Q. J., & Peng, Q. Z. (2016). Isolation, identification, and degradation 
performance of a PFOA-degrading strain. Genetics and Molecular Research, 15(2).  
Yuan, Y., Leeds, J. A., & Meredith, T. C. (2012). Pseudomonas aeruginosa Directly Shunts β-Oxidation 
Degradation Intermediates into De Novo Fatty Acid Biosynthesis. Journal of Bacteriology, 194(19), 5185–5196.  
Zhang, S., Lu, X., Wang, N., & Buck, R. C. (2016). Biotransformation potential of 6:2 fluorotelomer 
sulfonate (6:2 FTSA) in aerobic and anaerobic sediment. Chemosphere, 154, 224–230. 
  

 
103 
 
Chapter 5: Direct and lossless delivery of exogenous fatty acids 
to fatty acid synthesis for incorporation of fluorinated fatty acyl 
compounds 
Garret W. O'Connell1, Alexandre Perrin2, Pablo Ivan Nikel1  
   1Novo Nordisk Center for Biosustainability, Systems Environmental Microbiology group  
2Ecole Polytechnique, Centre de mathématiques appliquées 
Fatty acid metabolism is a crucial part to bacterial viability and fitness. In bacteria, and Pseudomonas putida in 
particular, fatty acid metabolism is divided into two major categories: fatty acid synthesis and degradation. 
Unidirectional in their respective process, fatty acid metabolism represents an opportunity to upcycle PFAS as 
polyfluorinated PFAS degradation  bears the hallmarks of fatty acid degradation. To bridge the PFAS -fatty acid 
metabolism gap, two major barriers need to be overcome in P. putida . Inhibition of fatty acid degradation to 
preserve the biosynthetic potential of polyfluorinated carboxylates and direct-to-ACP ligation, allowing for the entry 
into fatty acid synthesis of exogenous polyfluorinated carboxylates. To achieve this, two metabolic rearrangements 
were undertaken. First, fadA candidates in P. putida KT2440 were disrupted and screened for growth on two to 
nine carbon fatty acids. The fadA step of fatty acid degradation was chosen to prevent fatty -CoA chain length 
shortening while maintaining CoA ligation activity to exogenous fatty acids. Only when pcaf-II, bktB and fadA were 
disrupted was P. putida unable to grow on five to nine carbon fatty acids. Next, we attempted to re-route fatty acid 
synthesis to start from eight carbon fatty acids instead of the endogenous two by disrupting fatty acid initiation and 
enabling fatty acid initiation from eight carbon fatty acids instead of two. Disruption of all native fatty acid initiations 
enzymes in P. putida (fabH, PP_4545 and mtbM) with concomitant functional replacement with an octanoyl-CoA-
preferential fatty acid initiator from P. aeurginosa (PA3286) proved problematic. Instead, PA3286 was constitutively 
expressed from the pSEVA2313 and C13 substitution monitored by total methyl esterification and GC -MS when 
C13 labeled octanoate fed. When β-oxidation was inhibited, only single and unsubstituted C12, C14 and C16 fatty 
acids were identified, a stark contrast 3+ substitutions in P. putida fatty acids suggesting the potential presence of 
a cryptic octanoate-preferential fatty acid initiator in P. putida. Interestingly, expression of PA3286 did not lead to 
an increase in single substitution in C12, C14 and C16 fatty acids but an increase in unsubstituted fractions. 
Together, these results paint an inconclusive metabolic picture. While β-oxidation can confidently be considered 
inhibited, the question of the necessity PA3286 remains unclear. Moving forward, total disruption of fatty acid 
initiation will be required to appropriately assess direct-to-ACP ligation of medium chain fatty acids. If successful, 
these would set the stage for a metabolic ‘corridor’ for fatty acids, and PFAS, directly into fatty acid metabolism.  

 
104 
 
Introduction 
Fatty acid metabolism is a core part of a bacteria’s viability and fitness (Lopez-Lara and Soto, 2018 and Diomande 
et al. 2015). While underpinning membrane structure, fatty acid metabolism is also utilized for energy production 
and storage (Lu et al. 2009 and Gasser et al. 2009), biological signaling (Prieschl and Baumruker, 2000 and 
Kaushik et al., 2022), protein modification (Espinosa -Urgel, 2016) and secondary metabolite production (Chong 
and Li, 2017). For examples, when carbon sources are scarce, bact eria can degrade exogenous fatty acids 
releasing acetyl-CoA feeding carbon metabolism (Wang et al. 2024 and Jimenez-Diax et al. 2017) and energetic 
needs while when carbon sources are abundance, bacteria can produce carbon storage molecules such as 
polyhdroxyalkanoates (Lu et al. 2009 and Gasser et al. 2009). 
Fatty acids metabolism is a crucial process involving both synthesis and degradation (Jimenez -Diaz et al. 2017). 
Bacteria synthesize fatty acids de novo from acetyl-CoA and malonyl-acyl carrier protein (ACP) molecules in a 4-
step process called fatty acid synthesis. First, de novo fatty acids are typically initiated with the condensation of 
acetyl-CoA and malonyl-ACP through the activity of β-ketoacyl-ACP ligases (FabH; Tsay et al. 1992 and Boram et 
al. 2023). In Pseudomonas putida, malonyl-ACP can be decarboxylated by mtbM, a malonyl-ACP decarboxylase 
generating acetyl-ACP, an alternative fatty acid initiator (McNaught et al. 2023). Once initiated, nascent β-ketoacyl-
ACP molecules are first reduced to β-hydroxy-ACP by a β-ketoacyl-ACP reductase (FabG; Zhang et al. 2003). 
Next, the generated β-hydroxyacyl-ACP is reduced to trans-2-enoyl-ACP through the activity of a β-hydroxacyl-
ACP dehydratase (FabA/Z; Heat and Rock, 1996). Finally, the trans-2-enoyl-ACP is reduced by a trans-2-enoyl-
ACP reductase (FabVI; Heath and Rock 1995 and Bergler et al. 1996) generating a saturated acyl-ACP. Extension 
of the nascent fatty acid is achieved through the activity of β-ketoacyl-ACP ligases (FabF/B) generating a β -
ketoacyl-ACP molecules extended by two carbon units.  
Fatty acid degradation, often referred to as β-oxidation, is the reverse of this cycle whereby exogenous free fatty 
acids are degraded to release acetyl -CoA (Jimenez-Diaz et al. 2017). The notable difference between fatty acid 
synthesis and β-oxidation is the ligation to acetyl -CoA instead of ACP. First, free fatty acids are ligated to CoA 
through the activity of fatty acid CoA-ligase (FadD; Kamenda and Nunn, 1981). Fatty acyl-CoA molecules are then 
dehydrogenated by an acyl-CoA dehydrogenase (FadE; Campbell and Cronan Jr, 2002) to a trans-2-enoyl CoA 
followed by a hydroxylation generating a β-hydroxyacyl-CoA through the activity of an FadB; the activity of FadB 
also reduces the β-hydroxyl-CoA to a β-ketoacyl-CoA (Yang et al. 1988). Finally, a β-ketoacyl-CoA thiolase (FadA) 
will cleave one molecule of acetyl-CoA from the β-ketoacyl-CoA, shortening the chain length by two carbon units 
and regenerating the acyl-CoA molecule (Clomburg et al. 2012). 
Fatty acid metabolism is unidirectional (Jimenez-Dias et al. 2017), once ligated to ACP or CoA, fatty acyl molecules 
are destined for synthesis or degradation respectively which poses a significant barrier to directing exogenous fatty 
acids towards fatty acid synthesis by-products. In order to overcome this and potentially utilize PFAS as exogenous 
fatty acid for production of novel metabolites, two major milestones need to be met. First, β-oxidation needs to be 
inhibited. PFAS degradation studies over the past decade have demonstrated that polyfluorinated alkyl acids are 

 
105 
 
likely interacting with bacteria β-oxidation due to the presence of polyfluorinated ketones, enoyl acids and C2 -
shortened acids (Bernhau et al. 2023, Qiao et al. 2021 and Li et al. 2018). Next, entry of exogenous fatty acids into 
fatty acid synthesis will require direct -to-ACP ligation, something which could be attained with the octanoyl -CoA 
preferring β-ketoacyl-ACP synthase from P. aeruginosa PAO1 (PA3286; Yuan et al , 2012a, b). Should both 
milestones be met, P. putida could be used as chassis for delivery of polyfluorinated fatty acids directly to fatty acid 
metabolism. 
  
  

 
106 
 
Results and Discussion 
Investigating fatty acid degradation in P. putida KT2440 through combinatorial fadA variant disruption 
Fatty acid metabolism in Pseudomonas putida is crucial for energy homeostasis (Lopez-Lara and Soto, 2018 and 
Diomande et al. 2015), secondary metabolite production (Chong and Li, 2017), energy storage (Lu et al. 2009 and 
Gasser et al. 2009). Within the metabolic bounds of P. putida, two, cyclic, metabolisms govern fatty acid and 
synthesis: fatty acid synthesis and β-oxidation (Figure 1.). The former involves de novo fatty acid synthesis from 
acetyl-CoA and malonyl-ACP with subsequent extension via addition of two carbon units with from malonyl -CoA 
per iteration of the fatty acid synthesis cycle (McNaught et al. 2023). The later involves uptake and CoA ligation of 
free fatty acids (aliphatic carboxylates with no l igation and sequential removal of two carbon units per iteration of 
the β-oxidation cycle (Thompson et al. 2020). 
With the goal of preserving the biosynthetic potential of polyfluorinated carboxylates, β-oxidation was selectively 
disrupted with pSNW2 suicide vectors (Fig 2., A) and a combinatorial mini-library of β-oxidation inhibited variants 
screened for growth on two to nine carbon free fatty acids as sole carbon source. For homogeneity between variant 
screenings, total carbon fed was maintained to 40 mM (e.g. 20 mM aceta te compared to 5 mM octanoate). 
Resulting growth curves were analyze with QurvE (Wirth et al. 2023) and resulting growth parameters (growth rate, 
lag time and growth yield) analyzed with a fitness calculator to return Fscores. 
β-oxidation involves four steps prior to the removal of a two-carbon unit from degraded fatty acids. First, free fatty 
acids are ligated to CoA via the activity of FadD enzymes to allow entry into β-oxidation (Fig 2., B). Next, CoA -
attached fatty acids are reduced via FadE enzymes across the carbons of position 2 and 3 forming a trans-2-enoyl-
CoA molecule (Fig 2., B). Afterwards, FabB  enzymes will hydroxylate the carbon 3 position to a β-hydroxy-CoA 
molecule followed by oxidating the hydroxyl group to form a β-ketoacyl-CoA molecule (Fig 2., B). Finally, FadA 
enzymes can cleave a single acetyl -CoA molecule from the β-ketoacyl-CoA molecule, regenerating an acyl-CoA 
molecule. 
To preserve the biosynthetic potential of potentially delivered polyfluorinated carboxylates interacting with the 
metabolism of P. putida, partial inhibition of β-oxidation is required. To that end, we chose to disrupt fadA enzymes 
as they finalize the β-oxidation cycle and are fatty acid length-selective (Thompson et al. 2020). Meaning, medium 
to long chain fatty acid degradation could be disrupted without affecting short chain fatty acid metabolism. To 
identify fadA candidates in P. putida, an exhaustive search of fatty acid metabolic models from KEEG and a 
literature review (Thompson et al . 2020) were performed and three variants identified: pcaf-II, bktB and fadA 
(PP_2137, 3754 and 2051).  
Approximately 192 growth curves were generated from the challenging of eight fatty acids sources to eight fadA 
disrupted P. putida variants and wild-type P. putida. Fitness scores (Fscore) matrix are given in the supplementary 
(Table S1.) No major variations were observed in Fscores across all variants grown on two to four carbon long fatty 
acids ( Fig 2. , C; F score 0.57-0.89). All variants, including P. putida , were drastically inhibited from growing on 

 
107 
 
pentanoate, a five-carbon unit fatty acid ( Fig 3., C; Fscore <0.39). The remaining variants and wild -type P. putida 
were not drastically impacted in growth on six to nine carbon fatty acids with the following notable exceptions. 
Variant Δpacf-II bktB and ΔpcaF-II fadA were impacted six to nine carbon fatty acids (Fscore = 0.18, 0.46, 0.52 and 
0.54 respectively) and nine carbon fatty acids (Fscore = 0.19) respectively. When all three chosen fadA disruptions 
were preformed, the resulting variant could not grow on six to nine carbon fatty acids (Fscore=0). 
The reason for the substantial growth impact on pentanoate is puzzling. Pentanoate (valerate) is a known 
metabolite of P. putida (Thompson et al. 2020) and degradation produces both propionyl - and acetyl-CoA, non-
toxic metabolites to P. putida (Fig 2. C; Thompson et al. 2020). Furthermore, the alcohol of pentanoate, pentanol, 
has been reported to support growth of P. putida and variants with alcohol dehydrogenase disruption (Lu et al. 
2023). One possible explanation for the lack of growth on pentanoate may be in the formulation of the media. While 
pentanoate is reported in the works here-in, pentanoic acid was used to formulate media. DeBont media contains 
3.88 g/L K2HPO4 (22.2 mM) and 1.63 g/L NaH2PO4 (13.58 mM) (Hartmans et al. 1989) and 8 mM of pentanoic acid 
was used as final concentration to in pentanote media. Excessive media acidification is not expected during media 
preparation, however, added strain of pentanoic acid to metabolic-respiration dependent media acidification could 
have generated a hostil e environment for P. putida. Addition of a further buffering element such as HEPES or 
MOPS to pentanoate media would alleviate this issue. 
When Thompson et al. 2020 and colleagues individually disrupted each all β-ketoacyl-thioesterases in P. puitda 
KT2440, they found that disruption of pcaf-II had the largest impact of fatty acid metabolism but disruption of bktB 
or fadA had little effect. When bktB and fadA were disrupted, in addition to pcaF-II, growth on hexanoate and 
nonanoate were moderately affected compared to KT2440 F scores respectively (Fscore = 0.18 vs 0.50 and F score = 
0.19 vs 0.73 respectively). Notably, Thompson et al. 2020 repor ted growth defects on variants bktB and pcaf-II 
grown on butyrate and hexanoate whereas here, variants showed little to no difference when compared with 
KT2440 (Fscore = 0.77 and 0.82, 0.49 and 0.7 vs F score 0.72 and 0.50). However, when bktB and pcaf-II were both 
disrupted, variants here -in were moderately inhibited only when grown on hexanoate (F score 0.18 vs 0.50). 
Disruption of fadA has not been reported to have any major growth impacts on fatty acids and 1,4-butandiol growth, 
a short chain fatty diol (Thompson et al. 2020 and Li et al. 2020) and therefor we propose that fadA acts primarily 
on the upper end of medium chain fatty acids (9+ carbon units). Only when pcaF-II, bktB and fadA were disrupted 
was P. putida unable to grow on six to nine carbon fatty acids (Fscore = 0) suggesting that in order to disrupt medium 
chain fatty acid degradation, all three need to be disrupted. 
Integrating direct-to-ACP ligation towards shunting polyfluorinated carboxylates 
On the other end of the fatty acid metabolism spectrum exists fatty acid synthesis. Much like β-oxidation, fatty acid 
synthesis is a cyclic metabolism where fatty acids are extended two carbon units per cycle iteration but is initiated 
by the condensation of malonyl-ACP and acetyl-CoA (Jimenez-Dias et al. 2017). In P. putida, fatty acid metabolism 
can also be initiated through malonyl -ACP decarboxylation leading to the formation of acetyl -ACP as initiator 
(McNaught et al. 2023). 

 
108 
 
Should polyfluorinated fatty acids be delivered to the metabolism of P. putida and β-oxidation inhibited, enabling a 
shunt of free fatty acids directly into fatty acid synthesis is required to make use of free fatty acids. Β-ketoacyl-ACP 
ligases (e.g FabH) start fatty acid synthesis cycle with short chain fatty acids (malonate and pr opionate; Tsay et 
al. 1992 and Boram et al. 2023). To that end, we chose to express a heterologous medium chain β-ketoacyl-ACP 
ligases to potentially shunt eight carbon fatty acids directly into fatty acid synthesis (Yuan et al. 2012a, b). Further, 
disruption of all fatty acid synthesis initiation enzymes would render P. putida dependent on exogenous medium 
chain fatty acids and further confirming direct-to-ACP ligation. 
To achieve direct-to-ACP ligation, we first attempted to disrupt all potential fatty acid synthesis initiators in P. puitda 
of which there are three: fabH (PP_4379), PP_4545 and mtbM (PP_0262) with the concomitant expression of 
PA3286, an octanoyl -CoA preferential β-ketoacyl-ACP ligase. The later fatty acid initiator would be functionally 
replaced. The former two fatty acid initiators were successfully disrupted in P. putida, however disruption of mtbM 
proved problematic. To functionally replace mtbM with PA3286, pSNW2 vectors harboring PA3286 were flanked 
with flanking regions up and downstream of mtbM varying between 500 and 700 base pairs (bp). Furthermore, 
pSNW2 vectors were generated to functionally replace mtbM in line with mtbM, in the reverse complement direction 
of mtbM, replacement with PA3286 with ATG instead of GTG start codon and replacement with PA3286 with 
expression driven by the constitutive pEM7 promoter (Fig S1.; A-F). None of these pSNW2 vectors were successful 
in functionally replacing mtbM in strains with fabH and PP_4545 disrupted. Instead PA3286 was expressed from 
the pSEVA2313 vector with expression driven by the pEM7 promoter (Fig 3., A). 
To confirm if plasmid -based expression of PA3286 could ligate medium chain fatty acids directly into fatty acid 
synthesis, C13 labeled (position 1) octanoate was fed to wild -type and disrupted P. puitda strains with disruption 
of fabH and PP_4545. Total fatty acid content of each strain was methyl esterified and analyzed with GC-MS (Fig 
3., C). Resulting fractions of C13 substitution number per fatty acid identified were compared. Should octanoate 
be labelled and β-oxidation completely halted, each fatty acid should contain zero or one C13 substitution if PA3286 
is expressed.  
In total, 9 fatty acids were identified: hexanoate with one double bond (C6:1), octanoate (C8:1) with one double 
bond, dodecanoate (C12), tetradecanoate (C14), hexadecanoate with (C16:1) and without (C16) a double bond, 
heptadecanoate (C17) and octadecenoate (C18). For the purposes of this analysis, only C8:1, C12, C14 and C16 
were considered. 
Expectedly, when C13 labelled octanoate was fed, the vast majority of C8:1 analyzed fatty acids contained a single 
C13 substitution across all tested strains (85%). This is likely the result of intracellular 13C labeled octanoate not 
metabolized or supernatant contamination. When C12, C14 and C16 fatty acids were analyzed, P. putida KT2440 
could, unsurprisingly, degraded and integrate more than one C13 carbon into its nascent fatty acids leading to >1 
C13 substitution in resultant fatty acids (Fig 3., C; C12, C14 and C16). With the labeled carbon in position one of 
octanoate, only a single cycle of β-oxidation (which is intact in KT2440), would yield C13 labeled acetyl -CoA for 
fatty acid synthesis. 

 
109 
 
When pcaF-II, bktB and fadA enzymes were disrupted (PBF strain), no analyzed fatty acids contained more than 
one 13C substitution was identified with the exception of a small percentage substitution in C14 fatty acids (~15 %) 
containing two substitutions. Mirroring these, further disruption of fabH and PP_4545 (strain 355) led to a higher 
proportion of unsubstituted in C12, C14 and C16 fatty acids when compared to PBF strains (30 -36% in 355 
compared to 17-23% in PBF). Expression of PA3286 had little impact on the distribution of C13 substitution patterns 
in KT2440 and 355 with resulting fractions mirroring those of KT2440 without heterologous expression of PA3286. 
The largest difference in fraction pattern came when PA3286 was expressed in a PBF background, the fraction of 
unsubstituted C12, C14 and C16 fatty acids increased ~36% when compared the non-expressing strains. 
The BRENDA database of has 113 entries of enzyme -catalyzed reactions containing acyl -CoA, 3-hydroxyacyl-
CoA, 3-oxoacyl-CoA or trans-2-enoyl-CoA as substrate or product of which two generate acetyl-CoA: EC 2.3.1.16 
and EC 2.3.1.180 (Table SX). The former is the final step of β-oxidation where a β-hydroxyacyl-CoA is shortened 
generating an acyl -CoA and acetyl -CoA molecule. The latter reaction is the condensation of acetyl -CoA and 
malonyl-ACP to acetoacetyl-ACP, the first step to fatty acid synthesis. To our k nowledge, there are no possible 
reactions in P. putida which could explain the similarity between KT2440 and 355 13C proportions, however, a 
process addition might clarify and contaminating issues. Following biomass collection for 13C substitution 
quantification, an additional octanoate -only media test could be included to ensure the identity of strain 
backgrounds (PBF and 355 vs KT2440). 
At the inception of this chapter, the goal was to disrupt all known fatty acid initiators and replace their activity with 
that of the octanoyl -CoA specific β-ketoacyl ligase. Immediately, the high proportion of single 13C substitutions 
among analyzed fatty-acyl esters found in β-oxidation and further fatty acid initiator disrupted strains indicate an 
innate mechanism in P. putida to C8 fatty acid shunting into fatty acid synthesis. The drastic increase in un -
substituted fatty-acyl esters identified in PBF e xpressing PA3286 can be explained by the acetyl -CoA activity of 
PA3286 (Yuan et al. 2012) but the high proportion of single substitutions among PA3286 -non expressing strains 
cannot be. Overlooked during experimental design, McNaught and colleagues reported on PP_4545 having 
octanoyl-CoA specific activity and little or no acetyl -CoA specific activity. Evidence suggests that PP_4545 in P. 
putida is in fact a homolog to PA3286 from P. aeruginosa due to a 85% protein sequence identity ( Fig S2.) and 
the results supported by McNaught et al. 2023. While this would certainly explain the high proportion of single 
substitutions in PBF strains, it doesn’t explain the more than 70% proportion of single 13C substitutions in C12-16 
fatty-acyl esters (Fig 3., C). These results seem to suggest another, as of yet identified fatty acid shunting 
mechanism if no fault is found in the analytical process. 
Moving forward, the first step to establishing a strain of P. putida capable of utilizing medium chain fatty acids as 
sole fatty acid initiators is the total disruption of all fatty acid initiators P. putida. PP_4379 ( fabH) and PP_4545 
have already been successfully disrupted and further attempts to disrupt mtbM could be attempted with CRISPR 
counter-selection tools (Wirth et al. 2019) with concomitant expression of fabH, PP_4545 or mtbM. Should those 
attempts prove unsuccessful, regulation of expression in P. putida could be controlled by rhaP BAD (Jeske and 

 
110 
 
Altenbuchner 2010) and XylS/Pm (Zwick et al. 2013) expression systems. The Xyl-Pm system has been shown to 
be titratable making it an ideal candidate to control expression levels of fatty acid initiators (Volke et al. 2020).  
  

 
111 
 
Conclusion 
The challenge of upcycling PFAS into novel fluorinated fatty -acid derived products requires overcoming two 
challenges: preservation of biosynthetic potential and Direct -to-ACP ligation. In this work, we were successful in 
halting β-oxidation in P. putida, the key predicted mechanism depleting the biosynthetic potential of PFAS. Any 
intracellular PFAS interacting fatty acid metabolism should be unable to complete an entire β-oxidation due to 
disruption to fadA, bktB and pcaf-II cycle opening the door for Dir ect-to-ACP ligation. Enabling this, however, 
proved confounding. While fatty acids are typically initiated from acetyl-CoA and malonyl-ACP, P. putida seems to 
shunt octanoyl-CoA molecules in the absence of endogenous or heterologous octanoyl-CoA accepting β-ketoacyl 
ligase suggesting an as of yet determined shunting mechanism. These results raise the question, is a heterologous 
mechanism for Direct-to-ACP ligation needed? Contradictorily, if shunting were to occur solely due to PA3286 or 
PP_4545, we would e xpect a total absence of 13C labeled fatty acids in strains with inhibited β-oxidation or 
heterologous expression. Something not observed in our 13C labeled experiment. If octanoate were labelled in odd, 
even or all position, we could elucidate potential specific mechanisms of fatty acyl modification such as cryptic C1 
or C2 modifications to fatty acid derived CoA or ACP variants. Looking to the futu re, efforts should be redirected 
to take advantage of the endogenous octanoyl -CoA β-ketoacyl ligase, PP_4545,  instead of heterologous 
expression of PA3286. Disruption of fabH and mtbM should render P. putida an octanoate auxotroph and achieve 
the goals set out at the onset of this work. Following this, a biosynthetic apparatus could be connected and fatty 
acyl to product translation evaluated. 
  

 
112 
 
 
 
 
Figure 1. Simplified metabolic map of fatty acid metabolism in Pseudomonas putida. Solid arrows indicate putative 
reactions and gene names correspond to P. putida PP numbers as follows: fabH – PP_4379, madB – PP_0262, 
fabB – PP_4175, fabF – PP_1916, fabG – PP_1914, fabA – PP_4174, fabZ – PP_1602, fabV – PP_4635, fadB – 
PP_2163, fadE – PP_1893, fadA – PP_2051 and fadD – PP_4549-50.  
  


 
113 
 
 
 
Figure 2. Fatty acid degradation (β-oxidation) inhibition in Pseudomonas putida. A) Strategy to inhibit β-oxidation 
in Pseudomonas putida. B) Metabolic map of β-oxidation in P. putida. Solid arrows indicate putative reactions and 
gene names correspond to P. putida PP numbers as follows: fadE – PP_1893, fadB – 2163, fadA – PP_2051 and 
fadD – PP_4549-50. C) Fitness of P. putida and β-oxidation impacted variants. Fitness scores were calculated 
with the Fitness Score calculator with weights of 0.3, 0.6 and 0.1 for lag time, growth rate and maximum growth 
yield. A full matrix of growth parameters can be found in the supplementary materials. 
  


 
114 
 
 
 
Figure 3. Direct-to-ACP ligation in Pseudomonas putida. A) Strategy for direct -to-ACP ligation in Pseudomonas 
putida. In a P. putida background with fabH and mtbM disrupted where possible, PA3286 was constitutively 
expressed from a plasmid and cultured in C13 labelled octanoate. Biomass was collected and fatty acids esterified 
prior to GC-MS analysis. B) Metabolic map intended fatty acid synthesis and direct -to-ACP ligation. Solid arrows 
indicate putative reactions and red cross indicate intended inhibited reactions with genetic modifications. Dark 
green gene names indicate heterologous genes expressed e nzymes from Pseudomonas aeruginosa PAO1 and 
black gene names correspond t o P. putida PP numbers as follows: fabH – PP_4379, madB – PP_0260, fabB – 
PP_4175, fabF – PP_1916, fabG – PP_1914, fabA – PP_4174, fabZ – PP_1602 and fabV – PP_4635. 
 
 
 


 
115 
 
References 
Bergler, H., Fuchsbichler, S., Hogenauer, G., & Turnowsky, F. (1996). The Enoyl -[Acyl-Carrier-Protein] 
Reductase (FabI) of Escherichia coli, which Catalyzes a Key Regulatory Step in Fatty Acid Biosynthesis, Accepts 
NADH and NADPH as Cofactors and is Inhibi ted by Palmitoyl -CoA. European Journal of Biochemistry , 242(3), 
689–694.  
Berhanu, A., Mutanda, I., Taolin, J., Qaria, M. A., Yang, B., & Zhu, D. (2023). A review of microbial 
degradation of per- and polyfluoroalkyl substances (PFAS): Biotransformation routes and enzymes. Science of the 
Total Environment, 859, 160010.  
Boram, T. J., Benjamin, A. B., Silva, A., Stunkard, L. M., Stewart, T. A., Adams, T. J., Craft, N. A., 
Velázquez-Marrero, K. G., Ling, J., Nice, J. N., & Lohman, J. R. (2023). Activity of Fatty Acid Biosynthesis Initiating 
Ketosynthase FabH with Acetyl/Malonyl-oxa/aza(dethia)CoAs. ACS Chemical Biology, 18(1), 49–58.  
Campbell, J. W., & Cronan, J. E. (2002). The Enigmatic Escherichia coli fadE Gene Is yafH.  Journal of 
Bacteriology, 184(13), 3759–3764.  
Clomburg, J. M., Vick, J. E., Blankschien, M. D., Rodríguez-Moyá, M., & Gonzalez, R. (2012). A Synthetic 
Biology Approach to Engineer a Functional Reversal of the β-Oxidation Cycle. ACS Synthetic Biology, 1(11), 541–
554.  
Diomandé, S. E., Nguyen-The, C., Guinebretière, M.-H., Broussolle, V., & Brillard, J. (2015). Role of fatty 
acids in Bacillus environmental adaptation. Frontiers in Microbiology, 6.  
Gasser, I., Muller, H., & Berg, G. (2009). Ecology and characterization of polyhydroxyalkanoate-producing 
microorganisms on and in plants. FEMS Microbiology Ecology, 70(1), 142–150.  
Heath, R. J., & Rock, C. O. (1995). Enoyl-Acyl Carrier Protein Reductase (fabI) Plays a Determinant Role 
in Completing Cycles of Fatty Acid Elongation in Escherichia coli. Journal of Biological Chemistry, 270(44), 26538–
26542.  
Heath, R. J., & Rock, C. O. (1996). Roles of the FabA and FabZ β-Hydroxyacyl-Acyl Carrier Protein 
Dehydratases in Escherichia coli Fatty Acid Biosynthesis. Journal of Biological Chemistry, 271(44), 27795–27801.  
Heinrich, P., Köhler, C., Ellmann, L., Kuerner, P., Spang, R., Oefner, P. J., & Dettmer, K. (2018). 
Correcting for natural isotope abundance and tracer impurity in MS-, MS/MS- and high-resolution-multiple-tracer-
data from stable isotope labeling experiments with IsoCorrectoR. Scientific Reports, 8(1).  
Jeske, M., & Altenbuchner, J. (2009). The Escherichia coli rhamnose promoter rhaP BAD is in 
Pseudomonas putida KT2440 independent of Crp –cAMP activation.  Applied Microbiology and 
Biotechnology, 85(6), 1923–1933. 

 
116 
 
Jimenez-Diaz, L., Caballero, A., & Segura, A. (2017). Pathways for the Degradation of Fatty Acids in 
Bacteria. Aerobic Utilization of Hydrocarbons, Oils and Lipids, 1–23.  
Kameda K;Nunn WD. (2024). Purification and characterization of acyl coenzyme A synthetase from 
Escherichia coli. The Journal of Biological Chemistry, 256(11).  
Kaushik, S., He, H., & Dalbey, R. E. (2022). Bacterial Signal Peptides - Navigating the Journey of 
Proteins. Frontiers in Physiology, 13.  
Li, F., Su, Q., Zhou, Z., Liao, X., Zou, J., Yuan, B., & Sun, W. (2018). Anaerobic biodegradation of 8:2 
fluorotelomer alcohol in anaerobic activated sludge: Metabolic products and pathways.  Chemosphere, 200, 124–
132.  
López-Lara, I. M., & Soto, M. J. (2018). Fatty Acid Synthesis and Regulation. Springer EBooks, 1–17.  
Lu, C., Christos Batianis, Edward Ofori Akwafo, Wijffels, R. H., Santos, & Weusthuis, R. A. (2021). When 
metabolic prowess is too much of a good thing: how carbon catabolite repression and metabolic versatility impede 
production of esterified α,ω-diols in Pseudomonas putida KT2440. Biotechnology for Biofuels, 14(1).  
Lu, C., Edward Ofori Akwafo, Wijffels, R. H., Santos, & Weusthuis, R. A. (2023). Metabolic engineering 
of Pseudomonas putida KT2440 for medium -chain-length fatty alcohol and ester production from fatty 
acids. Metabolic Engineering, 75, 110–118.  
Lu, C., Ramalho, T. P., Markus M.M. Bisschops, Wijffels, R. H., Santos, & Weusthuis, R. A. (2023). 
Crossing bacterial boundaries: The carbon catabolite repression system Crc-Hfq of Pseudomonas putida KT2440 
as a tool to control translation in E. coli. New Biotechnology, 77, 20–29.  
Lu, J., Tappel, R. C., & Nomura, C. T. (2009). Mini -Review: Biosynthesis of 
Poly(hydroxyalkanoates). Polymer Reviews, 49(3), 226–248.  
McNaught, K. J., Kuatsjah, E., Zahn, M., Prates, É. T., Shao, H., Bentley, G. J., Pickford, A. R., Gruber, 
J. N., Hestmark, K., Jacobson, D., Poirier, B. C., Chen, L., Myrsini San Marchi, Michener, W. E., Nicora, C., 
Sanders, J. N., Szostkiewicz, C. J., Dušan Veličković, Zhou, M., & Nathalie Munoz Munoz. (2023). Initiation of fatty 
acid biosynthesis in Pseudomonas putida KT2440. Metabolic Engineering, 76, 193–203.  
Prieschl, E. E., & Baumruker, T. (2000). Sphingolipids: second messengers, mediators and raft 
constituents in signaling. Immunology Today, 21(11), 555–560.  
Qiao, W., Miao, J., Jiang, H., & Yang, Q. (2021). Degradation and effect of 6:2 fluorotelomer alcohol in 
aerobic composting of sludge. Biodegradation, 32(1), 99–112.  
S. Hartmans, Smits, J. P., van, F. Volkering, & de, M. (1989). Metabolism of Styrene Oxide and 2 -
Phenylethanol in the Styrene -Degrading Xanthobacter Strain 124X.  Applied and Environmental 
Microbiology, 55(11), 2850–2855.  

 
117 
 
Shrestha, S., Awasthi, D., Chen, Y., Gin, J., Petzold, C. J., Adams, P. D., Simmons, B. A., & Singer, S. 
W. (2023). Simultaneous carbon catabolite repression governs sugar and aromatic co-utilization in Pseudomonas 
putida M2. Applied and Environmental Microbiology, 89(10).  
Thompson, M. G., Incha, M. R., Pearson, A. W., Schmidt, M., Sharpless, W. A., Eiben, C. B., Cruz -
Morales, P., Blake-Hedges, J. M., Liu, Y., Adams, C. A., Haushalter, R. C., Krishna, R. N., Lichtner, P., Blank, L. 
M., Mukhopadhyay, A., Deutschbauer, A. M., Shih, P. M., & Keasling, J. D. (2020). Fatty Acid and Alcohol 
Metabolism in Pseudomonas putida: Functional Analysis Using Random Barcode Transposon 
Sequencing. Applied Environmental Microbiology, 86(21).  
Tsay J. T., Oh W., Larson T. J., Jackowski S., Rock C. O. (1992). Isolation and characterization of the 
beta-ketoacyl-acyl carrier protein synthase III gene (fabH) from Escherichia coli K -12. The Journal of Biological 
Chemistry, 267(10).  
Volke, D. C., Turlin, J., Mol, V., & Nikel, P. I. (2020). Physical decoupling of XylS/ Pm regulatory elements 
and conditional proteolysis enable precise control of gene expression in Pseudomonas putida.  Microbial 
Biotechnology, 13(1), 222–232.  
Volke, D. C., Wirth, N. T., & Nikel, P. (2021). Rapid Genome Engineering of Pseudomonas Assisted by 
Fluorescent Markers and Tractable Curing of Plasmids. BIO-PROTOCOL, 11(4).  
Wang, Z., Hou, X., Shang, G., Deng, G., Luo, K., & Peng, M. (2024). Exploring Fatty Acid β-Oxidation 
Pathways in Bacteria: From General Mechanisms to DSF Signaling and Pathogenicity in Xanthomonas.  Current 
Microbiology, 81(10).  
Wirth, N. T., Funk, J., Donati, S., & Nikel, P. I. (2023). QurvE: user -friendly software for the analysis of 
biological growth and fluorescence data. Nature Protocols, 18(8), 2401–2403. 
Wirth, N. T., Kozaeva, E., & Nikel, P. I. (2020). Accelerated genome engineering of Pseudomonas putida 
by I‐ Sce I―mediated recombination and CRISPR ‐Cas9 counterselection. Microbial Biotechnology, 13(1), 233–
249.  
Yang, S. Y., Li, J. M., He, X. Y., Cosloy, S. D., & Schulz, H. (1988). Evidence that the fadB gene of the 
fadAB operon of Escherichia coli encodes 3-hydroxyacyl-coenzyme A (CoA) epimerase, delta 3-cis-delta 2-trans-
enoyl-CoA isomerase, and enoyl -CoA hydrat ase in addition to 3 -hydroxyacyl-CoA dehydrogenase.  Journal of 
Bacteriology, 170(6), 2543–2548. 
Yuan, Y., Leeds, J. A., & Meredith, T. C. (2012). Pseudomonas aeruginosa Directly Shunts β-Oxidation 
Degradation Intermediates into De Novo Fatty Acid Biosynthesis. Journal of Bacteriology, 194(19), 5185–5196.  

 
118 
 
Yuan, Y., Sachdeva, M., Leeds, J. A., & Meredith, T. C. (2012). Fatty Acid Biosynthesis in Pseudomonas 
aeruginosa Is Initiated by the FabY Class of β-Ketoacyl Acyl Carrier Protein Synthases.  Journal of 
Bacteriology, 194(19), 5171–5184.  
Zhang, Y.-M., Wu, B., Zheng, J., & Rock, C. O. (2003). Key Residues Responsible for Acyl Carrier Protein 
and β-Ketoacyl-Acyl Carrier Protein Reductase (FabG) Interaction.  Journal of Biological Chemistry , 278(52), 
52935–52943. 
Zwick, F., Lale, R., & Valla, S. (2013). Regulation of the expression level of transcription factor XylS 
reveals new functional insight into its induction mechanism at the Pm promoter. BMC Microbiology, 13(1), 262.  
  

 
119 
 
Materials and Methods 
Reagents and media preparation. All chemicals in this study were purchased from Sigma-Aldrich (St. Louis, MI, 
USA). Lysogeny (LB) broth composed of 5g/L NaCl, 10 g/L tryptone and 5g/L yeast extract and agar plates 
prepared with the addition of 15 g/L agar. In this study, a deBont was pre pared containing the following: 3.88 g/L 
K2HPO4, 1.63 g/L NaH 2PO4, 4 g/L NH 4Cl, 10 mg/L ethylenediaminetetraacetic acid (EDTA), 100 mg/L MgSO 4, 2 
mg/L ZnSO4, 1 mg/L CaCl2·2H2O, 5 mg/L FeSO4, 0.2 mg/L Na2MoO4·2H2O, 0.2 mg/L CuSO4, 0.4 mg/L CoCl2·6H2O 
and 1  mg/L MnCl 2·2H2O. Carbon sources were added separately as described in the text. Kanamycin and 
gentamicin were added to 50- and 10 µg/L, respectively, when needed. 
Bacterial strains, plasmids and oligonucleotides. All strains, plasmids and oligonucleotides are listed in tables 
S1-3. Oligonucleotides were purchased from Integrated DNA technologies (Coralville, IA, USA). Genomic DNA 
extractions were performed using DNeasy blood and tissue DNA extraction kits (Qiagen, Hilden, Germany), 
plasmid extractions performed with Nucleospin ® Plasmid kit (Macherny-Nagel, Düren, Germany), gel extractions 
and PCR clean -up with NucleoSpin ® Gel and PCR clean -up kit (Macherny -Nagel, Düren, Germany ), 
oligonucleotides designed using the Benchling primer wizard function (San Francisco, CA, USA) and AMUSER 
web-tool (Genee et al. 2015). Polymerase chain reactions (PCR) were carried out with PhusionU (ThermoFisher, 
Waltham, MA, USA) or OneTaq (New England Biolabs, Ipswich, MA, USA) polymerase. 
Plasmid construction, and homologous recombination -mediated genome engineering of pseudomonas 
putida. Unless otherwise noted, plasmids were constructed with established USER cloning techniques (Nour-Eldin 
et al. 2006). In brief, primers were designed using the AMUSER we β- tool (Genee et al. 2015) uracil-containing 
primers were purchased from Invitrogen (Waltham, MA, USA) and PCR performed with PhusionU (ThermoFisher, 
Waltham, MA, USA). Cleaned PCR fragments were pooled to equimolar concentrations and ligated with USER™ 
enzyme (New England Biolabs, Ipswich, MA, USA). Contaminating methylated DNA was digested using DpnI (New 
England Biolabs, Ipswich, MA, USA). 
Genetic manipulation was performed using pSWN2 assisted homologous recombination (Volke et al. 2021). In 
brief, genetic constructs destined for chromosomal deletion or integration were designed with two homology arms, 
~500 bp upstream and downstream a target region of interest. For disruption, the homology arms flanking a gene 
of interest were ligated together. To integrate constructed pSNW2 plasmids, Pseudomonas putida strains were 
washed with 1 mL of 300 mM sucrose 2 -3 times and washed strains placed in a Gene Pulser® cuvette (Bio-Rad, 
Hercules, CA, USA) electroporation cuvette with 100-500 ng of purified plasmid and electroporated at 2.5 kV with 
a MicroPulser™ electroporator (Bio-Rad, Hercules, CA, USA). The cell mixture was recovered in 1 mL LB broth 
for one hour before plating on LB agar with kanamycin. 
Resulting colonies with green fluorescence and kanamycin resistance were considered single integrants. Single 
integrants were inoculated in LB with kanamycin, washed the following day 2 -3 times with 300 mM sucrose and 
electroporated with pQure-6-strong. The cell mixture was immediately suspended in 5 mL LB broth with gentamicin 

 
120 
 
and 5 mM 3-methyl benzoate and incubated at 30°C overnight to promote a secondary recombination event. The 
following day, the curing broth was plated on LB agar with gentamicin and colonies with red fluorescence, absence 
of green fluorescence, sensitivity to kanamycin and genetic background of interest were inoculated in LB media 
with no antibiotics to cure the pQure -6-strong plasmid. Next, the cell mixture was plate on LB with no antibiotics 
and colonies screen for sensitivity to gentamicin. Successful genetic manipulations were screen by PCR and final 
strains stored at -80°C 
Pseudomonas putida growth analysis. Growth curves of Pseudomonas putida strains were prepared by first 
pre-culturing the chosen strain in lysogen broth. The resulting biomass collected the following day and washed 
twice in distilled deionized H2O (dd H2O) before normalizing OD600 to ~2.5. Washed, OD600 normalized strains were 
inoculated 1:100 in 24- or 96-well plates (Greiner Bio-One, Kremsmünster, Austria) to an effective starting OD600 
of ~0.025. Plates were incubated in Epoch2 microtiter plate reader (Agilent, Santa Clara, CA, USA), SynergyH1 
microtiter plate reader (Agilent, Santa Clara, CA, USA) or ELx808 microtiter plate reader (BioTek, Winoosky VA, 
USA) and absorbance monitored at 600 or 630 nm. Resulting absorbances, when necessary, were converted to 
OD600 via transformation with a calibration curve 
The resulting growth curves were analyzed using the QurvE (Wirth et al. 2023) software with default settings unless 
otherwise mentioned. Fitness scores were determined using a fitness calculator 
(https://github.com/Garret721/fitness-calculator). In brief, a fitness score is weighted summary of normalized 
growth parameters. Fitness scores are determined by first normalizing growth parameters (Max OD, Growth Rate 
and Lag Time) across a data set and summarizing each per curve growth with user defined weights. 
Fatty acyl methyl esterification (FAME) analysis and C13 GC-MS determination. Esterification of C13 labeled 
fatty acids was performed via alkaline substitution of methanol generating a labeled fatty-acyl ester. In brief, strains 
destined for fatty acid content assessment were pre-cultured in deBont with 5 mM octanoate and 10 mM glucose 
to support growth in case of fatty acid degradation deficiencies. The following day, 3 -5 mL of deBont with 5 mM 
octanoate with a C13 label at position one of the acids and 10  mM glucose was inoculated with 30-50 µL of pre-
culture. The resulting culture was incubated for ~24 hours before cells were harvested. Supernatant was carefully 
removed, the biomass pellet disrupted by resuspending in 1 mL 2:1 chloroform methanol and tran sferred to a 5 
mL clear glass vial with PTFE line lid (Mikrolab Aarhus, Aarhus Denmark). Pellet, chloroform methanol suspension 
was vortex for up 45 seconds and left to incubate at room temperature for 4 hours to overnight. Once disruption 
complete, the su spension was evaporated near the opening of a fume hood. Esterification was performed by 
suspending dried, disrupted biomass in 500 µL of 0.5 M NaOH in methanol, vortex and incubated for 45-60 minutes 
at 40°C. Esterification reactions were shaken at half the incubation time. Once the esterification reaction complete, 
reaction mixes were cooled to room temperature before neutralizing the base with 500 µL of 0.5 M HCl in methanol. 
Fatty acid esters were extracted with 1000 µL of hexane (or amount equating to total 0.5 M NaOH and HCl added) 
and the resulting organic phase (top) extracted. Samples containing fatty acid esters were transferred to 1.5 mL 
clear via with PTFE-lined lids and 150 µL sample insert (Mikrolab Aarhus, Aarhus, Denmark).  

 
121 
 
Fatty-acyl esters were analyzed and reported by the DTU Center for Biosustainability analytics department. In 
breif, samples were analyzed on an Agilent 8890GC (Agilent Technologies Inc. Santa Clara, CA) gas 
chromatography (GC) system connected to an Agile nt 5977b high efficiency source (HES) mass spectrometer 
(MS) with DBS MS column (30m x 0.25 mm x 0.25 um) (Agilent Technologies Inc. Santa Clara, CA). Samples were 
injected at volumes of 1 uL into the GC system with injector temperatures 300C. Samples were  separated on a 
fixed gradient of 40C for 4 minutes followed by an increase in column temperature to 280C at a rate of 10C/min 
and an increase in column temperature to 325C at a rate of 50C/min. The column was held at 325C for 1 minute. 
The mobile phase consisted of high purity N2 and maintained at a flow rate of 1.2 mL/min. The mass spectrometer 
was set to selected ion monitoring (SIM) mode. Fatty acyl relative abundance data ware corrected following 
established methods (Heinrich et al. 2018). Corrected values are reported in the supplementary materials. 
 
 
 
 
 
  

 
122 
 
Chapter 6: Concluding remarks 
Establishing novel chemistries in bacteria is the first step to expanding the metabolic capacity of life and 
the range of biomolecules which can be built. The aim of this thesis was to build a platform by which 
researchers can systematically explore novel areas of bioproduction and, as case study, demonstrate 
the efficacy of the system as an answer for environmental pollutants. In these concluding remarks, I will 
revisit the contributions each chapter has made to the field of metabolic engineering. I will expand on the 
challenges encountered throughout the thesis , highlight the key successes and delineate the future 
direction in this field. 
In Chapter 1, we aimed at clarifying the underlying sulfur acquisition mechanisms in Pseudomonas putida 
with the goal of using this information to guide future engineering efforts. This process is heavily reliant 
on the knowledge of sulfur metabolism in Escherichia coli as P. putida shares many of the same putative 
genes. Through combinatorial deletions, we demonstrated that the underlying metabolic mechanisms 
innate to P. putida are in line with those of E. coli, in a general sense. There is only one assim ilatory 
sulfate reduction pathway, total sulfur metabolism is regulated by the master regulator cysB and the ssu 
operon has a much broader sulfonate acceptance capacity than that of the tau operon. We could not, 
however, fully assess the sulfur trophism levels to P. putida. Our proteomics results indicated sulfate had 
a regulational supressing effect, but cysteine  selectively did. Furthermore, limitations to our process  
meant we could not confirm sequential sulfur source consumption (e.g. cysteine → sulfate  → 
ethanesulfonate). These issues likely arose due to the instability of cysteine in vivo and in vitro. 
Despite sulfur trophism not being fully confirmed, it is possible to investigate the potential intermediates 
involved in ssu and tau regulation. If P. putida ΔcysH cannot grow on ethanesulfonate and sulfate as 
sulfur source, this would indicate that a Cbl-like regulator is involved in ssu and tau expression. In E. coli, 
sulfate is transformed to sulfite through adenosine phophosulfate and phosphoadenosine 
phosphosulfate. With an intact cysDNC, these intermediates should accumulate and, if a Cbl -like 
regulator in P. putida governs sulfonate uptake and degradation enzyme expression, ssu enzymes should 
not be expressed. If this is the case, we could be one step closer to identifying the identity of protein 
governing the extended sulfur response in P. putida. Identification of these regulator elements could 
inform novel selection strains not investigated in Chapter 3. 
The broad capacity of the  ssu operon positions P. putida as a suitable chassis for novel chemistry 
discovery as the sulfonates used in this study contain non-natural element (e.g. silicon and fluorine). But 
not all tested sulfonates could be used as sole sulfur source. The model PFAS, 6:2 fluorotelomer 
sulfonate (FTSA) could not be used as a sole sulfur source in addition to trifluoroethanesulfonate and 

 
123 
 
bromoethanesulfonate. These results raise the question, what are the true limiting factors to sulfonate 
utilization? Since the ssu operon is divided into two major actions (import and degradation), we could not 
discern if import or degradation are the bottleneck to utilization. Purification SsuDE and characterization 
with respects to the sulfonates challenged in this thesis would shed light on the true limitations of the ssu 
operon. 
With targets in mind for disruption, we next turned our focus on establishing a tool to adapt generated 
selection strains. In Chapter 2, we set out to upgrade the Chi.Bio reactor as a platform for adaptive 
laboratory evolution with P. putida in mind.  The development of cell factories is driven by the DBTL cycle, 
which includes adaptive laboratory evolution (ALE). Traditional methods for these studies are often 
cumbersome, but the miniaturized Chi.Bio bioreactor system offered an automated and efficient solution. 
In this chapter, we illustrated the suitability of the Chi.Bio system for cultivation of P. putida under 
atmospheric and CO2 enriched environments demonstrating the versatility of the system. By enhancing 
Chi.Bio's capabilities such as code-base and lid, we also demonstrated its effectiveness in cultivating and 
adapting P. putida under key physiological conditions. Together, these positioned the Chi.Bio system as 
a powerful tool for ALE in P. putida and was used throughout Chapter 3. 
In Chapter 3, we tried to synthesize the results obtained in Chapter 1 and Chapter 2 to permit the 
overconsumption of sulfonates. In our effort to create a platform strain for novel chemistry discovery, we 
successfully engineered a base P. putida strain which is entirely reliant on exogenous sulfonates or 
cysteine but further engineering this proved problematic.  We quickly realize that growth yield is an 
inefficient means to identify increased sulfonate consumption. Adaptation of engineered strains with the 
Chi.Bio system did not yield any adapted strains . We believe  that neither the selection strains nor the 
selection method was at fault here. Instead, we the operation range for adaptation with sulfur as an 
indicator is too narrow. Both carbon and nitrogen metabolism are needed in several orders of magnitude 
more than s ulfur which limits the operational range of enhancement when adapting for increased 
sulfonate.  
When constructing selection strains, it’s crucial to consider the operation range of the pathway being 
enhanced. A prime example of this is the adaptation of P. putida SEM10 with ribose as sole carbon 
source. While growth rates on ribose were low, the operational range of the strain was much large. Growth 
could be seen on microtiter plate reader and Chi.Bio online OD measurements. Matching sulfur 
requirements to a pathway or metabolism with equivalent demand would be the first step in streamlining 
engineering efforts. In addition to the discussed, future efforts should focus on refining experimental 
conditions, such as optimizing sample preparation and real time monitoring to accurately use 

 
124 
 
ethanesulfonate or taurine quantification as measure of fitness. Additionally, alternative metabolic 
selection schemes should be explored, such as targeting glycine auxotrophy.  
Chapters 4 and Chapter 5 mark the departure of sulfur-related metabolic engineering. In these chapters 
we explore the potential of connecting a biosynthesis apparatus for potential novel sulfonates. In Chapter 
4, we identified the potential of ‘killing two birds with one stone’ by reviewing and identifying the challenges 
to overcome in order to upcycle PFAS into fatty acid metabolism. We found four challenges that had to 
be overcome: PFAS and fluoride resistance , preservation of biosynthetic potential and d irect-to-ACP 
ligation. Wild-type P. putida can overcome the first two . The metabolic potential of entering PFAS is 
entirely dependent on the preservation of the non -fluorinated portions and, rearrangement of fatty acid 
initiation is needed to provide a point of entry into endogenous metabolism. 
In Chapter 5, we address the latter two metabolic rearrangements needed to enable PFAS  upcycling. 
PFAS degradation bears the hallmarks of bacterial β-oxidation meaning, if PFAS are to be upcycled, we 
had to ensure β-oxidation was not occurring on medium chain. Surprisingly, this was easily achieved with 
three disruptions to endogenous ketoacyl -CoA thiolases. While we are confident that we would be able 
to preserve the biosynthetic potential of entering PFAS, we could not confirm, beyond a reasonable doubt, 
that entering PFAS could be introduced into endogenous fatty acid supplies. In our attempt to provide an 
entry point for medium chain fatty acids into fatty acid supplies, we disrupted two known fatty acid initiators 
and used 13C labeled octanoate to confirm activity of a heterologous medium chain initiator. Our findings 
indicate that P. putida possesses an innate mechanism for shunting eight carbon fatty acids into fatty 
acid synthesis, as evidenced by the high proportion of single 13C substitutions in analyzed fatty-acyl esters 
with intact PP_4545 . This suggests that PP_4545 in P. putida might function similarly to PA3286 in P. 
aeruginosa, a hypothesis supported by their high protein sequence identity.  However, our results are 
limited by the fact that , when PP_4545 is disrupted and no other mechanism is provided to shunt fatty 
acids back into fatty acid synthesis, there is still a high proportion of  13C substitution across longer fatty 
acids. These results indicate a potential one carbon modifying mechanism innate to P. putida and needs 
to be addressed prior to moving forward. 
Together, this thesis had as goal to establish an efficient platform strain for the delivery of novel 
metabolites to enable novel chemistries and, provide an outlet to for those novel chemistries. While we 
were able to make great strides in developing tool s to adapt P. putida and shed light on a particularly 
under investigated metabolism, much work remains to leverage it to its fullest. It is my belief that, when 
designing a selection strain, it is crucial to match the expected output of the selection press ure with the 
desired phenotype being selected for. If this can be achieved for sulfur metabolism explored here, P. 

 
125 
 
putida has the potential of solidifying itself as a chassis for production of molecules which are New -to-
Nature. 
 
 
 
  

 
126 
 
 
Appendix I to Chapter 1, Unravelling the physiological structure 
of sulfur metabolism in P. putida KT2440 
 
Garret W. O'Connell1, Alexandre Perrin2, Pablo Ivan Nikel1 
   
1Novo Nordisk Center for Biosustainability, Systems Environmental Microbiology group 
2Ecole Polytechnique, Centre de mathématiques appliquées 
  

 
127 
 
Table 1. Targeted metabolomics method for ethanesulfonate quantification. 
Time (min) Step time (min) Eluent A Eluent B Flowrate 
0 - 5 5 100% 0% 0.4 mL/min 
5 - 9 4 98% 2% 0.4 mL/min 
9 - 9.5 0.5 94% 6% 0.4 mL/min 
9.5 - 11.5 2 94% 6% 0.4 mL/min 
11.5 -12 0.5 89% 11% 0.4 mL/min 
12 - 13.5 1.5 89% 11% 0.4 mL/min 
13.5 - 15.5 2 72% 28% 0.4 mL/min 
15.5 - 16.5 1 47% 53% 0.15 mL/min 
16.5 - 22.5 6 47% 53% 0.15 mL/min 
22.5 - 23 0.5 100% 0% 0.15 mL/min 
 
  

 
128 
 
Table S2. Differentially produce proteins of sulfate (MgSO4) vs cysteine (L-Cys) grown Pseudomonas putida 
proteomes. 
PP number Log2 (fold change) Log (p-value) Up or downregulated 
PP_4138 1.056118 1.303958 Upregulated 
PP_3445 1.462135 1.307169 Upregulated 
PP_2950 1.160569 1.335955 Upregulated 
PP_2458 1.202985 1.33748 Upregulated 
PP_3638 1.067116 1.339461 Upregulated 
PP_0163 1.287137 1.340224 Upregulated 
PP_1798 1.607105 1.340291 Upregulated 
PP_1752 1.163466 1.340941 Upregulated 
PP_5041 1.346149 1.34527 Upregulated 
PP_0657 1.11971 1.356789 Upregulated 
PP_4734 1.357384 1.36155 Upregulated 
PP_1251 1.189003 1.362082 Upregulated 
PP_3832 1.043273 1.364588 Upregulated 
PP_0411 1.702001 1.37213 Upregulated 
PP_0266 1.323102 1.383165 Upregulated 
PP_5677 1.442122 1.384952 Upregulated 
PP_0658 1.255918 1.387552 Upregulated 
PP_5587 1.250717 1.394487 Upregulated 
PP_3551 1.574627 1.399327 Upregulated 
PP_3738 1.209548 1.409011 Upregulated 
PP_5531 1.101723 1.411798 Upregulated 
PP_1822 1.137077 1.412875 Upregulated 
PP_3775 1.955149 1.415666 Upregulated 
PP_0738 1.335801 1.421881 Upregulated 
PP_3983 1.161382 1.436079 Upregulated 
PP_4550 1.514178 1.440975 Upregulated 
PP_5700 1.472496 1.446442 Upregulated 
PP_4502 2.643727 1.456034 Upregulated 
PP_4977 1.195453 1.463261 Upregulated 
PP_0744 1.089694 1.46646 Upregulated 
PP_5365 1.095142 1.470792 Upregulated 
PP_2371 1.613475 1.473247 Upregulated 
PP_4052 2.356425 1.482302 Upregulated 
PP_5005 1.124634 1.489758 Upregulated 
PP_0215 1.787286 1.497435 Upregulated 
PP_5325 1.733513 1.514489 Upregulated 
PP_1215 1.636396 1.518155 Upregulated 
PP_3219 1.335661 1.533351 Upregulated 
PP_3904 1.10431 1.533949 Upregulated 
PP_4804 1.893732 1.537362 Upregulated 
PP_0308 1.187585 1.5432 Upregulated 
PP_1873 1.459174 1.553316 Upregulated 
PP_2077 1.632069 1.5764 Upregulated 
PP_4519 1.514179 1.577098 Upregulated 
PP_4976 1.379456 1.592114 Upregulated 
PP_0550 1.155738 1.594562 Upregulated 
PP_1741 1.12734 1.596557 Upregulated 
PP_1349 1.498705 1.606136 Upregulated 
PP_0797 2.879236 1.609091 Upregulated 
PP_4054 1.223622 1.609788 Upregulated 
PP_0412 1.352549 1.619476 Upregulated 
PP_4447 1.353671 1.621364 Upregulated 
PP_4620 1.042966 1.623937 Upregulated 

 
129 
 
PP_1720 1.469114 1.625041 Upregulated 
PP_0294 1.451572 1.628457 Upregulated 
PP_1623 1.55868 1.632589 Upregulated 
PP_3713 1.352069 1.646137 Upregulated 
PP_0893 1.289615 1.647817 Upregulated 
PP_2233 1.162556 1.650192 Upregulated 
PP_2292 1.87596 1.652009 Upregulated 
PP_2220 1.179451 1.667172 Upregulated 
PP_5007 1.292655 1.671273 Upregulated 
PP_1502 1.153525 1.687466 Upregulated 
PP_4021 2.374016 1.704782 Upregulated 
PP_1538 1.616616 1.726626 Upregulated 
PP_4683 1.172502 1.7312 Upregulated 
PP_0739 1.68911 1.73262 Upregulated 
PP_3790 2.433696 1.734148 Upregulated 
PP_0203 1.46009 1.739757 Upregulated 
PP_4146 1.292464 1.757505 Upregulated 
PP_2036 3.589974 1.77492 Upregulated 
PP_4394 2.297444 1.793443 Upregulated 
PP_4967 1.572392 1.820731 Upregulated 
PP_4601 1.321641 1.839817 Upregulated 
PP_1982 1.151757 1.84568 Upregulated 
PP_2370 1.648217 1.848405 Upregulated 
PP_3722 1.390469 1.849457 Upregulated 
PP_2453 1.966178 1.849949 Upregulated 
PP_1291 1.039385 1.863055 Upregulated 
PP_4938 1.024256 1.865583 Upregulated 
PP_0542 1.003543 1.900201 Upregulated 
PP_0505 1.14435 1.910331 Upregulated 
PP_1304 2.427984 1.910751 Upregulated 
PP_0323 1.558998 1.931873 Upregulated 
PP_4279 1.908231 1.933629 Upregulated 
PP_2460 2.891248 1.950493 Upregulated 
PP_4040 1.071347 1.950779 Upregulated 
PP_4278 1.07669 2.031384 Upregulated 
PP_1762 2.389634 2.038008 Upregulated 
PP_0766 1.269641 2.038892 Upregulated 
PP_3785 4.013982 2.110742 Upregulated 
PP_3788 3.917169 2.169056 Upregulated 
PP_4966 1.638382 2.174961 Upregulated 
PP_5464 1.76234 2.177311 Upregulated 
PP_1478 1.592405 2.183344 Upregulated 
PP_2892 1.221106 2.200104 Upregulated 
PP_3786 4.16553 2.223752 Upregulated 
PP_1303 2.46722 2.226863 Upregulated 
PP_1631 1.135841 2.242877 Upregulated 
PP_0742 1.805807 2.2506 Upregulated 
PP_4038 1.850022 2.27533 Upregulated 
PP_4111 3.244793 2.284852 Upregulated 
PP_1428 1.700653 2.287911 Upregulated 
PP_4034 1.503496 2.34281 Upregulated 
PP_3787 3.603311 2.355666 Upregulated 
PP_4361 1.005542 2.384901 Upregulated 
PP_3611 1.756576 2.4098 Upregulated 
PP_1726 1.312617 2.410461 Upregulated 
PP_0168 1.871745 2.43018 Upregulated 
PP_3145 1.653431 2.443127 Upregulated 
PP_2674 3.050213 2.447918 Upregulated 

 
130 
 
PP_0325 2.420117 2.495326 Upregulated 
PP_0574 1.867762 2.541107 Upregulated 
PP_3783 4.480574 2.573183 Upregulated 
PP_1539 2.080714 2.578578 Upregulated 
PP_0324 1.203752 2.590334 Upregulated 
PP_1501 2.446736 2.611061 Upregulated 
PP_4867 1.257121 2.618092 Upregulated 
PP_4010 1.816232 2.645112 Upregulated 
PP_1638 1.905264 2.661566 Upregulated 
PP_2680 2.905056 2.67381 Upregulated 
PP_3777 2.938254 2.690004 Upregulated 
PP_3954 1.540102 2.801835 Upregulated 
PP_2422 1.233995 2.810067 Upregulated 
PP_3781 3.803209 2.880641 Upregulated 
PP_2488 1.507069 2.959584 Upregulated 
PP_3778 3.029818 2.982131 Upregulated 
PP_5502 1.751974 3.112577 Upregulated 
PP_2652 2.377268 3.133349 Upregulated 
PP_0397 1.824443 3.207486 Upregulated 
PP_3784 2.671707 3.243484 Upregulated 
PP_5516 1.635338 3.455048 Upregulated 
 
  

 
131 
 
Table S3. Gene ontology binning of sulfate (MgSO4) vs cysteine (L-Cys) grown Pseudomonas putida proteomes. 
 
  
Gene-Ontology-Terms p-
values 
Comprising genes Average Log2 (fold 
change) 
sulfate assimilation 3.25E-04 PP_1304, PP_1303, PP_2371 2.16956 
tetrahydrofolate metabolic process 0.001527 PP_4977, PP_0325, PP_0324, 
PP_0323 
1.59458 
sulfur compound metabolic process 0.00199 PP_4976, PP_1304, PP_4977, 
PP_2371, PP_4938, PP_0658, 
PP_3775, PP_1303, PP_3219, 
PP_4967 
1.622696 
hydrogen sulfide biosynthetic process 0.001991 PP_1304, PP_1303 2.447602 
folic acid-containing compound metabolic 
process 
0.002216 PP_4977, PP_0325, PP_0324, 
PP_0323 
1.59458 
pteridine-containing compound metabolic 
process 
0.00263 PP_4977, PP_0325, PP_0324, 
PP_0323 
1.59458 
aspartate family amino acid metabolic 
process 
0.002764 PP_3775, PP_2453, PP_4977, 
PP_0658, PP_3790, PP_2077 
1.739744 
organic cation transport 0.004075 PP_0411, PP_1726, PP_0294 1.48873 
one-carbon metabolic process 0.00754 PP_4977, PP_4976, PP_4967 1.382434 
sulfur compound biosynthetic process 0.010471 PP_4967, PP_4977, PP_0658, 
PP_4938, PP_1304, PP_1303 
1.657204 
aspartate family amino acid biosynthetic 
process 
0.016293 PP_4977, PP_0658, PP_3790, 
PP_2077 
1.629284 
organic hydroxy compound catabolic 
process 
0.016303 PP_0542, PP_3713, PP_4620 1.132859 
regulation of translation 0.016303 PP_3832, PP_5502, PP_5700 1.422581 
lysine metabolic process 0.018528 PP_3775, PP_3790, PP_2077 2.006971 
regulation of amide metabolic process 0.018528 PP_3832, PP_5502, PP_5700 1.422581 
post-transcriptional regulation of gene 
expression 
0.020912 PP_3832, PP_5502, PP_5700 1.422581 
organic cyclic compound catabolic process 0.026112 PP_4620, PP_4038, PP_2460, 
PP_1638, PP_3832, PP_3713 
1.680807 
regulation of protein metabolic process 0.029032 PP_3832, PP_5502, PP_5700 1.422581 
tetrapyrrole metabolic process 0.033004 PP_0744, PP_3781, PP_1638, 
PP_1349 
2.074218 
porphyrin-containing compound metabolic 
process 
0.035245 PP_0744, PP_3781, PP_1638 2.266056 
L-amino acid metabolic process 0.044403 PP_2077, PP_3790, PP_3778, 
PP_4977, PP_2453, PP_0658, 
PP_3775, PP_4620 
1.813906 
proteinogenic amino acid metabolic 
process 
0.044403 PP_2077, PP_3790, PP_3778, 
PP_4977, PP_2453, PP_0658, 
PP_3775, PP_4620 
1.813906 

 
132 
 
Table S4. Differentially produce proteins of sulfate (MgSO 4) vs ethanesulfonate (EtSO 3) grown Pseudomonas 
putida proteomes. 
PP number Log2 (fold change) Log (p-value) Up or downregulated 
PP_0170 -9.05739 2.453318 Downregulated 
PP_0237 -8.57494 1.738049 Downregulated 
PP_0238 -8.05229 3.848967 Downregulated 
PP_0241 -6.3337 2.669722 Downregulated 
PP_2762 -5.93298 2.872464 Downregulated 
PP_0233 -5.82557 1.694389 Downregulated 
PP_3217 -5.55311 1.808479 Downregulated 
PP_3528 -5.25608 3.282307 Downregulated 
PP_0222 -5.22347 2.458933 Downregulated 
PP_0207 -4.93372 2.343305 Downregulated 
PP_3218 -4.78287 3.303562 Downregulated 
PP_0230 -4.44471 2.718032 Downregulated 
PP_0240 -4.31924 3.648614 Downregulated 
PP_0235 -4.30304 3.645393 Downregulated 
PP_2756 -4.18002 1.791889 Downregulated 
PP_5171 -4.11591 1.95049 Downregulated 
PP_0169 -3.80293 3.600011 Downregulated 
PP_5172 -3.79217 4.06362 Downregulated 
PP_1185 -3.44323 2.474979 Downregulated 
PP_2770 -3.44186 2.029883 Downregulated 
PP_0221 -3.3484 1.654458 Downregulated 
PP_0223 -3.29409 4.446316 Downregulated 
PP_0533 -3.11489 2.451371 Downregulated 
PP_3229 -3.07884 1.582329 Downregulated 
PP_5167 -3.0178 1.785835 Downregulated 
PP_1186 -2.90324 2.709068 Downregulated 
PP_2765 -2.88472 3.429992 Downregulated 
PP_5165 -2.72764 1.630529 Downregulated 
PP_3219 -2.52115 2.133366 Downregulated 
PP_0224 -2.38468 3.040074 Downregulated 
PP_4342 -2.2864 1.628826 Downregulated 
PP_2755 -2.23807 2.296613 Downregulated 
PP_2752 -2.17315 2.05516 Downregulated 
PP_4504 -2.03117 1.675784 Downregulated 
PP_0236 -1.99038 3.641607 Downregulated 
PP_5502 -1.8867 2.961419 Downregulated 
PP_5168 -1.86029 3.011955 Downregulated 
PP_1062 -1.79268 2.273656 Downregulated 
PP_2874 -1.77661 1.843804 Downregulated 
PP_0234 -1.5016 3.322232 Downregulated 
PP_2439 -1.47305 3.227042 Downregulated 
PP_3602 -1.38138 2.843637 Downregulated 
PP_2849 -1.30125 2.421112 Downregulated 
PP_3706 -1.22729 2.221965 Downregulated 
PP_5270 -1.21266 1.49109 Downregulated 
PP_3639 -1.18977 2.526516 Downregulated 
PP_0742 -1.17106 2.273333 Downregulated 
PP_2118 -1.16431 1.652665 Downregulated 
PP_1832 -1.14138 1.608204 Downregulated 
PP_0363 -1.12847 1.5494 Downregulated 
PP_4305 -1.10489 2.142113 Downregulated 
PP_4830 -1.09973 2.086171 Downregulated 
PP_3288 -1.06111 3.019495 Downregulated 

 
133 
 
PP_0225 -1.05208 2.403861 Downregulated 
PP_3232 -1.02948 1.630163 Downregulated 
PP_1217 -1.00987 3.182934 Downregulated 
PP_0548 1.004608 1.424956 Upregulated 
PP_4804 1.026448 1.649179 Upregulated 
PP_0386 1.03112 1.389374 Upregulated 
PP_4637 1.057528 1.419896 Upregulated 
PP_1218 1.065406 2.039047 Upregulated 
PP_5483 1.070178 1.345388 Upregulated 
PP_3778 1.092214 2.042027 Upregulated 
PP_4316 1.100635 1.656412 Upregulated 
PP_3591 1.10674 1.559955 Upregulated 
PP_0614 1.109756 1.512031 Upregulated 
PP_0141 1.126623 1.44217 Upregulated 
PP_4864 1.169303 1.443173 Upregulated 
PP_0183 1.172894 3.508847 Upregulated 
PP_3784 1.196864 2.014507 Upregulated 
PP_2536 1.205113 1.404245 Upregulated 
PP_4698 1.240262 1.755859 Upregulated 
PP_2656 1.242944 1.370145 Upregulated 
PP_1958 1.251307 1.671485 Upregulated 
PP_1545 1.349595 1.640549 Upregulated 
PP_3790 1.350266 1.344559 Upregulated 
PP_2188 1.403809 1.412978 Upregulated 
PP_3828 1.451411 1.649607 Upregulated 
PP_3501 1.572509 1.671694 Upregulated 
PP_3783 1.616702 2.029314 Upregulated 
PP_3785 1.763418 1.900882 Upregulated 
PP_3777 1.776184 3.331413 Upregulated 
PP_4279 1.848662 3.077632 Upregulated 
PP_3781 1.901385 2.593032 Upregulated 
PP_0053 1.944252 2.200096 Upregulated 
PP_3779 2.026305 1.441392 Upregulated 
PP_0797 2.230882 1.506784 Upregulated 
PP_3787 2.328669 2.257055 Upregulated 
PP_3788 2.444882 2.208256 Upregulated 
PP_3786 2.51682 2.149209 Upregulated 
  

 
134 
 
Table S5. Gene ontology binning of sulfate (MgSO4) vs ethanesulfonate (EtSO3) grown Pseudomonas putida 
proteomes. 
Gene-Ontology-
Terms 
p-values Comprising genes Average Log2 (fold 
change) 
sulfur compound metabolic 
process 
7.28E-10 PP_3229, bioF, atsK, PP_2765, PP_3528, 
ssuE, PP_0169, PP_1832, PP_3217, 
PP_3219, ssuD, ssuA, tauA 
-4.38268 
alkanesulfonate catabolic 
process 
1.46E-08 ssuE, PP_3219, PP_2765, ssuD -4.25564 
sulfur compound catabolic 
process 
1.12E-07 ssuE, PP_3219, PP_2765, ssuD, atsK -4.08662 
alkanesulfonate metabolic 
process 
2.16E-07 ssuE, PP_3219, PP_2765, ssuD -3.97865 
organic acid catabolic 
process 
5.90E-05 sfnB, sfnA, dadA-II, PP_0224, PP_0223, 
ssuE, PP_3219, PP_2765, ssuD 
-3.86214 
sulfur compound transport 7.61E-05 tauA, cysA, sbp-II, sbp-I -3.73233 
leucine catabolic process 1.58E-04 sfnA, sfnB, PP_0224 -3.73233 
small molecule catabolic 
process 
1.60E-04 sfnB, sfnA, dadA-II, PP_0224, PP_0223, 
ssuE, PP_3219, PP_2765, ssuD 
-3.51858 
cellular catabolic process 1.98E-04 sfnB, sfnA, atsK, PP_2765, ssuE, dadA-II, 
PP_0224, PP_3219, ssuD, ahpC, 
PP_0223 
-3.51858 
sulfate transport 2.15E-04 sbp-II, cysA, sbp-I -3.51858 
sulfate transmembrane 
transport 
2.15E-04 sbp-II, cysA, sbp-I -3.25537 
leucine metabolic process 5.75E-04 sfnA, sfnB, PP_0224 -3.25537 
inorganic anion transport 7.37E-04 sbp-II, cysA, sbp-I, PP_0241 -3.25537 
branched-chain amino acid 
catabolic process 
8.45E-04 sfnA, sfnB, PP_0224 -3.20147 
catabolic process 0.001491667 sfnB, sfnA, atsK, PP_2765, ssuE, dadA-II, 
PP_0224, PP_3219, ssuD, ahpC, 
PP_0223 
-3.20147 
inorganic anion 
transmembrane transport 
0.001840715 sbp-II, cysA, sbp-I -2.76996 
cellular oxidant 
detoxification 
0.005980415 PP_3639, ahpC, PP_0235 -2.76725 
detoxification 0.007644008 PP_3639, ahpC, PP_0235 -2.63893 
cellular detoxification 0.007644008 PP_3639, ahpC, PP_0235 -2.63893 
alpha-amino acid catabolic 
process 
0.008216456 sfnA, sfnB, PP_0224, dadA-II -2.32195 
organic substance catabolic 
process 
0.008501492 sfnB, sfnA, PP_2765, ssuE, dadA-II, 
PP_0224, PP_3219, ssuD, PP_0223 
-2.22563 
branched-chain amino acid 
metabolic process 
0.009556473 sfnA, sfnB, PP_0224 0.792669 
amino acid catabolic 
process 
0.013524175 dadA-II, sfnA, sfnB, PP_0224 1.20609 
organic acid metabolic 
process 
0.015485572 sfnB, sfnA, bioF, PP_2765, ssuE, dadA-II, 
PP_1832, PP_0224, PP_3219, ssuD, 
PP_0223 
1.20609 
carboxylic acid catabolic 
process 0.027963713 sfnB, sfnA, dadA-II, PP_0224, PP_0223 1.307185 
cellular response to 
stimulus 0.04622766 pfeS-I, PP_3706, ruvB, PP_0235, ahpC 1.381578 
  

 
135 
 
Table S6. Differentially produce proteins of ethanesulfonate (EtSO 3) vs cysteine (L -Cys) grown Pseudomonas 
putida proteomes. 
PP number Log2 (fold change) Log (p-value) Up or downregulated 
PP_2435 -4.49907 2.242274 Downregulated 
PP_3901 -2.42994 3.091015 Downregulated 
PP_0053 -1.75228 2.114278 Downregulated 
PP_4748 -1.69266 1.942124 Downregulated 
PP_3828 -1.6655 1.894129 Downregulated 
PP_2188 -1.54337 4.159817 Downregulated 
PP_1574 -1.45937 1.448116 Downregulated 
PP_1567 -1.37219 1.91429 Downregulated 
PP_1331 -1.31033 1.531513 Downregulated 
PP_3946 -1.20264 1.564081 Downregulated 
PP_4917 -1.16332 1.465951 Downregulated 
PP_1573 -1.10278 2.11879 Downregulated 
PP_5377 -1.08328 2.394592 Downregulated 
PP_3822 -1.06645 1.657184 Downregulated 
PP_3501 -1.03712 2.169987 Downregulated 
PP_0951 1.002119 3.463329 Upregulated 
PP_1792 1.002461 2.212004 Upregulated 
PP_5035 1.006675 2.358227 Upregulated 
PP_0182 1.008885 2.403542 Upregulated 
PP_4036 1.011515 1.623623 Upregulated 
PP_3904 1.014055 2.035308 Upregulated 
PP_0225 1.014919 1.691048 Upregulated 
PP_0191 1.02752 1.839954 Upregulated 
PP_4949 1.027642 1.720717 Upregulated 
PP_2338 1.035075 2.173764 Upregulated 
PP_2947 1.047818 2.532648 Upregulated 
PP_0921 1.051566 2.274517 Upregulated 
PP_1001 1.054637 1.902125 Upregulated 
PP_2161 1.054759 2.597196 Upregulated 
PP_5183 1.057382 1.960145 Upregulated 
PP_0294 1.061125 1.302683 Upregulated 
PP_1505 1.06584 2.017081 Upregulated 
PP_3722 1.06755 2.420336 Upregulated 
PP_1486 1.068183 1.322189 Upregulated 
PP_5258 1.078546 2.819892 Upregulated 
PP_0315 1.081677 1.315335 Upregulated 
PP_3765 1.082504 2.539148 Upregulated 
PP_3790 1.08343 2.016483 Upregulated 
PP_0424 1.08527 1.807142 Upregulated 
PP_4233 1.101643 2.58895 Upregulated 
PP_2170 1.102392 2.258397 Upregulated 
PP_5041 1.108025 1.927302 Upregulated 
PP_1210 1.122901 2.007786 Upregulated 
PP_4657 1.12901 1.715796 Upregulated 
PP_5270 1.131316 2.089417 Upregulated 
PP_1859 1.131371 1.785362 Upregulated 
PP_0430 1.132603 1.784816 Upregulated 
PP_3637 1.132748 1.44108 Upregulated 
PP_5392 1.134864 1.542386 Upregulated 
PP_3639 1.140431 2.120726 Upregulated 
PP_4879 1.142556 1.527532 Upregulated 
PP_5003 1.146526 3.004627 Upregulated 
PP_4138 1.152838 1.400106 Upregulated 
PP_3777 1.16207 1.550883 Upregulated 

 
136 
 
PP_0082 1.176033 3.586884 Upregulated 
PP_1625 1.179223 2.6209 Upregulated 
PP_4508 1.17949 1.931018 Upregulated 
PP_3832 1.180636 1.525964 Upregulated 
PP_2308 1.182712 1.941838 Upregulated 
PP_2387 1.185534 2.563635 Upregulated 
PP_2143 1.194209 1.844718 Upregulated 
PP_5005 1.195872 1.493886 Upregulated 
PP_4264 1.197837 1.719704 Upregulated 
PP_0738 1.200682 1.714373 Upregulated 
PP_3983 1.208103 1.707195 Upregulated 
PP_0777 1.214974 1.413138 Upregulated 
PP_3443 1.22948 3.715089 Upregulated 
PP_2950 1.231933 2.25666 Upregulated 
PP_5325 1.235873 1.504943 Upregulated 
PP_0766 1.238604 1.850218 Upregulated 
PP_3819 1.248533 1.819685 Upregulated 
PP_5365 1.250411 1.85163 Upregulated 
PP_4475 1.264134 2.310248 Upregulated 
PP_4034 1.265203 2.656321 Upregulated 
PP_1538 1.266065 2.435243 Upregulated 
PP_0641 1.273926 2.002489 Upregulated 
PP_3787 1.274643 1.568317 Upregulated 
PP_1752 1.275099 2.258295 Upregulated 
PP_2849 1.284466 2.553121 Upregulated 
PP_0794 1.292526 2.209469 Upregulated 
PP_1291 1.292732 2.40994 Upregulated 
PP_1654 1.296744 2.829982 Upregulated 
PP_2422 1.298086 3.803532 Upregulated 
PP_5206 1.314691 2.705123 Upregulated 
PP_3067 1.318673 1.766532 Upregulated 
PP_3415 1.323768 2.132351 Upregulated 
PP_0992 1.328595 1.600604 Upregulated 
PP_3954 1.342692 1.513247 Upregulated 
PP_1121 1.352024 2.259568 Upregulated 
PP_0163 1.35742 1.432409 Upregulated 
PP_1623 1.35984 1.6344 Upregulated 
PP_0516 1.374138 2.559475 Upregulated 
PP_4620 1.378054 1.627059 Upregulated 
PP_2187 1.37902 2.109124 Upregulated 
PP_2648 1.387699 1.846441 Upregulated 
PP_2292 1.388356 2.784861 Upregulated 
PP_4054 1.411479 2.045397 Upregulated 
PP_0181 1.411929 2.181797 Upregulated 
PP_2925 1.416686 3.069326 Upregulated 
PP_1873 1.417691 3.132373 Upregulated 
PP_1251 1.420849 2.239794 Upregulated 
PP_5283 1.421415 2.340299 Upregulated 
PP_1741 1.435982 1.698053 Upregulated 
PP_0920 1.451854 3.115119 Upregulated 
PP_2453 1.466365 1.91398 Upregulated 
PP_3638 1.469419 2.666872 Upregulated 
PP_2488 1.469875 1.567913 Upregulated 
PP_3784 1.474843 2.695749 Upregulated 
PP_1217 1.476711 3.067956 Upregulated 
PP_0203 1.486482 1.824808 Upregulated 
PP_5677 1.490675 1.348871 Upregulated 
PP_0215 1.495603 1.589821 Upregulated 

 
137 
 
PP_0541 1.501 2.631026 Upregulated 
PP_2528 1.504974 2.335932 Upregulated 
PP_2652 1.526644 2.067491 Upregulated 
PP_5008 1.528776 2.652458 Upregulated 
PP_0999 1.537151 2.260106 Upregulated 
PP_1631 1.54425 2.149622 Upregulated 
PP_0085 1.545799 2.895908 Upregulated 
PP_4447 1.559622 2.455146 Upregulated 
PP_2118 1.568388 2.02627 Upregulated 
PP_0168 1.570979 2.680002 Upregulated 
PP_0493 1.577998 2.279761 Upregulated 
PP_3706 1.60097 1.802744 Upregulated 
PP_0545 1.619006 3.921496 Upregulated 
PP_2371 1.619341 3.239379 Upregulated 
PP_1832 1.632752 1.745761 Upregulated 
PP_3786 1.64871 1.962687 Upregulated 
PP_1062 1.658135 2.119822 Upregulated 
PP_2327 1.661828 1.959692 Upregulated 
PP_2771 1.681013 2.388338 Upregulated 
PP_1428 1.696275 1.973346 Upregulated 
PP_0323 1.73132 2.114136 Upregulated 
PP_2679 1.732978 1.587744 Upregulated 
PP_3128 1.735964 2.179899 Upregulated 
PP_2439 1.744682 5.154761 Upregulated 
PP_0657 1.74684 1.88744 Upregulated 
PP_0412 1.748716 1.843949 Upregulated 
PP_0574 1.756338 1.844926 Upregulated 
PP_1478 1.782716 2.416478 Upregulated 
PP_3145 1.787423 2.571925 Upregulated 
PP_5007 1.787529 2.630137 Upregulated 
PP_5358 1.814732 1.512818 Upregulated 
PP_0542 1.82374 1.406744 Upregulated 
PP_4305 1.850501 1.63297 Upregulated 
PP_5464 1.854311 2.470467 Upregulated 
PP_3611 1.881018 2.13593 Upregulated 
PP_4038 1.898381 2.631396 Upregulated 
PP_3775 1.900659 3.355842 Upregulated 
PP_3781 1.901824 2.502434 Upregulated 
PP_0222 1.902916 2.080584 Upregulated 
PP_0658 1.92827 1.88162 Upregulated 
PP_3778 1.937604 4.335181 Upregulated 
PP_2370 1.939304 3.380366 Upregulated 
PP_0363 1.950724 1.884682 Upregulated 
PP_2752 1.975788 2.023943 Upregulated 
PP_5700 1.993664 2.799035 Upregulated 
PP_4342 2.076206 1.405178 Upregulated 
PP_3602 2.078252 3.280247 Upregulated 
PP_4010 2.092726 2.140466 Upregulated 
PP_2770 2.097123 2.221354 Upregulated 
PP_0234 2.097613 2.402736 Upregulated 
PP_1501 2.11856 2.630963 Upregulated 
PP_1304 2.128165 2.865879 Upregulated 
PP_0411 2.153812 2.486342 Upregulated 
PP_0397 2.159888 3.840386 Upregulated 
PP_5165 2.210599 1.310832 Upregulated 
PP_1303 2.213453 2.940599 Upregulated 
PP_0396 2.231174 1.544767 Upregulated 
PP_3785 2.250564 2.325822 Upregulated 

 
138 
 
PP_2755 2.37377 2.039487 Upregulated 
PP_4052 2.390287 1.504444 Upregulated 
PP_2756 2.425836 1.71485 Upregulated 
PP_0236 2.442326 3.192861 Upregulated 
PP_1638 2.465199 4.051123 Upregulated 
PP_0325 2.479657 1.626317 Upregulated 
PP_4021 2.479959 2.209893 Upregulated 
PP_5168 2.501175 2.242803 Upregulated 
PP_2765 2.730454 3.363674 Upregulated 
PP_2762 2.755044 1.601431 Upregulated 
PP_0207 2.786715 2.186572 Upregulated 
PP_0230 2.82944 1.901406 Upregulated 
PP_3783 2.863872 2.461262 Upregulated 
PP_2036 2.882948 3.606044 Upregulated 
PP_0533 2.902929 2.494397 Upregulated 
PP_0742 2.976871 2.328204 Upregulated 
PP_0232 3.001195 2.097146 Upregulated 
PP_0224 3.016689 3.028436 Upregulated 
PP_0221 3.085911 1.599584 Upregulated 
PP_5171 3.098565 1.70647 Upregulated 
PP_5167 3.257396 1.366919 Upregulated 
PP_4111 3.272902 1.572536 Upregulated 
PP_5192 3.345035 2.672023 Upregulated 
PP_2680 3.481334 2.172385 Upregulated 
PP_2674 3.515858 2.096863 Upregulated 
PP_5172 3.576918 3.603209 Upregulated 
PP_5502 3.638672 2.835212 Upregulated 
PP_0223 3.650053 3.928586 Upregulated 
PP_0233 3.65272 1.574704 Upregulated 
PP_3219 3.856808 1.896937 Upregulated 
PP_0235 3.955051 2.971867 Upregulated 
PP_0169 3.976091 3.30106 Upregulated 
PP_0240 4.165649 3.03499 Upregulated 
PP_0237 4.230084 1.67899 Upregulated 
PP_3218 4.458655 2.257026 Upregulated 
PP_0171 4.721398 1.630422 Upregulated 
PP_0238 4.753847 3.278104 Upregulated 
PP_0170 5.00351 2.339204 Upregulated 
PP_3528 5.069399 3.16826 Upregulated 
PP_0241 5.169426 2.7298 Upregulated 
 
  

 
139 
 
Table S7. Gene ontology binning of ethanesulfonate (EtSO3) vs cysteine (L-Cys) grown Pseudomonas putida 
proteomes. 
Gene-Ontology-
Terms 
p-values Comprising genes Average 
Log2  
(fold 
change) 
sulfur compound 
metabolic process 
1.30E-08 PP_3775, PP_1654, PP_0236, PP_1832, PP_3819, 
PP_2327, PP_0363, PP_0169, PP_3528, PP_0237, 
PP_1303, PP_2528, PP_0658, PP_0238, PP_0233, 
PP_1304, PP_3219, PP_0230, PP_2371, PP_2765, 
PP_2308 
2.562349 
alkanesulfonate 
catabolic process 
2.11E-06 PP_0236, PP_3219, PP_2765, PP_0238 3.445859 
sulfur compound 
catabolic process 
5.01E-05 PP_0236, PP_3219, PP_2765, PP_0238, PP_0230 3.322575 
organic acid catabolic 
process 
1.16E-04 PP_3775, PP_5270, PP_2755, PP_5192, PP_0223, 
PP_4620, PP_0224, PP_3443, PP_1001, PP_4475, 
PP_2308, PP_0999, PP_2762, PP_0236, PP_3219, 
PP_2765, PP_0238 
2.329539 
alpha-amino acid 
metabolic process 
1.63E-04 PP_3775, PP_5270, PP_1654, PP_2755, PP_1832, 
PP_5192, PP_2327, PP_4620, PP_0224, PP_0082, 
PP_2528, PP_5183, PP_0658, PP_3778, PP_3790, 
PP_1001, PP_2453, PP_4475, PP_0999, PP_2762 
1.725094 
small molecule 
catabolic process 
1.80E-04 PP_0542, PP_3775, PP_5270, PP_2755, PP_5192, 
PP_0223, PP_4620, PP_0224, PP_3443, PP_1001, 
PP_4475, PP_2308, PP_0999, PP_2762, PP_0236, 
PP_3219, PP_2765, PP_0238 
2.301439 
organic acid metabolic 
process 
1.80E-04 PP_3775, PP_5270, PP_1654, PP_1752, PP_0236, 
PP_2338, PP_2755, PP_1832, PP_5192, PP_0223, 
PP_2327, PP_0363, PP_1505, PP_4620, PP_0224, 
PP_0082, PP_2528, PP_5183, PP_0658, PP_3778, 
PP_0238, PP_5035, PP_2170, PP_3443, PP_3787, 
PP_3219, PP_3790, PP_1001, PP_2453, PP_2765, 
PP_4475, PP_2308, PP_0999, PP_2762 
1.854647 
response to oxidative 
stress 
1.98E-04 PP_1638, PP_3819, PP_0235, PP_2439, PP_1873, 
PP_1859, PP_0777 
1.8825 
cellular oxidant 
detoxification 
1.98E-04 PP_4021, PP_3819, PP_3639, PP_2439, PP_2422, 
PP_0777, PP_0235 
1.868817 
amino acid catabolic 
process 
2.44E-04 PP_5270, PP_3775, PP_3443, PP_2762, PP_2755, 
PP_0224, PP_4620, PP_5192, PP_4475, PP_0999, 
PP_1001 
1.907815 
alpha-amino acid 
catabolic process 
3.15E-04 PP_2762, PP_2755, PP_0224, PP_5270, PP_3775, 
PP_4620, PP_5192, PP_4475, PP_0999, PP_1001 
1.975649 
detoxification 3.51E-04 PP_4021, PP_3819, PP_3639, PP_2439, PP_2422, 
PP_0777, PP_0235 
1.868817 
cellular detoxification 3.51E-04 PP_4021, PP_3819, PP_3639, PP_2439, PP_2422, 
PP_0777, PP_0235 
1.868817 
amino acid metabolic 
process 
5.05E-04 PP_3775, PP_5270, PP_1654, PP_2755, PP_1832, 
PP_5192, PP_2327, PP_4620, PP_0224, PP_0082, 
PP_2528, PP_5183, PP_0658, PP_3778, PP_3443, 
PP_0542, PP_3790, PP_1001, PP_2453, PP_4475, 
PP_0999, PP_2762 
1.70705 
L-amino acid metabolic 
process 
6.36E-04 PP_3775, PP_1654, PP_1832, PP_5192, PP_2327, 
PP_4620, PP_2528, PP_5183, PP_0658, PP_3778, 
PP_3790, PP_1001, PP_2453, PP_4475, PP_0999 
1.603268 

 
140 
 
proteinogenic amino 
acid metabolic process 
0.0006362 PP_3775, PP_1654, PP_1832, PP_5192, PP_2327, 
PP_4620, PP_2528, PP_5183, PP_0658, PP_3778, 
PP_3790, PP_1001, PP_2453, PP_4475, PP_0999 
1.603268 
catabolic process 7.74E-04 PP_3832, PP_3775, PP_5270, PP_1638, PP_0236, 
PP_2755, PP_5192, PP_0223, PP_3784, PP_4620, 
PP_0224, PP_2439, PP_4038, PP_5183, PP_5041, 
PP_0238, PP_3443, PP_0542, PP_3219, PP_0230, 
PP_1001, PP_2765, PP_4475, PP_2308, PP_0999, 
PP_2762 
2.122481 
organonitrogen 
compound catabolic 
process 
8.50E-04 PP_3775, PP_5270, PP_1638, PP_2755, PP_5192, 
PP_3784, PP_4620, PP_0224, PP_4038, PP_5183, 
PP_3443, PP_0542, PP_1001, PP_4475, PP_0999, 
PP_2762 
1.856595 
cellular catabolic 
process 
8.76E-04 PP_3832, PP_3775, PP_5270, PP_1638, PP_0236, 
PP_2755, PP_5192, PP_0223, PP_4620, PP_0224, 
PP_2439, PP_4038, PP_0238, PP_3443, PP_3219, 
PP_0230, PP_1001, PP_2765, PP_4475, PP_2308, 
PP_0999, PP_2762 
2.260023 
organic substance 
catabolic process 
9.17E-04 PP_3832, PP_3775, PP_5270, PP_1638, PP_0236, 
PP_2755, PP_5192, PP_0223, PP_3784, PP_4620, 
PP_0224, PP_4038, PP_5183, PP_5041, PP_0238, 
PP_3443, PP_0542, PP_3219, PP_1001, PP_2765, 
PP_4475, PP_2308, PP_0999, PP_2762 
2.108766 
regulation of translation 9.73E-04 PP_0951, PP_3832, PP_0493, PP_5502, PP_5700 1.878618 
sulfate assimilation 0.001028391 PP_1304, PP_1303, PP_2371 1.986986 
regulation of amide 
metabolic process 
0.001221001 PP_3832, PP_0951, PP_0493, PP_5502, PP_5700 1.878618 
post-transcriptional 
regulation of gene 
expression 
0.001512584 PP_0951, PP_3832, PP_0493, PP_5502, PP_5700 1.878618 
regulation of protein 
metabolic process 
0.002694939 PP_0951, PP_3832, PP_0493, PP_5502, PP_5700 1.878618 
oxoacid metabolic 
process 
0.002847948 PP_3775, PP_5270, PP_1654, PP_1752, PP_2338, 
PP_2755, PP_1832, PP_5192, PP_0223, PP_2327, 
PP_0363, PP_1505, PP_4620, PP_0224, PP_0082, 
PP_2528, PP_5183, PP_0658, PP_3778, PP_5035, 
PP_2170, PP_3443, PP_3787, PP_3790, PP_1001, 
PP_2453, PP_4475, PP_2308, PP_0999, PP_2762 
1.642485 
sulfur amino acid 
biosynthetic process 
0.003785409 PP_2528, PP_0658, PP_1832, PP_1654, PP_2327 1.604914 
carboxylic acid 
metabolic process 
0.003976838 PP_3775, PP_5270, PP_1654, PP_2338, PP_2755, 
PP_1832, PP_5192, PP_0223, PP_2327, PP_0363, 
PP_1505, PP_4620, PP_0224, PP_0082, PP_2528, 
PP_5183, PP_0658, PP_3778, PP_5035, PP_2170, 
PP_3443, PP_3787, PP_3790, PP_1001, PP_2453, 
PP_4475, PP_2308, PP_0999, PP_2762 
1.655154 
carboxylic acid 
catabolic process 
0.005029989 PP_3775, PP_5270, PP_2755, PP_5192, PP_0223, 
PP_4620, PP_0224, PP_3443, PP_1001, PP_4475, 
PP_2308, PP_0999, PP_2762 
1.986056 
sulfur compound 
biosynthetic process 
0.005862752 PP_2528, PP_0658, PP_1832, PP_1654, PP_2327, 
PP_0363, PP_1304, PP_1303 
1.789614 
proteinogenic amino 
acid catabolic process 
0.006901904 PP_3775, PP_4620, PP_5192, PP_4475, PP_0999, 
PP_1001 
1.746612 
L-amino acid catabolic 
process 
0.006901904 PP_3775, PP_4620, PP_5192, PP_4475, PP_0999, 
PP_1001 
1.746612 
sulfate transport 0.007361255 PP_5171, PP_5168, PP_4305 2.483414 
sulfate transmembrane 
transport 
0.007361255 PP_5171, PP_5168, PP_4305 2.483414 

 
141 
 
sulfur compound 
transport 
0.007572609 PP_0233, PP_5168, PP_5171, PP_4305 2.77574 
sulfur amino acid 
metabolic process 
0.008911263 PP_2528, PP_0658, PP_1832, PP_1654, PP_2327 1.604914 
arginine catabolic 
process 
0.009541692 PP_4475, PP_0999, PP_1001 1.285307 
cellular response to 
oxidative stress 
0.012059418 PP_1638, PP_3819, PP_0235 2.556261 
inorganic anion 
transport 
0.012733831 PP_5171, PP_5168, PP_4305, PP_0241, PP_5325 2.771108 
tricarboxylic acid cycle 0.014212796 PP_2925, PP_1505, PP_1251, PP_2338 1.234613 
glutamine family amino 
acid catabolic process 
0.014922521 PP_4475, PP_0999, PP_1001 1.285307 
proteinogenic amino 
acid biosynthetic 
process 
0.017694384 PP_1654, PP_2327, PP_5183, PP_3778, PP_2528, 
PP_0658, PP_1832, PP_3790 
1.512873 
L-amino acid 
biosynthetic process 
0.017694384 PP_1654, PP_2327, PP_5183, PP_3778, PP_2528, 
PP_0658, PP_1832, PP_3790 
1.512873 
aspartate family amino 
acid metabolic process 
0.017970288 PP_3775, PP_2453, PP_2528, PP_0658, PP_1832, 
PP_3790 
1.586075 
leucine metabolic 
process 
0.018136598 PP_2762, PP_2755, PP_0224 2.715168 
negative regulation of 
cellular metabolic 
process 
0.019509573 PP_2143, PP_5035, PP_1428, PP_5325, PP_0951, 
PP_3832 
1.219298 
cysteine metabolic 
process 
0.02170498 PP_1654, PP_2327, PP_2528 1.487849 
negative regulation of 
metabolic process 
0.022853645 PP_3832, PP_1428, PP_5325, PP_5035, PP_0951, 
PP_2143 
1.219298 
small molecule 
metabolic process 
0.024360696 PP_3775, PP_5270, PP_1654, PP_1752, PP_0236, 
PP_2338, PP_2755, PP_1832, PP_5192, PP_0223, 
PP_2327, PP_0363, PP_0516, PP_1505, PP_4620, 
PP_0224, PP_0082, PP_4038, PP_2528, PP_5183, 
PP_0658, PP_3778, PP_0238, PP_5035, PP_2170, 
PP_3443, PP_3787, PP_0542, PP_3219, PP_3790, 
PP_1001, PP_2453, PP_2765, PP_4475, PP_2308, 
PP_0999, PP_2762 
1.842007 
branched-chain amino 
acid catabolic process 
0.02562894 PP_2762, PP_2755, PP_0224 2.715168 
cellular response to 
chemical stress 
0.029907903 PP_1638, PP_3819, PP_0235 2.556261 
cell redox homeostasis 0.029907903 PP_3819, PP_2439, PP_0235 2.316089 
negative regulation of 
cellular process 
0.031027526 PP_4342, PP_2143, PP_5035, PP_1428, PP_5325, 
PP_0951, PP_3832 
1.341713 
alpha-amino acid 
biosynthetic process 
0.034743205 PP_1654, PP_2327, PP_5183, PP_3778, PP_2528, 
PP_0658, PP_1832, PP_3790, PP_0082 
1.475446 
negative regulation of 
biological process 
0.034950107 PP_3832, PP_1428, PP_5325, PP_5035, PP_0951, 
PP_2143, PP_4342 
1.341713 
non-proteinogenic 
amino acid metabolic 
process 
0.03631931 PP_2528, PP_5270, PP_3443, PP_1001 1.230102 
methionine biosynthetic 
process 
0.039520327 PP_2528, PP_0658, PP_1832 1.688665 
methionine metabolic 
process 
0.039520327 PP_2528, PP_0658, PP_1832 1.688665 
cell communication 0.039973717 PP_2143, PP_1217, PP_3706, PP_0168 1.460717 
negative regulation of 
nitrogen compound 
metabolic process 
0.044840045 PP_2143, PP_5035, PP_1428, PP_0951, PP_3832 1.215983 

 
142 
 
SOS response 0.044844948 PP_2143, PP_1217, PP_3706 1.423963 
organonitrogen 
compound metabolic 
process 
0.045263264 PP_4111, PP_3775, PP_5270, PP_1638, PP_1654, 
PP_2755, PP_1832, PP_5192, PP_3784, PP_3819, 
PP_1873, PP_0541, PP_2327, PP_0363, PP_3722, 
PP_0325, PP_0516, PP_0533, PP_4034, PP_4620, 
PP_0493, PP_0224, PP_0082, PP_4038, PP_2528, 
PP_5183, PP_4949, PP_0658, PP_4264, PP_4657, 
PP_3778, PP_5035, PP_3443, PP_0203, PP_3781, 
PP_0542, PP_0323, PP_2143, PP_3790, PP_0397, 
PP_1001, PP_2453, PP_4475, PP_2308, PP_0999, 
PP_2762 
1.684118 
biogenic amine 
metabolic process 
0.047890056 PP_0542, PP_0541, PP_5183, PP_0082 1.389539 
negative regulation of 
biosynthetic process 
0.04813604 PP_2143, PP_5035, PP_1428, PP_0951, PP_3832 1.215983 
negative regulation of 
cellular biosynthetic 
process 
0.04813604 PP_2143, PP_5035, PP_1428, PP_0951, PP_3832 1.215983 
negative regulation of 
macromolecule 
biosynthetic process 
0.04813604 PP_2143, PP_5035, PP_1428, PP_0951, PP_3832 1.215983 
 
  

 
143 
 
Table S8.  Differentially produce proteins of sulfate (MgSO 4) vs sulfate (MgSO 4) and ethanesulfonate (EtSO 3) 
grown Pseudomonas putida proteomes. 
PP number Log2 (fold change) Log (p-value) Up or downregulated 
PP_0158 -2.68055 1.557711 Downregulated 
PP_0238 -2.42524 1.968717 Downregulated 
PP_1454 -1.58997 2.021169 Downregulated 
PP_3232 -1.58906 1.443597 Downregulated 
PP_1971 -1.53525 1.87548 Downregulated 
PP_2874 -1.42362 1.477544 Downregulated 
PP_5393 -1.38446 1.845838 Downregulated 
PP_0367 -1.37097 1.737148 Downregulated 
PP_3288 -1.26784 1.838282 Downregulated 
PP_4395 -1.21599 1.572006 Downregulated 
PP_0235 -1.14888 1.730932 Downregulated 
PP_5502 -1.09729 1.888832 Downregulated 
PP_1000 -1.00006 2.351713 Downregulated 
PP_0434 1.032978 1.655636 Upregulated 
PP_3778 1.054317 1.70363 Upregulated 
PP_0736 1.082487 1.91139 Upregulated 
PP_3781 1.168856 1.993221 Upregulated 
PP_3191 1.253734 2.351019 Upregulated 
PP_3783 1.278517 1.896215 Upregulated 
PP_3785 1.341982 1.737342 Upregulated 
PP_3784 1.395055 1.595182 Upregulated 
PP_3788 1.591675 1.828185 Upregulated 
PP_3786 1.755686 1.61817 Upregulated 
PP_0797 2.223209 1.532357 Upregulated 
 
  

 
144 
 
Table S9. Gene ontology binning of sulfate (MgSO4) vs sulfate (MgSO4) and ethanesulfonate (EtSO3) grown 
Pseudomonas putida proteomes. 
Gene-Ontology-
Terms 
p-values Comprising genes Average Log2  
(fold change) 
organic acid catabolic 
process 0.004057 
PP_0158, PP_1000, 
PP_0238 -2.03528 
small molecule catabolic 
process 0.00583 
PP_0158, PP_1000, 
PP_0238 -2.03528 
cellular catabolic process 0.019137 
PP_0238, PP_0158, 
PP_1000 -2.03528 
organic substance catabolic 
process 0.027166 
PP_0238, PP_0158, 
PP_1000 -2.03528 
organonitrogen compound 
metabolic process 0.012381 
PP_3191, PP_3781, 
PP_3784, PP_0434, 
PP_0736, PP_3778 1.164571 
biosynthetic process 0.012588 
PP_3191, PP_3788, 
PP_3781, PP_3786, 
PP_0736, PP_3778 1.317793 
organic substance 
metabolic process 0.014228 
PP_3191, PP_3788, 
PP_3781, PP_3786, 
PP_3784, PP_0434, 
PP_0736, PP_3778 1.291849 
organonitrogen compound 
biosynthetic process 0.025087 
PP_3191, PP_3781, 
PP_0736, PP_3778 1.139849 
amino acid metabolic 
process 0.025735 
PP_3191, PP_3788, 
PP_3778 1.299909 
nitrogen compound 
metabolic process 0.029703 
PP_3191, PP_3781, 
PP_3786, PP_3784, 
PP_0434, PP_0736, 
PP_3778 1.249016 
metabolic process 0.035642 
PP_3191, PP_3788, 
PP_3781, PP_3786, 
PP_3784, PP_0434, 
PP_0736, PP_3778 1.291849 
organic substance catabolic 
process 0.040229 
PP_3191, PP_3784, 
PP_0434 1.227256 
 
  

 
145 
 
Table S10.  Differentially produce proteins of sulfate (MgSO 4) vs sulfate (MgSO 4) and cysteine (L -Cys) grown 
Pseudomonas putida proteomes. 
PP number Log2 (fold change) Log (p-value) Up or downregulated 
PP_2435 -5.19904 2.946301 Downregulated 
PP_4523 -3.19366 1.39263 Downregulated 
PP_3232 -2.30708 1.444476 Downregulated 
PP_0052 -1.55967 1.325235 Downregulated 
PP_1574 -1.47974 2.258553 Downregulated 
PP_3946 -1.43984 1.442688 Downregulated 
PP_5379 -1.43561 1.60133 Downregulated 
PP_4435 -1.29354 1.352569 Downregulated 
PP_3822 -1.11611 2.341253 Downregulated 
PP_0799 -1.07961 1.561163 Downregulated 
PP_1567 -1.05874 2.718038 Downregulated 
PP_2345 -1.04847 1.371705 Downregulated 
PP_0779 -1.03775 1.445664 Downregulated 
PP_4267 -1.03237 1.424413 Downregulated 
PP_5377 -1.01344 1.487481 Downregulated 
PP_0620 1.427543 2.255361 Upregulated 
PP_4055 1.759891 1.390642 Upregulated 
PP_2652 2.057512 2.116225 Upregulated 
PP_3790 2.063091 1.648319 Upregulated 
PP_3785 3.918949 1.39311 Upregulated 
PP_3788 4.204661 2.543695 Upregulated 
PP_3786 4.366212 1.663909 Upregulated 
PP_2036 5.243183 1.555119 Upregulated 
 
  

 
146 
 
Table S11. Differentially produce proteins of ethanesulfonate (EtSO 3) vs sulfate (MgSO 4) and ethanesulfonate 
(EtSO3) grown Pseudomonas putida proteomes. 
PP number Log2 (fold change) Log (p-value) Up or downregulated 
PP_4819 -2.42485 1.683325 Downregulated 
PP_3417 -2.2012 2.298652 Downregulated 
PP_2188 -2.19233 1.595889 Downregulated 
PP_4168 -2.12495 2.136074 Downregulated 
PP_2536 -1.70765 1.319479 Downregulated 
PP_4279 -1.63355 2.396547 Downregulated 
PP_0441 -1.60226 2.814814 Downregulated 
PP_1318 -1.53514 1.590854 Downregulated 
PP_1545 -1.48744 2.141565 Downregulated 
PP_4192 -1.48105 1.776806 Downregulated 
PP_1016 -1.44369 1.7215 Downregulated 
PP_3377 -1.43931 1.599081 Downregulated 
PP_4323 -1.38192 1.410848 Downregulated 
PP_3550 -1.28087 1.342553 Downregulated 
PP_3143 -1.25625 1.793472 Downregulated 
PP_1319 -1.24855 2.00402 Downregulated 
PP_4193 -1.24699 1.561226 Downregulated 
PP_2322 -1.20233 1.65179 Downregulated 
PP_1993 -1.16085 1.790991 Downregulated 
PP_4904 -1.09139 1.702647 Downregulated 
PP_1442 -1.06668 1.46455 Downregulated 
PP_4261 -1.04147 2.659484 Downregulated 
PP_4234 -1.03878 1.615653 Downregulated 
PP_5333 -1.03032 1.933589 Downregulated 
PP_3777 -1.02001 2.331913 Downregulated 
PP_4243 -1.00604 1.778586 Downregulated 
PP_5283 1.018226 1.560249 Upregulated 
PP_5008 1.053338 2.046617 Upregulated 
PP_3128 1.077015 1.534128 Upregulated 
PP_2118 1.109087 2.62081 Upregulated 
PP_0363 1.148254 1.554198 Upregulated 
PP_5270 1.182703 1.810734 Upregulated 
PP_3794 1.211278 1.843043 Upregulated 
PP_3706 1.229179 2.428087 Upregulated 
PP_4305 1.233918 1.436934 Upregulated 
PP_4924 1.319488 1.442227 Upregulated 
PP_0542 1.331678 1.553879 Upregulated 
PP_2771 1.341606 1.373131 Upregulated 
PP_1832 1.369457 1.391089 Upregulated 
PP_3602 1.402281 2.883459 Upregulated 
PP_4504 1.484221 1.568711 Upregulated 
PP_0234 1.556488 2.772944 Upregulated 
PP_3415 1.580901 3.657499 Upregulated 
PP_5168 1.610102 2.816306 Upregulated 

 
147 
 
PP_2439 1.630196 2.93394 Upregulated 
PP_2755 1.78612 2.656488 Upregulated 
PP_2752 2.026713 2.391185 Upregulated 
PP_5165 2.155313 1.444287 Upregulated 
PP_1185 2.205357 1.736716 Upregulated 
PP_4342 2.222587 1.400818 Upregulated 
PP_4927 2.240646 1.323463 Upregulated 
PP_1062 2.385593 2.482104 Upregulated 
PP_1186 2.761817 2.818779 Upregulated 
PP_0223 2.766024 4.219259 Upregulated 
PP_0236 2.768072 2.548874 Upregulated 
PP_2762 2.851404 2.632618 Upregulated 
PP_2765 2.874036 3.251248 Upregulated 
PP_0533 2.979085 2.388152 Upregulated 
PP_5171 3.025552 1.757249 Upregulated 
PP_0224 3.100829 3.37103 Upregulated 
PP_0235 3.154155 3.432271 Upregulated 
PP_3219 3.187987 2.373449 Upregulated 
PP_0221 3.388246 1.522107 Upregulated 
PP_0233 3.477012 1.507333 Upregulated 
PP_0169 3.563629 3.468866 Upregulated 
PP_0222 3.583009 2.778953 Upregulated 
PP_2770 3.645267 2.067197 Upregulated 
PP_2756 3.702125 1.398979 Upregulated 
PP_5172 3.872117 3.751747 Upregulated 
PP_0230 3.917516 2.739566 Upregulated 
PP_0237 4.175881 1.618088 Upregulated 
PP_0240 4.325387 3.291289 Upregulated 
PP_3528 4.372088 3.102413 Upregulated 
PP_3218 4.863511 3.577279 Upregulated 
PP_0170 5.109922 2.344438 Upregulated 
PP_0241 5.317473 2.59252 Upregulated 
PP_0207 5.393555 2.352323 Upregulated 
PP_0238 5.627051 3.761049 Upregulated 
PP_0171 5.726417 2.278495 Upregulated 
 
  

 
148 
 
Table S13. Gene ontology binning of ethanesulfonate (EtSO3) vs sulfate (MgSO4) and ethanesulfonate (EtSO3) 
grown Pseudomonas putida proteomes. 
Gene-Ontology-Terms p-values Comprising genes Average Log2  
(fold change) 
generation of precursor metabolites 
and energy 
0.00432 PP_4192, PP_1318, PP_4193, 
PP_1319 
-1.37793 
electron transport chain 0.012046 PP_1318, PP_4193, PP_1319 -1.34356 
transmembrane transport 0.044138 PP_3417, PP_0441, PP_1318, 
PP_3377, PP_4261, PP_1016 
-1.54385 
alkanesulfonate catabolic process 1.30E-08 PP_0236, PP_3219, PP_2765, 
PP_0238 
3.614287 
sulfur compound metabolic process 8.51E-08 PP_3219, PP_0237, PP_3528, 
PP_0238, PP_0363, PP_0236, 
PP_1832, PP_0233, PP_2765, 
PP_0230, PP_0169 
3.316453 
sulfur compound catabolic process 9.63E-08 PP_0236, PP_3219, PP_2765, 
PP_0238, PP_0230 
3.674932 
alkanesulfonate metabolic process 1.92E-07 PP_0236, PP_3219, PP_2765, 
PP_0238 
3.614287 
small molecule catabolic process 1.92E-05 PP_0542, PP_0224, PP_5270, 
PP_2762, PP_2755, PP_0223, 
PP_0236, PP_3219, PP_2765, 
PP_0238 
2.74759 
organic acid catabolic process 4.63E-05 PP_0224, PP_5270, PP_2762, 
PP_2755, PP_0223, PP_0236, 
PP_3219, PP_2765, PP_0238 
2.904914 
sulfur compound transport 6.80E-05 PP_0233, PP_5168, PP_5171, 
PP_4305 
2.336646 
leucine catabolic process 1.45E-04 PP_2762, PP_2755, PP_0224 2.579451 
cellular catabolic process 1.49E-04 PP_0224, PP_3219, PP_5270, 
PP_0238, PP_2762, PP_0236, 
PP_2755, PP_2765, PP_2439, 
PP_0230, PP_0223 
2.881085 
sulfate transport 1.98E-04 PP_5171, PP_5168, PP_4305 1.956524 
sulfate transmembrane transport 1.98E-04 PP_5171, PP_5168, PP_4305 1.956524 
catabolic process 2.78E-04 PP_0224, PP_3219, PP_0542, 
PP_5270, PP_0238, PP_2762, 
PP_0236, PP_2755, PP_2765, 
PP_2439, PP_0230, PP_0223 
2.751968 
leucine metabolic process 5.28E-04 PP_2762, PP_2755, PP_0224 2.579451 
inorganic anion transport 6.61E-04 PP_5171, PP_5168, PP_4305, 
PP_0241 
2.796761 
branched-chain amino acid catabolic 
process 
7.78E-04 PP_2762, PP_2755, PP_0224 2.579451 
inorganic anion transmembrane 
transport 
0.001695 PP_5171, PP_5168, PP_4305 1.956524 
organic substance catabolic process 0.00194 PP_0224, PP_3219, PP_0542, 
PP_5270, PP_0238, PP_2762, 
PP_0236, PP_2755, PP_2765, 
PP_0223 
2.74759 
alpha-amino acid catabolic process 0.007429 PP_2762, PP_2755, PP_0224, 
PP_5270 
2.230264 

 
149 
 
branched-chain amino acid 
metabolic process 
0.008835 PP_2762, PP_2755, PP_0224 2.579451 
amino acid catabolic process 0.012261 PP_5270, PP_2762, PP_2755, 
PP_0224 
2.230264 
organic acid metabolic process 0.012417 PP_0224, PP_3219, PP_5270, 
PP_0238, PP_0363, PP_2762, 
PP_0236, PP_2755, PP_1832, 
PP_2765, PP_0223 
2.605631 
carboxylic acid catabolic process 0.025028 PP_0224, PP_5270, PP_2762, 
PP_2755, PP_0223 
2.337416 
organonitrogen compound catabolic 
process 
0.041605 PP_0224, PP_0542, PP_5270, 
PP_2762, PP_2755 
2.050547 
 
  

 
150 
 
Table S14. Differentially produce proteins of ethanesulfonate (EtSO 3) vs cysteine (L -Cys) and ethanesulfonate 
(EtSO3) grown Pseudomonas putida proteomes. 
PP number Log2 (fold change) Log (p-value) Up or downregulated 
PP_1110 -3.67924 1.648509 Downregulated 
PP_1419 -3.02271 1.326666 Downregulated 
PP_4328 -1.82697 1.59208 Downregulated 
PP_4576 -1.52584 1.352905 Downregulated 
PP_4359 -1.15107 1.950722 Downregulated 
PP_5029 -1.12028 1.442403 Downregulated 
PP_0904 -1.05098 1.759223 Downregulated 
PP_4502 -1.01968 1.498326 Downregulated 
PP_0779 -1.01855 1.326941 Downregulated 
PP_5388 -1.01836 1.554521 Downregulated 
PP_0992 1.242365 1.398337 Upregulated 
 
  

 
151 
 
Table S15. Differentially produce proteins of cysteine (L -Cys) vs sulfate (MgSO 4) and cysteine (L -Cys) grown 
Pseudomonas putida proteomes. 
PP number Log2 (fold change) Log (p-value) Up or downregulated 
PP_0679 -1.17234 1.375444 Downregulated 
PP_1539 -1.42654 1.452095 Downregulated 
PP_0868 -1.16575 1.530783 Downregulated 
PP_5270 -1.06434 1.575056 Downregulated 
PP_2460 -2.75215 1.607281 Downregulated 
PP_5051 -1.26872 1.913307 Downregulated 
PP_3775 -1.03261 2.276916 Downregulated 
PP_1545 -1.08953 2.459154 Downregulated 
PP_4004 -1.22879 2.572564 Downregulated 
 
  

 
152 
 
Table S16. Gene ontology binning of cysteine (L-Cys) vs sulfate (MgSO4) and cysteine (L-Cys) grown 
Pseudomonas putida proteomes. 
Gene-Ontology-
Terms 
p-values Comprising genes Average Log2  
(fold change) 
small molecule catabolic 
process 0.001819 
PP_5270, PP_3775, 
PP_2460 -4.8491 
cellular catabolic process 0.006268 
PP_2460, PP_5270, 
PP_3775 -4.8491 
organic substance 
catabolic process 0.009073 
PP_2460, PP_5270, 
PP_3775 -4.8491 
catabolic process 0.012165 
PP_2460, PP_5270, 
PP_3775 -4.8491 
 
  

 
153 
 
Table S17. Differentially produce proteins of cysteine (L -Cys) vs ethanesulfonate (EtSO 3) and cysteine (L -Cys) 
grown Pseudomonas putida proteomes. 
PP number Log2 (fold change) Log (p-value) Up or downregulated 
PP_0226 -1.32523 1.706969 Downregulated 
PP_1349 -1.15528 1.35344 Downregulated 
PP_5182 -1.12869 1.304561 Downregulated 
PP_3286 1.422526 1.450653 Upregulated 
PP_0086 2.034033 1.620057 Upregulated 
 
  

 
154 
 
Table S18. Sulfur source and strain fitness score (Fscore) matrix. 
 
KT2440 
ΔcysDNC 
ΔcysNC 
ΔcysH 
ΔcysB 
Δssu 
Δtau 
Δssu tau 
ΔssuD 
ΔssuBC 
ΔtauD 
ΔtauABC 
ΔssuD tauABC 
ΔtauD ssuCB 
L-cysteine 0.65 0.62 0.59 0.83 0.54 0.66 0.82 0.63 0.91 0.62 0.63 0.68 0.75 0.66 
Sulfate 0.67 0.04 0.04 0.04 0.04 0.70 0.78 0.67 0.80 0.54 0.70 0.74 0.64 0.79 
Ethanesulfonate 0.61 0.56 0.44 0.71 0.04 0.04 0.73 0.04 0.04 0.51 0.62 0.67 0.04 0.61 
Taurine 0.60 0.55 0.42 0.70 0.04 0.50 0.64 0.04 0.63 0.58 0.63 0.63 0.36 0.68 
F-EtSO3 0.37 0.38 0.37 0.41 0.05 0.25 0.36 0.21 0.26 0.37 0.34 0.36 0.28 0.41 
3F-EtSO3 0.12 0.04 0.04 0.04 0.04 0.04 0.17 0.04 0.28 0.07 0.14 0.18 0.04 0.09 
Br-EtSO3 0.12 0.15 0.09 0.10 0.04 0.04 0.09 0.11 0.04 0.12 0.14 0.10 0.04 0.15 
Cl-EtSO3 0.45 0.35 0.35 0.35 0.04 0.04 0.23 0.04 0.04 0.31 0.43 0.35 0.04 0.36 
trimethylsililpropanesulfonate 0.59 0.62 0.62 0.45 0.07 0.16 0.47 0.10 0.04 0.46 0.13 0.48 0.04 0.08 
3-sulfopropyl acrylate 0.57 0.50 0.43 0.63 0.04 0.04 0.64 0.04 0.04 0.46 0.53 0.55 0.04 0.56 
3-NH3-1-propanesulfonic acid 0.62 0.46 0.46 0.61 0.04 0.54 0.68 0.50 0.67 0.53 0.55 0.57 0.58 0.50 
3-(1-pyridino)-1-propanesulfonate 0.21 0.10 0.17 0.25 0.04 0.04 0.24 0.04 0.04 0.04 0.22 0.37 0.04 0.04 
(1s)-(+)-10-Camphorsulfonic acid 0.04 0.04 0.04 0.04 0.04 0.04 0.05 0.04 0.04 0.04 0.04 0.04 0.04 0.04 
HEPES 0.51 0.35 0.23 0.49 0.04 0.04 0.49 0.04 0.04 0.04 0.49 0.45 0.04 0.04 
MOPS 0.60 0.53 0.43 0.64 0.04 0.04 0.65 0.04 0.04 0.22 0.61 0.56 0.07 0.24 
6:2 FTSA 0.35 0.04 0.09 0.04 0.04 0.09 0.49 0.19 0.77 0.18 0.25 0.56 0.33 0.46 
3-Cl-2-OH-1-propanesulfonate 0.63 0.54 0.44 0.67 0.04 0.04 0.71 0.04 0.23 0.55 0.59 0.62 0.04 0.70 
aminomethanesulfonic acid 0.66 0.54 0.35 0.52 0.04 0.64 0.74 0.60 0.72 0.60 0.63 0.66 0.59 0.75 
diphenylamine-4 sulfonate 0.64 0.04 0.04 0.04 0.04 0.63 0.69 0.60 0.72 0.58 0.61 0.66 0.60 0.64 
NSA 0.04 0.04 0.04 0.04 0.04 0.04 0.10 0.04 0.04 0.04 0.04 0.04 0.04 0.04 
 
  

 
155 
 
 
Figure S1. Visualzed targeted metabolomics method for ethanesulfonate quantification. 


 
156 
 
 
Figure S2. Average Log2 fold change of gene ontology terms binned from differentially produced proteins 
between MgSO4 and L-cys grown Pseudomonas putida proteomes. 
-5 -4 -3 -2 -1 0 1 2 3
inorganic anion transport
sulfur compound transport
sulfur compound metabolic process
sulfur compound catabolic process
alkanesulfonate catabolic process
sulfate transport
inorganic anion transmembrane transport
leucine catabolic process
branched-chain amino acid catabolic process
branched-chain amino acid metabolic process
organic acid catabolic process
small molecule catabolic process
organic substance catabolic process
cellular catabolic process
catabolic process
carboxylic acid catabolic process
organic acid metabolic process
alpha-amino acid catabolic process
amino acid catabolic process
cellular oxidant detoxification
cellular response to stimulus
sulfur compound metabolic process
cellular modified amino acid metabolic process
amide metabolic process
organonitrogen compound metabolic process
amino acid biosynthetic process
nitrogen compound metabolic process
metabolic process
organonitrogen compound biosynthetic process
L-amino acid biosynthetic process
carboxylic acid biosynthetic process
small molecule biosynthetic process
oxoacid metabolic process
organic substance metabolic process
dicarboxylic acid metabolic process
amino acid metabolic process
biosynthetic process
Average Fold Change (log2)

 
157 
 
 
Figure S3. Average Log2 fold change of gene ontology terms binned from differentially produced proteins 
between MgSO4 and EtSO3 grown Pseudomonas putida proteomes. 
-6 -4 -2 0 2 4
inorganic anion transport
sulfur compound transport
sulfur compound metabolic process
sulfur compound catabolic process
alkanesulfonate catabolic process
sulfate transport
inorganic anion transmembrane transport
leucine catabolic process
branched-chain amino acid catabolic process
branched-chain amino acid metabolic process
organic acid catabolic process
small molecule catabolic process
organic substance catabolic process
cellular catabolic process
catabolic process
carboxylic acid catabolic process
organic acid metabolic process
alpha-amino acid catabolic process
amino acid catabolic process
cellular oxidant detoxification
cellular response to stimulus
sulfur compound metabolic process
cellular modified amino acid metabolic process
amide metabolic process
organonitrogen compound metabolic process
amino acid biosynthetic process
nitrogen compound metabolic process
metabolic process
organonitrogen compound biosynthetic process
L-amino acid biosynthetic process
carboxylic acid biosynthetic process
small molecule biosynthetic process
oxoacid metabolic process
organic substance metabolic process
dicarboxylic acid metabolic process
amino acid metabolic process
biosynthetic process
Average Log2 Fold Change

 
158 
 
 
Figure S4. Average Log2 fold change of gene ontology terms binned from differentially produced proteins 
between EtSO3 and L-Cys grown Pseudomonas putida proteomes. 
0 1 2 3 4
negative regulation of biosynthetic process
negative regulation of cellular metabolic process
negative regulation of metabolic process
non-proteinogenic amino acid metabolic process
tricarboxylic acid cycle
arginine catabolic process
glutamine family amino acid catabolic process
negative regulation of cellular process
negative regulation of biological process
biogenic amine metabolic process
SOS response
cell communication
alpha-amino acid biosynthetic process
cysteine metabolic process
proteinogenic amino acid biosynthetic process
L-amino acid biosynthetic process
aspartate family amino acid metabolic process
L-amino acid metabolic process
proteinogenic amino acid metabolic process
sulfur amino acid biosynthetic process
sulfur amino acid metabolic process
oxoacid metabolic process
carboxylic acid metabolic process
organonitrogen compound metabolic process
methionine biosynthetic process
amino acid metabolic process
alpha-amino acid metabolic process
proteinogenic amino acid catabolic process
L-amino acid catabolic process
sulfur compound biosynthetic process
small molecule metabolic process
organic acid metabolic process
organonitrogen compound catabolic process
cellular oxidant detoxification
detoxification
cellular detoxification
regulation of translation
regulation of amide metabolic process
post-transcriptional regulation of gene expression
regulation of protein metabolic process
response to oxidative stress
amino acid catabolic process
alpha-amino acid catabolic process
carboxylic acid catabolic process
sulfate assimilation
organic substance catabolic process
catabolic process
cellular catabolic process
small molecule catabolic process
cell redox homeostasis
organic acid catabolic process
sulfate transport
sulfate transmembrane transport
cellular response to oxidative stress
cellular response to chemical stress
sulfur compound metabolic process
leucine metabolic process
branched-chain amino acid catabolic process
inorganic anion transport
sulfur compound transport
sulfur compound catabolic process
alkanesulfonate catabolic process
Average Log2 Fold Change

 
159 
 
 
 
Figure S4. Average Log2 fold change of gene ontology terms binned from differentially produced proteins 
between MgSO4 and MgSO4 and EtSO3 grown Pseudomonas putida proteomes. 
  
-3 -2 -1 0 1 2
organic acid catabolic process
cellular catabolic process
organonitrogen compound biosynthetic…
organic substance catabolic process
organic substance metabolic process
amino acid metabolic process
Average Log2 Fold chanage

 
160 
 
 
Figure S5. Average Log2 fold change of gene ontology terms binned from differentially produced proteins 
between EtSO3 and MgSO4 and EtSO3 grown Pseudomonas putida proteomes. 
 
Figure S6. Average Log2 fold change of gene ontology terms binned from differentially produced proteins 
between L-Cys and MgSO4 and L-Cys grown Pseudomonas putida proteomes. 
 
-2 -1 0 1 2 3 4
transmembrane transport
generation of precursor metabolites and energy
electron transport chain
sulfate transport
sulfate transmembrane transport
inorganic anion transmembrane transport
organonitrogen compound catabolic process
alpha-amino acid catabolic process
amino acid catabolic process
sulfur compound transport
carboxylic acid catabolic process
leucine catabolic process
leucine metabolic process
branched-chain amino acid catabolic process
branched-chain amino acid metabolic process
organic acid metabolic process
small molecule catabolic process
organic substance catabolic process
catabolic process
inorganic anion transport
cellular catabolic process
organic acid catabolic process
sulfur compound metabolic process
alkanesulfonate catabolic process
alkanesulfonate metabolic process
sulfur compound catabolic process
Average Log2 fold change
-2 -1.5 -1 -0.5 0
small molecule catabolic process
cellular catabolic process
organic substance catabolic process
catabolic process
Average Log2 fold change

 
161 
 
 
Figure S7. Control sulfur sources. Sulfur sources known to be metabolized by Pseudomonas putida. I) L-cysteine, 
II) sulfate, III) ethanesulfonate, IV) taurine. 
  


 
162 
 
 
Figure S8. Catalytic capacity sulfur sources. Sulfur sources used to determine the catalytic capacity of sulfur 
sulfonate acquisition enzymes in Pseudomonas putida . I) 3 -chloro-2-hydroxy-1-propanesulfonate, II) 
aminomethanesulfonic acid, III) diphenylamine-4-sulfonate 
 


 
163 
 
 
Figure S9. Import capacity sulfur sources. Sulfur sources used to determine the import capacity of sulfonate 
importing enzymes in Pseudomonas putida . I) fluoroethanesulfonate,  II) trifluoroethanesulfonate,  III) 
bromoethanesulfonate, IV) chloroethanesulfonate, V) trimethylsililpropanesulfonate, VI) 3-sulfopropyl acrylate, VII) 
3-amino-1-propanesulfonic acid, VIII) 3-(1-pyridino)-1-propanesulfonate, IX) (1s)-(+)-10-camphorsulfonic acid, X) 
4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid (HEPES), XI) 3-(N-morpholino)propanesulfonic acid (MOPS), 
XIII) 1-octanesulfonate, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8, tridecafluoro (6:2 FTSA). 
 


 
164 
 
 
 
Figure S10. Genetic organization of the ssuEADCB (top) and tauABCD (bottom) operons in Pseudomonas putida. 
Gene names correspond to PP numbers as follows: ssuE – PP_0236, ssuA – PP_0237, ssuD – PP_0238, ssuC – 
PP_0239, ssuB – PP_0240, tauA – PP_0233, tauB – PP_0232, tauC – PP_0231 and tauD – PP_0230. 
 
 
  


 
165 
 
Appendix II to Chapter 2: Upgrading the Chi.Bio system for 
automated cultivation, quantitative physiology analysis and 
adaptive laboratory evolution of biotechnologically-relevant 
bacteria 
 
Garret W. O'Connell1, Stefano Donati1, Filippo Federici1, Maria Gracia Victoria Alvan Vargas1, 
Aina Sendra-Ortiz1, Lachlan J. Munro1, Lars K. Nielsen2 & Pablo I. Nikel1 
  
1Novo Nordisk Center for Biosustainability, Systems Environmental Microbiology group 
2Novo Nordisk Center for Biosustainability, Automation group 
3University of Queensland 
  
Genomic analysis of Pseudomonas putida strains was performed at the Denmark Technical University, Center 
for Biosustainability, Biofoundry. Illumina sequencing (San Diego, CA, USA) was performed on purified genomic 
DNA and resulting data sets analyze with the GeneiousPrime. In this supplementary, vari ation is defined as a 
deviation from a reference genome. Variations can be insertions, disruption or single nucleotide polymorphisms 
(SNPs). Variations with 25% frequency were reported; variations with 50% freq uency or higher were considered 
for further analysis. 
 
Chi.Bio set up optimization for adaptive laboratory evolution and multi -omics sampling was met with 4 
major criteria: feed media sterility, reactor spill avoidance, facile sampling and effective aeration. To achieve media 
sterility, Chi.Bio units and reactors were placed and kept inside a laminar flow hood for the duration of the 
cultivations and feed media capped with DWK Life Science DURAN TM (Fischer Scientific) HPLC screw caps. To 
avoid spills and allow for effective sampling, custom made lids were designed and printed in high temp resin 
(FormLabs) material in a Form 3 (FormLabs) 3D printer; extended arms ensured any spill would fall outside of the 
Chi.Bio unit and sampling port above made for easy sampling with 5-10 cm syringe needle. For effective aeration 
and consistent vortex formation, stir bars of 20 x 0.6 mm were strictly used (Fischer Scientific). Further sterility was 
achieved by autoclaving all modular parts of the system in individual bags with media lids and reactors with lids 
kept separate. A typical experiment is started as follows: 
To begin, sterile feed media was capped with DWK Life Science DURANTM (Fischer Scientific) HPLC screw caps 
with one of the four connectors threaded with silicone tube and capped with barb -to-leur connections on either 
end. Reactor sets (glass vial + lid) were opened in the laminar flow hood and placed in the Chi.Bio reactor jacket. 
To cap the feed media bottles while maintaining sterility, the sterile feed media bottle and lid bag were opened 

 
166 
 
inside the laminar flow hood and attached by feeding the tube into the bottle first without contaminating the inlet or 
inlet tubing. A 0.22-0.45 µm leur lock filter was connected to the non-media facing end of the tubing. 
Prior to an experiment, the system was first sterilized and purged with 70% ethanol. To purge the system of any 
contamination, the inlet and outlets of pumps 1 and 2 were submerged in 70% ethanol and both pumps were kept 
in an ON state for 1-5 minutes (~100+ tubing volumes). Following the purge step, inlets and outlets were removed 
from the 70% ethanol and activated to clear residual ethanol before being connected to the feed media. Pump 1 
was connected to the luer lock of the feed media and activated to fi ll the system with media and purge any 
remaining residual ethanol before being connected to inlet of the desired Chi.Bio lid. Pump 1 and 2 are then 
connected and activated until the reactor is filled to the outlet spout. Reactors were inoculated via the sampling 
port with a 5-10 cm sterile needle and syringe. 
Following the completion of a Chi.Bio experiment, the pumps were turned off on the Chi.Bio system dashboard. 
All connections to the Chi.Bio lid were disconnected to isolate the reactor and prevent any spillage. Samples for 
cryostock and screening were taken via the sampling port before discarding the reactor. 
 
  

 
167 
 
Tables S1. Total variations found in SEM10, RA2, RA3 and RA6. 
Strain Total variations found1 Unique variations2 
SEM10 300 N/A 
RA2 325 80 
RA3 299 52 
RA6 308 75 
1 Total variations calculated as described in the M&M, variants reported with respect to the Pseudomonas putida 
KT2440 reference genome (https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000007565.2/). 
2 Unique variations as defined as mutations solely found in adapted strains. 
 
  

 
168 
 
Tables S2. Common variations to RA2, RA3 and RA6. 
Variation Region or locus tag affected1 Change Protein effect2 
Substitution PP_1650 GG → CC Substitution 
Deletion PP_1650 ΔG Frameshift 
Substitution PP_2984 GC → CT N/A 
Transversion Intergenic (PP_3486/ 3487) A → T  
Transition Intergenic (PP_4234/4235) A → G N/A 
Substitution Intergenic (PP_4234/4235) GC → TT N/A 
Transversion Intergenic (PP_4822/4823) C → G N/A 
Transversion Intergenic (PP_5172/5173) T → G N/A 
1 Intergenic regions affected are described with respect to flanking locus tag, locus tag refer to Pseudomonas 
putida KT2440 PP number. 
2 N/A refers to variations which do not cause any distinct protein affect. 
 
 
 
  

 
169 
 
Table S3. Common affected genes to RA2, RA3 and RA6. 
Affected gene1 Gene description Variation type2 Protein effect 
PP_1650 Sensor protein (gacS) Substitution P → G 
PP_1362 Pyruvate kinase II 
(pykA) 
Substitution, Insertion, 
Transition 
D → Y, Frameshift, 
Truncation 
PP_1397 Hypothetical protein Transversion, 
Substitution, 
Substitution 
None, AA → AP, A → 
P 
1 Affected genes bordering large deletions or regions of low coverage were not considered 
2 Variants are listed as found in RA2, RA3 and RA6 respectively. 
  

 
170 
 
Tables S4. Total variations found in rG1, rG1-E1 and rG1-E2. 
Strain Total variations found1 Unique variations2 
rG1 406 N/A 
rG1-E1 429 255  
rG1-E2 405 198 
1 Total variations calculated as described in the M&M, variants reported with respect to the Pseudomonas putida 
KT2440 reference genome (https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000007565.2/). 
2 Unique variations as defined as mutations solely found in adapted strains. 
 
 
 
  

 
171 
 
Table S5. Common affected genes to rG1-E1 and rG2-E2. 
Affected gene1 Gene description Variation type2 Protein effect 
PP_1231 quinolinate synthase iron -
sulfur cluster subunit (nadA) 
Substitution, 
substitution 
A → V, P → L 
 
1 Affected genes bordering large deletions or regions of low coverage were not considered 
2 Variants are listed as found in rG1-E1 and rG1-E2 respectively. 
  

 
172 
 
Tables S6. Common variations to rG1-E1 and rG1-E2. 
Variation Region or locus tag 
affected1 
Change Protein effect2 
Insertion Intergenic 
(PP_4887/4888) 
GCC N/A 
1 Intergenic regions affected are described with respect to flanking locus tag, locus tag refer to Pseudomonas 
putida KT2440 PP number. 
2 N/A refers to variations which do not cause any distinct protein affect. 
  

 
173 
 
Table S7. Relevant mutations unique to rG1-E1 and rG1-E2, respectively. 
 
Variation Region or locus 
tag affected1 
Change Protein effect2 Unique to 
Transversion Intergenic 
(gcvH_I/PP_0990) 
C→T N/A rG1-E1 
Transversion Intergenic 
(PP_1505/1506) 
G→C N/A rG1-E2 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  

 
174 
 
Table S8. Pseudomonas putida differentially expressed genes between T0 and T1. 
Enzyme Locus tag Log2 fold change 
glycogen synthase PP_4050 -3.43935 
aerobic cobaltochelatase subunit CobN PP_3507 -2.70256 
formyltetrahydrofolate deformylase PP_0327 -2.29994 
membrane protein PP_2006 -2.15346 
malate:quinone oxidoreductase PP_2925 -1.98088 
putative hydrolase PP_0711 -1.74614 
chaperone protein PP_2361 -1.72559 
3-oxoadipate CoA-transferase subunit A PP_3952 -1.69345 
AraC family transcriptional regulator PP_1395 -1.68493 
polyphosphate kinase PP_0712 -1.68322 
excinuclease ABC subunit A PP_3087 -1.63018 
hypothetical protein PP_1631 -1.49536 
3-hydroxyisobutyryl-CoA hydrolase PP_1412 -1.48448 
1,6-dihydroxycyclohexa-2,4-diene-1-
carboxylate dehydrogenase 
PP_3164 -1.45204 
heme oxygenase PP_1005 -1.39763 
dehydrogenase PP_1661 -1.31731 
two-component system response regulator PP_2942 -1.22214 
zinc ABC transporter ATP-binding protein PP_0118 -1.2202 
hypothetical protein PP_1660 -1.13154 
aminotransferase PP_3786 -1.12822 
dihydropyoverdine dehydrogenase PP_4215 -1.08209 
benzoate 1,2-dioxygenase subunit alpha PP_3161 -1.06434 
sugar ABC transporter substrate -binding 
protein 
PP_2264 -1.06217 

 
175 
 
oxygen-independent coproporphyrinogen III 
oxidase family protein 
PP_3781 -1.06167 
catechol 1,2-dioxygenase PP_3713 -1.02909 
non-ribosomal peptide synthetase PP_3788 1.007032 
threonine deaminase PP_3446 1.014547 
hypothetical protein PP_3787 1.0266 
hypothetical protein PP_3777 1.037628 
P-47-like protein PP_2007 1.048934 
catechol 1,2-dioxygenase PP_3166 1.067126 
polysaccharide biosynthesis/export protein PP_3126 1.095971 
hypothetical protein PP_1659 1.123339 
glyceraldehyde-3-phosphate dehydrogenase PP_3443 1.156503 
glyoxalase family protein PP_3444 1.170794 
aerotaxis receptor PP_4521 1.800824 
hypothetical protein PP_3785 2.080297 
benzoate 1,2 -dioxygenase electron transfer 
component 
PP_3163 2.206914 
pyrroline-5-carboxylate reductase PP_3778 2.590944 
hypothetical protein PP_3692 2.628976 
 
  

 
176 
 
Table S9. Binning of Pseudomonas putida differentially expressed genes between T0 and T1. 
Gene Ontology term1 Average Log2 fold change Consisting genes 
heme oxidation -3.43935 PP_1005 
tetrapyrrole metabolic process -2.46192 PP_1005, PP_3507 
glycogen biosynthetic process -2.15346 PP_4050 
glycogen metabolic process -2.15346 PP_4050 
energy reserve metabolic process -2.15346 PP_4050 
glucan biosynthetic process -2.15346 PP_4050 
threonine catabolic process -1.69345 PP_3446 
L-serine catabolic process -1.69345 PP_3446 
zinc ion transmembrane transport -1.63018 PP_0118 
response to zinc ion -1.63018 PP_0118 
zinc ion transport -1.63018 PP_0118 
response to metal ion -1.63018 PP_0118 
branched-chain amino acid metabolic 
process 
-1.57275 PP_3446, PP_1412 
alpha-amino acid catabolic process -1.57275 PP_1412, PP_3446 
valine catabolic process -1.45204 PP_1412 
polysaccharide transport -1.06434 PP_3126 
L-proline biosynthetic process 1.0266 PP_3778 
proline biosynthetic process 1.0266 PP_3778 
proline metabolic process 1.0266 PP_3778 
gamma-aminobutyric acid catabolic 
process 
1.067126 PP_3443 
gamma-aminobutyric acid metabolic 
process 
1.067126 PP_3443 
non-proteinogenic amino acid catabolic 
process 
1.067126 PP_3443 
DNA synthesis involved in DNA repair 1.123339 PP_3692 

 
177 
 
amino acid activation for nonribosomal 
peptide biosynthetic process 
1.170794 PP_3788 
secondary metabolite biosynthetic 
process 
1.170794 PP_3788 
metabolic process 1.47034 PP_3788, PP_3713, PP_3786, 
PP_3161, PP_3781, PP_3692, 
PP_3787, PP_3952, PP_3443, 
PP_3166, PP_3778, PP_3163 
cellular metabolic process 1.543566 PP_3713, PP_3161, PP_3781, 
PP_3692, PP_3787, PP_3952, 
PP_3443, PP_3166, PP_3778, 
PP_3163 
cellular catabolic process 2.033633 PP_3713, PP_3161, PP_3952, 
PP_3443, PP_3166 
catabolic process 2.033633 PP_3713, PP_3161, PP_3952, 
PP_3443, PP_3166 
aromatic compound catabolic process 2.27526 PP_3713, PP_3166, PP_3952, 
PP_3161 
beta-ketoadipate pathway 2.340248 PP_3952, PP_3166, PP_3713 
catechol-containing compound 
catabolic process 
2.60996 PP_3713, PP_3166 
catechol-containing compound 
metabolic process 
2.60996 PP_3713, PP_3166 
phenol-containing compound catabolic 
process 
2.60996 PP_3713, PP_3166 
organic hydroxy compound catabolic 
process 
2.60996 PP_3713, PP_3166 
phenol-containing compound metabolic 
process 
2.60996 PP_3713, PP_3166 
organic hydroxy compound metabolic 
process 
2.60996 PP_3713, PP_3166 

 
178 
 
organic cyclic compound catabolic 
process 
2.60996 PP_3713, PP_3166 
 
1 Gene Ontology terms were calculated with BioCyc gene enrichment for biological processes using the Fisher 
Exact statistic, no correction and reporting bins with p-values of <0.05 
 
 
 
  

 
179 
 
Table S10. Escherichia coli differentially expressed genes between T0 and T1. 
Enzyme Locus tag Log2 fold change 
N-acetylglucosamine-specific PTS enzyme 
IIABC component 
b0679 -1.24333 
cellulose phosphoethanolamine transferase b3538 -1.68634 
Rac prophage; uncharacterized protein YnaE b1375 -1.10504 
acetolactate synthase II subunit IlvG b4488 -3.10861 
antitoxin of the MqsRA toxin -antitoxin system / 
DNA-binding transcriptional repressor MqsA 
b3021 -1.05326 
acyl-CoA dehydrogenase b0221 -1.15603 
ferric citrate ABC transporter periplasmic 
binding protein 
b4290 -1.01068 
ATP-binding protein PhoH b1020 -1.24131 
 
 
  

 
180 
 
Table S11. Binning of Escherichia coli differentially expressed genes between T0 and T1. 
Gene Ontology term1 Average Log2 fold change Consisting genes 
valine biosynthetic process -3.10861 b4488 
valine biosynthetic process -3.10861 b4488 
valine metabolic process -3.10861 b4488 
isoleucine biosynthetic process -3.10861 b4488 
isoleucine metabolic process -3.10861 b4488 
cellulose biosynthetic process -1.68634 b3538 
cellulose metabolic process -1.68634 b3538 
beta-glucan biosynthetic process -1.68634 b3538 
beta-glucan metabolic process -1.68634 b3538 
glucan biosynthetic process -1.68634 b3538 
N-acetylglucosamine transport -1.24333 b0679 
peptidoglycan turnover -1.24333 b0679 
fatty acid beta-oxidation using acyl-CoA 
dehydrogenase -1.15603 b0221 
fatty acid beta-oxidation -1.15603 b0221 
import into cell -1.12701 b4290, b0679 
response to cold -1.10504 b1375 
response to iron ion -1.01068 b4290 
siderophore-dependent iron import into 
cell -1.01068 b4290 
1 Gene Ontology terms were calculated with BioCyc gene enrichment for biological processes using the Fisher 
Exact statistic, no correction and reporting bins with p-values of <0.05 
  

 
181 
 
Table S12. ATP, ADP and AMP concentrations of Pseudomonas putida and Escherichia coli at timepoints T0 and 
T1. 
   
Bacteria cultivated Biological 
replicate 
Timepoint [ATP] 
(µM) 
[ADP] 
(µM) 
[AMP] 
(µM) 
ATP/ADP ratio 
Pseudomonas putida 1 T0 131.04 7.72 8.85 16.98251 
Pseudomonas putida 2 T0 99.11 7.16 5.35 13.85148 
Pseudomonas putida 3 T0 132.09 10.83 6.70 12.19902 
Pseudomonas putida 1 T1 117.05 6.40 11.01 18.30089 
Pseudomonas putida 2 T1 117.59 8.03 4.79 14.64081 
Pseudomonas putida 3 T1 92.93 4.88 7.86 19.05857 
Escherichia coli 1 T0 106.22 7.69 6.31 13.806 
Escherichia coli 2 T0 112.57 8.47 7.14 13.29098 
Escherichia coli 3 T0 142.13 7.88 8.88 18.04081 
Escherichia coli 1 T1 161.21 10.67 11.86 15.10958 
Escherichia coli 2 T1 130.76 9.78 11.38 13.37404 
Escherichia coli 3 T1 137.10 10.15 10.57 13.51348 

 
182 
 
 
 
Figure S1. Modified Chi.Bio lids generated in this study 
 
 
 


 
183 
 
 
Figure S2. Supplementary 3D models generated in this study. 
 


 
184 
 
 
 
Figure S3. Lag phase of rG1 and adapted rG1-E1 and rG2-E2 grown on deBont medium with 20 mM acetate and 
80 mM formate. One way ANOVA analysis was performed using Graphpad Prism; two asterixis indicate p-values 
≤ 0.01, three indicates p-values less than ≤ 0.001 and four indicate less than ≤ 0.0001. 
 
 
 
 
 
 
 
 


 
185 
 
 
Figure S4. Lag phase of rG1 E. coli MG1655, 3_3 and 3_5 grown on M9 medium 2% w/v glucose and 1.2 % v/v 
butanol. One way ANOVA analysis was performed using Graphpad Prism; ns indicates p -values > 0.05, two 
asterixis indicate p-values ≤ 0.01, three indicates p-values less than ≤ 0.001 and four indicate less than ≤ 0.0001. 
 


 
186 
 
 
Figure S5. Binning of Pseudomonas putida differentially expressed genes between T0 and T1. Genes were binned 
by gene ontology terms using the BioCyc gene enrichment calculator. 
 
  


 
187 
 
 
Figure S6. Binning of Escherichia coli differentially expressed genes between T0 and T1. Genes were binned by 
gene ontology terms using the BioCyc gene enrichment calculator.  
 
  


 
188 
 
Appendix V to Chapter 5: Direct and lossless delivery of 
exogenous fatty acids to fatty acid synthesis for incorporation 
of fluorinated fatty acyl compounds 
Garret W. O'Connell1, Alexandre Perrin2, Pablo Ivan Nikel1  
   1Novo Nordisk Center for Biosustainability, Systems Environmental Microbiology group  
2Ecole Polytechnique, Centre de mathématiques appliquées 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
189 
 
Table S1. Fatty acid per strain deletion F score matrix. Header row indicate P. putida strains and left most column 
indicates fatty acids source. Total carbon content per fatty acid equates 40 mM (e.g. 5 mM Octanoate and 20 mM 
Acetate). Error’s indicate standard deviation (n=3) 
 
 
 
 
 
 
  
 Δpcaf-II ΔbktB ΔfadA Δpcaf-II 
bktB 
Δpcaf-II 
fadA 
ΔbktB 
fadA 
Δpcaf-II 
bktB fadA 
KT2440 
acetate 0.642356 0.636188 0.60967 0.577349 0.587669 0.575004 0.58284 0.585114 
propionate 0.610725 0.693547 0.678599 0.684991 0.650913 0.729569 0.735278 0.756458 
butyrate 0.891971 0.774212 0.82586 0.916709 0.846041 0.820658 0.846223 0.726271 
pentanote 0.083346 0.297539 0.168486 0.332744 0.157684 0.307569 0.316971 0.177782 
hexanoate 0.568292 0.49827 0.708209 0.185339 0.557579 0.455368 0 0.503435 
heptanoate 0.824208 0.839094 0.772526 0.467808 0.749209 0.739792 0 0.685252 
octanoate 0.755172 0.733516 0.760272 0.519296 0.687659 0.71001 0 0.711683 
nonanoate 0.732204 0.578013 0.842591 0.549125 0.191532 0.765482 0 0.73532 

 
190 
 
 
Figure S1 . Plasmids generated for functional replacement of mtbM (PP_0262) with PA3286. A) Functional 
replacement of mtbM with 500 bp flanking regions; B) with 700 bp upstream and 500 bp downstream flanking 
regions; C) with 500 bp upstream and 700 bp downstream; D) with PA3286 in the reverse direction; E) with PA3286 
driven by the pEM7 promoter (green); F) with PA3286 containing an ATG start codon. 
  


 
191 
 
 
Figure S2. Protein Multiple sequence alignment of PA3286 (Query) and PP_4545 (Sbjct). 
 
 
 
 
