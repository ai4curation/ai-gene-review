# PIF1 / PIL5 (Q8GZM7; At2g20180) curation notes

Session 2026-10-05/06 (phytochrome_photomorphogenesis module curation).

- Falcon deep research: the first attempt timed out, but a retry produced `PIF1-deep-research-falcon.md`, which was used as retrieval support. Claims used in the review were traced to primary literature.
- Identity check: PIF1_ARATH, Q8GZM7, 478 aa.

## Key evidence
- Pfr phytochrome binding [PMID:15448264 "PIF1 interacts specifically with the photoactivated conformer of phytochromes A and B"]; [PMID:15486102 "PIL5 preferentially interacts with the Pfr forms of Phytochrome A (PhyA) and Phytochrome B (PhyB)"].
- Rapid light-induced phosphorylation/degradation [PMID:18539749 "half-life of approximately 1 to 2 min under red light"]; CK2 contributes [PMID:21330376]; SPA1 kinase [PMID:31527679]; CUL4-COP1-SPA E3 [PMID:26037329 "The light-induced ubiquitylation and subsequent degradation of PIF1 is reduced in the cop1, spaQ and cul4 backgrounds"].
- Cofactor of COP1 in darkness [PMID:24858936 "enhances the substrate recruitment and autoubiquitylation and transubiquitylation activities of COP1"].
- Direct targets: GAI/RGA [PMID:17449805], SOM [PMID:21467583], PORC [PMID:18591656 "PIF1 directly binds to a G-box (CACGTG) DNA sequence element present in the PORC promoter"], 166 direct targets in seeds [PMID:19244139].
- Germination repression [PMID:16303558 "PIL5 represses seed germination and GA3ox expression in the dark"].

## Decisions
- protein binding: phyB rows -> MODIFY to phytochrome binding; PIF3/HFR1 -> heterodimerization; others REMOVE per policy.
- Four IEP rows from PMID:23708772 (review/meta-analysis of expression) -> MARK_AS_OVER_ANNOTATED.
- Chlorophyll / heme / GA biosynthesis rows kept as non-core (transcriptional, indirect).
