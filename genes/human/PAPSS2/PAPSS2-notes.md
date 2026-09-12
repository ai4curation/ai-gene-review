# PAPSS2 (O95340) review notes

Human gene **PAPSS2** — Bifunctional 3'-phosphoadenosine 5'-phosphosulfate synthase 2
(HGNC:8604; GeneID 9060; chromosome 10). Paralog of PAPSS1 (O43252).

## Summary of function (grounded in UniProt O95340)

PAPSS2 is one of the two human bifunctional PAPS synthases. It carries out both steps of
the "sulfate activation" pathway on a single polypeptide:

1. **ATP sulfurylase / sulfate adenylyltransferase (ATP)** (EC 2.7.7.4): sulfate + ATP + H+ =
   adenosine 5'-phosphosulfate (APS) + diphosphate. C-terminal domain (residues ~224–614).
2. **APS kinase / adenylyl-sulfate kinase** (EC 2.7.1.25): APS + ATP = 3'-phosphoadenylyl
   sulfate (PAPS) + ADP + H+. N-terminal domain (residues ~1–215).

The product PAPS is the universal sulfonate donor used by all cytosolic and Golgi
sulfotransferases.

- [file:human/PAPSS2/PAPSS2-uniprot.txt "Bifunctional enzyme with both ATP sulfurylase and APS kinase activity, which mediates two steps in the sulfate activation pathway"]
- [file:human/PAPSS2/PAPSS2-uniprot.txt "The first step is the transfer of a sulfate group to ATP to yield"] adenosine 5'-phosphosulfate (APS); the second step is the transfer of a phosphate group from ATP to APS yielding PAPS, "the activated sulfate donor used by sulfotransferases".
- [file:human/PAPSS2/PAPSS2-uniprot.txt "In mammals, PAPS is the sole source of sulfate while"] APS is only an intermediate.
- Domain architecture: [file:human/PAPSS2/PAPSS2-uniprot.txt "In the N-terminal section; belongs to the APS kinase"] family; [file:human/PAPSS2/PAPSS2-uniprot.txt "In the C-terminal section; belongs to the sulfate"] adenylyltransferase family.
- EC numbers: [file:human/PAPSS2/PAPSS2-uniprot.txt "EC=2.7.7.4"] and [file:human/PAPSS2/PAPSS2-uniprot.txt "EC=2.7.1.25"].
- Pathway: [file:human/PAPSS2/PAPSS2-uniprot.txt "Sulfur metabolism; sulfate assimilation."]

## Tissue specificity and physiology

- [file:human/PAPSS2/PAPSS2-uniprot.txt "Expressed in cartilage and adrenal gland."] (PubMed:19474428)
- PAPSS2 is the predominant PAPS synthase in cartilage; PAPS is required for
  glycosaminoglycan/proteoglycan sulfation. Reactome: PAPSS2 "is essential for the sulfation
  of glycosaminoglycan chains of proteoglycans, a necessary post-translational modification"
  (reactome/R-HSA-174389.md, R-HSA-174392.md).
- [file:human/PAPSS2/PAPSS2-uniprot.txt "Plays indirectly an important role in skeletogenesis"] during postnatal growth (PubMed:9771708).

## Disease

Biallelic loss-of-function PAPSS2 mutations cause an autosomal-recessive skeletal dysplasia,
**brachyolmia type 4 / spondyloepimetaphyseal dysplasia Pakistani type (SEMD-PA), MIM:612847**,
via undersulfation of cartilage proteoglycans; some patients also show premature pubarche and
androgen excess from impaired DHEA sulfation.

- [file:human/PAPSS2/PAPSS2-uniprot.txt "Brachyolmia type 4 with mild epiphyseal and metaphyseal"] changes (BCYM4) [MIM:612847].
- [file:human/PAPSS2/PAPSS2-uniprot.txt "Some BCYM4 patients may manifest premature pubarche and"] hyperandrogenism.
- Premature pubarche / androgen excess mechanism: SULT2A1 (DHEA sulfotransferase) "requires
  3'-phosphoadenosine-5'-phosphosulfate (PAPS) for catalytic activity" and compound
  heterozygous PAPSS2 mutations were identified "in a girl with premature pubarche,
  hyperandrogenic anovulation, very low DHEAS levels, and increased androgen levels"; these
  "indicate that PAPSS2 deficiency is a monogenic adrenocortical cause of androgen excess"
  (PMID:19474428 abstract).
- PAPSS2-brachyolmia mutation series: "loss-of-function mutations of PAPSS2, the gene encoding
  PAPS (3'-phosphoadenosine 5'-phosphosulfate) synthase 2"; "In vitro enzyme assays showed that
  the missense mutations were also loss-of-function mutations"; the disorder "is associated with
  abnormal androgen metabolism" (PMID:23824674 abstract).

## Subcellular localization

Both PAPS synthases shuttle between cytoplasm and nucleus; PAPSS2 is predominantly cytosolic
while PAPSS1 is predominantly nuclear (PMID:22242175, full text).

- [PMID:22242175 "PAPSS1 was predominantly nuclear, whereas PAPSS2 localised mainly within the cytoplasm."]
- [PMID:22242175 "both isoforms contain a conserved N-terminal basic Lys-Lys-Xaa-Lys motif indispensable for their nuclear localisation"]
- [PMID:22242175 "mobile enzymes capable of executing their function in the cytoplasm as well as in the nucleus"]
- Older nuclear-relocation observation (PMID:10657990, abstract only): PAPSS2 "localizes to the
  cytoplasm when ectopically expressed in mammalian cells, is relocated to the nucleus when
  coexpressed with PAPSS1." The nucleus IGI (GO:0005634) annotation is transferred with/from
  PAPSS1 (UniProtKB:O43252) — a genetic-interaction inference from PAPSS1 co-expression, not a
  demonstration that PAPSS2 acts natively in the nucleus.

## Protein interactions (high-throughput; bare protein binding)

GO:0005515 "protein binding" IPI annotations come from large-scale interactome screens:
- PMID:32296183 (HuRI binary interactome; partners HSF2BP/O75031, CEP19/Q96LK0)
- PMID:32814053 (neurodegenerative-disease Y2H network; partner OPTN/Q96CV9)
- PMID:33961781 (BioPlex AP-MS; partner PAPSS1/O43252 — consistent with the known PAPSS1/PAPSS2
  heterodimer)
UniProt INTERACTION block lists CEP19, HSF2BP, OPTN and PAPSS1 as partners. These are
uninformative for molecular function (bare protein binding) and are marked as over-annotated;
none is removed (experimental IPI).

## Core function determination

- MF: **GO:0004781 sulfate adenylyltransferase (ATP) activity** and **GO:0004020 adenylylsulfate
  kinase activity** (both experimentally/structurally established; the two catalytic domains).
- MF: **GO:0005524 ATP binding** (both catalytic reactions use ATP; UniProt BINDING sites for
  two ATP ligands).
- BP: **GO:0050428 PAPS biosynthetic process** and **GO:0000103 sulfate assimilation**.
- CC: **GO:0005829 cytosol** (predominant); nucleus is a secondary, PAPSS1-co-expression /
  shuttling context (kept non-core).

## Annotations judged non-core / over-annotated

- GO:0042445 hormone metabolic process (IMP, PMID:19474428): downstream/indirect — PAPSS2
  supplies PAPS to SULT2A1 for DHEA sulfation. Kept as non-core (pleiotropic downstream role),
  not a direct molecular function of PAPSS2.
- GO:0016779 nucleotidyltransferase activity (ISS, GO_REF:0000024): correct-branch parent of the
  sulfurylase activity but less informative than GO:0004781; MODIFY → GO:0004781.
- GO:0005515 protein binding (IPI x3): over-annotated (uninformative).
