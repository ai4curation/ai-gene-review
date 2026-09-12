# CYP21A2 (Steroid 21-hydroxylase, P450c21) — review notes

UniProtKB: P08686 (CP21A_HUMAN); gene CYP21A2 (syn. CYP21, CYP21B); HGNC:2600; EC 1.14.14.16.

## Core biology (from UniProt P08686 + cached publications)

- **Molecular function.** A microsomal (ER-membrane) cytochrome P450 monooxygenase.
  Heme-thiolate enzyme; heme b cofactor with Cys429 as axial (proximal) iron ligand
  (BINDING 92/121/366/427; 429 = "axial binding residue" for Fe). Electrons delivered
  by NADPH via cytochrome P450 reductase (POR/CPR).
- **Reactions (both C21 hydroxylations):**
  - progesterone + NADPH-hemoprotein reductase(red) + O2 -> 21-hydroxyprogesterone
    (= 11-deoxycorticosterone, DOC) + reductase(ox) + H2O + H+  (RHEA:50304; GO:0106309
    progesterone 21-hydroxylase activity) — mineralocorticoid branch.
  - 17alpha-hydroxyprogesterone + reductase(red) + O2 -> 11-deoxycortisol + reductase(ox)
    + H2O + H+  (RHEA:50308; GO:0103069 17-hydroxyprogesterone 21-hydroxylase activity)
    — glucocorticoid branch.
  These two specific MFs are subsumed by GO:0004509 steroid 21-monooxygenase activity
  (EC 1.14.14.16), which is the appropriate CORE MF term the GOA carries.
- **Location.** ER membrane / microsome membrane; **peripheral membrane protein**,
  anchored by the N-terminal leucine-rich hydrophobic segment (spans the membrane through
  its first hydrophobic domain only, per PMID:10198222). GO:0005789 ER membrane.
- **Biological process.** Adrenal steroidogenesis: supplies BOTH the mineralocorticoid
  (aldosterone via DOC) and glucocorticoid (cortisol via 11-deoxycortisol) branches of
  corticosteroid biosynthesis. GO:0006704 glucocorticoid biosynthetic process,
  GO:0006705 mineralocorticoid biosynthetic process, GO:0034651 cortisol biosynthetic
  process.
- **Disease.** Deficiency (AH3, MIM:201910) is the cause of ~95% of congenital adrenal
  hyperplasia (21-hydroxylase deficiency), spectrum salt-wasting -> simple virilizing ->
  non-classic; cortisol/aldosterone deficiency with androgen excess. Deleterious alleles
  arise mostly by gene conversion with the pseudogene CYP21A1P.

## Key supporting quotes (verbatim, verified against cached files)

- UniProt FUNCTION: "Catalyzes the hydroxylation at C-21 of progesterone and
  17alpha-hydroxyprogesterone to respectively form 11-deoxycorticosterone and
  11-deoxycortisol, intermediate metabolites in the biosynthetic pathway of
  mineralocorticoids and glucocorticoids" and "two electrons provided by NADPH via
  cytochrome P450 reductase". [file:human/CYP21A2/CYP21A2-uniprot.txt]
- UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane; Peripheral membrane
  protein ... Microsome membrane". COFACTOR "Name=heme b". [file: uniprot]
- PMID:25855791 (abstract): "Cytochrome P450 (P450) 21A2 is the major steroid
  21-hydroxylase, and deficiency of this enzyme is involved in ∼95% of cases of human
  congenital adrenal hyperplasia". Structure with progesterone; "progesterone, a substrate
  in adrenal 21-hydroxylation."
- PMID:16984992 (abstract): mutations gave "almost absent or negligible CYP21 activity for
  the conversion of 17-hydroxyprogesterone to 11-deoxycortisol and progesterone to
  deoxycorticosterone." Localization not affected by mutants (immunofluorescence).
- PMID:22014889 (abstract): "More than 90% of all cases of congenital adrenal hyperplasia
  (CAH) result from steroid 21-hydroxylase gene (CYP21A2) mutations"; residual activity +
  kinetic values measured for both substrates.
- PMID:27721825 (full text): assayed "enzyme activities towards 17-hydroxyprogesterone and
  progesterone"; "The most common cause of CAH is 21-hydroxylase deficiency (21OHD)".
- PMID:10198222 (abstract): membrane anchoring study; "P450c21 spans the membrane through
  its first hydrophobic domain only"; N-terminal hydrophobic segment for membrane
  integration. Supports ER/microsome membrane peripheral localization (is_active_in).
- PMID:1406709 (abstract): "R339H and P453S: CYP21 mutations associated with nonclassic
  steroid 21-hydroxylase deficiency" — TAS for steroid hydroxylase activity.

## Annotation-review reasoning

- CORE MF = GO:0004509 steroid 21-monooxygenase activity (IBA + IEA/EC + TAS). The two
  Rhea/EXP substrate-specific terms (GO:0106309, GO:0103069) are correct, specific, and
  directly experimentally supported (PMID:16984992/22014889/27721825/25855791) — ACCEPT.
- CORE BP = corticosteroid biosynthesis, split as glucocorticoid (GO:0006704), cortisol
  (GO:0034651), and mineralocorticoid (GO:0006705) biosynthetic processes — all directly
  supported by function; ACCEPT the specific ones.
- Heme binding GO:0020037 (IDA PMID:25855791, IBA) ACCEPT (secondary, structural). Iron
  ion binding GO:0005506 IEA ACCEPT (heme-Fe). Monooxygenase GO:0004497 and oxidoreductase
  GO:0016705 IEA are correct but too general vs GO:0004509 -> MARK_AS_OVER_ANNOTATED.
- Steroid hydroxylase activity GO:0008395 (IMP/TAS) correct but less specific than
  GO:0004509 -> MODIFY to GO:0004509.
- Broad BP IEAs from ARBA: primary alcohol metabolic (GO:0034308), ketone metabolic
  (GO:0042180), olefinic compound metabolic (GO:0120254) — chemistry-generic
  over-annotations from substrate/product chemical class -> MARK_AS_OVER_ANNOTATED.
  Steroid metabolic (GO:0008202 IMP) / steroid biosynthetic (GO:0006694 IDA) / sterol
  metabolic (GO:0016125 TAS) are correct but broad parents of the specific corticosteroid
  terms -> KEEP_AS_NON_CORE.
- ER membrane GO:0005789 (IDA PMID:10198222 is_active_in; IEA; several Reactome TAS) —
  ACCEPT the experimental/IDA as core location; ACCEPT the others.

No falcon deep-research file (provider out of credits, HTTP 402); grounded in UniProt +
GOA + cached PMIDs.
