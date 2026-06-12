# SPCS2 (Signal peptidase complex subunit 2) — review notes

UniProt: Q15005 (SPCS2_HUMAN), 226 aa; aka SPC25, "Microsomal signal peptidase 25 kDa subunit". HGNC:28962, chr 11. Multi-pass ER membrane protein (two TM helices ~87-107 and 112-132), N and C termini cytosolic.

## Core identity / function
- One of three non-catalytic accessory subunits (SPCS1, SPCS2, SPCS3) of the ER signal peptidase complex (SPC). Catalytic subunits = SEC11A (SPC-A) / SEC11C (SPC-C).
  - UniProt FUNCTION: "Component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum (PubMed:34388369). Enhances the enzymatic activity of SPC and facilitates the interactions between different components of the translocation site (By similarity)." [UniProt Q15005]
  - UniProt SUBUNIT: "Component of the signal peptidase complex paralog A (SPC-A) composed of a catalytic subunit SEC11A and three accessory subunits SPCS1, SPCS2 and SPCS3 ... Within the complex, interacts with SEC11A or SEC11C and SPCS1 ... The complex induces a local thinning of the ER membrane which is used to measure the length of the signal peptide (SP) h-region."
- Note: unlike SPCS1, SPCS2 is described (by similarity to yeast Spc25/Q04969) as ENHANCING SPC enzymatic activity and facilitating translocation-site component interactions. Still non-catalytic.
- Cryo-EM structure: [PMID:34388369] identifies SPCS2 in both SPC paralogs (PDB 7P2P/7P2Q).
- Historical: SPC25 (=SPCS2) topology determined together with SPC12 in [PMID:8632014] (the 25-kDa subunit). [SPCS2 GOA itself does not cite 8632014, but UniProt links it.]

## Secondary / non-core
- PMID:34232536 (coronavirus interactome): IntAct interaction with SARS-CoV-2 Spike (P0DTC2). High-throughput; bare protein binding; non-core.

## Annotation assessment
- GO:0005787 signal peptidase complex (IBA, IEA, IPI/ComplexPortal) — CORE, ACCEPT.
- GO:0005789 ER membrane (IEA, IDA, ISS, TAS) — CORE localization, ACCEPT.
- GO:0016020 membrane (IEA) — generic; KEEP_AS_NON_CORE.
- GO:0045047 protein targeting to ER (IBA) — mis-specified; SPC acts after translocation. MODIFY -> GO:0006465 signal peptide processing (UniProt DR uses GO:0006465 IDA:ComplexPortal).
- GO:0016485 protein processing (IDA, ComplexPortal) — ACCEPT (correct; GO:0006465 is more specific). Core process.
- GO:0005515 protein binding (IPI PMID:34232536 SARS-CoV-2 S; IPI PMID:34388369 intra-complex SPCS1/SEC11A/SPCS3) — KEEP_AS_NON_CORE (bare protein binding).

## Core function summary
Non-catalytic accessory subunit of the ER signal peptidase complex; ER multi-pass membrane protein that enhances SPC enzymatic activity and facilitates interactions at the translocation site, contributing to signal peptide processing of preproteins.

## Falcon deep-research findings (incorporated 2026-06)

- A 2024 yeast study provides the most direct mechanistic evidence for the SPCS2 ortholog: depleting/mutating **Spc2** compromises the SPC's discrimination between substrates and its identification of the cleavage site [PMID:39565596 "discrimination between substrates and identification of the cleavage site by SPC is compromised when Spc2 is absent or mutated"]. MD simulations show **membrane thinning at the SPC center is reduced without Spc2** [PMID:39565596 "membrane thinning at the center of SPC is reduced without Spc2"]. The paper explicitly cross-references structural conservation to human SPCS2, sharpening the prior generic "enhances enzymatic activity" annotation into a substrate/cleavage-site-selection (fidelity) role. (Verified PubMed; not cached.)
- Falcon notes Spc2/SPCS2 is reported to mediate a transient interaction with the **Sec61 translocon via the Sec61beta subunit** and to constitute much of the **cytosolic face** of the SPC (from the Chung 2024 / structural literature). Consistent with the existing UniProt "facilitates the interactions between different components of the translocation site" statement; no separate reference added beyond PMID:39565596.
- The SPCS2-containing SPC executes a **noncanonical, post-insertional cleavage of Jaw1 (IRAG2/LRMP)** that is specific to the **SEC11A** paralog and enhances IP3R-mediated Ca2+ release [PMID:36789796 "the SPC with the catalytic subunit SEC11A, but not SEC11C, specifically cleaves Jaw1 ... the cleavage event enhances the augmentative effect of Jaw1 on the Ca2+ release ability of IP3Rs"]. Illustrates SPC paralog selectivity and an expanded substrate range; SPCS2 is an accessory subunit but no SPCS2-specific contribution is assigned. (Verified PubMed; not cached.)
- HCV assembly interactome: cell-derived **SPCS2 interacts with both HCV p7 and E2** [PMID:38230952 "Cell-derived PREB, STT3B, and SPCS2 as well as viral NS2 interacted with both p7 and E2"], implicating the SPCS2-containing SPC in HCV glycoprotein processing/assembly. Secondary host-pathogen role. (Verified PubMed; not cached.)
- Falcon also cites a SARS-CoV-2 interactome (Chen et al. 2021 bioRxiv/EMBO J) listing SPCS2 among spike-binding host factors. The existing review already captures the coronavirus spike interaction via PMID:34232536 (IntAct); the Chen preprint adds nothing verified beyond that, so not added.
- The "SPC quality-control / noncanonical cryptic-site cleavage" framing (SPCS2 affecting noncanonical cleavage "to varying extents") derives from Zanotti 2023, a PhD thesis (doi:10.11588/heidok.00033417, no PMID, not peer-reviewed primary literature). Not added as a reference (unverifiable as PMID); logged here only.
