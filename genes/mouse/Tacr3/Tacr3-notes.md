# Tacr3 (mouse, UniProtKB:P47937) review notes

Neuromedin-K receptor / neurokinin-3 receptor (NK3R), 452 aa, class A (rhodopsin-like)
GPCR of the tachykinin receptor subfamily (InterPro IPR001681 neurokinin receptor,
IPR001013 NK3-specific; PANTHER PTHR46925:SF1 NEUROMEDIN-K RECEPTOR). MGI:892968,
approved symbol `Tacr3` (synonym Tac3r). The preferred ligand is neurokinin B (NKB),
the product of mouse *Tac2* (the ortholog of human *TAC3*).

## Evidence landscape: every GOA row is a transfer

All 60 GOA rows are IEA, IBA, ISO or ISS. There is no IDA, IMP, IGI or IEP row on
mouse Tacr3, so no claim in the GOA file rests on an experiment done on the mouse
gene. The donors are rat Tacr3 (RGD:3810 / UniProtKB:P16177, via GO_REF:0000096
mouse-rat ISO and GO_REF:0000107 Ensembl Compara) and human TACR3 (UniProtKB:P29371,
via GO_REF:0000119 mouse-human ISO and GO_REF:0000107). Each row therefore has to be
judged on the donor's own evidence plus whatever mouse literature exists. A
substantial mouse literature does exist, and it is cited below; it is just not in GOA.

The mouse UniProt FUNCTION paragraph is itself an inference, `ECO:0000250|UniProtKB:P16177`
(rat), and the SUBCELLULAR LOCATION is `ECO:0000250|UniProtKB:P29371` (human). Quoting
it records what UniProt asserts by similarity, not a mouse measurement.

## Ligand selectivity and receptor activity (direct mouse evidence)

- The mouse receptor was cloned from brain and characterised pharmacologically:
  452 aa, 96% identical to rat and 86% to human NK3R; agonist binding affinities and
  functional potencies in HEK293 cells were similar for the mouse and human receptors.
  [PMID:11226387 "The murine NK(3) receptor has a predicted sequence of 452 amino acids, sharing 96% and 86% identity to the rat and human NK(3) receptors, respectively."]
  [PMID:11226387 "Binding affinities and functional potencies of tachykinin receptor agonists were similar in HEK (human embryonic kidney) 293 cells expressing murine NK(3) receptor and human NK(3) receptor, although substance P and neurokinin A were more potent stimulators of Ca(2+) mobilization in murine NK(3) receptor cells."]
  The Ca2+ readout is a Gq/PLC readout, so this is mouse-specific support for both
  GO:0016498 and GO:0007209.
- Species difference worth knowing before reading any antagonist experiment in mouse:
  NK3R-selective non-peptide antagonists bind the mouse receptor 10-100-fold worse
  than the human receptor.
  [PMID:11226387 "NK(3) receptor-selective antagonists from two structural classes, had 10- to 100-fold lower binding affinities for murine NK(3) receptor compared to human NK(3) receptor"]
  A later survey of cloned NKRs reaches the same conclusion for rodents generally.
  [PMID:19426690 "Two AA differences located close to the antagonist binding site of NK3R likely influence the NK3R antagonist potency, explaining the 3-10-fold decrease in potency observed for the rat NK3R."]
- Senktide, the agonist used in nearly all the rodent physiology below, is selective
  for this receptor subtype.
  [PMID:1662278 "senktide was found to be a highly selective and potent agonist for neuromedin K receptor"]
  Its selectivity *in mouse* is confirmed genetically: in NK3-receptor knockout mice
  the electrophysiological response to senktide is lost.
  [PMID:18690106 "Knockout of the receptor was confirmed by lack of NK3 protein and lack of electrophysiological responsivity of presumed dopaminergic neurons to senktide."]
- UniProt's (inferred) statement of ligand rank order and transduction:
  [file:mouse/Tacr3/Tacr3-uniprot.txt "The rank order of affinity of this receptor to tachykinins is: neuromedin-K > substance K > substance P"]
  [file:mouse/Tacr3/Tacr3-uniprot.txt "Neuromedin-K binding to its receptor triggers G protein-coupled receptor signaling via activation of G(q) and phosphatidylinositol hydrolysis by phospholipase C"]

## Gq coupling in native mouse neurons

In mouse arcuate Kiss1 (KNDy) neurons, high-frequency release of endogenous NKB
produces a slow EPSP that is blocked by an NK3R antagonist, occluded by senktide and
abolished by dialysing the cell with a GDP analogue, i.e. mediated by the Gq-coupled
receptor.
[PMID:27549338 "the slow EPSP was attenuated by the Tacr3 antagonist SB222,200 and occluded by the Tacr3 agonist senktide pretreatment, demonstrating that the slow EPSP was mediated by the Gq-coupled Tacr3"]
This is the strongest mouse evidence for GO:0007209 (PLC-activating tachykinin
receptor pathway) acting through the endogenous receptor in its own cells.

cAMP/adenylate cyclase (GO:0007189) has no mouse measurement. The donor is the rat
IDA in CHO cells, where cAMP was the weaker of the two outputs.
[PMID:1370820 "The stimulation of cyclic AMP formation was less efficient than that of PI hydrolysis"]
UniProt carries the mouse statement by similarity only.
[file:mouse/Tacr3/Tacr3-uniprot.txt "Neuromedin-K binding also triggers signaling via activation of adenylate cyclase activity which results in increased intracellular levels of cyclic AMP (cAMP)"]
Decision: GO:0007209 ACCEPT (core), GO:0007189 KEEP_AS_NON_CORE, as in the human review.

## Localisation

- UniProt: cell membrane (by similarity to human), multi-pass.
  [file:mouse/Tacr3/Tacr3-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane"]
  [file:mouse/Tacr3/Tacr3-uniprot.txt "Multi-pass membrane protein"]
- The neuronal subdomain rows (dendrite membrane, dendritic spine membrane and head,
  neuronal cell body and its membrane, axon terminus) are all rat IDA transfers:
  [PMID:8788251 "The expression of NKR was indicated on neuronal cell bodies and dendrites."]
  [PMID:9295096 "the immunolabeling in lamina II involved mainly dendritic spines inside glomeruli, preterminal axons and axon terminals"]
  [PMID:16357093 "NK3Rs were membrane-bound on VP immunoreactive neurons in control rats"]
  Mouse work is consistent with a somatodendritic neuronal receptor: *Tacr3*-EGFP
  reporter mice label preoptic NK3R neurons whose transmitter phenotype was typed by
  RNAscope, and NK3R-antibody staining is absent in NK3R-knockout tissue.
  [PMID:30753503 "In the MnPO, 94% of NK3R neurons were glutamatergic, but in the adjacent medial preoptic area, 97% of NK3R neurons were GABAergic."]
  [PMID:30565563 "(A) Complete absence of staining in the ARC of an OVX NK3R KO female mouse."]
  Kept as non-core subdomains of the plasma membrane, as in the human review.
- Sperm midpiece: the donor is the human study, which detected NK1/NK2/NK3 receptor
  *protein* on human spermatozoa.
  [PMID:17437961 "Immunocytochemistry studies showed expression of the NK(1), NK(2) and NK(3) tachykinin receptor proteins in spermatozoa with different major sites of localization for each receptor."]
  The only study of mouse sperm looked for the transcripts and found only *Tacr2*:
  [PMID:12773411 "A low-abundance transcript corresponding to the NK2 receptor was the only target gene detected in mice sperm."]
  So there is no mouse support, and the one mouse experiment that addressed it is
  negative (for mRNA; mouse sperm protein has not been examined). Mouse rows for
  GO:0097225 and GO:1902093 are MARK_AS_OVER_ANNOTATED, where the human review kept
  them as non-core on its own IDA/IMP. This is a deliberate human/mouse divergence.

## Physiology: the KNDy/GnRH pulse generator (where the mouse evidence is strongest)

- Arcuate Kiss1 neurons co-express NKB, dynorphin and this receptor.
  [PMID:19776272 "Kiss1 neurons in the Arc of female mice not only express the Dyn and NKB genes but also the NKB receptor gene (NK3)"]
  [PMID:21914775 "KNDy neurons express Tacr3, whereas GnRH neurons do not"]
- Receptor activation excites those neurons and raises gonadotropins:
  [PMID:21914775 "senktide, an agonist for the NKB receptor (neurokinin 3 receptor, encoded by Tacr3), stimulates gonadotropin secretion"]
  [PMID:21914775 "senktide activates KNDy neurons but has no discernable effect on GnRH neurons"]
  [PMID:23744642 "The neurokinin 3 receptor (NK3R) agonist senktide increased action potential firing activity of KNDy neurons."]
  [PMID:23744641 "Both NKB and Senktide, a neurokinin 3 receptor agonist, exerted a potent stimulatory action on ∼95% of ARN kisspeptin neurons."]
  Note the caveat from the same study: endogenous NKB recruits all three tachykinin
  receptors, not NK3R alone.
  [PMID:23744641 "the activation of kisspeptin neurons by NKB was only blocked completely by a cocktail of antagonists against all 3 tachykinin receptors"]
- Loss of function in mouse is milder than in human but not silent. *Tacr3*-null mice
  reach puberty and are fertile, yet have central reproductive defects:
  [PMID:22253416 "Tacr3(-/-) mice demonstrated normal timing of preputial separation and day of first estrus, markers of sexual maturation."]
  [PMID:22253416 "Tacr3(-/-) males had significantly smaller testes and lower FSH levels than their wild-type littermates"]
  [PMID:22253416 "Tacr3(-/-) females had lower uterine weights and abnormal estrous cyclicity."]
  [PMID:22253416 "although capable of fertility, Tacr3-deficient mice have central reproductive defects"]
  Redundancy with the other tachykinin systems is the accepted explanation; removing
  all tachykinin ligands is far more severe than removing NKB signalling alone.
  [PMID:32512561 "females did not show signs of puberty onset (first estrus) within 45 days after vaginal opening, they displayed a low frequency (but normal amplitude) of LH pulses, and 80% of them remained infertile"]
- Direction is context dependent, which matters for how firmly GO:0033686 can be read.
  An NK3R antagonist blocks the oestradiol-induced LH surge in female mice:
  [PMID:32512561 "Both antagonists individually were able to block the LH surge"]
  but in gonad-intact males the *knockout* has faster, larger basal LH pulses:
  [PMID:33839770 "we document an increase in basal frequency and amplitude of luteinizing hormone (LH) pulses in intact male mice deficient in substance P, neurokinin A (NKA) signaling (Tac1KO), and NKB signaling (Tac2KO and Tacr3KO)"]
  and without oestradiol NKB inhibits LH release:
  [PMID:30565563 "the stimulatory action of NKB is dependent on circulating estrogen (E2) levels, without which, NKB inhibits luteinizing hormone (LH) release"]
  Decision: GO:0033686 ACCEPT (as in human), with the sign caveat recorded in the row.
  No negative-regulation term is proposed: the inhibitory arm is a property of the
  circuit's steroid state rather than a separate receptor function, and GO:0033686 is
  what the agonist and surge-blockade experiments support.
- A second, kisspeptin-independent LH-stimulating site exists in mouse:
  [PMID:30565563 "in the presence of E2, NKB signaling induces LH release in a kisspeptin-independent manner through the activation of NK3R (NKB receptor) neurons in the posterodorsal medial amygdala (MePD)"]

## Physiology: thermoregulation (mouse-specific, and the basis of a NEW row)

- A selective NK3R agonist given to unrestrained mice reproduces the vasomotor
  episode: core temperature falls, tail skin temperature rises, the animals seek cold,
  and Fos appears in the median preoptic area.
  [PMID:28531316 "Following both treatments, the mice exhibited a VMS-like response characterized by a drop in core body temperature and cold-seeking behavior on the thermocline."]
  [PMID:28531316 "Senktide also caused a rise in tail skin temperature and increased Fos expression in the median preoptic area, a hypothalamic temperature control center."]
- The NK3R-expressing population was defined in mouse with a *Tacr3* reporter and is
  required for normal core temperature; it is glutamatergic and is not itself a
  warm-sensing population.
  [PMID:30753503 "Loss of MnPO NK3R neurons increased the core temperature (TCORE) during the light phase, with the frequency distributions indicating a regulated shift in the balance point."]
  [PMID:30753503 "Thus, NK3R neurons in the MnPO are glutamatergic and play a role in reducing TCORE but are not activated by warm thermal stimuli (internal or external)."]
- The endogenous circuit was closed in mouse: activating arcuate Kiss1 neurons raises
  tail-skin temperature, and infusing neurokinin receptor antagonists into the preoptic
  area beforehand prevents it (a three-antagonist cocktail, so not NK3R-specific).
  [PMID:29996088 "Infusion of this antagonist cocktail 30 min prior to chemogenetic activation of Kiss1ARH neurons prevented the increase in tail-skin temperature"]
- Term choice: GO:0001659 temperature homeostasis ("A homeostatic process in which an
  organism modulates its internal body temperature"). GO:0031653 heat dissipation and
  GO:0031654 regulation of heat dissipation would be closer to the phenotype but have
  zero mouse annotations, whereas GO:0001659 has several hundred, including GPCRs
  annotated from rodent perturbation data (Drd1, Drd2, Htr2a, Grm5, Ntsr1, Adora1,
  Cckar, Mc5r). So the comparator check supports a receptor in a thermoregulatory
  circuit carrying GO:0001659.
- Why this is a NEW row while the rat behavioural rows are marked over-annotated: the
  rat rows rest on a single agonist injection with no identification of the receptor's
  cell population and no mouse data, whereas here the *Tacr3*-expressing population is
  mapped in mouse, its removal shifts core temperature, systemic selective agonist
  reproduces the response in mouse, and the endogenous NKB projection is sufficient.

## Rat agonist pharmacology behind the transferred behaviour rows

All of these are rat rows (IDA/IMP from local or central senktide injection) reaching
mouse through GO_REF:0000096 and GO_REF:0000107, with no mouse counterpart:
- positive regulation of heart rate [PMID:2471579 "senktide, a selective neurokinin B receptor peptide) into the NTS caused long-lasting hypertension and tachycardia"]
- positive regulation of blood pressure [PMID:2478257 "senktide (suc-[Asp6,Me-Phe8]-substance P6-11) and [Pro7]-neurokinin B, into the lateral brain ventricle of the normotensive rats caused dose-dependent increases in the blood pressure"]
- response to cocaine [PMID:17445241 "cocaine-induced (5 and 10 mg/kg i.p.) hyperactivity was potentiated by senktide"]
- drinking behavior [PMID:9392836 "TK NK-3, but not NK-1, receptor agonists selectively inhibit ethanol intake in alcohol-preferring rats"]
- regulation of feeding behavior [PMID:2462199 "it potently inhibited salt appetite induced by sodium depletion in rats"]
- conditioned place preference [PMID:9802842 "the same i.c.v. dose of NH2-SENK evoked a pronounced and statistically significant CPP"]
These stay MARK_AS_OVER_ANNOTATED, as in the human review.

Dopamine is the one of these with mouse genetic data, so it is treated differently
here (KEEP_AS_NON_CORE rather than MARK_AS_OVER_ANNOTATED): the rat IDA is a direct
demonstration that receptor activation changes striatal dopamine metabolism, and in
mouse the knockout loses senktide responsivity of dopaminergic neurons and shows
small changes in the dopamine system.
[PMID:8574643 "Continuous intranigral infusion of the neurokinin-3 receptor agonist senktide selectively increased striatal dopamine metabolism"]
[PMID:18690106 "A small decrease in D1 receptor binding was seen in the dorsal striatum and olfactory tubercle, and a small decrease of in tyrosine hydroxylase in the olfactory tubercle, but no change was seen in D2 receptor binding."]
The authors' own hedge is recorded in the row:
[PMID:18690106 "the lack of robust changes indicates that the sensitivity to dopamine may be activity-dependent or benign in nature"]

## Uterus: the clearest mouse-versus-rat divergence

In rat, senktide contracts isolated uterus through NK3R, which is why the human review
kept GO:0070474 as a genuine peripheral non-core function.
[PMID:12390879 "The receptors for neurokinin 1 (NK1-R), neurokinin 2 (NK2-R), and neurokinin 3 (NK3-R) are expressed and functionally active in the uterus, promoting strong contractions of the myometrium."]
In mouse, uterotonic responses are mediated by NK1R (non-pregnant) and NK2R (late
pregnant), and the NK3 receptor is barely expressed except in dioestrus, with its role
explicitly unresolved:
[PMID:15647454 "The tachykinin NK3 receptor is expressed in considerable amounts only in uteri from nonpregnant diestrous animals, and its physiological significance remains to be clarified."]
[PMID:15647454 "The tachykinin NK2 receptor is predominant in the late pregnant mouse and is the main receptor mediating uterotonic responses to tachykinins at late pregnancy."]
So both uterine-contraction rows (GO:0070474, and the ARBA parent GO:0070472 which is a
mouse-only row) are MARK_AS_OVER_ANNOTATED for mouse.

"response to estradiol" (GO:0032355) does have independent mouse support, but of the
same kind as the rat donor: oestradiol lowers *Tacr3* expression.
[PMID:19627578 "The present data show that E2 strongly reduces Tacr3 expression in uteri from ovariectomized mice."]
[PMID:19776272 "We also found that expression of the Dyn, NKB, KOR, and NK3 in the Arc are inhibited by estradiol, as has been established for Kiss1"]
That makes the receptor a target of oestradiol-dependent transcriptional regulation,
not a participant in a response-to-oestradiol process, so the row stays
MARK_AS_OVER_ANNOTATED as in the human review.

## Vagina development (GO:0060068): removed in mouse

The donor is a rat antagonist study in which vaginal opening was used as a marker of
puberty timing:
[PMID:24863620 "SB222200 significantly delayed the onset of vaginal opening and first oestrus (as markers of puberty) compared to controls in both normal and high-fat diet fed animals."]
The receptor acts in the hypothalamus, so this is a readout of central pubertal timing
rather than participation in vaginal morphogenesis — the human review called that
over-annotation. In mouse the transferred claim is additionally contradicted by the
null's own phenotype: *Tacr3*-null mice have normal timing of the sexual-maturation
markers [PMID:22253416], and even mice lacking all tachykinin ligands open the vagina
on time [PMID:32512561 "female Tac1/Tac2KO mice presented normal time of VO but absence of first estrus, unlike the single KO models"]. Hence REMOVE here, against
MARK_AS_OVER_ANNOTATED in the human review.

## Negative results in mouse

Worth recording so they are not re-derived: NK3-receptor-deficient mice mount a normal
allergic pulmonary response.
[PMID:15501700 "There was no difference in the magnitude of these allergic inflammatory pulmonary responses between NK3-/- and NK3+/+ mice."]

## Leads not turned into annotations

- Learning and memory. A dedicated knockout study reports deficits in passive-avoidance
  retention, acquisition of conditioned avoidance responding and the Morris water maze.
  [PMID:17558564 "However, in several cognition tests, including passive avoidance, acquisition of conditioned avoidance responding (CAR), and the Morris water maze, NK3 knockout mice displayed deficits compared to wild-type mice."]
  Mouse *Tacr1* carries GO:0007611 (by ISO from rat), so the term is used for this
  family. Not proposed here: the cache is abstract-only, the second independent
  knockout line tested locomotion rather than cognition, and a behavioural deficit in a
  receptor knockout is the kind of system-level readout the NEW rules ask to keep out.
  It is a reasonable candidate for a curator with the full text.
- Positive regulation of FSH secretion (GO:0046881). *Tacr3*-null males have lower FSH
  [PMID:22253416], which parallels the LH claim. Not proposed: the comparator check
  argues against it. The nine mouse annotations to GO:0046881 are activin/inhibin-axis
  genes (Inhbb, Acvr2a, Foxl2, Smad4, Lep), and no gene of the hypothalamic KNDy axis
  carries it — mouse *Kiss1* carries GO:0033686 (LH) and nothing for FSH, and
  *Kiss1r*, *Tac2* and *Gnrh1* carry neither. That is a convention, not a gap.

## PAINT / IBA

- `just paint-losses mouse Tacr3`: no IRD or IKR loss on this gene's lineage.
- PTN001544873 (tachykinin receptor activity, plasma membrane): seeded by the three
  mammalian tachykinin receptors plus zebrafish members; mouse Tacr3 sits inside that
  clade and the claim is directly supported in mouse by PMID:11226387. Accepted.
- PTN002538240 (sperm midpiece, positive regulation of flagellated sperm motility):
  seeded by the human NK1R/NK2R/NK3R annotations from PMID:17437961. Descent is not in
  question; the tissue claim does not carry to mouse (see Localisation above).
