# Escherichia coli ptsI review notes

## 2026-11-07

P08839 belongs to PTHR46244:SF6 alongside alpha-lineage PtsP candidates. Its proven native role is carbohydrate EI, so SF6 alone cannot grant the nitrogen-relay entry role. Curated UniProt also records less-efficient phosphorylation of NPr in vitro (PMID:7876255); this is biochemical cross-talk and does not prove a native canonical PtsP relay. Polar localization is regulation of a soluble enzyme, not evidence for a membrane transporter.

All 17 original machine annotation payloads, qualifiers and supporting entities remain in order. Only their review sections are changed, with no NEW rows. Generic protein-binding removals follow the repository exception and do not deny experimentally observed interactions. Broad terms are refined to the specific supported descendants; precise but substrate-specific context is treated separately from the general catalytic activity.

Primary evidence was inspected in the canonical publication caches. Accessible abstracts constrain detailed assay claims: bibliographic-only PMID:5545082 is not treated as a newly inspected experiment, and complexomic abstracts do not identify every protein in their supplementary results. Existing experimental curators are not overruled on that basis. Native biochemical and structural results independently ground the major functions.

Current official GO definitions were checked for authored activities. The shared Falcon module-research request failed HTTP403 authentication; direct evidence assessment was used and no provider report was fabricated. Full corpus and module-level validation remain separate integration gates.


## Incoming historical review (reconciled below)

# ptsI (enzyme I, P08839) notes

Reviewed 2026-11-11 as the enzyme I partner of FPr in the split-relay variant of the
generic fructose PTS module (`modules/fructose_pts_uptake_and_catabolism.yaml`).

Deep research: no provider deep-research file was generated for this gene in this
session; the review rests on the cached publications (abstract-only) and the UniProt
record, whose function, kinetics and location lines cite experimental papers.

- Core: PEP-protein phosphotransferase activity (EC 2.7.3.9) [PMID:12705838
  "EI(C502A) is 10 000 times less active than wild-type EI [EI(wt)] with PEP as the
  substrate"]; dimeric three-domain structure [PMID:17053069].
- All bare protein-binding IPI rows (HPr, BglG, TmaR) removed per policy.
- GO:0015764 N-acetylglucosamine transport marked as over-annotation: true in principle
  for the general enzyme I, but the comparator HPr (P0AA04) carries only GO:0009401 and no
  sugar-specific transport term in GOA (QuickGO query, 2026-11-11), and the node is rated
  TOO_DEEP in the PTHR46244 family review. Same action as Xanthomonas FruB; EI(Ntr) PtsP
  removes it because EI(Ntr) is not a sugar-PTS enzyme.
- Cytoplasm rows refined to cytosol (HDA cytosolic fraction), following E. coli ptsN.


## 2026-11-13 — integrate the reviewed nitrogen-PTS audit

Preserve all machine annotation payloads and the approved branch decisions. Compatible incoming positive quotations are retained without duplicate nested quotations. For ECOLI PtsI, the native carbohydrate EI-HPr-NagE pathway supports the existing non-core N-acetylglucosamine claim despite the broader family node also covering non-carbohydrate EI(Ntr); homodimerization remains the functional enzyme assembly. For ECOLI PtsN and PtsP, preferred regulatory partners and parallel-chain evidence do not prove every cross-system contribution absent; the conservative MARK_AS_OVER_ANNOTATED sugar-process assessment supersedes incoming universal deletion language. PtsN kinase activation retains its specific biochemical refinement of the KdpD interaction. PSEPK PtsP retains the target-specific distinction between FruB-to-NPr cross talk and PtsP function, and the unverified localization remains UNDECIDED. Incoming questions are preserved, while stronger claims unsupported by the target evidence are not adopted. Cached full-text publications are retained byte-for-byte from the audit branch.
