# lptD (A0A140FVZ0) notes

P. putida KT2440 lptD is the orthologue of E. coli K-12 lptD (both in PANTHER PTHR30189:SF1).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptD/lptD-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `Interacts with LptE and LptA.`
- `PF04453; LptD`
- `SUBCELLULAR LOCATION: Cell outer membrane`
- `Together with LptE, is involved in the assembly of lipopolysaccharide (LPS) at the surface of the outer membrane.`

## E. coli literature cited

- PMID:12207697, PMID:16861298, PMID:20203010, PMID:24990744, PMID:26370939, PMID:29449493

## Decisions in this review

- GO:0009279 cell outer membrane (IEA): ACCEPT.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0019867 outer membrane (IEA): MODIFY to GO:0009279 cell outer membrane.
- GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly (IEA): ACCEPT.
- GO:0061024 membrane organization (IEA): MODIFY to GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly.
- GO:1990351 transporter complex (IEA): MODIFY to GO:0062051 lipopolysaccharide transport system.
- GO:0015221 lipopolysaccharide transmembrane transporter activity (ISO): NEW, contributes_to (by orthology to E. coli lptD).
- Core function: contributes_to GO:0015221 lipopolysaccharide transmembrane transporter activity; processes GO:0015920, GO:0043165; complex GO:0062051 lipopolysaccharide transport system.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).

## 2026-11-07 independent LPS module consultation

All 7 original ordered annotation rows were reviewed. Their machine payloads, actions and historical NEW lifecycle are retained; no new annotation was added. The prior note about no provider attempt is historical: an actual Falcon run now failed HTTP 403, archived under `.cache/module-audit-logs/lps-20261107/psepk-consultation/falcon-lptD.log`; no provider report was fabricated.

PAINT-loss traversal could not be resolved because the exact KT2440 accession is absent from the cached family tree. The tool footer is not evidence of an independently established absence of loss. These original rows are IEA (and retained historical ISO proposals for LptD/E), not IBA.

KT2440 biological roles are inferred from its own specialized signatures and curated rule-supported statements plus source-scoped homolog experiments. P. aeruginosa PAO1-LAC structures and heterologous expression do not become KT2440 assays. Generic ABC identity is insufficient to specify LPS. The A/C bridge transfer, B ATPase motor, F/G cargo-cavity contributions and D/E outer-membrane translocation are distinct functional claims.

Official PDB4N4R entities establish Salmonella Typhimurium LT2 source proteins expressed in E. coli for PMID24990744; metadata are archived in the consultation. The inherited E. coli-only reference boilerplate was corrected. PMID26370939 is a review, not an additional primary experiment. The target HAMAP caution is not interpreted as loss of LptD activity or as proof that exact E. coli disulfides are conserved.

Relevant source findings:

- [PMID:12207697] The E. coli Imp/LptD depletion study links the protein to outer-membrane biogenesis; this abstract does not establish a KT2440 assay or conserved disulfide positions. Verbatim: "Upon depletion of Imp, lipids and outer membrane proteins appear in a novel membrane fraction with higher density than the outer membrane."
- [PMID:16861298] E. coli LptD/Imp and LptE/RlpB are required for newly synthesized LPS to reach the outer leaflet, supporting the outer-membrane assembly role of the pair. Verbatim: "These data clearly show that in the absence of Imp or RlpB de novo synthesized LPS does not reach the outer leaflet of the OM."
- [PMID:20203010] E. coli LptD and LptE form a stable complex; LptE specifically binds LPS and stabilizes LptD. These are homolog results, not direct KT2440 measurements. Verbatim: "We also demonstrate that LptE binds LPS specifically and may serve as a substrate recognition site at the OM."
- [PMID:26370939] This REVIEW synthesizes periplasmic LPS transport and outer-membrane insertion. It is secondary mechanistic context, not an independent primary experiment on a KT2440 protein. Verbatim: "Following extraction, it traverses a bridge formed by LptA and finally is selectively inserted into the outer leaflet of the OM by the LptDE OM translocon."
- [PMID:29449493] Purified E. coli Lpt components reconstitute ATP-dependent membrane-to-membrane LPS movement. Necessity/sufficiency refers to the tested assembled seven-protein system, not autonomous transport by every component. Verbatim: "Thus, all seven Lpt proteins and ATP are necessary and sufficient for membrane-to-membrane transport to occur."
- [PMID:24990744] The linked PDB4N4R structure is Salmonella Typhimurium LT2 LptD/LptE expressed in E. coli, verified from official entity records. The abstract supports the barrel/plug and lateral-insertion model; it is not an E. coli-native or KT2440 structural assay. Verbatim: "LptE adopts a roll-like structure located inside the barrel of LptD to form an unprecedented two-protein 'barrel and plug' architecture."
