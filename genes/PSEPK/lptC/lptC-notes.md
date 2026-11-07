# lptC (Q88P97) notes

P. putida KT2440 lptC is the orthologue of E. coli K-12 lptC (both in PANTHER PTHR37481:SF1).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptC/lptC-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `Facilitates the transfer of LPS from the inner membrane to the periplasmic protein LptA.`
- `SUBCELLULAR LOCATION: Cell inner membrane`
- `TIGR04409; LptC_YrbK`

## E. coli literature cited

- PMID:16765569, PMID:20720015, PMID:29449493, PMID:30894744

## Decisions in this review

- GO:0005886 plasma membrane (IEA): ACCEPT.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0017089 glycolipid transfer activity (IEA): MODIFY to GO:0140332 lipopolysaccharide transfer activity.
- GO:0030288 outer membrane-bounded periplasmic space (IEA): ACCEPT.
- GO:0043165 Gram-negative-bacterium-type cell outer membrane assembly (IEA): ACCEPT.
- GO:0046836 glycolipid transport (IEA): MODIFY to GO:0015920 lipopolysaccharide transport.
- GO:0140332 lipopolysaccharide transfer activity (IEA): ACCEPT.
- Core function: enables GO:0140332 lipopolysaccharide transfer activity; processes GO:0015920, GO:0043165.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).

## 2026-11-07 independent LPS module consultation

All 7 original ordered annotation rows were reviewed. Their machine payloads, actions and historical NEW lifecycle are retained; no new annotation was added. The prior note about no provider attempt is historical: an actual Falcon run now failed HTTP 403, archived under `.cache/module-audit-logs/lps-20261107/psepk-consultation/falcon-lptC.log`; no provider report was fabricated.

PAINT-loss traversal could not be resolved because the exact KT2440 accession is absent from the cached family tree. The tool footer is not evidence of an independently established absence of loss. These original rows are IEA (and retained historical ISO proposals for LptD/E), not IBA.

KT2440 biological roles are inferred from its own specialized signatures and curated rule-supported statements plus source-scoped homolog experiments. P. aeruginosa PAO1-LAC structures and heterologous expression do not become KT2440 assays. Generic ABC identity is insufficient to specify LPS. The A/C bridge transfer, B ATPase motor, F/G cargo-cavity contributions and D/E outer-membrane translocation are distinct functional claims.

PMID41407669 supplies structural/biochemical evidence for PAO1-LAC LptB2FG(C), not a target assay. Its discussion of Pa-LptC failure to substitute E. coli LptC cites prior studies and concerns partner compatibility; no native LptC role loss or universal cross-species compatibility follows. No assay-specific residue rule or partial-complementation magnitude is transferred.

Relevant source findings:

- [PMID:16765569] E. coli conditional expression and complementation establish essentiality of the yrbK/lptC-containing distal locus under the tested conditions; this is pathway-context evidence, not a direct KT2440 LPS-transfer assay. Verbatim: "the three distal genes (yrbK, yhbN and yhbG) are essential for E. coli viability."
- [PMID:18424520] E. coli localization and depletion distinguish cytoplasmic LptB, membrane-anchored LptC and periplasmic LptA within one LPS-assembly pathway. Verbatim: "Thus, we have identified an essential LPS transport component in every cellular compartment: LptB in the cytoplasm, LptC in the IM, LptA in the periplasm, and LptD and LptE in the OM."
- [PMID:20720015] E. coli LptC binds LPS and transfers it directionally to LptA; cysteine-accessibility experiments orient its soluble domain toward the periplasm. Verbatim: "In vitro, LptA can displace lipopolysaccharide from LptC (but not vice versa), consistent with their locations and their proposed placement in a unidirectional export pathway."
- [PMID:29449493] Purified E. coli Lpt components reconstitute ATP-dependent membrane-to-membrane LPS movement. Necessity/sufficiency refers to the tested assembled seven-protein system, not autonomous transport by every component. Verbatim: "Thus, all seven Lpt proteins and ATP are necessary and sufficient for membrane-to-membrane transport to occur."
- [PMID:30894744] E. coli K-12 lpt genes expressed in BL21(DE3) support nanodisc structural and ATPase analyses of LptB2FG(C); the structures resolve an LPS-binding cavity and coupling. These are homolog experiments for KT2440. Verbatim: "Six lipid acyl chains of LPS tightly fit into a cone-shaped hydrophobic pocket formed by TMs 1, 2, and 5 of LptF and LptG"
- [PMID:41407669] P. aeruginosa PAO1-LAC genes expressed in E. coli support structural/biochemical characterization of LptB2FG(C); tagged LptB variants partly complement a P. aeruginosa conditional mutant. The reported Pa-LptC/Ec-LptC incompatibility cites earlier work and concerns assembly compatibility, not loss of the native LptC role. No KT2440 assay is presented. Verbatim: "each gene (lptB, lptC, lptF and lptG) had been amplified from P. aeruginosa PAO1-LAC genomic DNA (47085D-5 ATCC) using PCR"
