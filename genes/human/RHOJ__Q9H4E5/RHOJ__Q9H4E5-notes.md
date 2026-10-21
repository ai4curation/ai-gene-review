# RHOJ (Q9H4E5, canonical human RHOJ_HUMAN) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: the reviewed canonical RHOJ product Q9H4E5 (214 aa, ENST00000316754). The folder is `RHOJ__Q9H4E5` because `genes/human/RHOJ` is keyed to the fragment-like G3V4H1 product of the NMD transcript ENST00000557447. No ProtNLM2 file or prediction output was opened or used.

### Provenance and process

- `just fetch-gene human Q9H4E5 --alias RHOJ__Q9H4E5`: 54 GOA rows were seeded. `just fetch-gene-pmids` cached all 11 GOA PMIDs.
- **Deep research failed.** `just deep-research-falcon human RHOJ__Q9H4E5 --fallback perplexity-lite` failed with falcon "Failed to authenticate", and the perplexity fallback returned HTTP 401 (insufficient quota). No deep-research file exists in this folder. As background I read the same-gene falcon report in `genes/human/RHOJ/RHOJ-deep-research-falcon.md` (same HGNC gene; generated for G3V4H1, but its literature content is gene-level). I re-derived every claim used here from primary papers, which I cached myself.
- Additional primary papers cached: PMID:21148427 (Kaur 2011), PMID:32347571 (Fukushima 2020), PMID:12960428 (de Toledo 2003, full text), PMID:24928894 (Wilson 2014, full text), PMID:24434213 (Kim 2014). PMIDs were found with NCBI esearch and their titles checked with esummary.
- New analysis: `RHOJ__Q9H4E5-bioinformatics/evolutionary_grounding.py` produced `RESULTS.txt` and `RESULTS.md`.

### Evolutionary grounding

- PANTHER 19 (live geneinfo) places Q9H4E5 in PTHR24072:SF17, RHO-RELATED GTP-BINDING PROTEIN RHOJ. The G domain is complete (G1 GDGAVGKT 28, switch I PTVFD 52, switch II DTAGQ 75, G4 TQID 133, G5 CSAL 175), and the CAAX box is CSII at 211.
- GTPase activity, GTP binding and plasma membrane are IBD at the family root PTN000632671, and Q9H4E5 is itself a seed. These three are measured on human RHOJ and also inherited.
- Actin filament organization and signal transduction come from the root, with no RHOJ seed. RHOJ-specific data agree with them.
- Protein kinase binding (PTN008604840), endocytosis and establishment of cell polarity (PTN008604842) come from Cdc42-seeded nodes. They are inferences for RHOJ. Protein kinase binding is independently confirmed (GTP-dependent PAK CRIB binding [PMID:10967094 "GTP-bound but not GDP-bound TCL protein directly interacts with Cdc42/Rac interacting binding domains, such as those found in PAK and WASP"]). For endocytosis, RHOJ-specific data refine the term [PMID:12960428 "Receptor-dependent internalization of transferrin (Tf) is unaffected by suppression of endogenous TCL by small interfering RNA treatment."]. Cell polarity is untested for RHOJ.

### Experimentally established in human (vs inferred)

- Human protein, in vitro: GDP/GTP exchange and intrinsic hydrolysis [PMID:10967094]; mant-GTP loading [PMID:27660391]; GTP-dependent CRIB binding [PMID:10967094].
- Human cells: plasma membrane localization, controlled by N-terminal residues 17-20 (HeLa) [PMID:27660391] and by palmitoylation of C3/C11 supported by GLUL (HUVEC) [PMID:30158707]; early/sorting endosomes and an early endocytic trafficking role (HeLa) [PMID:12960428]; focal adhesions (HUVEC, endogenous protein) [PMID:21148427, PMID:24928894]; promotion of focal adhesion disassembly (HUVEC TIRF) [PMID:24928894]; promotion of endothelial migration and tube/lumen formation (HUVEC, ECFC) [PMID:21148427, PMID:21628409, PMID:28727754].
- Mouse in vivo: retinal and tumor angiogenesis [PMID:32347571, PMID:24434213]. Sema3E/PlexinD1 transduction is in the PMID:32347571 abstract, which does not say which species' endothelial cells were used for the mechanism. That NEW annotation carries this caveat.
- Inferred only: establishment of cell polarity (from Cdc42).

### Decisions (summary)

- ACCEPT: GTPase activity (4 rows), G protein activity, GTP binding (3), plasma membrane (7), actin filament organization, signal transduction, protein kinase binding (IBA), actin cytoskeleton organization (2), GO:0090050.
- MODIFY: regulation of endothelial cell migration -> positive (GO:0010595); regulation of sprouting angiogenesis (2 rows) -> positive (GO:1903672); PAK1/2/3/5/6 protein-binding rows -> protein kinase binding.
- MARK_AS_OVER_ANNOTATED: endocytosis (IBA). RHOJ acts after internalization.
- KEEP_AS_NON_CORE: establishment of cell polarity (IBA), extracellular exosome (HDA).
- REMOVE: the remaining bare protein-binding rows (CRIB effectors WASL, CDC42EP1, PARD6B, TRIP10; screen hits; GLUL). These are removed under the GO:0005515 policy, not because the interactions are false. Effector binding is captured as NEW GBD domain binding.
- NEW: GBD domain binding (IDA, PMID:10967094), focal adhesion (IDA, PMID:21148427), positive regulation of focal adhesion disassembly (IMP, PMID:24928894), semaphorin-plexin signaling pathway (IMP, PMID:32347571; RHOJ binds the PlexinD1 cytoplasmic domain and transduces the signal, so it participates and is not merely required).
- Not proposed: lumen formation and phenotype-level angiogenesis terms beyond the existing rows. I did not add early endosome, because the evidence is HeLa overexpression, and recorded the trafficking question in suggested_questions instead.
