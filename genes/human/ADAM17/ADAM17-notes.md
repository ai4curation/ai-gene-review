# ADAM17 (TACE) — curation notes

> **Provenance note.** Provider deep research was unavailable for this gene: the Falcon
> provider returned `402 Payment Required` and perplexity is not configured in this
> checkout. No `*-deep-research-<provider>.md` file was created. The synthesis below is
> my own, built from the UniProt record (`ADAM17-uniprot.txt`), the cached publications
> in `publications/` (every PMID cited in the GOA-seeded review), and targeted
> literature retrieval (PubMed E-utilities; one additional paper, PMID:20676056, was
> fetched with `just fetch-pmid`). Every assertion below carries an inline citation
> with a verbatim quote from a cached publication.

## 1. What the protein is

ADAM17 (TACE, TNF-alpha converting enzyme; UniProt P78536; EC 3.4.24.86) is a type I
transmembrane zinc metalloprotease of the adamalysin/ADAM family. Domain order from the
UniProt feature table: signal peptide, inhibitory pro-domain, catalytic metalloprotease
domain (HExxHxxGxxH zinc site), disintegrin domain, membrane-proximal (MPD/CANDIS)
region, transmembrane segment, cytoplasmic tail ending in a group-I PDZ-binding motif.
It was cloned twice in 1997 as the protease that converts the 26-kDa membrane TNF
precursor to the soluble cytokine [PMID:9034190 "We have now purified and cloned a
metalloproteinase that specifically cleaves precursor TNF-alpha."]; [PMID:9034191 "TACE
is a membrane-bound disintegrin metalloproteinase."].

Zinc dependence and cofactor requirement are recorded in UniProt (`Binds 1 zinc ion per
subunit`), and the pro-domain is removed by a furin-type convertase in the secretory
pathway, which is the prerequisite for activity in this protease subfamily
[PMID:9920899 "Our results suggest that the pro-domain of MDC9 is removed by a
furin-type pro-protein convertase in the secretory pathway before the protein emerges
on the cell surface."] — for ADAM17 itself the same furin-dependent maturation in the
Golgi/raft compartment was shown directly [PMID:17010968 "during its transport through
the Golgi apparatus, ADAM17 is included in cholesterol-rich membrane microdomains
(lipid rafts) where its prodomain is cleaved by furin"].

## 2. Core activity: regulated ectodomain shedding

The single core molecular function is **metalloendopeptidase activity exerted on the
juxtamembrane stalks of transmembrane proteins** — i.e. ectodomain shedding at the
plasma membrane. UniProt summarises the breadth: "Transmembrane metalloprotease which
mediates the ectodomain shedding of a myriad of transmembrane proteins including
adhesion proteins, growth factor precursors and cytokines important for inflammation
and immunity". A 2024 paper puts a number on it [PMID:38771644 "ADAM17), a type I
transmembrane metallopeptidase, is responsible for shedding the ectodomains of over 90
substrates, including cytokines (such as TNF-α), cytokine receptors (such as IL-6R and
TNFR), and adhesion proteins"].

Substrates with direct, cited experimental support in the cached set:

- **TNF (pro-TNF-alpha)** — the founding substrate [PMID:9034190 "Inactivation of the
  gene in mouse cells caused a marked decrease in soluble TNF-alpha production."];
  the cleavage site is recorded in the UniProt catalytic-activity line
  (Pro-Leu-Ala-Gln-Ala-|-Val-Arg-Ser-Ser-Ser).
- **EGFR ligands (amphiregulin, TGF-alpha, HB-EGF, epiregulin, epigen)** —
  [PMID:12743035 "The results of this study indicate that treatment of squamous cell
  carcinoma cells with GPCR ligands such as LPA and carbachol leads to the rapid and
  specific cleavage of proAR at the cell surface by TACE."]; [PMID:29897336 "ADAM17 is
  the principal sheddase of the epidermal growth factor (EGF) receptor ligands
  amphiregulin (AREG), transforming growth factor alpha (TGFα), heparin-binding EGF
  (HB-EGF), epigen, and epiregulin"].
- **IL6R** — [PMID:16034137 "By 4 h of bacterial exposure, TACE colocalized with
  IL-6Ralpha on the apical surface of airway cells, and by 24 h, soluble IL-6Ralpha
  accumulated in the cell culture supernatant."]
- **KIT (c-Kit)** — [PMID:14625290 "we report that tumor necrosis factor
  alpha-converting enzyme (TACE; ADAM-17) mediates shedding of c-Kit"].
- **GP5 (platelet glycoprotein V)** — [PMID:15691827 "we show that recombinant ADAM17
  ectodomain efficiently releases GPV from the platelet surface"].
- **FCGR3A/CD16A on NK cells**, with the cleavage site mapped between Ala195 and Val196
  [PMID:24337742 "MALDI-TOF analysis revealed that the peptide was cleaved between
  Ala(195) and Val(196) (i.e., 1 aa upstream of the expected position)."].
- **MICA** (NKG2D ligand; tumour immune escape) [PMID:18676862 "MICA shedding by tumor
  cells was inhibited by silencing of the related ADAM10 and ADAM17 proteases"].
- **CXCL16** [PMID:18373975 "We identified ADAM10 and ADAM17 as being responsible for
  the cytokine-induced shedding of CXCL16."]
- **VASN (vasorin)** — the mechanism by which ADAM17 loss *raises* TGF-beta signalling
  [PMID:21170088 "we show that only the soluble form of VASN inhibits TGFβ and that the
  secretion of VASN is tightly controlled by ADAM17"].
- **ACE2** — ADAM17 competes with TMPRSS2 for the receptor
  [PMID:24227843 "TMPRSS2 was found to compete with the metalloprotease ADAM17 for ACE2
  processing, but only cleavage by TMPRSS2 resulted in augmented SARS-S-driven entry"].
- **TREM2** — relevant to the Alzheimer/microglia literature; FTD-associated TREM2
  missense variants "abolish shedding by ADAM proteases" [PMID:24990881 "missense
  mutations associated with FTD and FTD-like syndrome reduce TREM2 maturation, abolish
  shedding by ADAM proteases, and impair the phagocytic activity of TREM2-expressing
  cells"].
- **NOTCH1** at the S2 site, in vitro and glycosylation-sensitive [PMID:24226769
  "GALNT11 O-glycosylation enhanced cleavage of the juxtamembrane peptide by ADAM 17"].
- **DCC/Frazzled** in commissural axon guidance [PMID:36476876 "Here we establish a
  conserved and essential role for Tace and ADAM17 in cleaving Fra and Dcc and
  demonstrate that this proteolysis bi-directionally regulates axon guidance at the
  midline."]

## 3. How the activity is controlled (the part that matters for GO review)

ADAM17 is better described as the catalytic subunit of a **sheddase complex** than as a
free-standing protease. Three control layers are well documented:

1. **iRhom (RHBDF1/RHBDF2) dependence.** ER exit, surface delivery and activation all
   require an iRhom [PMID:22246777 "In contrast to wild-type cells, no TACE was found
   on the surface of iRhom2−/− macrophages"], and the iRhom tail is the platform that
   transduces activating stimuli [PMID:29897333 "Within the sheddase complex, iRhom
   proteins serve as a platform that senses and transduces TACE-activating stimuli."].
   FRMD8/iTAP stabilises the complex at the surface [PMID:29897336 "is a cofactor of
   iRhoms and is necessary to stabilise iRhoms and ADAM17 at the cell surface."].
2. **Membrane microenvironment.** Shedding activity partitions into cholesterol-rich
   rafts [PMID:17010968 "Consequently, ADAM17 shedding activity is sequestered in lipid
   rafts"], and cholesterol efflux to HDL mobilises it [PMID:17786981 "HDLs alter the
   lipid raft structure, which in turn activates the ADAM17-dependent processing of
   transmembrane substrates."]. Tetraspanins (CD9, CD81, TSPAN8) tune substrate
   selectivity [PMID:36078095 "all three investigated Tspans (CD9, CD81 and Tspan8)
   regulate ADAM17 substrate availability by different mechanisms."]
3. **Inhibitors and interactors.** TIMP3 is the physiological inhibitor and its complex
   with the catalytic domain has been crystallised [PMID:18638486 "TIMP-3 (tissue
   inhibitor of metalloproteinases 3) is unique among the TIMP inhibitors, in that it
   effectively inhibits the TNF-alpha converting enzyme"]. Integrin alpha5beta1 binds
   the disintegrin domain and *restrains* catalysis
   [PMID:30455686 "the interaction between integrin α5β1 and the disintegrin domain of
   ADAM17 has been shown to cause the inhibition of both the adhesive capacity of the
   integrin (i."]. The cytoplasmic PDZ motif recruits PTPH1/PTPN3 and SAP97/DLG1, both
   of which modulate levels or shedding output [PMID:12207026 "The interaction is
   mediated via binding of the PDZ domain of PTPH1 to the COOH terminus of TACE."];
   [PMID:12668732 "overexpression of SAP97, unlike that of a mutant form of SAP97
   deleted for its PDZ3 domain, altered the ability of TACE to release its substrates."]

This matters for review decisions: most of ADAM17's *signalling* annotations are
consequences of releasing a ligand or receptor ectodomain, not of ADAM17 performing a
step inside the downstream cascade. Where a signalling-pathway term is supported by
ADAM17 cleaving the pathway's own activating ligand (EGFR ligands → EGFR pathway; TNF →
TNF pathway; Notch S2 cleavage → Notch pathway), the participation test is met because
ADAM17 catalyses the activating step. Where the term describes a cascade downstream of
that release (PI3K/AKT signal transduction, G1/S transition, cell proliferation/growth),
ADAM17 is an upstream requirement rather than a participant, and those rows are best
kept as non-core or marked over-annotated.

## 4. ADAM17 vs ADAM10 as the APP alpha-secretase

This is the question the dismech Alzheimer entry depends on, and the evidence is
asymmetric:

- **ADAM17 is the regulated (phorbol-ester-stimulated) alpha-secretase.** The original
  knockout study is explicit [PMID:9774383 "we now demonstrate that TACE (tumor
  necrosis factor alpha converting enzyme), a member of the ADAM family (a disintegrin
  and metalloprotease-family) of proteases, plays a central role in regulated
  alpha-cleavage of APP."] An overexpression/RNAi comparison in glioblastoma cells
  placed ADAM9, ADAM10 and ADAM17 all in the alpha-secretase category [PMID:12535668
  "The results indicate that ADAM9, ADAM10, and ADAM17 catalyze alpha-secretory
  cleavage and therefore act as alpha-secretases in A172 cells."], but that design
  cannot separate constitutive from stimulated activity.
- **ADAM10, not ADAM17, is the constitutive alpha-secretase in neurons.** The decisive
  knockdown series found [PMID:20676056 "Knockdown of ADAM17 mildly reduced total APPs
  and APPsα in HEK293 cells ( Figure 2A and B ), but had no significant effect in
  SH-SY5Y cells ( Figure 2C and D )."] while ADAM17 was required specifically for the
  stimulated arm [PMID:20676056 "This shows that ADAM10 is not required for PMA
  induction of APP shedding and suggests that under these conditions ADAM17 can
  directly cleave APP."]; the same paper notes that ADAM17-deficient fibroblasts show no
  altered constitutive alpha-cleavage [PMID:20676056 "Our knockdown data for ADAM9 and
  17 complement the previous finding that ADAM9-deficient primary hippocampal neurons
  and ADAM17-deficient mouse embryonic fibroblasts do not show evidence of an altered
  α-secretase cleavage compared with their corresponding wild-type control cells (
  Buxbaum et al, 1998 ; Weskamp et al, 2002 )."] and leaves the physiological relevance
  of ADAM17-mediated APP cleavage explicitly open [PMID:20676056 "Future studies need
  to address whether ADAM17 cleavage of APP also occurs under physiologically or
  pathophysiologically relevant conditions other than upon treatment with the synthetic
  phorbol ester PMA."].

**Reading for the muscarinic M1 node.** The pharmacology that connects M1 signalling to
non-amyloidogenic APP processing runs through PKC-stimulated, i.e. *regulated*,
alpha-secretase — which is the arm ADAM17 demonstrably serves, and the arm ADAM10 is
dispensable for. So naming ADAM17 as the alpha-secretase effector of M1/PKC-stimulated
shedding is defensible; naming it as "the alpha-secretase" without that qualifier is
not, because the constitutive neuronal activity is ADAM10's. The strength of evidence is
**moderate for the regulated arm in cell lines and weak-to-absent for a physiological
GPCR-driven APP cleavage in neurons** (PMID:20676056's own caveat above). Note also that
the same asymmetry recurs for Notch: ADAM10 serves ligand-induced physiological
cleavage, and a 2024 paper is blunt that [PMID:38771644 "Conversely, ADAM17 can only
activate Notch signaling under nonphysiological conditions in vitro (62–66)."]

## 5. Loss of function phenotypes

- Mouse `TaceΔZn/ΔZn` animals are hypermetabolic and lean [PMID:18687778 "Because this
  effect is not matched by increased food intake, mice lacking TACE exhibit a lean
  phenotype."], which is the (mouse) basis of the negative-regulation-of-thermogenesis
  annotation.
- A human CANDIS-domain variant causes autosomal-dominant hypotrichosis with woolly
  hair through enhanced ubiquitin-mediated degradation of the mutant protein
  [PMID:38771644 "the variant in CANDIS enhanced ADAM17 susceptibility to
  ubiquitin-mediated degradation by enhancing its association with E3 ubiquitin ligase
  TRIM47."] — note this is a property of the **mutant** protein, which is why the
  derived `ubiquitin binding` molecular-function annotation from this paper is
  questionable (see the review row).
- Conditional deletion in mouse spinal cord reduces commissural midline crossing
  [PMID:36476876 "the thickness of Robo3-positive commissures at the ventral midline is
  significantly reduced in Adam17 cKO embryos, demonstrating that ADAM17 is required in
  vivo for the midline crossing of commissural axons (Figure 6J)."]

## 6. Review decisions taken (summary of reasoning patterns)

- `GO:0004222 metalloendopeptidase activity` and `GO:0006509 membrane protein ectodomain
  proteolysis` — accepted throughout; these are the core function and are supported by
  many independent IDA/IMP rows.
- `GO:0005515 protein binding` — removed per the curation guideline (uninformative),
  except where the cited paper supports a more informative function, in which case the
  row is MODIFYed (e.g. the TIMP3 structure paper → peptidase inhibitor binding;
  the integrin papers already carry `integrin binding`).
- Downstream signalling/proliferation terms (`GO:0043491`, `GO:1900087`,
  `GO:0008284`, `GO:0030307`) — kept as non-core or marked over-annotated: the ADAM17
  step is the ligand release, not a step inside the cascade.
- ISS rows transferred from the mouse gene paper PMID:10433800 (germinal centre
  formation, B/T cell differentiation, spleen development, mast cell apoptosis,
  xenobiotic response, cell motility) — these are mouse knockout phenotypes propagated
  by sequence similarity; the cited reference is a cDNA/gene-structure paper that
  contains none of those data, so each is kept as non-core (the underlying mouse
  biology is real) rather than accepted as a core function.
- No `NEW` annotations were proposed. The candidates considered and rejected:
  `GO:0050870 positive regulation of T cell activation`, `GO:0002687 positive regulation
  of leukocyte migration` and amyloid-pathway terms beyond the existing
  `GO:0042987`. In each case ADAM17's contribution is the release of a ligand already
  annotated for the downstream process, which fails the participation test, and the
  comparator check (other sheddases such as ADAM10, BACE1 and MMP14 are likewise not
  annotated to the downstream immune-activation terms their products drive) indicates a
  convention rather than a gap.
