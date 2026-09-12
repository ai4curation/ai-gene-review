# TMEM70 Hypothesis Evaluation: ATP Synthase c-Ring Assembly Scaffold, TMEM242 Handoff, and Complex I Involvement

## Summary

**Executive Judgment: PARTIALLY SUPPORTED.**

TMEM70 functions as a dedicated oligomeric scaffold for mitochondrial ATP synthase c-ring (proton channel rotor) assembly — this central aspect of the hypothesis is strongly confirmed by convergent biochemical, genetic, and imaging evidence from multiple independent laboratories. TMEM70 oligomers within cristae membranes interact with subunit c (Su.c) monomers not yet incorporated into ATP synthase, facilitating their gradual oligomerization into the decameric c-ring. TMEM242 operates downstream in this pathway: once the c-ring is assembled on the TMEM70 scaffold, TMEM242 participates in incorporating the completed c-ring into vestigial ATP synthase Fo complexes alongside MT-ATP6, MT-ATP8, and additional membrane subunits. This sequential TMEM70 → TMEM242 → Fo completion model is well established.

The second arm of the hypothesis — that reported respiratory chain complex I (CI) defects in TMEM70-deficient cells are entirely secondary consequences of complex V failure, cristae disruption, or broader OXPHOS remodeling — is only partially supported. While clinical case series and the Tmem70 knockout mouse consistently describe an "isolated deficiency in fully assembled ATP synthase" without proportional CI defects, high-resolution complexome profiling and proximity-labeling proteomics have revealed physical interactions between TMEM70 and MCIA (mitochondrial complex I intermediate assembly) complex components (NDUFAF1, ECSIT, ACAD9, TIMMDC1), and TMEM70 loss causes accumulation of specific CI assembly intermediates. These data do not definitively establish TMEM70 as a bona fide CI assembly factor comparable to dedicated MCIA components, but they suggest the protein may have a minor facilitating role in CI membrane arm biogenesis — possibly through shared cristae membrane neighborhood occupancy or through physical coupling of CV and CI assembly machineries at cristae tips. The existing GO annotation (GO:0032981, complex I assembly, IMP evidence) should be flagged as unable to distinguish direct from indirect causation, and the annotation confidence should be downgraded pending decisive separation-of-function or temporal-rescue experiments.

---

## Key Findings

### Finding 1: TMEM70 Directly Scaffolds c-Ring Assembly via Oligomeric Su.c Intermediates

The most mechanistically informative study is that of Bahri et al. (2021), who used a combination of immunoprecipitation, two-dimensional Blue-Native/SDS-PAGE, pulse-chase metabolic labeling, and expansion super-resolution microscopy to demonstrate that TMEM70 forms large oligomeric complexes within mitochondrial cristae membranes ([PMID: 33359711](https://pubmed.ncbi.nlm.nih.gov/33359711/)). These TMEM70 oligomers interact specifically with subunit c (Su.c) molecules that are not yet incorporated into assembled ATP synthase complexes. Crucially, discrete TMEM70–Su.c complexes with increasing Su.c content were detected, providing direct evidence for a model in which the c-ring is gradually assembled — one Su.c monomer at a time — on the TMEM70 scaffold. The direct correlation between TMEM70 levels and Su.c accumulation was observed regardless of the status of other ATP synthase subunits, confirming that TMEM70 acts at the earliest stage of Fo biogenesis, specifically at subunit c membrane insertion and oligomerization.

This finding is corroborated by Kovalčíková et al. (2019), who confirmed that TMEM70 promotes subunit c incorporation into the rotor structure ([PMID: 31652072](https://pubmed.ncbi.nlm.nih.gov/31652072/)), and by the Tmem70 knockout mouse (Vrbacký et al. 2016), which showed an approximately 80% decrease in fully assembled ATP synthase with marked accumulation of F1 subcomplexes — indicating that biogenesis stalls after F1 formation but before Fo completion, precisely the step at which c-ring assembly occurs ([PMID: 28173120](https://pubmed.ncbi.nlm.nih.gov/28173120/)). As stated in the original paper: "Blue-Native electrophoresis demonstrated an isolated deficiency in fully assembled ATP synthase in the Tmem70⁻/⁻ embryos (80% decrease) and a marked accumulation of F1 complexes indicative of impairment in ATP synthase biogenesis that was stalled at the early stage, following the formation of F1 oligomer."

Topology studies (Pařenicová et al. 2014) established that TMEM70 has a hairpin structure with both N- and C-termini oriented toward the mitochondrial matrix ([PMID: 24576557](https://pubmed.ncbi.nlm.nih.gov/24576557/)). On BN-PAGE, TMEM70 was detected in multiple forms including dimers, with partial overlap with assembled ATP synthase. Immunoprecipitation confirmed mutual interactions between TMEM70 molecules but, notably, not direct interaction with fully assembled ATP synthase subunits — consistent with the model that TMEM70 acts as a transient scaffold released upon c-ring completion.

**Confidence: HIGH.** Five independent lines of evidence from multiple laboratories using complementary approaches (biochemistry, genetics, imaging) converge on the same model.

### Finding 2: TMEM242 Acts Downstream of TMEM70, Incorporating the Assembled c-Ring into Vestigial ATP Synthase Complexes

Carroll et al. (2021) demonstrated that TMEM242 interacts with both TMEM70 and ATP5MC3 (subunit c isoform 3) and participates in the assembly of the ATP synthase rotor ring ([PMID: 33753518](https://pubmed.ncbi.nlm.nih.gov/33753518/)). UniProt annotation (Q9NWH2) based on these data states that TMEM242 "participates in incorporation of c-ring into vestigial complexes" and "additionally influences incorporation of MT-ATP6, MT-ATP8, ATP5MJ, and ATP5MK." This establishes a clear sequential pathway:

1. **TMEM70** builds the c-ring by scaffolding Su.c oligomerization within the cristae membrane.
2. **TMEM242** then receives the assembled c-ring and helps incorporate it into the larger Fo module with proton channel subunits ATP6/ATP8 and additional peripheral subunits.
3. The vestigial Fo complex then joins with the pre-assembled F1 module to form the holoenzyme.

This functional partitioning is consistent with the observation that TMEM70 interacts with free Su.c (pre-assembly intermediates) while TMEM242 interacts with both TMEM70 and later-stage assembly intermediates. Both proteins share a hairpin inner membrane topology (two transmembrane helices, N-in/C-in), but TMEM70's larger matrix domain (~98 amino acids) likely mediates the homo-oligomerization contacts essential for c-ring scaffolding, while TMEM242 has a longer intermembrane space loop (~31 vs ~18 amino acids), potentially reflecting its role in coordinating subunits that span the IMS/membrane interface.

Notably, Carroll et al. (2021) also showed that TMEM242 contacts complex I membrane subunits (NDUFC2, MT-ND2, MT-ND3) and MCIA complex components, suggesting that the shared CI interaction space extends to both TMEM70 and TMEM242.

**Confidence: MODERATE-HIGH.** Based primarily on one comprehensive study (Carroll et al. 2021) with supporting UniProt curation; independent replication of the TMEM70 → TMEM242 handoff model is desirable.

### Finding 3: Complex I Involvement — Evidence Genuinely Split Between Direct Role and Secondary Effects

This is the central boundary question of the hypothesis. The evidence is genuinely mixed, and the current data do not permit a definitive conclusion.

#### Evidence Favoring a Direct TMEM70 Role in Complex I Assembly

Sánchez-Caballero et al. (2020) used BioID proximity labeling, complexome profiling, and coevolution analysis to show that "TMEM70 interacts with complex I and V and for both complexes the loss of TMEM70 results in the accumulation of an assembly intermediate followed by a reduction of the next assembly intermediate in the pathway" ([PMID: 32275929](https://pubmed.ncbi.nlm.nih.gov/32275929/)). This pattern — accumulation of one intermediate with loss of the next — is the hallmark of a genuine assembly factor rather than a nonspecific downstream effect. Three orthogonal methodologies (BioID, complexome profiling, and coevolution) all pointed to a dual CI/CV role for TMEM70.

Carroll et al. (2021) independently confirmed that TMEM70 interacts with MCIA complex components (NDUFAF1, ECSIT, ACAD9) and TIMMDC1, all of which are established CI membrane arm assembly factors ([PMID: 33753518](https://pubmed.ncbi.nlm.nih.gov/33753518/)).

A current GO annotation (GO:0032981, mitochondrial complex I assembly) exists with IMP evidence from FlyBase, and TMEM186 — a TMEM70 family member — was independently confirmed as a bona fide MCIA complex component (Formosa et al. 2020; [PMID: 32320651](https://pubmed.ncbi.nlm.nih.gov/32320651/)). This phylogenetic relationship raises the possibility that ancestral TMEM70-family proteins served both CI and CV, with TMEM70 retaining vestigial CI interactions.

#### Evidence Favoring Secondary/Indirect CI Effects

The Tmem70 knockout mouse (Vrbacký et al. 2016) described an "isolated deficiency in fully assembled ATP synthase" — the word "isolated" implies that CI was not significantly affected in this model ([PMID: 28173120](https://pubmed.ncbi.nlm.nih.gov/28173120/)). Multiple clinical case reports corroborate this finding. Shchelochkov et al. (2010) documented a TMEM70 patient whose muscle biopsy showed "activities of respiratory chain enzymes (complexes I-IV) showed no deficiency" ([PMID: 20728387](https://pubmed.ncbi.nlm.nih.gov/20728387/)). Braczynski et al. (2015) reported "almost complete ATP synthase deficiency" in four affected siblings without documented CI loss ([PMID: 26550569](https://pubmed.ncbi.nlm.nih.gov/26550569/)). The largest patient cohort study — 48 patients by Magner et al. (2015) — describes TMEM70 deficiency as an isolated complex V disorder ([PMID: 25326274](https://pubmed.ncbi.nlm.nih.gov/25326274/)).

Habersetzer et al. (2013) demonstrated in mammalian cells that ATP synthase dimerization/oligomerization impairment (via subunit e/g knockdown) leads to secondary OXPHOS decreases and mitochondrial ultrastructural changes, establishing the principle that CV disruption alone can indirectly reduce other OXPHOS complex activities ([PMID: 24098383](https://pubmed.ncbi.nlm.nih.gov/24098383/)). Cameron et al. (2011) documented severe cristae disorganization with whorled morphology in TMEM70 patient muscle, with respiratory chain complexes confined to the outer rings of the whorls — providing a direct morphological basis for secondary OXPHOS effects ([PMID: 20920610](https://pubmed.ncbi.nlm.nih.gov/20920610/)).

Furthermore, BioID is a proximity-labeling method that detects proteins within approximately 10 nm. In the densely packed cristae membrane, this distance encompasses functionally unrelated proteins that simply co-occupy the same membrane domain. The TMEM70–MCIA interaction could reflect cristae membrane co-localization without functional coupling.

#### Assessment

The strongest argument for a direct TMEM70–CI role is the complexome profiling data showing specific CI assembly intermediate accumulation upon TMEM70 loss — cristae disruption would more likely cause general destabilization rather than a specific block at a defined assembly step. However, this argument is weakened by the consistent clinical presentation as "isolated CV deficiency" across dozens of patients and in the mouse KO, and by the availability of cristae disruption as a plausible indirect mechanism.

The most parsimonious interpretation is that TMEM70 has a **minor, facilitating role** in CI membrane arm assembly through membrane proximity and possibly weak physical interactions with MCIA components — a role that is genuine but quantitatively secondary to its primary c-ring scaffold function. This facilitating role may reflect shared cristae membrane domain occupancy and the physical coupling of CV and CI biogenesis machineries rather than a dedicated assembly factor function equivalent to NDUFAF1 or ACAD9.

**Confidence: MODERATE — UNRESOLVED.** The decisive experiments to resolve this question have not yet been performed.

---

## Mechanistic Model

```
MITOCHONDRIAL INNER MEMBRANE / CRISTAE

Step 1: c-Ring Assembly (TMEM70-dependent, STRONGLY SUPPORTED)
─────────────────────────────────────────────────────────────
  Su.c monomers → TMEM70 oligomeric scaffold in cristae membrane
                       │
                  Su.c₁ → Su.c₂ → ... → Su.c₁₀ (c-ring completed)
                       │
                  TMEM70 released (transient scaffold)

Step 2: Fo Completion (TMEM242-dependent, SUPPORTED)
────────────────────────────────────────────────────
  c-ring ──→ TMEM242 ──→ incorporation with ATP6/ATP8/ATP5MJ/ATP5MK
                             │
                        Vestigial Fo complex formed

Step 3: Holoenzyme Assembly
────────────────────────────
  F1 (α₃β₃γδε) + Fo (c₁₀-a-b₈-stator) → F1Fo monomer
                             │
                        Dimerization (via e/g subunits)
                             │
                        Oligomeric rows at cristae tips

Step 4: Cristae Morphogenesis (CV oligomer-dependent)
─────────────────────────────────────────────────────
  CV dimer rows → membrane curvature → cristae tip formation
                             │
                        Proper spatial organization of CI, CIII, CIV

TMEM70 LOSS CASCADE:
  TMEM70⁻ → c-ring fails → Fo incomplete → F1 accumulates
           → CV content ↓80% → CV dimers/oligomers ↓
           → cristae disruption → secondary OXPHOS effects
           → CI: direct minor role? OR indirect via cristae? (UNRESOLVED)
```

### Key Mechanistic Interpretations

1. **TMEM70 is a bona fide CV assembly factor** — not merely an accessory protein. It provides an oligomeric platform essential for the rate-limiting step of c-ring formation from Su.c monomers.

2. **The TMEM70 → TMEM242 pathway is sequential**, with TMEM70 handling c-ring nucleation and oligomerization and TMEM242 handling c-ring integration into the Fo module. This two-step model explains why both proteins are required for CV biogenesis but have distinct biochemical interaction profiles.

3. **The CI question constitutes a genuine boundary case** between three non-exclusive mechanisms: (a) cristae disruption after CV loss secondarily impairs CI assembly; (b) TMEM70 co-occupies the cristae membrane domain with CI assembly machinery, producing proximity-based physical interactions without functional requirement; or (c) TMEM70 genuinely facilitates both CV and CI membrane arm assembly, perhaps reflecting an ancestral dual function partially retained from the common TMEM70/TMEM186 ancestor.

---

## Evidence Matrix

| # | Citation | PMID | Evidence Type | Claim Tested | Finding | Confidence | Limitations |
|---|----------|------|--------------|--------------|---------|------------|-------------|
| 1 | Bahri et al. 2021 | [33359711](https://pubmed.ncbi.nlm.nih.gov/33359711/) | Biochemical (IP, 2D-BN/SDS-PAGE, pulse-chase, expansion microscopy) | TMEM70 scaffolds c-ring assembly | TMEM70 oligomers recruit Su.c progressively; discrete TMEM70–Su.c intermediates detected | HIGH | Single study; HEK293 cells may not recapitulate all tissue contexts |
| 2 | Vrbacký et al. 2016 | [28173120](https://pubmed.ncbi.nlm.nih.gov/28173120/) | Genetic (mouse KO) | TMEM70 essential for CV biogenesis | 80% CV decrease; F1 accumulation; "isolated" CV deficiency; embryonic lethality | HIGH | KO is embryonic lethal — limited tissue/developmental analysis |
| 3 | Kovalčíková et al. 2019 | [31652072](https://pubmed.ncbi.nlm.nih.gov/31652072/) | Biochemical | TMEM70 promotes Su.c incorporation | Confirmed Su.c rotor incorporation role | MODERATE-HIGH | Limited methodological details available |
| 4 | Carroll et al. 2021 | [33753518](https://pubmed.ncbi.nlm.nih.gov/33753518/) | Biochemical (co-IP, proteomics) | TMEM242 downstream; TMEM70–CI interaction | TMEM242 incorporates c-ring into Fo; TMEM70 interacts with MCIA | MODERATE-HIGH | Co-IP may capture indirect interactions |
| 5 | Sánchez-Caballero et al. 2020 | [32275929](https://pubmed.ncbi.nlm.nih.gov/32275929/) | Proteomics (BioID, complexome, coevolution) | TMEM70 functions in CI assembly | TMEM70 loss → specific CI intermediate accumulation; dual CI/CV interactions | MODERATE | BioID detects proximity (~10 nm), not functional interaction |
| 6 | Pařenicová et al. 2014 | [24576557](https://pubmed.ncbi.nlm.nih.gov/24576557/) | Biochemical (topology, BN-PAGE, immunogold EM) | TMEM70 topology and CV interaction | Hairpin topology; TMEM70–TMEM70 oligomerization; NO direct interaction with assembled CV | MODERATE | Negative IP may reflect transient interactions |
| 7 | Habersetzer et al. 2013 | [24098383](https://pubmed.ncbi.nlm.nih.gov/24098383/) | Functional (shRNA knockdown) | CV oligomerization affects other OXPHOS | CV oligomer loss → secondary OXPHOS decrease | HIGH | Different mechanism of CV disruption than TMEM70 loss |
| 8 | Cameron et al. 2011 | [20920610](https://pubmed.ncbi.nlm.nih.gov/20920610/) | Structural (EM, immunogold, tomography) | Cristae morphology in TMEM70 deficiency | Whorled cristae; nucleoid/OXPHOS disorganization | HIGH (descriptive) | Single patient |
| 9 | Shchelochkov et al. 2010 | [20728387](https://pubmed.ncbi.nlm.nih.gov/20728387/) | Clinical | CI status in TMEM70 patients | Normal CI-IV activities in patient muscle | MODERATE | Single patient, milder mutation |
| 10 | Braczynski et al. 2015 | [26550569](https://pubmed.ncbi.nlm.nih.gov/26550569/) | Clinical | CV isolation | "Almost complete ATP synthase deficiency" without CI loss | MODERATE | Tissue-specific variation possible |
| 11 | Magner et al. 2015 | [25326274](https://pubmed.ncbi.nlm.nih.gov/25326274/) | Clinical (48 patients) | TMEM70 natural history | Consistent presentation as isolated CV deficiency | HIGH | Enzyme assays may miss partial CI defects |
| 12 | Formosa et al. 2020 | [32320651](https://pubmed.ncbi.nlm.nih.gov/32320651/) | Biochemical | TMEM186 as MCIA component | TMEM186 (TMEM70 family) is bona fide CI assembly factor | HIGH | Family member; does not prove TMEM70 shares function |
| 13 | Torraco et al. 2012 | [22986587](https://pubmed.ncbi.nlm.nih.gov/22986587/) | Biochemical/clinical | TMEM70 in CV biogenesis | Mutant TMEM70 forms HMW complexes; mediates F1 incorporation | MODERATE | Overexpression system |

---

## GO Curation Implications

### Annotations Strongly Supported (Retain or Add)

| GO Term | Aspect | Recommendation | Evidence Basis |
|---------|--------|----------------|----------------|
| Mitochondrial proton-transporting ATP synthase complex assembly (GO:0033615 or related) | P | **RETAIN — HIGH CONFIDENCE** | Multi-lab evidence: Bahri 2021, Vrbacký 2016, Kovalčíková 2019, Carroll 2021 |
| ATP synthase complex binding (or equivalent) | F | **RETAIN** | Direct Su.c binding demonstrated by IP and 2D-BN/SDS-PAGE |
| Protein complex oligomerization (GO:0051259) | P | **RETAIN** | TMEM70 oligomers, c-ring oligomerization scaffolding |
| Mitochondrial crista (GO:0030061) | C | **RETAIN** | Expansion microscopy localization (Bahri 2021) |
| **NEW: c-ring assembly scaffold activity** | F | **RECOMMEND ADDITION** | Bahri 2021 demonstrates specific scaffold function for gradual c-ring nucleation; consider whether existing GO terms capture this specific molecular activity |
| **NEW: Facilitation of subunit c membrane insertion** | P | **CONSIDER ADDITION** | TMEM70 promotes Su.c insertion and protects against proteolysis |

### Annotation Requiring Review

| GO Term | Aspect | Current Status | Recommendation | Rationale |
|---------|--------|---------------|----------------|-----------|
| Complex I assembly (GO:0032981) | P | IMP evidence (FlyBase) | **FLAG FOR REVIEW — DOWNGRADE CONFIDENCE** | IMP evidence from mutant phenotype cannot distinguish direct from indirect causation. Clinical phenotype is consistently "isolated CV deficiency." Complexome data (Sánchez-Caballero 2020) suggests possible involvement but BioID proximity ≠ functional requirement. Recommend changing to "contributes_to" qualifier or adding cautionary note pending separation-of-function experiments. |

### Annotations NOT Supported

| Potential Annotation | Recommendation | Rationale |
|---------------------|----------------|-----------|
| Complex I binding (direct, IDA) | **Do not annotate** | Only proximity-based evidence (BioID ~10 nm radius); direct binding not demonstrated for TMEM70 |
| Complex I assembly factor (dedicated, IDA) | **Do not annotate** | No evidence TMEM70 is required for CI assembly in the way core MCIA components (NDUFAF1, ACAD9, TMEM126B) are required |

### Disease and Phenotype Annotations

| Annotation | Recommendation | Evidence |
|------------|----------------|----------|
| Cristae morphology disruption | **Annotate as downstream phenotype** | Whorled cristae documented in patients (Cameron 2011) and inferred from CV oligomer loss |
| Cardiomyopathy, lactic acidosis, 3-MGA-uria | **Retain as disease associations** | Consistent across 48+ patients in largest cohort study |
| CI deficiency (when observed in some patients) | **Annotate as secondary/downstream effect of CV failure** | Not consistently present; absent in milder cases and in mouse KO |

---

## Limitations and Knowledge Gaps

### Methodological Limitations

1. **BioID proximity labeling** detects proteins within an approximately 10 nm radius. In the densely packed cristae membrane, this distance encompasses functionally unrelated proteins that simply co-occupy the same membrane domain. The TMEM70–MCIA interaction detected by Sánchez-Caballero (2020) may reflect cristae membrane co-localization rather than functional coupling. This is the single largest interpretive caveat for the CI question.

2. **Complexome profiling** after TMEM70 knockout shows CI intermediate accumulation, but this technique cannot distinguish direct assembly factor function from indirect effects of cristae disruption on CI membrane arm assembly. The CI membrane arm (ND2-module) has the most elaborate assembly pathway of all OXPHOS complexes and may be especially sensitive to cristae morphology perturbation.

3. **Clinical enzyme assays** (spectrophotometric measurement of individual complex activities) may lack sensitivity to detect partial CI defects. The consistent clinical description of "isolated CV deficiency" could reflect assay limitations rather than genuinely normal CI levels, though the consistency across dozens of patients and multiple centers argues against this.

4. **Mouse KO is embryonic lethal** (at E9.5), limiting the ability to study tissue-specific and developmental effects of TMEM70 loss in mature organisms. The early lethality may prevent secondary effects from fully manifesting.

5. **TMEM242's role** is established primarily from a single comprehensive study (Carroll et al. 2021). Independent replication using different cell types and methodologies would strengthen confidence in the sequential TMEM70 → TMEM242 model.

### Conceptual Limitations

1. **The "direct vs. indirect" dichotomy may be oversimplified.** If TMEM70 organizes a cristae membrane domain required for both CV and CI assembly, then it has a genuine organizational role for CI even though the molecular mechanism is not a direct protein–protein interaction with CI subunits. The functional boundary between "organizing the membrane environment needed for assembly" and "directly participating in assembly" is not sharp.

2. **Tissue-specific variation** in CI involvement has not been systematically assessed. CI defects may be present in some tissues (e.g., brain, which has high CI dependence and where respirasomes are abundant) but not others (e.g., heart, where the predominant phenotype is CV-driven cardiomyopathy).

3. **The phylogenetic relationship between TMEM70 and TMEM186** (a confirmed MCIA component) raises the question of whether TMEM70 retains an ancestral CI function. However, functional divergence within protein families is common, and shared ancestry does not establish shared function.

---

## Proposed Follow-up Experiments

### Decisive Experiments to Resolve the CI Boundary Question

1. **Acute degron-mediated TMEM70 depletion with time-course complexome profiling.** Attach an auxin-inducible degron (AID) tag to endogenous TMEM70 and achieve rapid depletion. Monitor CV and CI assembly intermediates by complexome profiling at 2h, 6h, 12h, 24h, and 48h post-depletion. Simultaneously monitor cristae morphology by EM at each time point. **Decision rule:** If CI intermediates accumulate within hours (before any detectable cristae disruption), TMEM70 has a direct CI role. If CI effects appear only after cristae are disrupted, the effects are secondary.

2. **Orthogonal CV disruption control.** Use ATP6/ATP8 mutations, oligomycin treatment, or TMEM242 knockout to specifically block CV assembly without removing TMEM70. Perform identical complexome profiling and compare CI intermediate profiles to TMEM70 KO. **Decision rule:** If CI intermediates show the same pattern regardless of how CV is disrupted, the effect is secondary to CV loss. If TMEM70 KO produces unique CI intermediate accumulation not seen with other CV-specific defects, TMEM70 has a specific CI role.

3. **TMEM70 separation-of-function mutants.** Map which TMEM70 domains/residues interact with Su.c vs. MCIA components using crosslinking mass spectrometry. Engineer point mutations that selectively abolish one interaction surface. Test whether CI assembly is affected only when MCIA interaction is lost. **Decision rule:** If mutations that preserve Su.c binding but eliminate MCIA binding show no CI defect, the CI interaction is nonfunctional.

4. **Cristae rescue experiment.** In TMEM70-null cells, express a dominant-active form of OPA1 or overexpress Mic60 (MICOS complex component) to force maintenance of normal cristae morphology despite CV loss. **Decision rule:** If CI levels are restored despite continued TMEM70 absence and CV deficiency, CI effects are secondary to cristae disruption.

5. **TMEM70 vs. TMEM242 double-KO epistasis for CI.** Compare CI assembly intermediate profiles in TMEM70-KO, TMEM242-KO, and TMEM70/TMEM242 double-KO. If TMEM242-KO (which disrupts CV at a later step) produces identical CI intermediate patterns, the CI effect reflects CV loss rather than a TMEM70-specific function.

### Additional Informative Experiments

6. **CryoEM of TMEM70-Su.c intermediates.** Determine the structure of TMEM70 oligomers bound to Su.c at different stages of c-ring assembly. This would reveal the molecular mechanism of c-ring scaffolding and definitively show whether the TMEM70 structure has binding surfaces compatible with CI subunit interaction.

7. **Conditional Tmem70 KO mouse with tissue-specific analysis.** Generate a floxed Tmem70 allele and cross with tissue-specific Cre drivers (heart, brain, liver, skeletal muscle). Systematically quantify CI and CV assembly by BN-PAGE, complexome profiling, and respiratory chain enzyme assays. This would reveal whether CI involvement is tissue-specific.

8. **In vitro reconstitution.** Purify TMEM70 oligomers and test whether they can facilitate Su.c membrane insertion and c-ring formation in liposomes. If successful, add MCIA components and CI membrane subunits to test for any direct TMEM70-dependent facilitation of CI assembly in a minimal system free of cristae architecture effects.

---

## Evidence Base: Key Literature

### Core Mechanistic Studies

**Bahri et al. (2021)** — *"TMEM70 forms oligomeric scaffolds within mitochondrial cristae promoting in situ assembly of mammalian ATP synthase proton channel"* ([PMID: 33359711](https://pubmed.ncbi.nlm.nih.gov/33359711/))
The definitive study establishing TMEM70's molecular mechanism. Key quote from abstract: "TMEM70 forms large oligomers that interact with Su.c not yet incorporated into ATP synthase complexes. Moreover, discrete TMEM70-Su.c complexes with increasing Su.c contents can be detected, suggesting a role for TMEM70 oligomers in the gradual assembly of the c-ring." This provides the strongest biochemical evidence for the c-ring scaffolding model.

**Carroll et al. (2021)** — *"TMEM70 and TMEM242 help to assemble the rotor ring of human ATP synthase and interact with assembly factors for complex I"* ([PMID: 33753518](https://pubmed.ncbi.nlm.nih.gov/33753518/))
Established the functional relationship between TMEM70 and TMEM242, showing both participate in rotor ring assembly. Also documented TMEM70 interactions with MCIA complex components, providing the primary evidence for a potential direct CI role. The paper's title captures the dual finding that is central to the hypothesis evaluation.

**Sánchez-Caballero et al. (2020)** — *"TMEM70 functions in the assembly of complexes I and V"* ([PMID: 32275929](https://pubmed.ncbi.nlm.nih.gov/32275929/))
Used three orthogonal methods (BioID, complexome profiling, coevolution) to argue that "TMEM70 interacts with complex I and V and for both complexes the loss of TMEM70 results in the accumulation of an assembly intermediate followed by a reduction of the next assembly intermediate in the pathway." This is the strongest published argument for a direct CI role, though the methodology has important caveats regarding proximity vs. functional interaction.

### Genetic Model Studies

**Vrbacký et al. (2016)** — *"Knockout of Tmem70 alters biogenesis of ATP synthase and leads to embryonal lethality in mice"* ([PMID: 28173120](https://pubmed.ncbi.nlm.nih.gov/28173120/))
The gold-standard loss-of-function study. Demonstrated "an isolated deficiency in fully assembled ATP synthase in the Tmem70⁻/⁻ embryos (80% decrease) and a marked accumulation of F1 complexes." The consistent description as "isolated deficiency" without mention of CI defects is key evidence for the secondary-effects interpretation.

### Structural and Ultrastructural Studies

**Cameron et al. (2011)** — *"Complex V TMEM70 deficiency results in mitochondrial nucleoid disorganization"* ([PMID: 20920610](https://pubmed.ncbi.nlm.nih.gov/20920610/))
EM and tomography documented abnormal mitochondria with whorled cristae in TMEM70-deficient muscle. Nucleoid clusters disrupted, OXPHOS complexes confined to outer rings of whorls. Establishes the structural basis for secondary OXPHOS effects.

**Habersetzer et al. (2013)** — *"Human F1F0 ATP synthase, mitochondrial ultrastructure and OXPHOS impairment: a (super-)complex matter?"* ([PMID: 24098383](https://pubmed.ncbi.nlm.nih.gov/24098383/))
Demonstrated that CV dimerization/oligomerization impairment in mammalian cells leads to secondary OXPHOS decreases. Establishes the principle that CV structural integrity is prerequisite for normal function of other OXPHOS complexes.

### Complex I Assembly Context

**Formosa et al. (2020)** — *"Dissecting the Roles of Mitochondrial Complex I Intermediate Assembly Complex Factors in the Biogenesis of Complex I"* ([PMID: 32320651](https://pubmed.ncbi.nlm.nih.gov/32320651/))
Defined the MCIA complex and identified TMEM186 and COA1 as bona fide components. TMEM70 was not identified as a core MCIA component. TMEM186's role as a genuine CI assembly factor, combined with its phylogenetic relationship to TMEM70, informs but does not resolve the question of TMEM70's CI involvement.

### Clinical Studies

**Magner et al. (2015)** — *"TMEM70 deficiency: long-term outcome of 48 patients"* ([PMID: 25326274](https://pubmed.ncbi.nlm.nih.gov/25326274/))
The largest cohort study. Consistent clinical phenotype of isolated CV deficiency with cardiomyopathy, lactic acidosis, 3-MGA-uria, and developmental delay across multiple ethnic groups and mutation types.

---

## Conclusion

The seed hypothesis is **partially supported** based on the current evidence:

- **Strongly supported (high confidence):** TMEM70 directly assists ATP synthase c-ring assembly via oligomeric scaffolding of subunit c membrane insertion and oligomerization. Five independent lines of evidence from multiple laboratories using complementary methodologies (biochemistry, genetics, imaging) converge on this mechanism.

- **Supported (moderate-high confidence):** TMEM242 acts downstream of TMEM70, receiving the assembled c-ring and incorporating it into vestigial Fo complexes with ATP6/ATP8 and additional membrane subunits.

- **Partially supported but unresolved (moderate confidence):** The claim that complex I defects are entirely secondary consequences of complex V failure. Clinical literature consistently shows "isolated CV deficiency," and cristae disruption provides a plausible indirect mechanism. However, complexome profiling showing specific CI assembly intermediate effects (Sánchez-Caballero 2020) and physical interactions with MCIA components (Carroll 2021) suggest TMEM70 may have a minor direct facilitating role in CI membrane arm biogenesis — a role that may be genuine but quantitatively secondary to its primary CV function and likely reflective of shared cristae membrane domain occupancy.

For GO curation, TMEM70 should retain strong annotations for ATP synthase assembly and gain a specific annotation for c-ring scaffolding activity. The complex I assembly annotation (GO:0032981, IMP evidence) should be flagged for review with reduced confidence, pending separation-of-function experiments that can distinguish direct from indirect causation. The decisive experiments outlined — particularly acute degron-mediated depletion with time-course analysis and orthogonal CV disruption controls — are feasible with current technology and would definitively resolve this boundary question.
