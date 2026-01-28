---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T17:32:15.610592'
end_time: '2026-01-22T17:51:12.540221'
duration_seconds: 1136.93
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: HRC
  gene_symbol: HRC
  uniprot_accession: P23327
  protein_description: 'RecName: Full=Sarcoplasmic reticulum histidine-rich calcium-binding
    protein; Flags: Precursor;'
  gene_info: Name=HRC; Synonyms=HCP;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the HRC family. .
  protein_domains: Hist_rich_Ca-bd. (IPR019552); HRC. (IPR015666); Hist_rich_Ca-bd
    (PF10529)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P23327
- **Protein Description:** RecName: Full=Sarcoplasmic reticulum histidine-rich calcium-binding protein; Flags: Precursor;
- **Gene Information:** Name=HRC; Synonyms=HCP;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the HRC family. .
- **Key Domains:** Hist_rich_Ca-bd. (IPR019552); HRC. (IPR015666); Hist_rich_Ca-bd (PF10529)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HRC" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HRC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HRC** (gene ID: HRC, UniProt: P23327) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Histidine-Rich Calcium-Binding Protein (HRC): A Comprehensive Research Report

## 1. Introduction and Overview

Histidine-rich calcium-binding protein (HRC, also known as histidine-rich Ca2+-binding protein or HCP) is a 165-170 kDa luminal sarcoplasmic reticulum (SR) protein that functions as a critical regulator of intracellular calcium homeostasis in striated muscle. First characterized by Hofmann and colleagues in 1989 at the University of Texas Southwestern Medical Center, HRC was identified based on its ability to bind calcium ions with high capacity but low affinity, a property that distinguishes it from other calcium-binding proteins in the SR [hofmann-1989-cloning-abstract]. The human HRC gene (UniProt P23327) is located on chromosome 19q13.3 and encodes a protein that is predominantly expressed in cardiac and skeletal muscle, with additional expression in arterial smooth muscle cells.

The primary function of HRC is to regulate sarcoplasmic reticulum calcium cycling through dual interactions with two major SR protein complexes: the calcium uptake machinery (SERCA2a pump) and the calcium release apparatus (ryanodine receptor/triadin complex). This dual role positions HRC as a molecular integrator of excitation-contraction coupling in the heart, where precise calcium handling is essential for normal rhythmic contraction [arvanitis-2011-review-abstract]. A recent comprehensive review by Mackrill in 2024 further characterized HRC as "a molecular integrator of cardiac excitation-contraction coupling," highlighting its central position in cardiac calcium homeostasis [mackrill-2024-jeb-abstract]. Over the past three decades, research has established HRC as not only a calcium storage protein but also an active participant in the regulation of SR calcium flux, with significant implications for cardiac physiology and pathophysiology.

HRC belongs to a family of acidic calcium-binding proteins that also includes aspolin, an aspartic acid-rich paralogue found primarily in fish. Interestingly, while ray-finned fish genomes contain both aspolin and HRC genes, other vertebrates including mammals possess only the HRC gene, suggesting gene loss during vertebrate evolution [mackrill-2024-jeb-abstract]. Aspolin functions as a trimethylamine N-oxide (TMAO) demethylase, and whether HRC retains any enzymatic activity toward TMAO remains an intriguing open question for cardiac research.

## 2. Structural Organization and Biochemical Properties

The molecular architecture of HRC reveals a highly specialized protein designed for calcium binding and protein-protein interactions. The mature human HRC protein, following cleavage of a 27-residue N-terminal signal sequence, contains several distinct structural domains that confer its functional properties [hofmann-1989-cloning-abstract].

The most striking structural feature of HRC is its central region containing ten histidine-rich acidic tandem repeats located between amino acids 106-365. These repeats are organized into two types: Type A motifs (repeated four times) and Type B motifs (repeated six times). Each repeat consists of a histidine-rich sequence (HRHRGH), a stretch of 10-11 acidic amino acids (primarily glutamic and aspartic acid), and a sequence containing serines and threonines [arvanitis-2011-review-abstract]. The unusual amino acid composition—approximately 13% histidine, 12% aspartic acid, and 19% glutamic acid—creates an extensively acidic protein surface that is responsible for calcium binding.

HRC binds calcium with high capacity (approximately 200 nmoles Ca2+/mg protein) but low affinity (Kd = 1.9 mM), as characterized by Picello and colleagues [arvanitis-2011-review-abstract]. This low-affinity, high-capacity binding profile distinguishes HRC from high-affinity calcium sensors like calmodulin and instead places it in a functional category shared with calsequestrin, the major calcium storage protein of the SR. The calcium binding occurs through electrostatic interactions with pairs or triplets of acidic amino acids forming calcium-binding surfaces. These surfaces within the ten histidine-rich acidic tandem repeats may be closely packed in the presence of calcium, suggesting a calcium-dependent conformational change.

The C-terminal region of HRC contains a cluster of 14 closely spaced cysteine residues that forms a cysteine-rich domain critical for protein-protein interactions [hofmann-1989-cloning-abstract]. This domain appears to be under strong negative selection pressure during mammalian evolution, indicating functional constraint, while the remainder of the protein shows evidence of positive selection or relaxed negative selection. Additionally, HRC contains a 13-residue stretch of polyglutamic acid between the histidine-rich repeats and the cysteine-rich domain.

HRC also binds zinc ions at sites distinct from calcium-binding sites, a property not shared by calsequestrin, suggesting additional metal-binding functions that remain to be fully characterized [arvanitis-2011-review-abstract].

Kim and colleagues provided direct evidence for HRC's role as a calcium storage protein by demonstrating that acute HRC overexpression in rat neonatal cardiomyocytes significantly increased both caffeine-induced and depolarization-induced calcium release from the SR [kim-2003-storage-abstract]. Importantly, the elevated calcium content persisted even during SERCA inhibition with cyclopiazonic acid, while ryanodine receptor expression remained unchanged. This demonstrates that HRC directly contributes to the releasable calcium pool within the SR storage compartment.

## 3. Cellular Localization and Tissue Distribution

HRC resides exclusively within the lumen of the sarcoplasmic reticulum, where it exists as a multimer associated with the junctional SR membrane through calcium bridges. This localization places HRC at the critical junction where calcium is both released (via ryanodine receptors) and resequestered (via SERCA pumps), enabling its dual regulatory function [hofmann-1989-cloning-abstract].

Tissue distribution studies reveal that HRC expression is highly enriched in striated muscle, with the highest levels found in cardiac tissue (left ventricle shows 24.9-fold overexpression relative to average tissue expression) and skeletal muscle (10.9-fold enrichment) [arvanitis-2011-review-abstract]. Cardiac atrial tissue also shows significant HRC expression (12.0-fold enrichment). Beyond striated muscle, HRC is abundant in arterial smooth muscle cells lining small arteries and arterioles, where it localizes to calciosomes, the smooth muscle equivalent of the SR.

The tissue-specific expression of HRC is controlled by the myocyte enhancer factor 2 (MEF2) family of transcription factors. Anderson and colleagues identified a transcriptional enhancer within the HRC gene containing a highly conserved MEF2-binding site that is necessary and sufficient for directing expression during embryonic development in cardiac, skeletal, and vascular smooth muscle cells [anderson-2004-mef2-abstract]. This MEF2-dependent regulation is notable because it occurs independently of CArG motifs (serum response factor binding sites), making HRC the first identified MEF2-dependent, CArG-independent transcriptional target in smooth muscle.

The human HRC gene was cloned and characterized by Hofmann and colleagues, who mapped it to chromosome 19q13.3, near the myotonic dystrophy locus, while the mouse ortholog resides on chromosome 7 [hofmann-1991-genomic-abstract]. The gene contains six exons, with approximately 90% of the coding region located in the first exon. Variable acidic amino acid stretches in exon 1 establish useful polymorphisms that have been employed in linkage studies.

HRC expression is developmentally regulated and plays a role in myocyte differentiation. The protein is not detectable in undifferentiated, proliferating myoblast cultures, but accumulates rapidly when differentiation is induced [arvanitis-2011-review-abstract]. Interestingly, SOX15, a transcription factor that antagonizes muscle differentiation, acts as a suppressor of the HRC locus. SOX15 ablation in mouse embryonic stem cells results in selective overexpression of HRC mRNA, and SOX15-null mice exhibit delayed skeletal muscle regeneration after injury. The significance of HRC repression by SOX15 in the early stages of myocyte differentiation, especially during myofiber trauma repair, remains an active area of investigation.

## 4. Molecular Interactions and Functional Mechanisms

### 4.1 HRC-SERCA2a Interaction

A crucial discovery in understanding HRC function came from the demonstration that HRC directly interacts with SERCA2a (sarco/endoplasmic reticulum Ca2+-ATPase 2a), the primary calcium pump responsible for SR calcium reuptake in cardiac muscle [arvanitis-2007-serca-abstract]. This interaction is calcium-dependent, with maximal binding occurring at low calcium concentrations and diminishing as calcium levels rise.

The protein domains mediating this interaction have been mapped to the amino-terminal fragment of SERCA2 that projects into the SR lumen (amino acid residues 74-90) and the second histidine- and glutamic acid-rich domain of HRC (amino acids 320-460) [arvanitis-2011-review-abstract]. Functionally, HRC binding to SERCA2 at low intraluminal calcium concentrations inhibits pump activity, thereby reducing calcium uptake. This inhibitory effect has been demonstrated in transgenic mouse models where HRC overexpression resulted in 35% reduction in SR calcium uptake rates [gregory-2006-cardiac-function-abstract].

### 4.2 HRC-Triadin Interaction

The second major protein interaction of HRC involves triadin, an integral membrane protein of the SR that forms part of the calcium release complex along with the ryanodine receptor (RyR2), junctin, and calsequestrin [lee-2001-triadin-abstract]. Lee and colleagues demonstrated using co-immunoprecipitation experiments that HRC binds directly to triadin, identifying the histidine-rich acidic repeats of HRC as responsible for this binding.

The HRC-binding domain of triadin was localized to the luminal region containing the KEKE motif, the same region involved in triadin's interaction with calsequestrin. This finding is significant because it suggests that HRC and calsequestrin may compete for binding to triadin, providing a mechanism for reciprocal regulation of calcium release.

Critically, the HRC-triadin interaction is calcium-sensitive but with opposite characteristics to the HRC-SERCA interaction: HRC-triadin binding increases with rising calcium concentrations [arvanitis-2011-review-abstract]. This calcium-dependent switching of interaction partners positions HRC as an intra-SR calcium sensor that responds dynamically to changes in luminal calcium during the cardiac cycle.

### 4.3 HRC in Excitation-Contraction Coupling

During mammalian cardiomyocyte excitation-contraction coupling, calcium influx through voltage-gated L-type calcium channels (dihydropyridine receptors) triggers calcium release from the SR through ryanodine receptor channels, a process termed calcium-induced calcium release (CICR) [mackrill-2024-jeb-abstract]. This released calcium then binds to troponin C, enabling actin-myosin interaction and muscle contraction. For relaxation to occur, calcium must be resequestered into the SR primarily via SERCA2a, with the sodium-calcium exchanger (NCX) providing an additional extrusion pathway.

HRC plays a critical role in this cycle by acting as an intra-SR calcium sensor. Its ability to switch interaction partners based on luminal calcium concentration allows it to fine-tune both the uptake and release phases of the calcium cycle. By inhibiting SERCA at low SR calcium (immediately after release) and modulating the RyR2 complex through triadin at high SR calcium (during the filled state), HRC helps maintain the appropriate timing and magnitude of calcium transients essential for rhythmic cardiac contraction.

### 4.4 Functional Model of HRC Action

Based on these interactions, a comprehensive model of HRC function has emerged [arvanitis-2011-review-abstract]. At low SR calcium load (during diastole after calcium release), HRC preferentially interacts with SERCA2 and inhibits its activity, potentially preventing excessive calcium uptake. As SR calcium rises following SERCA-mediated reuptake, HRC dissociates from SERCA2 and exhibits enhanced binding to triadin, where it modulates SR calcium release through the ryanodine receptor complex.

Studies using CASQ2/HRC double knockout mice provided functional evidence supporting opposing roles of HRC and calsequestrin in ryanodine receptor regulation [liu-2015-casq2-dko-abstract]. The investigators proposed that whereas calsequestrin (CASQ2) inhibits and stabilizes RyR2 during diastole, HRC stimulates (primes for activation) RyR2 through triadin binding, facilitating RyR2 recovery from refractoriness. These proteins appear to compete for overlapping binding sites on triadin in a calcium-dependent manner during each calcium release-uptake cycle.

## 5. Physiological Roles and In Vivo Studies

### 5.1 HRC Overexpression Studies

Transgenic mouse models with cardiac-specific HRC overexpression have been instrumental in defining HRC's physiological roles. Gregory and colleagues generated mice with approximately 3-fold elevation of cardiac HRC and observed several key phenotypes [gregory-2006-cardiac-function-abstract]:

The overexpressing hearts showed impaired SR calcium uptake (reduced by 35%) and attenuated calcium transient decay (by nearly 40%), consistent with HRC's inhibitory effect on SERCA2. As compensatory mechanisms, the sodium-calcium exchanger (NCX) and triadin protein levels were markedly increased. Importantly, the impaired calcium handling triggered progressive cardiac remodeling and hypertrophy, with animals developing congestive heart failure by 18 months of age. These findings demonstrated that while HRC normally functions to fine-tune calcium handling, excessive HRC activity leads to cardiac dysfunction.

### 5.2 HRC Knockout Studies

Complementary information came from HRC knockout mouse studies. Park and colleagues reported that under baseline conditions, HRC-deficient mice were morphologically normal and actually displayed enhanced contractility, calcium transients, and maximal SR calcium uptake rates [park-2013-hrc-knockout-abstract]. However, when challenged with stress conditions (isoproterenol stimulation or high-frequency pacing), HRC-knockout cardiomyocytes were five-fold more prone to after-contractions.

Most dramatically, under pressure-overload stress (transverse aortic constriction), HRC-knockout mice developed severe cardiac hypertrophy, fibrosis, pulmonary edema, and premature death compared to wild-type controls. These findings indicate that while HRC may normally constrain calcium cycling, it becomes essential for maintaining cardiac integrity under pathological stress conditions.

### 5.3 HRC and Calsequestrin Double Knockout

The double knockout of both HRC and calsequestrin (CASQ2) provided remarkable insights into their functional interplay [liu-2015-casq2-dko-abstract]. Surprisingly, double knockout mice showed relatively mild phenotypes with preserved cardiac function, in stark contrast to the severe arrhythmia burden of CASQ2-null mice alone. The combined deletion ameliorated ventricular arrhythmia susceptibility and reduced arrhythmogenic calcium waves. At the cellular level, double knockout myocytes showed decreased frequency of spontaneous calcium sparks in the presence of isoproterenol.

These findings suggest that removing both proteins effectively cancels out their opposing effects on RyR2 regulation. However, the double knockouts exhibited impaired force-frequency relationships at elevated pacing rates, indicating that both proteins are necessary for robust contractile performance during physiological stress.

## 6. Clinical Significance and Disease Associations

### 6.1 The Ser96Ala Polymorphism and Ventricular Arrhythmias

The most significant clinical association of HRC involves the Ser96Ala genetic variant (rs3745297) and its link to life-threatening ventricular arrhythmias in patients with dilated cardiomyopathy [arvanitis-2008-ser96ala-abstract]. Arvanitis and colleagues screened 123 idiopathic dilated cardiomyopathy patients and identified that while the Ser96Ala polymorphism showed similar frequency between patients and controls (indicating it does not cause cardiomyopathy), it exhibited striking association with arrhythmic outcomes.

During follow-up of 4.02 years, homozygous Ala/Ala patients demonstrated dramatically elevated arrhythmia risk compared to Ser/Ser patients (hazard ratio 9.620; P = 0.003). The Ser96Ala variant emerged as the only significant genetic predictor of arrhythmogenesis on multivariable analysis (hazard ratio 4.191; P = 0.018), independent of age, sex, left ventricular ejection fraction, atrial fibrillation, or medication.

Mechanistically, bioinformatic analysis revealed that Ser96 represents a phosphorylation site for casein kinase II [arvanitis-2011-review-abstract]. The serine-to-alanine substitution eliminates this phosphorylation capability, potentially disrupting HRC's regulatory effects on both SERCA2 and ryanodine receptor function. Subsequent studies demonstrated that acute overexpression of the HRC Ser96Ala variant significantly increased binding of HRC to SERCA2, enhanced inhibition of SERCA2 activity, reduced maximal SR calcium uptake rate, and increased the frequency of spontaneous calcium sparks indicative of enhanced RyR2 activity [arvanitis-2018-rhythmicity-abstract].

Approximately 60% of the general population carries at least one Ser96Ala copy, yet only those with underlying dilated cardiomyopathy demonstrate arrhythmia susceptibility, indicating conditional penetrance dependent on the diseased cardiac substrate.

### 6.2 HRC Expression in Heart Failure

HRC expression levels are reduced in both animal models and human heart failure [arvanitis-2011-review-abstract]. Given HRC's role in increasing SR calcium load that is unavailable for release, it has been proposed that HRC downregulation in heart failure may represent a compensatory mechanism to increase the amount of calcium released from the SR, in an attempt to enhance calcium cycling and maintain cardiac function.

### 6.3 Cardioprotection Against Ischemia/Reperfusion Injury

Paradoxically, despite its association with cardiac dysfunction when overexpressed, HRC appears to confer cardioprotection against ischemia/reperfusion injury [zhou-2007-ischemia-abstract]. Zhou and colleagues demonstrated that transgenic HRC-overexpressing hearts, despite having depressed baseline function, showed significantly improved recovery of left ventricular developed pressure after ischemia (86.6% vs. 58.3% in wild-types) and smaller infarct sizes (56% reduction in the in vivo model).

The cardioprotective mechanism involves antiapoptotic effects. HRC overexpression significantly increased the Bcl-2/Bax ratio following reperfusion and markedly decreased active caspase-3, caspase-9, and caspase-12. The investigators hypothesized that decreased free SR calcium due to HRC overexpression leads to reduced intramitochondrial calcium accumulation, thereby preserving mitochondrial integrity and preventing activation of mitochondrial-mediated apoptotic pathways.

### 6.4 Therapeutic Implications

The Ser96Ala variant has emerged as a potential biomarker for risk stratification of sudden cardiac death in dilated cardiomyopathy patients [arvanitis-2018-rhythmicity-abstract]. Furthermore, the observation that CaMKII inhibition (with KN-93) reduced malignant arrhythmia occurrence in mouse models carrying the HRC Ser96Ala variant suggests potential therapeutic approaches targeting the underlying arrhythmogenic pathway in affected patients.

## 7. Phosphorylation and Post-Translational Regulation

HRC undergoes phosphorylation at multiple serine residues (Ser119, Ser157/159, Ser170/171, Ser431, Ser563, Ser567), primarily by casein kinase II in the SR lumen [arvanitis-2011-review-abstract]. Phosphorylation of HRC has been shown to affect the ryanodine affinity of the ryanodine receptor, suggesting that post-translational modification provides another layer of HRC functional regulation.

The functional importance of phosphorylation is underscored by the clinical significance of the Ser96Ala variant, which eliminates a casein kinase II phosphorylation site and is associated with life-threatening arrhythmias. The precise mechanisms by which HRC phosphorylation state modulates its interactions with SERCA2 and triadin remain active areas of investigation.

## 8. Open Questions and Future Directions

Despite significant advances in understanding HRC biology, several important questions remain:

1. **Structural basis of function**: The three-dimensional structure of HRC under varying calcium concentrations and phosphorylation states has not been determined. Such structural information would provide crucial insights into how HRC undergoes conformational changes that alter its protein interaction partners.

2. **In vivo dynamics**: While in vitro studies have characterized the calcium-dependence of HRC-SERCA and HRC-triadin interactions, the real-time dynamics of these interactions during the cardiac cycle in vivo remain to be directly visualized.

3. **Mechanism of Ser96Ala pathogenicity**: The precise molecular mechanism by which the Ser96Ala variant increases arrhythmia susceptibility specifically in the setting of dilated cardiomyopathy requires further elucidation. Understanding this conditional penetrance could reveal therapeutic targets.

4. **HRC in non-cardiac tissues**: The function of HRC in arterial smooth muscle and its potential roles in vascular disease remain largely unexplored.

5. **Therapeutic targeting**: Whether HRC or its interactions can be pharmacologically targeted for cardiac protection or arrhythmia prevention represents an important translational question.

6. **HRC phosphorylation cascade**: The complete regulatory network governing HRC phosphorylation and its functional consequences needs systematic characterization.

7. **Evolutionary significance**: Recent evidence suggests HRC is evolving more rapidly than other cardiac excitation-contraction coupling proteins, with positive selection (or relaxed negative selection) occurring along most of the protein sequence except the highly conserved C-terminal cysteine-rich region [mackrill-2024-jeb-abstract]. The histidine-rich region may be involved in pH sensing as an adaptation to air-breathing and endothermic life. The physiological significance of this adaptation warrants further investigation.

8. **TMAO demethylase activity**: Given that aspolin, the fish paralogue of HRC, functions as a trimethylamine N-oxide demethylase, whether HRC retains any enzymatic activity toward TMAO remains an intriguing question with potential implications for understanding cardiac metabolism [mackrill-2024-jeb-abstract].

9. **Role in muscle regeneration**: The significance of SOX15-mediated HRC repression in early myocyte differentiation and skeletal muscle regeneration following injury requires further investigation.

## References

1. **[hofmann-1989-cloning-abstract]** Hofmann SL, Goldstein JL, Orth K, Moomaw CR, Slaughter CA, Brown MS. Molecular cloning of a histidine-rich Ca2+-binding protein of sarcoplasmic reticulum that contains highly conserved repeated elements. J Biol Chem. 1989;264(30):18083-90. PMID: 2808365

2. **[arvanitis-2011-review-abstract]** Arvanitis DA, Vafiadaki E, Sanoudou D, Kranias EG. Histidine-rich calcium binding protein: the new regulator of sarcoplasmic reticulum calcium cycling. J Mol Cell Cardiol. 2011;50(1):43-9. PMID: 20807542. DOI: 10.1016/j.yjmcc.2010.08.021. PMC: PMC3018531

3. **[lee-2001-triadin-abstract]** Lee HG, Kang H, Kim DH, Park WJ. Interaction of HRC (histidine-rich Ca2+-binding protein) and triadin in the lumen of sarcoplasmic reticulum. J Biol Chem. 2001;276(43):39533-8. PMID: 11504710. DOI: 10.1074/jbc.M010664200

4. **[arvanitis-2007-serca-abstract]** Arvanitis DA, Vafiadaki E, Fan GC, Mitton BA, Gregory KN, Del Monte F, Kontrogianni-Konstantopoulos A, Sanoudou D, Kranias EG. Histidine-rich Ca-binding protein interacts with sarcoplasmic reticulum Ca-ATPase. Am J Physiol Heart Circ Physiol. 2007;293:H1581-H1589

5. **[arvanitis-2008-ser96ala-abstract]** Arvanitis DA, Sanoudou D, Kolokathis F, Vafiadaki E, Papalouka V, Kontrogianni-Konstantopoulos A, Theodorakis GN, Paraskevaidis IA, Adamopoulos S, Dorn GW, Kremastinos DT, Kranias EG. The Ser96Ala variant in histidine-rich calcium-binding protein is associated with life-threatening ventricular arrhythmias in idiopathic dilated cardiomyopathy. Eur Heart J. 2008;29:2514-2525. PMID: 18617481. DOI: 10.1093/eurheartj/ehn328. PMC: PMC2567024

6. **[gregory-2006-cardiac-function-abstract]** Gregory KN, Ginsburg KS, Bodi I, Hahn H, Marreez YM, Song Q, Padmanabhan PA, Mitton BA, Waggoner JR, Del Monte F, Park WJ, Dorn GW 2nd, Bers DM, Kranias EG. Histidine-rich Ca binding protein: a regulator of sarcoplasmic reticulum calcium sequestration and cardiac function. J Mol Cell Cardiol. 2006;40(5):653-65. PMID: 16600288. DOI: 10.1016/j.yjmcc.2006.02.003

7. **[liu-2015-casq2-dko-abstract]** Liu B, Györke S, et al. Ablation of HRC alleviates cardiac arrhythmia and improves abnormal Ca handling in CASQ2 knockout mice prone to CPVT. Cardiovasc Res. 2015;108(2):299-311. PMID: 26410369. DOI: 10.1093/cvr/cvv222. PMC: PMC4614688

8. **[park-2013-hrc-knockout-abstract]** Park CS, Chen S, Lee H, Cha H, Oh JG, Hong S, Han P, Ginsburg KS, Jin S, Park I, Singh VP, Wang HS, Bhel DM, Franzini-Armstrong C, Park WJ, Bers DM, Kranias EG, Cho C, Kim DH. Targeted ablation of the histidine-rich Ca2+-binding protein (HRC) gene is associated with abnormal SR Ca2+-cycling and severe pathology under pressure-overload stress. Basic Res Cardiol. 2013;108(3):344. PMID: 23553082. DOI: 10.1007/s00395-013-0344-2

9. **[zhou-2007-ischemia-abstract]** Zhou X, Fan GC, Ren X, Waggoner JR, Gregory KN, Chen G, Jones WK, Kranias EG. Overexpression of histidine-rich Ca-binding protein protects against ischemia/reperfusion-induced cardiac injury. Cardiovasc Res. 2007;75(3):487-97. PMID: 17499229. DOI: 10.1016/j.cardiores.2007.04.005

10. **[anderson-2004-mef2-abstract]** Anderson JP, Dodou E, Heidt AB, De Val SJ, Jaehnig EJ, Greene SB, Olson EN, Black BL. HRC is a direct transcriptional target of MEF2 during cardiac, skeletal, and arterial smooth muscle development in vivo. Mol Cell Biol. 2004;24(9):3757-68. PMID: 15082771. PMC: PMC387749

11. **[arvanitis-2018-rhythmicity-abstract]** Arvanitis DA, Vafiadaki E, Johnson DM, Kranias EG, Sanoudou D. The Histidine-Rich Calcium Binding Protein in Regulation of Cardiac Rhythmicity. Front Physiol. 2018;9:1379. PMID: 30319456. DOI: 10.3389/fphys.2018.01379. PMC: PMC6171002

12. **[mackrill-2024-jeb-abstract]** Mackrill JJ. Histidine-rich calcium-binding protein: a molecular integrator of cardiac excitation-contraction coupling. J Exp Biol. 2024;227(20):jeb247640. DOI: 10.1242/jeb.247640

13. **[hofmann-1991-genomic-abstract]** Hofmann SL, Topham M, Hsieh CL, Francke U. cDNA and genomic cloning of HRC, a human sarcoplasmic reticulum protein, and localization of the gene to human chromosome 19 and mouse chromosome 7. Genomics. 1991;9(4):656-69. PMID: 2037293

14. **[kim-2003-storage-abstract]** Kim E, Shin DW, Hong CS, Jeong D, Kim DH, Park WJ. Increased Ca2+ storage capacity in the sarcoplasmic reticulum by overexpression of HRC (histidine-rich Ca2+ binding protein). Biochem Biophys Res Commun. 2003. PMID: 12480542


## Citations

1. anderson-2004-mef2-abstract.md
2. arvanitis-2007-serca-abstract.md
3. arvanitis-2008-ser96ala-abstract.md
4. arvanitis-2011-review-abstract.md
5. arvanitis-2018-rhythmicity-abstract.md
6. gregory-2006-cardiac-function-abstract.md
7. hofmann-1989-cloning-abstract.md
8. hofmann-1991-genomic-abstract.md
9. kim-2003-storage-abstract.md
10. lee-2001-triadin-abstract.md
11. liu-2015-casq2-dko-abstract.md
12. mackrill-2024-jeb-abstract.md
13. park-2013-hrc-knockout-abstract.md
14. zhou-2007-ischemia-abstract.md