# RAB13 notes

Manual literature review for GO-CAM `65692e7e00001822`, activity
`657ba49f00000114`.

Provider deep research could not run in this worktree because the retained
runtime had no configured OpenAI, Edison, Asta, or Perplexity API key. This file
records the manual replacement synthesis from the cached primary papers and the
GO-CAM context.

## Core Rab switch and membrane traffic

RAB13 is a Rab-family small GTPase. Its nucleotide cycle and Rab GEF
compatibility are consistent with its existing generic GTPase, GTP-binding, and
small-G-protein terms; DENND1-family GEFs were assayed for RAB13 activation in a
family screen of DENN-domain Rab GEFs [PMID:20937701].

In polarized epithelial cells, RAB13 regulates transport between the
trans-Golgi network and recycling endosomes, with biosynthetic traffic to the
plasma membrane passing through a transferrin-receptor-positive recycling
endosome intermediate [PMID:18779367]. Separate occludin-recycling work showed
that RAB13 mediates continuous endocytic recycling of occludin back to the cell
surface, supporting both the GO endocytic-recycling process and the tight
junction role [PMID:15528189].

The early localization paper found RAB13 in cytoplasmic vesicles in
non-polarized cells and concentrated with ZO-1 at tight junctions in polarized
epithelial cells [PMID:8294494]. The functional tight-junction assembly paper
showed that a GTP-locked RAB13 mutant accelerated transepithelial-resistance
recovery, whereas a GDP-locked mutant impaired assembly [PMID:12058051].

## Junction and effector signaling

Activated RAB13 directly binds the PKA catalytic subunit and inhibits PKA
activity, providing direct support for the cAMP-dependent protein kinase
inhibitor activity and for negative regulation of cAMP/PKA signaling during
tight-junction assembly [PMID:15096524].

RAB13 also binds JRAB/MICAL-L2, an effector needed for occludin recycling and
tight-junction formation [PMID:16525024]. Additional junctional work placed
actinin-4 upstream of the JRAB/MICAL-L2 recruitment required for functional
tight-junction formation [PMID:18332111].

Several RAB13-associated trafficking contexts appear secondary to the core
TGN/recycling-endosome/tight-junction axis. RAB13 and JRAB/MICAL-L2 regulate
neurite outgrowth in PC12 cells [PMID:20008558]. MICAL-L1 work implicates
RAB13-family recycling traffic in EGFR endocytosis [PMID:21795389], and a
separate interaction study linked RAB13 to endospanin proteins [PMID:23772379].

## RNF115/TLR GO-CAM context

In the RNF115/TLR transport model, the RAB13 activity has `GO:0003924` GTPase
activity, `GO:0006893` Golgi to plasma membrane transport, and `GO:0005794`
Golgi apparatus. The GTPase and post-Golgi trafficking roles agree with the
gene-level review. `GO:0005794` is a coarse but acceptable GO-CAM location for
the Golgi/TGN transport step: the gene review accepts the more specific
trans-Golgi network row and removes only the historical NOT Golgi row that was
superseded by later positive TGN localization.

The remaining GO-CAM issues are model evidence and edge semantics, not the RAB13
annotation itself. RAB13 is relevant to TLR trafficking in PMID:35343654, whereas
the GO-CAM's RAB13-to-TLR4 edge still cites the 1993 localization paper
PMID:8294494. The causal relation from RAB13 to TLR4 also represents RAB13
post-Golgi carrier trafficking rather than direct biochemical regulation of
TLR4, matching the `DIRECT_VS_INDIRECT_CAUSAL` flag already present in the
GO-CAM review.
