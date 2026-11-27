# SLC31A1 manual notes

## GO-CAM 69ea894900001492

- GO-CAM activity `69ea894900002175` models SLC31A1/CTR1 as the plasma-membrane Cu(I) importer that supplies cytosolic copper for the ATOX1/ATP7A/SOD3 axis. This is the conserved core function retained in the gene review: hCTR1 is a homotrimeric high-affinity copper uptake protein with a central pore, experimentally measured Cu uptake, and copper-responsive internalization/recycling.
- The GO-CAM term `GO:0005375` is a correct molecular-function parent for SLC31A1. GOA also contains the matching process `GO:0015677` copper ion import and the more contextual `GO:0015679` plasma membrane copper ion transport.
- The model does not include SLC31A1's peripheral, VEGF-induced redox adaptor role in endothelial CTR1-VEGFR2 co-internalization. That angiogenesis branch is real but tissue-contextual and is not part of the SOD3 copper-loading GO-CAM.

## Manual literature synthesis

- Human CTR1/SLC31A1 is a plasma-membrane, multi-pass high-affinity copper uptake protein. It transports copper in a saturable and energy-independent manner at the plasma membrane [PMID:11734551], and mutational work on full-length human CTR1 established pore and C-terminal residues that regulate Cu entry [PMID:16135512; PMID:23658018].
- The active transporter is a trimeric membrane protein; electron crystallography and projection structures place the permeation pathway at the trimer axis [PMID:16501047; PMID:19240214].
- CTR1 surface levels are dynamically regulated by copper. Elevated extracellular copper triggers CTR1 internalization into Rab5/EEA1-positive early endosomes and Rab11-positive recycling compartments, and copper removal returns CTR1 to the plasma membrane [PMID:26945057].
- SLC31A1's cytosolic C terminus participates in Cu(I) handoff to ATOX1 and CCS/SOD1 pathway proteins [PMID:26745413; PMID:31292775]. These interactions are copper-dependent handoff surfaces, not stand-alone generic binding functions.
- CTR1 can mediate silver and platinum-drug accumulation in assays [PMID:20451502; PMID:20569931], but those are pharmacologic or nonphysiologic metal fluxes rather than the evolved copper-import role.
- VEGF stimulation of endothelial cells oxidizes CTR1 Cys189, promotes a CTR1-VEGFR2 disulfide complex, and co-internalizes the complex to early endosomes for sustained VEGFR2 signaling. That supports angiogenesis and VEGFR2-signaling rows as peripheral signaling roles [PMID:35027734].

## Deep research

`just deep-research-falcon human SLC31A1 --fallback perplexity-lite` was attempted on 2026-11-25. The local `deep-research-client` install only exposed the `claude_code` provider, and both Falcon and Perplexity-Lite failed provider availability checks, so no provider-authored `SLC31A1-deep-research-*.md` file was written. This notes file records the manual synthesis used instead.
