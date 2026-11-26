# HAECO P91730 notes

## Fetch and setup

- Fetched the reviewed Haemonchus contortus accession with `just fetch-gene HAECO P91730`.
- `P91730` is the reviewed Swiss-Prot HG4 record `GLUCB_HAECO`. UniProt does not
  assert a gene name for the entry, so this review keeps the accession-based
  folder and `gene_symbol` rather than inventing a symbol from the HG4 protein
  alias.
- `just fetch-gene-pmids HAECO P91730` found no PMIDs in the seeded GOA rows,
  which were all electronic or similarity-based.
- Cached UniProt's primary HG4 paper, PMID:9879896, directly with
  `uv run ai-gene-review fetch-pmid 9879896`; the local cache is abstract-only.
- `just deep-research-falcon HAECO P91730 --fallback perplexity-lite` failed
  because both configured remote providers were unavailable, so this review used
  the reviewed UniProt record, the abstract-only primary HG4 paper, PANTHER
  PTHR18945, the completed C. elegans GluCl reviews and the nematode GluCl
  module.
- `just paint-losses HAECO P91730` reported that P91730 is in PANTHER PTHR18945
  but is not a leaf of the PAINT tree, so no IRD/IKR loss applies.

## Evidence summary

PMID:9879896 cloned HG4 cDNAs from H. contortus by RT-PCR. The accessible
abstract reports "82% amino-acid identity with the C. elegans Glu-Cl beta
subunit", which makes P91730 a close parasite homolog of the C. elegans
GLC-2 beta subunit but does not by itself resolve a one-to-one orthologous
relationship.

The same paper raised antiserum to an N-terminal HG4 peptide and localized HG4
to anterior motor-neuron commissures: "Affinity purified antibodies reacted
with motor neuron commissures". The abstract does not report electrophysiology
for HG4, a native heteromeric partner, or postsynaptic localization within the
stained anterior motor-neuron commissures.

UniProtKB/Swiss-Prot curates P91730 as a reviewed glutamate-gated chloride
channel beta subunit, with a predicted signal peptide, four transmembrane
helices, and PANTHER PTHR18945 family membership. Its function and membrane
topology comments are by similarity to C. elegans GLC-1/GLC-2 and Drosophila
GluClalpha rather than direct HG4 electrophysiology.

The `modules/nematode_glutamate_gated_chloride_channels.yaml` module models C.
elegans GLC-2 as the beta subunit in GLC-1/GLC-2 and GLC-2/GLC-4 GluCls. P91730
is consistent with that GluCl-beta lane, but the concrete H. contortus receptor
needs alpha-partner resolution before HG4 can be promoted from a gene review to
an H. contortus receptor annoton in the module.

## Annotation decisions

- The generic InterPro Cys-loop receptor activity rows were accepted as true
  parent activities.
- The ARBA `GO:0008068` row was accepted as the specific inferred core GluCl
  molecular function and represented as `contributes_to_molecular_function`
  because no accessible evidence shows that HG4 forms homomeric
  glutamate-gated chloride channels.
- The generic membrane and ion-transport rows were marked `TOO_GENERAL` because
  plasma membrane and chloride transmembrane transport are already asserted.
- Plasma-membrane rows were accepted from HG4 receptor topology.
- Postsynaptic-membrane rows were marked `MARK_AS_OVER_ANNOTATED`: the cloned
  HG4 paper localized the protein to anterior motor-neuron commissures, but the
  accessible abstract does not localize it to postsynaptic specializations.
- The automated `GO:0060079` excitatory postsynaptic potential row was removed
  as sign-wrong for an anion-selective GluCl subunit; the same ontology problem
  was already recorded in the C. elegans GluCl reviews.
