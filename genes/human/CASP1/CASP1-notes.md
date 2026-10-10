# CASP1 (human) — curation notes

**Provenance note:** Provider deep research was unavailable for this gene (Falcon returned
402 Payment Required; Perplexity not configured). This notes file is my own literature
synthesis, written from the cached publications in `publications/` and the UniProt record
(`CASP1-uniprot.txt`), and replaces the usual `*-deep-research-<provider>.md` file. Every
assertion carries inline provenance as `[PMID:NNN "quote"]`. No PMID is cited from memory;
each cited title was checked against the cached `publications/PMID_*.md` record.

## Identity and architecture

CASP1 (P29466), interleukin-1β converting enzyme (ICE), is the founding inflammatory
caspase. It is synthesized as an inactive zymogen (pro-caspase-1) with an N-terminal CARD
(residues 1–91), a large catalytic subunit p20 (120–297), an interdomain linker (298–316),
and a small subunit p10 (317–404); catalytic residues are His237 and Cys285
(UniProt feature table; `CASP1-uniprot.txt`). The active enzyme is a heterotetramer of two
antiparallel p20/p10 heterodimers [PMID:8044845 "the holoenzyme is a homodimer of catalytic
domains, each of which contains a p20 and a p10 subunit"]. It is a cysteine-dependent,
Asp-specific protease (clan CD) with a preferred cleavage sequence Tyr-Val-Ala-Asp↓
(EC 3.4.22.36; UniProt CATALYTIC ACTIVITY). It was first cloned as the IL-1β-converting
enzyme [PMID:1373520 "A complementary DNA encoding a protease that carries out this cleavage
has been cloned"] and purified from monocytes as a heterodimeric cysteine protease
[PMID:1574116 "IL-1 beta-converting enzyme is composed of two nonidentical subunits that are
derived from a single proenzyme, possibly by autoproteolysis"]. Five alternatively spliced
isoforms (alpha–epsilon) exist; delta and epsilon are catalytically/apoptotically inactive,
and epsilon can act as a dominant-negative by dimerizing with the p20 subunit
[PMID:7876192 "ICE epsilon can bind to the p20 subunit of ICE and potentially may compete
with the p10 subunit to form an inactive ICE complex"].

## Core function 1 — cysteine protease activity (effector of the inflammasome)

CASP1 is the effector protease of canonical inflammasomes. Its activity and the heterodimeric
protease identity are repeatedly established [PMID:1574116], and it is the catalytic output of
the inflammasome platform [PMID:12191486 "the inflammasome ... comprises caspase-1, caspase-5,
Pycard/Asc, and NALP1"]. Activation is by proximity-induced autoproteolysis: ASC nucleates
CARD filaments of caspase-1 [PMID:24630722 "ASC thus nucleates CARD filaments of caspase-1,
leading to proximity-induced activation"], and the caspase-1 CARD itself polymerizes into a
filament whose structure has been solved [PMID:27043298 "we determined the structure of the
human caspase-1 CARD domain (caspase-1(CARD)) filament by cryo-electron microscopy"].
Interdomain-linker autoprocessing is required for full catalytic activity and for pyroptosis
[PMID:32051255 "pro-caspase-1 IDL cleavage is necessary for pyroptosis induced by both
ASC-dependent and ASC-independent inflammasomes"].

## Core function 2 — maturation of IL-1β and IL-18 (cytokine precursor processing)

The defining physiological substrates are the precursors of IL-1β and IL-18. CASP1 cleaves
pro-IL-1β at Asp116-Ala117 to the mature 17.5 kDa cytokine [PMID:2787508 "mutation of
Asp116→Ala116 rendered the IL-1 beta precursor resistant to cleavage"], and cleaves pro-IL-18
at Asp36-Tyr37 to generate the bioactive 18 kDa species [PMID:9334240 "caspase-1, which
cleaves prohIL-18 at the Asp36-Tyr37 site to generate the mature hIL-18"]. A naturally
occurring Δexon-3 pro-IL-18 isoform is resistant to caspase-1 processing yet still binds the
enzyme [PMID:15326478 "The Delta3pro-IL-18 protein was resistant to proteolytic activation by
caspase-1 and -4, although it was capable to bind caspase-1"]. This is cytokine precursor
processing (GO:0140447) / signaling receptor ligand precursor processing (GO:0140448), the
central role captured by UniProt [CASP1-uniprot.txt FUNCTION "cleaving other proteins, such
as the precursors of the inflammatory cytokines interleukin-1 beta (IL1B) and interleukin 18
(IL18)"].

## Core function 3 — GSDMD cleavage and pyroptosis

CASP1 cleaves gasdermin-D (GSDMD) in the interdomain linker, releasing the pore-forming
N-terminal fragment that executes pyroptosis [PMID:26375003 "Caspase-1 and caspase-4/5/11
specifically cleaved the linker between the amino-terminal gasdermin-N and carboxy-terminal
gasdermin-C domains in GSDMD, which was required and sufficient for pyroptosis"]. GSDMD is
required for IL-1β release and pyroptosis but not for IL-1β maturation itself
[PMID:26611636 "GSDMD is required for pyroptosis and for the secretion but not proteolytic
maturation of IL-1β"]. Recognition of GSDMD is not driven solely by the tetrapeptide
cleavage-site sequence but by an exosite on autoprocessed caspase-1 that binds the GSDMD
C-terminal domain [PMID:32109412 "the β sheet organizes a hydrophobic GSDMD-binding interface
that is only possible for p10-form caspase-4/11 ... Crystal structure of caspase-1-GSDMD-C
complex shows a similar GSDMD-recognition mode"; PMID:32553275 "This 'exosite' interface
endows an additional function for the GSDMD C-terminal domain as a caspase-recruitment module"].
This maps to pyroptotic inflammatory response (GO:0070269) / pyroptotic cell death.

## Inflammasome complex membership

CASP1 is the shared effector of NLRP1, NLRP3, NLRC4/IPAF, and AIM2 inflammasomes, recruited
through its CARD either directly (NLRC4/IPAF, CARD8) or via the ASC adaptor (NLRP3, AIM2,
pyrin). Specific complex memberships are well supported:
- NLRP1 inflammasome [PMID:12191486 "comprises caspase-1, caspase-5, Pycard/Asc, and NALP1";
  PMID:17349957 "we have reconstituted the NALP1 inflammasome"].
- NLRP3 inflammasome [PMID:15030775 "NALP2 and NALP3 associate with ASC ... and caspase-1 ...
  thereby forming an inflammasome with high proIL-1beta-processing activity"].
- NLRC4/IPAF inflammasome [PMID:11390368 "Ipaf associates directly and specifically with the
  CARD domain of procaspase-1 through CARD-CARD interaction"].
- AIM2 inflammasome [PMID:19158675 "AIM2 recognizes cytosolic dsDNA and forms a
  caspase-1-activating inflammasome with ASC"; PMID:19158676 "AIM2 ... caspase-1"].
- Canonical inflammasome [PMID:16037825 "assemble an inflammasome complex with ASC and
  procaspase-1"].

## Regulators binding the CARD (basis of many "protein binding" rows)

A family of CARD-only proteins binds the caspase-1 prodomain/CARD and inhibits activation:
COP/CARD16 [PMID:11432859 "COP ... binds to both RIP2 and the caspase-1 prodomain and inhibits
RIP2-induced caspase-1 oligomerization"], pseudo-ICE/COP and ICEBERG/CARD18
[PMID:11536016 "Pseudo-ICE and ICEBERG interact physically with caspase-1 and block ...
secretion of interleukin-1beta"; PMID:11051551 "ICEBERG ... inhibits generation of IL-1beta
by interacting with caspase-1 and preventing its association with RIP2"], INCA/CARD17
[PMID:15383541 "INCA physically interacts with procaspase-1 and blocks the release of mature
IL-1beta"], and CARD8 [PMID:11821383 "CARD-8 interacts physically with caspase-1 and
negatively regulates caspase-1-dependent IL-1beta generation"]. INCA caps the caspase-1 CARD
filament [PMID:27043298 "INCA caps caspase-1 filaments, thereby exerting potent inhibition"].
SERPINB1 restrains caspase-1 CARD oligomerization [PMID:30692621 "SERPINB1 limited the activity
of those caspases by suppressing their caspase-recruitment domain (CARD) oligomerization"].
MEFV/pyrin interacts via both p10 and p20 subunits [PMID:16785446]. These are CARD-mediated
protein-protein interactions; where a specific function underlies them, CARD domain binding
(GO:0050700) is the informative molecular-function term.

## Other substrates / functions (literature-supported, mostly non-core)

- Autoprocessing: generates the active p20/p10 enzyme [PMID:1574116; PMID:32051255] —
  protein autoprocessing (GO:0016540), under proteolysis, the substrate-is-the-enzyme case.
- Caspase-7 activation during bacterial infection → PARP1 cleavage and NF-κB target gene
  expression [PMID:22464733 "caspase 7 is activated by caspase 1, translocates to the nucleus,
  and cleaves PARP1"].
- cGAS cleavage dampens DNA-virus type-I IFN responses [PMID:28314590 "caspase-1 interacted
  with ... cGAS, cleaving it and dampening cGAS-STING-mediated IFN production"].
- Sphingosine kinase 2 (SPHK2) cleavage during apoptosis [PMID:20197547 "sphingosine kinase 2
  (SphK2) is cleaved at its N-terminus in a caspase-1-dependent manner"].
- ZNFX1 cleavage in a feed-forward NLRP3 loop [PMID:39333773 "ZNFX1 is cleaved by caspase-1,
  establishing a feed-forward loop that promotes NLRP3 accumulation in the trans-Golgi network"].
- Unconventional (leaderless) protein secretion [PMID:18329368 "secretion of the leaderless
  proteins proIL-1alpha, caspase-1, and fibroblast growth factor (FGF)-2 depends on caspase-1
  activity"].
- Eicosanoid "storm" downstream of NLRC4 inflammasome in vivo [PMID:22902502 "inflammasome
  activation results, within minutes, in an 'eicosanoid storm'"] — a downstream physiological
  consequence, not a direct CASP1 enzymatic step.
- Apoptosis / neurodegeneration contexts: PARP cleavage by ICE at high enzyme concentration
  [PMID:7642516], tau cleavage by multiple caspases including caspase-1 in vitro
  [PMID:12888622 "25 ng of caspase-1, -2, -3, -6, -7, or -8"], caspase-1 activation in
  Huntington's disease models [PMID:10353249]. These establish apoptotic activity for
  overexpressed/high-dose enzyme and roles in disease models, but IL-1β/IL-18/GSDMD processing
  and pyroptosis are the physiological core.

## Localization

CASP1 is a cytoplasmic/cytosolic enzyme active in the cytosol; a fraction localizes to the
plasma membrane [PMID:20197547 FUNCTION/SUBCELLULAR LOCATION in UniProt: Cytoplasm; Cell
membrane]. Cytosol is the compartment where the inflammasome assembles and where CASP1 is
active.

## Review decisions summary (rationale for actions)

- MF `cysteine-type endopeptidase activity` (GO:0004197): core — ACCEPT (many IDA + IBA).
- `endopeptidase activity` (GO:0004175, IDA PMID:24548080): generalization of the specific
  cysteine-type activity; MODIFY to GO:0004197.
- `cysteine-type peptidase activity` (GO:0008234, IEA): too general; MODIFY to GO:0004197.
- `protein binding` (GO:0005515): uninformative bare term; REMOVE (many of the interactions
  are real CARD-mediated regulator interactions captured by GO:0050700 / complex terms).
- `CARD domain binding` (GO:0050700): ACCEPT — informative, the mechanism of recruitment.
- `identical protein binding` (GO:0042802): ACCEPT/KEEP — CASP1 homodimerization/filament
  (p20/p10 tetramer, CARD filament) is real.
- `kinase binding` (GO:0019900, RIP2/RICK): KEEP_AS_NON_CORE — real CARD-CARD interaction with
  RIP2 but not the core function.
- `cytokine binding` (GO:0019955, PMID:15030775): pro-IL-18 binding is documented; KEEP_AS_NON_CORE.
- `enzyme binding` (GO:0019899, IEA): too generic; MODIFY toward kinase/CARD binding or REMOVE
  (IEA bare); treat as over-general → MARK_AS_OVER_ANNOTATED/REMOVE of the IEA.
- Complex terms (GO:0061702, GO:0072558/9, GO:0072557, GO:0097169, GO:0032991): ACCEPT the
  specific inflammasome complexes; the AIM2 IBA/IDA/IPI and NLRP3/NLRP1/IPAF rows are sound.
- `protease inhibitor complex` (GO:0097179, IMP PMID:11432859): this describes COP, the
  inhibitor; caspase-1 is the protease being inhibited, so being "part_of" a protease
  inhibitor complex is defensible (enzyme+inhibitor heterodimer) — KEEP_AS_NON_CORE.
- Cytokine processing: `cytokine precursor processing` (GO:0140447), `signaling receptor
  ligand precursor processing` (GO:0140448), `protein maturation` (GO:0051604),
  `protein processing`/`protein autoprocessing`: ACCEPT the core ones.
- `pyroptotic inflammatory response` (GO:0070269): ACCEPT — core.
- `positive regulation of interleukin-1 beta / -18 production` (GO:0032731/GO:0032741):
  ACCEPT — core; CASP1 performs the maturation step that produces the active cytokine.
- `pattern recognition receptor signaling pathway` (GO:0002221, NAS): CASP1 is the effector
  protease downstream of PRRs, not itself a PRR; MODIFY to inflammasome-mediated signaling
  pathway (GO:0141084), which is the precise home.
- `positive regulation of canonical NF-kappaB signal transduction` (GO:0043123): indirect /
  context-specific (via RIP2, Mal/TIRAP cleavage); KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED.
- `apoptotic process` / `positive/regulation of apoptotic process`: real for overexpressed
  enzyme and disease models but pleiotropic/non-core; KEEP_AS_NON_CORE.
- `icosanoid biosynthetic process` (GO:0046456, NAS PMID:22902502): downstream physiological
  consequence; CASP1 does not catalyze eicosanoid synthesis → MARK_AS_OVER_ANNOTATED.
- `osmosensory signaling pathway` (GO:0007231, NAS PMID:22981536): CASP1 is activated by cell
  swelling via NLRP3; it does not do the osmosensing → MARK_AS_OVER_ANNOTATED.
- `cellular response to mechanical stimulus` (GO:0071260, IEP PMID:19593445): the cached paper
  is about BAD/prostate cancer; cannot verify a CASP1 mechanical-stimulus assay → UNDECIDED.
- `microtubule` (GO:0005874, NAS PMID:27911804): that paper is about pyrin and microtubules,
  not CASP1 localizing to microtubules → MARK_AS_OVER_ANNOTATED / UNDECIDED.
- `nucleolus` (GO:0005730, NAS PMID:28263976): that paper reports NLRP1 nucleolar localization,
  not CASP1 → MARK_AS_OVER_ANNOTATED.
