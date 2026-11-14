# TAC3 (human, UniProtKB:Q9UHF0) review notes

Tachykinin-3 / preprotachykinin B, 121 aa, the precursor of the tachykinin decapeptide
neurokinin B (NKB, also called neuromedin K). PANTHER PTHR15536 (TACHYKININ-3),
InterPro IPR003635 (Neurokinin-B/TAC3) and IPR013055 (tachykinin C-terminal signature).

## Precursor and processing (UniProt record, sequence inspection)

- Signal peptide 1-16 (predicted), propeptides 17-78 and 94-121 (by similarity), mature
  NKB 81-90 (`DMHDFFVGLM`), C-terminal methionine amide (by similarity).
- The NKB decapeptide is flanked by Lys79-Arg80 and Gly91-Lys92-Arg93 in the displayed
  sequence, the usual dibasic convertase sites plus the glycine amide donor; UniProt
  keywords record "Cleavage on pair of basic residues" and "Amidation".
- Human placental cDNA encodes the 121-residue precursor giving a peptide identical to
  NKB of other mammals.
  [PMID:10866201 "we have cloned a complementary DNA from human placental messenger RNA encoding a precursor protein of 121 amino acids which gives rise to a mature peptide identical to the neuropeptide neurokinin B (NKB) of other mammalian species"]
- Isoforms: isoform 2 (alpha) changes only the C-terminal propeptide (VSP_013187,
  98-121) and keeps NKB. Isoform 3 (gamma, VSP_013186) replaces 80-98 by a single His,
  which removes the whole NKB sequence; from the sequence alone it cannot yield NKB.
  This is my inference from the UniProt VAR_SEQ features; no paper I read tested
  whether isoform 3 is translated or has a function.

## Molecular function: NK3R ligand

- NKB is the preferred endogenous ligand of NK3R (TACR3).
  [PMID:19079066 "encoding neurokinin B, the preferred ligand for the neurokinin-3 receptor"]
  [PMID:37391393 "Endogenous neurokinin B (NKB) is the most potent natural agonist of NK3R."]
- Cryo-EM structures of NK3R-Gq bound to NKB (Sun et al. 2023); receptor activation read
  out as IP-one accumulation (Gq/PLC).
  [PMID:37391393 "NKB preferentially activates NK3R coupled to the Gαq family of G proteins for intracellular signal transduction"]
  [PMID:37391393 "b IP-one accumulation assay of NK3R activation by NKB, SP, and senktide."]
- The amidated C-terminal Met is part of the receptor-engaging motif: the patient M90T
  peptide is about tenfold less potent at NK3R; non-amidated M90T is nearly inactive.
  [PMID:19079066 "The amidated mutant peptide (predicted to be the form that would occur in nature) had severely reduced activity, being around 10 fold less potent than amidated wild type NKB at stimulating the NK3R"]
- Rat NK3R in CHO cells: tachykinins stimulate both PI hydrolysis and (less efficiently)
  cAMP; this is the source of the cAMP ISS row (rat Tac3 RGD:3809 carries an IDA from
  this paper).
  [PMID:1370820 "The three receptors commonly showed a rapid and marked stimulation in both phosphatidylinositol (PI) hydrolysis and cyclic AMP formation in response to tachykinin interaction."]
  [PMID:1370820 "The stimulation of cyclic AMP formation was less efficient than that of PI hydrolysis"]
- MF term choice. GO:0048018 receptor ligand activity is the IDA row and the term both
  cached GO-CAMs (68d5ebd600000043, 68d5ebd600000736) use for TAC3, with TACR3 as the
  receptor (GO:0016498). GO:0160041 neuropeptide activity ("receptor ligand activity of
  any polypeptide expressed in, and secreted from a neuron") is its direct child and is
  used by curators for other human neuropeptide precursors (NPY, NPFF, NPS, NPVF, IDA in
  QuickGO, checked 2026-11-13). NKB is made by hypothalamic neurons (below), so I add
  GO:0160041 as NEW (IC) and keep GO:0048018 accepted; the two are compatible.
- GO:0005102 signaling receptor binding (TAS, 2003) is generic. Its GO definition says to
  also consider GO:0048018. Rat and mouse Tac3 carry GO:0031836 neuromedin K receptor
  binding, GO:0031837 substance K receptor binding and GO:1902093 (sperm motility) as ISO
  from human Q9UHF0 / its NKB chain, but human TAC3 no longer carries any of them
  (QuickGO, 2026-11-13); its current UniProt MF rows (2025) are GO:0048018 IDA. I do not
  know why the human rows went, so I do not reinstate them: I MODIFY GO:0005102 to the
  ligand term the current human annotation and both GO-CAMs use, GO:0048018. (The rodent
  ISO rows now point at a source that no longer exists; noted, not reviewed here.)

## Expression and localisation

- Secreted peptide (UniProt "Secreted"); acts on receptors in the extracellular space.
- Arcuate (infundibular) KNDy neurons co-express kisspeptin, dynorphin and NKB:
  - Sheep: [PMID:17823266 "Over three quarters of ARC kisspeptin neurons also expressed NKB, and a similar percentage of NKB neurons contained kisspeptin."]
  - Mouse: [PMID:19776272 "Kiss1 neurons in the Arc of female mice not only express the Dyn and NKB genes but also the NKB receptor gene (NK3)"]
  - Human autopsy: [PMID:20529119 "Dual-immunofluorescent studies established that 77% of kisspeptin-immunoreactive cells in the infundibular nucleus synthesize the tachykinin peptide neurokinin B"]
    and NKB is in kisspeptin axons: [PMID:20529119 "56 and 17% of kisspeptin fibers in the infundibular and periventricular nuclei, respectively, contained neurokinin B immunoreactivity"]
- Placenta: expression confined to the outer syncytiotrophoblast; NKB in maternal plasma
  from week 9, elevated in pregnancy-induced hypertension and pre-eclampsia.
  [PMID:10866201 "In human pregnancy, the expression of NKB was confined to the outer syncytiotrophoblast of the placenta, significant concentrations of NKB could be detected in plasma as early as week 9"]
- Sperm: TAC3 transcript detected by RT-PCR, and exogenous NKB increased progressive
  motility (abstract only).
  [PMID:17437961 "RT-PCR demonstrated expression of the genes that encode SP/NKA (TAC1), NKB (TAC3) and hHK-1 (TAC4)"]
  [PMID:17437961 "we found that substance P (SP), human hemokinin-1 (hHK-1), neurokinin A (NKA) and neurokinin B (NKB) produced concentration-dependent increases in sperm progressive motility"]

## Steroid regulation: rise after menopause / ovariectomy

- Human post-mortem in situ hybridisation (Rance & Young 1991): infundibular NKB neurons
  hypertrophy and NKB mRNA rises after menopause.
  [PMID:1708331 "the numbers of labeled neurons/tissue increased 6-fold (SP) and 15-fold (NKB) in the postmenopausal infundibular nucleus"]
  [PMID:1708331 "These data demonstrate that human menopause is associated with marked increases in hypothalamic NKB and SP gene expression."]
- Ovariectomised cynomolgus monkeys: estrogen (with or without progesterone) suppresses
  infundibular NKB expression, so the postmenopausal rise follows estrogen withdrawal.
  [PMID:10372719 "Both estrogen and estrogen plus progesterone treatments produced a marked suppression of the number of infundibular neurons expressing NKB gene transcripts."]
  [PMID:10372719 "These results provide strong support for the hypothesis that the increased NKB gene expression in the hypothalamus of postmenopausal women is secondary to estrogen withdrawal."]
- Mouse: arcuate NKB expression is inhibited by estradiol.
  [PMID:19776272 "We also found that expression of the Dyn, NKB, KOR, and NK3 in the Arc are inhibited by estradiol"]
- These are expression responses. I did not add any "response to estrogen" term: no row
  asks for one, and an expression change is not a function of the peptide.

## Reproduction: human genetics and animal models

- Homozygous TAC3 M90T (the C-terminal Met of NKB) in a consanguineous family with
  normosmic hypogonadotropic hypogonadism.
  [PMID:19079066 "All subjects who are in the second decade of life or older show unequivocal evidence of failure of pubertal progression with low circulating sex steroid levels and pre-pubertal levels of circulating gonadotropins."]
  [PMID:19079066 "These findings establish that NKB action via the NK3R is necessary for the central neuroendocrine control of human reproduction."]
- TAC3 splice-site deletion of NKB (Young 2010): very low LH with near-normal FSH,
  corrected by pulsatile GnRH, so the defect is hypothalamic.
  [PMID:20194706 "We demonstrated that these two mutations, respectively, deleted neurokinin B and truncated its receptor NK3R."]
  [PMID:20194706 "In several patients we observed a dissociation between the very low LH and normal or nearly normal FSH levels"]
  [PMID:20194706 "pulsatile GnRH administration normalized circulating sex steroids, LH release, and restored fertility in one subject"]
- Gianetti 2010: a TAC3 frameshift removing the decapeptide; frequent reversal in
  adulthood.
  [PMID:20332248 "In TAC3, one homozygous single base pair deletion was identified, resulting in complete loss of the neurokinin B decapeptide."]
  [PMID:20332248 "Although the neurokinin B pathway appears essential during early sexual development, its importance in sustaining the integrity of the hypothalamic-pituitary-gonadal axis appears attenuated over time."]
- Additional HH10 variant R80S at the processing site, in a patient also carrying an
  HS6ST1 mutation (UniProt, from PMID:23643382; cached, not read further).
- Mouse Tac2 (TAC3 orthologue) knockout: female delay of puberty, adult fertility retained.
  [PMID:25574869 "Tac2-/- females had profound delays in sexual maturation, with time to vaginal opening and first estrus occurring significantly later than controls"]
  The same paper suggests NKB can act through other tachykinin receptors when NK3R is absent.
  [PMID:25574869 "suggesting that in the absence of the NKB receptor, NKB may regulate the timing of sexual maturation through other tachykinin receptors."]
- Mechanistic model: NKB acts autosynaptically on KNDy neurons to pattern kisspeptin
  release and GnRH secretion.
  [PMID:19776272 "We propose a model whereby NKB and dynorphin act autosynaptically on kisspeptin neurons in the Arc to synchronize and shape the pulsatile secretion of kisspeptin and drive the release of GnRH from fibers in the median eminence."]
- Sign caveats: in rodents NKB can inhibit LH, and a 30-min NKB infusion in women did not
  change LH. The positive-regulation claim rests on human loss of function.
  [PMID:19776272 "confirmed that Dyn and NKB inhibit LH secretion"]
  [PMID:19079066 "Notably, central administration of a potent NK3R agonist to ovariectomized, oestrogen-primed rats suppressed LH production rather than stimulating it"]
  [PMID:25683060 "No significant changes in serum LH, FSH or estradiol were observed during the entire 30 minute NKB infusion period when compared with vehicle infusion period"]

### Ligand-side process terms: comparator check

- The question is whether a ligand gene gets "positive regulation of LH secretion" for a
  physiology performed by receptor-bearing cells. QuickGO, human, GO:0032276 regulation of
  gonadotropin secretion and descendants (2026-11-13): KISS1 GO:0033686 (IBA), NPVF
  GO:0032277 (IBA and IDA), INHA/INHBA/INHBB on FSH-secretion terms, LEP GO:0033686 (IEA),
  plus receptors (KISS1R, GNRHR, TACR3 IEA). So GO practice gives peptide hormones and
  neuropeptides their gonadotropin-secretion regulation terms; the regulation term names
  the regulator, which is the ligand. Human TAC3 loss of function gives low LH that
  pulsatile GnRH corrects. Decision: NEW GO:0033686 (IMP, PMID:20194706), matching the
  receptor review (TACR3 ACCEPTs GO:0033686) and KISS1.
- Not added: GnRH pulse generation itself (no GO term found for it, and the pacing is done
  by the KNDy network, not by the peptide), puberty / gonad development terms (downstream
  of gonadotropins), sperm motility (human TAC3 no longer carries it, see above; it is
  kept non-core on TACR3 only).

## Thermoregulation / hot flushes

- NKB infusion induces flushes in women.
  [PMID:25683060 "Our findings provide evidence that NKB administration can cause hot flushes in women."]
- Rat: ablating NK3-expressing arcuate KNDy neurons lowers tail-skin temperature (less
  cutaneous vasodilatation) and removes the estradiol effect.
  [PMID:23150555 "KNDy neuron ablation consistently reduced tail-skin temperature (T(SKIN)), indicating that KNDy neurons facilitate cutaneous vasodilatation, an important heat dissipation effector."]
- What the infusion study measured, beyond the symptom: skin temperature rose during the
  flush episodes and sternal skin conductance, an objective marker of sweating, rose with
  them, in healthy premenopausal women.
  [PMID:25683060 "In summary, our data shows that intravenous infusion of NKB acutely induces hot flushes in premenopausal healthy women."]
  [PMID:25683060 "Mean skin temperature increased significantly during flushing symptoms when compared with the pre-symptom period"]
  [PMID:25683060 "Concordant increases in sternal skin conductance (suggestive of sweating) were evident in six of the eight participants at the time of flushing during their NKB infusion"]
  And what it did not: nothing changed across the infusion as a whole, and core temperature
  was not measured (visits were scheduled in the follicular phase for its stability).
  [PMID:25683060 "overall mean levels of HR, MAP and skin temperature were similar between entire NKB and vehicle infusions in healthy women, which suggests that NKB per se does not affect these parameters"]
  [PMID:25683060 "All study visits were scheduled during days 3 to 10 of the menstrual cycle (follicular phase) when core body temperature is most stable."]
- Receptor-side requirement, from the trials of NK3R-selective antagonists in postmenopausal
  women. Evidence about the estrogen-deprived state, and about the receptor rather than the
  peptide, but it shows the pathway this peptide signals through is required for the
  episodes.
  [PMID:28385352 "MLE4901 significantly reduced the total weekly number of hot flushes by 45"]
  [PMID:36924778 "Compared with placebo, fezolinetant 30 mg and fezolinetant 45 mg significantly reduced the frequency of vasomotor symptoms at week 4"]
  The trial literature is also where the flush is defined as effector activation rather than
  a sensation only, which is what makes it a thermoregulatory process at all.
  [PMID:28385352 "A hot flush is characterised by an intense feeling of heat, which often rises through the body, and intermittent activation of heat dissipation effectors, including peripheral cutaneous vasodilatation, sweating, and behavioural change, to reduce temperature."]
- Decision, revised 2026-11-14, same revision as TACR3: **NEW GO:0001659 temperature
  homeostasis** (EXP, PMID:25683060). The earlier "no NEW BP" rested on the heat-dissipation
  terms having no annotations in any species, which is true and remains true, but only their
  parent was ever the usable term. GO:0001659 has 26 human rows and 42 mouse rows; the human
  rows are **all** transfers (IEA, ISS, IBA, TAS) and include the neuropeptides HCRT and NMU,
  while about twenty of the mouse rows are IMP (QuickGO, 2026-11-13). So the term is used for
  secreted neuropeptides, and the thin human side reflects the rarity of human
  thermoregulation experiments rather than a curator decision; nothing existed to transfer
  either, since neither rodent ortholog carries a GO:0001659 row in GOA. Participation test:
  the peptide is the signal acting on receptors in the thermoregulatory circuit. Evidence
  code EXP, on the ECO reasoning recorded in the TACR3 notes (ECO:0006053 pharmacological
  assay evidence is neither IMP's nor IDA's class, and resolves to EXP); IDA is also
  defensible here because the experiment administers the gene product itself, and GO's own
  guidance pages were unreachable from this environment.
  [PMID:25683060 "However, the central mechanisms through which sex steroid deficiency triggers flushing remain unclear."]
  The human circuit is still undefined, so the BIOLOGY knowledge gap stays, with the
  infusion study's two limits added to its boundary.

## Blood pressure and pregnancy rows

- IBA positive regulation of blood pressure (PTN002694376; donor rat Tac3 RGD:3809, IDA
  from PMID:2478257): ICV NK3 agonists raise blood pressure in rats, partly through
  vasopressin. Page 2000: supraphysiological plasma NKB is pressor in rats.
  [PMID:2478257 "senktide (suc-[Asp6,Me-Phe8]-substance P6-11) and [Pro7]-neurokinin B, into the lateral brain ventricle of the normotensive rats caused dose-dependent increases in the blood pressure"]
  [PMID:10866201 "In female rats, concentrations of NKB several-fold above that of an animal 20 days into pregnancy caused substantial pressor activity."]
  Agonist pharmacology, no loss-of-function or physiological evidence. MARK_AS_OVER_ANNOTATED,
  as the TACR3 review did for the receptor's rat-derived blood-pressure row.
  `just paint-losses human TAC3`: no IRD or IKR on the lineage.
- TAS female pregnancy (PMID:10866201): the paper shows placental expression and a
  correlation with pre-eclampsia, and proposes a pathological pressor role; it shows no
  function of NKB in pregnancy. MARK_AS_OVER_ANNOTATED.

## Protein binding rows

- HuRI (PMID:32296183) Y2H with PRB1 (A5D903) and an uncharacterised secreted protein
  (A0A087WZY1); Haenig 2020 (PMID:32814053) Y2H with JPH3 (an ER-plasma-membrane junction
  protein). Generic GO:0005515 is uninformative; the informative interaction (with
  TACR3) is captured by receptor ligand activity. REMOVE per the protein-binding policy;
  removal does not mean the interactions are false.
