---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACADM
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: P11310
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 22
citation_count: 24
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ACADM (human)

## Current model (mechanistic narrative)

ACADM encodes the mitochondrial flavoenzyme MCAD, which catalyzes the rate-determining first dehydrogenation step of medium-chain fatty acid β-oxidation; in MCAD-deficient cells decanoyl-CoA is readily shortened to octanoyl-CoA but octanoyl-CoA cannot be further oxidized, producing the characteristic accumulation of octanoyl-, decanoyl-, and decenoylcarnitine [PMID:7551818]. Catalysis proceeds through an FAD-dependent reductive half-reaction with octanoyl-CoA that generates kinetically distinct MCAD-FADH2–octenoyl-CoA charge-transfer complexes, and the enzyme's latent oxidase activity is suppressed while these charge-transfer species persist [PMID:7626613]; electrons are relayed to electron-transferring flavoprotein (ETF), and disease variants can alter both substrate chain-length dependence and ETF interaction [PMID:37257730]. Proper FAD incorporation is coupled to cofactor affinity, proteolytic and thermal stability, and correct tetramer assembly, with FAD supplementation able to structurally rescue some variants [PMID:37257730]. Newly imported MCAD monomers are folded along an ATP-dependent chaperone pathway in which they first bind mitochondrial hsp70 and are then transferred to hsp60 before release as mature tetramers [PMID:7905878]. The prevalent K304E (K329E) disease mutation does not impair import but introduces a charge that destabilizes the hsp60–MCAD complex against ATP-driven release and impairs subunit docking and tetramer stability; the neutral K304Q substitution restores far more activity, demonstrating that the glutamate negative charge is responsible [PMID:8104486, PMID:7905878, PMID:7730333]. Systematic variant studies separate folding/assembly defects, which are rescuable by chaperonin co-overexpression or permissive temperature, from purely catalytic lesions such as R256T that yield well-folded but inactive enzyme [PMID:16128823, PMID:24966162], and a large class of ACADM disease alleles act not on protein but on pre-mRNA splicing, disrupting exonic splicing enhancers/silencers or activating cryptic splice sites to cause exon skipping and NMD-mediated transcript loss [PMID:17273963, PMID:23810226, PMID:15171999]. Beyond classic β-oxidation, MCAD is transcriptionally repressed via the CAV1/SREBP1 axis in hepatocellular carcinoma [PMID:33975883], is phosphorylated downstream of PINK1 kinase in a pathway linking mitochondrial function to fatty acid metabolism [PMID:29563254], and re-oxidizes microbiota-derived phenylpropionic acid in a host-microbe co-metabolic pathway generating hippuric acid [PMID:36720857]. Loss of MCAD impairs hepatic glucose homeostasis under metabolic stress [PMID:18459129].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0016491 oxidoreductase activity, GO:0016740 transferase activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-392499 Metabolism of proteins
- **partners:** HSPD1, HSPA9, ETF, PINK1, SREBF1, CAV1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1991 | High | The prevalent 985A→G mutation in MCAD causes a lysine-to-glutamate substitution at position 304 (K304E, also referred to as K329E in mature protein numbering) that results in inactive enzyme due to impaired ability to form active tetramers, demonstrated by expression of mutant MCAD cDNA in E. coli producing inactive protein. | PMID:1902818, PMID:1684086, PMID:1363805 | Human genetics |
| 1992 | High | Expression of K304E mutant MCAD in eukaryotic COS-7 cells showed that mutant protein is synthesized and transported into mitochondria in similar amounts to wild-type, achieves correct mature protein size, adopts tetrameric structure, but is present at consistently lower steady-state levels than wild-type and is degraded more readily, indicating post-import instability rather than import defect. | PMID:1382617 | Biochimica et biophysica acta |
| 1993 | High | Co-overexpression of bacterial chaperonins GroEL/GroES partially rescues solubility and tetramer formation of K304E MCAD expressed in E. coli, but even soluble K304E tetramers show reduced amounts relative to wild-type, indicating the K304E mutation primarily impairs the rate of polypeptide folding and subunit assembly. Neutral substitution K304Q restores more activity than K304E, demonstrating that the negative charge of glutamate specifically impairs subunit docking. | PMID:8104486 | Biochimica et biophysica acta |
| 1993 | Medium | The R28C mutation (T157C in cDNA) in MCAD primarily affects polypeptide folding; based on the known 3D structure of MCAD, it is proposed to destroy a salt bridge between arginine-28 and glutamate-86. Expression in COS-7 cells confirmed impaired formation of enzymatically active protein. | PMID:8102510 | American journal of human genetics |
| 1994 | High | In vitro import of MCAD into isolated rat liver mitochondria demonstrated that: (1) newly imported MCAD first forms a transient complex with mitochondrial hsp70 (hsp70mit), (2) is then transferred to hsp60 (a ~700 kDa high-molecular-weight complex), and (3) subsequently released as mature tetramer in an ATP-dependent manner. K304E MCAD binds hsp70mit and transfers to hsp60 normally, but the hsp60–K304E complex is abnormally stable and resistant to ATP-driven release, indicating the folding/release step from hsp60 is impaired. | PMID:7905878 | The Journal of biological chemistry |
| 1995 | High | The R28C and K304E mutations in MCAD have distinct molecular effects: R28C predominantly affects folding (amounts of active enzyme can be modulated from undetectable to 100% of wild-type by chaperonin co-overexpression and low growth temperature), while K304E affects both folding and oligomer assembly/stability (active enzyme cannot exceed ~50% of wild-type even under optimal chaperonin conditions), and K304E assembled tetramers show decreased thermal stability. | PMID:7730333 | The Journal of biological chemistry |
| 1994 | Medium | Two-dimensional gel electrophoresis of MCAD expressed in eukaryotic cells revealed two spots for mature MCAD with different isoelectric points, demonstrating that MCAD undergoes post-translational modification in mitochondria after transit peptide removal. The pI shift is compatible with phosphorylation of one aspartic acid residue per monomer. The modified form accumulates over time relative to the unmodified form, indicating the modification is time-dependent. The K304E mutant shows a higher ratio of unmodified form, suggesting the modification efficiency or stability of the modified form is impaired by K304E. | PMID:7917465 | Biochemical medicine and metabolic biology |
| 1995 | High | The reductive half-reaction of MCAD with octanoyl-CoA as substrate generates two kinetically distinct forms of the reduced enzyme (MCAD-FADH2)–octenoyl-CoA charge-transfer complexes. Octenoyl-CoA dissociates from the more stable complex (CT2) via two pathways: a 'facile' pathway involving reversal of the reductive half-reaction (releasing octanoyl-CoA), and a 'restricted' pathway involving direct slow dissociation of octenoyl-CoA yielding MCAD-FADH2. The oxidase activity of MCAD is suppressed as long as reduced enzyme remains in charge-transfer complex form, emerging concomitantly with conversion of CT2 to the MCAD-FADH2–octenoyl-CoA Michaelis complex. | PMID:7626613 | Biochemistry |
| 2001 | Medium | The 199T→C mutation in MCAD (Y67H) is a mild folding mutation: overexpression experiments showed that it exhibits decreased levels of enzyme activity only under stringent conditions (i.e., impaired folding is partially compensated under permissive conditions), distinguishing it from the severe K304E mutation. | PMID:11349232 | American journal of human genetics |
| 2005 | High | The R256T mutation in MCAD results in a well-folded, stable protein that is completely devoid of catalytic activity, identifying R256 as critical for catalysis rather than folding. The K364R mutation by contrast causes a folding defect (protein is only active when GroELS chaperonin is co-overexpressed and shows reduced thermostability). Neither mutant shows marked FAD depletion. | PMID:16128823 | The FEBS journal |
| 2007 | High | A missense mutation in MCAD exon 5 primarily causes disease by inactivating an exonic splicing enhancer (ESE), leading to exon skipping rather than by direct protein dysfunction. The ESE functions by antagonizing a juxtaposed exonic splicing silencer (ESS) to define a suboptimal 3′ splice site. A synonymous polymorphic variant in exon 5 inactivates the ESS and renders splicing immune to the deleterious ESE mutation, demonstrating context-dependent SNP effects on pre-mRNA splicing. | PMID:17273963 | American journal of human genetics |
| 2013 | Medium | A synonymous SNP c.1161A>G in ACADM exon 11 affects pre-mRNA splicing efficiency. The c.1161A allele is associated with exon 11 missplicing; the c.1161G allele corrects this missplicing, apparently by altering the relative binding of splicing regulatory proteins SRSF1 and hnRNP A1, resulting in higher levels of full-length MCAD protein from the G allele. | PMID:23810226 | Molecular genetics and metabolism |
| 2018 | Medium | PINK1 kinase mediates phosphorylation of MCAD in vivo in Drosophila, identified by unbiased phosphoproteomic screen. Mimicking MCAD phosphorylation in a PINK1-null background rescued climbing, flight, thorax, and wing defects of PINK1 null flies, and partially corrected metabolic disruptions in acylcarnitines and amino acids, placing MCAD downstream of PINK1 in a pathway relevant to mitochondrial function and fatty acid metabolism. | PMID:29563254 | Molecular biology of the cell |
| 2021 | Medium | SREBP1 acts as a negative transcriptional regulator of ACADM in hepatocellular carcinoma. CAV1 (caveolin-1) was found to inhibit fatty acid oxidation by enhancing nuclear accumulation of SREBP1, which in turn suppresses ACADM expression and activity, promoting HCC cell aggressiveness. ACADM suppression led to elevated triglyceride, phospholipid, and lipid droplet levels and increased HCC cell motility. | PMID:33975883 | Cancer research |
| 2023 | High | MCAD (encoded by ACADM) participates in a host-microbe co-metabolic pathway for hippuric acid generation: gut bacteria reduce phenylalanine to phenylpropionic acid, and the host re-oxidizes phenylpropionic acid via MCAD (β-oxidation). This was demonstrated using MCAD-/- germ-free mice colonized with specific bacteria combined with stable isotope tracing and untargeted metabolomics, which also identified additional microbial metabolites processed by MCAD in host circulation. | PMID:36720857 | Nature communications |
| 2023 | Medium | ACADM interacts with the NSP4 protein of porcine epidemic diarrhea virus (PEDV), identified by immunoprecipitation-mass spectrometry. The interaction was confirmed by co-immunoprecipitation and laser confocal co-localization. ACADM overexpression inhibits PEDV replication while knockdown facilitates it. Mechanistically, ACADM reduces cellular free fatty acid levels and β-oxidation by hindering AMPK-mediated lipophagy, thereby suppressing PEDV replication. | PMID:39002673 | The Journal of biological chemistry |
| 2023 | High | Multiple MCAD missense variants alter FAD cofactor incorporation: half of studied variants showed FAD content <65% of wild-type. A correlation was established between FAD content and cofactor affinity, proteolytic stability, thermostability, and thermal inactivation rate. The p.Y372N variant assembles predominantly as dimers rather than tetramers. Some variants show altered substrate chain-length dependence and altered interaction with electron-transferring-flavoprotein (ETF). FAD supplementation structurally rescued some variants, suggesting mitochondrial FAD availability can modulate variant MCAD levels. | PMID:37257730 | Biochimica et biophysica acta. Molecular basis of disease |
| 2014 | High | Functional characterization of 18 ACADM missense variants by heterologous E. coli overexpression identified three variants (Y42H, E18K, R6H) with moderate impairment (22–47% residual octanoyl-CoA oxidation activity, normal temperature sensitivity, activity rescued to 100% by chaperonin co-overexpression), while 15 others showed severely reduced residual activities (<5%). Cross-linking experiments and 3D structure mapping were used to infer structural consequences. | PMID:24966162 | Journal of inherited metabolic disease |
| 2004 | Medium | A novel splice mutation IVS3-1G>C in MCAD leads to deletion of 7 bp and introduction of a premature stop codon through complete missplicing of MCAD mRNA. The misspliced mRNA is reduced in abundance due to nonsense-mediated mRNA decay (NMD), resulting in total absence of functional MCAD enzyme. This was the first functionally characterized splice mutation in the MCAD gene. | PMID:15171999 | Molecular genetics and metabolism |
| 2015 | Medium | A novel splice site mutation c.600-18G>A in ACADM activates a cryptic splice site that competes with the natural splice site, producing three transcripts, two of which result in truncated non-functional MCAD protein. Only partial missplicing occurs, leaving sufficient functional MCAD for a mild deficiency phenotype. The degree of missplicing was found to be temperature-sensitive, with octanoyl-CoA oxidation rate decreasing during febrile infection. | PMID:26223887 | BMC medical genetics |
| 2008 | High | MCAD-deficient (MCAD-/-) mice show specific alterations in hepatic carbohydrate management under metabolic stress: during lipopolysaccharide-induced acute phase response, de novo glucose-6-phosphate synthesis was significantly decreased (-20%) and newly formed G6P was preferentially directed toward glycogen, leading to decreased hepatic glucose output. During fasting alone, de novo G6P synthesis was not affected, suggesting compensatory mechanisms exist under that condition. | PMID:18459129 | Hepatology |
| 1995 | Medium | In vitro incubation of MCAD-deficient human fibroblasts with stable isotope-labeled fatty acid probes produced acylcarnitine profiles characteristic of MCAD deficiency regardless of the underlying DNA mutation: elevated octanoyl-, decanoyl-, and decenoylcarnitine with specific octanoylcarnitine-to-decanoylcarnitine ratios, indicating that MCAD-deficient cells readily convert decanoyl-CoA to octanoyl-CoA but cannot further oxidize octanoyl-CoA. | PMID:7551818 | Biochemical and molecular medicine |

## Citations

- PMID:11349232
- PMID:1363805
- PMID:1382617
- PMID:15171999
- PMID:16128823
- PMID:1684086
- PMID:17273963
- PMID:18459129
- PMID:1902818
- PMID:23810226
- PMID:24966162
- PMID:26223887
- PMID:29563254
- PMID:33975883
- PMID:36720857
- PMID:37257730
- PMID:39002673
- PMID:7551818
- PMID:7626613
- PMID:7730333
- PMID:7905878
- PMID:7917465
- PMID:8102510
- PMID:8104486
