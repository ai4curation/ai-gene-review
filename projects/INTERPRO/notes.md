---
title: "InterPro mapping review — historical notes"
autolink_gene_symbols: false
---

Historical session notes for the [InterPro mapping review](../INTERPRO.md). These preserve the original chronology and provisional interpretations; consult the project page and linked mapping set for the current summary.


## 2026-06-20

**Project creation.** Scoped the InterPro2GO (`GO_REF:0000002`) review. Built the
extractor and the per-entry priority worklist from all 2732 reviewed genes: 3652
InterPro2GO annotations, 47% flagged suspect across 1826 InterPro entries. Broad
domain/superfamily signatures dominate the suspect list (protein kinase domain, P450,
Cu/Zn SOD, GPCR), confirming the "fold ≠ function" failure mode as the main driver.

**Closed the PANTHER-vs-InterPro deep-research gap.** Gene deep research is a generated
process (`just deep-research-<provider>`); there was no equivalent for the InterPro
entries behind InterPro2GO annotations. Added the InterPro-family analogue —
`templates/interpro_family_research.md`, `scripts/deep_research_interpro_family.py`, and
the `just deep-research-interpro-family <IPR> [provider]` recipe (provider defaults to
`falcon`/Edison) — so families are researched by the same generated pipeline (output:
`interpro/<db>/<ID>/<ID>-deep-research-<provider>.md`), with `IPR000719` cached as a
seed.

**Batch 2 + first proposed new mapping.** Researched 6 more families; 3 grounded cleanly
(Radical SAM, Ras-type small GTPase, MADS-box) and are in the SSSOM (now 25 mappings).
Notable findings:

- **Genericity ≠ wrongness (Radical SAM, IPR007197).** I predicted the MF *root* term
  `catalytic activity` would be a REMOVE. The research says **ACCEPT**: because the
  superfamily catalyzes >100 mechanistically different reactions, the *only* universally
  true MF really is "is an enzyme", so the maximally generic term is the correct
  family-level annotation — replacing it with anything more specific would over-annotate.
- **First annotation-gain proposal (Ras-type, IPR020849).** The entry maps `GTP binding`
  but not `GTPase activity` (GO:0003924), even though the GTP-hydrolysis machinery
  (P-loop, Switch II/Gln61, Mg²⁺) is universal — so we **propose ADDING** it (an
  `exactMatch` row, flagged for curator confirmation since intrinsic hydrolysis is
  GAP-accelerated).
- **Domain-intrinsic vs whole-protein (MADS-box, IPR002100).** I expected to *add*
  `DNA-binding TF activity`; the research argues against it — the MADS domain provides
  DNA binding + dimerization, but being a transcription factor is a whole-protein
  property (K/C domains, complex context), so adding it would over-annotate the domain.
- **QC catch.** 3 of the 6 runs (sigma-54, pseudouridine synthase, GAPDH) silently
  returned **ungrounded** reports (exit 0, file written, but "no contexts were retrieved
  … not grounded in evidence", zero real citations) — likely Edison retrieval throttling
  under 6-way parallel load. A sequential re-run **also** failed fast (~3 s each, no
  retrieval), so this is a transient Edison retrieval-backend outage, not a load issue —
  these 3 entries are **deferred** (metadata cached) for re-running when the backend
  recovers. Excluded from the SSSOM. (Detect with: grep for "no contexts were retrieved"
  or `citation_count`/zero real refs — a groundedness guard worth adding to the wrapper.)

**Batch 1 of family deep research (falcon/Edison).** Ran five more top entries: P450
(`IPR001128`), Cu/Zn SOD (`IPR001424`), GPCR Class A (`IPR000276`), NRAMP/SLC11
(`IPR001046`), and DnaJ (`IPR012724`). See the verdict table under Workstream 2. A
recurring, independently-reached pattern: cofactor/binding terms (`heme binding`, `metal
ion binding`) and broad transport terms hold family-wide, but **whole-protein activity
and process terms attached to a structural module over-annotate** — most sharply for
IPR012724, where Edison flags `ATP binding` as factually wrong on DnaJ (the Hsp70 partner
binds ATP), and for IPR001424, where `superoxide metabolic process` mis-annotates
copper-chaperone members that do not dismutate.
