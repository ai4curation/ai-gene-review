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
is a multi-pass ER membrane protein whose four transmembrane helices form a
reticulon-homology domain (RHD, residues 84-233 in UniProt's annotation) with a
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
organization (IMP, PMID:34338405); human RETREG1 carries no ER-organisation term
in GOA. GO:0090158 (endoplasmic reticulum membrane organization), the child that
the comparable ER-shaping proteins carry (ARL6IP1 IDA, ATL3 IDA/IMP, RTN1/2/3
IBA, REEP5 ISS, per QuickGO), is the better fit for a bilayer-deforming RHD
protein and is proposed here as a `NEW` row.

### Procollagen quality control

Misfolded procollagen is a defined RETREG1 cargo, shown in human
collagen-producing cells with siRNA and CRISPR-Cas9 [PMID:30559329 "the
ER-resident lectin chaperone Calnexin (CANX) and the ER-phagy receptor FAM134B
are required for autophagy-mediated quality control of endogenous procollagens";
PMID:30559329 "FAM134B binds the autophagosome membrane-associated protein LC3
and delivers a portion of ER containing both CANX and procollagen to the
lysosome for degradation"]. CANX acts as the luminal co-receptor that reads the
misfolded client and hands it to RETREG1. The paralogue study used the same
cargo [PMID:34338405 "Utilizing pro-Collagen I, as a shared ER-phagy substrate,
we observe that FAM134A acts in a LIR-independent manner and compensates for the
loss of FAM134B and FAM134C"].

UniProt carries this for human only by similarity ("Required for collagen
quality control in a LIR motif-dependent manner (By similarity)"), and human
GOA has no annotation from PMID:30559329 at all, while MGI annotates mouse
Q8VE91 to GO:0030574 collagen catabolic process (IMP, PMID:34338405). The
comparator check for GO:0030574 in human returns mostly proteases (MMPs,
cathepsins, PLG, FURIN) **plus ITGB1 by IDA**, i.e. a receptor that delivers
collagen for lysosomal degradation rather than cleaving it — the same role shape
as RETREG1. So this looks like an uncurated paper rather than a deliberate
curator decline, and GO:0030574 is proposed here as a `NEW` row.

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

Two isoforms. Isoform 2 (Q9H6L5-2) lacks residues 1-141 and replaces 142-152, so
it loses the first two transmembrane helices and most of the RHD while keeping
the C-terminal LIR. No GOA row is isoform-specific and no paper assays
isoform 2's receptor activity separately, so nothing is asserted about it here;
this is recorded as a question.

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
endoplasmic reticulum membrane organization (BP), GO:0030574 collagen catabolic
process (BP).

`just validate human RETREG1` passes with one warning: REMOVE on GO:0061753
while GO:0140506 is accepted, because GO:0061753 is still an ancestor of
GO:0140506 in the GO release used for validation. This is the case
`docs/action_consistency.md` names explicitly as an accepted judgement case
("rows on GO:0061753, which GOA's ontology now marks obsolete but the local GO
release used for validation does not"), so no `consistency_exception` was added
and the action was not softened to keep an obsolete term.

## IBA reading

All three IBA rows sit on PANTHER node PTN002823632 and list
`UniProtKB:Q9H6L5` among their `WITH/FROM` sources alongside `MGI:MGI:1913520`
(mouse Fam134b). Per `projects/IBA_REVIEW.md` the target's own appearance in its
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
