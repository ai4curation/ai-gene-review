# lptE (Q88DN0) notes

P. putida KT2440 lptE is the orthologue of E. coli K-12 lptE (both in PANTHER PTHR38098:SF1).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptE/lptE-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `Binds LPS and may serve as the LPS recognition site at the outer membrane.`
- `Interacts with LptD.`
- `PF04390; LptE`
- `Required for the proper assembly of LptD.`
- `SUBCELLULAR LOCATION: Cell outer membrane`

## E. coli literature cited

- PMID:16861298, PMID:20203010, PMID:21257904, PMID:21257909, PMID:24938785, PMID:29449493

## Decisions in this review

- GO:0001530 lipopolysaccharide binding (IEA): ACCEPT.
- GO:0009279 cell outer membrane (IEA): ACCEPT.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0019867 outer membrane (IEA): MODIFY to GO:0009279 cell outer membrane.
- GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly (IEA): ACCEPT.
- GO:1990351 transporter complex (IEA): MODIFY to GO:0062051 lipopolysaccharide transport system.
- GO:0015221 lipopolysaccharide transmembrane transporter activity (ISO): NEW, contributes_to (by orthology to E. coli lptE).
- Core function: enables GO:0001530 lipopolysaccharide binding and contributes_to GO:0015221 lipopolysaccharide transmembrane transporter activity; processes GO:0015920, GO:0043165; complex GO:0062051 lipopolysaccharide transport system.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).

## 2026-11-07 independent LPS module consultation

All 7 original ordered annotation rows were reviewed. Their machine payloads, actions and historical NEW lifecycle are retained; no new annotation was added. The prior note about no provider attempt is historical: an actual Falcon run now failed HTTP 403, archived under `analysis/module_audits/bacterial_lps_transport/psepk-consultation/provider-attempts/falcon-lptE.log`; no provider report was fabricated.

PAINT-loss traversal could not be resolved because the exact KT2440 accession is absent from the cached family tree. The tool footer is not evidence of an independently established absence of loss. These original rows are IEA (and retained historical ISO proposals for LptD/E), not IBA.

KT2440 biological roles are inferred from its own specialized signatures and curated rule-supported statements plus source-scoped homolog experiments. P. aeruginosa PAO1-LAC structures and heterologous expression do not become KT2440 assays. Generic ABC identity is insufficient to specify LPS. The A/C bridge transfer, B ATPase motor, F/G cargo-cavity contributions and D/E outer-membrane translocation are distinct functional claims.

Relevant source findings:

- [PMID:16861298] E. coli LptD/Imp and LptE/RlpB are required for newly synthesized LPS to reach the outer leaflet, supporting the outer-membrane assembly role of the pair. Verbatim: "These data clearly show that in the absence of Imp or RlpB de novo synthesized LPS does not reach the outer leaflet of the OM."
- [PMID:20203010] E. coli LptD and LptE form a stable complex; LptE specifically binds LPS and stabilizes LptD. These are homolog results, not direct KT2440 measurements. Verbatim: "We also demonstrate that LptE binds LPS specifically and may serve as a substrate recognition site at the OM."
- [PMID:21257904] E. coli LptE resides within the LptD barrel and makes functionally important contacts, providing positive structural work for the joint translocon activity. Verbatim: "Here, we show that LptE resides within the LptD β-barrel both in vitro and in vivo."
- [PMID:21257909] The E. coli lptE6 mutant and specific lptD/bamA suppressors support an LptE role during LptD assembly. This does not imply generic folding-chaperone activity. Verbatim: "We show that lptE6 and both suppressor mutations affect the assembly of the LptD/E complex"
- [PMID:24938785] Purified E. coli LptE binds LPS and alters its aggregation state; matched in-vivo mutant phenotypes link this substrate interaction to the assembly function. Verbatim: "Our results establish that LptE binds LPS specifically and that this is crucial to LptE’s function in vivo."
- [PMID:29449493] Purified E. coli Lpt components reconstitute ATP-dependent membrane-to-membrane LPS movement. Necessity/sufficiency refers to the tested assembled seven-protein system, not autonomous transport by every component. Verbatim: "Thus, all seven Lpt proteins and ATP are necessary and sufficient for membrane-to-membrane transport to occur."


## PR6190 evidence/prose follow-up

Corrected the historical Falcon failure pointer to the already committed durable provider-attempt log. The failed attempt and all annotation decisions remain unchanged.
