# SSB1 review notes

## Identity and scope

- Target: *Saccharomyces cerevisiae* SSB1 / YDL229W, UniProt P11484, the
  613-residue ribosome-associated Ssb-type Hsp70. This is the canonical SSB1
  intended by the unfolded-protein-binding project and is not the unrelated
  RNA-binding protein Sbp1/P10080 that historically carried `SSB1` as a
  synonym in this repository.
- Ssb1 and Ssb2/P40150 are nearly identical paralogs and much of the primary
  literature assays the combined Ssb1/2 system. Claims are therefore phrased
  as Ssb or Ssb1/2 unless the experiment specifically isolates Ssb1.
- OpenScientist completed a GO-focused literature synthesis on 2026-08-11.
  Its report and HTML/PDF artifacts are preserved in this gene directory.

## Core molecular mechanism

- Ssb is an abundant Hsp70 associated with translating ribosomes. Puromycin
  releases Ssb together with nascent chains, and Ssb can be photocross-linked
  to nascent chains. The authors conclude that Ssb contacts both the ribosome
  and nascent polypeptide and prevents misfolding of newly synthesized
  proteins [PMID:9670014, "We propose that Ssb is a core component of the
  translating ribosome which interacts with both the nascent polypeptide chain
  and the ribosome."].
- Global substrate profiling shows that Ssb preferentially acts on longer,
  slowly translated, aggregation-prone nascent proteins; loss of SSB causes
  widespread aggregation of newly synthesized proteins [PMID:23332755,
  "Deletion of SSB leads to widespread aggregation of newly synthesized
  polypeptides."].
- Selective ribosome profiling resolved repeated binding-release cycles on
  degenerate motifs enriched in positively charged and aromatic residues;
  timely engagement as the motif exits the ribosome depends on RAC
  [PMID:28708998, "Ssb engages most substrates by multiple binding-release
  cycles to a degenerate sequence enriched in positively charged and aromatic
  amino acids."].
- Cryo-EM and biochemical analysis identify Rpl25/uL23 as the ribosomal
  docking site and show that RAC positions ATP-bound Ssb's substrate-binding
  domain at the tunnel exit [PMID:41545346, "these structures enable us to
  delineate the intricate RAC-dependent cycle, which positions the substrate
  binding domain of Ssb-ATP close to the tunnel exit to receive nascent
  chains."].
- Ssb has directly measured ATPase activity with unusual kinetics relative to
  Ssa Hsp70s: lower steady-state ATP affinity, higher maximal velocity, and no
  potassium dependence. C-terminal/substrate-binding domains govern these
  properties [PMID:9860955, "Ssb, however, has an unusually low steady-state
  affinity for ATP but a higher maximal velocity."].

## Secondary and downstream roles

- Loss of RAC or Ssb1/2 impairs translational fidelity, particularly
  termination [PMID:15456889, "The mutant strains suffered primarily from a
  defect in translation termination, while misincorporation was compromised
  to a lesser extent."].
- Deleting SSB1/SSB2 specifically inhibits programmed -1 frameshifting without
  affecting +1 frameshifting [PMID:16607023, "deletion of Ssb1p/Ssb2p or of
  Ssz1p/Zuo1p resulted in specific inhibition of -1 PRF"].
- Modern work supports two fidelity mechanisms: direct assistance at
  stalling-prone polylysine sequences and production of structurally competent
  ribosomes [PMID:31114879, "the RAC/Ssb system promotes the fidelity of
  translation termination via two distinct mechanisms."]. These processes are
  genuine but downstream/ancillary relative to cotranslational folding.
- Zuo1 with Ssb participates genetically in rRNA processing and ribosome
  biogenesis [PMID:20368619, "Zuo1, acting together with its Hsp70 partner,
  SSB (stress 70 B), also participates in maturation of the 35S rRNA."].
  Nuclear export/rRNA-processing annotations are retained as non-core because
  the evidence is genetic and the primary biochemical site of action is the
  cytosolic ribosome.
- Ssb1 contains an active nuclear export signal and appears cytosolic at steady
  state, although it can shuttle through the nucleus [PMID:10347213,
  "GFP-Ssb1p appeared only in the cytosol."]. Thus cytosol is the core
  localization; nucleus is a non-core/transient localization rather than a
  contradiction.
- Ssb also has a documented extra-ribosomal glucose-signaling role with Bmh and
  the SNF1/Glc7 system [PMID:27001512, "the defect in glucose-repression in the
  absence of Ssb is due to the ability of the chaperone to bridge between the
  SNF1 and Glc7 complexes."]. This is biologically credible but is not the
  primary protein-folding function.

## Annotation-specific cautions

- The seven `protein binding` annotations are uninformative generic outputs of
  interaction screens or complex studies. They are marked over-annotated even
  where the interaction itself is informative (for example Sse1 as an Ssb
  nucleotide-exchange factor in PMID:16688211).
- The plasma-membrane HDA annotation comes from a detergent-solubilized plasma
  membrane fraction containing many identified proteins; no specific membrane
  residence or membrane function for this abundant soluble Hsp70 is shown in
  the abstract [PMID:16622836]. It conflicts with direct cytosolic localization
  and is removed as likely fraction carryover.
- Calmodulin affinity chromatography and peptide mass fingerprinting directly
  recovered Ssb1 and proposed a conserved calmodulin-binding helix
  [PMID:17146552]. The binding call is retained, but as non-core because a
  physiological regulatory consequence was not established.
- Stationary-phase imaging detected Ssb1 in reversible cytoplasmic assemblies
  [PMID:19502427]. This supports cytoplasmic localization under nutrient
  stress, not a separate core function.
- PMID:14517260 (the proposed Ssb-to-TRiC WD40 folding relay) is explicitly
  marked as a retracted article in PubMed. It is excluded from the review's
  evidence and claims.

## Curation synthesis

- Core molecular function: ATP-dependent protein folding chaperone
  (GO:0140662), replacing the less specific protein folding chaperone term.
- Core process: de novo cotranslational protein folding (GO:0051083).
- Core location: cytosol (GO:0005829), specifically on translating cytosolic
  ribosomes near the 60S tunnel exit.
- ATP binding and ATP hydrolysis are retained as genuine molecular activities;
  translation fidelity, frameshifting, termination, rRNA processing, and
  ribosome export are retained but distinguished from the core folding role.

## Targeted hypothesis result: Ssb1 versus Ssb2 specialization

- A targeted OpenScientist run tested whether the four amino-acid differences
  between Ssb1 and Ssb2 have a *demonstrated* paralog-specific consequence. The
  report's verdict was refuted-as-stated: no primary study was found that
  resolves a distinct substrate spectrum or cotranslational folding mechanism
  for one paralog. Foundational and modern studies generally assay “Ssb” or
  delete SSB1 and SSB2 together
  [file:yeast/SSB1/SSB1-hypotheses/core-function-the-four-amino-acid-differences-between-ssb1-and-ssb2-confer-a-demonstrated-paralo/openscientist.md,
  "No competing paper asserting a demonstrated Ssb1-vs-Ssb2 functional
  difference was found."].
- The provider-generated sequence artifact confirms substitutions E49Q, M413I,
  C435V, and A436S. Three lie in the substrate-binding domain; C435V is the most
  physicochemically radical. This makes paralog specialization testable, not
  established. Current GO curation should continue to treat the core Hsp70
  activity as shared.
- Provider-output caveats: its GO table says 39 current annotations although the
  fetched/collapsed review has 36, and it recommends obsolete GO:0051082. Those
  claims were not adopted. The curated replacement remains GO:0140662.

## Completion audit (2026-08-28)

- Row-by-row reconciliation found 39 fetched GOA rows representing 36 distinct
  review assertions. The three extra rows are duplicate assertion keys that
  differ only in `WITH/FROM`: three PMID:16429126 protein-binding rows collapse
  to one review entry, and two PMID:1394434 cytoplasmic-translation IPI rows
  collapse to one. No GO term/evidence/reference/qualifier assertion is absent.
- All seven IBA rows were re-read against their GOA `WITH/FROM` fields and PAINT
  nodes. The cytoplasm, ATPase, generic chaperone, nucleus, heat-shock-protein
  binding, and cytosol transfers are biologically defensible; broad or secondary
  assertions are distinguished from the core ATP-dependent cotranslational
  chaperone function. The broad protein-refolding IBA was narrowed to directly
  demonstrated de novo cotranslational folding rather than being accepted as a
  generic refolding program.
- The plasma-membrane HDA was initially changed from `REMOVE` to `UNDECIDED`
  because PMID:16622836 is abstract-only in the cache and describes a stripped
  plasma-membrane fraction, while direct evidence places Ssb1 in the cytosol.
- Translation, frameshifting, termination, and fidelity phenotypes were retained
  as genuine but non-core. This brings row actions into agreement with the core
  function synthesis, which identifies ATP-dependent nascent-chain folding as
  primary and the translation phenotypes as downstream/contextual.

## PR review follow-up (2026-08-28)

- The missing ribosome-associated annotations are now explicit `action: NEW`
  rows: GO:0043022 `ribosome binding` and GO:0022626 `cytosolic ribosome`.
  PMID:9670014 directly characterizes Ssb-ribosome interaction, and PMID:1394434
  identifies Ssb1/2 as cytosolic Hsp70s associated with translating ribosomes.
  Because both are existing GO terms rather than ontology gaps, they belong in
  `existing_annotations`, not `proposed_new_terms`. GO:0022626 was also added
  to the core-function locations.
- The GO:0042026 IBA is now classified as `PROPAGATION_BAD` with
  `FUNCTIONAL_DIVERGENCE`, rather than a parent/child granularity problem.
  Protein refolding and de novo cotranslational folding are sibling processes;
  GO:0051083 is already present with direct IDA evidence from PMID:9670014, so
  MODIFY here effectively rejects the unsupported propagated refolding claim.
- The plasma-membrane HDA is now `MARK_AS_OVER_ANNOTATED`, harmonizing the call
  with the nearly identical Ssb2 paralog. This retains the bulk high-throughput
  fraction observation without treating plasma membrane as a demonstrated
  functional compartment for the soluble cytosolic chaperone.
