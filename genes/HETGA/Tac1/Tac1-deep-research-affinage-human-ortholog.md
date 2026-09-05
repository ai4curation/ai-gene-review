---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/TAC1
affinage_run_date: 2026-06-10T10:51:54
uniprot_accession: P20366
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 35
citation_count: 36
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for TAC1 (human)

## Current model (mechanistic narrative)

The TAC1 symbol in this corpus resolves to at least three biologically unrelated genes, and the mammalian TAC1 entries describe a tachykinin neuropeptide precursor. In mammals, TAC1 encodes substance P and neurokinin A, neuropeptides whose loss diminishes anxiety- and depression-related behavior and disrupts stress and fear responses [PMID:12427862]. These peptides act largely through NK1R: Tac1-expressing neurons drive defined circuits including a lateral/ventrolateral PAG pathway that facilitates the itch-scratching cycle via spinal GRPR neurons [PMID:30554781], a nucleus accumbens shell projection to ventral pallidum that bidirectionally controls stress-induced anhedonia [PMID:33147466], and an accumbens medial-shell projection to lateral hypothalamus governing aversive avoidance [PMID:36901777]. TAC1 tachykinins are required for injury-induced nociceptor mechanical sensitization and hyperexcitability [PMID:31012376], for morphine-induced respiratory depression and opioid withdrawal aversion [PMID:20590634], and they support endogenous spinal opioid peptide tone [PMID:26072188]. Beyond the nervous system, TAC1 peptides maintain basal cutaneous microcirculation [PMID:23499760], modulate puberty and GnRH-neuron responsiveness to kisspeptin via NK1R-Kiss1R heterodimerization [PMID:28444173], control energy balance and circadian feeding through the melanocortin/POMC system [PMID:28775376], and act as prolactin secretagogues in the seasonally regulated pars tuberalis [PMID:20434341]. TAC1 transcription is repressed by REST, which cooperates synergistically with NFκB at sites within exon 1 [PMID:19246391, PMID:17709376], and is activated downstream of SDF-1α through CRE/CREB signaling using distinct pathways in different cell types—cAMP-independent Gαi2-PI3K-PKCζ-ERK signaling in breast cells [PMID:18316470]—together with JNK/ATF-2/AP-1 input and enhancer (ECR) synergy in differentiating and sensory neurons [PMID:21160161, PMID:21671725], plus MeCP2 binding and promoter CpG methylation [PMID:23759142]. Separately and unrelated to the neuropeptide gene, the C. elegans TAC-1 (a TACC-family microtubule-associated protein) and the Candida/Candida parapsilosis Tac1 (a zinc-cluster transcription factor) and a plant TAC1 (tiller angle control) appear in this corpus as symbol collisions describing entirely distinct proteins.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0048018 receptor ligand activity
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-112316 Neuronal System, R-HSA-162582 Signal Transduction
- **partners:** NK1R, KISS1R
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | High | TAC-1 (C. elegans TACC protein) physically interacts with ZYG-9 (XMAP215 family MAP) both in vitro and in vivo, and the two proteins mutually stabilize each other; TAC-1 centrosomal localization requires gamma-tubulin and Aurora-A kinase AIR-1 activity; loss of TAC-1 results in defective microtubule assembly as measured by FRAP. | PMID:12956950, PMID:12956951, PMID:12956952 | Current biology : CB |
| 2003 | High | TAC-1 depletion (RNAi) in C. elegans embryos produces very short centrosomal microtubules and short spindles without reducing alpha-tubulin intensity near centrosomes, indicating microtubule nucleation is intact but elongation/stabilization is impaired; TAC-1 and ZYG-9 are mutually dependent for centrosomal localization. | PMID:12956951, PMID:12956952 | Current biology : CB |
| 2007 | High | In C. elegans, TAC-1 physically interacts with ZYG-8 (doublecortin domain protein) through ZYG-8's doublecortin domain; TAC-1 and ZYG-8 form a complex that does not contain ZYG-9 in vivo; TAC-1 is required for correct ZYG-9 centrosomal enrichment; the ZYG-9-TAC-1 complex is required for correct anaphase spindle positioning. | PMID:17666432 | Journal of cell science |
| 2023 | Medium | In C. elegans, Shugoshin SGO-1 binds TAC-1 (TACC protein) and constrains TAC-1 to the ciliary basal body via the transition zone; TAC-1 activity must be maintained below a threshold at the ciliary base for correct cilia function, and SGO-1 participates in this regulation. | PMID:37296204 | Scientific reports |
| 2002 | High | Targeted deletion of the Tac1 gene (encoding substance P and neurokinin A) in mice diminishes anxiety- and depression-related behaviors, establishing that Tac1-encoded tachykinins are required for normal fear and stress responses. | PMID:12427862 | The Journal of neuroscience : the official journal of the Society for Neuroscience |
| 2018 | High | Tac1-expressing glutamatergic neurons in the lateral/ventrolateral PAG facilitate the itch-scratching cycle via descending regulation; ablation or suppression of these neurons decreases itch-induced scratching; their activation-evoked scratching is suppressed by ablation of spinal GRPR neurons. | PMID:30554781 | Neuron |
| 2014 | High | Tac2 gene (encoding NkB) expressed in centromedial amygdala (CeM) neurons is required for fear memory consolidation; NkB and its receptor Nk3R mediate this effect; increased Tac2 expression or lentiviral CeA overexpression enhances fear consolidation, blocked by Nk3R antagonist osanetant; silencing Tac2-expressing neurons via DREADDs impairs fear consolidation. | PMID:24976214 | Neuron |
| 2016 | Medium | In vivo optogenetic stimulation of CeA Tac2-expressing neurons (ChR2 knockin mice) during fear acquisition enhanced fear memory consolidation and drove action potential firing in vitro; Tac2-CeA neurons co-express striatal-enriched protein tyrosine phosphatase (STEP), which may regulate Nk3R signaling. | PMID:27238620 | Neuropsychopharmacology : official publication of the American College of Neuropsychopharmacology |
| 2018 | High | Chronic social isolation stress (2 weeks) in mice induces brain-wide upregulation of Tac2/NkB; systemic Nk3R antagonist prevents virtually all behavioral effects of chronic social isolation; enhancing NkB expression and release in group-housed mice phenocopies social isolation stress; dissociable region-specific requirements for Tac2 peptide and Nk3R in different behavioral changes. | PMID:29775595 | Cell |
| 2021 | Medium | Sex differences exist in Tac2 pathway regulation of fear memory consolidation: CeA-Tac2 antagonism impairs fear memory in males but enhances it in females; CeA-testosterone mediates Tac2 effects in males, CeA-estradiol in females; Akt/GSK3β/β-Catenin signaling mediates the sex-differential Tac2 pathway regulation. | PMID:33941789 | Nature communications |
| 2020 | Medium | Tac1-expressing neurons in the nucleus accumbens (NAc) lateral shell project to ventral pallidum and contribute to stress-induced anhedonia-like behavior; selective inhibition and activation of Tac1-NAc neurons bidirectionally modulate stress susceptibility; inhibition of neurokinin 1 receptor promotes susceptibility to social stress. | PMID:33147466 | Cell reports |
| 2023 | Medium | Tac1 neurons in the NAc medial shell project to the lateral hypothalamic area (LH); the NAc-Tac1→LH pathway contributes to avoidance responses to aversive stimuli; medial prefrontal cortex sends excitatory inputs to NAc-Tac1 neurons regulating avoidance. | PMID:36901777 | International journal of molecular sciences |
| 2009 | Medium | REST (RE-1 silencing transcription factor) binds the 5' UTR of the TAC1 promoter and suppresses TAC1 expression; REST expression in breast cancer cells is inversely proportional to aggressiveness; REST knockdown increases TAC1 expression, proliferation, and migration in low-metastatic cells; ectopic REST in aggressive cells reduces these parameters. | PMID:19246391 | Proceedings of the National Academy of Sciences of the United States of America |
| 2007 | Medium | REST and NFκB synergistically repress TAC1 transcription in human mesenchymal stem cells; two REST-binding sites are adjacent to one NFκB site within exon 1 of the TAC1 promoter; ChIP and mutagenesis confirmed both factors cooperate for repression in neurogenic and cytokine-stimulated conditions. | PMID:17709376 | The Journal of biological chemistry |
| 2010 | Medium | TAC1 promoter requires synergy with a remote enhancer element (ECR2) to respond to MEK/ERK (MAPK) signaling in sensory neurons; antagonism of the MEK pathway blocks noxious stimulation-driven TAC1 enhancer-promoter synergy; capsaicin induction involves a non-cell-autonomous mechanism in larger diameter neurons. | PMID:21160161 | Neuro-Signals |
| 2011 | Medium | NK1 receptor is expressed in all SP-expressing sensory neurons after capsaicin induction; an NK1 agonist activates both SP expression and the TAC1 ECR1 enhancer-promoter in larger diameter neurons, demonstrating an autocrine loop controlling TAC1 promoter activity in sensory neurons. | PMID:21294877 | Journal of neuroinflammation |
| 2011 | Medium | During MSC-to-neuron differentiation, CRE1 and CRE2/AP-1 sites in the TAC1 promoter are activated sequentially (days 6 and 12); decrease of REST activates JNK, which activates ATF-2 and AP-1 to bind CRE1 and CRE2/AP-1 respectively; JNK inhibition blocks TAC1 induction; transplanted JNK-pathway-active MSCs improve spinal cord injury in zebrafish. | PMID:21671725 | Stem cells and development |
| 2007 | Medium | SDF-1α regulates TAC1 expression in bone marrow stromal cells via NF-κB; at high SDF-1α levels (≥50 ng/mL) NF-κB activation mediates repression of TAC1 within exon 1; substance P produced downstream does not regulate SDF-1α production (negative finding); substance P signals through NK1 (not NK2) receptor to stimulate hematopoiesis. | PMID:17277111 | Journal of immunology (Baltimore, Md. : 1950) |
| 2008 | Medium | In non-tumorigenic breast cells, SDF-1α at low concentrations activates TAC1 via CRE sites through a non-canonical Gαi2-PI3K-PKCζ-p38-ERK pathway to phosphorylate CREB, distinct from the cAMP-PKA pathway used in bone marrow stromal cells. | PMID:18316470 | Journal of molecular endocrinology |
| 2013 | Medium | MeCP2 binds directly to the TAC1 promoter in HEK cells as shown by ChIP; antiepileptic drug (valproic acid) treatment alters MeCP2 binding to TAC1 promoter; TAC1 promoter CpG hypermethylation correlates with reduced TAC1 expression in autism and seizure disorder. | PMID:23759142 | Journal of neurodevelopmental disorders |
| 2007 | Low | Post-transcriptional regulation of Tac1 mRNA in bone marrow stroma involves RNA-binding proteins (with differential binding kinetics for stimulatory vs. inhibitory cytokines) and cytokine-induced miRNAs that interact with the 3' UTR of Tac1 mRNA. | PMID:18061399 | Brain, behavior, and immunity |
| 2010 | Medium | Tac1-encoded tachykinins (substance P and neurokinin A) are required for morphine-induced respiratory depression and the aversive aspect of opioid withdrawal; in Tac1-/- mice morphine analgesia is enhanced and behavioral sensitization (addiction mechanism) is reduced. | PMID:20590634 | British journal of pharmacology |
| 2017 | Medium | Tac1 knockout male mice show delayed puberty, decreased Pdyn and Nos1 expression, and elevated GnRH levels; kisspeptin receptor (Kiss1R) and substance P receptor (NK1R) heterodimerize, suggesting SP tone alters GnRH neuron responsiveness to kisspeptin; Tac1-/- mice show decreased LH response to central kisspeptin and senktide administration despite intact GnRH neuron stimulation. | PMID:28444173 | Endocrinology |
| 2017 | Medium | TAC1-encoded substance P and neurokinin A maintain basal cutaneous microcirculation; Tac1-/- mice show significantly lower basal postoperative skin microcirculation but mustard oil-induced neurogenic vasodilation is unaffected, while motor coordination is impaired in Tac1-/- mice. | PMID:23499760 | Peptides |
| 2019 | Medium | Tac1 knockout nociceptors display disrupted encoding of tonic suprathreshold mechanical stimuli and fail to develop mechanical sensitization after injury; Tac1-/- mice show reduced paw edema, hypersensitivity, and weight-bearing deficits after incision, and their nociceptors lack post-incision electrical hyperexcitability, despite normal CGRP upregulation. | PMID:31012376 | Molecular pain |
| 2015 | Medium | Absence of Tac1-encoded tachykinins (Tac1-/- mice) is associated with significantly lower spinal cord concentrations of opioid peptides endomorphin-2, leucine-enkephalin, and dynorphin A (Dyn A ~3-fold lower), suggesting tachykinin system supports endogenous opioid tone. | PMID:26072188 | Neuropeptides |
| 2017 | Medium | Tac1 ablation in mice produces a lean phenotype with reduced food intake, altered circadian feeding rhythm (disrupted clock gene Cry1/2, Per1/2 expression in SCN, MBH, and liver), increased proopiomelanocortin (POMC) expression in MBH, resistance to diet-induced obesity, and improved glucose tolerance; Tac1 controls energy balance through the melanocortin system. | PMID:28775376 | International journal of obesity (2005) |
| 2017 | Medium | In Candida albicans, hyperactivated Tac1 (by gain-of-function mutations or xenobiotics) facilitates recruitment of the Mediator coactivator complex to the CDR1 promoter; CDR1 activation and azole resistance depend on the Tac1 C-terminal transcriptional activation domain (TAD) and Mediator tail module subunits; Tac1 hyperactivation correlates with Mediator-dependent Tac1 phosphorylation; the Tac1 middle region negatively regulates the TAD. | PMID:28807920 | Antimicrobial agents and chemotherapy |
| 2023 | Medium | In C. albicans Tac1, the N-terminal DNA binding domain (DBD) interacts with the Drug Responsive Element (DRE) in CDR1/CDR2 promoters; the C-terminal Acidic Activation Domain (AAD) interacts with TATA box binding protein (TBP); the Middle Homology Region (MHR) acts as a xenobiotic binding domain (XBD) important for drug resistance. | PMID:37502396 | Frontiers in microbiology |
| 2018 | Medium | C. albicans Tac1 and Znc1 are functionally activated by farnesol (quorum-sensing molecule) and together bind the CDR1 promoter to upregulate CDR1; CDR1 expression then facilitates farnesol efflux; Tac1 and Znc1 have overlapping but non-identical regulons. | PMID:30104273 | Antimicrobial agents and chemotherapy |
| 2023 | High | In Candida parapsilosis, gain-of-function mutation CpTac1-G650E causes 8-fold increase in fluconazole MIC and overexpression of CpCDR1, CpCDR1B, and CpCDR1C; correction of this mutation reduces MIC 16-fold; disruption of CDR1/CDR1B/CDR1C together reduces MIC 4-fold, establishing CpTac1 as a direct regulator of efflux pump-mediated triazole resistance. | PMID:37666448 | Clinical microbiology and infection : the official publication of the European Society of Clinical Microbiology and Infectious Diseases |
| 2010 | Medium | TAC1 is expressed in the sheep pars tuberalis (PT) and strongly activated by long photoperiod; TAC1-encoded peptides (substance P and neurokinin A) act as prolactin secretagogues on primary pituitary cells, making TAC1 a candidate for the PT-expressed 'tuberalin' seasonal hormone regulator. | PMID:20434341 | Current biology : CB |
| 2025 | Low | In indica rice, fine-tuning TAC1 expression levels via CRISPR-Cas9 editing of upstream and downstream non-coding regions produces gradient tiller angle changes proportional to TAC1 expression levels, with no effect on other agronomic traits; TAC1 is conserved across species including fruit trees. | PMID:40052456 | Journal of integrative plant biology |
| 2024 | Medium | In the spinal cord dorsal horn, Tac2-expressing neurons receive direct inhibitory input from Npy neurons; during chronic itch, Y1R expression on Tac2 neurons is reduced and NPY-Y1R inhibitory regulation of Tac2 neurons is diminished, contributing to mechanical hyperknesis. | PMID:38164144 | Theranostics |
| 2025 | Medium | PBNTac1 neurons form close synaptic connections with CeATac1 neurons; activation of the PBNTac1→CeA pathway increases scratching in histamine-induced itch but not chloroquine-induced itch; inhibition of this pathway decreases histamine-induced scratching, defining a modality-specific itch circuit. | PMID:39914640 | Brain research |

## Citations

- PMID:12427862
- PMID:12956950
- PMID:12956951
- PMID:12956952
- PMID:17277111
- PMID:17666432
- PMID:17709376
- PMID:18061399
- PMID:18316470
- PMID:19246391
- PMID:20434341
- PMID:20590634
- PMID:21160161
- PMID:21294877
- PMID:21671725
- PMID:23499760
- PMID:23759142
- PMID:24976214
- PMID:26072188
- PMID:27238620
- PMID:28444173
- PMID:28775376
- PMID:28807920
- PMID:29775595
- PMID:30104273
- PMID:30554781
- PMID:31012376
- PMID:33147466
- PMID:33941789
- PMID:36901777
- PMID:37296204
- PMID:37502396
- PMID:37666448
- PMID:38164144
- PMID:39914640
- PMID:40052456
