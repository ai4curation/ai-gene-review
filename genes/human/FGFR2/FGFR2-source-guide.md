# FGFR2 evidence guide

This guide describes the source boundaries of the 2026-10-27 assessment. The
[source evidence](FGFR2-source-evidence.yaml) indexes the actual database joins,
original-paper locators and response hashes. Annotation indices are zero-based.
The review YAML remains the single record of decisions.

## Receptor activity and product boundaries

FGFR2 is the FGF receptor and tyrosine kinase; GRB2 is a signaling adaptor that
binds it. An interaction with GRB2 does not give FGFR2 GRB2's adaptor activity.
The narrower FGF-binding replacements at indices 32 and 34 are supported by
actual ligand–receptor structural results, rather than by a general objection
to the term protein binding.

The original PMID:8663044 Table I, Materials and Figure 3 distinguish **human
FGFR2b** from **mouse FGFR2c**, expressed in murine BaF3 cells. FGF1 can activate
both forms. Table II and the accompanying Results compare mitogenic response
under the study's assay conditions; those values are not ligand-binding
constants or a universal specificity ranking. The paper itself discusses
cellular and heparan-sulfate context. PMID:10618369 Methods and structural Results
use human FGF1 and an extracellular FGFR2IIIc fragment. The recovered
PMID:11390973 Results/Figure 1–2 captions identify altered FGF2 contacts in Apert
mutant structures; complete construct Methods were not recovered.

PMID:16844695 Methods and Results/Figures 1–5 and 7–10 concern human FGFR2IIIc
and engineered glycosylation/C278F mutants in murine MC3T3-E1 and COS7 cells.
The original distinguishes surface receptor from retained intracellular pools,
with cell-dependent phosphorylation, dimerization and PLCG1 readouts. These are
not experiments assigning functions to each natural splice product.

The immutable UniProt alternative-product block, lines 892–934, identifies
P21802-1 as IIIc/BEK and P21802-3 as IIIb/KGFR. Products **named** 8 and 13 are
P21802-14 and P21802-19, respectively. Six sequence-note strings were repaired
only by joining their literal UniProt continuation lines. All 17 product
identities, names and order remain unchanged. Secretion alone does not establish
a physiological decoy function.

## Inference sources

- **PAINT:** the complete PTHR24416 TSV has 159 assertions, including 23 negative
  assertions. Eight positive IBD records exactly join the imported GOA nodes and
  terms. The tree request timed out and the MSA capture stopped at its size bound;
  neither establishes a target path or canonical sequence match. Family negatives
  are retained in the evidence index without asserting that they apply to FGFR2.
  The ancestral curator judgment is not rejected because of donor count,
  self-WITH entries, or the independent access limit.
- **Mouse ISS:** all 75 contexts join same-term positive records for mouse Fgfr2
  P21803 in the complete 206-record official response. Donor references,
  evidence codes and qualifiers are recorded. These are curated ortholog
  inferences, not newly read human experiments or independent re-analysis of all
  donor papers. Tissue-specific developmental claims can remain non-core without
  being false.
- **Rat Ensembl transfers:** all 11 contexts join rat Fgfr2 F1LSG7 in the complete
  171-record response. Expression-based response terms are retained at their
  response scope; they do not establish a signaling-effector mechanism.
- **InterPro and ARBA:** the actual P21802 response contains 14 target matches.
  Kinase-domain and receptor-family GO mappings are distinct from direct assays.
  Nine of 11 current ARBA rules have a condition set matching the saved target
  domains/FunFams and human lineage. Current ARBA00084763 and ARBA00089537 do not;
  their historical versions were not reconstructed. This is a provenance limit,
  not proof that the original electronic annotation was fabricated or false.
- **UniProt mappings:** EC, keyword and subcellular mappings are retained as
  curated database evidence, with extracellular soluble products, membrane
  receptors and trafficking compartments kept distinct.

## Reactome locations

All 58 inherited Reactome references have actual participant responses containing
P21802-family reference entities. The evidence index records each event, physical
entity identifiers and target accessions. These support target membership in
specified receptor/complex models; they do not give FGFR2 the activity of PI3K,
RAS exchange factors, or another component named by a reaction or set.

Most models contain membrane receptor complexes. R-HSA-109699 and R-HSA-2400009
also include a cytosol-labelled target-containing PI3K complex, which does not
place every component in the same compartment. The retained plasma-membrane
location has independent receptor support. Mutant/fusion contexts and the mixed
human/mouse IIIa-TM model in R-NUL-8853328 must not be assigned to all 17 natural
human products.

## Binding-source adjudication

| Indices | Actual evidence and boundary |
| --- | --- |
| 37 | PMID:22726438 identifies GRB2 as adaptor and FGFR2 as receptor. Full operative interaction evidence was not recovered; receptor–adaptor binding is not adaptor activity. |
| 38, 40 | IntAct identifies exact FGFR2–FGF1 or FGFR2–FGF2 NMR/direct-pair records despite drug-focused titles. Original panels remain unread, as does the later erratum associated with PMID:23597563. |
| 39 | PMID:25241761 IntAct records identify HeLa proximity-ligation evidence with FGF1/FGF10. Proximity is not a direct-affinity measurement; original panels remain unread. |
| 41 | Genuine BioPlex network rows identify FGFR1/FGF2 in 293T and FGF1 in HCT116. Original Methods use tagged human baits and gene-level network assembly. Association is supported; direct interfaces and natural-isoform specificity are not established by those rows. |
| 42 | PMID:35384245 original Results/Methods and Figure EV1 distinguish FGFR1 co-IP and FGFR1/FGF2 AP-MS association from the GRB2 BioID proximity record. The assay uses tagged human RTKs and phosphatase inhibition. |
| 43 | PMID:35922511 original supplementary workbooks contain the reciprocal FCER2–FGFR2 screen entries and network pair. The original processing Methods explicitly name FGFRs among recurrent nonspecific candidates. The target is accessible, but pair-specific physiological binding and orthogonal validation remain unresolved. |

For index 43, MOESM4 Table 1 identifies P21802/FGFR2 and P06734/FCER2; Table 2
contains the reciprocal raw cells. MOESM6 Figure1_network row 165 reports the
pair. The heatmap uses another processed metric. The author field `Expected=0`
is not a negative binding experiment, and the aggregate validation rate does
not validate every individual pair.

## Original-source access limits

The cache's `full_text_available` field describes that immutable generated cache,
not every separate source read. PMID:33961781 has a partial cache but a separately
read original Methods text and exact network rows. Conversely, an HTTP 200 BioC
response saying no article was found is not full-text access.

Original operative evidence remains incomplete for the sources listed in
`access_limits` in the evidence file. Their source-specific decisions remain
UNDECIDED; other supporting annotations are retained independently. In particular,
the PMID:21412257 abstract does not justify rejecting the negative keratinocyte
proliferation annotation, and endogenous nuclear localization is not dismissed
merely because FGFR2 is a transmembrane receptor. The original PMID:17959718
Methods instead identify mouse explants and a mouse FGFR2b–human Fc probe; the
source-specific human localization question is left open.

All inherited publication quotations and reference/findings associations remain
unchanged. No new quotations were added. Current assessments and precise locators
carry the new evidence boundaries; the inherited provider report is background,
not a substitute for reading a primary source.
