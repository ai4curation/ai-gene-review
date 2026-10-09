# ICE1 / SCRM (At3g26744, Q9LSE2) curation notes

Session 2026-10-06 (stomatal_lineage_development module). The initial `just fetch-gene ARATH ICE1` retrieved an unreviewed TrEMBL entry (A0A1I9LRH4, an alternative gene model); folder was deleted and refetched by accession (`Q9LSE2 --alias ICE1`). UniProt primary name is SCRM; gene_symbol set to ICE1 (TAIR symbol, folder name). Falcon deep research failed (HTTP 402).

## Key findings
- SCRM = ICE1; SCRM/SCRM2 heterodimerize with SPCH, MUTE, FAMA; scrm scrm2 successively phenocopies fama, mute, spch; scrm-D (R236H) gives stomata-only epidermis [PMID:18641265].
- SCRM scaffolds MPK3/6 to SPCH through a bipartite MAPK-docking + KRAAM (KiDoK) motif; scrm-D abolishes MPK3/6 binding [PMID:31235876].
- Cold: ICE1 binds MYC sites in CBF3 promoter and is a transcriptional activator, constitutively expressed [PMID:12672693]; HOS1 ubiquitinates [PMID:16702557]; SIZ1 sumoylates (K393) [PMID:17416732].
- DISPUTE: ice1-1 DREB1A/CBF3 repression is transgene-induced silencing; ICE1 OE or ice1 scrm2 loss did not alter DREB1A [PMID:32034036 "We showed that DREB1A repression in ice1-1 results from transgene-induced silencing and not genetic regulation by ICE1."]; rebuttal with ICE1 ChIP-seq at CBF/COR promoters [PMID:32068336].
- Seeds: ICE1 with ZOU controls endosperm and dormancy; represses ABI3 [PMID:30570804]; antagonizes ABI5/DELLA in germination [PMID:31123050].

## Curation decisions
- Core MFs: protein heterodimerization activity (NEW; SPCH protein binding MODIFIED), DNA-binding TF activity (accepted), protein-macromolecule adaptor activity (NEW, IDA PMID:31235876). Core BP: stomatal lineage progression.
- Cold-related: response to cold IEP MARK_AS_OVER_ANNOTATED (gene constitutively expressed; role disputed); response to freezing KEEP_AS_NON_CORE with dispute noted.
- Generic protein binding rows (HOS1 x2, MYB15, MYC67/70, ABI5/DELLAs, LFR) REMOVED.
- No GO-CAM models contain ICE1.
