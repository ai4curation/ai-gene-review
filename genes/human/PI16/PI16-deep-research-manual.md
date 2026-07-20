# Manual literature synthesis for human PI16 (Q6UXB8)

## Scope and provenance

This report was prepared manually from the project-cached UniProt record, GOA rows, PAINT trace, and primary publications after the configured automated providers failed on 2026-07-18 (Falcon/Edison HTTP 402; Perplexity-lite HTTP 401 insufficient quota). It is intentionally named `deep-research-manual` rather than after a provider.

## Molecular identity and localization

PI16 is a CAP-superfamily glycoprotein with an N-terminal secretory signal and a C-terminal hydrophobic sequence compatible with GPI-anchor processing. Human PI16 was originally purified as a glycosylated PSP94/MSMB-binding protein from serum, with expression detected in prostate, testis, ovary, intestine, peripheral leukocytes, pituitary, and Leydig cells. The direct serum purification establishes a soluble extracellular pool [PMID:15344909].

Human skin-homing CD8 T cells display PI16 on the plasma membrane through a GPI anchor; the protein is lost after restimulation through transcriptional down-regulation rather than demonstrated enzymatic shedding [PMID:30365157]. Mouse cardiac fibroblasts similarly expose Pi16 to the interstitium through a GPI anchor [PMID:27539859]. PI16 peptides and glycosylation sites have also been detected in human urine [PMID:22171320]. Thus, extracellular-region and cell-surface/plasma-membrane localizations are both supported and should not be treated as mutually exclusive.

## Direct molecular activities

The strongest direct human biochemical evidence identifies PI16 as an extracellular endopeptidase inhibitor with at least two target classes:

1. In primary human coronary artery endothelial cells, laminar shear strongly induces PI16, while inflammatory cytokines reduce it. Recombinant PI16 inhibits recombinant MMP2 with an approximate 10 nM IC50 and binds a loop adjacent to the MMP2 active site. PI16 overexpression lowers secreted MMP activity and reduces endothelial-cell migration [PMID:27996045]. This supports GO:0008191 metalloendopeptidase inhibitor activity and GO:0010596 negative regulation of endothelial cell migration.
2. In human skin-homing CD8 T cells, inhibitor screening and pull-down experiments show that PI16 inhibits cathepsin K and may not bind other tested skin proteases [PMID:30365157]. Mouse cardiac experiments independently show recombinant Pi16 inhibits cathepsin K and reduces conversion of pro-chemerin to active chemerin [PMID:27539859]. This supports GO:0004869 cysteine-type endopeptidase inhibitor activity, with target specificity presently bounded to cathepsin K.

The two activities are more informative than the generic GO:0030414 peptidase inhibitor activity and provide the best-supported core molecular functions.

## Biological roles and context

PI16 overexpression inhibits human coronary endothelial migration in vitro, consistent with reduced extracellular MMP activity [PMID:27996045]. In mouse myocardium, Pi16 suppresses cathepsin-K-dependent chemerin activation and limits cardiomyocyte growth [PMID:27539859; PMID:17909105]. Mouse loss-of-function also reduces nerve-injury-induced endothelial permeability, leukocyte influx, and neuropathic pain, placing fibroblast-derived Pi16 upstream of endothelial-barrier opening in that disease model [PMID:32079726]. These context-specific phenotypes are useful biological boundaries but do not by themselves establish additional human catalytic activities.

## PAINT inference assessment

The cached PANTHER trace places GO:0060090 molecular adaptor activity at the broad PTHR10334 node PTN000036124 from only MGI:MGI:1916536, mouse `Glipr1l1`. `Glipr1l1` functions in sperm adhesion/fusion, whereas PI16 is a long, glycosylated protease inhibitor expressed in fibroblasts, endothelium, T cells, serum, and urine. Because the inference crosses divergent CAP-family subfamilies and no PI16 study demonstrates adaptor activity, the IBA is an over-propagated family inference and should be removed. Direct MMP2 and cathepsin K inhibitor annotations replace it.

## Evidence boundaries and open questions

- It is not known which PI16 isoforms or processing events determine stable GPI anchoring versus release into extracellular fluids.
- The inhibitor specificity panel is incomplete. Direct evidence supports MMP2 and cathepsin K, not all metalloproteinases or cysteine peptidases.
- The structural mechanism by which the CAP domain recognizes and inhibits two mechanistically distinct protease classes is unresolved.
- Whether the mouse cardiac, chemerin-processing, and neuropathic-pain mechanisms operate similarly in humans remains to be tested.
- The physiological significance of PSP94/MSMB binding and of high-throughput interaction candidates, including TNFRSF21, is not established.
