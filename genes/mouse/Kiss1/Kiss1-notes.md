# Mouse Kiss1 (Q6Y4S4) — curation notes

Metastasis-suppressor KiSS-1 / kisspeptin-1 precursor, 130 aa, signal peptide 1-19,
with the mature peptides metastin (kisspeptin-52, 68-119) and kisspeptin-10 (110-119),
a C-terminal tyrosine amide at Tyr119 and a region (110-119) UniProt records as
"Essential for receptor binding and receptor activation"
[file:mouse/Kiss1/Kiss1-uniprot.txt FT lines]. Two splice isoforms (Q6Y4S4-1 displayed;
Q6Y4S4-2 lacks 25-28) with no reported functional difference.

Note the rodent/human difference in the amidated C-terminal residue and in overall
precursor identity: "the active peptides (10-amino-acid residues) are highly conserved
between mouse and human KiSS1 proteins, varying by only one conserved amino acid"
[PMID:12359743 "the active peptides (10-amino-acid residues) are highly conserved
between mouse and human KiSS1 proteins"], against ~52% identity over the whole
precursor. So pharmacological cross-species transfer of the decapeptide is safe; claims
about the precursor are less so.

## Molecular activity: agonist of Kiss1r/Gpr54

Mouse Kiss1 peptide activates the mouse receptor and the Gq/PLC arm directly:
[PMID:12359743 "Activation of the receptor by KiSS1 peptide leads to the activation of
G-protein-activated phospholipase C (PLC-beta)"]. The genetic proof that the kisspeptins
are the physiological ligand is the knockout phenocopy:
[PMID:17563351 "The virtually identical phenotype of Gpr54- and Kiss1-null mice provides
direct proof that kisspeptins are the true physiological ligand for the GPR54 receptor
in vivo"]. Receptor specificity of the peptide in vivo:
[PMID:15665093 "levels of kisspeptin injected i.p., which stimulate robust LH and FSH
release in wild-type mice, have no effect in gpr54-/- mice"].

Kiss1r in mouse is on the GnRH neuron
[PMID:15665093 "GPR54 transcripts are colocalized with gonadotropin-releasing hormone
(GnRH) neurons in the mouse hypothalamus"], and the proximal cellular effect is a
depolarization of that neuron
[PMID:18483150 "Kisspeptin (100 nm) depolarized (6 +/- 1 mV) and/or evoked an 87 +/- 4%
increase in firing rate of 75% of adult GnRH neurons"], produced by a mixed conductance
change
[PMID:18483150 "a heterogeneous closure of potassium channels and opening of
nonselective cation (NSC) channels was involved in kisspeptin's depolarizing response"]
with a modest calcium rise
[PMID:18483150 "kisspeptin evoked an approximately 10% increase in intracellular calcium
levels in GnRH neurons"]. A second, Gq-independent arm reaches LH secretion through
beta-arrestin
[PMID:25147978 "Kp-dependent LH secretion was significantly diminished relative to
wild-type mice"].

## Reproductive axis: the defining mouse function

Central administration of either mature peptide drives gonadotropin secretion, and the
effect is GnRH-dependent:
[PMID:15217982 "we administered the kisspeptins directly into the lateral cerebral
ventricle of the brain and demonstrated that both peptides stimulate LH secretion"],
[PMID:15217982 "it stimulated both LH and FSH secretion, at doses as low as 1 fmol;
moreover, this effect was shown to be blocked by pretreatment with acyline, a potent
GnRH antagonist"]. The FSH arm matters for annotation: it is not a restatement of the LH
claim, and it is reproduced genetically
[PMID:17563351 "Both sexes have low circulating gonadotropin (luteinizing hormone and
follicle-stimulating hormone) and sex steroid (beta-estradiol or testosterone) hormone
levels"], [PMID:17595229 "FSH levels in both Kiss1 and Gpr54 knockout males and females
are significantly lower than in controls"].

Loss of function in mouse is hypogonadotropic hypogonadism with failure of sexual
maturation, with the pituitary and gonads themselves intact
[PMID:17563351 "Kiss1-null mice are viable and healthy with no apparent abnormalities
but fail to undergo sexual maturation"],
[PMID:17563351 "The hypothalamic-pituitary axis is functional in these mice as shown by
robust luteinizing hormone secretion after peripheral administration of kisspeptin"].

### Two hypothalamic populations

Kiss1 is expressed in the nuclei that govern gonadotropin secretion
[PMID:15217982 "KiSS-1 mRNA is expressed in areas of the hypothalamus implicated in the
neuroendocrine regulation of gonadotropin secretion, including the anteroventral
periventricular nucleus, the periventricular nucleus, and the arcuate nucleus"], and the
two populations are oppositely regulated by estradiol
[PMID:15919741 "In the arcuate nucleus (Arc), KiSS-1 expression increased after
ovariectomy and decreased with E2 treatment"],
[PMID:15919741 "in the anteroventral periventricular nucleus (AVPV), KiSS-1 expression
was reduced after ovariectomy and increased with E2 treatment"]. This is regulation *of*
the gene, so it supports no annotation on the product, but it is what separates the two
functional arms.

- Arcuate (KNDy) population — the pulse generator. The arcuate Kiss1 neurons co-express
  dynorphin and neurokinin B and their receptors
  [PMID:19776272 "Kiss1 neurons in the Arc of female mice not only express the Dyn and
  NKB genes but also the NKB receptor gene (NK3) and the Dyn receptor"], and are proposed
  to shape pulsatile kisspeptin output
  [PMID:19776272 "NKB and dynorphin act autosynaptically on kisspeptin neurons in the Arc
  to synchronize and shape the pulsatile secretion of kisspeptin and drive the release of
  GnRH from fibers in the median eminence"]. Optogenetics ties that population to LH
  pulses
  [PMID:29109258 "The selective optogenetic activation of ARNKISS neurons for 1 min
  generated pulses of LH in freely behaving mice, whereas inhibition with archaerhodopsin
  for 30 min suppressed LH pulsatility"].
- AVPV/RP3V population — the preovulatory surge. Kisspeptin signalling is required for
  GnRH-neuron activation at the surge
  [PMID:18753370 "approximately 30% of RP3V kisspeptin neurons were found to express
  c-FOS in surging mice compared with 0% in nonsurging controls"],
  [PMID:18753370 "none of the mutant mice from either line showed an LH surge or any
  GnRH neurons with c-FOS"].

The rat work behind several ISO rows agrees and is the source of the cyclicity claim
[PMID:15976058 "The blockade of local metastin action in the POA with a specific
monoclonal antibody to rat metastin completely abolished proestrous LH surge and
inhibited estrous cyclicity"],
[PMID:17213691 "anti-rat metastin/kisspeptin monoclonal antibody blocked the
estrogen-induced LH surge"].

## Bone: a second, cell-autonomous peripheral action in mouse

[PMID:38346942 "Kiss1, Gpr54 and Dusp18 knockout mice all exhibit osteoclast
hyperactivation and bone loss"]. Both whole-body and osteoclast-lineage conditional
Kiss1 deletion do it, so the relevant kisspeptin is made locally in the osteoclast
lineage, not delivered from the hypothalamus. Two separable readouts: differentiation
[PMID:38346942 "In keeping with these results, Kiss1 loss also enhanced osteoclast
formation as measured by the TRAP staining assay"] and resorptive activity with rescue
[PMID:38346942 "osteoclast resorption was promoted by Kiss1 deletion, which was
effectively rescued by ectopic expression of Kiss1"]. Mechanism is on the receptor side
[PMID:38346942 "GPR54 activation by its natural ligand Kisspeptin-10 (Kp-10) causes
Dusp18 to dephosphorylate Src at Tyr 416"]. Single study (with a published erratum,
PMID:39702286), hence non-core here, as on the receptor.

## Reproductive tract outside the brain

Uterine arm: Kiss1 and Gpr54 rise during mouse decidualization and knockdown blocks it
in cultured stromal cells
[PMID:24830702 "KISS-1 and GPR54 proteins were spatiotemporally expressed in
decidualizing stromal cells in intact pregnant females"],
[PMID:24830702 "the attenuated expression of Kiss1 using small interfering RNA
approaches significantly blocked the progression of stromal cell decidualization"].
In vitro and single-study; and whole-animal Kiss1-null uterine phenotypes are confounded
by the hypogonadism.

Placental arm: this is where mouse and human part company. In mouse the gene is
essentially not a placental hormone
[PMID:25468546 "both Gpr54 and Kiss1 are expressed in the mouse placenta but Kiss1 mRNA
levels are very low"], [PMID:25468546 "Stereological measurements found no differences
between Kiss1 mutant and wild-type placentas"], [PMID:25468546 "the expression level of
the Kiss1 gene in the mouse placenta is so low as to be of questionable physiological
significance"]. So the human review's second core function (syncytiotrophoblast-derived
circulating kisspeptin restraining extravillous trophoblast) has no mouse counterpart and
is deliberately not carried over.

## Rat-only claims arriving by ISO, and how far they travel

- `GO:0060124` positive regulation of growth hormone secretion — rat pituitary cell
  culture only [PMID:17532794 "induced dose-related LH and growth hormone (GH) secretory
  responses, which were nevertheless of lower magnitude than those evoked by the primary
  regulators GnRH and GH-releasing hormone"], and the authors themselves defer the
  question [PMID:17532794 "The precise relevance and underlying mechanisms of this
  potential new actions of kisspeptins"]. Over-annotation for mouse.
- `GO:0016324` apical plasma membrane — rat oviduct immunoreactivity
  [PMID:17503086 "IR has been localized at the adluminal surface and the cytoplasmic
  domain of secretory cells"]. That is the secretory pole of an epithelium the peptide is
  leaving, not a site of action, and there is no mouse oviduct data. Over-annotation.
- `GO:0050806` positive regulation of synaptic transmission — rat hippocampus
  [PMID:16222076 "activation of GPR54 by submicromolar concentrations of metastin
  reversibly enhances excitatory synaptic transmission in hippocampal dentate granule
  cells in a mitogen-activated protein (MAP) kinase-dependent manner"]. Submicromolar
  agonist, no mouse replication; kept non-core, as on mouse Kiss1r.
- `GO:0043025` neuronal cell body — rat [PMID:15976058 "Metastin neurons were
  immunohistochemically found in the arcuate nucleus (ARC) to be colocalized with
  estrogen receptors"]; mouse kisspeptin-immunoreactive neurons are also described
  [PMID:18753370 "approximately 30% of RP3V kisspeptin neurons were found to express
  c-FOS in surging mice compared with 0% in nonsurging controls"]. True but it is where
  the peptide is before release, not where it acts.
- Secretion of the peptide itself was measured in rat hypothalamic cultures
  [PMID:17698953 "The production and secretion of kisspeptin in cultured hypothalamic
  neurons and GT1-7 cells were detected by a specific RIA"],
  [PMID:16339453 "The results support the hypothesis that metastin stimulates GnRH
  secretion from the hypothalamus"], which is the donor evidence behind the extracellular
  ISO rows.

## Open biological questions noted while reviewing

1. Kiss1-null is milder and bimodal relative to Gpr54-null on the same background
   [PMID:17595229 "Kiss1 knockout mice appear to be less severely affected than their
   receptor counterparts"], [PMID:17595229 "Kiss1 knockout females demonstrate two
   distinct phenotypes"], and the ligand-null animals still respond to agonist
   [PMID:17595229 "Gpr54 knockout mice fail to increase gonadotropins, whereas Kiss1
   knockout mice respond with increased gonadotropin levels"]. Whether this means
   ligand-independent Kiss1r activity, a second ligand, or strain/targeting differences is
   unresolved, and it bears on whether receptor-derived ISO rows should transfer to the
   ligand at all.
2. The processing enzymes for the *mouse* precursor are not established; furin was shown
   in human cell lines only, and nothing was found for mouse.
3. What local uterine kisspeptin does in vivo, given the systemic hypogonadism of the
   null and the negligible placental expression, needs a conditional uterine deletion.

## Annotation decisions worth recording

- `GO:0032278` positive regulation of gonadotropin secretion is kept (not treated as a
  redundant parent of `GO:0033686`) because the FSH arm is separately demonstrated in
  mouse by both pharmacology and genetics. The human KISS1 review had no such row to
  judge and declined to propose the parent; this is a deliberate, evidence-based
  divergence, not an inconsistency.
- `GO:0048018` receptor ligand activity is kept as the core MF, as in the human review
  and in GO's own GO-CAM models of the pathway. The descendants `GO:0160041` neuropeptide
  activity ("The receptor ligand activity of any polypeptide expressed in, and secreted
  from a neuron") and `GO:0005184` neuropeptide hormone activity fit the hypothalamic arm,
  and the mouse case for them is stronger than the human one because the placental arm is
  absent here — but the uterine stromal arm is not neuronal, so the parent remains the
  term true of all the mouse evidence. Raised as a question instead of asserted, and in
  any case a descendant of a term the gene already carries.
- `GO:0007186` rows are modified to `GO:0007200` (direct mouse evidence, Stafford) and
  `GO:0007218` (neuropeptide pathway), matching the human review and the receptor review.
- One `NEW` row: `GO:0045671` negative regulation of osteoclast differentiation, which is
  a separate branch from the annotated `GO:0045779` and is what the TRAP-staining result
  shows. Comparator check: mouse secreted ligands carry this term (Calca, Il4, Ifng,
  Ifnb1, Erfe, Sfrp1, Tnfaip6 among 55 annotations), so a secreted peptide agonist
  carrying it is conventional, and the mouse Kiss1r review added the same term on the
  receptor side.
- No GO term exists for GnRH secretion or its regulation (checked against QuickGO's
  ontology search: the matches are GnRH binding, receptor activity, receptor binding, and
  GnRH-neuron development terms), so the proximal action of this peptide is recorded one
  step downstream as regulation of LH/gonadotropin secretion.
- `just paint-losses mouse Kiss1` reports no IRD or IKR on this gene's lineage, so the
  four IBA rows are current.
