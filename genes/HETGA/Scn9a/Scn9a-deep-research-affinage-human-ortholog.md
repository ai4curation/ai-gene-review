---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/SCN9A
affinage_run_date: 2026-06-10T07:46:29
uniprot_accession: Q15858
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 42
citation_count: 42
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for SCN9A (human)

## Current model (mechanistic narrative)

SCN9A encodes Nav1.7, a voltage-gated sodium channel α-subunit that sets the threshold for action potential initiation in peripheral sensory neurons and is an essential, non-redundant requirement for human nociception and olfaction [PMID:17167479, PMID:21441906]. In nociceptors, Nav1.7 activity defines the action potential threshold and contributes to the upstroke; it is required for initiation of C-fiber action potentials in vivo and for normal C-fiber conduction velocity [PMID:37352856, PMID:30720580, PMID:29194125]. The channel is expressed along the entire nociceptive pathway from intraepidermal terminals through DRG somata to central presynaptic terminals, and it is the predominant sodium channel of olfactory sensory neurons where it drives odour-evoked synaptic transmission at the first olfactory synapse [PMID:21569247, PMID:23134641, PMID:21441906]. Inherited gain-of-function missense mutations cause erythromelalgia by hyperpolarizing activation and/or depolarizing steady-state inactivation, lowering firing threshold and amplifying subthreshold sodium influx to produce nociceptor hyperexcitability, with distinct biophysical signatures distinguishing erythromelalgia from PEPD phenotypes [PMID:14985375, PMID:15958509, PMID:24401712, PMID:24311784]; complete loss-of-function truncating and pore-region mutations abolish current and cause congenital insensitivity to pain [PMID:17167479, PMID:17597096, PMID:20635406]. The pain-free state of Nav1.7-null animals and humans is not explained by channel loss alone: deletion upregulates the enkephalin precursor Penk and rebalances GPCR signalling away from pronociceptive serotonergic toward antinociceptive µ- and δ-opioid tone, an endogenous opioid mechanism necessary for the analgesic phenotype [PMID:26634308, PMID:28074005, PMID:30271888]. Channel surface density is set post-translationally by hierarchical CRMP2 SUMOylation—promoted by CDK5 and antagonized by Fyn—that maintains membrane Nav1.7 and, when lost, triggers clathrin-dependent endocytosis via Nedd4-2 with adaptors Numb and EPS15; disrupting CRMP2 SUMOylation reduces surface Nav1.7 and is antinociceptive [PMID:23836888, PMID:27940916, PMID:34757807]. Trafficking and abundance are further controlled by NGF/TrkA–SGK1–Nedd4-2 signalling, paclitaxel-dependent vesicular transport, and direct 3′-UTR targeting by miR-30b and miR-182 [PMID:33063281, PMID:33734317, PMID:27765894, PMID:30425258]. Structural and pharmacological work has mapped how acylsulfonamides trap VSD4 in an activated state via the S4 gating charge and how the peptide ProTx2 antagonises VSD2 gating-charge movement from within the membrane, providing blueprints for isoform-selective inhibition [PMID:26680203, PMID:30661758]. Beyond neurons, Nav1.7 has been assigned roles in oncogene-induced senescence via NF-κB-driven depolarization and a Ca2+/Rb/E2F axis, and in cancer-cell and vascular smooth-muscle migration [PMID:29446526, PMID:18978189, PMID:30927332].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005215 transporter activity
- **localization:** GO:0005886 plasma membrane, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-112316 Neuronal System, R-HSA-162582 Signal Transduction, R-HSA-9609507 Protein localization
- **partners:** CRMP2, NEDD4L, NUMB, EPS15, SCN1B, SCN2B
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | High | Homozygous nonsense mutations (S459X, I767X, W897X) in SCN9A cause loss of function of Nav1.7; co-expression of mutant Nav1.7 with sodium channel β1 and β2 subunits in HEK293 cells produced no currents above background, establishing Nav1.7 as an essential, non-redundant requirement for nociception in humans. | PMID:17167479 | Nature |
| 2004 | Medium | Missense mutations in SCN9A (T2573A and T2543C) cause primary erythermalgia, identifying Nav1.7 as causative for this gain-of-function pain disorder in sensory and sympathetic neurons. | PMID:14985375 | Journal of medical genetics |
| 2005 | High | A gain-of-function mutation in Nav1.7 (erythromelalgia-associated) produces a hyperpolarizing shift in activation and a depolarizing shift in steady-state inactivation, lowering thresholds for single action potentials and high-frequency firing in dorsal root ganglion neurons. | PMID:15958509 | Brain : a journal of neurology |
| 2007 | High | The erythromelalgia mutation N395K, located within the local anaesthetic binding site of Nav1.7, attenuates lidocaine inhibition; IC50 for inactivated Nav1.7-N395K was ~2.8 mM versus ~500 µM for wild-type, establishing residue N395 as critical for lidocaine binding. | PMID:17430993 | The Journal of physiology |
| 2006 | High | The S241T erythromelalgia mutation in the domain I S4-S5 linker of Nav1.7 causes a hyperpolarizing shift in activation, slowed deactivation, and enhanced slow inactivation; S241A had no effect while S241L mimicked S241T, demonstrating that side-chain size at position 241 modulates channel gating. | PMID:17008310 | The Journal of biological chemistry |
| 2009 | High | The erythromelalgia mutation V400M in Nav1.7 alters activation, deactivation, steady-state inactivation, and ramp currents; carbamazepine at therapeutic concentrations selectively normalises the voltage dependence of activation and inactivation of V400M but not wild-type Nav1.7, explaining the clinical carbamazepine-responsiveness. | PMID:19557861 | Annals of neurology |
| 2013 | High | SUMOylation of the Nav1.7-binding partner CRMP2 at K374 controls Nav1.7 surface expression; expression of SUMOylation-incompetent CRMP2-K374A in CAD cells selectively reduces huwentoxin-IV-sensitive Nav1.7 currents and decreases surface Nav1.7 levels (biotinylation assay), without affecting Nav1.1 or Nav1.3 currents; deSUMOylation by SENP1/SENP2 similarly decreases surface Nav1.7. | PMID:23836888 | The Journal of biological chemistry |
| 2016 | High | CRMP2 SUMOylation is enhanced by prior phosphorylation by CDK5 and antagonized by Fyn phosphorylation; SUMOylated CRMP2 binds Nav1.7 and maintains membrane localisation and current density; loss of CRMP2 SUMOylation triggers Nav1.7 internalisation via clathrin-dependent endocytosis involving E3 ubiquitin ligase Nedd4-2 and adaptor proteins Numb and EPS15. | PMID:27940916 | Proceedings of the National Academy of Sciences of the United States of America |
| 2015 | High | Crystal structures of Nav1.7 voltage-sensor domain IV (VSD4) in complex with isoform-selective antagonists (GX-936 and related acylsulfonamides) show that these inhibitors bind the activated state of VSD4 by engaging the fourth arginine gating charge on the S4 helix with an anionic aryl sulfonamide warhead, opposing VSD4 deactivation via a voltage-sensor trapping mechanism; residues on S2 and S3 helices determine isoform selectivity; bound phospholipids implicate the membrane as a modulator. | PMID:26680203 | Science (New York, N.Y.) |
| 2019 | High | Cryo-EM and X-ray crystal structures of ProTx2 (Peruvian green velvet tarantula inhibitor cystine-knot peptide) in complex with Nav1.7 VSD2 reveal that ProTx2 partitions into the membrane to access VSD2, positions two basic residues into the extracellular vestibule to electrostatically antagonise S4 gating-charge movement, and traps both activated and deactivated states of VSD2 showing ~10 Å S4 helix translation. | PMID:30661758 | Cell |
| 2012 | High | Conditional deletion of Nav1.7 (SCN9A) in all sensory neurons (Advillin-Cre) abolishes mechanical pain, inflammatory pain, and heat withdrawal reflexes, while deletion limited to Nav1.8-positive nociceptors retains heat-evoked pain; neuropathic pain and hotplate responses require deletion in both sensory and sympathetic neurons, demonstrating a distinct role for Nav1.7 in sympathetic neurons for neuropathic pain. | PMID:22531176 | Nature communications |
| 2011 | High | Loss of Nav1.7 function (SCN9A knockout) abolishes odour-evoked synaptic signalling from olfactory sensory neuron axon terminals at the first olfactory synapse without preventing action potential generation in those neurons, causing anosmia; Nav1.7-null human patients also lack odour perception. | PMID:21441906 | Nature |
| 2015 | High | Loss of Nav1.7 (SCN9A deletion) upregulates the enkephalin precursor Penk mRNA and met-enkephalin protein specifically in sensory neurons; the opioid antagonist naloxone potentiates noxious spinal input and dramatically reduces analgesia in Nav1.7-null mice and a human Nav1.7-null mutant, indicating that Nav1.7 deletion drives endogenous opioid tone that contributes to the pain-free phenotype. | PMID:26634308 | Nature communications |
| 2011 | Medium | Nav1.7 is the predominant sodium channel transcript in rat and mouse olfactory sensory neurons (OSNs), with Nav1.7 immunoreactivity localised to peripheral presynaptic OSN axons; Nav1.6 is primarily postsynaptic in olfactory bulb glomeruli, providing a mechanistic basis for anosmia upon Nav1.7 loss. | PMID:21569247 | Molecular pain |
| 2012 | Medium | Nav1.7 immunoreactivity extends from peripheral intraepidermal terminals in skin through DRG somata to central presynaptic terminals in spinal cord dorsal horn, supporting roles in action potential electrogenesis, axonal conduction, and presynaptic depolarisation along the entire nociceptive pathway. | PMID:23134641 | Molecular pain |
| 2007 | High | A stop codon mutation in SCN9A (Y328X) truncates Nav1.7 before all pore-forming regions; expression of the truncated gene in cell lines produces no functional sodium currents and no compensatory changes in endogenous voltage-gated sodium currents, confirming complete loss of function. | PMID:17597096 | Human molecular genetics |
| 2010 | High | Two non-truncating Nav1.7 mutations causing CIP (R896Q missense and ΔR1370-L1374 in-frame deletion) both map to the channel pore region and cause significant reduction in membrane localisation and complete loss of sodium channel function, demonstrating that pore-region mutations impair both trafficking and conductance. | PMID:20635406 | Human mutation |
| 2009 | High | The SCN9A common polymorphism R1150W depolarises Nav1.7 activation by ~8–11 mV and depolarises resting membrane potential by ~6 mV, increasing firing frequency ~2-fold in DRG neurons, showing that naturally occurring polymorphisms in Nav1.7 can modulate nociceptor excitability. | PMID:20033988 | Annals of neurology |
| 2014 | High | In DRG neurons, dynamic-clamp delivery of the erythromelalgia L858H Nav1.7 mutation at physiological conductance levels produces a 27-fold amplification of net sodium influx during subthreshold depolarisations, providing a quantitative mechanistic link between altered channel biophysics and nociceptor hyperexcitability underlying pain. | PMID:24401712 | Journal of neurophysiology |
| 2013 | High | The erythromelalgia mutation A1632T shifts steady-state fast inactivation to depolarised potentials (normally a PEPD characteristic) without slowing open-state inactivation or increasing resurgent currents; DRG neurons expressing A1632T show hyperexcitability and spontaneous firing. This demonstrates that depolarised fast inactivation without increased resurgent currents produces an IEM rather than PEPD phenotype. | PMID:24311784 | The Journal of biological chemistry |
| 2015 | High | The erythromelalgia mutation Q875E produces a large −18 mV hyperpolarising shift in Nav1.7 activation; the mutant glutamate at position 875 is spatially proximate to gating charge Arg-214 in domain I voltage sensor (confirmed by engineered disulfide bridge), suggesting a salt bridge that stabilises the activated VSD conformation; extracellular Ca2+ or Mg2+ reverses the gating shift by electrostatic screening. | PMID:25575597 | The Journal of biological chemistry |
| 2011 | Low | Nav1.7 accumulates in transected axons of experimental rat neuromas and co-localises with phosphorylated ERK1/2 (pERK1/2), suggesting that MAP kinase signalling at sites of injury may modulate Nav1.7 properties and contribute to spontaneous ectopic firing. | PMID:21601570 | Experimental neurology |
| 2017 | High | Loss of Nav1.7 leads to decreased pronociceptive serotonergic (5-HT4/Gαs/PKA/RIIβ) signalling and increased efficacy of antinociceptive mu-opioid (Gαi) signalling in sensory neurons; opioids more efficiently inhibit TTX-resistant sodium currents in Nav1.7-null nociceptors, shifting the balance of GPCR signalling toward antinociception. | PMID:28074005 | Science signaling |
| 2018 | High | Both µ- and δ-opioid receptors are required for the analgesic phenotype of Nav1.7-null mice; pharmacological or genetic co-ablation of µ- and δ-opioid receptors (but not κ) abolishes the pain-free phenotype; enkephalins (Penk-encoded) are upregulated in Nav1.7 nulls but Nfat5 deletion also upregulates Penk without producing analgesia, indicating that endogenous opioid upregulation is necessary but not sufficient for the Nav1.7-null analgesic state. | PMID:30271888 | Wellcome open research |
| 2021 | High | Preventing CRMP2 SUMOylation (via compound 194 targeting CRMP2-Ubc9 interaction, or CRMP2-K374A mutation) selectively reduces Nav1.7 surface expression and current density in DRG neurons and produces antinociception in rodent pain models; analgesia conferred by compound 194 is opioid-receptor dependent. | PMID:34757807 | Science translational medicine |
| 2023 | High | Nav1.7 is required for the initiation of C-fiber action potentials in vivo; genetic removal or selective pharmacological inhibition of Nav1.7 blocks C-fiber AP initiation as shown by laser speckle contrast imaging and in vivo electrophysiology; enkephalin upregulation upon Nav1.7 deletion is restricted to cLTMR (low-threshold mechanoreceptor) neurons and does not contribute to the analgesic phenotype. | PMID:37352856 | Neuron |
| 2021 | High | Paclitaxel treatment increases vesicular trafficking flux and surface expression of Nav1.7 in sensory axons in a concentration-dependent manner (low concentrations increase flux; high concentrations decrease flux) without requiring increased Nav1.7 mRNA pool; inflammatory mediators further amplify this trafficking increase, providing a mechanism for Nav1.7-dependent peripheral sensitisation in chemotherapy-induced neuropathy. | PMID:33734317 | Brain : a journal of neurology |
| 2024 | High | Nav1.8 amplifies DRG neuron excitability driven by gain-of-function Nav1.7 (L848H) near action potential threshold; at threshold voltage (−21.9 mV), Nav1.8 open-probability exceeds Nav1.7-WT open-probability ninefold; dynamic-clamp reduction of Nav1.8 conductance by 25–50% reverses hyperexcitability in neurons expressing Nav1.7-L848H by increasing rheobase and reducing AP firing probability. | PMID:39378238 | The Journal of general physiology |
| 2007 | Medium | The erythromelalgia mutation L858F differentially shifts the voltage dependence of activation in a cooling-dependent manner (depolarising shift with cooling for L858F but not wild-type Nav1.7), providing a biophysical explanation for symptomatic relief upon limb cooling in affected patients. | PMID:17239250 | Molecular pain |
| 2008 | Medium | Nav1.7 (SCN9A) expression in cultured human aortic smooth muscle cells contributes to TTX-sensitive sodium current; SCN9A siRNA knockdown abolishes this current and significantly inhibits cell migration, endocytosis (HRP uptake), and matrix metalloproteinase-2 secretion, without affecting proliferation; Nav1.7 is also expressed in rabbit aorta after balloon injury. | PMID:18978189 | American journal of physiology. Heart and circulatory physiology |
| 2018 | Medium | SCN9A (Nav1.7) expression is upregulated in senescent cells during oncogene-induced senescence (OIS) via NF-κB transcription factors; Nav1.7 induction leads to plasma membrane depolarisation, which activates a calcium/Rb/E2F pathway to repress mitotic genes and promote senescence; loss of SCN9A allows cells to escape OIS. | PMID:29446526 | Aging cell |
| 2019 | High | iPSC-derived sensory nociceptors from IEM patients carrying Nav1.7/I848T show decreased firing threshold, enhanced action potential upstroke and afterhyperpolarization; the IEM mutation causes a hyperpolarising shift of tetrodotoxin-sensitive Nav activation; Nav1.7 is not active during subthreshold depolarisations but its activity defines AP threshold and contributes to AP upstroke in human sensory neurons. | PMID:30720580 | Pain |
| 2016 | Medium | miR-30b directly targets the 3′ UTR of SCN9A; overexpression of miR-30b in spared-nerve-injury rats inhibits SCN9A transcription and Nav1.7 protein, reducing pain hypersensitivity; miR-30b knockdown increases Nav1.7 expression and induces mechanical hypersensitivity in naïve rats. | PMID:27765894 | Molecular pain |
| 2018 | Medium | miR-182 directly pairs with the SCN9A 3′ UTR (verified by luciferase assay); miR-182 agomir overexpression in SNI rats reverses the pathological Nav1.7 increase in DRG at both mRNA and protein levels and attenuates mechanical hypersensitivity. | PMID:30425258 | Scientific reports |
| 2020 | Medium | NGF triggers sustained Nav1.7 upregulation in DRG via an NGF/TrkA–SGK1–Nedd4-2 phosphorylation pathway; conditional nociceptor-specific Nav1.7 knockout confirms Nav1.7's requirement for NGF-induced and post-surgical pain; pharmacological blockade of this pathway reduces Nav1.7 upregulation and spinal sensitisation. | PMID:33063281 | Molecular neurobiology |
| 2014 | High | In mouse pancreatic β-cells, Nav1.7 (Scn9a) accounts for >85% of the voltage-gated Na+ current; knockout of Scn9a lowers β-cell Na+ current by >85% but glucagon and insulin secretion are unaffected in Scn9a-deficient islets, because Nav1.7 is largely inactive at physiological membrane potentials due to its unusually negative voltage dependence of inactivation in β-cells. | PMID:25172946 | The Journal of physiology |
| 2015 | Low | Nav1.7 is expressed in smooth muscle cells of cutaneous arterioles and arteriole-venule shunts, as well as in endothelial cells lining these vessels and in sensory/sympathetic fibres innervating them, suggesting that mutant Nav1.7 activity in skin vasculature (not only in neurons) contributes to skin reddening in erythromelalgia and PEPD. | PMID:25957174 | Molecular pain |
| 2017 | High | In conditional NaV1.7 knockout (advillin-Cre) sensory neurons, C-fiber axonal conduction velocity is 20% slower than wild-type; activity-dependent slowing of conduction is markedly reduced; a large subpopulation of C-fibers is functionally absent by compound AP recording; heat-evoked CGRP release is normal, indicating Nav1.7 loss impairs C-fiber conduction but not peptide release per se. | PMID:29194125 | Pain |
| 2019 | Medium | SCN9A-encoded Nav1.7 in prostate cancer cells (Mat-LyLu) modulates RhoA and Rac1 Rho GTPase activity in a Nav1.7-dependent manner; Nav1.7 activator JZTX-I increases and inhibitor HNTX-III decreases cell migration/invasion; proteomic analysis identified 64 differentially expressed membrane proteins including cytoskeletal regulators (fascin, muskelin, annexin A2, cofilin-1). | PMID:30927332 | The FEBS journal |
| 2014 | Medium | Anandamide inhibits Nav1.7 sodium currents in a concentration-dependent manner (IC50 ~27 µM) in Xenopus oocytes, causing a depolarising shift of activation and hyperpolarising shift of inactivation, and shows use-dependent block; this is a direct pharmacological action on the channel. | PMID:24557103 | Anesthesia and analgesia |
| 2015 | Medium | The synthetic α-scorpion toxin OD1 and its analogs potently inhibit Nav1.7 fast inactivation by prolonging channel flickering between open and closed states; single-channel recordings confirm that toxins slow inactivation via a voltage-sensor trapping mechanism on domain IV, consistent with the gating-modifier model. | PMID:26646206 | Channels (Austin, Tex.) |
| 2022 | Medium | Buthus martensii Karsch scorpion toxin Makatoxin-3 acts on the S3-S4 loop of Nav1.7 VSD4, causing a hyperpolarising shift in steady-state fast inactivation and impairing inactivation kinetics; key residues mediating this interaction are distinct from those of other α-toxins, defining new structure-function relationships for toxin-Nav1.7 interactions. | PMID:34252912 | Pain |

## Citations

- PMID:14985375
- PMID:15958509
- PMID:17008310
- PMID:17167479
- PMID:17239250
- PMID:17430993
- PMID:17597096
- PMID:18978189
- PMID:19557861
- PMID:20033988
- PMID:20635406
- PMID:21441906
- PMID:21569247
- PMID:21601570
- PMID:22531176
- PMID:23134641
- PMID:23836888
- PMID:24311784
- PMID:24401712
- PMID:24557103
- PMID:25172946
- PMID:25575597
- PMID:25957174
- PMID:26634308
- PMID:26646206
- PMID:26680203
- PMID:27765894
- PMID:27940916
- PMID:28074005
- PMID:29194125
- PMID:29446526
- PMID:30271888
- PMID:30425258
- PMID:30661758
- PMID:30720580
- PMID:30927332
- PMID:33063281
- PMID:33734317
- PMID:34252912
- PMID:34757807
- PMID:37352856
- PMID:39378238
