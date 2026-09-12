# LMTK1 review notes

## 2026-08-09 setup, naming, and research provenance

- HGNC REST (`HGNC:21`, checked 2026-08-09) now approves **LMTK1** (lemur tail kinase 1) as the human symbol and records **AATK** as the previous symbol; the symbol-change date is 2026-07-09. The same record maps LMTK1 to UniProt Q6ZMQ8, NCBI Gene 9625, Ensembl ENSG00000181409, and mouse MGI:1197518. The live NCBI Gene 9625 record also uses LMTK1.
- The upstream protein/annotation records have not yet fully absorbed this very recent rename. UniProt Q6ZMQ8 entry version 169 is dated 2026-06-10, one month before the HGNC change: its entry name and recommended protein name use LMTK1, but its gene line still reads `Name=AATK` with `LMTK1` among the synonyms. Live QuickGO rows likewise use AATK as the gene-product symbol. This is an upstream lag, not a second human gene.
- Accordingly, bare `just fetch-gene human LMTK1` did not accept the synonym-only UniProt match. `just fetch-gene human LMTK1 --uniprot-id Q6ZMQ8` correctly seeded the review under the approved HGNC symbol while retaining the source GOA rows for Q6ZMQ8.
- Falcon deep research failed with Edison HTTP 402. The Perplexity fallback failed with HTTP 401. No provider-branded deep-research file was created or replaced with manual content. This note therefore records manual synthesis from the cached primary papers, live HGNC/NCBI/QuickGO checks, and the reviewed UniProt record.

## Identity and isoform boundaries

- Reviewed human Q6ZMQ8 is a 1,374-aa protein with a predicted N-terminal transmembrane helix at residues 32-52 and a protein-kinase domain at residues 125-395. The current record has three numbered isoforms. Q6ZMQ8-2 (`hAATYKs-p35BP`) lacks residues 1-433, and therefore lacks both the displayed N-terminal transmembrane segment and the kinase domain; Q6ZMQ8-3 retains the N terminus and kinase domain but lacks residues 468-503 and 916-1374.
- Historical AATYK1A/AATYK1B or AATKA/AATKB names do **not** map one-to-one onto current UniProt isoform numbers. The neuronal literature generally calls a 1,317-aa, transmembrane-domain-free protein AATYK1A/LMTK1A and a 57-aa N-terminally extended, transmembrane form AATYK1B. The human melanoma study independently calls these human AATKA (1,317 aa, cytoplasmic) and AATKB (the additional N-terminal 57 aa) [PMID:24589855, full-text methods verified at the publisher although the local cache is abstract-only]. Neither should be relabeled as current `isoform 1` or `isoform 2` without sequence-level mapping.
- PMID:14521924 cloned a 477-aa human brain splice fragment called `hAATYKs-p35BP`, corresponding to the current kinase-domain-free Q6ZMQ8-2 concept. The paper then made an engineered `hAATYKs` construct by fusing the KIAA0641 kinase domain to that fragment. Therefore, binding of the native short fragment to p35/CDK5R1 is separable from phosphorylation experiments performed with the engineered kinase-containing construct.
- Compartment claims must remain isoform-bounded. In particular, palmitoylation-dependent recycling-endosome localization of the transmembrane-domain-free AATYK1A in rodent neurons/COS-7 cells does not establish that every human isoform has that topology or localization, and the generic UniProt `membrane` mapping should not be used to assign all isoforms to membranes.

## Evidence hierarchy

### 1. Direct human catalytic evidence: PMID:35902728

- This is the decisive molecular-function paper. It used a human AATK coding sequence (the construct source traces to the full-length human AATKA/AATKB work of Ma and Rubin), human TREx293/HEK293T, MCF-7, U343/U251, HCT116, and Sk-Mel13 cells, wild-type and ATP-pocket kinase-dead AATK, peptide kinomic profiling, immunoprecipitation, and an in-vitro kinase assay. The exact isoform used is not stated clearly enough to map to a current Q6ZMQ8 isoform number.
- The abstract states: "Via large-scale kinomic profiling and kinase assays, we demonstrate that AATK acts a Ser/Thr kinase that phosphorylates TP53 at Ser366." The full results further report: "In contrast to the controls and AATK KD a clearly increased phosphorylation level of TP53 at Ser366 was identified (Fig. 5D)." This is direct evidence for human LMTK1 protein serine kinase activity and a defined human substrate/site (TP53 Ser366), not an orthology inference.
- The authors appropriately distinguished kinase-class profiles: "The individual basal activity profiles of all three replicates for AATK wt and AATK KD in the PTK assay was very heterogeneous (Fig. S11A). In contrast, the activity profiles from the STK assay comparing the AATK wt and AATK KD expressing clone pools depicted a clearly diverging activity profile (Fig. S11B)." This makes GO:0106310 protein serine kinase activity the strongest core MF; GO:0004674 protein serine/threonine kinase activity is a valid broader representation. GO:0018105 peptidyl-serine phosphorylation is a defensible new process annotation with TP53 (UniProtKB:P04637) as the supporting entity.
- The same paper ties catalysis to a growth phenotype: "The kinase activity of AATK in comparison to the kinase-dead mutant mediates a decreased expression of the key cell cycle regulators Cyclin D1 and WEE1. Moreover, growth suppression through AATK relies on its kinase activity." This supports a human negative-regulation-of-cell-population-proliferation role, but the proposed downstream CCND1/WEE1 cascade is broader than the directly demonstrated TP53 phosphorylation reaction.

### 2. Other human or human-cell evidence

- PMID:24589855 used full-length human AATKA and AATKB constructs plus human AATK shRNAs in human melanoma lines. Its abstract reports: "Overexpression of AATK inhibited cell proliferation, colony formation, and promoted apoptosis in melanoma cell lines derived from primary and metastatic melanomas." This independently corroborates growth suppression and apoptosis in human cells. It does not identify a catalytic substrate, and its A/B nomenclature must not be converted to current Q6ZMQ8 isoform numbers.
- PMID:10837911 used human SH-SY5Y neuroblastoma cells and reports that immunoprecipitated AATYK was an active kinase, cytoplasmic, and promoted neuronal differentiation. However, the abstract only says the cells were transfected "with AATYK cDNA" after introducing AATYK as a protein isolated from mouse 32D cells; it does not state the cDNA species. With the full text unavailable locally, this is direct evidence in a human cellular environment but should **not** be called unambiguous direct assay of the human Q6ZMQ8 protein.
- PMID:14521924 is direct human-sequence evidence for p35/CDK5R1 binding. It states: "A 3(')-terminal fragment of a splice variant of KIAA0641, a human homologue of apoptosis-associated tyrosine kinase (AATYK), was screened from human brain cDNA libraries by a yeast two-hybrid system using a Cdk5 activator p35 as a bait." Binding was tested with a human fragment in rat brain extract and with human constructs in HEK293 cells. The later full-text mouse/rat study clarifies that LMTK1A binds p35, not CDK5 directly: "Both p35 and Cdk5 were detected in the immunoprecipitates when Cdk5 and p35 were coexpressed ... however, Cdk5 was not found in the immunoprecipitates in the absence of p35 ... All these results indicate that AATYK1A binds to p35 but not to Cdk5." [PMID:20422042]. LMTK1 is a CDK5/p35 substrate/regulatory target; these data do not make it a CDK5 activator or a stable CDK5 complex subunit.

### 3. Seeded human interaction screens

| PMID | Q6ZMQ8 partner(s) in live GOA | Paper-level assay context | Interpretation |
|---|---|---|---|
| 22321011 | PPP1CA/P62136 | Human-brain high-throughput yeast two-hybrid survey of PP1α interactors | Direct binary screen support for PP1α binding; pair-specific evidence is in the screen data/GOA, not named in the abstract. |
| 25852190 | PPP1CA/P62136; PPP1CC/P36873 | Human DLD-1 TRAIL kinase screens plus mass-spectrometry interaction mapping and phosphoproteomics | Resource-level interaction evidence; the abstract foregrounds other kinases, so it does not establish an LMTK1 mechanism. |
| 28065597 | PPP1CA/P62136; PPP1CC/P36873 | Human MYTH and MaMTH RTK-phosphatase interactome | Binary/mammalian interaction support, but the authors explicitly warn that interactions are not equivalent to enzyme-substrate relationships. |
| 32296183 | TEPSIN/Q96N21 | HuRI proteome-scale human yeast-two-hybrid map with pairwise retesting and sequence confirmation | A binary contact, not evidence that TEPSIN regulates LMTK1, is its substrate, or forms a stable complex. |
| 35384245 | PPP1CC/P36873 | Human RTK atlas using AP-MS, BioID, and in-vitro kinase assays | The paper-level methods cannot by themselves identify which modality produced this particular GOA pair; no stable-complex or enzyme-substrate inference is warranted. |

- The independent recovery of PPP1CA/PPP1CC in four human interaction datasets makes a PP1-family association more credible than a one-off generic binding hit. GO:0008157 protein phosphatase 1 binding is therefore substantially more informative than GO:0005515 protein binding.
- PMID:17267545 supplies a mechanistic precedent from **AATYK1 expressed in Xenopus oocytes**, but the cached abstract does not identify the construct species: PP1 docking and SPAK-binding motifs were required for catalytic-independent inhibition of NKCC1. The abstract concludes that AATYK1 acts by "scaffolding an inhibitory phosphatase in proximity to a stimulatory kinase." This supports an adaptor/scaffold hypothesis for the repeated human PP1 interactions; it is not direct human evidence for the NKCC1 pathway and does not establish a persistent multiprotein complex.

### 4. Rodent and heterologous neuronal/endosomal evidence

- PMID:11314040 cloned AATYK cDNAs from a **mouse cerebellar library**, expressed mouse AATYK in 293 cells, and studied mouse cerebellar granule neurons. It reports tyrosine kinase activity/autophosphorylation and a kinase-dependent increase in neuronal apoptosis. This is the experimental lineage behind the mouse/PANTHER-supported human IBA tyrosine-kinase and neuron-apoptosis annotations, not human IDA.
- PMID:18691334 studies the transmembrane-domain-free AATYK1A in **mouse cortical neurons** (species confirmed by PubMed indexing) and COS-7 cells. It shows palmitoylation of three N-terminal cysteines, transferrin-receptor-positive recycling-endosome localization, Src association, and Src/Fyn phosphorylation of AATYK1A Tyr25/Tyr46. The latter is evidence that other kinases phosphorylate LMTK1 on tyrosines, not proof that LMTK1 itself is a tyrosine kinase.
- PMID:20422042 used HEK293 and COS-7 cells, PC12D cells, **rat cortical neurons**, and **mouse brain**. It directly shows that CDK5/p35 phosphorylates AATYK1A at Ser34 and that this modification suppresses Src-family-dependent tyrosine phosphorylation. The in-vivo neuronal evidence remains rodent, and transfer of the exact regulatory mechanism to a current human isoform requires sequence- and isoform-resolved testing.
- PMID:20553326 used CHO-K1 cells. It places AATYK1A at Rab11A-positive pericentrosomal recycling endosomes and connects CDK5-dependent Ser34 phosphorylation to recycling-endosome-compartment formation. Crucially, it states: "Although no direct interaction between AATYK1A and Rab11A could be detected," so Rab11A should be modeled as a downstream pathway component, not a direct binding partner.
- PMID:22573681 used **mouse brain cortical neurons**, knockdown, and an Lmtk1-targeted allele. LMTK1 loss accelerated anterograde Rab11A-positive-vesicle transport and increased axon elongation; wild-type or phosphomimetic S34D rescue reversed the phenotype. Its conclusion is that "LMTK1 can negatively control axonal outgrowth by regulating Rab11A activity in a Cdk5-dependent manner." This is strong mouse orthology evidence for neuronal function and recycling-endosome localization, not human IDA.
- PMID:24672056 extended the mouse model to dendrites. E17/E18 ICR and Lmtk1-knockout cortical neurons plus in-vivo brain analysis showed that loss increased Rab11A-positive-endosome dynamics, dendrite growth, and branching. The paper concludes that LMTK1 negatively regulates dendritic formation through Rab11A-positive endosomal trafficking in a CDK5-dependent manner.
- PMID:31628178 used primary **mouse** cortical/hippocampal neurons and mouse brain of both sexes. LMTK1 depletion or kinase-negative LMTK1 increased spine formation/maturation/density, and TBC1D9B was placed between LMTK1 and Rab11A. This supports a mouse LMTK1-TBC1D9B-Rab11A neuronal pathway. It does not demonstrate that human LMTK1 phosphorylates TBC1D9B, and it should not be turned into a human stable-complex assertion.

## Catalytic and core-function synthesis

- Direct human evidence now favors a protein serine kinase core with TP53 Ser366 as the only clearly defined direct human substrate in the reviewed literature. The older mouse tyrosine-activity/autophosphorylation report should be retained with species and assay caveats, not allowed to override PMID:35902728, and not confidently removed without the full older paper.
- A second, orthology-supported neuronal context places transmembrane-domain-free rodent LMTK1A on Rab11-positive recycling endosomes downstream of CDK5/p35 and upstream of TBC1D9B/Rab11A, where it restrains axon elongation, dendrite arborization, and dendritic-spine formation. No equivalent endogenous human-neuron perturbation is in the cached set.
- A PP1-binding/scaffold role is supported by repeated human physical-interaction screens and a catalytic-independent AATYK1/Xenopus mechanism whose construct species is unresolved in the cached abstract. It is informative but currently secondary to the catalytic core, and no stable `in_complex` assignment is justified.
- Existing GO terms are adequate: GO:0106310 protein serine kinase activity, GO:0018105 peptidyl-serine phosphorylation, GO:0008285 negative regulation of cell population proliferation, GO:0008157 protein phosphatase 1 binding, GO:0055037 recycling endosome, GO:0030517 negative regulation of axon extension, GO:0061002 negative regulation of dendritic spine morphogenesis, and GO:2001135 regulation of endocytic recycling cover the principal claims. No new ontology term is presently necessary.

## Knowledge gaps and discriminating experiments

- Determine which current human Q6ZMQ8 isoform was used in PMID:35902728 and test purified, sequence-defined Q6ZMQ8-1 and Q6ZMQ8-3 against TP53 Ser366 and unbiased substrate panels. Q6ZMQ8-2 lacks the kinase domain and should be tested for scaffold/binding functions rather than presumed catalytic activity.
- Establish endogenous human-neuron localization and function with isoform-specific reagents. Test whether human LMTK1 occupies Rab11-positive recycling endosomes and whether loss alters Rab11A activity, endosome movement, axon/dendrite growth, and spine formation.
- Test whether human LMTK1 phosphorylates TBC1D9B or another neuronal substrate; the mouse pathway establishes genetic order but not the direct kinase substrate connecting LMTK1 to Rab11A.
- Validate PPP1CA and PPP1CC binding with endogenous reciprocal experiments, map the PP1 docking motif in human LMTK1, and test whether it creates a catalytic-independent PP1-STK39 scaffold. This would distinguish a conserved regulatory function from recurrent screen detectability.
- Resolve whether LMTK1 has reproducible intrinsic tyrosine kinase activity using purified human protein, site-defined substrates, phospho-amino-acid analysis, and kinase-dead controls. Separately measure Src/Fyn-mediated tyrosine phosphorylation of LMTK1 so that substrate phosphorylation is not mistaken for LMTK1 catalytic specificity.
- Revisit PMID:10837911 full methods to identify the AATYK cDNA species and isoform before treating its cytoplasmic localization and neuronal-differentiation result as direct human-protein evidence.

## YAML-ready reference additions and updates

The following entries use exact cache-backed quotes. The nine abstract-only caches are explicitly flagged. Statements preserve species/model boundaries and can be copied into the review after merging with the existing seeded entries.

```yaml
- id: PMID:35902728
  title: >-
    Epigenetically silenced apoptosis-associated tyrosine kinase (AATK) facilitates a decreased
    expression of Cyclin D1 and WEE1, phosphorylates TP53 and reduces cell proliferation in a
    kinase-dependent manner.
  findings:
  - statement: >-
      Human AATK/LMTK1 is a protein serine/threonine kinase that directly phosphorylates human
      TP53 at Ser366.
    supporting_text: >-
      Via large-scale kinomic profiling and kinase assays, we demonstrate that AATK acts a
      Ser/Thr kinase that phosphorylates TP53 at Ser366.
    reference_section_type: ABSTRACT
  - statement: >-
      Wild-type versus kinase-dead AATK experiments link catalytic activity to lower CCND1/WEE1
      expression and growth suppression in human cell models.
    supporting_text: >-
      The kinase activity of AATK in comparison to the kinase-dead mutant mediates a decreased
      expression of the key cell cycle regulators Cyclin D1 and WEE1. Moreover, growth suppression
      through AATK relies on its kinase activity.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: HIGH
    correctness: VERIFIED
    review_notes: >-
      Strongest direct human catalytic evidence. Human coding sequence and human cell systems were
      used, but the construct is not mapped unambiguously to a current Q6ZMQ8 isoform number.

- id: PMID:24589855
  title: >-
    Apoptosis-associated tyrosine kinase 1 inhibits growth and migration and promotes apoptosis in
    melanoma.
  full_text_unavailable: true
  findings:
  - statement: >-
      Human AATK perturbation in melanoma cells supports anti-proliferative, anti-migratory, and
      pro-apoptotic roles.
    supporting_text: >-
      Overexpression of AATK inhibited cell proliferation, colony formation, and promoted apoptosis
      in melanoma cell lines derived from primary and metastatic melanomas.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: HIGH
    correctness: VERIFIED
    review_notes: >-
      Direct human-cell evidence and independent corroboration of growth suppression. Historical
      AATKA/AATKB names must not be mapped naively to current UniProt isoform numbers.

- id: PMID:10837911
  title: >-
    A novel kinase, AATYK induces and promotes neuronal differentiation in a human neuroblastoma
    (SH-SY5Y) cell line.
  full_text_unavailable: true
  findings:
  - statement: >-
      AATYK expression in human SH-SY5Y cells produced cytoplasmic kinase signal and promoted
      neuronal differentiation, but the abstract does not identify the AATYK cDNA species.
    supporting_text: >-
      Our results demonstrate for the first time that AATYK is an active, non-receptor, cytosolic
      kinase which induces neuronal differentiation and also promotes differentiation induced by
      other agents in the SH-SY5Y cells.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: MEDIUM
    correctness: VERIFIED
    review_notes: >-
      Direct human cellular environment; construct species/isoform unresolved in the abstract, so
      do not describe it as unambiguous human-Q6ZMQ8 IDA.

- id: PMID:14521924
  title: Apoptosis-associated tyrosine kinase is a Cdk5 activator p35 binding protein.
  full_text_unavailable: true
  findings:
  - statement: >-
      A human brain-derived short KIAA0641/AATYK splice fragment binds CDK5R1/p35; human constructs
      were also tested in HEK293 cells and were phosphorylated by CDK5/p35.
    supporting_text: >-
      Both hAATYKs and KIAA0641 bound to and were phosphorylated by Cdk5/p35.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: HIGH
    correctness: VERIFIED
    review_notes: >-
      Human-sequence evidence with mixed rat-brain-extract and HEK293 assays. The native short
      hAATYKs-p35BP fragment lacks the kinase domain; the kinase-containing hAATYKs construct was
      engineered.

- id: PMID:22321011
  title: Protein phosphatase 1α interacting proteins in the human brain.
  full_text_unavailable: true
  findings:
  - statement: >-
      A high-throughput human-brain yeast-two-hybrid survey identified PP1α interactors; GOA records
      the AATK-PPP1CA pair from this screen.
    supporting_text: >-
      Hence, an in-depth survey was taken to identify specific PP1α PIPs in human brain by a
      high-throughput Yeast Two-Hybrid approach. Sixty-six proteins were recognized to bind PP1α,
      39 being novel PIPs.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: MEDIUM
    correctness: VERIFIED
    review_notes: >-
      Supports human PP1α binding, but the abstract does not name AATK and does not establish a
      stable complex or downstream mechanism.

- id: PMID:25852190
  title: >-
    Integrative analysis of kinase networks in TRAIL-induced apoptosis provides a source of
    potential targets for combination therapy.
  full_text_unavailable: true
  findings:
  - statement: >-
      A human DLD-1 kinase-network resource combined perturbation screens with mass-spectrometry
      interaction mapping and phosphoproteomics; GOA records AATK interactions with PPP1CA/PPP1CC.
    supporting_text: >-
      We assembled protein interaction maps using mass spectrometry-based protein interaction
      analysis and quantitative phosphoproteomics.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: LOW
    correctness: VERIFIED
    review_notes: >-
      Pair-level provenance is in the data/GOA rather than the abstract; this is not direct evidence
      for an LMTK1 catalytic or TRAIL-pathway mechanism.

- id: PMID:28065597
  title: A Global Analysis of the Receptor Tyrosine Kinase-Protein Phosphatase Interactome.
  findings:
  - statement: >-
      Human MYTH/MaMTH screens support AATK interactions with PPP1CA/PPP1CC, but interaction does
      not imply an enzyme-substrate relationship.
    supporting_text: >-
      However, it should be noted that these interactions are not equivalent to enzyme-substrate
      interactions, and therefore do not necessarily suggest that the involved phosphatase directly
      dephosphorylates a given RTK or, conversely, that the RTK can phosphorylate the phosphatase.
    reference_section_type: DISCUSSION
  reference_review:
    relevance: MEDIUM
    correctness: VERIFIED
    review_notes: >-
      Independent human phosphatase-interaction evidence; no stable-complex or substrate inference.

- id: PMID:32296183
  title: A reference map of the human binary protein interactome.
  findings:
  - statement: >-
      HuRI provides systematically retested human binary interactions; GOA records AATK-TEPSIN.
    supporting_text: >-
      To map the reference interactome, we performed nine screens of Space III, followed by pairwise
      verification by quadruplicate retesting and sequence confirmation.
    reference_section_type: RESULTS
  reference_review:
    relevance: LOW
    correctness: VERIFIED
    review_notes: >-
      Supports a binary screen contact only; no evidence for TEPSIN regulation, substrate status, or
      a stable complex.

- id: PMID:35384245
  title: Physical and functional interactome atlas of human receptor tyrosine kinases.
  findings:
  - statement: >-
      A human kinase-interactome atlas used complementary stable-interaction, proximity, and
      substrate assays; GOA records the AATK-PPP1CC pair.
    supporting_text: >-
      We use affinity purification coupled to mass spectrometry (AP-MS) to characterize stable
      binding partners and RTK-protein complexes, proximity-dependent biotin identification (BioID)
      to identify transient and proximal interactions, and an in vitro kinase assay to identify RTK
      substrates.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: MEDIUM
    correctness: VERIFIED
    review_notes: >-
      The paper-level text does not identify which assay produced this specific pair; avoid stable-
      complex or enzyme-substrate claims.

- id: PMID:17267545
  title: >-
    Apoptosis-associated tyrosine kinase scaffolding of protein phosphatase 1 and SPAK reveals a
    novel pathway for Na-K-2C1 cotransporter regulation.
  full_text_unavailable: true
  findings:
  - statement: >-
      AATYK1 expressed in Xenopus oocytes uses PP1- and SPAK-binding motifs for a catalytic-
      independent scaffold effect on NKCC1.
    supporting_text: >-
      Taken together, our data are consistent with AATYK1 indirectly inhibiting the SPAK/WNK4
      activation of the cotransporter by scaffolding an inhibitory phosphatase in proximity to a
      stimulatory kinase.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: MEDIUM
    correctness: VERIFIED
    review_notes: >-
      Mechanistic precedent for repeated human PP1 interactions, but the construct species is not
      stated in the cached abstract and the functional assay was in Xenopus oocytes; not human
      pathway IDA.

- id: PMID:11314040
  title: Characterization of the apoptosis-associated tyrosine kinase (AATYK) expressed in the CNS.
  full_text_unavailable: true
  findings:
  - statement: >-
      Mouse AATYK expressed in 293 cells showed reported tyrosine kinase/autophosphorylation, and
      wild-type versus kinase-deficient mouse AATYK altered apoptosis of mouse cerebellar neurons.
    supporting_text: >-
      We isolated three related cDNA clones from a mouse cerebellar library; the type I cDNA was
      identical to the gene encoding the apoptosis-associated tyrosine kinase (AATYK), whose
      expression in myeloid precursor cells is increased during growth arrest or apoptosis.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: MEDIUM
    correctness: VERIFIED
    review_notes: >-
      Direct mouse evidence underlying human IBA propagation; not human IDA. Full methods are not
      locally available, so retain rather than overrule the legacy tyrosine-activity claim.

- id: PMID:18691334
  title: Palmitoylation-dependent endosomal localization of AATYK1A and its interaction with Src.
  full_text_unavailable: true
  findings:
  - statement: >-
      Transmembrane-domain-free AATYK1A was palmitoylated and localized to recycling endosomes in
      mouse cortical neurons/COS-7 cells; Src/Fyn phosphorylated AATYK1A Tyr25/Tyr46.
    supporting_text: >-
      AATYK1A, an isoform without a transmembrane domain, is highly expressed in neurons. We
      identified palmitoylation of AATYK1A at three N-terminal cysteine residues in cortical
      cultured neurons and COS-7 cells and found that palmitoylation determined localization of
      AATYK1A to the transferrin receptor-positive recycling endosomes.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: HIGH
    correctness: VERIFIED
    review_notes: >-
      Isoform-specific rodent/heterologous localization evidence; do not transfer topology or
      compartment indiscriminately to all human isoforms.

- id: PMID:20422042
  title: Phosphorylation of AATYK1 by Cdk5 suppresses its tyrosine phosphorylation.
  findings:
  - statement: >-
      CDK5/p35 binds and phosphorylates rodent AATYK1A at Ser34 in mixed cultured-cell, rat-neuron,
      and mouse-brain systems, suppressing Src-family-dependent tyrosine phosphorylation.
    supporting_text: >-
      AATYK1A was phosphorylated at Ser34 by Cdk5/p35 in vitro, in cultured neurons and in mouse
      brain.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: HIGH
    correctness: VERIFIED
    review_notes: >-
      Strong rodent neuronal regulatory evidence. LMTK1 is the CDK5/p35 substrate; p35/CDK5R1 is
      the direct binding subunit, not CDK5 itself.

- id: PMID:20553326
  title: AATYK1A phosphorylation by Cdk5 regulates the recycling endosome pathway.
  full_text_unavailable: true
  findings:
  - statement: >-
      In CHO-K1 cells, AATYK1A and its CDK5-site phosphomutants regulate the Rab11A-positive
      pericentrosomal recycling-endosome compartment without detectable direct AATYK1A-Rab11A
      binding.
    supporting_text: >-
      Although no direct interaction between AATYK1A and Rab11A could be detected, the exchange of
      guanine nucleotides bound to Rab11A was significantly reduced in the presence of the
      phosphorylation-mimic AATYK1A-S34D.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: MEDIUM
    correctness: VERIFIED
    review_notes: >-
      Heterologous Chinese-hamster cell evidence; supports pathway order/localization, not a direct
      Rab11A interaction or human-neuron annotation.

- id: PMID:22573681
  title: >-
    LMTK1/AATYK1 is a novel regulator of axonal outgrowth that acts via Rab11 in a Cdk5-dependent
    manner.
  findings:
  - statement: >-
      Mouse cortical-neuron knockdown/knockout and rescue experiments show that LMTK1 restrains
      axon elongation by regulating Rab11A-positive endosome dynamics downstream of CDK5.
    supporting_text: >-
      Thus, LMTK1 can negatively control axonal outgrowth by regulating Rab11A activity in a
      Cdk5-dependent manner, and Cdk5-LMTK1-Rab11 is a novel signaling pathway involved in axonal
      outgrowth.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: HIGH
    correctness: VERIFIED
    review_notes: Strong direct mouse ortholog evidence; any human annotation is orthology-supported, not IDA.

- id: PMID:24672056
  title: LMTK1 regulates dendritic formation by regulating movement of Rab11A-positive endosomes.
  findings:
  - statement: >-
      Mouse cortical-neuron and in-vivo knockout experiments show that LMTK1 restrains dendrite
      growth and branching by modulating Rab11A-positive endosome movement downstream of CDK5.
    supporting_text: >-
      Thus LMTK1 negatively controls dendritic formation by regulating Rab11A-positive endosomal
      trafficking in a Cdk5-dependent manner, indicating the Cdk5-LMTK1-Rab11A pathway as a
      regulatory mechanism of dendrite development as well as axon outgrowth.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: HIGH
    correctness: VERIFIED
    review_notes: Strong direct mouse ortholog evidence; not human IDA.

- id: PMID:31628178
  title: >-
    The LMTK1-TBC1D9B-Rab11A Cascade Regulates Dendritic Spine Formation via Endosome Trafficking.
  findings:
  - statement: >-
      Mouse neuron and brain perturbations place TBC1D9B between LMTK1 and Rab11A in a pathway that
      restrains dendritic-spine formation, maturation, and density.
    supporting_text: >-
      Depletion of LMTK1 increases spine formation, maturation, and density in primary cultured
      neurons and in mouse brain of either sex.
    reference_section_type: ABSTRACT
  reference_review:
    relevance: HIGH
    correctness: VERIFIED
    review_notes: >-
      Direct mouse ortholog evidence. The study does not identify TBC1D9B as a direct human LMTK1
      phosphorylation substrate or establish a stable human complex.
```

### Explicit PMID integration list

Beyond the five seeded interaction PMIDs, the recommended reference additions are:

- Direct human/high priority: PMID:35902728, PMID:24589855.
- Human-sequence or human-cell context with important caveats: PMID:14521924, PMID:10837911.
- PP1 scaffold mechanism in Xenopus with unresolved AATYK1 construct species: PMID:17267545.
- Rodent/heterologous catalytic-localization hierarchy: PMID:11314040, PMID:18691334, PMID:20422042, PMID:20553326.
- Mouse Rab11/neurite/spine pathway: PMID:22573681, PMID:24672056, PMID:31628178.

All twelve are now present in the local publication cache. Abstract-only flags are required for PMID:10837911, PMID:11314040, PMID:14521924, PMID:17267545, PMID:18691334, PMID:20553326, and PMID:24589855. The other five have cached full text.
