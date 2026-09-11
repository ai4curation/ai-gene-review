# Pnkd (B4F7D2): evidence and exact-input prediction review

The emitted HAGH reaction is an over-specific transfer across a functionally divergent family. PNKD-L shows very weak lactoylglutathione hydrolysis in vitro and fails to replace HAGH in vivo. B4F7D2 also differs from the longer PNKD product, so neither a standard glyoxalase II role nor the localization and synaptic function of a particular long isoform can be assumed.

## Input identity and functional boundary

B4F7D2 and the 424-residue rat D3ZXB0 record share RGD:2300155. Their first 79 residues are identical, but B4F7D2 lacks the next 39 reference residues and has a divergent C-terminal portion. The entire annotated metallo-beta-lactamase domain is conserved (163/163 identical residues). This establishes PNKD identity without equating the product to the experimentally studied PNKD-L or PNKD-M constructs. The model donor O35952 is rat Hagh, a different gene.

## Biological evidence

- [PMID:21487022 — Mutations in PNKD causing paroxysmal dyskinesia alters protein cleavage and stability.](https://pubmed.ncbi.nlm.nih.gov/21487022/): Human PNKD-L has weak measurable S-D-lactoylglutathione hydrolysis in vitro, rather than the robust HAGH activity; no complete absence of hydrolysis is claimed.

> PNKD-L has extremely low but consistent SLG hydrolysis activity


> introduction of a human PNKD-L transgene into the same null background shows no rescue of SLG metabolism


> the results suggest that PNKD-L is a membrane-associated protein.

## Exact non-GO claims

The complete emitted record is preserved in [Pnkd-protnlm-source.json](Pnkd-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Metallo-beta-lactamase domain-containing protein

CNN (CS 2). The name describes a verified domain present in B4F7D2; it does not itself claim beta-lactam antibiotic hydrolysis or glyoxalase-II substrate specificity. The full mapped domain is retained. [Sequence comparison](Pnkd-bioinformatics/RESULTS.md).

### Function

> Thiolesterase that catalyzes the hydrolysis of S-D-lactoyl-glutathione to form glutathione and D-lactic acid

PLI (CS 0; PARALOG_OVERANNOTATION) as a physiological enzyme-function assignment copied from Hagh/O35952. The direct comparison shows weak PNKD-L activity in vitro and failure to replace HAGH, so the HAGH reaction is not an established biological function of PNKD. This assessment does not mean that the bond can never be hydrolyzed by PNKD, and biochemical activity of B4F7D2 itself remains unmeasured. [PMID:21487022](https://pubmed.ncbi.nlm.nih.gov/21487022/).

### Location

> Mitochondrion matrix

UNC (CS 1). A HAGH mitochondrial localization cannot establish PNKD localization. Conversely, membrane localization of a particular human PNKD-L construct cannot categorically refute mitochondrial localization of every rat product. B4F7D2 retains the common N-terminus but has internal and terminal differences; no assay resolves its localization. The paper explicitly discusses conflicting mitochondrial localization results and isoform-specific evidence. [PMID:21487022](https://pubmed.ncbi.nlm.nih.gov/21487022/).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

The PNKD/HAGH relationship supports fold ancestry but not a shared physiological substrate. The failed HAGH complementation is a direct functional boundary. The selected protein retains the annotated beta-lactamase domain, so it is not classified as a catalytically dead fragment simply from its shorter length. No ancestral gain/loss node or stable pseudoenzyme status is asserted.

## Evidence limits

The cached 2011 paper contains full text, including the low-activity and complementation results and the conflicting localization literature. Its experiments concern defined PNKD-L constructs, not B4F7D2. A biochemical substrate or synaptic core function is therefore not assigned to this exact product. The genuine Falcon report supplies source leads; its gene-level neuronal synthesis is subject to the product and isoform boundary above.

Exact sequence mapping: [Pnkd-bioinformatics/RESULTS.md](Pnkd-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Neuronal evidence and product scope

[PMID:25730884](https://pubmed.ncbi.nlm.nih.gov/25730884/), DOI [10.1073/pnas.1501364112](https://doi.org/10.1073/pnas.1501364112), reports PNKD-RIM1/2 interactions and altered release in neuronal experiments and knockout mice. It supports the gene-level neuronal context, but no experiment in the paper is identified as testing the 369-residue B4F7D2 product. The conserved beta-lactamase domain alone does not establish its synaptic localization or RIM regulation.
