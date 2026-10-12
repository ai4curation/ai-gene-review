# smo (Drosophila melanogaster, UniProt P91682) — curation notes

Research journal for the GO annotation review. Entries are appended; inline citations give the
PMID and the supporting text quoted from the cached publication.

## 1. What the protein is

`smoothened` was cloned as a segment-polarity gene required for cells to *respond* to Hedgehog,
and the sequence immediately suggested a receptor: [PMID:8700230 "Sequence analysis of the
smoothened transcription unit reveals a single open reading frame encoding a protein with seven
putative transmembrane domains. This structure is typical of G-protein-coupled receptors,
suggesting that the Smoothened protein may act as a receptor for the Hedgehog ligand."]. The same
paper established the genetic requirement: [PMID:8700230 "the segment-polarity gene smoothened is
required for the response of cells to hedgehog signalling during the development of both the
embryonic segments and imaginal discs"].

Patched, not Smo, binds the ligand; Ptc acts on Smo [PMID:8898207 "Hh binds to Ptc, or a Ptc-Smo
complex, and thereby induces Smo activity"].

UniProt topology (smo-uniprot.txt): 1036 aa, signal/precursor, seven transmembrane segments
spanning residues 259–553, and a cytoplasmic TOPO_DOM of 554–1036. That ~480-residue C-terminal
tail is the single most important structural difference from vertebrate SMO (787 aa in human, with
a much shorter tail), and it is where nearly all the fly-specific regulation happens.

## 2. The activation cycle: Ptc off-state, phosphorylation, surface accumulation

Hedgehog inverts the fates of the two membrane proteins [PMID:10966113 "Hedgehog causes
phosphorylation, stabilization, and accumulation of Smoothened at the cell surface."]. Surface
accumulation is not a side effect but the readout of activation
[PMID:15616566 "phosphorylation-deficient forms of Smo fail to accumulate on the cell surface and
are unable to transduce the Hh signal"], and the dose-response is graded
[PMID:15616566 "Our data indicate that Hh induces progressive Smo phosphorylation by PKA and CKI,
leading to elevation of Smo cell-surface levels and signalling activity."].

Mass spectrometry mapped the sites: [PMID:15598741 "we identify here 26 serine/threonine residues
within the Smo C-terminal cytoplasmic tail that are phosphorylated in Hh-stimulated cells"], and
genetics showed the PKA/CK1 cluster architecture mirrors the one on Ci
[PMID:15592457 "a cluster of protein kinase A and protein kinase A-primed casein kinase 1
phosphorylation sites in Smoothened, similarly distributed to those regulating Ci, are essential
for Smoothened to transduce a Hh signal"].

The mechanism of the switch is electrostatic
[PMID:17960137 "The Arg clusters inhibit SMO by blocking its cell surface expression and keeping it
in an inactive conformation that is maintained by intramolecular electrostatic interactions."] and
the output is dimerisation
[PMID:17960137 "HH-induced phosphorylation disrupts the interaction, and induces a conformational
switch and dimerization of SMO cytoplasmic tails, which is essential for pathway activation."].
The three serine clusters are read in order, not in bulk
[PMID:22537496 "We propose a zipper-lock model in which the gradual phosphorylation at these
clusters induces a gradual conformational change in the Smo cytoplasmic tail, which promotes the
interaction between Smo and Costal2 (Cos2)."].

Additional layers on the same tail:
- **Gprk2** phosphorylates and also scaffolds: [PMID:20844016 "Gprk2 promotes Smo activation by
  phosphorylating Smo C-terminal tail (C-tail) at Ser741/Thr742, which is facilitated by PKA and
  CK1 phosphorylation at adjacent Ser residues."]; and it drives the opposite arm of the cycle
  [PMID:19850026 "we provide evidence that Gprk2 promotes Smo internalization subsequent to its
  activation, most likely by direct phosphorylation"]. Gprk2 also acts indirectly through cAMP
  [PMID:22096079 "loss of Gprk2 resulted in a decrease in cellular cAMP concentrations to a level
  that was limiting for Hh target gene activation"].
- **Ubiquitination** opposes accumulation: [PMID:22253574 "Hh inhibits Smo ubiquitination via
  PKA/CK1-mediated phosphorylation of SAID, leading to Smo cell surface accumulation."], countered
  by USP8 [PMID:22253573 "USP8 promotes the accumulation of Smo at the cell surface and prevents
  localization to the early endosomes, presumably by deubiquitinating Smo."].
- **Trafficking**: [PMID:36083801 "We provide evidence that HH promotes the stabilization of SMO by
  switching its fate after endocytosis toward recycling."] and, at the highest Hh levels,
  [PMID:36083801 "Moreover, in the presence of very high levels of HH, the second effect of FU leads
  to the local enrichment of SMO in the most basal domain of the cell membrane."].
- **Extracellular loops** matter too: [PMID:22223683 "We provide in vitro and in vivo evidence that
  EC1 cysteine mutation induces significant Hh-independent Smo signaling, triggering a level of
  pathway activation similar to that of a maximal Hh response in Drosophila and mammalian systems."].

## 3. The C-tail as an adaptor: Costal-2 and Fused

This is the core fly-specific mechanism and the reason so many `protein binding` rows exist.

[PMID:14597665 "Smo physically interacts with Costal2 (Cos2) and Fused (Fu) through its C-tail.
Deletion of the Cos2/Fu-binding domain from Smo abolishes its signaling activity."] — binding and
function map to the same segment.

Directness was established by two-hybrid plus co-IP
[PMID:14614827 "Combined with our immunoprecipitation and immunofluorescence data, our yeast
two-hybrid results provide strong evidence that Smo and Cos2 directly associate and that the
association occurs within the intracellular signaling portion of Smo."], with
[PMID:14614827 "Both Cos2 and Fu coimmunoprecipitated specifically with both Smo antisera but were
not detected in the control immunoprecipitation."].

Independently: [PMID:14636583 "Smo associates directly with a Ci-containing complex that is
scaffolded and stabilized by the atypical kinesin, Costal-2 (Cos2)"] and
[PMID:14523402 "we find that the Cos2-Fu-Ci protein complex is associated with Smo in membrane
fractions both in vitro and in vivo"].

The functional consequence is recruitment to the membrane
[PMID:21844892 "Collectively, our data indicate that, in response to a Hh gradient and Smo activity,
the Cos2/Fu complex is recruited to the cell membrane through an interaction between Smo and
Cos2."] and, explicitly,
[PMID:21844892 "Our findings suggest that the phosphorylated C-terminus of Smo recruits the Cos2/Fu
complex to the membrane through the interaction between Smo and Cos2, which further induces Fu
dimerization."]. Concentration at the membrane is what activates Fused
[PMID:21664578 "Here we show that the Fused (Fu) protein kinase is activated by Smo and Cos2 via
Fu- and CK1-dependent phosphorylation."] and
[PMID:21852395 "Here, we show that Hh-induced Smo conformational change recruits Costal2 (Cos2)/Fused
(Fu) and promotes Fu kinase domain dimerization."].

**Curation consequence.** This is why the bare `GO:0005515 protein binding` rows whose partner is
Costal-2 were modified to `GO:0030674 protein-macromolecule adaptor activity` rather than removed.
Smo is not merely in a complex with Cos2; its phosphorylated tail is the element that brings the
complex to the membrane, and deleting just that segment kills signalling. `modules/hedgehog_signaling.yaml`
assigns the same term to its `smo_tail_recruitment` annoton, so the review and the module agree.

Fused also binds Smo directly, and this is a reciprocal loop:
[PMID:17182028 "we show that the regulatory domain of FU physically interacts with the last 52 amino
acids of SMO and that the two proteins colocalize in vivo to vesicles"];
[PMID:17658259 "We show here that HH induces FU targeting to the plasma membrane in a SMO-dependent
fashion and that, reciprocally, FU controls SMO stability and phosphorylation."];
[PMID:30541874 "we show that the last amino acids of the cytoplasmic tail of Smo, in combination with
G protein-coupled receptor kinase 2 (Gprk2), bind to the regulatory domain of Fused (Fu) and highly
activate its kinase activity"]; and the feedback also runs through Cos2
[PMID:17671093 "Our data suggest that Cos2-Smo interaction blocks Hh-induced Smo phosphorylation, and
that Fu promotes Smo phosphorylation by antagonizing Cos2."].

PKA binds the tail as well, and Hh switches its preferred substrate:
[PMID:24985345 "We found that in cells exposed to Hh, the catalytic subunit of PKA (PKAc) bound to
the juxtamembrane region of the carboxyl terminus of Smo."];
[PMID:25289679 "Here we show that Hh signalling activation causes PKA to switch its substrates from
Ci to Smo within the Hh signalling complex (HSC)."].

## 4. Canonical GPCR behaviour

[PMID:18987629 "Here we present in vitro and in vivo evidence in Drosophila that Smo activates a G
protein to modulate intracellular cyclic AMP levels in response to Hh."] and
[PMID:18987629 "Our results demonstrate that Smo functions as a canonical GPCR, which signals through
Galphai to regulate Hh pathway activation."]. This supports both `GO:0004930` (IDA) and
`GO:0007193` (IMP), and is the basis for modifying the broad InterPro `GO:0004888` row.

## 5. Lipid regulation — the fly's ligands are not (demonstrably) sterols

Vertebrate SMO is activated by cholesterol/oxysterols occupying the CRD and a transmembrane channel.
In the fly the demonstrated lipid ligands are different:

- PI(4)P: [PMID:26863604 "We further found that PI(4)P directly binds Smo through an arginine motif,
  which then triggers Smo phosphorylation and activation."], with a clean separation-of-function
  mutant: [PMID:26863604 "we generated the Arg to Ala mutation in Smo full-length (Myc-SmoRA4) and
  found that Myc-SmoRA4 lost both the ability to bind PI(4)P (Fig 3J) and the interaction with
  Cos2-Fu complex (Fig 3K)"]. Note this ties lipid binding directly to the adaptor function.
- Phosphatidic acid: [PMID:37847757 "Smo also interacted with PA in vitro through a binding pocket
  located in the transmembrane region, and mutating residues in this pocket reduced Smo activity in
  vivo and in cells."].

UniProt's FUNCTION line carries "Activated by cholesterol in response to hedgehog (hh) morphogen"
but flags it `By similarity` (from human Q99835), not as fly evidence. Recorded as a
`suggested_questions` entry rather than asserted.

## 6. The cilium question (the specific issue this review was asked to settle)

`interpro/panther/PTHR11309/PTHR11309-review.yaml` records `assessment: UNRESOLVED` for
`GO:0005929 cilium` at PAINT node `PANTHER:PTN000885245`, because the node asserts cilium for all
eumetazoan Smoothened descendants while fly Hh signalling is famously cilium-independent — yet
`FB:FBgn0003444` (this gene) is one of the seeds. The family review could not inspect the fly
annotation offline and flagged it rather than pruning it.

**It resolves in favour of the node.** The fly GOA record carries its own experimental ciliary
annotation, `GO:0005929 cilium`, evidence `IDA`, reference `PMID:24768000` (Kuzhandaivel et al.,
*Cell Rep* 2014), qualifier `located_in`. The paper is exactly on point:

- [PMID:24768000 "Drosophila cells are nonciliated during development, which has led to the
  assumption that cilia-mediated Hh signaling is restricted to vertebrates."]
- [PMID:24768000 "Here, we identify and characterize a cilia-mediated Hh pathway in Drosophila
  olfactory sensory neurons."]
- [PMID:24768000 "We demonstrate that several fundamental key aspects of the vertebrate cilia
  pathway, such as ciliary localization of Smoothened and the requirement of the intraflagellar
  transport system, are present in Drosophila."]
- [PMID:24768000 "We show that Cos2 and Fused are required for the ciliary transport of Smoothened
  and that cilia mediate the expression of the Hh pathway target genes."]

UniProt independently records the location from the same study: the SUBCELLULAR LOCATION block in
smo-uniprot.txt has "Cell projection, cilium membrane {ECO:0000269|PubMed:24768000}", and TISSUE
SPECIFICITY has "Expressed in olfactory sensory neurons (at protein level)" with the same ECO.

So the apparent contradiction dissolves once the *cell type* is specified. Drosophila is not an
unciliated animal — it has ciliated sensory neurons and sperm; what is true is that the
developmental epithelia (imaginal discs, embryonic ectoderm) where the classical pathway was worked
out are unciliated, and there the Cos2/Fu complex substitutes for the ciliary compartment. In the
ciliated OSNs, Smo goes to the cilium and signals there. The eumetazoan node placement is therefore
grounded in protostome evidence as well as vertebrate evidence, and is not a vertebrate assertion
leaking into flies.

Two knock-on points:
- The same paper grounds the `GO:0030425 dendrite` (IDA) row, which is the fly seed for the
  *other* `UNRESOLVED` row at PTN000885245. That assessment resolves the same way. In an insect
  OSN the sensory cilium is elaborated from the distal tip of the dendrite, so ciliary and
  dendritic Smo are the same observation at two resolutions.
- By contrast, `GO:0071679 commissural neuron axon guidance` at the same node has **no** fly seed —
  the WITH/FROM is `PANTHER:PTN000885245|RGD:3726|ZFIN:ZDB-GENE-980526-89`, i.e. rat and zebrafish
  only. Verified: RGD:3726 is rat *Smo* ("smoothened, frizzled class receptor"),
  ZFIN:ZDB-GENE-980526-89 is zebrafish *smo*. The process presupposes a CNS midline that axons
  cross. That row was actioned `REMOVE` with a `propagation_review`, consistent with the family
  review's `TOO_DEEP` assessment and its observation that a vertebrate-scoped sibling node
  (PTN002601731) already exists.

This is a useful contrast to keep straight: three rows at one node, two of which are sound because
the fly is genuinely a seed, and one of which over-reaches because it is not.

## 7. Consistency with the PTHR11309 family review

No contradictions found. The family review's `PTHR11309:SF35` entry states that Smoothened
"does not bind Wnt and is not a Wnt receptor", that PAINT records losses of Wnt receptor activity,
Wnt-protein binding, and canonical/non-canonical Wnt signalling at PTN000885245, and that the node
asserts patched binding, smoothened signalling pathway, cilium and pattern specification. The fly
GOA record contains no Wnt terms at all, which is exactly what the recorded losses predict. The
`GO:0007389 pattern specification process` row was kept as non-core, matching the family review's
`SOUND` assessment and the human SMO review.

## 8. Consistency with the human SMO review

`genes/human/SMO/SMO-ai-review.yaml` takes the same actions on the shared rows: MODIFY
`GO:0004888`→`GO:0004930`, MODIFY `GO:0007166`→`GO:0007224`, MODIFY `GO:0016020`→plasma
membrane/ciliary membrane, ACCEPT plasma membrane / cilium / `GO:0004930` / `GO:0007193` /
`GO:0007224`, KEEP_AS_NON_CORE `GO:0005113 patched binding`, `GO:0007389`, `GO:0030425 dendrite`.
This review follows all of those.

Genuine fly/vertebrate differences recorded in the core functions:
1. The long C-tail adaptor function (`GO:0030674`) has no counterpart in the human core functions;
   the human protein instead uses ciliary compartmentalisation and a PKI pseudosubstrate motif that
   directly inhibits PKA-C.
2. Human core functions include `GO:0015485 cholesterol binding` and
   `GO:0004862 cAMP-dependent protein kinase inhibitor activity`. Neither is demonstrated for the
   fly protein in this annotation set — fly Smo instead *binds* PKAc as a substrate-enzyme pair
   (PMID:24985345), which is close to the opposite relationship, and its demonstrated lipid ligands
   are PI(4)P and PA.
3. Both share Gi coupling and cAMP lowering.

## 9. Notes on individual judgement calls

- **`GO:0042981 regulation of apoptotic process` (IGI, hid) → MARK_AS_OVER_ANNOTATED.** The cited
  study is explicit that the effect is not cell-autonomous:
  [PMID:23018595 "Surprisingly, cells with deregulated Hh activity do not protect themselves from
  apoptosis; instead, they promote cell survival of neighboring wild-type cells."] and
  [PMID:23018595 "This non-cell autonomous effect is mediated by Hh-induced Notch signaling, which
  elevates the protein levels of Drosophila inhibitor of apoptosis protein-1 (Diap-1), conferring
  resistance to apoptosis."]. Smo transduces the signal that starts this, but the apoptotic
  regulation is done by Notch and Diap-1 in *other* cells. Not false, but over-reaching.
- **`GO:0005515` with Sex-lethal (PMID:17284519) → REMOVE.** The evidence is co-IP/co-fractionation
  of a large assembly [PMID:17284519 "Cubitus interruptus, Sex-lethal, Patched and Smoothened
  co-immunoprecipitate and co-fractionate, suggesting a large complex of both membrane and
  cytoplasmic components of the Hedgehog pathway."], which does not establish a direct Smo-Sxl
  contact or any activity Smo performs. Removal is about the uninformativeness of the term, not
  about the co-purification being wrong.
- **`GO:0005515` with Usp8 (PMID:22253573, PMID:22253574) → REMOVE.** Here Smo is the *substrate*
  of a deubiquitinase. The informative annotation belongs on USP8. There is no MF term for being
  deubiquitinated, and inventing one would be exactly the `NEW`-inflation the project rules warn
  against.
- **`GO:0005515` with cos via PMID:15691767 → MODIFY (not UNDECIDED).** The cached record is
  abstract-only and its abstract is about Cos2-kinase complexes, never naming Smo. But UniProt cites
  this paper directly for the SUBUNIT line "Interacts with cos.", so the evidence is in the full
  text the curator read. Flagged in the reference's `reference_review` rather than used as grounds
  to doubt the annotation.
- **`GO:0042803` (IDA, PMID:21852395).** The cached full text of that paper documents Smo-Cos2 FRET
  and Fu kinase-domain dimerisation; the Smo C-tail dimerisation statement in it is
  [PMID:21852395 "Phosphorylation promotes Smo cell surface accumulation and active conformation in
  a dose-dependent manner, leading to dimerization/oligomerization of its C tails"]. Smo
  homodimerisation itself is demonstrated most directly in PMID:17960137 and PMID:26863604, and the
  gene separately carries `GO:0042802 identical protein binding` on both. ACCEPTed; the curator read
  the full text and the underlying claim is not in doubt.
- **Abstract-only IMP rows on `GO:0007224` that never name Smo in the abstract** (PMID:20435030,
  PMID:25512501, PMID:31279575, and the IGI PMID:16386907): all ACCEPTed. Each assays a step
  immediately downstream of Smo within the same pathway (Cos2 phosphorylation, CK1 protection of
  Ci-A, Fu phosphorylation of Ci, Slimb-mediated Ci processing). FlyBase curators read full texts we
  do not have; per project rules these are not grounds for doubt.
- **Reactome TAS rows for plasma membrane** (7 rows, R-DME-209168 etc.): ACCEPTed. They place Smo at
  the plasma membrane for the PKA/CK1 phosphorylation, conformational-change and Cos2-binding steps,
  which matches the primary evidence exactly.
- **No `NEW` terms proposed.** The obvious candidate would have been something for the ciliary
  route, but `GO:0005929` and `GO:0060170` already cover the compartment and `GO:0007224` covers the
  process; anything further would be an ancestor/descendant duplicate. The lipid and adaptor
  functions are reachable via MODIFY of existing rows, which is the correct mechanism.

## 10. Open questions carried into `suggested_questions`

1. Do ciliary (OSN) and cytoplasmic (imaginal disc) Hh transduction read the same C-tail
   phosphorylation code?
2. How much pathway output flows through Galphai/cAMP versus the Cos2/Fu route?
3. Is sterol regulation of Smo conserved in Drosophila, or has the fly switched to PI(4)P/PA?
4. Should `GO:0071679` at PTN000885245 be moved to the vertebrate-scoped sibling node PTN002601731?
