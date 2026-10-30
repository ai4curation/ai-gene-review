# Arl1 (DROME) review notes

## Session log

- Fetched with `just fetch-gene DROME Arl1`; UniProt P25160 (Swiss-Prot, ARL1_DROME), FlyBase
  FBgn0000115, GeneID 39745. GOA: 25 rows. Accession matches the requested one.
- Publications cached: the six GOA PMIDs plus PMID:26116655 (Arl1/Garz/Arfaptin, full text).
  PMID:1901655, 21693198 and 10798391 are abstract-only.
- No deep-research provider available; literature summary is in `Arl1-deep-research-manual.md`.

## Synthesis

Arl1 is a Golgi/TGN Arf-family GTPase. Its GTP-bound form recruits peripheral proteins to the
trans-Golgi: the GRIP-domain golgins [PMID:19001129, PMID:24610947], the BIG1/2 ortholog Sec71
[PMID:22291037] and Arfaptin [PMID:26116655]. Through Sec71 it promotes Arf1 activation and AP-1
recruitment at the TGN, which the salivary gland needs for secretory granule biogenesis
[PMID:24610947 "Taken together, these results are consistent with the model that AP-1 is recruited
to the TGN and immature secretory granules by Sec71-dependent activation of Arf1 downstream of Arl1."].

## Decisions worth flagging

- Bare protein binding (Sec71, PMID:22291037) was removed under the protein-binding policy; the
  biology is captured by the protein localization to Golgi membrane rows and by the core function.
- TAS rows from PMID:10798391 (neurotransmitter secretion, synaptic vesicle endocytosis) and the
  derived IEA presynapse row: marked over-annotated. That paper is a homolog listing; Arl1's neuronal
  role (PMID:26116655) is at the somatic Golgi, not the presynapse.
- ER membrane (IGI, PMID:21693198, abstract only): ER localization is reported in the ninaE(D1)
  retinopathy model; kept as non-core.
- Negative regulation of ER to Golgi vesicle-mediated transport (IMP, PMID:21693198): kept as
  non-core; the phenotype (accelerated secretion, Golgi overgrowth) may be indirect, and full text
  was not available.
- No NEW rows proposed. The Arfaptin and synapse-growth data (PMID:26116655) were not added as
  annotations; synapse growth is a mutant phenotype downstream of Golgi function.
