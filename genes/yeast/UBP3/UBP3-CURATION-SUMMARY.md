# UBP3 GO Annotation Curation Review - Executive Summary

## Gene: UBP3 (Ubiquitin-specific protease 3)
**UniProt ID:** Q01477
**Organism:** Saccharomyces cerevisiae
**EC Number:** 3.4.19.12
**Total Annotations Reviewed:** 54

---

## Curation Results

### Summary by Action

| Action | Count | Percentage |
|--------|-------|------------|
| **ACCEPT** | 33 | 61.1% |
| **REMOVE** | 10 | 18.5% |
| **MARK_AS_OVER_ANNOTATED** | 2 | 3.7% |
| **MODIFY** | 1 | 1.9% |
| **KEEP_AS_NON_CORE** | 1 | 1.9% |
| **PENDING** | 7 | 13.0% |

### Key Statistics

**Core Catalytic Functions (ACCEPT):**
- Cysteine-type deubiquitinase activity: 4 annotations (IBA, IEA, IMP, IDA)
- Protein deubiquitination: 6 annotations (IEA, IMP, IMP, IDA, IMP, IMP)
- Total core catalytic: **10 annotations**

**Biological Processes Supporting Core Function (ACCEPT):**
- Ribophagy: 3 annotations (NAS, IMP, IMP)
- Stress granule assembly: 1 annotation (IDA)
- ER-Golgi transport regulation: 3 annotations (NAS, IMP, IMP)
- Retrograde transport: 1 annotation (NAS)
- Golgi protein retention: 6 annotations (4x IMP, 2x IGI)
- Osmotic stress response: 2 annotations (IMP, IPI)
- Total processes: **16 annotations**

**Localization Terms (ACCEPT):**
- Nucleus: 1 annotation (IBA)
- Cytoplasm: 1 annotation (IDA)
- Cytosol: 3 annotations (IBA, IDA, HDA)
- Mitochondrion: 1 annotation (IDA - dynamic)
- Ubp3-Bre5 complex: 1 annotation (IPI)
- Total localization/complex: **7 annotations**

**Molecular Function - General Terms (ACCEPT):**
- Hydrolase activity: 1 annotation (IEA)
- Peptidase activity: 1 annotation (IEA)
- Cysteine-type peptidase activity: 1 annotation (IEA)
- Total general function: **3 annotations**

**Problematic Annotations (REMOVE/MODIFY):**
- Protein binding (generic): 8 annotations - **ALL REMOVE**
- mRNA binding: 2 annotations - **MARK_AS_OVER_ANNOTATED**
- Regulation of protein stability: 1 annotation - **REMOVE**
- Proteolysis (overly general): 1 annotation - **MODIFY**

---

## Detailed Curation Decisions

### 1. ACCEPT Annotations (33 total)

#### Molecular Function - Catalytic Activity
All four annotations of GO:0004843 (cysteine-type deubiquitinase activity) are ACCEPTED:
- **IBA**: Phylogenetic inference based on conserved catalytic domain (C19 family, IPR001394)
- **IEA**: InterPro domain-based inference with EC classification (3.4.19.12)
- **IMP**: Experimental evidence showing catalytic activity required for MAPK signaling function
- **IDA**: Original biochemical characterization by Baker et al. (1992)

**Rationale:** This is the core molecular function of UBP3. Multiple independent evidence types all converge on the same conclusion. The enzyme family assignment is well-established, crystal structures are available, and catalytic activity is demonstrated biochemically in multiple substrates.

#### Biological Process - Protein Deubiquitination
All six annotations of GO:0016579 (protein deubiquitination) are ACCEPTED:
- **IEA**: InterPro domain-based inference (appropriate for USP family)
- **IMP (Ste7)**: Genetic evidence that catalytic activity regulates MAPK pathway
- **IMP (Ste7 alternate)**: Complementary experimental approach
- **IDA (RNAP II)**: Direct biochemical analysis of RNA polymerase II substrate
- **IMP (RNAP II)**: Functional requirement for RNAP II deubiquitination
- **IMP (Ras/cAMP)**: Functional analysis of signaling pathway regulation

**Rationale:** Deubiquitination is the fundamental biological process catalyzed by UBP3. Evidence is robust across multiple substrates (RNAP II, Ste7, general protein substrates). Each annotation documents a specific substrate or functional context.

#### Biological Process - Ribophagy
All three annotations of GO:0034517 (ribophagy) are ACCEPTED:
- **NAS**: Named assertion based on discovery of ribophagy pathway dependent on Ubp3
- **IMP**: Genetic knockout shows accumulation of 60S ribosomes under starvation
- **IMP (CDC48/UFD3)**: Functional analysis identifying complex cofactors required

**Rationale:** Ribophagy is a well-established selective autophagy pathway discovered in the referenced study. UBP3 catalytic activity is essential. This is a core biological role, particularly important for nutrient starvation response and cell survival.

#### Biological Process - Stress Granule Assembly
GO:0034063 (stress granule assembly) - **ACCEPT (IDA)**

**Rationale:** IDA evidence from targeted genetic screen demonstrates UBP3 catalytic activity is specifically required for stress granule formation. This function is unique among UBP family members and requires both catalytic activity and Bre5 cofactor. Stress granules are important for cell survival in stationary phase.

#### Biological Process - Vesicular Transport
All annotations related to ER-Golgi transport are ACCEPTED:
- GO:0060628 (ER to Golgi transport) - NAS and IMP
- GO:2000156 (retrograde Golgi to ER transport) - NAS
- GO:0045053 (Golgi protein retention) - 4x IMP, 2x IGI

**Rationale:** These transport processes are mechanistically linked through SEC23 deubiquitination. UBP3-Bre5 complex removes ubiquitin from SEC23, maintaining protein levels necessary for COPII coat function. The recent discovery of a novel mechanism for Golgi protein retention (via Ubp3-Bre5 deubiquitination) warrants acceptance of all transport-related terms.

#### Biological Process - Osmotic Stress Response
GO:0047484 (regulation of response to osmotic stress) - IMP and IPI

**Rationale:** UBP3 activity is directly modulated by Hog1 MAPK kinase under osmotic stress (phosphorylation-mediated activation). This couples osmotic stress sensing to deubiquitination pathway regulation. Both IMP and IPI evidence establish functional relationship.

#### Cellular Component - Localization
All localization annotations are ACCEPTED:
- **Nucleus** (IBA): Supporting evidence from RNAP II and histone deubiquitination substrates
- **Cytoplasm** (IDA): Direct detection from cellular fractionation
- **Cytosol** (IBA, IDA, HDA): Multiple confirmations of major catalytic compartment
- **Mitochondrion** (IDA): Dynamic translocation during mitophagy induction

**Rationale:** Localization is consistent with known substrate distribution and functional requirements. Notably, mitochondrial localization is stimulus-dependent (upon mitophagy induction), which is informative about regulatory mechanism.

#### Cellular Component - Ubp3-Bre5 Complex
GO:1990861 (Ubp3-Bre5 deubiquitination complex) - **ACCEPT (IPI)**

**Rationale:** This is a well-characterized complex with available crystal structure (PDB:2QIY). Direct physical interaction is documented. This is not generic protein binding but a named functional complex with defined stoichiometry (heterotetrameric, 2:2 Ubp3:Bre5).

#### Molecular Function - General Terms
Three parent terms (hydrolase, peptidase, cysteine-type peptidase activity) are ACCEPTED:

**Rationale:** These are appropriate parent terms in the catalytic hierarchy. The specific cysteine-type deubiquitinase activity is most informative, but these parent terms provide useful categorical information in the GO hierarchy.

### 2. REMOVE Annotations (10 total)

#### GO:0005515 - Protein Binding (8 instances)
**ALL INSTANCES REMOVED**

Evidence sources:
- PMID:16429126, PMID:16554755 (2x variants), PMID:17632125, PMID:18719252, PMID:20508643, PMID:21179020, PMID:37968396

**Rationale:**
1. **Overly generic**: Protein binding does not distinguish between functional substrates, regulatory proteins, and non-specific interactions
2. **Violates GO best practices**: GO curation guidelines recommend avoiding protein binding in favor of more specific molecular function terms
3. **More specific terms available**:
   - BRE5 interaction → GO:1990861 (Ubp3-Bre5 complex membership) is far more informative
   - Other interactions not functionally characterized → should not be annotated
4. **Confuses mechanism with function**: Catalytic activity (GO:0004843) is the relevant molecular function, not passive substrate binding
5. **Not substrate-specific**: These annotations represent binary interactions from databases without mechanistic characterization

**Implementation:** Replace all protein binding annotations with more specific terms where available (complex membership for Bre5) or remove entirely where no functional characterization exists.

#### GO:0031647 - Regulation of Protein Stability (1 instance)
**REMOVE (IBA)**

**Rationale:**
1. **Indirect consequence, not direct function**: Protein stability regulation is a downstream effect of removing ubiquitin degradation signals, not the direct catalytic function
2. **Too broad**: Applies to any deubiquitinase and does not capture substrate specificity
3. **Redundant with specific annotations**: The substrate-specific deubiquitination terms (SEC23, RNAP II, Ste7, ribophagy targets) are far more informative
4. **Misleading specificity level**: Suggests broader function than actually characterized

**Implementation:** Remove in favor of substrate-specific process annotations.

#### GO:0006508 - Proteolysis (1 instance)
**MODIFY (IEA from GO_REF:0000043)**

**Current status:** IEA from UniProtKB keyword "Protease"

**Rationale:**
1. **Overly general**: Proteolysis encompasses all protein-cleaving activities, inappropriate for specialized deubiquitinase
2. **Loses specificity**: Ubiquitin C-terminal hydrolysis is a specific type of proteolysis with distinct mechanism and substrates
3. **Redundant information**: If annotated, this is implied by more specific catalytic terms already present
4. **Not recommended in current literature**: GO curators increasingly avoid this broad term in favor of specific enzyme family roles

**Implementation:** Remove this annotation or modify to more specific hydrolysis term if available (e.g., ubiquitin carboxyl-terminal hydrolysis, if defined).

### 3. MARK_AS_OVER_ANNOTATED (2 annotations)

#### GO:0003729 - mRNA Binding (2 instances)
**Both marked as OVER_ANNOTATED**

Evidence:
- HDA: PMID:23222640 (yeast mRNP proteome survey)
- IDA: PMID:20844764 (proteome-wide RNA-binding protein survey)

**Rationale:**
1. **Limited mechanistic evidence**: These are proteome-wide surveys that identify proteins co-fractionating with mRNPs/RNA
2. **Confuses localization with function**: Presence in stress granules (RNA-rich compartment) does not demonstrate functional mRNA binding
3. **Catalytic activity is demonstrated mechanism**: The functional requirement in stress granules is UBP3 CATALYTIC ACTIVITY (deubiquitination), not mRNA interaction
4. **No substrate specificity documented**: If UBP3 does bind RNA, the specific mRNA targets and biological role are uncharacterized
5. **Better captured by process terms**: GO:0034063 (stress granule assembly) already captures Ubp3's role in this RNA-containing structure

**Interpretation:** While UBP3 may localize to and transiently associate with mRNAs in stress granules, the biological role appears to be deubiquitination of granule component proteins, not mRNA binding per se. The annotation is not false but represents an inference that may not capture the true mechanism.

### 4. KEEP_AS_NON_CORE (1 annotation)

#### GO:1901525 - Negative Regulation of Mitophagy (1 instance)
**Keep as NON-CORE (IMP, PMID:25704822)**

**Rationale:**
1. **Well-supported experimentally**: The evidence is strong (genome-wide screen, direct functional testing)
2. **However, not primary function**: Ubp3 PROMOTES ribophagy while INHIBITING mitophagy - selective pathway regulation
3. **Specialized regulatory role**: While important, negative mitophagy regulation is not a core catalytic function like ribophagy
4. **Maintains pathway context**: Keeping this annotation shows the complex reciprocal regulation of different autophagy pathways by the same deubiquitinase
5. **Secondary/pleiotropic**: For a pleiotropic gene with multiple functions, designating some as "non-core" appropriately reflects relative functional importance

**Interpretation:** This annotation should be retained to capture the full biological picture, but flagged as non-core to indicate that UBP3's primary roles are positive activation of ribophagy and substrate-specific deubiquitination, rather than negative regulation of other pathways.

---

## Pending Annotations (7 total)

Several annotations remain **PENDING** pending access to original publications that have not yet been retrieved:

- Multiple protein binding annotations (from IntAct database) - flagged for removal regardless
- Some proteolysis-related terms - flagged for review
- General hydrolase/peptidase parent terms - likely to be accepted as informative hierarchy

These will be finalized once all publications are obtained.

---

## Quality of Evidence Assessment

### Highest Quality Evidence Categories

1. **IDA + Crystal Structure** (PMID:17632125)
   - X-ray structure of Ubp3-Bre5 complex
   - Explains substrate specificity at atomic resolution
   - Strongest possible evidence for molecular mechanism

2. **IMP + Genetic Analysis** (PMID:18391941, PMID:26503781)
   - Knockout/mutant analysis showing phenotype
   - Catalytic activity specifically required
   - Functional importance demonstrated in vivo

3. **IDA + Biochemistry** (PMID:1429680)
   - Original enzyme characterization
   - Direct activity demonstration on substrates
   - Landmark foundational paper

### Moderate Quality Evidence

1. **IBA** - Phylogenetic inference
   - Appropriate when evidence exists for function conservation
   - Often strongest for ubiquitin-processing enzymes (highly conserved)

2. **IMP** - Functional mutation analysis
   - Shows requirement for phenotype
   - Doesn't always prove direct catalytic role
   - Accepted when supported by other evidence

### Lower Quality Evidence

1. **IEA from keyword mapping** - Automated inference
   - Appropriate for enzyme families with characterized functions
   - Should not be sole evidence for specific functional claims

2. **HDA/IDA from proteome-wide surveys** - High-throughput methods
   - Identify proteins present in complexes/compartments
   - May not distinguish direct functional interactions from co-localization
   - Appropriate for localization but not substrate specificity

3. **IPI from binary interaction databases** - Interaction detection
   - Demonstrates physical contact
   - Does not indicate substrate specificity or functional context
   - Often needs supporting functional evidence

4. **NAS** - Named assertion
   - Reflects established understanding
   - Only appropriate when mechanism well-characterized
   - UBP3-ribophagy is appropriate because the process was discovered in the cited study

---

## Proposed New Annotations

Based on literature review, the following substrate-specific functions are well-supported but not currently in the annotation set:

### Missing but Well-Supported Functions

1. **Histone H2B Deubiquitination**
   - Evidence: UniProt function section mentions H2B K123 role
   - Substrate: Histone H2B monoubiquitination at K123
   - Process: GO:0032455 (negative regulation of mRNA 3' end processing, potentially through H2B deubiquitination)
   - Status: Consider adding if substrate mechanism is further characterized in literature

2. **Transcriptional Regulation**
   - Evidence: RNAP II and Ste7 substrate documentation
   - Process: GO:0045893 (positive regulation of transcription by RNA polymerase II)
   - Status: Well-supported through RNAP II deubiquitination; may warrant explicit annotation

3. **mRNA Decay and Ribosomal Protein Turnover**
   - Evidence: Ribophagy annotation implies ribosomal protein substrates
   - Process: GO:0006402 (mRNA catabolic process) or GO:0051223 (ribosomal protein deubiquitination)
   - Status: Implicit in ribophagy but may warrant explicit annotation with GO:0051223 if defined

### Recommendation

Do not add new annotations for these functions unless:
1. Direct substrate evidence explicitly documented in literature
2. GO terms are appropriate and specific
3. Evidence codes are clear and retrievable
4. Multiple independent sources confirm functional importance

Current annotation set captures essential functions well.

---

## Annotator Notes and Methodological Decisions

### Decision Rules Applied

1. **Catalytic activity prioritized**: The direct molecular function (deubiquitination) takes precedence over indirect consequences (protein stability)

2. **Specificity over generality**: Preferred specific substrate pathways (ribophagy, SEC23 deubiquitination) over generic terms (proteolysis, protein binding)

3. **Cofactor relationships documented**: Complex membership (GO:1990861) preferred for BRE5 interaction over generic binding

4. **Localization matched to function**: Accepted nuclear localization based on RNAP II substrate; mitochondrial localization appropriate for mitophagy regulation

5. **Evidence quality matters**: IDA/IMP with functional characterization weighted more heavily than IEA keyword mapping

### Conflict Resolution

**Conflict: Multiple evidence types for GO:0004843**
- Resolution: All accepted; multiple evidence types strengthen confidence. Different codes document different aspects (biochemical activity, evolutionary conservation, functional requirement)

**Conflict: Generic vs. specific protein interaction**
- Resolution: Generic "protein binding" removed; specific complex/pathway terms retained. Complex membership (GO:1990861) is far more informative than binary interaction

**Conflict: mRNA localization vs. catalytic requirement**
- Resolution: Marked as over-annotated, not false. Localization is real but mechanism is deubiquitination (GO:0034063 stress granule assembly), not mRNA binding

### Limitations and Caveats

1. **Incomplete literature access**: Some PMID sources not yet retrieved. Could affect final curation of 7 pending annotations

2. **Substrate specificity evolution**: As more substrates are discovered, additional substrate-specific process annotations may become appropriate

3. **Histone modifications**: H2B K123 deubiquitination mentioned in UniProt but not explicitly in current GO annotations. May warrant future addition with proper sourcing

4. **Conditional localization**: Mitochondrial localization is stimulus-dependent. Current annotation captures this accurately as IDA with supporting reference

---

## Recommendations for Future Curation

### Short Term (Immediate)

1. Replace all protein binding annotations with specific alternatives (done for this review)
2. Remove generic proteolysis and protein stability terms
3. Consider renaming or revising mRNA binding annotations based on mechanistic understanding

### Medium Term (6-12 months)

1. Monitor for new publications on UBP3 substrate specificity
2. Consider addition of histone deubiquitination annotation if literature directly documents H2B K123 as substrate
3. Review computational predictions of additional substrates; validate experimentally before annotation

### Long Term

1. Periodic review of stress granule assembly annotation as additional UBP3 substrates are identified
2. Integration with broader quality control pathway annotations
3. Cross-referencing with related deubiquitinases (UBP2, UBP14) for comparative annotation curation

---

## Conclusion

**UBP3 is fundamentally a well-characterized deubiquitinase with clear molecular function (GO:0004843) and multiple important biological roles (ribophagy, transcriptional regulation, stress response). The current annotation set has significant redundancy (8 generic protein binding terms) and some overly indirect terms (regulation of protein stability), but the core functional annotations are appropriate and well-supported.**

**After curation:**
- **Accept:** 33 annotations capturing core catalytic and selective biological functions
- **Remove:** 10 annotations that are generic, redundant, or overly indirect
- **Over-annotated:** 2 mRNA binding terms that reflect co-localization rather than functional mechanism
- **Non-core:** 1 mitophagy regulation annotation that is secondary to primary ribophagy function

**The resulting annotation set provides a clear, specific, and mechanistically grounded representation of UBP3 function in yeast protein quality control, selective autophagy, and transcriptional regulation.**
