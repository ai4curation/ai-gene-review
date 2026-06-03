# AMBRA1 review notes

## Deep research provenance

- `just deep-research-falcon human AMBRA1 --fallback perplexity-lite` was attempted for this review. Falcon timed out after 600 seconds, then the configured Perplexity fallback failed with an API quota error. No provider-generated deep-research report was available, so this review uses the cached UniProt record, GOA seed, publication cache, Reactome cache, PANTHER family data, and Proteostasis PN projection files.

## Core biology

- AMBRA1 is a WD40-repeat autophagy regulator originally described as a BECN1-dependent positive regulator of autophagy. AMBRA1 deficiency caused autophagy impairment and accumulation of ubiquitinated proteins in mouse embryos [PMID:17589504 "positive regulator of the Becn1-dependent programme of autophagy"].
- AMBRA1 links ULK1 activation to the BECN1-PIK3C3 complex. Under basal conditions the BECN1-VPS34 complex is tethered to dynein through AMBRA1, and ULK1 phosphorylation releases AMBRA1 to support ER-associated autophagosome nucleation [PMID:20921139 "releasing the autophagy core complex from dynein"].
- AMBRA1 also interacts with BCL2 at mitochondria, connecting mitochondrial BCL2 pools with BECN1-dependent autophagy and apoptosis regulation [PMID:21358617 "binds preferentially the mitochondrial pool"].
- AMBRA1 is a mitophagy regulator. It interacts with PRKN/Parkin during mitochondrial depolarization and is important for mitochondrial clearance after Parkin recruitment [PMID:21753002 "critically important for subsequent mitochondrial clearance"].
- AMBRA1 can promote LC3-dependent mitophagy through its LIR motif in both PARKIN-dependent and PARKIN-independent contexts [PMID:25215947 "binds the autophagosome adapter LC3"].
- HUWE1 and IKKa regulate AMBRA1-mediated mitophagy, including phosphorylation near the LIR motif and MFN2 degradation [PMID:30217973 "regulates mitophagy through a novel pathway"].
- AMBRA1 functions as a CRL4/DDB1-CUL4 substrate receptor. CRL4AMBRA1 targets ELOC for degradation, thereby cross-regulating CRL5 assembly and activity [PMID:30166453 "targets Elongin C (ELOC)"].
- Multiple 2021 studies identify CRL4AMBRA1 as a cyclin D E3 ligase adaptor controlling G1/S progression through ubiquitin-dependent proteasomal degradation of D-type cyclins [PMID:33854239 "mediates ubiquitylation and proteasomal degradation of cyclin D"].
- AMBRA1 has non-core but supported regulatory roles through PP2A. It enhances PP2A-dependent MYC dephosphorylation/degradation [PMID:25438055 "enhances PP2A activity"] and PP2A/FOXO3-dependent regulatory T cell differentiation [PMID:30513302 "promotes the stability of the transcriptional activator FOXO3"].
- AMBRA1 has reported nuclear scaffolding roles in cancer cells, where Ambra1-bound nuclear complexes regulate transcriptional signaling [PMID:32616651 "scaffolds protein complexes at chromatin"].

## PN projection review

- The PN projection contains an exact existing GOA match for `GO:1990756 ubiquitin-like ligase-substrate adaptor activity` through the UPS CRL4 substrate receptor branch. This is consistent with the direct CRL4AMBRA1 literature and should be retained as a core molecular function.
- The PN projection also suggests `GO:1904716 positive regulation of chaperone-mediated autophagy` as more specific than the existing broad positive-autophagy GOA row. The AMBRA1-specific PN leaf in `autophagy_lysosome_pathway.yaml` is explicitly marked `curation_status: no_mapping`; the rationale says the label is contextual and does not support a universal GO assertion for all member genes.
- I did not find direct cached AMBRA1 evidence for LAMP2A/HSPA8-dependent CMA substrate uptake, substrate translocation, or CMA reporter assays. Therefore this review does not propose or accept `GO:1904716` for AMBRA1.

## Curation decisions

- Treat `GO:0005515 protein binding` rows as over-annotations. The papers often support biologically meaningful interactions, but generic protein binding hides the specific AMBRA1 functions: CRL4 substrate receptor/adaptor activity, ubiquitin ligase binding, protein phosphatase binding/activation, autophagy scaffolding, and mitophagy regulation.
- Treat `GO:0051020 GTPase binding` from PMID:25891078 as over-annotated for AMBRA1. The cached paper supports IRGM organization of autophagy regulators and a physical IRGM-AMBRA1 interaction, but does not establish AMBRA1 as a general GTPase-binding molecular-function effector.
- Treat `GO:0051897 positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction` as a term-choice problem. The Parkin/AMBRA1 paper supports local class III PI3K activation during mitophagy, not canonical PI3K/AKT signaling, so `GO:1901526 positive regulation of mitophagy` is the better replacement.
