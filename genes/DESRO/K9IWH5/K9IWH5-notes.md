# K9IWH5 Research Notes

## Key findings
- UniProt names this protein lysozyme [file:DESRO/K9IWH5/K9IWH5-uniprot.txt "RecName: Full=lysozyme"].
- UniProt assigns this protein to glycosyl hydrolase family 22 [file:DESRO/K9IWH5/K9IWH5-uniprot.txt "Belongs to the glycosyl hydrolase 22 family."].
- Deep research identifies LYZ as a c-type lysozyme in the GH22 family [file:DESRO/K9IWH5/K9IWH5-deep-research-falcon.md "LYZ corresponds to a c-type lysozyme (muramidase; EC 3.2.1.17) that hydrolyzes peptidoglycan and belongs to the classical GH22 lysozyme family."].

## 2026-07-31 compliance review

**There is a gene-specific paper, and it was not being used.** The UniProt entry
lists three EMBL records; the third (MK561737 / QEQ43371.1, liver) carries
`RX PubMed=31506780` — He et al. 2019, *Adaptive Evolution of C-Type Lysozyme in
Vampire Bats*. Fetched into the cache (abstract only; `full_text_available:
false`). Key points:

- [PMID:31506780 "Only a single lysozyme gene was identified in each of these
  species."] — no paralogue in vampire bats, unlike the insectivorous bat clade
  that duplicated lysozyme for chitin digestion.
- [PMID:31506780 "Evidence for positive selection on mature lysozyme was found
  on lineages leading to vampire bats"] and [PMID:31506780 "several amino acid
  substitutions found in mature lysozymes from the sanguivorous clade are
  predicted to have functional impacts"].
- The authors' reading — [PMID:31506780 "Functional adaptation of vampire bat
  lysozymes could be associated with anti-microbial defense, possibly driven by
  the specialized sanguivory-related habits of vampire bats."] — is an
  interpretation of a selection analysis, not a measurement. Tagged as such in
  `finding_review` and turned into a knowledge gap rather than an annotation.

The second salivary-gland EMBL record (JAA45151.1) traces to the Vampirome study
(PMID:23411029), which puts lysozyme in the accessory gland at both transcript
and protein level [PMID:23411029 "families were expressed at higher levels in
the AC gland, as indicated by both transcriptome and proteome analysis (Figure
2B)."] and detects it directly by LC-MS/MS [PMID:23411029 "components of the
complement pathway, galectins, lysozyme, lipases"].

**Reversed three annotation calls made by the previous version.** All three were
in the direction of throwing information away:

- `GO:0050830` (Gram-positive) and `GO:0050829` (Gram-negative) had been set to
  MODIFY → `GO:0042742` *defense response to bacterium*. That generalises two
  specific, mechanistically explained terms into a parent that is **already
  separately annotated and accepted** in the same file — pure information loss.
  Both are now ACCEPT. Cross-checked against human LYZ (P61626) in QuickGO:
  `GO:0050830` is IDA (PMID:21093056), `GO:0050829` is IBA — the same TreeGrafter
  propagation applied here.
- `GO:0031640` *killing of cells of another organism* had been marked
  over-annotated for being "too broad". It is not an inflation: bacteriolysis is
  the direct outcome of muramidase action, the keyword source is literally
  "Bacteriolytic enzyme", and human LYZ carries the term by **IDA**
  (PMID:9727055). Now ACCEPT.

**Filled a missing GO aspect.** The GOA record has no cellular component term at
all. Added `GO:0005576` extracellular region as a NEW (ISS) annotation, supported
independently by the signal peptide (`SIGNAL 1..18`), by the human orthologue's
IDA annotation to the same term, and by proteomic detection in the bat gland.

`gene_symbol` changed from the accession to `LYZ`, matching both the UniProt
`GN Name=LYZ` line and the GOA `SYMBOL` column.
