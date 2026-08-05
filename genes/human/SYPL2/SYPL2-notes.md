# SYPL2 review notes

## Review scope and evidence acquisition

- Review initiated 2026-07-18 for human SYPL2 (UniProt Q5VXT5; HGNC:27638), also known as mitsugumin 29 (MG29).
- `just fetch-gene human SYPL2` retrieved the reviewed UniProt record and four current GOA annotations.
- Falcon deep research was attempted with the required Perplexity Lite fallback. Falcon failed with HTTP 402 (provider payment required) and the fallback failed with HTTP 401 (quota exhausted). No provider-authored deep-research file was created. This manual note is therefore the provenance record for the literature synthesis.
- The GOA-cited PMID:22926577 and six additional primary studies were cached and inspected. Full text is locally available for PMID:10613905, PMID:26141232, and PMID:28706255; only abstracts are available for PMID:9512495, PMID:11988740, PMID:22290180, and PMID:22926577.
- Most mechanistic evidence is from mouse, rabbit, or other mammalian muscle systems. The human protein has a reviewed UniProt record and conserved synaptophysin/MARVEL architecture, but direct loss-of-function experiments in human skeletal muscle are lacking. Proposed human annotations based on the animal studies should therefore use an orthology/sequence-similarity inference rather than an experimental human evidence code.

## Protein identity and architecture

- Human SYPL2 is a 272-aa reviewed protein with a MARVEL domain (residues 30-238), four predicted transmembrane helices, two luminal/vesicular loops, cytoplasmic N- and C-termini, and two reported splice isoforms. UniProt assigns it to the synaptophysin/synaptobrevin family and predicts a membrane, multi-pass topology [file:human/SYPL2/SYPL2-uniprot.txt, "DOMAIN          30..238"; "Belongs to the synaptophysin/synaptobrevin family."]
- The founding MG29 study identified the protein as a transmembrane component of the skeletal-muscle triad and inferred communication between T-tubular and junctional sarcoplasmic-reticulum (SR) membranes [PMID:9512495, "Here we report the identification using monoclonal antibody and primary structure by cDNA cloning of mitsugumin29, a novel transmembrane protein from the triad junction in skeletal muscle."]

## Core localization and structural role

- In mouse skeletal muscle, MG29 is expressed at the junctional membrane complex between T-tubules and SR. Knockout causes swollen/irregular T-tubules, abnormal SR structures, and partial triad misformation [PMID:10613905, "Ultrastructural abnormalities of the membranes around the triad junction were detected in skeletal muscle from the mutant mice, i.e., swollen T tubules, irregular SR structures, and partial misformation of triad junctions."]
- The knockout study concludes that MG29 is required for refinement/maturation rather than initial formation of the specialized junctional membrane system. It is recovered in both SR and T-tubular biochemical fractions [PMID:10613905, "MG29 is recovered in both SR and T tubular fractions in biochemical membrane preparations"].
- These data support missing human annotations, by orthology, to junctional membrane complex (GO:0030314), T-tubule (GO:0030315), junctional sarcoplasmic reticulum membrane (GO:0014701), and T-tubule organization (GO:0033292).
- Mouse cardiac experiments independently show that induced Mg29 localizes to T-tubules and can preserve T-tubule organization in a heart-failure context, but endogenous cardiac expression is context-dependent and is not the main physiological setting [PMID:28706255, "These data indicate that in the heart, Mg29 is localized to t-tubules, not the SR"].

## Calcium handling and muscle physiology

- Mg29-null skeletal muscle has reduced twitch force and less efficient excitation-contraction coupling, while maximal tetanic force is comparatively preserved. The structural and physiological defects are linked [PMID:10613905, "The morphological and functional abnormalities of the mutant muscle seem to be related to each other and indicate that MG29 is essential for both refinement of the membrane structures and effective excitation-contraction coupling in the skeletal muscle triad junction."]
- Targeted deletion causes severe dysfunction of store-operated calcium-channel function/SR calcium homeostasis and increased fatigue susceptibility [PMID:11988740, "Targeted deletion of mg29 alters the junctional membrane structure, causes severe dysfunction of SOC and SR calcium homeostasis and increases the susceptibility of muscle to fatigue stimulation."]
- Full-text mouse myotube experiments mapped TRPC3 binding to the MG29 N-terminus and first luminal loop. A deletion mutant lacking the full binding region disrupted endogenous MG29-TRPC3 association and reduced depolarization-induced calcium transients without changing RyR1 activity or releasable SR calcium [PMID:26141232, "The N-terminus and the I-II loop of MG29 constitute the binding region for TRPC3."; "myotubes expressing Δ116-MG29 showed a significantly reduced response to KCl compared with wild-type MG29 control"].
- These findings support calcium channel regulator activity (GO:0005246) and regulation of store-operated calcium entry (GO:2001256) as conservative proposed human annotations by orthology. They do not establish that SYPL2 itself is a calcium channel.

## Neural and disease-context observations

- In non-Alzheimer human brain, MG29 mRNA was reported in neurons but not quiescent astrocytes; in Alzheimer lesions it was induced in plaque-associated activated astrocytes. Human MG29-transfected cells showed ER localization and expression-dependent effects on calcium-dependent exocytosis [PMID:22290180, "In non-AD brains, MG29 mRNA has been detected in neurons, but not in quiescent astrocytes."; "Human MG29-transfected cells express the protein in the endoplasmic reticulum and the level of expression is involved in Ca2+-dependent exocytosis mechanisms."]
- This disease-context expression does not demonstrate localization to synaptic vesicles. It also does not outweigh the direct muscle-triad localization and knockout evidence.
- PMID:22926577 is an adult human substantia-nigra proteomics comparison across neurodegenerative diseases. The accessible abstract reports differential abundance of proteins in diseased adult tissue but no developmental experiment and does not name SYPL2 [PMID:22926577, "Using a quantitative proteomic approach, we investigated protein expressions in the substantia nigra of Alzheimer's disease, Huntington's disease, and Multiple sclerosis."] Therefore, even if the inaccessible full dataset confirms SYPL2 detection, it cannot by itself establish a role in substantia nigra development.

## Annotation decision rationale

- Local PAINT provenance confirms that GO:0030672 was placed at ancestral node PTN000033897 in the mixed PTHR10306 family. The local family table separates SYPL2/MG29 as SF8, SYPL1 as SF9, neuronal synaptophysin/SYP as SF10, and synaptoporin/SYNPR as SF16. Thus, the node-level propagation crosses named paralog subfamilies with distinct compartments [file:interpro/panther/PTHR10306/PTHR10306-paint.tsv; file:interpro/panther/PTHR10306/PTHR10306-entries.csv].
- **Synaptic vesicle membrane (IBA; GO:0030672): REMOVE.** This appears to be an over-propagated family localization from neuronal synaptophysin paralogs. Direct MG29 evidence places the mammalian ortholog at muscle T-tubule/SR junctions; no inspected source demonstrates synaptic-vesicle localization for SYPL2.
- **Synaptic vesicle (IEA; GO:0008021): REMOVE.** The InterPro2GO mapping from the broad synaptophysin/porin family is too coarse for the specialized SYPL2/MG29 subfamily and conflicts with direct subfamily localization evidence.
- **Membrane (IEA; GO:0016020): ACCEPT.** Four predicted transmembrane helices and experimental triad/ER membrane localization make this broad annotation correct, albeit much less informative than the proposed triad terms.
- **Substantia nigra development (HEP; GO:0021762): MARK_AS_OVER_ANNOTATED.** The cited adult-tissue proteomics paper can support expression/detection in substantia nigra but the accessible study design does not establish development or a causal developmental role. Because the cached paper is abstract-only, the review does not dispute that SYPL2 was detected in the full proteomic dataset.

## Remaining uncertainties

- What is the endogenous molecular activity of human SYPL2 at the triad: direct modulation of TRPC3/other channels, membrane curvature/oligomerization, or a combination?
- Are both human isoforms present in skeletal muscle, and does isoform 2 (which replaces part of the fourth transmembrane helix/C-terminal region) localize and function differently?
- Does neuronal SYPL2 occupy synaptic vesicles, ER, or another membrane compartment? The available human brain study establishes expression but not synaptic-vesicle localization.
- Are the cardiac and Alzheimer-associated expression patterns compensatory stress responses rather than normal core functions?
