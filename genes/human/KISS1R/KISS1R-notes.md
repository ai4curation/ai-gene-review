# KISS1R (GPR54, AXOR12, hOT7T175) — curation notes

UniProt Q969F8. Human kisspeptin receptor; class A (rhodopsin-like) 7TM GPCR, 398 aa,
PANTHER PTHR45695 (G-protein coupled receptor 1), InterPro IPR008103 (KiSS_1 receptor).
All primary claims below trace to a cached publication, UniProt, or Reactome.

## Identity

The symbol is unambiguous. GPR54/AXOR12/hOT7T175/KISS1R all name this one receptor
for the KISS1-derived peptides (kisspeptins). Cloned from human brain as AXOR12, 81%
identical to rat GPR54 [PMID:11387329 "A novel human G protein-coupled receptor named
AXOR12, exhibiting 81% homology to the rat orphan receptor GPR54, was cloned from a
human brain cDNA library."].

## Molecular function — receptor for kisspeptins

Three groups deorphanised GPR54 in parallel (2001): the KISS1-derived peptides
(kisspeptin-54/metastin, -14, -13, and the minimal -10 decapeptide), all sharing a
C-terminal RF-amide, are the agonists.
- Kotani 2001: peptides from human placenta bind rat and human GPR54 with low-nM affinity
  and stimulate PIP2 hydrolysis / Ca2+ [PMID:11457843 "They bound with low nanomolar
  affinities to rat and human GPR54 expressed in Chinese hamster ovary K1 cells and
  stimulated PIP(2) hydrolysis, Ca(2+) mobilization, arachidonic acid release, ERK1/2 and
  p38 MAP kinase phosphorylation, and stress fiber formation but inhibited cell
  proliferation."].
- Muir 2001: high-potency agonism indicative of a cognate ligand, from KiSS-1 peptides
  with a C-terminal amidated motif [PMID:11387329 "High potency agonism, indicative of a
  cognate ligand, was evident from peptides derived from the gene KiSS-1"].
- Ohtaki/Nature 2001 (metastin / hOT7T175) — same receptor; cached as PMID:11385580.

So the receptor-side MF is a G protein-coupled (neuro)peptide receptor activity. The
IBA at the neuropeptide-receptor level is `GO:0008188 neuropeptide receptor activity`,
with KISS1R itself and zebrafish paralogs among the WITH/FROM (and the gene appears in
its own WITH/FROM because it has its own IDA — expected, not circular). `GO:0008528 G
protein-coupled peptide receptor activity` is the mechanistically precise descendant
(is_a both peptide receptor activity and GPCR activity). `GO:0004930` is the grandparent.
Direct human IDA for GPCR activity: Kotani (PMID:11457843) and Wacker (PMID:18772143).

Clements 2001 (PMID:11414709): surrogate FMRFamide/RFamide peptides activate GPR54 via
Gαq at µM range; optimal motif Gly-Leu-Arg-Trp-NH2. Mouse/human/rat GPR54 ~85% identical.
This is the paper behind the mouse IDA GPCR/peptide-receptor rows.

## G-protein coupling and proximal signalling

Canonical axis: Gq/11 → PLCβ → PIP2 hydrolysis, Ca2+, PKC, ERK1/2 & p38
[PMID:11457843, as above]. UniProt CC:FUNCTION states the GnRH-neuron mechanism:
Gq → PLC → IP3/Ca2+, inhibition of Kir channels, activation of TRPC-like cation channels
→ depolarisation (By similarity, rodent electrophysiology).

Wacker 2008 (full text): the IHH mutation L148S in IL2 does not change expression,
trafficking, surface localisation, or ligand binding (KD ~1.6 nM WT vs 2.5 nM mutant) but
abolishes >90% of PI-hydrolysis and ERK responses; FRET shows it blocks catalytic
activation of Gαq (no Gβγ dissociation) while leaving Gαq *binding* intact
[PMID:18772143 "the mutation does not affect the expression, ligand binding properties,
or protein interaction network of GPR54. In contrast, diverse GPR54 functional responses
are markedly inhibited"; "the interaction between GPR54 IL2 and Gα q was completely
unaffected by the L148S mutation"]. This supplies the direct human IDA for `GO:0007200`
PLC-activating GPCR signalling and plasma-membrane localisation.

β-arrestin arm: KISS1R also signals G-protein-independently through β-arrestin to ERK.
Pampillo 2009 (PMID:19846537): GRK2 desensitises GPR54; β-arrestin-2 mediates ERK1/2
activation; receptor associates with GRK2 and β-arrestins-1/2 via IL2 and C-tail
sequences. Ahow 2014 (PMID:25147978): β-arrestin-1/-2 KO mice have reduced Kp-induced LH;
the Gαq-uncoupled L148S mutant still drives β-arrestin-dependent ERK. Both are mouse/HEK
mechanism papers.

Gi/o: Wu 2024 (PMID:39151001, full text) report KISS1R can also couple Gi/o besides Gq/11
[PMID:39151001 "we demonstrated that KISS1R can couple to the Gi/o pathway besides the
well-known Gq/11 pathway"; "It primarily couples to Gq/11 and then signals through Gi/o
pathway."]. Cryo-EM KISS1R-Gq/-Gi with TAK448 and KP54. Shen 2024 (PMID:38935498,
abstract only) also solved KISS1R-Gq and note a ~40° TM6 deviation vs other Gq receptors.

## Cellular location

- Plasma membrane / cell membrane: UniProt SUBCELLULAR LOCATION "Cell membrane; Multi-pass
  membrane protein" (PMID:18772143); direct FACS/confocal surface expression in Wacker.
  Reactome places the receptor at the plasma membrane. IBA `is_active_in` plasma membrane
  across the neuropeptide-receptor clade.
- Primary cilium: Koemeter-Cox 2014 (PMID:24982149) — Kiss1r is enriched in primary cilia
  of mouse GnRH neurons, GnRH neurons become multiciliated with maturation, and ablating
  cilia reduces kisspeptin-evoked activity. Hsieh/Mukhopadhyay 2017 (PMID:28154160, full
  text) — KISS1R-GFP localises to cilia in RPE cells and requires TULP3 for ciliary
  trafficking [PMID:28154160 "with GPR83 and KISS1R, the steady-state ciliary levels were
  significantly decreased"]. This is the human GOA cilium IDA row (MGI assignment,
  PMID:28154160). Ciliary membrane is part of the plasma membrane — cilium is a real,
  specific location but observed in an overexpression system; keep cilium, keep PM.

## Physiology — HPG axis, puberty (core organismal role)

Kisspeptin–KISS1R is the gatekeeper of GnRH secretion and puberty.
- Human loss-of-function → normosmic IHH: Seminara 2003 (PMID:14573733, L148S homozygous +
  compound het) and de Roux 2003 (PMID:12944565, 155-nt deletion). Gpr54-/- mice phenocopy,
  still respond to exogenous GnRH → defect is upstream, in GnRH secretion control
  [PMID:14573733 "Mutations in GPR54... cause autosomal recessive idiopathic
  hypogonadotropic hypogonadism... this receptor is essential for normal
  gonadotropin-releasing hormone physiology and for puberty."].
- Semple 2005 (PMID:15598687): compound het C223R (profoundly impaired signalling) + R297L
  (mild reduction). Tenenbaum-Rakover 2007 (PMID:17164310): L102P abolishes signalling.
- Gain-of-function → central precocious puberty: Teles 2008 (PMID:18272894), R386P, prolonged
  signalling from reduced desensitisation [PMID:18272894 "this mutation leads to prolonged
  activation of intracellular signaling pathways in response to kisspeptin"].
- Site of action is the GnRH neuron: Messager 2005 (PMID:15665093) GPR54 colocalises with
  GnRH neurons, i.p. kisspeptin fails in gpr54-/- mice; Kirilov 2013 (PMID:24051579)
  GnRH-neuron-specific Gpr54 deletion causes infertility and the knock-in rescues it
  [PMID:24051579 "the GnRH neuron is the key site of kisspeptin-Gpr54 signaling for
  fertility"].
- Mechanism of depolarisation: Zhang 2008 (PMID:18434521, mouse GnRH neurons) — kisspeptin
  depolarises via concurrent inhibition of Kir and activation of TRPC-like NSCC; Liu/Herbison
  2008 (PMID:18483150, mouse) — PLC-IP3R-Ca2+ cascade modulating K+ and NSC channels;
  Han 2005 (PMID:16339030, mouse) — kisspeptin potently depolarises >90% of adult GnRH neurons.

These establish `GO:0032278 positive regulation of gonadotropin secretion` (human IMP from
Seminara and Semple genetics) and the membrane-depolarisation rows — but note these are
*downstream* organismal/physiological consequences performed by the GnRH neuron, not the
receptor's own molecular activity; GO curators annotate them as `involved_in` and the GnRH
GO-CAM 68d5ebd600001111 models the receptor → Gq → TRPC4 chain. Keep as non-core vs core:
`positive regulation of gonadotropin secretion` is the defining physiological role of this
receptor (its loss defines the disease), so it is reasonable to treat as a core process, while
the raw `regulation of membrane depolarization` / cation-transport IEA rows are more generic
downstream descriptions.

## Peripheral / secondary roles

- Anti-metastatic / anti-proliferative / anti-migratory (the original "metastin" biology):
  Ohtaki 2001 (PMID:11385580), Hori 2001 (PMID:11527393), Becker 2005 (PMID:15596153,
  apoptosis/cell-cycle arrest via PLC-PKC). Trophoblast invasion inhibition: Bilban 2004
  (PMID:15020672). Real but not the receptor's defining role.
- Bone / osteoclast: Li 2024 (PMID:38346942, full text). Kp-10→Gpr54 recruits active SRC and
  DUSP18 to the C-terminal PR motif via a Gq-dependent mechanism; DUSP18 dephosphorylates
  SRC(Y416), suppressing osteoclast differentiation/activity and bone resorption. Mechanism
  shown largely in mouse (whole-body and LysM-Cre osteoclast cKO Gpr54/Kiss1, Dusp18 KO,
  OVX model) with confirmatory human giant-cell-tumour-of-bone osteoclast data
  [PMID:38346942 "GPR54 activation by its natural ligand Kisspeptin-10 (Kp-10) causes Dusp18
  to dephosphorylate Src at Tyr 416... Gpr54 recruits both active Src and the Dusp18
  phosphatase at its proline/arginine-rich motif in its C terminus"]. This is the basis of the
  ISS/IEA `negative regulation of osteoclast differentiation` / `negative regulation of bone
  resorption` rows (transferred from mouse Q91V45), and the bone GO-CAM 68d5ebd600001504.
  Judged on evidence: the bone claim is well-supported but the direct human data are a GCT-cell
  osteoclast assay; the osteoclast cKO (cell-autonomous) data are mouse. Keep as non-core
  (peripheral), evidence sound.

## Interactions (the IPI rows)

- PP2A catalytic subunit (PPP2CA, P67775): Evans 2008 (PMID:18977201) — GPR54 C-terminal
  PR-rich SH3-binding region binds PP2A-C in a Y2H + pull-down [PMID:18977201 "Yeast two
  hybrid experiments identified the catalytic subunit of protein phosphatase 2A (PP2A-C) as
  an interacting protein."]. Bare `GO:0005515` row → per protein-binding policy, REMOVE
  (uninformative); the specific partner could in principle be `GO:0051721 protein phosphatase
  2A binding` but that is not asserted in GOA and the functional consequence is undefined, so
  I will not add a NEW MF — note the interaction in reason.
- GNAQ (P50148): the cognate Gαq. The Wacker IPI is really the receptor-Gα coupling; bare
  protein binding row → REMOVE under policy (coupling captured by GPCR activity / `GO:0007200`).
- RAMP1/2/3 (O60894/5/6): Kotliar 2024 (PMID:39083597) high-throughput GPCR-RAMP interactome.
  Bare protein binding → REMOVE under policy (functional significance unknown; UniProt and the
  deep-research both flag RAMP significance as open).

Generic `GO:0060090 molecular adaptor activity` (IEA from mouse, PMID:38346942 via Ensembl):
the C-terminal scaffolding of SRC+DUSP18 is an activation-dependent recruitment, not a
dedicated structural adaptor function — MARK_AS_OVER_ANNOTATED (receptor signalling, not an
adaptor). `GO:0051049 regulation of transport` (ARBA) and `GO:1904062 regulation of monoatomic
cation transmembrane transport` (IEA, from the TRPC/Kir mechanism) are generic downstream
descriptions; keep the specific depolarisation framing where supported, the ARBA transport
row is too general.

## Decisions summary (for the review)
- Receptor MF rows (GPCR activity, peptide-receptor activity, neuropeptide receptor activity):
  ACCEPT the specific ones; the three co-exist as is_a reinforcing lines.
- `GO:0007200` PLC-activating GPCR signalling: ACCEPT core (direct human IDA).
- `GO:0007186` plain GPCR signalling pathway (IEA/NAS): TOO_GENERAL (entailed by GO:0007200).
- `GO:0007218` neuropeptide signalling pathway (IBA): ACCEPT (clade-level, correct).
- plasma membrane rows: ACCEPT; cilium IDA: KEEP_AS_NON_CORE.
- bone/osteoclast rows: KEEP_AS_NON_CORE (mouse-derived, sound).
- gonadotropin secretion: ACCEPT (defining physiology); hormone secretion IBA: KEEP/ACCEPT;
  membrane depolarization + cation transport IEA: KEEP_AS_NON_CORE or MODIFY to the
  depolarization framing.
- bare protein binding (PP2A, GNAQ, RAMP1/2/3): REMOVE (protein-binding policy).
- molecular adaptor activity: MARK_AS_OVER_ANNOTATED.
- regulation of transport (ARBA): too general vs the specific depolarization role.
