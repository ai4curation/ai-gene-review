# Metabolic Model Analysis Project

## Overview

Analysis of genome-scale metabolic models (GEMs) as an additional source for GO annotation validation. This project uses the **iRP911** model for *Methylorubrum extorquens* AM1 as a pilot to identify discrepancies between model annotations and UniProt/GO annotations.

**Hypothesis**: GEMs contain curated gene-protein-reaction (GPR) associations and EC numbers that can serve as an independent validation source for GO molecular function annotations.

## Model

- **Model**: iRP911 (Peyraud et al. 2011, [DOI:10.1186/1752-0509-5-189](https://doi.org/10.1186/1752-0509-5-189))
- **Organism**: *Methylorubrum extorquens* AM1 (taxon:272630)
- **Statistics**: 884 genes, 1139 reactions, 977 metabolites
- **Files**: `models/metabolic/iRP911_*.tsv`

## Discrepancy Categories

### Summary

| Category | Count | Severity | Description |
|----------|-------|----------|-------------|
| CLASS_CHANGE | 22 | HIGH | Different EC enzyme class (e.g., 1.x → 7.x) |
| GEM_MISSING_EC | 2 | HIGH | GEM has `noEC` but UniProt has assigned EC |
| EC_UPDATE | 37 | MEDIUM | Same class, different specific EC number |
| PARTIAL_EC | 41 | LOW | Incomplete EC (ends in `-`) |
| OTHER | 13 | LOW | Miscellaneous |

**Total discrepancies**: 115 / 277 aligned genes (42%)

## High-Priority Discrepancies

### 1. EC Class 7 Reclassifications (Expected)

EC class 7 (Translocases) was established in 2018, after iRP911 was published (2011). These are **not errors**, but documentation of systematic reclassifications:

| Gene | Locus | Old EC (GEM) | New EC (UniProt) | Enzyme |
|------|-------|--------------|------------------|--------|
| coxA | META1_0115 | 1.9.3.1 | 7.1.1.9 | Cytochrome c oxidase |
| coxA | META1_3473 | 1.9.3.1 | 7.1.1.9 | Cytochrome c oxidase |
| coxB | META1_3474 | 1.9.3.1 | 7.1.1.9 | Cytochrome c oxidase |
| atpD | META1_1359 | 3.6.3.14 | 7.1.2.2 | ATP synthase beta |
| atpA | META1_1361 | 3.6.3.14 | 7.1.2.2 | ATP synthase alpha |
| kdpB | META1_0130 | 3.6.3.12 | 7.2.2.6 | K+-transporting ATPase |
| petA | META1_2509 | 1.10.2.2 | 7.1.1.8 | Cytochrome bc1 complex |
| hppa | META1_3299 | 3.6.1.1 | 7.1.3.1 | H+-PPase |

### 2. GEM Missing EC Numbers (Investigate)

These genes have `noEC` in the model but have been assigned EC numbers in UniProt:

- [x] **META1_0180** (ecm) - Ethylmalonyl-CoA mutase, EC 5.4.99.63 - **REVIEWED**
  - UniProt: [Q49115](https://www.uniprot.org/uniprotkb/Q49115) (Swiss-Prot)
  - **Finding**: GO:0004494 (methylmalonyl-CoA mutase) is WRONG - different substrate
  - **Recommendation**: New GO term needed for "ethylmalonyl-CoA mutase activity"
  - Review: `genes/METEA/ecm/ecm-ai-review.yaml`

- [x] **META1_1541** (sucB) - Dihydrolipoyllysine-residue succinyltransferase, EC 2.3.1.61 - **REVIEWED**
  - UniProt: [C5B053](https://www.uniprot.org/uniprotkb/C5B053) (TrEMBL)
  - **Finding**: All GO annotations correct; GEM simply outdated
  - Review: `genes/METEA/sucB/sucB-ai-review.yaml`

### 3. Potential Model Errors (Investigate)

These show different EC classes that are NOT simple reclassifications:

- [x] **META1_0025** (mdcD) - Malonate decarboxylase beta subunit - **REVIEWED**
  - GEM: 4.1.1.89 (carboxy-lyase) - **CORRECT**
  - UniProt: 6.4.1.3 (ligase) - **INCORRECT**
  - **Finding**: UniProt EC is WRONG. MdcD is a decarboxylase (lyase, EC class 4), NOT a ligase (EC class 6)
  - **Impact**: 5 of 8 GO annotations removed as incorrect
  - Review: `genes/METEA/mdcD/mdcD-ai-review.yaml`

- [ ] **META1_0028** (mdcB) - Malonate decarboxylase
  - GEM: 2.7.8.25 (phosphotransferase)
  - UniProt: 2.4.2.52 (glycosyltransferase)
  - Question: Different reaction mechanism?

- [ ] **META1_0175** (ilvC) - Ketol-acid reductoisomerase
  - GEM: 1.1.1.86; 4.2.1.33
  - UniProt: 1.1.1.86 only
  - Note: GEM attributes additional 3-isopropylmalate dehydratase activity

- [ ] **META1_1937** (purK) - N5-CAIR synthetase
  - GEM: 4.1.1.21 (decarboxylase)
  - UniProt: 6.3.4.18 (ligase)
  - Note: Enzyme mechanism reclassification

### 4. Bifunctional Enzyme Discrepancies

These reflect differences in annotating multifunctional enzymes:

- [x] **META1_0620** (gcvP) - Glycine cleavage system P protein - **REVIEWED** (prior review)
  - GEM: 1.4.4.2; 1.8.1.4; 2.1.2.10 (3 activities)
  - UniProt: 1.4.4.2 only - **CORRECT**
  - **Finding**: GEM over-annotates by assigning L protein (1.8.1.4) and T protein (2.1.2.10) activities to P protein
  - **Conclusion**: UniProt is correct; extra EC numbers belong to other GCV complex subunits
  - Review: `genes/METEA/gcvP/gcvP-ai-review.yaml` (status: COMPLETE)

- [ ] **META1_1862** (tal) - Transaldolase
  - GEM: 5.3.1.9; 2.2.1.2
  - UniProt: 2.2.1.2 only
  - Note: GEM adds glucose-6-phosphate isomerase activity

## Methylotrophy Core Genes (Validation Targets)

Key genes in methylotrophic metabolism with aligned annotations:

| Gene | Locus | EC | Pathway | Status |
|------|-------|----|---------| ------ |
| mxaF | META1_4538 | 1.1.2.7 | Methanol oxidation | Aligned |
| fae | META1_1766 | 4.2.1.147 | H4MPT pathway | Minor EC diff |
| mtdA | META1_1728 | 1.5.1.5 | THF pathway | Aligned |
| glyA | META1_3384 | 2.1.2.1 | Serine cycle | Aligned |
| mtkA/B | META1_1730/1731 | 6.2.1.9 | Serine cycle | Aligned |
| ecm | META1_0180 | 5.4.99.63 | EMC pathway | **GEM missing** |

## Use Cases

1. **GO Annotation Validation**: Compare GEM EC → GO MF mappings with existing GO annotations
2. **Gap Identification**: Find genes with metabolic function in GEM but missing GO MF terms
3. **Model Updating**: Identify GEM annotations that need updating based on current UniProt

## Files

- `models/metabolic/iRP911_M_extorquens_AM1.xml` - SBML model (2011, has compatibility issues)
- `models/metabolic/iRP911_reactions.xlsx` - Reactions with GPR
- `models/metabolic/iRP911_metabolites.xlsx` - Metabolite inventory with external IDs
- `models/metabolic/iRP911_uniprot_alignment.tsv` - GEM-UniProt alignment
- `models/metabolic/iRP911_ec_discrepancies.tsv` - Full discrepancy report

## Future Work: Running FBA Simulations

The original 2011 SBML file has compatibility issues with modern COBRApy:
- Invalid SBML IDs (starting with numbers, special characters)
- No FBC (Flux Balance Constraints) package
- Biomass equation not defined in SBML

**To enable FBA simulations:**
1. Standardize metabolite names between reaction/metabolite files
2. Build COBRApy model programmatically from Excel data
3. Define biomass equation from literature (Peyraud et al. 2011)
4. Validate against published growth rates (~0.15 h⁻¹ on methanol)

**Potential experiments to simulate:**
- Growth on methanol vs succinate (different carbon sources)
- Gene knockouts (ecm, gcvP) to validate essentiality predictions
- Flux distributions in serine cycle vs EMC pathway

---

# STATUS

- [x] Download iRP911 model and supplementary files
- [x] Extract gene-reaction mappings
- [x] Align with UniProt proteome
- [x] Identify EC number discrepancies
- [x] Categorize discrepancies by severity
- [x] Review ecm - **GO term error found** (GO:0004494 is wrong substrate)
- [x] Review sucB - Annotations correct; GEM outdated
- [x] Review mdcD - **MAJOR FINDING: UniProt EC wrong, GEM correct**
- [x] Review gcvP - **Resolved: GEM over-annotated complex activities to single subunit**
- [ ] Review mdcB, ilvC, purK (remaining potential errors)
- [ ] Cross-reference with GO annotations
- [ ] Document findings for model curation
- [x] Download and analyze E. coli iML1515 from BiGG
- [x] Compare iML1515 EC numbers with UniProt
- [x] Identify GEM complex representation convention (all ECs to all subunits)
- [x] Review E. coli rbsD - **Model error confirmed**: pyranase reaction missing
- [x] Review E. coli glgX - **EC annotation wrong** (2.4.1.18 → 3.2.1.196)
- [x] Run FBA experiment demonstrating impact of rbsD error
- [x] Create corrected model with pyranase reaction
- [x] Download and analyze human Recon3D from BiGG
- [x] Focus on Alzheimer's disease-relevant pathways
- [x] Identify HADHB gene-reaction misassignment error
- [x] Complete HADHB GO annotation review - **2 incorrect annotations found**
- [x] Complete CPT1C GO annotation review - **4 incorrect annotations found** (neofunctionalization case)
- [x] Run FBA experiments on Recon3D confirming annotation errors
- [ ] Review remaining AD-relevant genes with CLASS_CHANGE discrepancies

## 2026-02-03

### Session Notes

Created metabolic models cache at `models/metabolic/` with iRP911 for *M. extorquens* AM1.

**Key findings**:
- 884 genes in GEM, 277 successfully aligned with UniProt entries
- 115 EC number discrepancies identified (42% of aligned genes)
- 22 are EC class 7 reclassifications (expected, EC7 created 2018)
- 2 genes have missing EC in model (ecm, sucB) - likely characterized post-2011
- Several bifunctional enzyme annotation differences worth investigating

**Interesting observation**: The ethylmalonyl-CoA mutase (ecm, META1_0180) is marked `noEC` in the 2011 model but now has EC 5.4.99.63 in UniProt. This is a key enzyme in the ethylmalonyl-CoA pathway that was likely fully characterized after the model was published.

**Next steps**:
1. Investigate the 2 GEM_MISSING_EC cases
2. Look at bifunctional enzyme discrepancies
3. Consider using GEM→GO MF mappings as validation source

## 2026-02-04

### mdcD Review - MAJOR FINDING

**Reviewed**: META1_0025 (mdcD) - Malonate decarboxylase beta subunit

**Key Discovery**: The GEM was **CORRECT** and UniProt was **WRONG** about the EC number.

- **GEM EC**: 4.1.1.89 (carboxy-lyase/decarboxylase) - **CORRECT**
- **UniProt EC**: 6.4.1.3 (propionyl-CoA carboxylase/ligase) - **WRONG**

This is a class-level enzyme misclassification:
- EC class 4 = Lyases (break bonds)
- EC class 6 = Ligases (form bonds)

MdcD, together with MdcE, forms the malonyl-S-ACP decarboxylase (EC 4.1.1.87), part of the biotin-independent malonate decarboxylase complex (EC 4.1.1.88). The enzyme **decarboxylates** malonyl-ACP to acetyl-ACP - the opposite of carboxylation.

**Root cause**: MdcD has 35% sequence identity with acetyl-CoA carboxylase beta subunit (a ligase), causing:
1. Incorrect EC 6.4.1.3 in UniProt/EMBL entry
2. Wrong GO annotations via GO_REF:0000003 (EC-to-GO mapping)
3. Incorrect keyword propagation (Ligase, Transferase)
4. TreeGrafter using PANTHER family instead of correct subfamily

**GO Annotation Impact**:
| Annotation | Status |
|------------|--------|
| GO:0003989 (acetyl-CoA carboxylase) | REMOVE - opposite function |
| GO:0004658 (propionyl-CoA carboxylase) | REMOVE - based on wrong EC |
| GO:0006633 (fatty acid biosynthesis) | REMOVE - wrong pathway |
| GO:2001295 (malonyl-CoA biosynthesis) | REMOVE - opposite direction |
| GO:0016740 (transferase) | REMOVE - not a transferase |
| GO:0016874 (ligase) | REMOVE - not a ligase |
| **GO:0016831 (carboxy-lyase)** | **ACCEPT - CORRECT** |
| GO:0005975 (carbohydrate metabolism) | KEEP_AS_NON_CORE |
| GO:0090410 (malonate catabolism) | **NEW - core BP** |

**Conclusion**: GEMs can catch annotation errors that automated pipelines propagate from sequence homology. The malonate decarboxylase case shows how a single incorrect EC assignment cascades through multiple annotation sources.

### gcvP - Previously Reviewed

gcvP was already reviewed (status: COMPLETE). The discrepancy was resolved:
- GEM assigned 3 EC activities (1.4.4.2; 1.8.1.4; 2.1.2.10) to GcvP
- UniProt correctly has only EC 1.4.4.2
- The extra ECs (1.8.1.4 = L protein, 2.1.2.10 = T protein) belong to other GCV complex subunits
- This is a GEM over-annotation issue where complex activities were assigned to individual subunits

### ecm Review - ANOTHER GO ANNOTATION ERROR

**Reviewed**: META1_0180 (ecm) - Ethylmalonyl-CoA mutase (Swiss-Prot Q49115)

**Key Discovery**: GO:0004494 (methylmalonyl-CoA mutase activity) is **incorrectly assigned** to ecm.

| Enzyme | EC | Substrate | Product |
|--------|----|-----------|---------|
| methylmalonyl-CoA mutase | 5.4.99.2 | (R)-methylmalonyl-CoA | succinyl-CoA |
| **ethylmalonyl-CoA mutase** | 5.4.99.63 | (2R)-ethylmalonyl-CoA | (2S)-methylsuccinyl-CoA |

The annotation was incorrectly transferred based on sequence similarity. These are homologous enzymes but with **different substrate specificities**.

**Recommendation**: Request new GO term "ethylmalonyl-CoA mutase activity" for EC 5.4.99.63.

The GEM's `noEC` was because the enzyme wasn't assigned EC 5.4.99.63 until Good et al. 2015 (PMID:25448820).

### sucB Review - Straightforward Case

**Reviewed**: META1_1541 (sucB) - Dihydrolipoyllysine-residue succinyltransferase (TrEMBL C5B053)

All GO annotations are correct for this TCA cycle E2 subunit:
- GO:0004149 (dihydrolipoyllysine-residue succinyltransferase activity) - correct core MF
- GO:0006099 (tricarboxylic acid cycle) - correct core BP
- GO:0045252 (oxoglutarate dehydrogenase complex) - correct core CC

The GEM's `noEC` simply reflects the 2011 model predating the EC assignment.

### Project Summary So Far

| Gene | GEM vs UniProt | Outcome |
|------|----------------|---------|
| mdcD | GEM correct, UniProt wrong | Major UniProt EC error found |
| gcvP | GEM over-annotated | Complex activities assigned to single subunit |
| ecm | GEM outdated | GO term error found (wrong substrate specificity) |
| sucB | GEM outdated | All annotations correct |

**Key insight**: 2/4 reviews found annotation errors that GEM comparison helped identify. Metabolic models can serve as independent validation source for GO curation.

---

## E. coli iML1515 Comparison

To test whether M. extorquens findings generalize, we analyzed E. coli K-12 MG1655 using the well-curated iML1515 model from BiGG.

### Model Details

- **Model**: iML1515 (Monk et al. 2017)
- **Source**: BiGG Models database (curated, FBC-compliant)
- **Organism**: *Escherichia coli* K-12 MG1655 (taxon:511145)
- **Statistics**: 2712 reactions, 1877 metabolites, 1516 genes
- **Files**: `models/metabolic/iML1515_*.tsv`

### Discrepancy Summary

| Category | Count | Description |
|----------|-------|-------------|
| MODEL_MISSING_EC | 251 | Model reaction has no EC number |
| EC_UPDATE | 207 | Same class, different specific EC |
| UNIPROT_MISSING_EC | 123 | Model has EC, UniProt doesn't |
| PARTIAL_EC | 81 | Incomplete EC (ends in `-`) |
| CLASS_CHANGE | 59 | Different EC enzyme class |
| EC7_RECLASSIFICATION | 47 | EC class 3/1 → 7 (expected) |

**Total discrepancies**: 768 / 1515 aligned genes (**51%**)

Surprisingly, E. coli shows MORE discrepancies than M. extorquens (51% vs 42%), despite being much better studied.

### CLASS_CHANGE Analysis

The 59 class-change discrepancies break down into:

| Sub-pattern | Count | Description |
|-------------|-------|-------------|
| GENUINE_DISCREPANCY | 31 | Needs investigation |
| COMPLEX_EC_PROPAGATION | 22 | Model assigns all complex ECs to each subunit (expected) |
| EC_RECLASSIFICATION | 5 | Legitimate EC class changes (not EC7) |
| OTHER | 1 | Miscellaneous |

### GEM Complex Representation Convention

The same pattern found in M. extorquens gcvP appears systematically in E. coli:

**Pyruvate Dehydrogenase Complex** (aceE, aceF, lpd):
- Model assigns EC 1.2.4.1, 1.8.1.4, 2.3.1.12 to EACH subunit
- UniProt correctly assigns one EC per subunit
- lpd additionally gets gcvP, sucA, sucB activities (10 total ECs!)

**2-Oxoglutarate Dehydrogenase Complex** (sucA, sucB):
- Same pattern - each subunit gets 4 ECs
- UniProt: sucA=1.2.4.2, sucB=2.3.1.61

**Glycine Cleavage System** (gcvP, gcvT):
- Model: 3 ECs each (1.4.4.2; 1.8.1.4; 2.1.2.10)
- UniProt: gcvP=1.4.4.2, gcvT=2.1.2.10

**Fatty Acid Synthase Cluster** (fabZ, fabA, fabG, fabI, fabB):
- Model assigns 4-8 fab EC numbers to each gene
- UniProt assigns specific activities

**Glutaminase/Amidotransferases** (glsA, glsB, ansB):
- Model: 9-11 amidotransferase ECs each
- UniProt: Single specific EC

### Interpretation

This is **not an error** but a **modeling convention**. GEMs represent reactions, not molecular functions:

1. Complex reactions require GPR associations that list all subunits
2. EC numbers are attached to reactions, not genes
3. When extracting gene→EC mappings, ALL reaction ECs propagate to ALL genes in the GPR

**Implication for GO validation**: GEMs cannot be used directly for GO MF validation. The gene→EC mappings must be filtered to identify true molecular function assignments vs. complex membership.

### Files

- `models/metabolic/iML1515_ecoli.json` - COBRApy-compatible model
- `models/metabolic/iML1515_gene_reactions.tsv` - Gene-reaction associations
- `models/metabolic/iML1515_ec_discrepancies.tsv` - Full discrepancy report
- `models/metabolic/uniprot_ecoli_proteome.tsv` - UniProt reference data

### 2026-02-04 (continued) - E. coli Analysis

**Motivation**: User expected E. coli would have fewer discrepancies due to being well-studied. Result was surprising.

**Key findings**:
1. E. coli has 51% discrepancy rate vs 42% for M. extorquens
2. The higher rate is largely due to more complete EC coverage in iML1515
3. GEM complex representation (all ECs to all subunits) is systematic - expected modeling convention
4. EC class 7 reclassifications account for 47 discrepancies (expected)

**Notable CLASS_CHANGE cases worth investigating**:
- b0185/b2316 (accA/accD): EC 6.4.1.2 → 2.1.3.15 (carboxyltransferase reclassification)
- b2411 (ligA): EC 3.6.1.22 → 6.5.1.2 (DNA ligase mechanism update)
- b0902/b3952 (pflA/pflC): EC 2.3.1.54 → 1.97.1.4 (activating enzyme classification)
- b3748 (rbsD): EC 3.6.3.17 → 5.4.99.62 (D-ribose pyranase - possible model error)

**Conclusion**: GEM-UniProt comparison reveals systematic representation differences, not just point errors. The complex EC assignment pattern (all ECs to all subunits) is a deliberate GEM modeling convention, not an error - it's required for proper FBA essentiality predictions when any subunit knockout should abolish complex activity.

### Confirmed Model Errors (GO Annotations Correct)

#### rbsD (b3748) - D-ribose pyranase

| Source | EC | Function |
|--------|-----|----------|
| iML1515 | 3.6.3.17 | ABC transporter ATPase |
| UniProt | 5.4.99.62 | D-ribose pyranase |

**Root cause**: Model uses pre-2004 annotation. Function was corrected in PMID:15060078 showing RbsD is a pyranase that converts β-D-ribopyranose ↔ β-D-ribofuranose, NOT a transport protein.

**GO annotations**: All correct (GO:0062193 D-ribose pyranase activity, IDA evidence).

#### glgX (b3431) - Glycogen debranching enzyme

| Source | EC | Function | Direction |
|--------|-----|----------|-----------|
| iML1515 | 2.4.1.18 | Branching enzyme | ADDS branches |
| UniProt | 3.2.1.196 | Debranching enzyme | REMOVES branches |

**Root cause**: Model assigned the **opposite function**. GlgX removes α-1,6 branches during glycogen catabolism; the model has it as GlgB-like (adds branches during synthesis).

**GO annotations**: All correct (GO:0004135 amylo-alpha-1,6-glucosidase, IDA evidence).

**Impact**: These errors could affect FBA predictions for ribose utilization and glycogen metabolism.

### FBA Experiment: Validating Annotation Error Impact

**Experiment**: Compare iML1515 predictions for rbsD knockout on ribose.

**Setup**:
1. Original model: rbsD (b3748) incorrectly assigned to ribose ABC transporter GPR
2. Corrected model:
   - Remove rbsD from transporter GPR
   - Add missing pyranase reaction: `rib__D_c <=> rib_act_c` (EC 5.4.99.62, GPR: b3748)
   - Modify ribokinase (RBK) to require activated ribose

**Results**:

| Model | rbsD KO growth on ribose | Biological reality |
|-------|-------------------------|-------------------|
| Original iML1515 | 100% (no effect) | ✗ Wrong |
| Corrected | 0% (lethal) | ✓ Correct |

**Interpretation**:
- Original model: rbsD KO doesn't affect ribose growth because alternative transporters exist (OR in GPR)
- Corrected model: rbsD KO blocks ribose metabolism because the pyranase step is essential
- Real biology: rbsD mutants have severely impaired ribose utilization (PMID:15060078)

**Files**:
- `models/metabolic/iML1515_with_pyranase.json` - Corrected model
- `models/metabolic/fba_annotation_experiment.py` - Analysis script

**Conclusion**: Annotation errors in GEMs can lead to incorrect essentiality predictions. The rbsD case demonstrates that a "simple" gene misassignment (transport vs enzyme) results in missing an essential reaction.

---

## Human Recon3D Analysis - Alzheimer's Focus

### Model Details

- **Model**: Recon3D (Brunk et al. 2018)
- **Source**: BiGG Models database
- **Organism**: *Homo sapiens* (human)
- **Statistics**: 10,600 reactions, 5,835 metabolites, 2,248 genes
- **Files**: `models/metabolic/human/Recon3D_*.tsv`

### Discrepancy Summary

| Category | Count | Description |
|----------|-------|-------------|
| MODEL_MISSING_EC | 586 | Model reaction has no EC number |
| EC_UPDATE | 309 | Same class, different specific EC |
| PARTIAL_EC | 133 | Incomplete EC (ends in `-`) |
| CLASS_CHANGE | 71 | Different EC enzyme class |
| UNIPROT_MISSING_EC | 40 | Model has EC, UniProt doesn't |
| EC7_RECLASSIFICATION | 6 | EC class reclassifications |

**Total discrepancies**: 1,145 / 1,884 aligned genes (**61%**)

### AD-Relevant Pathway Analysis

Focused on subsystems implicated in Alzheimer's disease metabolic dysfunction:

| Subsystem | Total Genes | Discrepancies | CLASS_CHANGE |
|-----------|-------------|---------------|--------------|
| Oxidative phosphorylation | 101 | 24 | 0 |
| Glycolysis/gluconeogenesis | 79 | 62 | 10 |
| Citric acid cycle | 28 | 22 | 6 |
| Fatty acid oxidation | 90 | 70 | 7 |
| Cholesterol metabolism | 37 | 20 | 4 |
| Sphingolipid metabolism | 143 | 120 | 0 |
| Glutamate metabolism | 16 | 13 | 3 |
| Transport, mitochondrial | 49 | 12 | 0 |

### Confirmed Model Errors

#### HADHB (Entrez 3034) - Gene-Reaction Misassignment

| Source | Reaction | EC | Function |
|--------|----------|-----|----------|
| Recon3D | HISDr (Histidase) | 4.3.1.3 | Histidine degradation |
| UniProt | (not assigned) | 2.3.1.155, 2.3.1.16 | 3-ketoacyl-CoA thiolase |

**Error type**: HADHB (hydroxyacyl-CoA dehydrogenase beta subunit) is assigned to a **completely wrong reaction** (histidase instead of fatty acid beta-oxidation).

**Expected function**: HADHB is the beta subunit of the mitochondrial trifunctional protein (MTP), catalyzing the last three steps of long-chain fatty acid beta-oxidation:
- Long-chain enoyl-CoA hydratase
- Long-chain 3-hydroxyacyl-CoA dehydrogenase
- Long-chain 3-ketoacyl-CoA thiolase (EC 2.3.1.155)

**Impact**: The correct thiolase reactions exist in the model but use GPRs with 3030/3032/10449 - NOT 3034 (HADHB).

#### NSDHL (Entrez 7177) - Cholesterol Pathway

| Source | EC | Function |
|--------|-----|----------|
| Recon3D | 5.3.3.1 | Steroid delta-isomerase |
| UniProt | 1.1.1.170 | NAD(P)-dependent steroid dehydrogenase |

NSDHL (NAD(P)-dependent steroid dehydrogenase-like) is assigned to a reaction called "Tryptase" in the model, with no EC annotation. The model's inferred EC (5.3.3.1) from other sources is an isomerase, but NSDHL is a dehydrogenase involved in cholesterol biosynthesis.

### Key Observations

1. **Standard GEM complex representation**: As expected, multi-subunit enzyme complexes have all ECs assigned to each subunit via GPR propagation - this is a modeling convention, not an error

2. **AD genes not in model**: Classic AD risk genes (APOE, APP, PSEN1/2, BACE1, CLU) are NOT in metabolic models because they're not metabolic enzymes. However, mitochondrial and glycolytic enzymes ARE present and relevant.

3. **Mitochondrial dysfunction genes present**: All NADH dehydrogenase (Complex I) and cytochrome c oxidase (Complex IV) subunits are in the model with correct annotations

4. **Higher discrepancy rate than E. coli**: 61% vs 51% for E. coli - likely due to Recon3D's broader scope including many poorly characterized reactions

### Files

- `models/metabolic/human/Recon3D.json` - COBRApy-compatible model
- `models/metabolic/human/Recon3D_gene_reactions.tsv` - Gene-reaction associations
- `models/metabolic/human/Recon3D_ec_discrepancies.tsv` - Full discrepancy report
- `models/metabolic/human/uniprot_human_proteome.tsv` - UniProt reference data
- `models/metabolic/human/justfile` - Reproducibility commands

### 2026-02-05 - Human Recon3D Analysis

**Motivation**: Extend GEM-UniProt comparison to human model, with focus on Alzheimer's disease-relevant pathways.

**Key findings**:

1. **Higher discrepancy rate**: Recon3D has 61% discrepancies vs 51% for E. coli iML1515. This likely reflects:
   - Broader scope of Recon3D (many poorly characterized drug/xenobiotic reactions)
   - More complete EC coverage in UniProt for well-studied human enzymes

2. **HADHB misassignment found**: HADHB (hydroxyacyl-CoA dehydrogenase beta, mitochondrial trifunctional protein) is assigned to histidase (HISDr) instead of fatty acid oxidation reactions. This is a clear gene-reaction mapping error.

3. **AD genes absent from metabolic model**: Classic AD risk genes (APOE, APP, PSEN1/2, BACE1) are not metabolic enzymes so they're not in GEMs. However, mitochondrial dysfunction genes (NDUFS*, COX*, ATP5*) and glucose metabolism genes (SLC2A1, HK1/2, PKM) ARE present.

4. **Mitochondrial genes well-annotated**: Oxidative phosphorylation complex subunits (Complex I, IV, V) have relatively few discrepancies - mostly EC_UPDATE type, not CLASS_CHANGE.

5. **Fatty acid oxidation has issues**: Multiple CLASS_CHANGE cases including:
   - HSD17B4 (peroxisomal D-bifunctional protein)
   - EHHADH (peroxisomal bifunctional enzyme)
   - CPT1C (carnitine palmitoyltransferase 1C)

**Next steps**:
- Design FBA experiments for AD-relevant knockouts (e.g., mitochondrial complex genes, glucose transporters)
- Investigate brain-specific GEMs (iHumanBrain2690) for more targeted AD analysis
- Compare findings with tissue-specific models if available

### Completed AD-Relevant Gene Reviews

#### HADHB (Q8TCG5) - Mitochondrial Trifunctional Protein Beta Subunit

**Status**: COMPLETE

**Recon3D Error**: Gene ID 3034 assigned to HISDr (histidase, EC 4.3.1.3) instead of fatty acid beta-oxidation thiolase reactions.

**GO Annotation Errors Found**:

| Term | Assigned To | Correct Gene | Action |
|------|-------------|--------------|--------|
| GO:0003857 (3-hydroxyacyl-CoA dehydrogenase) | HADHB | HADHA (alpha) | REMOVE |
| GO:0004300 (enoyl-CoA hydratase) | HADHB | HADHA (alpha) | REMOVE |

**Root cause**: PMID:1550553 (1992) characterized the whole MTP complex before subunit-specific activities were known. PMID:8135828 (1994) later showed:
- Alpha subunit (HADHA): hydratase + dehydrogenase activities
- Beta subunit (HADHB): thiolase activity ONLY

**Core function**: 3-ketoacyl-CoA thiolase (GO:0003985, GO:0003988, GO:0050633)

**Review file**: `genes/human/HADHB/HADHB-ai-review.yaml`

---

#### CPT1C (Q8TCG5) - Palmitoyl Thioesterase (NOT a Palmitoyltransferase!)

**Status**: COMPLETE

**Recon3D Error**: CPT1C assigned EC 2.3.1.21 (carnitine O-palmitoyltransferase), but actual function is EC 3.1.2.22 (palmitoyl thioesterase). This is a **CLASS_CHANGE** error - hydrolase vs transferase.

**GO Annotation Errors Found**:

| Term | Evidence | Action | Reason |
|------|----------|--------|--------|
| GO:0016740 (transferase activity) | IEA | REMOVE | CPT1C is a hydrolase |
| GO:0016746 (acyltransferase activity) | IEA | REMOVE | CPT1C lacks this activity |
| GO:0006631 (fatty acid metabolic process) | IBA | REMOVE | Wrong phylogenetic inference |
| GO:0009437 (carnitine metabolic process) | IBA | REMOVE | Wrong phylogenetic inference |

**Critical NOT annotations (ACCEPTED)**:
- NOT GO:0004095 (carnitine O-palmitoyltransferase activity)
- NOT GO:0005739 (mitochondrion)
- NOT GO:0006631 (fatty acid metabolic process)
- NOT GO:0009437 (carnitine metabolic process)

**Root cause**: CPT1C is named based on sequence homology to CPT1A/CPT1B, which ARE carnitine palmitoyltransferases. However, CPT1C has neofunctionalized:

| Feature | CPT1A/CPT1B | CPT1C |
|---------|-------------|-------|
| EC number | 2.3.1.21 | 3.1.2.22 |
| Enzyme class | Transferase | Hydrolase |
| Localization | Mitochondria | ER |
| Function | Fatty acid transport | Protein depalmitoylation |
| Substrate | Palmitoyl-CoA + carnitine | Palmitoylated GRIA1 |
| Role | Energy metabolism | AMPAR trafficking |

**Key evidence**: PMID:30135643 demonstrated palmitoyl thioesterase activity with catalytic triad Ser-252/His-470/Asp-474.

**Core function**: Palmitoyl-(protein) hydrolase activity (GO:0008474) - depalmitoylates GRIA1 to regulate AMPAR trafficking in neurons

**Review file**: `genes/human/CPT1C/CPT1C-ai-review.yaml`

---

### AD Relevance Summary

Both HADHB and CPT1C are relevant to Alzheimer's disease metabolic dysfunction:

| Gene | AD Connection | Model Impact |
|------|---------------|--------------|
| HADHB | Mitochondrial FAO; ketone body production | FBA wrong for HADHB KO on FAO flux |
| CPT1C | AMPAR trafficking; brain-specific | Model incorrectly predicts FAO involvement |

The Recon3D errors would cause:
1. **HADHB KO simulations** to incorrectly predict no effect on fatty acid oxidation (wrong GPR)
2. **CPT1C involvement** in fatty acid metabolism pathways (wrong enzyme class)

---

### FBA Validation of Annotation Errors (2026-02-05)

#### Methods

**Objective**: Determine whether the identified GO annotation errors (HADHB, CPT1C) correspond to errors in the Recon3D metabolic model that affect flux predictions.

**Model**: Recon3D human genome-scale metabolic model from BiGG (Brunk et al. 2018), loaded via COBRApy. The model contains 10,600 reactions, 5,835 metabolites, and 2,248 genes with gene-protein-reaction (GPR) associations.

**Gene ID mapping**: Recon3D uses Entrez gene IDs with suffixes (e.g., `3034_AT1` for HADHB). Genes were identified by prefix matching on Entrez IDs.

**Analysis approach**:

1. **Reaction count analysis**: For each gene, enumerate all reactions in which it appears via GPR rules. Compare actual assignments to expected based on known enzyme function.

2. **Knockout simulation**: Use COBRApy's gene knockout functionality to simulate loss-of-function. Optimize for biomass objective under default medium conditions.

3. **Reaction-specific essentiality**: For reactions of interest, set the reaction as the objective function and maximize flux. Then knockout the gene and re-optimize. If max flux drops to zero, the gene is essential for that reaction.

4. **EC number verification**: Extract EC annotations from reactions and verify genes are assigned to reactions matching their known enzyme activities.

**Scripts**:
- `models/metabolic/human/fba_recon3d_experiment.py` - Initial reaction counting and knockout analysis
- `models/metabolic/human/fba_forced_fao.py` - Reaction-specific essentiality testing
- `models/metabolic/human/fba_meaningful_impact.py` - Forced FAO conditions

**Key limitation**: Under default growth conditions (rich medium, biomass optimization), fatty acid oxidation carries zero flux because glucose and other carbon sources are preferred. This means knockout phenotypes only manifest when FAO is specifically required or when testing reaction-specific essentiality.

#### Reaction Count Analysis

| Gene | Entrez ID | Reactions in Model | Expected | Error |
|------|-----------|-------------------|----------|-------|
| HADHB | 3034 | **1** (HISDr only) | ~50+ FAO | **MISSING from correct pathway** |
| HADHA | 3033 | 81 (FAO reactions) | ~80 FAO | Correct |
| CPT1C | 126129 | **92** (FAO reactions) | **0** | **Falsely included** |
| CPT1A | 1374 | 103 (FAO reactions) | ~100 FAO | Correct |
| CPT1B | 1375 | 167 (FAO reactions) | ~170 FAO | Correct |

#### Key Observations

1. **HADHB (3034)** is ONLY in HISDr (histidase, EC 4.3.1.3) - a reaction it has nothing to do with
   - Compare to HADHA which IS correctly in FAO reactions
   - This is a gene ID mapping error in Recon3D

2. **CPT1C (126129)** is included in 92 carnitine palmitoyltransferase reactions alongside CPT1A/CPT1B
   - These reactions have GPR like: `1374_AT1 or 126129_AT1 or 1375_AT1`
   - This implies CPT1C can substitute for CPT1A/CPT1B - **biologically incorrect**
   - CPT1C is a thioesterase (EC 3.1.2.22), NOT a palmitoyltransferase (EC 2.3.1.21)

3. **Under default conditions**, gene knockouts show 0% growth reduction
   - This is expected - fatty acid oxidation not essential for default biomass
   - The errors affect pathway-specific flux predictions, not overall viability

#### Biological Impact

**Fatty acid oxidation in brain metabolism**

Fatty acid β-oxidation (FAO) is the mitochondrial pathway by which long-chain fatty acids are catabolized to acetyl-CoA for energy production. While the brain primarily uses glucose, FAO provides an alternative energy source and is essential for lipid homeostasis in neural tissue. The mitochondrial trifunctional protein (MTP), a hetero-octamer of HADHA (α-subunit) and HADHB (β-subunit), catalyzes the final three steps of long-chain FAO: 2-enoyl-CoA hydratase and 3-hydroxyacyl-CoA dehydrogenase activities (HADHA) and 3-ketoacyl-CoA thiolase activity (HADHB).

**FAO dysfunction in Alzheimer's disease**

Mitochondrial dysfunction is a hallmark of Alzheimer's disease (AD), with multiple lines of evidence implicating impaired FAO:

- Lipidomic studies show accumulation of long-chain acylcarnitines in AD brain tissue, consistent with FAO defects (Snowden et al. 2017, PMID:28115367)
- Transcriptomic analysis reveals downregulation of FAO genes including HADHA/HADHB in AD hippocampus (Blalock et al. 2004, PMID:14973227)
- Metabolomic profiling identifies altered carnitine metabolism as an early biomarker of AD progression (Mapstone et al. 2014, PMID:24413353)
- The ketogenic diet, which increases FAO flux, shows therapeutic benefit in AD mouse models (Kashiwaya et al. 2013, PMID:23092880)

**CPT1C and synaptic function**

CPT1C, unlike its paralogs CPT1A/CPT1B, is a brain-specific protein localized to the endoplasmic reticulum rather than mitochondria. Despite its name, CPT1C lacks carnitine palmitoyltransferase activity and instead functions as a palmitoyl thioesterase that regulates AMPA receptor (AMPAR) trafficking (Gratacós-Batlle et al. 2018, PMID:30135643). AMPAR-mediated glutamatergic transmission is impaired early in AD, and CPT1C knockout mice show reduced synaptic transmission.

**Impact of model errors on AD research**

The identified errors create incorrect predictions for AD-relevant analyses:

| Error | Predicted | Actual | Research Impact |
|-------|-----------|--------|-----------------|
| HADHB missing from FAO | HADHB KO → no FAO effect | HADHB KO → blocked thiolase | Gene screens miss HADHB as FAO-essential |
| CPT1C in FAO reactions | CPT1C can rescue CPT1A/B | CPT1C has no CPT1 activity | False redundancy in lipid transport |
| HADHB in histidase | HADHB KO → histidine defect | HADHB has no histidase role | Wrong pathway predicted for MTPD2 |

For systems biology studies integrating transcriptomics with metabolic models, these errors would cause:
1. HADHB expression changes to correlate with histidine flux rather than FAO flux
2. CPT1C expression to incorrectly predict fatty acid transport capacity
3. Essentiality screens to miss HADHB as a FAO bottleneck

**Clinical relevance**

HADHB mutations cause Mitochondrial Trifunctional Protein Deficiency type 2 (MTPD2, MIM:620300), characterized by hypoketotic hypoglycemia, cardiomyopathy, and peripheral neuropathy. The current Recon3D model cannot correctly simulate this disorder because HADHB is absent from the affected pathway.

#### Meaningful Impact Validation

**Script**: `models/metabolic/human/fba_forced_fao.py`

**Rationale**: Default FBA optimization (maximize biomass) showed zero FAO flux, making knockout effects invisible. To demonstrate meaningful impact, we used reaction-specific objectives: set each reaction as the objective function and maximize its flux, then test if gene knockout blocks that flux.

**Method**: For each gene's associated reactions:
1. Set reaction as objective: `model.objective = reaction`
2. Optimize to find maximum achievable flux
3. Knockout the gene: `gene.knock_out()`
4. Re-optimize and compare flux

If flux drops from >0 to ~0 after knockout, the gene is essential for that specific reaction.

**Results - HADHA vs HADHB essentiality**:

| Gene | Reaction | Subsystem | Max Flux | After KO | Interpretation |
|------|----------|-----------|----------|----------|----------------|
| HADHA | FAOXC5C3x | FAO | 1000 | 0 | **ESSENTIAL** - correctly in FAO |
| HADHB | HISDr | Histidine | 1000 | 0 | Blocks wrong pathway |

HADHA knockout completely blocks FAOXC5C3x (fatty acid beta-oxidation C5→C3), demonstrating it IS essential for FAO. HADHB knockout only blocks histidase - a reaction HADHB has no biological role in.

**Thiolase reaction GPR analysis**:

Searched all reactions with EC 2.3.1.16 (acetyl-CoA C-acyltransferase / thiolase) or EC 2.3.1.155 (long-chain-3-ketoacyl-CoA thiolase):

| Reaction | EC | GPR | HADHB present? |
|----------|-----|-----|----------------|
| ACACT7m | 2.3.1.16, 2.3.1.155 | (10449 and 3032) or (3032 and 30) | **NO** |
| ACACT5m | 2.3.1.16, 2.3.1.155 | (10449 and 3032) or (3032 and 30) | **NO** |
| KAT180_m | 2.3.1.16 | 3030 or 3032 or 10449 | **NO** |
| ACACT10m | 2.3.1.16 | 38 or 3032 or 10449 | **NO** |

**Conclusion**: HADHB (Entrez 3034) is completely absent from all thiolase/acyltransferase reactions it should catalyze. The genes present (3030=HADH, 3032=HSD17B10, 10449=ACAA2) are paralogs, but HADHB - the beta subunit of MTP - is missing. This means:

1. Gene essentiality screens for FAO will not identify HADHB
2. HADHB expression data cannot be integrated with FAO flux predictions
3. MTPD2 (HADHB deficiency, MIM:620300) phenotype cannot be modeled
4. Drug target analysis for HADHB will predict wrong pathway effects
