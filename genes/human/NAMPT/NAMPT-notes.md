# NAMPT (P43490) review notes

Human NAMPT (nicotinamide phosphoribosyltransferase; also PBEF / PBEF1 / visfatin).
HGNC:30092, chromosome 7, 491 aa. EC 2.4.2.12.

## Core enzymatic identity

NAMPT is the rate-limiting enzyme of the NAD+ salvage pathway. It condenses
nicotinamide with 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to yield
nicotinamide mononucleotide (NMN), the immediate precursor of NAD+.

UniProt FUNCTION:
[file:human/NAMPT/NAMPT-uniprot.txt "Catalyzes the condensation of nicotinamide with 5-"] +
[file:human/NAMPT/NAMPT-uniprot.txt "phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an"] +
"intermediate in the biosynthesis of NAD. It is the rate limiting component in the
mammalian NAD biosynthesis pathway." (UniProt wraps these lines with the `CC` prefix;
each verbatim quote below is confined to a single line.)

Verbatim single-line UniProt quotes usable as supporting_text:
- "phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, an"
- "intermediate in the biosynthesis of NAD. It is the rate limiting"
- "Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-" (PATHWAY line)
- "Homodimer. {ECO:0000269|PubMed:16783377}." (SUBUNIT)
- "Nucleus {ECO:0000269|PubMed:24130902}. Cytoplasm" (SUBCELLULAR LOCATION)

CATALYTIC ACTIVITY (RHEA:16149; EC 2.4.2.12) is written right-to-left in UniProt
(beta-nicotinamide D-ribonucleotide + diphosphate = PRPP + nicotinamide + H+); the
physiological direction is right-to-left, i.e. NAM + PRPP -> NMN + PPi.

EC/MF is well supported experimentally by crystal structures with substrate/product
and inhibitor FK866 [PMID:16783377] and by mechanistic/phosphoenzyme studies
[PMID:19666527]. Catalytic residues D219 (substrate specificity), H247
(phosphohistidine, activated by ATP), R311 are established by mutagenesis
[PMID:16783377 "Asp219 is a determinant of substrate specificity"] and
[PMID:19666527 "ATP-phosphorylation of an active-site histidine causes catalytic activation, increasing NAM affinity by"].

## Two forms: intracellular (iNAMPT) enzyme vs secreted (eNAMPT/visfatin) cytokine

UniProt: "The secreted form behaves both as a cytokine with immunomodulating
properties and an adipokine with anti-diabetic properties, it has no enzymatic
activity, partly because of lack of activation by ATP".
Verbatim single-line quotes:
- "behaves both as a cytokine with immunomodulating properties and an"
- "adipokine with anti-diabetic properties, it has no enzymatic activity,"

Origin of the "visfatin"/PBEF names: originally cloned as a secreted pre-B-cell
colony-enhancing factor (PBEF), a putative cytokine synergizing with SCF+IL-7 for
pre-B colony formation [PMID:8289818 "define PBEF as a novel cytokine which acts on early B-lineage precursor cells"].
Note PBEF itself had no direct colony activity — it synergized:
[PMID:8289818 "PBEF itself had no activity but synergized the pre-B-cell colony formation activity of stem"].

The "visfatin = insulin-mimetic hormone" claim is CONTESTED. Revollo et al. showed
eNAMPT does NOT exert insulin-mimetic effects but instead has robust NAD-biosynthetic
activity and acts systemically via NMN:
[PMID:17983582 "eNampt does not exert insulin-mimetic effects in vitro or in vivo but rather exhibits robust NAD"].
GOA correctly records the insulin-receptor-signaling and adipose-development
annotations from this paper as NOT (negated). Keep as negated.

## Extracellular pro-inflammatory action depends on enzyme (NAMPT) activity

Romacho et al.: extracellular PBEF/NAMPT/visfatin induces iNOS in human aortic
smooth muscle cells via ERK1/2 -> NF-kappaB, and this depends on its intrinsic NAMPT
enzymatic activity (NMN mimics the effect; the NAMPT inhibitor APO866 blocks it):
[PMID:19727662 "Through its intrinsic NAMPT"] + "activity, ePBEF/NAMPT/visfatin appears to be a direct contributor to vascular inflammation".
Verbatim single-line quotes:
- "ePBEF/NAMPT/visfatin (10-250 ng/ml) induced iNOS in a"
- "triggered a biphasic ERK 1/2 activation"
- "elicited a sustained \nactivation of NF-kappaB" -> use "activation of NF-kappaB and triggered a biphasic ERK 1/2 activation." (single line 70)
- "exogenous nicotinamide mononucleotide, the product"
- "of NAMPT activity, mimicked NF-kappaB activation and iNOS induction by"

This paper grounds the GOA annotations: inflammatory response (IDA), positive
regulation of gene expression (iNOS), positive regulation of NF-kappaB (IDA),
positive regulation of ERK1/2 cascade (IDA), and NAMPT activity (IMP). These are
genuine but represent the secreted-cytokine physiology, not the core enzymatic MF;
treat the signaling/inflammation BP terms as KEEP_AS_NON_CORE.

## Subcellular location

- Cytosol/cytoplasm: primary site of the NAD-salvage enzyme. Reactome TAS + ISS from
  mouse ortholog Q99KQ4. ACCEPT cytosol as core.
- Nucleus: intranuclear granular pattern in non-inflamed endothelial cells
  [PMID:24130902 "visfatin predominantly showed an intra-nuclear granular pattern"] and
  UniProt SUBCELLULAR LOCATION "Nucleus {ECO:0000269|PubMed:24130902}". Real; the
  enzyme supplies NAD to nuclear NAD-consumers (sirtuins, PARPs). KEEP_AS_NON_CORE.
- Secreted / extracellular region: eNAMPT/visfatin is genuinely released despite
  lacking a signal peptide; secreted into milk at ~100x serum levels
  [PMID:21741723 "visfatin is abundantly secreted into"] and by inflamed endothelium
  [PMID:24130902 "IL-1β promoted \nvisfatin secretion"]. KEEP_AS_NON_CORE (secreted form).
- Extracellular exosome (GO:0070062): HDA from two large exosome-proteomics datasets
  [PMID:23533145 prostatic-secretion exosomes; PMID:20458337 B-cell exosomes]. These
  are high-throughput proteomic detections; keep as non-core.

## Circadian role

By-similarity (mouse Q99KQ4): NAMPT-dependent oscillatory NAD production regulates
clock-target gene expression by releasing CLOCK-BMAL1 from SIRT1-mediated suppression.
UniProt: "Plays a role in the modulation of circadian clock function." IEA (Ensembl)
and ISS annotations for circadian rhythm / circadian regulation of gene expression.
Real but derivative of enzymatic NAD output; KEEP_AS_NON_CORE.

## Protein-binding annotations (IPI / IEA)

- GO:0005515 protein binding, IPI PMID:18486613: PBEF interacts with FTL (P02792),
  IFITM3 (Q01628), MT-ND1 (P03886) in pulmonary endothelial cells (oxidative-stress
  context). [PMID:18486613 "interactions between PBEF and NADH dehydrogenase subunit"].
  Bare "protein binding" — uninformative MF; MARK_AS_OVER_ANNOTATED (do not REMOVE, IPI).
- GO:0005515 protein binding, IPI PMID:32296183: HuRI binary interactome (high-throughput
  Y2H); interactor USP49 (Q70CQ1-2). MARK_AS_OVER_ANNOTATED.
- GO:0042802 identical protein binding, IPI PMID:16783377 and PMID:19666527: NAMPT is a
  homodimer, well supported [PMID:16783377 "SUBUNIT" homodimer; from UniProt
  "Homodimer. {ECO:0000269|PubMed:16783377}."]. Homodimerization is functionally real
  (the FK866 site and active site lie at the dimer interface), so ACCEPT / KEEP_AS_NON_CORE
  rather than over-annotated. GO:0042802 IEA (GO_REF:0000120) is redundant with these.

## PMID:23001182 positive regulation of transcription by RNA Pol II (IDA)

This paper is primarily about HCLS1/HAX1/LEF-1 in granulopoiesis. It references the
Nampt-NAD+-SIRT1 pathway as an upstream trigger of G-CSF-induced granulopoiesis
[PMID:23001182 "G-SCF induces granulopoiesis via upregulation \nof the Nampt-NAD+-SIRT1 pathway"],
but NAMPT is treated as a pathway component whose mRNA is measured as a control; the
paper does not demonstrate NAMPT acting directly as a Pol II transcriptional activator.
The BHF-UCL IDA "positive regulation of transcription by RNA polymerase II" is an
indirect/over-reaching call — MARK_AS_OVER_ANNOTATED (not REMOVE; it is an experimental
IDA and the curator read the full text). Cannot find verbatim support for NAMPT itself
positively regulating Pol II transcription as a direct effector.

## PMID:8289818 cytokine/signaling/proliferation TAS (ProtInc, 1994)

Original PBEF cloning paper. Supports "novel cytokine" framing and B-lineage synergy.
TAS annotations: cytokine activity, signal transduction, cell-cell signaling, positive
regulation of cell population proliferation. These reflect the secreted eNAMPT/PBEF
biology. cytokine activity is genuine for the secreted form -> KEEP_AS_NON_CORE. The
generic signal transduction / cell-cell signaling / proliferation TAS are legacy 2003
ProtInc annotations that are vague; positive regulation of cell population proliferation
was a synergistic effect (PBEF alone had no activity) -> MARK_AS_OVER_ANNOTATED for the
proliferation term; KEEP_AS_NON_CORE for cytokine activity, signal transduction,
cell-cell signaling (broad but consistent with the cytokine role).

## nicotinate metabolic process (GO:1901847) TAS Reactome R-HSA-196807

Reactome groups the NAMPT reaction under "Nicotinate metabolism". NAMPT's substrate is
nicotinamide (an amide), not nicotinate; the more precise process is NAD+ biosynthesis /
salvage. Keep as non-core (broad grouping term), do not REMOVE (TAS).

## Summary of core functions

- MF: GO:0047280 nicotinamide phosphoribosyltransferase activity (EC 2.4.2.12).
- BP: GO:0034355 NAD+ biosynthetic process via the salvage pathway (rate-limiting step).
  (GO:0009435 NAD+ biosynthetic process is the broader GOA-seeded term; salvage is more precise.)
- CC: GO:0005829 cytosol (primary catalytic compartment).

Non-core but real: secreted/extracellular cytokine-adipokine (eNAMPT/visfatin), nucleus,
circadian modulation, homodimerization, pro-inflammatory signaling of the secreted form.
Negated (per PMID:17983582): insulin receptor signaling pathway; adipose tissue development.
</content>
</invoke>
