# Curation Notes for Drosophila melanogaster CG2059 (UniProtKB:Q9W3R8)

## 1. Identity, Active-Site Conservation, and Dipteran Paralog Context (`PANTHER:PTHR46118:SF4`)
- **Gene / UniProtKB**: `CG2059` (`FBgn0029942` / `UniProtKB:Q9W3R8`, unreviewed TrEMBL entry, 308 aa, `sv=1`).
- **MOD gene description check**: `mod_description_deep_research DROME CG2059` confirmed that FlyBase provides no hand-written `MOD_provided_gene_description` for `FBgn0029942` (`CG2059`).
- **Active catalytic triad (`file:human/ABHD11/ABHD11-bioinformatics/RESULTS.md`)**:
  - `CG2059` (`PANTHER:PTN000106319`) is the catalytically active *Drosophila melanogaster* member of the Diptera duplication (`PTN002451173`, sister to `Gly120` pseudoenzyme `CG14717` `Q9VGJ4`).
  - `Q9W3R8` conserves the canonical oxyanion-hole motif (`60-HGLGG-64`) and complete charge-relay catalytic triad: `Ser127` (`123-LLGHSMGGK-131`), `Asp151` (`147-IITIDISPS-155`), and `His286` (`282-PKAGHWIHA-290`), corresponding 1:1 to human `ABHD11` (`Q8NFV4` `sv=2`) `Ser132`, `Asp156`, and `His287`.

## 2. Biochemical Evidence and Literature Search (`ND` Audit)
- **Direct chemoproteomic / functional proteomic catalysis in *Drosophila melanogaster***:
  - `PMID:22198472` (Birner-Gruenberger et al. 2012 *Insect Biochem Mol Biol*) identified `CG2059` as an active esterolytic enzyme in functional activity-based proteomics of the *Drosophila melanogaster* fat body (`GO:0106435` `carboxylesterase activity`, `IDA`), which also serves as an experimental PAINT IBD seed at `PANTHER:PTN002919262` (`GO:0052689`).
  - `PMID:33827210` (Kumar et al. 2021 *Biochemistry*) detected endogenous `CG2059` fluorophosphonate-reactive serine hydrolase activity across developmental stages and adult fly tissues (`GO:0017171` `serine hydrolase activity`, `HDA`). Note that in the GO hierarchy `GO:0017171` (`serine hydrolase activity`) is NOT an ancestor of `GO:0106435` (`carboxylesterase activity`), so `GO:0017171` contributes distinct mechanistic catalytic-triad information alongside `GO:0106435`!
- **Literature search for endogenous biological process (`GO:0008150`, `ND`)**:
  - Targeted PubMed and cached-corpus queries for `("CG2059" OR "FBgn0029942" OR "Q9W3R8") AND ("Drosophila" OR "melanogaster")` confirmed that aside from functional esterase/serine-hydrolase chemoproteomic profiling in `PMID:22198472` and `PMID:33827210`, **zero** genetic perturbation or physiological substrate studies in *Drosophila melanogaster* have established which endogenous biological process `CG2059` performs in vivo (e.g., whether `CG2059` deglutarylates lipoylated OGDHc in fly mitochondria like mammalian `ABHD11` `PMID:32792488`/`PMID:40664791` or hydrolyzes another mitochondrial ester/thioester).
  - Wait: under `projects/NO_DATA.md`, because human and mouse `ABHD11` (`PTHR46118:SF4`) have a well-established physiological process in mitochondrial OGDHc lipoylation maintenance / 2-oxoglutarate metabolism (`PMID:32792488`, `PMID:40664791`), is `CG2059`'s `ND` `TRUE_GAP` or `INFERABLE`? Because Dipteran `PTHR46118:SF4` duplicated into `CG2059` + `CG14717` and OGDHc lipoyl deglutarylation has only been experimentally demonstrated in mammals (`PMID:32792488`, `PMID:40664791`) while fungal homologs diverge (`EAT1` synthesizes ethyl acetate `PMID:28356220`), the endogenous biological pathway of `CG2059` in *Drosophila* is genuinely unresolved (`nd_case: TRUE_GAP` with a `BIOLOGY` `BP_DARK` knowledge gap, `ACCEPT` citing both `PMID:22198472`/`PMID:33827210` and this search record).

## 3. Annotation Review Decisions
- `GO:0005739` (`mitochondrion`, `IBA`) and `GO:0005759` (`mitochondrial matrix`, `ISS` from `UniProtKB:Q8NFV4`): `ACCEPT` (conserved mitochondrial targeting and `SF4` matrix residence).
- `GO:0006629` (`lipid metabolic process`, `IBA` from `PTN002919262`/`SGD:S000003263`): `MARK_AS_OVER_ANNOTATED` (propagated from yeast `IMO32` high-copy overexpression TAG shifts; `PMID:22198472` mutated `alpha-Est7` rather than `CG2059`).
- `GO:0008150` (`biological_process`, `ND`, `GO_REF:0000015`): `ACCEPT` (`nd_case: TRUE_GAP`, paired with `BIOLOGY` `BP_DARK` knowledge gap).
- `GO:0008233` (`NOT peptidase activity`, `IKR`, `negated: true`, `MEROPS:S33.UNW`): `ACCEPT`.
- `GO:0017171` (`serine hydrolase activity`, `HDA`, `PMID:33827210`): `ACCEPT` (orthogonal mechanistic term not entailed by `GO:0106435`).
- `GO:0052689` (`carboxylic ester hydrolase activity`, `IBA`, `GO_REF:0000033`): `MODIFY` -> `GO:0106435` (`carboxylesterase activity`, `is_a` descendant directly demonstrated on `CG2059` by `IDA` in `PMID:22198472`).
- `GO:0106435` (`carboxylesterase activity`, `IDA`, `PMID:22198472`): `ACCEPT` (core molecular function).
