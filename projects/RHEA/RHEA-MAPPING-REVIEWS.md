---
title: "RHEA->GO Mapping Reviews: enzymes backing the curated mappings"
---

# RHEA->GO Mapping Reviews

**Parent project:** [RHEA.md](../RHEA.md) - **Mapping set:** [rhea2go.sssom.yaml](rhea2go.sssom.yaml)

Every curated RHEA->GO mapping in [`rhea2go.sssom.yaml`](rhea2go.sssom.yaml) is backed here by a review
of a reviewed (Swiss-Prot) enzyme that carries the reaction. All RHEA reactions are **absent from the
public `rhea2go`**; GO ids are QuickGO-verified non-obsolete molecular-function terms; `PE1` = protein-
level (experimental) existence. Most exactMatch rows are **EC-bridge supported** (`ec2go(EC)=GO term`
and `rhea2ec(reaction)=EC`).

## exactMatch / broadMatch mappings

| RHEA | GO term | Reviewed enzyme | Organism | Evidence | Type |
|------|---------|-----------------|----------|----------|------|
| RHEA:11536 | GO:0033713 choline:oxygen 1-oxidoreductase activity | Choline oxidase (Q7X2H8) | Arthrobacter globiformis | PE1, PMID:12795615 | exactMatch |
| RHEA:28106 | GO:0008868 galactitol-1-phosphate 5-dehydrogenase activity | Galactitol 1-phosphate 5-dehydrogenase (P0A9S3) | Escherichia coli | PE1, PMID:13331868 | exactMatch |
| RHEA:37599 | GO:0102988 acyl-CoA 15-desaturase activity | Fatty acid desaturase DES3 (Q594P3) | Sorghum bicolor | PE1, PMID:17178719 | exactMatch |
| RHEA:41792 | GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity | Malonyl-CoA-acyl carrier protein transacylase, mitochondrial (Q8IVS2) | Homo sapiens | PE1, PMID:19549604 | exactMatch |
| RHEA:42664 | GO:0044103 L-arabinose 1-dehydrogenase (NADP+) activity | L-arabinose 1-dehydrogenase (D4GP33) | Haloferax volcanii | PE1, PMID:23949136 | exactMatch |
| RHEA:43620 | GO:0031132 serine 3-dehydrogenase activity | NADP-dependent 3-hydroxy acid dehydrogenase YdfG (P39831) | Escherichia coli | PE1, PMID:12535615 | exactMatch |
| RHEA:49072 | GO:0018640 dibenzothiophene monooxygenase activity | Dibenzothiophene monooxygenase (Q6WNP1) | Rhodococcus erythropolis | PE1, PMID:24470304 | exactMatch |
| RHEA:67008 | GO:0004482 mRNA 5'-cap (guanine-N7-)-methyltransferase activity | mRNA cap guanine-N (O43148) | Homo sapiens | PE1, PMID:9790902 | exactMatch |
| RHEA:67012 | GO:0004484 mRNA guanylyltransferase activity | mRNA-capping enzyme (O60942) | Homo sapiens | PE1, PMID:9473487 | exactMatch |
| RHEA:73067 | GO:0033925 mannosyl-glycoprotein endo-beta-N-acetylglucosaminidase activity | Cytosolic endo-beta-N-acetylglucosaminidase 1 (F4JZC2) | Arabidopsis thaliana | PE1, PMID:21796445 | exactMatch |
| RHEA:76995 | GO:0004324 ferredoxin-NADP+ reductase activity | Ferredoxin--NADP reductase A (A9ES55) | Sorangium cellulosum | PE1, PMID:19696019 | exactMatch |
| RHEA:77171 | GO:0047708 biotinidase activity | Biotinidase (P43251) | Homo sapiens | PE1, PMID:9654207 | exactMatch |
| RHEA:10908 | GO:0047704 bile-salt sulfotransferase activity | Sulfotransferase 2A6 (B2RVI8) | Mus musculus | PE2, Swiss-Prot curator | exactMatch |
| RHEA:11440 | GO:0018677 pentachlorophenol monooxygenase activity | Pentachlorophenol 4-monooxygenase (P42535) | Sphingobium chlorophenolicum | PE1, PMID:25238136 | exactMatch |
| RHEA:11608 | GO:0050208 polysialic-acid O-acetyltransferase activity | Polysialic acid O-acetyltransferase (A1ADJ6) | Escherichia coli O1:K1 / APEC | PE1, PMID:17519228 | exactMatch |
| RHEA:11640 | GO:0033729 anthocyanidin reductase activity | Anthocyanidin reductase (Q9SEV0) | Arabidopsis thaliana | PE1, PMID:14725861 | exactMatch |
| RHEA:12500 | GO:0047127 thiomorpholine-carboxylate dehydrogenase activity | Ketimine reductase mu-crystallin (Q14894) | Homo sapiens | PE1, PMID:25931162 | exactMatch |
| RHEA:12609 | GO:0008119 thiopurine S-methyltransferase activity | Thiopurine S-methyltransferase (P51580) | Homo sapiens | PE1, PMID:657528 | exactMatch |
| RHEA:12685 | GO:0050627 mycothione reductase [NAD(P)H] activity | Mycothione reductase (P9WHH3) | Mycobacterium tuberculosis | PE1, PMID:10512639 | exactMatch |
| RHEA:13817 | GO:0047057 vitamin-K-epoxide reductase (warfarin-sensitive) activity | Vitamin K epoxide reductase complex subunit 1-like protein 1 (Q8N0U8) | Homo sapiens | PE1, PMID:24532791 | exactMatch |
| RHEA:14105 | GO:0004735 pyrroline-5-carboxylate reductase activity | Pyrroline-5-carboxylate reductase 1, mitochondrial (P32322) | Homo sapiens | PE1, PMID:28258219 | exactMatch |
| RHEA:16573 | GO:0004648 O-phospho-L-serine:2-oxoglutarate transaminase activity | Phosphoserine aminotransferase (P23721) | Escherichia coli | PE1, PMID:8706854 | exactMatch |
| RHEA:16905 | GO:0047408 alkenylglycerophosphocholine hydrolase activity | Lysoplasmalogenase TMEM86A (Q8N2M4) | Homo sapiens | PE1, PMID:36592658 | exactMatch |
| RHEA:18021 | GO:0047288 beta-D-galactosyl-(1->3)-N-acetyl-beta-D-galactosaminide alpha-2,3- sialyltransferase activity | CMP-N-acetylneuraminate-beta-galactosamide-alpha-2,3-sialyltransferase 1 (Q11201) | Homo sapiens | PE1, PMID:8027041 | exactMatch |
| RHEA:16981 | GO:0018506 maleylacetate reductase activity | Maleylacetate reductase 2 (P94135) | Cupriavidus pinatubonensis | PE1, Swiss-Prot curator | exactMatch |
| RHEA:14317 | GO:0050109 morphine 6-dehydrogenase activity | Aldo-keto reductase family 1 member C13 (P82809) | Mesocricetus auratus | PE1, Swiss-Prot curator | exactMatch |
| RHEA:48940 | GO:0016805 dipeptidase activity | Dipeptidase 2 (Q9H4A9) | Homo sapiens | PE1, PMID:32325220 | broadMatch |

## New GO term suggestions (no suitable GO MF term exists)

These reviewed enzymes catalyse a well-characterised reaction for which **QuickGO returns no specific
molecular-function term**. Each is recorded in the mapping set as `sssom:NoTermFound` with a proposed
term, and is a GO new-term-request candidate.

### (S)-2-hydroxypropylphosphonic acid epoxidase (hppE Q56185)
- **Organism / evidence:** Streptomyces wedmorensis; reviewed, PE1, catalytic activity PMID:16015285.
- **Reaction (RHEA:10808, EC 1.11.1.23):** (S)-2-hydroxypropylphosphonate + H2O2 = (1R,2S)-epoxypropylphosphonate + 2 H2O
- **GO status:** no specific MF term (QuickGO). **Proposed new term:** *(S)-2-hydroxypropylphosphonic acid epoxidase activity*, anchored to RHEA:10808 / EC 1.11.1.23.

### [2-(trimethylamino)ethyl]phosphonate dioxygenase (tmpA A0A4V8H042)
- **Organism / evidence:** Leisingera caerulea; reviewed, PE1, catalytic activity PMID:30789718.
- **Reaction (RHEA:11380, EC 1.14.11.72):** [2-(trimethylamino)ethyl]phosphonate + 2-oxoglutarate + O2 = [(1R)-1-hydroxy-2-(trimethylamino)ethyl]phosphonate + succinate + CO2
- **GO status:** no specific MF term (QuickGO). **Proposed new term:** *[2-(trimethylamino)ethyl]phosphonate dioxygenase activity*, anchored to RHEA:11380 / EC 1.14.11.72.

### Cellobionic acid phosphorylase (cbp Q8P3J4)
- **Organism / evidence:** Xanthomonas campestris pv. campestris; reviewed, PE1, catalytic activity PMID:24055472.
- **Reaction (RHEA:11564, EC 2.4.1.321):** 4-O-beta-D-glucopyranosyl-D-gluconate + phosphate = D-gluconate + alpha-D-glucose 1-phosphate
- **GO status:** no specific MF term (QuickGO). **Proposed new term:** *Cellobionic acid phosphorylase activity*, anchored to RHEA:11564 / EC 2.4.1.321.

### 1,4-beta-mannosyl-N-acetylglucosamine phosphorylase (BT_0458 Q8A8Y4)
- **Organism / evidence:** Bacteroides thetaiotaomicron; reviewed, PE1, catalytic activity PMID:23943617.
- **Reaction (RHEA:13145, EC 2.4.1.320):** 4-O-beta-D-mannopyranosyl-N-acetyl-D-glucosamine + phosphate = alpha-D-mannose 1-phosphate + N-acetyl-D-glucosamine
- **GO status:** no specific MF term (QuickGO). **Proposed new term:** *1,4-beta-mannosyl-N-acetylglucosamine phosphorylase activity*, anchored to RHEA:13145 / EC 2.4.1.320.

## Reproduce / validate

```bash
just validate-rhea-mappings   # SSSOM structural + GO term/label validation
```

## Batch 3 mappings

| RHEA | GO term | Reviewed enzyme | Organism | Evidence |
|------|---------|-----------------|----------|----------|
| RHEA:30807 | GO:0050241 pyrroline-2-carboxylate reductase activity | Ketimine reductase mu-crystallin (Q14894) | Homo sapiens | PE1, PMID:25931162 |
| RHEA:17377 | GO:0004169 dolichyl-phosphate-mannose-protein mannosyltransferase activity | Protein O-mannosyl-transferase 2 (Q9UKY4) | Homo sapiens | PE1, PMID:28512129 |
| RHEA:17901 | GO:0030753 8-hydroxyfuranocoumarin 8-O-methyltransferase activity | Esculetin O-methyltransferase (A0A4P8DY91) | Kitagawia praeruptora | PE1, PMID:30934718 |
| RHEA:18225 | GO:0019875 6-aminohexanoate-dimer hydrolase activity | 6-aminohexanoate-dimer hydrolase (P07061) | Paenarthrobacter ureafaciens | PE1, PMID:6389532 |
| RHEA:20465 | GO:0050501 hyaluronan synthase activity | Hyaluronan synthase 1 (Q92839) | Homo sapiens | PE1, Swiss-Prot curator |
| RHEA:20800 | GO:0047238 glucuronosyl-N-acetylgalactosaminyl-proteoglycan 4-beta-N-acetylgalactosaminyltransferase activity | Chondroitin sulfate synthase 3 (Q70JA7) | Homo sapiens | PE1, PMID:12907687 |
| RHEA:21924 | GO:0047559 3-dehydro-L-gulonate 2-dehydrogenase activity | 2,3-diketo-L-gulonate reductase (P37672) | Escherichia coli | PE1, Swiss-Prot curator |
| RHEA:23048 | GO:0047988 hydroxyacid-oxoacid transhydrogenase activity | Hydroxyacid-oxoacid transhydrogenase, mitochondrial (Q8IWW8) | Homo sapiens | PE1, PMID:16435184 |
| RHEA:23240 | GO:0030409 glutamate formimidoyltransferase activity | Formiminotransferase cyclodeaminase-like protein (Q9SKT4) | Arabidopsis thaliana | PE2, Swiss-Prot curator |
| RHEA:23260 | GO:0047034 15-hydroxyicosatetraenoate dehydrogenase activity | 15-hydroxyprostaglandin dehydrogenase [NAD (P15428) | Homo sapiens | PE1, PMID:8086429 |
| RHEA:23428 | GO:0050510 N-acetylgalactosaminyl-proteoglycan 3-beta-glucuronosyltransferase activity | Chondroitin sulfate synthase 3 (Q70JA7) | Homo sapiens | PE1, PMID:12907687 |
| RHEA:23956 | GO:0004653 polypeptide N-acetylgalactosaminyltransferase activity | Polypeptide N-acetylgalactosaminyltransferase 10 (Q86SR1) | Homo sapiens | PE1, PMID:12417297 |
| RHEA:24670 | GO:0004854 xanthine dehydrogenase activity | Xanthine dehydrogenase/oxidase (P47989) | Homo sapiens | PE1, PMID:8670112 |
| RHEA:24869 | GO:0017061 S-methyl-5-thioadenosine phosphorylase activity | S-methyl-5'-thioadenosine phosphorylase (Q2RXH9) | Rhodospirillum rubrum | PE1, PMID:31950558 |
| RHEA:25054 | GO:0047070 3-carboxyethylcatechol 2,3-dioxygenase activity | 2,3-dihydroxyphenylpropionate/2,3-dihydroxicinnamic acid 1,2-dioxygenase (P0ABR9) | Escherichia coli | PE1, PMID:8752345 |
| RHEA:25058 | GO:0008695 3-phenylpropionate dioxygenase activity | 3-phenylpropionate/cinnamic acid dioxygenase subunit beta (Q47140) | Escherichia coli | PE1, Swiss-Prot curator |
| RHEA:25173 | GO:0016403 dimethylargininase activity | N (O94760) | Homo sapiens | PE1, PMID:37296100 |
| RHEA:25193 | GO:0018504 cis-1,2-dihydrobenzene-1,2-diol dehydrogenase activity | Cis-toluene dihydrodiol dehydrogenase (P13859) | Pseudomonas putida | PE1, Swiss-Prot curator |
| RHEA:25269 | GO:0004603 phenylethanolamine N-methyltransferase activity | Phenylethanolamine N-methyltransferase (P11086) | Homo sapiens | PE1, PMID:8812853 |
| RHEA:26269 | GO:0016852 sirohydrochlorin cobaltochelatase activity | Sirohydrochlorin cobaltochelatase (Q05592) | Salmonella typhimurium | PE1, PMID:9150215 |
| RHEA:27846 | GO:0008688 3-(3-hydroxyphenyl)propionate hydroxylase activity | 3- (P77397) | Escherichia coli | PE1, Swiss-Prot curator |
| RHEA:28062 | GO:0043842 Kdo transferase activity | 3-deoxy-D-manno-octulosonic acid transferase (P0AC75) | Escherichia coli | PE1, PMID:1577828 |
| RHEA:28178 | GO:0102895 colneleate synthase activity | Divinyl ether synthase CYP74 (Q2WE96) | Allium sativum | PE1, PMID:9128734 |
| RHEA:28406 | GO:0103023 ITPase activity | Inosine/xanthosine triphosphatase (P39411) | Escherichia coli | PE1, PMID:16216582 |
| RHEA:28418 | GO:0008735 L-carnitine CoA-transferase activity | L-carnitine CoA-transferase (P31572) | Escherichia coli | PE1, PMID:11551212 |
| RHEA:29859 | GO:0008782 adenosylhomocysteine nucleosidase activity | 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase (P0AF12) | Escherichia coli | PE1, PMID:3911944 |
| RHEA:30367 | GO:0043755 alpha-ribazole phosphatase activity | Adenosylcobalamin/alpha-ribazole phosphatase (P52086) | Escherichia coli | PE1, Swiss-Prot curator |
| RHEA:31375 | GO:0034941 pyrrole-2-carboxylate decarboxylase activity | Pyrrole-2-carboxylic acid decarboxylase (Q9I6N5) | Pseudomonas aeruginosa | PE1, PMID:33763291 |
| RHEA:31599 | GO:0052614 uracil oxygenase activity | Pyrimidine monooxygenase RutA (P75898) | Escherichia coli | PE1, PMID:28661684 |
| RHEA:31799 | GO:0050334 thiaminase activity | Aminopyrimidine aminohydrolase (P25052) | Bacillus subtilis | PE1, PMID:17618314 |
| RHEA:32951 | GO:0050006 isomaltulose synthase activity | Isomaltulose synthase (Q8KR84) | Klebsiella variicola | PE1, PMID:12039719 |
| RHEA:33507 | GO:0008117 sphinganine-1-phosphate aldolase activity | Sphingosine-1-phosphate lyase 1 (O95470) | Homo sapiens | PE1, PMID:28165339 |
| RHEA:33955 | GO:0047254 2,4-dihydroxy-7-methoxy-2H-1,4-benzoxazin-3(4H)-one 2-D-glucosyltransferase activity | DIMBOA UDP-glucosyltransferase BX9 (B4G072) | Zea mays | PE1, PMID:16666853 |
| RHEA:33979 | GO:0102726 DIMBOA glucoside beta-D-glucosidase activity | 4-hydroxy-7-methoxy-3-oxo-3,4-dihydro-2H-1,4-benzoxazin-2-yl glucoside beta-D-glucosidase 1d, chloroplastic (D5MTF8) | Triticum aestivum | PE1, PMID:21875895 |
| RHEA:13969 | GO:0003963 RNA-3'-phosphate cyclase activity | RNA 3'-terminal phosphate cyclase (Q8U0N7) | Pyrococcus furiosus | PE1, PMID:22074260 |

### Batch 3 new GO term suggestions

**Coproheme decarboxylase** (chdC Q8Y5F1, Listeria monocytogenes serovar 1/2a; PE1, PMID:31423350). Reaction RHEA:56516 (EC 1.3.98.5): Fe-coproporphyrin III + 2 H2O2 + 2 H(+) = heme b + 2 CO2 + 4 H2O. No specific GO MF term (QuickGO); proposed *Coproheme decarboxylase activity*.

**5-methyl-1-naphthoate synthase** (aziB B4XYB8, Streptomyces sahachiroi; PE1, PMID:18635006). Reaction RHEA:42836 (EC 2.3.1.236): 5 malonyl-CoA + acetyl-CoA + 3 NADPH + 7 H(+) = 5-methyl-1-naphthoate + 5 CO2 + 3 NADP(+) + 6 CoA + 4 H2O. No specific GO MF term (QuickGO); proposed *5-methyl-1-naphthoate synthase activity*.

**UDP-Gal:alpha-D-GlcNAc-diphosphoundecaprenol beta-1,3-galactosyltransferase** (wbbD Q03084, Escherichia coli; PE1, PMID:18536883). Reaction RHEA:36747 (EC 2.4.1.303): N-acetyl-alpha-D-glucosaminyl-di-trans,octa-cis-undecaprenyl diphosphate + UDP-alpha-D-galactose = beta-D-Gal-(1->3)-alpha-D-GlcNAc-di-trans,octa-cis-undecaprenyl diphosphate + UDP + H(+). No specific GO MF term (QuickGO); proposed *UDP-Gal:alpha-D-GlcNAc-diphosphoundecaprenol beta-1,3-galactosyltransferase activity*.


## Batch 4 mappings (ranked by UniProt propagation gain)

| RHEA | GO term | Reviewed enzyme | Organism | Evidence | UniProt gain |
|------|---------|-----------------|----------|----------|-------------:|
| RHEA:48564 | GO:0102682 cytokinin riboside 5'-monophosphate phosphoribohydrolase activity | Cytokinin riboside 5'-monophosphate phosphoribohydrolase LOG8 (Q84MC2) | Arabidopsis thaliana | PE1, PMID:19837870 | 8,360 |
| RHEA:85243 | GO:0003960 quinone reductase (NADPH) activity | Zeta-crystallin (Q08257) | Homo sapiens | PE1, PMID:17497241 | 4,995 |
| RHEA:18113 | GO:0004550 nucleoside diphosphate kinase activity | Adenylate kinase 7 (Q96M32) | Homo sapiens | PE1, PMID:23416111 | 645 |
| RHEA:59468 | GO:0036374 glutathione gamma-glutamate hydrolase | Putative glutathione hydrolase 3 proenzyme (A6NGU5) | Homo sapiens | PE5, Swiss-Prot curator | 340 |
| RHEA:53428 | GO:0003908 methylated-DNA-[protein]-cysteine S-methyltransferase activity | Methylated-DNA--protein-cysteine methyltransferase (P16455) | Homo sapiens | PE1, Swiss-Prot curator | 200 |
| RHEA:63644 | GO:0046922 peptide-O-fucosyltransferase activity | GDP-fucose protein O-fucosyltransferase 3 (Q6P4F1) | Homo sapiens | PE1, PMID:39775168 | 186 |
| RHEA:44880 | GO:0004675 transmembrane receptor protein serine/threonine kinase activity | Activin receptor type-1B (P36896) | Homo sapiens | PE1, Swiss-Prot curator | 183 |
| RHEA:77639 | GO:0008441 3'(2'),5'-bisphosphate nucleotidase activity | 3' (O95861) | Homo sapiens | PE1, PMID:10675562 | 167 |
| RHEA:47844 | GO:0004789 thiamine-phosphate diphosphorylase activity | Thiamine-phosphate synthase (P39594) | Bacillus subtilis | PE1, PMID:9139923 | 151 |
| RHEA:54712 | GO:0071885 N-terminal protein N-methyltransferase activity | N-terminal Xaa-Pro-Lys N-methyltransferase 1 (Q9BV86) | Homo sapiens | PE1, PMID:26543159 | 149 |
| RHEA:34287 | GO:0004503 tyrosinase activity | Tyrosinase (P14679) | Homo sapiens | PE1, PMID:28661582 | 138 |
| RHEA:79699 | GO:0008486 diphosphoinositol-polyphosphate diphosphatase activity | Inositol diphosphatase DSP2 (Q0DX67) | Oryza sativa subsp. japonica | PE2, Swiss-Prot curator | 131 |
| RHEA:42288 | GO:0008710 8-amino-7-oxononanoate synthase activity | 8-amino-7-oxononanoate synthase (P12998) | Escherichia coli | PE1, PMID:20693992 | 86 |
| RHEA:65896 | GO:0047315 L-kynurenine:glyoxylate transaminase activity | Kynurenine--oxoglutarate transaminase 3 (Q6YP21) | Homo sapiens | PE1, Swiss-Prot curator | 80 |
| RHEA:85579 | GO:0004347 glucose-6-phosphate isomerase activity | Glucose-6-phosphate isomerase (P06744) | Homo sapiens | PE1, PMID:28803808 | 80 |
| RHEA:27738 | GO:0004731 purine-nucleoside phosphorylase activity | Purine nucleoside phosphorylase (P00491) | Homo sapiens | PE1, PMID:9305964 | 69 |
| RHEA:36231 | GO:0004623 A2-type glycerophospholipase activity | Cytosolic phospholipase A2 zeta (Q68DD2) | Homo sapiens | PE1, PMID:29158256 | 69 |
| RHEA:24768 | GO:0034256 chlorophyll(ide) b reductase activity | Probable chlorophyll (Q93ZA0) | Arabidopsis thaliana | PE1, Swiss-Prot curator | 68 |
| RHEA:37339 | GO:0003837 beta-ureidopropionase activity | Beta-ureidopropionase (Q9UBR1) | Homo sapiens | PE1, PMID:29976570 | 61 |
| RHEA:16541 | GO:0045549 9-cis-epoxycarotenoid dioxygenase activity | 9-cis-epoxycarotenoid dioxygenase NCED3, chloroplastic (Q9LRR7) | Arabidopsis thaliana | PE1, PMID:15466233 | 49 |
| RHEA:25104 | GO:0008478 pyridoxal kinase activity | Pyridoxal kinase (O00764) | Homo sapiens | PE1, PMID:9099727 | 42 |
| RHEA:52540 | GO:0016154 pyrimidine-nucleoside phosphorylase activity | Pyrimidine/purine nucleoside phosphorylase (P0C037) | Escherichia coli | PE1, PMID:27941785 | 37 |
| RHEA:50496 | GO:0004596 protein-N-terminal amino-acid acetyltransferase activity | N-alpha-acetyltransferase 10 (P41227) | Homo sapiens | PE1, PMID:25489052 | 32 |
| RHEA:51904 | GO:0004326 tetrahydrofolylpolyglutamate synthase activity | Dihydrofolate synthase/folylpolyglutamate synthase (P08192) | Escherichia coli | PE1, PMID:2985605 | 29 |
| RHEA:64648 | GO:0016621 cinnamoyl-CoA reductase activity | Cinnamoyl-CoA reductase CAD2 (G7IYC1) | Medicago truncatula | PE1, PMID:25217505 | 27 |
| RHEA:33099 | GO:0004145 diamine N-acetyltransferase activity | Diamine acetyltransferase 1 (P21673) | Homo sapiens | PE1, PMID:17516632 | 19 |
| RHEA:25112 | GO:0033883 pyridoxal phosphatase activity | Chronophin (Q96GD0) | Homo sapiens | PE1, PMID:14522954 | 18 |
| RHEA:61392 | GO:0102193 protein-ribulosamine 3-kinase activity | Fructosamine-3-kinase (Q9H479) | Homo sapiens | PE1, PMID:11522682 | 14 |
| RHEA:75931 | GO:0047972 guanidinopropionase activity | Guanidino acid hydrolase, mitochondrial (Q9BSE5) | Homo sapiens | PE1, PMID:36543883 | 13 |
| RHEA:43632 | GO:0008914 leucyl-tRNA--protein transferase activity | Leucyl/phenylalanyl-tRNA--protein transferase (P0A8P1) | Escherichia coli | PE1, Swiss-Prot curator | 12 |
| RHEA:34495 | GO:0016165 linoleate 13S-lipoxygenase activity | Lipoxygenase 7, chloroplastic (P38419) | Oryza sativa subsp. japonica | PE2, Swiss-Prot curator | 11 |
| RHEA:58284 | GO:0017113 dihydropyrimidine dehydrogenase (NADP+) activity | Dihydropyrimidine dehydrogenase [NADP (Q12882) | Homo sapiens | PE1, PMID:1512248 | 11 |
| RHEA:36179 | GO:0004142 diacylglycerol cholinephosphotransferase activity | Choline/ethanolaminephosphotransferase 1 (Q9Y6K0) | Homo sapiens | PE1, PMID:10191259 | 10 |
| RHEA:56552 | GO:0050254 rhodopsin kinase activity | Rhodopsin kinase GRK7 (Q8WTQ7) | Homo sapiens | PE1, PMID:15946941 | 10 |
| RHEA:62556 | GO:0043722 4-hydroxyphenylacetate decarboxylase activity | 4-hydroxyphenylacetate decarboxylase glycyl radical subunit (Q38HX4) | Clostridium scatologenes | PE1, PMID:16878993 | 7 |
| RHEA:59760 | GO:0047891 flavone 7-O-beta-glucosyltransferase activity | Gallate 1-beta-glucosyltransferase 84A23 (A0A193AUF6) | Punica granatum | PE1, PMID:27227328 | 6 |
| RHEA:53900 | GO:0004687 myosin light chain kinase activity | Myosin light chain kinase 3 (Q32MK0) | Homo sapiens | PE1, Swiss-Prot curator | 5 |
| RHEA:59980 | GO:0008413 8-oxo-7,8-dihydroguanosine triphosphate pyrophosphatase activity | ADP-sugar pyrophosphatase (Q9UKK9) | Homo sapiens | PE1, PMID:27257257 | 4 |
| RHEA:65152 | GO:0047243 flavanone 7-O-beta-glucosyltransferase activity | UDP-glycosyltransferase 3A2 (Q3SY77) | Homo sapiens | PE1, PMID:21088224 | 2 |
| RHEA:16457 | GO:0009027 tartrate dehydrogenase activity | Probable tartrate dehydrogenase/decarboxylase (P42958) | Bacillus subtilis | PE3, Swiss-Prot curator | 1 |
