# E. coli ptsP: native nitrogen-PTS review

2026-11-07. All seeded annotation payloads and order are retained; every review decision was manually assigned. No NEW annotation was added. Core functions synthesize the demonstrated role and are not additional machine annotation rows.

PtsP (enzyme I-Ntr) is the soluble phosphoenolpyruvate-dependent entry enzyme of the E. coli nitrogen-regulatory PTS. It transfers phosphate through its phosphohistidine intermediate to NPr/PtsO, which passes it to the PtsN regulatory effector. Its N-terminal GAF domain couples this relay to glutamine and alpha-ketoglutarate: in the characterized E. coli system glutamine inhibits and alpha-ketoglutarate stimulates PtsP autophosphorylation. The relay regulates protein targets rather than constituting a sugar-specific membrane uptake complex.

The native reference relay is PtsP(P37177) → NPr/PtsO(P0A9N0) → PtsN(P69829). PMID10473571 and PMID7876255 have explicit positive biochemical abstracts, while PMID23517463 provides full primary entry-enzyme regulation and downstream reporter context. Reversible purified exchange is not a measured native bypass flux. No Pseudomonas FruB bypass, AceE inhibition, or Caulobacter SpoT result is transferred to E. coli.

Current official GO definitions are archived in analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107/go-terms.json. GO0016775 captures a nitrogenous acceptor without requiring ATP. Generic kinase is not rejected merely because its definition says usually ATP. GO0141110 specifies transporter inhibition; TrkA/KdpD/YcgO outputs are kept chemically and experimentally distinct.

PAINT raw IBD assertions were read. A self-source at a target-supported IBD is legitimate experimental grounding. Actual PANTHER tree ancestry was subsequently retrieved and joined to the cached IBD assertions in analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107/paint-join.json. All three E. coli target leaves descend from their asserted nodes; cached slices contain no negative rows. Sugar-process uncertainty concerns physiological function within those broad clades, not missing ancestry, donor counts or an invented loss. No MSA residue-loss inference was performed. The family-based control PtsI and carbohydrate HPr do not automatically become native nitrogen-relay members.

The shared real Falcon attempt failed HTTP403 authentication, recorded under analysis/module_audits/bacterial_nitrogen_regulatory_pts/acquisition-20261107/module-falcon-attempt.json and .log. These notes are manual research, not fabricated provider output. No duplicate provider attempt was requested.

## Source-specific findings and access limits

- PMID:10473571 — Enzyme I(Ntr) from Escherichia coli. A novel enzyme of the phosphoenolpyruvate-dependent phosphotransferase system exhibiting strict specificity for its phosphoryl acceptor, NPr.. Abstract-only; positive purified reaction and specificity are explicit. Detailed donor strain, all constructs and kinetic interpretation were not independently recovered.
  Purified E. coli PtsP phosphorylates NPr from PEP. Supporting source text: "EI(Ntr) was shown to phosphorylate NPr in vitro using either a [(32)P]PEP-dependent protein phosphorylation assay or a quantitative sugar phosphorylation assay."

- PMID:23517463 — Reciprocal regulation of the autophosphorylation of enzyme INtr by glutamine and α-ketoglutarate in Escherichia coli.. Full text read. Direct entry-enzyme assays are distinguished from downstream K75D PtsN mobility-shift reporter measurements and GAF-deletion constructs.
  E. coli glutamine and alpha-ketoglutarate regulate PtsP autophosphorylation in opposite directions. Supporting source text: "Autophosphorylation by [32P]PEP of EINtr is inhibited by glutamine (Fig. 5A) and stimulated by α–ketoglutarate (Fig. 5B)."

- PMID:41870250 — Bacterial nitrogen-related phosphotransferase systems: new insights into diverse roles in virulence, physiology, and central metabolism.. Full 2026 review read as mechanistic synthesis and source discovery, not a new target experiment or universal family-output grant.
  The regulatory PTS is distinguished from the coupled sugar-uptake machinery. Supporting source text: "Instead of a sugar substrate, the PTSNtr appears to carry out its regulatory roles through protein-protein interactions that primarily involve PtsN, although relatively few PtsN protein targets have been characterized."

- PMID:7876255 — Novel proteins of the phosphotransferase system encoded within the rpoN operon of Escherichia coli. Enzyme IIANtr affects growth on organic nitrogen and the conditional lethality of an erats mutant.. Abstract-only. Positive exchange is explicit; do not infer physiological bypass dominance or a complete membrane transport reaction.
  Purified NPr and PtsN exchange phosphate with carbohydrate-PTS components. Supporting source text: "Purified IIANtr and NPr exchange phosphate appropriately with Enzyme I, HPr, and Enzyme IIA proteins of the phosphoenolpyruvate: sugar phosphotransferase system."


## 2026-11-08 — consistent Ntr/sugar scope and evidence limits

The action discriminator is target evidence, not species labels or donor count: P. putida has a native sugar-independent route and a documented failure of PtsN to replace fructose EIIA; Caulobacter separates its Ntr effectors from sugar permeases and its mannose assignments originate in an incorrect transporter EC mapping. E. coli has measured cross-system phosphate exchange in vitro but lacks demonstrated native sugar-uptake participation for the Ntr branch, so physiological process assignment is over-annotation rather than an absolute negative. Bona fide E. coli/Bacillus HPr controls retain the sugar process because they feed sugar-specific EIIA proteins in the native carbohydrate route; common ancestry at PTN002135312 does not erase this functional divergence.

Where the only localization assertion is ARBA-derived, compartment adjudication remains UNDECIDED and the core location is omitted. PtsN–KdpD target interaction plus regulatory output supports direction-neutral regulator inference without claiming an isolated kinase assay. Source annotation payloads are unchanged.


## 2026-11-10 — phosphate-flow direction and propagation status

The P. putida NPr/EINtr sugar-process assignment is over-annotated in light of real in vivo FruB-to-Ntr cross talk, without borrowing the PtsN-specific negative replacement assay. E. coli EINtr GlcNAc rejection now has propagation metadata matching its measured acceptor-specificity argument. Original annotation payloads are unchanged.


## 2026-11-11 — target-specific cross-system evidence

The domain mapping joins a regulatory relay enzyme to the coupled carbohydrate uptake process. Native PtsP preferentially serves NPr, but in-vitro coupling assays and exchange between PTS components preclude using specialization as proof that all sugar-related participation is impossible. A target-specific physiological sugar-transport role is not established by the present evidence. Demonstrated cross-system chemistry involving this target supports MARK_AS_OVER_ANNOTATED, while native sugar transport remains unestablished.
