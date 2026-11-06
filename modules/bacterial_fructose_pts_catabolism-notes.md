# Fructose PTS comparative audit

## 2026-11-06 — boundary and evidence assessment

The starting module has four reaction parts and six distinct exemplar accessions,
but only five existing gene reviews: PSEPK FruA/FruB/FruK and ECOLI FruA/FruK.
All five are DRAFT. Their 54 annotation payloads and twelve raw/provider sources
were frozen before review in the audit baseline. XANCP FruB previously had no
review. Nine normal fetches now add XANCP, RHOCA and AZOBR three-protein panels;
the separate seed baseline records their initial annotation payloads and sources.

The intended boundary remains PEP-dependent fructose uptake through a **fused
FruB relay**, ending at fructose 1,6-bisphosphate. E. coli provides experimentally
useful component comparisons; its FruB lacks EI and requires separate PtsI, so
an E. coli FruA/FruK pair does not demonstrate this complete architecture.
Sequence order in the fused protein is EIIA–HPr–EI, whereas phosphate flows
EI→HPr→EIIA. Fusion does not by itself demonstrate that every transfer is
intramolecular rather than between subunits.

The 2014 PTS review explains both the relay chemistry and the existence of
regulatory PTS homologs without transport components
[PMID:24847021, "These PTSs are therefore probably not involved in carbohydrate transport but carry out only regulatory functions."].
This is essential comparative context: a PTS domain hit does not establish
fructose uptake. Its account of archaeal PTS also supersedes the broad absence
claim in the older 2005 comparative survey. The latter remains useful as a
historical genome comparison, not a current census of the tree of life.

## Family and architecture constraints

Live UniProt P08839 (E. coli PtsI, standalone enzyme I) belongs to
PTHR46244:SF6, the same subfamily currently assigned to fused FruB. The result
is preserved in `analysis/module_audits/bacterial_fructose_pts_catabolism/standalone-ei-control.yaml`.
Therefore that subfamily is not a sufficient fused-FruB selector. Both FruB
parts require the EI, HPr and fructose-specific EIIA functions in the same
polypeptide, plus compatible phosphate handoff to the transport component.
The standalone PtsI is an architecture-negative control, not a missing
member to add to the fused family descriptor.

PSEPK and RHOCA FruA records contain two EIIB-like domains and an EIIC domain.
The AZOBR FruA1 record detects one EIIB domain explicitly and two IIB-like
structural-superfamily matches. A mandatory count of two PROSITE/Pfam hits
would confuse detection with biological architecture. E. coli biochemical
work distinguishes the facilitating B′ domain from the catalytic B domain
(PMID:8626640); do not call both catalytic. The functional requirement is
compatible phosphotransfer and fructose translocation, with the architecture
of each exemplar documented separately.

GO:0022877 describes the **net** phosphohistidyl-carrier-to-fructose reaction.
GO:0090582 describes the immediate phosphocysteine-to-fructose step. The
presence of a catalytic EIIB cysteine does not, by itself, falsify the net
reaction. Keep donor bookkeeping consistent between the function term,
substrates, products and connection to FruB; do not change only the term.

## Cross-species evidence and limits

- P. putida KT2440: PMID:18296519 supports fructose-dependent communication
  with the nitrogen PTS branch. Its measured PtsN phosphorylation is not a
  direct assay of every internal FruB transfer. The same study reports that
  PtsN cannot substitute for FruB in fructose transport. PMID:27933319 gives
  pathway and regulatory context; its Cra/F1P sensing findings must not be
  generalized to E. coli without independent evidence.
- X. campestris: PMID:7496537 and PMID:1655739 establish the classic fused
  system. Current UniProt accessions name ATCC33913, whereas the experimental
  cloning studies use ATCC13951, and FruB records sequence differences. Treat
  the current exemplars as strain-qualified homologs until identity is proved.
  PMID:1650911 describes an alternative non-PTS fructose route; loss of this
  module must not be equated with inability to use fructose by any route.
- R. capsulatus: PMID:2193161 describes a three-moiety fusion with EIIA-like,
  HPr-like and EI-like regions. Its phosphorylation sites are explicitly
  **predicted from sequence comparisons**, not all directly measured.
  PMID:2254279 and PMID:1850730 ground the companion transporter and kinase.
  Primary sequence records link the proteins to DSM938/37b4 and X53150.
- A. brasilense Sp7: PMID:39817736 directly compares the two Fru-PTS loci.
  The main locus comprises AMK58_25885/25880/25875 (FruB1/K1/A1). The
  consultation verified exact whole-sequence matches to current UniProt
  A0A0P0ES92/A0A0P0F764/A0A0P0F8C9; the reproducible mapping is being saved
  with the member reviews. The principal FruA1 mutant and the second-locus
  mutant differ in growth and complementation. A second homologous locus is
  not an interchangeable default pathway. Fructose-induced T6SS and
  chemotaxis are outside this metabolic module.

The current positive panel spans Alpha- and Gammaproteobacteria, but a
Pseudomonadota-only scope is not yet justified. The 2008 comparative study
(PMID:18485189) includes Deinococcus FruB ancestry. PMID:21822900 reports
ATP-dependent fructose phosphorylation with a fruB pseudogene in its tested
D. radiodurans material; reciprocal membrane/cytosol reconstitution with
R. capsulatus follows the cytosolic donor system. More recent resequencing
(PMID:38962131) recovers complete KDR_B0075 in ATCC13939K and reports intact
fruR-fruBKA in ATCC13939 strains. This is a strain/gene-model boundary, not
proof that the 2012 phenotype or the 2024 intact sequence applies to every
D. radiodurans strain. Resolve exact strain/protein mappings and whether the
PEP-driven route has direct functional evidence before finalizing the taxon
envelope. The module remains at its original scope pending that assessment.

## Work still required

Complete all fourteen member reviews, curate the module reference assessments
and per-step findings, check actual family membership across the panel, and
implement capacity cases that distinguish fused from split relays, compatible
from regulatory PTS proteins, and the two Sp7 loci. Preserve the original
machine annotation payloads and raw sources. Only then finalize the module,
run scoped and full validation, publish its own PR, and shepherd it to merge.
The missing GO term belongs in notes/proposed terms, not a biology knowledge
gap: a wet-lab experiment would not create an ontology class.
