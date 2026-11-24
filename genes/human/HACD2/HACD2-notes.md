# HACD2 (Q6Y1H2) review notes

This is the HACD2 paralog-companion correction arising from the HACD1 ClinGen review
in [PR #6311](https://github.com/ai4curation/ai-gene-review/pull/6311). The campaign's
user-authorized generic-binding exception applies to this companion work: supported
interactions remain KEEP_AS_NON_CORE unless a specific refinement is supported.
HACD2 is not being added as a ClinGen Mendelian association or counted as a ClinGen
completion.

## Identity and family

- HGNC:9640; UniProt Q6Y1H2; gene HACD2, synonym PTPLB (protein-tyrosine
  phosphatase-like member B). RefSeq NP_940684.1 / NM_198402.5. 254 aa,
  ER multi-pass membrane protein with 5 predicted TM helices.
  [file:human/HACD2/HACD2-uniprot.txt "RecName: Full=Very-long-chain (3R)-3-hydroxyacyl-CoA dehydratase 2"]
- Belongs to the HACD (PTPLA/PTPLB) very-long-chain fatty acid dehydratase family;
  contains a Pfam PF04387 (PTPLA) domain / InterPro IPR007482 "Tyr_Pase-like_PTPLA".
  Despite the "protein tyrosine phosphatase-like" name, it has no phosphatase activity.
  [file:human/HACD2/HACD2-uniprot.txt "Shares some similarity with tyrosine phosphatase proteins but"]
- One of four mammalian HACD paralogs (HACD1-4). HACD1 (PTPLA) is muscle-enriched;
  HACD2 (PTPLB) is the ubiquitously/broadly expressed dehydratase.
  [file:human/HACD2/HACD2-uniprot.txt "Highly expressed in testis, spleen, prostate, colon"]

## Core molecular function

- EC 4.2.1.134; a lyase. Catalyzes the dehydration of a very-long-chain
  (3R)-3-hydroxyacyl-CoA to a very-long-chain (2E)-enoyl-CoA + H2O
  (RHEA:45812). This is the THIRD step of the microsomal (ER) VLCFA
  four-step elongation cycle (condensation → reduction → dehydration → reduction).
  [file:human/HACD2/HACD2-uniprot.txt "a very-long-chain (3R)-3-hydroxyacyl-CoA = a very-long-chain"]
  [file:human/HACD2/HACD2-uniprot.txt "This enzyme catalyzes the dehydration of the"]
- UniProt curates C16-C26 reaction entries; this is not a statement that a full
  chain-length kinetic panel was measured. KM = 121.7 uM for 3-hydroxypalmitoyl-CoA.
  [file:human/HACD2/HACD2-uniprot.txt "KM=121.7 uM for 3-hydroxypalmitoyl-CoA (at 37 degrees Celsius)"]
- Experimentally established in [PMID:18554506], which characterized all four mammalian
  HACD proteins by rescue of a PHS1-shutoff yeast strain and in vitro 3-hydroxypalmitoyl-CoA
  dehydratase assays. [PMID:18554506 "in growth suppression experiments using a PHS1-shut off yeast strain and/or in vitro 3-hydroxypalmitoyl-CoA dehydratase assays"]
  The best-supported GO MF term is GO:0102158 (very-long-chain (3R)-3-hydroxyacyl-CoA
  dehydratase activity), which matches the UniProt catalytic activity / EC exactly;
  GO:0018812 (3-hydroxyacyl-CoA dehydratase activity) is its more general parent.

## Localization

- ER membrane, multi-pass. [PMID:15024066] describes it as "an integral protein of the
  endoplasmic reticulum membrane with four membrane-spanning alpha helices"
  [PMID:15024066 "an integral protein of the endoplasmic reticulum membrane with four"]
  (UniProt topology annotates 5 TM helices). [PMID:18554506] also reports subcellular
  location (FUNCTION/SUBCELLULAR LOCATION in the paper's scope line).
  [file:human/HACD2/HACD2-uniprot.txt "Endoplasmic reticulum membrane"]

## Interactions / complex

- Part of the ER VLCFA elongase complex. UniProt SUBUNIT: "May interact with enzymes of
  the ELO family (including ELOVL1)" and may be part of a larger elongase complex; the
  enzyme-binding IDA (GO:0019899) traces to these ELOVL condensation-enzyme interactions
  reported in [PMID:18554506]. [PMID:18554506 "We also establish that HACD proteins interact with the condensation enzymes ELOVL1-7, with some preferences."]
- Interacts with TECR (the downstream trans-2-enoyl-CoA reductase, step 4) via its third
  lumenal loop; HACD2-TECR forms a stable complex ([PMID:38422897]).
  [PMID:38422897 "we identified a stable complex of human HACD2-TECR based on extensive in vitro characterizations"]
  [file:human/HACD2/HACD2-uniprot.txt "Interacts\nCC       (via the third lumenal loop) with TECR (PubMed:38422897)."]
  (Note: quote above spans two CC lines in UniProt so cannot be used verbatim as
  supporting_text; TECR interaction verified from the abstract of PMID:38422897 instead.)
- Interacts with BCAP31 (BAP31), which acts as an ER chaperone/quality-control factor
  regulating HACD2 turnover; HACD2/PTPLB turns over rapidly via the proteasome.
  [PMID:15024066 "PTPLB turns \nover rapidly through degradation by the proteasome system"]
- The IntAct-sourced GO:0005515 "protein binding" IPI annotations come from
  high-throughput interactome maps (PMID:25416956 HuRI/CCSB Y2H; PMID:32296183 HuRI;
  PMID:30021884 crosslinking-MS histone landscape) plus PMID:15024066 (BCAP31) and
  PMID:38422897 (TECR). The three HT-interactome papers' cached full text does not
  mention HACD2/PTPLB by name (interactions are in supplementary data), consistent with
  large-scale screens. Bare "protein binding" is uninformative and is marked as
  non-core under the ClinGen exception when no supported specific refinement is available.
  The three TECR-specific contexts are refined to enzyme binding using independent
  HACD2-TECR complex evidence from PMID:38422897.

## Not a phosphatase

- GO:0004725 protein tyrosine phosphatase activity is a NOT (negated) annotation
  (IMP, PMID:15024066). Despite the PTPLB "phosphatase-like" name and a MUTAGEN of
  Pro-101 tested for phosphatase activity, HACD2 has no phosphatase activity.
  [file:human/HACD2/HACD2-uniprot.txt "it has probably no phosphatase activity"]
  [file:human/HACD2/HACD2-uniprot.txt "P->R: Does not restore any protein tyrosine"]

## Downstream biology (non-core)

- VLCFAs made by this elongation cycle are precursors of membrane lipids and lipid
  mediators, including sphingolipids/ceramides.
  [file:human/HACD2/HACD2-uniprot.txt "participates in the production of"]
  Sphingolipid biosynthetic process (GO:0030148, IGI involving yeast Phs1, UniProt P40857) is a
  downstream consequence of supplying VLCFAs, not the direct catalytic function — kept
  as non-core.

## Curation decisions summary

- Core MF: GO:0102158 very-long-chain (3R)-3-hydroxyacyl-CoA dehydratase activity.
- Core BP: fatty acid elongation (GO:0030497) and very long-chain fatty acid biosynthetic
  process (GO:0042761).
- Core CC: endoplasmic reticulum membrane (GO:0005789) and the experimentally supported
  ER compartment (GO:0005783).
- GO:0080023 "(2E)-enoyl-CoA hydratase activity" (IEA/Rhea) already defines the
  reversible dehydration chemistry. MODIFY to GO:0102158 for enzyme-class specificity.
  The earlier reverse-direction argument incorrectly inferred reaction direction from
  the hydratase label; it was not a valid reason for this refinement.
- GO:0005515 protein binding (5 IPI): three TECR-specific contexts → MODIFY to
  GO:0019899 enzyme binding; the BAP31 and mixed-partner HuRI contexts →
  KEEP_AS_NON_CORE under the ClinGen exception. Generic binding is not itself
  over-annotation.
- Sphingolipid biosynthesis, general fatty acid biosynthetic process, long-chain
  fatty-acyl-CoA biosynthetic process, and the original GO:0019899 IDA enzyme-binding
  annotation → KEEP_AS_NON_CORE.

## 2026-11-12: correct the GO:0080023 refinement rationale

This entry supersedes the reaction-direction explanation in the earlier curation
summary. The existing `MODIFY` action and replacement `GO:0102158` are retained.
The [official GO:0080023 definition](https://www.ebi.ac.uk/QuickGO/term/GO:0080023)
is “Catalysis of the reaction: a (3R)-3-hydroxyacyl-CoA = a (2E)-enoyl-CoA + H2O.”
Thus its hydratase label does not make the annotation chemically wrong.

The official `is_a` chain is `GO:0102158` → `GO:0080023` → `GO:0018812`.
[GO:0102158](https://www.ebi.ac.uk/QuickGO/term/GO:0102158) supplies the more
specific ER elongation enzyme class already supported for HACD2 by its retained
IDA annotation from PMID:18554506 and UniProt Q6Y1H2 catalytic record
[file:human/HACD2/HACD2-uniprot.txt, “a very-long-chain (3R)-3-hydroxyacyl-CoA = a very-long-chain”].
This supports refinement by specificity without claiming a measured C18-C26
substrate-kinetics panel. The original physiological-direction quotation remains
valid source evidence and is preserved.

Definitions and parent relationships were checked on 2026-11-12 using the
[QuickGO term API](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0080023,GO:0018812,GO:0102158).
The 1,634-byte response has SHA256
`d4659da499d24a79087d692c55437c99aabc82813f9c6336f6a59076e9c9efe7`.
This is a bounded rationale correction: the other 26 annotation contexts,
all actions, native source fields, earlier quotations and `INITIALIZED` status
are preserved. It is not a full reassessment or ClinGen completion.


## 2026-11-14: PR #6316 review follow-up

Correct the earlier reaction-direction claim in place, including why it was wrong,
and remove stray markup. Refine both GO:0018812 contexts to GO:0102158: the supported
HACD2 enzyme class is more informative than the general dehydratase class. UniProt's
generic very-long-chain reaction carries ECO:0000269|PubMed:18554506; physiological
direction is separately curated. Neither a hydratase label nor an equilibrium `=`
reaction establishes an incompatible direction.

The directly inspectable ontology evidence is from the official
[QuickGO term endpoint](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0018812,GO:0080023,GO:0102158),
checked 2026-11-14. [QuickGO GO/about](https://www.ebi.ac.uk/QuickGO/services/ontology/go/about)
identifies `http://purl.obolibrary.org/obo/go/releases/2026-11-12/extensions/go-plus.owl`.
The exact GO:0080023 `definition.text` is "Catalysis of the reaction: a
(3R)-3-hydroxyacyl-CoA = a (2E)-enoyl-CoA + H2O." Its `children` contain
`{"id":"GO:0102158","relation":"is_a"}`; GO:0018812's `children` contain
`{"id":"GO:0080023","relation":"is_a"}`. These small source fragments record the
claimed edges directly, rather than relying on the earlier uncommitted response hash.

Also correct the five legacy generic-binding judgments: the three TECR-specific
contexts are refined to enzyme binding with independent complex evidence; the BAP31
and mixed HuRI contexts are retained as non-core under the ClinGen exception. Do not
apply the TECR-specific refinement to every partner in the combined HuRI context.
Accept the two informative ER-compartment annotations as core localization,
without using term breadth to argue against the localization. All 27 native contexts and
source fields are preserved. No NEW annotation or ClinGen completion is added.

Final follow-up accounting: 27 contexts; 14 ACCEPT, 7 KEEP_AS_NON_CORE, 6 MODIFY.
The status helper reports DRAFT; the stale INITIALIZED value is reconciled to that
computed state. The dated 2026-11-12 counts above describe the earlier commit.

Correct the older donor-name error: [P40857 is yeast Phs1](https://www.uniprot.org/uniprotkb/P40857/entry),
verified from the official UniProt entry on 2026-11-14. It is a dehydratase, not
KAR/HSD17B12. The native IGI source identifier is unchanged.


## 2026-11-14 UTC — Companion scope and source-context clarification

The 33 native GOA rows are represented by 27 retained review contexts. Six HuRI
partner rows map to one legacy context; the two PMID:38422897 TECR rows from IntAct
and UniProt map to one context. The mixed HuRI context includes TECR, but its other
partners do not support a uniform enzyme-binding replacement. Its non-core generic
action does not reject the TECR-specific interpretation in the three TECR-only
contexts. This bounded correction preserves the source rows and context structure.

The core-function description now distinguishes the curated elongation enzyme class
and C16 assay from an unmeasured C18-C26 panel. Annotation actions remain 14 ACCEPT,
7 KEEP_AS_NON_CORE and 6 MODIFY; status remains DRAFT, with no NEW annotation or
ClinGen completion credit. The top-level biological description is only rewrapped.
