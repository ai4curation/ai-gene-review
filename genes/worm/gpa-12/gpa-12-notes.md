# gpa-12 (C. elegans) — research notes

UniProt: Q19572 (GPA12_CAEEL) · WormBase: WBGene00001674 / F18G5.3 · 355 aa · Chromosome X

## Summary / identity

GPA-12 is a heterotrimeric guanine-nucleotide-binding protein alpha subunit of the
**Gα12/13 subfamily** (InterPro IPR000469 Gprotein_alpha_12/13; PRINTS PR00440 GPROTEINA12;
PANTHER PTHR10218 "GTP-binding protein alpha subunit"). It is the C. elegans homolog of
mammalian Gα12/Gα13 [PMID:12646136 "a C. elegans Galpha subunit gene, gpa-12, which is a
homolog of mammalian G(12)/G(13)alpha, and found that animals defective in gpa-12 are viable"].
The protein has the canonical G-alpha domain with all five G-box GTP/Mg2+-binding motifs
(G1 31–44 … G5 325–330; UniProt) and N-terminal cysteines (…MVCCFGKK…) typical of
membrane-anchored Gα subunits.

## KNOWN (well supported)

### Molecular function
- **G protein (Gα) GTP/GDP molecular switch — GO:0003925 G protein activity.** Family
  membership and the intact G1–G5 nucleotide-binding motifs (UniProt) support intrinsic
  guanine-nucleotide binding and GTPase-based cycling. The functional read-out of the switch
  is demonstrated genetically: a Q205L substitution in the catalytic Gln (the residue whose
  mutation blocks GTP hydrolysis in Gα subunits) yields a **constitutively active** GPA-12
  that drives constitutive antimicrobial-peptide gene expression [UniProt MUTAGEN Q205L,
  ECO:0000269|PMID:22470487]. Intrinsic GTPase activity of the worm protein has not been
  measured biochemically (inferred from homology + the behavior of the GQ→L mutant).
- Assembles into a **heterotrimeric G protein complex** (Gα·Gβγ). The curated GO-CAM
  (gomodel:5b91dbd100002057) models GPA-12's molecular function as **GO:0031683 G-protein
  beta/gamma-subunit complex binding**, partnered in the pathway with the Gβ RACK-1.

### Biological process — epidermal antifungal innate immunity (the core physiological role)
- Required for **antifungal innate immune response / defense response to fungus** in the
  epidermis: GPA-12 signaling is needed for infection- and wounding-induced up-regulation of
  antimicrobial peptides of the NLP (nlp-29 cluster) and CNC families
  [PMID:19380113 IMP; PMID:22470487 IMP].
- **Genetic pathway position (epistasis):** GPA-12/G-protein signaling acts **upstream of**
  PKCδ (TPA-1) and a conserved p38 MAPK cassette (TIR-1 → NSY-1 → SEK-1 → PMK-1) →
  STAT-like STA-2, driving nlp/cnc gene expression [PMID:19380113 "This involves G protein
  signaling and specific C-type phospholipases acting upstream of PKCdelta"; "C. elegans PKC
  acts through the p38 MAPK pathway to regulate nlp-29"]. In PMID:22470487:
  "Wounding and infection require G-protein signaling, involving the Gα protein GPA-12 and the
  Gß RACK-1, while infection specifically involves the Tribbles-like kinase NIPI-3".
- **Gain-of-function drives the effector program:** epidermis-restricted expression of active
  GPA-12* (Pcol-19::GPA-12*) causes marked constitutive Pnlp-29::GFP expression
  ["In uninfected transgenic worms carrying the Pcol-19::GPA-12* construct, we observed a very
  marked increase in the expression of Pnlp-29::GFP in the epidermis from the late L4 stage
  onwards"] and constitutive nlp/cnc transcript induction ["the transgenic strain exhibited an
  elevated constitutive expression of nlp-29, nlp-31 and nlp-34, and cnc-1, cnc-4"]; this
  effect is abrogated in a nipi-4 (downstream pseudokinase) mutant ["When we crossed the
  Pcol-19::GPA-12* transgene into nipi-4(fr106) mutant, the elevated expression of the
  Pnlp-29::GFP reporter provoked by the active form of GPA-12 was abrogated"] (all
  PMID:22470487). → supports **positive regulation of gene expression (GO:0010628, IMP)**.
- **GO-CAM causal structure** (gomodel:5b91dbd100002057, "Antifungal innate immune response in
  the hypodermis via MAPK cascade"): GPA-12 activity is causally **upstream, positive effect**
  (RO:0002304) of TPA-1 activity, within GO:0061760 antifungal innate immune response
  (evidence PMID:19380113). Consistent with the literature.

### A second, developmental context (Gα12 gain-of-function)
- Activated **GPA-12 (G12QL) causes a developmental growth arrest** via a feeding defect
  (reduced pharyngeal pumping); genetic suppressors map to **tpa-1** (PKCθ/δ), placing TPA-1
  downstream of G12 signaling here too [PMID:12646136 "Expression of activated GPA-12 (G(12)QL)
  results in a developmental growth arrest caused by a feeding behavior defect that is due to a
  dramatic reduction in pharyngeal pumping"; "TPA-1 is a downstream target of both G(12)
  signaling and PMA in modulating feeding and growth in C. elegans"]. gpa-12 loss-of-function
  animals are viable (i.e. not essential).

### Localization
- WormBase IDA: **cytoplasm (GO:0005737)** and **nucleus (GO:0005634)** [PMID:12646136, IDA].
  Full text of PMID:12646136 is not in cache (abstract-only); the localization data are in the
  full text I cannot read. Cytoplasmic/peripheral-membrane localization is expected for a Gα;
  nuclear localization of a Gα is unusual — I defer to the WormBase curator but treat these as
  non-core.

## NOT known / genuine knowledge gaps
- **Cognate receptor / activating input.** The receptor(s) and ligand(s) that activate GPA-12
  to launch epidermal immune signaling, and whether GPA-12 couples directly to a damage-sensing
  GPCR, are not established from the cached primary literature. PMID:22470487 states the
  upstream elements are only partly defined ("Our current understanding of both epidermal and
  intestinal innate immunity is far from complete"). (A candidate epidermal GPCR, DCAR-1,
  has been reported elsewhere in the field, but that paper is not in the cache and the direct
  GPA-12↔receptor biochemical coupling is not shown here.)
- **Direct downstream effector.** Genetic epistasis places GPA-12 upstream of PLC-3 / TPA-1
  (PKCδ) and the p38 cascade, but the *immediate biochemical* effector of GPA-12 is unproven.
  Notably, the canonical mammalian Gα12/13 effector arm (RhoGEF → Rho; GO:0007266 Rho protein
  signal transduction) has not been demonstrated for the worm protein; in worm the demonstrated
  arm runs through phospholipase/PKCδ, which is more Gq-like. Whether GPA-12 directly engages a
  RhoGEF, a phospholipase, or another effector is unresolved.
- **Tissue-restricted requirement / broader physiology.** GPA-12 is required for AMP induction
  in the hyp7 epidermal syncytium (UniProt DISRUPTION PHENOTYPE, from PMID:19380113 full text),
  and activated G12 separately perturbs pharyngeal pumping/feeding (PMID:12646136). The full
  endogenous tissue/behavioral repertoire of GPA-12, and why the immune requirement is
  epidermis/cell-type restricted, are not resolved.

## Annotation review plan (existing_annotations, 20 total)
- ACCEPT (core): GO:0003925 G protein activity (IBA); GO:0061760 antifungal innate immune
  response (IMP); GO:0050832 defense response to fungus (IMP, ×2); GO:0007186 GPCR signaling
  pathway (IEA); GO:0007266 Rho protein signal transduction (IBA) [canonical G12/13 effector,
  homology]; GO:0005834 heterotrimeric G-protein complex (IBA, part_of); GO:0010628 positive
  regulation of gene expression (IMP).
- ACCEPT / KEEP_AS_NON_CORE (true but generic or supporting): GO:0003924 GTPase activity (IEA);
  GO:0019001 guanyl nucleotide binding (IEA); GO:0031683 G-protein beta/gamma-subunit complex
  binding (IEA); GO:0001664 GPCR binding (IEA); GO:0007165 signal transduction (IEA, generic);
  GO:0007266 Rho signal transduction (IEA, redundant with IBA); GO:0005737 cytoplasm (IBA & IDA).
- KEEP_AS_NON_CORE / defer: GO:0005634 nucleus (IDA) — unusual for a Gα, full text unavailable.
- REMOVE / MARK_AS_OVER_ANNOTATED (over-propagated to this G12/13 worm protein):
  - GO:0007188 adenylate cyclase-modulating GPCR signaling pathway (IBA) — REMOVE: cAMP/adenylate
    cyclase modulation is a Gs/Gi function; G12/13 subfamily does not signal this way (pan-Gα
    PANTHER node PTN000026392 over-propagation).
  - GO:0031752 D5 dopamine receptor binding (IBA) — REMOVE: hyper-specific mammalian receptor;
    no worm ortholog/evidence.
  - GO:0031526 brush border membrane (IBA) — MARK_AS_OVER_ANNOTATED: mammalian intestinal
    microvillar location; GPA-12 acts in epidermis; no worm evidence.

## Key references (cached)
- PMID:12646136 — van der Linden et al. 2003, Curr Biol. gpa-12 = Gα12/13 homolog; active G12QL
  → growth arrest via feeding/pharyngeal-pumping defect; TPA-1/PKC downstream. (abstract-only)
- PMID:19380113 — Ziegler et al. 2009, Cell Host Microbe. PKCδ links G-protein signaling and the
  p38 MAPK cascade in antifungal immunity; GPA-12 upstream of TPA-1/p38 → nlp-29. (abstract-only)
- PMID:22470487 — Labed et al. 2012, PLoS One. NIPI-4 pseudokinase downstream of TPA-1;
  epidermal GPA-12* drives constitutive nlp/cnc AMP expression, nipi-4-dependent. (full text)
- GO-CAM gomodel:5b91dbd100002057 — antifungal innate immune response in the hypodermis via MAPK
  cascade; GPA-12 (Gβγ-binding) causally upstream (+) of TPA-1.
</content>
