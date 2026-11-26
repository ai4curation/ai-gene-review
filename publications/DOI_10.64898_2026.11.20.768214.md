---
reference_id: DOI:10.64898/2026.11.20.768214
extractor_version: 1
title: Homologs of the Major Vault Protein defend bacteria against ribotoxins
authors:
- Nathan P. Bullen
- Lucia C. Holiday
- Toni A. Nagy
- Laurel K. Robbins
- Aaron T. Whiteley
year: '2026'
doi: 10.64898/2026.11.20.768214
content_type: full_text_pdf
is_preprint: true
peer_review_status: preprint
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.biorxiv.org/content/biorxiv/early/2026/11/21/2026.11.20.768214.full.pdf"
oa_status: green
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.64898_2026.11.20.768214.pdf
full_text_access_type: open
---

# Homologs of the Major Vault Protein defend bacteria against ribotoxins
**Authors:** Nathan P. Bullen, Lucia C. Holiday, Toni A. Nagy, Laurel K. Robbins, Aaron T. Whiteley
**DOI:** [10.64898/2026.11.20.768214](https://doi.org/10.64898/2026.11.20.768214)

## Content

Abstract

                  Bacteria use sophisticated mechanisms to defend themselves against antibiotics and bacteriophages, yet how they combat toxins deployed during interbacterial competition remains poorly understood. Bacteria use type VI secretion, bacteriocins, and contact dependent inhibition systems to deliver antibacterial toxins that inhibit growth by antagonizing essential processes. Here, we discover that
                  Pseudomonas aeruginosa
                  uses homologs of the eukaryotic major vault protein and a tRNA-like noncoding RNA to defend against RNA-damaging ribotoxins. Using an engineered pyocin delivery system, we showed that
                  P. aeruginosa
                  sensed ribotoxin damage and activated transcription of an RNA repair operon, which included
                  band7
                  , a homolog of the major vault protein. Genetic analyses demonstrated that
                  band7
                  -expressing bacteria were significantly more protected against growth inhibition by a ribotoxin that cleaved the anticodon loop of specific tRNA. Band7 was necessary but not sufficient, and defense also required a non-coding band7 RNA (bRNA). bRNA was cleaved by the ribotoxin, suggesting a mechanism for specificity and defense. Bioinformatic analyses revealed that
                  band7
                  and candidate
                  bRNA
                  are widely distributed within RNA repair systems across diverse bacteria. Our data suggest that bacteria use structures related to the eukaryotic vault complex to respond to RNA damage thereby providing a hypothesis for the function of the enigmatic human vault.

 1 
Homologs of the Major Vault Protein defend bacteria against ribotoxins 2 
 3 
 4 
Nathan P. Bullen1, Lucia C. Holiday1, Toni A. Nagy1, Laurel K. Robbins1, Aaron T. Whiteley1* 5 
 6 
 7 
1 Department of Biochemistry, University of Colorado Boulder, Boulder, CO, USA 8 
 9 
*To whom correspondence should be addressed: aaron.whiteley@colorado.edu 10 
  11 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

Abstract: 12 
 13 
Bacteria use sophisticated mechanisms to defend themselves against antibiotics and 14 
bacteriophages, yet how they combat toxins deployed during inter bacterial competition remains 15 
poorly understood. Bacteria use type VI secretion, bacteriocins, and contact dependent inhibition 16 
systems to deliver antibacterial toxins that inhibit growth by antagonizing essential processes. 17 
Here, we discover that Pseudomonas aeruginosa uses homologs of the eukaryotic major vault 18 
protein and a tRNA -like noncoding RNA to defend against RNA -damaging ribotoxins. Using an 19 
engineered pyocin delivery system, we showed that P. aeruginosa sensed ribotoxin damage and 20 
activated transcription of an RNA repair operon , which included band7, a homolog of the major 21 
vault protein. Genetic analyses demonstrated that band7-expressing bacteria were significantly 22 
more protected against growth inhibition by a ribotoxin that cleaved the anticodon loop of specific 23 
tRNA. Band7 was necessary but not sufficient, and defense also required a non -coding band7 24 
RNA (bRNA). bRNA was cleaved by the ribotoxin, suggesting a mechanism for specificity and 25 
defense. Bioinformatic analyses revealed that band7 and candidate bRNA are widely distributed 26 
within RNA repair systems across diverse bacteria. Our data suggest that bacteria use structures 27 
related to the eukaryotic vault complex to respond to RNA damage thereby providing a hypothesis 28 
for the function of the enigmatic human vault.  29 
 30 
Keywords: bacterial immune system, bacterial antagonism, RNA repair, vault complex 31 
  32 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

Main text: 33 
 34 
Interbacterial antagonism is an inescapable aspect of bacterial life  when bacteria compete for 35 
space and resources in complex environments ranging from the soil to sites of infection.  A 36 
consequence of the relentless competition is the evolution of diverse antibacterial weapons that 37 
bacteria use to eliminate competitors. Among these are protein toxins that antagonize competing 38 
cells and  kill by inhibiting essential processes, such as  damaging cell envelope integrity, 39 
compromising the bacterial genome, or disrupting protein synthesis  (1). Toxins are deployed 40 
through multiple mechanisms that each translocate protein cargo into a target cell . T ype VI 41 
secretion systems (T6SSs) inject effectors directly into neighboring cells (2). Contact-dependent 42 
inhibition (CDI) systems deliver toxins following recognition of target -cell receptors (3). Protein 43 
bacteriocins are released into the extracellular environment and exploit cell-surface receptors and 44 
endogenous transport machinery to enter target cells (4). New toxins and delivery systems 45 
continue to be discovered, further expanding the known repertoire of weapons  deployed during 46 
bacterial competition. 47 
 48 
Survival during microbial competition is not just about deploying offensive strategies to kill 49 
competitors but also includes defensive strategies to survive threats. The threat of bacteriophages 50 
has driven the evolution of a staggering diversity of phage defense systems  (5, 6). Similarly, 51 
bacteria must also defend themselves against predatory bacteria (7, 8). Perhaps the most famous 52 
defense strategy is antibiotic resistance, which evolved during intermicrobial competition long 53 
before clinical use of these compounds (9). 54 
 55 
The diversity and abundance of antibacterial toxins deployed during microbial competition 56 
provides considerable selective pressure for bacteria to evolve mechanisms of defense  against 57 
these threats. Toxin-producing bacteria neutralize their toxins  using cognate immunity proteins 58 
that bind to the toxin with high affinity to block toxin activity and avoid self-intoxication (10). Closely 59 
related bacteria will also encode these immunity proteins to protect themselves, and one strategy 60 
of defense is to acquire immunity genes through horizontal gene transfer (11, 12). However, less 61 
is known about how bacteria survive intoxication when they lack these cognate immunity proteins. 62 
Here, we used Pseudomonas aeruginosa as a model to investigate how bacteria survive the 63 
damage inflicted by antibacterial toxins. 64 
 65 
Engineering a toxin delivery platform 66 
 67 
We searched the literature for antibacterial toxins produced by  P. aeruginosa and identified 50 68 
toxins with experimentally demonstrated antibacterial activity ( Table S1). These toxins are 69 
deployed through three major delivery mechanisms: type VI secretion system s, contact -70 
dependent inhibition, and S-type pyocins (soluble, pseudomonas-specific bacteriocins) (Fig. 1A) 71 
(13). Collectively, these toxins target essential cellular components that include the cell envelope 72 
(pore-forming toxins, phospholipases, and peptidoglycan hydrolases), the genome (DNases), 73 
coding and non-coding RNAs (RNases), and metabolites (NAD+ and ATP destroying-enzymes) 74 
(1). Toxins that cleave or modify tRNA, rRNA, and mRNA (ribotoxins) were the most prevalent in 75 
our survey (Fig. 1B). We hypothesized that P. aeruginosa must have evolved mechanisms to  76 
counter toxin-inflicted RNA damage and searched for mechanisms of ribotoxin defense. 77 
 78 
We investigated diverse ribotoxins by engineering a system to deliver heterologous toxins into P. 79 
aeruginosa using an S-type pyocin as a delivery platform. Pyocin S4 uses an N-terminal receptor-80 
binding and translocation domains to mediate uptake of a C -terminal toxin domain through the 81 
ferripyoverdine receptor FpvAI  (14). The pyocin S4 toxin domain is related to colicin E5  and 82 
predicted to cleave tRNA (15, 16). To repurpose the pyocin S4 delivery system, we substituted 83 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

the native S4 C-terminal RNase domain with four alternative toxin domains representing distinct 84 
RNase families (Fig.1, C and D, Fig. S1A). These included the rRNase domain of pyocin S6 (S4-85 
S6tox), which shares homology with colicin E3 and is predicted to cleave 16S rRNA ; the tRNase 86 
domains of the contact-dependent inhibition toxins CdiA1 and CdiA2 from P. aeruginosa PA14 87 
(S4-D1tox and S4-D2tox), which shares homology with colicin D and is predicted to cleave tRNA 88 
anticodon loops ; and the RNase domain of CdiA2 from PAO1 (S4 -EndoUtox), which shares 89 
homology with the EndoU-family and whose cellular targets remain undefined (16, 17). Together 90 
with native pyocin S4  (S4-S4tox), this yielded a panel of five purified ribotoxins  with a range of 91 
targets (Fig. S1B). The DNA-targeting pyocin S2 was purified to use as a control for non -RNA 92 
damage (18). 93 
 94 
We measured the impact of our chimeric pyocins on growth of P. aeruginosa by exposing bacteria 95 
to toxin and measuring colony formation.  We selected strain PA14 for our analysis  and, where 96 
necessary, deleted the endogenous copies of the toxin -antitoxin genes that would otherwise 97 
counter pyocin killing. Specifically, the toxin domains of S4-D1tox and S4-D2tox originate from PA14 98 
and we deleted these toxins and cognate immunity proteins (∆cdiA-I). A close homolog to pyocin 99 
S4 and its immunity protein were also found in PA14 and we deleted these genes (∆PA14_13940-100 
PA14-13950, Fig. S1A). Using the appropriate toxin-sensitive strains, we found a ll six pyocins 101 
potently inhibited bacterial growth (Fig. 1E). Next, we repeated the intoxication assay using strains 102 
heterologously expressing the immunity protein of each ribotoxin and found that each strain grew 103 
equally well to the no-toxin control (Fig. 1E). Immunity proteins inhibit their cognate toxins by 104 
specifically binding and occluding the ir active site , thereby providing an important control to 105 
demonstrate pyocin killing depended on the toxin domain. These data confirm that the observed 106 
growth inhibition for each chimeric pyocin was the result of the toxin domain’s activity. 107 
 108 
Ribotoxins activate an RNA damage response 109 
 110 
We next investigated how P. aeruginosa responds to damage inflicted by ribotoxins by performing 111 
RNA sequencing of intoxicated cells. We focused our analysis on S4-EndoUtox because 112 
examination of total cellular RNA from intoxicated cells revealed EndoUtox induced the most 113 
grossly apparent RNA damage (Fig. 2A). After 5 minutes of intoxication with EndoUtox, the gene 114 
with the highest increase in abundance compared to non-intoxicated cells was PA14_60630 (86-115 
fold), a gene of unknown function encoding a protein with a predicted Band7 domain, hereafter 116 
referred to as band7 (Fig. 2B and S2A). Examination of the surrounding genomic region revealed 117 
that band7 is encoded in an operon with three additional genes that were also strongly induced 118 
compared to cells not exposed to toxin: rtcB, encoding an RNA ligase (45-fold); rlaP, encoding a 119 
putative nucleotidyltransferase (12-fold); and rtcA, encoding an RNA 3′-phosphate cyclase (7.5-120 
fold) (Fig. 2, B and C, Table S2). By 15 minutes of intoxication, band7, rtcB, rlaP, and rtcA had 121 
increased -590, 300-, 101-, and 56-fold, respectively (Fig. 2B, and Table S2). 122 
 123 
Together, band7, rtcB, rlaP, and rtcA constitute the Rtc operon of P. aeruginosa PA14, which is 124 
regulated by the divergently encoded σ54-dependent transcriptional activator RtcR (Fig. 2C). RNA 125 
repair systems (Rtc operons and RtcR) are widespread among bacteria and their physiological 126 
roles remain poorly understood (19, 20). Although these systems are named for RNA repair, their 127 
functions can also include RNA damage responses that mitigate, rather than heal, damage (21, 128 
22). In a comprehensive analysis of bacterial RNA repair systems, Burroughs and Aravind found 129 
that bacteria encode a broad-range of diverse genes within their  Rtc operons and neighboring 130 
genomic regions (23). The canonical Rtc operon in E. coli encodes only the minimal rtcB and rtcA 131 
genes divergently transcribed from rtcR (Fig. 2C). However, many  bacteria encode additional 132 
components with known or predicted RNA repair functions. P. aeruginosa has broadened its Rtc 133 
operon to include band7 and rlaP. Rtc-related RNA repair  loci show patterns of gene shuffling 134 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

and horizontal transfer that are consistent with the rapidly evolving systems involved in microbial 135 
conflict (23). Given the strong induction of the PA14 Rtc operon following ribotoxin treatment, we 136 
hypothesized these genes function as a defense pathway to counter antibacterial ribotoxins. 137 
 138 
We deleted the PA14 Rtc locus (∆rtc-locus), challenged this mutant with our toxin panel , and 139 
measured colony formation. We recovered over 50-fold fewer colony forming units (CFU) of the 140 
∆rtc-locus mutant compared to wild -type when treated with either  S4-EndoUtox or S4-S4tox, but 141 
saw no change in sensitivity of ∆rtc-locus to the other four pyocins (Fig. 2D). Importantly, the ∆rtc-142 
locus mutant had no growth defect in the absence of toxin (Fig. S2B). 143 
 144 
We next challenged the  ∆rtc-locus strain with diverse biotic and abiotic stressors , including UV 145 
irradiation, temperature stress, redox stress, bacteriophage infection, and varied antibiotics, to 146 
further examine the specificity of this defense response (see Methods). For each stressor , the 147 
∆rtc-locus mutant was as equivalently sensitive as wild-type (Fig. S2, C, D, E and F). Together, 148 
our findings suggest that the Rtc operon functions as a specialized defense pathway against  149 
specific ribotoxin-mediated RNA damage. 150 
 151 
Rtc operon genes provide ribotoxin defense 152 
 153 
We next identified the genes within the Rtc operon that were responsible for defense against 154 
pyocin S4-S4tox and S4 -EndoUtox by generating in-frame deletions of each gene . band7 was 155 
required for defense against S4 -EndoUtox, rtcB was required for defense against S4 -S4tox, rlaP 156 
was dispensable for both toxins, and rtcA was required for protection against both toxins (Fig. 3, 157 
A and B).  The degree of ribotoxin defense was not equivalent for each individual rtc gene . 158 
Specifically, the ∆band7 and ∆rtcB mutants were similarly sensitive to intoxication as the ∆rtc-159 
locus strain for S4-EndoUtox and S4-S4tox, respectively. In contrast, deletion of rtcA resulted in an 160 
intermediate sensitivity for both toxins.  161 
 162 
RtcR activates transcription of the divergently transcribed Rtc operon upon binding of damaged 163 
RNA fragments (24, 25). The RtcR N-terminal CARF domain recognizes RNA damage by binding 164 
2′,3′-cyclic phosphate termini, which frees the AAA+ ATPase domain to interact with σ54 and leads 165 
to increased target gene expression (19, 26). One of the sources of cyclic 2′,3′-cyclic phosphate 166 
termini is RtcA, which  converts RNA 3′ -phosphate ends to 2′,3′ -cyclic phosphates  (20). Our 167 
transcriptomics suggested RtcR was activated following ribotoxin damage and we hypothesized 168 
that RtcA might help to po tentiate this response by increasing the abundance  of 2′,3′-cyclic 169 
phosphate termini, thereby explaining the ∆rtcA intermediate phenotype for S4-EndoUtox and S4-170 
S4tox. To test this hypothesis, we measured ribotoxin sensitivity during heterologous expression 171 
of a constitutively active RtcR variant deleted for its N-terminal CARF domain (rtcR∆CARF). RNA-172 
sequencing analysis confirmed that rtcR∆CARF induced expression of the Rtc operon in the 173 
absence of intoxication (Fig. 3C). Further, expression of constitutively active rtcR∆CARF rescued 174 
the sensitivity of ∆rtcA strains (Fig. 3, D and E). These data suggest that the principal function of 175 
RtcA in these conditions is amplifying expression of the Rtc operon through production of RtcR-176 
activating ligands. 177 
 178 
Unlike in the ∆ rtcA mutant, expression of constitutively active rtcR∆CARF failed to rescue the 179 
sensitivity of the ∆rtcB strain to S4-S4tox, indicating that RtcB is directly responsible for defense 180 
against this ribotoxin (Fig. S3A). RtcB is an RNA ligase that joins cleaved RNA ends bearing 3′ -181 
phosphate or 2′,3′-cyclic phosphate with 5′-hydroxyl termini (27, 28). Colicin E5-family ribotoxins, 182 
including pyocin S4 tox, cleave tRNAs within their anticodon loops, preventing their use in 183 
translation (29). Previous studies have shown that E. coli RtcB can directly repair tRNAs cleaved 184 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

within their anticodon loops  in vitro (27). Our data, suggest that RtcB protects against S4-S4tox 185 
through ligation to directly repair pyocin-cleaved tRNAs.  186 
 187 
Heterologous expression of constitutively active rtcR∆CARF also did not affect the sensitivity of the 188 
∆band7 mutant to S4-EndoUtox, implying that Band7 directly mediates defense against this toxin 189 
(Fig S3B). Band7 domain-containing proteins have not been previously shown to contribute to 190 
RNA damage defense, prompting us to further investigate their molecular function. 191 
 192 
A homolog of major vault protein and a non-coding RNA are required for defense 193 
 194 
Band7 proteins belong to the widespread stomatin, prohibitin, flotillin, HflK/C (SPFH) superfamily, 195 
whose members are often associated with membrane organization and the formation of large 196 
oligomeric assemblies (30, 31). A previous bioinformatic analysis of bacterial RNA repair operons 197 
noted that the subset of bacterial Band7 proteins  in these loci share distant homology with the 198 
eukaryotic major vault protein (MVP), and raised the possibility that these proteins form vault-like 199 
assemblies (23). Vaults are massive, barrel -shaped ribonucleoprotein complexes composed 200 
primarily of MVP , and are  of largely unknown function  (32, 33). We examined the predicted 201 
structure of PA14 Band7 and found striking resemblance to MVP, including a similar arrangement 202 
of N-terminal repeat domains, a shared Band7/SPFH shoulder domain, and a C-terminal capping 203 
helix (Fig. 4A). Modeling the oligomeric complex of 12 Band7 monomers revealed a vault like 204 
complex comparable in shape to the human vault (Fig. 4B). 205 
 206 
The band7 gene was required for defense against S4 -EndoUtox and we next attempted to show 207 
that band7 expression was sufficient to res tore the ∆ rtc-locus mutant sensitivity  to toxin . 208 
Unexpectedly, e xpression of band7 did not restore defense in the  ∆rtc-locus strain. This was 209 
unlikely to be technical failin g because complementation of the ∆band7 mutant with the same 210 
band7 expression vector restored protection against S4 -EndoUtox (Fig. 4 C). These findings 211 
suggested that an additional component within the  rtc-locus was required for defense , but our 212 
other data showed this component was not rtcB, rlaP , or rtcA. To discover the unknown 213 
component, we returned to our rtcR∆CARF RNA-seq results and  closely examined transcription 214 
across the Rtc locus. Transcription appeared to originate from three locations: from the promoter 215 
of rtcR, from the promoter of the Rtc operon, and in the intergenic region between rtcR and the 216 
Rtc operon (Fig. 4D). Notably, the intergenic region transcript included an annotated arginyl-tRNA 217 
gene. 218 
Northern blot analysis using probes targeting this region in cells expressing rtcR∆CARF revealed a 219 
distinct RNA species of approximately 450 nucleotides, substantially longer than the 75-90 220 
nucleotides expected for a mature arginyl-tRNA (Fig. 4E). Based on RNA-sequencing coverage 221 
and the estimated transcript size, this RNA’s transcription start site appeared to be approximately 222 
140 nucleotides upstream of the annotated tRNA , with transcription  terminating roughly 50 223 
nucleotides upstream of the band7 coding sequence. We renamed this non-coding RNA band7-224 
associated RNA (bRNA). To determine whether bRNA contributes to defense, we heterologously 225 
expressed both bRNA and band7 in ∆band7 and ∆rtc-locus mutants and challenged these strains 226 
with S4-EndoUtox. This construct restored protection to ∆ band7 and ∆ rtc-operon, u nlike 227 
expression of band7 alone (Fig. 4F). Introduction of a premature stop codon into the band7 coding 228 
sequence abolished protection, demonstrating that both the Band7 protein and upstream 229 
noncoding RNA are required for defense  (Fig. S4). Together, these findings reveal that crucial 230 
elements of the Rtc operon ribotoxin defense system include a vault-like Band7 protein and an 231 
associated noncoding bRNA. 232 
 233 
S4-EndoUtox cleaves tRNAs near their anticodon loops 234 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 235 
Antibacterial ribotoxins kill cells by cleaving essential RNAs, particularly tRNAs and rRNAs (1). 236 
Unlike the other ribotoxins in our panel, sequence and structural predictions provided little insight 237 
into the potential RNA targets of S4 -EndoUtox. We investigated how this toxin inhibits bacterial 238 
growth by performing northern blot analysis of RNA isolated from intoxicated cells using probes 239 
targeting six distinct tRNA species, 16S rRNA, and 23S rRNA. Probes targeting the variable loop 240 
regions of tRNAs Arg ACG, Arg CCU, ArgCCG, and Glu UUC revealed distinct cleavage products of 241 
approximately 3 5-40 nucleotides  (Fig. 5A, B  and S5A). The size of these 3′ fragment s was 242 
consistent with cleavage of each tRNA within its anticodon loop. To further investigate the position 243 
of cleavage, we repeated the analysis of ArgACG cleavage using a probe targeting the region 5′ of 244 
the anticodon loop (Fig 5B and C). This revealed a similarly sized cleavage product, consistent 245 
with the accumulation of the 5′ half of the cleaved tRNA. In contrast, we did not detect cleavage 246 
products for SerGCU or ValUAC, suggesting that EndoUtox targets a subset of tRNA species rather 247 
than cleaving tRNAs indiscriminately (Fig. S5B). 248 
 249 
Northern blot analysis of 23S rRNA also revealed a prominent cleavage product of approximately 250 
150 nucleotides (Fig. 5D). This observation was consistent with analysis of total cellular RNA, 251 
which showed a near  complete loss of full -length 23S rRNA following intoxication with S4 -252 
EndoUtox (Fig. 2A). In contrast, we detected no comparable cleavage of 16S rRNA  (Fig. 5D). 253 
Together, these findings suggest that S4-EndoUtox inhibits bacterial growth by damaging multiple 254 
components of the translation machinery, including cleavage of a subset of tRNAs near their 255 
anticodon loops and degradation of 23S rRNA. 256 
 257 
bRNA is cleaved during S4-EndoUtox intoxication 258 
 259 
bRNA encompasses an internal 74 -nucleotide sequence annotated in the PA14 genome as an 260 
arginyl-tRNA with an ACG anticodon. Secondary structure prediction confirmed this region adopts 261 
a canonical tRNA cloverleaf structure (Fig. 5B). Sequence alignment with the five other arginine 262 
tRNA genes annotated in the PA14 genome revealed that this region retains conserved sequence 263 
motifs characteristic of the tRNA (i.e. D- and TΨC-loops) but lacks a genetically encoded CCA at 264 
the 3′-terminus, which is found on the other five arginyl-tRNA (Fig. S5C). RNA sequencing failed 265 
to detect post -transcriptional addition of a CCA  3′-end and our norther n blot analysis did not 266 
identify bRNA at the expected size of mature tRNA. This suggests that bRNA is not a mature 267 
tRNA, unlikely to be amino acylated, and probably not participating in translation. 268 
 269 
Given the s imilarity of  bRNA to tRNA, we investigated whether bRNA is cleaved during S4-270 
EndoUtox intoxication. Northern blot analysis using a probe targeting the 5′ region upstream of the 271 
tRNA-like features revealed two prominent cleavage products  following treatment with S4 -272 
EndoUtox. The first migrated between the 150- and 300-nucleotide markers and the second just 273 
below the 150-nucleotide marker (Fig. 5E). A second probe targeting the region 3′ of the tRNA -274 
like features revealed a prominent cleavage product migrating below the 300 -nucleotide marker 275 
(Fig. 5F). These sizes are consistent with cleavage near the predicted anticodon-loop like feature 276 
of bRNA, similarly to the observed cleavage of tRNA ArgACG.  277 
 278 
We next determined whether bRNA cleavage was associated with coordinating defense against 279 
S4-EndoUtox intoxication. If bRNA cleavage is linked to this protective response, we reasoned 280 
cleavage should only occur specifically during intoxication with S4 -EndoUtox and not with 281 
ribotoxins from our panel for which Band7-bRNA did not provide protection. Northern blot analysis 282 
following intoxication with each of the five ribotoxins  showed that only S4-EndoUtox produced 283 
detectable bRNA cleavage  (Fig. 5G). These findings establish that bRNA undergoes selective 284 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

cleavage during S4 -EndoUtox intoxication, suggesting the tRNA-like features of bRNA may be 285 
important for sensing and responding to specific tRNA-targeting toxins. 286 
 287 
Bacterial vault-like proteins are widespread and associate with RNA repair systems 288 
 289 
We next sought to determine how widely vault-like Band7 proteins are distributed among bacteria 290 
and whether their association with RNA repair systems is conserved. Initial sequence similarity 291 
searches using PA14 Band7 as a query returned many non-vault-like members of  the SPFH 292 
superfamily, such as HflK/C homologs with N-terminal transmembrane helices rather than the 293 
globular N-terminal repeats characteristic of the major vault protein. To overcome this limitation, 294 
we used PSI-BLAST to curate a list of 19 Band7 proteins from distinct bacterial species that were 295 
confirmed to adopt N-terminal globular repeat domains and resemble PA14 Band7 and MVP. We 296 
then used these 19 sequences to construct a profile Hidden Markov model (HMM) designed to 297 
capture sequence features conserved among vault-like Band7 proteins while distinguishing them 298 
from other SPFH family members. Searching 88 .8 million proteins from bacterial and archaeal 299 
RefSeq genomes assemblies with this model identified 2,026 high-confidence homologs.  300 
 301 
Phylogenetic analysis of the Band7 homologs identified in our search revealed that vault -like 302 
Band7 proteins are distributed across most major bacterial phyla, including  Pseudomonadota, 303 
Actinomycetota, Bacillota, and Bacteroidota  (Fig. 6A). Structural modeling of representative 304 
proteins revealed conservation of the overall vault architecture, with predicted complexes varying 305 
in size and shape according to the number of N -terminal repeat domains and the length of the 306 
cap helix (Fig. 6B and C). Examination of the genomic neighborhoods surrounding these genes 307 
revealed that many are associated with Rtc RNA repair systems : adjacent to transcriptional 308 
regulators and enzymes with predicted RNA repair functions, including homologs of RtcB, RtcA, 309 
and RlaP (Fig. 6B and C ). Intriguingly, many band7 genes were also encoded  immediately 310 
downstream of annotated tRNA-like sequences, resembling the genomic arrangement of bRNA 311 
and band7 observed in PA14. These sequences were identified across distantly related bacterial 312 
lineages and corresponded to different predicted tRNA identities, suggesting that the association 313 
between vault-like Band7 proteins and tRNA-like bRNAs is a conserved feature of these systems. 314 
Together, these analyses reveal that vault-like Band7 proteins are phylogenetically widespread 315 
and retain a conserved association with RNA repair machinery, suggesting an ancient and 316 
conserved role in bacterial ribotoxin defense. 317 
 318 
Discussion 319 
 320 
Here, we establish that the P. aeruginosa RNA repair system mitigates damage by  ribotoxins 321 
deployed during intermicrobial antagonism . Following intoxication, the RNA cyclase RtcA 322 
amplifies signals of  RNA damage by producing the chemical signal that  activates the 323 
transcriptional activator RtcR. RtcR drives expression of the divergently encoded Rtc operon, 324 
including genes for : Band7, an uncharacterized protein  predicted to assemble into complex 325 
homologous to the mammalian vault ; RtcB, an  RNA ligase ; RlaP, a poorly characterized 326 
nucleotidyltransferase, and RtcA. Upstream of the Rtc operon, RtcR also activate s transcription 327 
of bRNA, a noncoding RNA with tRNA-like features. The diversity of Rtc operon constituents 328 
across bacteria suggests that these genes have evolved to be coordinately regulated in response 329 
to a common hallmark of RNA damage, 2′,3′-cyclic phosphate  ends, while individual  genes 330 
counter distinct forms of RNA damage. Here, we demonstrate roles for Band7, RtcB, and RtcA in 331 
countering ribotoxins, however, our panel of toxins did not reveal a protective role for RlaP. Recent 332 
work suggest ed that RlaP counters ribotoxins that cleave RNA and remove one or more 333 
nucleotides, preventing repair by RtcB alone  (34). Testing a wider range of ribotoxins in future 334 
studies may capture the specific utility of this gene. 335 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 336 
Our findings place Rtc operons within a growing repertoire of genes that protect bacteria against 337 
toxins deployed during microbial conflict. These defenses range from very specific , such as 338 
acquiring cognate immunity proteins, to very generalized defenses, such as protective barriers 339 
that block intoxication  (10, 35). Rtc operons are induced by damage inflicted by antibacterial 340 
toxins and join a larger family of damage induced responses. A conceptually similar screen for 341 
resistance to T6SS toxins in P. aeruginosa  identified three discrete gene clusters, termed 342 
antagonism resistance clusters (Arc1–3), that protect against antibacterial effectors that damage 343 
the cell membrane  (36). Arc1–3 are regulated by the Gac/Rsm danger -sensing system and 344 
recently rtcB was also shown to be regulated by Gac/Rsm in PAO1 (37). This regulatory overlap 345 
supports the notion that defense against antibacterial toxins is part of a broad immune response 346 
to microbial antagonism and may constitute a new arm of the bacterial immune system . Indeed, 347 
the apparent escalation of offensive ribotoxins and the corresponding repertoire of genes within 348 
RNA defense systems is reminiscent of the molecular arms race between phages and phage 349 
defense systems. This analogy implies that, like phage defense systems, there may be many 350 
additional antibacterial toxin defense systems waiting to be discovered. 351 
 352 
The most surprising finding of our study is that bacteria encode proteins homologous to the 353 
eukaryotic MVP that mitigate RNA damage to allow bacteria to survive treatment with a ribotoxin. 354 
Multiple publications have identified MVP homologs  (23, 38–43) and t wo recent studies 355 
demonstrated that related Band7 proteins assemble into vault complexes in vitro and oligomerize 356 
with 70 or more protomers to form particles that rival the human vault in size (44, 45). Although 357 
our structural predictions were limited to 12 Band7 protomers, we anticipate PA14 Band7 proteins 358 
may also form particles similar in size to human vaults. An outstanding question is, why does 359 
ribotoxin defense require a molecular vessel like the vault? We envision at least three potential 360 
models. First, bacterial vaults may trap ribotoxins to sequester these dangerous molecules away 361 
from cellular tRNAs. Second, the vault may be a cryptic enzyme or may capture another cellular 362 
enzyme that requires compartmentalization for specificity or activity . Third, the vault may 363 
encapsulate damaged tRNA molecules to facilitate their repair or destruction. 364 
 365 
The proposed models for bacterial vault s are not mutually exclusive, however, each final 366 
mechanism must have a role for bRNA  because this component was necessary for ribotoxin 367 
defense. We hypothesize that bRNA serves as the “canary in the coal mine” for toxin presence. 368 
By resembling tRNA, the bRNA acts as a decoy substrate for ribotoxins and bRNA cleavage likely 369 
activates defense via Band7. However, it cannot be as simple as bRNA hold ing Band7 in an 370 
inactive state until cleavage because expression of Band7 in the absence of bRNA did not result 371 
in a constitutive defensive state. Perhaps the 5′ and 3′ extensions that separate bRNA from similar 372 
arginyl-tRNAs serve a crucial function  for defense activation . Looking past P. aeruginosa, the 373 
bRNA genes we identify across bacteria are not just similar to arginyl-tRNA but resemble a wide 374 
range of other tRNA species. Some even encode multiple tRNA annotations. These observations 375 
suggest that each bRNA/Band7 pair may be specific for toxins that cleave different target tRNA. 376 
In this way, bRNA must retain the tRNA identity elements recognized by the ribotoxin. 377 
 378 
The eukaryotic vault complex has mystified researchers for over 40 years  (46). While this 379 
nanoparticle has been implicated in diverse  cellular processes and disease states, a molecular 380 
explanation for how the vault contributes to cellular homeostasis has yet to emerge. A unique 381 
challenge of understanding the vault has been the absence of these complexes in conventional 382 
eukaryotic model organisms such as Saccharomyces cerevisiae, Caenorhabditis elegans, and 383 
Drosophila melanogaster (47). Our findings establish that bacteria could be the  missing model 384 
organism for these observations. Accordingly, we hypothesize that the human vault complex may 385 
play a crucial part in repairing or responding to RNA damage.  386 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

Acknowledgements: 387 
 388 
The authors would like to thank the CU Boulder Department of Biochemistry Shared Instruments 389 
Pool core facility (RRID:SCR_018986), Anette Erbse, and its staff; Karolin Luger and her lab for 390 
sharing lab space, resources and equipment; Michael Nosalla for helpful discussions; John 391 
Whitney for strains and plasmids; and members of the Whiteley laboratory , particularly Kishen 392 
Patel, for their advice, support, and helpful discussions.  393 
 394 
Funding:  395 
 396 
This work was funded by  the PEW Charitable Trust Biomedical Scholars A ward (A.T.W.); the 397 
Burroughs Wellcome Fund PATH  Award 1186087 (A.T.W.); and the Cancer Research Institute 398 
Lloyd J. Old STAR award CRI17515 (A.T.W.). N.P.B is supported in part by the Jane Coffin Childs 399 
Memorial Fund for Medical Research  Fellowship Award . L.C.H is supported in part by  the 400 
Biochemistry Undergraduate Research Scholar Award, University of Colorado Boulder. 401 
 402 
Authors Contributions: 403 
 404 
Conceptualization: NPB and ATW  405 
Methodology: NPB and ATW 406 
Investigation: NPB, LCH, LKR  407 
Visualization: NPB and ATW  408 
Funding acquisition: ATW  409 
Supervision: ATW  410 
Writing - original draft: NPB and ATW  411 
Writing - review & editing: NPB, TAN, and ATW 412 
 413 
Competing Interests: 414 
 415 
The authors declare no competing interests. 416 
 417 
Data, code, and material availability:  418 
 419 
All data are available in the manuscript or supplementary materials. No new code was generated 420 
for this study.  Strains and plasmids used in this study are available following publication upon 421 
request and/or are distributed by Addgene (addgene.org). 422 
 423 
List of Supplementary Materials: 424 
 425 
Tables S1 to S2 426 
 427 
  428 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

Materials and Methods 429 
 430 
Bacterial strains and bacteriophages 431 
 432 
Bacteria used in this study are listed in Supplementary Table 1. All strains were cultured in LB 433 
medium (1% tryptone, 0.5% yeast extract, and 0.5% NaCl) at 37 °C with shaking at 220 rpm in 1-434 
3 mL of medium in 14 mL culture tubes, unless otherwise indicated. Where applicable, cultures 435 
were supplemented with gentamicin (15 µg/mL for E. coli and 30 µg/mL for P. aeruginosa) or 436 
carbenicillin (100 µg/mL). Bacterial strains were frozen for storage in LB supplemented with 10% 437 
glycerol at -70 °C. E .coli Omnipir was used for the construction and propagation of all plasmids. 438 
E. coli SM10 was used for mating the allelic exchange vector pEXG2 into all P. aeruginosa strains, 439 
and E. coli  Rosetta2 was used for all heterologous recombinant protein expression. E. coli  440 
MG1655 and P. aeruginosa PA14 were used to collect all experimental data.  When growing 441 
strains that required induction, 250 µM or 500 µM β-D-1-thiogalactopyranoside (IPTG) were used 442 
to induce, as appropriate. 443 
 444 
All bacteriophages used in this study are listed in Supplementary Table 1.  445 
 446 
Cloning, plasmid construction and mutant strain generation 447 
 448 
Plasmids used in this study are listed in Supplementary Table 3. Genes of interest were amplified 449 
from bacterial genomic DNA using Q5 Hot Start High Fidelity Master Mix (NEB M0494L), flanked 450 
by 18 base pairs of homology to vector backbone. Amplified genes were ligated into restriction-451 
digested, linearized vector backbones using Gibson assembly(48). Gibson reactions were then 452 
transformed into bacteria by electroporation and plated on the appropriate antibiotic selection. All 453 
enzymes used for cloning were purchased from New England Biolabs.  454 
 455 
Mutants of P. aeruginosa were generated through allelic exchange as previously described (49). 456 
Mutants of E. coli were generated through Lambda red recombineering as described previously 457 
(50).  458 
 459 
Recombinant protein expression and purification 460 
For protein expression and purification of pyocin S4 and the S4 chimeras, each toxin was co -461 
expressed with its cognate immunity protein from  a single pETDuet vector to prevent cellular 462 
intoxication and to increase yield of  recombinant protein. 2 L of LB broth supplemented with 463 
carbenicillin was inoculated 1:50 with an overnight culture of E. coli Rosetta2 harboring the toxin-464 
immunity construct. Cultures were grown at 37°C with shaking at 220rpm until they reached an 465 
OD600 of 0.4, and IPTG was added at a final concentration of 500 µM IPTG prior to growth for an 466 
additional 3 h. Cells were harvested by centrifugation at 4,660 x g and 4°C, pellets were then 467 
resuspended in lysis buffer (100 mM Tris -HCl, pH 8.0, 300 mM NaCl, 10 mM imidazole) , and 468 
sonicated with a Sonicator 4000 (Misonix) on ice at an amplitude of 75%  for six 30 second on / 469 
off pulses. Lysates were cleared of insoluble debris by centrifugation at 39,000 x g for 60 min. 470 
Soluble fractions were then loaded onto 1.5-mL gravity-flow columns packed with 1 mL of Ni-NTA 471 
agarose, pre-equilibrated with lysis buffer. The column -bound toxin-immunity complexes were 472 
washed three times with 20 mL of lysis buffer and subsequently eluted using 5 mL of lysis buffer 473 
supplemented with 400 mM imidazole. Proteins in each Ni-NTA elution were then further purified 474 
by fast protein liquid chromatography using gel filtration on a HiLoad 16/600 Superdex 200 column 475 
equilibrated in 20 mM Tris -HCl, pH 8.0, and 150 mM NaCl. The purity of each protein was 476 
determined by SDS-PAGE followed by gel staining with Coomassie Brilliant Blue. 477 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

SDS-polyacrylamide gel electrophoresis 478 
 479 
Purified pyocin S2, S4 and the S4 chimeric toxins  were diluted 1:2 in 4X Laemmli buffer 480 
supplemented with 1.5% β-mercaptoethanol. Samples were heated to 95 °C for 10 minutes and 481 
then loaded on  a SurePageTM, Bis-Tris 4-20% gradient polyacrylamide gel (Genscript). Protein 482 
samples were resolved for 50 minutes at 155V before being stained with Coomassie brilliant blue 483 
and visualized using a Azure 200 Gel Imaging Workstation (Azure Biosystems).  484 
 485 
Bacterial intoxication spot assays 486 
 487 
Spot assays were used to measure the sensitivity of P. aeruginosa strains to pyocin S2, S4 and 488 
the S4-chimera ribotoxins. Overnight cultures of P. aeruginosa were back diluted 1:50 in LB and 489 
cultivated at 37 °C with shaking at 220 rpm to a final OD600 of 0.4. Cultures were serially diluted 490 
10-fold into fresh LB. From each 10-fold dilution (ranging from 10-1 to 10-8), 10 µL of culture was 491 
added to the well of a microtiter plate containing 87 µL of LB and 3 µL of toxin, and the resulting 492 
mix spotted onto LB agar plates. Plates were incubated overnight at 37 °C prior to imaging.  493 
 494 
The amount of toxin needed for measurable intoxication was empirically determined for each 495 
toxin. Final concentrations of toxin used in Fig. 2D were 80 nM for S 4-EndoUtox, 50 nM for S4 -496 
S4tox, 69 nM for S4 -D1tox, 900 nM for S4 -D2tox, 690 nM for S4 -S6tox, and 89 nM for S2 . For all 497 
other spot assay intoxications, these values were increased approximately 10 -fold to better 498 
measure the relative growth inhibition between mutants and wildtype P. aeruginosa.. 499 
 500 
Temperature Stress Assay 501 
 502 
Overnight cultures were diluted 1:50 into fresh LB medium and cultivated at 37 °C with shaking 503 
at 220 rpm to an OD600 of 0.5. Cultures were serially diluted and spotted onto LB agar plates. 504 
Plates were incubated at 10 °C, 22 °C (room temperature), or 37 °C. Plates incubated at 22 °C 505 
and 37 °C were imaged following overnight growth, whereas plates incubated at 10 °C were 506 
imaged after 3 days, when visible colonies had developed. 507 
 508 
UV exposure assays 509 
 510 
Overnight cultures were back diluted 1:50 in LB and cultivated to an OD600 of 0.4. 100 µL of cells 511 
were pelleted by centrifugation at 8,000 x g and resuspended in 100 µL of phosphate buffered 512 
saline (PBS,137 mM NaCl, 2.7 mM KCl, 10 mM Na 2HPO4, and 1.8 mM KH2PO4, pH 7.4). 50 µL 513 
of the resuspended pellet was then spotted onto the  lid of a petri dish and place d drop side up 514 
into a Stratalinker UV crosslinker (Stratagene)  operating at 254 nm. Samples were exposed to 515 
UV irradiation (80-120 µJ/cm2), serially diluted 10 -fold in PBS , then spotted on  1.6 % LB agar 516 
plates and grown overnight at 37 °C for quantification of cell viability.  517 
 518 
Disk diffusion assays 519 
 520 
Overnight cultures were diluted 1:50 into fresh LB and cultivated to an OD 600 of 0.4. 300 µL of 521 
culture was then mixed with 3.5 mL of 0.35% LB agarose warmed to 40 °C. This mixture was then 522 
poured onto a 1.6 % agar LB plate and cooled for 10 minutes to solidify. One cm diameter disks 523 
of filter paper were soaked with 50 µL of  streptomycin (100 µg/mL) , kanamycin (50 µg/mL) , 524 
gentamicin (30 µg/mL), spectinomycin (100 µg/mL), apramycin (15 µg/mL), chloramphenicol (20 525 
µg/mL), tetracycline (15 µg/mL), carbenicillin (100 µg/mL), polymyxin b (30 µg/mL), mitomycin (5 526 
µg/mL), zeocin (50 µg/mL), ciprofloxacin (5 µg/mL), rifampin (5 µg/mL), irgasan (24 µg/mL), or 527 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

H2O2 (3% solution). Impregnated disks were then placed onto the cooled agar overlay and plates 528 
were incubated overnight at 37 °C.  529 
 530 
Efficiency of plating/phage replication analysis 531 
A modified double agar overlay assay was used to measure phage replication. Briefly, overnight 532 
cultures of the indicated strains were diluted 1:100 and cultivated for an additional two hours to 533 
reach logarithmic growth phase (OD600 0.1-0.8). 400 µL of the culture was then mixed with 3.5 mL 534 
0.35% LB agar, plus an additional 10 mM MgCl 2,10 mM CaCl2, and 0.1 mM MnCl2. The mixture 535 
was then poured onto a 1.6% agar LB plate and cooled for 15 minutes. 2 µL of a phage dilution 536 
series in SM buffer (100 mM NaCl, 8 mM MgSO 4, 50 mM Tris -HCl pH 7.5, 0.01% gelatin)  was 537 
spotted onto the overlay and allowed to dry under a flame before incubation overnight at 37 °C. 538 
Plaque formation was analyzed the following day. When no plaques were observable or a hazy 539 
zone of clearance occurred, 0.9 plaques at the least dilute spot was used as the limit of detection. 540 
Intoxication of bacterial cells for RNA extraction 541 
 542 
For isolation of RNA from intoxicated cells for RNA sequencing or Urea-PAGE, overnight cultures 543 
of P. aeruginosa PA14 were back diluted 1:50 and cultivated to an OD 600 0.4. 500 µL of culture 544 
was then mixed with 20 µL of purified S4-S4EndoUtox for a final concentration of 1.6 µM, and 545 
incubated at room temperature for 5, 15, 30, 45, or 60 minutes. Bacterial cells were then pelleted 546 
by centrifugation at 8,000 x g and frozen at -70 prior to RNA extraction and purification.  547 
 548 
Extraction, purification and sequencing of RNA 549 
 550 
Cell pellets were resuspended in 1 mL of TRIzol reagent ( ThermoFisher), vortexed for 10 551 
seconds, and incubated at room temperature for 5 minutes. Chloroform (200 µL) was added, and 552 
samples were vortexed for 30 seconds before incubation on ice for 2 minutes. Samples were 553 
briefly mixed and centrifuged at 14,000 x g for 15 minutes at 4 °C to separate the aqueous and 554 
organic phases. Approximately 500 µL of the upper aqueous phase was transferred to an equal 555 
volume of ice -cold isopropanol, vortexed for 15 seconds, and incubated on ice for 20 minutes. 556 
RNA was pelleted by centrifugation at 14,000 x g for 15 minutes at 4 °C, washed three times with 557 
1 mL of 75% ethanol, and air-dried. Pellets were resuspended in 100 µL of DNase I reaction buffer 558 
(NEB; 10 mM Tris-HCl pH 7.6, 2.5 mM MgCl2, 0.5 mM CaCl2) and treated with 4 units of DNase 559 
I (NEB) for 30 minutes at 37 °C. RNA was further purified using the Monarch RNA Cleanup Kit 560 
(NEB) according to the manufacturer’s instructions and eluted in DEPC -treated water. RNA 561 
concentration and purity were assessed  via absorbance at 254 nm using a NanoDrop One C . 562 
Sample concentrations were adjusted to a final concentration of 100 ng/µL and stored at -80 °C. 563 
RNA was sequenced using Illumina with rRNA depletion and number of reads (SeqCenter).  564 
 565 
RNA-seq read processing and alignment 566 
 567 
Paired-end sequencing reads were quality -filtered and trimmed using fastp before alignment to 568 
the P. aeruginosa PA14 reference genome (NC_008463) using Bowtie2 with the --very-sensitive 569 
and --end-to-end settings (51, 52). Resulting alignments were sorted and indexed using SAMtools 570 
(53). Gene-level read counts were generated using featureCounts with reverse-stranded, paired-571 
end fragment counting (-s 2 -p --countReadPairs), using the NCBI PA14 genome annotation and 572 
grouping features by locus tag (54). 573 
 574 
Transcript abundance and expression analysis  575 
 576 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

Transcript abundance was calculated as transcripts per million (TPM) by normalizing gene -level 577 
fragment counts to annotated gene lengths and subsequently scaling to one million transcripts 578 
per sample. Relative expression was determined by comparing TPM values between all  579 
experimental conditions (EndoUtox exposure for 5 and 15 minutes, and heterologous expression 580 
of RtcR∆CARF) and the empty vector control (no toxin, no induction). Genes exhibiting at least a 581 
2.5-fold change in either direction, with a minimum abundance of 10 TPM in at least one condition, 582 
were classified as differentially expression. A pseudocount of 1 TPM was applied when calculating 583 
fold changes. Coverage tracks were generated using deepTools bamCoverage with counts-per-584 
million (CPM) normalization and a bin size of 1 nucleotide (55). Coverage tracks were visualized 585 
using Integrative Genomics Viewer (IGV) (56). 586 
 587 
Urea-polyacrylamide gel electrophoresis 588 
 589 
200 ng of purified RNA in water was diluted 1:2 with 2x RNA loading dye (NEB) . Sample were 590 
heated to 80 °C for 2 minutes to denature RNA and then placed on ice for 5 minutes. Samples 591 
were then separated using 10 cm TBE-denaturing acrylamide gels ( 8.25% v/v acrylamide,  8M 592 
urea,1X TBE) at 200V for 50 minutes  in 1X TBE buffer. Gels were stained for 10 minutes with  593 
SYRB gold (ThermoFisher) and visualized using an Azure 200 Gel Imaging Workstation (Azure 594 
Biosystems).  595 
 596 
Northern Blotting 597 
 598 
RNA resolved by urea -PAGE was transferred to a positively charged quaternary amine nylon 599 
membrane (Roche) via wet transfer at 0.4 A for 45 minutes using a BioRad Mini Trans -Blot 600 
electrophoretic transfer system. RNA was crosslinked to the membrane using a Stratalinker UV 601 
crosslinker with the “Auto Crosslink” setting , and the  membrane was subsequently transferred 602 
directly into 10 mL of ULTRAhyb-Oligo hybridization buffer (Thermo Fisher Scientific), preheated 603 
to 42 °C in a shaking incubator rotating at 70 rpm. After prehybridization for 10 minutes, 604 
biotinylated DNA probe was added to the buffer  at a final concentration of 3 nM. Hybridization 605 
was performed overnight, and membranes were washed twice for 10 minutes each with 10 mL of 606 
stringency wash buffer (2 x SSC, 5% SDS, w/v) at 42 °C with gentle agitation . Blots were then 607 
moved to room temperature and washed twice for 10 minutes with 10 mL of wash buffer (PBS, 608 
pH 7.4, 0.5% SDS, w/v) , followed by three washes with 10 mL of blocking buffer (PBS, pH 7.4, 609 
0.5% SDS, w/v, 0.1% Thermo Fisher I-Block reagent). Blots were left in blocking buffer for 1 hour 610 
at room temperature. Licor IRDye 800CW was diluted 1:5,000 into 12 mL of fresh blocking buffer 611 
and added to the blot. After 1 hour of incubation with gentle agitation, the blot was washed twice 612 
with 10 mL of blocking buffer and then twice with 10 mL of wash buffer. Blots were subsequently 613 
imaged using a Licor Odyssey CLx imaging system. Following imaging, RNA ladder positions on 614 
Northern blots were determined by overlaying an image of the acrylamide gel containing 615 
separated RNA stained with SYBR Gold prior to transfer and marking the corresponding positions 616 
of the RNA standards on the blot. 617 
 618 
Sequence database and profile HMM search  619 
 620 
The Band7 protein from P. aeruginosa PA14 was used as a query in iterative PSI -BLAST 621 
searches (2 rounds)  to identify 19 candidate vault -like Band7 proteins from diverse bacterial 622 
species. Candidate proteins were manually inspected using AlphaFold structural models available 623 
through InterPro to confirm the presence of N-terminal globular repeat domains characteristic of 624 
vault proteins. The 19 sequences were aligned using MAFFT, and the resulting alignment was 625 
used to construct a profile Hidden Markov model (HMM) using HMMER hmmbuild (57, 58). The 626 
HMM was searched against a local database of approximately 88.8 million nonredundant protein 627 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

sequences derived from bacterial and archaeal NCBI RefSeq assemblies using hmmsearch. Hits 628 
were retained using a full-sequence E-value threshold of ≤1 x 10-30, a minimum protein length of 629 
150 amino acids, and exclusion of proteins with NP_ or YP_ accession prefixes, yielding 2,026 630 
candidate vault-like Band7 proteins.  631 
 632 
Phylogenetic and gene neighborhood analyses 633 
 634 
Candidate proteins were clustered using MMseqs2 at 90% sequence identity and 80% alignment 635 
coverage, yielding 1,31 2 representative proteins (58). Taxonomic assignments were obtained 636 
using NCBI taxonomy, and archaeal sequences and proteins with unresolved bacterial taxonomic 637 
assignments were excluded. The remaining representative proteins and 19 initial query 638 
sequences were aligned using MAFFT ( --auto) (58). An approximately maximum -likelihood 639 
phylogeny was inferred using FastTree with default parameters and visualized using Interactive 640 
Tree of Life (iTOL) (59, 60). 641 
 642 
Genomic neighborhood analysis of vault-like Band7 proteins  643 
 644 
The genomic neighborhoods of Band7 homologs were examined using FlaGs2 (Flanking Genes) 645 
(61). RefSeq protein accession numbers were used to retrieve genomic regions encompassing 646 
five protein -coding genes upstream and downstream of each Band7 homolog ( -g 5). Gene 647 
neighborhoods were compared across bacterial taxonomic groups to identify conserved gene 648 
associations. Genomic regions were retrieved from NCBI as annotated GenBank files and 649 
visualized using Geneious Prime version X. 650 
 651 
Structural modeling of bacterial vault-like Band7 proteins 652 
 653 
Protein structures of bacterial vault -like Band7 homologs were predicted using the AlphaFold 654 
online server (62). Predicted structures were visually inspected to assess conservation of the 655 
vault-like architecture, including variation in the number of N -terminal repeat domains and the 656 
length of the C-terminal cap helix. Structural models were visualized and rendered using UCSF 657 
ChimeraX(63). 658 
 659 
Multiple sequence alignment of P. aeruginosa arginyl-tRNA sand bRNA 660 
 661 
Annotated P. aeruginosa  PA14 arginine tRNA sequences and the tRNA -like region of bRNA  662 
(PA14_60630) were extracted and aligned using the Geneious multiple sequence alignment tool 663 
with default settings. 664 
 665 
Secondary structure prediction of arginyl-tRNA and bRNA 666 
 667 
The mimimum free energy secondary structures of P. aeruginosa arginyl-tRNAACG and tRNA-like 668 
region of bRNA was modelled using the Vienna RNAfold webserver under default settings (64). 669 
  670 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

Figures: 671 
 672 
Figure 1. Pyocin S4 engineered into a RNAse delivery platform 673 
(A) Schematic illustrating the major antibacterial toxin delivery mechanisms used by P. 674 
aeruginosa. Attacking P. aeruginosa cell is shown in green and the targeted bacterium in gray. 675 
(B) Distribution of cellular targets for experimentally characterized antibacterial toxin domains 676 
identified in our literature survey (Table S1). 677 
(C) Domain architectures of native pyocin S4 (S4-S4tox), engineered S4 ribotoxin chimeras, and 678 
pyocin S2 used in this study. Transporter-binding domain (TBD); Antigen-binding domain (ABD); 679 
Inner membrane translocation domain (IMTD). 680 
(D) AlphaFold-predicted structure of P. aeruginosa pyocin S4 in complex with its cognate immunity 681 
protein. The inset highlights the interaction between the toxin domain and the immunity protein. 682 
Domain colors and labels correspond to (C). 683 
(E) Toxicity assay showing tenfold serial dilutions of P. aeruginosa following exposure to the 684 
indicated toxins, spotted onto LB agar. For simplicity, the S4- prefix has been omitted and data 685 
are labelled according to toxin domains. -/-, no toxin exposure or immunity induction; Toxin/-, 686 
toxin exposure without immunity induction; Toxin/Immunity, toxin exposure with expression of 687 
the corresponding immunity protein induced with 250 µM IPTG.  688 
  689 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 690 
Figure 2. The P. aeruginosa PA14 Rtc operon protects against ribotoxins 691 
(A) Urea-PAGE analysis of total cellular RNA extracted from P. aeruginosa pre- and post- 15 min 692 
of exposure to the indicated ribotoxins. Major RNA species and cleavage products are indicated. 693 
(B) RNA-sequencing analysis of P. aeruginosa  following 5 or 15 min utes of S4 -EndoUtox 694 
intoxication. Gene expression (transcripts per million, TPM) is plotted against untreated control 695 
cells. Genes within the rtc locus and the adjacent tRNAArg are highlighted. Dashed lines indicate 696 
equal expression between conditions. Colored data points correspond to (C).  697 
(C) Gene locus schematic of the  P. aeruginosa and E.coli rtc operons. Locus tags for the P. 698 
aeruginosa operon are indicated under each gene.  699 
(D) Quantification of colony-forming units (CFU ml -1) of wildtype and ∆rtc-locus P. aeruginosa 700 
PA14 following exposure to the indicated toxins. Data are the mean ± standard error of the mean 701 
(SEM) of three biological replicates (n = 3), with individual replicates shown as points. 702 
  703 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 704 
Figure 3. Rtc locus components required for distinct ribotoxins 705 
(A and B) Toxicity assays showing tenfold serial dilutions of the indicated P. aeruginosa mutants 706 
following exposure to S4-S4tox (A) or S4-EndoUtox (B), spotted onto LB agar. 707 
(C) RNA-sequencing analysis of P. aeruginosa 20 minutes after induction of rtcR∆CARF 708 
with 250 µM IPTG. Gene expression (transcripts per million, TPM) is plotted against  an empty 709 
vector containing control strain . Genes within the Rtc locus and the adjacent tRNA Arg are 710 
highlighted. Dashed lines indicate equal expression between conditions. 711 
(D and E) Toxicity assays showing tenfold serial dilutions of the indicated P. aeruginosa strains 712 
expressing rtcR∆CARF or carrying an empty vector control (EV), following exposure to S4-S4tox (D) 713 
or S4-EndoUtox (E). Cells were spotted onto LB agar supplemented with 250 μM IPTG. 714 
  715 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 716 
Figure 4. Band7 and a tRNA -like noncoding RNA confer protection against ribotoxin -717 
mediated damage 718 
(A) Domain architecture and AlphaFold-predicted structural model of P. aeruginosa Band7 protein 719 
compared to the structure of  the human major vault protein (PD B 9BW5). Corresponding 720 
structural features are indicated.  721 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

(B) Predicted oligomeric assembly of the P. aeruginosa Band7 modelled as a 12-mer compared 722 
with the human vault complex (PDB 9BW5). A protomer in each structure is highlighted.  723 
(C) Tenfold serial dilutions of wildtype  P. aeruginosa, ∆rtc-locus, and ∆ band7 strains carrying 724 
either an empty vector (EV) or a plasmid expressing band7, following intoxication with S4 -725 
EndoUtox. Cells were spotted onto LB agar supplemented with 250 μM IPTG. 726 
(D) RNA-sequencing coverage across the P. aeruginosa Rtc operon in untreated cells, cells 727 
intoxicated with S4 -EndoUtox, and cells expressing RtcR lacking its N -terminal CARF domain  728 
(rtcR∆CARF). Coverage is shown as log -transformed counts per million (CPM). The annotated 729 
tRNA-like region upstream of band7, subsequently identified as part of bRNA, is highlighted. 730 
(E) Northern blot analysis of bRNA expression using four probes targeting the indicated regions 731 
of the transcript. RNA was isolated from wildtype P. aeruginosa and the ∆rtc-locus mutant grown 732 
in the presence or absence of IPTG. Arrowheads indicate the approximately 450-nucleotide bRNA 733 
transcript. A background band for probe 4 is indicated by * .The 5S rRNA imaged prior to 734 
electrophoretic transfer of RNA to the membrane is used as loading control. 735 
(F) Tenfold serial dilutions of wildtype PA14, ∆rtc-locus, and ∆band7 strains carrying either an 736 
empty vector (EV) or a plasmid expressing bRNA and band7, following intoxication with S4 -737 
EndoUtox. Cells were spotted onto LB agar supplemented with 250 μM IPTG. 738 
  739 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 740 
Figure 5. EndoUtox selectively cleaves tRNAs, 23S rRNA, and the Band7-associated bRNA 741 
(A) Northern blot analysis of tRNA cleavage following intoxication with S4 -EndoUtox. RNA was 742 
isolated from PA14 cells before intoxication (Pre) or after 5, 15, 30, 45, and 60 min of intoxication. 743 
Probes targeting regions 3′ (Probe A) or 5′ (Probe B) of the anticodon loop of tRNA  ArgACG are 744 
indicated and correspond to labels in (C). Arrowheads indicate major cleavage products.  745 
(B) Northern blot analysis of 16S and 23S rRNA following S4 -EndoUtox intoxication. RNA was 746 
isolated from P. aeruginosa before intoxication (Pre) or at the indicated times post-intoxication. 747 
An approximately 150-nucleotide cleavage product of 23S rRNA is indicated by the arrowhead. 748 
(C) Secondary structure prediction depicting cloverleaf structure of tRNA Arg ACG and the tRNA-749 
like region of bRNA. Nucleotides are numbered according to their positions within respective 750 
tRNA-like sequences. The positions of probes used to target 5′ (Probe A) and 3′ (Probe B) of the 751 
anticodon region for each molecule are indicated in orange. The schematic in the top left depicts 752 
conserved features of the tRNA cloverleaf, including the D-loop (D), the anticodon loop (AC), the 753 
T-loop (T), and the CCA acceptor stem.  754 
(D) Northern blot analysis of bRNA cleavage following intoxication with S4 -EndoUtox. RNA was 755 
isolated from P. aeruginosa before intoxication (Pre) or at the indicated times post-intoxication. 756 
Probes targeting regions 3′ (Probe A) or 5′ (Probe B) of the anticodon loop of bRNA Arg ACG are 757 
indicated and correspond to labels in (C). Arrowheads indicate major cleavage products. 758 
(E) Northern blot analysis of bRNA cleavage following intoxication with the indicated ribotoxins. 759 
RNA was isolated from P. aeruginosa before intoxication (Pre) or at the indicated times post -760 
intoxication. Probes used are as in (D). Arrowheads indicate major cleavage products. 761 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 762 
Figure 6.  Vault-like Band7 proteins are widespread and frequently associate with RNA 763 
repair systems.  764 
(A) Maximum-likelihood phylogeny of 1,313 vault-like Band7 proteins identified across bacterial 765 
genomes. The outer ring indicates bacterial taxonomic groups, with colors corresponding to the 766 
legend. Letters indicate phylogenetic clusters examined in (B) and (C). Protein in clades E and F 767 
were non-vault like SPFH family members. The position of P. aeruginosa PA14 Band7 is indicated. 768 
Scale bar represents 0.25 amino acid substitutions per site. 769 
(B) Genomic neighborhoods of representative vault -like band7 homologs from the indicated 770 
phylogenetic clusters. Genes are colored according to their predicted functions, including 771 
transcriptional regulation, RNA ligation, RNA cyclization, and nucleotidyltransferase activity. 772 
Putative tRNA-like sequences adjacent to band7 are highlighted in green, with their predicted 773 
amino acid identities indicated when available. Blue shading highlights band7 and its associated 774 
tRNA-like region. Gene organization is shown to scale.  775 
(C) Predicted oligomeric structures of representative vault-like Band7 proteins from the indicated 776 
phylogenetic clusters. An individual Band7 protomer is highlighted in each structure. Structures 777 
are colored according to their corresponding taxonomic groups in (A). 778 
  779 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

Supplementary Figures: 780 
 781 
 782 
Figure S1. Generation of chimeric ribotoxins 783 
(A) Genomic organization of the Cdi and S-type pyocin loci encoding toxins used to generate the 784 
engineered ribotoxin panel, together with the DNA -targeting pyocin S2 used as a control.  Toxin 785 
domains and cognate immunity genes labeled “toxin” and “Imm,” respectively.  The bacterial 786 
strains from which each locus originates are indicated.  Breaks in cdiA genes indicate regions of 787 
DNA omitted for clarity.  788 
(B) Polyacrylamide gel electrophoresis of purified pyocins S2, S4, and chimeric S4 toxins co -789 
expressed with their respective immunity proteins. The predicted molecular weights of the toxin 790 
and immunity proteins, respectively, are as follows: S2 (74 and 10 kDa), S4-S4tox (81 and 13 kDa), 791 
S4-S6tox (81 and 9 kDa), S4 -D1tox (83 and 18 kDa), S4-D2tox (84 and 18 kDa), and S4 -EndoUtox 792 
(85 and 10 kDa). 793 
  794 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 795 
Figure S2. Challenge of the ∆rtc-locus mutant with diverse stressors 796 
(A) Urea-PAGE analysis of total cellular RNA extracted from P. aeruginosa exposed to S4 -797 
EndoUtox for the indicated time points. Major RNA species and cleavage products are indicated. 798 
(B) Quantification of colony -forming units (CFU) of wildtype and rtc -locus P. aeruginosa in the 799 
absence of toxin. Data are the mean ± SEM of three biological replicates (n = 3), with individual 800 
replicates shown as points. 801 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

(C) Disk diffusion assays comparing sensitivity of wildtype and ∆rtc -locus P. aeruginosa to the 802 
indicated antibiotics and other stressors. Compounds are grouped according to the cellular targets 803 
or processes they inhibit.  804 
(D) UV sensitivity of wildtype P. aeruginosa and the ∆rtc -locus mutant. Cultures were serially 805 
diluted tenfold and spotted onto LB agar before exposure to increasing doses of UV irradiation 806 
(80-200 μJ/cm2). 807 
(E) Temperature sensitivity of wildtype E. coli MG1655 and E. coli MG1655 carrying the Band7-808 
containing locus from E. coli ECOR67. Cultures were serially diluted tenfold, spotted onto LB agar, 809 
and incubated at 10 °C, 22°C, or 37 °C. The Ecor67 Band7 protein is a homolog to PA14 Band7. 810 
(F) Plaque formation (PFU mL -1) was enumerated for each phage infecting  wildtype E. coli  811 
MG1655 or MG1655 carrying the chromosomally integrated Band7-containing locus from E. coli 812 
ECOR67. The Ecor67 Bandy protein is a homolog to PA14 Band7. Fold protection was calculated 813 
by dividing the phage titer of wildtype MG1655 by that on MG1655 carrying the ECOR67 locus  814 
and depicted as a heatmap . Phages are grouped by family, indicated above each group, with 815 
numbers corresponding to their identifiers in the BASEL phage collection(65). 816 
  817 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 818 
Figure S3.  Constitutively active RtcR ∆CARF does not complement the ∆ band7 or ∆ rtcB 819 
mutants 820 
(A and B) Toxicity assays showing tenfold serial dilutions of the indicated P. aeruginosa strains 821 
expressing rtcR∆CARF or carrying an empty vector control (EV), following exposure to S4-EndoUtox 822 
(A) or S4-S4tox (B). Cells were spotted onto LB agar supplemented with 250 μM IPTG to induce 823 
protein expression. 824 
  825 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 826 
Figure S4. Requirement of Band7 and bRNA for protection against ribotoxic stress 827 
(A) Tenfold serial dilutions of wildtype P. aeruginosa or the ∆rtc -locus strain carrying either an 828 
empty vector (EV) or the indicated construct, following intoxication with S4 -EndoUtox. Cells were 829 
spotted onto LB agar supplemented with 250 μM IPTG. Introduction of a premature stop codon 830 
in the band7 reading frame abolished protection against S4-EndoUtox.  831 
  832 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

 833 
Figure S5. bRNA retains conserved features of tRNAs 834 
(A) Northern blot analysis of tRNA ArgCCU cleavage following intoxication with EndoUtox. RNA was 835 
isolated from P. aeruginosa before intoxication (Pre) or at the indicated times post -intoxication. 836 
Arrowheads indicate major cleavage products. 837 
(B) Northern blot analysis of tRNAs ArgCCU and SerGCU following intoxication with EndoUtox. RNA 838 
was isolated from P. aeruginosa  before intoxication (Pre) or at the indicated times post -839 
intoxication.  840 
(C) Multiple sequence alignment of five annotated arginine tRNAs in P. aeruginosa and the 74-841 
nucleotide tRNA-like region of bRNA (PA14_60620). Conserved sequence motifs corresponding 842 
to the D -stem/loop, anticodon region, and the T -stem/loop are highlighted. The sequence logo 843 
above the alignment indicates nucleotide conservation at each position.  844 
 845 
  846 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

Supplementary Tables: 847 
 848 
Table S1. Toxins used by P. aeruginosa during intermicrobial warfare 849 
A list of antibacterial toxins produced by P. aeruginosa with characterized bacterial killing 850 
activity. A non-exhaustive literature search identified 52 antibacterial toxins deployed through 851 
type six secretion, contact-dependent inhibition, or pyocin release. Note that that antibacterial 852 
activity has not been directly demonstrated for the CdiA1 and CdiA2 loci in P. aeruginosa PA14. 853 
However, as the equivalent loci in strain PAO1 have been characterized as having antibacterial 854 
activity, we included them in this list. We demonstrate their antibacterial properties in this study. 855 
References to studies showing antibacterial activity are included as Pubmed IDs under the row 856 
titled “Reference (Pubmed ID)”.  857 
 858 
Table S2. Raw read counts and transcripts per million (TPM) values from RNA 859 
sequencing.  860 
 861 
  862 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

References: 863 
 864 
1.  Z. C. Ruhe, D. A. Low, C. S. Hayes, Polymorphic Toxins and Their Immunity Proteins: 865 
Diversity, Evolution, and Mechanisms of Delivery. Annu Rev Microbiol 74, 497–520 (2020). 866 
2.  B. T. Ho, T. G. Dong, J. J. Mekalanos, A view to a kill: the bacterial type VI secretion 867 
system. Cell Host Microbe 15, 9–21 (2014). 868 
3.  B. J. Cuthbert, C. S. Hayes, C. W. Goulding, Functional and Structural Diversity of 869 
Bacterial Contact-Dependent Growth Inhibition Effectors. Front Mol Biosci 9, 866854 870 
(2022). 871 
4.  Y. C. Kim, A. W. Tarr, C. N. Penfold, Colicin import into E. coli cells: a model system for 872 
insights into the import mechanisms of bacteriocins. Biochim Biophys Acta 1843, 1717–873 
1731 (2014). 874 
5.  H. Georjon, A. Bernheim, The highly diverse antiphage defence systems of bacteria. Nat 875 
Rev Microbiol 21, 686–700 (2023). 876 
6.  D. S. Saxton, M. T. Laub, How bacterial immune systems sense phage infection. Nat Rev 877 
Microbiol, doi: 10.1038/s41579-026-01376-x (2026). 878 
7.  R. E. Sockett, Predatory lifestyle of Bdellovibrio bacteriovorus. Annu Rev Microbiol 63, 879 
523–539 (2009). 880 
8.  H. E. Ledvina, R. Sayegh, R. O. Carale, A. M. Burroughs, A. R. Macklin, A. L. Azadeh, L. 881 
D. Borja Najera, L. Aravind, A. T. Whiteley, Functional amyloid proteins confer defence 882 
against predatory bacteria. Nature 644, 197–204 (2025). 883 
9.  V. M. D’Costa, C. E. King, L. Kalan, M. Morar, W. W. L. Sung, C. Schwarz, D. Froese, G. 884 
Zazula, F. Calmels, R. Debruyne, G. B. Golding, H. N. Poinar, G. D. Wright, Antibiotic 885 
resistance is ancient. Nature 477, 457–461 (2011). 886 
10.  N. W. Kennedy, L. E. Comstock, Mechanisms of bacterial immunity, protection, and 887 
survival during interbacterial warfare. Cell Host Microbe 32, 794–803 (2024). 888 
11.  B. D. Ross, A. J. Verster, M. C. Radey, D. T. Schmidtke, C. E. Pope, L. R. Hoffman, A. M. 889 
Hajjar, S. B. Peterson, E. Borenstein, J. D. Mougous, Human gut bacteria contain acquired 890 
interbacterial defence systems. Nature 575, 224–228 (2019). 891 
12.  A. Azhieh, P. Hernandez, A. C. Anderson, D. Sychantha, A. J. Verster, J. C. Whitney, B. D. 892 
Ross, Rapidly evolving orphan immunity genes protect human gut bacteria from 893 
intoxication by the type VI secretion system. bioRxiv: The Preprint Server for Biology 894 
2025.05.03.651265 [Preprint] (2025). https://doi.org/10.1101/2025.05.03.651265. 895 
13.  L. M. Nolan, L. P. Allsopp, Antimicrobial Weapons of Pseudomonas aeruginosa. Adv Exp 896 
Med Biol 1386, 223–256 (2022). 897 
14.  A. Elfarash, Q. Wei, P. Cornelis, The soluble pyocins S2 and S4 from Pseudomonas 898 
aeruginosa bind to the same FpvAI receptor. Microbiologyopen 1, 268–275 (2012). 899 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

15.  A. Parret, R. De Mot, Novel bacteriocins with predicted tRNase and pore-forming activities 900 
in Pseudomonas aeruginosa PAO1. Mol Microbiol 35, 472–473 (2000). 901 
16.  T. Ogawa, S. Inoue, S. Yajima, M. Hidaka, H. Masaki, Sequence-specific recognition of 902 
colicin E5, a tRNA-targeting ribonuclease. Nucleic Acids Res 34, 6065–6073 (2006). 903 
17.  C. Mercy, B. Ize, S. P. Salcedo, S. de Bentzmann, S. Bigot, Functional Characterization of 904 
Pseudomonas Contact Dependent Growth Inhibition (CDI) Systems. PLoS One 11, 905 
e0147435 (2016). 906 
18.  Y. Sano, H. Matsui, M. Kobayashi, M. Kageyama, Molecular structures and functions of 907 
pyocins S1 and S2 in Pseudomonas aeruginosa. J Bacteriol 175, 2907–2916 (1993). 908 
19.  K. J. Hughes, X. Chen, A. M. Burroughs, L. Aravind, S. L. Wolin, An RNA Repair Operon 909 
Regulated by Damaged tRNAs. Cell Rep 33, 108527 (2020). 910 
20.  P. Genschik, K. Drabikowski, W. Filipowicz, Characterization of the Escherichia coli RNA 911 
3’-terminal phosphate cyclase and its sigma54-regulated operon. J Biol Chem 273, 25516–912 
25526 (1998). 913 
21.  C. Engl, J. Schaefer, I. Kotta-Loizou, M. Buck, Cellular and molecular phenotypes 914 
depending upon the RNA repair system RtcAB of Escherichia coli. Nucleic Acids Res 44, 915 
9933–9941 (2016). 916 
22.  J. E. Kurasz, C. E. Hartman, D. J. Samuels, B. K. Mohanty, A. Deleveaux, J. Mrázek, A. C. 917 
Karls, Genotoxic, Metabolic, and Oxidative Stresses Regulate the RNA Repair Operon of 918 
Salmonella enterica Serovar Typhimurium. J Bacteriol 200, e00476-18 (2018). 919 
23.  A. M. Burroughs, L. Aravind, RNA damage in biological conflicts and the diversity of 920 
responding RNA repair systems. Nucleic Acids Res 44, 8525–8555 (2016). 921 
24.  X. Chen, S. L. Wolin, Transfer RNA halves are found as nicked tRNAs in cells: evidence 922 
that nicked tRNAs regulate expression of an RNA repair operon. RNA 29, 620–629 (2023). 923 
25.  I. Kotta-Loizou, M. G. Giuliano, M. Jovanovic, J. Schaefer, F. Ye, N. Zhang, D. A. Irakleidi, 924 
X. Liu, X. Zhang, M. Buck, C. Engl, The RNA repair proteins RtcAB regulate transcription 925 
activator RtcR via its CRISPR-associated Rossmann fold domain. iScience 25, 105425 926 
(2022). 927 
26.  M. Bush, R. Dixon, The role of bacterial enhancer binding proteins as specialized 928 
activators of σ54-dependent transcription. Microbiol Mol Biol Rev 76, 497–529 (2012). 929 
27.  N. Tanaka, S. Shuman, RtcB is the RNA ligase component of an Escherichia coli RNA 930 
repair operon. J Biol Chem 286, 7727–7731 (2011). 931 
28.  A. K. Chakravarty, R. Subbotin, B. T. Chait, S. Shuman, RNA ligase RtcB splices 3’-932 
phosphate and 5’-OH ends via covalent RtcB-(histidinyl)-GMP and polynucleotide-933 
(3’)pp(5’)G intermediates. Proc Natl Acad Sci U S A 109, 6072–6077 (2012). 934 
29.  T. Ogawa, K. Tomita, T. Ueda, K. Watanabe, T. Uozumi, H. Masaki, A cytotoxic 935 
ribonuclease targeting specific transfer RNA anticodons. Science 283, 2097–2100 (1999). 936 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

30.  C. Ma, C. Wang, D. Luo, L. Yan, W. Yang, N. Li, N. Gao, Structural insights into the 937 
membrane microdomain organization by SPFH family proteins. Cell Res 32, 176–189 938 
(2022). 939 
31.  M. Hinderhofer, C. A. Walker, A. Friemel, C. A. O. Stuermer, H. M. Möller, A. Reuter, 940 
Evolution of prokaryotic SPFH proteins. BMC Evol Biol 9, 10 (2009). 941 
32.  M. González-Álamos, P. Guerra, N. Verdaguer, Structure, Dynamics and Functional 942 
Implications of the Eukaryotic Vault Complex. Subcell Biochem 104, 531–548 (2024). 943 
33.  H. Tanaka, K. Kato, E. Yamashita, T. Sumizawa, Y. Zhou, M. Yao, K. Iwasaki, M. 944 
Yoshimura, T. Tsukihara, The structure of rat liver vault at 3.5 angstrom resolution. Science 945 
323, 384–388 (2009). 946 
34.  A. Carruthers, S. Fatma, R. H. Huang, Biochemical and structural characterization of the 947 
RlaP family nucleotidyltransferase potentially involved in RNA repair. bioRxiv: The Preprint 948 
Server for Biology 2025.12.29.696909 [Preprint] (2025). 949 
https://doi.org/10.64898/2025.12.29.696909. 950 
35.  H. E. Ledvina, R. Sayegh, R. O. Carale, A. M. Burroughs, A. R. Macklin, A. L. Azadeh, L. 951 
D. Borja Najera, L. Aravind, A. T. Whiteley, Functional amyloid proteins confer defence 952 
against predatory bacteria. Nature 644, 197–204 (2025). 953 
36.  S.-Y. Ting, K. D. LaCourse, H. E. Ledvina, R. Zhang, M. C. Radey, H. D. Kulasekara, R. 954 
Somavanshi, S. K. Bertolli, L. A. Gallagher, J. Kim, K. M. Penewit, S. J. Salipante, L. Xu, S. 955 
B. Peterson, J. D. Mougous, Discovery of coordinately regulated pathways that provide 956 
innate protection against interbacterial antagonism. Elife 11, e74658 (2022). 957 
37.  D. M. Brinkley, S. K. Bertolli, L. A. Gallagher, Y. Tan, M. Motha de Silva, A. Brockman, D. 958 
Zhang, S. B. Peterson, J. D. Mougous, Pseudomonads coordinate innate defense against 959 
viruses and bacteria with a single regulatory system. Cell Host Microbe 33, 1333-1346.e7 960 
(2025). 961 
38.  T. H. Sokolskyi, Bacterial Major Vault Protein homologs shed new light on origins of the 962 
enigmatic organelle. Evolutionary Biology [Preprint] (2019). https://doi.org/10.1101/872010. 963 
39.  T. K. Daly, A. J. Sutherland-Smith, D. Penny, In silico resurrection of the major vault protein 964 
suggests it is ancestral in modern eukaryotes. Genome Biol Evol 5, 1567–1583 (2013). 965 
40.  R. D. Schaeffer, J. Pei, R. Guo, J. Zhang, K. Medvedev, Q. Cong, N. Grishin, Domain 966 
classification of archaeal proteomes reveals conserved fold repertoire. PLoS Comput Biol 967 
22, e1014188 (2026). 968 
41.  J. F. Banfield, L. E. Valentin-Alvarado, L.-D. Shi, C. M. Robinson, R. S. Bamert, F. 969 
Coulibaly, Z. K. Barth, F. O. Aylward, M. C. Schoelmerich, S. Lei, R. Sachdeva, G. J. Knott, 970 
Convergent evolution of viral-like Borg archaeal extrachromosomal elements and giant 971 
eukaryotic viruses. Nat Commun 16, 10641 (2025). 972 
42.  S. Köstlbacher, J. J. E. van Hooff, K. Panagiotou, D. Tamarit, V. De Anda, K. E. Appler, B. 973 
J. Baker, T. J. G. Ettema, Prediction of eukaryotic cellular complexity in Asgard archaea 974 
using structural modelling. Nat Microbiol 11, 747–758 (2026). 975 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

43.  T. M. Santos, E. Galvão, H. Gomes, L.-E. Del-Bem, Characterization and Phylogenetic 976 
Insights into the First Viral Major Vault Proteins (MVPs), Identified in Bacteriophages from 977 
the Human Gut. Genomics [Preprint] (2023). https://doi.org/10.1101/2023.11.10.566534. 978 
44.  J. S. Athukoralage, P. H. Yoon, A. Shanehsazzadeh, E. Kauderer-Abrams, N. T. Perry, M. 979 
G. Durrant, Prokaryotic homologs of the major vault protein form engineerable vault 980 
nanocapsules. Molecular Biology [Preprint] (2026). 981 
https://doi.org/10.64898/2026.11.04.764334. 982 
45.  J. C. Lachowicz, M. Hoque, A. Zhou, T. Zhang, M. C. Franklin, R. Copin, K. D. Cygnar, A. 983 
J. Murphy, K. Saotome, A. D. Baik, Bacterial major vault protein homologs form divergent 984 
vault structures. Biochemistry [Preprint] (2026). 985 
https://doi.org/10.64898/2026.11.06.764734. 986 
46.  N. L. Kedersha, L. H. Rome, Isolation and characterization of a novel ribonucleoprotein 987 
particle: large structures contain a single species of small RNA. J Cell Biol 103, 699–709 988 
(1986). 989 
47.  V. A. Kickhoefer, S. K. Vasu, L. H. Rome, Vaults are the answer, what is the question? 990 
Trends Cell Biol 6, 174–178 (1996). 991 
48.  D. G. Gibson, L. Young, R.-Y. Chuang, J. C. Venter, C. A. Hutchison, H. O. Smith, 992 
Enzymatic assembly of DNA molecules up to several hundred kilobases. Nat Methods 6, 993 
343–345 (2009). 994 
49.  N. P. Bullen, D. Sychantha, S. S. Thang, P. H. Culviner, M. Rudzite, S. Ahmad, V. S. Shah, 995 
A. Filloux, G. Prehna, J. C. Whitney, An ADP-ribosyltransferase toxin kills bacterial cells by 996 
modifying structured non-coding RNAs. Mol Cell 82, 3484-3498.e11 (2022). 997 
50.  K. A. Datsenko, B. L. Wanner, One-step inactivation of chromosomal genes in Escherichia 998 
coli K-12 using PCR products. Proc Natl Acad Sci U S A 97, 6640–6645 (2000). 999 
51.  S. Chen, Y. Zhou, Y. Chen, J. Gu, fastp: an ultra-fast all-in-one FASTQ preprocessor. 1000 
Bioinformatics 34, i884–i890 (2018). 1001 
52.  B. Langmead, S. L. Salzberg, Fast gapped-read alignment with Bowtie 2. Nat Methods 9, 1002 
357–359 (2012). 1003 
53.  H. Li, B. Handsaker, A. Wysoker, T. Fennell, J. Ruan, N. Homer, G. Marth, G. Abecasis, R. 1004 
Durbin, 1000 Genome Project Data Processing Subgroup, The Sequence Alignment/Map 1005 
format and SAMtools. Bioinformatics 25, 2078–2079 (2009). 1006 
54.  Y. Liao, G. K. Smyth, W. Shi, featureCounts: an efficient general purpose program for 1007 
assigning sequence reads to genomic features. Bioinformatics 30, 923–930 (2014). 1008 
55.  F. Ramírez, D. P. Ryan, B. Grüning, V. Bhardwaj, F. Kilpert, A. S. Richter, S. Heyne, F. 1009 
Dündar, T. Manke, deepTools2: a next generation web server for deep-sequencing data 1010 
analysis. Nucleic Acids Res 44, W160-165 (2016). 1011 
56.  J. T. Robinson, H. Thorvaldsdóttir, W. Winckler, M. Guttman, E. S. Lander, G. Getz, J. P. 1012 
Mesirov, Integrative genomics viewer. Nat Biotechnol 29, 24–26 (2011). 1013 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 

57.  S. R. Eddy, Accelerated Profile HMM Searches. PLoS Comput Biol 7, e1002195 (2011). 1014 
58.  K. Katoh, D. M. Standley, MAFFT multiple sequence alignment software version 7: 1015 
improvements in performance and usability. Mol Biol Evol 30, 772–780 (2013). 1016 
59.  M. N. Price, P. S. Dehal, A. P. Arkin, FastTree 2--approximately maximum-likelihood trees 1017 
for large alignments. PLoS One 5, e9490 (2010). 1018 
60.  I. Letunic, P. Bork, Interactive Tree of Life (iTOL) v6: recent updates to the phylogenetic 1019 
tree display and annotation tool. Nucleic Acids Res 52, W78–W82 (2024). 1020 
61.  C. K. Saha, R. Sanches Pires, H. Brolin, M. Delannoy, G. C. Atkinson, FlaGs and 1021 
webFlaGs: discovering novel biology through the analysis of gene neighbourhood 1022 
conservation. Bioinformatics 37, 1312–1314 (2021). 1023 
62.  J. Abramson, J. Adler, J. Dunger, R. Evans, T. Green, A. Pritzel, O. Ronneberger, L. 1024 
Willmore, A. J. Ballard, J. Bambrick, S. W. Bodenstein, D. A. Evans, C.-C. Hung, M. 1025 
O’Neill, D. Reiman, K. Tunyasuvunakool, Z. Wu, A. Žemgulytė, E. Arvaniti, C. Beattie, O. 1026 
Bertolli, A. Bridgland, A. Cherepanov, M. Congreve, A. I. Cowen-Rivers, A. Cowie, M. 1027 
Figurnov, F. B. Fuchs, H. Gladman, R. Jain, Y. A. Khan, C. M. R. Low, K. Perlin, A. 1028 
Potapenko, P. Savy, S. Singh, A. Stecula, A. Thillaisundaram, C. Tong, S. Yakneen, E. D. 1029 
Zhong, M. Zielinski, A. Žídek, V. Bapst, P. Kohli, M. Jaderberg, D. Hassabis, J. M. Jumper, 1030 
Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 1031 
493–500 (2024). 1032 
63.  E. F. Pettersen, T. D. Goddard, C. C. Huang, E. C. Meng, G. S. Couch, T. I. Croll, J. H. 1033 
Morris, T. E. Ferrin, UCSF ChimeraX: Structure visualization for researchers, educators, 1034 
and developers. Protein Sci 30, 70–82 (2021). 1035 
64.  M. Zuker, P. Stiegler, Optimal computer folding of large RNA sequences using 1036 
thermodynamics and auxiliary information. Nucleic Acids Res 9, 133–148 (1981). 1037 
65.  E. Maffei, A. Shaidullina, M. Burkolter, Y. Heyer, F. Estermann, V. Druelle, P. Sauer, L. Willi, 1038 
S. Michaelis, H. Hilbi, D. S. Thaler, A. Harms, Systematic exploration of Escherichia coli 1039 
phage-host interactions with the BASEL phage collection. PLoS Biol 19, e3001424 (2021). 1040 
 1041 
.CC-BY-NC-ND 4.0 International licenseavailable under a 
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprintthis version posted November 21, 2026. ; https://doi.org/10.64898/2026.11.20.768214doi: bioRxiv preprint 