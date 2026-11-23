# CASP8 notes

## 2026-09-30

- Seeded and completed the human CASP8 review from GOA, UniProt, cached PubMed
  records, Reactome, GO-CAM models, and PAINT transfer context.
- Kept the CASP8 core centered on three direct mechanisms: FADD/death-effector
  domain recruitment to death-inducing signaling complexes, Asp-directed
  cysteine endopeptidase activity that matures downstream procaspases and
  gasdermin substrates, and RIPK1 cleavage that restrains RIPK1/RIPK3-dependent
  necroptosis.
- Tightened top-level `GO:0006915 apoptotic process` assertions toward
  death-domain receptor extrinsic apoptotic signaling, while leaving the
  abstract-only PMID:22891283 Fas vesicle row `UNDECIDED`.
- Moved CASP8 away from effector-only `GO:0097194 execution phase of apoptosis`
  wording. CASP8 is an initiator that activates CASP3/CASP7 and other
  substrates by proteolytic maturation; CASP3 and CASP7 carry the direct
  executioner role.
- Removed all 94 generic `GO:0005515 protein binding` rows. The FADD/CFLAR/FAS
  edges were either already represented by specific death-effector-domain or
  DISC annotations, and the BioPlex, binary-interactome, viral-inhibitor, and
  other screen edges did not identify a CASP8-specific molecular activity.
- Removed the impossible Ensembl electronic `GO:0030690 Noc1p-Noc2p complex`
  mapping to human CASP8, together with stimulus-response and assay-readout rows
  that did not establish direct CASP8 work.
- Kept pyroptosis, dectin-1 inflammasome, TLR3/TLR4 ripoptosome, N4BP1 innate
  immune, and host-pathogen perturbation rows as non-core where they captured
  real CASP8-containing complexes or substrate-cleavage branches.
- Deferred rows whose visible cached evidence was abstract-only, review-derived,
  or centered on a different caspase or readout, including the
  HSP70/GATA1 localization rows, the COP/CARD-only protein paper, the
  CAAP/C9orf82 paper, the p23 paper, and specific immune differentiation terms
  sourced only to PMID:18309324.

## 2026-10-02 PR follow-up

- Broad orthology and electronic angiogenesis, heart-development, animal-organ
  development, chordate-development, and neuron-apoptosis rows were kept non-core
  or marked over-annotated because they are transferred organismal contexts
  rather than direct human CASP8 biochemical activities.
- Regulation-of-cytokine-production, lipopolysaccharide-response,
  innate-immune, and macrophage-differentiation rows were treated as
  inflammatory or differentiation contexts for CASP8 scaffolds and substrate
  cleavage, not as core death-receptor, DISC, or protease functions.
- Generic immune-process, positive-signal-transduction, and cell-differentiation
  electronic rows were marked over-annotated because they are diffuse high-level
  projections, not specific steps carried out by CASP8.
- Ensembl and rat-transfer Noc1p-Noc2p complex, cell body,
  protein-containing-complex-binding, cobalt, estradiol, ethanol, and anesthetic
  rows were removed as unsupported electronic projections rather than human
  CASP8 activities or locations.

## 2026-10-04 evidence and annotation reassessment

This entry supersedes the interpretation of the earlier notes where the two disagree. The older journal remains intact as provenance. The review retains all 264 source assertions, including every original reference, evidence code, qualifier and partner, and all nine UniProt product records. No new GO assertion is proposed. The important changes are scientific: supported generic interactions are retained, direct protease experiments are distinguished from downstream phenotypes, and unresolved evidence is no longer described as proof of absence.

### Molecular work and compartment

CASP8 has two closely coupled molecular functions: aspartate-directed cysteine endopeptidase activity, and death-effector-domain recognition that organizes activation complexes. The catalytic synthesis combines substrate-dependent outcomes of the same enzyme: effector-caspase maturation, RIPK1 cleavage that restrains necroptosis, and direct GSDMC cleavage in the tested cancer-cell contexts. A separate DED unit captures physical recruitment and assembly. The previous three catalytic core entries have been consolidated without dropping their supported processes. Cytosol is accepted consistently as a central compartment; membrane, mitochondrial, cytoskeletal and nuclear pools are assessed in their particular contexts.

The canonical PMID:16916640 cache is abstract-only, but the author-hosted Stanford PDF supplied primary Results, the Figure 1 caption, kinetic comparisons and Methods. Recombinant DED-deleted CASP8 cleaves and activates human procaspase-7; activation-site mutants and subtraction of CASP8-alone reporter turnover constrain the result. The optimized buffers and engineered constructs are not measurements of endogenous DISC kinetics. The paper's CASP7 title therefore cannot justify discarding its CASP8 assays. The official GO:0008656 comment expressly includes active caspases that cleave inactive effector caspases. Proteolysis does not exclude that activator activity.

The GO-CAM index separately places CASP8 in cytosolic protein maturation and death-receptor pathways, consistent with these existing assertions. This index check is not a new model audit or a reason to invent additional annotations. In the GSDME sources, CASP8 is upstream of CASP3; CASP3 supplies the specific GSDME cleavage. In the GSDMC source, recombinant cleavage, cellular perturbation and a cleavage-resistant substrate support direct CASP8 action. Gasdermin supplies the pore, not CASP8 (PMID:32929201, PMID:33852854, PMID:35594856). The GSDMC correction concerns omitted funding acknowledgments, not altered experiments.

The former categorical exclusion of CASP8 from apoptotic execution was too strong. GO:0097194 permits other effectors in controlled cellular breakdown, and PMID:10891503 directly identifies plectin as a CASP8 substrate. Human-cell localization experiments distinguish active subunits from the prodomain, while recombinant plectin cleavage fragments include a rat construct; those observations are not interchangeable. CASP8 can perform a structural-substrate cut as well as activate downstream proteases. The ripoptosome study primarily establishes upstream complex/death regulation; its existing execution assertion is retained with curator deference and independent substrate support, not transformed into an exclusive terminal-executor claim (PMID:21737330).

### Nonapoptotic and human disease evidence

The normal primary cache PMID:12353035 supplies direct human immunodeficiency context: "defects in their activation of T lymphocytes, B lymphocytes
and natural killer cells". It supports the existing T-, B- and NK-activation assertions that the old review left unresolved solely because the cited review was abstract-only. This clinical result does not identify every direct molecular step, nor equate CASP8 deficiency with classic ALPS. Only the complete abstract was available; no unseen patient-protein or rescue experiment is claimed.

Peripheral-blood monocyte differentiation involves CASP8 activation, downstream caspase processing and RIP1 cleavage that limits sustained NF-kappaB signaling. That is protease work, not merely an accompanying differentiation phenotype (PMID:17047155). Positive NF-kappaB signaling from prodomain-only CASP8 constructs is a different context and can coexist with this negative effect (PMID:12884866). The human-cDNA screen uses experimental expression evidence; IEP must not be called an electronic annotation (PMID:12761501). Its original CASP8 table remains uninspected, with independent target evidence supporting the retained direction.

The proteolytic-reporter study transfects CASP8 into human 293ET cells and measures a dose-dependent DEVDG reporter with a no-cleavage-motif control. Downstream caspases can contribute to the signal, but that does not invalidate the positive-regulation-of-proteolysis assertion (PMID:18387192). Human-cell migration experiments separately use catalytic-site and Y380 variants to distinguish protease activity from localization and migration signaling (PMID:18216014). No new migration molecular function or broad human developmental process is manufactured from these findings.

### Interaction evidence and its limits

The former removal of all 94 generic binding rows on informativeness grounds is withdrawn. Source-specific reading supports qualified complex association, direct recognition in selected assays, or explicit uncertainty. Five existing rows are refined where the target experiment supports a narrower function: RIPK1 and NIK kinase binding by CASP8 prodomain constructs, nuclear androgen receptor binding, SHP1 phosphatase binding, and FADD DED binding. None makes CASP8 a kinase, receptor, phosphatase or ubiquitin ligase. The exact long-FLIP, Fas, UNG and FMR1 suffixes and the mouse/viral partner identifiers remain literal.

Several papers contain positive controls that their titles or abstracts obscure. These include CASP8 in apoptotic U937 receptor complexes despite receptor-independent monocyte differentiation, positive Jurkat DISC controls despite defective DU145 signaling, and CASP8 recruitment in sensitive human cells despite inhibitory complexes in resistant cells (PMID:17047155, PMID:14612908, PMID:18846110). FASLG capture establishes a ligand-containing receptor complex, not direct contact between an extracellular ligand and cytosolic CASP8. BCAP31 coimmunoprecipitation is retained even though its original in-vitro direct-binding experiment was negative; an unidentified bridge was proposed (PMID:9334338).

Where a source's exact assay or table is inaccessible but separately read evidence establishes the same literal partner interaction, retention explicitly names the independent support and defers to the experimental curator. That does not authenticate the uninspected original dataset. UniProt repeats many exact edges, but can share IntAct provenance and is not an independent experimental replication. Novel network pairs without independently verified target evidence remain uncertain. The mutant-context breast-cancer FADD record and unresolved mouse/viral construct mappings also retain their specific uncertainties rather than being generalized from ordinary human FADD binding.

PMID:21713032 distinguishes a CASP8-negative migratory MISC from an agonist-induced apoptotic DISC positive control. Its 2019 and 2023 corrections alter cell/construct descriptions, labels and image presentation and disclose missing original H9 S1C data; the corrected Figure 5C retains the DISC control. No raw-image reanalysis is claimed. The PMID:21988832 correction changes an author name; the PMID:19060883 corrigendum changes an author name and affiliations. Neither announces an interaction-dataset correction. These notices are reflected in the reference assessments.

### Unresolved propagation and citation questions

The Noc1p-Noc2p term explicitly permits analogous complexes outside yeast, so its name does not make a human annotation impossible. An official mouse graph contains the donor experimental assertion, but the linked Nur77/apoptosis source does not resolve preribosomal-complex membership in the accessible evidence. The exact original donor experiment and historical source mapping remain unresolved. The old confident removal is replaced by uncertainty, without asserting a corrected citation or fabricating a sequence analysis.

Rat transfers for death-receptor binding, cobalt/estradiol/ethanol/anesthetic responses and cell-body localization need their individual assay provenance. General death-complex membership is not proof of direct receptor contact; generic cytoplasm is not proof of the more specific cell-body term. These access limits are not evidence that the annotations are false. The BAD-associated mechanical-stimulus citation likewise lacks a resolved target assay; its IEP evidence must not be dismissed as electronic. The specific placental differentiation assertion remains uncertain because species and developmental evidence could not be reconstructed from the accessible review. Broad developmental and neuronal assertions already supported by curated transfer are retained with explicit limits, not called false simply for breadth.

PAINT assertions represent ancestral-node judgments. Target inclusion among descendant evidence is legitimate, and donor-list size is not a proxy for quality. The ancestral nodes and alignments were not independently inspected; no target-specific residue loss or phylogenetic placement claim is made. This review proposes no additional processes, no new partner-derived functions, and no removal based only on title, organism name or absence of a keyword.

### Access and validation provenance

All referenced cached abstracts and all 42 Reactome summaries were read by the author or the two bounded source consultants; selected full Methods, Results and captions were inspected where they resolve the target mechanism. Coverage is recorded per reference. A `full_text_available` flag is not a guarantee of a complete extracted paper: PMID:10521396 contains only a short abstract-like body, and several interactome HTML caches omit most original experimental text. External indexed or author-hosted passages are distinguished from unchanged canonical caches. Unseen images, supplements and target tables are not claimed as inspected.

One isolated standard research attempt used the installed Falcon provider and its normal fallback. Both failed without generating a report. The review therefore rests on the manually read sources and consultations; no provider report was authored or substituted. The earlier notes are historical statements, not evidence for the revised decisions. Long repeated YAML quotations and self-notes support have been replaced by source references and a small set of exact short anchors. The revised DRAFT status retains unresolved biological and access questions; warning counts are reported separately by normal validation.

The final process classification treats the tau proteolysis and upstream gasdermin-maturation-cascade assertions consistently with the broad catalytic core. Their substrate and causal limits remain explicit; acceptance does not turn the CASP3-mediated GSDME cut into direct CASP8 cleavage.


## 2026-10-04 follow-up: evidence anchors and the Noc donor assertion

Short anchors below make the load-bearing assays traceable while retaining their experimental boundaries. Publication `supporting_text` is taken verbatim from the canonical caches. The procaspase-7 quotation instead uses the explicitly external `supporting_text_fulltext` field; its source is linked below. Ontology comment text is manually checked against the official record. None of these distinctions changes the immutable source files or establishes a new annotation.

- **Direct procaspase-7 cleavage/activation (PMID:16916640):** [PMID:16916640 "procaspase-7 activation site mutants were incubated with recombinant caspase-8"] — [author-hosted primary PDF](https://med.stanford.edu/content/dam/sm/bogyolab/documents/Denaultetal.pdf), page 524, Figure 1C caption; corresponding Results and Methods were inspected. The experiment uses recombinant DED-deleted CASP8 and human procaspase-7 activation-site mutants, with a CASP8-alone substrate-turnover control. Optimized high-salt conditions do not measure native DISC kinetics. This is an external passage, not text in the abstract-only canonical cache. The same short passage anchors the direct catalytic annotation and explains the source used for procaspase maturation/execution and the protease core; no self-notes citation replaces the paper.
- **RIPK1/NIK binding (PMID:12884866):** the cached abstract itself states the GST pull-down specificity and contains the short annotation anchors. The independently read [original paper in the official grant archive](https://mhlw-grants.niph.go.jp/system/files/2005/057081/200500616B/200500616B0007.pdf), Methods 4.2, identifies [PMID:12884866 "respective prodomains"] in the GST construct preparation. This is construct-limited CASP8 binding evidence; it neither assigns kinase activity to CASP8 nor resolves the two mouse-accession mappings. PDF figure images were not inspected.
- **Monocyte proteolysis and distinct apoptotic controls (PMID:17047155):** the cached abstract supplies the RIP1-cleavage anchor. In the separately accessed [official primary Figure 3 caption](https://pmc.ncbi.nlm.nih.gov/articles/PMC2492986/), [PMID:17047155 "As positive controls, U937 cells were treated"] introduces the TRAIL and agonistic Fas-antibody experiments. Those apoptotic controls must be distinguished from receptor-independent differentiation-associated complexes. The inspected primary text/caption supports that distinction; this is not a claim that the canonical abstract cache contains the complete paper or that native coassociation proves purified direct receptor contact.
- **Other annotation anchors:** cached abstract snippets now expose the AR interaction-disrupting substitutions (PMID:17170703), phospho-CASP8 association with SHP-1 (PMID:18086677), RIP cleavage (PMID:10521396), and plectin cleavage (PMID:10891503). SHP-1 performs dephosphorylation; CASP8 is the substrate. The plectin experiment supports direct structural-substrate proteolysis despite CASP8's initiator role. For PMID:10521396, the canonical extraction is abstract-like despite its full-text flag; no complete-paper read is claimed here. The existing historical notes and earlier assay limitations remain intact.

**Noc1p-Noc2p complex (GO:0030690).** The [official GO record at MGI](https://www.informatics.jax.org/vocab/gene_ontology/GO:0030690) defines a heterodimer associated with 90S/66S preribosomes and explicitly permits analogous complexes outside yeast. Its exact short comment is attached to the annotation with DATABASE_ENTRY provenance; it establishes the term's scope, not CASP8 membership. This resolves the reviewer's request to expose the actual ontology wording.

The [historical MGI annotation graph](https://www.informatics.jax.org/GOgraphs/OrthoDisease/GeneGraphs/CASP8.html) identifies mouse Casp8 O89110 and an IMP donor assertion linked to J:87073 / PMID:14657025. The canonical cache for that paper contains only its abstract. Separately inspected [official primary Results, Figure 6 and selected Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC291815/) describe NDG1-induced CASP8 p41/p43 processing, fluorogenic activity assays and inhibition in 293T cells; these are distinct from the paper's mouse thymocyte experiments. The inspected passages do not establish membership in a preribosomal heterodimer. The original curator mapping and uninspected supplementary material remain unresolved, so the existing assertion stays UNDECIDED rather than being accepted on the ontology comment or rejected through a taxon/name argument. This is a concrete donor-source audit question, not deference to the electronic pipeline. No absence of Noc membership in every species or historical mapping error has been established.

All 264 source assertions, their actions, nine products, two core functions and prior references are preserved. The added donor paper and ontology record document this bounded audit; they do not add a molecular function, cellular component or biological process.
