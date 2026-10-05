# CSF1R (human, P07333) curation notes

## Status of inputs

- `just fetch-gene human CSF1R` was run before this session (uniprot, goa, stub).
- `just fetch-gene-pmids human CSF1R` completed; all GOA PMIDs cached.
- `just deep-research-falcon human CSF1R` launched in parallel (no perplexity key, no fallback).
  Status recorded at the end of this file.
- Extra publications cached for this review (via `just fetch-pmid`): PMID:11756160 (Csf1r KO mouse),
  PMID:18467591 (IL-34 discovery), PMID:20489731 (IL-34 vs M-CSF), PMID:22197934 (HDLS),
  PMID:30982608, PMID:30982609 (biallelic CSF1R disease), PMID:22542597 (Csf1r and corticogenesis),
  PMID:20889566 (source of the mouse "host-mediated activation of viral process" annotation),
  PMID:16705167 (PTPN2/Tcptp dephosphorylates CSF-1R), PMID:21727904, PMID:16170366,
  PMID:23408870, PMID:18342505.

## Identity / architecture

- Class III receptor tyrosine kinase (CSF-1/PDGF receptor subfamily, with KIT, FLT3, PDGFRA/B).
  972 aa; five extracellular Ig-like domains, single TM helix, juxtamembrane autoinhibitory region,
  split kinase domain [PMID:2421165 "The 972-amino-acid c-fms protein has an extracellular domain, a membrane-spanning region, and a cytoplasmic tyrosine protein kinase domain"].
- c-fms proto-oncogene; v-fms from McDonough feline sarcoma virus differs at C-terminus [PMID:2421165].
- UniProt: "Tyrosine-protein kinase that acts as a cell-surface receptor for CSF1 and IL34 and plays an essential role in the regulation of survival, proliferation and differentiation of hematopoietic precursor cells, especially mononuclear phagocytes, such as macrophages and monocytes." [file:human/CSF1R/CSF1R-uniprot.txt]
- Catalysis: EC 2.7.10.1, L-tyrosyl-[protein] + ATP = O-phospho-L-tyrosyl-[protein] + ADP [UniProt].

## Ligands and receptor assembly

- Two unrelated dimeric helical cytokine ligands: CSF1 (M-CSF) and IL-34.
  IL-34 receptor identified by extracellular-domain screen [PMID:18467591 "we used a collection of extracellular domains of transmembrane proteins to discover the receptor for IL-34, which was a known cytokine receptor, colony-stimulating factor 1 (also called macrophage colony-stimulating factor) receptor"].
- Human ternary complex: 1 CSF-1 dimer : 2 CSF-1R ectodomains, high affinity, with homotypic D4/D5
  receptor-receptor contacts [PMID:22153499 "the complex is characterized by bivalent binding of hCSF-1 to the receptor ectodomain (1 hCSF-1 dimer to 2 molecules of hCSF-1RD1-D5)"].
- Mouse M-CSF:FMS crystal structure; two-step activation, D4-D5 needed for dimerization
  [PMID:19017797 "Calorimetric data indicate that M-CSF cannot dimerize FMS without receptor-receptor interactions mediated by FMS domains D4 and D5"].
- IL-34 complex architecture similar to CSF-1 complex [PMID:22483114 "the complex architecture of IL-34 bound to the N-terminal immunoglobulin domains of CSF-1R is similar to the CSF-1/CSF-1R assembly"]; [PMID:23478061 "bivalent binding of human IL-34 to CSF-1R leads to an extracellular assembly hallmarked by striking similarities to the CSF-1:CSF-1R complex, including homotypic receptor-receptor interactions"]; [PMID:26235028 crystal structures of hCSF-1:hCSF-1R ternary complexes].
- EBV BARF1 sequesters hCSF-1 (decoy) [PMID:22902366].

## Kinase activation and signaling

- Ligand-induced dimerization -> trans-autophosphorylation (Y561 juxtamembrane, Y699, Y708, Y723 kinase insert, Y809 activation loop, Y923, Y969). Docking: SRC family (Y561, Y809), GRB2 (Y699, Y923), PIK3R1 (Y723), PLCG2 (Y723, Y809), CBL (Y969) [UniProt PTM section].
- SRC/FYN/YES activation and binding to receptor; Y809 mutant reduced binding [PMID:7681396 "CSF-1 stimulation resulted in activation of three Src family kinases, Src, Fyn and Yes. Concomitant with their activation, all three Src family kinases were found to associate with the ligand-activated CSF-1 receptor"].
- CSF1R downstream: ERK1/2, PI3K-AKT, PLCG2/PKC, STAT3/5 [UniProt; Reactome R-HSA-6787820].
- IL-34 and CSF-1 both drive CSF-1R tyrosine phosphorylation and macrophage proliferation [PMID:20504948 "muIL-34 and a muIL-34 isoform lacking Q81 stimulated mouse macrophage proliferation, CSF-1R tyrosine phosphorylation, and signaling and synergized with other cytokines to generate macrophages and osteoclasts from cultured progenitors"].
- IL-34 signal stronger but transient vs M-CSF [PMID:20489731 "IL-34 induced a stronger but transient tyrosine phosphorylation of Fms and downstream molecules, and rapidly downregulated Fms"].
- Downregulation: ubiquitination/internalization (CBL), dephosphorylation by PTPN2 [PMID:16705167 "we have identified the CSF-1 receptor (CSF-1R) as a physiological target of Tcptp through substrate-trapping experiments"]. CSF-1R also clears circulating CSF-1 by endocytosis [PMID:11756160 "The circulating CSF-1 concentration in Csf1r(-)/Csf1r(-) mice was elevated 20-fold, in agreement with the previously reported clearance of circulating CSF-1 by CSF-1R-mediated endocytosis and intracellular destruction"].
- Kinase inhibitors (imatinib, GW2580 etc.) [PMID:16170366 "imatinib is also an effective inhibitor of the closely related FMS receptor for macrophage colony stimulating factor"].

## Biology (largely mouse genetics)

- Csf1r KO phenocopies Csf1 op/op: osteopetrosis, tissue macrophage deficiency, reproductive defects [PMID:11756160 "The phenotype of Csf1(-)/Csf1r(-) mice closely resembled the phenotype of CSF-1-nullizygous (Csf1(op)/Csf1(op)) mice, including the osteopetrotic, hematopoietic, tissue macrophage, and reproductive phenotypes"].
- Monocyte development CSF1R-dependent [PMID:19132917 "monocytes originate in the bone marrow in a Csf-1R (MCSF-R, CD115)-dependent manner"].
- Anti-CSF-1R antibody depletes Ly6C-lo monocytes and resident macrophages [PMID:21727904].
- Microglia: CSF1R drives microglial proliferation in prion disease [PMID:23392676 "We identified the system of CSF1R and its mitogens, CSF1 and IL34, as the main drivers of microglial proliferation during chronic neurodegeneration"]; biallelic loss in human -> absence of microglia [PMID:30982608 "Post-mortem analysis identified a complete absence of microglia within the brain"].
- Chemokine production: M-CSF/IL-34 induce MCP-1/CCL2, IP-10, IL-8 in human whole blood, blocked by GW2580 [PMID:20829061].
- Epithelial: autocrine CSF-1R in MCF-10A acini disrupts E-cadherin junctions via SRC (Y561) [PMID:15117969 "autocrine CSF-1R activation induces hyperproliferation and a profound, progressive disruption of junctional integrity in acinar structures formed by human mammary epithelial cells"]. Note this is a pathological/overexpression model; it argues *against* "cell-cell junction maintenance" as a physiological role; the effect is disruption.
- Neural: Nandi et al. (mouse) propose a neural-progenitor-intrinsic role (Nestin-Cre deletion) [PMID:22542597]; source of mouse IMP annotations transferred to human (olfactory bulb development, forebrain neuron differentiation, axon guidance, negative regulation of proliferation, negative regulation of apoptosis). Neuronal CSF1R expression is debated; most CNS effects are thought to be mediated by microglia.

## Disease

- HDLS / ALSP (adult-onset leukoencephalopathy with axonal spheroids, autosomal dominant), kinase-domain mutations abolish autophosphorylation [PMID:22197934 "Upon stimulation with CSF-1, autophosphorylation on multiple CSF1R tyrosine-residues was observed for CSF1RWT, while none of the mutants showed detectable levels of autophosphorylation"].
- BANDDOS (biallelic): brain malformation, absent microglia, dysosteosclerosis [PMID:30982608; PMID:30982609].
- Overexpression in breast, ovarian cancer; target of TAM-depleting drugs (pexidartinib) [UniProt disease notes].

## Annotation-specific issues

- `GO:0044794 host-mediated activation of viral process` IEA (Ensembl Compara from mouse): mouse source is IGI from PMID:20889566 (IGF2R and HIV), which used a *Csf1r-driven* Igf2r knockout; Csf1r is only the Cre driver. Spurious -> REMOVE.
- `GO:0019903 protein phosphatase binding` IEA: source mouse IPI PMID:16705167 = CSF-1R is a PTPN2 substrate. Enzyme-substrate contact, not a CSF1R function -> over-annotation.
- Protein binding IPIs: partners CSF1 (P09603) and IL34 (Q6ZMJ4-1) from structural papers -> MODIFY to cytokine binding (GO:0019955); EPHA7/EPHB2 from RTK interactome (PMID:35384245) -> REMOVE (uninformative).
- `GO:0045217 cell-cell junction maintenance` (IMP, PMID:15117969): the paper shows CSF-1R *disrupts* junctions; the curator presumably captured "involved in" via the loss of junctions after hyperactivation; marked over-annotated rather than removed.
- `GO:0060603 mammary gland duct morphogenesis` TAS PMID:15117969: paper's intro states CSF-1R required for ductal outgrowth, attributed to macrophage recruitment -> non-core.

## Deep research status

- `just deep-research-falcon human CSF1R` SUCCEEDED (~21 min; 60 citations) ->
  `CSF1R-deep-research-falcon.md`. Consistent with this review: CSF1/IL-34-activated cell-surface
  receptor tyrosine kinase driving myeloid trophic/differentiation signaling.
- Additional points from falcon (not independently verified, not cached as publications):
  - Yu et al. 2008 (doi:10.1189/jlb.0308171): in Csf1r-/- macrophages, WT receptor rescues survival,
    proliferation, differentiation and morphology; receptor lacking all eight intracellular tyrosines does not;
    Y559F and Y807F (mouse numbering) strongly impair responses.
  - Dorion et al. 2024 (doi:10.1186/s13024-024-00723-x): ALSP p.V784M iPSC-microglia show reduced surface
    CSF1R and autophosphorylation, impaired migration; knockdown/isogenic data support haploinsufficiency.
  - Chadarevian et al. 2024 (Neuron; doi:10.1016/j.neuron.2024.05.023): p.L786S microglia proliferate poorly;
    isogenic correction restores engraftment in a chimeric mouse model.
  - Clinical: CSF1R inhibitors pexidartinib (ENLIVEN) and vimseltinib (MOTION) treat tenosynovial giant cell tumor.
- These support the suggested question on haploinsufficiency vs dominant-negative mechanisms in ALSP.
