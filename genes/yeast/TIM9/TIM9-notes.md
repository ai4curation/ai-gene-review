# TIM9 review notes

## 2026-08-28 dedicated re-review

- All 29 physical GOA rows correspond to 29 distinct term/evidence/reference/
  qualifier signatures and are represented in `existing_annotations`. The obsolete
  GO:0051082 row is modified to the more specific GO:0140309.

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

- The single GO:0005515 IPI should be removed rather than retained: the
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

## 2026-09-29 IBA refresh

- Current PTHR13172 PAINT now places `GO:0140309` unfolded protein holdase
  activity at `PANTHER:PTN004407763`, dated 2026-06-03. That corroborates the
  existing TIM9 `GO:0051082` to `GO:0140309` MODIFY.

- The stale GOA IBA rows are otherwise unchanged: the GOA snapshot still carries
  `GO:0005743`, `GO:0045039`, and `GO:0140318` from `PTN004407763`, while the
  current PAINT table carries only `GO:0042719` and `GO:0140309` at that node.

- 2025-2026 searches for TIM9, Tim9-Tim10, `YEL020W-A`, and yeast small-TIM
  literature did not find a newer TIM9-specific primary paper that changes the
  core holdase/chaperone interpretation.

## 2026-10-01 current GOA refresh

Refreshing GOA added 14 exact current rows. I retired nine assertions that have
fallen out of the current snapshot: the three stale `PANTHER:PTN004407763` IBA
rows for `GO:0005743`, `GO:0045039`, and broad `GO:0140318`; the old UniProt
keyword `GO:0015031` and `GO:0046872` IEAs; the old ARBA `GO:0042719` IEA;
the two former direct `GO:0140318` rows from `PMID:9822593`; and the old
`GO:0051082` unfolded-protein-binding row that GO has replaced with direct
`GO:0140309` holdase rows.

The current `PTHR13172` PAINT slice still places the new `GO:0042719`
mitochondrial IMS chaperone-complex IBA and the 2026 `GO:0140309` unfolded
protein holdase activity assertion at `PANTHER:PTN004407763`, so the new IBA is
a clean `NO_FAILURE_CORE` transfer. As in the 2026-09-29 pass, older GOA rows
against the same node disappeared from GOA because current PAINT no longer
places mitochondrial inner membrane, protein insertion into mitochondrial inner
membrane, or broad protein transporter activity at `PTN004407763`.

The full-text 2018 Weinhäupl et al. TIM9-TIM10 structural paper now supports
four current FlyBase rows. Its recombinant TIM9-TIM10/client data directly
support `GO:0140309` and `GO:7770061` TOM-TIM22-mediated mitochondrial inner
membrane protein insertion. The same paper also supports
`GO:7770063` beta barrel protein insertion into mitochondrial outer membrane
through VDAC/Por1 beta-hairpin binding and Por1 assembly defects in small-Tim
binding-cleft mutants, but I kept this row non-core because TIM22-directed
carrier delivery remains TIM9's dominant route.

I changed the new ARBA `GO:0070013` intracellular organelle lumen row to
`MODIFY` with `GO:0005758` mitochondrial intermembrane space as the replacement,
because direct and UniProt evidence resolve the location to IMS and make the
ARBA term an unhelpful parent.
