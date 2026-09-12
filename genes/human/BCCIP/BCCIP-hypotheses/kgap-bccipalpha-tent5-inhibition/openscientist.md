# BCCIPalpha Inhibition of FAM46/TENT5 Noncanonical Poly(A) Polymerases: Evidence Assessment and Curation Recommendations

## Summary

BCCIPalpha directly binds and inhibits FAM46/TENT5 noncanonical poly(A) polymerases through active-site blockade, as demonstrated by high-resolution crystal structures of FAM46A/BCCIPalpha and cryo-EM of FAM46C/BCCIPalpha complexes ([PMID: 37018411](https://pubmed.ncbi.nlm.nih.gov/37018411/)). A helix-loop-helix segment unique to BCCIPalpha inserts into the catalytic cleft of FAM46, physically occluding the polymerase active site. This inhibition is strictly isoform-specific: BCCIPbeta — which shares the first 258 residues with BCCIPalpha but diverges completely in its C-terminal segment — adopts an entirely different three-dimensional fold and cannot bind FAM46. This makes TENT5 inhibition the single molecular activity that most sharply distinguishes BCCIPalpha from BCCIPbeta.

However, a critical gap remains between the biochemical demonstration of inhibition and its physiological significance. While TENT5 family substrates are well characterized in other contexts — immunoglobulin mRNAs for TENT5C in plasma cells, collagen mRNAs for TENT5A in osteoblasts, and ER-targeted protein mRNAs more broadly — no study has yet demonstrated which specific cellular RNAs are affected by BCCIPalpha-mediated TENT5 inhibition, nor what downstream phenotypic consequences arise from this inhibition in vivo. The Liu et al. 2023 study that solved the structures did not include cellular poly(A) tail-length assays or transcriptomic readouts.

For Gene Ontology curation purposes, the structural and biochemical evidence is sufficient to support a molecular function annotation of **"enzyme inhibitor activity" (GO:0004857)** — or ideally a more specific child term such as "nucleotidyltransferase inhibitor activity" — applied isoform-specifically to BCCIPalpha. However, this should not yet be treated as the core or primary molecular function of BCCIP until the downstream cellular consequences are validated. No process-level annotation (e.g., "negative regulation of mRNA polyadenylation") is warranted without cellular evidence. Current GO annotations for BCCIP (Q9P287) do not reference the Liu et al. 2023 paper or any TENT5-related activity.

---

## Key Findings

### Finding 1: BCCIPalpha Directly Binds and Inhibits FAM46/TENT5 via Active-Site Blockade

The central finding of this investigation is that BCCIPalpha functions as a direct, stoichiometric inhibitor of the FAM46/TENT5 family of noncanonical poly(A) polymerases. This was established by Liu et al. (2023) through a combination of structural biology and biochemical assays ([PMID: 37018411](https://pubmed.ncbi.nlm.nih.gov/37018411/)).

**Structural evidence:** Three independent structures were solved: two crystal structures of the FAM46A/BCCIPalpha complex (PDB: 8EXE at 3.5 A and 8EXF at 3.2 A resolution) and one cryo-EM structure of the FAM46C/BCCIPalpha/Nanobody complex (PDB: 8EQB at 6.5 A resolution). These structures reveal that BCCIPalpha binds FAM46 through an extensive interface in which the beta-sheets of the two proteins pack side-by-side to form a continuous extended beta-sheet. Critically, a helix-loop-helix segment within BCCIPalpha inserts directly into the active-site cleft of FAM46, physically blocking substrate access to the catalytic center. This mechanism of inhibition — active-site occlusion by a protein inhibitor — is conceptually analogous to classic enzyme-inhibitor pairs (e.g., Barstar-Barnase) and represents a well-defined molecular function.

**Biochemical evidence:** In vitro poly(A) polymerase activity assays confirmed that addition of BCCIPalpha abolishes or substantially reduces the PAP activity of FAM46 family members. Importantly, BCCIPbeta was tested in parallel and showed no binding to FAM46 and no inhibition of PAP activity, establishing strict isoform specificity.

As stated in the paper's abstract: *"The FAM46 (also known as TENT5) proteins are noncanonical poly(A) polymerases (PAPs) implicated in regulating RNA stability. The regulatory mechanisms of FAM46 are poorly understood. Here, we report that the nuclear protein BCCIPalpha, but not the alternatively spliced isoform BCCIPbeta, binds FAM46 and inhibits their PAP activity."* And: *"A helix-loop-helix segment in BCCIPalpha inserts into the active site cleft of FAM46, thereby inhibiting the PAP activity."*

### Finding 2: BCCIPalpha and BCCIPbeta Adopt Completely Different Three-Dimensional Folds Despite >80% Sequence Identity

One of the most striking findings is that BCCIPalpha (322 amino acids) and BCCIPbeta (314 amino acids), which share identical sequence for their first 258 residues, adopt completely different overall protein folds. This is an unusual example of how alternative splicing of a relatively small C-terminal segment (64 amino acids in alpha vs. 56 in beta) can drive global structural rearrangement of an entire protein.

BCCIPbeta, whose structure was previously solved (PDB: 7KYQ, 7KYS; [PMID: 33452718](https://pubmed.ncbi.nlm.nih.gov/33452718/)), adopts a fold resembling GCN5-related N-acetyltransferases (GNATs), consistent with the yeast ortholog BCP1 structure ([PMID: 32805410](https://pubmed.ncbi.nlm.nih.gov/32805410/)). In contrast, BCCIPalpha in complex with FAM46 displays a unique fold with no structural homolog. The distinct C-terminal segment of BCCIPalpha serves as a structural "switch" — it does not directly contact FAM46, but it drives the entire protein to refold into the conformation competent for FAM46 binding and inhibition.

As Liu et al. stated: *"Unexpectedly, our structures of the FAM46A/BCCIPalpha and FAM46C/BCCIPalpha complexes show that, despite sharing most of the sequence and differing only at the C-terminal portion, BCCIPalpha adopts a unique structure completely different from BCCIPbeta. The distinct C-terminal segment of BCCIPalpha supports the adoption of the unique fold but does not directly interact with FAM46."*

This finding has profound implications for isoform-specific curation: BCCIPalpha and BCCIPbeta are effectively different proteins from a structural and functional standpoint, despite being encoded by the same gene through alternative splicing.

### Finding 3: BCCIPalpha and BCCIPbeta Have Clearly Partitioned Isoform-Specific Functions

The two BCCIP isoforms have well-documented, non-overlapping functional roles beyond the TENT5 inhibition:

| Function | BCCIPalpha | BCCIPbeta | Evidence |
|----------|-----------|----------|----------|
| FAM46/TENT5 PAP inhibition | **Yes** (direct, structural) | No | [PMID: 37018411](https://pubmed.ncbi.nlm.nih.gov/37018411/) |
| RPL23/uL14 nuclear chaperoning & 60S ribosome biogenesis | No | **Yes** (ternary complex with RPL23/eIF6) | [PMID: 25150171](https://pubmed.ncbi.nlm.nih.gov/25150171/) |
| RAD51 ADP release & presynaptic filament activation | No | **Yes** (direct biochemical) | [PMID: 27694622](https://pubmed.ncbi.nlm.nih.gov/27694622/) |
| Spindle pole/centrosome regulation | **Enriched** | Present but less | [PMID: 28394342](https://pubmed.ncbi.nlm.nih.gov/28394342/) |
| BRCA2 binding | Yes (shared region aa 59-167) | Yes | [PMID: 15713648](https://pubmed.ncbi.nlm.nih.gov/15713648/) |
| p21/CDKN1A binding & CDK2 regulation | Yes (shared region aa 161-259) | Yes | [PMID: 19713748](https://pubmed.ncbi.nlm.nih.gov/19713748/), [PMID: 14726710](https://pubmed.ncbi.nlm.nih.gov/14726710/) |
| DNA repair (HR) | Yes | Yes | [PMID: 17947333](https://pubmed.ncbi.nlm.nih.gov/17947333/) |
| Replication fork stabilization | Yes (both isoforms implicated) | Yes | [PMID: 35592921](https://pubmed.ncbi.nlm.nih.gov/35592921/) |

BCCIPbeta-specific functions rely on the GNAT-like fold adopted by that isoform. The ternary complex with RPL23/uL14 and eIF6 — essential for nuclear chaperoning of the ribosomal protein and 60S biogenesis — requires the BCCIPbeta-specific C-terminal domain ([PMID: 25150171](https://pubmed.ncbi.nlm.nih.gov/25150171/)): *"We show that mammalian BCCIPbeta, but not BCCIPalpha, forms a ternary complex with the ribosomal protein RPL23/uL14 and the pre-60S trans-acting factor eIF6."* Similarly, BCCIPbeta specifically promotes ADP release from the RAD51 presynaptic filament ([PMID: 27694622](https://pubmed.ncbi.nlm.nih.gov/27694622/)).

BCCIPalpha, in addition to TENT5 inhibition, is particularly enriched at spindle poles and centrosomes, where it regulates mitotic spindle architecture and orientation ([PMID: 28394342](https://pubmed.ncbi.nlm.nih.gov/28394342/)): *"we demonstrate BCCIP, especially BCCIPalpha, as a previously unidentified component of the mitotic spindle pole and the centrosome."* Whether the spindle function connects mechanistically to TENT5 inhibition — perhaps through the known FAM46C/Plk4 interaction at centrosomes ([PMID: 32433990](https://pubmed.ncbi.nlm.nih.gov/32433990/)) — remains to be investigated.

### Finding 4: TENT5 RNA Substrates Are Known, but BCCIPalpha-Regulated Targets Are Not

The TENT5 family members have well-characterized RNA substrates in specific cellular contexts:

- **TENT5C/FAM46C** polyadenylates immunoglobulin heavy and light chain mRNAs in plasma cells, stabilizing them and boosting antibody production ([PMID: 32141701](https://pubmed.ncbi.nlm.nih.gov/32141701/), [PMID: 28931820](https://pubmed.ncbi.nlm.nih.gov/28931820/)). Loss-of-function mutations in FAM46C are found in up to 20% of multiple myeloma patients.
- **TENT5A/FAM46A** polyadenylates Col1alpha1, Col1alpha2, and other secreted protein mRNAs in osteoblasts ([PMID: 33882302](https://pubmed.ncbi.nlm.nih.gov/33882302/)). Homozygous mutations cause osteogenesis imperfecta.
- **TENT5D** is the most ER-associated family member, enhancing expression of ER, ERGIC, Golgi, and lysosomal proteins ([PMID: 42247288](https://pubmed.ncbi.nlm.nih.gov/42247288/)).
- **TENT5B** lacks ER targeting and instead regulates proteins involved in cell division ([PMID: 42247288](https://pubmed.ncbi.nlm.nih.gov/42247288/)).

A unifying theme is that TENT5 proteins selectively stabilize mRNAs encoding ER-targeted and secreted proteins through FNDC3-mediated ER membrane localization ([PMID: 32966780](https://pubmed.ncbi.nlm.nih.gov/32966780/), [PMID: 42247288](https://pubmed.ncbi.nlm.nih.gov/42247288/)).

**However**, the Liu et al. 2023 study demonstrating BCCIPalpha inhibition of TENT5 PAP activity did not include cellular experiments showing which specific mRNAs have shortened poly(A) tails or reduced stability as a consequence of BCCIPalpha-mediated TENT5 inhibition. No transcriptomic, TAIL-seq, or poly(A) tail-length profiling data exist linking BCCIPalpha expression to changes in TENT5 target RNA metabolism. This is the single most important gap in the evidence base.

### Finding 5: Current GO Annotations for BCCIP Lack Any TENT5-Related Terms

A survey of the Gene Ontology annotations for human BCCIP (UniProt: Q9P287) via QuickGO reveals 43 annotations as of July 2026. These include molecular function terms for DNA binding (IDA), RNA binding (HDA), kinase regulator activity (IDA), identical protein binding (IPI), tubulin binding (IDA), and protein binding (IPI). Notably:

- No annotation references [PMID: 37018411](https://pubmed.ncbi.nlm.nih.gov/37018411/) (Liu et al. 2023)
- No annotation describes enzyme inhibitor activity, poly(A) polymerase inhibitor activity, or negative regulation of polyadenylation
- The TENT5C/FAM46C UniProt entry (Q5VWP2) also does not reference the BCCIPalpha interaction

The closest existing GO molecular function terms would be **GO:0004857 "enzyme inhibitor activity"** or **GO:0140870 "RNA polymerase inhibitor activity"**, but no specific "poly(A) polymerase inhibitor activity" or "nucleotidyltransferase inhibitor activity" child term currently exists in the ontology.

---

## Mechanistic Model and Interpretation

### Structural Basis of Isoform-Specific TENT5 Inhibition

The mechanistic picture can be summarized as follows:

```
Gene: BCCIP (10q26.1) — 9 exons
           |
    Alternative splicing of 3' exons
           |
    ┌──────┴──────┐
    v              v
BCCIPalpha        BCCIPbeta
(322 aa)          (314 aa)
Unique fold       GNAT-like fold
    |                  |
    v                  v
Helix-loop-helix   RPL23/eIF6 binding
inserts into       RAD51 ADP release
FAM46 active       60S ribosome
site cleft         biogenesis
    |
    v
BLOCKS PAP activity
of FAM46A/B/C/D
(TENT5A/B/C/D)
    |
    v
??? (cellular RNA
consequences unknown)
```

The key mechanistic insight is that alternative splicing does not simply add or remove a binding domain; rather, the 64-residue C-terminal segment unique to BCCIPalpha causes the entire protein — including the 258 residues shared with BCCIPbeta — to refold into a completely different structure. This "fold-switching" behavior is rare in biology and represents an extreme case of how alternative splicing can generate functionally distinct proteins. The alpha-specific C-terminal segment does not directly contact FAM46; instead, it acts as an intramolecular structural determinant that enables the shared region to adopt the FAM46-binding conformation.

### Separating Direct Inhibition from Downstream Phenotypes

It is essential to distinguish between:

1. **Direct enzyme inhibition (established):** BCCIPalpha binds FAM46 and blocks PAP activity in vitro. This is demonstrated by structural data (three independent structures) and biochemical assays. Evidence code: IDA (Inferred from Direct Assay).

2. **Downstream cellular consequences (not established):** No study has demonstrated that BCCIPalpha expression in cells leads to shortened poly(A) tails on TENT5 target mRNAs, reduced stability of those mRNAs, or altered protein output from the secretory pathway. Without this evidence, we cannot assign process-level annotations such as "negative regulation of mRNA polyadenylation" or "negative regulation of protein secretion."

3. **Physiological context (unknown):** BCCIPalpha is described as a nuclear protein, while TENT5 members are primarily cytoplasmic (ER-associated for TENT5A/C/D). It remains unclear in which cellular compartment the inhibitory interaction occurs, whether it is constitutive or regulated, and what signals control it.

### GO Annotation Recommendations

Based on the evidence:

| Annotation Type | Recommended | Evidence Code | Justification |
|----------------|-------------|---------------|---------------|
| MF: enzyme inhibitor activity (GO:0004857) | **Yes**, isoform-specific to BCCIPalpha | IDA | Structural + biochemical proof of active-site blockade |
| MF: protein binding (GO:0005515) with FAM46A/B/C/D | **Yes**, isoform-specific | IPI | Co-crystal structures, co-IP |
| MF: RNA binding | Not new (already annotated HDA) | — | Existing annotation; not directly related to TENT5 inhibition |
| MF: poly(A) polymerase inhibitor activity | **Ideal but term does not exist** | — | Would require new GO term request |
| BP: negative regulation of mRNA polyadenylation | **Not yet** | — | No cellular evidence |
| BP: negative regulation of mRNA stability | **Not yet** | — | No cellular evidence |
| MF: adaptor activity | **No** | — | BCCIPalpha acts directly as inhibitor, not as adaptor |

The strongest recommendation is to annotate BCCIPalpha with **GO:0004857 "enzyme inhibitor activity"** using evidence code IDA, referencing [PMID: 37018411](https://pubmed.ncbi.nlm.nih.gov/37018411/), with an isoform-specific qualifier. A GO term request for a more specific child term (e.g., "nucleotidyltransferase inhibitor activity" or "poly(A) polymerase inhibitor activity") would be appropriate.

---

## Evidence Base

### Primary Source

| Paper | PMID | Key Contribution |
|-------|------|-----------------|
| Liu et al. (2023) *Inhibition of FAM46/TENT5 activity by BCCIPalpha adopting a unique fold* | [37018411](https://pubmed.ncbi.nlm.nih.gov/37018411/) | Central paper: crystal/cryo-EM structures of FAM46A/BCCIPalpha and FAM46C/BCCIPalpha complexes; biochemical demonstration of isoform-specific PAP inhibition; discovery that BCCIPalpha adopts a unique fold different from BCCIPbeta |

### Supporting Structural and Biochemical Studies

| Paper | PMID | Relevance |
|-------|------|-----------|
| Nie et al. (2021) *Structure of human BCCIP and implications for binding and modification of partner proteins* | [33452718](https://pubmed.ncbi.nlm.nih.gov/33452718/) | BCCIPbeta crystal structure showing GNAT-like fold; provides structural contrast with BCCIPalpha |
| Zhang et al. (2020) *Crystal structure of BCP1 from S. cerevisiae* | [32805410](https://pubmed.ncbi.nlm.nih.gov/32805410/) | Yeast ortholog structure confirming GNAT superfamily relationship |
| Zheng et al. (2021) *Structural and functional characterization of FAM46C* | [34048638](https://pubmed.ncbi.nlm.nih.gov/34048638/) | FAM46C crystal structure at 2.35 A; PAP activity characterization; MM mutation analysis |
| Kuchta et al. (2020) *Structural and functional analyses of FAM46C/Plk4 complex* | [32433990](https://pubmed.ncbi.nlm.nih.gov/32433990/) | FAM46C/Plk4 complex structure; centrosomal recruitment mechanism |

### TENT5 Substrate and Function Studies

| Paper | PMID | Relevance |
|-------|------|-----------|
| Bilska et al. (2020) *FAM46C controls antibody production* | [32141701](https://pubmed.ncbi.nlm.nih.gov/32141701/) | TENT5C polyadenylates immunoglobulin mRNAs in plasma cells |
| Mroczek et al. (2017) *FAM46C as onco-suppressor in multiple myeloma* | [28931820](https://pubmed.ncbi.nlm.nih.gov/28931820/) | TENT5C stabilizes ER-targeted protein mRNAs; tumor suppressor role |
| Gewartowska et al. (2021) *Cytoplasmic polyadenylation by TENT5A in bone formation* | [33882302](https://pubmed.ncbi.nlm.nih.gov/33882302/) | TENT5A polyadenylates collagen mRNAs in osteoblasts |
| Buchan et al. (2025) *C-terminal region of TENT5 drives ER-associated polyadenylation via FNDC3* | [42247288](https://pubmed.ncbi.nlm.nih.gov/42247288/) | FNDC3-mediated ER localization; paralog-specific substrate preferences |
| Fucci et al. (2020) *FAM46C interaction with p62 and FNDC3* | [32966780](https://pubmed.ncbi.nlm.nih.gov/32966780/) | FNDC3A/B-dependent ER localization; p62 regulatory interaction |
| Krawczyk et al. (2025) *TENT5/FAM46: Secretory tuners* (review) | [40407157](https://pubmed.ncbi.nlm.nih.gov/40407157/) | Comprehensive review of TENT5 family functions in secretory cells |

### BCCIP Isoform Function Studies

| Paper | PMID | Relevance |
|-------|------|-----------|
| Lu et al. (2005) *BCCIP functions in RAD51 and BRCA2 focus formation* | [15713648](https://pubmed.ncbi.nlm.nih.gov/15713648/) | Both isoforms interact with BRCA2; shared region mediates binding |
| Kelso et al. (2017) *BCCIPbeta promotes ADP release from RAD51* | [27694622](https://pubmed.ncbi.nlm.nih.gov/27694622/) | BCCIPbeta-specific RAD51 regulation |
| Meng et al. (2012) *BCCIPbeta stabilizes nuclear RPL23/uL14* | [25150171](https://pubmed.ncbi.nlm.nih.gov/25150171/) | BCCIPbeta-specific ribosome biogenesis role |
| Rong et al. (2019) *Regulation of spindle integrity by BCCIP* | [28394342](https://pubmed.ncbi.nlm.nih.gov/28394342/) | BCCIPalpha enrichment at spindle poles |
| Lu et al. (2009) *BCCIP required for nuclear localization of p21* | [19713748](https://pubmed.ncbi.nlm.nih.gov/19713748/) | Shared BCCIP-p21 interaction; nuclear localization regulation |
| Meng et al. (2004) *Inhibition of G1 to S by BCCIPbeta* | [14726710](https://pubmed.ncbi.nlm.nih.gov/14726710/) | Both isoforms bind p21; cell cycle regulation |

---

## Limitations and Knowledge Gaps

### Critical Gaps

1. **No cellular validation of TENT5 inhibition:** The most significant limitation is the absence of any cellular or in vivo evidence that BCCIPalpha expression leads to measurable changes in poly(A) tail lengths, mRNA stability, or protein levels of known TENT5 target mRNAs. Without TAIL-seq, PAT assays, or transcriptomic data in BCCIPalpha-knockdown or overexpression systems, the physiological relevance of the inhibition remains speculative.

2. **Compartmentalization paradox:** BCCIPalpha is described as a nuclear protein, while TENT5 family members (particularly TENT5A, C, and D) are cytoplasmic and ER-associated. The subcellular context in which the inhibitory interaction occurs is unclear. It is possible that BCCIPalpha sequesters newly synthesized FAM46 in the nucleus before it can reach the ER, or that a fraction of BCCIPalpha is cytoplasmic, or that the interaction occurs during specific cell-cycle phases. This remains unresolved.

3. **Paralog specificity within TENT5 family:** While structures were solved with FAM46A and FAM46C, it is unclear whether BCCIPalpha equally inhibits all four TENT5 family members (A, B, C, D) in vivo, and whether it preferentially targets specific paralogs in different tissues.

4. **No knockout phenotype attributed to TENT5 inhibition:** BCCIP conditional knockout mice show neural development defects, microcephaly, and progenitor proliferation failures ([PMID: 22292003](https://pubmed.ncbi.nlm.nih.gov/22292003/)), but these phenotypes have been attributed to DNA repair/replication stress rather than TENT5 dysregulation. No study has tested whether any BCCIP-deficiency phenotype is rescued by concurrent TENT5 knockout.

5. **Cryo-EM resolution:** The FAM46C/BCCIPalpha complex was solved at 6.5 A resolution by cryo-EM, which is relatively low for detailed mechanistic interpretation. The higher-resolution crystal structures (3.2-3.5 A) of the FAM46A complex are more informative but involve a different TENT5 paralog.

### Methodological Limitations of This Analysis

This investigation was based entirely on literature review and database interrogation; no new experimental data were generated. The assessment relies on published abstracts and the reported findings of Liu et al. (2023) as the sole primary source for the BCCIPalpha-TENT5 interaction. Independent replication of the biochemical findings by other groups has not yet been reported.

---

## Proposed Follow-up Experiments and Actions

### High Priority — Cellular Validation

1. **TAIL-seq or nano-TAIL-seq in BCCIPalpha-manipulated cells:** Perform global poly(A) tail-length profiling in cells with BCCIPalpha knockdown, knockout, or overexpression. Compare poly(A) tail distributions on known TENT5 target mRNAs (Ig mRNAs in plasma cells, collagen mRNAs in osteoblasts, ER-targeted mRNAs broadly) to determine which transcripts are affected.

2. **BCCIPalpha-TENT5 interaction in live cells:** Use proximity ligation assays (PLA), FRET, or BioID/TurboID proximity labeling to confirm that BCCIPalpha and TENT5 family members interact in intact cells and to determine the subcellular compartment of interaction.

3. **Epistasis experiments:** In TENT5C-active cell lines (e.g., plasma cells), test whether BCCIPalpha overexpression phenocopies TENT5C knockout (reduced Ig secretion, shortened poly(A) tails on Ig mRNAs) and whether this effect requires TENT5C (i.e., is abolished in TENT5C-null cells).

### Medium Priority — Mechanistic Extension

4. **Paralog panel:** Test BCCIPalpha inhibition of all four TENT5 family members (A, B, C, D) side-by-side in quantitative PAP assays with defined RNA substrates to determine relative inhibition constants.

5. **BCCIPalpha-spindle-TENT5 connection:** Investigate whether BCCIPalpha's spindle pole localization relates to TENT5B (the only family member regulating cell division proteins rather than secretory proteins) or to the known FAM46C/Plk4 interaction at centrosomes.

6. **Structure of BCCIPalpha alone:** Determine whether BCCIPalpha adopts the unique fold constitutively or only upon FAM46 binding (induced fit vs. conformational selection). This would clarify whether BCCIPalpha exists in cells as a pre-formed inhibitor or requires FAM46 contact to refold.

### GO Curation Actions

7. **Immediate annotation:** Add GO:0004857 "enzyme inhibitor activity" to BCCIPalpha (Q9P287-1 or appropriate isoform identifier) with evidence code IDA, referencing PMID: 37018411. Add qualifier for isoform specificity.

8. **Term request:** Submit a GO term request for "poly(A) polymerase inhibitor activity" or "nucleotidyltransferase inhibitor activity" as a child of GO:0004857, if such a term does not already exist.

9. **Defer process annotation:** Do not add biological process annotations related to mRNA polyadenylation or RNA stability regulation until cellular evidence is available.

---

## Conclusion

The evidence that BCCIPalpha directly inhibits FAM46/TENT5 poly(A) polymerases is structurally and biochemically robust, representing one of the clearest examples of isoform-specific molecular function partitioning in mammalian biology. The active-site blockade mechanism is well defined at atomic resolution. However, this biochemical capability has not yet been connected to specific cellular RNA targets or physiological outcomes. The field stands at a clear inflection point: the molecular mechanism is solved, but the biological significance awaits validation. For GO curation, a molecular function annotation is warranted now; process annotations should await cellular evidence. TENT5 inhibition should be recognized as a defining molecular feature of BCCIPalpha, but designating it as the "core" function of BCCIP as a gene requires understanding what this inhibition accomplishes in the cell.
