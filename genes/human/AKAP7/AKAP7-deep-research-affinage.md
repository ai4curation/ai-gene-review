---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AKAP7
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: O43687
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 12
citation_count: 12
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AKAP7 (human)

## Current model (mechanistic narrative)

AKAP7 (AKAP15/AKAP18) is an A-kinase anchoring protein that tethers PKA—and PKC—to defined subcellular sites to enable spatially restricted phosphorylation of ion channels and Ca2+-handling proteins [PMID:11733497, PMID:9748250, PMID:22670899]. It anchors PKA to skeletal muscle L-type Ca2+ channels through a leucine-zipper interaction with the CaV1.1 alpha1 C-terminus, where disrupting this interaction blocks voltage-dependent channel potentiation [PMID:11733497], and to brain Nav1.2 sodium channels by binding the intracellular I-II loop, positioning PKA at defined serine sites whose phosphorylation is gated by prior PKC modification [PMID:9748250, PMID:12359152]. PKA recruitment is mediated by a PKA-binding domain that contacts the RIIα D/D domain through anchor points flanking the core binding helix [PMID:27102985]. Beyond scaffolding, the central 2H phosphoesterase domain of long isoforms binds AMP and functions as a 2',5'-phosphodiesterase that degrades the 2-5A activators of RNase L, an activity abolished by the H185R mutation and dependent on cytoplasmic localization for antiviral function [PMID:18082768, PMID:24987090]. In the heart, long isoforms (AKAP7γ/δ) scaffold PKA together with the deubiquitinase USP4 at sarcomere Z bands via the phosphoesterase domain; anchored PKA phosphorylates USP4 at Ser829 to stimulate its deubiquitinase activity and promote SERCA2-mediated SR Ca2+ reuptake [PMID:40449590]. In the brain, the AKAP7/PKA complex in dentate granule cell mossy fibers is required for cAMP-dependent presynaptic LTP and pattern-separation behavior [PMID:27911261]. Notably, global AKAP7 deletion leaves β-adrenergic Ca2+ handling in mouse ventricular cardiomyocytes intact, indicating its cardiac role is context- and isoform-specific rather than essential for canonical β-adrenergic Ca2+ regulation [PMID:23035250].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0140096 catalytic activity, acting on a protein, GO:0016787 hydrolase activity, GO:0140098 catalytic activity, acting on RNA
- **localization:** GO:0005886 plasma membrane, GO:0005634 nucleus, GO:0005829 cytosol, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-112316 Neuronal System, R-HSA-168256 Immune System, R-HSA-397014 Muscle contraction
- **partners:** PRKAR2A, CACNA1S, SCN2A, USP4
- **complexes:** AKAP18/PKA/USP4 Z-band complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | High | AKAP15 (AKAP7α) directly interacts with the C-terminal domain of the CaV1.1 alpha1 subunit via a leucine zipper (LZ) motif, anchoring PKA to skeletal muscle L-type Ca2+ channels; disruption of the LZ interaction inhibits voltage-dependent potentiation of L-type Ca2+ channels. | PMID:11733497 | The Journal of biological chemistry |
| 1998 | High | AKAP15 (AKAP7) co-purifies with rat brain sodium channels and anchors PKA to the Nav1.2 alpha subunit; AKAP15 was identified by mass spectrometry in purified sodium channel preparations and co-immunoprecipitates with the sodium channel alpha subunit, enabling PKA phosphorylation of four serine residues on the channel. | PMID:9748250 | The Journal of biological chemistry |
| 2002 | High | AKAP-15 (AKAP7) binds specifically to intracellular loop I-II (L(I-II)) of Nav1.2a sodium channels, targeting PKA directly to its phosphorylation sites (S554, S573, S576, S687); PKC phosphorylation of S576 enhances subsequent PKA modulation requiring additional phosphorylation at S687, revealing convergent multi-site regulation. | PMID:12359152 | Molecular and cellular neurosciences |
| 2007 | High | The central domain of AKAP18δ (AKAP7δ) is a member of the 2H phosphoesterase family, featuring two conserved His-x-Thr motifs; X-ray crystallography reveals this domain specifically binds AMP and CMP in a groove between two pseudo-2-fold-related lobes, with AMP affinity in the physiological concentration range. | PMID:18082768 | Journal of molecular biology |
| 2014 | High | Mouse AKAP7 contains a functional 2',5'-phosphodiesterase (2',5'-PDE) domain that rapidly degrades 2',5'-oligoadenylate (2-5A) activators of RNase L; the PDE domain requires cytoplasmic localization for antiviral activity (as shown by complementation of ns2-mutant coronavirus), while full-length AKAP7 localizes to the nucleus and cannot complement. A single point mutation AKAP7(H185R) abolishes PDE activity. | PMID:24987090 | mBio |
| 2016 | High | Crystal structure of AKAP18β PKA-binding domain bound to the D/D domain of PKA RIIα reveals three hydrophilic anchor points outside the core PKA-binding helix that mediate contacts with the D/D domain; in vitro and cell-based experiments confirm these anchor points are required for RII subunit interaction with AKAP18. | PMID:27102985 | The Biochemical journal |
| 2016 | High | Genetic ablation of AKAP7 specifically from dentate granule cells disrupts mossy fiber–CA3 LTP initiated by cAMP and impairs pattern separation behavior, establishing that the AKAP7/PKA complex in mossy fiber projections is essential for presynaptic PKA-dependent plasticity and spatial discrimination. | PMID:27911261 | eLife |
| 2012 | High | AKAP7 knockout mice (all isoforms deleted) show normal cardiomyocyte responses to β-adrenergic stimulation: Ca2+ current, intracellular Ca2+ transients, Ca2+ reuptake, and phosphorylation of CaV1.2 and phospholamban are unaffected, indicating AKAP7 is not required for regulation of Ca2+ handling in mouse ventricular cardiomyocytes. | PMID:23035250 | Proceedings of the National Academy of Sciences of the United States of America |
| 2012 | Medium | AKAP7γ and AKAP7α both interact with multiple PKC isoenzymes via multi-site binding on both proteins; AKAP7 scaffolding enhances PKC substrate phosphorylation (shown by FRET-based activity reporter) and restricts PKC mobility within cells (shown by FRAP and virtual modeling). | PMID:22670899 | The Biochemical journal |
| 2006 | Low | AKAP18 isoforms and PDE4 family phosphodiesterases are differentially localized in renal collecting duct principal cells, where AKAP-anchored PKA participates in AVP-stimulated aquaporin-2 (AQP2) phosphorylation and redistribution to the plasma membrane. | PMID:16500722 | European journal of cell biology |
| 2022 | Medium | AKAP7γ (long isoform) is highly mobile within cardiomyocytes as demonstrated by FRAP of GFP-tagged AKAP7γ; PKA activation accelerates AKAP7γ-GFP wash-out upon saponin permeabilization, indicating PKA signaling increases AKAP7γ mobility, which may contribute to spatial propagation of β-adrenergic signaling to SR Ca2+ uptake. | PMID:35620477 | Function (Oxford, England) |
| 2025 | High | Long AKAP18 isoforms (AKAP7γ/δ) scaffold PKA together with ubiquitin-specific proteinase USP4 at cardiac sarcomere Z bands via the AKAP18 2'-phosphoesterase domain; AKAP18-anchored PKA phosphorylates USP4 at Ser829 near its active site, stimulating USP4 deubiquitinase activity. Pharmacological PKA inhibition or AKAP7 gene deletion decreases calcium flux through SERCA2, establishing the AKAP18/PKA/USP4 complex as a regulator of SR Ca2+ reuptake. | PMID:40449590 | The Journal of biological chemistry |

## Citations

- PMID:11733497
- PMID:12359152
- PMID:16500722
- PMID:18082768
- PMID:22670899
- PMID:23035250
- PMID:24987090
- PMID:27102985
- PMID:27911261
- PMID:35620477
- PMID:40449590
- PMID:9748250
