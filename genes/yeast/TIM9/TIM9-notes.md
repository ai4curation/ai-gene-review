# TIM9 review notes

## 2026-08-28 dedicated re-review

- All 29 physical GOA rows correspond to 29 distinct term/evidence/reference/
  qualifier signatures and are represented in `existing_annotations`. One
  evidence-supported NEW annotation adds GO:0140309.

- TIM9 and TIM10 form the soluble IMS chaperone shuttle, but their roles are not
  assumed to be identical at the subunit level. The intact complex binds carrier
  precursor and exhibits chaperone activity [PMID:12138093, “the reconstituted
  TIM10 complex is functional because it bound to the physiological substrate
  ADP/ATP carrier and displayed chaperone activity in refolding the model
  substrate firefly luciferase.”]. Deep research notes that isolated Tim10 binds
  AAC more strongly than isolated Tim9, supporting a comparatively stronger
  structural contribution from Tim9 while retaining a functional role in the
  assembled holdase/transporter.

- Live QuickGO calls GO:0140309 `unfolded protein holdase activity`; the former
  `unfolded protein carrier activity` is an exact synonym. The term covers binding
  an unfolded client, preventing its aggregation, and escorting it to an acceptor
  or location. GO:0140318 remains independently appropriate and core because its
  definition is direct protein binding plus delivery to a cellular location, and
  its ontology comment explicitly cites the soluble Tim9-Tim10 shuttle.

- All three GOA IBA rows use PTN004407763. The current cached PAINT table retains
  this node but now carries only GO:0042719 IMS chaperone-complex membership;
  GO:0005743, GO:0045039, and GO:0140318 are absent. Each GOA IBA therefore records
  `SOURCE_STALE_OR_MISSING` for the PTN while retaining ACCEPT because direct TIM9
  experimental annotations independently support all three claims. The target
  `SGD:S000007256` appearing in WITH/FROM is valid experimental grounding, not
  circularity.

- The single GO:0005515 IPI is marked over-annotated rather than removed: the
  Tim9-Tim10 interaction is real, but generic protein binding loses the informative
  IMS chaperone-complex and transporter context.

- Metal-ion and zinc-binding rows remain over-annotated for mature TIM9. UniProt
  says zinc coordination during cytoplasmic transit is probable, whereas the mature
  IMS protein contains two intramolecular disulfides; the RCA zinc-proteome row is
  motif-based rather than a direct TIM9 zinc-binding assay.

- TIM22-directed carrier delivery is the best directly supported route. UniProt and
  the deep-research synthesis implicate small Tims in some beta-barrel precursor
  delivery toward SAM, but the cached TIM9 primary literature reviewed here does not
  establish that route at the same resolution, so it is described as secondary and
  remains an experimental question.

- PMID:19037698 is a verified wrong identifier: its cached full text is an unrelated
  colorectal-surgery paper. The IMS localization is independently established, so
  the annotation remains ACCEPT while the reference is marked `WRONG_IDENTIFIER`;
  PMID:19037098 is the plausible transposed identifier.

- Twelve of the thirteen cached PMID records are abstract-only. Experimental rows
  were not rejected merely because their full assay details were unavailable.
