# GPR25 review notes

Gene: human GPR25 (UniProt O00155), class A GPCR, 360 aa, chr 1q32.1.
Reviewed as part of a contested-function batch (see also GPR158, GPR75). Within that
batch GPR25 is the positive control: the deorphanization here is far stronger than for
either of the other two.

## What was orphan until 2024

GPR25 was cloned in 1997 by PCR with somatostatin-receptor primers:
[PMID:9020062 "isolation of a gene, GPR25, encoding an additional member of the G
protein-coupled receptor family (GPCR)"], and had essentially no function attached for
27 years.

## The deorphanization — three labs, three assay systems

**1. Ocón et al., Nature 2024 (Butcher lab, Stanford).**
[PMID:39293486 "Here we leveraged diverse omics datasets to identify GPR25 as a
lymphocyte receptor for CXCL17"], with in vivo homing:
[PMID:39293486 "GPR25 characterizes B and T tissue resident memory cells and regulatory
T lymphocytes in non-intestinal mucosal tissues and lungs in humans and mediates
lymphocyte homing to barrier epithelia of the airways, oral cavity, stomach, and biliary
and genitourinary tracts in mouse models."]
The decisive adoptive-transfer experiment:
[PMID:39293486 "To ask whether GPR25 mediates homing from blood into NIMT, we examined
in vivo localization of Gpr25- and co-injected control vector-transduced T cells"], with
the result
[PMID:39293486 "In WT recipients, GPR25 enhanced homing to trachea, stomach, tongue,
gallbladder and uterine mucosae, but not to the intestines or control peripheral lymph
nodes (PLNs) or spleen"] — and this was assayed in Cxcl17-null as well as wild-type
recipients, tying the homing to the ligand.

**2. Hu et al., FEBS J 2025 (Guo lab, Tongji).**
[PMID:40279398 "we identified the rarely studied orphan G protein-coupled receptor 25
(GPR25) as a receptor of CXCL17"], with structure-guided mutagenesis:
[PMID:40279398 "Alanine replacement of W95 or R178 of human GPR25, two conserved
residues in the predicted orthosteric ligand binding pocket, almost abolished its
response to CXCL17."] and a matched-pair specificity test
[PMID:40279398 "Only the pairing of wild-type CXCL17 with wild-type GPR25 could cause
shedding of transforming growth factor α and induce chemotactic movement of transfected
HEK293T cells."]

**3. Yang, Giblin & Pease, Basic Clin Pharmacol Toxicol 2026 (Imperial College).**
A third, fully independent laboratory:
[PMID:42207165 "GPR25 was expressed in the murine pre-B cell line L1.2 and mediated
robust migration of transfectants to nanomolar concentrations of recombinant CXCL17
(24-119)."] concluding
[PMID:42207165 "In conclusion, we verify GPR25 as a bona fide CXCL17 receptor and suggest
a two-step model of GPR25 activation"]. Note that this group independently recovered the
same W95 and R178 residues (plus R264) as essential.

**4. Independent in vivo genetics.**
[PMID:41270189 "Here, we identify the G protein-coupled receptor GPR25, induced by TGF-β
signaling, as a regulator of TRM cell formation."] with
[PMID:41270189 "Using adoptive transfer, we found that Gpr25-deficient T cells
infiltrated tissues normally after viral infection but failed to efficiently develop into
TRM cells."]
This is a fourth lab (La Jolla Institute) and, importantly, a *non-chemotaxis* phenotype
that converges on the same tissue-residency biology.

## The residual controversy is about CXCL17, not about GPR25

[PMID:41167449 "C-X-C motif chemokine ligand 17 (CXCL17) is a chemoattractant whose
receptor remains controversial."] — the same Tongji group reports that CXCL17 also
activates MRGPRX1, MRGPRX2 and MAS1. But the mechanistic dissection points the other way
from what that sentence suggests:
[PMID:41167449 "However, removal of C-terminal residues from CXCL17 did not affect its
activation of these three MRGPRs, even though this region is essential for GPR25
activation."]

In other words, the MRGPR responses require micromolar CXCL17 and a *different*
structural determinant, whereas the GPR25 response is nanomolar-to-~100 nM, requires the
conserved C-terminal fragment, and maps to a defined orthosteric pocket. A promiscuous
ligand does not make one of its receptors wrong. The direction of residual doubt is
"which receptor carries CXCL17's physiological signal in which tissue", not "is GPR25 a
CXCL17 receptor".

There is also a live taxonomic argument about CXCL17 itself — the Imperial group
"advocate the reclassification of CXCL17 as a chemoattractant distinct from the chemokine
family" (PMID:42207165). That is a question about the ligand's nomenclature; it does not
disturb `GO:0016494`, whose scope is C-X-C-named chemokine ligands, and CXCL17 is one.

## A mis-scoped GO term found in review

`GO:0097021` **lymphocyte migration into lymphoid organs** is annotated twice with IDA
(PMID:39293486, PMID:40279398). Its definition is "The movement of a lymphocyte within
the lymphatic system into lymphoid organs such as lymph nodes, spleen or Peyer's
patches...". The full text of PMID:39293486 states the opposite for GPR25: homing was
enhanced to mucosal barrier tissues "but not to the intestines or control peripheral
lymph nodes (PLNs) or spleen". This is a term-scoping error, not a gene error — the
underlying biology (lymphocyte migration to peripheral tissue) is right. Action:
**MODIFY** both rows to `GO:0072676` lymphocyte migration, which is true and does not
assert lymphoid-organ entry. A mucosal-homing child term would be better still and is
raised in `suggested_questions`.

## Curation position taken

- `GO:0016494` C-X-C chemokine receptor activity (IDA ×2) → **ACCEPT, core**. This is
  about as well-replicated as a 2024-2026 deorphanization gets: three labs, three assay
  platforms, converging site-directed mutagenesis, plus in vivo genetics in two labs.
- `GO:0070098` chemokine-mediated signaling pathway (IDA ×2) → **ACCEPT, core**.
- `GO:0048247` lymphocyte chemotaxis (IDA ×2) → **ACCEPT, core**.
- `GO:0030595` leukocyte chemotaxis (IDA) → **ACCEPT** (correct parent of the above).
- `GO:0097021` lymphocyte migration into lymphoid organs (IDA ×2) → **MODIFY** to
  `GO:0072676`, see above.
- `GO:0004930` GPCR activity (IBA, IEA, IDA ×2, TAS) → **ACCEPT**. Correct, now subsumed
  by the ligand-specific child, and the IBA is a sound family-level statement.
- `GO:0007186`, `GO:0005886`, `GO:0016020` → **ACCEPT**.
- `GO:0005515` protein binding (IPI ×20, from three interactome screens and one
  GPCR-RAMP mapping) → **MARK_AS_OVER_ANNOTATED** per project guidance; bare protein
  binding carries no functional information. Most partners are unrelated membrane
  proteins recovered in Y2H-style binary screens.

## Unresolved

- Is CXCL17 the *only* endogenous GPR25 agonist, and does GPR25 have additional ligands?
- Does CXCL17 signal through MRGPRX1/X2/MAS1 at physiological concentrations, or are
  those micromolar responses in vitro artefacts of a cationic peptide?
- GPR25's TGF-β-induced role in TRM formation (PMID:41270189) is phenotypically distinct
  from chemotaxis; whether it is downstream of CXCL17 binding or a separate output is
  not established.
