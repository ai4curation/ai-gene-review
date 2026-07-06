# FBXL16 Client Stabilization Mechanism: Anti-Degradative Adaptor or Context-Dependent Dual-Function F-Box Protein?

## Summary

FBXL16 (F-box and leucine-rich repeat protein 16, UniProt Q8N461) is a structurally atypical member of the F-box protein family that stabilizes multiple oncoproteins — most notably c-MYC, IRS1, SRC-3, and beta-catenin — by functioning as a **catalytically dead decoy** within the SCF (SKP1–CUL1–F-box) ubiquitin ligase system. The strongest mechanistic evidence, from Morel et al. (2020), demonstrates that FBXL16 binds SKP1 via its N-terminal F-box domain and substrates (e.g., c-MYC) via its C-terminal leucine-rich repeat (LRR) domain, but critically **does not interact with the scaffold protein CUL1**. This inability to recruit CUL1 renders FBXL16 incapable of assembling a functional E3 ligase complex, and instead it sequesters substrates away from bona fide degradative SCF complexes such as SCF-FBW7 and SCF-beta-TrCP. The result is protein stabilization through competitive antagonism rather than catalytic activity.

However, this elegant decoy model is complicated by two reports showing FBXL16 can **promote degradation** of specific targets: HIF1alpha in triple-negative breast cancer ([PMID: 34818544](https://pubmed.ncbi.nlm.nih.gov/34818544/)) and LATS2 in the Hippo signaling pathway ([PMID: 38200110](https://pubmed.ncbi.nlm.nih.gov/38200110/)). These contradictory findings suggest FBXL16 possesses context-dependent dual functionality — acting as a stabilizer for some substrates and a degrader for others — raising fundamental questions about how a protein that reportedly cannot bind CUL1 can nonetheless mediate ubiquitin-dependent degradation. The resolution of this paradox remains an open question in the field.

Current Gene Ontology (GO) annotations for FBXL16 are misleading: they classify it as a canonical SCF complex component (GO:0019005) involved in SCF-dependent proteasomal degradation (GO:0031146), based on phylogenetic inference (IBA evidence code) rather than direct experimentation. These annotations fail to capture FBXL16's dominant anti-degradative activity and urgently require revision. We propose that a new molecular function term — such as **"anti-degradative substrate adaptor activity"** — is needed to accurately describe FBXL16's primary mechanism of action. Notably, no published evidence links FBXL16 to ERalpha/ESR1 stabilization.

---

## Key Findings

### Finding 1: FBXL16 Stabilizes c-MYC by Antagonizing FBW7-Mediated Ubiquitination (Strongest Evidence)

The most mechanistically detailed study of FBXL16 function was published by Morel, Shah, and Long in 2020 ([PMID: 32345600](https://pubmed.ncbi.nlm.nih.gov/32345600/)). This work established that FBXL16 directly binds c-MYC through its C-terminal LRR domain and SKP1 through its N-terminal F-box domain. The critical discovery was that **FBXL16 does not interact with CUL1**, the scaffold protein essential for assembling a functional SCF ubiquitin ligase complex. As the authors stated: *"Because it does not interact with the scaffold protein cullin 1 (CUL1), we hypothesized that FBXL16 might not form a functional SCF-E3 ligase complex."*

The functional consequence is that FBXL16 competes directly with the tumor suppressor FBW7 (FBXW7) for c-MYC binding. FBW7 is the substrate-recognition component of the SCF-FBW7 complex, which is the principal E3 ligase responsible for c-MYC ubiquitination and proteasomal degradation. By sequestering c-MYC in a catalytically inert FBXL16–SKP1 complex, FBXL16 shields c-MYC from FBW7-mediated ubiquitination. The study demonstrated that FBXL16 *"stabilizes C-MYC by antagonizing FBW7-mediated C-MYC ubiquitination and degradation"* and that both the F-box domain (for SKP1 binding) and the LRR domain (for substrate binding) are required for this stabilization activity. Furthermore, the paper also reported that *"FBXL16 up-regulates the levels of proteins targeted by SCF-E3 ligases, such as C-MYC, beta-catenin, and steroid receptor coactivator 3 (SRC-3)."*

This finding is supported by extensive independent literature on FBW7's role as a tumor suppressor that degrades c-MYC ([PMID: 33070870](https://pubmed.ncbi.nlm.nih.gov/33070870/); [PMID: 37408248](https://pubmed.ncbi.nlm.nih.gov/37408248/)). The c-MYC–FBXL16 relationship represents the **gold standard** for FBXL16 client characterization, with direct binding, domain mapping, ubiquitination assays, and half-life measurements all reported.

{{figure:fbxl16_domain_architecture.png|caption=FBXL16 domain architecture showing F-box domain (SKP1 binding), LRR domain (substrate binding), and the critical absence of CUL1 interaction that defines the anti-degradative decoy mechanism}}

### Finding 2: FBXL16 Stabilizes IRS1 in KRAS-Mutant Lung Adenocarcinoma

Morel and Long (2024) extended the FBXL16 story to insulin receptor substrate 1 (IRS1) in the context of KRAS-mutant lung adenocarcinoma (LUAD) ([PMID: 37983945](https://pubmed.ncbi.nlm.nih.gov/37983945/)). FBXL16 is selectively upregulated in KRAS-mutant tumors and *"upregulates insulin receptor substrate 1 (IRS1) protein stability, leading to an increase of IGF1/AKT signaling, thereby promoting cell growth and migration."* Importantly, this study also demonstrated therapeutic relevance: *"FBXL16 depletion greatly enhances sensitivity to the KRASG12C inhibitor (sotorasib) in resistant cells by downregulating phosphatidylinositol 3-kinase (PI3K)/protein kinase B (PKB; also known as AKT) signaling."*

IRS1 is a known substrate of at least two SCF-type E3 ligases: SCF-beta-TrCP, which targets IRS1 following mTORC1-mediated phosphorylation at Ser422 ([PMID: 30240640](https://pubmed.ncbi.nlm.nih.gov/30240640/)), and SCF-Fbxo40, which ubiquitinates IRS1 in skeletal muscle downstream of IGF1R activation ([PMID: 22033112](https://pubmed.ncbi.nlm.nih.gov/22033112/)). The involvement of multiple SCF-type ligases in IRS1 turnover is consistent with FBXL16's proposed decoy mechanism — by sequestering IRS1, FBXL16 could shield it from degradation by any of these competing E3 complexes.

While the IRS1 study did not include the same depth of domain-mapping experiments as the c-MYC work, the consistent involvement of the same research group (Morel and Long) and the coherent mechanistic framework with the c-MYC findings lend strong support to this client relationship.

### Finding 3: SRC-3 and Beta-Catenin Stabilization — Confirmed but Mechanistically Shallow

FBXL16 was reported to upregulate the protein levels of both SRC-3 (steroid receptor coactivator 3) and beta-catenin in addition to c-MYC ([PMID: 32345600](https://pubmed.ncbi.nlm.nih.gov/32345600/)). An independent confirmation of SRC-3 regulation came from Yang and Jing (2021) ([PMID: 34333223](https://pubmed.ncbi.nlm.nih.gov/34333223/)), who demonstrated that *"FBXL16 deficiency was demonstrated to reduce the level of steroid receptor coactivator 3 (SRC-3) in MDA-MB-231 and MCF-7 cells."*

Both SRC-3 and beta-catenin are established substrates of SCF-type E3 ligases: SRC-3 is degraded by SCF-FBW7alpha following GSK3-mediated phosphorylation ([PMID: 17574025](https://pubmed.ncbi.nlm.nih.gov/17574025/)), and beta-catenin is the canonical substrate of SCF-beta-TrCP within the Wnt destruction complex ([PMID: 32129710](https://pubmed.ncbi.nlm.nih.gov/32129710/); [PMID: 34352208](https://pubmed.ncbi.nlm.nih.gov/34352208/)). The fact that FBXL16 stabilizes substrates of both FBW7 and beta-TrCP suggests it may act as a broad-spectrum antagonist of multiple SCF complexes.

However, neither study demonstrated **direct binding** of FBXL16 to SRC-3 or beta-catenin, nor were domain-dependence or ubiquitination assays performed for these specific substrates. These relationships therefore remain mechanistically plausible but incompletely characterized. SRC-3 is classified as moderate evidence due to two independent reports, while beta-catenin is weak — mentioned only alongside c-MYC and SRC-3 without dedicated investigation.

### Finding 4: FBXL16 Promotes HIF1alpha Degradation — A Mechanistic Paradox

In striking contrast to its stabilizing activity, Kim et al. (2021) reported that FBXL16 acts as a **degradative** E3 ligase for HIF1alpha in triple-negative breast cancer ([PMID: 34818544](https://pubmed.ncbi.nlm.nih.gov/34818544/)). The study found that *"FBXL16 directly binds to HIF1alpha and induces its ubiquitination and degradation, regardless of the tumor microenvironment, resulting in blockade of the HIF1alpha-mediated epithelial-mesenchymal transition (EMT) and angiogenesis features of breast cancer."* In this context, FBXL16 functions as a **tumor suppressor** — the opposite of its oncogenic role in c-MYC stabilization.

This finding creates a fundamental mechanistic paradox. If FBXL16 cannot bind CUL1 (as demonstrated by Morel et al. 2020), how can it mediate canonical ubiquitin-dependent degradation of HIF1alpha? Several possible explanations exist: (1) alternative E3 ligase recruitment through a non-cullin-based mechanism; (2) context-dependent CUL1 binding regulated by post-translational modifications or cell-type-specific cofactors; (3) indirect promotion of HIF1alpha degradation through stabilization of a negative regulator; or (4) technical discrepancies between experimental systems. The HIF1alpha interaction is notable for being the only FBXL16 interaction confirmed by multiple experiments in the UniProt IntAct database (6 experiments).

### Finding 5: FBXL16 Also Degrades LATS2 via the Hippo Pathway

A second degradative target was reported in 2024: LATS2, a core kinase of the Hippo tumor suppressor pathway ([PMID: 38200110](https://pubmed.ncbi.nlm.nih.gov/38200110/)). The study found that *"This oncogenic FBXL16 complex blocks LATS2 condensation by binding to the PRM region to promote its degradation."* This further supports the notion that FBXL16's degradative activity is not limited to a single substrate but may represent a genuine alternative mode of action. However, neither the HIF1alpha nor the LATS2 study provides a clear mechanistic explanation for how a protein lacking CUL1 binding can drive ubiquitin-dependent degradation.

### Finding 6: No Published Evidence for FBXL16–ERalpha Interaction

Despite ERalpha being listed in the research question as a potential FBXL16 client, multiple PubMed searches combining FBXL16 with ERalpha, estrogen receptor, and ESR1 returned **zero results**. ERalpha is not mentioned in any of the identified FBXL16 publications. While ERalpha stability is regulated by ubiquitin-proteasome pathways, no connection to FBXL16 has been published as of July 2026. This client relationship is **entirely speculative** and lacks any supporting evidence.

### Finding 7: Current GO Annotations Are Misleading and Require Revision

A SPARQL query of UniProt (Q8N461) revealed that FBXL16 carries only three GO annotations: GO:0005829 (cytosol), GO:0019005 (SCF ubiquitin ligase complex), and GO:0031146 (SCF-dependent proteasomal ubiquitin-dependent protein catabolic process). The UniProt function annotation states: *"Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex."* However, Morel et al. (2020) explicitly demonstrated that *"Because it does not interact with the scaffold protein cullin 1 (CUL1), we hypothesized that FBXL16 might not form a functional SCF-E3 ligase complex."*

The existing GO annotations are based on **IBA (Inferred from Biological Aspect of Ancestor)** evidence codes — phylogenetic inference, not experimental evidence on FBXL16 itself. This represents a textbook case where phylogenetic inference fails because FBXL16 has functionally diverged from its paralogs. The UniProt subunit annotation claiming FBXL16 *"Interacts with SKP1 and CUL1"* directly contradicts experimental data. Strikingly, FBXL16 has **no Molecular Function GO annotation at all** — only Cellular Component and Biological Process terms.

{{figure:fbxl16_evidence_matrix.png|caption=Comprehensive evidence matrix for all reported FBXL16 client proteins, showing direct binding, ubiquitination changes, domain dependence, competing ligase involvement, and overall evidence strength}}

---

## Mechanistic Model and Interpretation

### The Anti-Degradative Decoy Model (Primary Mode)

The best-supported model for FBXL16 function is as a **dominant-negative decoy** within the SCF ubiquitin ligase system. The mechanism can be summarized as follows:

```
CANONICAL SCF COMPLEX (e.g., SCF-FBW7):
  SKP1 ── F-box protein (FBW7) ── CUL1 ── RBX1 ── E2~Ub
                |                                      |
            Substrate (c-MYC)  <─── Ubiquitination ────┘
                |
            Proteasomal Degradation

FBXL16 DECOY COMPLEX:
  SKP1 ── FBXL16 (F-box + LRR)   ✗   CUL1 (NO interaction)
                |
            Substrate (c-MYC)  <─── SEQUESTERED, STABILIZED
                |
            NO ubiquitination, NO degradation

COMPETITIVE ANTAGONISM:
  SCF-FBW7    + FBXL16  ──compete──>  c-MYC, SRC-3
  SCF-β-TrCP  + FBXL16  ──compete──>  β-catenin, IRS1
```

FBXL16 retains the ability to bind SKP1 (potentially also sequestering SKP1 from productive SCF complexes) and to recognize substrates via its LRR domain, but its inability to recruit CUL1 means the catalytic ubiquitin-transfer machinery is never assembled. The net effect is substrate stabilization through competitive sequestration.

### The Degradative Mode (Secondary, Context-Dependent)

For HIF1alpha and LATS2, FBXL16 reportedly promotes ubiquitination and degradation. The mechanism for this alternative mode remains unresolved, and several non-exclusive hypotheses should be considered:

1. **Alternative E3 recruitment**: FBXL16 may recruit non-cullin E3 ligases to specific substrates
2. **Context-dependent CUL1 binding**: Cell-type-specific cofactors or modifications may enable CUL1 interaction
3. **Indirect effects**: FBXL16 may stabilize a negative regulator of HIF1alpha or LATS2
4. **Bridging protein**: An unknown adaptor may connect FBXL16 to CUL1 in certain contexts

{{figure:fbxl16_mechanism_model.png|caption=Mechanistic diagram illustrating FBXL16's dual behavior: anti-degradative decoy for c-MYC/IRS1/SRC-3/beta-catenin versus degradative activity for HIF1alpha/LATS2}}

### Evolutionary Precedents for Non-SCF F-Box Proteins

Two important yeast precedents support the concept of F-box proteins functioning outside canonical SCF complexes:

- **Rcy1p** in *S. cerevisiae* ([PMID: 11287615](https://pubmed.ncbi.nlm.nih.gov/11287615/)): Forms a Skp1p–Rcy1p complex without Cdc53p (CUL1 ortholog), Hrt1p, or Cdc34p, and functions in SNARE recycling rather than ubiquitin-dependent degradation. This is the closest known mechanistic analogy to FBXL16's decoy behavior.
- **Roy1/Ymr258c** in *S. cerevisiae* ([PMID: 21389113](https://pubmed.ncbi.nlm.nih.gov/21389113/)): A non-SCF F-box protein that binds Skp1 and inhibits the Rab5-like GTPase Ypt52, functioning as a negative regulator of intracellular transport independently of ubiquitination.

These precedents establish that F-box proteins can form SKP1-containing complexes with non-degradative functions, providing evolutionary context for FBXL16's anti-degradative activity.

### Client Protein Evidence Summary Table

| Client | Direct Binding | Ub Changes | Half-life | F-box Req. | LRR Req. | Competing Ligase | Direction | Evidence |
|--------|:---:|:---:|:---:|:---:|:---:|---|---|---|
| **c-MYC** | Yes (LRR) | Decreased Ub | Increased | Yes | Yes | SCF-FBW7 | Stabilization | **Strong** |
| **IRS1** | Implied | Not directly shown | Increased | Not tested | Not tested | SCF-beta-TrCP, SCF-Fbxo40 | Stabilization | **Moderate-Strong** |
| **SRC-3** | Not tested | Not tested | Increased (inferred) | Not tested | Not tested | SCF-FBW7alpha | Stabilization | **Moderate** |
| **beta-catenin** | Not tested | Not tested | Increased (inferred) | Not tested | Not tested | SCF-beta-TrCP | Stabilization | **Weak** |
| **HIF1alpha** | Yes | Increased Ub | Decreased | Not detailed | Not detailed | VHL (O2-dependent) | Degradation | **Moderate** |
| **LATS2** | Yes (PRM) | Increased | Decreased | Not detailed | Not detailed | Unknown | Degradation | **Moderate** |
| **ERalpha** | **No data** | No data | No data | No data | No data | N/A | Unknown | **None** |

---

## GO Annotation Assessment

### Current Annotations vs. Experimental Evidence

| GO ID | Term | Category | Evidence Code | Assessment |
|---|---|---|---|---|
| GO:0005829 | Cytosol | CC | TAS (Reactome) | **Accurate** |
| GO:0019005 | SCF ubiquitin ligase complex | CC | IBA (phylogenetic) | **Misleading** — FBXL16 does not form canonical SCF |
| GO:0031146 | SCF-dependent proteasomal Ub-dependent protein catabolic process | BP | IBA (phylogenetic) | **Misleading** — primary activity is anti-catabolic |

### Recommended Changes

| Action | GO Term | Rationale |
|---|---|---|
| Remove | GO:0019005 (SCF complex) | FBXL16 does not bind CUL1; not a canonical SCF member |
| Remove | GO:0031146 (SCF-dependent degradation) | Primary activity is anti-degradative |
| Add | GO:0050821 (protein stabilization) | Captures dominant anti-degradative function |
| Add | GO:0150091 (ubiquitin ligase inhibitor activity) | Captures competitive antagonism of SCF-FBW7 |
| **Propose** | **"Anti-degradative substrate adaptor activity"** (new MF term) | Most precise description of the unique mechanism |

No existing GO molecular function term precisely captures FBXL16's mechanism. "Ubiquitin-protein transferase activity" (GO:0004842) implies degradation. "Ubiquitin ligase inhibitor activity" (GO:0150091) captures antagonism but not substrate binding. "Protein binding" (GO:0005515) is too generic. A new term would fill a genuine gap in the ontology. However, the contradictory HIF1alpha/LATS2 degradation reports complicate a purely anti-degradative annotation and suggest that substrate-specific dual annotations may ultimately be needed.

{{figure:fbxl16_go_assessment.png|caption=Evidence strength ranking for FBXL16 client proteins and assessment of current vs. proposed GO molecular function annotations}}

---

## Evidence Base

### Core FBXL16 Studies

| PMID | Year | Key Contribution | Client(s) |
|---|---|---|---|
| [32345600](https://pubmed.ncbi.nlm.nih.gov/32345600/) | 2020 | Definitive mechanistic study: FBXL16 binds SKP1 + c-MYC but not CUL1; antagonizes FBW7 | c-MYC, beta-catenin, SRC-3 |
| [37983945](https://pubmed.ncbi.nlm.nih.gov/37983945/) | 2024 | IRS1 stabilization in KRAS-mutant LUAD; sotorasib sensitization | IRS1 |
| [34818544](https://pubmed.ncbi.nlm.nih.gov/34818544/) | 2021 | HIF1alpha degradation (contradicts decoy model); tumor suppressor in TNBC | HIF1alpha |
| [38200110](https://pubmed.ncbi.nlm.nih.gov/38200110/) | 2024 | LATS2 degradation via Hippo pathway | LATS2 |
| [34333223](https://pubmed.ncbi.nlm.nih.gov/34333223/) | 2021 | Independent SRC-3 confirmation; AKT/mTOR signaling | SRC-3 |
| [20043084](https://pubmed.ncbi.nlm.nih.gov/20043084/) | 2010 | FBXL16 is E2F1-regulated; upregulated upon CDKN2A loss | (FBXL16 regulation) |

### Supporting Literature on Competing E3 Ligases

| PMID | Relevance to FBXL16 |
|---|---|
| [30240640](https://pubmed.ncbi.nlm.nih.gov/30240640/) | SCF-beta-TrCP degrades IRS1 via mTORC1-dependent Ser422 phosphorylation |
| [22033112](https://pubmed.ncbi.nlm.nih.gov/22033112/) | SCF-Fbxo40 ubiquitinates IRS1 in skeletal muscle |
| [17574025](https://pubmed.ncbi.nlm.nih.gov/17574025/) | SCF-FBW7alpha degrades SRC-3 via GSK3 phosphorylation |
| [32129710](https://pubmed.ncbi.nlm.nih.gov/32129710/) | SCF-beta-TrCP mediates beta-catenin destruction in Wnt pathway |
| [34352208](https://pubmed.ncbi.nlm.nih.gov/34352208/) | Reconstituted beta-catenin destruction complex biochemistry |
| [33070870](https://pubmed.ncbi.nlm.nih.gov/33070870/) | FBW7 loss drives mammary tumorigenesis via c-MYC/cyclin E accumulation |
| [11287615](https://pubmed.ncbi.nlm.nih.gov/11287615/) | Rcy1p: yeast non-SCF F-box protein precedent |
| [21389113](https://pubmed.ncbi.nlm.nih.gov/21389113/) | Roy1: yeast non-SCF F-box inhibitor precedent |

---

## Limitations and Knowledge Gaps

### Major Unresolved Questions

1. **The CUL1 paradox**: How can FBXL16 mediate HIF1alpha and LATS2 degradation if it cannot bind CUL1? No study has directly addressed this contradiction. It is possible that CUL1 binding is context-dependent, that alternative cullin family members are involved, or that the degradation is mediated through a non-SCF mechanism.

2. **Structural basis unknown**: No crystal structure or cryo-EM structure of FBXL16 (alone or in complex) has been reported. The structural basis for its selective failure to bind CUL1 — despite other F-box proteins doing so — is entirely unknown.

3. **Incomplete domain mapping**: Only the c-MYC interaction has been mapped to specific FBXL16 domains (F-box for SKP1, LRR for c-MYC). For IRS1, SRC-3, beta-catenin, HIF1alpha, and LATS2, domain-dependence has not been systematically tested.

4. **Limited cell-type diversity**: Most studies use cancer cell lines. Whether FBXL16's stabilization activity operates in normal tissues is unknown.

5. **Quantitative competition dynamics**: No study has measured binding affinities (Kd values) of FBXL16 vs. FBW7 for c-MYC, making it unclear how efficiently FBXL16 competes under physiological expression levels.

6. **Small literature base**: FBXL16 is a relatively understudied protein with approximately 7 primary papers. The contradictory degradation reports (HIF1alpha, LATS2) are from different laboratories with potentially different experimental systems and have not been independently replicated.

7. **ERalpha**: The absence of published evidence does not exclude a possible FBXL16–ERalpha interaction; it simply has not been tested.

---

## Proposed Follow-up Experiments

### High Priority

1. **Structural characterization of FBXL16–SKP1 complex**: Determine the cryo-EM or crystal structure to understand why CUL1 binding is impaired. Compare with canonical F-box protein structures (FBW7, beta-TrCP) bound to SKP1–CUL1.

2. **Reconcile the CUL1 binding paradox**: Perform co-immunoprecipitation of FBXL16 with CUL1 across multiple cell types (TNBC, LUAD, normal epithelia) and under varied conditions (normoxia vs. hypoxia, +/- neddylation) to determine if CUL1 interaction is context-dependent.

3. **In vitro reconstitution**: Reconstitute the FBXL16–SKP1–substrate complex from purified components and test whether it can recruit CUL1–RBX1 or alternative cullin complexes.

4. **Quantitative binding affinity measurements**: Use SPR, ITC, or fluorescence polarization to measure binding affinities of FBXL16 vs. FBW7 for shared substrates (c-MYC, SRC-3), establishing whether competitive sequestration is thermodynamically plausible at physiological concentrations.

### Medium Priority

5. **Systematic domain mapping for all clients**: Test F-box and LRR deletion/mutation constructs for binding to IRS1, SRC-3, beta-catenin, HIF1alpha, and LATS2.

6. **Proteome-wide substrate identification**: Perform BioID or AP-MS proteomics to identify the complete FBXL16 interactome and discover additional client proteins.

7. **Ubiquitome analysis**: Compare global ubiquitination profiles (K-epsilon-GG proteomics) in FBXL16-overexpressing vs. FBXL16-knockout cells.

### Lower Priority

8. **GO annotation correction**: Submit evidence-based requests to the Gene Ontology Consortium and UniProt to correct FBXL16 annotations.

9. **ERalpha testing**: Directly test whether FBXL16 affects ERalpha protein levels in breast cancer cells.

10. **In vivo validation**: Generate conditional FBXL16 knockout mice to assess physiological consequences on c-MYC, IRS1, and HIF1alpha levels.

---

## Conclusion

FBXL16 represents a remarkable example of evolutionary repurposing within the F-box protein family. Its primary, best-supported function is as an **anti-degradative substrate adaptor** — a catalytically dead decoy that sequesters SCF substrates from productive ubiquitin ligase complexes. The c-MYC–FBW7 antagonism is the most rigorously characterized mechanism (Tier 1 evidence), with IRS1 stabilization providing therapeutically relevant confirmation (Tier 2). SRC-3 and beta-catenin stabilization are supported but mechanistically shallow (Tiers 3–4). The contradictory reports of HIF1alpha and LATS2 degradation reveal either genuine dual functionality or unresolved technical discrepancies requiring urgent investigation.

Current GO and UniProt annotations are experimentally inaccurate, based on phylogenetic inference that incorrectly classifies FBXL16 as a canonical SCF component. A refined annotation framework — including a new molecular function term such as "anti-degradative substrate adaptor activity" — is needed to accurately represent FBXL16's dominant mechanism. ERalpha has no published connection to FBXL16, and this putative client relationship lacks any supporting evidence.
