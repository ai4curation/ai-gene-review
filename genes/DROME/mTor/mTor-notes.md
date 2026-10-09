# mTor (Tor, CG5092, Q9VK45) curation notes

Deep research: `mTor-deep-research-falcon.md` (falcon; the wrapper reported a 600 s timeout but the run
completed later and wrote the file).

## Literature journal

- TOR is the catalytic subunit of TORC1 and TORC2; Lst8 acts only in TORC2 in flies
  [PMID:22493059 "Here, we demonstrate that Drosophila LST8, the  only conserved TOR-binding protein present in both TORC1 and TORC2, functions  exclusively in TORC2 and is not required for TORC1 activity."]
- TORC2 (rictor-TOR) phosphorylates Akt hydrophobic motif in fly and human cells
  [PMID:15718470 "We show that in Drosophila and human cells the target of rapamycin (TOR) kinase and its associated protein rictor are necessary for Ser473 phosphorylation"]
- TOR suppresses starvation-induced autophagy in fat body
  [PMID:15296714 "signaling through TOR and its upstream regulators PI3K and Rheb is necessary and sufficient to suppress starvation-induced autophagy in the Drosophila fat body"]
- Rheb-TOR promote ribosome biogenesis, protein synthesis and cell size
  [PMID:17371599 "both gene products are important regulators of ribosome biogenesis, protein synthesis, and cell size"]
- TOR multimerizes
  [PMID:16219781 "We present biochemical evidence that TOR self-associates in vivo"]
- Lifespan extension by dominant-negative dTOR
  [PMID:15186745 "We find that overexpression of dTsc1, dTsc2, or dominant-negative forms of dTOR or dS6K all cause lifespan extension."]
- TORC2 and dendritic tiling via Trc
  [PMID:19875983 "We here report that Sin1, Rictor, and target of rapamycin (TOR), components of  the TOR complex 2 (TORC2), are required for dendritic tiling of class IV da  neurons."]
- Deep research: TORC2 readout Akt Ser505 [file:DROME/mTor/mTor-deep-research-falcon.md "Loss of fly Rictor reduced Ser505 phosphorylation by"]

## Curation decisions

- Core: protein Ser/Thr kinase activity in TORC1 (TORC1 signaling, positive regulation of cell size,
  negative regulation of macroautophagy) and TORC2 (TORC2 signaling, positive regulation of PI3K/PKB).
- Sign check: TOR negatively regulates macroautophagy; macroautophagy IMP row MODIFY to the negative
  regulation term (TOR is not autophagy machinery). Consistent with Lkb1/AMPKalpha/Mo25/Stlk reviews,
  in which those kinases negatively regulate TORC1 signaling.
- Generic kinase/regulation terms MODIFY to specific terms carried.
- chromatin DNA binding (from ChIP) over-annotated; broad ARBA regulatory terms over-annotated;
  drug-response row over-annotated; two rows UNDECIDED (17183368 PI3K/PKB sign; axon guidance sign
  from Rheb gain-of-function).
- protein binding (Lst8) REMOVE; complex membership captures it.
