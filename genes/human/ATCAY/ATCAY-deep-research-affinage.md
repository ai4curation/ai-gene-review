---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATCAY
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q86WG3
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 9
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATCAY (human)

## Current model (mechanistic narrative)

ATCAY (Caytaxin/BNIP-H) is a neuron-restricted CRAL-TRIO domain adaptor protein that organizes metabolic enzyme localization at neurite terminals to control neurotransmitter homeostasis and neurite outgrowth [PMID:14556008, PMID:16899818, PMID:26343454]. It directly binds kidney-type glutaminase (KGA), relocalizing it from mitochondria to neurite terminals and inhibiting its enzymatic activity to lower steady-state glutamate levels [PMID:16899818]. In parallel, Caytaxin couples the kinesin-1 light chain (KLC1) to ATP citrate lyase (ACL) to drive anterograde transport of ACL to terminals, where the ACL/BNIP-H complex recruits choline acetyltransferase (ChAT) to locally generate acetylcholine, which activates MAPK/ERK through muscarinic receptors to promote neurite outgrowth; loss of Caytaxin abolishes the KLC1–ACL and ACL–ChAT associations and impairs cholinergic motor neuron development [PMID:26343454]. The glutaminase complex is regulated post-translationally: NGF stimulation promotes binding of Pin1 to two cryptic C-terminal sites, which disrupts the BNIP-H/glutaminase complex [PMID:18628984], and the protein is targeted for ubiquitin-proteasome degradation by the E3 ligase CHIP (STUB1) at defined lysine residues [PMID:39703232]. Loss of Caytaxin function causes Cayman ataxia in humans and ataxia/dystonia in jittery mice, with expression of wild-type human Caytaxin rescuing the murine phenotype, establishing functional conservation [PMID:14556008, PMID:23226316].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0008289 lipid binding
- **localization:** GO:0005829 cytosol, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-112316 Neuronal System, R-HSA-1266738 Developmental Biology, R-HSA-392499 Metabolism of proteins
- **partners:** GLS (KGA), PIN1, KLC1, ACLY, CHAT, STUB1 (CHIP)
- **complexes:** BNIP-H/KGA glutaminase complex, KLC1/ATP citrate lyase/BNIP-H transport complex, BNIP-H/ACL/ChAT complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | High | ATCAY/Caytaxin was identified as the gene responsible for Cayman ataxia and jittery mouse ataxia/dystonia; it encodes a neuron-restricted protein containing a CRAL-TRIO motif, a domain common to proteins that bind small lipophilic molecules, with 3D structural modeling predicting a more polar ligand than vitamin E. | PMID:14556008 | Nature genetics |
| 2005 | Medium | Caytaxin is encoded by Atcay in rats; an intracisternal A particle (IAP) insertion into Intron 1 creates a hypomorphic allele in the genetically dystonic (dt) rat. Atcay transcript is neuronally restricted (absent from heart, spleen, lung, liver, muscle, kidney, testis) and expressed in all neuronal populations including cerebellar molecular, Purkinje, and granular layers, with developmental regulation peaking at P7 in hippocampus and increasing linearly in cerebellum. | PMID:16246457 | Brain research. Molecular brain research |
| 2006 | High | BNIP-H/Caytaxin directly binds kidney-type glutaminase (KGA) via protein-protein interaction; endogenous BNIP-H and KGA form a physiological complex in brain. BNIP-H overexpression relocalizes KGA from mitochondria to neurite terminals and reduces steady-state glutamate levels by inhibiting KGA enzyme activity. | PMID:16899818 | Journal of cell science |
| 2006 | Medium | Caytaxin deficiency in dt rats disrupts phosphatidylinositol signaling pathways, calcium homeostasis, and extracellular matrix interactions in cerebellar cortex; specifically, CRH-R1, CRH, and PMCA4 are upregulated in cerebellar cortex of caytaxin-deficient rats, implicating caytaxin in the molecular response of Purkinje cells to climbing fiber input. | PMID:17092653 | Neuroscience |
| 2008 | Medium | BNIP-H interacts with Pin1 (peptidyl-prolyl cis/trans isomerase) following nerve growth factor stimulation; they co-localize in neurites and cytosol of differentiating PC12 and P19 cells. Deletional mutagenesis mapped two cryptic Pin1-binding sites in the BNIP-H C-terminus; single point mutations in Pin1's WW domain abolished binding. BNIP-H harbors an intramolecular inhibitory interaction that must be disrupted for Pin1 binding. Pin1 expression disrupts the BNIP-H/glutaminase complex in NGF-stimulated PC12 cells, indicating competitive post-translational regulation. | PMID:18628984 | PloS one |
| 2009 | Medium | The Nxf1(CAST) allele suppresses the Atcay(hes) insertional mutation by approximately 2-fold increase in correctly-spliced Atcay mRNA and decrease in alternatively-processed mutant RNA, establishing that Nxf1-mediated mRNA nuclear export and splicing regulation can modulate caytaxin expression levels as a genetic suppressor. | PMID:19436707 | PLoS genetics |
| 2012 | Medium | Caytaxin protein is completely absent in severely ataxic Atcay(jit) and Atcay(swd) mouse mutants and markedly decreased in the mildly ataxic Atcay(ji-hes) line, establishing a correlation between protein level and phenotype severity. Expression of wild-type human Caytaxin in mutant sidewinder and jittery mice rescues the ataxic phenotype, demonstrating functional conservation between human and mouse orthologs. Caytaxin is expressed as multiple protein isoforms initiated from conserved upstream methionine start sites. | PMID:23226316 | PloS one |
| 2015 | High | BNIP-H/Caytaxin links kinesin-1 (KLC1) to ATP citrate lyase (ACL) and transports ACL to neurite terminals via this tripartite complex. At terminals, the BNIP-H/ACL complex recruits choline acetyltransferase (ChAT), leading to enhanced ACh secretion, which then activates MAPK/ERK via muscarinic receptors to promote neurite outgrowth. In BNIP-H-deficient mice, ACL fails to interact with KLC1 and the ACL/ChAT complex does not form. Bnip-h knockdown in zebrafish causes motor neuron developmental defects through impaired cholinergic pathway. | PMID:26343454 | Developmental cell |
| 2024 | High | BNIP-H/Caytaxin is ubiquitinated by the E3 ligase CHIP (STUB1); CHIP autoubiquitinates itself primarily at Lys23 and Lys31 in vitro, and CHIP-mediated ubiquitination of BNIP-H is abolished when four key lysine residues on BNIP-H are mutated to arginine. Hydrogen-deuterium exchange mass spectrometry supports a model in which transient N-terminal CHIP–BNIP-H interactions allow the CHIP U-box domain to swing and ubiquitinate BNIP-H, after which BNIP-H is degraded via the ubiquitin-proteasome pathway. | PMID:39703232 | PNAS nexus |

## Citations

- PMID:14556008
- PMID:16246457
- PMID:16899818
- PMID:17092653
- PMID:18628984
- PMID:19436707
- PMID:23226316
- PMID:26343454
- PMID:39703232
