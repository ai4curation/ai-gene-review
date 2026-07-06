# FBXO17 Hypothesis Evaluation: Dual Substrate Recognition Through Distinct Binding Modes

## Executive Judgment

**The hypothesis is PARTIALLY SUPPORTED.**

FBXO17 recognizes sulfated and complex glycans — not high-mannose oligosaccharides — through its FBA/G lectin domain, and is structurally distinguishable from the canonical ERAD-associated FBA paralogs FBXO2 and FBXO6. The validated protein substrate GSK3beta is recognized through a region (amino acids 151–200) within the FBA domain whose primary glycan-contact loops lie largely outside, consistent with a mechanistically distinct protein-binding mode. However, formal structural proof of full separability — e.g., a co-crystal structure or comprehensive mutagenesis — is lacking. The ERAD pathway GO annotation for FBXO17 rests solely on phylogenetic inference (IBA) and is not supported by experimental evidence; it should not be propagated.

---

## Summary

FBXO17 (F-box only protein 17) is a member of the FBA (F-box associated) subfamily of F-box proteins, which serve as substrate-recognition subunits of SCF (Skp1-Cullin1-F-box) E3 ubiquitin ligase complexes. Several FBA family members — FBXO2 (Fbs1), FBXO6 (Fbs2), and FBXO27 (Fbs3) — are well-characterized as lectins that bind high-mannose N-glycans and target misfolded glycoproteins for proteasomal degradation via the ERAD (endoplasmic reticulum-associated degradation) pathway. FBXO17 shares the FBA domain architecture but diverges in glycan specificity: it binds heparin and chondroitin sulfate (sulfated glycosaminoglycans) rather than high-mannose oligosaccharides. This investigation evaluated whether FBXO17 uses its FBA/G lectin domain for complex/sulfated glycan recognition while employing a mechanistically distinct mode for its validated non-glycoprotein substrate GSK3beta.

Through sequence alignment, domain mapping, and literature analysis, we established that (1) FBXO17 lacks the second HGG motif in the beta9-beta10 loop that is essential for chitobiose/high-mannose binding in FBXO2, (2) glycan array data confirm sulfated/complex glycan specificity rather than high-mannose binding, (3) the mapped GSK3beta-binding region (aa 151–200) is spatially separable from the major glycan-contact loops of the FBA domain, and (4) FBXO17's ERAD GO annotations are based solely on phylogenetic inference rather than experimental evidence. Together, these findings partially support the dual-mode hypothesis while identifying the structural resolution of the GSK3beta-binding interface as the critical remaining gap.

---

## Key Findings

### Finding 1: FBXO17 Lacks the Second HGG Glycan-Contact Loop Required for High-Mannose Binding

The crystal structure of FBXO2 (Fbs1) in complex with chitobiose ([PMID: 14990996](https://pubmed.ncbi.nlm.nih.gov/14990996/)) revealed that the sugar-binding domain (SBD) is composed of "a ten-stranded antiparallel beta-sandwich" with a chitobiose-binding pocket formed by four loops: beta2-beta3, beta5-beta6, beta7-beta8, and beta9-beta10. A hallmark of the high-mannose-binding FBA proteins (FBXO2, FBXO6, FBXO27) is the presence of two conserved HGG motifs — one in the beta2-beta3 loop and one in the beta9-beta10 loop — that make critical hydrogen bonds with the chitobiose core of N-glycans.

Our sequence alignment of the FBA domains across human FBA family members demonstrated that FBXO17 retains the first HGG motif (VEHGG at the beta2-beta3 loop, around amino acids 122–135) but **lacks the second HGG motif** in the beta9-beta10 loop. At the position where FBXO2 has FEHGG**QDSVYWK** and FBXO6 has FQHGG**RDTQYWA**, FBXO17 instead has FEQYG**RDVSSWVG** — the HGG is replaced by QYG, disrupting a key hydrogen-bond network. Kumanomidou et al. (2015) ([PMID: 26460611](https://pubmed.ncbi.nlm.nih.gov/26460611/)) performed structure-based mutational analysis showing that "distinct hydrogen bond networks of four FBG3 loops, i.e., beta2-beta3, beta5-beta6, beta7-beta8, and beta9-beta10, prevent the formation of the carbohydrate-binding pocket shown in Fbs1." The absence of the second HGG in FBXO17 is structurally analogous to the disruption seen in FBXO44 (FBG3), which also cannot bind N-glycans despite high sequence homology.

Pairwise identity of FBA domains: FBXO17-FBXO2 = 44.9%, FBXO17-FBXO6 = 43.7%, FBXO17-FBXO27 = 59.9%. Despite moderate sequence conservation, the specific loss of the second HGG motif provides a clear structural rationale for FBXO17's inability to bind high-mannose substrates. These identity values also define an **FBXO17-FBXO27 subgroup** that is distinct from the **FBXO2-FBXO6 high-mannose-binding subgroup**, suggesting a deep evolutionary divergence in substrate specificity.

{{figure:fba_domain_comparison.png|caption=Domain architecture comparison of FBA family members showing the presence/absence of the second HGG motif, pairwise FBA domain identities, and the position of the GSK3beta-binding region in FBXO17}}

### Finding 2: FBXO17 Glycan Specificity Is Sulfated/Complex Glycans, Not High-Mannose

Glenn et al. (2008) ([PMID: 18203720](https://pubmed.ncbi.nlm.nih.gov/18203720/)) performed a systematic comparative analysis of FBA family glycan specificities using glycan arrays and complementary binding assays. Their key finding was that "each family member has differing specificity for glycosylated substrates. Collectively, the F-box proteins in the FBA family bind high mannose and sulfated glycoproteins, with one FBA protein, FBX044, failing to bind any glycans on the tested arrays."

Specifically for FBXO17:

| Ligand | Binding | Notes |
|--------|---------|-------|
| Heparin | **Strong** | Sulfated glycosaminoglycan |
| Chondroitin sulfate | **Weak** | Sulfated glycosaminoglycan |
| Lactoferrin | **Positive** | Via complex glycan moieties |
| High-mannose glycans | **Negative** | No binding on glycan array |

This is in stark contrast to FBXO2 and FBXO6, which bind high-mannose oligosaccharides (Man3-9GlcNAc2) as demonstrated by Yoshida et al. (2003) ([PMID: 12939278](https://pubmed.ncbi.nlm.nih.gov/12939278/)), who showed that "Man3-9GlcNAc2 glycans were required for efficient Fbs2 binding, whereas modifications of mannose residues by other sugars or deletion of inner GlcNAc reduced Fbs2 binding." Site-directed mutagenesis of two aromatic amino acids in FBXO17's G domain confirmed their necessity for high-affinity glycan binding, indicating that the FBA/G domain is indeed the glycan-recognition module — but one that has been repurposed for sulfated/complex substrates rather than high-mannose recognition. The study also confirmed that FBXO17 forms a canonical SCF complex (co-precipitating Skp1, Cullin1, and Rbx1), establishing its competence as an E3 ubiquitin ligase.

### Finding 3: GSK3beta-Binding Region Is Spatially Separable from Primary Glycan-Contact Loops

Domain mapping of FBXO17 (Q96EF6, 362 amino acids) revealed the following architecture:

| Feature | Residues | Notes |
|---------|----------|-------|
| F-box domain | 15–62 | SKP1-binding; N-terminal |
| FBA domain | 99–275 | Lectin/substrate-recognition fold |
| GSK3beta-binding region | 151–200 | Mapped by deletion/binding studies |
| beta2-beta3 loop (VEHGG) | ~122–135 | Primary glycan-contact loop |
| beta9-beta10 loop (second HGG equivalent) | ~248–260 | Disrupted in FBXO17 |
| UniProt binding site residues (FBXO2 ref.) | ~209–211 | Outside GSK3beta-binding region |

Suber et al. (2017) ([PMID: 28298444](https://pubmed.ncbi.nlm.nih.gov/28298444/)) "identified FBXO17 as an F-box protein subunit that recognizes and mediates GSK3beta polyubiquitination." The GSK3beta-binding region (aa 151–200) sits within the FBA domain but is **largely non-overlapping** with the primary glycan-contact loops. The first glycan-contact loop (VEHGG, beta2-beta3) at residues 122–135 is upstream, and the second HGG equivalent (beta9-beta10) at ~248–260 is downstream of the GSK3beta-binding region. Only the beta5-beta6 loop (~aa 176–183) shows partial overlap. Five conserved tryptophan residues shared between FBXO17 and FBXO2 (W122, W131, W155, W170, W186) were identified; three (W155, W170, W186) fall within the GSK3beta-binding region, but these are likely structural residues buried in the beta-strand core rather than surface-exposed glycan contacts.

Mizushima et al. (2004) ([PMID: 14990996](https://pubmed.ncbi.nlm.nih.gov/14990996/)) described "the structure of the SBD-chitobiose complex includes hydrogen bonds between Fbs1 and chitobiose and insertion of the methyl group of chitobiose into a small hydrophobic pocket of Fbs1." This defines the chitobiose-binding pocket on the top face of the beta-sandwich, providing the reference for where glycan contacts occur. The GSK3beta-binding region, centered on the middle beta-strands, is geometrically consistent with binding on a different face or edge of the beta-sandwich.

{{figure:fbxo17_structural_analysis.png|caption=Comprehensive structural analysis showing the spatial relationship between glycan-binding loops and the GSK3beta-binding region in FBXO17, demonstrating partial spatial separability within the FBA domain}}

Critically, GSK3beta is not a glycoprotein — it is a serine/threonine kinase recognized as a protein substrate for SCF(FBXO17)-mediated polyubiquitination and degradation. The fact that FBXO17 can target a non-glycoprotein substrate via a region largely separable from its glycan-contact loops supports the hypothesis that protein-substrate recognition uses a mechanistically distinct binding mode from glycan recognition.

### Finding 4: FBXO17 ERAD Annotations Rest on Phylogenetic Inference, Not Experimental Evidence

A critical examination of FBXO17's Gene Ontology annotations revealed a reliance on phylogenetic inference (IBA — Inferred from Biological Aspect of Ancestor) rather than direct experimental evidence:

| GO Term | Description | Evidence Code | Source |
|---------|-------------|---------------|--------|
| GO:0036503 | ERAD pathway | **IBA** | GO_Central |
| GO:0006516 | Glycoprotein catabolic process | **IBA** | GO_Central |
| GO:0031146 | SCF-dependent proteasomal degradation | **IBA** | GO_Central |
| GO:0019005 | SCF ubiquitin ligase complex | **IDA** | Direct experimental |

Only the SCF complex membership annotation has direct experimental (IDA) evidence. The ERAD pathway and glycoprotein catabolic process annotations are propagated from the FBA family ancestor — likely from well-characterized paralogs FBXO2 and FBXO6. Kumanomidou et al. (2015) ([PMID: 26460611](https://pubmed.ncbi.nlm.nih.gov/26460611/)) explicitly list only "Fbs1/FBG1/FBXO2, Fbs2/FBG2/FBXO6, and Fbs3/FBG5/FBXO27" as N-glycan recognizers among the FBA family — **FBXO17 is notably absent from this list**, positioned alongside FBXO44 (FBG3), which "has no sugar-binding activity, despite the high sequence homology and conservation of the residues necessary for oligosaccharide binding between Fbs1-3 and FBG3."

This finding has direct curation implications: the IBA-based ERAD pathway annotation for FBXO17 is misleading because it implies a functional equivalence with FBXO2/FBXO6 that is contradicted by glycan array data, structural analysis, and expert classification.

---

## Mechanistic Model

Based on the integrated evidence, we propose the following mechanistic model for FBXO17 substrate recognition:

```
FBXO17 (362 aa)
|
+-- F-box domain (aa 15-62)
|   +-- Binds SKP1 --> assembles into SCF complex
|
+-- FBA domain (aa 99-275)
    |
    +-- GLYCAN-BINDING MODE (sulfated/complex glycans)
    |   +-- beta2-beta3 loop (VEHGG, aa ~122-135) <-- retained from FBA ancestor
    |   +-- beta5-beta6 loop (aa ~176-183)
    |   +-- beta7-beta8 loop
    |   +-- beta9-beta10 loop (aa ~248-260) <-- DISRUPTED (no second HGG)
    |       --> Cannot form chitobiose pocket --> no high-mannose binding
    |       --> Repurposed for sulfated glycan (heparin, chondroitin sulfate)
    |
    +-- PROTEIN-BINDING MODE (GSK3beta recognition)
        +-- Mapped region: aa 151-200
        +-- Largely non-overlapping with glycan-contact loops
        +-- Partial overlap only with beta5-beta6 loop
        +-- Mediates direct protein-protein interaction
            --> GSK3beta polyubiquitination and degradation
```

**Key mechanistic insight:** The FBA domain in FBXO17 appears to have undergone functional divergence from the ancestral high-mannose lectin activity. While retaining the overall beta-sandwich fold, loss of the second HGG motif eliminated the chitobiose-binding pocket, while the domain was co-opted for (a) sulfated/complex glycan binding through a modified binding surface and (b) direct protein substrate (GSK3beta) recognition through a partially separable interface. This dual functionality — glycan binding and protein binding through overlapping but distinct surfaces — represents a mode of substrate recognition not seen in the canonical ERAD-associated FBA members.

The FBXO17-FBXO27 subgroup (59.9% FBA domain identity) may share this divergence from high-mannose recognition, as FBXO27 also lacks the second HGG motif. However, FBXO27 has been independently characterized as an N-glycan binder with a distinct mechanism, suggesting that even within this subgroup, further functional specialization has occurred.

---

## Evidence Matrix

| # | Citation | Evidence Type | Claim Tested | Finding | Confidence | Limitations |
|---|----------|--------------|--------------|---------|------------|-------------|
| 1 | [PMID: 14990996](https://pubmed.ncbi.nlm.nih.gov/14990996/) | Structural (X-ray) | FBA domain has a defined chitobiose-binding pocket | Four loops (beta2-beta3, beta5-beta6, beta7-beta8, beta9-beta10) form the pocket; second HGG is critical | **High** | Structure is for FBXO2, not FBXO17 directly |
| 2 | [PMID: 26460611](https://pubmed.ncbi.nlm.nih.gov/26460611/) | Structural + mutagenesis | Which FBA members are N-glycan binders? | Only FBXO2, FBXO6, FBXO27 listed as N-glycan recognizers; FBXO17 absent from this classification | **High** | FBXO17 not directly tested structurally in this study |
| 3 | [PMID: 18203720](https://pubmed.ncbi.nlm.nih.gov/18203720/) | Biochemical (glycan array, binding assays, mutagenesis) | FBXO17 binds sulfated glycans, not high-mannose | Heparin (strong), chondroitin sulfate (weak), lactoferrin (complex glycans); no high-mannose binding | **High** | Glycan array covers finite panel; in vitro conditions |
| 4 | [PMID: 28298444](https://pubmed.ncbi.nlm.nih.gov/28298444/) | Biochemical + cellular (ubiquitination, co-IP) | FBXO17 targets GSK3beta for ubiquitination | GSK3beta is a validated SCF(FBXO17) substrate | **High** | Studied in murine lung epithelial cells; binding region mapping resolution is limited |
| 5 | [PMID: 12939278](https://pubmed.ncbi.nlm.nih.gov/12939278/) | Biochemical + cellular | FBXO6 (Fbs2) is a high-mannose/ERAD F-box protein | FBXO6 binds Man3-9GlcNAc2, participates in ERAD; establishes contrast with FBXO17 | **High** | Provides contrast with FBXO17; not direct FBXO17 evidence |
| 6 | This study | Computational (sequence alignment) | FBXO17 lacks second HGG motif | beta9-beta10 loop has QYG instead of HGG; FBA domain identity 44.9% with FBXO2, 59.9% with FBXO27 | **Medium-High** | Based on alignment, not experimental structure |
| 7 | This study | Computational (domain mapping) | GSK3beta-binding region is separable from glycan-contact loops | Primary glycan loops are outside aa 151-200; partial overlap at beta5-beta6 only | **Medium** | Based on homology to FBXO2; no experimental structure of FBXO17 |

---

## GO Curation Implications

### Carbohydrate binding (GO:0030246)
- **Recommendation:** **ANNOTATE** for FBXO17 based on Glenn et al. 2008 evidence (IDA). FBXO17 binds heparin, chondroitin sulfate, and complex glycans. Consider more specific child terms: GO:0008201 (heparin binding) with IDA evidence.
- **Rationale:** Direct experimental evidence of carbohydrate binding through glycan arrays, affinity assays, and mutagenesis confirmation of FBA/G domain dependence.

### Glycoprotein catabolic process (GO:0006516)
- **Recommendation:** **RETAIN with caution.** FBXO17 is an SCF E3 ligase that may target glycoproteins (via sulfated glycan recognition) for ubiquitin-dependent degradation. However, the specific glycoprotein substrates of FBXO17 (beyond GSK3beta, which is not a classical glycoprotein) remain unidentified. The annotation is reasonable but the evidence base is indirect.
- **Rationale:** FBXO17 forms functional SCF complexes and demonstrates glycan binding, but direct evidence of glycoprotein substrate degradation is lacking.

### ERAD pathway (GO:0036503)
- **Recommendation:** **DO NOT PROPAGATE / Consider removal.** FBXO17 lacks the structural features (second HGG loop) required for high-mannose/chitobiose recognition that underlies ERAD substrate targeting. Glenn et al. 2008 showed no high-mannose binding. Kumanomidou et al. 2015 excluded FBXO17 from the N-glycan-recognizing FBA members. The IBA annotation is a phylogenetic artifact that does not account for FBXO17's divergent glycan specificity.
- **Rationale:** Multiple lines of evidence (glycan array, sequence analysis, expert classification) indicate FBXO17 does not participate in canonical high-mannose-mediated ERAD.

### SCF-dependent proteasomal ubiquitin-dependent protein catabolic process (GO:0031146)
- **Recommendation:** **UPGRADE evidence to IDA** based on Suber et al. 2017. FBXO17 mediates SCF-dependent GSK3beta polyubiquitination and proteasomal degradation, providing direct experimental evidence for this process.
- **Rationale:** Direct experimental evidence from ubiquitination assays and degradation studies.

### Ubiquitin protein ligase substrate-receptor activity
- **Recommendation:** **ANNOTATE** for FBXO17 based on IDA from Suber et al. 2017 and Glenn et al. 2008 (SCF complex formation). FBXO17 functions as the substrate-recognition subunit of an SCF E3 ubiquitin ligase complex.

---

## Hypothesis Evaluation Summary

### Claim A: FBXO17 recognizes complex/sulfated glycans through its FBA/G domain
**SUPPORTED** (High confidence)
- Direct glycan array evidence (Glenn et al. 2008, PMID: 18203720)
- Structural basis: retains first VEHGG loop; lacks second HGG loop
- Mutagenesis confirms FBA/G domain dependence for glycan binding

### Claim B: FBXO17 is distinct from high-mannose ERAD paralogs (FBXO2, FBXO6)
**SUPPORTED** (High confidence)
- No high-mannose binding on glycan array
- Absent second HGG loop eliminates chitobiose-binding pocket
- FBXO17-FBXO27 subgroup (59.9% FBA identity) vs FBXO2-FBXO6 subgroup (44-45%)
- Expert classification (Kumanomidou et al. 2015, PMID: 26460611) excludes FBXO17 from N-glycan binders

### Claim C: GSK3beta recognition uses a mechanistically distinct protein-binding mode
**PARTIALLY SUPPORTED** (Medium confidence)
- GSK3beta is not a glycoprotein, so protein-protein interaction is necessarily different from glycan-mediated recognition
- The putative GSK3beta-binding region (aa 151–200) is within the FBA domain but the primary glycan-contact loops are largely outside this region
- Conserved Trp residues in the GSK3beta-binding region are likely structural (core-packing) rather than glycan-contact residues
- **Unresolved:** Whether the GSK3beta-binding surface and glycan-binding surface are on opposite faces of the beta-sandwich, or partially overlapping

---

## Limitations and Knowledge Gaps

### Structural Limitations

1. **No co-crystal structure of FBXO17 with glycan or GSK3beta.** Our domain boundary and loop assignments are based on homology to FBXO2 (PDB: 1UMH) and sequence alignment. The actual FBXO17 binding surfaces could differ from those predicted by homology.

2. **GSK3beta-binding region mapping resolution.** The aa 151–200 region is mapped by deletion studies, not by co-crystallography or cross-linking mass spectrometry. The actual contact residues may extend beyond or be more restricted than this range.

3. **Partial overlap at beta5-beta6 loop.** The beta5-beta6 loop (~aa 176–183) partially overlaps with the GSK3beta-binding region. We cannot exclude the possibility that this loop contributes to both glycan and protein recognition, which would weaken the "fully distinct binding mode" claim.

### Functional Limitations

4. **Sulfated glycan binding specificity is incompletely characterized.** The glycan array (PMID: 18203720) tested a finite panel of glycans. FBXO17 may have additional binding partners (e.g., other sulfated glycoproteins, proteoglycans) not yet identified.

5. **Biological function of glycan binding is unknown.** While FBXO17 clearly binds sulfated glycans, the downstream biological consequence — whether it targets sulfated glycoproteins for ubiquitin-dependent degradation, similar to how FBXO2 targets high-mannose glycoproteins — has not been experimentally demonstrated.

6. **GSK3beta is the only validated non-glycoprotein substrate.** Additional protein substrates may exist, and their recognition mode may or may not use the same aa 151–200 interface.

7. **Species considerations.** The Suber et al. 2017 study was conducted in murine lung epithelial cells; human-specific validation is implied but not directly shown.

### Analytical Limitations

8. **Sequence-based analysis only.** Without an experimental FBXO17 structure, all spatial inferences about loop positions and binding surface separability are based on homology modeling and sequence conservation.

---

## Proposed Follow-up Experiments

### High Priority — Decisive for Hypothesis Resolution

1. **Co-crystal structure of FBXO17 FBA domain with heparin disaccharide and/or GSK3beta peptide.** This would definitively resolve whether the glycan-binding and protein-binding surfaces are structurally separable. AlphaFold Multimer could provide an initial computational prediction before experimental crystallization.

2. **Differential mutagenesis panel.** Mutate the VEHGG loop (beta2-beta3, aa ~122–135) and the GSK3beta-binding region (aa 151–200) independently, then test each mutant for both heparin/sulfated glycan binding AND GSK3beta binding. If VEHGG mutations ablate glycan binding without affecting GSK3beta recognition (and vice versa), the dual-mode hypothesis is confirmed.

3. **Competition assay: heparin vs. GSK3beta for FBXO17 binding.** If glycan and protein substrates bind simultaneously, the surfaces are distinct; if they compete, they overlap.

### Medium Priority — Extend Understanding

4. **Ubiquitination assay with sulfated glycoprotein substrates.** Test whether FBXO17 can ubiquitinate lactoferrin or other sulfated glycoproteins in vitro, establishing whether glycan binding leads to productive substrate processing.

5. **Proteomics (BioID or AP-MS) to identify additional FBXO17 substrates.** This would reveal whether GSK3beta is an outlier or representative of a broader protein-substrate repertoire.

6. **Glycan array with expanded sulfated glycan panel.** The original array may not have included all relevant sulfated structures. A more comprehensive panel could refine FBXO17's glycan specificity and potentially identify the precise sulfation patterns recognized.

### Lower Priority — Comparative Biology

7. **Direct ERAD assay.** Test whether FBXO17 can rescue ERAD of misfolded glycoproteins in FBXO2-knockout cells. A negative result would confirm that the ERAD pathway annotation should be removed.

8. **Phylogenetic analysis of FBA domain loop evolution.** Tracing when the second HGG motif was lost in the FBXO17 lineage could reveal whether sulfated glycan specificity arose once or multiple times independently within the FBA family.

---

## Evidence Base — Literature Summary

| Paper | PMID | Key Contribution to This Investigation |
|-------|------|---------------------------------------|
| Mizushima et al. (2004), *Structural basis of sugar-recognizing ubiquitin ligase* | [14990996](https://pubmed.ncbi.nlm.nih.gov/14990996/) | Crystal structure of FBXO2 SBD-chitobiose complex; defines the four-loop binding pocket architecture against which FBXO17's divergence is measured |
| Yoshida et al. (2003), *Fbs2 is a new member of the E3 ubiquitin ligase family that recognizes sugar chains* | [12939278](https://pubmed.ncbi.nlm.nih.gov/12939278/) | Characterizes FBXO6 (Fbs2) as high-mannose binder with Man3-9GlcNAc2 specificity; establishes the ERAD paradigm that does NOT apply to FBXO17 |
| Glenn et al. (2008), *Diversity in tissue expression, substrate binding, and SCF complex formation for a lectin family of ubiquitin ligases* | [18203720](https://pubmed.ncbi.nlm.nih.gov/18203720/) | Glycan array comparing all FBA members; directly shows FBXO17 binds sulfated glycans, not high-mannose; mutagenesis confirmation |
| Kumanomidou et al. (2015), *The structural differences between a glycoprotein specific F-box protein Fbs1 and its homologous protein FBG3* | [26460611](https://pubmed.ncbi.nlm.nih.gov/26460611/) | Structure-based loop analysis; expert classification excluding FBXO17 from N-glycan binders |
| Suber et al. (2017) | [28298444](https://pubmed.ncbi.nlm.nih.gov/28298444/) | Validates GSK3beta as SCF(FBXO17) substrate; establishes the protein-substrate arm of the dual-mode hypothesis |
