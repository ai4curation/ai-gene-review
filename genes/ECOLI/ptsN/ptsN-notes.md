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


## 2026-11-08 — consistent Ntr/sugar scope and evidence limits

The action discriminator is target evidence, not species labels or donor count: P. putida has a native sugar-independent route and a documented failure of PtsN to replace fructose EIIA; Caulobacter separates its Ntr effectors from sugar permeases and its mannose assignments originate in an incorrect transporter EC mapping. E. coli has measured cross-system phosphate exchange in vitro but lacks demonstrated native sugar-uptake participation for the Ntr branch, so physiological process assignment is over-annotation rather than an absolute negative. Bona fide E. coli/Bacillus HPr controls retain the sugar process because they feed sugar-specific EIIA proteins in the native carbohydrate route; common ancestry at PTN002135312 does not erase this functional divergence.

Where the only localization assertion is ARBA-derived, compartment adjudication remains UNDECIDED and the core location is omitted. PtsN–KdpD target interaction plus regulatory output supports direction-neutral regulator inference without claiming an isolated kinase assay. Source annotation payloads are unchanged.


## 2026-11-11 — target-specific cross-system evidence

Domain ancestry and in-vitro exchange with carbohydrate proteins are real, but do not alone demonstrate native coupled sugar uptake by the Ntr effector. PtsN regulates other proteins, including potassium transporters and KdpD. A physiological sugar-transport contribution cannot be established or excluded from those results. Demonstrated cross-system chemistry involving this target supports MARK_AS_OVER_ANNOTATED, while native sugar transport remains unestablished.


## 2026-11-11 — incoming main journal retained

The following is the incoming review journal; current target-specific adjudication follows below.

# ptsN / EIIA(Ntr) (E. coli K-12, P69829) notes

## Provenance

- Deep research could not be generated: no deep-research provider API key is
  configured in this session, so `just deep-research ECOLI ptsN` was not run and no
  `-deep-research-*.md` file exists. The review is based on the UniProt record, the
  GOA table and the cached publications PMID:7876255, PMID:17289841, PMID:19400808
  (abstracts), PMID:18304323 and PMID:24561554 (full text).

## Findings

- Dephosphorylated IIA(Ntr) binds TrkA and limits K+ accumulation [PMID:17289841
  "We demonstrate that dephosphorylated EIIA(Ntr), but not its phosphorylated form,
  forms a tight complex with TrkA that inhibits the accumulation of high
  intracellular concentrations of K(+)."].
- IIA(Ntr) binds KdpD and stimulates its kinase activity [PMID:19400808 "Two-hybrid
  data and biochemical analysis revealed that IIA(Ntr) interacts with sensor kinase
  KdpD and stimulates kinase activity, resulting in increased levels of
  phosphorylated response regulator KdpE."].
- In P. putida the PtsN-KdpD interaction represses kdpFABC (PMID:26224366, see the
  PSEPK ptsN review), so the direction of KdpD regulation is lineage-dependent.

## Curation decisions

- InterPro2GO maps IPR006320 (PTS_Nitro_regul, the nitrogen-regulatory IIA family
  itself) to sugar-PTS terms; both rows are removed and recorded as source defects.
- enzyme inhibitor activity (TrkA) is refined to transporter inhibitor activity:
  TrkA is the regulatory subunit of a K+ transporter, not an enzyme.
- The bare protein-binding rows are replaced by the regulatory activities each paper
  shows; the large-scale yeast two-hybrid row (PMID:24561554) is removed.


## 2026-11-11 — reconcile merged parallel PTS review

Retain target-specific cross-system judgments and assay limits from this audit. Incorporate incoming experimentally coded proposals and retire their historical TAS predecessors in place where present. Incoming source-defect records are retained when consistent with the current action; broad sugar-process rejection is superseded where direct target cross-system chemistry supports over-annotation. Core relay activities and all original machine source rows remain unchanged.


## 2026-11-11 — review follow-up: evidence and source routing

Quote the Discussion inference that FruB delivers phosphate to NPr where that target-specific claim distinguishes NPr from PtsP. Route InterPro2GO and TreeGrafter source defects to INTERPRO and PANTHER respectively, retaining their claims and requested corrections. No annotation payload or action changes.


## 2026-11-11 — separate coupled transporter activity from process scope

Remove the obsolete cross-species BP contrast from the GO:0008982 MF reason. This coupled transmembrane carbohydrate transport/phosphorylation activity remains REMOVE for soluble PtsN effectors, regardless of measured cross-system protein phosphate exchange. The target-specific BP judgments are unchanged.


## Incoming historical review (reconciled below)

# ptsN / EIIA(Ntr) (E. coli K-12, P69829) notes

## Provenance

- Deep research could not be generated: no deep-research provider API key is
  configured in this session, so `just deep-research ECOLI ptsN` was not run and no
  `-deep-research-*.md` file exists. The review is based on the UniProt record, the
  GOA table and the cached publications PMID:7876255, PMID:17289841, PMID:19400808
  (abstracts), PMID:18304323 and PMID:24561554 (full text).

## Findings

- Dephosphorylated IIA(Ntr) binds TrkA and limits K+ accumulation [PMID:17289841
  "We demonstrate that dephosphorylated EIIA(Ntr), but not its phosphorylated form,
  forms a tight complex with TrkA that inhibits the accumulation of high
  intracellular concentrations of K(+)."].
- IIA(Ntr) binds KdpD and stimulates its kinase activity [PMID:19400808 "Two-hybrid
  data and biochemical analysis revealed that IIA(Ntr) interacts with sensor kinase
  KdpD and stimulates kinase activity, resulting in increased levels of
  phosphorylated response regulator KdpE."].
- In P. putida the PtsN-KdpD interaction represses kdpFABC (PMID:26224366, see the
  PSEPK ptsN review), so the direction of KdpD regulation is lineage-dependent.

## Curation decisions

- InterPro2GO maps IPR006320 (PTS_Nitro_regul, the nitrogen-regulatory IIA family
  itself) to sugar-PTS terms; both rows are removed and recorded as source defects.
- enzyme inhibitor activity (TrkA) is refined to transporter inhibitor activity:
  TrkA is the regulatory subunit of a K+ transporter, not an enzyme.
- The bare protein-binding rows are replaced by the regulatory activities each paper
  shows; the large-scale yeast two-hybrid row (PMID:24561554) is removed.


## 2026-11-13 — integrate the reviewed nitrogen-PTS audit

Preserve all machine annotation payloads and the approved branch decisions. Compatible incoming positive quotations are retained without duplicate nested quotations. For ECOLI PtsI, the native carbohydrate EI-HPr-NagE pathway supports the existing non-core N-acetylglucosamine claim despite the broader family node also covering non-carbohydrate EI(Ntr); homodimerization remains the functional enzyme assembly. For ECOLI PtsN and PtsP, preferred regulatory partners and parallel-chain evidence do not prove every cross-system contribution absent; the conservative MARK_AS_OVER_ANNOTATED sugar-process assessment supersedes incoming universal deletion language. PtsN kinase activation retains its specific biochemical refinement of the KdpD interaction. PSEPK PtsP retains the target-specific distinction between FruB-to-NPr cross talk and PtsP function, and the unverified localization remains UNDECIDED. Incoming questions are preserved, while stronger claims unsupported by the target evidence are not adopted. Cached full-text publications are retained byte-for-byte from the audit branch.
