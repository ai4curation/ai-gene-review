---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BACE2
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9Y5Z0
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 31
citation_count: 31
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for BACE2 (human)

## Current model (mechanistic narrative)

BACE2 is a membrane-anchored aspartyl protease of the A1 family that functions as a regulated ectodomain sheddase, processing a diverse set of transmembrane substrates across the secretory and endosomal pathways [PMID:16305800, PMID:10683441]. It matures by autocatalytic removal of its prodomain (cleavage between Leu62 and Ala63) within the ER/early Golgi, a step abolished by mutation of the catalytic aspartate (D110N), after which mature enzyme traffics through ER, Golgi, TGN, endosomes, and the plasma membrane in a transmembrane-domain-dependent manner [PMID:11316808, PMID:11423558]. Its crystal structure confirms the canonical aspartic-protease fold with an enlarged C-terminal domain and active-site pockets (S3, S2, S1', S2') distinct from BACE1, and the enzyme samples an ensemble of low-energy conformations [PMID:16305800, PMID:23695257]. On APP, BACE2 acts principally as an anti-amyloidogenic protease, cleaving within the Aβ domain at the theta site (Phe19-Phe20) to raise sAPP/p3-like products and suppress Aβ, while retaining conditional beta-site activity that is normally restrained by the APP juxtamembrane helix and unmasked by clusterin binding during aging [PMID:12065613, PMID:16816112, PMID:30626751]; it additionally degrades Aβ peptide directly with catalytic efficiency rivaling IDE [PMID:22986058]. This protective function is gene-dose sensitive: BACE2 trisomy suppresses Alzheimer-like pathology in Down syndrome organoids, and loss-of-function variants drive Aβ-dependent neuronal death [PMID:32647257, PMID:35110536]. Beyond the brain, BACE2 sheds Tmem27 to control pancreatic β-cell mass and glucose homeostasis, processes the melanosomal protein PMEL to enable functional amyloid fibril formation and pigmentation, cleaves the lymphangiogenic receptor VEGFR3 to limit its signaling, and acts on the insulin receptor, Kv2.1, IAPP, and glial substrates including SEZ6L/SEZ6L2 and VCAM-1 under inflammatory conditions [PMID:21907142, PMID:23754390, PMID:38888964, PMID:29804876, PMID:29703946, PMID:26840340, PMID:23430253, PMID:30456346]. Genetic ablation in mice and zebrafish yields viable animals with pigmentation and melanophore phenotypes non-redundant with BACE1 [PMID:23754390, PMID:15987683, PMID:23406323].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016787 hydrolase activity
- **localization:** GO:0005886 plasma membrane, GO:0005794 Golgi apparatus, GO:0005783 endoplasmic reticulum, GO:0005768 endosome, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-1643685 Disease
- **partners:** APP, TMEM27, PMEL, VEGFR3, KCNB1, INSR, SEZ6L, VCAM1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2000 | High | BACE2 cleaves APP at the beta-secretase site (Asp1) and more efficiently at a site within the Aβ domain (near Phe19-Phe20); the Flemish missense mutation of APP markedly increases Aβ production by BACE2 but not BACE1; mutation of a conserved active-site Asp inhibits beta-site cleavage but not cleavage within Aβ by both enzymes. | PMID:10931940 | Proceedings of the National Academy of Sciences of the United States of America |
| 2000 | Medium | BACE2 is a membrane-anchored aspartic protease with a predicted transmembrane region; in vitro translation and cell transfection showed it encodes a glycosylated protein that localizes mainly intracellularly but also to some extent at the plasma membrane. | PMID:10683441 | FEBS letters |
| 2000 | Medium | ASP1 (BACE2) expressed as an Fc fusion protein exhibits beta-secretase activity, cleaving both wild-type and Swedish-variant APP peptides at the beta-secretase site; overexpression of ASP1 in APP-expressing cells increases beta-secretase-derived soluble APP and the corresponding C-terminal fragment, but paradoxically decreases soluble Aβ secretion; ASP1 co-localizes with APP in Golgi/ER compartments. | PMID:11083922 | Molecular and cellular neurosciences |
| 2001 | High | BACE2 prodomain processing is autocatalytic: cleavage occurs between Leu62 and Ala63; BACE2 cleaved a maltose-binding protein–prodomain fusion and a synthetic peptide at this site; mutation of the catalytic Asp (D110N) abolished processing; prodomain removal occurs intramolecularly within the ER/early Golgi, and mature BACE2 is expressed on the cell surface. | PMID:11316808 | The Journal of biological chemistry |
| 2001 | High | In cells, BACE2 functions primarily as an alternative alpha-secretase, cleaving APP near the alpha-secretase site (mainly Phe19-Phe20 and Phe20-Ala21) with limited effect at the beta-site; purified BACE2 can be autoactivated in vitro; BACE2 localizes to ER, Golgi, TGN, endosomes, and plasma membrane, with localization dependent on its transmembrane domain; BACE2 chimeras that increase TGN localization do not alter APP processing patterns. | PMID:11423558 | The Journal of biological chemistry |
| 2002 | High | BACE2 cleaves APP in cells between Phe19 and Phe20 within the Aβ domain (not at the beta-secretase site), resulting in increased APPsα and p3-like products and reduced Aβ production; this cleavage occurs in the Golgi and later secretory compartments; radiosequencing of the membrane-bound C-terminal cleavage product confirmed the exact cleavage site. | PMID:12065613 | Journal of neurochemistry |
| 2003 | Medium | Stably transfected HEK293 cells overexpressing BACE2 produce the C-terminal fragment C79 (corresponding to cleavage between Phe19-Phe20), less genuine Aβ1-40/42, and higher sAPPβ and N-terminal-truncated Aβ species; BACE2 activity is enhanced by the Swedish APP mutation and is maximal at pH 4.5. | PMID:12736275 | The Journal of biological chemistry |
| 2005 | High | Crystal structure of mature BACE2 in complex with a hydroxyethylamine transition-state inhibitor determined at 3.1 Å; structure confirms BACE2 follows the general fold of A1 aspartic proteases but its C-terminal domain is larger than other family members; differences in S3, S2, S1' and S2' active-site substrate pockets compared to BACE1 were identified; mature BACE2 was produced by autocatalytic activation of pro-BACE2 refolded from E. coli inclusion bodies. | PMID:16305800 | Journal of molecular biology |
| 2006 | Medium | BACE2 cleaves APP at a novel theta (θ) site downstream of the alpha-site, abolishing Aβ production; lentiviral overexpression of BACE2 markedly reduces Aβ production in primary neurons from Swedish-mutant APP transgenic mice; BACE1, not BACE2, is responsible for the major beta-secretase activity in Down syndrome. | PMID:16816112 | FASEB journal |
| 2005 | Medium | BACE2 overexpression significantly increases sAPP levels (non-amyloidogenic) in conditioned media and markedly reduces Aβ production; knockdown of BACE2 results in increased APP C83; BACE2 processes APP within the Aβ domain at a site downstream of the alpha-secretase cleavage site, not at the beta-site; BACE2 and BACE1 have distinct transcriptional regulation (TATA-less promoter, Sp1 can regulate both but promoters share little similarity). | PMID:15857888 | FASEB journal |
| 2011 | High | Bace2 is the sheddase of the proproliferative plasma membrane protein Tmem27 in pancreatic β-cells; identified through siRNA screen; mice with functionally inactive Bace2 and insulin-resistant mice treated with a BACE2 inhibitor both display augmented β-cell mass and improved glucose homeostasis due to increased insulin levels. | PMID:21907142 | Cell metabolism |
| 2012 | High | Tmem27 dimerization (mediated by intracellular cysteine) prevents Bace2 cleavage; extracellular asparagine glycosylation is essential for Tmem27 trafficking to the plasma membrane and its processing by Bace2; the amount of Tmem27 at the plasma membrane is proportional to total cell levels upon glucose stimulation and Bace2 inhibition; the double phenylalanine motif in the Tmem27 cleavage site acts as an intramolecular Bace2 inhibitor. | PMID:22628310 | Biological chemistry |
| 2012 | High | BACE2 is a potent Aβ-degrading protease in vitro, cleaving Aβ at three peptide bonds (Phe19-Phe20, Phe20-Ala21, and Leu34-Met35, with Leu34-Met35 being the initial and principal site); BACE2 catalytic efficiency exceeds all known Aβ-degrading proteases except IDE; BACE2 overexpression in cultured cells lowers net Aβ levels comparably to IDE and greater than neprilysin or ECE1. | PMID:22986058 | Molecular neurodegeneration |
| 2013 | High | BACE2 processes PMEL (melanocyte protein) by cleaving its integral membrane form within the juxtamembrane domain, releasing the PMEL luminal domain into endosomal precursors for amyloid fibril formation and melanosome morphogenesis; Bace2-/- but not Bace1-/- mice display coat color defects; confirmed using RNA silencing, pharmacologic inhibition, and BACE2 overexpression in human melanocytic cell lines. | PMID:23754390 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | High | Systematic proteomic analysis of BACE2 substrates in pancreatic β-cells identified SEZ6L and SEZ6L2 (seizure 6 protein family members) as specific BACE2 substrates; BACE2 regulates a distinct, β-cell-enriched set of ectodomain shedding targets, non-redundant with BACE1 substrates. | PMID:23430253 | The Journal of biological chemistry |
| 2013 | Medium | BACE2 degradation is mediated by the macroautophagy-lysosome pathway (half-life ~20 h); lysosomal inhibition increased BACE2 protein levels while proteasomal inhibition had no effect; lysosomal inhibition also increased BACE2 cleavage of APP. | PMID:23773066 | The European journal of neuroscience |
| 2016 | High | Pharmacological inhibition of BACE2 (and BACE1) in mice inhibits PMEL17 proteolytic processing, leading to dose-dependent irreversible hair depigmentation; BACE2-mediated PMEL17 processing was confirmed in vitro in mouse and human melanocytes; bace2-/- mice show PMEL17 processing deficiency and hair depigmentation. | PMID:26912421 | Scientific reports |
| 2016 | Medium | BACE2 cleaves human IAPP (islet amyloid polypeptide) at two distinct sites in the mature IAPP sequence; BACE2-mediated proteolysis modulates human IAPP fibrillation and leads to IAPP protein degradation. | PMID:26840340 | PloS one |
| 2018 | Medium | BACE2 is expressed in discrete subsets of neurons and glia in the adult mouse brain; four new BACE2 substrates in cultured glia were identified: VCAM-1, DNER, FGFR1, and plexin domain containing 2; TNF induced a drastic increase in BACE2-mediated shedding of VCAM-1 in CSF under proinflammatory conditions. | PMID:30456346 | Life science alliance |
| 2018 | Medium | BACE2 cleaves the potassium channel Kv2.1 at Thr376, Ala717, and Ser769, disrupting Kv2.1 clustering on the cell membrane, resulting in decreased delayed rectifier K+ current and a hyperpolarizing shift; cleaved Kv2.1 forms reduce the delayed rectifier surge and reduce neuronal apoptosis. | PMID:29703946 | Molecular psychiatry |
| 2018 | High | In zebrafish, Bace2 cleaves the insulin receptor as a sheddase in melanophores; loss of bace2 (wanderlust mutant) causes hyperdendritic, hyperproliferative melanophores with aberrant localization due to hyperactive insulin/PI3K/mTOR signaling; inhibition of insulin/PI3Kγ/mTOR signaling rescues the wanderlust phenotype. | PMID:29804876 | Developmental cell |
| 2019 | Medium | BACE2 also processes APP at the beta-site; the juxtamembrane helix (JH) of APP normally inhibits BACE2 beta-secretase activity; JH-disrupting mutations and clusterin binding to JH trigger BACE2-mediated beta-cleavage of APP; both BACE2 and clusterin are elevated in aged mouse brains, enhancing beta-cleavage during aging. | PMID:30626751 | JCI insight |
| 2010 | Medium | In pancreatic β-cells, BACE2 co-localizes with clathrin-coated vesicles at the plasma membrane; pharmacological inhibition or silencing of BACE2 increases BACE2 content in clathrin-coated vesicles, reduces insulin internalization rate, decreases insulin receptor β-subunit at the plasma membrane (increased in Golgi), and reduces insulin gene expression, indicating a role for BACE2 in insulin receptor trafficking. | PMID:20943756 | American journal of physiology. Endocrinology and metabolism |
| 2020 | High | BACE2 trisomy in Down syndrome is a gene dose-sensitive AD suppressor; CRISPR/Cas9 elimination of the third copy of BACE2 in trisomy 21 cerebral organoids triggered AD-like pathology (Aβ deposits, tau pathology, neuronal loss); T21 organoids secrete increased Aβ-preventing (Aβ1-19) and Aβ-degradation products (Aβ1-20, Aβ1-34); this protective mechanism is cross-inhibited by BACE1 inhibitors. | PMID:32647257 | Molecular psychiatry |
| 2024 | High | BACE2 is the protease responsible for shedding of the lymphangiogenic receptor VEGFR3 from lymphatic endothelial cells; BACE2 (not BACE1) inactivation inhibited VEGFR3 shedding from primary human lymphatic endothelial cells, reduced soluble VEGFR3 in blood of mice, non-human primates, and humans, and increased full-length VEGFR3 and VEGFR3 signaling; in zebrafish, BACE2 inactivation enhanced LEC migration; soluble VEGFR3 can serve as pharmacodynamic plasma marker for BACE2 activity. | PMID:38888964 | The Journal of clinical investigation |
| 2013 | High | Multiple high-resolution crystal structures of BACE2 in six different packing environments were obtained using surface mutagenesis and co-crystallization with Fab fragments, Fynomers, and Xaperones; these structures define an ensemble of low-energy conformations accessible to the enzyme. | PMID:23695257 | Acta crystallographica. Section D, Biological crystallography |
| 2010 | Medium | In rat astrocytes, beta-secretase activity and Aβ production are due to BACE2 (not BACE1), whose expression is blocked at the translational level in astrocytes; neuroinflammatory changes can both positively and negatively modulate BACE2-dependent beta-secretase activity in astrocytes. | PMID:21073551 | The European journal of neuroscience |
| 2021 | Medium | BACE2 overexpression in ocular melanoma cells inhibits tumor progression in vitro and in vivo; BACE2 regulates TMEM38B expression, and the BACE2/TMEM38B axis modulates calcium release from the endoplasmic reticulum; increased N6-methyladenosine (m6A) RNA methylation leads to upregulation of BACE2 mRNA in ocular melanoma. | PMID:33601055 | Molecular therapy |
| 2022 | Medium | BACE2 loss-of-function mutation (BACE2G446R) in human pluripotent stem cell-derived brain organoids causes increased apoptosis and elevated Aβ oligomers resembling AD phenotypes; these phenotypes are rescued by APP removal; BACE2WT overexpression in organoids carrying APP Swedish/Indiana mutations attenuates Aβ accumulation and neuronal cell death. | PMID:35110536 | Cell death discovery |
| 2005 | High | BACE2 knockout mice display an overall healthy phenotype; combined BACE1/BACE2 deficiency enhances BACE1-/- lethality; BACE2 contributes to Aβ generation in glia (which lack BACE1 activity), not in neurons. | PMID:15987683 | The Journal of biological chemistry |
| 2013 | High | In zebrafish, loss of Bace2 results in a specific melanocyte migration and morphology phenotype not observed in Bace1-/- fish; double homozygous bace1-/-; bace2-/- fish do not enhance single mutant phenotypes, indicating non-redundant, distinct physiological functions for Bace1 and Bace2. | PMID:23406323 | Journal of neurochemistry |

## Citations

- PMID:10683441
- PMID:10931940
- PMID:11083922
- PMID:11316808
- PMID:11423558
- PMID:12065613
- PMID:12736275
- PMID:15857888
- PMID:15987683
- PMID:16305800
- PMID:16816112
- PMID:20943756
- PMID:21073551
- PMID:21907142
- PMID:22628310
- PMID:22986058
- PMID:23406323
- PMID:23430253
- PMID:23695257
- PMID:23754390
- PMID:23773066
- PMID:26840340
- PMID:26912421
- PMID:29703946
- PMID:29804876
- PMID:30456346
- PMID:30626751
- PMID:32647257
- PMID:33601055
- PMID:35110536
- PMID:38888964
