---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/TRPV1
affinage_run_date: 2026-06-10T10:51:56
uniprot_accession: Q8NER1
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 24
citation_count: 22
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for TRPV1 (human)

## Current model (mechanistic narrative)

TRPV1 is a polymodal, non-selective cation channel that transduces noxious chemical and physical stimuli into nociceptive signaling and serves as a hub for inflammatory sensitization [PMID:34496225, PMID:31676602]. Cryo-EM studies establish that protons, vanilloid agonists, and peptide toxins drive selectivity-filter conformational transitions allosterically coupled to the cytoplasmic gate, and that channel opening proceeds as a sequential trajectory—intracellular gate opening, then selectivity filter dilation, then pore-loop rearrangement [PMID:34496225, PMID:35610228]. Capsaicin engages a transmembrane pocket in a 'tail-up, head-down' configuration and stabilizes the open state through 'pull-and-contact' with the S4-S5 linker [PMID:28044278]. Beyond exogenous vanilloids, TRPV1 is directly activated by endogenous lipids, including the diacylglycerol metabolites 2-AG and 1-AG generated downstream of phospholipase C, and by retinoids, defining it as an ionotropic receptor for these ligands [PMID:24312564, PMID:23925292]. Channel activity is tuned by membrane PIP2, which acts as a direct positive cofactor whose depletion by Ca2+-activated PLCδ underlies capsaicin desensitization [PMID:17074976, PMID:25754030], and by phosphorylation: AKAP150 scaffolds PKA to sensitize the channel [PMID:18381233], PKC phosphorylation at S801 mediates inflammatory sensitization to ligand [PMID:31676602], and PKCε phosphorylation at T704/S502 underlies cytokine sensing in the carotid body [PMID:33180962]. Growth-factor signaling sensitizes TRPV1 through PI3K p85β binding to its N-terminus and consequent trafficking to the plasma membrane [PMID:17074976, PMID:15857517]. TRPV1 also assembles into heteromeric channels with TRPA1 and TRPV4 that alter its gating and pharmacology [PMID:24643480, PMID:31369032]. Beyond its channel role, TRPV1 modulates μ-opioid receptor signaling by binding MOR1 and blocking GRK5- and β-arrestin2-dependent receptor phosphorylation and desensitization [PMID:30940767, PMID:29203659], and in the CNS it localizes to synapses, regulates vesicle recycling, and controls stress responses via a glucocorticoid receptor/HDAC2 pathway [PMID:20483957, PMID:28402861].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005215 transporter activity, GO:0060089 molecular transducer activity, GO:0008289 lipid binding, GO:0140299 molecular sensor activity
- **localization:** GO:0005886 plasma membrane, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-112316 Neuronal System, R-HSA-162582 Signal Transduction, R-HSA-9709957 Sensory Perception
- **partners:** PIK3R2 (P85Β), AKAP150, TRPA1, TRPV4, OPRM1 (MOR1), GRK5
- **complexes:** TRPV1::TRPA1 heteromeric channel, TRPV1::TRPV4 heteromeric channel

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | Cryo-EM structural snapshots of TRPV1 revealed mechanism of polymodal functionality: protons, vanilloid agonists, and peptide toxins induce conformational transitions of the selectivity filter that permit permeation by small and large organic cations, with allosteric coupling identified between sites proximal to the selectivity filter and the cytoplasmic gate. | PMID:34496225 | Cell |
| 2022 | High | Cryo-EM ensemble analysis of TRPV1 with resiniferatoxin (RTx) bound revealed a sequential conformational trajectory: intracellular gate opening occurs first, followed by selectivity filter dilation, then pore loop rearrangement to reach the final open state, demonstrating a concerted stepwise allosteric mechanism. | PMID:35610228 | Nature communications |
| 2017 | High | Capsaicin binds to a pocket formed by TRPV1 transmembrane segments in a 'tail-up, head-down' configuration, mediated by hydrogen bonds and van der Waals interactions; upon binding, capsaicin stabilizes the open state by 'pull-and-contact' with the S4-S5 linker. | PMID:28044278 | Protein & cell |
| 2006 | High | PI3K p85β subunit physically interacts with the N-terminal region of TRPV1 (demonstrated by yeast 2-hybrid, co-immunoprecipitation from HEK293 cells and DRG neurons, and in vitro pulldown), and this physical coupling facilitates NGF-mediated trafficking of TRPV1 to the plasma membrane, increasing channel number at the surface; wortmannin abolished NGF-mediated sensitization. | PMID:17074976 | The Journal of general physiology |
| 2008 | High | AKAP150 associates with TRPV1 in trigeminal ganglia neurons and scaffolds PKA to mediate PKA-dependent phosphorylation and sensitization of TRPV1; siRNA knockdown of AKAP150 reduced PKA phosphorylation of TRPV1 and attenuated PKA sensitization of TRPV1 activity; in vivo AKAP antagonist reduced prostaglandin E2-induced thermal hyperalgesia. | PMID:18381233 | Pain |
| 2014 | High | TRPV1 and TRPA1 form functional heteromeric channels: TRPV1::TRPA1 concatemers form tetrameric channels (confirmed by AFM) with two TRPV1::TRPA1 units arranged face-to-face; these heteromers respond to TRPV1 agonists (capsaicin, acidic pH, ethanol) but not TRPA1 agonists, have only two capsaicin binding sites, show reduced total current, and TRPA1 presence exerts functional inhibition on TRPV1. | PMID:24643480 | Pflugers Archiv : European journal of physiology |
| 2019 | High | PKC-mediated phosphorylation of TRPV1 at S801 contributes to inflammation-mediated sensitization of TRPV1 to ligand (capsaicin) but not to heat in vivo; S801A knock-in mice generated by CRISPR/Cas9 showed impaired PKC-induced sensitization of capsaicin-mediated currents in sensory neurons, attenuated PMA-evoked nocifensive responses, and reduced ongoing inflammatory pain, while basal sensitivity was preserved. | PMID:31676602 | The Journal of neuroscience : the official journal of the Society for Neuroscience |
| 2013 | High | 2-Arachidonoylglycerol (2-AG) and 1-arachidonoylglycerol (1-AG), diacylglycerol metabolites generated by phospholipase C, directly activate TRPV1 on native vascular sensory nerve fibers and in heterologously expressed TRPV1 in whole cells and inside-out membrane patches; monoacylglycerol lipase inhibitors augmented TRPV1-mediated responses to these endogenous ligands, and vasodilator responses to 2-AG were minor in TRPV1 knockout mice. | PMID:24312564 | PloS one |
| 2005 | Medium | Insulin and IGF-I enhance TRPV1-mediated membrane currents through both increased receptor sensitivity and translocation of TRPV1 from cytosol to plasma membrane; this process requires receptor tyrosine kinase activation leading to PI3K and PKC-mediated phosphorylation of TRPV1. | PMID:15857517 | Molecular pain |
| 2017 | High | TRPV1 activation stimulates a MAPK signaling pathway that causes β-arrestin2 to translocate to the nucleus, thereby preventing β-arrestin2 recruitment to the μ-opioid receptor (MOR), blocking MOR internalization and desensitization, and thus prolonging opioid analgesia during inflammation; this mechanism was absent in TRPV1-deficient mice. | PMID:30940767 | Science signaling |
| 2017 | Medium | TRPV1 physically binds MOR1 and blocks opioid-dependent phosphorylation of MOR1 while leaving G protein signaling intact; Ca2+ influx through TRPV1 activates calcium/calmodulin-dependent translocation of GRK5 away from the plasma membrane, thereby blocking its ability to phosphorylate MOR1. | PMID:29203659 | Proceedings of the National Academy of Sciences of the United States of America |
| 2017 | Medium | TRPV1 regulates stress responses through HDAC2: TRPV1-deficient mice show reduced glucocorticoid receptor (GR)-mediated HDAC2 expression and activity; hippocampal knockdown of TRPV1 phenocopied stress resilience, and this behavioral effect was blocked by HDAC2 overexpression, establishing HDAC2 as a molecular link between TRPV1 activity and stress responses. | PMID:28402861 | Cell reports |
| 2007 | Medium | TRPV1 expression induces filopodia and neurite-like structures; TRPV1 localizes to filopodial tips; the N-terminal intracellular domain of TRPV1 is sufficient for filopodial initiation, while the C-terminal cytoplasmic domain stabilizes microtubules within filopodia; TRPV1 expression also alters cellular distribution and enhances endogenous expression of myosin IIA and myosin IIIA. | PMID:17714453 | Journal of neurochemistry |
| 2010 | Medium | TRPV1 is present in synaptic structures (co-localizes with pre- and postsynaptic proteins in cortical neuron spines), is detected in synaptosomes and synaptic transport vesicles, and its activation rapidly modulates vesicle recycling/fusion as demonstrated by FM4-64 dye imaging. | PMID:20483957 | Journal of cell science |
| 2013 | Medium | TRPV1 activation in human corneal fibroblasts (HCF) by capsaicin induces Ca2+ influx, activates MAPK p38 signaling, and leads to IL-6 release; these effects were abolished by TRPV1 siRNA silencing or p38 MAPK inhibitor SB203580, establishing a TRPV1→p38 MAPK→IL-6 pathway in corneal inflammation. | PMID:23232207 | Experimental eye research |
| 2013 | High | Retinoids (naturally occurring and synthetic) directly activate recombinant and native TRPV1 ion channel; in vivo retinoid-induced pain behaviors were eliminated or significantly reduced by genetic or pharmacological inhibition of TRPV1, identifying TRPV1 as an ionotropic receptor for retinoids. | PMID:23925292 | The Journal of clinical investigation |
| 2020 | Medium | Resolvins (RvD1, RvD2, RvE1) prevent histamine-induced TRPV1 sensitization in DRG neurons; RvD2 reversal of TRPV1 sensitization is blocked by the GPR18 antagonist O-1918 and by pertussis toxin, establishing a GPR18/Gi-dependent pathway through which RvD2 desensitizes TRPV1. | PMID:33023902 | Gut |
| 2020 | High | PKCε-dependent phosphorylation of TRPV1 at sites T704 and S502 mediates carotid body sensing of asthma-associated Th2 cytokines; site-directed mutagenesis of these residues impaired the response, and systemic PKCε blockade reduced asthmatic bronchoconstriction without affecting oxygen sensing. | PMID:33180962 | The Journal of physiology |
| 2008 | High | PIP2 directly potentiates TRPV1 in excised inside-out patches; polylysine (a cationic phosphoinositide sequestering agent) inhibited TRPV1 rather than potentiating it, contradicting the proposed tonic inhibition model for PIP2 on TRPV1. | PMID:17074976 | The Journal of general physiology |
| 2016 | Low | TRPV1 activation by capsaicin in SUM149PT triple-negative breast cancer cells induced Ca2+ influx (blocked by capsazepine), caused growth inhibition, and induced apoptosis and necrosis, establishing a functional TRPV1-mediated Ca2+-dependent anti-tumor signaling pathway. | PMID:28008282 | Breast cancer (Dove Medical Press) |
| 2018 | Low | Troglitazone activates TRPV1 to cause deacetylation of PPARγ in 3T3-L1 cells; TRPV1 inhibition by capsazepine prevented Troglitazone-induced Ca2+ influx, and inhibition of TRPV1 or Sirtuin 1 prevented PPARγ deacetylation, establishing a TRPV1→Ca2+→Sirtuin1→PPARγ deacetylation pathway. | PMID:30496795 | Biochimica et biophysica acta. Molecular basis of disease |
| 2019 | Medium | TRPV1 and TRPV4 form functional heteromeric channel complexes in retinal microvascular endothelial cells (RMECs), demonstrated by proximity ligation assay and electrophysiological recording; pharmacological inhibition of either channel suppressed in vitro tubulogenesis and reduced retinal neovascularization in the oxygen-induced retinopathy mouse model. | PMID:31369032 | Investigative ophthalmology & visual science |
| 2016 | Medium | In TRPV1-expressing HEK cells co-expressing the histamine H1 receptor (a PLC-coupled receptor), histamine stimulated 2-arachidonoylglycerol (2-AG) formation via diacylglycerol lipase, and the resulting 2-AG activated TRPV1 currents; this effect was augmented by monoacylglycerol lipase inhibition (JZL184) and abolished by diacylglycerol lipase inhibition, placing 2-AG generation downstream of PLC as a direct TRPV1 activator. | PMID:24312564 | PloS one |
| 2015 | Medium | Ca2+ flowing through TRPV1 activates PLCδ isoforms, resulting in PIP2 depletion that limits TRPV1 channel activity and contributes to capsaicin-induced desensitization; PIP2 acts as a positive cofactor for TRPV1 via direct interaction, and its depletion is a mechanism of desensitization. | PMID:25754030 | Pflugers Archiv : European journal of physiology |

## Citations

- PMID:15857517
- PMID:17074976
- PMID:17714453
- PMID:18381233
- PMID:20483957
- PMID:23232207
- PMID:23925292
- PMID:24312564
- PMID:24643480
- PMID:25754030
- PMID:28008282
- PMID:28044278
- PMID:28402861
- PMID:29203659
- PMID:30496795
- PMID:30940767
- PMID:31369032
- PMID:31676602
- PMID:33023902
- PMID:33180962
- PMID:34496225
- PMID:35610228
