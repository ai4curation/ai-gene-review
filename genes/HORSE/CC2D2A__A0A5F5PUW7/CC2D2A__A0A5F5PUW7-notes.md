# CC2D2A (horse, A0A5F5PUW7) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: new review of A0A5F5PUW7, the full-length, gene-centric UniProt model of horse CC2D2A
(Ensembl ENSECAG00000025115, VGNC:16103). The second horse model, A0A5F5PJ44 (folder `genes/HORSE/CC2D2A`),
is an identical 1480-residue sub-sequence of this one. ProtNLM2 output was not consulted.

### Data and deep research

- `just fetch-gene HORSE A0A5F5PUW7 --alias CC2D2A__A0A5F5PUW7` gave 8 GOA rows: 3 IBA from PTN000464650
  and 5 Ensembl Compara IEA from mouse Cc2d2a (Q8CFW7).
- `just deep-research-falcon ... --fallback perplexity-lite` FAILED. Falcon returned "Failed to authenticate",
  and the perplexity fallback returned HTTP 401 (insufficient quota). No deep-research file was written.
  This review relies instead on the cached primary literature on mammalian, worm and zebrafish CC2D2A.
- No horse-specific literature on CC2D2A was found (web search, 2026-10-20). Every functional statement
  is therefore an orthology inference.

### Evolutionary grounding (`CC2D2A__A0A5F5PUW7-bioinformatics/RESULTS.md`)

- PANTHER: PTHR20837:SF7, the same subfamily as human CC2D2A Q9P2K1 and mouse Cc2d2a Q8CFW7. CC2D2B is
  in SF2.
- PAINT: all three IBDs in the family (GO:0035869, GO:1904491, GO:1905515) are at PTN000464650 (Eukaryota),
  and the horse protein receives all three.
- Identity: 88.9% to human CC2D2A, 85.0% to mouse, 42.3% to human CC2D2B; full-length alignment.
- 25 of 26 human disease missense positions are conserved; human E1447 corresponds to horse D1470.

### Decisions

- All 3 IBA rows: ACCEPT. Horse is inside the clade, with no sign of divergence.
- The Compara IEA rows for transition zone, MKS complex, cilium assembly and TZ protein localization:
  ACCEPT. The donor is in the same subfamily, and the mouse data show that the protein does structural
  work (participation, not only necessity): it is a structural subunit of the MKS module, and it is on
  the subdistal appendages that it builds [PMID:24947469 "We therefore conclude that CC2D2A is needed
  for the assembly of SDA at mother centriole, for stable MT anchoring and docking of transport vesicles,
  and for further elaboration of the transition zone."].
- MKS complex was not propagated by PAINT. That fits the evidence for complex membership, which is mammalian
  biochemistry (PMID:21725307, PMID:22179047), and it is still sound for a mammal-to-mammal SF7 transfer.
- smoothened signaling pathway (IEA): KEEP_AS_NON_CORE. CC2D2A acts by gating ciliary entry of Smo
  [PMID:21725307 "Smo displayed reduced ciliary localization in Tctn1−/− and Tctn2−/− MEFs treated with
  the Hh pathway agonist SAG, an effect that was even stronger in Cc2d2a−/− MEFs"]. The same action is
  used on the human ortholog.
- NEW (ISS): ciliary basal body (GO:0036064) and centriolar subdistal appendage (GO:0120103), from mouse
  immunogold and human RPE1 localization. GO:0120103 is not accepted in the core_functions `locations`
  enum, so the core function uses the basal body. The subdistal appendage remains as a NEW existing-annotation
  row.
- Organismal phenotypes (neural-tube patterning, photoreceptor outer-segment defects, laterality) were
  not annotated as processes.
- No molecular-function term: the TGL fold is predicted inactive in the CC2D2A clade (PMID:22983010),
  and no specific binding activity has been established that would justify a term beyond protein binding.
