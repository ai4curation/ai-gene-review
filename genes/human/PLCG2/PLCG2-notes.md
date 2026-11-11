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


## 2026-10-26 full annotation audit: evidence review in progress

The preserved acquisition baseline and raw-file hashes are in `.cache/module-audit-logs/b-cell-panel-baseline.json`. This review covers all annotations, including functions outside B-cell signaling. Normal acquisition and actual provider attempts are recorded in `b-cell-acquisition-report.md` and `b-cell-fetch/provider-publication-results.json`; provider failures are not research reports. Existing genuine exact-target reports, where available, are discovery aids. Original machine annotation payloads and raw source records will be preserved.


## 2026-10-26 completed full annotation audit

The catalytic core is PI(4,5)P2 hydrolysis to DAG and IP3, with phosphotyrosine recognition by its SH2 domains. The phosphatidylinositol-biosynthesis row is corrected laterally to IP3 biosynthesis; this is a product-role correction, not an ontology descendant claim. Broad lipid/phospholipid catabolism is refined to glycerophospholipid catabolism, while phosphatidylinositol metabolism remains an appropriate substrate-class process.

Full PMID:11331309 identifies human PLCγ2 constructs, EGF-stimulated membrane/ruffle recruitment and subsequent vesicular internalization. The experimental expression system is distinguished from universal native-cell residence. PMID:23555801 directly shows dynamic perinuclear BANK1–PLCG2 proximity in Daudi cells. Full PMID:15509800 establishes BTK-dependent Y753/Y759 phosphorylation in human Ramos cells, with Y1217 behaving differently. Human PLCγ2 with avian BLNK in reconstitution experiments does not become an entirely native human complex assay.

PMID:24642916 supports phosphotyrosine binding directly. Full PMID:27609517 independently recovers human platelet SYK with PLCγ2 tandem SH2 domains, although much more weakly than with PLCγ1; this supports the kinase-binding class without resolving the exact microglial interaction behind PMID:32514138. Generic interaction rows are refined only where the functional binding class is supported; other bare GO:0005515 rows are removed under policy while preserving the interaction provenance. Epithelial migration (PAINT PTN000741536) and Wnt signaling remain unresolved; hematopoietic enrichment is not evidence of loss, and an inaccessible full source is not proof of misattribution.

All 178 original annotation payloads, including qualifiers and any negation flags, were preserved; no NEW assertions were added. Normal source acquisition and actual provider outcomes are retained in the acquisition logs. Failed provider calls were not replaced with fabricated reports. Source-access limits are recorded above and in the individual row reasons; partial publisher pages and captcha responses were not treated as full articles. The six-member focused strict/schema, GO-term and source-quotation check passed with zero errors and warnings before final packaging; the final package reruns those checks after finding additions. Record-section backfill, HTML rendering, helper-generated Codex provenance and exact payload/raw-hash checks accompany the package.
