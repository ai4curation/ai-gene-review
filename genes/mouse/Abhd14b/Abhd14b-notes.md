# Abhd14b (mouse) — review notes

Family-coordinated review of mouse `Abhd14b` (`UniProtKB:Q8VCR7`, `MGI:1915894` paralogous family `PANTHER:PTHR46197:SF2`, 210 aa).

## 1. Direct in vivo mouse evidence (`PMID:31478652`, `PMID:35700823`)

Although GOA currently carries **zero** direct experimental GO annotations on mouse `Q8VCR7` (all 16 rows are `IBA`, `ISO`, `ISS`, or `IEA` projections from human `Q96IU4`, `RHEA:45948`, and UniProt SubCell), two primary papers characterize endogenous mouse ABHD14B directly:
1. **Tissue proteome expression (`PMID:31478652`)**: Western blot profiling of soluble proteomes across wild-type C57BL/6J mouse organs showed endogenous ABHD14B is enriched in metabolically active tissues, specifically liver and kidney [PMID:31478652, "To test this, we harvested different tissues (heart, brain, liver, lungs, kidney and spleen) from C57Bl/6 wild type mice, and assessed their soluble proteomes for ABHD14B protein levels by western blot analysis."].
2. **Hepatic glucose homeostasis and fasting energetics (`PMID:35700823`)**: Tail-vein shRNA knockdown of hepatic `Abhd14b` in mice caused defective systemic glucose metabolism during fasting (failure to lower blood glucose upon 6 h fasting, impaired glucose and pyruvate tolerance responses, ~15% fasting weight loss, sluggishness, and exacerbated depletion of hepatic ATP) [PMID:35700823, "Further, we show that depleting hepatic ABHD14B in mice also results in defective systemic glucose metabolism, particularly during fasting."].

Sequence conservation between mouse `Q8VCR7` (210 aa, `sequence_version: 1`) and human `Q96IU4` (210 aa) is 89% identity over the full length, with complete conservation of the catalytic triad (`Ser111`, `Asp162`, `His188` in identical `SPSLSGMY`, `VYGDQDPM`, and `GAGHPCYL` motifs) and soluble cytosolic/nuclear architecture lacking any transmembrane helix.

## 2. Review of the 16 existing GOA rows

- **`GO:0061733` (`protein-lysine-acetyltransferase activity`, `IEA` `GO_REF:0000116` via `RHEA:45948` and `ISS` `GO_REF:0000024` from `UniProtKB:Q96IU4`) -> `REMOVE` (with `source_defects`)**:
  - Inherited from the undirected `RHEA:45948` mapping on human/mouse UniProt entries despite explicit `PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:45950` (CoA-dependent lysine deacetylation, not lysine acetyltransferase activity). Both rows invert the physiological reaction direction.
- **`GO:0016787` (`hydrolase activity`, `IBA` `PTN002920773` and `ISO` `GO_REF:0000119` from `Q96IU4`) -> `MARK_AS_OVER_ANNOTATED`**:
  - Reflects slow in vitro surrogate *p*-nitrophenyl ester hydrolysis on human `Q96IU4` (`PMID:14672934`, `PMID:31478652`), whereas physiological catalysis transfers the acetyl group from acetyl-lysine to CoA (`GO:0016407` `acetyltransferase activity` / `RHEA:45950`) without hydrolyzing water.
- **`GO:0045944` (`positive regulation of transcription by RNA polymerase II`, `IBA` `PTN002920773` and `ISO` `GO_REF:0000119` from `Q96IU4`) -> `KEEP_AS_NON_CORE`**:
  - Projected from human CIB reporter transactivation assays (`PMID:14672934`); valid orthologous projection within `SF2`, though downstream/context-dependent relative to core CoA-dependent KDAC activity.
- **Localization (`GO:0005829` `cytosol` `ACCEPT`, `GO:0005634` `nucleus` `ACCEPT`, `GO:0005654` `nucleoplasm` `ACCEPT`, `GO:0005730` `nucleolus` `KEEP_AS_NON_CORE`, `GO:0005737` `cytoplasm` `TOO_GENERAL`)**:
  - Harmonized with human `ABHD14B` (`Q96IU4`) and direct soluble liver/kidney fractionation in C57BL/6 mice (`PMID:31478652`).
- **`NEW` annotations**:
  - `GO:0016407` (`acetyltransferase activity`, `ISS` / `PMID:31478652` + `file:mouse/Abhd14b/Abhd14b-uniprot.txt` `RHEA:45950`) for the conserved CoA-dependent acetyl-transfer KDAC mechanism, paired with `proposed_new_terms` for `CoA-dependent protein-lysine deacetylase activity`.
  - `GO:0042593` (`glucose homeostasis`, `IMP` / `PMID:35700823`) or ` acts_upstream_of` — wait: let's check qualifier rules! Hepatic `Abhd14b` regulates systemic glucose homeostasis via metabolic enzyme regulation (`PMID:35700823`); per `AGENTS.md` ("Do not add what curators deliberately declined to add — A gene product is `involved_in` a process only if the product itself does some of the work of that process"), `Abhd14b` directly catalyzes protein deacylation (`GO:0035601` `protein deacylation`) rather than catalyzing a step of gluconeogenesis itself, so `GO:0035601` (`protein deacylation`) is the direct process while glucose homeostasis is an upstream regulatory outcome (`acts_upstream_of` or recorded in `description`/`findings` without over-annotating `involved_in`)!
