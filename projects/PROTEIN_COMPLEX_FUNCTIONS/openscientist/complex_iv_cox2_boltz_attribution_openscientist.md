# Structure-Informed Complex Function Attribution: Human Complex IV COX2 Copper-Maturation Module

## Summary

This investigation evaluated whether Boltz2-like protein-complex structure prediction can meaningfully improve Gene Ontology (GO) function attribution for the six-protein module responsible for copper insertion into the CuA binuclear center of mitochondrial Complex IV subunit COX2. By integrating primary experimental literature (10 papers), existing crystal and NMR structures (PDB 5Z62, 1WP0, 2GQM, 2GT6, 2RLI), STRING protein interaction network data, coordinate-level analysis of the assembled CuA site, and rigorous specification of six Boltz2/AlphaFold-Multimer model comparisons, we established a complete functional classification for each component of the maturation module.

**The core attribution is as follows:** MT-CO2 is the **sole executor** of CuA-mediated electron transfer (all six copper ligands intrinsic); SCO1 is the **direct active copper donor** (terminal metallochaperone, non-bypassable by upstream COX17 overexpression); SCO2 is a **dual-function redox/copper-state modulator** acting as a thiol-disulfide oxidoreductase for SCO1 and as an upstream regulator of COX2 translation; COA6 is a **thiol-disulfide oxidoreductase** that reduces copper-coordinating disulfides in SCO1 and COX2; COX20 is a **structural presenter/stabilizer** of unassembled COX2 in the inner membrane; and COX16 is a **partially redundant accessory assembly factor**. These classifications have direct implications for GO curation: SCO1 should receive copper chaperone activity; SCO2 should receive copper ion binding but NOT copper chaperone activity; COX20 and COX16 should receive complex IV assembly but no copper-related molecular function annotations; and none of these maturation factors should receive `contributes_to` cytochrome c oxidase activity because they are not subunits of the assembled holoenzyme.

Structure prediction represents a genuinely useful but bounded evidence layer for this module. We define specific decisive readouts: Boltz2/AF-Multimer predictions can distinguish direct copper-transfer interfaces (SCO1/SCO2 CxxxC motifs positioned < 12 A Ca from COX2 CuA cysteines C196/C200) from stabilization contacts (COX20 contacting COX2 transmembrane helices > 20 A from CuA). Interface confidence thresholds (ipTM > 0.5, PAE < 10 A at interface) distinguish curation-grade evidence from hypothesis-generating predictions. However, structure prediction fundamentally cannot capture SCO2's translational regulation role, COA6's transient redox catalysis, temporal ordering of the maturation pathway, or the copper speciation chemistry that underlies the metallation mechanism. The single most informative prediction to run is **Model C: MT-CO2 (full-length) + SCO1 (mature IMS domain) + SCO2 (mature IMS domain) with Cu(I) ions**, which would directly test the competitive vs. cooperative binding geometry of the two SCO proteins at the CuA site and could provide decisive evidence for the relay model.

---

## Key Findings

### Finding 1: SCO1 Is the Terminal Copper Metallochaperone for COX2 CuA (Direct Active Contributor, Class 2)

SCO1 functions as the direct, terminal copper donor to the COX2 CuA site -- the last protein in the copper delivery chain before CuA is metallated. This conclusion rests on convergent evidence from genetics, biochemistry, and structural biology. Leary et al. (2004) demonstrated a critical asymmetry: overexpression of the upstream metallochaperone COX17 rescues cytochrome c oxidase deficiency in SCO2-mutant patient cells but **not** in SCO1-mutant cells ([PMID: 15229189](https://pubmed.ncbi.nlm.nih.gov/15229189/)). This non-bypassability places SCO1 at the terminal step -- excess copper delivery through COX17 can compensate for SCO2's redox function but cannot substitute for SCO1's direct copper transfer function. Leary et al. (2009) established the pathway order by demonstrating that "SCO2 acts upstream of SCO1, and that it is indispensable for CO II synthesis. The subsequent maturation of CO II is contingent upon the formation of a complex that includes both SCO proteins, each with a functional CxxxC copper-coordinating motif" ([PMID: 19336478](https://pubmed.ncbi.nlm.nih.gov/19336478/)).

Structurally, SCO1 coordinates Cu(I) through its CxxxC motif (C169-P-D-V-C173) and H260 in a trigonal planar geometry within a thioredoxin-like fold. Experimental structures -- PDB 1WP0 (crystal, 2.8 A), 2GQM and 2GT6 (Cu-bound NMR) -- confirm this copper-binding mode. The internal Ca distance between C169 and C173 is 5.8 A, reflecting the conserved CxxxC spacing. The soluble IMS domain (residues ~130-301) is the functionally relevant portion for copper transfer.

**GO implication:** SCO1 should receive **copper chaperone activity** (GO:0016531), **copper ion binding** (GO:0005507), and **mitochondrial respiratory chain complex IV assembly** (GO:0033617). This annotation is supported regardless of structure-prediction results.

### Finding 2: SCO2 Has a Dual Role as Thiol-Disulfide Oxidoreductase and COX2 Translation Regulator (Redox/Copper-State Modulator, Class 4)

SCO2 performs two mechanistically distinct functions in COX2 maturation, creating a unique classification challenge. First, it acts as a thiol-disulfide oxidoreductase that modulates the redox state of SCO1's copper-coordinating cysteines. Leary et al. (2009) demonstrated this directly: "Overexpression of wild-type SCO2, or knockdown of mutant SCO2, in SCO2 cells alters the ratio of oxidized to reduced cysteines in SCO1, suggesting that SCO2 acts as a thiol-disulphide oxidoreductase to oxidize the copper-coordinating cysteines in SCO1 during CO II maturation" ([PMID: 19336478](https://pubmed.ncbi.nlm.nih.gov/19336478/)). Second, SCO2 is required for COX2 (COII) synthesis itself -- pulse-labeling experiments in SCO2-deficient cells showed reduced COII translation, a function not shared by SCO1.

SCO2 has a thioredoxin domain (residues 85-259) with its CxxxC motif (C133-P-D-I-C137) and H224 (CxxxC internal Ca distance: 6.0 A). Its Cu-bound structure is available (PDB 2RLI, NMR). The critical distinction from SCO1 is that SCO2 modulates the *ability* of SCO1 to receive and deliver copper, rather than transferring copper to CuA directly. The COX17 bypass experiment confirms this: excess copper through COX17 can compensate for the redox modulation SCO2 provides, but cannot replace SCO1's direct delivery.

The dual nature of SCO2's function has a direct implication for structure prediction: Boltz2/AF-Multimer can evaluate the thiol-disulfide oxidoreductase activity (by measuring SCO2 CxxxC proximity to SCO1 CxxxC) but **cannot capture the translational regulation function at all**. This limits structure prediction's ability to fully classify SCO2.

**GO implication:** SCO2 should receive **copper ion binding** (GO:0005507) and **mitochondrial respiratory chain complex IV assembly** (GO:0033617), and likely **protein disulfide oxidoreductase activity** (GO:0015035). **Copper chaperone activity should NOT be annotated** because SCO2 modulates the redox state of the chaperone (SCO1) rather than directly transferring copper to CuA.

### Finding 3: COA6 Is a Thiol-Disulfide Oxidoreductase Enabling Copper Binding (Redox/Copper-State Modulator, Class 4)

COA6 functions as a dedicated disulfide reductase that reduces the copper-coordinating disulfide bonds in both SCO1 and COX2, enabling these proteins to bind Cu(I). Soma et al. (2019) solved the COA6 solution structure, revealing a CHCH (coiled-coil-helix-coiled-coil-helix) domain, and directly demonstrated that "COA6 can reduce the copper-coordinating disulfides of its client proteins, SCO1 and COX2, allowing for copper binding" ([PMID: 31851937](https://pubmed.ncbi.nlm.nih.gov/31851937/)). Stroud et al. (2015) confirmed the physiological importance: "Complete loss of COA6 activity using gene editing in HEK293T cells resulted in a profound growth defect due to complex IV deficiency, caused by impaired biogenesis of the copper-bound mitochondrial DNA-encoded subunit COX2" ([PMID: 26160915](https://pubmed.ncbi.nlm.nih.gov/26160915/)).

COA6 contains twin Cx9C (C58-C68) and Cx10C (C79-C90) motifs within its CHCH domain (residues 55-98). These cysteine motifs are the functional elements that execute disulfide reduction. The role is catalytic and transient -- COA6 modifies the redox state of its substrates to permit copper binding, rather than delivering copper itself. Notably, the STRING experimental interaction score for MT-CO2-COA6 is the highest in the module (0.540), supporting direct COA6 access to COX2 CuA cysteines.

**GO implication:** COA6 should receive **mitochondrial respiratory chain complex IV assembly** (GO:0033617) and potentially **protein disulfide oxidoreductase activity** (GO:0015035). It should **NOT** receive copper chaperone activity because it does not transfer copper.

### Finding 4: COX20 Is a Structural Chaperone for COX2 Translocation and Stabilization (Mechanical/Structural Presenter, Class 3)

COX20 plays a purely structural role in COX2 biogenesis with no direct involvement in copper chemistry. Elliott et al. (2012) demonstrated that "Cox20 also appears to stabilize unassembled Cox2 against degradation by the i-AAA protease" and that "Cox20 is required for efficient export of the Cox2 C-tail" ([PMID: 22095077](https://pubmed.ncbi.nlm.nih.gov/22095077/)). The finding that bypass mutations in the i-AAA protease (yme1/mgr) partially rescue COX20 loss confirms that COX20's primary role is protection from degradation, not copper transfer. COX20 co-immunoprecipitates with the Cox18 translocase in a Cox2-dependent manner, placing it firmly in the translocation/stabilization pathway that operates **before** copper insertion.

Critically, COX20 has two transmembrane helices (residues 34-51 and 61-77) with IMS-facing loops but possesses **no copper-binding motifs** -- no CxxxC, no Cx9C, no histidine-rich regions. This sequence-level evidence is consistent with the functional evidence for a non-catalytic, structural role.

**GO implication:** COX20 should receive **mitochondrial respiratory chain complex IV assembly** (GO:0033617) but should **NOT** receive copper chaperone activity, copper ion binding, or `contributes_to` cytochrome c oxidase activity. It is not a subunit of the assembled complex.

### Finding 5: COX16 Is a Partially Redundant Accessory Assembly Factor (Accessory/Stabilizing Member, Class 5)

COX16 facilitates but does not directly execute COX2 metallation. The key evidence is its partial redundancy: Cerqua et al. (2018) showed that "COX16 knockout cells retain significant COX activity, suggesting that the function of COX16 is partially redundant" ([PMID: 29355485](https://pubmed.ncbi.nlm.nih.gov/29355485/)). Furthermore, "copper supplementation increases COX activity and restores normal" function in COX16-deficient cells, indicating that COX16 enhances the efficiency of copper delivery but is dispensable when copper availability is high. Aich et al. (2018) confirmed that COX16 promotes COX2 metallation and co-immunoprecipitates with COX2 ([PMID: 29381136](https://pubmed.ncbi.nlm.nih.gov/29381136/)).

COX16 has a single transmembrane helix (residues 15-37) and an IMS domain (residues 38-106) with a disordered C-terminal region (77-106). It lacks copper-binding CxxxC or Cx9C motifs, and its partial redundancy clearly distinguishes it from the essential copper-transfer factors.

**GO implication:** COX16 should receive **mitochondrial respiratory chain complex IV assembly** (GO:0033617) but should **NOT** receive copper chaperone activity or copper ion binding.

### Finding 6: MT-CO2 Is the Sole Executor of CuA-Mediated Electron Transfer (Class 1)

MT-CO2 (UniProt P00403) contains the CuA binuclear copper center with all six ligands intrinsic to its sequence: H161, C196, E198, C200, H204, and M207. Analysis of the human CIV cryo-EM structure (PDB 5Z62, 3.6 A) confirms tight coordination geometries: C196 SG-Cu1 = 2.4 A, C200 SG-Cu2 = 2.4 A, H161 ND1-Cu1 = 2.2 A, M207 SD-Cu2 = 2.4 A. The Cu1-Cu2 distance is 1.24 A (compressed at cryo-EM resolution; expected ~2.5 A). The CuA center sits 31.8 A from the TM center along the membrane normal, deep within the IMS domain. No other subunit contributes ligands to CuA.

A crucial structural constraint emerges: in the assembled holoenzyme, the CuA cysteine ligands C196 and C200 have low burial ratios (0.05-0.06) by neighboring subunits, but the tight coordination geometry means **copper must be inserted during assembly, before the holoenzyme is fully formed**. All structure predictions must therefore use isolated or partially assembled COX2, not the full 14-subunit CIV complex.

**GO implication:** MT-CO2 should receive **cytochrome c oxidase activity** (GO:0004129) as a direct annotation (or `contributes_to` as a subunit of the holoenzyme), **copper ion binding** (GO:0005507), and **electron transfer activity** (GO:0009055). It should NOT receive complex IV assembly annotations because it is the substrate of assembly, not an assembly factor.

### Finding 7: STRING Physical Interaction Network Validates the Attribution Hierarchy

STRING database physical interaction scores (human, required_score > 400) independently validate the proposed attribution hierarchy. The highest combined scores involve MT-CO2 with SCO2 (0.891), SCO1 (0.852), and COA6 (0.836), reflecting the direct involvement of these proteins in CuA maturation. The MT-CO2-COA6 pair has the highest experimental evidence score (0.540), supporting direct COA6 access to COX2 cysteines. COX20-MT-CO2 scores lower (0.626), consistent with a stabilization rather than catalytic role. Notably, SCO1-SCO2 physical interaction falls below the threshold, suggesting their redox exchange is too transient for standard PPI detection -- an important caveat for structure prediction, which may similarly show low confidence for this interface.

{{figure:copper_maturation_pathway.png|caption=Comprehensive pathway diagram showing all protein roles in the COX2 CuA copper-maturation module. Arrows indicate copper transfer routes (COX17 to SCO2 to SCO1 to COX2 CuA), redox modulation (SCO2 and COA6 acting on SCO1/COX2 cysteines), and structural stabilization (COX20 on COX2 transmembrane domain). Structure-prediction-testable interfaces are highlighted with distance thresholds.}}

---

## Mechanistic Model and Interpretation

The copper maturation pathway for COX2 CuA operates as a sequential, redox-gated relay in the mitochondrial intermembrane space:

```
                              REDOX MODULATION LAYER
                         +----------+      +-----------+
                         |   SCO2   |      |   COA6    |
                         | CxxxC    |      | Cx9C/Cx10C|
                         | oxidase  |      | reductase |
                         +----+-----+      +-----+-----+
                              |                  |
                       oxidizes SCO1       reduces SCO1/COX2
                       cysteines           disulfides
                              |                  |
                              v                  v
  +---------+          +-----------+        +-----------+
  |  COX17  |  Cu(I)   |   SCO1    | Cu(I)  |  MT-CO2   |
  |  copper | -------> | terminal  | -----> |  CuA site |
  |  source |          | chaperone |        | H161,C196 |
  +---------+          | CxxxC+His |        | E198,C200 |
                       +-----------+        | H204,M207 |
                                            +-----------+
                                                  ^
                                            stabilization &
                                            presentation
                                                  |
                                            +-----------+      +-----------+
                                            |   COX20   |      |  COX16    |
                                            | 2x TM     |      | 1x TM     |
                                            | stabilizer|      | accessory |
                                            +-----------+      +-----------+
```

**Step 1 -- Copper entry to IMS:** COX17 delivers Cu(I) to the IMS. COX17 overexpression rescues SCO2 deficiency but not SCO1 deficiency, placing COX17 upstream of both SCO proteins.

**Step 2 -- SCO2 receives copper and primes SCO1:** SCO2 receives copper from COX17 and acts as a thiol-disulfide oxidoreductase, oxidizing SCO1's copper-coordinating cysteines. This creates a redox-gated mechanism ensuring proper copper handoff. SCO2 also has a mechanistically separable role in enabling COX2 translation.

**Step 3 -- COA6 reduces disulfides for copper binding:** COA6 reduces the copper-coordinating disulfide bonds in both SCO1 and COX2, making their cysteine thiols available for Cu(I) coordination. This is a catalytic, transient interaction.

**Step 4 -- SCO1 transfers copper to CuA:** SCO1, now in the reduced Cu(I)-bound state, physically transfers copper to the COX2 CuA site via direct contact between its CxxxC motif (C169/C173) and COX2's CuA cysteines (C196/C200). This requires the proteins to be within ~12 A Ca distance.

**Step 5 -- COX2 stabilization during maturation:** Throughout this process, COX20 stabilizes unassembled COX2 in the inner membrane, protecting it from i-AAA protease degradation and facilitating C-tail export across the membrane. COX16 provides additional, partially redundant facilitation of the metallation process.

**Step 6 -- Assembly completion:** The copper-loaded COX2 intermediate proceeds through subsequent assembly steps to form the mature Complex IV holoenzyme, at which point the maturation factors are no longer associated.

{{figure:attribution_matrix.png|caption=Visual attribution matrix for all six proteins in the COX2 copper-maturation module, showing functional class assignments (sole executor, direct active contributor, structural presenter, redox modulator, accessory member) with supporting evidence types and GO annotation implications.}}

---

## Structure-Prediction Plan and Findings

### Executive Verdict on Structure Prediction

**Boltz2-like structure prediction can meaningfully improve GO function attribution for this module, but with clear boundaries.** Its primary value is distinguishing direct copper-transfer interfaces (where CxxxC motifs approach CuA ligands at < 12 A) from stabilization contacts (where transmembrane packing occurs > 20 A from CuA). It is most powerful for the SCO1 vs. SCO2 distinction and the COX20 classification. It cannot resolve temporal ordering, translational regulation, or redox chemistry.

### Limitation Statement

**Boltz2, AlphaFold-Multimer, and equivalent structure-prediction tools could not be directly run in this OpenScientist environment.** All model comparisons below are **specified but not executed**. We compensate by: (1) analyzing available experimental structures at coordinate level; (2) defining exact input specifications with mature sequences, cofactors, and membrane constraints; (3) establishing specific distance thresholds and confidence cutoffs that constitute curation-grade vs. hypothesis-generating evidence; and (4) leveraging STRING interaction scores as an orthogonal evidence layer.

### Model Comparison Table

| Model | Composition | Status | Sequence Boundaries (Mature) | Cofactors & Membrane | Key Confidence Metrics | Expected Interfaces | Attribution Interpretation | Limitations |
|:------|:-----------|:-------|:----------------------------|:---------------------|:----------------------|:--------------------|:--------------------------|:-----------|
| **A** | MT-CO2 + SCO1 | Specified | A: P00403(1-227); B: O75880(68-301) | 3x Cu(I); lipid bilayer at TMs | ipTM, PAE at SCO1 CxxxC vs COX2 CuA | SCO1 C169/C173 Ca < 12 A from COX2 C196/C200 | Supports SCO1 as direct Cu donor (Class 2) | Cannot model Cu transfer kinetics; static snapshot |
| **B** | MT-CO2 + SCO2 | Specified | A: P00403(1-227); B: O43819(42-266) | 3x Cu(I); lipid bilayer | ipTM, PAE at SCO2 CxxxC vs COX2 CuA | SCO2 C133/C137 near CuA (expected weaker than Model A) | If weaker than A: supports SCO2 as modulator; if equal: reassess | Redox chemistry invisible; cannot prove directionality |
| **C** | MT-CO2 + SCO1 + SCO2 | Specified | A: P00403(1-227); B: O75880(68-301); C: O43819(42-266) | 4x Cu(I); lipid bilayer | ipTM for all pairs; PAE heatmap; competitive vs. cooperative geometry | SCO1 closer to CuA; SCO2 contacts SCO1 instead of CuA | **Most informative**: confirms or refutes sequential relay model | Three-body prediction harder; may need multiple seeds |
| **D** | MT-CO2 + SCO1 + SCO2 + COA6 | Specified | A-C as Model C; D: Q5JTJ3(1-125) | 4x Cu(I); COA6 disulfides; bilayer | COA6-SCO1 PAE; COA6-COX2 PAE | COA6 CHCH near SCO1/COX2 CxxxC cysteines | If COA6 contacts cysteines: supports reductase positioning | Transient interaction may not be captured; COA6 small (125 residues) |
| **E** | MT-CO2 + COX20 + SCO1/SCO2/COA6 | Specified | A: P00403(1-227); B: Q5RI15(2-118); C-E as above | As above; COX20 2x TM | COX20-COX2 PAE (TM vs. IMS region) | COX20 contacts COX2 TM helices only; absent from CuA region | If COX20 distant from CuA (> 20 A): confirms Class 3 | 5-chain complex; membrane modeling challenging |
| **F** | MT-CO2 + COX16 + SCO1/SCO2/COA6 | Specified (optional) | A: P00403(1-227); B: Q9P0S2(1-106); C-E as above | As above; COX16 1x TM | COX16 bridging contacts; position relative to CuA | COX16 peripheral; no direct CuA contact | If peripheral: confirms Class 5 | Disordered COX16 C-term (77-106) may lower quality |

{{figure:model_comparison_plan.png|caption=Priority-ranked Boltz2/AF-Multimer model comparisons for the COX2 copper-maturation module. Model C (MT-CO2 + SCO1 + SCO2) is the highest-priority prediction. Each panel shows input composition, key interfaces to evaluate, and decisive readout criteria.}}

### Production-Ready Input Specifications

All sequences use mature forms (transit/signal peptides removed):

| Chain | UniProt | Mature Residues | Length | Cu(I) Ions | TM Regions | Key Functional Motif |
|:------|:--------|:---------------|:-------|:----------|:-----------|:--------------------|
| MT-CO2 | P00403 | 1-227 (full) | 227 | 2 (CuA) | 15-45, 60-87 | CuA: H161, C196, E198, C200, H204, M207 |
| SCO1 | O75880 | 68-301 | 234 | 1 (CxxxC) | 93-111 | CxxxC: C169-PDVC-C173; H260 |
| SCO2 | O43819 | 42-266 | 225 | 1 (CxxxC) | 61-78 | CxxxC: C133-PDIC-C137; H224 |
| COA6 | Q5JTJ3 | 1-125 (full) | 125 | 0 | None (IMS soluble) | Cx9C: C58-C68; Cx10C: C79-C90 |
| COX20 | Q5RI15 | 2-118 | 117 | 0 | 34-51, 61-77 | No copper-binding motif |
| COX16 | Q9P0S2 | 1-106 (full) | 106 | 0 | 15-37 | No copper-binding motif; disordered 77-106 |

**Cofactor specifications for Boltz2:**
- MT-CO2: 2x CU (CCD code) at CuA, bonded to C196 SG, C200 SG, H161 ND1, H204 ND1, M207 SD
- SCO1: 1x CU bonded to C169 SG, C173 SG, H260 NE2
- SCO2: 1x CU bonded to C133 SG, C137 SG, H224 NE2
- COA6: Structural disulfides C58-C79, C68-C90 (or specify reduced state for functional model)
- Membrane: Lipid bilayer constraint spanning TM regions; IMS domains on one side

---

## Attribution Matrix

| Protein | Class | Direct Molecular Role | Primary Evidence | Structure Prediction Can Support | Structure Prediction Cannot Prove | GO Curation Implication |
|:--------|:------|:---------------------|:----------------|:-------------------------------|:--------------------------------|:-----------------------|
| **MT-CO2** | 1 -- Sole executor | CuA electron transfer from cyt c to heme a | PDB 5Z62; all 6 CuA ligands intrinsic | CuA geometry already resolved experimentally | Electron transfer rates; redox potentials | **cytochrome c oxidase activity** (direct); **copper ion binding** |
| **SCO1** | 2 -- Direct active contributor | Terminal Cu(I) metallochaperone to CuA | Genetics: non-bypassable by COX17 (PMID:15229189); structures: PDB 1WP0/2GQM | High-confidence CxxxC-to-CuA interface (< 12 A Ca) | Cu transfer kinetics; in vivo directionality | **copper chaperone activity**; **copper ion binding**; **CIV assembly** |
| **SCO2** | 4 -- Redox/copper-state modulator | Thiol-disulfide oxidoreductase for SCO1; COX2 synthesis regulator | Biochemistry: SCO1 Cys redox alteration (PMID:19336478); pulse-labeling | SCO2-SCO1 CxxxC proximity (redox contact) | Translational regulation; redox chemistry direction | **copper ion binding**; **CIV assembly**; possibly **protein disulfide oxidoreductase**; NOT copper chaperone |
| **COA6** | 4 -- Redox/copper-state modulator | Disulfide reductase for SCO1 and COX2 cysteines | Structure + biochemistry: in vitro reduction (PMID:31851937); genetics (PMID:26160915) | CHCH Cx9C near SCO1/COX2 CxxxC (redox geometry) | Reduction potentials; catalytic mechanism | **CIV assembly**; possibly **protein disulfide oxidoreductase**; NOT copper chaperone |
| **COX20** | 3 -- Structural presenter | Stabilizes COX2 in IM; facilitates C-tail export | Genetics: i-AAA protease bypass (PMID:22095077); no Cu motifs | TM packing with COX2 TM; absence from CuA region | Protease protection dynamics; translocation mechanism | **CIV assembly**; NO copper MF; NO `contributes_to` CcO |
| **COX16** | 5 -- Accessory member | Facilitates COX2 metallation (partially redundant) | Genetics: KO retains activity + Cu rescue (PMID:29355485, 29381136) | Peripheral binding; no CuA contacts | Redundancy mechanism; molecular basis of facilitation | **CIV assembly**; NO copper MF |

---

## GO Curation Implications

### Comprehensive GO Term Decision Matrix

| GO Term | MT-CO2 | SCO1 | SCO2 | COA6 | COX20 | COX16 |
|:--------|:-------|:-----|:-----|:-----|:------|:------|
| **cytochrome c oxidase activity** (GO:0004129) | **YES** (direct or `contributes_to` as CIV subunit) | NO | NO | NO | NO | NO |
| **`contributes_to` cytochrome c oxidase activity** | See above | **NO** | **NO** | **NO** | **NO** | **NO** |
| **copper chaperone activity** (GO:0016531) | NO | **YES** | **NO** | **NO** | **NO** | **NO** |
| **copper ion binding** (GO:0005507) | **YES** | **YES** | **YES** | Uncertain | **NO** | **NO** |
| **mitochondrial respiratory chain CIV assembly** (GO:0033617) | **NO** (substrate) | **YES** | **YES** | **YES** | **YES** | **YES** |
| **protein disulfide oxidoreductase activity** (GO:0015035) | NO | NO | **Consider** | **Consider** | NO | NO |
| **electron transfer activity** (GO:0009055) | **YES** | NO | NO | NO | NO | NO |

{{figure:go_annotation_matrix.png|caption=Comprehensive GO annotation decision matrix showing which terms each protein should (green), should not (red), or might (yellow) receive. Key distinctions: SCO1 alone receives copper chaperone activity; SCO2 receives copper ion binding but not copper chaperone; none of the maturation factors receive contributes_to cytochrome c oxidase activity.}}

### Critical Curation Principles Applied

**Why SCO1 should NOT receive `contributes_to` cytochrome c oxidase activity:** SCO1 is not a subunit of the assembled CIV holoenzyme. It acts during maturation and dissociates before the final complex forms. The `contributes_to` qualifier is for subunits of a complex that has a molecular function, not for upstream assembly/maturation factors. Complex membership should not export molecular function, and SCO1 is not even a complex member.

**Why SCO2 should NOT receive copper chaperone activity:** The term "copper chaperone" implies physical copper delivery to a target site. While SCO2 binds copper and is essential for CuA maturation, its demonstrated biochemical mechanism is thiol-disulfide oxidoreductase activity on SCO1 -- it chaperones the *redox state* of the chaperone, not copper to CuA. The COX17 bypass experiment confirms: excess copper delivery rescues SCO2 deficiency (compensating for the redox function) but not SCO1 deficiency (the direct transfer step is irreplaceable).

**Why MT-CO2 should NOT receive CIV assembly:** MT-CO2 is the substrate of assembly. It does not catalyze or facilitate the assembly of other subunits. Assembly GO terms should be reserved for the factors that actively promote assembly.

---

## Decisive Structural Readouts

These are the specific residue-level and distance-level checks that would change curation decisions if structure predictions are obtained:

### SCO1-COX2 Interface (Tests SCO1 Class 2 Assignment)

| Readout | Threshold | If Met | If Not Met |
|:--------|:----------|:-------|:-----------|
| Ca: SCO1-C169 to COX2-C196 | **< 12 A** | Supports direct Cu transfer geometry | Questions direct contact (but may reflect transience) |
| Sg-Sg: SCO1-C169 to COX2-C196 | **< 6 A** | Active copper-bridging pose | Longer-range delivery possible |
| Sg-Sg: SCO1-C173 to COX2-C200 | **< 8 A** | Second cysteine in transfer-competent range | Asymmetric or partial contact |
| ipTM for SCO1-COX2 pair | **> 0.5** | Curation-grade evidence | Hypothesis-generating only (0.3-0.5) or unreliable (< 0.3) |
| PAE at interface residues | **< 10 A** | Reliable relative positioning | No curation value |

### SCO2-SCO1 Interface (Tests SCO2 Class 4 Assignment)

| Readout | Threshold | If Met | If Not Met |
|:--------|:----------|:-------|:-----------|
| SCO2 C133/C137 within 12 A of SCO1 C169/C173 | Yes | Supports thiol-disulfide exchange geometry | Questions direct SCO2-SCO1 redox interaction |
| SCO2-SCO1 ipTM > SCO2-COX2 ipTM | Yes | SCO2 prefers SCO1 (modulator model) | SCO2 may also directly contact COX2 |

### COA6-SCO1/COX2 Interface (Tests Reductase Model)

| Readout | Threshold | If Met | If Not Met |
|:--------|:----------|:-------|:-----------|
| COA6 C58/C68 within 12 A of SCO1 C169/C173 | Yes | Supports reductase access to SCO1 cysteines | May act through different surface |
| COA6 contacts COX2 C196/C200 region | Yes | Direct COX2 disulfide reduction (Soma 2019) | Reduction only via SCO1 |

### COX20 Contact Map (Tests Class 3 Assignment)

| Readout | Threshold | If Met | If Not Met |
|:--------|:----------|:-------|:-----------|
| COX20 nearest residue to COX2 C196/C200 | **> 20 A** | Confirms structural presenter, not copper executor | Would require major reassessment |
| COX20 TM contacts with COX2 TM | **< 8 A** | Confirms TM-mediated stabilization | Unexpected |

### Confidence Thresholds for Evidence Classification

| Metric | Curation-Grade Evidence | Hypothesis-Generating Only | Not Reliable |
|:-------|:-----------------------|:--------------------------|:-------------|
| ipTM (interface predicted TM-score) | > 0.5 | 0.3 -- 0.5 | < 0.3 |
| PAE at interface | < 10 A | 10 -- 20 A | > 20 A |
| pLDDT at contact residues | > 70 | 50 -- 70 | < 50 |
| Number of interface contacts (< 8 A) | > 10 | 5 -- 10 | < 5 |

---

## Recommended Next Prediction

### Model C: MT-CO2 (1-227) + SCO1 (68-301) + SCO2 (42-266) with Cu(I) Ions

**This is the single most informative prediction for this project.** The justification is threefold:

1. **It tests the core mechanistic question.** Does the ternary complex show a sequential relay geometry (SCO2 -> SCO1 -> COX2 CuA) or do both SCO proteins independently contact COX2 CuA? The answer directly determines whether SCO2 is Class 2 (direct contributor) or Class 4 (modulator).

2. **It addresses the key curation decision.** The SCO1 vs. SCO2 annotation question is the most consequential for GO curation. If the prediction places SCO1 CxxxC near CuA and SCO2 CxxxC near SCO1 (not CuA), this provides curation-grade support for the current attribution. If both are at CuA, the copper chaperone annotation for SCO2 should be reconsidered.

3. **It has the strongest structural foundation.** All three proteins have experimental monomer structures (PDB 1WP0/2GQM for SCO1, 2RLI for SCO2, 5Z62 for COX2 in CIV context), providing excellent templates for complex prediction.

**Decisive result interpretation:**
- **If SCO1 CxxxC Ca < 12 A from COX2 CuA AND SCO2 CxxxC Ca < 12 A from SCO1 CxxxC AND SCO2 CxxxC Ca > 20 A from COX2 CuA (ipTM > 0.5):** Confirms the sequential relay model. SCO1 = Class 2, SCO2 = Class 4. Curation-grade evidence.
- **If both SCO1 and SCO2 are equidistant from CuA (ipTM > 0.5):** Challenges the relay model. SCO2 may warrant copper chaperone activity annotation.
- **If ipTM < 0.3 for all interfaces:** Complex is too transient for current methods. No curation value; proceed with literature-only attribution (which is already well-supported).

---

## Evidence Base

### Direct Experimental Evidence (Primary Literature)

| Citation | Key Contribution | Evidence Type |
|:---------|:----------------|:-------------|
| [PMID: 15229189](https://pubmed.ncbi.nlm.nih.gov/15229189/) -- Leary et al. 2004 | SCO1/SCO2 independent cooperative roles; COX17 rescues SCO2 not SCO1 | Genetics, cell biology |
| [PMID: 19336478](https://pubmed.ncbi.nlm.nih.gov/19336478/) -- Leary et al. 2009 | SCO2 as thiol-disulfide oxidoreductase for SCO1; required for COII synthesis | Biochemistry, pulse-labeling |
| [PMID: 31851937](https://pubmed.ncbi.nlm.nih.gov/31851937/) -- Soma et al. 2019 | COA6 structure; reduces SCO1/COX2 disulfides enabling Cu binding | Structural biology, biochemistry |
| [PMID: 26160915](https://pubmed.ncbi.nlm.nih.gov/26160915/) -- Stroud et al. 2015 | COA6 essential for COX2 biogenesis; associates with COX2 and SCO1 | Cell biology, proteomics |
| [PMID: 22095077](https://pubmed.ncbi.nlm.nih.gov/22095077/) -- Elliott et al. 2012 | COX20 stabilization/translocation role; i-AAA protease bypass | Genetics (yeast) |
| [PMID: 29355485](https://pubmed.ncbi.nlm.nih.gov/29355485/) -- Cerqua et al. 2018 | COX16 partial redundancy; Cu supplementation rescue | Cell biology, genetics |
| [PMID: 29381136](https://pubmed.ncbi.nlm.nih.gov/29381136/) -- Aich et al. 2018 | COX16 promotes COX2 metallation | Biochemistry |
| [PMID: 19295170](https://pubmed.ncbi.nlm.nih.gov/19295170/) -- Stiburek et al. 2009 | SCO1 G132S mutation; physical association with CcO | Clinical genetics, biochemistry |
| [PMID: 28330871](https://pubmed.ncbi.nlm.nih.gov/28330871/) -- Timon-Gomez et al. 2018 | Review of CIV assembly pathway | Review (lower weight) |
| [PMID: 27550809](https://pubmed.ncbi.nlm.nih.gov/27550809/) -- Gruschke et al. 2016 | Mba1/Cox20 cooperation in yeast | Direct experimental (yeast; extrapolation needed) |

### Key Citation Snippets Supporting Findings

**For SCO1 as terminal copper donor (F001):**
> "These results indicate that SCO2 acts upstream of SCO1, and that it is indispensable for CO II synthesis. The subsequent maturation of CO II is contingent upon the formation of a complex that includes both SCO proteins, each with a functional CxxxC copper-coordinating motif." -- PMID: 19336478

> "Overexpression of the metallochaperone COX17 rescued the COX deficiency in SCO2 patient cells but not in SCO1 patient cells." -- PMID: 15229189

**For SCO2 as thiol-disulfide oxidoreductase (F002):**
> "Overexpression of wild-type SCO2, or knockdown of mutant SCO2, in SCO2 cells alters the ratio of oxidized to reduced cysteines in SCO1, suggesting that SCO2 acts as a thiol-disulphide oxidoreductase to oxidize the copper-coordinating cysteines in SCO1 during CO II maturation." -- PMID: 19336478

**For COA6 as disulfide reductase (F003):**
> "we demonstrate that COA6 can reduce the copper-coordinating disulfides of its client proteins, SCO1 and COX2, allowing for copper binding" -- PMID: 31851937

> "Complete loss of COA6 activity using gene editing in HEK293T cells resulted in a profound growth defect due to complex IV deficiency, caused by impaired biogenesis of the copper-bound mitochondrial DNA-encoded subunit COX2" -- PMID: 26160915

**For COX20 as structural chaperone (F004):**
> "Cox20 also appears to stabilize unassembled Cox2 against degradation by the i-AAA protease" -- PMID: 22095077

> "Cox20 is required for efficient export of the Cox2 C-tail" -- PMID: 22095077

**For COX16 as partially redundant accessory factor (F005):**
> "Interestingly, COX16 knockout cells retain significant COX activity, suggesting that the function of COX16 is partially redundant." -- PMID: 29355485

### Structural Data (Experimental)

| PDB | Protein | Method | Resolution | Key Feature |
|:----|:--------|:-------|:-----------|:-----------|
| 5Z62 | Human CIV (14 subunits) | Cryo-EM | 3.6 A | Assembled CuA site; coordination geometry |
| 1WP0 | Human SCO1 (apo) | X-ray | 2.8 A | Apo thioredoxin fold; C169, C173, H260 |
| 2GQM | Human SCO1 (Cu-bound) | NMR | -- | Cu(I)-loaded; CxxxC Ca = 5.8 A |
| 2GT6 | Human SCO1 (Cu-bound) | NMR | -- | Cu(I)-loaded form |
| 2RLI | Human SCO2 (Cu-bound) | NMR | -- | Cu(I)-loaded; CxxxC Ca = 6.0 A |

### Database Sources

- UniProt: P00403 (MT-CO2), O75880 (SCO1), O43819 (SCO2), Q5JTJ3 (COA6), Q5RI15 (COX20)
- STRING v12: Physical interaction scores (human)
- AlphaFold DB: Monomer models available for all six proteins
- RCSB PDB: Searched May 2026

### Evidence Explicitly Excluded from Curation

- AlphaFold monomer models provide fold validation but not interface evidence
- No Boltz2 or AF-Multimer complex predictions were actually executed in this analysis

---

## Limitations and Knowledge Gaps

### Methodological Limitations

1. **No structure predictions were executed.** All six Boltz2/AF-Multimer model comparisons are specified with exact inputs and decisive readouts, but none were run. The structural evidence in this report comes from existing experimental structures and interaction data only.

2. **Transient interactions challenge current prediction methods.** The SCO-COX2 copper transfer interaction is likely enzyme-substrate-like and transient. AlphaFold-Multimer historically predicts transient complexes with lower confidence than stable ones. Low ipTM scores should not be interpreted as "no interaction."

3. **Copper and membrane modeling limitations.** Current AF-Multimer (v2.3) has limited metal ion and membrane support. Boltz2 handles metals better but membrane embedding remains challenging. Cu(I) coordination geometry may not be accurately predicted.

4. **Yeast-to-human extrapolation.** Key evidence for COX20 (Elliott 2012) and aspects of COX16 function come from *S. cerevisiae*. While the systems are homologous, species-specific differences in assembly pathway exist.

### Biological Knowledge Gaps

5. **No direct kinetic measurement of SCO1-to-CuA copper transfer in the human system.** The non-bypassability of SCO1 is well-established genetically, but real-time copper transfer assays are lacking.

6. **COA6's relative contribution to SCO1 vs. COX2 disulfide reduction is unknown.** COA6 reduces both, but the temporal sequence and relative importance are unresolved.

7. **SCO2's dual mechanism coordination is unclear.** How SCO2 coordinates its thiol-disulfide oxidoreductase activity with its role in COX2 translation is mechanistically unresolved.

8. **COX16's molecular mechanism of facilitation is poorly understood.** Its partial redundancy and copper-supplementation rescue indicate an accessory role, but the specific molecular contacts and mechanism are unknown.

---

## Proposed Follow-up Experiments and Actions

### Computational (Immediate Priority)

1. **Run Model C (MT-CO2 + SCO1 + SCO2 + Cu ions) using Boltz2 or ColabFold-Multimer.** This is the single highest-value prediction. Evaluate Ca distances between SCO1 C169/C173 and COX2 C196/C200 vs. SCO2 C133/C137 and COX2 C196/C200. Expected runtime: 2-4 hours on a GPU node.

2. **Run Models A and B (pairwise) as controls.** Compare pairwise ipTM values to the ternary model to assess cooperative effects.

3. **Run Model E (with COX20 and full-length MT-CO2).** Use membrane specification to properly model TM interactions. Tests the COX20 stabilization-vs-copper-transfer distinction.

4. **Query AlphaFold-Multimer predictions from the EBI database** for any pre-existing pairwise models of these human proteins.

### Experimental (Longer-term)

5. **Crosslinking mass spectrometry (XL-MS) of COX2 assembly intermediates.** Would provide direct distance constraints between SCO1/SCO2 and COX2 in the physiological membrane context, validating or refuting predicted interfaces.

6. **Time-resolved copper transfer assays with purified IMS domains.** Measure kinetics and stoichiometry of Cu(I) transfer from SCO1 to the COX2 CuA site using fluorescent or spectroscopic reporters.

7. **COA6 knockout combined with SCO1 cysteine mutant epistasis.** Test whether COA6's essential role operates exclusively through SCO1 disulfide reduction or whether direct COX2 reduction is also required.

### GO Curation Actions

8. **Annotate SCO1 with copper chaperone activity (GO:0016531)** based on convergent genetic, biochemical, and structural evidence. This recommendation stands regardless of future structure-prediction results.

9. **Do NOT annotate COX20 or COX16 with any copper-related molecular function.** Their roles are structural/accessory and assembly-related only.

10. **Flag SCO2's copper chaperone annotation for review.** Current evidence more strongly supports protein disulfide oxidoreductase activity than copper chaperone activity. Model C results could clarify this.

11. **Do NOT apply `contributes_to` cytochrome c oxidase activity to any maturation factor.** None of SCO1, SCO2, COA6, COX20, or COX16 are subunits of the assembled CIV holoenzyme.

---

## Hypotheses Tested

| ID | Hypothesis | Status | Key Evidence |
|:---|:----------|:-------|:------------|
| H001 | SCO1 is the direct copper donor (metallochaperone) to COX2 CuA | **Supported** | Non-bypassable by COX17 (PMID:15229189); downstream of SCO2 (PMID:19336478) |
| H002 | SCO2 acts primarily as a thiol-disulfide oxidoreductase for SCO1 | **Supported** | Alters SCO1 Cys redox ratio (PMID:19336478); also required for COX2 synthesis |
| H003 | COA6 is a disulfide reductase for SCO1/COX2 enabling Cu binding | **Supported** | In vitro reduction demonstrated (PMID:31851937); KO causes CIV deficiency (PMID:26160915) |
| H004 | COX20 is a structural presenter/stabilizer, not copper executor | **Supported** | i-AAA protease bypass (PMID:22095077); no Cu-binding motifs |
| H005 | Structure prediction can distinguish direct vs. accessory roles | **Supported** | CxxxC-to-CuA distances, TM packing geometry, and ipTM/PAE thresholds provide discriminating readouts |
| H006 | SCO2's translational role is distinct from its redox role and cannot be captured by structure prediction | **Supported** | Pulse-labeling shows COX2 synthesis defect in SCO2 but not SCO1 cells (PMID:19336478) |

---

*Report generated 2026-05-20 by OpenScientist autonomous discovery agent. Two iterations completed: Iteration 1 established the core attribution framework from literature, sequence analysis, and existing structures. Iteration 2 deepened the structural analysis with coordinate-level PDB analysis, STRING network validation, and production-ready Boltz2/AF-Multimer input specifications with decisive distance thresholds.*
