# PP_0983 (Q88P70) notes

P. putida KT2440 PP_0983 is the orthologue of E. coli K-12 lptG (both in PANTHER PTHR33529:SF2).
All GOA rows for this entry are electronic (IEA). Each row is supported by curated text from this entry's
UniProt record (HAMAP-rule statements or family/domain signatures; ARBA-only statements are not cited) and
by experimental quotes on the E. coli orthologue, reused from `genes/ECOLI/lptG/lptG-ai-review.yaml`.
No provider deep research was run for this gene.

## UniProt statements quoted

- `IPR030923; LptG`
- `PF03739; LptF_LptG`
- `TIGR04408; LptG_lptG`

## E. coli literature cited

- PMID:15919996, PMID:18375759, PMID:19500581, PMID:30894744

## Decisions in this review

- GO:0005886 plasma membrane (IEA): ACCEPT.
- GO:0015920 lipopolysaccharide transport (IEA): ACCEPT.
- GO:0016020 membrane (IEA): MODIFY to GO:0005886 plasma membrane.
- GO:0043190 ATP-binding cassette (ABC) transporter complex (IEA): ACCEPT.
- GO:0055085 transmembrane transport (IEA): MODIFY to GO:0015920 lipopolysaccharide transport.
- Core function: contributes_to GO:0140332 lipopolysaccharide transfer activity; processes GO:0015920; complex GO:0043190 ATP-binding cassette (ABC) transporter complex.

## History

- 2026-11-02: support added to every row and core function; correct-but-general terms changed to MODIFY;
  methods-only quotes dropped; notes rewritten to list this review's own decisions (PR #5365 review rounds).

## 2026-11-07 independent LPS module consultation

All 5 original ordered annotation rows were reviewed. Their machine payloads, actions and historical NEW lifecycle are retained; no new annotation was added. The prior note about no provider attempt is historical: an actual Falcon run now failed HTTP 403, archived under `analysis/module_audits/bacterial_lps_transport/psepk-consultation/provider-attempts/falcon-PP_0983.log`; no provider report was fabricated.

PAINT-loss traversal could not be resolved because the exact KT2440 accession is absent from the cached family tree. The tool footer is not evidence of an independently established absence of loss. These original rows are IEA (and retained historical ISO proposals for LptD/E), not IBA.

KT2440 biological roles are inferred from its own specialized signatures and curated rule-supported statements plus source-scoped homolog experiments. P. aeruginosa PAO1-LAC structures and heterologous expression do not become KT2440 assays. Generic ABC identity is insufficient to specify LPS. The A/C bridge transfer, B ATPase motor, F/G cargo-cavity contributions and D/E outer-membrane translocation are distinct functional claims.

PMID41407669 supplies structural/biochemical evidence for PAO1-LAC LptB2FG(C), not a target assay. Its discussion of Pa-LptC failure to substitute E. coli LptC cites prior studies and concerns partner compatibility; no native LptC role loss or universal cross-species compatibility follows. No assay-specific residue rule or partial-complementation magnitude is transferred.

The generic 601-protein topology-method quote from PMID15919996 was removed from row-level support. It remains accurately assessed as a context reference; Lpt-specific topology evidence and target-specific signatures support the location.

Relevant source findings:

- [PMID:15919996] The E. coli global inner-membrane topology survey describes a large-scale method. Its abstract-level aggregate result alone does not independently verify the topology of KT2440 LptF or LptG. Verbatim: "Using C-terminal tagging with the alkaline phosphatase and green fluorescent protein, we established the periplasmic or cytoplasmic locations of the C termini for 601 inner membrane proteins."
- [PMID:18375759] E. coli LptF/YjgP and LptG/YjgQ are distinct inner-membrane proteins required for LPS surface transport, supporting specialized roles within the membrane extractor. Verbatim: "two essential Escherichia coli IM proteins of unknown function, YjgP and YjgQ, which are required for the transport of LPS to the cell surface"
- [PMID:19500581] The E. coli biochemical study reports LptF/LptG association with LptB and inclusion of LptC. Complex association supports subunit assignments but is not itself a complete transport-flux assay. Verbatim: "We report here that both LptF and LptG formed a complex with LptB."
- [PMID:30894744] E. coli K-12 lpt genes expressed in BL21(DE3) support nanodisc structural and ATPase analyses of LptB2FG(C); the structures resolve an LPS-binding cavity and coupling. These are homolog experiments for KT2440. Verbatim: "Six lipid acyl chains of LPS tightly fit into a cone-shaped hydrophobic pocket formed by TMs 1, 2, and 5 of LptF and LptG"
- [PMID:41407669] P. aeruginosa PAO1-LAC genes expressed in E. coli support structural/biochemical characterization of LptB2FG(C); tagged LptB variants partly complement a P. aeruginosa conditional mutant. The reported Pa-LptC/Ec-LptC incompatibility cites earlier work and concerns assembly compatibility, not loss of the native LptC role. No KT2440 assay is presented. Verbatim: "each gene (lptB, lptC, lptF and lptG) had been amplified from P. aeruginosa PAO1-LAC genomic DNA (47085D-5 ATCC) using PCR"


## PR6190 evidence/prose follow-up

Corrected the historical Falcon failure pointer to the already committed durable provider-attempt log. The failed attempt and all annotation decisions remain unchanged.
