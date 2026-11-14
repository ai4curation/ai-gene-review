# Curation Notes for Saccharomyces cerevisiae EAT1 (UniProtKB:P53208)

## 1. Identity, Neofunctionalization, and Catalytic Triad (`PANTHER:PTHR46118:SF4`)
- **Gene / UniProtKB**: `EAT1` (`YGR015C` / `SGD:S000003247` / `UniProtKB:P53208`, reviewed Swiss-Prot entry `EAT1_YEAST`, 328 aa, `sv=1`).
- **Neofunctionalized alpha/beta-hydrolase alcohol O-acetyltransferase (`PMID:28356220`, `PMID:30054364`)**:
  - Within `PANTHER:PTHR46118:SF4`, Saccharomycetaceae yeast duplicated an ancestral mitochondrial alpha/beta-hydrolase into `IMO32` (`YGR031W`, `P53219`) and `EAT1` (`YGR015C`, `P53208`).
  - Kruis et al. (`PMID:28356220`) discovered that `Eat1` defines a novel family of mitochondrial alcohol O-acetyltransferases (`EC 2.3.1.268`, `RHEA:55972`) within the alpha/beta-hydrolase superfamily: `Eat1` catalyzes the synthesis of ethyl acetate from ethanol and acetyl-CoA, and deletion of *S. cerevisiae* `EAT1` (`YGR015C`) reduces endogenous ethyl acetate production by at least 50% (`PMID:28356220`; `EAT1-uniprot.txt`).
  - Because `Eat1` uses a canonical alpha/beta-hydrolase oxyanion loop (`45-HGLLG-49` within `42-INIHGLLGSH-51`) and covalent acyl-enzyme Ser-Asp-His catalytic triad (`Ser115` in `111-LLGFSMGGK-119` with `Phe114` in `GFSMG`, `Asp139` in `135-CISIDLPPY-143`, and `His302` in `298-FNTGHNLLL-306`; `FT ACT_SITE 115 / 139 / 302` in `EAT1-uniprot.txt`), water competes with ethanol as acyl acceptor in the absence of high ethanol concentrations, giving `Eat1` genuine secondary thioesterase (`acetyl-CoA hydrolase activity`, `EC 3.1.2.1`, `RHEA:20289`, `GO:0003986`) and carboxylesterase (`acetylesterase activity` on ethyl acetate, `RHEA:58148`, `GO:0008126`) activities (`EAT1-uniprot.txt`).

## 2. Organelle Granularity (`projects/ORGANELLES.md`)
- `EAT1` carries three `GO:0005739` (`mitochondrion`) rows (`HDA` `PMID:14562095`, `IBA` `GO_REF:0000033`, `IEA` `GO_REF:0000044`) — all `ACCEPT`.
- Per `projects/ORGANELLES.md`, we stay at root `GO:0005739` without adding `GO:0005759` (`mitochondrial matrix`) as `NEW` because in *S. cerevisiae* (`P53208`) mitochondrial localization is established by whole-organelle GFP fluorescence (`PMID:14562095`, corroborated by yEGFP localization in *Kluyveromyces lactis* and in silico targeting predictions in `PMID:30054364`), while *S. cerevisiae* Eat1 lacks mapped matrix peptidase cleavage (`FT CHAIN 1..328` in `EAT1-uniprot.txt`, unlike `Imo32`) or sub-mitochondrial mitoplast protease-protection data.

## 3. Audit of SGD Gene Description (`file:yeast/EAT1/EAT1-deep-research-sgd.md`) and Source Defects in GOA
1. **SGD curated gene description (`EAT1-deep-research-sgd.md`)**:
   - Verbatim text: `Ethanol acetyltransferase; green fluorescent protein (GFP)-fusion protein localizes to the mitochondrion`
   - Assessment: Factually accurate and concise (`relevance: HIGH`, `correctness: VERIFIED`), tracing to `PMID:28356220` and `PMID:14562095`/`PMID:30054364`, though incomplete in omitting the reaction product (`ethyl acetate` from ethanol + acetyl-CoA) and secondary thioesterase/esterase side-activities (`MISSING_STATEMENT` `source_defects` with `requested_change: CHECK`).
2. **GOA defect 1 — Mis-curated `GO:0016453` (`C-acetyltransferase activity`, `IDA`, `PMID:28356220`)**:
   - SGD curated `PMID:28356220` to `GO:0016453` (`C-acetyltransferase activity`, which transfers an acetyl group onto a **carbon** atom), whereas `Eat1` transfers the acetyl group from acetyl-CoA onto the hydroxyl **oxygen** of ethanol to form ethyl acetate (`EC 2.3.1.268`, `RHEA:55972`, `GO:0004026` `alcohol O-acetyltransferase activity`, already present on `EAT1` via `GO_REF:0000116`!). Action: `MODIFY` -> `GO:0004026` with `source_defects` (`SGD`, `WRONG_TERM`, `REPOINT` `GO:0016453` -> `GO:0004026`, `cause: LABEL_WITHOUT_DEFINITION`).
3. **GOA defect 2 — Stale `GO:0008150` (`biological_process`, `ND`, `GO_REF:0000015`)**:
   - Stale `ND` left in SGD despite `PMID:28356220` and `PMID:30054364` directly demonstrating that *S. cerevisiae* `EAT1` catalyzes mitochondrial ethyl acetate biosynthesis (`Disruption phenotype: Reduces ethyl acetate production by at least 50%`, `PMID:28356220`). Action: `REMOVE` with `nd_case: STALE` + `source_defects` (`SGD`, `OTHER`, `DELETE_ROW`, `GO:0008150`), and add `NEW` `IMP` `GO:1902819` (`ethyl acetate biosynthetic process`, `involved_in`, `PMID:28356220`).
4. **Remaining rows**:
   - `GO:0004026` (`alcohol O-acetyltransferase activity`, `IEA`, `RHEA:55972`): `ACCEPT` (core MF).
   - `GO:0003986` (`acetyl-CoA hydrolase activity`, `IEA` and `ISS`): `KEEP_AS_NON_CORE` (real secondary thioesterase side-activity in absence of ethanol).
   - `GO:0008126` (`acetylesterase activity`, `IEA`, `RHEA:58148`): `KEEP_AS_NON_CORE` (real secondary ethyl acetate esterase side-activity).
   - `GO:0052689` (`carboxylic ester hydrolase activity`, `IBA`): `MODIFY` -> `GO:0008126` (`acetylesterase activity`, `is_a` descendant already carried on `EAT1`).
   - `GO:0006629` (`lipid metabolic process`, `IBA` from `IMO32`): `MARK_AS_OVER_ANNOTATED`.
