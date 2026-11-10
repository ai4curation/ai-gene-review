# TERF2 (TRF2, Q15554) review notes

## Literature search (no deep-research provider available)

Sources checked, 2026-11-04:

- UniProt Q15554 record (`TERF2-uniprot.txt`): function, subunit, domain and PTM text.
- All 62 GOA-cited publications cached via `just fetch-gene-pmids human TERF2`. Full text is
  available for 21852327, 23685356, 24012755, 24095731, 22536324, 31595153, 20479256,
  25620558, 15314656, 25399868, 30629181, 22157895, 28216226 and the HTP interactome papers;
  the rest are abstract-only.
- Web search "TRF2-S short isoform neurons axonal mRNA transport" for the ortholog-derived
  axon/axonal mRNP transport IEA rows; found and cached PMID:26586091 (rat TRF2-S).
- Context: telomere end-joining pathway choice (NBS1 phospho-switch, TRF2 TRFH docking)
  (module and GO-CAM review proposed in ai4curation/ai-gene-review#5904; not on this branch and not used as evidence). The cached source model `gocams/65a1f4f800002884/65a1f4f800002884-src.yaml` was read.

## Key findings

- Duplex TTAGGG binding via C-terminal Myb/homeodomain, as a TRFH-domain homodimer
  [PMID:9326950 "bound specifically to duplex TTAGGG repeats in vitro and localized to all human telomeres in metaphase chromosomes"].
- End protection: dominant-negative TRF2 causes end-to-end fusions
  [PMID:9476899 "Here, we show that the human telomeric protein TRF2 plays a key role in the protective activity of telomeres."].
- NHEJ repression requires TRF2, and ERCC1/XPF removes the overhang in its absence
  [PMID:14690602 "establish that TRF2  prevents NHEJ at telomeres through protection of the telomeric overhang from  ERCC1/XPF"].
- T-loop formation [PMID:10338214 "Electron microscopy reported here demonstrated that TRF2 can remodel linear telomeric DNA into large duplex loops (t loops) in vitro."].
- Basic domain represses HR-mediated t-loop excision [PMID:15507207 "TRF2DeltaB-induced deletions depended on XRCC3, a protein implicated in Holliday junction resolution, and created t-loop-sized telomeric circles."].
- TRFH docking hub: YxLxP/[Y/F]xL motifs of Apollo, NBS1, SLX4, PNUTS, MCPH1
  [PMID:19287395 "Our findings indicate that an array of TRF2 molecules functions as a protein hub and regulates telomeres by recruiting different signaling molecules via a linear sequence code."];
  RTEL1 recruitment in S phase [PMID:25620558 "Here, we establish that the shelterin protein TRF2 recruits RTEL1 to telomeres in S phase"].
- ATM/MRN repression and NBS1 docking [PMID:28216226 "Telomeres employ TRF2 to protect chromosome ends from activating the DNA damage sensor MRE11-RAD50-NBS1 (MRN), thereby repressing ATM-dependent DNA damage checkpoint responses."].
- Length regulation is telomerase-independent in the targeting assay [PMID:11971978 "In contrast, TRF2 targeting and telomerase inhibition have additive effects."].
- Telomerase co-IP in the HOT1 paper is attributed to TPP1 [PMID:23685356 "Antibodies against TRF1 and TRF2 immunoprecitated telomerase activity, putatively dependent on the previously established link between the shelterin component TPP1 and telomerase"] -> contributes_to telomerase activity removed.
- Neuronal TRF2-S (rat) lacks the DNA-binding domain and transports axonal mRNAs [PMID:26586091]; not shown for human, so axon / axonal mRNP transport IEA rows marked over-annotated.

## Curation decisions to remember

- GO:0140463 chromatin-protein adaptor activity chosen as the docking-hub MF (TRF2 on telomeric
  chromatin recruits Apollo, RAP1, SLX4, RTEL1). PMID:19287395 calls TRF2 a protein hub, and PMID:28216226
  shows NBS1, Apollo and PNUTS competing for the same TRFH surface, so the adaptor role is placed on TRF2;
  gomodel:65a1f4f800002884 instead draws NBN adaptor activity with has_input TERF2 (see suggested_questions).
- Positive regulation of telomere maintenance and negative regulation via telomerase marked over-annotated.
