# FLD (At3g10390, UniProt Q9CAE3) curation notes

## 2026-10 review session (autonomous pathway module)

- Accession verified: Q9CAE3 FLD_ARATH, At3g10390 (synonym SOF1).
- Deep research (falcon) failed (HTTP 429).
- LSD1 homolog required by FCA [PMID:17996704 "FCA requires FLOWERING LOCUS D (FLD), a homolog of the human lysine-specific demethylase 1 (LSD1) for FLC downregulation."]
- FLD/LD/SDG26 complex, H3K4me1 [PMID:32541063 "FLD tightly associates with LUMINIDEPENDENS (LD) and SET DOMAIN GROUP 26 (SDG26) in vivo, and, together, they prevent accumulation of monomethylated H3K4 (H3K4me1) over the FLC gene body."]
- Genome-wide convergent genes, Pol II colocalization [PMID:33649596 "FLD localizes to actively transcribed genes, where it colocalizes with elongating RNA polymerase II phosphorylated at the Ser2 or Ser5 sites."]
- HDA6 interaction via SWIRM [PMID:21398257]; HDA5/FVE/FLD/HDA6 complex [PMID:25922987].
- Paralogs LDL1/LDL2 partially redundant [PMID:17921315].

## Decisions
- Histone demethylase activity and oxidoreductase -> MODIFY to histone H3K4 demethylase activity (GO:0032453). Did not use the FAD-dependent child GO:0140682 because direct in vitro activity of FLD is not established in the cached literature.
- Organellar ISM predictions removed. Photoperiodism term -> timing of transition (autonomous pathway is photoperiod-independent).
- NEW: negative regulation of gene expression, epigenetic (GO:0045814); chromatin (GO:0000785, ChIP).


## 2026-10-26 complete annotation audit

The earlier organelle REMOVEs are superseded by UNDECIDED: nuclear chromatin localization is not a test excluding mitochondrial or plastid pools. The broad oxidoreductase IBA remains true and is refined with its actual ancestral PTN source. The existing two NEW rows are preserved; no new rows were added. Demethylation remains a well-supported conserved catalytic inference rather than a claimed purified assay. PMID:32392578 photoperiodism is unresolved because the available abstract establishes DA-responsive floral timing, not the relevant daylength comparison. Existing chromatin, flowering and defense claims were separately retained on their sources.

All seeded rows were reviewed, with original term, evidence, source, supporting-entity and qualifier/NOT payloads preserved. The shared normal Falcon attempt and perplexity-lite fallback both failed; logs are retained under `.cache/module-audit-logs/autonomous-flowering-fetch/ARATH-FLD-provider.log`. No provider report was fabricated. Manual primary-literature assessment and normal publication fetching supplied this review. Source access limits are stated per reference/claim. Generic protein binding follows the current informative-function policy; its removal does not reject the physical interactions. Nuclear localization does not by itself exclude additional compartments.
