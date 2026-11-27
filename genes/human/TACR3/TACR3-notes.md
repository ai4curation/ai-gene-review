# TACR3 (human, UniProtKB:P29371) review notes

Neuromedin-K receptor / neurokinin-3 receptor (NK3R), 465 aa, class A (rhodopsin-like)
GPCR of the tachykinin receptor subfamily (InterPro IPR001681, NK3-specific IPR001013;
PANTHER PTHR46925:SF1 NEUROMEDIN-K RECEPTOR).

## Ligand selectivity and receptor activity

- Human NK3R cloning and expression: neurokinin B (NKB, the TAC3 product, also called
  neuromedin K) is the most potent agonist.
  [PMID:1374246 "Neurokinin B is the most potent agonist, followed by eledoisin, substance K and substance P."]
- Human genomic clone expressed in Xenopus oocytes and mammalian cells: NKB-evoked membrane
  conductance, binding, calcium mobilisation and arachidonic acid release; mRNA mainly CNS.
  [PMID:1312036 "expression of the gene in mammalian cells resulted in detection of receptor binding as well as neurokinin-stimulated calcium mobilization and arachidonic acid release, all displaying the pharmacological characteristics expected of a neurokinin-3 receptor"]
  [PMID:1312036 "mRNA for the human neurokinin-3 receptor is expressed predominantly in the central nervous system"]
- Krause et al. 1997 compared the human NK-3 receptor with an NK-3 receptor homolog in CHO
  cells; tachykinins stimulated inositol phospholipid hydrolysis and arachidonic acid release
  at both. [PMID:8990205 "Tachykinin peptides stimulated both inositol phospholipid hydrolysis and arachidonic acid release at NK-3 and NK-3 receptor homolog cell lines"]
- HEK293 NanoBiT/Ca2+ work (2023): NKB, NKA and SP are all full agonists of NK3, NKB the most
  potent; NK3 homodimerises and does not heterodimerise with NK1 or NK2.
  [PMID:37968728 "all tested peptides acted as full agonists for the three NKs with different potency"]
  [PMID:37968728 "Furthermore, coimmunoprecipitation revealed that NK3 did not interact with NK1 or NK2."]
- So NK3R is a tachykinin receptor that prefers NKB but responds to all three mammalian
  tachykinins. Both GO:0004995 tachykinin receptor activity and its child GO:0016498
  neuromedin K receptor activity are accurate; GO:0016498 is the core MF (and is the MF used
  in both cached GO-CAMs, gocams/68d5ebd600000043 and gocams/68d5ebd600000736).

## Structure and G protein coupling

- Cryo-EM structures of NK3R-Gq bound to NKB, SP and senktide (Sun et al. 2023).
  [PMID:37391393 "we determined the cryogenic electron microscopy (cryo-EM) structures of the NK3R-Gq complex bound to NKB, SP and senktide"]
  [PMID:37391393 "NKB preferentially activates NK3R coupled to the Gαq family of G proteins for intracellular signal transduction"]
  Function was read out as IP-one accumulation (a Gq/PLC readout).
  [PMID:37391393 "b IP-one accumulation assay of NK3R activation by NKB, SP, and senktide."]
- Conserved C-terminal FxGLM-NH2 binds the same way for all three peptides; divergent
  N-termini confer subtype preference.
  [PMID:37391393 "the consensus C-termini of the three peptide agonists share a conserved binding mode to NK3R, while the divergent N-termini of the peptides confer the preferential binding of the agonist to NK3R"]
- Topaloglu et al. 2009 used NKB-evoked calcium flux in HEK293 cells as the functional assay
  for wild-type and mutant receptor.
  [PMID:19079066 "NK3R activation is linked to Gq proteins and its action results in an increase in intracellular calcium."]
  [PMID:19079066 "In transiently transfected cells, identified on the basis of coexpressed GFP, NKB elicited a robust increase in intracellular calcium"]
- cAMP: shown for the rat receptor in CHO cells, about tenfold less efficient than PI
  hydrolysis. UniProt records it "By similarity" to rat P16177. For the human receptor,
  Oury-Donat et al. 1995 report agonist-evoked cAMP accumulation in CHO cells with an EC50
  about 25-fold higher than for inositol monophosphate formation; neither paper identifies Gs.
  [PMID:7616392 "NK3 agonists such as [MePhe7]-NKB and senktide stimulated inositol monophosphate formation with EC50 values of 2.0 +/- 1.4 and 2.1 +/- 0.7 nM, respectively."]
  [PMID:7616392 "The cyclic AMP accumulation induced by 10(-7) M [MePhe7]-NKB (EC50 of 54 +/- 2 nM) also was antagonized by SR142801"]
  [PMID:1370820 "The three receptors commonly showed a rapid and marked stimulation in both phosphatidylinositol (PI) hydrolysis and cyclic AMP formation in response to tachykinin interaction."]
  [PMID:1370820 "The stimulation of cyclic AMP formation was less efficient than that of PI hydrolysis"]
  Decision: Gq/PLC pathway (GO:0007209) is core; GO:0007189 kept as non-core.

## Localisation

- UniProt: cell membrane, from PMID:37968728; multi-pass membrane topology predicted.
- PMID:37968728 measured surface expression with an extracellular HiBiT assay; NK3 surface
  signal was detectable but weak relative to NK1/NK2.
  [PMID:37968728 "Membrane expression of NKs was detected using the Nano-Glo® HiBiT extracellular detection system."]
  [PMID:37968728 "Signals were quite strong in cells expressing NK1 and NK2, but relatively weak in NK3, implying that either protein expression or membrane localization of NK3 was relatively low"]
- Rat brain: somatodendritic NK3R immunoreactivity; in spinal cord lamina II, dendritic
  spines, preterminal axons and axon terminals; on vasopressin neurons NK3R is
  membrane-bound and internalises after agonist.
  [PMID:8788251 "The expression of NKR was indicated on neuronal cell bodies and dendrites."]
  [PMID:9295096 "the immunolabeling in lamina II involved mainly dendritic spines inside glomeruli, preterminal axons and axon terminals"]
  [PMID:16357093 "Immunohistochemistry revealed that NK3Rs were membrane-bound on VP immunoreactive neurons in control rats."]
  These support the neuronal plasma-membrane subdomain IEA rows as non-core.
- Human sperm: NK3R protein detected by immunocytochemistry and western blot, but TACR3 mRNA
  not detected by RT-PCR; NK3R antagonist only partly blocked tachykinin-stimulated motility.
  [PMID:17437961 "The effects of tachykinins were antagonized by the NK(1) receptor-selective antagonist SR 140333, the NK(2) receptor-selective antagonist, SR 48968 and, to a lesser extent, also by the NK(3) receptor-selective antagonist SR 142801."]
  [PMID:17437961 "Immunocytochemistry studies showed expression of the NK(1), NK(2) and NK(3) tachykinin receptor proteins in spermatozoa with different major sites of localization for each receptor."]
  Abstract only; the midpiece site comes from the full text the curator read. Kept non-core.

## Physiology: GnRH/LH control (human genetics)

- Homozygous loss-of-function TACR3 mutations cause congenital gonadotropin deficiency and
  pubertal failure; patient missense receptors fail to signal.
  [PMID:19079066 "We report four human pedigrees with severe congenital gonadotropin deficiency and pubertal failure in which all affected individuals are homozygous for loss-of-function mutations in TAC3 (encoding Neurokinin B) or its receptor TACR3 (encoding NK3R)."]
  [PMID:19079066 "Thus, both the missense TACR3 mutations found in all affected subjects in Families 1 through 3 show unequivocal evidence of impaired receptor signaling."]
- Young et al. 2010: the defect is hypothalamic (pulsatile GnRH restores LH and sex
  steroids); very low LH.
  [PMID:20194706 "Our data demonstrate the hypothalamic origin of the gonadotropin deficiency in these genetic forms of normosmic CHH."]
  [PMID:20194706 "pulsatile GnRH administration normalized circulating sex steroids, LH release, and restored fertility in one subject"]
- Mouse arcuate Kiss1 (KNDy) neurons express Tacr3 (NK3); autosynaptic NKB model.
  [PMID:19776272 "we found that Kiss1 neurons in the Arc of female mice not only express the Dyn and NKB genes but also the NKB receptor gene (NK3)"]
  [PMID:19776272 "We propose a model whereby NKB and dynorphin act autosynaptically on kisspeptin neurons in the Arc to synchronize and shape the pulsatile secretion of kisspeptin and drive the release of GnRH from fibers in the median eminence."]
- Rat: chronic central NK3R antagonist delays puberty markers and the rise in LH pulse
  frequency. This is also the source of the rat "vagina development" IMP (vaginal opening is
  used there as a puberty marker).
  [PMID:24863620 "SB222200 significantly delayed the onset of vaginal opening and first oestrus (as markers of puberty) compared to controls in both normal and high-fat diet fed animals."]
  [PMID:24863620 "the increase in LH pulse frequency was delayed and that the LH pulse amplitude was reduced in response to NK3R antagonism"]
- Decision: GO:0033686 positive regulation of luteinizing hormone secretion is ACCEPTED as
  the main physiological process (human loss-of-function plus rodent antagonist data),
  following the MC4R precedent of including the physiological regulation term in the core
  function. GO:0060068 vagina development is MARK_AS_OVER_ANNOTATED: the receptor acts in the
  hypothalamus and vaginal opening is a downstream pubertal readout.

## Physiology: thermoregulation

- Rat MnPO: senktide lowers core temperature; NK3R-saporin ablation of MnPO NK3R neurons
  lowers tail-skin temperature and abolishes senktide hypothermia.
  [PMID:22028440 "Senktide microinfusion into the rat MnPO decreased core temperature in a dose-dependent manner."]
  [PMID:25825817 "These data show that NK3R neurons in the MnPO are required for the hypothermic effects of senktide but not for the E2 modulation of thermoregulation."]
- Human: NKB infusion induces flushing; NK3R antagonists reduce menopausal hot flushes
  (MLE4901 phase 2; fezolinetant phase 3).
  [PMID:25683060 "Our findings provide evidence that NKB administration can cause hot flushes in women."]
  [PMID:28385352 "MLE4901 significantly reduced the total weekly number of hot flushes by 45"]
  [PMID:36924778 "Compared with placebo, fezolinetant 30 mg and fezolinetant 45 mg significantly reduced the frequency of vasomotor symptoms at week 4"]
- The human site and circuit are unresolved.
  [PMID:25683060 "However, the central mechanisms through which sex steroid deficiency triggers flushing remain unclear."]
- Additional human evidence, added when this decision was revisited (see below): the flush
  is defined in the trial literature as effector activation, not a sensation only, the
  MLE4901 result was confirmed objectively by skin conductance, and a third antagonist
  replicates it.
  [PMID:28385352 "A hot flush is characterised by an intense feeling of heat, which often rises through the body, and intermittent activation of heat dissipation effectors, including peripheral cutaneous vasodilatation, sweating, and behavioural change, to reduce temperature."]
  [PMID:28385352 "The reported subjective effect of decreased flushes by MLE4901 was confirmed by objective measurement using the skin conductance monitor and detection algorithm software"]
  [PMID:39172446 "Elinzanetant significantly reduced VMS frequency at week 4"]
  Note elinzanetant is not NK3R-selective, so it supports the pathway rather than this
  receptor.
  [PMID:39172446 "To evaluate the efficacy and safety of elinzanetant, a selective neurokinin-1,3 receptor antagonist, for the treatment of moderate to severe menopausal vasomotor symptoms."]
- Decision, revised 2026-11-14: **NEW GO:0001659 temperature homeostasis** (EXP,
  PMID:28385352). The earlier decision here was "no NEW BP", on the ground that
  GO:0031653/GO:0031654/GO:0031656 carry no annotations in any species. That is still true,
  but it was an incomplete check: it looked only at the heat-dissipation subtree and not at
  their parent, GO:0001659 ("A homeostatic process in which an organism modulates its
  internal body temperature"), which is the term the corpus actually uses.
  - Comparator check (QuickGO, GO:0001659 exact, 2026-11-13). Human: 26 rows, **every one a
    transfer** (IEA, ISS, IBA or TAS), including the GPCRs ADORA1, DRD2, GRM5, HTR2A, MC5R
    and NTSR1 and the neuropeptides HCRT and NMU. Mouse: 42 rows, about twenty of them IMP
    (Drd1, Drd2, Trpv1, Mc5r, Nmu, Fto, Stat3, Nox3 ...). So the term is used for receptors
    of this kind; the human side is thin because human thermoregulation is rarely perturbed
    experimentally, not because curators decided against the term. There was also nothing to
    transfer: neither mouse nor rat Tacr3 carries a GO:0001659 row in GOA (the mouse one in
    this corpus is this project's own proposal).
  - Participation test: the receptor transduces the NKB signal onto the heat-loss circuit, so
    it performs a step in the regulatory process. Receptor blockade is evidence about *this*
    gene product, because the drug's target is the receptor.
  - Population caveat, carried on the row: the antagonist trials are in postmenopausal women,
    so they establish the receptor's role in the estrogen-deprived state. The eugonadal arm
    comes from the ligand side (NKB infusion in healthy premenopausal women) and from the
    rodent MnPO data; no human experiment has measured core temperature during NK3R agonism
    or blockade.
  - Evidence code: EXP. ECO classes assaying an organism's response to a receptor agonist or
    antagonist as pharmacological assay evidence (ECO:0006053), which sits under experimental
    phenotypic evidence, **not** under mutant-phenotype evidence (ECO:0000315, the IMP class
    -- its descendants cover mutation, RNAi, morpholino, antisense and over-expression, but no
    drug) and not under direct-assay evidence; the manual-assertion form resolves to EXP. GO's
    own IMP and IDA guidance pages could not be read from this environment
    (wiki.geneontology.org returns 403), so this is reasoning from ECO and not a verified
    consortium convention.
  - The human circuit is still undefined, so the BIOLOGY knowledge gap stays, with the two
    limits above added to its boundary.

## Rat pharmacology behind the Ensembl Compara IEA rows (source: rat Tacr3 P16177 GOA)

All are effects of central or local NK3 agonist (senktide / aminosenktide) injection in rat:
- positive regulation of heart rate, PMID:2471579 (NTS microinjection): "caused long-lasting hypertension and tachycardia".
- positive regulation of blood pressure, PMID:2478257 (ICV, partly vasopressin-dependent).
- regulation of dopamine metabolic process, PMID:8574643 (intranigral infusion).
- response to cocaine, PMID:17445241 (senktide potentiates cocaine responses).
- drinking behavior, PMID:9864063 and PMID:9392836 (alcohol intake in alcohol-preferring rats).
- regulation of feeding behavior, PMID:2462199 (salt appetite).
- conditioned place preference, PMID:9802842 (agonist evokes CPP).
- response to estradiol, PMID:10342838 (uterine Tacr3 mRNA falls with E2) and PMID:12390879.
- positive regulation of uterine smooth muscle contraction, PMID:12390879 (senktide contracts
  isolated rat uterus; a direct tissue effect).
Agonist pharmacology in rat with no loss-of-function or human data: MARK_AS_OVER_ANNOTATED,
except uterine contraction (direct tissue response, KEEP_AS_NON_CORE). Expression-based
"response to estradiol" is MARK_AS_OVER_ANNOTATED.

## Protein binding rows

- PMID:12716968 (endokinins; IntAct partners substance P/TAC1 chain and NKB) and PMID:23597562
  (an FGFR allosteric blocker paper whose abstract does not mention NK3R; the IntAct record
  with NKB is presumably from the full text). Both are receptor-ligand interactions already
  captured by the receptor-activity terms. REMOVE per the protein-binding policy; removal does
  not mean the interactions are false.

## PAINT / IBA

- `just paint-losses human TACR3`: no IRD or IKR on the lineage.
- PTN001544873: tachykinin receptor activity and plasma membrane, consistent.
- PTN002538240: sperm midpiece and positive regulation of flagellated sperm motility, seeded by
  the human NK1R/NK2R/NK3R annotations from PMID:17437961 (TACR3 legitimately appears in its own
  WITH/FROM). Kept non-core.
