# E. coli ptsN: native nitrogen-PTS review

2026-11-07. All seeded annotation payloads and order are retained; every review decision was manually assigned. No NEW annotation was added. Core functions synthesize the demonstrated role and are not additional machine annotation rows.

PtsN (enzyme IIA-Ntr) is the cytosolic terminal phosphoacceptor and regulatory effector of the E. coli PtsP–NPr phosphorelay. Its phosphorylation state controls interactions with potassium-homeostasis proteins. The unphosphorylated form inhibits Trk-mediated potassium uptake through interaction with TrkA, stimulates the sensor kinase KdpD, and inhibits the potassium/proton antiporter YcgO. These partner-specific effects connect metabolic input signals to potassium handling; PtsN is not itself a sugar permease or a KdpD-like kinase.

The native reference relay is PtsP(P37177) → NPr/PtsO(P0A9N0) → PtsN(P69829). PMID10473571 and PMID7876255 have explicit positive biochemical abstracts, while PMID23517463 provides full primary entry-enzyme regulation and downstream reporter context. Reversible purified exchange is not a measured native bypass flux. No Pseudomonas FruB bypass, AceE inhibition, or Caulobacter SpoT result is transferred to E. coli.

Current official GO definitions are archived in analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107/go-terms.json. GO0016775 captures a nitrogenous acceptor without requiring ATP. Generic kinase is not rejected merely because its definition says usually ATP. GO0141110 specifies transporter inhibition; TrkA/KdpD/YcgO outputs are kept chemically and experimentally distinct.

PAINT raw IBD assertions were read. A self-source at a target-supported IBD is legitimate experimental grounding. Actual PANTHER tree ancestry was subsequently retrieved and joined to the cached IBD assertions in analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107/paint-join.json. All three E. coli target leaves descend from their asserted nodes; cached slices contain no negative rows. Sugar-process uncertainty concerns physiological function within those broad clades, not missing ancestry, donor counts or an invented loss. No MSA residue-loss inference was performed. The family-based control PtsI and carbohydrate HPr do not automatically become native nitrogen-relay members.

The shared real Falcon attempt failed HTTP403 authentication, recorded under analysis/module_audits/bacterial_nitrogen_regulatory_pts/acquisition-20261107/module-falcon-attempt.json and .log. These notes are manual research, not fabricated provider output. No duplicate provider attempt was requested.

## Source-specific findings and access limits

- PMID:17289841 — Escherichia coli enzyme IIANtr regulates the K+ transporter TrkA.. Full text read: E. coli K-12/MG1655 interaction, phosphostate and potassium accumulation evidence. Trk transport regulation is distinct from inhibition of a catalytic enzyme.
  Dephosphorylated PtsN inhibits Trk-mediated potassium uptake through TrkA interaction. Supporting source text: "dephosphorylated EIIA Ntr interacts with TrkA, resulting in the inhibition of Trk-mediated K + uptake."

- PMID:18304323 — Protein abundance profiling of the Escherichia coli cytosol.. Full text read; cohort/strain verified. Target-specific supplementary peptide identification was not independently re-extracted.
  The study profiles E. coli MC4100 cytosolic proteins; the target IDA is retained with its curated attribution. Supporting source text: "we identified 1103 proteins from the cytosolic fraction of the Escherichia coli strain MC4100."

- PMID:19400808 — Stimulation of the potassium sensor KdpD kinase activity by interaction with the phosphotransferase protein IIA(Ntr) in Escherichia coli.. Abstract-only, but interaction and biochemical kinase assay are explicitly reported. Positive curator-supported E. coli activation is retained without reconstructing uninspected assay details.
  PtsN interacts with KdpD and increases kinase activity. Supporting source text: "Two-hybrid data and biochemical analysis revealed that IIA(Ntr) interacts with sensor kinase KdpD and stimulates kinase activity, resulting in increased levels of phosphorylated response regulator KdpE."

- PMID:24561554 — The binary protein-protein interaction landscape of Escherichia coli.. Full article describes large-scale binary interaction mapping; do not treat the network as an independent KdpD kinase assay.
  The binary interaction study supports the inherited KdpD interaction assertion; the functional consequence is independently supported by PMID19400808.

- PMID:39742999 — Interaction of unphosphorylated PtsN with the K(+)/H(+) antiporter YcgO inhibits its activity in Escherichia coli.. Full text read. Native K-12 genetic context, overexpressed-protein copurification and everted-vesicle antiport are distinguished; a detailed CorC/RCK activation mechanism remains a model.
  E. coli YcgO antiport is measured in everted vesicles, separately from PtsN binding/phosphostate experiments. Supporting source text: "Copurification studies show that unphospho-PtsN specifically interacts with YcgO, and phosphorylation of PtsN leads to marked attenuation of the interaction."

- PMID:41870250 — Bacterial nitrogen-related phosphotransferase systems: new insights into diverse roles in virulence, physiology, and central metabolism.. Full 2026 review read as mechanistic synthesis and source discovery, not a new target experiment or universal family-output grant.
  The regulatory PTS is distinguished from the coupled sugar-uptake machinery. Supporting source text: "Instead of a sugar substrate, the PTSNtr appears to carry out its regulatory roles through protein-protein interactions that primarily involve PtsN, although relatively few PtsN protein targets have been characterized."

- PMID:7876255 — Novel proteins of the phosphotransferase system encoded within the rpoN operon of Escherichia coli. Enzyme IIANtr affects growth on organic nitrogen and the conditional lethality of an erats mutant.. Abstract-only. Positive exchange is explicit; do not infer physiological bypass dominance or a complete membrane transport reaction.
  Purified NPr and PtsN exchange phosphate with carbohydrate-PTS components. Supporting source text: "Purified IIANtr and NPr exchange phosphate appropriately with Enzyme I, HPr, and Enzyme IIA proteins of the phosphoenolpyruvate: sugar phosphotransferase system."
