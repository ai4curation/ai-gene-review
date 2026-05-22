# PARA (Nicotiana tabacum) — research notes

UniProt: P25317 (GSTXA_TOBAC). "Probable glutathione S-transferase parA";
AltNames "Auxin-regulated protein parA" and "STR246C protein". EC 2.5.1.18.
220 aa, GST superfamily, tau (U) class. PANTHER PTHR11260:SF756 ("GLUTATHIONE
S-TRANSFERASE PARA-RELATED"). 220 aa, two-domain GST architecture (GST N-terminal
4-83; GST C-terminal 89-209). Reference proteome UP000790787, chromosome 2.
Evidence level PE 2 (transcript level) — no purified-protein characterization of
parA itself.

This review is part of the SPKW-PLANTS retrospective subproject: assessing whether
GOA's retirement of the keyword-to-GO (GO_REF:0000043) pipeline removed a correct
annotation or an over-annotation. The retired annotation here is
**auxin-activated signaling pathway (GO:0009734)**.

## The par gene family — discovery and identity

The `par` ("protoplast auxin-regulated") genes were isolated by Takahashi & Nagata
from cultured tobacco mesophyll protoplasts as genes induced very rapidly by
2,4-dichlorophenoxyacetic acid (2,4-D, a synthetic auxin) during the G0→S transition.

- `parA` was the founding clone [PMID:2594768 "A cDNA clone for an auxin-regulated
  gene was isolated from a tobacco mesophyll protoplast cDNA library by differential
  screening"; "The mRNA of the par gene ... its accumulation was detected in
  cultured mesophyll protoplasts as early as 30 min after the addition of
  2,4-dichlorophenoxyacetic acid to the culture medium. The par mRNA was not
  detected in leaves or freshly prepared protoplasts or in protoplasts in the
  absence of 2,4-dichlorophenoxyacetic acid"]. At the time of isolation the authors
  found "No significant homology to other known proteins" — the GST relationship
  was recognised only later.
- `parB` was isolated from the same system and was the first par gene whose product
  was directly shown to be a GST [PMID:1729717 "parB cDNA has homology to glutathione
  S-transferase (GST; RX:glutathione R-transferase, EC 2.5.1.18) from several sources
  including plant and animal cells. When we introduced expression vector pKK233-2,
  which retains parB cDNA, into Escherichia coli, we could detect GST activity in the
  parB gene product"]. parB is also known as Nt103. parB GST activity is robustly
  induced by 2,4-D [PMID:1729717 "a significant increase of GST activity was
  detected in the tobacco mesophyll protoplasts cultured in the presence of
  2,4-dichlorophenoxyacetic acid"].
- `parC` is another member of the family; PANTHER places parC (P49332/Q03666) in
  subfamily PTHR11260:SF726 ("PARC-RELATED"), distinct from parA's SF756. parA, parC
  and Nicotiana plumbaginifolia MSR-1 (P50471) share the PARA-related subfamily/
  closely related subfamilies — all tau-class plant GSTs.

So the par family is a cluster of auxin-inducible (and stress-inducible) tau-class
plant GSTs. The naming "auxin-regulated" refers to **transcriptional induction by
auxin**, established by promoter-reporter work: deletion of a 111-bp direct repeat
in the parA promoter abolished auxin-induced expression, localising a cis-acting
auxin-responsive region [PMID:2236015 (abstract) "deletion of a 111-base-pair (bp)
direct repeat in the 5' flanking sequences of the par gene abolished the
auxin-induced GUS activity ... an auxin-responsive region, which regulates
auxin-mediated activation of transcription"].

## parA = str246C: a pathogen/stress defense gene

The genomic clone str246C is sequence-identical to parA [PMID:7948901 "The
nucleotide sequence of the str 246C gene was found to be identical to that of the
parA gene, previously shown to be regulated by auxin"]. str246C transcripts
accumulate in leaves on inoculation with the bacterial pathogen Pseudomonas
(Ralstonia) solanacearum [PMID:7948901 "a cDNA clone, pNt246, whose corresponding
transcripts accumulate in leaves in response to inoculation by compatible and
incompatible isolates of the phytopathogenic bacterium Pseudomonas solanacearum"].
str246C/parA is therefore both auxin-inducible AND pathogen/defense-inducible —
classic behaviour of stress-responsive plant tau GSTs, which are induced by a wide
range of stimuli (auxin, herbicides, pathogens, oxidative stress, heavy metals).

## Is parA a "conventional" GST? — the key functional ambiguity

A direct study of the parA protein itself found important departures from a typical
cytosolic GST [PMID:7767232]:
- Enzyme activity: "we detected a low level of GST activity in the parA products,
  whose value was below 1/30 of that of parB products encoding tobacco ... GST."
  So parA has measurable but very weak GST activity relative to parB.
- Localization: "the subcellular location of parA protein is the nucleus in
  cultured tobacco mesophyll protoplasts, while conventional GSTs including the
  parB product were primarily located in the cytoplasm." Confocal imaging of BY-2
  cells showed "the parA product was confined to the nucleus, but was excluded
  from the nucleolus."
- The authors note "exon/intron organization of the parA family was appreciably
  different from that of conventional GSTs including parB" and that "the parA
  protein is much more similar to a 24-kDa protein of Escherichia coli that is
  reported to bind to RNA polymerase."
- Conclusion: "These different characteristics of parA compared with the
  conventional GSTs indicate that parA protein would have distinct functions, such
  as involvement in transcription, rather than functioning as a conventional GST."

Caveats: this is a single 1995 study; the "24-kDa E. coli RNA polymerase-binding
protein" comparison is weak by modern standards, and nuclear localization of an
overexpressed/tagged protein in protoplasts can be artefactual. UniProt nonetheless
retains "Probable glutathione S-transferase" (the name carries "Probable"), retains
EC 2.5.1.18 (a generic GST reaction RX + GSH), and assigns the "cytoplasm" CC term
by TreeGrafter family inference rather than experiment. The honest position: parA
has GST-family sequence/structure (tau class) and weak catalytic activity, but its
true physiological substrate and primary cellular role are not established. The
modern GOA molecular-function (glutathione transferase activity, IEA from
InterPro/RHEA/EC/PANTHER) and process (glutathione metabolic process) annotations
are family-level inferences that are reasonable but not experimentally proven for
parA specifically.

## Plant tau-class GST biology (general)

Plant GSTs (EC 2.5.1.18) are a large, plant-specific-rich superfamily; phi (F) and
tau (U) classes are plant-specific and most numerous [PMID:11897031 "can be divided
on the basis of sequence identity into the phi, tau, theta, zeta and lambda classes
... the tau and phi classes being the most numerous"]. They use GSH as cosubstrate/
coenzyme; functions include "conjugation and resulting detoxification of herbicides,
the reduction of organic hydroperoxides formed during oxidative stress and the
isomerization of maleylacetoacetate" plus non-catalytic ligandin roles "binding
flavonoid natural products in the cytosol prior to their deposition in the vacuole"
and roles "as components of ultraviolet-inducible cell signaling pathways"
[PMID:11897031]. "GSTs are predominantly expressed in the cytosol" [PMID:11897031].
The tau/phi classes "are largely responsible for catalyzing glutathione-dependent
reactions with xenobiotics, notably conjugation leading to detoxification"; plant
GSTs use "a catalytic serine in place of a tyrosine residue" [PMID:21425939].
Endogenous roles are "less well defined ... linked to a diverse range of functions,
including signaling, counteracting oxidative stress, and detoxifying and
transporting secondary metabolites" [PMID:21425939].

## Auxin-INDUCED ≠ component of the auxin signaling pathway

Critical distinction for this review. The bona fide auxin **signal-transduction
pathway** (GO:0009734, "auxin-activated signaling pathway") consists of: auxin
perception by the TIR1/AFB F-box receptors, auxin-promoted degradation of Aux/IAA
repressors via the SCF^TIR1 ubiquitin ligase, and de-repression of ARF
transcription factors. parA/parB/parC are **downstream auxin-responsive target
genes** — their promoters contain auxin-responsive cis-elements and they are
transcriptionally induced when auxin signaling is active. A downstream
auxin-responsive metabolic enzyme is not a "component" of the signaling pathway.
The GO term that correctly captures "this gene is transcriptionally induced by
auxin" is "response to auxin" (GO:0009733), which is a parent that includes
auxin-responsive gene expression without implying signal-transduction-component
status. GO:0009734 (auxin-activated signaling pathway) is reserved for receptors/
Aux-IAA/ARF/SCF-TIR1 components.

The SPKW pipeline (GO_REF:0000043) generated GO:0009734 purely from the UniProt
keyword "Auxin signaling pathway", which UniProt had attached on the basis of the
historical name "Auxin-regulated protein". This is a textbook "expression ≠
function" / "downstream effector mislabeled as pathway component" over-annotation.

## Summary judgement

- parA is a tobacco tau-class plant GST (GST superfamily, PTHR11260:SF756),
  EC 2.5.1.18; "Probable" because parA's own catalytic activity is weak (<1/30 of
  parB) and its physiological substrate is unknown [PMID:7767232].
- parA = str246C: auxin-inducible AND pathogen/defense-inducible
  [PMID:2594768; PMID:7948901].
- The retired SPKW annotation "auxin-activated signaling pathway" (GO:0009734) is an
  over-annotation derived from the historical "auxin-regulated" name. parA is a
  downstream auxin-responsive gene, not a TIR1/Aux-IAA/ARF signaling component.
  GOA's removal of this annotation when retiring the keyword2GO pipeline was
  JUSTIFIED. If a process term is warranted it is "response to auxin" (GO:0009733).
- The current GOA GST/glutathione-metabolism/cytoplasm IEA annotations are
  family-level inferences. GST activity and glutathione metabolic process are
  acceptable (parA is a tau-class GST with detectable activity). The "cytoplasm"
  TreeGrafter annotation is the family-typical location and is reasonable as a
  general call, but note the one direct study reports parA protein in the nucleus
  [PMID:7767232] — a discrepancy worth flagging.
