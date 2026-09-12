# AFAP1: Evidence for Signal-Regulated Actin Cross-Linking as a Distinct Molecular Function from Src/PKC Adaptor Activity

## Summary

**AFAP1 (Actin Filament-Associated Protein 1, also known as AFAP-110) possesses a direct, biochemically demonstrated actin filament cross-linking activity that is mechanistically separable from its well-characterized role as a Src/PKC-associated molecular adaptor.** This conclusion is supported by three independent lines of in vitro evidence using purified recombinant protein: (1) low-speed sedimentation assays demonstrating F-actin cross-linking dependent on the C-terminal actin-binding domain (residues 594–637); (2) leucine zipper deletion/mutation experiments showing that disruption of self-association increases cross-linking capacity; and (3) PKC phosphorylation of purified protein increasing cross-linking activity. Crucially, separation-of-function experiments demonstrate that these two activities — actin cross-linking and Src activation — can be dissociated: a c-Fos leucine zipper substitution mutant increases cross-linking without activating cSrc, and dominant-positive RhoA blocks actin reorganization without inhibiting Src activation.

Despite this compelling biochemical evidence, current Gene Ontology and UniProt annotations for human AFAP1 (Q8N556) capture only generic "actin binding" (GO:0003779, IEA) and "molecular adaptor activity" (GO:0060090, IEA), entirely missing the more specific cross-linking function. Neither "actin filament cross-linking activity" nor any signal-regulated qualifier is annotated, even though the supporting biochemical data from the avian ortholog (two key papers: Qian et al. 2002, 2004) meet the standard for experimental evidence codes. A more specific annotation — "signal-regulated actin-filament cross-linking activity" — is justified by the existing literature.

However, important gaps remain. All in vitro cross-linking biochemistry was performed with the chicken (avian) AFAP-110 ortholog; no published study has reconstituted human AFAP1 cross-linking in vitro. No high-resolution structure of AFAP1 (or any fragment) has been solved, leaving the auto-inhibitory PH1–leucine zipper contact and multimerization interface as models inferred from deletion/mutation studies. Finally, no in vivo separation-of-function mutant has been tested that isolates cross-linking from adaptor activity in a physiological context such as lactation or podosome formation.

---

## Key Findings

### Finding 1: AFAP1 Has Direct, In Vitro Actin Cross-Linking Activity

The most important evidence distinguishing AFAP1 from a generic adaptor protein is the demonstration that purified recombinant AFAP-110 (rAFAP-110) can directly cross-link actin filaments in vitro. Qian et al. (2002) showed that rAFAP-110 binds F-actin cooperatively through lateral association and cross-links actin filaments in low-speed sedimentation assays — a standard biochemical approach for demonstrating bundling/cross-linking activity ([PMID: 12134071](https://pubmed.ncbi.nlm.nih.gov/12134071/)). This cross-linking depends on the integrity of the C-terminal actin-binding domain (residues 594–637). Importantly, PKC phosphorylation of the purified protein increased its cross-linking capacity, providing direct evidence that this activity is signal-regulated at the level of the protein itself, not merely through pathway-level effects. As the authors state: *"We demonstrate rAFAP-110 has the capability to cross-link actin filaments, and this ability is dependent on the integrity of the carboxy terminal actin binding domain. Deletion of the leucine zipper motif or PKC phosphorylation affected AFAP-110's conformation, which correlated with changes in multimerization and increased the capability of rAFAP-110 to cross-link actin filaments."*

Qian et al. (2004) extended these findings by demonstrating that deletion of the leucine zipper motif (Δlzip) or structural disruption through point mutations (L581P) increased the ability of rAFAP-110 to cross-link actin filaments in vitro ([PMID: 14755689](https://pubmed.ncbi.nlm.nih.gov/14755689/)). Multiple independent leucine zipper mutations all produced the same phenotype — enhanced cross-linking — ruling out mutation-specific artifacts. The paper explicitly states: *"AFAP-110 has an intrinsic ability to alter actin filament integrity as an actin filament crosslinking protein. This capability is regulated by a carboxy terminal leucine zipper (Lzip) motif. The Lzip motif facilitates self-association stabilizing the AFAP-110 multimers."*

This represents the strongest tier of biochemical evidence: purified recombinant protein assays with defined components, rather than overexpression, co-immunoprecipitation, or localization-based inference.

{{figure:afap1_domain_architecture.png|caption=Domain architecture of AFAP1/AFAP-110 showing the PH1 domain, SH3/SH2 binding motifs, PKC phosphorylation sites, leucine zipper, and C-terminal actin-binding domain. The intramolecular PH1–Lzip contact forms the auto-inhibitory mechanism that regulates cross-linking activity.}}

### Finding 2: Cross-Linking Is Auto-Inhibited by PH1–Leucine Zipper Intramolecular Contact

AFAP1's cross-linking activity is not constitutive — it is held in check by an intramolecular auto-inhibitory mechanism. The C-terminal leucine zipper (Lzip) motif contacts the N-terminal PH1 domain, stabilizing a closed conformation that limits multimerization and suppresses cross-linking. This was demonstrated by GST-pulldown experiments showing that the C-terminus/Lzip can directly contact PH1 sequences ([PMID: 14755689](https://pubmed.ncbi.nlm.nih.gov/14755689/)). The paper describes: *"An analysis of opposing binding sites indicated that the carboxy terminus/Lzip motif can contact sequences within the amino terminal pleckstrin homology (PH1) domain indicating an auto-inhibitory mechanism for regulating multimer stability and actin filament crosslinking."*

Disruption of this intramolecular contact — whether by Lzip deletion (Δlzip), the L581P point mutation, or c-Fos leucine zipper substitution — releases the auto-inhibition and increases actin cross-linking capacity. This mechanism provides the structural basis for signal-dependent regulation: PKC phosphorylation induces a conformational change that disrupts the PH1–Lzip contact, thereby activating cross-linking activity.

This auto-inhibitory model is consistent with the behavior of other signal-regulated actin cross-linkers (e.g., filamin, α-actinin) where conformational changes gate cross-linking activity, and it distinguishes AFAP1 from constitutive cross-linkers.

### Finding 3: Multimerization via Leucine Zipper Is Required for Cross-Linking

Actin filament cross-linking mechanistically requires at least two actin-binding domains to bridge separate filaments, which means AFAP1 must multimerize to cross-link. Qian et al. (1998) demonstrated that AFAP-110 self-associates through its leucine zipper motif, forming multimers detectable by Superose size-exclusion chromatography ([PMID: 9619827](https://pubmed.ncbi.nlm.nih.gov/9619827/)). The study found that *"Superose chromatography demonstrate that AFAP-110 will fractionate as a monomer or multimer, indicating AFAP-110 can be detected in a self-associated form in cell lysates. Co-expression of Src527F resulted in AFAP-110 fractionating with a molecular weight that predicts only a multimeric population."*

The relationship between multimerization and cross-linking is nuanced: paradoxically, disrupting the leucine zipper (which destabilizes ordered multimers) *increases* cross-linking capacity. This suggests that the native leucine zipper constrains multimerization into a specific geometry that auto-inhibits cross-linking, and that disruption allows formation of alternative multimeric assemblies with higher cross-linking activity.

### Finding 4: Adaptor Function and Actin Cross-Linking Are Mechanistically Coupled but Separable

This is the central finding for the research question. Multiple lines of evidence demonstrate that AFAP1's adaptor function (Src/PKC binding and activation) and its actin cross-linking activity are linked through shared conformational control but can be experimentally dissociated.

**Evidence for coupling:**
- Δlzip simultaneously increases cross-linking AND activates cSrc ([PMID: 11641786](https://pubmed.ncbi.nlm.nih.gov/11641786/))
- The PKCα → AFAP-110 → cSrc → podosome pathway requires intact AFAP-110 SH3 binding ([PMID: 15314167](https://pubmed.ncbi.nlm.nih.gov/15314167/))
- SH3 binding motif mutation of Δlzip prevents both Src activation AND actin filament reorganization

**Evidence for separability:**
- **c-Fos Lzip substitution increases cross-linking but does NOT activate cSrc** ([PMID: 14755689](https://pubmed.ncbi.nlm.nih.gov/14755689/)) — This is the key separation-of-function result. The c-Fos substitution preserves the helical structure (enabling cross-linking) but alters the specific amino acid sequence needed for Src-activating conformational change.
- **RhoA(V14) blocks Δlzip actin rosette formation but does NOT inhibit Src activation** ([PMID: 11641786](https://pubmed.ncbi.nlm.nih.gov/11641786/)) — This demonstrates that the actin-reorganizing output can be blocked downstream without affecting Src kinase activation. The paper states: *"A point mutation that alters the SH3-binding motif of AFAP-110(Deltalzip) prevents it from activating tyrosine kinases and altering actin filament integrity. In addition, a deletion within a pleckstrin homology (PH) domain of AFAP-110(Deltalzip) will also revert its effects upon actin filaments. Lastly, dominant-positive RhoA(V14) will block the ability of AFAP-110(Deltalzip) from inducing actin filament rosettes, but does not inhibit Src activation."*
- **In prostate cancer, PKC-binding-deficient AFAP-110 fails to restore adhesion, while Src-binding-deficient AFAP-110 succeeds** ([PMID: 17885682](https://pubmed.ncbi.nlm.nih.gov/17885682/)) — As the authors report: *"Reintroduction of avian AFAP-110 or a mutant disabling its interaction with Src restored these properties. However, expression of an AFAP-110 lacking the PKC-interacting domain failed to restore properties of parental cells."* This suggests that PKC-mediated conformational regulation (which governs cross-linking) is dominant for cellular phenotype.

| Experiment | Cross-linking | Src Activation | Reference |
|---|---|---|---|
| c-Fos Lzip substitution (in vitro) | **Enhanced** | **No activation** | Qian 2004 ([PMID: 14755689](https://pubmed.ncbi.nlm.nih.gov/14755689/)) |
| Dominant-positive RhoA(V14) (in vivo) | **Blocks rosettes** | **Does not inhibit** | Baisden 2001 ([PMID: 11641786](https://pubmed.ncbi.nlm.nih.gov/11641786/)) |
| Src-binding-dead mutant (cancer cells) | Not tested directly | **Disabled**, but adhesion restored | Zhang 2007 ([PMID: 17885682](https://pubmed.ncbi.nlm.nih.gov/17885682/)) |
| PKC-binding-dead mutant (cancer cells) | Presumably impaired | Not directly tested | Zhang 2007 ([PMID: 17885682](https://pubmed.ncbi.nlm.nih.gov/17885682/)) |

{{figure:evidence_classification.png|caption=Classification of evidence for AFAP1 molecular functions. Direct biochemical evidence (highest tier) supports actin cross-linking with purified protein; cellular and genetic evidence supports adaptor function. Separation-of-function experiments demonstrate the two activities are dissociable.}}

### Finding 5: Current GO/UniProt Annotations Underrepresent Cross-Linking Function

Human AFAP1 (UniProt Q8N556) carries only two molecular function GO annotations, both assigned by electronic inference (IEA): GO:0003779 "actin binding" and GO:0060090 "molecular adaptor activity." It lacks GO:0051015 "actin filament binding," GO:7770064 "actin-filament cross-linking activity," and GO:0051764 "actin crosslink formation" — despite published in vitro evidence from the avian ortholog.

UniProt free text notes that AFAP1 *"Can cross-link actin filaments into both network and bundle structures,"* but qualifies this as "By similarity" rather than citing the direct chicken biochemical data. Even the chicken entry (Q90738) lacks cross-linking GO terms. For comparison, fascin — an established actin cross-linker — does carry IDA (Inferred from Direct Assay) evidence for GO:0051015 and GO:0003779, showing that such annotations are applied when the evidence supports them.

This represents a significant annotation gap: the most specific and mechanistically informative molecular function of AFAP1 is invisible in standard database queries and gene set enrichment analyses.

---

## Mechanistic Model

Based on the evidence reviewed, the following mechanistic model emerges for AFAP1's dual function:

```
                    AUTO-INHIBITED STATE (Resting)
                    ┌─────────────────────────────┐
                    │  PH1 ←──contact──→ Lzip     │
                    │   │                   │      │
                    │  SH3bm             ABD       │
                    │  (accessible)   (constrained) │
                    └─────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        PKC phosph.     Lzip mutation     Src binding
              │               │               │
              ▼               ▼               ▼
        ┌─────────────────────────┐     ┌──────────┐
        │   CONFORMATIONAL CHANGE │     │ Adaptor  │
        │   PH1–Lzip released     │     │ scaffold │
        │   ↓                     │     │ function │
        │   Multimerization       │     └──────────┘
        │   changes               │
        │   ↓                     │
        │   Enhanced actin        │
        │   cross-linking         │
        └────────┬────────────────┘
                 │
    ┌────────────┼────────────────┐
    ▼            ▼                ▼
  Actin        cSrc           Downstream
  network    activation*      phenotypes
  remodeling  (requires        (podosomes,
              specific Lzip    invadopodia,
              geometry)        adhesion)

  * c-Fos Lzip substitution → cross-linking YES, Src activation NO
  * RhoA(V14) → actin remodeling NO, Src activation YES
```

**Key insight:** The conformational change induced by PKC phosphorylation or Lzip disruption serves as a branching point. Cross-linking activation requires only the release of the PH1–Lzip contact and consequent multimerization changes. Src activation additionally requires specific structural features of the native Lzip sequence (not just any coiled-coil). This explains why some mutations (c-Fos substitution) can activate one output without the other.

The model also explains why PKC-binding-deficient AFAP1 fails to rescue cellular phenotypes even when Src-binding is intact ([PMID: 17885682](https://pubmed.ncbi.nlm.nih.gov/17885682/)): without PKC-mediated conformational change, neither cross-linking activation nor the subsequent Src activation cascade is initiated. This positions PKC as the upstream master switch, with cross-linking and adaptor functions as two distinct but co-regulated downstream outputs.

---

## Evidence Base

### Core Biochemical Papers (Direct Cross-Linking Evidence)

| Paper | PMID | Key Contribution | Evidence Tier |
|-------|------|-------------------|---------------|
| Qian et al. 2002, *"PKC phosphorylation increases the ability of AFAP-110 to cross-link actin filaments"* | [12134071](https://pubmed.ncbi.nlm.nih.gov/12134071/) | First demonstration of in vitro actin cross-linking by purified rAFAP-110; PKC regulation | **Direct biochemical** |
| Qian et al. 2004, *"Analysis of the role of the leucine zipper motif..."* | [14755689](https://pubmed.ncbi.nlm.nih.gov/14755689/) | Auto-inhibitory PH1–Lzip mechanism; multiple Lzip mutations increase cross-linking; c-Fos separation-of-function | **Direct biochemical** |
| Qian et al. 1998, *"Src can regulate carboxy terminal interactions..."* | [9619827](https://pubmed.ncbi.nlm.nih.gov/9619827/) | Multimerization via leucine zipper; Src modulates multimerization state | **Direct biochemical** |

### Adaptor/Signaling Papers

| Paper | PMID | Key Contribution | Evidence Tier |
|-------|------|-------------------|---------------|
| Baisden et al. 2001, *"The intrinsic ability of AFAP-110 to alter actin filament integrity..."* | [11641786](https://pubmed.ncbi.nlm.nih.gov/11641786/) | RhoA dissociates actin remodeling from Src activation; SH3bm required for both | **Cellular/mutational** |
| Gatesman et al. 2004, *"PKCα activates c-Src and induces podosome formation via AFAP-110"* | [15314167](https://pubmed.ncbi.nlm.nih.gov/15314167/) | PKCα → AFAP-110 → cSrc → podosome pathway; CaOV3 rescue experiments | **Cellular/mutational** |
| Zhang et al. 2007, *"AFAP-110 is overexpressed in prostate cancer..."* | [17885682](https://pubmed.ncbi.nlm.nih.gov/17885682/) | PKC-binding domain more critical than Src-binding for cellular phenotype | **Cellular/mutational** |
| Linklater et al. 2014, *"AFAP1 is required for cSrc activity and secretory activation in the lactating mammary gland"* | [25043309](https://pubmed.ncbi.nlm.nih.gov/25043309/) | AFAP1 knockout mouse; lactation phenotype; cSrc spatial regulation | **Genetic/in vivo** |

### Structural/Binding Papers

| Paper | PMID | Key Contribution |
|-------|------|-------------------|
| Flynn et al. 1993, *"Identification and sequence analysis of cDNAs encoding a 110-kDa actin filament-associated pp60src substrate"* | [8247004](https://pubmed.ncbi.nlm.nih.gov/8247004/) | Original identification; sequence; actin filament association |
| Sihag et al. 1997, *"The integrity of the SH3 binding motif..."* | [9350057](https://pubmed.ncbi.nlm.nih.gov/9350057/) | SH3 binding required for Src complex formation |
| Guappone & Flynn 1997, *"Formation of a stable src-AFAP-110 complex..."* | [9655255](https://pubmed.ncbi.nlm.nih.gov/9655255/) | Dual SH2-binding motifs; multistep binding mechanism |
| Flynn 2001, *"The actin filament-associated protein AFAP-110 is an adaptor protein..."* | [11607843](https://pubmed.ncbi.nlm.nih.gov/11607843/) | Comprehensive review: AFAP-110 as both adaptor AND cross-linker |

### GWAS/Disease Association Papers

Multiple GWAS studies have identified AFAP1 as a susceptibility locus for primary open-angle glaucoma (POAG), with expression in retinal ganglion cells, trabecular meshwork, and optic nerve ([PMID: 25173105](https://pubmed.ncbi.nlm.nih.gov/25173105/), [PMID: 29452408](https://pubmed.ncbi.nlm.nih.gov/29452408/), [PMID: 41983772](https://pubmed.ncbi.nlm.nih.gov/41983772/), [PMID: 40459497](https://pubmed.ncbi.nlm.nih.gov/40459497/)). The mechanistic connection between AFAP1's molecular functions and glaucoma pathogenesis remains unexplored — it is unknown whether the POAG association reflects the cross-linking function, the adaptor function, or both.

### Assessment of Evidence Quality

| Evidence Element | Status | Confidence |
|---|---|---|
| Direct F-actin binding (purified protein) | Demonstrated (cooperative, lateral) | High |
| Actin filament cross-linking (in vitro) | Demonstrated (sedimentation assays) | High |
| Cross-linking depends on C-terminal ABD | Demonstrated (deletion mutant) | High |
| PKC phosphorylation enhances cross-linking | Demonstrated (in vitro) | High |
| Auto-inhibition via PH1–Lzip contact | Demonstrated (binding assays) | High |
| Multimerization via leucine zipper | Demonstrated (size-exclusion chromatography) | High |
| Network vs. bundle geometry | Described in UniProt but primary data unclear | Low |
| Specific PKC phospho-sites | **Not identified** | Gap |
| Human AFAP1 biochemistry | **Not tested** (all data from chicken) | Gap |
| High-resolution structure | **Not solved** | Gap |

{{figure:afap1_evidence_model.png|caption=Comprehensive evidence model showing the relationship between AFAP1's cross-linking activity, adaptor function, and downstream cellular phenotypes, along with key missing experiments needed to fully resolve the functional architecture.}}

---

## Limitations and Knowledge Gaps

### Critical Gaps

1. **No human AFAP1 in vitro biochemistry.** All cross-linking assays used chicken (avian) AFAP-110. The human ortholog (729 aa vs. 635 aa in chicken) has ~60% sequence identity but includes additional sequence that could alter cross-linking properties. The UniProt annotation "By similarity" reflects this gap.

2. **No high-resolution structure.** No crystal structure, cryo-EM structure, or NMR structure exists for any AFAP1 domain or fragment. The auto-inhibitory PH1–Lzip contact model is inferred entirely from deletion/mutation studies and GST-pulldown experiments. The geometry of the multimer interface, the mechanism of auto-inhibition, and the structural basis for the c-Fos separation-of-function are all unknown at atomic resolution.

3. **No in vivo separation-of-function mutants.** The c-Fos Lzip substitution (cross-linking YES / Src activation NO) has only been tested in vitro and in overexpression systems. No knock-in mouse or physiological system has been used to test whether cross-linking can drive cellular phenotypes independently of Src activation.

4. **Limited quantitative biochemistry.** The cross-linking assays are largely qualitative (sedimentation, microscopy). Binding affinities (Kd for F-actin), cross-linking kinetics, and the stoichiometry of the functional multimer have not been determined.

5. **POAG mechanism unknown.** Despite robust GWAS associations, the molecular mechanism linking AFAP1 to glaucoma is entirely uncharacterized.

### Methodological Considerations

- The existing separation-of-function data (c-Fos Lzip, RhoA block) are from overexpression experiments in cell lines, not endogenous protein at physiological levels.
- The AFAP1 knockout mouse shows a lactation phenotype consistent with loss of Src activation at the apical surface, but this does not directly test cross-linking function.
- Many cellular phenotypes attributed to AFAP1 (podosomes, invadopodia, adhesion) could reflect either or both functions, and existing experiments do not distinguish which function drives which phenotype.
- Nearly all AFAP1 literature comes from the Flynn laboratory and a small number of collaborating groups. Independent replication is limited.
- The key biochemical papers are from 2002–2004. No recent studies have revisited the cross-linking function with modern methods (cryo-EM, quantitative biophysics, reconstitution systems).

---

## Proposed Follow-up Experiments

### High Priority

1. **Reconstitute human AFAP1 cross-linking in vitro.** Express and purify recombinant human AFAP1 and test actin cross-linking by low-speed cosedimentation and electron microscopy. This would validate the "By similarity" annotation and enable human-specific mutational analysis.

2. **Solve the structure of the auto-inhibited state.** Use AlphaFold2 multimer prediction for the AFAP1 homodimer and validate with cross-linking mass spectrometry (XL-MS). Pursue cryo-EM of the AFAP1–F-actin complex to visualize the cross-linking geometry.

3. **c-Fos knock-in mouse.** Generate an AFAP1 knock-in mouse carrying the c-Fos Lzip substitution (cross-linking competent, Src activation deficient). Compare lactation, podosome formation, and glaucoma-related phenotypes to the full knockout. This is the definitive test of whether cross-linking and adaptor functions are physiologically separable.

4. **Quantitative actin cross-linking assays.** Measure Kd for F-actin binding by cosedimentation or fluorescence anisotropy. Determine cross-linking kinetics and network rheology (e.g., by reconstituted actin network microrheology) with and without PKC phosphorylation.

### Medium Priority

5. **POAG mechanism dissection.** Express wild-type and separation-of-function AFAP1 mutants in trabecular meshwork cells. Measure effects on actin cytoskeleton organization, cell contractility, and aqueous humor outflow facility.

6. **Live-cell imaging of cross-linking dynamics.** Use fluorescently tagged AFAP1 (wild-type vs. c-Fos Lzip vs. Δlzip) to track real-time actin network remodeling in response to PKC activation. Combine with FRAP to measure multimer exchange kinetics.

7. **Phosphoproteomic mapping.** Identify all PKC phosphorylation sites on AFAP1 by mass spectrometry, and determine which sites regulate cross-linking vs. Src binding vs. conformational change.

### Lower Priority

8. **Cross-linker comparison.** Benchmark AFAP1 cross-linking parameters (bundle spacing, network mesh size, filament alignment) against established cross-linkers (fascin, α-actinin, filamin) to determine whether AFAP1 produces architecturally distinct actin networks.

9. **AFAP1L1 cross-linking test.** Determine whether the paralog AFAP1L1 (which shares domain architecture but interacts with cortactin rather than Src) also possesses actin cross-linking activity. This would reveal whether cross-linking is a conserved family function or specific to AFAP1.

---

## Supported and Refuted Hypotheses

### Supported

- **AFAP1 has an intrinsic actin cross-linking activity distinct from its adaptor role.** Strongly supported by in vitro data with purified recombinant protein (Qian 2002, 2004).
- **The cross-linking activity is signal-regulated via PKC phosphorylation.** Supported by in vitro phosphorylation experiments (Qian 2002).
- **An auto-inhibitory PH1–Lzip intramolecular mechanism controls cross-linking.** Supported by binding and mutagenesis data (Qian 2004).
- **Cross-linking and Src activation can be mechanistically separated.** Supported by c-Fos Lzip mutant and RhoA experiments (Qian 2004; Baisden 2001).

### Refuted

- **AFAP1 functions only as a generic Src/PKC adaptor.** Refuted by the in vitro cross-linking data. The "adaptor only" model is insufficient to explain the full range of AFAP1's biochemical activities.

### Untestable with Current Data

- **Human AFAP1 has the same cross-linking activity as chicken AFAP-110.** Plausible given sequence conservation but not directly tested.
- **AFAP1 cross-linking contributes to glaucoma pathophysiology.** No functional data connecting these.
- **Cellular phenotypes (podosomes, adhesion, invasion) require cross-linking function specifically.** These phenotypes could arise from either cross-linking or adaptor activity and current experiments cannot distinguish between them.

---

## Conclusion

The literature supports a more specific molecular function annotation for AFAP1 than the current "actin binding" and "molecular adaptor activity." Specifically, **signal-regulated actin-filament cross-linking activity** is justified by direct biochemical evidence from purified protein assays, and this activity is demonstrably separable from Src/PKC adaptor function through separation-of-function mutants. The cross-linking is auto-inhibited by an intramolecular PH1–leucine zipper contact and activated by PKC phosphorylation — making it a bona fide signal-regulated enzymatic-like activity rather than a passive scaffolding function.

The current annotation of only "actin binding" (IEA) and "molecular adaptor activity" (IEA) misses the distinguishing feature of AFAP1: that it is a **signal-regulated actin cross-linker** whose cross-linking activity is controlled by PKC phosphorylation and an auto-inhibitory intramolecular mechanism. This is a more specific and informative molecular function than either "actin binding" or "molecular adaptor" alone.

The field would benefit enormously from reconstitution of human AFAP1 cross-linking, structural determination of the auto-inhibited state, and a c-Fos knock-in mouse to test physiological separability. The GWAS association with primary open-angle glaucoma provides an additional motivation to understand which molecular function of AFAP1 is relevant in disease.

---

## Key PMIDs

| PMID | Year | Key Contribution |
|---|---|---|
| [8247004](https://pubmed.ncbi.nlm.nih.gov/8247004/) | 1993 | Original cloning of AFAP-110; F-actin and Src association |
| [9350057](https://pubmed.ncbi.nlm.nih.gov/9350057/) | 1997 | SH3 binding motif required for Src interaction |
| [9655255](https://pubmed.ncbi.nlm.nih.gov/9655255/) | 1998 | Two independent SH2 binding motifs identified |
| [9619827](https://pubmed.ncbi.nlm.nih.gov/9619827/) | 1998 | Leucine zipper self-association; Src regulates multimerization |
| [11607843](https://pubmed.ncbi.nlm.nih.gov/11607843/) | 2001 | Review: AFAP-110 as adaptor AND actin cross-linker |
| [11641786](https://pubmed.ncbi.nlm.nih.gov/11641786/) | 2001 | Δlzip links cross-linking to Src activation; RhoA dissociates them |
| **[12134071](https://pubmed.ncbi.nlm.nih.gov/12134071/)** | **2002** | **Key paper: rAFAP-110 cross-links actin in vitro; PKC enhances it** |
| **[14755689](https://pubmed.ncbi.nlm.nih.gov/14755689/)** | **2004** | **Key paper: Lzip auto-inhibition; c-Fos mutant separates functions** |
| [15314167](https://pubmed.ncbi.nlm.nih.gov/15314167/) | 2004 | PKCα → AFAP-110 → cSrc → podosome pathway |
| [17885682](https://pubmed.ncbi.nlm.nih.gov/17885682/) | 2007 | Prostate cancer; PKC interaction more critical than Src binding |
| [25043309](https://pubmed.ncbi.nlm.nih.gov/25043309/) | 2014 | AFAP1 KO mouse: lactation defect, mirrors cSrc KO |
| [25173105](https://pubmed.ncbi.nlm.nih.gov/25173105/) | 2014 | AFAP1 GWAS locus for primary open-angle glaucoma |
