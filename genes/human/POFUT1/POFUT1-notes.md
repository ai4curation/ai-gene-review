# POFUT1 (human, Q9H488) — review notes

GDP-fucose protein O-fucosyltransferase 1 (O-FucT-1; EC 2.4.1.221). HGNC:14988.
CAZy GT65. Chromosome 20. Glycobiology-project exemplar (Notch O-fucosylation axis).

## Core molecular function

POFUT1 transfers L-fucose from GDP-beta-L-fucose to the hydroxyl of a Ser/Thr in the
consensus C2-X(4,5)-S/T-C3 of EGF-like repeats, generating O-linked fucose. The enzyme
strictly requires a *properly folded, disulfide-bonded* EGF domain — it does not modify
linear peptides.

- Enzyme assay / acceptor requirement: [PMID:9023546 "The enzyme catalyzes the reaction that attaches fucose through an O-glycosidic linkage to a conserved serine or threonine residue in EGF domains"] and [PMID:9023546 "the enzyme appears to require more than just a consensus primary sequence and likely requires that the EGF domain disulfide bonds be properly formed"]. Mn2+ stimulates but is not absolutely required: [PMID:9023546 "the enzyme did not exhibit an absolute requirement for Mn2+, enzymatic activity did increase ten fold in the presence of 50 mM MnCl2"].
- Molecular cloning of human POFUT1 cDNA and recombinant enzymatic confirmation (EC 2.4.1.221 is ECO-coded to this paper in UniProt): [PMID:11524432 "Expression of a soluble form of human O-FucT-1 in insect cells yielded a protein of the predicted molecular weight with O-FucT-1 kinetic and enzymatic properties similar to those of O-FucT-1 purified from CHO cells"]. The same paper notes type II membrane topology prediction: [PMID:11524432 "a predicted N-terminal transmembrane sequence typical of a type II membrane orientation"]. Kinetics (UniProt): KM 6 uM (F7 EGF), 4 uM (GDP-fucose).
- Most specific GO MF term = GO:0046922 peptide-O-fucosyltransferase activity (verified MF; definition: transfer of alpha-L-fucosyl from GDP-beta-L-fucose to the serine hydroxy group of a protein acceptor). This is the exact term for EC 2.4.1.221; no narrower GO MF term exists. Generic parents (UDP/hexosyl/fucosyltransferase) are not present in GOA here — good.

## Subcellular localization — ER, NOT Golgi

POFUT1 is a *soluble ER-luminal* enzyme retained by a C-terminal KDEL-like motif; it is
unique among fucosyltransferases in being ER-localized (FUT1-9 are Golgi type-II membrane
enzymes). O-fucosylation of Notch happens in the ER.

- [PMID:15653671 "O-FucT-1 is a soluble protein that localizes to the endoplasmic reticulum (ER)"], [PMID:15653671 "O-FucT-1 is retained in the ER by a KDEL-like sequence at its C terminus"], [PMID:15653671 "enzymatic addition of O-fucose to proteins occurs in the ER"].
- Quality-control hypothesis: [PMID:15653671 "The fact that O-FucT-1 recognizes properly folded epidermal growth factor-like repeats, together with this unique localization, suggests that it may play a role in quality control"].
- UniProt SUBCELLULAR LOCATION: Endoplasmic reticulum. UniProt FT MOTIF 385-388 "Prevents secretion from ER".
- Structure paper restates ER residence: [PMID:28334865 "POFUT1 is an ER-resident protein that catalyzes O-linked fucosylation of an acceptor site on an EGF-like repeat of a recipient protein, using GDP-fucose as the donor substrate"].

Implication for GOA review: ER annotations (IDA PMID:15653671; IBA; IEA; ISS) are correct
and the ER is CORE. The "membrane" (GO:0016020) annotations are problematic:
- HDA PMID:19946888 is an NK-cell *membrane proteome* MS catalog (1843 proteins; ~40% predicted membrane); POFUT1 is a soluble ER-luminal protein, so this is a fraction/contaminant-type assignment, uninformative.
- IDA PMID:11524432 and PMID:9023546 "membrane" annotations: both papers report the enzyme is largely *soluble*; PMID:9023546 recovered only 37% from membranes after Triton extraction of rat liver and attributes membrane association to a protease-susceptible stem. PMID:11524432 predicts a type-II TM anchor but Luo & Haltiwanger (PMID:15653671) later showed the active human/mammalian enzyme is soluble luminal. "membrane" is at best a trivial/uninformative location and is superseded by ER lumen. Mark as over-annotated rather than core.

## Notch signaling — best-supported biological role (downstream of catalysis)

O-fucose on Notch EGF repeats primes for Fringe (LFNG/MFNG/RFNG) GlcNAc elongation, which
modulates ligand (DLL1/DLL4, JAG1/JAG2) binding; POFUT1 is essential for Notch signal
transduction in mammals; loss traps Notch in the ER / blocks surface delivery and abolishes
signaling.

- [PMID:28334865 "Protein O-fucosyltransferase-1 (POFUT1) ... is essential for Notch signal transduction in mammals"].
- [PMID:28334865 "knockout mice lacking POFUT1 exhibit early embryonic lethality resulting from generalized Notch signaling defects"].
- Fringe extension and ligand tuning: [PMID:28334865 "After O-fucosylation by POFUT1, subsequent sugar-chain extension is catalyzed by Fringe glycosyltransferases, which deliver N-acetylglucosamine to the O-linked fucose"]; the fucose on T466/EGF12 directly contacts DLL4 [PMID:28334865 "the fucose appended to T466 directly contacts three residues from the MNNL domain of DLL4"].
- IMP (PMID:28334865) to GO:0008593 regulation of Notch signaling: CRISPR POFUT1 KO in U2OS suppresses normal AND oncogenic ligand-independent Notch1 signaling; rescued by WT but impaired by active-site R240A [PMID:28334865 "Normal and oncogenic signaling are rescued by wild-type POFUT1 but rescue is impaired by an active-site R240A mutation"], and loss blocks surface delivery [PMID:28334865 "transfected Notch1 is readily delivered to the cell surface in wild-type U2OS cells, but remains intracellularly trapped in the CRISPR-engineered U2OS cells lacking POFUT1"]. This is solid IMP evidence — KEEP (regulation of Notch is downstream/non-core relative to the catalytic+ER role, but well supported).

The "Notch signaling pathway" GO:0007219 (IEA from UniProt keyword / InterPro) — POFUT1 is
not a transducing core component of Notch; it post-translationally modifies the receptor in
the ER. "regulation of Notch signaling pathway" (GO:0008593) is the more accurate framing and
is independently supported by IMP. So GO:0007219 is best modified to GO:0008593 (or kept as
non-core); GO:0008593 IMP is the anchor.

## Chaperone activity (do not over-claim for human)

Drosophila Ofut1 has an enzyme-independent chaperone activity required for Notch surface
expression; whether this extends to mammals is explicitly unresolved:
[PMID:28334865 "Whether the enzyme-independent chaperone activity of Pofut1 extends to mammals is not clear"], and mammalian data are context-dependent [PMID:28334865 "Loss of Pofut1 in mice is associated with reduced cell-surface expression of Notch1 in pre-somitic mesoderm ... but not in ES cells ... suggesting that, at least in some cell contexts, Pofut1 does not have a chaperone-like role"]. => Note the QC/folding-stabilization role (anchored to PMID:15653671 quality-control statement) but do NOT author a definitive mammalian "chaperone" molecular-function annotation. Capture as a suggested question/experiment.

## Disease

Dowling-Degos disease 2 (DDD2, MIM 615327): autosomal dominant reticulate hyperpigmentation,
caused by haploinsufficiency (LoF) of POFUT1 (UniProt DISEASE; original Li et al. 2013
PMID:23684010, not cached). Structure paper tested the 4 DDD missense mutants: all except
M262T fail to rescue Notch1 signaling [PMID:28334865 "The reported Dowling-Degos mutations of POFUT1, except for M262T, fail to rescue Notch1 signaling efficiently in the CRISPR-engineered POFUT1-/- background"]. Disease is not used as a GO annotation here but informs the Notch-dependent mechanism.

## Per-annotation disposition (GOA, 21 rows)

MF peptide-O-fucosyltransferase activity GO:0046922:
- IDA PMID:11524432 -> ACCEPT (core; recombinant human enzyme characterization)
- IDA PMID:9023546 -> ACCEPT (core; original enzyme assay / acceptor specificity)
- IDA PMID:15653671 -> ACCEPT (core)
- TAS PMID:11698403 -> KEEP_AS_NON_CORE / caution: this is a *Drosophila* genome survey of fucosylated-glycan metabolism, not a human enzymatic characterization; TAS provenance is weak but the term is correct. Flag in reference_review (MISCITED risk — better human IDA refs exist).
- IBA GO_REF:0000033 -> ACCEPT (core; PAN-GO)
- IEA GO_REF:0000120 (EC 2.4.1.221 mapping) -> ACCEPT (core)

BP protein O-linked glycosylation via fucose GO:0036066:
- IDA PMID:11524432, PMID:9023546, PMID:15653671 -> ACCEPT (this is the process directly assayed)
- IBA, IEA(InterPro) -> ACCEPT

CC endoplasmic reticulum GO:0005783:
- IDA PMID:15653671 -> ACCEPT (core; the definitive ER-localization paper)
- IBA, IEA(GO_REF:0000044), ISS(GO_REF:0000024) -> ACCEPT (concordant)

BP regulation of Notch signaling pathway GO:0008593:
- IMP PMID:28334865 -> KEEP_AS_NON_CORE (well-supported downstream consequence; core function is ER catalysis)
- IBA GO_REF:0000033 -> KEEP_AS_NON_CORE

BP Notch signaling pathway GO:0007219:
- IEA GO_REF:0000002 (InterPro keyword) -> MODIFY to GO:0008593 (POFUT1 is a modifier of the receptor, not a transducing pathway component; the regulation term is more accurate and is the curated IMP framing)

CC membrane GO:0016020:
- HDA PMID:19946888 -> MARK_AS_OVER_ANNOTATED (NK membrane-proteome MS catalog; POFUT1 is soluble ER-luminal)
- IDA PMID:11524432 -> MARK_AS_OVER_ANNOTATED (trivial/uninformative; enzyme is largely soluble, superseded by ER lumen)
- IDA PMID:9023546 -> MARK_AS_OVER_ANNOTATED (same; only 37% membrane-associated via susceptible stem)

## Falcon integration (2026-06-21)

The Falcon deep-research report (POFUT1-deep-research-falcon.md) is broadly accurate and well
aligned with the primary literature. Findings I USED:
- ER-luminal soluble localization; ER quality-control of folded EGF repeats; avoid Golgi/cytosol/nucleus/plasma-membrane locations. (Concordant with PMID:15653671, PMID:28334865.)
- GO:0046922 / EC 2.4.1.221 as the defensible core MF; folded-EGF-repeat acceptor specificity. (Concordant with PMID:9023546, PMID:11524432.)
- Notch signaling as the central downstream role; somitogenesis/hematopoiesis are tissue-specific Notch-dependent manifestations (non-core); cancer roles are pathological/context-specific and should not drive normal-process GO annotation.
- Caution against annotating direct apoptosis, pyroptosis, inflammatory signaling, synaptic remodeling.

Findings I did NOT use / treated with caution (and why):
- Falcon's citation keys (e.g. hao2025..., holdener2019...) are review-derived and many were
  NOT independently fetched/verified here; I anchored all YAML supporting_text to the six
  cached primary PMIDs in GOA, not to Falcon's reference list.
- The "Ajima 2017 ... uterine/placental angiogenesis via uPA/RhoA" attribution in Falcon's BP
  table looks like a citation-mismatch (Ajima 2017, PMID:28334865-adjacent PLoS ONE, is about
  somitogenesis point-mutants, not angiogenesis). REJECTED as a basis for any annotation;
  angiogenesis/uPA is not in GOA and not added.
- AGRN O-fucosylation / AChR clustering (from UniProt FUNCTION + Falcon): real and noted, but
  there is NO GOA annotation for it and I could not fetch a primary human POFUT1-AGRN paper
  from the cache, so I did not author a neuromuscular-junction core function; captured as a
  suggested question instead.
- HCC PD-L1 stabilization "independent of catalytic activity" (li2024): interesting but a
  single cancer-context, catalysis-independent claim; not fetched/verified, not annotated.
- Mammalian enzyme-independent chaperone activity: Falcon leans on it; primary source
  (PMID:28334865) says this is explicitly unresolved in mammals -> kept as hypothesis only.
