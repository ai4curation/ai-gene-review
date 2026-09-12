# TIM10 review notes

## 2026-08-28 completion audit

- TIM10 is a small-Tim mitochondrial intermembrane-space chaperone. Its core
  activity is best represented by GO:0140309, unfolded protein holdase activity
  (the current official label; “unfolded protein carrier activity” is an exact synonym):
  the reconstituted Tim9-Tim10 complex “bound to the physiological substrate
  ADP/ATP carrier and displayed chaperone activity in refolding the model
  substrate firefly luciferase” [PMID:12138093]. This supports directed client
  shielding and delivery, not membrane insertase activity.

- The two direct GO:0140318 protein-transporter rows remain ACCEPT and are
  represented as a second core function. GO:0140309 captures the substrate-state-
  specific holdase behavior (maintaining hydrophobic clients without aggregation),
  whereas GO:0140318 records directed delivery between TOM-side intermediates and
  the TIM22 pathway. These claims overlap but emphasize experimentally supported
  mechanistic dimensions rather than contradicting one another.

- All 34 physical GOA rows are represented by 34 review entries. When grouped only
  by term, evidence, reference, and qualifier they comprise 33 signatures; the sole
  repeated signature is the pair of GO:0005515 / IPI / PMID:27107014 / `enables`
  rows distinguished by their WITH/FROM human partners. Five generic protein-binding
  rows are retained as over-annotated interaction statements, while the two intentional
  cross-species human-partner rows are removed as nonphysiological yeast annotations;
  the informative biology is captured by Tim9-Tim10 chaperone-complex membership,
  TIM22-pathway participation, and unfolded-protein carrier activity.

- All three IBA rows use PTN000113167. Current cached PAINT retains the
  GO:0042721 complex-membership and GO:0045039 inner-membrane-insertion-process
  IBDs. Their WITH/FROM seeds are conserved small-Tim/TIM22-pathway components,
  including TIM12 (`SGD:S000000295`), the target TIM10
  (`SGD:S000003530`), human TIMM10 (`UniProtKB:P62072`), and orthologous mouse
  and worm sources for the process term. Target-in-own-WITH/FROM is valid
  experimental grounding, not circularity.

- GOA also carries GO:0032977 membrane insertase activity from PTN000113167 and
  human TIMM10, but that assertion is absent from the current cached PAINT table.
  It also conflates the small-Tim delivery role with the membrane-embedded Tim22
  insertase. The row is therefore modified to GO:0140309 and recorded as stale
  PAINT provenance plus role conflation. Direct work instead states that Tim10
  transports carrier precursors while Tim12/Tim22 mediate insertion
  [PMID:9430585, “Tim10p readily dissociated from the complex and was required
  to transport carrier precursors across the outer membrane; Tim12p was firmly
  bound to Tim22p and mediated the insertion of carriers into the inner
  membrane.”].

- Metal and zinc binding are retained as non-core. The reduced twin-CX3C motif
  can bind zinc [PMID:9495346, “Both proteins contain a zinc-finger-like motif
  with four cysteines and bind equimolar amounts of zinc ions.”], whereas the
  mature IMS protein uses those cysteines in intramolecular disulfide bonds.

- PMID:19037698 is a verified wrong identifier for the ComplexPortal IMS row:
  its cached full text concerns colorectal anastomotic leakage. The biological
  localization is independently established by multiple TIM10 papers, so the
  annotation is accepted while the reference is explicitly marked
  `WRONG_IDENTIFIER`; PMID:19037098 is the plausible transposed identifier.

- PMID:23267104 is also a verified wrong identifier for its TIM10-TIM12 IPI row.
  Full-text inspection found an E. coli-only study with no yeast, Tim10, or Tim12
  mention. The physiological TIM10-TIM12 association is independently supported,
  but this citation cannot support the generic interaction row.

- PMID:12637749 is abstract-only. Its abstract supports the TIM22 complex as a
  twin-pore translocase but does not name Tim10, Tim18, or their partner-level IPI,
  so no title or non-supporting abstract sentence was used as evidence for that row.

- Thirteen of the sixteen cached PMID records are abstract-only. The only cached
  full texts are the unrelated PMID:19037698 paper, PMID:23267104, and
  PMID:27107014. Experimental annotations were not rejected merely because assay
  detail was unavailable from an abstract.
