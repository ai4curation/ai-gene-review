# lptB (Q88P99) notes

P. putida KT2440 lptB is the orthologue of E. coli K-12 lptB (both in PANTHER PTHR45772:SF10).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptB/lptB-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `PF00005; ABC_tran`
- `PS00211; ABC_TRANSPORTER_1`
- `TIGR04406; LPS_export_lptB`

## E. coli literature cited

- PMID:19500581, PMID:24639492, PMID:27795402, PMID:29449493, PMID:30894744

## Decisions in this review

- GO:0000166 nucleotide binding (IEA): MODIFY to GO:0005524 ATP binding.
- GO:0005524 ATP binding (IEA): ACCEPT.
- GO:0005737 cytoplasm (IEA): KEEP_AS_NON_CORE.
- GO:0005886 plasma membrane (IEA): ACCEPT.
- GO:0016887 ATP hydrolysis activity (IEA): ACCEPT.
- GO:0043190 ATP-binding cassette (ABC) transporter complex (IEA): ACCEPT.
- GO:0055085 transmembrane transport (IEA): MODIFY to GO:0015920 lipopolysaccharide transport.
- Core function: enables GO:0016887 ATP hydrolysis activity; processes GO:0015920; complex GO:0043190 ATP-binding cassette (ABC) transporter complex.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).

## 2026-11-07 independent LPS module consultation

All 7 original ordered annotation rows were reviewed. Their machine payloads, actions and historical NEW lifecycle are retained; no new annotation was added. The prior note about no provider attempt is historical: an actual Falcon run now failed HTTP 403, archived under `.cache/module-audit-logs/lps-20261107/psepk-consultation/falcon-lptB.log`; no provider report was fabricated.

PAINT-loss traversal could not be resolved because the exact KT2440 accession is absent from the cached family tree. The tool footer is not evidence of an independently established absence of loss. These original rows are IEA (and retained historical ISO proposals for LptD/E), not IBA.

KT2440 biological roles are inferred from its own specialized signatures and curated rule-supported statements plus source-scoped homolog experiments. P. aeruginosa PAO1-LAC structures and heterologous expression do not become KT2440 assays. Generic ABC identity is insufficient to specify LPS. The A/C bridge transfer, B ATPase motor, F/G cargo-cavity contributions and D/E outer-membrane translocation are distinct functional claims.

PMID41407669 supplies structural/biochemical evidence for PAO1-LAC LptB2FG(C), not a target assay. Its discussion of Pa-LptC failure to substitute E. coli LptC cites prior studies and concerns partner compatibility; no native LptC role loss or universal cross-species compatibility follows. No assay-specific residue rule or partial-complementation magnitude is transferred.

Relevant source findings:

- [PMID:19500581] The E. coli biochemical study reports LptF/LptG association with LptB and inclusion of LptC. Complex association supports subunit assignments but is not itself a complete transport-flux assay. Verbatim: "We report here that both LptF and LptG formed a complex with LptB."
- [PMID:24639492] E. coli LptB nucleotide-state structures and activity/function measurements distinguish ATP hydrolysis from productive coupling to LPS transport. Verbatim: "Our studies establish the essentiality of ATP hydrolysis by LptB to power LPS transport in cells"
- [PMID:27795402] E. coli LptB2FG mutational work examines coupling of ATP hydrolysis to extraction; exact residue phenotypes are not assigned to KT2440 without sequence/construct verification. Verbatim: "The LptB2FG proteins form an ATP-binding cassette (ABC) transporter that uses energy from ATP hydrolysis in the cytoplasm to facilitate extraction of LPS from the outer face of the cytoplasmic membrane prior to transport to the cell surface."
- [PMID:29449493] Purified E. coli Lpt components reconstitute ATP-dependent membrane-to-membrane LPS movement. Necessity/sufficiency refers to the tested assembled seven-protein system, not autonomous transport by every component. Verbatim: "Thus, all seven Lpt proteins and ATP are necessary and sufficient for membrane-to-membrane transport to occur."
- [PMID:30894744] E. coli K-12 lpt genes expressed in BL21(DE3) support nanodisc structural and ATPase analyses of LptB2FG(C); the structures resolve an LPS-binding cavity and coupling. These are homolog experiments for KT2440. Verbatim: "Six lipid acyl chains of LPS tightly fit into a cone-shaped hydrophobic pocket formed by TMs 1, 2, and 5 of LptF and LptG"
- [PMID:18424520] E. coli localization and depletion distinguish cytoplasmic LptB, membrane-anchored LptC and periplasmic LptA within one LPS-assembly pathway. Verbatim: "Thus, we have identified an essential LPS transport component in every cellular compartment: LptB in the cytoplasm, LptC in the IM, LptA in the periplasm, and LptD and LptE in the OM."
- [PMID:41407669] P. aeruginosa PAO1-LAC genes expressed in E. coli support structural/biochemical characterization of LptB2FG(C); tagged LptB variants partly complement a P. aeruginosa conditional mutant. The reported Pa-LptC/Ec-LptC incompatibility cites earlier work and concerns assembly compatibility, not loss of the native LptC role. No KT2440 assay is presented. Verbatim: "each gene (lptB, lptC, lptF and lptG) had been amplified from P. aeruginosa PAO1-LAC genomic DNA (47085D-5 ATCC) using PCR"
