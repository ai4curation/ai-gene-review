# SELENOI (EPT1) — gene review notes

UniProt: Q9C0D9 (EPT1_HUMAN). HGNC:29361. Human, NCBITaxon:9606. 397 aa.
Gene symbol SELENOI (synonyms EPT1, SELI, KIAA1724). All identifiers and quotes
below from `file:human/SELENOI/SELENOI-uniprot.txt` unless a PMID is given.

## Core identity

SELENOI is **ethanolaminephosphotransferase 1 (EPT1 / hEPT1)**, a **selenoprotein**
(Selenoprotein I) and a **multi-pass ER-membrane** enzyme of the **CDP-alcohol
phosphatidyltransferase class-I family**. It catalyzes the **final (third) step of
the CDP-ethanolamine branch of the Kennedy pathway** for phosphatidylethanolamine
(PE) biosynthesis.

- RecName in UniProt: "Ethanolaminephosphotransferase 1"; Short "hEPT1"; EC 2.7.8.1
  [file:human/SELENOI/SELENOI-uniprot.txt "RecName: Full=Ethanolaminephosphotransferase 1"].
- Selenoprotein: contains a **selenocysteine at residue 387** (`NON_STD 387 /note="Selenocysteine"`),
  established by [PMID:12775843] ("Characterization of mammalian selenoproteomes");
  AltName "Selenoprotein I" [file:human/SELENOI/SELENOI-uniprot.txt "AltName: Full=Selenoprotein I"].
- Multi-pass ER membrane protein: 10 TRANSMEM helices annotated; SUBCELLULAR LOCATION
  "Endoplasmic reticulum membrane ... Multi-pass membrane protein"
  [file:human/SELENOI/SELENOI-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"].
- Family: "Belongs to the CDP-alcohol phosphatidyltransferase class-I family"
  [file:human/SELENOI/SELENOI-uniprot.txt "Belongs to the CDP-alcohol phosphatidyltransferase class-I"].

## Catalytic activity

Two reactions in UniProt CATALYTIC ACTIVITY:
1. **Diacyl (canonical PE):** CDP-ethanolamine + 1,2-diacyl-sn-glycerol (DAG) =
   1,2-diacyl-sn-glycero-3-phosphoethanolamine (PE) + CMP + H+ (RHEA:32943; EC 2.7.8.1),
   evidenced experimentally by PubMed:17132865, 28052917, 29500230.
2. **Ether-linked (plasmanyl-PE):** 1-O-alkyl-2-acyl-sn-glycerol + CDP-ethanolamine =
   1-O-alkyl-2-acyl-sn-glycero-3-phosphoethanolamine + CMP + H+ (RHEA:36187),
   ECO:0000305 from PubMed:29500230.

Cofactor: **Mg(2+) or Mn(2+)** (ECO:0000269|PubMed:17132865). Kinetics: KM 1.8 uM for
CDP-ethanolamine (PubMed:17132865). Explains the `metal ion binding` (GO:0046872,
UniProtKB-KW) IEA annotation, though this is over-annotation of the divalent-cation
requirement rather than a distinct informative MF.

PATHWAY: "Phospholipid metabolism; phosphatidylethanolamine biosynthesis;
phosphatidylethanolamine from ethanolamine: step 3/3"
[file:human/SELENOI/SELENOI-uniprot.txt "phosphatidylethanolamine from ethanolamine: step 3/3"].

## Experimental evidence for GO annotations

- **PMID:17132865 (Horibata & Hirabayashi 2007, J Lipid Res)** — abstract-only cache
  (full_text_available: false). Identified/characterized hEPT1: bacterial (E. coli)
  expression showed the product "specifically used CDP-ethanolamine as the phosphobase
  donor to produce PE with the activation by both Mn(2+) and Mg(2+)"
  [PMID:17132865 "specifically used \nCDP-ethanolamine as the phosphobase donor to \nproduce PE"].
  Supports GO:0004307 (IDA, HGNC) and GO:0006646 (IDA). CDP-alcohol phosphatidyltransferase
  signature noted [PMID:17132865 "human selenoprotein I contained the CDP-alcohol \nphosphatidyltransferase signature"].
  Tissue specificity: ubiquitous; highest in brain cerebellum.

- **PMID:28052917 (Ahmed et al. 2017, Brain)** — FULL TEXT available. First human disease
  (complex HSP / SPG81) from EPT1 mutation; p.Arg112Pro in the CDP-alcohol phosphotransferase
  motif. WT and mutant human EPT1 expressed in an S. cerevisiae strain "devoid of endogenous
  ethanolaminephosphotransferase activity"; 14C-ethanolamine incorporation into PE by the
  mutant was "only 3% that of wild-type EPT1" — a loss-of-function
  [PMID:28052917 "only 3% that of wild-type EPT1"]. Supports IMP GO:0004307 & GO:0006646.
  ER-membrane / integral-membrane: the enzyme was "associated with the membrane fraction as
  would be expected for an integral membrane protein"
  [PMID:28052917 "associated with \nthe membrane fraction as would be expected for an integral membrane protein"].
  NOTE: the "is_active_in ER membrane" IDA (ECO:0000314, PubMed:28052917) rests on membrane-
  fraction association in the heterologous yeast system, not on direct human-cell imaging;
  the ER localization is nonetheless firmly established across sources (UniProt SUBCELLULAR
  LOCATION, Reactome). Kept as core location.
  Function: "catalyses the final step in the synthesis of PE via the Kennedy pathway"
  [PMID:28052917 "catalyses the final step in the synthesis of PE via the Kennedy pathway"].

- **PMID:29500230 (Horibata et al. 2018, J Lipid Res)** — abstract-only cache. Patient with
  severe complicated HSP; EPT1 exon-skipping mutation. EPT "transfers phosphoethanolamine
  from cytidine diphosphate-ethanolamine to lipid acceptors to produce ethanolamine
  glycerophospholipids, such as diacyl-linked phosphatidylethanolamine (PE) and ether-linked
  plasmalogen [plasmenyl-PE]"
  [PMID:29500230 "produce ethanolamine \nglycerophospholipids, such as diacyl-linked phosphatidylethanolamine (PE) and \nether-linked plasmalogen"].
  In patient fibroblasts and EPT1-KO HeLa cells: reduced PE species and "most plasmenyl-PE
  species were significantly decreased" [PMID:29500230 "most plasmenyl-PE species were significantly decreased"].
  Concludes "the indispensable role of EPT1 in the myelination process and neurodevelopment,
  and in the maintenance of normal homeostasis of ether-linked phospholipids in humans"
  [PMID:29500230 "the indispensable role of EPT1 in the myelination process and neurodevelopment"].
  Supports IMP GO:0004307 & GO:0006646; underpins ISS/Ensembl myelination (GO:0042552) and
  ether-lipid (GO:0008611) annotations.

## Disease

**Spastic paraplegia 81, autosomal recessive (SPG81; MIM:618768)** — a complicated HSP with
white-matter abnormalities / hypomyelination, delayed motor development, spasticity, impaired
intellectual development, bifid uvula, microcephaly, seizures, ocular anomalies
[file:human/SELENOI/SELENOI-uniprot.txt "Spastic paraplegia 81, autosomal recessive (SPG81)"].
Refs: PubMed:28052917, 29500230, 36942482. This is a phenotypic/disease association, not a GO
process the gene product directly executes; myelination (GO:0042552) is the closest BP but is
downstream/consequential and only IEA/ISS-supported → KEEP_AS_NON_CORE.

## GO annotation review summary (24 GOA rows)

Core MF: **GO:0004307 ethanolaminephosphotransferase activity** (IDA PMID:17132865, IMP
PMID:28052917, IMP PMID:29500230; also IBA/ISS/IEA). ACCEPT the experimental ones as core.

Core BP: **GO:0006646 phosphatidylethanolamine biosynthetic process** (IDA/IMP experimental).
ACCEPT as core (this is the specific "PE from CDP-ethanolamine, step 3/3" pathway; no
more-specific GO child exists — verified against go.db).

Core CC: **GO:0005789 endoplasmic reticulum membrane** (IDA PMID:28052917; IBA; IEA; TAS
Reactome). ACCEPT as core location.

- GO:0005794 Golgi apparatus (IBA) — pan-family phylogenetic call; SELENOI itself is
  established as ER, not Golgi. UniProt/Reactome place it at the ER. IBA over-propagation →
  MARK_AS_OVER_ANNOTATED (not REMOVE: IBA, and some CEPT-family members do localize to
  Golgi/nuclear envelope).
- GO:0008611 ether lipid biosynthetic process (ISS + Ensembl IEA) — supported: plasmanyl/
  plasmenyl-PE synthesis (PMID:29500230). Real but secondary → KEEP_AS_NON_CORE.
- GO:0042552 myelination (ISS + Ensembl IEA) — downstream phenotype/consequence, not a direct
  MF/BP the enzyme executes → KEEP_AS_NON_CORE.
- GO:0008610 lipid biosynthetic process (IEA, ARBA) — correct but too general vs GO:0006646/
  GO:0008654 → MARK_AS_OVER_ANNOTATED.
- GO:0008654 phospholipid biosynthetic process (IEA, InterPro) — correct but a generalization
  of the specific PE process → MARK_AS_OVER_ANNOTATED.
- GO:0016020 membrane (IEA, InterPro) — correct but generic; ER membrane is the specific,
  experimentally-supported CC → MARK_AS_OVER_ANNOTATED.
- GO:0016780 phosphotransferase activity, for other substituted phosphate groups (IEA,
  InterPro) — parent/general form of GO:0004307 → MODIFY to GO:0004307.
- GO:0046872 metal ion binding (UniProtKB-KW; in UniProt DR, not in the 24-row seeded GOA
  TSV as a distinct reviewed row) — reflects the Mg2+/Mn2+ cofactor requirement; not a
  distinct informative MF. (Not present as a seeded existing_annotation row.)

## core_functions chosen (author-supplied, strictly validated)

- MF: GO:0004307 ethanolaminephosphotransferase activity
  (+ directionally, catalysis of PE and plasmanyl-PE from CDP-ethanolamine)
- located in: GO:0005789 endoplasmic reticulum membrane
- part of BP: GO:0006646 phosphatidylethanolamine biosynthetic process (CDP-ethanolamine /
  Kennedy pathway, final step)

## 2026-11-19 ORGANELLES Golgi batch 4 (Golgi apparatus rows)

- One GO:0005794 row (IBA, is_active_in). MARK_AS_OVER_ANNOTATED changed to KEEP_AS_NON_CORE.
- PAINT IBD at PTN000045767 (interpro/panther/PTHR10414/PTHR10414-paint.tsv) is seeded only by the
  CHPT1 lineage (fly cpt FBgn0031948, mouse Chpt1 MGI:2384841, human CHPT1 Q8WUD6). SELENOI seeds
  the ER membrane IBD at the same node. This is the same seed pattern as CEPT1 (Golgi batch 1).
- The earlier action assumed SELENOI is an established ER enzyme. The UniProt ER item is ECO:0000305
  (curator inference), and none of the cached SELENOI papers images the protein.
- A PubMed search (EPT1/SELENOI/selenoprotein I AND Golgi/localization) found Horibata, Ando and
  Sugimoto 2020 [PMID:32576654 "Immunohistochemical analyses revealed that EPT1 localizes to the
  Golgi apparatus and CEPT1 to the ER."]. Fetched with `ai-gene-review fetch-pmid`: abstract only.
  The full text (PMC7397746, DOI 10.1194/jlr.RA120000898) could not be retrieved through the PubMed
  MCP or the Europe PMC REST API. So the Golgi marker and whether EPT1 was endogenous or tagged are
  unchecked. The positive author statement gets deference (P3H2/RP2 pattern).
- Varlamova et al. 2017 (PMID:29101747, abstract seen in PubMed only, not cached or cited) report
  SELENOI in nucleus, cytoplasm and ER of tumour cell lines. Low weight.
- is_active_in: activity at the Golgi is not shown. Brefeldin A did not change the PE species made.
- Description now says the protein is assigned to the ER membrane and reported in the Golgi in
  HEK293 cells. The ER rows and core_functions (ER membrane) were left untouched (outside this
  check). Open question for a later pass: whether EPT1's ER location (ECO:0000305 only) still holds
  given PMID:32576654, and whether CEPT1's review should cite PMID:32576654 as a second line for
  its ER location.
