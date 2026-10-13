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


## 2026-10-13 — source-specific augmentation

This dated assessment supersedes the earlier action rationales where stated below. The preceding journal remains verbatim, including its historical quotations and source-access observations. All 116 original annotation source objects match the 116 freshly fetched groups exactly; qualifiers, evidence, references and WITH/FROM are preserved. The prior successful Falcon report and artifacts remain intact.

### Receptor mechanism and products

The compact core is one ligand-activated receptor tyrosine kinase, with separate CSF1 and IL34 signaling branches. GO:0061514 now provides an explicit IL34 pathway term, correcting the earlier claim that none exists. Human receptor reconstitution was performed in cloned mouse macrophages, not human macrophages: [PMID:20504948](https://pmc.ncbi.nlm.nih.gov/articles/PMC2924605/), “huIL-34 stimulated macrophage proliferation” (abstract; full original Results/Methods distinguish the human construct from mouse-host experiments).

Human ectodomain studies establish CSF1 binding and D4-mediated homotypic contacts. The old D4–D5 contact wording was too definite: [PMID:22153499](https://pmc.ncbi.nlm.nih.gov/articles/PMC3260422/), “the possible contribution of D5 still remains unclear” (Discussion). The named CSF1–CSF1R complex is retained and used to refine its own source row; the generic receptor-complex core accommodates both ligands. GO:1990682 is not a captured typed child of GO:0043235. The original [PMID:22483114 supplement](https://ars.els-cdn.com/content/image/1-s2.0-S0969212612000664-mmc1.pdf) supports human IL34 ectodomain assembly and BLI for both ligands; the complete main article was not recovered.

Both official products reconstruct exactly, at 972 and 306 residues. Product 2 retains canonical residues 1–296, replaces 297–306, and lacks the canonical transmembrane and kinase regions. The engineered D1–D3 proteins used for structural work are not this numbered splice product. Sequence identity does not establish secretion, ligand affinity, antagonism or equivalent signaling by product 2.

### Positive interactions and source precision

The earlier removal of both generic screen interactions is superseded. The standing CLINGEN_MENDELIAN binding policy retains accurate positive interactions; here, the exact EPHB2 and EPHA7 partners support protein tyrosine kinase binding (GO:1990782). Four literal co-IP/AP-MS records and eight backbone ROGID matches are recorded, including tagged/pervanadate-treated HEK293 and spoke-expansion limits. No native encounter or functional cross-phosphorylation is inferred from [PMID:35384245](https://pmc.ncbi.nlm.nih.gov/articles/PMC9171411/).

The [PMID:35922511 original supplement](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-022-05028-x/MediaObjects/41586_2022_5028_MOESM4_ESM.xlsx) directly identifies the CSF1R ectodomain in Table 1 row 343 and reciprocal CSF1–CSF1R raw absorbance values in Table 2 rows 481 and 41. These are raw screen values, not affinity estimates. Table 3 row 70 imports affinity values from PMID:22483114. The [2024 author correction](https://www.nature.com/articles/s41586-024-07928-6) changes a different figure label, a concentration unit and scRNA citations; it does not report a CSF1R target-table correction.

Phosphatase binding is retained at non-core scope: substrate trapping in [PMID:16705167](https://pubmed.ncbi.nlm.nih.gov/16705167/) is a real positive interaction context even though CSF1R is the phosphatase substrate. The wild-type trapping comparison is negative; stable native complex formation and direct human construct identity are not inferred.

The human MCF10A source supports inhibition of cadherin adhesion rather than generic junction maintenance: [PMID:15117969](https://pubmed.ncbi.nlm.nih.gov/15117969/), “CSF-1R disrupts cell adhesion” (abstract; actual Y561/Src, internalization and motility experiments read). The cadherin–catenin complex itself remains intact. Engineered autocrine signaling is positive experimental evidence with a stated context, not an automatic reason to reject the process. Introductory mammary duct biology is distinct from performed acinar experiments.

### Developmental and viral contexts

Stress and ischemia definitions include expression responses. Their breadth does not make the positive responses false; they are retained as contextual roles. Mouse forebrain differentiation, survival and olfactory-bulb phenotypes remain positive within their species and intervention scope. Precise axon guidance is UNDECIDED: the actual growth-cone chemotaxis definition is not resolved by global callosal/GFAP developmental phenotypes or the human callosal association, but absence of that function is not established either.

The viral source problem and target biology are separate. [PMID:20889566](https://pmc.ncbi.nlm.nih.gov/articles/PMC2966802/) deletes Igf2r using Csf1r-promoter Cre and uses human IGF2R siRNA; it does not provide the presumed Csf1r perturbation. The inherited donor citation is marked MISCITED at that source-specific scope, with the original human source tuple preserved.

Later [PMID:25060299](https://link.springer.com/article/10.1007/s13365-014-0270-6) independently supports a contextual human fetal-microglial viral-output role. Its 470 nM GW2580 result lowers extracellular HIV p24 “without appreciable cell loss” (Results). No quantified viability test, receptor genetic confirmation or target-engagement assay is supplied. Ligand-only significance depends on removal of one control outlier and must not be conflated with the separately reported inhibitor contrasts. The endpoint is p24, not infectious progeny or viral entry. The manuscript cache lists three inhibitor doses whereas final publisher Methods list only 470 nM; the shared reported 470 nM result is used. Both authentic variants remain unchanged. The row is retained as non-core, with no new viral-stage term.

### Propagation and access boundaries

The actual 2,746-node tree, exact 972-residue target MSA and eleven on-path positive IBDs were reconstructed. A target's own experimental evidence is not circular. Current IBD donor lists differ from the historical GOA lists at rows 24, 35, 42 and 89; both are recorded rather than silently harmonized. All eleven ARBA rule outputs have genuine target-matching branches. Current source support identifies provenance, not an automatic biological verdict.

HPA supports plasma membrane and vesicles with cell-line-specific additional signals; no pixels or product-specific attribution were inspected. Seven actual Reactome paths through 24 objects identify the receptor. In the VENTX transcription event, the nuclear input is the gene while membrane CSF1R is the protein output; CSF1R is not the transcription catalyst.

Full-paper access is stated per source. PMID:26754294's precise CSF1R genetic panels and PMID:22902366's exact receptor pair panel remain unverified here; their positive curated assertions are retained with deference. Full original Methods/Results recovered externally are not falsely represented as present in an abstract-only cache. No cached publication, provider artifact or historical record was edited.

The [portable source-evidence index](CSF1R-source-evidence.yaml) contains literal identities, interaction and donor records, current phylogenetic/rule data, target tables and access locators. Its judgment mirrors refer to quotation hashes rather than repeat excerpts. The short new excerpts above and the current review total at most 25 words per primary source; inherited journal quotations are unchanged historical content.


## 2026-10-13: CSF1R PR #4979 evidence and core clarification

This assessment supersedes the preceding row 93 retention judgment only at the level of viral-process specificity. The positive human extracellular p24 result remains, and the original 2010 Igf2r/Csf1r-Cre source mismatch remains explicit. The 2015 inhibitor result does not distinguish receptor regulation of viral activity from altered host state without receptor-specific intervention and viable-cell normalization; row 93 is therefore MARK_AS_OVER_ANNOTATED, not a claim of absent viral effects. Ligand-only outlier dependence, separately significant inhibitor contrasts, and the manuscript/publisher dose difference remain distinct.

The single core now explicitly includes tyrosine catalysis, autophosphorylation and major phagocyte differentiation/proliferation outputs. GO:0005011 already includes the kinase chemistry and descends from GO:0004714; a duplicate generic kinase MF would repeat the same activity. The complex field identifies GO:1990682 for the CSF1-bound assembly only. IL34 signaling remains represented independently of that ligand-specific complex; no unverified IL34 complex identifier is supplied. These existing accepted processes are not NEW annotations.

Positive supported_by pointers now connect the reviewed claims to their actual source publications or the portable source-evidence sections. Short source-exact excerpts are included for representative receptor, cytokine-binding, differentiation, stress-response, axon-phenotype and phosphatase-partner claims. Quotes appear once in the review; the sidecar carries hashes and locators. Source pointers without repeated text prevent multiplication of identical quotations across parallel GOA records. PMID:11157073 supplies additional rat/mouse microglial SHP1-association context for row 59; it does not replace the original transfer or establish a human-specific experiment.

Row 38 remains UNDECIDED after actual full main-text access to PMID:22542597 because the receptor-dependent guidance mechanism is unresolved. The enum includes unclear annotations as well as inaccessible evidence. Broad stress and organ-development annotations remain positive, contextual judgments supported by explicit expression and developmental data. There is no requested action quota. The standing CLINGEN_MENDELIAN Curation instructions govern positive generic binding; the two EPH-receptor screen associations already have supported partner-class refinements and are not removed merely for being non-core.

All 116 original source objects, ordinary qualifiers, the two product descriptions, original caches and the complete preceding notes history remain exact. The public evidence sidecar retains all literal raw sections for auditability. Its reference assessment now identifies manual provenance rather than independent primary evidence. DRAFT is the prior genuine updater result, reflecting unresolved review content; it is not a hand-selected desired status. Current ordinary validation and status results are recorded with this follow-up.


## 2026-10-13: CSF1R second follow-up, source anchors and process specificity

This entry supersedes the earlier row 32 retention rationale. The complete original ischemia paper was recovered from the [publisher PDF](https://link.springer.com/content/pdf/10.1007/s004010050550.pdf) and its main Methods, Results, Discussion and captions were read. Recombinant human CSF1 delivery improved neuronal survival in mouse cortical lesions; receptor mRNA/protein increased. The study did not perturb the receptor, and neuronal receptor mediation was proposed rather than experimentally isolated. Row 32 is now MARK_AS_OVER_ANNOTATED for the broad electronic stress-process inference, while preserving these positive observations. The original abstract cache is unchanged; external full-text access is explicitly distinguished from cache composition.

The [GO Consortium annotation guidance](https://pmc.ncbi.nlm.nih.gov/articles/PMC3706743/) allows expression-based response annotations in some circumstances and also permits declining them because changed expression does not itself establish contribution. Its direct-versus-indirect mutant discussion calls for biological interpretation. Neither guidance nor the current stress definition requires the receptor to be an intrinsic stress sensor. The current GO evidence-code guide still lists IEP; the separately attempted wiki IEP page returned HTTP 403, so no new read of that page is claimed.

Row 98 remains KEEP_AS_NON_CORE. The [actual mouse progenitor study](https://pubmed.ncbi.nlm.nih.gov/22542597/) includes purified Nestin-GFP clonal ligand assays and neural Csf1r conditional deletion with normal microglial development, in addition to global brain phenotypes. Receptor-mediated control of progenitor maturation contributes to organ formation. The assays separate part of that role from microglial loss; they do not establish that every global phenotype is direct or that a human neural product was tested. Relevant main-text locators are the clonal differentiation Results, conditional deletion Results/Figures 7–8/Table 3, and Discussion on neural and microglial contributions (paragraph-index entries 65, 74–75 and 82–85). Existing axon-guidance uncertainty remains distinct.

Seven concise excerpts were added for topology, bivalent assembly, neural-conditional scope and the four named Reactome events. Each appears once in the review; the sidecar contains only its hash and locator. The Reactome titles identify events, while their preserved structured entity paths establish the membrane compartment. Restoring 161 repeated historical excerpts would exceed the per-source quotation budget; the immutable historical record and all positive evidence pointers remain available. The 17 sole-index pointers now have exact paths to literal rule, donor or IBD records in the public sidecar. These machine-checkable provenance locators are not presented as primary experiments or independent scientific corroboration.

The biological description adds the ligand-contact and CSF1 assembly context without asserting that IL34 is the CSF1-named complex. The single receptor core, both product descriptions, all 116 original source objects, ordinary qualifiers and all existing source caches remain unchanged. The preceding journal is retained byte for byte.

Status precision: the ordinary updater computes DRAFT when there are no PENDING rows but validation warnings remain. UNDECIDED is a scientific disposition and is not by itself the updater's criterion. The earlier wording tying DRAFT generally to unresolved content is superseded by this algorithm-specific explanation; the new ordinary check receipts determine the actual status.
