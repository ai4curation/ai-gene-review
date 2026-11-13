# Kiss1r (Gpr54) — mouse curation notes

UniProt Q91V45 (KISSR_MOUSE), MGI:2148793, approved MGI symbol `Kiss1r` (synonym `Gpr54`).
396 aa class A (rhodopsin-like) 7TM GPCR; InterPro IPR008103 (KiSS-1 receptor), PANTHER
PTHR45695. Ortholog of human KISS1R (Q969F8), which has its own review in
`genes/human/KISS1R/`; this review follows its judgements unless mouse evidence differs, and
says so where it does. Every claim below traces to a cached publication or the UniProt record.

## Identity and ligand

- Mouse GPR54 was cloned together with human GPR54 as orthologs of the rat orphan receptor
  [PMID:11414709 "We have isolated and determined the coding sequences of human and mouse
  orthologs of the rat orphan G-protein-coupled receptor GPR54"; "Mouse and rat GPR54 are nearly
  95% identical to each other, and both are approximately 85% identical to human GPR54 at the
  amino acid level"].
- Mouse Kiss1 and its receptor characterised together; mouse and human kisspeptin-10 differ by
  one residue [PMID:12359743 "the active peptides (10-amino-acid residues) are highly conserved
  between mouse and human KiSS1 proteins"]; ligand activation of the receptor engages Gq/PLC-beta
  [PMID:12359743 "Activation of the receptor by KiSS1 peptide leads to the activation of
  G-protein-activated phospholipase C (PLC-beta)"]. This is the IPI (Kiss1, Q6Y4S4) and cell
  surface IDA source; cached as abstract only, so the assay behind each MGI row is not visible.
- Surrogate RF/RW-amide agonists act through Gq at µM [PMID:11414709 "invertebrate neuropeptides
  of the RFamide and RWamide family that were able to activate GPR54 at microM range through the
  G(alpha)q pathway"] — source of the mouse IDA G protein-coupled peptide receptor activity and
  signal transduction rows (MGI, 2001).
- In vivo, kisspeptins are the physiological ligand: Kiss1-null mice phenocopy Gpr54-null mice
  [PMID:17563351 "The virtually identical phenotype of Gpr54- and Kiss1-null mice provides direct
  proof that kisspeptins are the true physiological ligand for the GPR54 receptor in vivo"], and
  the mouse agonist fails in Gpr54 knockouts [PMID:17595229 "When injected with mouse metastin
  43-52, a Gpr54 agonist, Gpr54 knockout mice fail to increase gonadotropins, whereas Kiss1
  knockout mice respond with increased gonadotropin levels"].

MF conclusion (same as human): `GO:0008188 neuropeptide receptor activity` is the core term.
OLS confirms GO:0008188 is_a GO:0008528 is_a GO:0004930, and GO:0008188 has_part GO:0042923
neuropeptide binding and part_of GO:0007218 neuropeptide signaling pathway, so GPCR activity,
peptide receptor activity and neuropeptide binding rows are all entailed (TOO_GENERAL).

## Physiology: the HPG axis (mouse is the primary evidence here)

- Whole-body knockouts, two independent lines:
  - Seminara 2003 (Paradigm line) [PMID:14573733 "The Gpr54-deficient mice had isolated
    hypogonadotropic hypogonadism (small testes in male mice and a delay in vaginal opening and an
    absence of follicular maturation in female mice), but they showed responsiveness to both
    exogenous gonadotropins and gonadotropin-releasing hormone"].
  - Funes 2003 (Schering-Plough line) [PMID:14652023 "we have generated a mutant mouse line with a
    targeted disruption of the GPR54 receptor (GPR54 -/-)"; "The analysis of the GPR54 mutant mice
    revealed developmental abnormalities of both male and female genitalia"].
- Kisspeptin acts only through the receptor for gonadotropin release, at the level of the GnRH
  neuron [PMID:15665093 "GPR54 transcripts are colocalized with gonadotropin-releasing hormone
  (GnRH) neurons in the mouse hypothalamus"; "levels of kisspeptin injected i.p., which stimulate
  robust LH and FSH release in wild-type mice, have no effect in gpr54-/- mice"]. (The direct GnRH
  release measurement in that paper is in sheep, not mouse.)
- Cell-specific genetics put the site of action in the GnRH neuron:
  - Kirilov 2013: GnRH-neuron deletion and BAC rescue [PMID:24051579 "Mutant mice are infertile,
    fail to go through puberty and exhibit markedly reduced gonadal size and follicle-stimulating
    hormone levels alongside GnRH neurons that are unresponsive to kisspeptin"; "the GnRH neuron is
    the key site of kisspeptin-Gpr54 signaling for fertility"].
  - Novaira 2014 GKirKO [PMID:24422632 "Both female and male GKirKO mice were infertile, having low
    serum LH and FSH levels."].
- GOA for mouse has no experimental row for gonadotropin secretion: the two
  `GO:0032278 positive regulation of gonadotropin secretion` rows are IEA/ISO from human. The mouse
  genetics above independently support the term; ACCEPT both.

Participation check for GO:0032278: the receptor's signalling in the GnRH neuron drives GnRH
release, which drives pituitary LH/FSH; a regulation term is the appropriate way to say this, and
the human review keeps it as the defining physiological process. No GO term exists for GnRH
secretion itself (OLS search: only "response to gonadotropin-releasing hormone" and
"gonadotropin secretion"), so nothing more proximal can be proposed.

## Signalling in mouse GnRH neurons

- Kisspeptin depolarises nearly all adult GnRH neurons [PMID:16339030 "kisspeptin (10-100 nM)
  evoked a remarkably potent, long-lasting depolarization of >90% of gonadotropin-releasing hormone
  (GnRH)-green fluorescent protein neurons in situ"; "Approximately 90% of GnRH neurons were found
  to express GPR54 mRNA"].
- PLC-IP3R-Ca2+ cascade gating K+ and NSC channels (full text, GnRH-GFP and GnRH-Pericam mice)
  [PMID:18483150 "kisspeptin activates G protein-coupled receptor 54 (GPR54) to initiate a
  PLC-IP3R-calcium cascade that modulates both potassium and NSC channels to initiate
  depolarization in GnRH neurons"; "PLC and IP3R antagonism reduced the percentage of responding
  GnRH neurons from 80 to 15 and 7%, respectively"].
- Ionic mechanism [PMID:18434521 "caused by the concurrent inhibition of barium-sensitive,
  inwardly rectifying (Kir) potassium channels and activation of sodium-dependent, nonselective
  cationic channels (NSCCs)"; "kisspeptin depolarizes GnRH neurons through activating TRPC-like
  channels and, to a lesser extent, inhibition of Kir channels"]. The cached abstract and the PMC
  front matter I could retrieve do not name the species; UniProt's mouse entry attributes the
  finding to mouse (ECO:0000269, PubMed:18434521) and the human review's notes also call these
  mouse GnRH neurons. I defer to the UniProt curator who read the full text.
- Same lab, 2013: TRPC activation needs PIP2 depletion and cSrc, but NOT Ca2+ [PMID:23744639
  "Neither removing extracellular Ca(2+) nor buffering intracellular Ca(2+) with EGTA or BAPTA had
  any effect on the kisspeptin activation of the TRPC channels."]. This conflicts with the Ca2+
  dependence reported by Liu/Herbison for the overall response: a genuine open question (recorded
  as a knowledge gap). Species again not stated in the cached abstract.
- Gq-independent beta-arrestin arm [PMID:25147978 "Results revealed that Kp-dependent LH secretion
  was significantly diminished relative to wild-type mice"; "we conclude that KISS1R signals via
  Gαq/11 and β-arrestin to regulate GnRH secretion"]. The in vivo part is beta-arrestin-1/-2
  knockout mice (the arrestins' genes are perturbed, not Kiss1r); the L148S receptor part is in
  HEK293 cells and MEFs.

GO consequences:
- `GO:0007200` PLC-activating GPCR signaling: ACCEPT (Stafford 2002 mouse receptor; Liu 2008 in
  mouse GnRH neurons).
- `GO:0003254 regulation of membrane depolarization` (IDA, PMID:18434521): correct but general; the
  evidence is directional (depolarisation). Human review marks its IEA copy TOO_GENERAL only
  because human also carries `GO:1904181 positive regulation of membrane depolarization` (TAS).
  Mouse has no GO:1904181 row, so here the right action is MODIFY → GO:1904181 (OLS-verified).
- `GO:1904062 regulation of monoatomic cation transmembrane transport` (IDA): the receptor's
  signalling both opens TRPC-like NSCCs and closes Kir channels, so the non-directional
  "regulation" is as precise as warranted. KEEP_AS_NON_CORE (as human).
- `GO:0019722 calcium-mediated signaling` (ISO from rat IMP PMID:16222076): mouse support from
  Liu 2008; but TRPC activation itself is Ca-independent per Zhang 2013. KEEP_AS_NON_CORE.
- `GO:0043410 positive regulation of MAPK cascade` (ISO from rat IDA, Kotani PMID:11457843 ERK1/2
  and p38): mouse support from Ahow 2014 (ERK via beta-arrestin). KEEP_AS_NON_CORE.

## Cilium

Koemeter-Cox 2014 is native mouse evidence [PMID:24982149 "is enriched in cilia projecting from
mouse gonadotropin-releasing hormone (GnRH) neurons"; "disruption of cilia selectively on GnRH
neurons leads to a significant reduction in kisspeptin-mediated GnRH neuronal activity"], stronger
than the human row (GFP-KISS1R overexpressed in RPE cells, PMID:28154160). Yet mouse GOA only has
cilium as IEA/ISO transfers of the human row. KEEP_AS_NON_CORE, as in the human review. GO's
"primary cilium" class (GO:0072372) is obsolete in the current ontology (OLS), and neither paper
tests motility, so cilium is the appropriate level.

## Bone (Li 2024, full text cached)

- [PMID:38346942 "Kiss1, Gpr54 and Dusp18 knockout mice all exhibit osteoclast hyperactivation and
  bone loss"]; osteoclast-specific (LysM-Cre) Gpr54 cKO also loses bone.
- Gpr54-null bone-marrow macrophages form more osteoclasts [PMID:38346942 "Consistent with these
  findings, Gpr54-deletion enhanced osteoclast formation by TRAP staining"]; resorption is rescued
  by re-expression [PMID:38346942 "Additionally, bone resorption was promoted when Gpr54 was
  deleted, which could be rescued upon ectopic expression of Gpr54"].
- Mechanism: [PMID:38346942 "Gpr54 recruits both active Src and the Dusp18 phosphatase at its
  proline/arginine-rich motif in its C terminus"]; Gq/11-dependent [PMID:38346942 "Kp-10 inhibited
  the phosphorylation of Src in WT BMMs, but failed to have a significant effect in Gq/11 KO
  BMMs"], but not via PLC/PKC/ERK/CaMKII inhibitors [PMID:38346942 "were all obvioulsly dampened by
  Src kinase inhibitor (Saracatinib), but not by the inhibitors of Gq/11 downstream signals
  including PLC inhibitor (U73122)"] (quoted with the source's typo). The ternary complex is shown
  with tagged constructs in 293T cells [PMID:38346942 "the complex formation of the heterotrimer
  including DUSP18, Src, and GPR54, was enhanced after Kp-10 stimulation in 293 T cells transfected
  with HA-Src, GPR54-Myc, and DUSP18-Flag (WT)"].
- Decisions: `GO:0045779 negative regulation of bone resorption` IMP → KEEP_AS_NON_CORE (sound,
  peripheral; as human). `GO:0060090 molecular adaptor activity` IDA → MARK_AS_OVER_ANNOTATED (as
  human for its IEA copy of this very row): the recruitment is real, but it is an
  activation-dependent receptor-tail interaction from one study, the heterotrimer rests on
  overexpression, and the GO-CAM curators who modelled this pathway (68d5ebd600001504) gave the
  receptor GPCR activity, not adaptor activity.
- NEW `GO:0045671 negative regulation of osteoclast differentiation` (IMP, PMID:38346942): the human
  review carries this term as ISS from MGI:2148793 (this mouse gene), but mouse GOA has no such row.
  Direct mouse loss-of-function evidence (Gpr54-null BMMs form more TRAP+ osteoclasts). Non-core.

## Rat-derived ISO rows (GO_REF:0000096, RGD:70930 = rat Kiss1r)

Traced through QuickGO (rat Q924U1 annotations):
- Kotani 2001 [PMID:11457843 "They bound with low nanomolar affinities to rat and human GPR54
  expressed in Chinese hamster ovary K1 cells and stimulated PIP(2) hydrolysis, Ca(2+)
  mobilization, arachidonic acid release, ERK1/2 and p38 MAP kinase phosphorylation, and stress
  fiber formation but inhibited cell proliferation"; "Stimulation of oxytocin secretion after
  kisspeptin administration to rats confirmed this hypothesis."] → rat IDA rows for arachidonate
  secretion, stress fiber assembly, cell proliferation, MAPK cascade, hormone secretion (the hormone
  is oxytocin).
- Arai 2005 [PMID:16222076 "activation of GPR54 by submicromolar concentrations of metastin
  reversibly enhances excitatory synaptic transmission in hippocampal dentate granule cells in a
  mitogen-activated protein (MAP) kinase-dependent manner"] → rat IMP rows for GPCR signalling,
  calcium-mediated signaling and positive regulation of synaptic transmission.
- Clements 2001 → rat IDA neuropeptide binding.

Decisions:
- arachidonate secretion, positive regulation of stress fiber assembly: heterologous CHO-cell
  readouts of signalling with no mouse or in vivo evidence → MARK_AS_OVER_ANNOTATED.
- negative regulation of cell population proliferation: two lines (rat receptor in CHO; mouse
  receptor in Stafford 2002 [PMID:12359743 "activation of the KiSS1 receptor inhibits cell
  proliferation and cell migration"]) → KEEP_AS_NON_CORE.
- positive regulation of synaptic transmission: one rat slice study, pharmacological, no mouse data
  → KEEP_AS_NON_CORE (peripheral; not contradicted).
- positive regulation of hormone secretion (IBA + ISO): entailed by GO:0032278 → TOO_GENERAL (as
  human IBA).

## Protein binding

Only one IPI: Kiss1 (PR:Q6Y4S4, KISS1_MOUSE), Stafford 2002. This is the receptor binding its
ligand, captured by neuropeptide receptor activity → REMOVE per protein-binding policy (as human
for the equivalent KISS1 IPI).

## IBA / PAINT

`just paint-losses mouse Kiss1r`: "Q91V45 is not a leaf of this tree; losses not checked." No IRD/IKR
could therefore be checked for this lineage. IBA rows (plasma membrane, neuropeptide signalling,
neuropeptide receptor activity, positive regulation of hormone secretion) all agree with the
experimental picture; the plasma membrane and neuropeptide receptor nodes include human KISS1R
itself among the donors.

## Human/mouse differences in the two reviews (for the coordinator)

1. Mouse GOA lacks any experimental gonadotropin-secretion row despite the mouse knockout
   literature; human has two IMP rows. Both reviews ACCEPT GO:0032278.
2. GO:0045671 is ISS on human (from mouse) but absent from mouse GOA → NEW here.
3. GO:0003254: human TOO_GENERAL (human has GO:1904181); mouse MODIFY → GO:1904181.
4. Cilium: mouse has native-cell evidence (Koemeter-Cox) but only transferred rows; human has the
   overexpression IDA. Same action in both.
5. Mouse carries rat-derived rows (arachidonate secretion, stress fibres, synaptic transmission,
   MAPK, calcium signalling, proliferation) that human does not; human carries PP2A/GNAQ/RAMP IPIs
   and Reactome TAS rows that mouse does not. Human-only claims (Gi/o coupling, cryo-EM, IHH and CPP
   variants) are not ported to mouse.
