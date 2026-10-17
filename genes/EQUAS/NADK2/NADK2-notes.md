# NADK2 (donkey, A0A9L0K2P4) notes

## Sources
- Donkey UniProt A0A9L0K2P4 (unreviewed, TrEMBL; Ensembl ENSEASP00005059781.1). All names, EC, subunit and location statements in this record are ARBA-derived (ECO:0000256), i.e. automated predictions, not evidence.
- Human ortholog NADK2 Q4G0N4 (Swiss-Prot), genes/human/NADK2/NADK2-uniprot.txt, and the human review genes/human/NADK2/NADK2-ai-review.yaml.
- Sequence comparison: NADK2-bioinformatics/RESULTS.md (Biopython global alignment).

## Biology (human ortholog, transferred by orthology)
- Human NADK2 is the mitochondrial NAD kinase: [file:human/NADK2/NADK2-uniprot.txt "Mitochondrial NAD(+) kinase that phosphorylates NAD(+) to yield NADP(+)"].
- Activity with ATP and polyphosphate shown on purified protein: [PMID:23212377 "showing that C5orf33 protein has NADK activity using ATP and poly(P) as phosphoryl donors"].
- Mitochondrial localization with a functional N-terminal targeting sequence: [PMID:23212377 "confirming that C5orf33 protein is a mitochondrial NADK, and that its N-terminal 62 residues contain a functional mitochondrial-targeting sequence"].
- NAD kinase is the sole NADP+ biosynthetic enzyme: [PMID:23212377 "NAD kinase is the sole NADP(+) biosynthetic enzyme"].
- Homodimer statement in human UniProt is a curator inference (ECO:0000305) from PMID:23212377; the cached text does not contain a dimerization result.

## Donkey sequence
- 96.59% identity over 410 aligned residues to human; but the donkey model has a 96-aa N-terminal extension and lacks the human 288-319 segment (= human isoform 2 deletion VSP_027193) [file:EQUAS/NADK2/NADK2-bioinformatics/RESULTS.md]. GGDG motif retained.
- Consequence: the gene-level function (mitochondrial NAD kinase) transfers by orthology; the activity of this exact isoform-2-like model, and the use of its internal transit peptide, are unverified.

## Annotation decisions
- NAD+ kinase activity (GO_REF:0000120): ACCEPT (core).
- mitochondrion (GO_REF:0000120), mitochondrial matrix (ARBA GO_REF:0000117): ACCEPT.
- NAD+ metabolic process (TreeGrafter GO_REF:0000118): ACCEPT; added NEW NADP+ biosynthetic process (GO:0006741), the direct product of the catalysed step (the enzyme performs the step; passes the participation test).
