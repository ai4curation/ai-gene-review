# LPCAT4 literature notes

## Search and cache provenance

- PubMed was searched directly on 2026-08-12 for `LPCAT4`, `LPEAT2`, `LPLAT10`, and `AGPAT7`, with follow-up searches for substrate specificity, topology, lipid remodeling, and disease context.
- Project tooling was used to fetch PMID:16243729, PMID:38226852, and the full-text PMC record for PMID:37294538. PMID:41740885 was retried as requested and the tooling confirmed that the complete PMC-backed record was already cached. One PubMed endpoint attempt for PMID:37294538 returned HTTP 429, but the project tooling's PMC fallback produced a complete cache that was then quote-validated.
- No deep-research provider file was created or fabricated. The evidence below comes from cached primary publications, UniProt Q643R3, and cached Reactome records.

## Identity and nomenclature

Human LPCAT4 is the 524-residue membrane lysophospholipid acyltransferase also called LPEAT2 or LPLAT10. The older name AGPAT7 reflects its sequence-family assignment, not demonstrated lysophosphatidic-acid acyltransferase activity. The cloning paper states that the cDNA encodes “a putative protein with 524 amino acid residues, which contains an acyltransferase domain in 123-234 aa” [PMID:16243729]. Direct biochemical work instead found that it “lacked appreciable acylating activity toward glycerol-3-phosphate, lysophosphatidic acid, lysophosphatidylinositol, and diacylglycerol” [PMID:18458083].

The reviewed UniProt Q643R3 record lists no alternative protein isoforms. Its two old sequence-accession cautions concern cloning errors, not biologically supported isoforms; isoform-specific functional claims are therefore not warranted.

## Membrane location and topology

LPCAT4 is an ER-membrane enzyme. In HeLa cells, “AGPAT7 protein was mainly localized to the endoplasmic reticulum (ER)” [PMID:16243729], and the later enzymology paper independently reports, “When overexpressed in mammalian cells, LPEAT2 is localized to the endoplasmic reticulum” [PMID:18458083]. UniProt predicts two transmembrane helices (residues 40–62 and 87–107), supporting an integral multi-pass membrane topology; the exact membrane orientation was not established in the primary papers reviewed here.

## Enzymatic activity and substrate specificity

The 2008 human-cell study established broad lysophospholipid acyltransferase activity with especially prominent LPE acylation. HEK293T expression caused “a dramatic increase (up to 9-fold) in LPEAT activity” and the enzyme also acted on ether/alkenyl LPE, LPG, ether LPC, LPS, and LPC [PMID:18458083]. It accepted “a broad range of medium and long chain fatty acyl-CoA as acyl donors” [PMID:18458083]. These are heterologous-cell/membrane assays and should not be read as equal physiological use of every substrate.

The 2026 full-text study resolves the positional chemistry that was not determined in the older work. It identifies LPLAT10/LPEAT2/LPCAT4 as the enzyme “responsible for generating PLs with an unsaturated FA at the sn-1 position” and shows incorporation into LPC, LPE, and LPS “selectively at the sn-1 position” [PMID:41740885]. In the controlled positional assay, LPC was preferred over LPE and LysoPS, sn-2-dominant lyso acceptors were preferred, and the authors concluded that “LPLAT10 is a novel sn-1 selective LPLAT that preferentially incorporates unsaturated FAs” [PMID:41740885]. Both saturated and unsaturated acyl-CoAs worked in vitro, but affinity favored unsaturated donors; DHA (C22:6-CoA) was a particularly effective substrate.

The apparent differences between studies are bounded rather than collapsed. PMID:18458083 reported LPG activity, whereas PMID:41740885 found no LPG activity under its assay conditions. Both studies found no LPA acylation. Thus PC, PE, and PS remodeling are well supported; PG remodeling remains assay-dependent; generic AGPAT/LPAAT or phosphatidic-acid synthesis assignments are contradicted by the direct LPCAT4 assays.

## Lipid remodeling and physiological boundaries

Mouse knockout lipidomics provides in-vivo support for acyl-chain remodeling: only phospholipids carrying unsaturated C18:1, C18:2, C20:4, or C22:6 at sn-1 decreased in Lplat10-deficient brain [PMID:41740885]. In situ hybridization and functional mass-spectrometry imaging localized strong mouse activity to cortex, hippocampus, and cerebellum, consistent with neuronal enrichment. This is mouse evidence and should not be silently converted into a human neuron-specific physiological annotation. The knockout mice had no overt cerebellar histology or Purkinje-cell staining abnormality, and the paper states that the biological roles of these minor atypical phospholipids remain elusive [PMID:41740885].

Liver overexpression is a separate gain-of-function context. Adenoviral LPLAT10 expression in mouse liver raised hepatic and serum PC 40:7 containing C18:1/C22:6 and increased glucose-stimulated insulin secretion [PMID:38226852]. The same abstract says normal hepatic expression is low. This supports a possible lipid-mediated endocrine effect under experimental overexpression, not an established endogenous human liver or diabetes mechanism.

In hepatocellular carcinoma models, LPCAT4 was reported to enhance cell growth and cholesterol biosynthesis by increasing ACSL3 through WNT/β-catenin/c-JUN signaling [PMID:37294538]. This is a disease-context regulatory phenotype from cell models plus pan-cancer association analyses; it should not be generalized into LPCAT4's constitutive biochemical function or normal human physiology.

## Reactome reconciliation

Cached Reactome reactions placing LPCAT4/LPEAT2 in LPC→PC, LPE→PE, and LPS→PS reactions are consistent with both direct biochemical papers. Reactome LPG→PG records match the older broad-substrate assay but conflict with the negative LPG result in PMID:41740885, so they remain disputed/context-sensitive. Reactome’s generic PA-synthesis and AGPAT/LPAAT records should not be treated as LPCAT4 evidence: PMID:18458083 and PMID:41740885 both report no appreciable LPA acylation.

## Curation takeaways

- Core molecular role: ER-membrane sn-1-selective lysophospholipid acyltransferase that remodels PC, PE, and PS and favors unsaturated acyl-CoAs, including DHA.
- Do not infer LPAAT/AGPAT catalytic activity from the historical AGPAT7 name.
- Preserve assay context for LPG/PG, which differs between the 2008 and 2026 studies.
- Preserve human-cell versus mouse-knockout and mouse-overexpression boundaries.
- No supported alternative protein isoforms or isoform-specific functions were identified.
