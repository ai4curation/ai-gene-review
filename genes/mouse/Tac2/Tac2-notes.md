# Tac2 (mouse, UniProtKB:P55099) review notes

Preprotachykinin-B / tachykinin-3, 116 aa, the precursor of the tachykinin decapeptide
neurokinin B (NKB, neuromedin K). InterPro IPR003635 (Neurokinin-B/TAC3) and IPR013055
(tachykinin C-terminal signature); PANTHER PTHR15536:SF1 (TACHYKININ-3). The receptor
is NK3R, the product of mouse *Tacr3*.

## Gene symbol: MGI says Tac2, UniProt says Tac3

UniProt's primary gene name for P55099 is `Tac3` with `Tac2` as a synonym
[file:mouse/Tac2/Tac2-uniprot.txt "GN   Name=Tac3; Synonyms=Nknb, Tac2;"], and QuickGO
therefore labels the GOA rows `Tac3`. The MGI-approved symbol is `Tac2`: the UniProt
record's own MGI cross-reference gives it
[file:mouse/Tac2/Tac2-uniprot.txt "DR   MGI; MGI:98476; Tac2."], and the Alliance/MGI
record for MGI:98476 returns symbol `Tac2`, name "tachykinin 2" (Alliance API, checked
2026-11-13). The mouse literature uses *Tac2* throughout (Tac2KO, Tac1/Tac2KO), so this
review uses `Tac2` as the symbol and folder name. Fetched by accession
(`just fetch-gene mouse Tac2 --uniprot-id P55099`) so the files are certainly P55099.

## The peptide

- Signal peptide 1-20 (predicted), propeptides 21-79 and 95-116, mature NKB 82-91, with
  a C-terminal methionine amide
  [file:mouse/Tac2/Tac2-uniprot.txt "FT   MOD_RES         91"]
  [file:mouse/Tac2/Tac2-uniprot.txt "/note=\"Methionine amide\""].
  The decapeptide is flanked by Lys80-Arg81 and Gly92-Lys93-Arg94 — the usual dibasic
  convertase sites plus the glycine amide donor — and the record carries the keywords
  "Cleavage on pair of basic residues" and "Amidation".
- **The mouse and human decapeptides are identical.** Mouse residues 82-91 and human
  residues 81-90 are both `DMHDFFVGLM`
  [file:mouse/Tac2/Tac2-uniprot.txt "LLKVLSKASV GPKETSLPQK RDMHDFFVGL MGKRNSQPDT"]
  [file:human/TAC3/TAC3-uniprot.txt "LKALSQASTD PKESTSPEKR DMHDFFVGLM GKRSVQPDSP"].
  This is my inference from inspecting the two sequence records. It matters for this
  review: the ligand is the same molecule in both species, so differences between mouse
  and human phenotypes are differences in the circuits and receptors the peptide acts
  on, not in the peptide.
- Protein existence is `PE   3: Inferred from homology`, and both UniProt FUNCTION
  paragraphs are inferences (`ECO:0000250|UniProtKB:P08435` from rat,
  `ECO:0000250|UniProtKB:Q9UHF0` from human). Quoting them records what UniProt asserts
  by similarity, not a mouse measurement.
  [file:mouse/Tac2/Tac2-uniprot.txt "Is a ligand for TACR3, and triggers G protein-coupled receptor signaling via activation of G(q) and phosphatidylinositol hydrolysis by phospholipase C (By similarity)"]

## Evidence landscape: every GOA row is a transfer

All 15 GOA rows are IEA, ISO or IBA. There is no IDA, IMP, IGI or IEP row on mouse Tac2,
so no claim in the GOA file rests on an experiment done on the mouse gene. The donors are
human TAC3 (UniProtKB:Q9UHF0, via GO_REF:0000119 mouse-human ISO and GO_REF:0000107
Ensembl Compara), rat Tac3 (RGD:3809, via GO_REF:0000096), InterPro IPR003635, and one
PAINT node (PTN002694376). As on mouse *Tacr3*, a large mouse literature exists and is
cited below; it is simply not in GOA.

### Three ISO rows cite a human annotation that no longer exists

GO:0031836 (neuromedin K receptor binding), GO:0031837 (substance K receptor binding) and
GO:1902093 (positive regulation of flagellated sperm motility) are ISO rows whose
WITH/FROM is `UniProtKB:Q9UHF0`, but human TAC3 carries none of those three terms today
(QuickGO, Q9UHF0, 2026-11-13: its current MF rows are GO:0005102 TAS, GO:0005515 IPI and
GO:0048018 IDA). Rat Tac3 has the same three rows, as ISO from Q9UHF0 and its NKB chain
`Q9UHF0-PRO_0000033566`, and that chain identifier returns no annotations at all. So the
donor side of these transfers has gone. I could not establish why, so — as the human TAC3
review decided for the mirror-image observation — I do not treat it as a source defect and
I judge each row on its own claim plus the mouse evidence. Two of the three claims hold in
mouse on independent grounds (below); the sperm one does not.

## Molecular function: the NK3R ligand

- The mouse receptor was cloned and characterised pharmacologically, and the mouse and
  human receptors respond similarly to tachykinin agonists in HEK293 cells, read out as
  Ca2+ mobilisation (a Gq/PLC readout).
  [PMID:11226387 "Binding affinities and functional potencies of tachykinin receptor agonists were similar in HEK (human embryonic kidney) 293 cells expressing murine NK(3) receptor and human NK(3) receptor"]
- Applied NKB excites mouse arcuate kisspeptin neurons, the cells that make it.
  [PMID:23744641 "Both NKB and Senktide, a neurokinin 3 receptor agonist, exerted a potent stimulatory action on"]
  (∼95% of ARN kisspeptin neurons, in the male mouse.)
- **Endogenous mouse NKB, released by the neurons' own action potentials, activates NK3R.**
  High-frequency photoactivation of Kiss1 neurons releases NKB, which produces a slow EPSP
  in neighbouring Kiss1 neurons; the EPSP is blocked by an NK3R antagonist, occluded by
  senktide, and so is mediated by the Gq-coupled receptor.
  [PMID:27549338 "High-frequency photostimulation of Kiss1 neurons in the ARH releases NKB that depolarizes and recruits other Kiss1ARH neurons."]
  [PMID:27549338 "the slow EPSP was attenuated by the Tacr3 antagonist SB222,200 and occluded by the Tacr3 agonist senktide pretreatment, demonstrating that the slow EPSP was mediated by the Gq-coupled Tacr3"]
  This is the strongest mouse evidence for the ligand's molecular function and for
  GO:0007209, because the peptide is the endogenous one and it is acting in its own tissue.
- Human structural and signalling data on the same decapeptide: cryo-EM of NKB-bound
  NK3R-Gq, with NKB the most potent natural agonist.
  [PMID:37391393 "Endogenous neurokinin B (NKB) is the most potent natural agonist of NK3R."]
  Used as cross-species support only; mouse has no structure.
- MF term choice: GO:0048018 receptor ligand activity (two GOA rows) is the core term, as
  in the human TAC3 review, with the receptor activity kept on *Tacr3* (GO:0016498).
  GO:0031836 neuromedin K receptor binding is kept as well: unlike bare GO:0005515 it names
  the receptor, so it is informative, and the claim is independently supported in mouse by
  the slow-EPSP and agonist experiments above.

### NKB is not an NK3R-only ligand in the mouse

This is the mouse-specific point that governs several rows. NKB's excitation of arcuate
kisspeptin neurons is **not** abolished by NK3R antagonists alone:
[PMID:23744641 "the activation of kisspeptin neurons by NKB was only blocked completely by a cocktail of antagonists against all 3 tachykinin receptors"]
[PMID:23744641 "Whole-cell recordings revealed that individual kisspeptin neurons were activated directly by all 3 tachykinins substance, P, neurokinin A, and NKB."]
The same three-antagonist cocktail is needed to abrogate the endogenous slow EPSP
[PMID:27549338 "(A–C) The slow EPSP was abrogated by an NKB receptor (Tacr3) antagonist SB222,200 (A) and the NKB receptor antagonist cocktail SDZ-NKT 343 (1 µM), GR94,800 (1 µM) and SB222,200 (3 µM) (Tacr1, 2 and 3 antagonists, respectively) (B)."],
the Kiss1-neuron thermoregulatory experiment used a cocktail for the stated reason that
NKB has affinity for all three
[PMID:29996088 "Because there are three neurokinin receptors (NK1R, NK2R, and NK3R), and NkB has some affinity for all of them, we infused a cocktail of antagonists for all three"],
and the ligand-versus-receptor knockout comparison points the same way
[PMID:25574869 "suggesting that in the absence of the NKB receptor, NKB may regulate the timing of sexual maturation through other tachykinin receptors."].
So GO:0031837 substance K receptor binding (NK2R) is a defensible non-core claim in mouse,
where its human donor row has gone. Note what the evidence is: receptor-antagonist
pharmacology in native tissue, not a mouse binding assay.

## Localisation

Secreted peptide [file:mouse/Tac2/Tac2-uniprot.txt "SUBCELLULAR LOCATION: Secreted."],
acting on cell-surface receptors from the extracellular side — which is what the
photostimulation experiment shows directly, since the peptide crosses from one neuron's
terminals to another's receptors. All three GO:0005576 rows (two `located_in`, one
`is_active_in`) are accepted, as in the human review.

## Physiology: the KNDy network and gonadotropin secretion

- Mouse arcuate Kiss1 neurons co-express NKB, dynorphin and NK3R, and all four transcripts
  are oestradiol-inhibited.
  [PMID:19776272 "Kiss1 neurons in the Arc of female mice not only express the Dyn and NKB genes but also the NKB receptor gene (NK3)"]
  [PMID:19776272 "We also found that expression of the Dyn, NKB, KOR, and NK3 in the Arc are inhibited by estradiol"]
- *Tac2* and *Tacr3* transcripts rise across puberty, and *Tac2* is less sensitive than
  *Kiss1* to steroid negative feedback; but an NK3R antagonist did not block pubertal onset,
  so rising NKB signalling is a marker rather than a trigger in the mouse.
  [PMID:22893725 "levels of Tac2 mRNA, encoding NKB, and its receptor (NK3R; encoded by Tacr3) increased as a function of puberty in both wild-type and hpg mice"]
- What the endogenous peptide does in the network: it synchronises the arcuate Kiss1
  population, which is the drive onto GnRH neurons.
  [PMID:27549338 "We discovered that high-frequency photoactivation of Kiss1ARH neurons induced a NKB-mediated slow excitatory postsynaptic potential (EPSP), which was modulated by co-released dynorphin, and caused synchronization of Kiss1ARH neurons."]
  [PMID:27549338 "Therefore, our findings provide the first evidence that Kiss1ARH neurons can synchronize via NKB/Dyn auto-excitation/inhibition to provide an excitatory drive (via Kiss1AVPV/PeN neurons) to GnRH neurons for stimulating GnRH neuronal activity and subsequent GnRH release."]
- Receptor-side confirmation that this output is gonadotropin secretion:
  [PMID:21914775 "senktide, an agonist for the NKB receptor (neurokinin 3 receptor, encoded by Tacr3), stimulates gonadotropin secretion"]
- Loss of function in the mouse is mild and sex-specific. *Tac2*-null females have delayed
  sexual maturation and recover; males are unaffected.
  [PMID:25574869 "Tac2-/- females had profound delays in sexual maturation, with time to vaginal opening and first estrus occurring significantly later than controls"]
  [PMID:25574869 "Male Tac2-/- mice showed no difference in the timing of sexual maturation or fertility compared with wild-type littermates and were fertile."]
- Removing the ligand matters most for the preovulatory surge, and the single knockouts are
  partly compensated by each other.
  [PMID:32512561 "Interestingly, Tac1KO and Tac2KO mice presented a trend to smaller increases in LH release (LH surge) than controls."]
  [PMID:32512561 "The absence of one of the tachykinin systems reduces the magnitude of the LH surge"]
  [PMID:32512561 "females did not show signs of puberty onset (first estrus) within 45 days after vaginal opening, they displayed a low frequency (but normal amplitude) of LH pulses, and 80% of them remained infertile"]
  Acute receptor blockade in wild-type females, which removes endogenous NKB signalling
  without a lifetime of compensation, blocks the surge outright:
  [PMID:32512561 "Both antagonists individually were able to block the LH surge"]
  The attribution of the double knockout's ligand loss to NKB rather than to NKA/SP on the
  Kiss1 neurons themselves is helped by the fact that *Tac1* is not expressed in those
  neurons:
  [PMID:32512561 "Because Tac1 is not expressed in Kiss1 neurons but upstream of these"]
- **Sign caveat, recorded on the row rather than hidden.** In gonad-intact males, deleting
  the ligand *raises* basal LH pulse frequency and amplitude:
  [PMID:33839770 "we document an increase in basal frequency and amplitude of luteinizing hormone (LH) pulses in intact male mice deficient in substance P, neurokinin A (NKA) signaling (Tac1KO), and NKB signaling (Tac2KO and Tacr3KO)"]
  and in the absence of oestrogen NK3R activation suppresses LH rather than stimulating it
  (mouse Tacr3 review, PMID:30565563). So the positive direction rests on the ligand- and
  antagonist-based surge experiments and the agonist data, not on basal pulsatility.

### Comparator check for the gonadotropin term

QuickGO, 2026-11-13: mouse *Kiss1* (Q6Y4S4), the other KNDy ligand, carries GO:0033686
positive regulation of luteinizing hormone secretion (IBA and ISO) and GO:0032278; mouse
*Tacr3* carries GO:0033686 (ISO and IEA from rat). So GO does put the LH-secretion
regulation term on the KNDy **ligand** as well as the receptor in mouse. Participation: the
peptide is the signalling molecule that performs the synchronising step on NK3R, so it does
part of the work rather than merely being required. Decision: NEW GO:0033686.

Not proposed: GO:0046881 positive regulation of FSH secretion (the mouse annotations to it
are activin/inhibin-axis genes, not the KNDy axis — the same convention argument as in the
*Tacr3* review), and no puberty or gonad-development term (those are downstream of
gonadotropins, and the mouse null reaches puberty).

## Physiology: thermoregulation

- Activating the arcuate Kiss1 neurons — the cells whose tachykinin is NKB — reproduces the
  vasomotor response in mouse, and the response needs neurokinin receptors in the preoptic
  area.
  [PMID:29996088 "Activation of ChR2 in Kiss1ARH-neuron fibers in the POA also increased tail-skin temperature"]
  [PMID:29996088 "Infusion of this antagonist cocktail 30 min prior to chemogenetic activation of Kiss1ARH neurons prevented the increase in tail-skin temperature"]
  The cocktail is the honest limit of this experiment: it blocks all three tachykinin
  receptors, for the stated reason that NKB binds all three. It does establish that a
  tachykinin released by these neurons carries the signal, and *Tac1* is not expressed in
  them (PMID:32512561, above).
- Receptor-side support in mouse: a selective NK3R agonist reproduces the episode, and the
  receptor-expressing preoptic population is required for normal core temperature.
  [PMID:28531316 "Following both treatments, the mice exhibited a VMS-like response characterized by a drop in core body temperature and cold-seeking behavior on the thermocline."]
  [PMID:30753503 "Loss of MnPO NK3R neurons increased the core temperature (TCORE) during the light phase, with the frequency distributions indicating a regulated shift in the balance point."]
- Term choice: GO:0001659 temperature homeostasis ("A homeostatic process in which an
  organism modulates its internal body temperature"), the term the companion *Tacr3* review
  used, and the term the mouse corpus uses for this kind of claim — 42 mouse rows, many IMP
  from perturbation data (Drd1, Drd2, Trpv1, Mc5r, Nmu, Fto), against **zero** annotations
  in any species for GO:0031653 heat dissipation, GO:0031654 and GO:0031656 (QuickGO,
  2026-11-13). Decision: NEW GO:0001659 on the ligand, with the cocktail limitation stated
  in the row and the remaining gap recorded as a knowledge gap.

## Blood pressure and sperm rows

- GO:0045777 positive regulation of blood pressure arrives twice, as an IBA from
  PTN002694376 and as an ISO from rat Tac3; both trace to the same rat experiment, which is
  intracerebroventricular NK3 agonist injection with a partly vasopressin-dependent pressor
  response.
  [PMID:2478257 "into the lateral brain ventricle of the normotensive rats caused dose-dependent increases in the blood pressure"]
  Tachykinins are vasoactive as a family, so the claim is not false and the node placement is
  reasonable, but there is no mouse evidence and no loss-of-function evidence that endogenous
  NKB raises blood pressure. MARK_AS_OVER_ANNOTATED, as in the human TAC3 and mouse *Tacr3*
  reviews. `just paint-losses mouse Tac2`: no IRD or IKR on this lineage, so the IBA is
  current.
- GO:1902093 positive regulation of flagellated sperm motility is an ISO from the human
  sperm study (exogenous tachykinins raising human sperm motility). The one mouse experiment
  that looked found neither *Tac2* nor *Tacr3* transcripts in mouse sperm:
  [PMID:12773411 "A low-abundance transcript corresponding to the NK2 receptor was the only target gene detected in mice sperm."]
  MARK_AS_OVER_ANNOTATED for mouse, matching the *Tacr3* review's deliberate human/mouse
  divergence (the human reviews keep the sperm claims on their own data).

## Leads not turned into annotations

- **Chronic social isolation.** Two weeks of isolation raises *Tac2*/NKB brain-wide, an NK3R
  antagonist prevents nearly all the behavioural changes, and raising NKB expression and
  release phenocopies isolation.
  [PMID:29775595 "2 weeks (but not 24 hr) of social isolation stress (SIS) caused multiple behavioral changes in mice and induced brain-wide upregulation of the neuropeptide tachykinin 2 (Tac2)/neurokinin B (NkB)"]
- **Fear memory consolidation**, through *Tac2* neurons of the centromedial amygdala.
  [PMID:24976214 "We provide evidence that the Tac2 gene, expressed by neurons specifically within the CeM, is required for modulating fear memories."]
  Both are genuine mouse functions of this gene and both are in the description. Neither is
  proposed as a GO row: the readouts are whole-animal behaviour (aggression, persistent fear,
  fear consolidation) produced by region-specific manipulations, which is the system-level
  kind of claim the NEW rules ask to keep out, and the effect in the fear paradigm is
  reported to be sex-dependent in later work I did not read. A curator with those full texts
  could reasonably propose a behaviour term; the two papers are cited in `references` with a
  `reference_review` saying so.
- **GO:0160041 neuropeptide activity.** The human TAC3 review considered it, and declined
  while the disappearance of the human MF rows is unexplained. Same decision here, for the
  same reason and to keep the pair consistent.
