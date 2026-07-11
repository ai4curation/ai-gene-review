# CYP17A1 (P450c17) review notes

UniProtKB: P05093 (CP17A_HUMAN). HGNC:2593. Human, NCBITaxon:9606.
Name: Steroid 17-alpha-hydroxylase/17,20 lyase; Cytochrome P450c17; Cytochrome P450 17A1.
EC 1.14.14.19 (17alpha-hydroxylase) and EC 1.14.14.32 (17,20-lyase / 17-alpha-hydroxyprogesterone aldolase).

## Core biology (grounded in UniProt P05093 + cached literature)

CYP17A1 is a **microsomal (ER-membrane) heme-thiolate cytochrome P450 monooxygenase** that
sits at the **branch point of steroidogenesis**, determining whether pregnane precursors are
routed toward glucocorticoids (cortisol) or toward androgens/estrogens. It is a **single,
bifunctional enzyme** carrying two catalytic activities on one polypeptide:

1. **17-alpha-hydroxylase (EC 1.14.14.19):** hydroxylates C21 steroids —
   pregnenolone -> 17alpha-hydroxypregnenolone, progesterone -> 17alpha-hydroxyprogesterone.
   These 17-OH intermediates are precursors of cortisol (adrenal glucocorticoid pathway).
   [PMID:9452426 "P450c17 is the single enzyme that catalyzes both the 17alpha-hydroxylation of 21-carbon steroids and the 17,20-lyase activity that cleaves the C17-C20 bond to produce C19 sex steroids"]

2. **17,20-lyase (EC 1.14.14.32):** cleaves the C17-C20 bond of the 17-OH intermediates ->
   DHEA (from 17OH-pregnenolone) and androstenedione (from 17OH-progesterone), the committed
   step toward androgens/estrogens.
   [PMID:9452426 "the 17,20-lyase activity that cleaves the C17-C20 bond to produce C19 sex steroids"]

The lyase reaction is **cytochrome b5- and POR-dependent**: cytochrome b5 acts as an
allosteric effector that raises the Vmax of the lyase (not the hydroxylase) reaction, without
direct electron transfer. [PMID:9452426 "coexpression of human b5 with P450c17 also increases the Vmax of the 17,20-lyase reactions but not of the 17alpha-hydroxylase reactions"]
[file quote P05093 "The 17,20-lyase activity is stimulated by cytochrome b5, which acts as an allosteric effector increasing the Vmax of the lyase activity"]

Mechanism: monooxygenase using molecular O2, one atom inserted into substrate, second reduced
to water; two electrons from NADPH via cytochrome P450 reductase (POR).
[file quote P05093 "two electrons provided by NADPH via cytochrome P450 reductase"]

Minor/additional activities (UniProt): 16-alpha-hydroxylase activity relevant to estriol
synthesis (PMID:25301938, PMID:27339894); mouse ortholog characterized similarly (PMID:36640554).

## Localization

ER membrane / microsome membrane. [file quote P05093 "Endoplasmic reticulum membrane"]
NAS/TAS legacy annotations (GO:0005783 endoplasmic reticulum; GO:0005789 ER membrane) all
consistent. UniProt SUBCELLULAR LOCATION cites PubMed:2808364.

## Disease

Combined 17alpha-hydroxylase/17,20-lyase deficiency = Adrenal hyperplasia 5 (AH5, MIM:202110),
a form of congenital adrenal hyperplasia: hypertension + sexual-development defects.
[PMID:24140098 "characterized by hypertension and sexual infantilism and caused by loss-of-function mutations in CYP17A1"]
Isolated 17,20-lyase deficiency also occurs (46,XY DSD); true isolated lyase deficiency can
also be caused by CYB5A mutation. [PMID:9326943; PMID:22170710]

## Structure

Multiple X-ray structures (DeVore & Scott 2012 PMID:22266943 with abiraterone/TOK-001;
Petrunak 2014 PMID:25301938 with substrates). Heme-iron axial Cys442; substrate binding
via Asn202. Abiraterone (prostate cancer drug) is a CYP17A1 inhibitor.

## Curation decisions summary

Core MF: GO:0004508 steroid 17-alpha-monooxygenase activity (no dedicated 17,20-lyase MF term
exists in GO; GO:0004508 is the canonical CYP17A1 MF, well supported by IDA/EXP/IMP + IBA).
Core BP: androgen biosynthesis (GO:0006702), glucocorticoid/cortisol biosynthesis
(GO:0006704 / GO:0034651). Core CC: GO:0005789 ER membrane. Secondary MF: heme binding
(GO:0020037), iron ion binding (GO:0005506).

Over-annotated / generic IEA MF terms (monooxygenase, steroid hydroxylase, oxidoreductase
16705/16712) are not wrong but are ancestors of the specific GO:0004508; keep as non-core.
GO:0019825 oxygen binding (legacy TAS from PINC/ProtInc, cited to PMID:2808364 which does not
mention oxygen binding) is an over-annotation for a P450 — mark as over-annotated.
Generic ARBA IEA BP terms (primary alcohol metabolic, olefinic compound metabolic) are
mechanistically-derived over-general terms — keep as non-core / over-annotated.
