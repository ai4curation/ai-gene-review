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


## 2026-11-11 — incoming main journal retained

The following is the incoming review journal; current target-specific adjudication follows below.

# ptsP (E. coli K-12, P37177) notes

## Provenance

- Deep research could not be generated for this review: no deep-research provider
  API key (Perplexity, OpenAI, FutureHouse/Falcon) is configured in this session, so
  `just deep-research ECOLI ptsP` was not run. The review is based on the UniProt
  record, the GOA table, and the cached publications listed below. No
  `-deep-research-*.md` file was written.
- Publications read: PMID:10473571 (abstract), PMID:23517463 (full text),
  PMID:19400808 (abstract), PMID:18296519 (full text, P. putida ortholog context).

## Findings

- EI(Ntr) is the GAF-domain paralogue of enzyme I. Purified EI(Ntr) phosphorylates
  NPr from PEP and does not phosphorylate HPr [PMID:10473571 "EI(Ntr) phosphorylated
  NPr but not HPr, whereas Enzyme I exhibited a strong preference for HPr."].
- Glutamine and 2-oxoglutarate act on EI(Ntr) autophosphorylation through the GAF
  domain [PMID:23517463 "glutamine and α-ketoglutarate, the canonical signals of
  nitrogen availability, reciprocally regulate the phosphorylation state of the
  PTS(Ntr) by direct effects on enzyme I(Ntr) autophosphorylation"].
- The EI(Ntr)-NPr-IIA(Ntr) chain works in parallel to the sugar transport PTS
  [PMID:19400808 "Proteins EI(Ntr), NPr and IIA(Ntr) form a phosphoryl group transfer
  chain (Ntr-PTS) working in parallel to the phosphoenolpyruvate:carbohydrate
  phosphotransferase system (transport-PTS) in Escherichia coli."].

## Curation decisions

- The sugar PTS (GO:0009401) InterPro2GO row and the N-acetylglucosamine transport
  IBA are removed: EI(Ntr) does not feed sugar transport, and the NAG term was placed
  on the root PAINT node from a single P. aeruginosa multiphosphoryl transfer protein
  seed (PA3760, Q9HXN5).
- The broad phosphorus-group transferase row is refined to GO:0008965.


## 2026-11-11 — reconcile merged parallel PTS review

Retain target-specific cross-system judgments and assay limits from this audit. Incorporate incoming experimentally coded proposals and retire their historical TAS predecessors in place where present. Incoming source-defect records are retained when consistent with the current action; broad sugar-process rejection is superseded where direct target cross-system chemistry supports over-annotation. Core relay activities and all original machine source rows remain unchanged.


## Incoming historical review (reconciled below)

# ptsP (E. coli K-12, P37177) notes

## Provenance

- Deep research could not be generated for this review: no deep-research provider
  API key (Perplexity, OpenAI, FutureHouse/Falcon) is configured in this session, so
  `just deep-research ECOLI ptsP` was not run. The review is based on the UniProt
  record, the GOA table, and the cached publications listed below. No
  `-deep-research-*.md` file was written.
- Publications read: PMID:10473571 (abstract), PMID:23517463 (full text),
  PMID:19400808 (abstract), PMID:18296519 (full text, P. putida ortholog context).

## Findings

- EI(Ntr) is the GAF-domain paralogue of enzyme I. Purified EI(Ntr) phosphorylates
  NPr from PEP and does not phosphorylate HPr [PMID:10473571 "EI(Ntr) phosphorylated
  NPr but not HPr, whereas Enzyme I exhibited a strong preference for HPr."].
- Glutamine and 2-oxoglutarate act on EI(Ntr) autophosphorylation through the GAF
  domain [PMID:23517463 "glutamine and α-ketoglutarate, the canonical signals of
  nitrogen availability, reciprocally regulate the phosphorylation state of the
  PTS(Ntr) by direct effects on enzyme I(Ntr) autophosphorylation"].
- The EI(Ntr)-NPr-IIA(Ntr) chain works in parallel to the sugar transport PTS
  [PMID:19400808 "Proteins EI(Ntr), NPr and IIA(Ntr) form a phosphoryl group transfer
  chain (Ntr-PTS) working in parallel to the phosphoenolpyruvate:carbohydrate
  phosphotransferase system (transport-PTS) in Escherichia coli."].

## Curation decisions

- The sugar PTS (GO:0009401) InterPro2GO row and the N-acetylglucosamine transport
  IBA are removed: EI(Ntr) does not feed sugar transport, and the NAG term was placed
  on the root PAINT node from a single P. aeruginosa multiphosphoryl transfer protein
  seed (PA3760, Q9HXN5).
- The broad phosphorus-group transferase row is refined to GO:0008965.


## 2026-11-13 — integrate the reviewed nitrogen-PTS audit

Preserve all machine annotation payloads and the approved branch decisions. Compatible incoming positive quotations are retained without duplicate nested quotations. For ECOLI PtsI, the native carbohydrate EI-HPr-NagE pathway supports the existing non-core N-acetylglucosamine claim despite the broader family node also covering non-carbohydrate EI(Ntr); homodimerization remains the functional enzyme assembly. For ECOLI PtsN and PtsP, preferred regulatory partners and parallel-chain evidence do not prove every cross-system contribution absent; the conservative MARK_AS_OVER_ANNOTATED sugar-process assessment supersedes incoming universal deletion language. PtsN kinase activation retains its specific biochemical refinement of the KdpD interaction. PSEPK PtsP retains the target-specific distinction between FruB-to-NPr cross talk and PtsP function, and the unverified localization remains UNDECIDED. Incoming questions are preserved, while stronger claims unsupported by the target evidence are not adopted. Cached full-text publications are retained byte-for-byte from the audit branch.
