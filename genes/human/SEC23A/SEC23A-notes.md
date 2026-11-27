# SEC23A (human, Q15436) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised reference for HORSE/SEC23A
(A0A3Q2H5Z6). ProtNLM2 output was not opened or used.

### Deep research

`just deep-research-falcon human SEC23A --fallback perplexity-lite` failed: falcon
returned "Failed to authenticate" and the perplexity fallback returned HTTP 401
(insufficient quota). No deep-research file exists; the review is based on the cached
publications, the UniProt record and Reactome entries.

### Evolutionary grounding

- UniProt Q15436 is in PANTHER PTHR11141:SF7 (PROTEIN TRANSPORT PROTEIN SEC23A) within
  PTHR11141 (SEC23). The paralog SEC23B is in a separate subfamily (PROTEIN TRANSPORT
  PROTEIN SEC23B).
- The four IBA rows (COPII vesicle coat, ER exit site, COPII-coated vesicle cargo
  loading, GTPase activator activity) come from PAINT node PTN000124617. Human Q15436 is
  itself a donor for the first three; the GTPase activator IBA rests on yeast Sec23
  donors only. The horse ortholog receives the same four IBA rows.
- PAINT did not propagate zinc ion binding, ER membrane, cytosol, or any binding term from
  the human experimental data; I took those omissions as deliberate and did not add them
  as inherited family functions.

### What is experimentally established in human SEC23A

- Localisation to the transitional ER / ER exit sites and associated vesicles by
  immuno-EM; soluble cytosolic ~350 kDa complex; complementation of yeast sec23-1
  [PMID:8898360 "hSec23Ap is a functional homologue of the yeast Sec23p as the hSec23A
  isoform complemented the temperature sensitivity of the Saccharomyces cerevisiae
  sec23-1 mutation at a restrictive temperature of 34 degrees C."]
- CLSD F382L is a loss of function in cell-free budding [PMID:16980979 "Cell-free vesicle
  budding assays show that the F382L substitution results in loss of SEC23A function."]
  and the mutant poorly recruits SEC13-SEC31 [PMID:17981132].
- Structures with SEC22B cargo at the Sec23/24 interface [PMID:17499046] and PPP-motif
  binding by the gelsolin-like domain to TANGO1/cTAGE5 PRDs and SEC31 [PMID:27551091
  "Sec23 recognizes merely a PPP motif"].
- Preferential binding to SAR1B [PMID:32358066].

### Inferred, not shown directly in human (in the cached literature)

- SAR1 GTPase-activating activity: established for yeast Sec23p; human assignment is
  PAINT inference plus the conserved SAR1 interface. Accepted, flagged in a suggested
  question.
- Zinc: structure-derived UniProt binding sites (C61/C66/C85/C88), kept as non-core.

### Decisions worth flagging

- 48 GO:0005515 rows: REMOVE per policy, except MODIFY to SNARE binding (SEC22B,
  PMID:17499046), MHC class I protein binding (PMID:20946353), protein kinase binding
  (CDK16, PMID:16091426) and proline-rich region binding (TANGO1/cTAGE5,
  PMID:27551091 and PMID:28442536).
- Endocytic recycling (ISO from mouse, GLUT4 trafficking): MARK_AS_OVER_ANNOTATED,
  because COPII acts at ER exit and the GLUT4 requirement reads as necessity, not
  participation.
- The zebrafish morpholino craniofacial phenotype in PMID:16980979 was not used as
  process evidence.
- No NEW terms. COPII vesicle coat assembly (GO:0048208) was considered, but budding and
  cargo loading already cover the process, so I did not add it.
