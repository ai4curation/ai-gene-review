# BACE2 notes

## 2026-10-05 review (PAINT, affinage)

- PMEL: [PMID:23754390 "Here we show that the BACE1 homologue BACE2 processes PMEL to generate functional amyloids."] TMEM27/CLTRN is shed in beta cells (PMID:21907142).
- PMID:10591213 (IDA endopeptidase and ectodomain proteolysis): the cached abstract describes Asp2, which is BACE1. Per CLAUDE.md, the curator's full-text reading is relied on (UniProt also cites the paper for BACE2), and the activity is independently shown for purified BACE2 (PMID:11423558).
- GO:0042985 (negative regulation of APP biosynthetic process) is changed to GO:1902430 negative regulation of amyloid-beta formation. BACE2 cleaves within the Abeta region and does not affect APP synthesis.
- Peptide hormone processing (NAS, from an expression-only abstract) is marked as an over-annotation.
- Removed 20 GO:0005515 rows.

## 2026-10-05 revision (reviewer round 1)

- Golgi rows now quote the UniProt line that names the Golgi. TGN is grounded in [PMID:11423558 "BACE2 localizes in the endoplasmic reticulum, Golgi, trans-Golgi network, endosomes, and plasma membrane, and its cellular localization patterns depend on the presence of its transmembrane domain."]. The proteolysis NAS now quotes the family-definition sentence.
- The PMID:10591213 Asp2 sentence is no longer used as support. Its reference_review correctness is omitted (unassessed).
- NEW protein autoprocessing (IDA, PMID:11316808). Also added Abeta degradation (PMID:22986058) and VEGFR3 shedding (PMID:38888964). core_functions is split into plasma-membrane shedding and melanosomal PMEL processing.
- The IAPP IPI stays REMOVE: the binding of a substrate is captured by the endopeptidase activity, and MODIFY to an enzyme activity is not appropriate for an IPI row.

## 2026-11-04 ORGANELLES ER batch 1 (endoplasmic reticulum rows)

- Rows: one GO:0005783 row, IEA GO_REF:0000044 (UniProt SL-0095), located_in. No ER sub-compartment row.
- Check: in the UniProt subcellular-location line the PubMed:11423558 tag belongs to the Golgi item; the "Endoplasmic reticulum" item has no evidence tag [file:human/BACE2/BACE2-uniprot.txt "CC       {ECO:0000269|PubMed:11423558}. Endoplasmic reticulum. Endosome."]. The same paper's abstract reports an ER pool directly [PMID:11423558 "BACE2 localizes in the endoplasmic reticulum, Golgi, trans-Golgi network, endosomes, and plasma membrane"].
- Topology: type I membrane protease (signal 1-20, propeptide 21-62, TM 474-494); no ER-retention motif, no ER-resident function; substrates are cleaved in endosomes/melanosomes and at the surface.
- Outcome: kept KEEP_AS_NON_CORE (real, transient biosynthetic pool shown directly). No NEW ER membrane row: the only ER-specific line is transit, not residence.
