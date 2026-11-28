# RETREG1 (FAM134B) curation notes

UniProt: Q9H6L5 (RETR1_HUMAN), 497 aa, HGNC:25964, chromosome 5p15.
Synonyms: FAM134B, JK1. PANTHER family PTHR28659 (RETICULON-LIKE PROTEIN),
subfamily PTHR28659:SF3; InterPro IPR043384 (RETREG1/3), IPR055255 (RETR1_RHD),
Pfam PF24456 (RHD_RETREG1-3).

No deep-research provider was reachable in this environment (`just deep-research
human RETREG1 --provider perplexity` failed: "Provider 'perplexity' not
available. Available: claude_code"), so these notes were assembled by hand from
the cached publications and the UniProt flat file. They are **not** a
provider-generated deep-research file.

## Summary of the biology

RETREG1/FAM134B is the founding mammalian ER-phagy (reticulophagy) receptor. It
is a multi-pass ER membrane protein with four transmembrane helices (60-80,
96-116, 119-139, 209-229); the reticulon-homology domain (RHD, residues 84-233 in
UniProt's annotation) spans the last three of them, with TM1 lying just N-terminal
to it, and there is a
large cytosolic C-terminal tail (230-497) carrying a LIR motif at 453-458
(`DDFELL`). The RHD bends and fragments ER membrane; the LIR hands the resulting
fragments to ATG8-family proteins on the forming autophagosome. Loss of function
causes hereditary sensory and autonomic neuropathy type 2B (HSAN2B, MIM:613115).

### ER-phagy receptor activity (core)

The founding paper established the family as ER-resident ATG8-binding receptors
[PMID:26040720 "members of the FAM134 reticulon protein family are ER-resident
receptors that bind to autophagy modifiers LC3 and GABARAP, and facilitate ER
degradation by autophagy ('ER-phagy')"], with a clean gain/loss phenotype
[PMID:26040720 "Downregulation of FAM134B protein in human cells causes an
expansion of the ER, while FAM134B overexpression results in ER fragmentation
and lysosomal degradation."] and a direct link to the human disease alleles
[PMID:26040720 "Mutant FAM134B proteins that cause sensory neuropathy in humans
are unable to act as ER-phagy receptors."].

The LIR is what makes it a receptor rather than just a membrane shaper
[file:human/RETREG1/RETREG1-uniprot.txt "DOMAIN: The LIR motif interacts with
ATG8 family proteins and is necessary to target the ER fragments to
autophagosomes for subsequent lysosomal degradation."]. UniProt records
interaction with all six human ATG8s (MAP1LC3A/B/C, GABARAP, GABARAPL1,
GABARAPL2), with a GABARAP-subfamily preference
[file:human/RETREG1/RETREG1-uniprot.txt "Shows higher affinity for GABARAPL1
than for MAP1LC3A or MAP1LC3B"]. A crystal structure explains the preference
[PMID:34854256 "we found that FAM134B bound to the GABARAP subfamily more
strongly than to the LC3 subfamily"; PMID:34854256 "demonstrated that FAM134B
used both its LIR core and the C-terminal helix to bind to GABARAP"].

Mutagenesis of the LIR (`DDFELL`→`AAAAAA`, 453-458) abolishes ATG8 binding
(UniProt MUTAGEN, from PMID:26040720), and `FELL`→`AELA` (455-458) abolishes
binding and reduces ER branching (from PMID:34338405).

### Membrane bending / ER scission (second molecular function)

Separately from the LIR, the RHD actively deforms the bilayer
[file:human/RETREG1/RETREG1-uniprot.txt "DOMAIN: The reticulon homology domain
provides capacity to bend the membrane and promotes ER scission"], and this was
shown with a cell-free assay [PMID:31930741 "oligomerization of ER-phagy
receptor FAM134B (also referred to as reticulophagy regulator 1 or RETREG1)
through its reticulon-homology domain is required for membrane fragmentation in
vitro and ER-phagy in vivo"]. The activity is switched up by RHD phosphorylation
[PMID:31930741 "Under ER-stress conditions, activated CAMK2B phosphorylates the
reticulon-homology domain of FAM134B, which enhances FAM134B oligomerization and
activity in membrane fragmentation"; file:human/RETREG1/RETREG1-uniprot.txt
"Phosphorylation at Ser-151 by CAMK2B enhances oligomerization and membrane
scission and reticulophagy activity."]. Oligomerisation is the activation step
[file:human/RETREG1/RETREG1-uniprot.txt "Homooligomer; oligomerization is
enhanced following endoplasmic reticulum stress and is mediated by the reticulon
homology domain"].

The HSAN2B variant G216R is instructive because it is a *gain* of this activity
[PMID:31930741 "FAM134B G216R, a variant derived from a type II hereditary
sensory and autonomic neuropathy (HSAN) patient, exhibits gain-of-function
defects, such as hyperactive self-association and membrane scission, which
results in excessive ER-phagy and sensory neuron death"]. Both too little and
too much RETREG1 activity kill sensory neurons.

### ER morphology

Across the family, ER shape depends on the receptors
[PMID:34338405 "FAM134A, FAM134B/RETREG1, and FAM134C are essential for
maintaining ER morphology in a LC3-interacting region (LIR)-dependent manner"],
and the FAM134B LIR is required for the fragmentation step
[PMID:34338405 "Genetic inactivation of the FAM134B LIR domain abrogates ER
fragmentation and subsequent lysosomal degradation (Khaminets et al, 2015)."].
MGI annotates the mouse ortholog Q8VE91 to GO:0007029 endoplasmic reticulum
organization (IMP, `acts_upstream_of_or_within`, PMID:34338405, assigned_by MGI,
2021-12-08; QuickGO annotation search, retrieved 2026-11-24); human RETREG1
carries no ER-organisation term in GOA. GO:0090158 (endoplasmic reticulum
membrane organization), the child that the comparable ER-shaping proteins carry
(ARL6IP1 IDA PMID:24262037, ATL3 IDA PMID:37102997 / IMP PMID:27619977,
ATL1/ATL2/RTN4 IMP, RTN1/2/3 IBA, REEP5 ISS; 74 human rows, QuickGO, retrieved
2026-11-24), is the better fit for a bilayer-deforming RHD protein and is
proposed here as a `NEW` row.

**Which paper anchors the row.** PMID:34338405 is corroboration, not the anchor.
Its ER-morphology experiments are electron microscopy and immunofluorescence of
*mouse* Fam134 single-knockout MEFs [PMID:34338405 "we subjected Fam134 single
knockout MEFs to electron microscopy analysis"], the swelling phenotype it
measures is for Fam134a and Fam134c [PMID:34338405 "the ER in Fam134a and
Fam134c knockout cells appeared swollen and dilated"], and for Fam134b it refers
back to Khaminets 2015 [PMID:34338405 "This phenotype was also found in Fam134b
knockout cells"]. The human loss-of-function receipt is PMID:26040720, so the
`NEW` row is IMP on that paper.

**On the LIR-dependence.** The morphology requirement being LIR-dependent does
not argue against RETREG1 participating in ER membrane organisation directly. ER
membrane leaves the network by being fragmented and then committed to
degradation, so both halves of the receptor do part of the work: the RHD supplies
the scission [PMID:31930741 "oligomerization of ER-phagy receptor FAM134B (also
referred to as reticulophagy regulator 1 or RETREG1) through its
reticulon-homology domain is required for membrane fragmentation in vitro and
ER-phagy in vivo"] and the LIR commits the fragment. GO:0090158 is therefore
attached to both core functions in the review, not to the membrane-bending one
alone.

### Procollagen quality control

Misfolded procollagen is a defined RETREG1 cargo [PMID:30559329 "the
ER-resident lectin chaperone Calnexin (CANX) and the ER-phagy receptor FAM134B
are required for autophagy-mediated quality control of endogenous procollagens";
PMID:30559329 "FAM134B binds the autophagosome membrane-associated protein LC3
and delivers a portion of ER containing both CANX and procollagen to the
lysosome for degradation"]. CANX acts as the luminal co-receptor that reads the
misfolded client and hands it to RETREG1. The paralogue study used the same
cargo [PMID:34338405 "Utilizing pro-Collagen I, as a shared ER-phagy substrate,
we observe that FAM134A acts in a LIR-independent manner and compensates for the
loss of FAM134B and FAM134C"].

**Which species each loss-of-function experiment is in.** The abstract's "siRNA
interference, CRISPR-Cas9 or knockout-mediated gene deletion" does not separate
them, and the full text does. The FAM134B siRNA screen is human Saos2 osteoblasts
[PMID:30559329 "we silenced genes belonging to different functional autophagy
clusters in Saos2 cells treated with BafA1 and quantified the levels of PC1
within lysosomes"; PMID:30559329 "we found that FAM134B silencing most
effectively inhibited PC1 delivery to lysosomes"]; the FAM134B CRISPR-Cas9
knockout is mouse MEFs, rescued by wild-type human protein but not by a
LIR-deleted mutant [PMID:30559329 "The impaired delivery of PC1 to lysosomes in
CRISPR Fam134b MEFs was rescued by reintroducing WT human FAM134B, but not a
FAM134B protein lacking the (LIR) motif"]. So the human receipt is the Saos2
siRNA result, and the MEF rescue is a cross-species argument for the human
protein's sufficiency.

**GO:0030574 does not fit, so the review proposes a term instead.** An earlier
draft of this review proposed `GO:0030574 collagen catabolic process` as a `NEW`
row, on the reasoning that human usage includes ITGB1 by IDA — a receptor that
delivers collagen for lysosomal degradation rather than cleaving it, which looked
like the same role shape as RETREG1. Checking the term definition settles it the
other way. GO:0030574 is defined as "The proteolytic chemical reactions and
pathways resulting in the breakdown of collagen in the extracellular matrix,
usually carried out by proteases secreted by nearby cells" (QuickGO, retrieved
2026-11-24), which locates the substrate in the ECM. RETREG1's cargo is misfolded
procollagen that never leaves the ER lumen, so substrate and compartment are both
wrong, and RETREG1 performs no proteolysis.

Re-reading the comparator set with the definition in hand makes it consistent
with the definition rather than evidence against it: of 88 human GO:0030574 rows
(QuickGO, taxon 9606, retrieved 2026-11-24) every one is a protease
(MMP1-MMP28, CTSB/CTSK/CTSL/CTSS, PLG, PRSS2, FAP, ADAMTS3, FURIN, TMPRSS6,
KLK6), a regulator of one (CST3), or an endocytic receptor for *extracellular*
collagen (ITGB1 IDA PMID:10455171, MRC2/Endo180 IDA PMID:12972549). The two
receptors handle collagen that originated in the matrix, so they are
definition-compatible and are not a precedent for an ER-luminal client.

The MGI receipt is real — MGI annotates mouse Retreg1 (Q8VE91) to GO:0030574
(IMP, `acts_upstream_of_or_within`, PMID:34338405, assigned_by MGI, 2021-12-08;
QuickGO, retrieved 2026-11-24) — but the hedged qualifier hedges the
participation, not the compartment or the substrate, so it does not resolve the
mismatch. There is no other collagen catabolism term: QuickGO's ontology search
for "collagen catabolic" returns only GO:0030574 and its three regulation
children. The review therefore records the claim as a `proposed_new_terms` entry
("procollagen quality control by reticulophagy", parent GO:0061709) rather than
as an annotation to a term whose definition excludes it. UniProt carries the role
for human only by similarity ("Required for collagen quality control in a LIR
motif-dependent manner (By similarity)"), and human GOA has no annotation from
PMID:30559329 at all, so this is an unannotated claim rather than a curator
decline.

### Redundancy with the other ER-phagy receptors

RETREG1 is one of several receptors and is not individually rate-limiting in
every cell type [PMID:31006538 "ER-phagy is profoundly blocked by deletion of
TEX264 alone and almost completely by additional deletion of FAM134B and CCPG1"].
This matters for reading knockdown phenotypes: a modest ER-phagy defect in
RETREG1-null cells is expected.

### Neuronal survival and the HSAN2B phenotype

The disease was mapped first [PMID:19838196 "loss-of-function mutations in
FAM134B, encoding a newly identified cis-Golgi protein, cause HSAN II"], with the
cellular readout being neuronal death, not a defect in nociceptive signalling
[PMID:19838196 "Fam134b knockdown results in structural alterations of the
cis-Golgi compartment and induces apoptosis in some primary dorsal root ganglion
neurons. This implicates FAM134B as critical in long-term survival of
nociceptive and autonomic ganglion neurons."]. Mouse knockout reproduces it
[PMID:26040720 "disruption of Fam134b in mice causes expansion of the ER,
inhibits ER turnover, sensitizes cells to stress-induced apoptotic cell death and
leads to degeneration of sensory neurons"].

This is why the GOA row `GO:0019233 sensory perception of pain` (IMP,
PMID:19838196) is treated here as an over-annotation: impaired nociception in
HSAN2B patients is the organism-level consequence of losing nociceptive neurons.
RETREG1 does no part of the work of perceiving pain; it keeps the neurons that do
alive. `GO:0043524 negative regulation of neuron apoptotic process` is the real,
if downstream, claim and is kept as non-core.

### The cis-Golgi question

Kurth et al. named FAM134B a cis-Golgi protein, and MGI's mouse GO:0005801
annotation is an IDA from exactly that paper. Every human GOA row for Golgi
(GO:0005794 IEA GO_REF:0000044) and cis-Golgi network (GO:0005801 ISS
GO_REF:0000024, IEA GO_REF:0000107) is transferred from mouse Q8VE91, and
UniProt's own statement is by similarity
[file:human/RETREG1/RETREG1-uniprot.txt "Golgi apparatus, cis-Golgi network
membrane {ECO:0000250|UniProtKB:Q8VE91}"], whereas the ER membrane location is
experimental on the human protein
[file:human/RETREG1/RETREG1-uniprot.txt "Endoplasmic reticulum membrane
{ECO:0000269|PubMed:26040720}"]. Everything published since 2015 treats the
protein as ER-resident, including the topology mapping in PMID:26040720 (UniProt
TOPO_DOM 1-59 cytoplasmic and 230-497 cytoplasmic are both
`ECO:0000269|PubMed:26040720`) and the family review [PMID:34338405 "FAM134B has
been classified as an intra-membrane ER-resident protein that harbors a reticulon
homology domain (RHD) and a LIR sequence"].

Judgement: the Golgi/cis-Golgi rows are marked over-annotated rather than
removed. There is a real primary IDA behind them in mouse, no later paper has
explicitly tested and excluded a cis-Golgi pool, and the 2009 immunofluorescence
predates the ER characterisation; "wrong" is more than the evidence supports,
but a by-similarity location that no subsequent study reproduced should not be
read as a second resident compartment. A co-staining experiment with ER and
cis-Golgi markers on endogenous human RETREG1 would settle it (recorded under
`suggested_experiments`).

The question is also routed upstream rather than left in this file: the
GO:0005794 row carries a `source_defects` entry against UniProt Q9H6L5
(`OUTDATED_STATEMENT`, `requested_change: CHECK`, `confidence: SUSPECTED`) asking
UniProt to re-examine the by-similarity `Golgi apparatus, cis-Golgi network
membrane` location. Mapping that location to GO is the source of the two
UniProt-assigned Golgi rows — GO:0005794 (IEA, `GO_REF:0000044`, from
`UniProtKB-SubCell:SL-0132`) and GO:0005801 (ISS, `GO_REF:0000024`, from
`UniProtKB:Q8VE91`) — but not of the third: the second GO:0005801 row is IEA
from `GO_REF:0000107` and `assigned_by Ensembl`, an Ensembl Compara projection of
the *mouse GO annotation* rather than of this CC line, so a UniProt fix would not
clear it. That row needs the mouse annotation or the projection to change, which
is why one upstream request does not retire the Golgi claim on its own.
`CHECK` at `SUSPECTED` is the right strength: no study has tested and excluded a
human Golgi pool, and the mouse source is a genuine IDA, so this is a request to
look again, not an assertion that the location is false.

### Viral exploitation (context, not a proposed annotation)

RETREG1 is a target of viral manipulation in both directions. SARS-CoV-2 ORF3a
induces RETREG1-dependent reticulophagy [PMID:35239449 "suggesting that
SARS-CoV-2 ORF3a hijacks reticulophagy and then disrupts ER homeostasis to
induce ER stress and inflammatory responses during SARS-CoV-2 infection"], and
dengue virus destroys the receptor
[Reactome:R-HSA-9921595 "DENV protease NS2B:NS3 (NS2B3) cleaves Reticulophagy
regulator 1 (RETREG1, FAM134B), inhibiting its oligomerization and blocking the
formation of ER and DENV protein-enriched autophagosomes."]. In both, RETREG1 is
the entity acted upon, so no viral-process term is proposed for it; the
SARS-CoV-2 paper is used only for the ER/ER-membrane localisation it
establishes.

### Isoforms

Two isoforms. Isoform 2 (Q9H6L5-2) lacks residues 1-141 (VSP_025685) and replaces
142-152 with `MPEGEDFGPGK` (VSP_025686). The deletion removes the first *three*
transmembrane helices (60-80, 96-116, 119-139) and with them most of the RHD,
leaving only TM4 (209-229); the substitution additionally removes the CAMK2B
phosphoacceptor Ser-151 and the neighbouring Ser-149, while Ser-153 falls just
outside the replaced segment and is retained. So isoform 2 is predicted to lack
both the membrane-bending hairpin and (two thirds of) the phospho-switch that
tunes it, while keeping the C-terminal LIR. No GOA row is isoform-specific and no
paper assays isoform 2's receptor activity separately, so nothing is asserted
about it here; this is recorded as a question.

## Per-row decisions (GOA, 28 rows)

| Term | Evidence | Action |
|---|---|---|
| GO:0140506 ER-autophagosome adaptor activity | IEA (Ensembl, mouse) | ACCEPT (core MF) |
| GO:0061709 reticulophagy | IBA, IEA, IMP ×3 | ACCEPT (core BP) |
| GO:0005789 ER membrane | IBA, IDA, IEA, EXP, TAS | ACCEPT (core location) |
| GO:0005783 endoplasmic reticulum | IDA ×2, IEA | ACCEPT (root organelle, informative) |
| GO:0005515 protein binding ×6 | IPI (all ATG8-family partners) | MODIFY → GO:0140506 |
| GO:0043524 neg. reg. neuron apoptotic process | IBA, IEA, IMP | KEEP_AS_NON_CORE |
| GO:0019233 sensory perception of pain | IMP | MARK_AS_OVER_ANNOTATED |
| GO:0005794 Golgi apparatus | IEA | MARK_AS_OVER_ANNOTATED |
| GO:0005801 cis-Golgi network | ISS, IEA | MARK_AS_OVER_ANNOTATED |
| GO:0061753 (obsolete) substrate localization to autophagosome | IEA | REMOVE (obsolete) |

Proposed `NEW`: GO:0180020 membrane bending activity (MF), GO:0090158
endoplasmic reticulum membrane organization (BP). The procollagen-cargo claim is
recorded as a `proposed_new_terms` entry instead of a `NEW` row, because
GO:0030574 is defined over extracellular-matrix collagen (see "Procollagen
quality control" above).

`just validate human RETREG1` passes with one warning: REMOVE on GO:0061753
while GO:0140506 is accepted, because GO:0061753 is still an ancestor of
GO:0140506 in the GO release used for validation. This is the case
`docs/action_consistency.md` names explicitly as an accepted judgement case
("rows on GO:0061753, which GOA's ontology now marks obsolete but the local GO
release used for validation does not"), so no `consistency_exception` was added
and the action was not softened to keep an obsolete term.

## IBA reading

All three IBA rows sit on PANTHER node PTN002823632 and list
`UniProtKB:Q9H6L5` among their `WITH/FROM` sources. Two of them — GO:0043524 and
GO:0061709 — also list `MGI:MGI:1913520` (mouse Fam134b); the GO:0005789 row's
`WITH/FROM` is `PANTHER:PTN002823632|UniProtKB:Q9H6L5` only. Per
`projects/IBA_REVIEW.md` the target's own appearance in its
`WITH/FROM` is the marker that the IBD node was seeded partly by experimental
evidence on this very gene, not circularity: human RETREG1 has IMP reticulophagy
(PMID:26040720, PMID:31930741) and mouse Fam134b has IDA/IMP reticulophagy
(PMID:34338405), which are exactly the descendant evidences a PAINT curator would
use. The node placement is sound for reticulophagy and ER membrane; for
GO:0043524 it propagates the mouse/human neuronal-survival phenotype, which is
true but peripheral, hence non-core rather than accepted.

## Open questions

- Does isoform 2, which lacks most of the RHD but keeps the LIR, retain receptor
  activity, and does it act as a dominant-negative or LIR-only tether?
- Is there a genuine cis-Golgi pool of endogenous human RETREG1, or was the 2009
  assignment a fixation/marker artefact?
- What dephosphorylates Ser-149/151/153 to switch the RHD back off after ER
  stress resolves?
- How is the choice between RETREG1, TEX264, CCPG1, SEC62, RTN3 and ATL3 made
  for a given ER subdomain or cargo?

## Session log: 2026-11-24, PR review follow-up

Addressing the three requested changes on PR #6703, plus the optional
suggestions. Network was reachable in this session (it was not in the review
job), so the GO term definition and the MGI and comparator rows could be queried
directly rather than taken on trust.

1. **GO:0090158 re-anchored.** Was IMP on PMID:34338405, whose ER-morphology
   experiments turn out to be mouse single-knockout MEFs that cite Khaminets 2015
   for Fam134b specifically. Now IMP on PMID:26040720 (the human knockdown), with
   PMID:34338405 kept as corroboration and labelled as such, and PMID:31930741
   added as the receipt for the RHD membrane-fragmentation participation argument
   that `reason` makes. The LIR-dependence objection is answered in `reason`, and
   GO:0090158 is now attached to **both** core functions rather than to the
   membrane-bending one alone, since the scission and the commitment-to-degradation
   steps both remove membrane from the network.
2. **PMID:30559329 reference review corrected.** It is not abstract-only: the
   cache has the full text (689 lines). The full text also separates the species,
   which the abstract does not — see "Procollagen quality control" above. Added a
   finding recording the split and the MEF-rescue-with-human-protein result.
3. **GO:0030574 withdrawn, not merely documented.** The receipts the reviewer
   asked for were retrieved, and they settle the row against itself. The MGI row
   is real (mouse Retreg1 Q8VE91, IMP, `acts_upstream_of_or_within`,
   PMID:34338405, 2021-12-08) but the term definition is explicitly
   extracellular-matrix-scoped, and the human comparator set is consistent with
   that scope rather than against it — ITGB1 and MRC2 internalise collagen that
   originated in the matrix, which is not a precedent for an ER-luminal client.
   The `NEW` row has therefore been removed and replaced with a
   `proposed_new_terms` entry, and GO:0030574 dropped from
   `core_functions[0].directly_involved_in`. This is a change of substance beyond
   what the review asked for, so it is spelled out here and in the PR discussion.

Optional suggestions: isoform-2 TM count fixed (three helices lost, not two, plus
loss of Ser-149/Ser-151 — note Ser-153 is retained, just outside VSP_025686);
the three UniProt quotes now carry `record_section` (`backfill-record-sections`
leaves them alone because the quote matches two separate `SUBCELLULAR LOCATION`
blocks, but both are the same section type, so the value was set by hand and the
tool reports no mismatch); the IBA `WITH/FROM` overstatement corrected above; a
`source_defects` `CHECK` added against the UniProt by-similarity Golgi location.
`PMID:19838196` is left at `correctness: VERIFIED`: the existing `review_notes`
already reasons about `DISPUTED` explicitly and the reviewer called it defensible
either way, so it was not re-litigated.
