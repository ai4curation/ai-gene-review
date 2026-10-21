# TGFBR3 (donkey, A0A8C4M6Z6) - review notes

DONKEY40 cohort. 33 IEA GOA rows; most are Ensembl Compara (GO_REF:0000107) transfers of human experimental annotations; 4 TreeGrafter rows.

## Sequence
- [file:EQUAS/TGFBR3/TGFBR3-bioinformatics/RESULTS.md "89.47% identity over 836 paired residues"]; signal peptide, ZP-domain disulfides and TM helix conserved (["TRANSMEM Helical: human [788, 809] MY -> donkey [773, 794] MY"]).

## Function
- [PMID:18184661 "The TGF-beta type III receptor (TbetaRIII or betaglycan) is an abundant cell surface proteoglycan that has been well characterized as a TGF-beta and inhibin receptor."]
- [PMID:18184661 "TbetaRIII directly and specifically binds to multiple members of the BMP subfamily, including BMP-2, BMP-4, BMP-7, and GDF-5"]
- Human UniProt: [file:EQUAS/TGFBR3/TGFBR3-bioinformatics/human-Q03167-uniprot.txt "In gonadotrope cells, acts as an inhibin A coreceptor and regulates follicle-stimulating hormone (FSH) levels and female fertility"]; ["Exists both as a membrane-bound form and as soluble form in serum and in the extracellular matrix."]
- Immune response source: [PMID:16886151 "We found significant associations with SNPs in IGF1R and genes of the TGF-beta /BMP pathway (BMP6, TGFBR3, BMPR1A, SMAD6 and SMAD3)."] - association only.
- ECM assembly / gene expression source: [PMID:30729664 "TGFBR3 siRNA could increase fibrosis-related genes expression, along with the Smad1 inactivation and Smad3 activation in HAFs."]

## Ontology note
- GO:0070123 (TGF-beta receptor activity, type III) is_a GO:0005024, whose definition includes Ser/Thr kinase catalysis; betaglycan has no kinase domain. Raised as a suggested question; GO:0005024 row MODIFY -> GO:0070123.

## Decisions
- Core: GO:0070123, GO:0015026 coreceptor, GO:0050431 TGF-beta binding, inhibin-betaglycan-ActRII complex, TGF-beta receptor signalling, plasma membrane/external side.
- Over-annotated: organ development, immune response, gene expression, hormone/PGE responses, intracellular signal transduction, SMAD binding, negative regulation of ECM assembly.
- ProtNLM2 GO:0005576 extracellular region: correct (shed soluble betaglycan) and not in donkey GOA -> COR.
