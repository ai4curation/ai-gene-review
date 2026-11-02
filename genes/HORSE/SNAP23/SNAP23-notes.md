# SNAP23 (horse, Equus caballus) — A0A3Q2HTF1

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: HORSE partner of the DONKEY40 cohort (donkey SNAP23 A0A8C4M285 is reviewed
separately). No previous review existed; folder created with
`just fetch-gene HORSE A0A3Q2HTF1 --alias SNAP23`; stub id confirmed as A0A3Q2HTF1.
ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon HORSE SNAP23 --fallback perplexity-lite` failed: falcon
returned "Edison API request failed: Failed to authenticate" and the perplexity-lite
fallback returned HTTP 403 Forbidden. No deep-research file exists; the review uses
the cached literature on human/mouse SNAP23 listed below.

### Identity

- A0A3Q2HTF1 is a TrEMBL entry (PE 3), 211 aa, Ensembl ENSECAP00000038505.2, VGNC:23373 SNAP23.
- Same length as human SNAP-23a (O00161-1, 211 aa); global alignment 87.2% identical
  with no gaps; 89.5% to mouse O09044 (file:HORSE/SNAP23/SNAP23-bioinformatics/RESULTS.md).
- Both t-SNARE coiled-coil motifs (horse 14..76 and 146..208) and the palmitoylated
  cysteine linker (C79, C80, C83, C85, C87) are present. Human C112 aligns to horse S112.
- C-terminal four residues differ (horse ...LLPQ vs human/mouse ...LIDS), after the
  end of the second SNARE motif. Possibly the gene model for the last exon; noted but
  not a functional concern. Not a fragment and not an isoform: treat as the canonical
  horse SNAP23 product.
- PANTHER PTHR19305:SF4 (SYNAPTOSOMAL-ASSOCIATED PROTEIN 23), same subfamily as human
  O00161. No PANTHER family review exists under interpro/panther/PTHR19305 (only the
  InterPro metadata and entries files), so there is no placement disagreement to report.

### Literature (human/mouse SNAP23, same subfamily)

- [PMID:8663154 "we have identified a 23-kDa protein from human B lymphocytes (termed SNAP-23) that binds tightly to multiple syntaxins and synaptobrevins/VAMPs in vitro"; "Unlike SNAP-25, SNAP-23 was expressed in all tissues examined."]
- [PMID:10036234 "syntaxin 11 binds to the SNARE proteins VAMP and SNAP-23 in vitro and also exists in a complex with SNAP-23 in transfected HeLa cells and in native human B lymphocytes"]
- [PMID:12556468 "SNAP-23N can assemble spontaneously with the coiled-coil domains from SNAP-23C, syntaxin-4, and VAMP-3 to form a heterotetrameric complex."]
- [PMID:30811271] SNAP23 cooperates with STX11 for TLR4 transport to the plasma membrane in macrophages (UniProt O00161 FUNCTION, ECO:0000269).
- Synaptic role: in Snap25-null chromaffin cells, [PMID:12859899 "SNAP-23 did not support a standing pool of primed vesicles"]; in Snap25-null neurons, [PMID:17728451 "SNAP-23 supported asynchronous release only, reminiscent of synaptotagmin-1 null neurons."] These are overexpression rescues; the endogenous synaptic vesicle t-SNARE is the paralog SNAP25.
- [PMID:23395379 "KDs of SNAP-25 and SNAP-47, but not SNAP-23, impaired LTP."]

### Annotation decisions (summary)

- helical-bundle zippering fusogenic activity (IBA, IEA), SNARE complex (IBA, IEA),
  syntaxin binding (IBA), plasma membrane (IBA, IEA), exocytosis (IBA, IEA): ACCEPT.
  These come from PTN000447753/PTN000447752, nodes whose donors include human SNAP23
  (O00161) itself, and the horse protein retains every relevant feature.
- synaptic vesicle priming and synaptic vesicle fusion to presynaptic active zone membrane
  (IBA, PTN000447754, single donor Drosophila Snap25 FBgn0011288) and the derived
  presynapse (IEA GO_REF:0000108): MARK_AS_OVER_ANNOTATED. The node is placed above the
  vertebrate SNAP25/SNAP23 duplication, but SNAP23 is the ubiquitous paralog and does
  not support a primed vesicle pool when tested in place of SNAP25; the synaptic
  vesicle function was retained by SNAP25 (SF5), so this is target-lineage divergence
  after duplication rather than an inherited function.

### Relative

Closest characterised relative by PANTHER subfamily (SF4): human SNAP23 O00161. No
review exists in the repo (no genes/human/SNAP23, no mouse Snap23). needs_review=true.

### Modules

modules/synaptic_vesicle_exocytosis.yaml and modules/synaptic_vesicle_cycle.yaml
mention the SNAP-25 (SNAP25/SNAP23) family as a family descriptor; SNAP23 is not the
synaptic vesicle t-SNARE, so these are family-level context only.

### Housekeeping

While caching references I also fetched PMID:20685959 and PMID:9032285 by mistake
(unrelated papers: PKR/IRS in HepG2 cells; Bombyx SGFB). They are not cited here.
