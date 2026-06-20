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
