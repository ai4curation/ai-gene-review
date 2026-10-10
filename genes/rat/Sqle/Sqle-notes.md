# Sqle (rat) notes

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d) changes:
- 6 new rows, all resolved:
  - squalene monooxygenase activity ISO from human SQLE (Q14534): ACCEPT. Donor-split duplicate of the mouse-donor ISO row.
  - cholesterol biosynthetic process IEA (GO_REF:0000120) and ISO from human SQLE: ACCEPT.
  - sterol biosynthetic process IBA (PTN000089417): ACCEPT.
  - sterol metabolic process (ARBA) -> MODIFY to sterol biosynthetic process (GO:0016126).
  - secondary alcohol metabolic process (ARBA) -> MODIFY to cholesterol biosynthetic process (GO:0006695). The term is a chemical-class grouping.
- 6 rows retired: cholesterol metabolic process IEA, cholesterol biosynthetic process IEA (GO_REF:0000107), and four via-desmosterol/via-lathosterol rows. QuickGO shows GO:0033489 and GO:0033490 are now obsolete ("represents a specific pathway variant, which is out of scope for GO"). Reviews kept with a retirement note.

Action changes:
- ER (IBA) and ER membrane (IEA, ISO): KEEP_AS_NON_CORE -> ACCEPT. The ER membrane is where the enzyme acts [UniProtKB:P52020 "SUBCELLULAR LOCATION: Microsome membrane"; "Endoplasmic reticulum membrane; Peripheral membrane protein"]. Added ER membrane to core_functions.locations.
- Zymosterol biosynthetic process (IEA, ISO): MODIFY -> KEEP_AS_NON_CORE. Sqle does catalyze an upstream step toward zymosterol; the earlier MODIFY pointed to a term the gene already carries. This now matches the treatment of the same term in the Lss review.
- Response to biphenyl (IDA, PMID:11520216): stays REMOVE, but the reason was rewritten. The old text said the paper "does not mention biphenyl", which is wrong: HHDP esters are biphenyl derivatives. The real problem is that the paper reports in vitro inhibition of the recombinant enzyme [PMID:11520216 "were evaluated as enzyme inhibitors of recombinant rat squalene epoxidase"]. That is not a response-to-stimulus process carried out by Sqle.
- Location, FAD-binding and lipid-droplet-formation rows now cite specific UniProt CC text (COFACTOR "Name=FAD", SUBUNIT "Interacts with SMIM22; this interaction modulates lipid droplet formation.") instead of the generic FUNCTION quote.
- 2 stale UniProt quotes fixed (core_functions and the biphenyl row).
- Description rewritten without curation commentary.

Open questions:
- Regulation of cell population proliferation (IEA/ISS/ISO from human SQLE) stays MARK_AS_OVER_ANNOTATED as an indirect, cholesterol-dependent consequence. A human curator may prefer REMOVE.
