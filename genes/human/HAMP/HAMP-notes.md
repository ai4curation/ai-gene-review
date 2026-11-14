# HAMP curation notes

## 2026-11-14 — primary-source review

Human HAMP (UniProt P81172) was fetched with the repository's native pipeline.
The review preserves all 21 GOA rows as 21 annotation contexts, including their
original terms, evidence codes, references, qualifiers and supporting entities.
Decisions: 16 ACCEPT, 2 KEEP_AS_NON_CORE, 2 MODIFY, 1 UNDECIDED; no NEW or retired
contexts. The review remains DRAFT.

Falcon research failed with an authentication error and its configured
perplexity-lite fallback reported insufficient quota. Neither produced a research
report. These notes document manual primary-source research; no provider-named
research file was written. The annotation-reviewer and core-function synthesis
guidance were applied, with an independent read-only reviewer assessing all rows.

### Physiological core and processing products

The principal function is a single endocrine mechanism: secreted hepcidin binds
ferroportin, inhibits iron export and promotes transporter internalization and
degradation. Direct transport inhibition and transporter removal are compatible
mechanisms, not competing interpretations of separate gene functions.

- PMID:15514116, *Hepcidin regulates cellular iron efflux by binding to ferroportin
  and inducing its internalization*: “After binding, ferroportin was internalized
  and degraded, leading to decreased export of cellular iron.” The native cache
  is abstract-only.
- PMID:29237594, *Structure-function analysis of ferroportin defines the binding
  site and an alternative mechanism of action of hepcidin*: “We experimentally
  confirmed hepcidin-mediated occlusion of Fpn in the absence of endocytosis in
  multiple cellular systems:”. The native cache is abstract-only; the accessible
  abstract explicitly describes the relevant inhibition experiments.
- PMID:32814342, *Structure of hepcidin-bound ferroportin reveals iron homeostatic
  mechanisms*: “Hepcidin binds ferroportin in an outward-open conformation and
  completely occludes the iron efflux pathway to inhibit transport.” The retained
  full text includes human ferroportin structural and transport experiments.
  The proposed iron-occupancy feedback model should not be restated as an
  unconditional rule that only iron-loaded transporters can bind hepcidin.
- PMID:22682227, *Hepcidin-induced endocytosis of ferroportin is dependent on
  ferroportin ubiquitination*: “Our study demonstrates that ubiquitination is the
  functionally relevant signal for hepcidin-induced ferroportin endocytosis.”
  The retained cache is abstract-only; this statement does not require importing
  an older JAK2/phosphorylation model as an established HAMP core function.

The native UniProt record describes an 84-residue precursor with a signal peptide
at residues 1–24, hepcidin-25 at 60–84 (PRO_0000013379), and hepcidin-20 at 65–84
(PRO_0000013380). These are proteolytic processing products, not splice isoforms.
No synthetic isoform flags or residue substitutions were added to GOA contexts.
PMID:16141345, *The N-terminus of hepcidin is essential for its interaction with
ferroportin: structure-function study*, reports loss of activity after deleting
five N-terminal residues. Its abstract describes ferroportin-expressing cultured
cells and mouse hypoferremia assays; it does not directly establish a physiological
role for circulating human hepcidin-20.

Human HAMP mutations in PMID:12469120 establish juvenile hemochromatosis and
support systemic iron regulation. They are not a direct measurement of every
intestinal transport step. PMID:19740974 adds human oral-iron loading and
absorption data: “Oral iron loading, measured by stable-isotope appearance curves,
increases circulating hepcidin.” Its first study found only a modest association
with dietary iron bioavailability, so the review does not treat hepcidin
concentration as a complete predictor of absorption or as the upstream iron sensor.

### Two refinements

1. **GO:0141108 transporter regulator activity → GO:0097690 iron ion
   transmembrane transporter inhibitor activity.** The cited PMID:29237594
   establishes the inhibitory direction and ferroportin substrate context. This
   refines a valid broader annotation and reuses an already present term; it is
   not a NEW annotation or a claim that the broader curated activity is false.
2. **GO:0032436 positive regulation of proteasomal ubiquitin-dependent protein
   catabolic process → GO:1905167 positive regulation of lysosomal protein
   catabolic process.** PMID:37277838 was read in full from the retained native
   cache. Its described ferroportin pathway includes “thus signaling for its
   internalization and lysosomal degradation.” The ubiquitination inhibitor
   PYR-41 is not evidence that the subsequent destruction occurs in a proteasome.
   The replacement names the documented route while retaining HAMP's regulatory
   role, not attributing protease activity to the peptide.

QuickGO definitions were retrieved directly on 2026-11-14 from
`https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1905167,GO:0032436,GO:0097690,GO:0141108`:

- GO:1905167: “Any process that activates or increases the frequency, rate or
  extent of lysosomal protein catabolic process.”
- GO:0032436: “Any process that activates or increases the frequency, rate or
  extent of the breakdown of a protein or peptide by hydrolysis of its peptide
  bonds, initiated by the covalent attachment of ubiquitin, and mediated by the
  proteasome.”
- GO:0097690: “Binds to and stops, prevents, or reduces the activity of an iron
  ion transmembrane transporter.”
- GO:0141108: “Binds to and modulates the activity of a transporter.”

All four were returned as non-obsolete. The review retains the original GOA term
ids and places refinements only under proposed replacement terms.

### Transcriptional annotation remains unresolved

The ISS GO:0000122 annotation names mouse Hamp, UniProtKB:Q9EQ21, as its source.
Live QuickGO donor tracing identifies GO:0000122, IMP, PMID:18539898. That paper's
native abstract states: “Iron overload developed by Smad4- and Hamp1-deficient mice
also increased Bmp6 transcription.” Its full text was not obtained. This accessible
evidence cannot settle whether the curated regulatory interpretation is specific
to hepcidin or follows indirectly from altered iron balance. The action is
UNDECIDED and the source assessment is UNRESOLVED; neither the mouse experimental
annotation nor the reference is labelled erroneous. This donor paper is distinct
from the older JAK2 literature.

### Antimicrobial activity and physiological limits

PMID:11113131 reports antibacterial and antifungal activity of processed human
hepcidins, including Gram-positive organisms. PMID:11034317 also reports peptide
isolation from human blood and dose-dependent microbial sensitivity in radial
diffusion assays. These support the immune-response and Gram-positive-defense
contexts. Both are retained as non-core because the reviewed experiments do not
establish their quantitative contribution at physiological human concentrations
and ionic conditions. The biological knowledge gap is bounded to the physiological
role of hepcidin-20, rather than presented as uncertainty about the well-established
ferroportin-regulatory mechanism.

### PAINT and GO-CAM context

The existing PTHR16877 PAINT slice contains six non-negated IBD assertions at
PTN002704075: GO:0005179, GO:0005576, GO:0006879, GO:0050830, GO:0060586 and
GO:0097690. These match all six seeded IBA contexts. Human P81172 is an experimental
seed at the ancestral node; its presence is expected and is not circular evidence.
No claim of target-specific loss, family-wide functional divergence, or a new
phylogenetic boundary is made. The native InterPro fetch updated family metadata
and membership data; those machine-generated files were not hand-edited.

The retained GO-CAM index and source models already represent HAMP as hormone
activity in model 66187e4700001156 and transporter regulator activity in
66e382fb00001606 and 66e382fb00001786, in extracellular iron-homeostasis roles.
The single core-function unit unifies these physiological and molecular roles.
No NEW process was inferred from apparent pathway incompleteness.

### Source preservation and validation

The fetched UniProt and GOA files are retained unchanged. Five existing publication
caches were reused from the base Git revision after confirming that refetching
changed only publication-type metadata and whitespace, not scientific text.
Additional publication caches were produced by the native fetcher. All supporting
snippets were checked against their exact retained sources after whitespace
normalization before applying the review. Formal schema, ontology, reference,
quote and history validation follows the completed review.

### Completed local checks

`just validate human HAMP` passed with no curation warnings. The reference
validator checked 40 supporting snippets and 11 titles with no issues; the
independent quote check verified 51 occurrences with zero unchecked or blocking
quotes. The canonical renderer produced HTML in memory successfully, without
writing a generated HTML file; this was not a graphical inspection. Independent
biological QA found no actionable issue and confirmed that PMID:37277838 includes
hepcidin experiments, not merely transferrin findings. A preliminary schema check
caught the suggested-question object format, which was corrected before the final
successful validation.

### PR #6372 review follow-up — 2026-11-14

The two processing products are now explicitly represented in `functional_isoforms`
as `CLEAVAGE_PRODUCT` records mapped to the native UniProt chain identifiers and
residue ranges. This schema field covers proteolytic products as well as splice
classes. Their descriptions distinguish the established endocrine action of
hepcidin-25 from the bounded cell/mouse truncation result and unresolved
physiological antimicrobial contribution of hepcidin-20. Native GOA isoform fields
remain unchanged.

The core unit no longer lists GO:0007165 signal transduction or GO:0010039 response
to iron ion. The specific ferroportin-regulatory mechanism remains; the corresponding
original GOA rows retain their supported ACCEPT decisions.

The suggested extracellular-region refinement was checked against the live
[QuickGO term service](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005615,GO:0005576)
on 2026-11-14. GO:0005615 was returned as **obsolete extracellular space** with
`isObsolete: true`, whereas GO:0005576 extracellular region was non-obsolete.
Accordingly, all four GO:0005576 contexts retain ACCEPT with the ontology check
recorded in their reasons; an obsolete replacement is not proposed. The annotation
action counts, native fields, references and supporting quotations are unchanged.

Follow-up validation passed: `just validate human HAMP`, the new history record,
and canonical rendering in memory. References and all supporting quotations were
preserved exactly from the previously validated revision. The runtime guard
confirmed unchanged `uv.lock` and no checkout-local environment.
