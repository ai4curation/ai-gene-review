# lptA (Q88P98) notes

P. putida KT2440 lptA is the orthologue of E. coli K-12 lptA (both in PANTHER PTHR36504:SF1).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptA/lptA-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `May form a bridge between the inner membrane and the outer membrane, via interactions with LptC and LptD, thereby facilitating LPS transfer across the periplasm.`
- `Required for the translocation of LPS from the inner membrane to the outer membrane.`
- `SUBCELLULAR LOCATION: Periplasm`
- `TIGR03002; outer_YhbN_LptA`

## E. coli literature cited

- PMID:17056748, PMID:18424520, PMID:18480051, PMID:20446753, PMID:20720015, PMID:22668317, PMID:29449493

## Decisions in this review

- GO:0001530 lipopolysaccharide binding (IEA): ACCEPT.
- GO:0009279 cell outer membrane (IEA): KEEP_AS_NON_CORE.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0017089 glycolipid transfer activity (IEA): MODIFY to GO:0140332 lipopolysaccharide transfer activity.
- GO:0030288 outer membrane-bounded periplasmic space (IEA): ACCEPT.
- GO:0042597 periplasmic space (IEA): MODIFY to GO:0030288 outer membrane-bounded periplasmic space.
- GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly (IEA): ACCEPT.
- GO:0046836 glycolipid transport (IEA): MODIFY to GO:0015920 lipopolysaccharide transport.
- Core function: enables GO:0140332 lipopolysaccharide transfer activity; processes GO:0015920, GO:0043165.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).

## 2026-11-07 independent LPS module consultation

All 8 original ordered annotation rows were reviewed. Their machine payloads, actions and historical NEW lifecycle are retained; no new annotation was added. The prior note about no provider attempt is historical: an actual Falcon run now failed HTTP 403, archived under `.cache/module-audit-logs/lps-20261107/psepk-consultation/falcon-lptA.log`; no provider report was fabricated.

PAINT-loss traversal could not be resolved because the exact KT2440 accession is absent from the cached family tree. The tool footer is not evidence of an independently established absence of loss. These original rows are IEA (and retained historical ISO proposals for LptD/E), not IBA.

KT2440 biological roles are inferred from its own specialized signatures and curated rule-supported statements plus source-scoped homolog experiments. P. aeruginosa PAO1-LAC structures and heterologous expression do not become KT2440 assays. Generic ABC identity is insufficient to specify LPS. The A/C bridge transfer, B ATPase motor, F/G cargo-cavity contributions and D/E outer-membrane translocation are distinct functional claims.

Relevant source findings:

- [PMID:17056748] E. coli LptA/LptB depletion disrupts LPS targeting to the outer membrane. Together with biochemical transfer studies this supports a transport role rather than attributing all envelope phenotypes to direct catalytic activities. Verbatim: "Similar defects are observed in cells in which LptA and LptB are individually depleted (Fig. 6 ), indicating that both proteins are required for LPS targeting to the OM."
- [PMID:18424520] E. coli localization and depletion distinguish cytoplasmic LptB, membrane-anchored LptC and periplasmic LptA within one LPS-assembly pathway. Verbatim: "Thus, we have identified an essential LPS transport component in every cellular compartment: LptB in the cytoplasm, LptC in the IM, LptA in the periplasm, and LptD and LptE in the OM."
- [PMID:18480051] Purified E. coli LptA binds structurally diverse LPS through the lipid A region, directly supporting substrate binding; KT2440 transfer is inferred from specialized family membership and the conserved bridge role. Verbatim: "Here we provide evidence that LptA binds structurally diverse LPS substrates in vitro and demonstrate that it interacts specifically with the lipid A domain of LPS."
- [PMID:20446753] E. coli membrane fractionation and copurification support a trans-envelope Lpt assembly. LptA cofractionation denotes assembled membrane association, not an integral outer-membrane beta-barrel. Verbatim: "Remarkably, LptA was also found to co-fractionate almost exclusively with these OM fractions (Figure 2B)."
- [PMID:20720015] E. coli LptC binds LPS and transfers it directionally to LptA; cysteine-accessibility experiments orient its soluble domain toward the periplasm. Verbatim: "In vitro, LptA can displace lipopolysaccharide from LptC (but not vice versa), consistent with their locations and their proposed placement in a unidirectional export pathway."
- [PMID:22668317] E. coli assembly experiments support domain-to-domain connection of the periplasmic bridge; membrane cofractionation does not make LptA an integral membrane protein. Verbatim: "This protein has been proposed to physically link the IM and the OM because it is the only periplasmic Lpt component without a membrane tether and because it fractionates with both membranes."
- [PMID:29449493] Purified E. coli Lpt components reconstitute ATP-dependent membrane-to-membrane LPS movement. Necessity/sufficiency refers to the tested assembled seven-protein system, not autonomous transport by every component. Verbatim: "Thus, all seven Lpt proteins and ATP are necessary and sufficient for membrane-to-membrane transport to occur."
