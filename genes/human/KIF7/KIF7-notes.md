# KIF7 (human, Q2M1P5) — curation notes

Working journal for the GO annotation review. Appended to as work proceeded.

## 1. What the protein is

KIF7 is a 1343-residue kinesin-family protein with an N-terminal kinesin motor
domain (UniProt feature `DOMAIN 15..349`), a long coiled-coil/α-helical stalk
(`COILED 480..542` and further coiled segments), and an extensive C-terminal
region carrying the GLI-binding and NPHP1-binding determinants
(`REGION 513..775 /note="Sufficient for interaction with NPHP1"`). UniProt places
it in the "TRAFAC class myosin-kinesin ATPase superfamily. Kinesin family. KIF27
subfamily."

PANTHER classification (authoritative source `interpro/panther/panther-members.tsv`):

```
Q2M1P5	PTHR24115:SF445
```

`PTHR24115` is `KINESIN-RELATED`; `PTHR24115:SF445` is `KINESIN-LIKE PROTEIN KIF7`,
and its sister subfamily `PTHR24115:SF949` is `KINESIN-LIKE PROTEIN COSTA`
(Drosophila Costal-2). The KIF7/Cos2 orthology is therefore supported directly by
the family classification, not only by pathway analogy. Note that the cached
UniProt flat file still prints the older `PTHR47969` / `PTHR47969:SF8` mapping in
its `DR PANTHER` lines; `panther-members.tsv` is the authority and the
`modules/hedgehog_signaling.yaml` grounding (`PTHR24115:SF445`) matches it.

Human disease: KIF7 loss-of-function causes acrocallosal syndrome, hydrolethalus
syndrome 2, Joubert syndrome 12 and Al-Gazali-Bakalinova syndrome, and KIF7
missense alleles act as modifiers across the ciliopathy spectrum
[PMID:21552264 "KIF7 is also a likely contributor of alleles across the ciliopathy
spectrum, as sequencing of a diverse cohort identified several missense mutations
detrimental to protein function"], [PMID:21633164 "Here we report the identification
of a disease locus, JBTS12, with mutations in the KIF7 gene, an ortholog of the
Drosophila kinesin Costal2, in a consanguineous JBTS family and subsequently in
other JBTS patients"].

## 2. The decisive biochemistry: KIF7 is an immotile kinesin

This is the single most important fact for grading the molecular-function
annotations, and two independent purified-protein studies establish it.

He et al. 2014 (Nat Cell Biol) purified recombinant KIF7 and assayed it on dynamic
microtubules by TIRF:

- [PMID:24952464 "KIF7 can interact directly with microtubules but lacks detectable motility"]
- [PMID:24952464 "Purified recombinant Kif7 binds the plus ends of growing microtubules in vitro, where it reduces the rate of microtubule growth and increases the frequency of microtubule catastrophe."]
- [PMID:24952464 "Together, our in vitro analysis suggests that the plus-end-associated KIF7 promotes catastrophe and inhibits microtubule growth in an ATP-hydrolysis dependent manner."]
- [PMID:24952464 "In addition to promoting catastrophe, KIF7 decreased the rate of microtubule growth in a dose-dependent manner"]
- [PMID:24952464 "At microtubule minus-ends, neither the catastrophe frequency nor the growth rate was significantly affected by KIF7560-GFP"]

Yue et al. 2018 (J Cell Biol) did the kinetic dissection across the whole
kinesin-4 family and reached the same conclusion, with a mechanism:

- [PMID:29351996 "KIF4 and KIF21 motors are fast and processive, KIF7 and its Drosophila melanogaster homologue Costal2 (Cos2) are immotile, and KIF27 is slow and processive."]
- [PMID:29351996 "The mechanistic basis of immotile KIF7 behavior arises from an inability to release adenosine diphosphate in response to microtubule binding"]
- [PMID:29351996 "Neither KIF7 nor KIF27 can cooperate for fast processive transport when working in teams."]
- [PMID:29351996 "We suggest that evolutionarily selected sequence differences enable immotile KIF7 and Cos2 motors to function not as transporters but as microtubule-based tethers of signaling complexes."]

Consequences for the review:

1. `GO:0003777 microtubule motor activity` ("A motor activity that generates
   movement along a microtubule, driven by ATP hydrolysis") is contradicted for
   KIF7. The defensible residue of those rows is microtubule binding, and
   specifically plus-end binding (`GO:0051010`).
2. `GO:0007018 microtubule-based movement` and `GO:0030705
   cytoskeleton-dependent intracellular transport` inherit the same problem. The
   real microtubule-directed activity is negative regulation of microtubule
   polymerization (`GO:0031115`) at the axonemal plus end.
3. ATP binding and ATP hydrolysis are *not* contradicted. KIF7 hydrolyses ATP —
   weakly, with only modest microtubule stimulation — and the catastrophe-promoting
   activity is ATP-hydrolysis dependent: [PMID:29351996 "For immotile KIF7, very
   little microtubule-dependent stimulation of ATPase activity was observed."] So
   `GO:0005524` and `GO:0016887` stand; what fails is the coupling of hydrolysis to
   stepping, not hydrolysis itself.

The motor domain is still functionally required — it is what targets KIF7 to the
ciliary tip [PMID:19666503 "Activation of the Shh pathway promotes trafficking of
Kif7-eGFP from the base to the tip of the cilium, and localization to the tip of the
cilium is disrupted in a motor domain mutant."] This is why the older literature
called KIF7 a "putative ciliary motor protein" [PMID:21633164] and
"may also act as a ciliary motor" [PMID:19666503 "We conclude that Kif7 is a core
regulator of Shh signaling that may also act as a ciliary motor."] — a hypothesis
that the 2014 and 2018 biochemistry then falsified. Reactome's own text has
already absorbed the correction: the cached entry
`reactome/R-HSA-5610733.md` says KIF7 "binds directly to the plus ends of axonemal
microtubules and inhibits their growth in an ATP-dependent manner (He et al, 2014)".

## 3. What KIF7 actually does: organize the ciliary tip compartment

He et al. 2014 is also the paper that gives KIF7 a positive functional
description rather than a motor description:

- [PMID:24952464 "Here we show that Kif7 localizes to the cilium tip, the site of microtubule plus ends, where it limits cilium length and controls cilium structure."]
- [PMID:24952464 "Instead, a central function of Kif7 in the mammalian Hh pathway is to control cilium architecture and to create a single cilium tip compartment, where Gli-Sufu activity can be correctly regulated."]
- [PMID:24952464 "Thus, in the absence of KIF7, the Gli-Sufu complex and IFT81 localize to ectopic tip-like compartments along the axoneme."]
- [PMID:24952464 "indicating that KIF7 is required to restrict Gli-Sufu complexes to the distal end of the cilium"]
- [PMID:24952464 "Proteins that normally localize to distal cilia tips, including the Gli and Sufu proteins that mediate Hh signaling, are found in ectopic puncta along the Kif7 mutant cilium."]
- [PMID:24952464 "We propose that the ectopic activation of the pathway seen in Kif7 mutants is due to the ectopic Gli/Sufu complexes away from the cilia tip, where they become inappropriately activated in the absence of ligand"]

Two negative results in the same paper matter for the transport annotations:

- [PMID:24952464 "Kif7 is not required for normal intraflagellar transport or for trafficking of Hh pathway proteins into cilia."]
- [PMID:24952464 "Thus there was no significant difference in the rates of IFT between wild type and Kif7L130P cilia, indicating that KIF7 does not control cilia length by affecting the rates of IFT."]
- [PMID:24952464 "Thus KIF7 is not required for trafficking of Gli2 into cilia, but it does control proper localization of Gli2 within the cilium."]

Targeting to the tip does not depend on the pathway components it regulates:
[PMID:24952464 "KIF7 was also present at cilia tips in MEFs derived from mutant
embryos that lack Smo or Gli2 and Gli3, indicating that KIF7 is targeted to cilia
independently of Shh pathway proteins"].

## 4. Position in the Hedgehog pathway: both signs, downstream of SMO

Three 2009 papers established KIF7 as the mammalian Cos2 counterpart, all with
the same bidirectional result.

- Liem et al. (mouse genetics): [PMID:19666503 "we show that, similar to Drosophila and zebrafish Cos2, mouse Kif7 acts downstream of Smo and upstream of Gli2 and has both negative and positive roles in Shh signal transduction"], and [PMID:19666503 "Mouse Kif7 activity depends on the presence of cilia and Kif7-eGFP localizes to base of the primary cilium in the absence of Shh."]
- Cheung et al.: [PMID:19549984 "Similar to Cos2, Kif7 physically interacted with Gli transcription factors and controlled their proteolysis and stability, and acted both positively and negatively in Hh signaling."]
- Endoh-Yamagami et al.: [PMID:19592253 "We show that Kif7 accumulates at the distal tip of the primary cilia in a Hh-dependent manner."], [PMID:19592253 "We also demonstrate a requirement for Kif7 in the efficient localization of Gli3 to cilia in response to Hh and for the processing of Gli3 to its repressor form."], and [PMID:19592253 "These results suggest a role for Kif7 in coordinating Hh signal transduction at the tip of cilia and preventing Gli3 cleavage into a repressor form in the presence of Hh."]

The negative and positive arms were separated genetically in two mouse tissues,
and in both the positive arm runs through SUFU:

- Growth-plate chondrocytes: [PMID:21795282 "Kif7 plays a role in the turnover of Sufu and the exclusion of Sufu-Gli complexes from the primary cilium."], [PMID:21795282 "Importantly, halving the dose of Sufu restores normal hedgehog pathway activity and chondrocyte development in Kif7-null mice, demonstrating that the positive role of Kif7 is to restrict the inhibitory activity of Sufu."], [PMID:21795282 "Therefore, Kif7 regulates the activity of Gli transcription factors through both Sufu-dependent and -independent mechanisms."]
- Keratinocytes/skin: [PMID:23034632 "Kif7 possesses Sufu-dependent and -independent regulatory functions in Hh signaling: while it promotes Hh pathway activity through the dissociation of Sufu-Gli2 complex, it also contributes to the repression of Hh target genes in the absence of Sufu."]

Human genetics agrees on the GLI read-out: [PMID:21552264 "Consistent with a role
of KIF7 in Hedgehog signaling, we show deregulation of most GLI transcription
factor targets and impaired GLI3 processing in tissues from individuals with KIF7
mutations."]

Zebrafish adds the cross-species substitution experiment that seals the Cos2
equivalence, and the cytoplasmic pool:

- [PMID:24339784 "Moreover, we show that Drosophila Costal2 can substitute for Kif7, suggesting a conserved mode of action of the two proteins."]
- [PMID:24339784 "Notably, we find that endogenous Kif7 protein accumulates not only in the primary cilium, as previously observed in mammalian cells, but also in cytoplasmic puncta that disperse in response to Hh pathway activation."]
- [PMID:24339784 "We show that Kif7 interacts with both Gli1 and Gli2a and suggest that it functions to sequester Gli proteins in the cytoplasm, in a manner analogous to the regulation of Ci by Cos2 in Drosophila."]
- [PMID:24339784 "We also show that zebrafish Kif7 potentiates Gli2a activity by promoting its dissociation from the Suppressor of Fused (Sufu) protein"]

This is exactly the compartment axis the pan-metazoan module records
(`modules/hedgehog_signaling.yaml`, `gli_activation_compartment_axis`): the same
kinesin scaffold step runs at the ciliary tip in vertebrates and on a cytoplasmic
complex in Drosophila. Nothing found here contradicts the module; the zebrafish
cytoplasmic puncta show the two implementations are not mutually exclusive even
within one vertebrate.

## 5. The interaction set, and what it means for `GO:0005515`

GOA carries eight bare `GO:0005515` rows for KIF7. They fall into three groups.

**(a) Core pathway partners** — GLI3 (P10071), Gli1 (P47806), SMO (Q99835) and
Sufu (Q9Z0P7), all from PMID:19592253, matching the UniProt SUBUNIT line
"Interacts with GLI1, GLI2, GLI3, SMO and SUFU (PubMed:19592253)". These are not
generic interactions: they are the tethering activity that the functional papers
describe, and the informative molecular function is adaptor/scaffold activity
(`GO:0030674`), the term the module already assigns to the KIF7 annoton.

**(b) P4HA2 (O15460), three rows** from three separate high-throughput interactome
papers (PMID:33961781 BioPlex, PMID:35271311 OpenCell, PMID:40205054 multimodal
cell maps). Ordinarily three screen hits would still leave a bare
protein-binding row uninformative — but this interaction has since been validated
and given a mechanism, and the validating paper explicitly credits those three
screens: [PMID:38909089 "Despite the previous CRISPR-based screenings of the Hh
pathway regulators [5, 49], where P4HA2 was not uncovered, three independent
proteome interactome studies have detected the interaction between P4HA2 and KIF7
[50-52]."] The mechanism is scaffolding by KIF7:

- [PMID:38909089 "Notably, a strong direct interaction was observed between P4HA2 and KIF7, while no significant or direct interaction was detected between P4HA2 and GLI1 or SUFU"]
- [PMID:38909089 "suggesting that the ciliary localization of P4HA2 is dependent on KIF7"]
- [PMID:38909089 "In summary, KIF7 serves as a scaffold protein, facilitating the ciliary localization of P4HA2 and its association with other components, thereby regulating the impact of P4HA2 on the Hh signaling pathway."]
- [PMID:38909089 "Additionally, KIF7, acting as a key scaffold protein, is involved in the post-translational modification of the Hh pathway component, facilitating the hydroxylation of key proline residues in SUFU."]
- [PMID:38909089 "are crucial for the interaction between KIF7 and P4HA2"] — domain mapping placed the contact on the KIF7 GLI-binding domain, so the same surface that binds GLI mediates the P4HA2 contact, which is the structural reason one adaptor term covers both.

So these three rows also resolve to `GO:0030674` rather than to removal.

**(c) NPHP1 (O15259)** from PMID:21633164 — [PMID:21633164 "We found that KIF7
co-precipitated with nephrocystin-1."] A single co-precipitation with no
established functional consequence. Nothing more informative is supported, so the
bare row should go.

## 6. Localisation summary

- Ciliary tip, enhanced by pathway activation: [PMID:19592253 "We show that Kif7 accumulates at the distal tip of the primary cilia in a Hh-dependent manner."]; HPA immunofluorescence (GO_REF:0000052) independently records tip and cilium.
- Ciliary base / basal body in the unstimulated state: [PMID:19666503 "Mouse Kif7 activity depends on the presence of cilia and Kif7-eGFP localizes to base of the primary cilium in the absence of Shh."] This is the direct source for the ISS `GO:0036064 ciliary basal body` row transferred from mouse Kif7 (UniProtKB:B7ZNG0); mouse Kif7 additionally carries an independent IDA for `GO:0036064`.
- Cytoplasmic puncta: [PMID:24339784 "Notably, we find that endogenous Kif7 protein accumulates not only in the primary cilium, as previously observed in mammalian cells, but also in cytoplasmic puncta that disperse in response to Hh pathway activation."] and [PMID:38909089 "We found that P4HA2-EGFP co-localized with KIF7-BFP in cytoplasm."]
- Axonemal microtubules: the tip localisation *is* plus-end binding, per section 2.

## 7. Decisions taken, and the ones deliberately not taken

Actions assigned: `GO:0003777` (×3) MODIFY to plus-end/microtubule binding;
`GO:0007018` (×2) MODIFY to `GO:0031115`; `GO:0030705` REMOVE; of the eight
`GO:0005515` rows, six MODIFY to `GO:0030674` and two (SMO, NPHP1) REMOVE; everything cilium-,
microtubule-, ATP- and smoothened-related ACCEPTed, with `GO:0005737 cytoplasm`
and `GO:0005871 kinesin complex` kept as non-core.

Three `NEW` annotations were considered and rejected:

- **Cilium-length / cilium-organization terms** (`GO:1902017`, `GO:0044782`).
  He et al. 2014 shows KIF7 itself limits axonemal microtubule growth at the tip,
  so the participation test would pass. The comparator check argues against it:
  mouse Kif7 (B7ZNG0) carries *no* cilium-assembly or cilium-organization term
  anywhere in its GOA record, and the one annotation a curator did take from
  PMID:24952464 is `GO:0042802 identical protein binding` — i.e. a curator read
  this exact paper and deliberately did not add a cilium-organization term. The
  structural effect is captured by the `GO:0031115` replacement proposed on the
  `GO:0007018` rows, which sits in the microtubule branch GOA already asserts.
- **`GO:0042802 identical protein binding`.** KIF7 homodimerises (UniProt "Can
  form homodimers") and mouse Kif7 has the IPI from PMID:24952464, so the human
  row would be defensible — but it is another child of `protein binding` with no
  functional content, which the root `CLAUDE.md` rule tells us to avoid rather
  than to add. Raised as a question instead.
- **`GO:0008589 regulation of smoothened signaling pathway`.** Redundant: it is
  the parent of `GO:0045879` and `GO:0045880`, both of which KIF7 already carries.

Terms verified against QuickGO before use (labels and non-obsolete status):
`GO:0051010 microtubule plus-end binding`, `GO:0031115 negative regulation of
microtubule polymerization`, `GO:0030674 protein-macromolecule adaptor activity`.
