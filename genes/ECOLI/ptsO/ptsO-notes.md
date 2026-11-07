# E. coli ptsO: native nitrogen-PTS review

2026-11-07. All seeded annotation payloads and order are retained; every review decision was manually assigned. No NEW annotation was added. Core functions synthesize the demonstrated role and are not additional machine annotation rows.

PtsO (NPr) is a soluble histidine phosphocarrier in the E. coli nitrogen-regulatory PTS. It receives phosphate from PtsP and transfers it to a histidine in PtsN, coupling the PEP-fed entry reaction to phosphostate-dependent regulatory outputs. Phosphate exchange with carbohydrate-PTS proteins has also been demonstrated in vitro. Dephosphorylated NPr interacts with the lipid A biosynthetic enzyme LpxD, linking its phosphostate to an additional regulatory output whose catalytic mechanism is less directly established than the relay.

The native reference relay is PtsP(P37177) → NPr/PtsO(P0A9N0) → PtsN(P69829). PMID10473571 and PMID7876255 have explicit positive biochemical abstracts, while PMID23517463 provides full primary entry-enzyme regulation and downstream reporter context. Reversible purified exchange is not a measured native bypass flux. No Pseudomonas FruB bypass, AceE inhibition, or Caulobacter SpoT result is transferred to E. coli.

Current official GO definitions are archived in analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107/go-terms.json. GO0016775 captures a nitrogenous acceptor without requiring ATP. Generic kinase is not rejected merely because its definition says usually ATP. GO0141110 specifies transporter inhibition; TrkA/KdpD/YcgO outputs are kept chemically and experimentally distinct.

PAINT raw IBD assertions were read. A self-source at a target-supported IBD is legitimate experimental grounding. Actual PANTHER tree ancestry was subsequently retrieved and joined to the cached IBD assertions in analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107/paint-join.json. All three E. coli target leaves descend from their asserted nodes; cached slices contain no negative rows. Sugar-process uncertainty concerns physiological function within those broad clades, not missing ancestry, donor counts or an invented loss. No MSA residue-loss inference was performed. The family-based control PtsI and carbohydrate HPr do not automatically become native nitrogen-relay members.

The shared real Falcon attempt failed HTTP403 authentication, recorded under analysis/module_audits/bacterial_nitrogen_regulatory_pts/acquisition-20261107/module-falcon-attempt.json and .log. These notes are manual research, not fabricated provider output. No duplicate provider attempt was requested.

## Source-specific findings and access limits

- PMID:10473571 — Enzyme I(Ntr) from Escherichia coli. A novel enzyme of the phosphoenolpyruvate-dependent phosphotransferase system exhibiting strict specificity for its phosphoryl acceptor, NPr.. Abstract-only; positive purified reaction and specificity are explicit. Detailed donor strain, all constructs and kinetic interpretation were not independently recovered.
  Purified E. coli PtsP phosphorylates NPr from PEP. Supporting source text: "EI(Ntr) was shown to phosphorylate NPr in vitro using either a [(32)P]PEP-dependent protein phosphorylation assay or a quantitative sugar phosphorylation assay."

- PMID:21605551 — Dephosphorylated NPr of the nitrogen PTS regulates lipid A biosynthesis by direct interaction with LpxD.. Abstract-only; direct interaction is explicit, but the proposed catalytic inhibition mechanism is not promoted to an independently verified purified enzyme assay.
  Dephosphorylated NPr interacts with E. coli LpxD. Supporting source text: "dephosphorylated NPr of the nitrogen PTS interacts with Escherichia coli LpxD which catalyzes biosynthesis of lipid A of the lipopolysaccharide (LPS) layer."

- PMID:7876255 — Novel proteins of the phosphotransferase system encoded within the rpoN operon of Escherichia coli. Enzyme IIANtr affects growth on organic nitrogen and the conditional lethality of an erats mutant.. Abstract-only. Positive exchange is explicit; do not infer physiological bypass dominance or a complete membrane transport reaction.
  Purified NPr and PtsN exchange phosphate with carbohydrate-PTS components. Supporting source text: "Purified IIANtr and NPr exchange phosphate appropriately with Enzyme I, HPr, and Enzyme IIA proteins of the phosphoenolpyruvate: sugar phosphotransferase system."
