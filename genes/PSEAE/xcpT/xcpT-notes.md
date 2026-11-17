# xcpT (Pseudomonas aeruginosa PAO1, Q00514) curation notes

## 2026-11-13 initial review

- Reviewed as the characterized GspG major-pseudopilin exemplar for
  `modules/bacterial_type_ii_secretion.yaml`, alongside the KT2440 member `genes/PSEPK/gspG`.
- Deep research was not run: no deep-research provider credentials are available in this environment and
  no `-deep-research-<provider>.md` file was created. The review rests on the cached publications cited by
  GOA (`publications/PMID_*.md`, mostly abstract-only) and the curated UniProt record.
- Both EXP plasma-membrane rows are sound: SRP-Sec-dependent insertion of XcpT-PhoA hybrids
  [PMID:17172336 "this transport process involves the cotranslational signal recognition particle
  targeting route and is dependent on a functional Sec translocon"] and inner-membrane fractionation of
  the PilD-processed protein [PMID:8331069 "the precursor forms of XcpT-W are located predominantly in the
  bacterial inner membrane"].
- The PAINT node PTN000764351 (PTHR30093) is seeded by XcpT, XcpU and HxcT. Its leaf composition was
  checked in `genes/PSEAE/xcpT/xcpT-bioinformatics/RESULTS.md`: 639 of 642 leaves carry T2SS names, so the
  node stops short of the type IV pilin subfamily PTHR30093:SF34 and the IBA rows are accepted.
- Two recurring PseudoCAP defects are recorded, consistently with the other Xcp reviews: the GO:0015627
  IDA keyed to PMID:8331069 (a processing and fractionation paper) is better keyed to PMID:9282737, and
  the GO:0015628 IDA keyed to the review PMID:9818381 should be TAS or re-keyed to a primary paper.
- A NEW GO:0005198 structural molecule activity row was added: the GOA set gives XcpT no molecular
  function, yet XcpT alone among the Xcp pseudopilins polymerises into the pseudopilus
  [PMID:16012171 "none of the other four pseudopilins are able to form a pseudopilus"], visualised by
  electron microscopy [PMID:12700254]. The same assignment is used for KT2440 GspG.
- The adhesive property of the overproduced hyper-pseudopilus [PMID:12700254] is left unannotated: it is
  an overexpression phenotype, raised as a suggested question instead.
