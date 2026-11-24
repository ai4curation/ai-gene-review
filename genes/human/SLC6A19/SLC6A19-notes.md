# SLC6A19 (B0AT1, Q695T7) — curation notes

Batch 10 canonical-surfaceome backfill. Research journal for the GO annotation review.

## Summary of gene function

SLC6A19 encodes B0AT1 (system B0 neutral amino acid transporter 1), the major apical/brush-border
transporter responsible for epithelial (re)absorption of neutral amino acids in the small intestine
and the renal proximal tubule. It is a secondary-active, Na+-coupled, **chloride-independent**
symporter of neutral (aliphatic/branched/aromatic) L-amino acids. This is the defining mechanistic
distinction from the Cl--dependent SLC6 neurotransmitter symporters (GAT1, SERT, DAT, GlyT, etc.):
B0AT1 couples uptake to the inward Na+ gradient only, with no Cl- cotransport.

- [PMID:15286788 "SLC6A19 is a sodium-dependent and chloride-independent neutral amino acid transporter, expressed predominately in kidney and intestine, with properties of system B(0)."]
- [PMID:15286787 "results from impaired transport of neutral amino acids across epithelial cells in renal proximal tubules and intestinal mucosa"]
- [PMID:26240152 "B 0 AT1 (SLC6A19) catalyzes the secondary active transport of neutral amino acids across the apical membrane in the small intestine and kidney"]

Loss-of-function mutations in SLC6A19 cause **Hartnup disorder** (autosomal recessive neutral
hyperaminoaciduria; OMIM 234500), and SLC6A19 deficiency also contributes to hyperglycinuria and
iminoglycinuria in combination with other transporter deficiencies (UniProt DISEASE sections).

## Substrates (from UniProt CATALYTIC ACTIVITY / Rhea; all Na+-coupled, no chloride)

L-alanine (CHEBI:57972), L-cysteine (CHEBI:35235), L-glutamine (CHEBI:58359), glycine (CHEBI:57305),
L-isoleucine (CHEBI:58045), L-leucine (CHEBI:57427), L-methionine (CHEBI:57844),
L-phenylalanine (CHEBI:58095), L-serine (CHEBI:33384), L-tryptophan (CHEBI:57912),
L-tyrosine (CHEBI:58315), L-valine (CHEBI:57762); co-substrate Na+ (CHEBI:29101). No Cl-.

Verified the ChEBI ids supplied in the task against UniProt Rhea reactions: L-leucine CHEBI:57427,
L-isoleucine CHEBI:58045, L-valine CHEBI:57762, L-methionine CHEBI:57844, L-phenylalanine CHEBI:58095,
Na+ CHEBI:29101 — all match the UniProt record exactly.

## ACE2 / collectrin (CLTRN) accessory-subunit partnership — modeling decision

B0AT1 is **not** an SLC3-type heavy-chain/light-chain heteromeric amino acid transporter (that is the
SLC7 system, disulfide-linked to 4F2hc/rBAT). Instead B0AT1 requires a tissue-specific single-pass
**accessory/chaperone subunit** for surface trafficking and catalytic activation:
- **ACE2** in the small intestine
- **collectrin (CLTRN / TMEM27)** in the kidney

This is a genuine, obligate functional partnership, not a bystander co-purification:

- [PMID:26240152 "require the ancillary protein collectrin or ACE2 for plasma membrane expression"]
- [PMID:26240152 "Both transporters require collectrin or angiotensin-converting enzyme 2 (ACE2) as an essential subunit for trafficking to the plasma membrane in all in vitro and in vivo expression systems tested to date"]
- [PMID:26240152 "collectrin is also necessary for B 0 AT1 and B 0 AT3 catalytic function"]
- [PMID:19185582 "B0AT1 requires association with collectrin for luminal surface expression in the kidney proximal tubule, whereas collectrin is nearly absent in the small intestine"]
- [PMID:18424768 "Addition of a peptide containing a carboxyterminal leucine residue to ACE2- and B(0)AT1-coexpressing oocytes caused inward currents due to Na(+)-leucine cotransport, demonstrating the formation of a metabolic complex."]

UniProt SUBUNIT also records a positive regulatory interaction with ANPEP (aminopeptidase N) in
intestine. The cryo-EM B0AT1–ACE2 complex (PMID:32132184; PDB 6M17/6M18/6M1D and many later entries)
is also the structural context in which the SARS-CoV-2 spike/ACE2 interaction was solved.

**Modeling choice.** The partnership is captured as complex membership, not bare protein binding.
- The existing `GO:1902495 transmembrane transporter complex` (part_of, IDA/NAS) rows are ACCEPTed.
- A more specific `GO:1990184 amino acid transport complex` (part_of) is added as a NEW row and used in
  `core_functions.in_complex`. OLS confirms GO:1990184 is a protein-containing / plasma-membrane protein
  complex term (is_a GO:0098797 plasma membrane protein complex), fitting the B0AT1–ACE2/collectrin
  heteromeric amino acid transporter complex (ComplexPortal CPX-8191, CPX-8192). GO:1990184 is NOT an
  ancestor or descendant of GO:1902495, so the two are complementary, not redundant.
- The three bare `GO:0005515 protein binding` rows (all ACE2, UniProtKB:Q9BYF1) are REMOVED per the
  protein-binding policy: bare binding is uninformative, and the functionally meaningful ACE2/collectrin
  relationship is already captured by the complex-membership annotations above. Removal does not imply
  the interaction is false.

## Core molecular function (exact GO id)

Core MF = **GO:0005295 neutral L-amino acid:sodium symporter activity** (verified via OLS; Na-coupled,
neutral, chloride-independent). This generalizes the experimentally grounded substrate-specific symporter
terms (GO:0015375 glycine:sodium symporter, GO:0015655 alanine:sodium symporter) and adds the Na-coupling
to the neutral-amino-acid transporter term GO:0015175. The general IEA `GO:0015370 solute:sodium symporter
activity` (ARBA) is MODIFYed to GO:0005295 (OLS confirms GO:0005295 is_a GO:0015370 via GO:0005283).
`GO:0015175 neutral L-amino acid transmembrane transporter activity` (IDA/IBA/IEA) is ACCEPTed as the
directly-annotated transporter MF; it is a sibling of GO:0005295 under GO:0015171, not an ancestor.

No Cl--coupling MF term is accepted. (Confirmed the symporter terms annotated — GO:0015370, GO:0015375,
GO:0015655 — and the proposed GO:0005295 are all sodium-only; the chloride-dependent siblings such as
GO:0140931 neutral L-amino acid:sodium:chloride symporter activity are NOT used.)

## Locations

- GO:0005886 plasma membrane — ACCEPT (core; direct EXP, PMID:19185582, PMID:26240152).
- GO:0016324 apical plasma membrane — ACCEPT (IDA PMID:18424768; physiologically central — epithelial apical).
- GO:0031526 brush border membrane — ACCEPT (IBA; IDA PMID:25534429; the functional resorptive surface).
- GO:0016020 membrane (IEA, InterPro) — MODIFY → GO:0005886 plasma membrane (membrane is uninformatively general).
- GO:0070062 extracellular exosome (HDA, PMID:19056867 urinary-exosome proteomics) — KEEP_AS_NON_CORE
  (detection in shed urinary exosomes is consistent with a renal apical membrane protein; peripheral to function).

## Participation-test calls for process terms

- GO:0089718 amino acid import across plasma membrane (IDA x2) — ACCEPT, core. B0AT1 performs the import step.
- GO:0015804 neutral amino acid transport (IBA) — ACCEPT, core.
- GO:0035725 sodium ion transmembrane transport (IBA) — ACCEPT. Na+ is co-transported in every symport cycle; B0AT1 moves Na+ across the membrane as part of the coupled mechanism.
- GO:0015816 glycine transport / GO:0032328 alanine transport (IEA inter-ontology from the EXP symporter terms) — ACCEPT; glycine and alanine are experimentally confirmed substrates.
- GO:0006865 amino acid transport (TAS) — TOO_GENERAL; entailed by the ACCEPTed GO:0015804 neutral amino acid transport (neutral amino acid transport is_a amino acid transport).
- GO:0015171 amino acid transmembrane transporter activity (TAS x2) — TOO_GENERAL; entailed by the ACCEPTed GO:0015175 (is_a parent).
- GO:0006836 neurotransmitter transport (TAS, Reactome pathway grouping) — MARK_AS_OVER_ANNOTATED. B0AT1 is an epithelial amino-acid resorption transporter, not a synaptic neurotransmitter transporter, and UniProt records it is "Not detected in testis, whole brain, cerebellum". The annotation arises from the SLC6 family name (sodium:neurotransmitter symporter family) and the Reactome neurotransmitter-transport pathway, not from a neurotransmitter-transport function of this gene.
- GO:0007584 response to nutrient (IEA from rat ortholog, Ensembl) — MARK_AS_OVER_ANNOTATED; an indirect/regulatory over-propagation, not a step B0AT1 performs.
- GO:0019058 viral life cycle (NAS, PMID:33737693 SARS-CoV-2 spike/ACE2) — MARK_AS_OVER_ANNOTATED.
  Participation test fails: ACE2 is the SARS-CoV-2 receptor; B0AT1 is an accessory subunit co-purified in
  the ACE2 complex used for the cryo-EM structures, and executes no step of the viral life cycle.
  Comparator: the viral-entry receptor role sits on ACE2, not on its transporter cargo.

## proposed_new_terms / source_defects

- No proposed_new_terms required: GO:0005295 and GO:1990184 already exist and are used (NEW row / MODIFY / core).
- No source_defects identified. The GOA rows are internally consistent with UniProt; the over-annotations
  (neurotransmitter transport, viral life cycle, response to nutrient) are handled with
  MARK_AS_OVER_ANNOTATED rather than as source defects, since they reflect pathway/family-level
  propagation rather than a mis-keyed record.
