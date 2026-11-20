# xcpY (Pseudomonas aeruginosa PAO1, P25060) curation notes

## 2026-11-13 initial review

- Reviewed as the characterized GspL assembly-platform exemplar for
  `modules/bacterial_type_ii_secretion.yaml`, alongside the KT2440 member `genes/PSEPK/xcpY`.
- Deep research was not run (no provider credentials in this environment); no
  `-deep-research-<provider>.md` file was created. Sources are the GOA-cited cached publications and the
  curated UniProt record.
- Topology is experimentally mapped [PMID:8763961 "We report data demonstrating the N(in)-C(out)
  topologies of three general secretion pathway components, the XcpP, -Y, and -Z proteins"], giving
  cytoplasmic 1-233, one transmembrane helix and periplasmic 255-382 in the UniProt record.
- The IEA row for GO:0009276 Gram-negative-bacterium-type cell wall was removed. That term is a subclass
  of GO:0009274 peptidoglycan-based cell wall, and no part of a bitopic inner-membrane platform protein
  lies in the peptidoglycan layer. The fault is in the InterPro2GO mapping of IPR007812 (T2SS GspL),
  which affects the whole family, so it is recorded as an INTERPRO source defect rather than a
  PSEUDOCAP one.
- Complex membership rests on co-purification with His-tagged XcpZ and then with XcpR and XcpS
  [PMID:16168578 "This subcomplex was also found to interact with XcpR and XcpS to form a XcpRSYZ
  complex which was isolated under native conditions"], supported by mutual stabilisation with XcpZ
  [PMID:9884230] and by stabilisation of XcpS together with XcpR [PMID:17464073].
- Substrate engagement by the periplasmic domain [PMID:30337370] is noted but not annotated as a
  separate molecular function; it is raised as a suggested question.
