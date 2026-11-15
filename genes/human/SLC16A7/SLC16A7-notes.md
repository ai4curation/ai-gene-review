# SLC16A7 (MCT2) curation notes

UniProt: O60669 (MOT2_HUMAN). HGNC:10928. Gene **SLC16A7**, protein **Monocarboxylate transporter 2 (MCT2)**. 478 aa, 12 TM helices, major facilitator superfamily / monocarboxylate porter family (TC 2.A.1.13). Chromosome 12q13.

## Core function

MCT2 is a **proton-coupled (H+-linked), high-affinity monocarboxylate (L-lactate / pyruvate / ketone body) transporter** of the plasma membrane, i.e. an electroneutral 1:1 H+:monocarboxylate symporter.

- UniProt curated FUNCTION: "Proton-coupled monocarboxylate symporter." and catalyzes transport of "monocarboxylates such as L-lactate, pyruvate and ketone bodies, acetoacetate, beta-hydroxybutyrate and acetate" [file:human/SLC16A7/SLC16A7-uniprot.txt "Proton-coupled monocarboxylate symporter"].
- **Highest pyruvate affinity of the MCTs.** The cloning/characterization paper established MCT2 as an H+/monocarboxylate transporter whose "unique biochemical feature ... is its high affinity for the transport of pyruvate (apparent Km of 25 microM), implying that it is a primary pyruvate transporter in man" [PMID:9786900 "the unique biochemical feature of human MCT2 is its high affinity for the transport of pyruvate (apparent Km of 25 microM)"]. The same paper states the kinetic properties "fulfill the criteria to establish it as a H+/monocarboxylate transporter" [PMID:9786900 "fulfill\nthe criteria to establish it as a H+/monocarboxylate transporter"].
- **Proton coupling is direct and experimentally localized.** The cryo-EM/functional study directly demonstrated H+-coupled transport: pyruvate influx is reciprocal to intracellular acidification, and the conserved Asp293 is required for proton coupling (D293N reduces proton-dependent symport but not substrate counterflow) [PMID:32415067 "These data confirm an H+-coupled pyruvate transport of MCT2"] [PMID:32415067 "Asp293 is strictly conserved in all identified proton-linked monocarboxylate transporters"].

## Molecular function GO terms (verified via QuickGO)

- **GO:0015650 lactate:proton symporter activity** — "reaction: lactate (out) + H+ (out) = lactate (in) + H+ (in)." is_a GO:0015129 (lactate transmembrane transporter activity), is_a GO:0015355 (secondary active monocarboxylate transmembrane transporter activity), and is a proton symporter (is_a GO:0015293 symporter). This is the most specific *supported* lactate term capturing the proton coupling. (QuickGO ancestors confirm the lineage.)
- **GO:0005477 pyruvate secondary active transmembrane transporter activity** — is_a GO:0050833 (pyruvate transmembrane transporter activity) and is_a GO:0015355. Most specific pyruvate term capturing secondary-active (proton-coupled) pyruvate transport. Already in GOA as a TAS row.
- GO:0050833 pyruvate transmembrane transporter activity (IDA) and GO:0015129 lactate transmembrane transporter activity (IDA/IBA) — substrate-specific, core, retained.
- GO:0008028 monocarboxylic acid transmembrane transporter activity (InterPro IPR004743) — family/substrate-class level; as precise as the InterPro signature allows.
- GO:0015355 secondary active monocarboxylate transmembrane transporter activity — accurately captures secondary-active (proton-coupled) monocarboxylate transport.
- **No "pyruvate:proton symporter activity" GO term exists** (QuickGO search returned none); GO:0005477 is the best available for the proton-coupled/secondary-active pyruvate activity.

## Homodimer and cooperative transport

MCT2 is a functional homodimer; dimerization is required for cooperative transport (positive cooperativity, Hill coefficient ~1.6) [PMID:32415067 "MCT2 exists as a homodimer"] [PMID:32415067 "dimerization is\nfunctionally required and both subunits work cooperatively in transporting\nsubstrate"]. This supports **GO:0042802 identical protein binding** (IDA), which is informative (self-association) and is retained; it is not reduced to bare protein binding.

## Ancillary subunit EMBIGIN (chaperone / complex membership)

MCT2 is reported to require the single-pass ancillary glycoprotein **EMBIGIN (EMB, gp70)** for plasma-membrane trafficking in most tissues, analogous to the MCT1/MCT3/MCT4–BSG(CD147) partnership. UniProt curated SUBUNIT/LOCATION:
- [file:human/SLC16A7/SLC16A7-uniprot.txt "Interacts with EMB; interaction mediates SLC16A7 targeting"] (to the plasma membrane; By similarity to rodent MCT2).
- [file:human/SLC16A7/SLC16A7-uniprot.txt "Requires the ancillary protein,"] EMB for plasma membrane localization (By similarity).
- Also "Interacts with isoform 2 of BSG (By similarity)" and "Colocalizes with BSG in spermatozoa."

Caveat (debated necessity): the human cryo-EM study found that mEGFP-MCT2 localized to the plasma membrane of HEK293 cells *without* embigin co-expression, and notes embigin "was reported necessary ... or unnecessary" for MCT2 trafficking [PMID:32415067 "embigin was reported necessary9,10 or unnecessary11 for the intracellular trafficking of the MCT2 to the plasma membrane"]. The MCT2–EMBIGIN partnership is modeled here as **complex membership** (GO:1902495 transmembrane transporter complex, part_of; NEW row, ISS) rather than as a bare protein-binding annotation; this mirrors the batch-10 B0AT1/ACE2 treatment. EMBIGIN (Q6PCB8) is NOT among the GOA IntAct protein-binding partners, so there is no EMBIGIN row to remove.

## Protein-binding (GO:0005515) IntAct rows — PDZ scaffolds

39 bare GO:0005515 protein-binding IPI rows (PMID:30126976, PMID:32296183, PMID:36115835). The partners are overwhelmingly **PDZ-domain scaffolds**: DLG1/DLG3/DLG4 (PSD-95), GRIP1/GRIP2, MPDZ, MAGI1/MAGI2, PATJ, SCRIB, SNTA1/SNTB1, PDZK1, NHERF4, WHRN, TJP1, FRMPD2, GRID2IP, LNX1/LNX2, APBA1/APBA2, etc. These reflect MCT2's **C-terminal class-I PDZ-binding motif** (C-terminus "...SERETNI") engaging postsynaptic/epithelial PDZ scaffolds [file:human/SLC16A7/SLC16A7-uniprot.txt "Interacts with GRID2IP"]. The fragmentomics/phospho-PDZ/binary-interactome assays yield only generic "protein binding," which is uninformative. Per the protein-binding policy these bare GO:0005515 rows are REMOVE (the sanctioned exception); removal does not imply the interactions are false. The functionally meaningful PDZ-scaffolding is recorded in notes/reason, not as GO:0005515.

## Localization

- **Plasma membrane (GO:0005886)** — core; direct experimental evidence: cryo-EM/cell imaging [PMID:32415067], leukocyte IHC "Plasmalemmal staining occurred with all MCTs in all leukocyte fractions" [PMID:15505343 "Plasmalemmal staining occurred with all MCTs in all leukocyte fractions"], HPA immunofluorescence (GO_REF:0000052), Reactome TAS, and IBA.
- **Cytoplasm (GO:0005737)** — a real intracellular pool (UniProt: detected in cytoplasm of Sertoli cells, By similarity; leukocyte cytoplasmic staining [PMID:15505343 "all the MCTs also stained leukocyte cytoplasm, often with distinct granularity"]). Non-core.
- **Basolateral plasma membrane (GO:0016323)** — ISS/IBA from the rat MCT1 ortholog (P53988) and family; a context-specific epithelial PM sub-compartment. Non-core.
- **Neuronal/synaptic (GO:0098839 postsynaptic density membrane, GO:0098978 glutamatergic synapse, GO:0098685/0098686/0098688 specific synapse types)** — electronic transfer from rat MCT2 (Q63344). MCT2 is the well-known **neuronal (post-synaptic) monocarboxylate transporter** of the astrocyte–neuron lactate shuttle; these are genuine family localizations but electronic for human and peripheral to the core transport MF. Non-core.
- **GO:0016020 membrane** (InterPro) — uninformatively general; refine to plasma membrane.

## Biological process

- Core: GO:0035873 lactate transmembrane transport (IMP), GO:0035879 plasma membrane lactate transport (IBA/IEA), GO:1901475 pyruvate transmembrane transport (IDA). MCT2 *performs* the monocarboxylate transport step.
- GO:0015718 monocarboxylic acid transport (InterPro) — family/substrate-class process, as precise as the signature allows.
- GO:0055085 transmembrane transport and GO:0022857 transmembrane transporter activity — root transport terms, uninformative once lactate/pyruvate transport is asserted → TOO_GENERAL.
- **GO:0150104 transport across blood-brain barrier (NAS, PMID:26590417)** — over-annotation. The citation is a general BBB review that does not establish an MCT2-specific BBB-endothelial transport role. The BBB (luminal/abluminal endothelial) monocarboxylate transporter is MCT1; MCT2 is the neuronal/post-synaptic transporter. MCT2 does not perform transport across the BBB endothelium → MARK_AS_OVER_ANNOTATED (participation test fails; necessity/context is not participation).

## Tissue expression

High in testis; moderate-to-low in spleen, heart, kidney, pancreas, skeletal muscle, brain, leukocytes; restricted in normal tissues but widely expressed in cancer cells [file:human/SLC16A7/SLC16A7-uniprot.txt "High expression in"] testis [PMID:9786900 "Human MCT2 mRNA expression was restricted in normal human tissues but widely\nexpressed in cancer cell lines"].

## Action summary

- ACCEPT (21): core transporter MF (lactate/pyruvate transporter activities), plasma membrane CC rows, homodimer (GO:0042802), lactate/pyruvate transport BP, monocarboxylate family MF/BP.
- MODIFY (3): GO:0015293 symporter activity ×2 → GO:0015650 lactate:proton symporter activity (generic symport → specific proton-coupled monocarboxylate symport, supported by the H+-coupled transport evidence); GO:0016020 membrane → GO:0005886 plasma membrane.
- KEEP_AS_NON_CORE (10): cytoplasm ×2, basolateral PM ×3, neuronal/synaptic ×5.
- TOO_GENERAL (2): GO:0022857 transmembrane transporter activity, GO:0055085 transmembrane transport.
- MARK_AS_OVER_ANNOTATED (1): GO:0150104 transport across blood-brain barrier.
- REMOVE (39): bare GO:0005515 protein binding (PDZ-scaffold IntAct rows; protein-binding policy).
- NEW (1): GO:1902495 transmembrane transporter complex (part_of) — MCT2–EMBIGIN ancillary complex.
