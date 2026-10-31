# FGFR2 evidence guide

This guide describes the source boundaries of the 2026-10-27 assessment. The
[source evidence](FGFR2-source-evidence.yaml) indexes the actual database joins,
original-paper locators and response hashes. Annotation indices are zero-based.
The review YAML remains the single record of decisions.

## Receptor activity and product boundaries

FGFR2 is the FGF receptor and tyrosine kinase; GRB2 is a signaling adaptor that
binds it. An interaction with GRB2 does not give FGFR2 GRB2's adaptor activity.
The FGF-binding replacements at indices 32–36 identify measured ligand
recognition. Indices 32 and 34 use recovered original structural evidence;
33, 35 and 36 use explicit positive abstract-level reports with complete
Methods limits retained. No replacement is inferred solely from a paper title.

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
| 37 | The PMID:22726438 abstract explicitly reports dimeric GRB2 binding FGFR2 C termini. Complete Methods remain unread; the positive association does not give FGFR2 adaptor activity. |
| 38, 40 | Seven positive human IntAct NMR/direct-pair records identify FGFR2–processed FGF1 or FGFR2-fragment–FGF2-fragment binding. Together with independently established FGF recognition, these support refinement to FGF binding. Original panels and the PMID:23597563 erratum remain unread; no all-product or new affinity assertion follows. |
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
`access_limits` in the evidence file. That limit is not a blanket judgment on
every claim. The `abstract_followup_2026_10_27` section records positive
statements directly present in the immutable abstracts and distinguishes them
from unresolved source details. Established generic receptor, kinase and membrane
claims can also be retained with explicit curator deference and independently
read target evidence. In particular,
the PMID:21412257 abstract does not justify rejecting the negative keratinocyte
proliferation annotation, and endogenous nuclear localization is not dismissed
merely because FGFR2 is a transmembrane receptor. The original PMID:17959718
Methods instead identify mouse explants and a mouse FGFR2b–human Fc probe; the
source-specific human assay is not newly verified. The generic surface location
is retained using independent human receptor evidence.

All inherited publication quotations and reference/findings associations remain
unchanged. No new quotations were added. Current assessments and precise locators
carry the new evidence boundaries; the inherited provider report is background,
not a substitute for reading a primary source.

## Follow-up: positive evidence versus missing detail

PMID:8386828 explicitly reports human FGFR2 binding/autophosphorylation and
nanomolar FGF5 binding; missing complete Methods do not erase that measurement.
PMID:15629145 reports KGFR Y769-mutant effects on PLCG/FRS2 phosphorylation,
MAPK activation and proliferation. Generic receptor and membrane statements
also have independent target support. PMID:1697263 reports cloned human BEK
membrane architecture and ligand binding. A clinical NAS reference is not
misrepresented as an activity experiment when an established generic receptor
function is retained by explicit curator deference.

The human urothelial abstracts PMID:16597614 and PMID:17471512 explicitly report
receptor localization. These support contextual compartments, not functions for
every product. The latter paper's ligand redistribution experiment is not
relabelled as receptor cytoplasmic or cortical evidence.

PMID:7874170 and PMID:7987400 positively associate FGFR2 variants with
craniosynostosis. The [official GO:0048701 definition](https://www.ebi.ac.uk/QuickGO/term/GO:0048701)
requires cranial-skeleton organization during the embryonic phase. That precise
stage remains unresolved in the accessible clinical evidence, and PMID:7874170
has an unread erratum. The narrower embryonic core is not restored merely from
a disease label; conserved bone and branching-organ signaling retain their
separately documented ortholog support. No core BP was omitted for presumed
ontology redundancy.

Supported BioPlex/RTK associations remain non-core under the
[ClinGen campaign instructions](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions).
The exact network/IntAct/original-source evidence is in the now-cited evidence
file; the inherited title quotation is not its sole support. AP-MS/co-IP
association and BioID proximity are not converted into an unsupported
direct-binding subtype. All inherited quotations remain untouched.

## Second follow-up: generic claims and source-specific limits

The three cell-surface rows retain the core receptor location; both cytoplasm
rows retain a contextual compartment. PMID:16597614 reports human receptor
microscopy, and PMID:1697263 describes human cell-surface BEK. The mouse
FGFR2b–human Fc probe in PMID:17959718 remains a mouse-reagent experiment,
and PMID:17471512 ligand redistribution is not relabelled as receptor evidence.

Osteoblast-proliferation and broad skeletal-morphogenesis rows retain non-core
roles with curator deference. The inspected UniProt FUNCTION statement supports
these target functions; human mutant-osteoblast responses in PMID:15190072 and
craniosynostosis genetics in PMID:7987400/7874170 give their respective contexts.
The unread PMID:15190072 proliferation/tissue endpoints are not newly claimed,
and the narrower embryonic-stage uncertainty remains.

The current complete 250-record QuickGO response has grouped cell/tissue
extensions on the positive PMID:16597614 siblings (120/121). The evidence index
preserves each connected group verbatim; it does not flatten alternatives into
a conjunction. The disputed generic rows have null current extensions; the old
ARBA row 25 has no current exact match. The historical TSV lacks an extension
column, so historical extension presence is not inferred and no original source
field is changed. Contextual microscopy still supports the generic compartment
without a claim about all tissues. PLA proximity at index 39 remains unresolved.
