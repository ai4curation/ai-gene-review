# PLCG2 notes

Automated deep research was attempted with `just deep-research-falcon human PLCG2 --fallback perplexity-lite`, but the run timed out before producing a deep-research file. This review therefore uses the cached GOA publications, the UniProt record, Reactome-derived entries, and the PANTHER family fetch.

PLCG2 encodes phospholipase C-gamma 2, a hematopoietic and microglial phosphoinositide-specific phospholipase C. The central biochemical activity is receptor-regulated hydrolysis of phosphatidylinositol 4,5-bisphosphate to IP3 and DAG: activated PLC-gamma2 "converts phosphatidylinositol 4,5-bisphosphate into the second messenger inositol 1,4,5-trisphosphate (IP3)" [PMID:11043765 "The activated PLC-gamma2 converts phosphatidylinositol 4,5-bisphosphate into the second messenger inositol 1,4,5-trisphosphate (IP3)"]. The general PLC-gamma reaction also generates "two second messengers: inositol 1,4,5-trisphosphate (I 1,4,5-P3) and diacylglycerol" [PMID:11331309 "The hydrolysis of phosphatidylinositol 4,5-bisphosphate (PI 4,5-P2) occurs in response to a large number of extracellular signals to generate two second messengers: inositol 1,4,5-trisphosphate (I 1,4,5-P3) and diacylglycerol"].

Activation is controlled by tyrosine phosphorylation and SH2-domain recruitment. In B-cell signaling, Tyr753 and Tyr759 are important for PLCG2 function, with Btk directly phosphorylating PLCG2 while Syk phosphorylates BLNK to create docking sites [PMID:11606584 "two tyrosine residues, Tyr(753) and Tyr(759), were important for the PLCgamma2 signaling function"; PMID:11606584 "function of Syk is to phosphorylate BLNK, providing binding sites for PLCgamma2"]. Independent biochemical work in recombinant PLCG2 and platelets supports Tyr753/Tyr759 as activating phosphorylation sites [PMID:12181444 "phosphorylation of PLCgamma2 led to activation of the recombinant enzyme"; PMID:12181444 "collagen, a PLCgamma2-dependent agonist, induces phosphorylation of PLCgamma2 at Y753 and Y759"].

Protein recruitment annotations should be interpreted specifically, not as generic "protein binding." PLCG2 binds phosphorylated receptor/adaptor motifs via SH2-domain biology and can be regulated by scaffold/adaptor complexes such as BLNK and BANK1. BANK1 work showed that "PLCg2 interacts with BANK1 and that the interaction is promoted by B-cell receptor" stimulation [PMID:23555801 "PLCg2 interacts with BANK1 and that the interaction is promoted by B-cell receptor"], with dependence on BANK1 tyrosine/proline residues [PMID:23555801 "the interaction between BANK1 and PLCg2 was dependent on specific tyrosine and proline residues"]. A structural study also supports direct Rac2-dependent activation of PLCG2 [PMID:19394299 "the crystal structure of the complex of Rac2 bound to the split pleckstrin homology (spPH) domain of phospholipase C-gamma(2)"].

PLCG2 has important evolved immune-cell roles. It is central in BCR signaling and calcium mobilization, with BCR pathway reviews emphasizing Syk, Btk, BLNK, PLCG2, IP3, and calcium release [PMID:11043765 "the intracellular protein tyrosine kinases Syk and Btk in PLC-gamma2 activation"; PMID:11043765 "Binding of IP3 to the IP3 receptors is essential for triggering a calcium release from the ER"]. It also functions in platelets and myeloid/microglial cells. In human iPSC-derived microglia-like cells, TREM2 signals through PLCG2 to mediate survival, phagocytosis, neuronal debris processing, and lipid metabolism; PLCG2 also mediates TLR-linked inflammatory responses [PMID:32514138 "TREM2 signals through PLCgamma2 to mediate cell survival, phagocytosis, processing of neuronal debris, and lipid metabolism"; PMID:32514138 "PLCG2 also signals downstream of Toll-like receptors to mediate inflammatory responses"].

For curation, the specific molecular-function term `phosphatidylinositol-4,5-bisphosphate phospholipase C activity` should be retained as core. Broad terms such as `phosphoric diester hydrolase activity`, `C-type glycerophospholipase activity`, `lipid metabolic process`, and `signal transduction` are true in spirit but less informative than the specific PIP2 phospholipase and receptor-proximal signaling terms. `phosphatidylinositol biosynthetic process` is the wrong direction for PLCG2 and should be replaced by phosphatidylinositol-mediated signaling or PIP2 phospholipase activity. Generic `protein binding` annotations should be modified to `phosphotyrosine residue binding`/`phosphorylation-dependent protein binding` when the evidence is SH2-phosphopeptide recruitment, or marked over-annotated when they come from high-throughput interaction screens without a clear PLCG2-specific mechanism.

## 2026-06-20 Second-Pass Review Notes

Second-pass audit confirmed the existing action calls and reference-review
coverage. No YAML changes were needed in this pass.

The single UNDECIDED annotation is GO:1990782 protein tyrosine kinase binding
from PMID:32514138. The cached abstract supports PLCG2 signaling in microglia
but does not expose the full IPI evidence for direct protein tyrosine kinase
binding, so this remains UNDECIDED under the project rule not to overrule
experimental annotations from abstract-only evidence.

The REMOVE annotation for GO:0016055 Wnt signaling pathway remains appropriate:
the cited PMID:18784435 abstract describes Wilms tumor/fetal kidney expression
profiling and lack of PLCG2 expression, not functional PLCG2 involvement in Wnt
signaling.

The core function remains receptor-activated PIP2 phospholipase C activity that
generates IP3 and DAG, plus phosphotyrosine/adaptor-dependent recruitment in
immune receptor signaling complexes. Alzheimer relevance should be captured
through microglial receptor-proximal PLCG2 signaling, calcium/lipid
second-messenger output, phagocytosis, survival, and inflammatory response
biology rather than disease-progression annotations.
