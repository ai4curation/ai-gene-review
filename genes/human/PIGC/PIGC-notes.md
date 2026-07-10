# PIGC (Q92535) review notes

Human PIGC / phosphatidylinositol N-acetylglucosaminyltransferase subunit C (HGNC:8960; synonym GPI2).
297 aa, multi-pass ER membrane protein (8 predicted TM helices per UniProt FT).

## Core biology
PIGC is a required, **non-catalytic accessory subunit** of the GPI-GlcNAc transferase
(GPI-GnT) complex, which catalyses the **first committed step of GPI-anchor biosynthesis**:
transfer of GlcNAc from UDP-GlcNAc onto phosphatidylinositol (PI) to give GlcNAc-PI, in the
ER membrane. PIGA is the catalytic subunit; the complex also contains PIGH, PIGP, PIGQ (GPI1),
PIGY and DPM2.

- [PMID:8806613 "The first step of the biosynthesis, the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to phosphatidylinositol, is mediated by at least three genes in mammalian cells (PIG-A, PIG-H and PIG-C)"] — cloning of PIG-C as a human homologue of yeast GPI2; "PIG-C protein is a 297 amino-acid membrane protein in the endoplasmic reticulum".
- [PMID:9463366 "four mammalian gene products form a protein complex in the endoplasmic reticulum membrane. ... The protein complex had GPI-GlcNAc transferase (GPI-GnT) activity in vitro"] — PIG-A, PIG-H, PIG-C and GPI1 (PIGQ) form the ER-membrane complex with GPI-GnT activity. IntAct IPI here is PIGC–PIGQ (Q9BRB3).
- [PMID:10944123 "GPI-GnT ... consisting of at least four proteins, PIG-A, PIG-H, PIG-C and GPI1 ... DPM2 ... associates with GPI-GnT through interactions with PIG-A, PIG-C and GPI1"] — adds PIG-P and DPM2. IntAct IPI here is PIGC–DPM2 (O94777).
- [PMID:16162815 "human GPI-GnT requires another component, termed PIG-Y ... A complex of six components was formed without PIG-Y ... PIG-A ... the catalytic subunit PIG-A"] — seventh component PIG-Y; explicitly names PIG-A as the catalytic subunit (so PIGC is accessory, not catalytic).

## Molecular function in GOA
GOA carries only **GO:0005515 protein binding** (IPI, IntAct, x2: DPM2 and PIGQ) and a legacy
**GO:0003824 catalytic activity** (TAS, ProtInc, from PMID:8806613, dated 2003). There is NO
specific glycosyltransferase MF term for PIGC in the GOA. Given PIGA is the catalytic subunit
and PIGC is an accessory/structural subunit, the broad "catalytic activity" is an
over-annotation for this subunit (the catalytic activity belongs to the complex/PIGA). Per
project policy I do not invent a catalytic MF; core_functions omits `function` and records the
BP + location + complex membership.

## Localization
ER membrane, multi-pass. [PMID:8806613 "membrane protein in the endoplasmic reticulum"];
UniProt SUBCELLULAR LOCATION "Endoplasmic reticulum membrane ... Multi-pass membrane protein".

## Disease
Autosomal recessive GPI biosynthesis defect 16 (GPIBD16; MIM 617816): global developmental
delay, intellectual disability, drug-responsive seizures — an inherited GPI-deficiency /
epileptic-encephalopathy phenotype.
- [PMID:27694521 "PIGC joins the list of genes in which mutations result in defective biosynthesis of GPI anchoring, manifesting by global developmental delay and seizure disorder"]; patient variants (L189W; L212P/R21X) reduce surface expression of GPI-anchored proteins (IMP for GPI anchor biosynthetic process).

## Annotation dispositions (summary)
- GPI anchor biosynthetic process (GO:0006506): core BP. Kept across IBA/IEA/IDA/IMP/TAS.
- GPI-GnT complex (GO:0000506): core CC. Kept across IBA/IPI/IDA.
- ER membrane (GO:0005789): core CC. Kept across IEA/IDA/TAS.
- membrane (GO:0016020, IEA InterPro): correct but generic vs ER membrane -> MARK_AS_OVER_ANNOTATED.
- protein binding (GO:0005515, IPI x2): uninformative bare term -> MARK_AS_OVER_ANNOTATED (real content is complex membership, captured by GO:0000506).
- catalytic activity (GO:0003824, TAS): over-annotation for accessory subunit (PIGA is catalytic) -> MARK_AS_OVER_ANNOTATED.
